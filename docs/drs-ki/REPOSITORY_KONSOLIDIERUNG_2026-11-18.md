# GitHub-Konsolidierung – Branch- und Dokumentationsinventar

**Stand:** 18.11.2026 · **Repository:** `baem-oss/THEOAgent` · **Arbeitsbranch:** `drs-ki-test`  
**Status:** Durch GitHub-API verifizierte Bestandsaufnahme und nicht-destruktive Navigationskonsolidierung. **Keine Branchlöschungen, keine Merges nach `main`, keine Freigabe- oder Baselineänderung.** Branch-Stände beziehen sich auf die unten genannten Commit-SHAs zum Prüfzeitpunkt, nicht auf eine dauerhafte Zusicherung.

## 1. Leitentscheidung: zwei dauerhafte Hauptlinien

- **`main`**: PO-freigegebene Requirements-Baseline v1.2.0 und genehmigter Projektstand. HEAD `15326fe465275c2b774ab864a8da02799be9bf5c`. Keine ungeprüfte Zusammenführung von DEV-Artefakten.
- **`drs-ki-test`**: laufende DRS:KI-DEV-Entwicklung, Tests, Tool-/Skill-/Prompt-Prototypen und historische Nachweise. HEAD **vor dieser Dokumentationskonsolidierung** `b0ba67db2f6cee6ad7282268a1b49d1eb178ff44`.
- Das Repository ist die technische SSOT; eine Branch-Gleichheit oder ein Merge stellt **keine** fachliche Produktfreigabe dar.

## 2. Alle neun Branches bei Bestandsaufnahme

Vergleich jeweils gegen `main` (GitHub Compare API); `ahead`/ `behind` sind Commit-Zahlen, nicht Anzahl freigegebener Änderungen.

| Branch | HEAD (kurz) | Gegenüber `main` | Bewertung / Vorschlag |
|---|---|---|---|
| `main` | `15326fe` | Referenz | **Behalten** (PO-freigegeben) |
| `drs-ki-test` | `b0ba67d` | diverged; +188 / -1 | **Behalten** (aktiver DEV-Branch) |
| `docs/drs-ki-repo-pflege` | `1fe55f1` | diverged; +152 / -1 | Technischer Vorläufer von `drs-ki-test`; vollständig enthalten; **Löschkandidat nach PO-Zustimmung** |
| `docs/fachstandard-repo-pflege` | `15326fe` | identical; +0 / -0 | Mit `main` identisch; **Löschkandidat** |
| `review/requirements-v1.2.0-qs` | `6ddee49` | behind; +0 / -20 | Historischer, in `main` aufgegangener Reviewbranch; **Löschkandidat**, Reviews in `docs/reviews/` erhalten |
| `test/t01-t03-diagnostics-v1` | `2fb93a9` | behind; +0 / -7 | Historischer, in `main` aufgegangener Diagnosebranch; **Löschkandidat** |
| `test/t02-execution-2026-11-11` | `d0ca2c5` | behind; +0 / -2 | PR #3 gemergt; **Löschkandidat** |
| `test/t01-execution-2026-11-11` | `8ec7668` | diverged; +2 / -6 | **Nicht löschen, bevor Sonderartefakt dispositioniert ist** |
| `test/t03-execution-plan-2026-11-11` | `24a6a74` | diverged; +2 / -1 | **Nicht löschen, bevor zwei Sonderartefakte dispositioniert sind** |

**Zusatzvergleich:** `drs-ki-test` ist gegenüber `docs/drs-ki-repo-pflege` um 36 Commits voraus und 0 zurück. Die ältere DRS-Dokumentationslinie enthält damit keine exklusiven, außerhalb des aktuellen Arbeitsbranches liegenden Commits.

GitHub-PRs (Stand der Sichtung): **#1** Requirements-Baseline (merged), **#2** T-01–T-03 Diagnostic Concept (merged), **#3** T-02-Diagnose (merged); **#4 „Drs ki test“** ist *closed, not merged* und darf nicht mit einer Mergefreigabe verwechselt werden.

## 3. Drei noch nicht in die beiden Hauptlinien übernommene Dokumente

Der Vergleich mit `main` und die vollständige Pfadliste des Arbeitsbranches `drs-ki-test` zeigen, dass folgende Dateien **nur über ältere Testbranches nachgewiesen** sind:

| Herkunft | Datei | Maßnahme |
|---|---|---|
| `test/t01-execution-2026-11-11` | `tests/runs/2026-11-11-T01-P-N.md` | **Erhalten**, inhaltlich prüfen; dann als historische Ausführung nach `drs-ki-test` übernehmen oder explizit als abgelöst klassifizieren |
| `test/t03-execution-plan-2026-11-11` | `docs/testing/T03_EXECUTION_RUNBOOK_2026-11-11.md` | **Erhalten**, mit vorhandenen DRS-T03-Unterlagen auf Redundanz prüfen |
| `test/t03-execution-plan-2026-11-11` | `tests/runs/2026-11-11-T03-P.md` | **Erhalten**, mit vorhandenem `2026-11-11-DRS-T03-P.md` abgleichen; nicht als Dublette voraussetzen |

**Keine stillschweigende Löschung, Umschreibung oder Umdeklaration** historischer Testprotokolle. Vor Branchentfernung die drei Dateien explizit übernehmen bzw. begründet als archivierte, weiter zugängliche Historie kennzeichnen. Ein bloßes Branch-Löschen ohne Ablageentscheidung könnte Zugriff und Wiederauffindbarkeit erschweren.

## 4. Repository-Struktur und Volumen

Verifiziert mittels vollständiger Git-Tree-Abfrage (`recursive=1`, `truncated=false`):

| Branch | Dateien | Kernaussage |
|---|---:|---|
| `main` | 26 | Schlanke freigegebene Grundlage: `docs/requirements/`, `docs/reviews/`, `docs/testing/`, `tests/`, `docs/WORKFLOW.md` |
| `drs-ki-test` | 123 | Entwicklung, Testläufe und historische Dokumente: `config/drs-ki/`, `docs/drs-ki/` (45 Dateien), `docs/testing/` (14), `tests/runs/` (22), `tools/drs_ki/` (5), weitere |

**Viele Dateien sind beabsichtigte Historie** (Promptversionen, Reviews, Testprotokolle, SourceGuard-Versionen), nicht automatisch Müll. Eine massenhafte physische Bereinigung widerspräche der Nachvollziehbarkeit. Konsolidierung bedeutet daher vor allem: wenige aktive Branches, klare Einstiegsdokumentation, explizite historische Archivierung statt Geschichtslöschung.

## 5. Orientierung in der aktiven DEV-Dokumentation

- [DRS:KI-DEV-Übersicht](README.md) – bestehender Einstieg; Teile des historischen Textes nennen noch ältere DEV-Fassungen.
- [Aktueller Übergabestand vom 18.11.2026](TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md) – K-01 bis K-04c sowie W-02/W-03, Toolnachweise, letzte vom PO gemeldete DEV-Konfiguration.
- [WEB-01](WEB_01_WEBSUCHZUSAMMENFASSUNG_OHNE_ORIGINALLEKTUERE_2026-11-18.md) – ursprüngliches Finding: Webdigest ohne nachgewiesene Originallektüre, offen.
- [Wissenskorpus-Bestand](WISSENSKORPUS_BESTAND_2026-11-18.md) – nachgewiesenes Teilinventar, kein Vollinventar.
- [Systemprompt v0.3.11](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md) – letzte hier dokumentierte DEV-Fassung; historische Versionen beibehalten.
- [SourceGuard 0.2.3](../../tools/drs_ki/sourceguard_web_poc_v0_2_3.py) – zuletzt dokumentierte SourceGuard-Version; F-C1 bleibt kritisch offen.
- [Requirements-Baseline v1.2.0](../requirements/BASELINE.md) – ausschließlich im PO-freigegebenen `main` maßgeblich.

## 6. Konkreter Bereinigungsvorschlag mit Entscheidungsgrenzen

**Bereits durch dieses Dokument erledigt:** Alle Branches klassifiziert, Merges/PR-Status geprüft, Sonderartefakte identifiziert, bestehende Quellen-/Teststände verlinkt, nachvollziehbare Löschkandidaten benannt. **Keine Merges oder Branchlöschungen erfolgt.**

**Vorgeschlagener nächste Schritt nach ausdrücklicher PO-Entscheidung:**

1. **Fünf** klar redundante Branches löschen (Git-Refs, nicht die Dateien in `main` oder `drs-ki-test`): `docs/drs-ki-repo-pflege`, `docs/fachstandard-repo-pflege`, `review/requirements-v1.2.0-qs`, `test/t01-t03-diagnostics-v1`, `test/t02-execution-2026-11-11`. Vorher Heads und Merge-/Ancestor-Verhältnis erneut prüfen.
2. Die **drei Sonderdateien** aus T-01/T-03 zunächst gegen vorhandene Dokumentation lesen und fachlich einsortieren. Erst dann die beiden verbleibenden historischen Testbranches zur Löschung vorschlagen.
3. `main` und `drs-ki-test` dauerhaft behalten. **Kein Merge nach `main` ohne explizite PO-Freigabe und risikoorientierte Prüfung.**

**Warum nicht sofort löschen?** Ein allgemeiner Auftrag zur Konsolidierung ist keine eindeutige fachliche Freigabe, historische Testnachweise/Branchrefs unwiderruflich zu entfernen. Das Ziel ist eine übersichtliche **und** prüfbare SSOT, keine maximale Löschquote.

## 7. Einschränkung

Die Analyse basiert auf direkten GitHub-Metadaten, Compare- und Tree-Rückgaben vom 18.11.2026; sie beinhaltet **keinen** lokalen Build, keinen Live-Test in DRS:KI und keine unabhängige inhaltliche Abnahme jedes historischen Testdokuments.

## 8. Vollzug der fünf freigegebenen Branchlöschungen (18.11.2026)

**PO-Freigabe:** Der PO gab die Löschung der fünf in Abschnitt 6 beschriebenen redundanten Branches ausdrücklich frei. **Ausführung:** Der PO führte einen authentifizierten `git push https://github.com/baem-oss/THEOAgent.git --delete ...` aus. Die Terminalausgabe meldete für alle fünf Branches `[deleted]`.

**Unabhängige Nachprüfung durch den SE:** Eine anschließende GitHub-API-Abfrage `GET /repos/baem-oss/THEOAgent/branches?per_page=100` ergab **exakt vier** verbleibende Branches:

- `main` (HEAD `15326fe465275c2b774ab864a8da02799be9bf5c`)
- `drs-ki-test` (HEAD vor diesem Dokumentationsnachtrag `3ec3aec2e978d2631ce7afde850fb7c6c8267283`)
- `test/t01-execution-2026-11-11` (HEAD `8ec76687ca3c22ecf85e93f1f144612d3cb02e9a`)
- `test/t03-execution-plan-2026-11-11` (HEAD `24a6a74bb5fe87e988933ae6c7e2e6012d5e0418`)

**Tatsächlich gelöscht:** `docs/drs-ki-repo-pflege`, `docs/fachstandard-repo-pflege`, `review/requirements-v1.2.0-qs`, `test/t01-t03-diagnostics-v1`, `test/t02-execution-2026-11-11`.

**Fortsetzung:** Die beiden verbliebenen Testbranches sind bis zur Sichtung/Disposition ihrer drei Sonderdateien ausdrücklich **nicht** freigegeben zur Löschung. Alle vorangehenden Tabellen bleiben als historischer Vorher-Stand erhalten. Keine Änderungen an `main` oder Requirements-Baseline.
