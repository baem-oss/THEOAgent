"""
Name: THEOAgent SourceGuard 0.2.1
Zweck: Quellenübergreifende Evidenzaufbereitung für THEOAgent: kontrollierter
       Abruf öffentlicher Webquellen, Verarbeitung von Originalauszügen aus
       Fachbibliothek und DRS-Werkzeugen sowie technische Prüfung von
       Fundstellen, Zitaten und Textübereinstimmungen.
Grenze: Keine eigenständige semantische Verifikation; fachliche Belegprüfung
        erfolgt durch THEOAgent anhand der bereitgestellten Originalpassage.
Autor: BäM (PO, RE) / ChatGPT (SE) / Deepseek (QE)
Datum: 16.11.2026
Version: 0.2.1

Hinweis: Open-WebUI-Werkzeug für DRS:KI DEV; keine SourceGuard-Pipe.
Knowledge- und DRS-Tool-Inhalte stammen aus vorhandenen Werkzeugaufrufen.
SourceGuard authentifiziert übergebene Werkzeugauszüge nicht selbst.
"""

import hashlib
import http.client
import ipaddress
import json
import re
import socket
import ssl
import unicodedata
from html.parser import HTMLParser
from typing import Optional
from urllib.parse import urljoin, urlsplit, urlunsplit

from pydantic import BaseModel, Field


# Versionskennung der laufenden Werkzeugimplementierung.
VERSION = "0.2.1"

# Nur diese öffentlichen Webseiten sind ab Werk für den Abruf freigegeben.
# Die Valves erlauben eine lokale Anpassung, jedoch keine Platzhalter-Domains.
DEFAULT_HOSTS = (
    "www.vatican.va,vatican.va,www.dbk.de,dbk.de,"
    "www.drs.de,drs.de,amtsblatt.drs.de,"
    "rechtssammlung.drs.de,recht.drs.de,"
    "www.die-bibel.de,die-bibel.de"
)


class RetrievalError(Exception):
    """Erwarteter Fehler, etwa bei gesperrten URLs oder unlesbaren Dokumenten."""


class TextExtractor(HTMLParser):
    """HTML auf lesbaren Fließtext reduzieren, ohne Skriptinhalte zu übernehmen."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        # Zähler für HTML-Bereiche, deren Inhalt nicht zur Quelle gehört.
        self.skip = 0
        # Textteile werden gesammelt und später zu einem Dokument verbunden.
        self.parts = []

    def handle_starttag(self, tag, attrs):
        # Skripte, Styles und SVG enthalten keine zu zitierenden Textabsätze.
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1
        # Absatz- und Überschriftentags beginnen eine neue Textzeile.
        # Das hilft später, Abschnittsnummern am Zeilenanfang zu finden.
        if not self.skip and tag in (
            "p", "div", "article", "section", "h1", "h2", "h3",
            "h4", "h5", "h6", "li", "br", "tr"
        ):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        # Geschützten HTML-Bereich beenden und Absatzgrenzen erhalten.
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1
        if not self.skip and tag in ("p", "div", "article", "section", "li", "tr"):
            self.parts.append("\n")

    def handle_data(self, data):
        # Nur sichtbare, nichtleere Textbestandteile in die Evidenz aufnehmen.
        if not self.skip and data.strip():
            self.parts.append(data)


def _parse_url(url, allowed_hosts):
    """URL vor jedem Abruf und vor jeder Weiterleitung auf Zulässigkeit prüfen."""
    # Steuerzeichen und überlange URLs werden vor dem Netzwerkzugriff verworfen.
    if not isinstance(url, str) or len(url) > 2048 or any(ord(c) <= 32 for c in url):
        raise RetrievalError("Unzulässiges URL-Format")
    try:
        u = urlsplit(url)
        host = (u.hostname or "").lower().rstrip(".")
        # Ausschließlich HTTPS, Standardport 443 und exakt freigegebene Hosts.
        # Benutzerinformationen in URLs sind nicht gestattet.
        if (
            u.scheme.lower() != "https" or not host
            or u.username is not None or u.password is not None
            or u.port not in (None, 443)
            or host not in allowed_hosts
        ):
            raise RetrievalError("Nur freigegebene öffentliche HTTPS-Hosts sind zulässig")
        # Ein URL-Fragment (#...) wird nicht an den Webserver übertragen.
        if u.fragment:
            url = urlunsplit((u.scheme, u.netloc, u.path, u.query, ""))
        return host, url
    except ValueError as exc:
        raise RetrievalError("Ungültige URL") from exc


def _public_ip(host):
    """DNS prüfen: alle gelieferten IPs müssen global erreichbar sein."""
    try:
        found = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
        addresses = list(dict.fromkeys(item[4][0] for item in found))
        # Wichtig gegen SSRF: Bereits eine einzige private/interne IP reicht
        # aus, um den gesamten Host-Abruf abzulehnen.
        if not addresses or not all(ipaddress.ip_address(ip).is_global for ip in addresses):
            raise RetrievalError("Nichtöffentliche oder ungültige DNS-Ziele abgewiesen")
        return addresses[0]
    except (socket.gaierror, ValueError) as exc:
        raise RetrievalError("Host konnte nicht sicher aufgelöst werden") from exc


class PinnedHTTPSConnection(http.client.HTTPSConnection):
    """Verbindung zur geprüften IP; TLS-Zertifikat bleibt an Hostnamen gebunden."""

    def __init__(self, hostname, pinned_ip, timeout):
        super().__init__(
            hostname, port=443, timeout=timeout,
            context=ssl.create_default_context()
        )
        self.pinned_ip = pinned_ip

    def connect(self):
        # Nach der DNS-Prüfung keine zweite, ungeprüfte Namensauflösung.
        sock = socket.create_connection((self.pinned_ip, 443), self.timeout)
        try:
            # Trotz IP-Pinning muss das HTTPS-Zertifikat zum echten Host passen.
            self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
        except Exception:
            sock.close()
            raise


def _decode_document(content, content_type, return_details=False):
    """HTML-Bytes dekodieren; verwendete Kodierung auf Wunsch mitmelden.

    Der ISO-8859-1-Fallback bleibt für historische Webseiten erhalten. Ohne
    eindeutige Kodierungsdeklaration ist die Interpretation aber unsicher.
    """
    header = re.search(r'charset\s*=\s*["\']?([a-z0-9_-]+)', content_type.lower())
    meta = re.search(
        rb'<meta[^>]+charset\s*=\s*["\']?([a-z0-9_-]+)',
        content[:8192], flags=re.IGNORECASE,
    )
    meta_charset = meta.group(1).decode("ascii").lower() if meta else None
    http_charset = header.group(1).lower() if header else None
    # Byte Order Mark (BOM) hat Vorrang; danach deklarierte Kodierungen.
    candidates = []
    if content.startswith(b"\xef\xbb\xbf"):
        candidates.append("utf-8-sig")
    # Kodierungen werden strikt getestet: defekte Umlaute dürfen nicht durch
    # Ersatzzeichen kaschiert und anschließend als Originaltext zitiert werden.
    candidates.extend([http_charset, meta_charset, "utf-8", "windows-1252", "iso-8859-1"])
    allowed = {"utf-8", "utf-8-sig", "windows-1252", "iso-8859-1", "us-ascii", "latin1"}
    for charset in dict.fromkeys(x for x in candidates if x in allowed):
        try:
            result = content.decode(charset, errors="strict")
        except (UnicodeError, LookupError):
            continue
        if "\ufffd" not in result:
            # Der permissive Latin-1-Fallback darf nicht als sichere
            # Originalkodierung ausgegeben werden. Ebenso kann ein deklarierter
            # Charset inhaltlich falsch sein; diese Unsicherheit bleibt offen.
            uncertain = charset in ("windows-1252", "iso-8859-1") and charset not in (
                http_charset, meta_charset
            )
            return (result, charset, uncertain) if return_details else result
    raise RetrievalError("Zeichenkodierung nicht sicher lesbar")


def _locator_pattern(locator):
    """Suchmuster für eine Fundstelle am Anfang einer extrahierten Zeile.

    Unterstützt Nummerierungen mit/ohne Punkt sowie wörtliche Überschriften.
    Eine bloße Nennung der Nummer innerhalb eines Satzes ist kein Treffer.
    """
    locator = locator.strip()
    if not locator or len(locator) > 100 or "\n" in locator:
        raise RetrievalError("Ungültige Fundstelle")
    # Sonderzeichen des Locators werden als Text behandelt, nicht als Regex.
    label = re.escape(locator).replace(r"\ ", r"\s+")
    if locator.isdigit():
        # Abschnitt 12 darf nicht mit Unterabschnitt 12.1 verwechselt werden.
        return re.compile(r"(?m)^\s*" + label +
                          r"(?:[.)](?!\d)|(?=\s+))\s*(?=\S)")
    return re.compile(r"(?mi)^\s*" + label + r"(?=\s|[.:)]|$)")


def _normalize_evidence(text):
    """Leerzeichen und Zeilenumbrüche für den rein textuellen Vergleich glätten.

    Weder das Alter noch die theologische Richtigkeit einer Quelle wird geprüft.
    """
    normalized = unicodedata.normalize("NFC", text).replace("\u00ad", "")
    normalized = normalized.translate(str.maketrans({
        "‘": "'", "’": "'", "‚": "'",
        "“": '"', "”": '"', "„": '"',
        "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
    }))
    return " ".join(normalized.split()).casefold()


def _section_scope_confirmed(item):
    """Nur eindeutig begrenzter Originalabschnitt, nicht bloßes Textfenster."""
    return (
        item.get("status") == "TEXT_RETRIEVED"
        and item.get("section_boundary") == "NEXT_NUMBER"
        and not item.get("section_window_truncated", False)
        and bool(item.get("section_text", "").strip())
    )


def _evidence_verification_status(source_type, source_scope_confirmed=False):
    """Textprovenienz und Fundstellenabgrenzung, niemals semantische Wahrheit."""
    if source_type != "web":
        return "MODEL_SUPPLIED_UNVERIFIED"
    return (
        "WEB_TEXT_SCOPE_CONFIRMED" if source_scope_confirmed
        else "WEB_TEXT_SCOPE_UNCONFIRMED"
    )


def _locate(text, locator):
    """Genau einen Fundstellentreffer verlangen; Mehrdeutigkeit ist kein PASS."""
    matches = list(_locator_pattern(locator).finditer(text))
    if not matches:
        return None, "SECTION_NOT_LOCATED"
    # Zwei gleich aussehende Nummern können z. B. in Haupttext und Anhang
    # vorkommen. Der Adapter wählt dann nicht einfach den ersten Treffer.
    if len(matches) != 1:
        return None, "LOCATOR_AMBIGUOUS"
    return matches[0], "FOUND"


def _section_text(text, locator, match, max_chars):
    """Textfenster ab der Fundstelle bestimmen, ohne konkrete Werke zu kennen.

    Die nächste Abschnittsnummer ist ein möglicher Grenzmarker, jedoch kein
    Beweis, dass das gesamte Dokument strukturell korrekt erschlossen wurde.
    """
    # Für freie Überschriften ist die folgende Absatzgrenze unbekannt.
    if not locator.isdigit():
        rest = text[match.start():]
        return rest[:max_chars], (
            "WINDOW_LIMIT" if len(rest) > max_chars else "DOCUMENT_END_OR_UNKNOWN"
        )
    # Bei numerischen Locators wird nach der direkt folgenden Nummer gesucht.
    # Eine Erwähnung dieser Zahl mitten im Fließtext genügt ausdrücklich nicht.
    next_label = str(int(locator) + 1)
    following, state = _locate(text[match.end():], next_label)
    if state == "FOUND":
        # Nur der Abschnitt bis vor den Anfang des nächsten Abschnitts gehört
        # zum zurückgegebenen Fundstellentext.
        end = match.end() + following.start()
        return text[match.start():min(end, match.start() + max_chars)], (
            "NEXT_NUMBER" if end - match.start() <= max_chars else "WINDOW_LIMIT"
        )
    # Fehlt eine eindeutige Folgenummer, endet das Fenster am Dokumentende
    # oder am Zeichenlimit. Der Abschnitt gilt deshalb nicht als sicher komplett.
    rest = text[match.start():]
    return rest[:max_chars], (
        "WINDOW_LIMIT" if len(rest) > max_chars else "DOCUMENT_END_OR_UNKNOWN"
    )


def _download(url, allowed_hosts, max_bytes, timeout):
    """Öffentlichen HTML-/Textinhalt mit Limits und Redirect-Kontrolle abrufen."""
    current = url
    # Jede Weiterleitung wird erneut auf erlaubten HTTPS-Host geprüft.
    # Die Schleife begrenzt zugleich die maximale Zahl an Redirects.
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
                "User-Agent": "THEOAgent-SourceGuard/0.2.1",
                "Connection": "close",
            })
            response = connection.getresponse()
            # Redirects dürfen die Allowlist-/IP-Kontrolle nicht umgehen.
            if response.status in (301, 302, 303, 307, 308):
                location = response.getheader("Location")
                if not location:
                    raise RetrievalError("Redirect ohne Ziel")
                current = urljoin(current, location)
                continue
            if response.status != 200:
                raise RetrievalError("HTTP-Abruf fehlgeschlagen (Status %s)" % response.status)
            # Andere Dateitypen (insbesondere PDFs) sind hier bewusst
            # ausgeschlossen; sie benötigen einen eigenen, geprüften Parser.
            mime = (response.getheader("Content-Type") or "").lower()
            if not mime.startswith(("text/html", "text/plain", "application/xhtml+xml")):
                raise RetrievalError("Dokumentformat nicht unterstützt (nur HTML/Text)")
            # Sowohl die angekündigte Größe als auch die tatsächlich gelesenen
            # Bytes werden begrenzt: Content-Length kann falsch oder leer sein.
            size = response.getheader("Content-Length")
            if size and size.isdigit() and int(size) > max_bytes:
                raise RetrievalError("Quelle überschreitet Downloadlimit")
            content = response.read(max_bytes + 1)
            if len(content) > max_bytes:
                raise RetrievalError("Quelle überschreitet Downloadlimit")
            # Erst Zeichensatz korrekt dekodieren, danach HTML-Struktur entfernen.
            raw, charset_used, charset_uncertain = _decode_document(
                content, mime, return_details=True
            )
            if mime.startswith(("text/html", "application/xhtml+xml")):
                parser = TextExtractor()
                parser.feed(raw)
                raw = "".join(parser.parts)
            # Uneinheitliche horizontale Leerzeichen glätten; Zeilengrenzen
            # für die spätere Abschnittssuche bewusst erhalten.
            lines = [
                re.sub(r"[ \t\r\f\v]+", " ", line).strip()
                for line in raw.splitlines()
            ]
            text = "\n".join(line for line in lines if line)
            if len(text) < 100:
                raise RetrievalError("Kein hinreichender lesbarer Text")
            return current, text, charset_used, charset_uncertain
        finally:
            connection.close()
    raise RetrievalError("Zu viele Umleitungen")


class Tools:
    """Von Open WebUI erkannte Werkzeugfunktionen für THEOAgent."""

    class Valves(BaseModel):
        """Einstellungen, die auf DRS:KI DEV im Werkzeugeditor sichtbar sind."""
        ALLOWED_HOSTS: str = Field(
            default=DEFAULT_HOSTS,
            description="Exact public HTTPS hostnames, comma-separated; no wildcards",
        )
        # Begrenzung gegen sehr große oder unerwartete Webantworten.
        MAX_DOWNLOAD_KB: int = Field(default=1024, ge=32, le=2048)
        # Maximaler Zeichenumfang je zurückgegebenem Textfenster.
        MAX_EXCERPT_CHARS: int = Field(default=12000, ge=1000, le=30000)
        # Abbruch zu langsamer Abrufe, damit das Modell nicht endlos wartet.
        TIMEOUT_SECONDS: int = Field(default=12, ge=3, le=30)

    def __init__(self):
        self.valves = self.Valves()

    def compare_sources(self, url_a: str, url_b: str, locator: str) -> str:
        """Zwei unabhängig abgerufene Textstellen technisch vergleichen.

        :param url_a: URL der ersten Quelle, ohne Altersannahme.
        :param url_b: URL der zweiten Quelle, ohne Altersannahme.
        :param locator: Gesuchte Nummer oder Überschrift.
        :return: Textgleichheit/-abweichung; keine Editionsauthentifizierung.
        """
        result = {
            "status": "INCOMPLETE", "locator": locator,
            "version_verified": False, "semantic_claim_verified": False,
            "comparisons": [],
        }
        # F-01: Ein Vergleich benötigt immer eine eindeutige Fundstelle.
        if not isinstance(locator, str) or not locator.strip() or len(locator) > 100:
            result["status"] = "INVALID_LOCATOR"
            return json.dumps(result, ensure_ascii=False)
        # Jede Quelle wird mit denselben technischen Prüfungen separat gelesen.
        for role, url in (("source_a", url_a), ("source_b", url_b)):
            item = json.loads(self.read_source(url, locator))
            # Scheitert bereits ein Abruf, wird kein Vergleichsergebnis behauptet.
            if item.get("status") != "TEXT_RETRIEVED":
                result["comparisons"].append({
                    "role": role, "url": url, "status": item.get("status"),
                    "error": item.get("error"),
                })
                return json.dumps(result, ensure_ascii=False)
            result["comparisons"].append({
                "role": role, "url": item["url"], "evidence_id": item["evidence_id"],
                "section_scope_confirmed": _section_scope_confirmed(item),
                "section_text": item["section_text"],
                "section_boundary": item["section_boundary"],
                "section_window_truncated": item["section_window_truncated"],
            })
        # Verglichen werden nur die lokalisierten Abschnitte, nicht das
        # gesamte Dokument und auch nicht ein beliebiger Textausschnitt davor.
        a, b = (x["section_text"] for x in result["comparisons"])
        if not a.strip() or not b.strip():
            result["reason"] = "Mindestens eine gelesene Fundstellenpassage ist leer."
        elif not all(x["section_scope_confirmed"] for x in result["comparisons"]):
            result["reason"] = "Mindestens eine Fundstellenpassage ist nicht sicher abgegrenzt."
        # Unterschiede bei Zeilenumbrüchen allein gelten nicht als Textabweichung.
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
        """Prüfen, ob ein Zitat im abgerufenen Fundstellentext vorkommt.

        :param claim: Wörtlich zu suchender Text; eine Paraphrase ist nicht prüfbar.
        :param url: URL der Originalquelle.
        :param locator: Fundstelle im Dokument.
        :return: Treffer-/Nichttrefferstatus; kein semantischer Wahrheitsbeweis.
        """
        # Leere und überlange Prüftexte werden nicht an die Quellensuche übergeben.
        if not isinstance(claim, str) or not claim.strip() or len(claim) > 4000:
            return json.dumps({"status": "INVALID_CLAIM", "semantic_claim_verified": False})
        if not isinstance(locator, str) or not locator.strip() or len(locator) > 100:
            return json.dumps({"status": "INVALID_LOCATOR", "semantic_claim_verified": False})
        item = json.loads(self.read_source(url, locator))
        result = {
            "status": "INCOMPLETE", "semantic_claim_verified": False,
            "source_status": item.get("status"), "url": item.get("url", url),
            "locator": locator, "evidence_id": item.get("evidence_id"),
            "evidence_id_origin": "DIRECT_WEB_RETRIEVAL" if item.get("evidence_id") else None,
        }
        if item.get("status") == "TEXT_RETRIEVED":
            # Wörtliche Suche nach Normalisierung der Leerzeichen. Synonyme
            # oder logische Folgerungen kann dieses Verfahren nicht beurteilen.
            result["exact_quote_found_in_excerpt"] = (
                _normalize_evidence(claim) in _normalize_evidence(item["section_text"])
            )
            result["section_scope_confirmed"] = _section_scope_confirmed(item)
            result["status"] = (
                "QUOTE_FOUND" if (
                    result["exact_quote_found_in_excerpt"] and result["section_scope_confirmed"]
                ) else (
                    "QUOTE_FOUND_SCOPE_UNCONFIRMED"
                    if result["exact_quote_found_in_excerpt"]
                    else "QUOTE_NOT_FOUND_IN_EXCERPT"
                )
            )
            result["truncated"] = item.get("section_window_truncated")
            result["limitations"] = (
                "Wörtliche Textsuche, kein semantischer Beweis; bei gekürztem "
                "Textfenster ist ein negativer Befund nicht abschließend."
            )
        return json.dumps(result, ensure_ascii=False)

    def review_evidence(
        self,
        claim: str,
        source_type: str,
        source_title: str,
        locator: str,
        evidence_text: str = "",
        source_url: str = "",
        evidence_reference: str = "",
        source_tool: str = "",
        evidence_kind: str = "original_excerpt",
    ) -> str:
        """Eine Aussage anhand von Web-/Knowledge-/DRS-Werkzeugevidenz prüfen.

        :param claim: Die genau zu überprüfende Aussage oder das Zitat.
        :param source_type: "web", "knowledge", "document" oder "tool_excerpt".
        :param source_title: Name des Werks oder Dokuments.
        :param locator: Abschnitt, Kapitel oder vom Knowledge-Tool gemeldete Stelle.
        :param evidence_text: Gelesene Passage aus view_knowledge_file bzw.
                              einem anderen bestehenden Dokumentwerkzeug.
                              Für "web" wird sie NICHT als Beleg akzeptiert.
        :param source_url: Original-URL, nur für source_type="web".
        :param evidence_reference: Rückverweis auf einen tatsächlichen Tool-Leseaufruf.
        :param source_tool: Name des ausliefernden Knowledge-/DRS-Werkzeugs.
        :param evidence_kind: "original_excerpt", "search_snippet" oder "summary".
        :return: Strukturierte Evidenz und Prüfbeschränkungen als JSON.
        """
        # Alle Quellenarten erhalten dasselbe Prüfschema. Der technische Weg,
        # auf dem der Text zur Verfügung gestellt wird, bleibt aber sichtbar.
        result = {
            "status": "INCOMPLETE",
            "source_type": source_type,
            "source_title": source_title,
            "locator": locator,
            "source_url": source_url or None,
            "evidence_reference": evidence_reference or None,
            "source_tool": source_tool or None,
            "evidence_kind": evidence_kind,
            "claim": claim,
            "semantic_claim_verified": False,
            "source_provenance_verified": False,
            "evidence_verification_status": "NOT_VERIFIED",
            "section_scope_confirmed": False,
            "claim_assessment": "NOT_ASSESSED",
            "exact_wording_found": False,
            "evidence_text": "",
        }

        # Keine leeren oder überlangen Eingaben unkontrolliert an das Modell
        # zurückgeben. Besonders Knowledge-Passagen können sehr lang sein.
        if (
            not isinstance(claim, str) or not claim.strip() or len(claim) > 4000
            or not isinstance(source_type, str)
            or not isinstance(source_title, str) or len(source_title) > 500
            or not isinstance(locator, str) or len(locator) > 200
            or not isinstance(evidence_text, str) or len(evidence_text) > 30000
            or not isinstance(evidence_reference, str)
            or len(evidence_reference) > 2000
            or not isinstance(source_tool, str) or len(source_tool) > 160
            or not isinstance(evidence_kind, str)
        ):
            result["status"] = "INVALID_INPUT"
            return json.dumps(result, ensure_ascii=False)

        kind = source_type.strip().lower()
        if kind not in ("web", "knowledge", "document", "tool_excerpt"):
            result["status"] = "UNSUPPORTED_SOURCE_TYPE"
            return json.dumps(result, ensure_ascii=False)
        result["source_type"] = kind
        if evidence_kind not in ("original_excerpt", "search_snippet", "summary"):
            result["status"] = "UNSUPPORTED_EVIDENCE_KIND"
            return json.dumps(result, ensure_ascii=False)

        # Suchtreffer und KI-Zusammenfassungen genügen nicht als Originalbeleg.
        # Die modellseitige Einstufung ist kein unabhängiger Tool-Nachweis.
        if kind != "web" and evidence_kind != "original_excerpt":
            result["status"] = "INSUFFICIENT_EVIDENCE"
            result["limitations"] = (
                "Nur Such-Snippet oder Zusammenfassung übergeben. "
                "Eine einschlägige Originalpassage muss zunächst mit einem "
                "geeigneten Werkzeug geöffnet werden."
            )
            return json.dumps(result, ensure_ascii=False)

        if kind == "web":
            # Webquellen werden tatsächlich neu abgerufen. Ein vom Modell
            # mitgelieferter Text kann den Originalabruf nicht ersetzen.
            if not source_url or not locator.strip():
                result["status"] = "MISSING_SOURCE_REFERENCE"
                return json.dumps(result, ensure_ascii=False)
            retrieved = json.loads(self.read_source(source_url, locator))
            result["retrieval_status"] = retrieved.get("status")
            if retrieved.get("status") != "TEXT_RETRIEVED":
                result["status"] = "SOURCE_NOT_READ"
                result["retrieval_error"] = retrieved.get("error")
                result["retrieval_error_type"] = retrieved.get("error_type")
                return json.dumps(result, ensure_ascii=False)
            source_text = retrieved.get("section_text", "")
            result["source_url"] = retrieved.get("url")
            result["evidence_id"] = retrieved.get("evidence_id")
            result["source_provenance_verified"] = True
            result["source_provenance_level"] = "TECHNICALLY_RETRIEVED_URL"
            result["section_scope_confirmed"] = _section_scope_confirmed(retrieved)
            result["evidence_verification_status"] = _evidence_verification_status(
                "web", result["section_scope_confirmed"]
            )
            result["evidence_id_origin"] = "DIRECT_WEB_RETRIEVAL"
            result["charset_used"] = retrieved.get("charset_used")
            result["charset_uncertain"] = retrieved.get("charset_uncertain")
            result["limitations"] = (
                "Nachgewiesen ist nur der technische Abruf der angegebenen URL, "
                "nicht die Autorenschaft, Editions-/Normfassung oder inhaltliche "
                "Richtigkeit. Eine Abschnittsgrenze kann unklar sein."
            )
            result["text_window_limited"] = retrieved.get(
                "section_window_truncated", False
            )
            result["section_boundary"] = retrieved.get("section_boundary")
        else:
            # Knowledge, Dokumente und DRS-Originalauszüge: Vorhandene
            # Werkzeuge liefern die Passage. SourceGuard besitzt weder
            # direkten Knowledge-Zugriff noch den technischen Kontext anderer
            # DRS-Toolaufrufe und kann deren Text nicht unabhängig bestätigen.
            # Deshalb ist eine Referenz auf den Lesevorgang verpflichtend.
            if (
                not source_title.strip() or not locator.strip()
                or not evidence_reference.strip() or not evidence_text.strip()
                or not source_tool.strip()
            ):
                result["status"] = "MISSING_SOURCE_REFERENCE"
                result["required"] = (
                    "source_title, locator, evidence_reference, source_tool, "
                    "evidence_text aus einem tatsächlich ausgeführten Werkzeugaufruf"
                )
                return json.dumps(result, ensure_ascii=False)
            source_text = evidence_text
            result["source_provenance_level"] = "MODEL_SUPPLIED_TOOL_EXCERPT"
            result["evidence_verification_status"] = _evidence_verification_status(kind)
            result["evidence_id_origin"] = "MODEL_SUPPLIED_TOOL_EXCERPT"
            result["text_window_limited"] = None
            result["limitations"] = (
                "Text, Werkzeugname und Fundstelle vom aufrufenden Modell "
                "übergeben. Keine unabhängige Authentifizierung des "
                "Knowledge-/DRS-Toolaufrufs oder des Originaldokuments. "
                "Die Quellenautorität ist gesondert fachlich zu beurteilen."
            )

        if not source_text.strip():
            result["status"] = "EMPTY_EVIDENCE"
            return json.dumps(result, ensure_ascii=False)

        # Lexikalische Übereinstimmung ist ein nützlicher erster Hinweis:
        # Sie kann ein exaktes Zitat belegen, aber KEINE Paraphrase beurteilen.
        result["evidence_text"] = source_text
        result["exact_wording_found"] = (
            _normalize_evidence(claim)
            in _normalize_evidence(source_text)
        )
        result["evidence_id"] = result.get("evidence_id") or hashlib.sha256(
            (source_title + "\n" + locator + "\n" + source_text).encode("utf-8")
        ).hexdigest()[:20]
        # Ein Treffer im nicht sicher begrenzten Webfenster darf nicht als
        # gültige Zuordnung zur verlangten Fundstelle erscheinen.
        result["status"] = (
            "EVIDENCE_SCOPE_UNCONFIRMED"
            if kind == "web" and not result["section_scope_confirmed"]
            else "EVIDENCE_READY_FOR_REVIEW"
        )
        result["claim_assessment"] = "REQUIRES_MODEL_JUDGEMENT"
        result["review_instruction"] = (
            "Prüfe anhand des tatsächlich gelesenen Belegtextes, ob die "
            "Behauptung gestützt, widerlegt oder nicht überprüfbar ist. "
            "Zitiere die Fundstelle und trenne Textbefund von Interpretation. "
            "Ein wörtlicher Treffer allein ist keine semantische Verifikation."
        )
        return json.dumps(result, ensure_ascii=False)

    def read_source(self, url: str, section: str = "") -> str:
        """Originalquelle abrufen, Fundstelle finden und Nachweise zurückgeben.

        :param url: Exakte URL; eine Suchmaschine muss sie zuvor ermitteln.
        :param section: Optionale Abschnittsnummer oder wörtliche Überschrift.
        :return: JSON mit URL, Evidenzkennung, Text und technischen Grenzen.
        """
        try:
            # Die zugelassenen Hosts werden aus der aktuellen Valve gelesen.
            # Die Prüfung geschieht bei jedem einzelnen Abruf erneut.
            hosts = {
                host.strip().lower().rstrip(".")
                for host in self.valves.ALLOWED_HOSTS.split(",") if host.strip()
            }
            if not hosts:
                raise RetrievalError("Keine erlaubten Quellenhosts konfiguriert")
            if not isinstance(section, str) or len(section) > 100:
                raise RetrievalError("Ungültige Abschnittsangabe")
            # Der bisherige zweielementige Rückgabewert bleibt als
            # Kompatibilitätsweg für ältere Aufrufer/Mocks möglich.
            downloaded = _download(
                url, hosts, self.valves.MAX_DOWNLOAD_KB * 1024,
                self.valves.TIMEOUT_SECONDS,
            )
            final_url, full_text = downloaded[:2]
            charset_used = downloaded[2] if len(downloaded) > 2 else None
            charset_uncertain = downloaded[3] if len(downloaded) > 3 else None
            # Ohne gewünschten Abschnitt wird der allgemeine Dokumentanfang
            # als Vorschau bereitgestellt. Mit Abschnitt gilt: eindeutig finden.
            marker_found = None
            location_status = None
            start = 0
            if section.strip():
                marker = section.strip()
                match, location_status = _locate(full_text, marker)
                marker_found = match is not None
                if match:
                    start = max(0, match.start() - 200)
            # Fail-closed: Eine fehlende oder mehrfach vorkommende Fundstelle
            # darf nicht als erfolgreich gelesener Beleg ausgegeben werden.
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
            # section_text beginnt an der Fundstelle; excerpt beginnt für den
            # Kontext bis zu 200 Zeichen davor. Beide Zwecke sind verschieden.
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
                # Kennung aus finaler URL und extrahiertem Gesamttext:
                # bei Textänderungen ändert sich grundsätzlich auch die Kennung.
                "evidence_id": hashlib.sha256(
                    (final_url + "\n" + full_text).encode("utf-8")
                ).hexdigest()[:20],
                "excerpt": excerpt,
                "section_text": section_text,
                "section_boundary": section_boundary,
                "section_scope_confirmed": section_boundary == "NEXT_NUMBER",
                "section_window_truncated": section_window_truncated,
                "charset_used": charset_used,
                "charset_uncertain": charset_uncertain,
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
        # Erwartete Sicherheits-/Quellenfehler werden strukturiert gemeldet,
        # statt einen scheinbar belegten Text zu erzeugen.
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
