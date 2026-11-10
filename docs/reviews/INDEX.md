# Reviews – Verzeichnis

**Zweck:** Ablage abgeschlossener Reviewberichte des unabhängigen Reviewers, damit Reviews reproduzierbar und überprüfbar bleiben (Arbeitsregel 8 des Auftragsdokuments).

**Ablageort:** `docs/reviews/` im jeweils zugehörigen Repository.
**Benennung:** `YYYY-MM-DD-review-<gegenstand>-<version>-<sha7>.md`
**Ablegeweg:** Der Bericht wird vom Product Owner entschieden und vom Software Engineer committet; der Reviewer legt keine Dateien selbst ab.

## Berichte

| Datum | Gegenstand | Geprüfter Stand | Gesamturteil | BLOCKER / MAJOR / MINOR | Status |
|---|---|---|---|---|---|
| 2026-11-10 | Requirements-Baseline v1.1.0 (THEOAgent) | `b3d901c` | Nicht freigabefähig als Architektur- und Abnahmegrundlage; freigabefähig als fachlicher Anforderungsumfang | 3 / 9 / 6 | Punkte offen – noch keine Rückmeldung des Software Engineers zu F-01 … F-18 |

## Offene Punkte des jüngsten Berichts

| ID | Priorität | Kurzgegenstand |
|---|---|---|
| F-01 | BLOCKER | 11 von 12 NFANF ohne Schwellenwert und Testkorpus |
| F-02 | BLOCKER | Keine messbare Anforderung gegen erfundene Fundstellen |
| F-03 | BLOCKER | Kein Datenmodell für Arbeitsfassung, Freigabe, Freeze |
| F-04 | MAJOR | Granularität und Format der Fundstelle undefiniert |
| F-05 | MAJOR | US-25 ohne deckende Funktion (Traceability formal erfüllt, inhaltlich nicht) |
| F-06 | MAJOR | Schrittweises Arbeiten nur für Predigten spezifiziert (FANF-14) |
| F-07 | MAJOR | „Unterstützte Dateiformate“ nirgends definiert |
| F-08 | MAJOR | GR-09 ↔ FANF-17 widerspruchsanfällig |
| F-09 | MAJOR | Keine Netzwerk- und Quellenzulassungspolicy |
| F-10 | MAJOR | Nutzungsrechte ohne Merkmal und ohne Prozess |
| F-11 | MAJOR | RANF-04 ohne Artefaktbindung (Fachstandard) |
| F-12 | MAJOR | Verwendete Ausgabe (Bibel/KKK/CIC) nicht anzuzeigen |
| F-13 … F-18 | MINOR | Terminologie, Testbarkeit, Kann-Formulierung, Redundanz, Herkunftsnachweis |

## Regeln für Einträge

- Berichte werden **nicht** nachträglich inhaltlich verändert. Korrekturen und Nachtragungen erfolgen als eigener Abschnitt im Bericht oder als Folgebericht mit neuem Datum.
- Jeder Bericht muss den geprüften Commit-SHA und die Git-Blob-Kennungen der geprüften Dateien nennen.
- Jeder Bericht kennzeichnet ausdrücklich, welche Tests **tatsächlich** ausgeführt wurden und welche PASS-Angaben nur berichtet sind.
- Ein grüner CI-Lauf ist keine fachliche Abnahme.
- Berichte enthalten keine Geheimnisse, keine personenbezogenen Daten und keine urheberrechtlich geschützten Volltexte.
