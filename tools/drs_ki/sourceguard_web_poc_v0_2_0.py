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


def _locator_pattern(locator):
    """Match a locator at the beginning of an extracted line, never a heading reference.

    Supports numbered sections with or without a dot, and literal line headings.
    Does not infer a missing section from a table of contents.
    """
    locator = locator.strip()
    if not locator or len(locator) > 100 or "\n" in locator:
        raise RetrievalError("Ungültige Fundstelle")
    label = re.escape(locator).replace(r"\ ", r"\s+")
    if locator.isdigit():
        # Exclude decimal subsections (e.g. 12.1 when requesting 12).
        return re.compile(r"(?m)^\s*" + label +
                          r"(?:[.)](?!\d)|(?=\s+))\s*(?=\S)")
    return re.compile(r"(?mi)^\s*" + label + r"(?=\s|[.:)]|$)")


def _normalize_evidence(text):
    """Formatting-insensitive comparison only; neither dating nor semantic proof."""
    return " ".join(text.split())


def _locate(text, locator):
    matches = list(_locator_pattern(locator).finditer(text))
    if not matches:
        return None, "SECTION_NOT_LOCATED"
    if len(matches) != 1:
        return None, "LOCATOR_AMBIGUOUS"
    return matches[0], "FOUND"


def _section_text(text, locator, match, max_chars):
    """Best-effort numbered section window without assuming any named work."""
    if not locator.isdigit():
        rest = text[match.start():]
        return rest[:max_chars], (
            "WINDOW_LIMIT" if len(rest) > max_chars else "DOCUMENT_END_OR_UNKNOWN"
        )
    next_label = str(int(locator) + 1)
    # Only the next numbered paragraph, anchored at the beginning of a line,
    # counts as a boundary. A number inside a sentence does not.
    following, state = _locate(text[match.end():], next_label)
    if state == "FOUND":
        end = match.end() + following.start()
        return text[match.start():min(end, match.start() + max_chars)], (
            "NEXT_NUMBER" if end - match.start() <= max_chars else "WINDOW_LIMIT"
        )
    rest = text[match.start():]
    return rest[:max_chars], (
        "WINDOW_LIMIT" if len(rest) > max_chars else "DOCUMENT_END_OR_UNKNOWN"
    )


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
                "User-Agent": "THEOAgent-SourceGuard-PoC/0.2",
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

    def compare_sources(self, url_a: str, url_b: str, locator: str) -> str:
        """Compare literal evidence at the same locator in two original URLs.

        :param url_a: First source URL; no version assumption.
        :param url_b: Second source URL; no version assumption.
        :param locator: Number or heading in the extracted text.
        :return: Verifiable equal/different excerpt status, never an edition date.
        """
        result = {
            "status": "INCOMPLETE", "locator": locator,
            "version_verified": False, "semantic_claim_verified": False,
            "comparisons": [],
        }
        for role, url in (("source_a", url_a), ("source_b", url_b)):
            item = json.loads(self.read_source(url, locator))
            if item.get("status") != "TEXT_RETRIEVED":
                result["comparisons"].append({
                    "role": role, "url": url, "status": item.get("status"),
                    "error": item.get("error"),
                })
                return json.dumps(result, ensure_ascii=False)
            result["comparisons"].append({
                "role": role, "url": item["url"], "evidence_id": item["evidence_id"],
                "section_text": item["section_text"],
                "section_boundary": item["section_boundary"],
                "section_window_truncated": item["section_window_truncated"],
            })
        a, b = (x["section_text"] for x in result["comparisons"])
        if any(x["section_window_truncated"] for x in result["comparisons"]):
            result["reason"] = "Mindestens eine Fundstellenpassage wurde gekürzt."
        elif _normalize_evidence(a) == _normalize_evidence(b):
            result["status"] = "SAME_TEXT"
        else:
            result["status"] = "DIFFERENT_TEXT"
        result["limitations"] = (
            "Textvergleich nach Whitespace-Normalisierung. Fundstelleninhalt "
            "und historische Edition nicht semantisch oder chronologisch geprüft."
        )
        return json.dumps(result, ensure_ascii=False)

    def verify_evidence(self, claim: str, url: str, locator: str) -> str:
        """Check an exact quotation, NOT the truth of a paraphrased claim.

        :param claim: Exact quote to find, or a paraphrase requiring manual review.
        :param url: Original page URL.
        :param locator: Required section label.
        :return: Literal quote-match result; semantic_claim_verified is always false.
        """
        if not isinstance(claim, str) or not claim.strip() or len(claim) > 4000:
            return json.dumps({"status": "INVALID_CLAIM", "semantic_claim_verified": False})
        item = json.loads(self.read_source(url, locator))
        result = {
            "status": "INCOMPLETE", "semantic_claim_verified": False,
            "source_status": item.get("status"), "url": item.get("url", url),
            "locator": locator, "evidence_id": item.get("evidence_id"),
        }
        if item.get("status") == "TEXT_RETRIEVED":
            result["exact_quote_found_in_excerpt"] = (
                _normalize_evidence(claim) in _normalize_evidence(item["section_text"])
            )
            result["status"] = (
                "QUOTE_FOUND" if result["exact_quote_found_in_excerpt"]
                else "QUOTE_NOT_FOUND_IN_EXCERPT"
            )
            result["truncated"] = item.get("section_window_truncated")
            result["limitations"] = (
                "Wörtliche Textsuche, kein semantischer Beweis; bei gekürztem "
                "Textfenster ist ein negativer Befund nicht abschließend."
            )
        return json.dumps(result, ensure_ascii=False)

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
            location_status = None
            start = 0
            if section.strip():
                marker = section.strip()
                match, location_status = _locate(full_text, marker)
                marker_found = match is not None
                if match:
                    start = max(0, match.start() - 200)
            if section.strip() and marker_found is False:
                return json.dumps({
                    "status": location_status,
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
            section_text = ""
            section_boundary = None
            section_window_truncated = False
            if section.strip() and match:
                section_text, section_boundary = _section_text(
                    full_text, section.strip(), match,
                    self.valves.MAX_EXCERPT_CHARS,
                )
                section_window_truncated = section_boundary == "WINDOW_LIMIT"
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
                "section_text": section_text,
                "section_boundary": section_boundary,
                "section_window_truncated": section_window_truncated,
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
