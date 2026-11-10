# Reviews – Verzeichnis

**Zweck:** Ablage abgeschlossener Reviewberichte des unabhängigen Reviewers, damit Reviews reproduzierbar und überprüfbar bleiben (Arbeitsregel 8 des Auftragsdokuments).

**Ablageort:** `docs/reviews/` im jeweils zugehörigen Repository.
**Benennung:** `YYYY-MM-DD-review-<gegenstand>-<version>-<sha7>.md`
**Ablegeweg:** Der Bericht wird vom Product Owner entschieden und vom Software Engineer committet; der Reviewer legt keine Dateien selbst ab.

## Berichte

| Datum | Gegenstand | Geprüfter Stand | Gesamturteil | BLOCKER / MAJOR / MINOR | Status |
|---|---|---|---|---|---|
| 2026-11-10 | Requirements-Baseline v1.1.0 (THEOAgent) | `b3d901c` | Nicht freigabefähig als Architektur- und Abnahmegrundlage; freigabefähig als fachlicher Anforderungsumfang | 3 / 9 / 6 | Durch [Nachreview zu v1.2.0](2026-11-10-nachreview-requirements-v1.2.0-ab1b0aa.md) fortgeschrieben |
| 2026-11-10 | [Requirements-Nachreview v1.2.0](2026-11-10-nachreview-requirements-v1.2.0-ab1b0aa.md) | `ab1b0aa` | Freigabefähig als Requirements-Grundlage mit Hinweisen; keine Implementierungs-/Qualitätsabnahme | 0 / 1 / 2 **neue** Findings; 13 CLOSED, 2 PARTIAL, 3 OPEN aus Erstbericht | Review abgeschlossen; N-01 und F-14 vor Architektursign-off klären |

## Offene Punkte des jüngsten Berichts

| ID | Reviewstatus | Kurzgegenstand |
|---|---|---|
| N-01 | MAJOR – neu | Freigabe einer Arbeitsfassung in FANF-18 noch nicht als eigene Nutzermöglichkeit spezifiziert |
| N-02 | MINOR – neu | „Vorlagen“ in US-23 nicht ausdrücklich als Arbeitsfassung eingeordnet |
| N-03 | MINOR – neu | RANF-06 vermischt Formatumfang mit dem Verbot fingierter Volldokumentlektüre |
| F-01 | PARTIAL | Elf Qualitätsgrenzwerte und Testkorpora bleiben bis zur PO-Entscheidung offen |
| F-18 | PARTIAL | Verbindliche Fachstandardfassung und Herkunftsnachweis noch zu entscheiden |
| F-14 | OPEN – MINOR | Bedeutung von „ausreichendem Kontext“ bei Originallektüre nicht festgelegt |
| F-16 | OPEN – MINOR | Formulierung der Datenanforderungen „zuordnen können“ |
| F-17 | OPEN – MINOR | Abgrenzung Fachregel / Qualitätsanforderung nicht explizit erläutert |

**Dateiintegrität des Nachreviews:** Der archivierte Upload ist 17.024 Byte groß und hat SHA-256 `28b8a9072f25227639addba3380c7829d4dc53a8c5ae2367295fa16676e0b2b8` (Git-Blob `4da57bb00cc479d1e9835dabe273a0ffc1c6b5be`). Im Bericht selbst wird abweichend 16.219 Byte und SHA-256 `04484ea4809ba6b39ed5d281cef0d34a6cf36675bb8d70b3c201874c1e465320` genannt. Der hochgeladene vollständige Bericht wurde **ohne Änderung** archiviert; die Übereinstimmung mit der vom Reviewer angekündigten Ausgangsdatei ist nicht nachgewiesen.

## Regeln für Einträge

- Berichte werden **nicht** nachträglich inhaltlich verändert. Korrekturen und Nachtragungen erfolgen als eigener Abschnitt im Bericht oder als Folgebericht mit neuem Datum.
- Jeder Bericht muss den geprüften Commit-SHA und die Git-Blob-Kennungen der geprüften Dateien nennen.
- Jeder Bericht kennzeichnet ausdrücklich, welche Tests **tatsächlich** ausgeführt wurden und welche PASS-Angaben nur berichtet sind.
- Ein grüner CI-Lauf ist keine fachliche Abnahme.
- Berichte enthalten keine Geheimnisse, keine personenbezogenen Daten und keine urheberrechtlich geschützten Volltexte.
