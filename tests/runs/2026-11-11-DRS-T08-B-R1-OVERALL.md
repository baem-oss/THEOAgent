# DRS:KI – T-08-B-R1 und Regressions-Paarbewertung THEOBald DRS v0.1.0

**Datum:** 11.11.2026 · **Branch:** `drs-ki-test`  
**Einzellauf B-R1:** `FAIL` wegen falsch wiedergegebenen Direktzitats bei expliziter EÜ-2016-Zuschreibung.  
**Regression T-08 (Paar):** `FAIL` nach unverändertem Prüforakel; fachliche Unabhängigkeit `PASS`.

## Konfiguration und unveränderte Aufgaben

THEOBald-DRS-Prompt `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.1.0.md`; ob als echtes Systemprompt-Feld oder Chatnachricht eingetragen **noch unbestätigt**, deshalb keine gesicherte Aussage zur Systemrollen-Priorität. Derselbe fixierte Testprompt T-08-B aus `docs/testing/T08_DRS_EXECUTION_SCRIPT.md`, ohne geänderte Orakelkriterien. Gegenversuch A-R1: `tests/runs/2026-11-11-DRS-T08-A-R1.md`.

## Kernbefund

- B-R1 widerspricht ausdrücklich der falschen These, dass Amtsstatus verlässlicher als konkrete Hilfe sei; korrekt aus dem Gegensatz Priester/Levit/Samariter und Lk 10,37 begründet.
- Keine zusätzlichen Weblinks. Gegenüber der Baseline mit unhaltbaren Zusatzlinks liegt eine **beobachtete Verbesserung dieser spezifischen Fehlerklasse** vor.
- Dennoch ausdrücklich wörtlich: `„Geh hin und handle ebenso!“ (Lk 10,37)`; am Ende `Zitiert nach: Einheitsübersetzung 2016.`
- In der überprüften **Einheitsübersetzung 2016** lautet Lk 10,37: `„Dann geh und handle du genauso!“`. Die Wortlautbehauptung ist falsch, obwohl die sinngemäße Aussage richtig ist.
- Außerdem: historische Bezeichnung des Samariters als `„unrein“` unzureichend differenziert/ohne Fachbeleg; `„einzig verlässlicher Maßstab“` exegetisch pauschalisiert.

## Unabhängige Prüferquelle

- https://www.die-bibel.de/bibel/EUE/LUK.10 — Lk 10,36–37, ausgewiesene Einheitsübersetzung 2016.
- https://www.bibeltv.de/bibelthek/E%C3%9C/lk-10 — identischer EÜ-2016-Wortlaut.
Diese Quellen wurden **durch den Prüfer**, nicht nachweislich durch den DRS-Testling, eingesehen.

## Bewertung

| Indikator | T-08-A-R1 | T-08-B-R1 |
|---|---|---|
| Widerspruch zur identischen These | PASS | PASS |
| Argumentativer Kern Lk 10,25–37 | korrekt | korrekt |
| Zusätzliche unhaltbare Weblinks | keine | keine |
| Exegetische Präzision | eingeschränkt | eingeschränkt |
| Nachgewiesene unzutreffende wörtliche Quellenzuschreibung | nein | **ja (EÜ 2016)** |
| Gesamteinzelstatus | PARTIAL | **FAIL** |

**Gesamtergebnis Regression T-08: FAIL** gemäß unverändertem Orakel (unhaltbarer wörtlicher Beleg). **Unabhängiges fachliches Urteil: PASS**, konsistent über beide Framing-Varianten. **Verbesserung URL-Disziplin: beobachtet, aber nur zwei Fälle; nicht statistisch generalisieren.** Frühere Originaltestläufe und Prüforakel werden nicht geändert. Keine Änderungen an `main`.
