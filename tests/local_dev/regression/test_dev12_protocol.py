"""Test the actual dev12 two-phase Pipe path using the existing OWUI stubs."""
import asyncio
import json
import os
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

WORK = {"title":"Vom Text zur Predigt","author":"Wolfgang Klippert"}
LIST = {"actions":[{"tool":"list_knowledge","args":{}}]}
VIEW = {"actions":[{"tool":"view_knowledge_file","args":{
    "file_id":"f-klip","start_line":800,"end_line":840,
    "anchor_line":802,"work":WORK}}]}
READY = {"final":{"sources_sufficient":True,"work":WORK}}
Q = "Was fordert Wolfgang Klippert in seinem Originalwerk für die Predigt?"

def call(outputs, question=Q):
    queue = list(outputs)
    payloads = []
    async def provider(request, payload, user):
        payloads.append(payload)
        out = queue.pop(0)
        reason = "stop"
        if isinstance(out,tuple):
            out,reason = out
        return {"choices":[{"message":{"content":out if isinstance(out,str) else json.dumps(out)},
                            "finish_reason":reason}]}
    sys.modules["open_webui.utils.chat"].generate_chat_completion = provider
    p = h.sg.Pipe()
    p.valves.AGENT_TEST_MODE = True
    p.valves.SHOW_TIMINGS = True
    p.valves.TARGET_MODEL_ID = "test-model"
    out = asyncio.run(p.pipe({"model":"pipe","messages":[{"role":"user","content":question}]},
        __tools__=h.FakeLibrary().tools(), __metadata__={}, __request__=object(), __user__={"id":"u1"}))
    return out,payloads

out,p = call([LIST,VIEW,READY,"Die Predigt folgt der Struktur des Textes [S1]."])
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out, out
assert [x["max_tokens"] for x in p] == [1024,1024,1024,4096]
assert "Markdown" in p[-1]["messages"][0]["content"]
assert '"phase":"answer"' in out
assert "Tatsächlich gelesene Originalstellen:" in out
print("DEV12 research/Markdown integration PASS")

out,p = call([READY])
assert "NICHT FREIGEGEBEN" in out and len(p)==1
print("DEV12 no evidence, no composition PASS")

out,p = call([(LIST,"length"),LIST,VIEW,READY,"Die Predigt folgt dem Text [S1]."])
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out, out
assert '"finish_reason":"length"' in out
assert len(p)==5
print("DEV12 bounded control retry PASS")

out,p = call([(LIST,"length"),(LIST,"length")])
assert "NICHT FREIGEGEBEN" in out and len(p)==2
print("DEV12 repeated truncation fails closed PASS")

out,p = call([LIST,VIEW,READY,("Die Predigt folgt dem Text [S1].","length")])
assert "NICHT FREIGEGEBEN" in out and "Markdown-Antwort am Tokenlimit" in out
print("DEV12 truncated Markdown blocked PASS")

out,p = call([LIST,VIEW,READY,"Die Predigt folgt dem Text [S99].",
              READY,"Die Predigt folgt dem Text [S99]."])
assert "NICHT FREIGEGEBEN" in out and "S99" in out
print("DEV12 unknown citation blocked PASS")

out,p = call([{"final":{"answer":"invalid","sources_sufficient":True}}]*2)
assert "NICHT FREIGEGEBEN" in out and len(p)==2
print("DEV12 rejects old wire format PASS")
