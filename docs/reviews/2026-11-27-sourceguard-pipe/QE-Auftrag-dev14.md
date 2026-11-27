# QE-Auftrag: dev14 – auftragsabhängige Qualitätssicherung

Stand 27.11.2026. Unabhängiger QE; keine Schreiboperationen, keine Freigabe-, Merge- oder Baseline-Hoheit. SSOT baem-oss/THEOAgent, Branch local-dev.

## Prüfstand

- PO-Entscheidung: PO-Entscheidung-dev14.md (in diesem Verzeichnis).
- Prüfling: tools/local_dev/sourceguard_pipe_v0_5_5_dev14.py, Commit 7186a39f7079d4110442970b251b51cd6e588da7, Blob 79ea41393414abdb3fa4fb3e9c941c2a87d93222.
- Neue Protokolltests: tests/local_dev/regression/test_dev14_protocol.py, Commit e298107930eadbd1bfde1f33dd4535ebe4eaffa9.
- Referenz dev13: fbf6c5b009d9aa840fef1cf4df2dbc9fd2bc6c79. PO-Testausgabe: Compile PASS, AP1 5/5, Protokoll 13/13, AP2 7/7, historischer Korpus 35 PASS/0 FAIL/11 PARTIAL/1 INFO. Zwei Live-Erstanfragen FAIL wegen coverage (siehe PO-Entscheidung); keine dev13-Folgefrage. dev14 noch nicht live getestet.
- Historische QE-Berichte, Tests und Baseline v1.2.0 bleiben unverändert.

## Auftrag

1. Prüfe den Diff dev13→dev14 gegen die PO-Entscheidung, GR-01/02/03/17/18 und die gesamte Baseline. Trenne fachliche Fundierung, technische Provenienz und Präsentation. Keine Behauptung einer semantischen Vollprüfung durch Python.
2. Prüfe den tatsächlichen Zweiphasenpfad: normale Paraphrasen mit/ohne interne Kennungen; fehlende Originallektüre; explizite Quellenfrage mit/ohne Belege; Folgefrage nach Quellen einer vorherigen Antwort; konkrete Wortzitate und Fundstellen, auch ohne ausdrücklichen Nachweisauftrag. Prüfe, ob Bibelstellen, Dokumenttitel, KKK- und CIC-Referenzen ausreichend erfasst sind; bestehende Lücken von neuen Regressionen trennen. Prüfe die Freigabe- und Darstellungspfade getrennt.
3. Prüfe wants_sources/needs_inline_evidence/show_source_details auf Fehlklassifikation, Negation, unterschiedliche deutsche Formulierungen, kombinierte Aufträge, Gesprächskontext und Nachweiswünsche. Keine umfangreiche Keyword-Ontologie als Selbstzweck. Prüfe insbesondere, ob ein expliziter Nachweisauftrag durch eine oberflächliche Negation verloren gehen kann. Prüfe, ob der Quellenwunsch in einer Folgefrage angemessen behandelt wird und alte Aussagen nicht als Evidenz verwendet werden.
4. Prüfe coverage bei allgemeinen Fachfragen und ausdrücklichen Nachweisaufträgen ohne Pflichtteilthemen (auch ungültige optionale Metadaten) sowie tatsächliche Pflichtteilthemen mit fehlenden, falschen oder vollständigen Belegen. Prüfe, ob die bestehende Erkennung expliziter Aufzählungen unnötige Sperren erzeugt. Bei normalen Paraphrasen darf das Weglassen sichtbarer Kennungen kein Ersatz für erforderliche Werk-/Originalprüfung sein.
5. Prüfe Werkidentität ohne Inline-Kennungen, work/works, unbekannte oder nichtkanonische Kennungen, Quellenlisten, Wortlautprüfung, Nummernbindung, fehlende Evidenz, LOCAL_ONLY, Skill-/Werkzeugautorisierung, Kontextbereinigung und Token-/Rundenbudgets. Prüfe die Darstellungsbereinigung auf unbeabsichtigten Textverlust (Code, Markdown, Zitate, Abstände); Diagnosekennungen im Entwicklermodus getrennt beurteilen.
6. Führe die unten genannten Tests aus. Prüfe die neuen Fixtures auf tatsächliche Aussagekraft, insbesondere positive Wortzitate und Pflichtteilthemen. Identifiziere falsch-positive Tests anhand genauer Sperrursachen und Provider-Aufrufzahlen. Vergleiche den historischen Korpus auf Einzelfallebene: bewusst entfallene Formalpflichten sind keine Regression; unbewiesene Sachbehauptungen, falsche Quellen oder unberechtigte Freigaben sind weiterhin Defekte. Keine stillschweigende Änderung historischer Tests.
7. Prüfe ausdrücklich die Grenze der Lösung: die Pflicht zur Originallektüre bei allen nicht rein sprachlichen Fachaufträgen bleibt in dev14 erhalten; ob dies bei kreativen/liturgischen Aufträgen verhältnismäßig ist, als Finding bewerten, nicht eigenmächtig ändern. GR-18-Teilergebnisse sind separat zu bewerten, kein automatischer PASS aufgrund einer Sperre.
8. Priorisiere konkrete, kleine Korrekturen nach Nutzen, Risiko und Aufwand. KISS und Reuse before Build. Keine neue Architektur ohne nachgewiesenen Bedarf.

## Reproduktion

Im Repository-Root, Python-Umgebung mit pydantic:

```bash
export SG_PIPE=tools/local_dev/sourceguard_pipe_v0_5_5_dev14.py
python -m py_compile "$SG_PIPE"
python tests/local_dev/regression/test_dev13_ap1.py
python tests/local_dev/regression/test_dev14_protocol.py
python tests/local_dev/regression/test_ap2_citations.py
python tests/local_dev/regression/test_ap2_quotes.py
python tests/local_dev/qe_reference/qe_tests.py
```

Historische Tests können aufgrund der geänderten Präsentationspflicht ein abweichendes Soll haben. Keine pauschale Erwartung 35/0/11/1. Reproduziere mit dev13 und benenne Einzelfalldifferenzen. dev14-Protokolltests sind neue, noch nicht ausgeführte Tests des SE. Keine Live-Zugänge vorausgesetzt. Live-Test durch PO nach Review: normaler Klippert-Auftrag, expliziter Originalstellenauftrag (bisherige Frage), Folgefrage nach Anwendung und Quellen; weitere risikoorientierte Fälle nach Findings.

## Ergebnis

Priorisierter Bericht mit Anforderungsbezug, Code-/Teststelle, Reproduktion, Soll/Ist, nachgewiesener Ursache vs. Hypothese, kleinstem Fix und Restrisiko. Keine Freigabeentscheidung. Keine Repo-Änderung. 
