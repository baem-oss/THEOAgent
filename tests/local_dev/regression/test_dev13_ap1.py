"""AP1 integration regressions for the actual two-phase protocol; no live OWUI."""
import asyncio
import os
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev13.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

SP = "S" * 20916
manifest = "<available_skills><skill><id>homiletik</id></skill></available_skills>"
system = SP + "<attached_knowledge>inventory</attached_knowledge>" + manifest

def call(messages, outputs, tools=None):
    p = h.sg.Pipe()
    p.valves.AGENT_TEST_MODE = True
    p.valves.TARGET_MODEL_ID = "test-model"
    h._script["outputs"][:] = outputs
    h._script["prompts"].clear()
    result = asyncio.run(p.pipe({"model": "pipe", "messages": messages},
        __tools__=tools if tools is not None else h.FakeLibrary().tools(),
        __metadata__={"system_prompt": system}, __request__=object(), __user__={"id": "u1"}))
    return result, h._script["prompts"][:]

final = {"final": {"sources_sufficient": False}}
msgs = [{"role":"system","content":system},
        {"role":"user","content":"Was sagt Klippert? Nur Fachbibliothek."},
        {"role":"assistant","content":"Frühere Antwort."},
        {"role":"user","content":"Und zur Anwendung?"}]
result, prompts = call(msgs, [final])
assert SP in prompts[0][0]["content"]
assert manifest in prompts[0][0]["content"]
assert "<attached_knowledge>" not in prompts[0][0]["content"]
assert any("Klippert" in m["content"] for m in prompts[0] if m["role"]=="user")
print("AP1-01/04 PASS")

calls = []
async def skill(id):
    calls.append(id)
    return '{"name":"Homiletik","content":"Prüfe die Texttreue."}'

tools = h.FakeLibrary().tools(with_web=True)
tools["view_skill"] = {"callable":skill}
result, prompts = call(msgs, [{"actions":[{"tool":"view_skill","args":{"id":"homiletik"}}]}, final], tools)
assert calls == ["homiletik"]
assert any("Prüfe die Texttreue." in m["content"] for m in prompts[1])
assert "NICHT FREIGEGEBEN" in result and "Keine ausreichende Originallektüre" in result
print("AP1-02/03 PASS")

result, _ = call(msgs, [{"actions":[{"tool":"view_skill","args":{"id":"foreign"}}]}], tools)
assert "Skill-ID nicht im verfügbaren Skill-Inventar" in result and calls == ["homiletik"]
print("AP1-02 unauthorized skill PASS")

result, _ = call(msgs, [{"actions":[{"tool":"search_web","args":{"query":"Klippert"}}]}], tools)
assert "Websuche/Website-Abruf im LOCAL_ONLY-Modus verboten" in result
print("AP1-05 PASS")

r = h.run("Was sagt die Quelle?", tools,
    [{"final":{"answer":"Unbelegte Aussage [S1].","sources_sufficient":True}}]*2)
assert r["status"] == "NICHT FREIGEGEBEN"
print("AP1-06 missing evidence PASS")
