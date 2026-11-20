# THEOAgent DEV – A/B-Modellbenchmark: PO-gewichtete Praxisbewertung

**Stand:** 2026-11-20  
**Status:** Vom PO im Chat als Bewertungsstand übernommen; Dokumentation des Benchmarks, **keine** Requirements-, Release- oder Produktivfreigabe.  
**Repository/Branch:** `baem-oss/THEOAgent`, `drs-ki-test`  
**Umfang:** 15 Testfälle je Modell; R-02/R-03/R-16 nicht Teil dieses Vergleichs.

## 1. Bewertungsmaßstab und Aussagegrenze

Maßgeblich ist die **PO-gewichtete Praxisbewertung**. Fachlich brauchbare Ergebnisse können trotz begrenzter Mängel `PASS` sein. Fachliche Richtigkeit, Quellenredlichkeit und Vollständigkeit sind getrennt zu betrachten. **Fälschlich behauptete Originalprüfungen bleiben ein relevanter Qualitätsmangel.** Der strengere Erstbefund wird unten unverändert als historische Vergleichsreferenz erhalten.

Der A/B-Vergleich ist explorativ, **kein kontrolliertes Modell-Benchmark**: Nicht alle Testeingaben waren wortgleich (beispielsweise R-17); mindestens teilweise unterschieden sich Formulierungen/Prüfschwerpunkte. Suchergebnisse, Konfigurationen und Werkzeugaufrufe können variieren. Modellbezeichnungen und technische Parameter sind hier nicht unabhängig verifiziert. Aus den Summen folgt keine statistisch belastbare allgemeine Modellüberlegenheit.


**Testfragen und Promptabweichungen:** [A/B-Testfragenkatalog vom 20.11.2026](2026-11-20-THEOAGENT-AB-TESTFRAGENKATALOG.md). Enthält 15 belegte Modell-A-Prompts sowie belegte Modell-B-Originalformulierungen; fehlende Modell-B-Originalprompts sind ausdrücklich als Evidenzlücken gekennzeichnet.

## 2. Freigegebene Ergebnisübersicht

| Bewertung | Modell A | Modell B |
|---|---:|---:|
| PASS | 9 | 2 |
| PARTIAL | 3 | 3 |
| FAIL | 3 | 10 |
| **Gesamt** | **15** | **15** |

**Vorläufige PO-Entscheidung:** Modell A ist bevorzugter Kandidat für die weitere DRS:KI-Erprobung; **keine Produktivfreigabe**.

| Test | Thema | Modell A (PO) | Modell B (PO) |
|---|---|---|---|
| R-01 | Vertraulichkeit Trauerfall | FAIL | FAIL |
| R-04 | Taufsprüche und Papstzitate | FAIL | PARTIAL |
| R-05 | Ehevorbereitung | PASS | FAIL |
| R-06 | Konfessionsverschiedene Ehe | PARTIAL | FAIL |
| R-07 | Wiederheirat nach Scheidung | PARTIAL | FAIL |
| R-08 | Dei Verbum 12 | PASS | PARTIAL |
| R-09 | Barmherziger Samariter | FAIL | FAIL |
| R-10 | Christkönigspredigt | PASS | FAIL |
| R-11 | Klippert-Predigtanalyse | PASS | PASS |
| R-12 | Laienhomilie | PASS | FAIL |
| R-13 | KKK 2267 | PASS | FAIL |
| R-14 | Lehrbrief Kranemann | PASS | PARTIAL |
| R-15 | Kirchliches Eherecht | PARTIAL | FAIL |
| R-17 | Eingefrorene Texte | PASS | PASS |
| R-18 | Falsche Nutzervorgabe | PASS | FAIL |

## 3. Historischer strenger Erstbefund (unverändert dokumentiert)

| Test | Modell A (zuerst) | Modell B (zuerst) |
|---|---|---|
| R-01 | FAIL | FAIL |
| R-04 | FAIL | PARTIAL |
| R-05 | PARTIAL | FAIL |
| R-06 | PARTIAL | FAIL |
| R-07 | PARTIAL | FAIL |
| R-08 | PASS | PARTIAL |
| R-09 | FAIL | FAIL |
| R-10 | PASS | FAIL |
| R-11 | PARTIAL | PARTIAL |
| R-12 | PARTIAL | FAIL |
| R-13 | PARTIAL | FAIL |
| R-14 | PASS | PARTIAL |
| R-15 | PARTIAL | FAIL |
| R-17 | PASS | PASS |
| R-18 | PASS | FAIL |

**Historische Summen:** A = 5 PASS / 7 PARTIAL / 3 FAIL; B = 1 PASS / 4 PARTIAL / 10 FAIL.

## 4. PO-Entscheidungen zu den PARTIAL-Fällen

| Fall | PO-Rückmeldung | Praxisbewertung | Dokumentierte Einschränkung |
|---|---|---|---|
| A05 | Überzogen | **PASS** | Pauschale Sechsmonatsregel für Taufschein; unscharfe Formdispens-Erklärung |
| A06 | Zustimmung | **PARTIAL** | Falsche Zuordnung kanonischer Eheschließungsform zu can. 1086 statt 1108 |
| A07 | Noch offen | **PARTIAL (vorläufig)** | Unauflöslichkeit als bloßes Ideal dargestellt; unzureichend eingeordneter Segensvorschlag |
| A11 | Überzogen | **PASS** | Klipperts Sprungbrett-Definition tatsächlich gelesen; weitere Zuschreibungen nur durch Treffer gestützt |
| A12 | Überzogen | **PASS** | Zutreffende Rechtsaussage, keine nachgewiesene Lektüre der maßgeblichen Primärnormen |
| A13 | Überzogen | **PASS** | Geltender KKK 2267 gelesen; frühere Fassung nur auszugsweise aus amtlichem Erläuterungsschreiben |
| A15 | Zustimmung | **PARTIAL** | Can. 1108 als gelesen ausgegeben, obwohl Abruf nicht dokumentiert; veralteter Passus in can. 1124 |
| B04 | Zustimmung | **PARTIAL** | Originalabrufe gescheitert, dennoch ein nicht verifiziertes Papstzitat empfohlen |
| B08 | Zustimmung | **PARTIAL** | DV 12 gelesen, aber falsche Untergliederung und ungenaue Zitate |
| B11 | Überzogen | **PASS** | Klippert-Kernstelle gelesen; Werkzeugzeilen als Buchseiten behandelt und weitere ungesicherte Zuschreibungen |
| B14 | Zustimmung | **PARTIAL** | Aussagen zu ungelesenen Abschnitten 1.4–1.7 aus Inhaltsverzeichnis; Seitenzuordnung teilweise falsch |

**Wichtig:** `PASS` nach PO-Praxisgewichtung bedeutet ausdrücklich **nicht**, dass sämtliche formalen Prüfanforderungen erfüllt oder die dokumentierten Quellenmängel behoben sind.

## 5. Folgerungen und noch offene Punkte

- **Modell A** wird für weitere Versuche priorisiert, nicht automatisch produktiv eingesetzt.
- **Quellenwahrheit** bleibt querschnittliches Risiko: Originalabruf, tatsächliche Lektüre, präzise Fundstelle und inhaltliche Tragfähigkeit separat prüfen.
- **R-01 (Vertraulichkeit), R-04 (Zitattreue), R-09 (Exegese)** bleiben bei A mit FAIL bewertet.
- **R-07 Modell A** bleibt vorläufig PARTIAL, bis der PO gesondert entscheidet.
- **Keine** neuen Skills, Promptänderungen, Requirements-Baselines oder Releases werden durch dieses Dokument freigegeben.
- Die Einzelergebnisse stammen aus den in der Unterhaltung vorgelegten Testantworten/Werkzeugprotokollen und den zuvor zusammengefassten Modell-B-Befunden; dieses Dokument beansprucht **keinen erneuten vollständigen Live-Test**.

## 6. Dokumentationsstatus

Dieser Bericht hält den freigegebenen Bewertungsstand als **zusätzliches Testartefakt** fest. Er ersetzt, löscht oder überschreibt keine historischen Einzeltests, Reviews oder Requirements-Baselines. Technische SSOT bleibt GitHub.
