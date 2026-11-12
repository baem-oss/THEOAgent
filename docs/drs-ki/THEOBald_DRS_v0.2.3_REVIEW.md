# THEOBald DRS – Minimaländerung v0.2.3

**Stand:** 12.11.2026 · **Branch:** `drs-ki-test` · **Status:** ungetesteter Kandidat.

## Ausgangsbefund

`tests/runs/2026-11-12-DRS-T04-R1-v0.2.2.md`: direkter sichtbarer Aufruf von `view_knowledge_file`, aber **FAIL (6/8)**. Nr. 5: explizit fehlende empirische Befunde fälschlich „nicht überprüfbar“; Nr. 7: der Satz wurde zutreffend in § 4.1 gefunden, die Behauptung „steht in § 3.1“ dennoch als „belegt“ bewertet.

## Inhaltliche Änderung

**Nur die Negativ- und Gesamtbehauptungsregel wird fachlich verändert:** Beurteilt wird jede Behauptung samt ihrem Inhalt, Fundstelle, Quantifizierungen und Schlussfolgerung. **Belegt** nur bei vollständigem Nachweis; **widerlegt** bei mindestens einem durch die Quelle falsifizierten Bestandteil; **nicht überprüfbar** bei entscheidend fehlender Evidenz ohne Gegenbeleg. Das Nichtvorkommen eines externen Werks im Korpus widerlegt keine allgemeine Aussage über dieses Werk.

Die redaktionellen Straffungen anderer Abschnitte dienen nur der Länge. Werkzeugweg, sieben Fachverfahren, Quellenordnung und Freeze-Regeln sind inhaltlich unverändert.

## Testdesign und Grenze

`docs/testing/T04-R2_DRS_v0.2.3_PLAN.md` verwendet die **unveränderte** Datei `tests/fixtures/t04/belegkorpus.md`, denselben T-04-Nutzerprompt und das fixierte `tests/oracles/T04_DRS_ORACLE.md`. Primärer Fokus Nr. 5, 6, 7; alle 8 für Gesamtbewertung. Eine einzelne erfolgreiche Wiederholung beweist noch keine kausale Wirkung gegenüber v0.2.2.

## Umfang

v0.2.2: 9986 Zeichen; v0.2.3: 10000 Zeichen. **Noch nicht getestet.** Keine Änderung an `main`, Testkorpus oder Orakel.
