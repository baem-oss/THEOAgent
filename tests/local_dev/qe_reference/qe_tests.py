"""QE-Tests gegen die UNVERÄNDERTE Datei (Kopie, SHA-256 geprüft). Ergebnis: Tabelle Erwartet/Tatsächlich."""
import asyncio, json, hashlib
import harness as h

A = h.A
G = h.GuardError
RESULTS = []


def rec(tid, gegenstand, erwartet, tatsaechlich, ok, art="Unit (simuliert)"):
    verdict = ok if isinstance(ok, str) else ("PASS" if ok else "FAIL")
    RESULTS.append((tid, art, gegenstand, erwartet, tatsaechlich, verdict))


def vf(answer, evidence, question="Was sagt die Quelle zur Predigt?", **final):
    f = {"answer": answer, "sources_sufficient": True}
    f.update(final)
    try:
        out = A["validate_final"](question, f, evidence, require_work=final.pop("_rw", False))
        return "FREIGEGEBEN", out
    except G as e:
        return "GESPERRT", str(e)


def rendered_ids(answer, evidence):
    r = {"status": "FREIGEGEBEN", "answer": answer, "evidence": evidence, "diagnostic": [], "metrics": {}}
    txt = A["render_result"](r)
    tail = txt.split("**Tatsächlich gelesene Originalstellen:**")
    return sorted(set(__import__("re").findall(r"^- \[(S\d+)\]", tail[1], flags=8))) if len(tail) > 1 else []


E3 = [h.ev(1, nums=[12]), h.ev(2), h.ev(3)]

# ---------------------------------------------------------------- 7.1 Belegkennungen
s, o = vf("Aussage A [S1].", E3)
rec("B-01", "[S1]", "erkannt, Freigabe, S1 im Quellenverzeichnis", f"{s}; Verzeichnis {rendered_ids(o, E3) if s=='FREIGEGEBEN' else '-'}", s == "FREIGEGEBEN" and rendered_ids(o, E3) == ["S1"])
s, o = vf("Aussage A [S1] [S2].", E3)
rec("B-02", "[S1] [S2]", "beide erkannt", f"{s}; Verzeichnis {rendered_ids(o, E3)}", s == "FREIGEGEBEN" and rendered_ids(o, E3) == ["S1", "S2"])
s, o = vf("Aussage A [S1, S2].", E3)
rec("B-03", "[S1, S2] (einziger Beleg)", "beide erkannt, Freigabe", f"{s}: {o}", s == "FREIGEGEBEN")
s, o = vf("Aussage A [S1, S2, S3].", E3)
rec("B-04", "[S1, S2, S3] (einziger Beleg)", "alle erkannt, Freigabe", f"{s}: {o}", s == "FREIGEGEBEN")
s, o = vf("Aussage A [S1]. Aussage B [S1, S99].", E3)
rec("B-05", "[S1] … [S1, S99]", "Sperre wegen S99", f"{s}", s == "GESPERRT")
s, o = vf("Aussage A [S99] [S1].", E3)
rec("B-06", "[S99] [S1]", "Sperre wegen S99", f"{s}: {o}", s == "GESPERRT")
s, o = vf("Aussage A [S2, S3]. Aussage B [S1, S2].", E3)
rec("B-07", "ausschließlich kombinierte Belege", "vollständige Validierung, Freigabe", f"{s}: {o}", s == "FREIGEGEBEN")
s, o = vf("Aussage A ohne Beleg.\n\nQuellen:\n[S1]", E3)
rec("B-08", "Kennung nur im Quellenverzeichnis", "Sperre", f"{s}: {o}", s == "GESPERRT")
s, o = vf("Nach Nr. 13 gilt A [S1].", E3)
rec("B-09", "nicht registrierte Absatznummer (S1 hat Nr. 12)", "Sperre", f"{s}: {o}", s == "GESPERRT")
s, o = vf("Nach Nr. 12 gilt A [S1].", E3)
rec("B-09b", "registrierte Absatznummer", "Freigabe", f"{s}", s == "FREIGEGEBEN")
# Werkzuordnung
W_OK = {"title": "Vom Text zur Predigt", "author": "Wolfgang Klippert"}
W_X = {"title": "Andere Homiletik", "author": "Hans Mueller"}
Ew = [h.ev(1, work=W_OK), h.ev(2, work=W_OK), h.ev(3, work=W_OK)]
s, o = vf("Aussage A [S1].", Ew, work=W_X)
rec("B-10", "falsche Werkzuordnung (final.work ≠ gelesenes Werk)", "Sperre", f"{s}: {o}", s == "GESPERRT")
Ew2 = [h.ev(1, work=W_OK), h.ev(2, work=W_OK), h.ev(3, work=W_X)]
s, o = vf("Aussage A [S1]. Aussage B [S1, S3].", Ew2, works={"S1": W_OK, "S3": W_OK})
rec("B-10b", "falsche Werkzuordnung nur in kombiniertem Beleg (S3 deklariert Klippert, gelesen Mueller)", "Sperre", f"{s}", s == "GESPERRT")
# Wortzitat
s, o = vf('Klippert schreibt: „Die Predigt ist vor allem eine Plauderei über das Wetter der Woche.“ [S1]', E3)
rec("B-11", "erfundenes Wortzitat mit gültiger Kennung", "Sperre oder Kennzeichnung (GR-03)", f"{s}", s == "GESPERRT")
# weitere Schreibweisen
for tid, ans in [("B-12", "Aussage A [S1]. Aussage B [S1 und S99]."),
                 ("B-13", "Aussage A [S1]. Aussage B [S1–S9]."),
                 ("B-14", "Aussage A [S1]. Aussage B (vgl. S99)."),
                 ("B-15", "Aussage A [S1]. Aussage B [S 99].")]:
    s, o = vf(ans, E3)
    rec(tid, ans.split(". ", 1)[1], "Sperre (nicht registrierte Kennung)", f"{s}", s == "GESPERRT")
s, o = vf("Aussage A [S1]. Aussage B [S1, S2].", E3)
rec("B-16", "gemischt: [S1] … [S1, S2] → Quellenverzeichnis", "S1 und S2 im Verzeichnis", f"{s}; Verzeichnis {rendered_ids(o, E3)}", rendered_ids(o, E3) == ["S1", "S2"])
# Textbearbeitung
q_edit = "Kürze den folgenden Absatz und ergänze ein Zitat aus Dei Verbum 12: Die Schrift ist auszulegen."
try:
    out = A["validate_final"](q_edit, {"answer": 'Die Schrift ist auszulegen; Dei Verbum 12 sagt: „Erfundener Satz.“ [S1, S2]', "sources_sufficient": True}, [])
    s, o = "OHNE QUELLENPFLICHT", out
except G as e:
    s, o = "GESPERRT", str(e)
rec("B-17", "kombinierte Kennung im Textbearbeitungs-Pfad", "Sperre (Kennungen bei Textbearbeitung unzulässig)", s, s == "GESPERRT")

# ---------------------------------------------------------------- 7.2 Werkzeugargumente
DVQ = ("Welche drei wesentlichen Grundsätze der Schriftauslegung nennt Dei Verbum 12? Erläutere diese anhand des "
       "amtlichen Originaltextes des Zweiten Vatikanischen Konzils und belege deine Aussagen.")


def web_case(tid, gegenstand, action, expect, check, with_web=True, more=()):
    lib = h.FakeLibrary()
    r = h.run(DVQ, lib.tools(with_web=with_web), [{"actions": [action]}, *more])
    diag = "; ".join(r["diagnostic"])
    actual = f"{r['status']}: {r['answer'][:70]} | Runden {r['metrics']['rounds']}, Aufrufe {r['metrics']['tool_calls']}"
    rec(tid, gegenstand, expect, actual, check(r, diag))
    return r


web_case("A-01", "gültige Websuche", {"tool": "search_web", "args": {"query": "Dei Verbum 12 Schriftauslegung"}},
         "Trefferliste zur Nutzerauswahl",
         lambda r, d: r["status"] == "WEBQUELLE AUSWÄHLEN")
fallback = {"final": {"answer": "Keine Quelle lesbar.", "sources_sufficient": False}}
for tid, g, act in [
        ("A-02", "fehlendes query", {"tool": "search_web", "args": {}}),
        ("A-03", "leerer Suchausdruck", {"tool": "search_web", "args": {"query": ""}}),
        ("A-04", "falscher Datentyp (Liste)", {"tool": "search_web", "args": {"query": ["Dei Verbum 12"]}}),
        ("A-07", "181 Zeichen", {"tool": "search_web", "args": {"query": "x" * 181}}),
        ("A-07b", "Nutzerfrage DV 12 wörtlich als Suchausdruck", {"tool": "search_web", "args": {"query": DVQ}}),
        ("A-07c", "query auf Aktionsebene statt in args", {"tool": "search_web", "query": "Dei Verbum 12"}),
        ("A-07d", "\"arguments\" statt \"args\"", {"tool": "search_web", "arguments": {"query": "Dei Verbum 12"}})]:
    web_case(tid, g, act, "kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance)",
             lambda r, d: "PASS" if r["metrics"]["rounds"] >= 2 else ("PARTIAL" if r["status"] == "NICHT FREIGEGEBEN" else "FAIL"), more=[fallback])
web_case("A-06", "180 Zeichen", {"tool": "search_web", "args": {"query": "x" * 180}},
         "Validierung bestanden, Ausführung", lambda r, d: r["status"] == "WEBQUELLE AUSWÄHLEN")
web_case("A-08", "zusätzliches Argument count (Teil der nativen Signatur)",
         {"tool": "search_web", "args": {"query": "Dei Verbum 12", "count": 3}},
         "Korrekturchance oder Ignorieren des optionalen Arguments", lambda r, d: "PASS" if r["status"] == "WEBQUELLE AUSWÄHLEN" else "PARTIAL", more=[fallback])
web_case("A-09", "Webwerkzeug nicht verfügbar (Websuche im Chat aus)", {"tool": "search_web", "args": {"query": "Dei Verbum 12"}},
         "kontrollierte Sperre, Ursache sichtbar", lambda r, d: r["status"] == "NICHT FREIGEGEBEN" and "nicht verfügbar" in json.dumps(r["_infer"].seen[-1], ensure_ascii=False),
         with_web=False, more=[fallback])
r = h.run(DVQ, h.FakeLibrary().tools(with_web=True),
          [{"actions": [{"tool": "search_web", "args": {"query": "Dei Verbum"}}, {"tool": "list_knowledge", "args": {}}]}])
rec("A-10", "search_web zusammen mit weiterer Aktion", "Korrekturhinweis statt Totalabbruch", f"{r['status']}: {r['answer']}", "PASS" if r["metrics"]["rounds"] >= 2 else "PARTIAL")
r = h.run(DVQ, h.FakeLibrary().tools(), [{"actions": [{"tool": "view_skill", "args": {"name": "homiletik"}}]}])
rec("A-11", "Modell ruft view_skill (vom Systemprompt v0.3.11 verlangt)", "kontrollierte Behandlung ohne Totalabbruch", f"{r['status']}: {r['answer']}", "PASS" if r["metrics"]["rounds"] >= 2 else "PARTIAL")
# fehlerhafter Originalabruf (fetch) -> keine Freigabe
lib = h.FakeLibrary()
URL = "https://www.vatican.va/x.html"
r = h.run(DVQ, lib.tools(with_web=True, fetch_text=json.dumps({"error": "HTTP 404"})),
          [{"actions": [{"tool": "fetch_url", "args": {"url": URL}}]},
           {"final": {"answer": "DV 12 sagt A [S1].", "sources_sufficient": True}},
           {"final": {"answer": "DV 12 sagt A [S1].", "sources_sufficient": True}}], selected_url=URL)
rec("A-12", "fehlerhafter Originalabruf (fetch_url liefert Fehler)", "keine Freigabe", f"{r['status']}: {r['answer'][:80]}", r["status"] == "NICHT FREIGEGEBEN")

# ---------------------------------------------------------------- 7.3 Freigabemechanismus
KQ = ("Welche methodischen Anforderungen stellt Wolfgang Klippert an eine textgemäße Predigt? Nutze ausschließlich "
      "das Originalwerk von Klippert aus deiner Fachbibliothek und belege deine Aussagen mit konkreten Originalstellen.")
FIN = {"final": {"answer": "Die Predigt folgt dem Text [S1].", "sources_sufficient": True, "work": W_OK}}


def view(s, fid="f-klip", work=W_OK, **kw):
    a = {"file_id": fid, "start_line": s, "end_line": s + 40, "anchor_line": s + 2, "work": work}
    a.update(kw)
    return {"tool": "view_knowledge_file", "args": a}


LIST = {"actions": [{"tool": "list_knowledge", "args": {}}]}
r = h.run(KQ, h.FakeLibrary().tools(), [FIN, FIN])
rec("F-01", "kein Lesezugriff", "Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")
r = h.run(KQ, h.FakeLibrary().tools(), [LIST, {"actions": [view(1, fid="f-unbekannt")]}, FIN])
rec("F-02", "erfundene Datei-ID", "Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")
lib = h.FakeLibrary(); lib.files["f-klip"] = (lib.files["f-klip"][0], lib.files["f-klip"][1][:5])
r = h.run(KQ, lib.tools(), [LIST, {"actions": [view(100)]}, FIN, FIN])
rec("F-03", "leere Originalpassage (Fenster hinter Dateiende)", "Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")
lib = h.FakeLibrary()
toc = ["Inhaltsverzeichnis"] + [f"{i}. Kapitel über etwas .......... {i*10}" for i in range(1, 60)]
lib.files["f-klip"] = (lib.files["f-klip"][0], ["Vom Text zur Predigt", "Wolfgang Klippert"] + toc + h.prose_lines(400))
r = h.run(KQ, lib.tools(), [LIST, {"actions": [view(3)]}, FIN, FIN])
rec("F-04", "Lesefenster ist Inhaltsverzeichnis", "keine Registrierung, Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")
r = h.run(KQ, h.FakeLibrary().tools(), [LIST, {"actions": [view(800, fid="f-other", work=W_X)]},
                                        {"final": {"answer": "A [S1].", "sources_sufficient": True, "work": W_X}},
                                        {"final": {"answer": "A [S1].", "sources_sufficient": True, "work": W_X}}])
rec("F-05", "gültige Lektüre eines fremden Werks bei Klippert-Auftrag", "Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")
r = h.run(KQ, h.FakeLibrary().tools(), [LIST] + [{"actions": [view(100 + 50 * i)]} for i in range(9)] + [FIN])
rec("F-06", "Lesebudget (MAX_READS=8) überschritten", "kontrollierte Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")
r = h.run(KQ, h.FakeLibrary().tools(), [LIST] * 10)
rec("F-07", "Rundenbudget (MAX_ROUNDS=10) erreicht", "kontrollierte Sperre", f"{r['status']}: {r['answer']}", r["status"] == "NICHT FREIGEGEBEN")


def bad_json(_):
    raise A["ModelOutputError"]("Keine JSON-Struktur")


r = h.run(KQ, h.FakeLibrary().tools(), [bad_json, bad_json])
rec("F-08", "zweimal ungültige strukturierte Modellausgabe", "kontrollierte Sperre", f"{r['status']}: {r['answer'][:80]}", r["status"] == "NICHT FREIGEGEBEN")
for tid, q in [("F-09", "Kürze den Absatz und ergänze, was Dei Verbum 12 über die Schriftauslegung lehrt: Die Bibel ist Gottes Wort."),
               ("F-09b", "Korrigiere meinen Satz: Klippert fordert in seinem Buch, dass jede Predigt drei Punkte hat.")]:
    r = h.run(q, h.FakeLibrary().tools(), [{"final": {"answer": 'Dei Verbum 12 lehrt: „Erfundenes Zitat.“', "sources_sufficient": True}}])
    rec(tid, "quellenpflichtige Anfrage mit Textbearbeitungs-Verb: " + q[:60] + "…", "Quellenpflicht bleibt bestehen", f"{r['status']}", r["status"] != "OHNE QUELLENPFLICHT")
# Statusanzeige: frühere Antwortprüfung bleibt in Freigabe-Diagnose (P-03-Muster)
r = h.run(KQ, h.FakeLibrary().tools(), [LIST, FIN, {"actions": [view(800)]}, FIN])
txt = A["render_result"](r, True)
rec("F-10", "frühe Abschlussantwort ohne Lektüre, dann Lektüre, dann Freigabe (P-03-Muster)",
    "Diagnose kennzeichnet frühere Prüfmeldung als überholt", f"{r['status']}; Diagnose enthält 'Antwortprüfung: Keine Originalstelle…' ohne Einordnung",
    "PARTIAL" if r["status"] == "FREIGEGEBEN" and "Antwortprüfung: Keine Originalstelle" in txt else "FAIL")
# Überlappende Lesefenster als getrennte Belege (P-03: S2/S3/S4)
r = h.run(KQ, h.FakeLibrary().tools(), [LIST, {"actions": [view(2000), view(2002), view(2009)]},
                                        {"final": {"answer": "A [S1]. B [S2]. C [S3].", "sources_sufficient": True, "work": W_OK}}])
ov = [e["locator"] for e in r["evidence"]]
rec("F-11", "drei überlappende Lesefenster", "eine Fundstelle oder Überlappung erkennbar", f"{r['status']}; {ov}", "INFO")

# ---------------------------------------------------------------- Pipe-Integration (gestubbt)
SP = "S" * 20916  # Länge Systemprompt v0.3.11 in Zeichen
sysmsg = SP + "\n<attached_knowledge>\n<knowledge type=\"collection\" id=\"k1\"/>\n</attached_knowledge>\n<available_skills>…</available_skills>"
body = {"model": "theoagent-pipe-dev", "messages": [{"role": "system", "content": sysmsg},
                                                    {"role": "user", "content": "Frühere Frage zu Klippert"},
                                                    {"role": "assistant", "content": "Frühere Antwort"},
                                                    {"role": "user", "content": "Und was sagt er zur Anwendung?"}]}
p = h.sg.Pipe(); p.valves.AGENT_TEST_MODE = True; p.valves.TARGET_MODEL_ID = "google/gemma-4-31b-it"
h._script["outputs"][:] = [{"final": {"answer": "x", "sources_sufficient": False}}]; h._script["prompts"].clear()
out = asyncio.run(p.pipe(body, __tools__=h.FakeLibrary().tools(), __metadata__={"system_prompt": sysmsg},
                         __request__=object(), __user__={"id": "u1"}))
pr = h._script["prompts"][0]
first = pr[0]["content"]
rec("I-01", "Weitergabe Systemprompt (20.916 Z.) bei angehängter Wissenssammlung", "vollständiger Systemprompt erreicht das Modell",
    f"{len(pr)} Nachrichten; 1. Systemnachricht {len(first)} Zeichen (Systemprompt-Anteil {first.count('S')} von 20916)", first.count("S") >= 20916, "Pipe-Integration (gestubbt)")
um = [m["content"] for m in pr if m["role"] == "user"]
rec("I-02", "Gesprächskontext bei Folgefrage", "Vorkontext (Klippert) verfügbar", f"Modell erhält nur: {um}", any("Klippert" in u for u in um), "Pipe-Integration (gestubbt)")

if __name__ == "__main__":
    print("SHA-256 Testobjekt:", hashlib.sha256(open(h.PIPE_PATH, "rb").read()).hexdigest())
    print("| ID | Art | Gegenstand | Erwartet | Tatsächlich | Ergebnis |\n|---|---|---|---|---|---|")
    for row in RESULTS:
        print("| " + " | ".join(str(x).replace("|", "/").replace("\n", " ") for x in row) + " |")
    from collections import Counter
    print(Counter(r[-1] for r in RESULTS))