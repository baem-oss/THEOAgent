"""
title: Single Domain Web Search Tool with Visible Status Events
author: Fedor
version: 2.0.1
"""

import asyncio
import html
import ipaddress
import json
import re
import socket
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field

from open_webui.models.users import Users
from open_webui.utils.chat import generate_chat_completion

BLOCKED_HOSTNAMES = {
    "localhost",
    "host.docker.internal",
    "searxng",
    "open-webui",
    "ollama",
    "litellm",
}

BLOCKED_EXACT_IPS = {
    ipaddress.ip_address("169.254.169.254"),
}

HTML_TAGS_TO_REMOVE = {
    "script",
    "style",
    "noscript",
    "svg",
    "header",
    "footer",
    "nav",
    "form",
    "iframe",
}

USEFUL_LINK_TOKENS = {
    ".pdf",
    "tabelle",
    "entgelt",
    "vergütung",
    "zulage",
    "anlage",
    "beschluss",
    "ordnung",
    "avo",
    "satzung",
    "richtlinie",
    "formular",
    "download",
}


class Tools:
    class Valves(BaseModel):
        SEARXNG_BASE_URL: str = Field(
            default="http://searxng:8080",
            description="SearXNG base URL.",
        )
        SEARCH_DOMAIN: str = Field(
            default="bibleserver.com",
            description="The only domain searched by this tool.",
        )
        LANGUAGE: str = Field(
            default="all",
            description="SearXNG language parameter.",
        )
        MAX_RESULTS_PER_ROUND: int = Field(
            default=8,
            description="Maximum fetched page results per evidence round.",
        )
        MAX_PAGE_CHARS: int = Field(
            default=7000,
            description="Maximum characters retained per fetched page.",
        )
        MAX_SEARCH_ROUNDS: int = Field(
            default=3,
            description="Maximum evidence rounds.",
        )
        REQUEST_TIMEOUT: int = Field(
            default=15,
            description="HTTP timeout in seconds.",
        )
        VERIFY_SSL: bool = Field(
            default=True,
            description="Verify SSL certificates.",
        )
        LLM_TEMPERATURE: float = Field(
            default=0.0,
            description="Temperature for the internal sufficiency-check model call.",
        )
        STATUS_AFTER_EACH_FETCH: bool = Field(
            default=True,
            description="Emit visible status after each fetched evidence URL.",
        )

    def __init__(self) -> None:
        self.valves = self.Valves()
        self.citation = False
        self.session = requests.Session()

    async def get_websearch_results(
        self,
        query: str = Field(
            ...,
            description="The user's question with the most important meaningful keywords.",
        ),
        __event_emitter__=None,
        __metadata__: Optional[Dict[str, Any]] = None,
        __model__: Optional[Dict[str, Any]] = None,
        __request__=None,
        __user__: Optional[Dict[str, Any]] = None,
    ) -> str:
        try:
            query = self._clean_text(query)
            domain = self._clean_domain(self.valves.SEARCH_DOMAIN)
            model_id = self._get_current_model_id(__model__, __metadata__)
            max_rounds = max(1, int(self.valves.MAX_SEARCH_ROUNDS))

            await self._emit_status(
                __event_emitter__,
                f"Starting restricted search on {domain}.",
            )

            seen_urls: Set[str] = set()
            all_rounds: List[List[Dict[str, Any]]] = []
            current_query = query
            query_history = f"Round 1 query: {query}"
            citation_index = 0
            llm_decision = self._empty_llm_decision(
                "No sufficiency check was needed or completed."
            )

            for round_no in range(1, max_rounds + 1):
                await self._emit_status(
                    __event_emitter__,
                    f"Running evidence round {round_no}/{max_rounds}.",
                )

                results = await self._search_and_fetch_round(
                    query=current_query,
                    domain=domain,
                    round_no=round_no,
                    seen_urls=seen_urls,
                    __event_emitter__=__event_emitter__,
                )

                if not results:
                    if round_no == 1:
                        await self._emit_status(
                            __event_emitter__,
                            "Search completed, but no relevant results were found.",
                            done=True,
                        )
                        return "No relevant results found."
                    break

                all_rounds.append(results)
                seen_urls.update(result["url"] for result in results)

                for result in results:
                    citation_index += 1
                    result["id"] = citation_index

                    if not __event_emitter__:
                        continue

                    title = (
                        result.get("title")
                        or result.get("url")
                        or f"Result {citation_index}"
                    )
                    url = result.get("url", "")
                    page_text = result.get("page_text", "")
                    snippet = result.get("snippet", "")
                    citation_text = page_text[:2000] or snippet or url

                    await __event_emitter__(
                        {
                            "type": "source",
                            "data": {
                                "document": [citation_text],
                                "metadata": [
                                    {
                                        "source": title,
                                        "title": title,
                                        "url": url,
                                        "date_accessed": result.get("date_accessed"),
                                    }
                                ],
                                "source": {
                                    "name": title,
                                    "url": url,
                                },
                            },
                        }
                    )
                    await asyncio.sleep(0)

                if round_no >= max_rounds:
                    break

                await self._emit_status(
                    __event_emitter__,
                    "Checking whether the collected evidence is sufficient.",
                )

                llm_decision = await self._llm_sufficiency_check(
                    user_query=query_history,
                    results=[item for group in all_rounds for item in group],
                    model_id=model_id,
                    __request__=__request__,
                    __user__=__user__,
                )

                if llm_decision["sufficient"]:
                    await self._emit_status(
                        __event_emitter__,
                        "Collected evidence is sufficient.",
                    )
                    break

                followup_query = self._clean_followup_query(
                    llm_decision.get("followup_query", "")
                )

                if not followup_query:
                    break

                current_query = followup_query
                query_history += f"\nRound {round_no + 1} query: {followup_query}"

            await self._emit_status(__event_emitter__, "Search completed.", done=True)

            return self._format_context(
                original_query=query,
                domain=domain,
                model_id=model_id,
                llm_decision=llm_decision,
                round_results=all_rounds,
            )

        except Exception as exc:
            safe_error = self._safe_error(exc)
            await self._emit_status(
                __event_emitter__,
                f"Search failed: {safe_error}",
                done=True,
                error=True,
            )
            return f"Web search error: {safe_error}"

    async def _search_and_fetch_round(
        self,
        query: str,
        domain: str,
        round_no: int,
        seen_urls: Set[str],
        __event_emitter__,
    ) -> List[Dict[str, Any]]:
        search_query = self._site_query(query, domain)

        await self._emit_status(
            __event_emitter__,
            f"Searching SearXNG for round {round_no}.",
        )

        max_results = max(1, int(self.valves.MAX_RESULTS_PER_ROUND))
        raw_results = await asyncio.to_thread(
            self._search_raw,
            search_query,
            max_results * 2,
        )

        results: List[Dict[str, Any]] = []

        for item in raw_results:
            if len(results) >= max_results:
                break

            url = self._clean_text(item.get("url", ""))

            if not url or url in seen_urls:
                continue

            if not self._url_belongs_to_domain(url, domain):
                continue

            if not await asyncio.to_thread(self._is_safe_fetch_url, url):
                continue

            await self._emit_status(
                __event_emitter__,
                f"Fetching result {len(results) + 1}/{max_results}: {self._host_label(url)}",
            )

            page_text, outgoing_links = await asyncio.to_thread(
                self._fetch_page_text_and_links,
                url,
            )

            results.append(
                {
                    "id": None,
                    "round": round_no,
                    "search_query": search_query,
                    "title": self._clean_text(item.get("title", "")),
                    "url": url,
                    "snippet": self._clean_text(item.get("content", "")),
                    "page_text": page_text,
                    "links": outgoing_links,
                    "date_accessed": datetime.now().isoformat(timespec="seconds"),
                }
            )

            if self.valves.STATUS_AFTER_EACH_FETCH:
                await self._emit_status(
                    __event_emitter__,
                    f"Fetched {len(results)}/{max_results} results for round {round_no}.",
                )

        return results

    def _search_raw(self, search_query: str, result_limit: int) -> List[Dict[str, Any]]:
        response = self.session.get(
            f"{self.valves.SEARXNG_BASE_URL.rstrip('/')}/search",
            params={
                "q": search_query,
                "format": "json",
                "language": self.valves.LANGUAGE,
            },
            timeout=self.valves.REQUEST_TIMEOUT,
            verify=self.valves.VERIFY_SSL,
        )
        response.raise_for_status()

        results = response.json().get("results", [])

        if not isinstance(results, list):
            return []

        return results[: max(0, int(result_limit))]

    def _fetch_page_text_and_links(self, url: str) -> Tuple[str, List[Dict[str, str]]]:
        try:
            if not self._is_safe_fetch_url(url):
                return "[URL blocked by safety policy.]", []

            response = self.session.get(
                url,
                timeout=self.valves.REQUEST_TIMEOUT,
                verify=self.valves.VERIFY_SSL,
                headers={
                    "User-Agent": "Mozilla/5.0 OpenWebUI-WebSearch-Tool/1.0",
                    "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.8",
                },
                allow_redirects=True,
            )
            response.raise_for_status()

            final_url = response.url or url

            if not self._is_safe_fetch_url(final_url):
                return "[Redirect blocked by safety policy.]", []

            content_type = response.headers.get("content-type", "").lower()

            if "application/pdf" in content_type or final_url.lower().endswith(".pdf"):
                return self._extract_pdf_text(response.content), []

            soup = BeautifulSoup(response.text, "html.parser")

            for tag in soup(HTML_TAGS_TO_REMOVE):
                tag.extract()

            links = self._extract_links(soup, final_url)
            text = self._clean_text(html.unescape(soup.get_text(separator="\n")))

            return text[: self.valves.MAX_PAGE_CHARS], links

        except Exception as exc:
            return f"[ERROR fetching page: {self._safe_error(exc)}]", []

    def _extract_pdf_text(self, content: bytes) -> str:
        try:
            from io import BytesIO
            from pypdf import PdfReader

            reader = PdfReader(BytesIO(content))
            text = "\n".join(page.extract_text() or "" for page in reader.pages[:10])
            return self._clean_text(text)[: self.valves.MAX_PAGE_CHARS]

        except ImportError:
            return "[PDF detected but pypdf is not installed.]"
        except Exception as exc:
            return f"[ERROR extracting PDF text: {self._safe_error(exc)}]"

    def _extract_links(
        self,
        soup: BeautifulSoup,
        base_url: str,
    ) -> List[Dict[str, str]]:
        links: List[Dict[str, str]] = []
        seen: Set[str] = set()

        for anchor in soup.find_all("a", href=True):
            href = urljoin(base_url, anchor["href"])
            text = self._clean_text(anchor.get_text(" ", strip=True))

            if not href or not text or href in seen:
                continue

            if not self._is_safe_fetch_url(href):
                continue

            if not any(
                token in f"{text} {href}".lower() for token in USEFUL_LINK_TOKENS
            ):
                continue

            seen.add(href)
            links.append({"text": text[:200], "url": href})

            if len(links) >= 30:
                break

        return links

    def _is_safe_fetch_url(self, url: str) -> bool:
        try:
            parsed = urlparse(url)

            if parsed.scheme not in {"http", "https"}:
                return False

            if parsed.username or parsed.password:
                return False

            hostname = parsed.hostname

            if not hostname:
                return False

            host = hostname.rstrip(".").lower()

            if host in BLOCKED_HOSTNAMES:
                return False

            for info in socket.getaddrinfo(host, None):
                ip = ipaddress.ip_address(info[4][0])

                if ip in BLOCKED_EXACT_IPS:
                    return False

                if (
                    ip.is_private
                    or ip.is_loopback
                    or ip.is_link_local
                    or ip.is_multicast
                    or ip.is_reserved
                    or ip.is_unspecified
                ):
                    return False

            return True

        except Exception:
            return False

    async def _llm_sufficiency_check(
        self,
        user_query: str,
        results: List[Dict[str, Any]],
        model_id: str,
        __request__,
        __user__: Optional[Dict[str, Any]],
    ) -> Dict[str, Any]:
        try:
            if not __request__ or not __user__ or not __user__.get("id"):
                return self._empty_llm_decision(
                    "Open WebUI request or user context was missing."
                )

            user = await Users.get_user_by_id(__user__["id"])
            context = self._format_compact_context_for_llm(results)

            response = await generate_chat_completion(
                __request__,
                {
                    "model": model_id,
                    "messages": [
                        {
                            "role": "system",
                            "content": self._sufficiency_system_prompt(),
                        },
                        {
                            "role": "user",
                            "content": f"""
USER QUESTION:
{user_query}

SEARCH RESULTS:
{context}
""".strip(),
                        },
                    ],
                    "temperature": self.valves.LLM_TEMPERATURE,
                    "stream": False,
                },
                user,
            )

            parsed = self._parse_json_object(self._extract_completion_text(response))

            return {
                "sufficient": bool(parsed.get("sufficient", False)),
                "reason": str(parsed.get("reason", "")),
                "needed_evidence": str(parsed.get("needed_evidence", "")),
                "followup_query": str(parsed.get("followup_query", "")),
            }

        except Exception as exc:
            return {
                "sufficient": False,
                "reason": f"LLM sufficiency check failed: {type(exc).__name__}",
                "needed_evidence": "Unknown",
                "followup_query": self._heuristic_followup_query(user_query, results),
            }

    def _extract_completion_text(self, response: Any) -> str:
        if not isinstance(response, dict):
            body = getattr(response, "body", None)

            if isinstance(body, bytes):
                response = json.loads(body.decode("utf-8", errors="replace"))
            elif isinstance(body, str):
                response = json.loads(body)
            elif hasattr(response, "json"):
                response = response.json()

        if not isinstance(response, dict):
            raise ValueError("Unsupported completion response type.")

        return response.get("choices", [{}])[0].get("message", {}).get("content", "")

    def _sufficiency_system_prompt(self) -> str:
        return f"""
Today is {datetime.now().strftime("%d %b %Y")}.

Decide whether the provided search results contain enough exact evidence to answer the user's question.

Return strict JSON only:
{{
  "sufficient": true | false,
  "reason": "short reason",
  "needed_evidence": "what exact data is missing, if any",
  "followup_query": "one improved search query without site: prefix"
}}

Rules:
- Mark sufficient=true only if the results contain the exact answer data requested by the user.
- If the user asks for amounts, salaries, allowances, tables, levels, dates, or percentages, exact numeric values must be present.
- If the results only point to a document/table but values are absent, sufficient=false.
- Build followup_query from concrete hints in titles, snippets, excerpts, and useful links.
- Keep followup_query short and specific.
""".strip()

    def _heuristic_followup_query(
        self,
        user_query: str,
        results: List[Dict[str, Any]],
    ) -> str:
        hints: List[str] = []

        for result in results:
            hints.extend(
                [
                    result.get("title", ""),
                    result.get("snippet", ""),
                ]
            )

            for link in result.get("links", [])[:10]:
                hints.extend([link.get("text", ""), link.get("url", "")])

        text = self._clean_text(" ".join(hints))

        phrases = re.findall(
            r"(Anlage\s+\d+[a-zA-Z]?|Tabelle\s+[A-Za-z0-9 ._-]+|§\s*\d+[a-zA-Z]?|AVO[- ]?DRS[- ]?Ordnung)",
            text,
            flags=re.IGNORECASE,
        )

        return self._clean_text(
            f"{user_query} Entgelt Vergütung Zulage Betrag Tabelle Anlage {' '.join(phrases[:5])}"
        )[:300]

    def _format_compact_context_for_llm(self, results: List[Dict[str, Any]]) -> str:
        parts: List[str] = []

        for index, result in enumerate(results, start=1):
            links = "\n".join(
                f"- {link.get('text', '')} | {link.get('url', '')}"
                for link in result.get("links", [])[:15]
            )

            parts.append(f"""
RESULT {index}
TITLE: {result.get("title", "")}
URL: {result.get("url", "")}
SNIPPET: {result.get("snippet", "")}

USEFUL LINKS:
{links}

PAGE EXCERPT:
{result.get("page_text", "")[:2500]}
""".strip())

        return "\n\n".join(parts)

    def _format_context(
        self,
        original_query: str,
        domain: str,
        model_id: str,
        llm_decision: Dict[str, Any],
        round_results: List[List[Dict[str, Any]]],
    ) -> str:
        all_results = [result for group in round_results for result in group]
        results_text = "\n".join(self._format_result(result) for result in all_results)

        return f"""
<ANSWERING_INSTRUCTIONS>
Use PAGE_CONTENT and SNIPPET to answer.
Use RESULT ID values for citations.
Answer directly when exact values are present.
If exact values are absent, say that the retrieved sources only point to the relevant source.
Do not invent values.
</ANSWERING_INSTRUCTIONS>

<SEARCH_METADATA>
<ORIGINAL_QUERY>{self._xml_escape(original_query)}</ORIGINAL_QUERY>
<SEARCH_DOMAIN>{self._xml_escape(domain)}</SEARCH_DOMAIN>
<MODEL_ID>{self._xml_escape(model_id)}</MODEL_ID>
<ROUNDS_EXECUTED>{self._xml_escape(len(round_results))}</ROUNDS_EXECUTED>
<LLM_SUFFICIENT>{self._xml_escape(llm_decision.get("sufficient"))}</LLM_SUFFICIENT>
<LLM_REASON>{self._xml_escape(llm_decision.get("reason"))}</LLM_REASON>
<LLM_NEEDED_EVIDENCE>{self._xml_escape(llm_decision.get("needed_evidence"))}</LLM_NEEDED_EVIDENCE>
<LLM_FOLLOWUP_QUERY>{self._xml_escape(llm_decision.get("followup_query"))}</LLM_FOLLOWUP_QUERY>
</SEARCH_METADATA>

{results_text}
""".strip()

    def _format_result(self, result: Dict[str, Any]) -> str:
        links = "\n".join(
            (
                "<LINK>"
                f"<TEXT>{self._xml_escape(link.get('text'))}</TEXT>"
                f"<URL>{self._xml_escape(link.get('url'))}</URL>"
                "</LINK>"
            )
            for link in result.get("links", [])[:20]
        )

        return f"""
<RESULT>
<ID>{self._xml_escape(result.get("id"))}</ID>
<ROUND>{self._xml_escape(result.get("round"))}</ROUND>
<TITLE>{self._xml_escape(result.get("title"))}</TITLE>
<URL>{self._xml_escape(result.get("url"))}</URL>
<SNIPPET>{self._xml_escape(result.get("snippet"))}</SNIPPET>
<SEARCH_QUERY>{self._xml_escape(result.get("search_query"))}</SEARCH_QUERY>
<DATE_ACCESSED>{self._xml_escape(result.get("date_accessed"))}</DATE_ACCESSED>
<USEFUL_LINKS_ON_PAGE>{links}</USEFUL_LINKS_ON_PAGE>
<PAGE_CONTENT>{self._xml_escape(result.get("page_text"))}</PAGE_CONTENT>
</RESULT>
""".strip()

    async def _emit_status(
        self,
        __event_emitter__,
        description: str,
        done: bool = False,
        error: bool = False,
    ) -> None:
        if not __event_emitter__:
            return

        data = {
            "description": description,
            "done": done,
            "hidden": False,
        }

        if error:
            data["status"] = "error"

        await __event_emitter__({"type": "status", "data": data})
        await asyncio.sleep(0)

    def _site_query(self, query: str, domain: str) -> str:
        return (
            f"site:{domain} {self._clean_text(query)} Einheitsübersetzung 2016".strip()
        )

    def _clean_domain(self, domain: str) -> str:
        clean = (
            str(domain)
            .strip()
            .removeprefix("https://")
            .removeprefix("http://")
            .strip("/")
            .lower()
        )

        if not clean:
            raise ValueError("SEARCH_DOMAIN must not be empty.")

        return clean

    def _url_belongs_to_domain(self, url: str, domain: str) -> bool:
        host = (urlparse(url).hostname or "").rstrip(".").lower()
        return host == domain or host.endswith(f".{domain}")

    def _get_current_model_id(
        self,
        __model__: Optional[Dict[str, Any]],
        __metadata__: Optional[Dict[str, Any]],
    ) -> str:
        for source, keys in (
            (__model__, ("id", "model", "base_model_id")),
            (__metadata__, ("model_id", "model")),
        ):
            if not isinstance(source, dict):
                continue

            for key in keys:
                value = source.get(key)

                if isinstance(value, str) and value.strip():
                    return value.strip()

        raise ValueError("Could not resolve current Open WebUI model ID.")

    def _parse_json_object(self, text: str) -> Dict[str, Any]:
        text = self._clean_text(text)
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()

        try:
            parsed = json.loads(text)
        except Exception:
            match = re.search(r"\{.*\}", text, flags=re.DOTALL)

            if not match:
                raise ValueError("No JSON object found in model response.")

            parsed = json.loads(match.group(0))

        if not isinstance(parsed, dict):
            raise ValueError("Model response JSON is not an object.")

        return parsed

    def _clean_followup_query(self, query: str) -> str:
        query = self._clean_text(query)
        query = re.sub(r"\bsite:\S+", "", query).strip()
        return query.strip('"').strip("'").strip()[:300]

    def _clean_text(self, text: Any) -> str:
        if text is None:
            return ""

        cleaned = html.unescape(str(text)).replace("\xa0", " ")
        cleaned = re.sub(r"[ \t]+", " ", cleaned)
        cleaned = re.sub(r"\n\s*\n\s*\n+", "\n\n", cleaned)
        cleaned = re.sub(r"[ \t]*\n[ \t]*", "\n", cleaned)

        return cleaned.strip()

    def _xml_escape(self, value: Any) -> str:
        return html.escape(str(value or ""), quote=False)

    def _safe_error(self, error: Exception) -> str:
        message = str(error) or type(error).__name__
        message = re.sub(r"https?://[^@\s]+@", "https://***:***@", message)
        message = re.sub(r"/[A-Za-z0-9._~:/-]+", "[path]", message)
        return message[:300]

    def _empty_llm_decision(self, reason: str) -> Dict[str, Any]:
        return {
            "sufficient": False,
            "reason": reason,
            "needed_evidence": "Unknown",
            "followup_query": "",
        }

    def _host_label(self, url: str) -> str:
        return urlparse(url).hostname or url[:80]