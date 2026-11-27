"""Test the actual dev14 two-phase Pipe path using the existing OWUI stubs."""
import asyncio
import json
import os
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev14.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

WORK = {"title":"Vom Text zur Predigt","author":"Wolfgang Klippert"}
LIST = {"actions":[{"tool":"list_knowledge","args":{}}]}
VIEW = {"actions":[{"tool":"view_knowledge_file","args":{
    "file_id":"f-klip","start_line":800,"end_line":840,
    "anchor_line":802,"work":WORK}}]}
READY = {"final":{"sources_sufficient":True,"work":WORK}}
Q = "Was fordert Wolfgang Klippert in seinem Originalwerk für die Predigt? Belege deine Aussagen mit konkreten Originalstellen."

def call(outputs, question=Q, messages=None, usage=True):
    queue = list(outputs)
    payloads = []
    async def provider(request, payload, user):
        payloads.append(payload)
        out = queue.pop(0)
        reason = "stop"
        if isinstance(out,tuple):
            out,reason = out
        response={"choices":[{"message":{"content":out if isinstance(out,str) else json.dumps(out)},
                            "finish_reason":reason}]}
        if usage:
            response["usage"]={"prompt_tokens":123,"completion_tokens":12,"total_tokens":135}
        return response
    sys.modules["open_webui.utils.chat"].generate_chat_completion = provider
    p = h.sg.Pipe()
    p.valves.AGENT_TEST_MODE = True
    p.valves.SHOW_TIMINGS = True
    p.valves.TARGET_MODEL_ID = "test-model"
    out = asyncio.run(p.pipe({"model":"pipe","messages":messages or [{"role":"user","content":question}]},
        __tools__=h.FakeLibrary().tools(), __metadata__={}, __request__=object(), __user__={"id":"u1"}))
    return out,payloads

out,p = call([LIST,VIEW,READY,"Die Predigt folgt der Struktur des Textes [S1]."])
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out, out
assert [x["max_tokens"] for x in p] == [1024,1024,1024,4096]
assert any(m["role"] == "system" and "Fachantwort als Markdown" in m["content"]
           for m in p[-1]["messages"]), "Missing Markdown system instruction"
assert not any(m["role"] == "system" and "Sobald die Recherche ausreicht" in m["content"]
               for m in p[-1]["messages"]), "Conflicting control instruction in answer phase"
assert '"phase":"answer"' in out
assert "Tatsächlich gelesene Originalstellen:" in out
print("DEV14 research/Markdown integration PASS")

out,p = call([READY])
assert "NICHT FREIGEGEBEN" in out and len(p)==1
print("DEV14 no evidence, no composition PASS")

out,p = call([(LIST,"length"),LIST,VIEW,READY,"Die Predigt folgt dem Text [S1]."])
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out, out
assert '"finish_reason":"length"' in out
assert len(p)==5
print("DEV14 bounded control retry PASS")

out,p = call([(LIST,"length"),(LIST,"length")])
assert "NICHT FREIGEGEBEN" in out and len(p)==2
print("DEV14 repeated truncation fails closed PASS")

out,p = call([LIST,VIEW,READY,("Die Predigt folgt dem Text [S1].","length")])
assert "NICHT FREIGEGEBEN" in out and "Markdown-Antwort am Tokenlimit" in out
print("DEV14 truncated Markdown blocked PASS")

out,p = call([LIST,VIEW,READY,"Die Predigt folgt dem Text [S99].",
              READY,"Die Predigt folgt dem Text [S99]."])
assert "NICHT FREIGEGEBEN" in out and "S99" in out
print("DEV14 unknown citation blocked PASS")

out,p = call([{"final":{"answer":"invalid","sources_sufficient":True}}]*2)
assert "NICHT FREIGEGEBEN" in out and len(p)==2
print("DEV14 rejects old wire format PASS")

# Two independent format incidents: a valid tool round resets the retry budget.
out,p = call([(LIST,"length"),LIST,VIEW,"Prosa in der Steuerungsphase",
              READY,"Die Predigt folgt dem Text [S1]."])
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out, out
assert len(p)==6 and all(x["max_tokens"]==1024 for x in p[:-1])
assert all("STEUERUNGSPHASE" in x["messages"][-1]["content"] for x in p[:-1])
assert not any("Agenten-JSON-Schnittstelle" in m["content"] for m in p[-1]["messages"] if m["role"]=="system")
print("DEV14 independent incidents and phase isolation PASS")

# Negative cases must fail at the intended gate, not via an exhausted stub queue.
for ans, reason in [
    ("A [S1]. B [S1/Extrakt 1668].","Nichtkanonische Quellenkennung"),
    ("A [S1]. B [S1, S99].","Nicht gelesene Quellenkennung"),
    ("Nach Zeile 1668 folgt die Predigt dem Text [S1].","Technische Zeilen- und Seitenlokatoren"),
    ('Klippert schreibt: „Die Predigt ist eine Plauderei über das Wetter der Woche.“ [S1]',"Originalzitat stimmt nicht"),
]:
    out,p=call([LIST,VIEW,READY,ans,READY,ans])
    assert "NICHT FREIGEGEBEN" in out and reason in out and len(p)==6, out
    assert "IndexError" not in out
print("DEV14 citation, locator and literal quote rejection PASS")

out,p=call([LIST,VIEW,READY,"A [S1, S1]."])
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out and "- [S1]" in out
print("DEV14 grouped citations PASS")

for meta,reason in [
    (dict(READY["final"],works={"S7":WORK}),"in works"),
]:
    out,p=call([LIST,VIEW,{"final":meta},"A [S1].",{"final":meta},"A [S1]."])
    assert "NICHT FREIGEGEBEN" in out and reason in out and len(p)==6,out
print("DEV14 metadata validation PASS")

first,p=call([LIST,VIEW,READY,"## Anforderungen\nDie Predigt folgt dem Text [S1]."])
history=[{"role":"user","content":Q+" Nur Fachbibliothek."},
         {"role":"assistant","content":first.replace("[S1].","[S1/Extrakt 1668].")+"X"*14000},
         {"role":"user","content":"Und was sagt er zur Anwendung?"}]
out,p=call([LIST,VIEW,READY,"Die Anwendung bleibt textgebunden [S1]."],messages=history)
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out,out
assert "LOCAL_ONLY: aktiv (auch aus Verlauf)" in out
ctx=p[0]["messages"]
assert not any(m["role"]=="assistant" for m in ctx)
historical=next(m["content"] for m in ctx if m["content"].startswith("Bisheriger Gesprächsverlauf"))
assert len(historical)<=12200 and "Klippert" in historical
assert "DIAGNOSE" not in historical and "Messung:" not in historical and "[S1" not in historical and "Extrakt 1668" not in historical
print("DEV14 history sanitation and local-only continuity PASS")

out,p=call([LIST,VIEW,READY,("Die Predigt folgt dem Text [S1].",None)],usage=False)
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out and "finish_reason fehlt" in out,out
assert '"prompt_tokens":null' in out
print("DEV14 missing provider metadata PASS")

# PO decision: evidence remains mandatory; presentation is independent.
NORMAL = "Was fordert Wolfgang Klippert in seinem Originalwerk für die Predigt?"
for text in ("Die Predigt folgt dem Text.", "Die Predigt folgt dem Text [S1]."):
    out,p=call([LIST,VIEW,READY,text],question=NORMAL)
    body=out.split(" – DIAGNOSE:")[0]
    assert "FREIGEGEBEN" in out and "Tatsächlich gelesene Originalstellen:" not in body and "[S1]" not in body,out
    assert len(p)==4
print("DEV14 evidence without mandatory presentation PASS")

for coverage in (None, "unbrauchbar", {"Anwendung":"S1"}, {"Anwendung":["S7"]}):
    meta=dict(READY["final"],coverage=coverage)
    out,p=call([LIST,VIEW,{"final":meta},"Die Predigt folgt dem Text [S1]."])
    assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out and "Optionale coverage-Metadaten nicht benötigt" in out and len(p)==4,out
print("DEV14 optional coverage does not block explicit source request PASS")

out,p=call([LIST,VIEW,READY,"Die Predigt folgt dem Text.",READY,"Die Predigt folgt dem Text."])
assert "NICHT FREIGEGEBEN" in out and "Keine aussagebezogenen Quellenkennungen" in out and len(p)==6,out
print("DEV14 explicit sources remain mandatory PASS")

out,p=call([READY],question=NORMAL)
assert "NICHT FREIGEGEBEN" in out and len(p)==1,out
for ans,reason in [
    ("A [S99].","Nicht gelesene Quellenkennung"),
    ("A [S1/Extrakt 1668].","Nichtkanonische Quellenkennung"),
    ('Er schreibt: „Ein erfundenes Zitat.“ [S1]',"Originalzitat stimmt nicht"),
    ('Er schreibt: „Ein erfundenes Zitat.“',"Originalzitat ohne nachfolgende Quellenkennung"),
    ("Nach Nr. 1668 gilt A.","Absatznummer ohne zugehörige Quellenkennung"),
]:
    out,p=call([LIST,VIEW,READY,ans,READY,ans],question=NORMAL)
    assert "NICHT FREIGEGEBEN" in out and reason in out and len(p)==6,out
print("DEV14 no evidence and invalid concrete claims blocked in ordinary mode PASS")

out,p=call([LIST,VIEW,READY,'Klippert schreibt: „Die Anwendung bleibt an die Aussage des Textes gebunden und wird nicht von außen an ihn herangetragen.“ [S1]'],question=NORMAL)
assert "SOURCEGUARD AGENT: FREIGEGEBEN" in out and "Tatsächlich gelesene Originalstellen:" in out,out
print("DEV14 verified literal quotation retains provenance PASS")

topics="Erläutere Predigt, Anwendung und Kontext."
for coverage in ({"Predigt":["S7"],"Anwendung":["S1"],"Kontext":["S1"]},{}):
    meta=dict(READY["final"],coverage=coverage)
    out,p=call([LIST,VIEW,{"final":meta},"Predigt, Anwendung und Kontext [S1].",{"final":meta},"Predigt, Anwendung und Kontext [S1]."],question=topics)
    assert "NICHT FREIGEGEBEN" in out and ("coverage" in out or "Pflichtteilthemen" in out) and len(p)==6,out
print("DEV14 mandatory coverage remains strict PASS")

q="Korrigiere den folgenden Text rein sprachlich: Der Glaube tragen."
out,p=call([{"final":{"sources_sufficient":False}},"Der Glaube trägt."],question=q)
assert "OHNE QUELLENPFLICHT" in out and len(p)==2,out
print("DEV14 language revision remains proportionate PASS")
