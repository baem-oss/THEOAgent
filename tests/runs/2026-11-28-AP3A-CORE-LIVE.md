# AP3a – Core v0.1.0: Live-Smoke-Test ohne Werkzeuge

28.11.2026. PO führte den Test auf dem lokalen OpenWebUI-System aus und übermittelte Antwort und Diagnose. SE hat keinen eigenen Zugriff auf den Homeserver. Referenzumgebung laut PO: OpenWebUI 0.11.4, google/gemma-4-31b-it über OpenRouter. Installationsreferenz: tools/local_dev/sourceguard_v2_core.py, Commit fc7d0281c4c57a18ca0fa4c8eb751ee9647bf760. Installierter Code nicht unabhängig per Hash verifiziert. Vorheriger HEAD 1f4cc9dbb984f38d31ee7830310be89c712b58dd.

## Konfiguration

PO-Screenshot zeigt TARGET_MODEL_ID google/gemma-4-31b-it, SYNTHETIC_DEV_ENABLED true, ENABLE_NATIVE_TOOLS false, INPUT_BYTES 48000, MAX_OUTPUT_TOKENS 4096, SHOW_DIAGNOSTICS true. Vorgabe: keine Fachbibliothek, keine Skills, keine Websuche, leerer Systemprompt; deren effektive Zuweisung nicht separat verifiziert. Ausschließlich synthetischer Testauftrag. Die Diagnose belegt keine Tool-Aufrufe durch den Core.

## Testauftrag

Formuliere drei kurze, lebensnahe Fürbitten für eine katholische Kindertaufe.

## Tatsächliche Diagnose (PO-Protokoll)

```json
{"version":"0.1.0","events":[{"event":"model_response","ms":4416.5,"prompt_tokens":1981,"finish_reason":"stop"}],"model_calls":1,"tool_calls":0,"status":"COMPLETED","reason":"stop","duration_ms":4416.9}
```

## Ergebnis: PASS (Smoke-Orakel)

Ein Modellaufruf, null Werkzeugaufrufe, regulärer Abschluss, drei verständliche und grundsätzlich verwendbare Fürbitten. Themen: Kind, Eltern/Paten, Kinder weltweit. Kleinere sprachliche Schwäche (ihm/ihr), kein relevanter Fehler für dieses Smoke-Orakel. Keine erkennbare Antwortunterdrückung oder vorgetäuschte Quellenprüfung. Kein fachlicher Abnahmelauf AP4/AP7. Gemessene Core-Dauer 4.4169 s; Differenz zur gemeldeten Modellzeit 0.4 ms, nicht gesamte Plattform-Overheadmessung. Q-09-Zielwert einfach 10 s im Core-Messbereich unterschritten; keine E2E-Abnahme. Prompt-Tokens 1981; Ursache/Anteil des Plattformkontexts nicht separat gemessen. Erfolgreiche Function-Ausführung spricht für vorhandene Importabhängigkeiten, Versionen nicht separat geprüft.

AP3a: implementiert, 10 synthetische Offline-Tests PASS laut vorherigem Bericht, Live-Smoke ohne Tools PASS. Keine erneute Offline-Testausführung in diesem Schritt. Keine allgemeine Schutzabnahme, kein Nachweis des neuen Core mit nativen Knowledge-Tools, kein Nachweis von Freeze, Folgeprovenienz, W2-Rechten oder DRS:KI-Integration.

## Disposition

AP3a im vorgesehenen Umfang abgeschlossen. Nächster Schritt AP3b: vorhandene native Knowledge-/Skill-Werkzeuge und nutzbare antwortbezogene Herkunft im neuen Core; gezielter integrierter Test mit autorisierten synthetischen Daten. Kein erneuter isolierter AP2-Kommunikationsnachweis. Vertrauenswürdige Zielumgebung gemäß Architektur Rev.3 §9, keine zusätzliche Sicherheitsinfrastruktur. Vor geschützten extern übermittelten Fachtexten Rechte-/Providerklärung. Keine Produktfreigabe oder Baseline-Änderung.