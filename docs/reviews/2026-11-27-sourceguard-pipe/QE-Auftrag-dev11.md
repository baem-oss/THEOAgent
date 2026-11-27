# QE-Auftrag – dev11 (Neubasis dev5)

PO-Entscheidung: 27.11.2026, dev5 als Basis, geänderte Zitatstrategie, Testmetriken, danach unabhängiger QE-Check.
Referenz: dev5 @ 39e96646c1265eb0e9c4b6d903d1316071c65c9f (AP1 abgenommen).
Prüfling: tools/local_dev/sourceguard_pipe_v0_5_5_dev11.py @ 407c9c4ea9e233757323857ed4d0fd6d509a1b07.
Tests: tests/local_dev/regression/test_dev11_metrics.py @ 27096be664776a05a1e675307e48c7cb95e8ef48.
SSOT: Repository local-dev. Keine Schreib- oder Freigabebefugnis des QE.

## Ausgangslage
dev5: erfolgreiche Klippert-Erstanfrage (23,2 s) und Folgefrage (16,6 s), 21 PASS / 14 FAIL / 11 PARTIAL / 1 INFO im historischen QE-Korpus. dev6–dev10: bis 35 PASS / 0 FAIL / 11 PARTIAL / 1 INFO in Simulation, aber dev8–dev10 Live-Fehlschläge. dev10: 74 s, 5 Runden, 7 Tools, 0 Originallektüren; zwei ungültige JSON-Ausgaben (16827 und 15320 Zeichen). Ursache nicht belegt.

## Prüfumfang
1. Diff gegen dev5: nur paraphrasenorientierte Agentenanweisung und Messinstrumentierung; keine stillschweigende Veränderung der technischen Gates, Budgets oder Zugriffskontrolle.
2. Zitatstrategie: Paraphrase Standard, explizite Originalzitate nur nach Verifikation, fehlender Nachweis kennzeichnen. Kein zusätzlicher deterministischer Wortlautprüfer. Bewerte insbesondere verbleibende GR-03-Risiken und die kleinste tragfähige Maßnahme; keine Baseline-Abschwächung.
3. Telemetrie: pro Modellrunde und tatsächlichem Werkzeugaufruf (einschließlich Kontextlektüre) Zeiten, Zeichen, Status; Provider-Finish-Reason, Usage, Input/Output-Längen, auch bei ungültigem JSON. Keine erfundenen Metadaten, keine vertraulichen Inhalte in neuen Messfeldern. Prüfe auch Overhead, fehlende Metadaten und korrekte Zuordnung.
4. Führe AP1, neuen Metriktest und historischen QE-Korpus aus; dokumentiere SHA-256 und Einzelfallvergleich mit dev5. Bekannte dev5-Findings QE01/02/03 bleiben offen, keine Erwartung von 35 PASS. AP2 bleibt offen. Prüfe insbesondere gruppierte Belege, falsche Zitate, gemischte Bearbeitungsaufträge und doppelte Quellenlisten als bekannte Risiken.
5. Prüfe ohne Architekturumbau, ob die Diagnose geeignet ist, Output-Truncation, Providerlatenz, Werkzeuglatenz und Kontextwachstum zu unterscheiden. Keine Live-Behauptungen auf Basis von Stubs. Zeitlimits nicht Teil dieses Prüflings.
6. Liefere Findings nach Schweregrad, reproduzierbare Schritte, erwartetes/tatsächliches Verhalten, Evidenz, minimalen Fixvorschlag. Trenne neue Regressionen von wieder sichtbaren bekannten dev5-Defiziten. Keine Änderungen am Repository, keine Freigabeentscheidung.

## Ausführung
Im Repo-Root:
```bash
export SG_PIPE=tools/local_dev/sourceguard_pipe_v0_5_5_dev11.py
python -m py_compile "$SG_PIPE"
python tests/local_dev/regression/test_ap1.py
python tests/local_dev/regression/test_dev11_metrics.py
python tests/local_dev/qe_reference/qe_tests.py
```
dev6–dev10-Regressionstests sind für diese bewusst zurückgesetzte Basis nicht als PASS-Gate definiert; ihre Findings sind weiterhin relevante offene Arbeitspunkte. SE hat die neue Version noch nicht ausgeführt. PO entscheidet über Abnahme und Folgearbeiten.
