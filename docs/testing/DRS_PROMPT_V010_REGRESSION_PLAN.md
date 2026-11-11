# DRS:KI – Regressionstest THEOBald DRS v0.1.0

**Stand:** 2026-11-11 · **Branch:** `drs-ki-test` · **Status:** vorbereitet, keine Läufe durchgeführt.

**Änderung gegenüber Baseline:** `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.1.0.md`. Sonstige Konfiguration unverändert, soweit kontrollierbar. Unbekannt: effektive Modell-/Provider-ID, Systemrollen-Priorität und tatsächliche Toolverfügbarkeit.

**Konfiguration vor Lauf festhalten:** Wurde Text in ein echtes Systemprompt-Feld eingetragen, als benutzerseitige Custom Instructions gesetzt oder als gewöhnliche Chatnachricht gesendet? Letzteres ist als `chat-instruction` gesondert zu kennzeichnen, nicht als bestätigter Systemprompt-Test.

## Regression und Reihenfolge

1. `T-08-A/B-R1` – Quellenintegrität und Framing. Wortgleiche Prompts aus `docs/testing/T08_DRS_EXECUTION_SCRIPT.md`; getrennte frische Chats, pro Chat gleiche Prompt-Konfiguration. Fixiertes Orakel `tests/oracles/T08_DRS_ORACLE.md`.
2. `T-05-R1` – Freeze/Freigabe. Alle sechs unveränderten Stufen aus `docs/testing/T05_DRS_EXECUTION_SCRIPT.md`, in **einem** frischen Chat, nie zwischen Stufen wechseln; Orakel `tests/oracles/T05_DRS_ORACLE.md`.
3. `T-04-R1` – Dokumentenzitate. Identische hochgeladene Testfixture und identischer Fragenkatalog des ursprünglichen T-04; Fixierung in Baseline-Protokoll.
4. `T-03-P-R1` – Recherche amtlicher Normen. Exakt gleiche Fragestellung wie Baseline T-03; Referenz `tests/runs/2026-11-11-DRS-T03-P.md`; amtliche Primärtextprüfung im Orakel.

**Beweissicherung:** vollständiger DRS-Output, sichtbare Werkzeuge, Auffälligkeiten, tatsächlicher Prompt-Kanal, Testkennung und Bewertung separat festhalten. Die Orakel nicht anpassen. Kein PASS durch bloße bessere Selbstdarstellung. Keine Änderungen an Baseline oder `main`.

**Falsifizierbarkeit:** Verbesserungen dürfen nur für geprüfte Testfälle und das tatsächlich beobachtete Setup behauptet werden. Eingefügter Systemprompt-Text als normale Nachricht ist kein nachgewiesener Systemrollen-Prompt.
