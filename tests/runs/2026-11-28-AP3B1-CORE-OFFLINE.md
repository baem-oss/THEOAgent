# AP3b.1 – SourceGuard v2 Core v0.2.0: Offline-Test

28.11.2026 (Projektzeit). Prüfstand dev-v2 c988338953a12d04d5fa492e0a340b63f5671b99. SE hat die Tests tatsächlich in isolierter Python-Umgebung ausgeführt. Kein externer Modell-/OWUI-Aufruf.

## Identität und Ausführung

Aus den vorhandenen lokalen AP3a-Dateien wurde der AP3b.1-Stand anhand der abgerufenen Repository-Inhalte rekonstruiert. Beide Git-Blob-SHAs wurden mit git hash-object geprüft und stimmen exakt mit dem Repository überein:
- tools/local_dev/sourceguard_v2_core.py: b1a1ee62b43e133ec79877c374cc76f233da5bff
- tests/local_dev/test_sourceguard_v2_core.py: 45ea3961ef444bc1baa2b98af10e5b91204fcc87

Python 3.13.5, pydantic 2.13.5, jsonschema 4.26.0. Befehle aus isoliertem Verzeichnis mit beiden Dateien in Repository-Struktur:

- python -m py_compile tools/local_dev/sourceguard_v2_core.py tests/local_dev/test_sourceguard_v2_core.py: PASS.
- python -m unittest discover -s tests/local_dev -v: 15 Tests, 0.032 s, OK. Nur Core-Suite, nicht das gesamte historische Repository.

## Tatsächliche Testausgabe (Kurzform)

| Test | Ergebnis |
|---|---|
| test_budget | PASS |
| test_context | PASS |
| test_disabled_profile | PASS |
| test_followup_no_new_read | PASS |
| test_invalid_ids | PASS |
| test_no_provenance_for_error_or_oversize | PASS |
| test_no_tools | PASS |
| test_read_provenance | PASS |
| test_read_unknown_identity | PASS |
| test_rejected_and_error | PASS |
| test_retry | PASS |
| test_roundtrip | PASS |
| test_secrets | PASS |
| test_truncated_and_filter | PASS |
| test_unsubmitted_read_not_displayed | PASS |

Ran 15 tests in 0.032s

OK

## Bewertung und Grenzen

Alle zehn AP3a-Regressionsfälle und fünf AP3b.1-Fälle bestanden. Provenienz aus strukturierten synthetischen Tool-Rückgaben, unbekannte Identität, Fehler/Übergröße und nicht gesendete Abrufe korrekt im getesteten Umfang. Folgefrage-Test prüft Weitergabe des Verlaufes und fehlende neue Abrufanzeige anhand eines Modell-Stubs, nicht tatsächliche Modellinterpretation. Keine Aussage zur realen Metadatenstruktur oder Plattformpersistenz. Kein fachlicher Abnahmenachweis, kein Freeze-, Web-, ACL- oder Datenschutznachweis. Keine Codeänderung erforderlich für diese Tests. Nächster Schritt integrierter Live-Test mit synthetischer Markdown-Quelle und Folgefrage, keine geschützte Fachbibliothek bis geklärter Übermittlungsfreigabe. Native Skills können bei autorisiertem synthetischem Profil getestet werden. AP3b.2 bleibt offen. Keine Produktfreigabe oder Baseline-Änderung.
