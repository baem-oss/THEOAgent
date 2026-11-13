"""
title: Outline Document Tools
author: BKurschatke (https://github.com/drsBK26)
version: 0.1.0
description: Analyze and search Outline-linked PDF, DOCX, XLSX and text documents from allowed HTTPS download hosts.
requirements: requests,pymupdf,python-docx,openpyxl
"""

import io
import ipaddress
import re
import socket
import zipfile
from typing import Optional
from urllib.parse import urlparse, urljoin

import requests
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        ALLOWED_HOSTS: str = Field(
            default="",
            description="Comma-separated exact HTTPS download hostnames, e.g. wiki.example.org,files.example.org. Required.",
        )
        MAX_DOWNLOAD_MB: int = Field(default=20, ge=1, le=100)
        MAX_EXTRACTED_CHARS: int = Field(default=250000, ge=1000, le=1000000)
        TIMEOUT_SECONDS: int = Field(default=25, ge=5, le=120)

    def __init__(self):
        self.valves = self.Valves()

    def _allowed(self, url: str) -> None:
        p = urlparse(url)
        hosts = {
            h.strip().lower().rstrip(".")
            for h in self.valves.ALLOWED_HOSTS.split(",")
            if h.strip()
        }
        if not hosts:
            raise ValueError(
                "ALLOWED_HOSTS is empty. Configure trusted Outline attachment hostnames in Tool Valves."
            )
        if (
            p.scheme != "https"
            or not p.hostname
            or p.username
            or p.password
            or p.port not in (None, 443)
        ):
            raise ValueError(
                "Only HTTPS URLs without embedded credentials or custom ports are supported."
            )
        host = p.hostname.lower().rstrip(".")
        if host not in hosts:
            raise ValueError(f"Download host is not on the allowlist: {host}")
        # This check reduces accidental SSRF, but DNS rebinding still requires network-level egress controls.
        for info in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM):
            addr = ipaddress.ip_address(info[4][0])
            if not addr.is_global:
                raise ValueError(
                    "Host resolves to a non-public IP address; blocked for safety."
                )

    def _download(self, url: str):
        self._allowed(url)
        limit = self.valves.MAX_DOWNLOAD_MB * 1024 * 1024
        session = requests.Session()
        session.trust_env = False
        current = url
        try:
            for _ in range(6):
                self._allowed(current)
                response = session.get(
                    current,
                    stream=True,
                    timeout=self.valves.TIMEOUT_SECONDS,
                    allow_redirects=False,
                    headers={"Accept": "application/pdf,application/octet-stream,*/*"},
                )
                if response.status_code in (301, 302, 303, 307, 308):
                    target = response.headers.get("Location")
                    response.close()
                    if not target:
                        raise ValueError("Redirect without Location")
                    current = urljoin(current, target)
                    continue
                response.raise_for_status()
                try:
                    if int(response.headers.get("Content-Length", "0")) > limit:
                        raise ValueError("Document exceeds configured download size")
                    content = bytearray()
                    for chunk in response.iter_content(65536):
                        content.extend(chunk)
                        if len(content) > limit:
                            raise ValueError(
                                "Document exceeds configured download size"
                            )
                    return bytes(content), response.headers.get("Content-Type", "")
                finally:
                    response.close()
            raise ValueError("Too many redirects")
        finally:
            session.close()

    def _extract(self, url: str):
        data, mime = self._download(url)
        path = urlparse(url).path.lower()
        pages = []
        info = {"bytes": len(data), "content_type": mime.split(";")[0]}
        if data.startswith(b"%PDF-"):
            import fitz

            with fitz.open(stream=data, filetype="pdf") as doc:
                info.update(type="pdf", pages=len(doc))
                for i, page in enumerate(doc):
                    pages.append((f"Seite {i+1}", page.get_text(sort=True)))
        elif zipfile.is_zipfile(io.BytesIO(data)) and (
            "word/" in "\n".join(zipfile.ZipFile(io.BytesIO(data)).namelist())
        ):
            from docx import Document

            d = Document(io.BytesIO(data))
            blocks = [p.text for p in d.paragraphs if p.text.strip()]
            for i, table in enumerate(d.tables, 1):
                blocks.append(f"[Tabelle {i}]")
                blocks += [" | ".join(c.text for c in row.cells) for row in table.rows]
            pages = [("Dokument", "\n".join(blocks))]
            info.update(type="docx", tables=len(d.tables))
        elif zipfile.is_zipfile(io.BytesIO(data)) and (
            "xl/" in "\n".join(zipfile.ZipFile(io.BytesIO(data)).namelist())
        ):
            from openpyxl import load_workbook

            wb = load_workbook(io.BytesIO(data), read_only=True, data_only=True)
            try:
                for ws in wb.worksheets:
                    lines = []
                    for row in ws.iter_rows(values_only=True):
                        lines.append(
                            " | ".join("" if v is None else str(v) for v in row)
                        )
                        if sum(map(len, lines)) > self.valves.MAX_EXTRACTED_CHARS:
                            break
                    pages.append((f"Tabelle: {ws.title}", "\n".join(lines)))
                info.update(type="xlsx", sheets=len(wb.worksheets))
            finally:
                wb.close()
        elif path.endswith((".txt", ".md", ".csv", ".json")) or mime.startswith(
            "text/"
        ):
            pages = [("Text", data.decode("utf-8-sig", errors="replace"))]
            info.update(type="text")
        else:
            raise ValueError(
                "Unsupported file format. Supported: PDF, DOCX, XLSX, TXT, MD, CSV, JSON. Scanned PDFs need OCR."
            )
        budget = self.valves.MAX_EXTRACTED_CHARS
        limited = []
        for label, body in pages:
            if budget <= 0:
                break
            limited.append((label, body[:budget]))
            budget -= len(body[:budget])
        info["extracted_characters"] = sum(len(t) for _, t in limited)
        info["truncated"] = sum(len(t) for _, t in pages) > info["extracted_characters"]
        return limited, info

    def analyze_document(
        self, url: str, question: str = "Fasse die wichtigsten Inhalte zusammen."
    ) -> str:
        """Read an Outline-linked document and return extracted text for analysis. Provide the complete signed attachment URL."""
        try:
            sections, info = self._extract(url)
            text = "\n\n".join(f"[{label}]\n{body}" for label, body in sections)
            return f"Dokumentdaten: {info}\nFrage: {question}\n\nExtrahierter Inhalt:\n{text}\n\nBitte beantworte die Frage ausschließlich anhand des Inhalts und nenne Fundstellen."
        except Exception as exc:
            return (
                f"Dokument konnte nicht analysiert werden: {type(exc).__name__}: {exc}"
            )

    def search_document(self, url: str, query: str, max_hits: int = 15) -> str:
        """Search for a word or phrase in an Outline-linked document, with page/sheet references."""
        if not query.strip():
            return "Bitte einen Suchbegriff angeben."
        try:
            sections, info = self._extract(url)
            hits = []
            for label, body in sections:
                for match in re.finditer(re.escape(query), body, re.IGNORECASE):
                    a, b = max(0, match.start() - 130), min(
                        len(body), match.end() + 180
                    )
                    hits.append(f'[{label}] ...{body[a:b].replace(chr(10), " ")}...')
                    if len(hits) >= max(1, min(max_hits, 50)):
                        break
                if len(hits) >= max(1, min(max_hits, 50)):
                    break
            return (
                f"Suche: {query}\nDokument: {info}\nTreffer (maximal {max_hits}): {len(hits)}\n"
                + ("\n\n".join(hits) if hits else "Keine Treffer im extrahierten Text.")
            )
        except Exception as exc:
            return f"Suche fehlgeschlagen: {type(exc).__name__}: {exc}"

    def document_info(self, url: str) -> str:
        """Get type, size, and page/sheet counts for an Outline-linked document."""
        try:
            _, info = self._extract(url)
            return str(info)
        except Exception as exc:
            return f"Dokumentinformationen nicht verfügbar: {type(exc).__name__}: {exc}"

    def extract_images(self, markdown: str) -> str:
        """Find image links in Outline Markdown and return Markdown image tags for chat rendering. Does not bypass browser authorization."""
        matches = re.findall(
            r'!\[([^\]]*)\]\((https://[^\s)]+)(?:\s+"[^"]*")?\)', markdown
        )
        result = []
        for alt, url in matches[:30]:
            try:
                self._allowed(url)
                result.append(f"![{alt}]({url})")
            except Exception:
                result.append(f'Bildreferenz nicht freigegeben: {alt or "ohne Titel"}')
        return (
            "\n\n".join(result) if result else "Keine Markdown-Bildreferenzen gefunden."
        )

    def analyze_outline_article(
        self,
        markdown: str,
        question: str = "Welche relevanten Informationen stehen im Artikel und seinen Anhängen?",
        max_attachments: int = 8,
    ) -> str:
        """Analyze an Outline article plus linked PDF/DOCX/XLSX/TXT attachments. Pass the Markdown returned by native Outline MCP; no manual URL copying needed. Call this after retrieving a matching Outline article."""
        from urllib.parse import unquote

        if not markdown.strip():
            return "Kein Artikelinhalt übergeben."
        # Standard Markdown links and image links; also supports bare HTTPS URLs.
        links = re.findall(
            r'!?\[[^\]]*\]\(<?(https://[^\s)>]+)>?(?:\s+"[^"]*")?\)', markdown
        )
        links += re.findall(r'(?<![\w(])https://[^\s<>"\']+', markdown)
        supported = (".pdf", ".docx", ".xlsx", ".txt", ".md", ".csv", ".json")
        unique = []
        for link in links:
            link = link.rstrip(".,;)")
            if link in unique:
                continue
            path = unquote(urlparse(link).path).lower()
            # Signed download endpoints may not have extensions. Include common attachment paths.
            if (
                path.endswith(supported)
                or "/attachments/" in path
                or "/api/attachments." in path
            ):
                unique.append(link)
        limit = max(1, min(int(max_attachments), 20))
        output = [
            f"Frage: {question}",
            "OUTLINE-ARTIKEL:",
            markdown[: self.valves.MAX_EXTRACTED_CHARS],
        ]
        budget = self.valves.MAX_EXTRACTED_CHARS
        output.append(
            f"\nErkannte Anhang-URLs: {len(unique)}; verarbeite maximal {limit}."
        )
        for idx, link in enumerate(unique[:limit], 1):
            try:
                sections, info = self._extract(link)
                extracted = "\n".join(f"[{label}] {body}" for label, body in sections)
                extracted = extracted[:budget]
                budget -= len(extracted)
                output.append(
                    f'\nANHANG {idx} ({info.get("type")}, {info.get("pages", info.get("sheets", "?"))} Seiten/Tabellen):\n{extracted}'
                )
                if budget <= 0:
                    output.append(
                        "Textbudget erreicht; weitere Anhänge nicht vollständig berücksichtigt."
                    )
                    break
            except Exception as exc:
                output.append(
                    f"\nANHANG {idx}: Nicht lesbar ({type(exc).__name__}: {exc})."
                )
        output.append(
            "\nBeantworte die Frage mit Artikel und erfolgreich gelesenen Anhängen. Nenne Dateiname und Seite/Tabelle. Weise auf nicht lesbare oder abgeschnittene Anhänge hin."
        )
        return "\n".join(output)