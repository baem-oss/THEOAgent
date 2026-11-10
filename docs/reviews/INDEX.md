# Reviews – Verzeichnis

**Zweck:** Ablage unabhängiger Prüfberichte als reproduzierbare **Review-Evidenz**. **Verbindliche Single Source of Truth ist das GitHub-Repository**, nicht der Reviewerbericht oder eine externe QE-Notiz. Die Projektregeln stehen in [WORKFLOW.md](../WORKFLOW.md).

**Ablageort:** `docs/reviews/` im jeweils zugehörigen Repository.
**Benennung:** `YYYY-MM-DD-review-<gegenstand>-<version>-<sha7>.md` (der Suffix bezeichnet den **tatsächlich geprüften Commit**, keine vom QE vorgegebene SHA).
**Ablegeweg:** Der Product Owner entscheidet über die Aufnahme und fachliche Freigabe; der Software Engineer committet. Der Reviewer hat keine Schreib-, Merge-, Hash- oder Freigabehoheit.

## Berichte

| Datum | Gegenstand | Geprüfter Stand | Gesamturteil | BLOCKER / MAJOR / MINOR | Status |
|---|---|---|---|---|---|
| 2026-11-10 | Requirements-Baseline v1.1.0 (THEOAgent) | `b3d901c` | Nicht freigabefähig als Architektur- und Abnahmegrundlage; freigabefähig als fachlicher Anforderungsumfang | 3 / 9 / 6 | Durch [Nachreview zu v1.2.0](2026-11-10-nachreview-requirements-v1.2.0-ab1b0aa.md) fortgeschrieben |
| 2026-11-10 | [Requirements-Nachreview v1.2.0](2026-11-10-nachreview-requirements-v1.2.0-ab1b0aa.md) | `ab1b0aa` | Freigabefähig als Requirements-Grundlage mit Hinweisen; keine Implementierungs-/Qualitätsabnahme | 0 / 1 / 2 **neue** Findings; 13 CLOSED, 2 PARTIAL, 3 OPEN aus Erstbericht | Durch [Nachprüfung N-01/F-14](2026-11-10-review-nachpruefung-n01-f14-v1.2.0-9c020fe.md) fortgeschrieben |
| 2026-11-10 | [Nachprüfung N-01 und F-14](2026-11-10-review-nachpruefung-n01-f14-v1.2.0-9c020fe.md) | `9c020fe` | Beide Findings CLOSED; Requirements-Freigabe empfohlen, keine Implementierungs-/Qualitätsabnahme | N-01 CLOSED / F-14 CLOSED | Archiviert; PO-Freigabe am 10.11.2026 erteilt |


## Freigabe der Requirements-Baseline v1.2.0

**Product-Owner-Entscheidung vom 10.11.2026:** Die fachliche Requirements-Baseline **v1.2.0 ist freigegeben** und wurde mit [PR #1](https://github.com/baem-oss/THEOAgent/pull/1) in `main` übernommen (Merge-Commit [`5c041389`](https://github.com/baem-oss/THEOAgent/commit/5c04138946827bc73a04e3ba266cea932027f473)). Diese Freigabe betrifft **die Requirements**, nicht Implementierung, Realtests, Produktqualität oder die noch offenen Qualitätsgrenzwerte.

Die verbleibenden Prüfpunkte bleiben nachvollziehbar, sind aber vom Product Owner **nicht** als Hindernis für die fachliche Freigabe eingestuft. Die unveränderten Berichte dokumentieren ihre jeweiligen historischen Prüfstände.

## Findings-Status nach der Nachprüfung

| ID | Reviewstatus | Kurzgegenstand |
|---|---|---|
| N-01 | CLOSED | Freigabe als Funktion in FANF-18 spezifiziert und durch T-05 prüfbar |
| N-02 | MINOR – neu | „Vorlagen“ in US-23 nicht ausdrücklich als Arbeitsfassung eingeordnet |
| N-03 | MINOR – neu | RANF-06 vermischt Formatumfang mit dem Verbot fingierter Volldokumentlektüre |
| F-01 | PARTIAL | Elf Qualitätsgrenzwerte und Testkorpora bleiben bis zur PO-Entscheidung offen |
| F-18 | PARTIAL | Verbindliche Fachstandardfassung und Herkunftsnachweis noch zu entscheiden |
| F-14 | CLOSED | Kontextbezogene Lesepflicht in FANF-05 und Negativtest T-02 |
| F-16 | OPEN – MINOR | Formulierung der Datenanforderungen „zuordnen können“ |
| F-17 | OPEN – MINOR | Abgrenzung Fachregel / Qualitätsanforderung nicht explizit erläutert |

**Historische Übergabeabweichung (Nachreview):** Eine vom QE mitgeteilte externe SHA-256-Prüfsumme stimmte nicht mit dem empfangenen Bericht überein. Der Bericht wurde als empfangene Fassung archiviert; sein Git-Blob lautet `4da57bb00cc479d1e9835dabe273a0ffc1c6b5be`. **Das ist keine offene Freigabesperre und keine Autorität des QE über den Repositoryinhalt.** Maßgeblich ist die tatsächlich in GitHub abgelegte Fassung. Der Widerspruch bleibt als Transport-/Provenienznotiz dokumentiert, nicht als Anforderung zur nachträglichen Veränderung des Berichts.

## Regeln für Einträge

- Archivierte Berichte werden **nicht** nachträglich inhaltlich verändert. Korrekturen werden in einem gesonderten, datierten Folgedokument festgehalten; nur das Verzeichnis wird fortgeschrieben.
- Jeder Bericht nennt, **soweit ermittelbar**, den tatsächlich geprüften Commit und die Git-Blob-Kennungen der Prüfobjekte als reine Herkunftsangaben. Der QE darf keine SHA-Werte vorgeben und keine außerhalb des Repos errechnete Prüfsumme zur maßgeblichen Projektversion erklären.
- Jeder Bericht kennzeichnet ausdrücklich, welche Tests **tatsächlich** ausgeführt wurden und welche PASS-Angaben nur berichtet sind.
- Ein grüner CI-Lauf und ein positives QE-Urteil sind keine fachliche Abnahme. Die Freigabe trifft ausschließlich der Product Owner und wird im Repository nachvollziehbar dokumentiert.
- Berichte enthalten keine Geheimnisse, keine personenbezogenen Daten und keine urheberrechtlich geschützten Volltexte.
