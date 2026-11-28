"""
title: THEOAgent v2 – Native Tool Probe
version: 0.1.0
description: Isolated synthetic native tool-call round trip; no external tool or private data.
"""
import json
import secrets
import time
from typing import Any, Optional
from pydantic import BaseModel, Field

TOOL = {
    "type": "function",
    "function": {
        "name": "probe_nonce",
        "description": "Generate a fresh synthetic proof token. Call this to obtain the token.",
        "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
    },
}

def decode(raw):
    if isinstance(raw, dict):
        return raw
    return json.loads(raw.body)

async def run_probe(complete):
    trace = {"version": "0.1.0", "events": []}
    started = time.perf_counter()
    def finish(status, reason, answer=""):
        trace.update(status=status, reason=reason,
                     duration_ms=round((time.perf_counter()-started)*1000, 1))
        return answer + "\n\n```json\n" + json.dumps(trace, ensure_ascii=False, indent=2) + "\n```"
    try:
        messages = [
            {"role": "system", "content": "This is a synthetic interface test. Call probe_nonce exactly once using native tool calling. After the tool result, reply in ordinary text with the exact token returned. Do not invent a token."},
            {"role": "user", "content": "Obtain the proof token using the provided tool."},
        ]
        first = decode(await complete(messages, True))
        choice = first["choices"][0]
        msg = choice["message"]
        calls = msg.get("tool_calls") or []
        trace["events"].append({"event": "model_response_1", "finish_reason": choice.get("finish_reason"), "native_calls": len(calls)})
        if len(calls) != 1:
            return finish("FAIL", "Expected exactly one native tool call")
        call = calls[0]
        cid = call.get("id")
        fun = call.get("function") or {}
        if not isinstance(cid, str) or not cid or call.get("type") != "function" or fun.get("name") != "probe_nonce":
            return finish("FAIL", "Invalid native tool call")
        args = json.loads(fun.get("arguments", ""))
        if args != {}:
            return finish("FAIL", "Unexpected tool arguments")
        # Actual execution: token generated only here, after receiving native call.
        token = "SGV2-" + secrets.token_hex(12)
        trace["events"].append({"event": "tool_executed", "call_id": cid, "name": "probe_nonce", "token": token})
        messages = messages + [
            {"role": "assistant", "content": msg.get("content"), "tool_calls": calls},
            {"role": "tool", "tool_call_id": cid, "content": json.dumps({"token": token})},
        ]
        trace["events"].append({"event": "tool_result_submitted", "call_id": cid})
        second = decode(await complete(messages, False))
        choice = second["choices"][0]
        msg = choice["message"]
        answer = msg.get("content")
        matched = isinstance(answer, str) and token in answer
        trace["events"].append({"event": "model_response_2", "finish_reason": choice.get("finish_reason"), "token_match": matched, "native_calls": len(msg.get("tool_calls") or [])})
        ok = matched and not msg.get("tool_calls") and choice.get("finish_reason") == "stop"
        return finish("PASS" if ok else "FAIL", "Round trip complete" if ok else "Final response did not satisfy oracle", answer if isinstance(answer, str) else "")
    except Exception as exc:
        return finish("FAIL", "Exception: " + type(exc).__name__)

class Pipe:
    class Valves(BaseModel):
        TARGET_MODEL_ID: str = Field(default="google/gemma-4-31b-it", description="Exact existing OpenWebUI target model ID, not this Pipe")
    def __init__(self):
        self.valves = self.Valves()
    async def pipe(self, body: dict, __request__: Any = None, __user__: Optional[dict] = None) -> str:
        target = self.valves.TARGET_MODEL_ID.strip()
        if not target or target == body.get("model") or __request__ is None or not __user__ or not __user__.get("id"):
            return "PROBE FAIL: target or request context invalid"
        from open_webui.models.users import Users
        from open_webui.utils.chat import generate_chat_completion
        user = Users.get_user_by_id(__user__["id"])
        if hasattr(user, "__await__"):
            user = await user
        if user is None:
            return "PROBE FAIL: user unavailable"
        async def complete(messages, first):
            payload = {"model": target, "messages": messages, "stream": False, "tools": [TOOL], "tool_choice": "auto" if first else "none"}
            return await generate_chat_completion(__request__, payload, user)
        return await run_probe(complete)
