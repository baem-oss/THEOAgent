"""
title: THEOAgent SourceGuard Web – DEV PoC
author: THEOAgent
version: 0.2.0
description: Controlled retrieval of public HTTPS source text. Not a SourceGuard Pipe.
"""

import hashlib
import http.client
import ipaddress
import json
import re
import socket
import ssl
from html.parser import HTMLParser
from typing import Optional
from urllib.parse import urljoin, urlsplit, urlunsplit

from pydantic import BaseModel, Field


VERSION = "0.2.0"
DEFAULT_HOSTS = (
    "www.vatican.va,vatican.va,www.dbk.de,dbk.de,"
    "www.drs.de,drs.de,amtsblatt.drs.de,"
    "rechtssammlung.drs.de,recht.drs.de,"
    "www.die-bibel.de,die-bibel.de"
)


class RetrievalError(Exception):
    pass


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1
        if not self.skip and tag in (
            "p", "div", "article", "section", "h1", "h2", "h3",
            "h4", "h5", "h6", "li", "br", "tr"
        ):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1
        if not self.skip and tag in ("p", "div", "article", "section", "li", "tr"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data)


def _parse_url(url, allowed_hosts):
    if not isinstance(url, str) or len(url) > 2048 or any(ord(c) <= 32 for c in url):
        raise RetrievalError("Unzulässiges URL-Format")
    try:
        u = urlsplit(url)
        host = (u.hostname or "").lower().rstrip(".")
        if (
            u.scheme.lower() != "https" or not host
            or u.username is not None or u.password is not None
            or u.port not in (None, 443)
            or host not in allowed_hosts
        ):
            raise RetrievalError("Nur freigegebene öffentliche HTTPS-Hosts sind zulässig")
        if u.fragment:
            url = urlunsplit((u.scheme, u.netloc, u.path, u.query, ""))
        return host, url
    except ValueError as exc:
        raise RetrievalError("Ungültige URL") from exc


def _public_ip(host):
    try:
        found = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
        addresses = list(dict.fromkeys(item[4][0] for item in found))
        if not addresses or not all(ipaddress.ip_address(ip).is_global for ip in addresses):
            raise RetrievalError("Nichtöffentliche oder ungültige DNS-Ziele abgewiesen")
        return addresses[0]
    except (socket.gaierror, ValueError) as exc:
        raise RetrievalError("Host konnte nicht sicher aufgelöst werden") from exc


class PinnedHTTPSConnection(http.client.HTTPSConnection):
    """TCP connects to the DNS-validated IP; TLS verifies the requested hostname."""

    def __init__(self, hostname, pinned_ip, timeout):
        super().__init__(
            hostname, port=443, timeout=timeout,
            context=ssl.create_default_context()
        )
        self.pinned_ip = pinned_ip

    def connect(self):
        sock = socket.create_connection((self.pinned_ip, 443), self.timeout)
        try:
            self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
        except Exception:
            sock.close()
            raise


def _decode_document(content, content_type):
    """Decode HTML by BOM, HTTP charset, then HTML meta; reject unrecoverable text."""
    header = re.search(r'charset\s*=\s*["\']?([a-z0-9_-]+)', content_type.lower())
    meta = re.search(
        rb'<meta[^>]+charset\s*=\s*["\']?([a-z0-9_-]+)',
        content[:8192], flags=re.IGNORECASE,
    )
    meta_charset = meta.group(1).decode("ascii").lower() if meta else None
    http_charset = header.group(1).lower() if header else None
    candidates = []
    if content.startswith(b"\xef\xbb\xbf"):
        candidates.append("utf-8-sig")
    # Explicit declarations are tested without replacement, so a wrong
    # declaration cannot silently destroy accents.
    candidates.extend([http_charset, meta_charset, "utf-8", "windows-1252", "iso-8859-1"])
    allowed = {"utf-8", "utf-8-sig", "windows-1252", "iso-8859-1", "us-ascii", "latin1"}
    for charset in dict.fromkeys(x for x in candidates if x in allowed):
        try:
            result = content.decode(charset, errors="strict")
        except (UnicodeError, LookupError):
            continue
        if "\ufffd" not in result:
            return result
    raise RetrievalError("Zeichenkodierung nicht sicher lesbar")


def _kkk_2267_classification(section_text):
    """Recognize two substantive phrasings, never infer an edition year."""
    clean = " ".join(section_text.lower().split())
    new = "todesstrafe unzulässig" in clean or (
        "todesstrafe" in clean and "unantastbarkeit und würde" in clean
        and "abschaffung" in clean
    )
    old = (
        "soweit unblutige mittel" in clean
        or "einzig gangbare weg" in clean
        or "nur dann gerechtfertigt" in clean
    )
    if new and not old:
        return "POST_2018_WORDING"
    if old and not new:
        return "PRE_2018_WORDING"
    return "UNCLASSIFIED"


def _kkk_2267_paragraph(text):
    # Ignore incidental mentions of 2267 in surrounding headings by requiring
    # the numeral to introduce a nonempty paragraph and bounded next 2268.
    start = re.search(r'(?<!\d)2267\s*[.]?\s+(?=Lange Zeit|Soweit unblutige Mittel|Die überlieferte Lehre|Unter der Voraussetzung)', text, flags=re.IGNORECASE)
    if not start:
        return None
    stop = re.search(r'(?<!\d)2268\s*[.]?\s+(?=[A-ZÄÖÜ])', text[start.end():])
    candidate = text[start.start():start.end()+stop.start()] if stop else text[start.start():]
    return candidate[:16000]


def _download(url, allowed_hosts, max_bytes, timeout):
    current = url
    for _ in range(4):
        host, current = _parse_url(current, allowed_hosts)
        ip = _public_ip(host)
        connection = PinnedHTTPSConnection(host, ip, timeout)
        try:
            u = urlsplit(current)
            path = (u.path or "/") + (("?" + u.query) if u.query else "")
            connection.request("GET", path, headers={
                "Accept": "text/html,text/plain,application/xhtml+xml",
                "Accept-Encoding": "identity",
                "User-Agent": "THEOAgent-SourceGuard-PoC/0.1",
                "Connection": "close",
            })
            response = connection.getresponse()
            if response.status in (301, 302, 303, 307, 308):
                location = response.getheader("Location")
                if not location:
                    raise RetrievalError("Redirect ohne Ziel")
                current = urljoin(current, location)
                continue
            if response.status != 200:
                raise RetrievalError("HTTP-Abruf fehlgeschlagen (Status %s)" % response.status)
            mime = (response.getheader("Content-Type") or "").lower()
            if not mime.startswith(("text/html", "text/plain", "application/xhtml+xml")):
                raise RetrievalError("Dokumentformat nicht unterstützt (nur HTML/Text)")
            size = response.getheader("Content-Length")
            if size and size.isdigit() and int(size) > max_bytes:
                raise RetrievalError("Quelle überschreitet Downloadlimit")
            content = response.read(max_bytes + 1)
            if len(content) > max_bytes:
                raise RetrievalError("Quelle überschreitet Downloadlimit")
            raw = _decode_document(content, mime)
            if mime.startswith(("text/html", "application/xhtml+xml")):
                parser = TextExtractor()
                parser.feed(raw)
                raw = "".join(parser.parts)
            lines = [
                re.sub(r"[ \t\r\f\v]+", " ", line).strip()
                for line in raw.splitlines()
            ]
            text = "\n".join(line for line in lines if line)
            if len(text) < 100:
                raise RetrievalError("Kein hinreichender lesbarer Text")
            return current, text
        finally:
            connection.close()
    raise RetrievalError("Zu viele Umleitungen")


class Tools:
    class Valves(BaseModel):
        ALLOWED_HOSTS: str = Field(
            default=DEFAULT_HOSTS,
            description="Exact public HTTPS hostnames, comma-separated; no wildcards",
        )
        MAX_DOWNLOAD_KB: int = Field(default=1024, ge=32, le=2048)
        MAX_EXCERPT_CHARS: int = Field(default=12000, ge=1000, le=30000)
        TIMEOUT_SECONDS: int = Field(default=12, ge=3, le=30)

    def __init__(self):
        self.valves = self.Valves()

    def compare_kkk_2267_versions(self, historical_url: str, current_url: str) -> str:
        """Compare independently fetched KKK 2267 passages; flag version conflicts.

        :param historical_url: Historical candidate URL, not trusted as a date proof.
        :param current_url: Current KKK candidate URL.
        :return: JSON with text-classification evidence and explicit limits.
        """
        output = {"status": "UNVERIFIED", "version_verified": False,
                  "semantic_claim_verified": False, "comparisons": []}
        urls = (("historical_candidate", historical_url), ("current_candidate", current_url))
        for role, url in urls:
            retrieved = json.loads(self.read_source(url, "2267"))
            if retrieved.get("status") != "TEXT_RETRIEVED":
                output["status"] = "INCOMPLETE"
                output["comparisons"].append({
                    "role": role, "url": url,
                    "status": retrieved.get("status"),
                    "error": retrieved.get("error"),
                })
                return json.dumps(output, ensure_ascii=False)
            # Use the supplied excerpt only; never claim paragraph completeness
            # if 2268 cannot be observed in that excerpt.
            excerpt = retrieved.get("excerpt", "")
            paragraph = _kkk_2267_paragraph(excerpt)
            next_number_seen = bool(re.search(
                r'(?<!\d)2268\s*[.]?\s+(?=[A-ZÄÖÜ])', excerpt
            ))
            # A standalone 2018 revision notice has no following 2268.
            standalone_notice = (
                role == "current_candidate"
                and "/20180801_catechismo-penadimorte_" in retrieved["url"]
                and retrieved.get("truncated") is False
            )
            boundary = next_number_seen or standalone_notice
            classification = _kkk_2267_classification(paragraph or "")
            output["comparisons"].append({
                "role": role,
                "url": retrieved["url"],
                "evidence_id": retrieved.get("evidence_id"),
                "classification": classification,
                "paragraph_boundary_observed": boundary,
                "boundary_method": "next_paragraph" if next_number_seen else ("complete_revision_notice" if standalone_notice else "unknown"),
                "text": paragraph if boundary else "",
                "excerpt_truncated": retrieved.get("truncated"),
            })
        old, new = (item["classification"] for item in output["comparisons"])
        if old == "POST_2018_WORDING" and new == "POST_2018_WORDING":
            output["status"] = "VERSION_CONFLICT"
            output["reason"] = "Als historisch bezeichnete URL enthält ebenfalls den Text von 2018."
        elif old == "PRE_2018_WORDING" and new == "POST_2018_WORDING":
            output["status"] = "DISTINCT_WORDINGS_OBSERVED"
            output["reason"] = (
                "Unterschiedliche Textformulierungen gelesen; das konkrete "
                "Editionsjahr und die historische Originalausgabe bleiben unbelegt."
            )
        else:
            output["status"] = "VERSION_UNDETERMINED"
            output["reason"] = "Wortlaut kann nicht sicher zugeordnet werden."
        if not all(x.get("paragraph_boundary_observed") for x in output["comparisons"]):
            output["status"] = "INCOMPLETE"
            output["reason"] = "Mindestens eine Absatzgrenze oder vollständige Passage fehlt."
        return json.dumps(output, ensure_ascii=False)

    def read_source(self, url: str, section: str = "") -> str:
        """Fetch an allowed public HTTPS page and report actual text provenance.

        :param url: Exact URL of the source document, discovered separately.
        :param section: Optional section marker (e.g. '12'); not a verified locator.
        :return: JSON with provenance, excerpt and limitations; not semantic proof.
        """
        try:
            hosts = {
                host.strip().lower().rstrip(".")
                for host in self.valves.ALLOWED_HOSTS.split(",") if host.strip()
            }
            if not hosts:
                raise RetrievalError("Keine erlaubten Quellenhosts konfiguriert")
            if not isinstance(section, str) or len(section) > 40:
                raise RetrievalError("Ungültige Abschnittsangabe")
            final_url, full_text = _download(
                url, hosts, self.valves.MAX_DOWNLOAD_KB * 1024,
                self.valves.TIMEOUT_SECONDS,
            )
            marker_found = None
            start = 0
            if section.strip():
                marker = section.strip()
                expression = (
                    r"(?<![\w\d])(?:Nr\.\s*)?" + re.escape(marker)
                    + r"\s*[.)\]:\-](?!\d)"
                )
                match = re.search(expression, full_text, flags=re.IGNORECASE)
                marker_found = match is not None
                if match:
                    start = max(0, match.start() - 200)
            if section.strip() and marker_found is False:
                return json.dumps({
                    "status": "SECTION_NOT_LOCATED",
                    "technical_retrieval": True,
                    "semantic_claim_verified": False,
                    "section_requested": section.strip(),
                    "section_marker_found": False,
                    "url": final_url,
                    "total_extracted_characters": len(full_text),
                    "excerpt": "",
                    "limitations": (
                        "Die verlangte Abschnittsmarke wurde im extrahierten "
                        "Originaltext nicht gefunden; keine Abschnittslektüre "
                        "oder Fundstellenprüfung behaupten."
                    ),
                }, ensure_ascii=False)
            excerpt = full_text[start:start + self.valves.MAX_EXCERPT_CHARS]
            return json.dumps({
                "status": "TEXT_RETRIEVED",
                "technical_retrieval": True,
                "semantic_claim_verified": False,
                "section_requested": section.strip() or None,
                "section_marker_found": marker_found,
                "url": final_url,
                "evidence_id": hashlib.sha256(
                    (final_url + "\n" + full_text).encode("utf-8")
                ).hexdigest()[:20],
                "excerpt": excerpt,
                "excerpt_start_character": start,
                "total_extracted_characters": len(full_text),
                "truncated": start + len(excerpt) < len(full_text),
                "limitations": (
                    "HTML/Text extrahiert; Abschnittsmarker nur lexikalisch "
                    "gesucht. Weder Druckseite noch inhaltliche "
                    "Übereinstimmung der Behauptung technisch geprüft. "
                    "Keine SourceGuard-Pipe oder Antwortsperre."
                ),
            }, ensure_ascii=False)
        except RetrievalError as exc:
            return json.dumps({
                "status": "RETRIEVAL_FAILED",
                "technical_retrieval": False,
                "semantic_claim_verified": False,
                "error": str(exc),
            }, ensure_ascii=False)
        except (OSError, ssl.SSLError, http.client.HTTPException, UnicodeError) as exc:
            return json.dumps({
                "status": "RETRIEVAL_FAILED",
                "technical_retrieval": False,
                "semantic_claim_verified": False,
                "error": "Netzwerk-, TLS- oder Textverarbeitungsfehler",
                "error_type": type(exc).__name__,
            }, ensure_ascii=False)
