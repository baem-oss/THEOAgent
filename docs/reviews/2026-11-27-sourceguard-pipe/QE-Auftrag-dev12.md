# QE-Auftrag – dev12: Kommunikationsarchitektur und Belegintegrität

Stand: 27.11.2026. PO hat unabhängigen Check vor dev13 freigegeben.
SSOT: https://github.com/baem-oss/THEOAgent, Branch local-dev.
Prüfstand vor Ablage dieses Auftrags: ef15f876c45fa62cf40a3c216cecfe936e6ccf42.
Prüfling: tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py, Commit be8b147d9a8cfa61b48f7d8d2b33428213375626, Git-Blob 8de0196214419bb38268c341fa95f2bd69f78718.
Protokolltest: tests/local_dev/regression/test_dev12_protocol.py (Stand ef15f87).
Vorgängerauftrag QE-Auftrag-dev11.md bleibt historisch erhalten; dieser Auftrag erweitert und aktualisiert dessen Umfang.
Baseline: docs/requirements/BASELINE.md, v1.2.0. Keine Änderung oder Freigabe durch QE.

## 1. Empirische Befunde (vom PO übermittelte Testausgaben)
- dev5 (abgenommene AP1-Referenz, 39e96646c1265eb0e9c4b6d903d1316071c65c9f): Klippert-Erstanfrage 23,2 s, Folgefrage 16,6 s, beide freigegeben.
- dev8: Erstfrage 24,4 s, Zitatzuordnung gesperrt. dev9: 53,0 s, fehlende vollständige Zitatdeklaration. dev10 (2f1446e): 74,0 s, 5 Modellrunden, 7 Tools, keine Originallektüre; zweimal ungültiges JSON nahe Ausgabeende. Truncation dort nicht nachgewiesen.
- dev11 (407c9c4): AP1 5 Testblöcke PASS; 4 neue Metriktestblöcke PASS. Historischer Korpus 21 PASS/14 FAIL/11 PARTIAL/1 INFO. Erstanfrage freigegeben, 64,219 s, 6 Runden/15 Tools/4 registrierte Lesebelege. Runde 4: 48,204 s, 8192 Completion-Tokens, finish_reason=length, 15182 Ausgabezeichen, JSON-Fehler. Einmalige Korrektur erfolgreich. Fachantwort 751 Tokens, 7,275 s. Abschneidung in diesem Lauf belegt, Ursache des Ausuferns offen.
- dev12: Compile und alle 7 neuen Protokolltests PASS nach Korrektur der Testassertion zur Position des Systemprompts. Historischer Korpus 21/14/11/1 (Summengleichheit, keine Einzelfallidentität belegt). AP1/dev11-Pipe-Integrationstests noch nicht auf neues Protokoll migriert.
- dev12 Erstanfrage: freigegeben, 21,278 s, 7 Modellrunden/17 Tools/4 registrierte Lesebelege. Steuerung 6 Runden, max_tokens=1024, beobachtete Completion-Tokens 79/105/210/492/670/167, alle finish_reason=stop. Runde 5: Modell-JSON ohne actions/final, einmalige Korrektur erfolgreich. Fachantwort separate Runde, max_tokens=4096, 681 Completion-Tokens, 5,192 s. LOCAL_ONLY aktiv, Skill theologische-quellenprufung geladen. S1–S4 registriert.
- Konkreter Belegdefekt in freigegebener dev12-Antwort: zweimal [S4/Extrakt 1668] bei registriertem S4 Extraktzeilen 1779–1799. Aussage zur deskriptiven Exegese/Übertragung nicht unabhängig am Original geprüft. Keine Behauptung, dass der Inhalt falsch ist; Fundstellenbindung technisch unzureichend.
- Folgefrage im selben Chat: "Und was sagt er zur Anwendung?" dev12 NICHT FREIGEGEBEN, 22,734 s, 4 Modellrunden/8 Tools/1 registrierter Lesebeleg. LOCAL_ONLY aus Verlauf, 2 historische Nachrichten, Skills exegetisch-homiletischer-arbeitsgang und homiletik geladen. Runde 1: 1024 Tokens, length, 3505 Zeichen, 11,004 s; Runde 2: 108 Tokens, stop; Runde 3: 195 Tokens, stop; Runde 4: 809 Tokens, stop, 3153 Zeichen, keine JSON-Struktur, 7,018 s. Formatkorrekturbudget verbraucht, keine Antwortphase. Keine Rohinhalte der fehlgeschlagenen Modellausgaben verfügbar.
- Nutzer bestätigt, dass zusätzlicher Hinweis zur erneuten SourceGuard-Prüfung aus Systemprompt oder Skill stammt; genaue Herkunft nicht verifiziert.
- Direkter OpenRouter Structured-Outputs-Probe CD03 hing laut PO; kein belastbarer Befund über Backend-Unterstützung. PO entschied provider-/modellunabhängige Architektur: kompaktes JSON für Steuerung, Markdown für Fachantwort. Keine Verpflichtung zu Constrained Decoding.

## 2. Reviewfragen
1. Ist die zweiphasige Schnittstelle als kleinste robuste Lösung geeignet? Prüfe tatsächlichen Kontrollfluss, Metadaten (work/works, coverage, sources_sufficient), Evidenzgrenze, Round-/Call-Budgets, Umgang mit abgeschnittenen und vollständig falschen Antworten. Bewerte Risiken der optionalen compose-Schnittstelle und Aussagekraft historischer Tests, die den alten Pfad direkt aufrufen.
2. Untersuche plausible Ursachen der Formatabweichung, ohne unzugängliche Rohantworten zu rekonstruieren: konkurrierende technische/fachliche Anweisungen, historische Antwort im assistant-Rollenformat, Diagnoseballast, Skill-/Toolfeedback. Prüfe konkret, welche Anweisungen in beiden Phasen an den Provider gehen. Bewerte minimale Abhilfe (Historie bereinigen, technische Phaseninstruktion unmittelbar vor Aufruf, ggf. alternative kompakte Steuerung), ohne fachliche Anforderungen oder Kontextkontinuität aufzuweichen.
3. Prüfe die Belegintegrität: kanonische und gruppierte Kennungen, nichtkanonische Angaben [S4/Extrakt 1668], Bindung von Absatznummern und Extraktzeilen, Werkidentität, Abdeckungsnachweise, Quellenverzeichnis, reine Sprachbearbeitung vs. fachlicher Auftrag. Vergleiche dev10 mit dev12; empfehle gezielte Wiederverwendung statt Neubau. Prüfe GR-03 insbesondere bei expliziten Wortzitaten; Paraphrasenstandard ist keine Erlaubnis für unprüfbare Wortzitate. Trenne semantische Tragfähigkeit von technischer Validierung.
4. Prüfe Metriken auf Korrektheit, Datenschutz, Zuordnung und Overhead. Tokenbudgets 1024/4096 sind Entwicklungsparameter. Keine Garantie für Provider-Durchsetzung; lokale Zeichenprüfung ist nachgelagert. Zeitlimits und Teilergebnisse bleiben offen.
5. Führe relevante Tests tatsächlich aus, inkl. Compile, historischem Korpus mit Einzelfallvergleich, neuem Protokolltest. Prüfe AP1-Integration auf realem zweiphasigem Stub-Pfad (Skill-Inventar, Autorisierung, Gesprächshistorie, LOCAL_ONLY). Adaptiere alte Testfixtures nur in eigener Arbeitskopie; keine Änderung der historischen Artefakte im Repository. Prüfe fehlende Evidenz, Formatfehler nach gültiger Aktion, wiederholte Fehler, Antwortphase mit falschen Metadaten, nichtkanonische Fundstellen, fehlende/abgeschnittene Antwort, fehlende Provider-Metadaten. Dokumentiere Befunde zu tatsächlicher Live-Ausführung getrennt.
6. Empfehle eine priorisierte, schlanke dev13-Strategie. Entscheide nicht über Anforderungen, Freigabe, Versionsbaseline oder Merge. Keine Repository-Schreiboperationen.

## 3. Reproduktion
Im Repository-Root auf fixiertem Prüfstand:
```bash
export SG_PIPE=tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py
python -m py_compile "$SG_PIPE"
python tests/local_dev/regression/test_dev12_protocol.py
python tests/local_dev/qe_reference/qe_tests.py
```
Für Vergleichsläufe SG_PIPE auf dev5/dev11/dev10 ändern; die neuen dev12-Protokolltests sind nicht für diese Altversionen vorgesehen. AP1 und dev11-Metriktests mit bisherigem Wire-Format nicht unbesehen als dev12-PASS-Gate verwenden.
Live-Frage im neuen Chat, Websuche aus: "Welche methodischen Anforderungen stellt Wolfgang Klippert an eine textgemäße Predigt? Nutze ausschließlich das Originalwerk von Klippert aus deiner Fachbibliothek und belege deine Aussagen mit konkreten Originalstellen."
Anschließend im selben Chat: "Und was sagt er zur Anwendung?"
Kein Zugriff auf Homeserver oder DRS:KI vorausgesetzt; fehlende Live-Möglichkeit transparent kennzeichnen.

## 4. Ergebnisformat
Befunde nach Schweregrad, Anforderungsbezug, genaue Code-/Teststelle, Reproduktion, Soll/Ist, Evidenz, kleinster sinnvoller Fix, Restrisiko. Neue Regressionen von bereits bekannten Defiziten unterscheiden. Empfohlene nächste Schritte nach Nutzen/Risiko/Aufwand priorisieren. Keine Freigabeentscheidung; PO entscheidet.
