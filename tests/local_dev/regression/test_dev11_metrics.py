"""Metrics tests for the dev5-derived dev11 candidate; no live provider."""
import asyncio
import json
import os
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev11.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

lib = h.FakeLibrary()
result = h.run("Was steht in der Fachbibliothek?", lib.tools(), [
    {"actions":[{"tool":"list_knowledge","args":{}}]},
    {"final":{"answer":"Keine ausreichende Evidenz.","sources_sufficient":False}}
])
trace = result["metrics"]["trace"]
assert [e["kind"] for e in trace] == ["model","tool","model"]
assert trace[1]["name"] == "list_knowledge"
assert trace[1]["result_chars"] > 0
assert trace[0]["feedback_chars"] > 0
assert all(e["ms"] >= 0 for e in trace)
assert trace[2]["history_chars"] > trace[0]["history_chars"]
assert result["status"] == "NICHT FREIGEGEBEN"
print("DEV11 timing and sizes PASS")

async def broken(**kwargs):
    raise RuntimeError("PRIVATE_TEST_SENTINEL")
result = h.run("Was steht in der Fachbibliothek?", {"list_knowledge":{"callable":broken}}, [
    {"actions":[{"tool":"list_knowledge","args":{}}]},
    {"final":{"answer":"Keine Evidenz.","sources_sufficient":False}}
])
assert result["metrics"]["trace"][1]["status"] == "RuntimeError"
assert "PRIVATE_TEST_SENTINEL" not in json.dumps(result["metrics"])
print("DEV11 failure metadata PASS")

async def provider(request, payload, user):
    return {"choices":[{"message":{"content":'{"final":{"answer":"Keine Evidenz.","sources_sufficient":false}}'},
                        "finish_reason":"stop"}],
            "usage":{"prompt_tokens":123,"completion_tokens":21,"total_tokens":144}}
sys.modules["open_webui.utils.chat"].generate_chat_completion = provider
p = h.sg.Pipe()
p.valves.AGENT_TEST_MODE = True
p.valves.TARGET_MODEL_ID = "test-model"
p.valves.SHOW_TIMINGS = True
out = asyncio.run(p.pipe({"model":"pipe","messages":[{"role":"user","content":"Was steht in der Quelle?"}]},
    __tools__={}, __metadata__={}, __request__=object(), __user__={"id":"u1"}))
assert '"finish_reason":"stop"' in out and '"prompt_tokens":123' in out
assert '"completion_tokens":21' in out and '"total_tokens":144' in out
assert '"input_chars":' in out and '"output_chars":' in out
p.valves.SHOW_TIMINGS = False
out = asyncio.run(p.pipe({"model":"pipe","messages":[{"role":"user","content":"Was steht in der Quelle?"}]},
    __tools__={}, __metadata__={}, __request__=object(), __user__={"id":"u1"}))
assert "Provider:" not in out and "Messung:" not in out
print("DEV11 provider metadata and display switch PASS")

async def malformed(request, payload, user):
    return {"choices":[{"message":{"content":"{bad"},"finish_reason":"length"}]}
sys.modules["open_webui.utils.chat"].generate_chat_completion = malformed
p.valves.SHOW_TIMINGS = True
out = asyncio.run(p.pipe({"model":"pipe","messages":[{"role":"user","content":"Was steht in der Quelle?"}]},
    __tools__={}, __metadata__={}, __request__=object(), __user__={"id":"u1"}))
assert out.count('"finish_reason":"length"') == 2
assert '"prompt_tokens":null' in out
assert '"status":"ModelOutputError"' in out
assert "NICHT FREIGEGEBEN" in out
print("DEV11 malformed output and missing usage PASS")
