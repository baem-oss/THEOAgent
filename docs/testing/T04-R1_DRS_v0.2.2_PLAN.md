# T-04-R1 – Gezielter DRS:KI-Wiederholungstest unter v0.2.2

**Status:** NOT_RUN / geplant · **Branch:** `drs-ki-test` · **Datum Planung:** 12.11.2026

## Ziel

Prüfen, ob der Assistent **ohne Nutzerintervention** den Inhalt des hochgeladenen Korpus tatsächlich liest und alle acht Aussagen korrekt klassifiziert, und ob die neue bedingte Werkzeugregel sichtbar befolgt wird. Zwei getrennte Prüfdimensionen: **fachliche Quellenintegrität** und **Werkzeug-/Recovery-Verhalten**.

## Unveränderte Bestandteile

- Einziger Upload: `tests/fixtures/t04/belegkorpus.md`
- Wortgleicher Nutzerprompt: `docs/testing/T04_DRS_PROMPT.md`, Abschnitt **Nutzerprompt** (keine erklärenden Zusätze)
- Fixiertes Bewertungsorakel: `tests/oracles/T04_DRS_ORACLE.md` (**nicht** an den Testling übermitteln)
- Neuer Chat im DRS:KI-Allrounder; nutzerseitiges Systemprompt-Feld mit dem vollständigen `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.2.2.md`; tatsächlichen Einbringungsweg und Modell, soweit sichtbar, protokollieren.
- Keine weiteren Quellen, kein nachträgliches Umformulieren der acht Behauptungen.

## Zu erfassender Ablauf

1. Upload- und Extraktionsanzeige, Dateiname.
2. **Erster sichtbarer Werkzeugname** und, wenn verfügbar, seine Eingabe/Dateireferenz.
3. Erscheint `view_knowledge_file`? Als erstes Leseinstrument oder als gezielter Ausweichweg **nach** `analyze_uploaded_documents`? Falls nicht: Aus den sichtbaren Daten **nicht** einfach schließen, dass das Werkzeug verfügbar war.
4. Bei Analysefehlern genau die Werkzeugmeldung und die folgenden Schritte sichern; keine eigenständige Nutzerkorrektur vor Sicherung des Erstlaufs.
5. Gesamte Erstantwort sichern: acht Klassifikationen, konkrete Abschnittsfundstellen, alle Zitate, Quellenstatus.
6. Nach dem Erstlauf gesondert dokumentierte Nutzerinterventionen sind **separate Diagnosefortsetzungen**, keine Reparatur des autonomen Erstlauf-Ergebnisses.

## Bewertung

Das fachliche PASS/PARTIAL/FAIL/BLOCKED/NOT_RUN ergibt sich **ausschließlich** aus dem bereits fixierten `T04_DRS_ORACLE.md`. In insbesondere **Aussage 6** ist „Werk nicht im Korpus“ nicht mit „Werk existiert nicht / Behauptung widerlegt“ gleichzusetzen. Ein zweites unabhängiges Feld beschreibt die Werkzeugstrategie: `view_knowledge_file` zuerst / nach `analyze_uploaded_documents` / nicht sichtbar / nicht verfügbar / unklar. Kein stillschweigendes PASS der Werkzeugregel nur aufgrund fachlich korrekter Ausgabe.

## Aussagekraft

Auch bei PASS bleibt die ursächliche Wirkung von Werkzeugreihenfolge, Promptkürzung, anderen fachlichen Regeln und möglichem Modell-/Backend-Wechsel **unbestimmt**; diese Variablen wurden nicht isoliert. Eine A/B-Testreihe mit identischen Rahmenbedingungen wäre für Kausalzuschreibungen nötig. Dieser einzelne Test liefert eine pragmatische operative Diagnose.
