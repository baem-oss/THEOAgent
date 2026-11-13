"""
title: THEOAgent DRS:KI Tool Contract Probe
author: THEOAgent project
version: 0.1.0
description: DEV-only, read-only inventory of tools injected into an Open WebUI Pipe.
"""

from typing import Any, Optional
from pydantic import BaseModel, Field


REQUIRED = (
    "list_knowledge",
    "query_knowledge_files",
    "grep_knowledge_files",
    "view_knowledge_file",
    "search_web",
    "fetch_url",
)


def _parameter_names(entry: dict) -> list:
    """Expose names only; never expose defaults, descriptions, schema or secrets."""
    spec = entry.get("spec")
    if not isinstance(spec, dict):
        return []
    function = spec.get("function")
    if isinstance(function, dict):
        spec = function
    params = spec.get("parameters")
    if not isinstance(params, dict):
        return []
    props = params.get("properties")
    if not isinstance(props, dict):
        return []
    return sorted(str(key)[:100] for key in props if isinstance(key, str))[:40]


def _status(entry: Any) -> str:
    if not isinstance(entry, dict):
        return "ENTRY_INVALID"
    return "CALLABLE" if callable(entry.get("callable")) else "NOT_CALLABLE"


class Pipe:
    class Valves(BaseModel):
        SHOW_OTHER_NAMES: bool = Field(
            default=False,
            description="DEV only: display names of other injected tools (no content).",
        )

    def __init__(self):
        self.valves = self.Valves()

    async def pipe(self, body: dict, __tools__: Optional[dict] = None) -> str:
        """Pure inventory: no tool calls, network requests, model requests or body reads."""
        if __tools__ is None:
            return (
                "TOOL_CONTRACT_PROBE 0.1.0\n"
                "INJECTION: NONE\n"
                "No __tools__ dictionary was supplied. This is not proof that "
                "tools do not exist on the server."
            )
        if not isinstance(__tools__, dict):
            return "TOOL_CONTRACT_PROBE 0.1.0\nINJECTION: INVALID_TYPE"

        lines = [
            "TOOL_CONTRACT_PROBE 0.1.0",
            "INJECTION: DICT",
            f"TOTAL_ENTRIES: {len(__tools__)}",
            "REQUIRED_SOURCEGUARD_TOOLS:",
        ]
        for name in REQUIRED:
            if name not in __tools__:
                lines.append(f"- {name}: MISSING_FROM_INJECTION")
                continue
            entry = __tools__[name]
            lines.append(
                f"- {name}: {_status(entry)}; "
                f"PARAMETER_NAMES={_parameter_names(entry) if isinstance(entry, dict) else []}"
            )

        if self.valves.SHOW_OTHER_NAMES:
            others = sorted(
                name for name in __tools__
                if isinstance(name, str) and name not in REQUIRED
            )
            lines.append("OTHER_INJECTED_TOOL_NAMES (first 80):")
            for name in others[:80]:
                lines.append(f"- {name[:120]}: {_status(__tools__[name])}")
            if len(others) > 80:
                lines.append(f"- OMITTED_NAMES: {len(others) - 80}")
        else:
            lines.append("OTHER_NAMES: HIDDEN (enable SHOW_OTHER_NAMES on DEV if needed)")

        lines.append(
            "LIMITATION: This report proves registry injection only. It does not "
            "prove successful tool calls, original-text retrieval, tool access "
            "for end users, or SourceGuard compatibility."
        )
        return "\n".join(lines)
