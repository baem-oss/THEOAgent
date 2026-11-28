# AP3a – SourceGuard v2 Core: Offline-Teststand

Datum: 28.11.2026 (Projektzeit). PO-Freigabe AP3a im Projektchat. Ausgangsstand 2b9d56fe5a47c9c46e8135e83a2877ea18c9960d, Architektur Rev.3 inkl. §9. Keine Änderung an Baseline oder main.

## Artefakte

- tools/local_dev/sourceguard_v2_core.py, v0.1.0, Commit fc7d0281c4c57a18ca0fa4c8eb751ee9647bf760, Git-Blob 51ef573c5f43aa5efc957c2289da7090bac8ce07.
- tests/local_dev/test_sourceguard_v2_core.py, Commit f219b633fcc57b8101c24da4c9e06b630dabd91b, Git-Blob 144a9573e5695626beb4840f8c098fbd23180731.

Beide Repository-Blobs stimmen mit den lokal mittels git hash-object identifizierten tatsächlich getesteten Dateien überein. Historische Probes unverändert.

## Ausführung

Isolierte SE-Python-Umgebung, Python 3.13.5, pydantic 2.13.5, jsonschema 4.26.0; keine OpenWebUI-/Provider-Verbindung. Abhängigkeit jsonschema in OWUI-Zielumgebung noch zu prüfen. Befehle aus temporärem Projektverzeichnis mit den zwei Dateien in Repository-Struktur:
- python -m py_compile tools/local_dev/sourceguard_v2_core.py – PASS
- python -m unittest discover -s tests/local_dev -v – 10 Tests in 0.026 s, OK (nur neue Tests in diesem Verzeichnis; nicht die gesamte Repo-Suite).

| Test | Ergebnis |
|---|---|
| test_no_tools | PASS |
| test_roundtrip | PASS |
| test_rejected_and_error | PASS (unzulässiges Tool, ungültiger Typ, Callable-Fehler) |
| test_invalid_ids | PASS |
| test_retry | PASS (Timeout, einmalige Wiederholung) |
| test_context | PASS |
| test_budget | PASS |
| test_secrets | PASS (expliziter synthetischer Canary) |
| test_truncated_and_filter | PASS |
| test_disabled_profile | PASS |

## Umsetzung und Grenzen

Native Schleife auf Basis der Probe, Tool-Schema/Typprüfung über jsonschema, feste Allowlist der fünf Knowledge-/Skill-Tools, optionale Diagnose ohne Rohtexte, einfache UTF-8-Byte-Grenze und Ausgabe-Tokenlimit, Fehlerübergabe, einmaliger Retry im Lauf und begrenzter Abschlussversuch bei Budget/ungültigen IDs. Kein Pflichttool, keine fest verdrahtete fachliche Arbeitsanweisung, kein Web. Status COMPLETED bedeutet regulärer Textabschluss, nicht fachliche Verifikation. submitted bedeutet Aufruf des Modelladapters mit Rückgabe im Request, nicht bewiesene Providerverarbeitung; response_received bedeutet Antwort des Adapters. Keine Behauptung vollständiger Lektüre. Bei nicht erreichbarem Modell derzeit allgemeine technische Einschränkung, keine kontextspezifische Teilantwortrekonstruktion. Bytebudget ist konservativer konfigurierbarer Näherungswert, keine exakte Modelltokenisierung. Der Secret-Canary-Test prüft explizit übergebenes Testgeheimnis; Adapter übergibt keine Liste produktiver Geheimnisse. Keine umfassende SP-04-Abnahme.

DEV standardmäßig deaktiviert, native Tools separat deaktiviert. Aktivierung ausschließlich nach Betreiberbestätigung eines isolierten synthetischen Profils und zulässigen Providers, keine allgemeine Rechtefreigabe; keine neuen ACL. Keine echten Fachbibliotheken oder vertraulichen Eingaben im AP3a-Live-Test. Berechtigungen, Plattform-Datenfluss, W2-Modellwechsel, tatsächliche Dokumentidentität und Herkunft, Folgeprovenienz, Freeze, Anhänge, Web sowie reale Modellfehlerpfade nicht nachgewiesen. Keine Produktivsetzung. Lokaler OWUI-Adapter und dessen Versions-/Schema-/Task-Vertrag NOT_RUN. Historische Probe-Unit-Tests nicht erneut ausgeführt.

## Nächster Schritt

Gezielter AP3a-Live-Smoke-Test des neuen Codes in OWUI 0.11.4, zunächst ohne Knowledge, Skills, Web oder andere Tools und ausschließlich synthetische Eingaben. Bei Importfehler insbesondere jsonschema prüfen; kein ungefragter Infrastrukturumbau. Danach bei autorisiertem synthetischem Profil ein integrierter Tool-Lauf im Rahmen AP3b, keine allgemeine Wiederholung von AP2. Technische Diagnose für Smoke aktivieren. Keine fachliche oder Sicherheitsabnahme.
