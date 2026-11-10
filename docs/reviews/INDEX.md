# Reviews – Verzeichnis

**Zweck:** Ablage unabhängiger Prüfberichte als reproduzierbare **Review-Evidenz**. **Verbindliche Single Source of Truth ist das GitHub-Repository**, nicht der Reviewerbericht oder eine externe QE-Notiz. Die Projektregeln stehen in [WORKFLOW.md](../WORKFLOW.md).

**Ablageort:** `docs/reviews/` im jeweils zugehörigen Repository.
**Benennung:** `YYYY-MM-DD-review-<gegenstand>-<version>-<sha7>.md` (der Suffix bezeichnet den **tatsächlich geprüften Commit**, keine vom QE vorgegebene SHA).
**Ablegeweg:** Der Product Owner entscheidet über die Aufnahme und fachliche Freigabe; der Software Engineer committet. Der Reviewer hat keine Schreib-, Merge-, Hash- oder Freigabehoheit.

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

**Historische Übergabeabweichung (Nachreview):** Eine vom QE mitgeteilte externe SHA-256-Prüfsumme stimmte nicht mit dem empfangenen Bericht überein. Der Bericht wurde als empfangene Fassung archiviert; sein Git-Blob lautet `4da57bb00cc479d1e9835dabe273a0ffc1c6b5be`. **Das ist keine offene Freigabesperre und keine Autorität des QE über den Repositoryinhalt.** Maßgeblich ist die tatsächlich in GitHub abgelegte Fassung. Der Widerspruch bleibt als Transport-/Provenienznotiz dokumentiert, nicht als Anforderung zur nachträglichen Veränderung des Berichts.

## Regeln für Einträge

- Archivierte Berichte werden **nicht** nachträglich inhaltlich verändert. Korrekturen werden in einem gesonderten, datierten Folgedokument festgehalten; nur das Verzeichnis wird fortgeschrieben.
- Jeder Bericht nennt, **soweit ermittelbar**, den tatsächlich geprüften Commit und die Git-Blob-Kennungen der Prüfobjekte als reine Herkunftsangaben. Der QE darf keine SHA-Werte vorgeben und keine außerhalb des Repos errechnete Prüfsumme zur maßgeblichen Projektversion erklären.
- Jeder Bericht kennzeichnet ausdrücklich, welche Tests **tatsächlich** ausgeführt wurden und welche PASS-Angaben nur berichtet sind.
- Ein grüner CI-Lauf und ein positives QE-Urteil sind keine fachliche Abnahme. Die Freigabe trifft ausschließlich der Product Owner und wird im Repository nachvollziehbar dokumentiert.
- Berichte enthalten keine Geheimnisse, keine personenbezogenen Daten und keine urheberrechtlich geschützten Volltexte.
