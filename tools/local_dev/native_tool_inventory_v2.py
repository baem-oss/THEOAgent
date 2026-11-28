"""
title: THEOAgent v2 – Native Tool Inventory
version: 0.1.0
description: Local inspection of injected tool schemas. No model or tool execution.
"""
import json
from typing import Optional

NAMES = ("view_skill", "list_knowledge", "grep_knowledge_files",
         "query_knowledge_files", "view_knowledge_file", "search_web", "fetch_url")
SAFE_TYPES = {"object", "array", "string", "integer", "number", "boolean", "null"}

def schema_shape(spec):
    if not isinstance(spec, dict):
        return None
    if isinstance(spec.get("function"), dict):
        spec = spec["function"]
    params = spec.get("parameters")
    if not isinstance(params, dict):
        return {"parameters_present": False}
    props = params.get("properties")
    props = props if isinstance(props, dict) else {}
    # Only interface structure, never descriptions, defaults, examples or values.
    fields = {}
    for key, value in props.items():
        if not isinstance(key, str) or not key.isidentifier() or len(key) > 80:
            continue
        typ = value.get("type") if isinstance(value, dict) else None
        fields[key] = typ if isinstance(typ, str) and typ in SAFE_TYPES else "unspecified"
    required = params.get("required", [])
    return {"parameters_present": True, "fields": fields,
            "required": [x for x in required if isinstance(x, str) and x in fields] if isinstance(required, list) else []}

class Pipe:
    async def pipe(self, body: dict, __tools__: Optional[dict] = None,
                   __metadata__: Optional[dict] = None) -> str:
        tools = __tools__ if isinstance(__tools__, dict) else {}
        result = {"version": "0.1.0", "tool_count": len(tools), "tools": {},
                  "model_calls": 0, "tool_calls": 0}
        for name in NAMES:
            entry = tools.get(name)
            if not isinstance(entry, dict):
                result["tools"][name] = {"present": False}
                continue
            shape = {}
            for key in ("spec", "schema", "function", "tool"):
                if isinstance(entry.get(key), dict):
                    shape[key] = schema_shape(entry[key])
            result["tools"][name] = {"present": True,
                "callable": callable(entry.get("callable")),
                "schema_candidates": shape}
        result["status"] = "INVENTORY" if tools else "NO_TOOLS"
        return "```json\n" + json.dumps(result, ensure_ascii=False, indent=2) + "\n```"
