"""
title: TYPO3 Document Tools
author: BKurschatke (https://github.com/drsBK26)
version: 0.3.2
description: Analyze TYPO3 sys_file_reference attachments returned by vzorgaoauth_ReadTable.
requirements: requests, pymupdf, python-docx, openpyxl
"""

import io
import json
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
            description="Comma-separated exact HTTPS download hostnames, e.g. vzorga.drsintra.de, wiki.xyz.typo required.",
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
                "ALLOWED_HOSTS is empty. Configure trusted TYPO3 file hostnames in Tool Valves."
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

        # Erlaubt Loopback-Blockierung, lässt aber Intranet (drsintra) zu,
        # wenn der Host explizit in den Valves erlaubt wurde.
        for info in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM):
            addr = ipaddress.ip_address(info[4][0])
            if addr.is_loopback:
                raise ValueError(
                    "Host resolves to a loopback address; blocked for safety."
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
            # PyMuPDF-Import hier gekapselt
            import fitz

            with fitz.open(stream=data, filetype="pdf") as doc:
                info.update(type="pdf", pages=len(doc))
                for i, page in enumerate(doc):
                    pages.append((f"Seite {i+1}", page.get_text(sort=True)))

        elif zipfile.is_zipfile(io.BytesIO(data)) and (
            "word/" in "\n".join(zipfile.ZipFile(io.BytesIO(data)).namelist())
        ):
            # python-docx-Import hier gekapselt
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
            # openpyxl-Import hier gekapselt
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

    def analyze_typo3_files(
        self,
        records_json: str,
        question: str = "Fasse die Inhalte der TYPO3-Dateien zusammen.",
        query: str = "",
        max_files: int = 10,
        max_hits_per_file: int = 10,
    ) -> str:
        """Analyze or search TYPO3 sys_file_reference records returned by MCP ReadTable.

        Pass the JSON result of vzorgaoauth_ReadTable, including records and public_url.
        This tool does not call MCP itself; retrieve records with MCP first.
        """
        try:
            raw = records_json.strip()
            if raw.startswith("```"):
                raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.I)
            data = json.loads(raw)
            records = data.get("records", []) if isinstance(data, dict) else data
            if not isinstance(records, list):
                raise ValueError(
                    "Expected a JSON object with records array or a JSON array"
                )
            candidates = [
                r for r in records if isinstance(r, dict) and r.get("public_url")
            ]
            limit = max(1, min(int(max_files), 30))
            budget = self.valves.MAX_EXTRACTED_CHARS
            output = [
                f"Frage: {question}",
                f"Suchbegriff: {query or '(kein Filter)'}",
            ]

            # Hier wird die Iteration und Verarbeitung deiner Dokumente fortgesetzt...
            for item in candidates[:limit]:
                url = item.get("public_url")
                try:
                    content_segments, file_info = self._extract(url)
                    output.append(
                        f"\n--- Datei: {url} ({file_info.get('type', 'unbekannt')}) ---"
                    )
                    for title, text in content_segments:
                        output.append(f"[{title}]:\n{text}")
                except Exception as file_err:
                    output.append(f"\n--- Datei-Fehler ({url}): {str(file_err)} ---")

            return "\n".join(output)

        except Exception as e:
            return f"Fehler bei der JSON-Analyse: {str(e)}"
