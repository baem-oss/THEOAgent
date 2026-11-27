"""QE-Arbeitskopie (nicht im Repo): reale dev12-Zweiphasen-Pipe mit Provider-Stub (finish_reason/usage).
Aufruf im Repo-Root:  SG_PIPE=tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py python qe_dev12_twophase.py
Vergleich:           SG_PIPE=<pfad>/dev13_candidate.py python qe_dev12_twophase.py
Hinweis: PASS/FAIL bezieht sich auf das QE-Soll der jeweiligen Zeile, nicht auf eine Freigabe."""
import asyncio, json, os, sys, re
from pathlib import Path
root = Path(os.environ.get("THEOAGENT_ROOT", "."))  # Repository-Root, Branch local-dev
os.environ.setdefault("SG_PIPE", str(root/"tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py"))
sys.path.insert(0, str(root/"tests/local_dev/qe_reference"))
import harness as h
A = h.A
WORK = {"title":"Vom Text zur Predigt","author":"Wolfgang Klippert"}
LIST = {"actions":[{"tool":"list_knowledge","args":{}}]}
def VIEW(s=1779,e=1799): return {"actions":[{"tool":"view_knowledge_file","args":{"file_id":"f-klip","start_line":s,"end_line":e,"anchor_line":s+2,"work":WORK}}]}
READY = {"final":{"sources_sufficient":True,"work":WORK}}
KQ = ("Welche methodischen Anforderungen stellt Wolfgang Klippert an eine textgemäße Predigt? Nutze ausschließlich "
      "das Originalwerk von Klippert aus deiner Fachbibliothek und belege deine Aussagen mit konkreten Originalstellen.")
MANIFEST = "<available_skills><skill><id>homiletik</id></skill><skill><id>exegetisch-homiletischer-arbeitsgang</id></skill></available_skills>"
SYSPROMPT = ("THEOBald-Systemprompt. Antworte strukturiert in Markdown mit Überschriften. " * 300)[:20916] + MANIFEST
RESULTS=[]
def rec(tid, what, soll, ist, ok): RESULTS.append((tid, what, soll, ist, "PASS" if ok is True else "FAIL" if ok is False else ok))

def call(outputs, messages=None, tools=None, question=KQ, timings=True, usage=True):
    queue=list(outputs); payloads=[]
    async def provider(request, payload, user):
        payloads.append(payload)
        out=queue.pop(0); reason="stop"
        if isinstance(out,tuple): out,reason=out
        c = out if isinstance(out,str) else json.dumps(out,ensure_ascii=False)
        r={"choices":[{"message":{"content":c}}]}
        if reason is not None: r["choices"][0]["finish_reason"]=reason
        if usage: r["usage"]={"prompt_tokens":1,"completion_tokens":len(c)//4,"total_tokens":1}
        return r
    sys.modules["open_webui.utils.chat"].generate_chat_completion=provider
    p=h.sg.Pipe(); p.valves.AGENT_TEST_MODE=True; p.valves.SHOW_TIMINGS=timings; p.valves.TARGET_MODEL_ID="test-model"
    msgs = messages or [{"role":"system","content":SYSPROMPT},{"role":"user","content":question}]
    if tools is None: tools=h.FakeLibrary().tools()
    out=asyncio.run(p.pipe({"model":"pipe","messages":msgs},__tools__=tools,__metadata__={},__request__=object(),__user__={"id":"u1"}))
    return out,payloads,queue
def status(out): return out.split("\n",1)[0]
def released(out): return status(out).startswith("SOURCEGUARD AGENT: FREIGEGEBEN")

# ---------- Belegintegrität im realen Zweiphasenpfad
cases = [
 ("BI-01","nichtkanonisch [S4/Extrakt 1668] neben gültigem [S1]","Sperre","Die Predigt folgt dem Text [S1]. Deskriptive Exegese führt zur Übertragung [S1/Extrakt 1668]."),
 ("BI-02","nur nichtkanonisch [S1/Extrakt 1668]","Sperre","Die Predigt folgt dem Text [S1/Extrakt 1668]."),
 ("BI-03","gruppiert [S1, S99] neben [S1]","Sperre (S99 ungelesen)","Aussage A [S1]. Aussage B [S1, S99]."),
 ("BI-04","nur gruppiert [S1, S1]","Freigabe mit Quellenverzeichnis","Aussage A [S1, S1]."),
 ("BI-05","erfundenes Wortzitat mit [S1]","Sperre (GR-03)","Klippert schreibt: „Die Predigt ist eine Plauderei über das Wetter der Woche.“ [S1]"),
 ("BI-06","Extraktzeile im Text: 'Zeile 1668' [S1] (S1=1779–1799)","Sperre oder Kennzeichnung","Nach Zeile 1668 folgt die Predigt dem Text [S1]."),
 ("BI-07","Modell schreibt eigenes Quellenverzeichnis mit [S99]","Sperre oder Entfernung","Aussage A [S1].\n\nQuellen:\n- [S99] erfundenes Werk"),
]
for tid,what,soll,ans in cases:
    out,p,_=call([LIST,VIEW(),READY,ans, READY, ans])
    rec(tid,what,soll,status(out)+(" | Verzeichnis: "+",".join(re.findall(r"(?m)^- \[(S\d+)\]",out.split("Tatsächlich gelesene Originalstellen:**")[1])) if "Tatsächlich gelesene" in out else ""),
        (not released(out)) if "Sperre" in soll else (released(out) and "- [S1]" in out))

# ---------- Antwortphase mit falschen Metadaten
WX={"title":"Andere Homiletik","author":"Hans Mueller"}
out,p,_=call([LIST,VIEW(),{"final":{"sources_sufficient":True,"work":WX}},"A [S1].",{"final":{"sources_sufficient":True,"work":WX}},"A [S1]."])
rec("AM-01","final.work ≠ gelesenes Werk","Sperre",status(out),"NICHT FREIGEGEBEN" in out)
out,p,_=call([LIST,VIEW(),{"final":{"sources_sufficient":True}},"A [S1]."])
rec("AM-02","Werkauftrag (Klippert) ohne final.work","Sperre oder Korrektur",status(out)+" | Calls "+str(len(p)),"INFO")
out,p,_=call([LIST,VIEW(),{"final":{"sources_sufficient":True,"work":WORK,"coverage":{"Anwendung":["S7"]}}},"A [S1]."])
rec("AM-03","coverage verweist auf ungelesenes S7 (keine Pflichtaufzählung)","Sperre",status(out),"NICHT FREIGEGEBEN" in out)

# ---------- Formatfehler / Budget
out,p,_=call([LIST,"Hier ist meine Antwort in Prosa.",VIEW(),"## Anwendung\nKlippert sagt [S1].",READY,"x [S1]."])
rec("FB-01","Muster Folgefrage: gültig → Prosa → gültig → Prosa","Korrekturchance pro Vorfall (QE-Soll)",status(out)+" | Provider-Calls "+str(len(p))+" | "+(re.search(r"Modellausgabe trotz[^\n]*",out).group(0)[:80] if "trotz" in out else ""),released(out))
out,p,_=call([("x"*3505,"length"),LIST,VIEW(),"Prosa-Fachantwort [S1] in Steuerungsphase",READY,"A [S1]."])
rec("FB-02","Runde1 length (3505 Z.) → gültig → gültig → Prosa (reales Muster Folgefrage)","Korrektur möglich",status(out)+" | Calls "+str(len(p)),released(out))
out,p,_=call([LIST,VIEW(),READY,'{"final":{"sources_sufficient":true}}'])
rec("FB-03","Antwortphase liefert JSON","Sperre, keine Freigabe",status(out),"NICHT FREIGEGEBEN" in out)
out,p,_=call([LIST,VIEW(),READY,"Einleitung.\n```json\n{\"actions\":[]}\n```\nA [S1]."])
rec("FB-04","Antwortphase Markdown mit eingebettetem JSON-Block","Freigabe zulässig (nur Präfixprüfung)",status(out),"INFO")
out,p,_=call([LIST,VIEW(),READY,("Die Predigt folgt dem Text [S1]. Und dann",None)],usage=False)
rec("FB-05","Antwortphase ohne finish_reason/usage, Text endet mitten im Satz","Kennzeichnung fehlender Provider-Metadaten",status(out)+" | finish_reason "+("null" if '"finish_reason":null' in out else "?"),"INFO")
out,p,_=call([LIST,VIEW(),{"final":{"sources_sufficient":True,"work":WORK,"answer":""}},READY,"A [S1]."])
rec("FB-06","final mit leerem answer-Schlüssel","Formatkorrektur",status(out)+" | Calls "+str(len(p)),released(out))
out,p,_=call([LIST,{"sources_sufficient":True,"work":WORK}, VIEW(), READY,"A [S1]."])
rec("FB-07","final-Metadaten ohne final-Hülle (plausibles Muster Erstanfrage R5)","Formatkorrektur, dann Freigabe",status(out),released(out))

# ---------- Prompt-Inspektion Folgefrage
first,p1,_=call([LIST,VIEW(),READY,"## Anforderungen\nDie Predigt folgt dem Text [S1]."])
hist=[{"role":"system","content":SYSPROMPT},{"role":"user","content":KQ},{"role":"assistant","content":first},{"role":"user","content":"Und was sagt er zur Anwendung?"}]
out,p,_=call([LIST,VIEW(1500,1520),READY,"Die Anwendung bleibt textgebunden [S1]."],messages=hist)
ctrl=p[0]["messages"]; ans=p[-1]["messages"]
roles=[m["role"] for m in ctrl]
asst=next((m["content"] for m in ctrl if m["role"] in("assistant","user") and ("## Anforderungen" in m["content"])),"")
rec("PI-01","Rollenfolge Steuerungsaufruf 1 (Folgefrage)","Historie nicht als Assistant-Markdown",str(roles),"assistant" not in roles)
rec("PI-02","Historische Assistant-Nachricht enthält Diagnoseballast",
    "keine Diagnose/Messwerte im Modellkontext",f"{len(asst)} Z.; DIAGNOSE={'DIAGNOSE' in asst}; Messung-Zeilen={asst.count('Messung:')}; Provider-Zeilen={asst.count('Provider:')}",
    "DIAGNOSE" not in asst)
rec("PI-03","Historische Belegkennungen [S1] im Folgekontext","Kennungsraum je Turn getrennt",f"[S1] in Historie={('[S1]' in asst)}; neue Recherche registriert erneut S1","[S1]" not in asst)
lastu=ctrl[-1]["content"][:60]
rec("PI-04","Letzte Nachricht vor Steuerungsaufruf","technische Phaseninstruktion unmittelbar vor Aufruf",repr(lastu),"STEUER" in ctrl[-1]["content"].upper())
sys_ans=[m["content"][:70] for m in ans if m["role"]=="system"]
rec("PI-05","Systemblöcke Antwortphase","fachlicher Prompt + Markdown-Instruktion, keine widersprüchliche JSON-Anweisung",
    f"{len(sys_ans)} Systemblöcke; JSON-Schnittstellen-Hinweis im Präfix={'Agenten-JSON-Schnittstelle' in ans[0]['content']}","Agenten-JSON-Schnittstelle" not in ans[0]["content"])
rec("PI-06","Zeichenumfang Steuerungsaufruf 1",'Info',f"{sum(len(m['content']) for m in ctrl)} Z. (Systemprompt {len(ctrl[0]['content'])}, AGENT_PROMPT {len(ctrl[1]['content'])}, Historie {len(asst)})","INFO")
# Historie größer als 12000 Zeichen -> vollständiger Verlust?
big=[{"role":"system","content":SYSPROMPT},{"role":"user","content":KQ},{"role":"assistant","content":first+"\n"+("Diagnosezeile\n"*1200)},{"role":"user","content":"Und was sagt er zur Anwendung?"}]
out,p,_=call([LIST,VIEW(1500,1520),READY,"Die Anwendung bleibt textgebunden [S1]."],messages=big)
n=[m for m in p[0]["messages"] if m["role"] in("user","assistant")]
rec("PI-07","Vorantwort > 12000 Zeichen (z. B. Diagnose an)","Vorkontext gekürzt erhalten",f"{len(n)} Nutzer/Assistant-Nachrichten; Ursprungsfrage enthalten={any('Klippert' in m['content'] for m in n)}",any('Klippert' in m['content'] for m in n))
# Kennungskollision: Antwort zitiert alte S2 die in neuer Recherche nicht existiert / alte S1 -> neue S1
rec("PI-08","Kennungskollision alte/neue [S1]","alte Kennungen im Kontext neutralisiert",f"[S1] im Folgekontext={'[S1]' in asst}; neutralisiert={'früherer Beleg' in asst}","[S1]" not in asst)

# ---------- AP1 im Zweiphasenpfad
calls=[]
async def skill(id):
    calls.append(id); return json.dumps({"name":id,"content":"Gliedere die Antwort in Exegese, Meditation, Predigt. Antworte ausführlich."},ensure_ascii=False)
tools=h.FakeLibrary().tools(); tools["view_skill"]={"callable":skill}
out,p,_=call([{"actions":[{"tool":"view_skill","args":{"id":"homiletik"}}]},LIST,VIEW(),READY,"A [S1]."],messages=hist,tools=tools)
rec("AP1-A","view_skill autorisiert, Zweiphasen-Freigabe, LOCAL_ONLY aus Verlauf","Freigabe; LOCAL_ONLY aktiv (Verlauf)",status(out)+" | "+("LOCAL_ONLY: aktiv (auch aus Verlauf)" if "aus Verlauf" in out else "?"),released(out) and "aus Verlauf" in out)
skill_fb=[m["content"] for m in p[1]["messages"] if m["role"]=="user"][-1:]
rec("AP1-B","Skill-Inhalt (Ausgabe-/Gliederungsanweisung) erreicht Steuerungsphase","Info: konkurrierende Formatanweisung als user-Daten",f"{'Antworte ausführlich' in (skill_fb[0] if skill_fb else '')}","INFO")
out,p,_=call([{"actions":[{"tool":"view_skill","args":{"id":"fremd"}}]},LIST,VIEW(),READY,"A [S1]."],messages=hist,tools=tools)
rec("AP1-C","nicht inventarisierter Skill","kontrollierte Sperre/Korrektur, kein Aufruf",status(out)+f" | Aufrufe {calls}",calls==["homiletik"])
out,p,_=call([{"actions":[{"tool":"search_web","args":{"query":"Klippert"}}]},LIST,VIEW(),READY,"A [S1]."],messages=hist,tools=h.FakeLibrary().tools(with_web=True))
rec("AP1-D","Websuche trotz LOCAL_ONLY aus Verlauf","keine Websuche",status(out),"search_web" not in str(h.FakeLibrary().calls))

import collections
for r in RESULTS: print(" | ".join(map(str,r)))
print(collections.Counter(r[-1] for r in RESULTS))
