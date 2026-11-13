"""
title: Simple MediaWiki MCP Tool with Citations
author: Fedor
version: 1.5.0
requirements: requests
"""

import json
import re
import requests
from urllib.parse import quote, unquote, urlsplit, urlunsplit
from pydantic import BaseModel, Field


class UserSafeToolError(Exception):
    pass


def decode_response(response: requests.Response) -> str:
    return response.content.decode("utf-8", errors="replace")


def fix_mojibake(value):
    if value is None:
        return ""

    if not isinstance(value, str):
        value = str(value)

    if "Ã" not in value and "Â" not in value and "â" not in value:
        return value

    candidates = [value]

    try:
        candidates.append(value.encode("latin1").decode("utf-8"))
    except Exception:
        pass

    try:
        candidates.append(value.encode("cp1252").decode("utf-8"))
    except Exception:
        pass

    def score(s: str) -> int:
        return s.count("Ã") + s.count("Â") + s.count("â") + s.count("�")

    return min(candidates, key=score)


def normalize_text(value) -> str:
    value = fix_mojibake(value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"\n{4,}", "\n\n\n", value)
    return value.strip()


def normalize_title(value) -> str:
    value = normalize_text(value)

    if "%" in value:
        try:
            value = unquote(value)
        except Exception:
            pass

    return value.strip()


def normalize_url(url: str) -> str:
    url = normalize_text(url)

    if not url:
        return ""

    try:
        parts = urlsplit(url)

        if not parts.scheme or not parts.netloc:
            return url

        path = quote(unquote(parts.path), safe="/:@!$&'()*+,;=-._~%")
        query = quote(unquote(parts.query), safe="=&?/:@!$'()*+,;%-._~")
        fragment = quote(unquote(parts.fragment), safe=":@!$&'()*+,;=-._~%")

        return urlunsplit((parts.scheme, parts.netloc, path, query, fragment))
    except Exception:
        return url


def parse_mcp_sse_response(text: str) -> dict:
    text = normalize_text(text)

    if not text:
        raise UserSafeToolError("The MCP server returned an empty response.")

    if not text.startswith("event:") and not text.startswith("data:"):
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            print(
                f"[MediaWiki MCP Tool] JSON parse failed: {exc}; response={text[:1000]}"
            )
            raise UserSafeToolError("The MCP server returned an invalid JSON response.")

    data_lines = []

    for line in text.splitlines():
        if line.startswith("data:"):
            data_lines.append(line.removeprefix("data:").strip())

    if not data_lines:
        print(f"[MediaWiki MCP Tool] SSE response had no data lines: {text[:1000]}")
        raise UserSafeToolError(
            "The MCP server returned an unreadable streaming response."
        )

    try:
        return json.loads("\n".join(data_lines))
    except json.JSONDecodeError as exc:
        print(
            f"[MediaWiki MCP Tool] SSE JSON parse failed: {exc}; data={data_lines[:3]}"
        )
        raise UserSafeToolError("The MCP server returned malformed streaming JSON.")


def parse_mcp_response(response: requests.Response) -> dict:
    return parse_mcp_sse_response(decode_response(response))


def esc(value) -> str:
    return (
        normalize_text(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def get_text_from_mcp_result(parsed: dict) -> str:
    blocks = parsed.get("result", {}).get("content", [])
    texts = []

    if not isinstance(blocks, list):
        return ""

    for block in blocks:
        if isinstance(block, dict) and block.get("type") == "text":
            texts.append(normalize_text(block.get("text", "")))

    return "\n\n".join(t for t in texts if t).strip()


def extract_url_from_text(text: str) -> str:
    text = normalize_text(text)

    for line in text.splitlines():
        line = line.strip()

        for prefix in ["HTML URL:", "Page URL:", "URL:"]:
            if line.startswith(prefix):
                url = line[len(prefix) :].strip()
                if url.startswith(("http://", "https://")):
                    return normalize_url(url)

    match = re.search(r"https?://[^\s<>\]\"']+", text)
    if match:
        return normalize_url(match.group(0))

    return ""


class Tools:
    class Valves(BaseModel):
        MCP_URL: str = Field(default="http://mcp_mediawiki:8080/mcp")
        TIMEOUT: int = 30
        MAX_RESULTS: int = 5
        MAX_CHARS_PER_RESULT: int = 12000
        EMIT_STATUS: bool = True

    def __init__(self):
        self.valves = self.Valves()
        self.citation = False

    async def search_mediawiki(
        self,
        query1: str,
        query2: str = "",
        query3: str = "",
        __event_emitter__=None,
    ) -> str:
        """
        Search MediaWiki via MCP.

        Create up to 3 short keyword queries from the user's question.
        Prefer page-title words and main nouns. Omit filler words.
        """

        try:
            return await self._search_mediawiki_impl(
                query1=query1,
                query2=query2,
                query3=query3,
                __event_emitter__=__event_emitter__,
            )
        except UserSafeToolError as exc:
            await self._status(__event_emitter__, str(exc), done=True)
            return f"<CONTEXT>{esc(str(exc))}</CONTEXT>"
        except requests.Timeout:
            msg = "The MediaWiki MCP server did not respond in time."
            print("[MediaWiki MCP Tool] Request timed out")
            await self._status(__event_emitter__, msg, done=True)
            return f"<CONTEXT>{esc(msg)}</CONTEXT>"
        except requests.ConnectionError:
            msg = "The MediaWiki MCP server is not reachable."
            print("[MediaWiki MCP Tool] Connection error")
            await self._status(__event_emitter__, msg, done=True)
            return f"<CONTEXT>{esc(msg)}</CONTEXT>"
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else "unknown"
            msg = f"The MediaWiki MCP server returned an HTTP error ({status})."
            print(f"[MediaWiki MCP Tool] HTTP error: {exc}")
            await self._status(__event_emitter__, msg, done=True)
            return f"<CONTEXT>{esc(msg)}</CONTEXT>"
        except Exception as exc:
            msg = "The MediaWiki search failed due to an unexpected internal error."
            print(f"[MediaWiki MCP Tool] Unexpected error: {type(exc).__name__}: {exc}")
            await self._status(__event_emitter__, msg, done=True)
            return f"<CONTEXT>{esc(msg)}</CONTEXT>"

    async def _search_mediawiki_impl(
        self,
        query1: str,
        query2: str = "",
        query3: str = "",
        __event_emitter__=None,
    ) -> str:
        queries = []
        for q in [query1, query2, query3]:
            q = normalize_text(q)
            if q and q not in queries:
                queries.append(q)

        if not queries:
            raise UserSafeToolError("No MediaWiki search query was provided.")

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }

        await self._status(
            __event_emitter__, "Initializing MediaWiki MCP session.", done=False
        )

        init = requests.post(
            self.valves.MCP_URL,
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "open-webui-mediawiki-tool",
                        "version": "1.4.0",
                    },
                },
            },
            timeout=self.valves.TIMEOUT,
        )
        init.raise_for_status()

        session_id = init.headers.get("Mcp-Session-Id")
        if not session_id:
            print(
                "[MediaWiki MCP Tool] initialize returned no Mcp-Session-Id; "
                f"status={init.status_code}; body={decode_response(init)[:1000]}"
            )
            raise UserSafeToolError("The MCP server did not return a valid session ID.")

        headers["Mcp-Session-Id"] = session_id

        initialized = requests.post(
            self.valves.MCP_URL,
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "method": "notifications/initialized",
                "params": {},
            },
            timeout=self.valves.TIMEOUT,
        )
        initialized.raise_for_status()

        results = []
        seen = set()
        request_id = 2

        await self._status(__event_emitter__, "Searching MediaWiki pages.", done=False)

        for q in queries:
            search = requests.post(
                self.valves.MCP_URL,
                headers=headers,
                json={
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "method": "tools/call",
                    "params": {
                        "name": "search-page",
                        "arguments": {
                            "query": q,
                            "limit": self.valves.MAX_RESULTS,
                        },
                    },
                },
                timeout=self.valves.TIMEOUT,
            )
            request_id += 1
            search.raise_for_status()

            parsed = parse_mcp_response(search)

            found = (
                parsed.get("result", {}).get("structuredContent", {}).get("results", [])
            )

            if not isinstance(found, list):
                print(
                    f"[MediaWiki MCP Tool] Unexpected search result shape: {str(found)[:500]}"
                )
                continue

            for item in found:
                if not isinstance(item, dict):
                    continue

                title = normalize_title(item.get("title") or "")
                url = normalize_url(item.get("url") or item.get("pageUrl") or "")
                snippet = normalize_text(
                    item.get("snippet") or item.get("description") or ""
                )

                key = url or title
                if not key or key in seen:
                    continue

                seen.add(key)

                results.append(
                    {
                        "title": title,
                        "url": url,
                        "snippet": snippet,
                        "matched_query": q,
                        "raw": item,
                        "page_text": "",
                        "page_fetch_error": "",
                    }
                )

                if len(results) >= self.valves.MAX_RESULTS:
                    break

            if len(results) >= self.valves.MAX_RESULTS:
                break

        if not results:
            return (
                "<CONTEXT>\n"
                "No MediaWiki search results found.\n\n"
                "Tried queries:\n"
                + "\n".join(f"- {esc(q)}" for q in queries)
                + "\n</CONTEXT>"
            )

        await self._status(
            __event_emitter__, "Fetching full MediaWiki page contents.", done=False
        )

        for result in results:
            title = normalize_title(result["title"])
            if not title:
                continue

            try:
                get_page = requests.post(
                    self.valves.MCP_URL,
                    headers=headers,
                    json={
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "method": "tools/call",
                        "params": {
                            "name": "get-page",
                            "arguments": {
                                "title": title,
                                "content": "source",
                                "metadata": True,
                            },
                        },
                    },
                    timeout=self.valves.TIMEOUT,
                )
                request_id += 1
                get_page.raise_for_status()

                parsed_page = parse_mcp_response(get_page)
                page_text = normalize_text(get_text_from_mcp_result(parsed_page))

                if page_text:
                    result["page_text"] = page_text[: self.valves.MAX_CHARS_PER_RESULT]

                if not result["url"]:
                    maybe_url = extract_url_from_text(page_text)
                    if maybe_url:
                        result["url"] = maybe_url

            except requests.Timeout:
                result["page_fetch_error"] = "Page content request timed out."
                print(f"[MediaWiki MCP Tool] get-page timeout for title={title!r}")
            except requests.HTTPError as exc:
                status = (
                    exc.response.status_code if exc.response is not None else "unknown"
                )
                result["page_fetch_error"] = (
                    f"Page content could not be fetched (HTTP {status})."
                )
                print(
                    f"[MediaWiki MCP Tool] get-page HTTP error for title={title!r}: {exc}"
                )
            except Exception as exc:
                result["page_fetch_error"] = "Page content could not be fetched."
                print(
                    f"[MediaWiki MCP Tool] get-page failed for title={title!r}: {type(exc).__name__}: {exc}"
                )

        for index, result in enumerate(results, start=1):
            title = normalize_title(result["title"]) or f"MediaWiki result {index}"
            url = normalize_url(result["url"])

            content = (
                result["page_text"]
                or result["snippet"]
                or json.dumps(result["raw"], ensure_ascii=False, indent=2)
            )
            content = normalize_text(content)[: self.valves.MAX_CHARS_PER_RESULT]

            if __event_emitter__:
                try:
                    await __event_emitter__(
                        {
                            "type": "citation",
                            "data": {
                                "document": [url],
                                "metadata": [
                                    {
                                        "source": f"bja.wiki: {title}",
                                        "url": url,
                                        "matched_query": normalize_text(
                                            result["matched_query"]
                                        ),
                                    }
                                ],
                                "source": {
                                    "name": f"bja.wiki: {title}",
                                    "url": url,
                                },
                            },
                        }
                    )
                except Exception as exc:
                    print(
                        f"[MediaWiki MCP Tool] citation emission failed: {type(exc).__name__}: {exc}"
                    )

        parts = []

        for index, result in enumerate(results, start=1):
            content = (
                result["page_text"]
                or result["snippet"]
                or json.dumps(result["raw"], ensure_ascii=False, indent=2)
            )
            content = normalize_text(content)[: self.valves.MAX_CHARS_PER_RESULT]

            # excluded by HWA from block below
            # <SNIPPET>{esc(result["snippet"])}</SNIPPET>

            parts.append(f"""
<RESULT>
<ID>{index}</ID>
<TITLE>{esc(result["title"])}</TITLE>
<URL>{esc(result["url"])}</URL>
<MATCHED_QUERY>{esc(result["matched_query"])}</MATCHED_QUERY>
<PAGE_FETCH_ERROR>{esc(result.get("page_fetch_error", ""))}</PAGE_FETCH_ERROR>
<CONTENT>
{esc(content)}
</CONTENT>
</RESULT>
""".strip())

        await self._status(
            __event_emitter__, f"Loaded {len(results)} MediaWiki result(s).", done=True
        )

        return (
            "<CONTEXT>\n"
            + "\n\n".join(parts)
            + "\n</CONTEXT>\n\n"
            + "Use these MediaWiki page contents as sources. "
            + "Cite them with [1], [2], etc. according to the result ID."
        )

    async def _status(self, __event_emitter__, description: str, done: bool):
        if not __event_emitter__ or not self.valves.EMIT_STATUS:
            return

        try:
            await __event_emitter__(
                {
                    "type": "status",
                    "data": {
                        "description": description,
                        "done": done,
                        "hidden": False,
                    },
                }
            )
        except Exception as exc:
            print(
                f"[MediaWiki MCP Tool] status emission failed: {type(exc).__name__}: {exc}"
            )