# QE-Findings-Disposition – v2.0.0 Draft, Revision 2

27.11.2026. Review des Stands 54a074fbff01784d0bdea17c94059f6b871eaa57, 21 Findings. Grundlage: vom PO übermittelter QE-Bericht. SE-Disposition, keine QE-Schließung und keine PO-Freigabe.

| Finding | Maßnahme / Status zur Nachprüfung |
|---|---|
| QE-01 | Begriffe aus v1.2.0 übernommen; Betreiberfreigabe in H-03; Negativtest ergänzt. |
| QE-02 | F-05, N0–N4, H-02: eindeutige Zuordnung ab N2; unmarkierte präzise Referenz beansprucht Richtigkeit. |
| QE-03 | F-04/F-15: Motiv/Stilvorbild kein automatischer Rechercheauftrag. |
| QE-04 | F-03/04: Mindestkatalog, alternativer Suchweg, zulässiger Web-Fallback; F-06 bei Budget-/Fehlergrenze. |
| QE-05 | H-02/F-05: Fassung nur soweit erheblich; kleinste wirksame Maßnahme, Antworterhaltung. |
| QE-06 | Q-02: Null schwere fachliche/pastorale Fehler, Schwereorakel vorab. |
| QE-07 | H-02/Q-04: keine erfundenen Hinweise auch bei Kennzeichnung; zugeschriebene Wortzitate nur geprüft. |
| QE-08 | H-03 und §2: Nicht-Vortäuschung/Substitution als harte Grenzen; Erweiterung exklusiven Quellenraums erst nach Zustimmung. |
| QE-09 | SP-01: Chat-Eingaben, Betreiber-Datenfluss, Anonymisierung vor Übermittlung. Rechts-/Providerklärung offen; keine behauptete Umsetzung. |
| QE-10 | F-08/09: Auftragsbedingungen wiederhergestellt. |
| QE-11 | Abnahmeprofil: jeder Lauf zählt, Q-02 nur PASS, Fallzahlen und vorab fixiertes Raster. |
| QE-12 | Q-01: Reaktionsquote je Lauf, keine Verfügbarkeitsgarantie. |
| QE-13 | Q-07: beobachtbare Blockade/Verkürzung und Suchausfall; Laufzeitgrenzen offen. |
| QE-14 | Q-03: vorab definierte Kernaussagen N2–N4. |
| QE-15 | Abnahmeprofil: zwei frühe Zusatzfälle, 25–30 Aufträge als Vorschlag, Gewichtung offen. |
| QE-16 | H-05: akute Gefährdung, Hilfe, Missbrauch; SP-06 ergänzt Vertraulichkeit. |
| QE-17 | User Stories wortgleich als Anhang übernommen. |
| QE-18 | F-02/04/09/14: fehlende Details wiederhergestellt. |
| QE-19 | RANF-04: Herkunft und öffentliche Referenz präzisiert; keine Rechteentscheidung, Fachstandardfreigabe offen. |
| QE-20 | Verblindung und zweite Fachperson soweit praktikabel vorgeschlagen; Prüfer offen. |
| QE-21 | Q-12 gestrafft; Laufzeitgrenzen nach Referenzmessung vor Abnahme festlegen. |

## PO-Richtungsentscheidungen und SE-Vorschläge

Aus dem Dialog: obligatorische Pipe im nächsten lokalen Zyklus, nicht restriktive Qualitätssicherung, keine erzwungene deterministische fachliche Arbeitsweise. RANF-07 und §2 tragen diese Entscheidungen. DRS:KI-Integration ungeklärt. RANF-08 Modellqualifikation und SP-06 Vertraulichkeit folgen den historischen Befunden. 90-%-Gebrauchstauglichkeit und 100-%-Reaktionsziel sind Abnahmeziele im definierten Korpus, keine allgemeine Garantie. Keine konkrete Implementierung festgelegt.

Zur ausdrücklichen PO-Bestätigung verbleiben die konkrete Auslegung N0–N4 einschließlich ungeprüfter Referenzhinweise, Null schwere Fehler, Web-Fallback, Zielgruppe, endgültige v2-Freigabe, Korpus/Prüfer/Grenzwerte und Datenfluss. Die SE-Vorschläge sind im Draft umgesetzt, nicht als gesondert erteilte PO-Freigaben behauptet.

## Historische Evidenz

DRS:KI A/B-Benchmark vom 20.11.2026 (A 9 PASS/3 PARTIAL/3 FAIL; B 2/3/10), F-C1 und KNOW-01/WEB-01 belegen die Grenzen freiwilliger Tool-Aufrufe und Quellenprovenienz. Die lokale Pipe dev14/15 zeigt die Gefahr restriktiver Gates; sechs aufeinanderfolgende Live-Fehler einschließlich Fürbitten. Keine kausale Garantie oder kontrollierte Modellstudie. Bestehende Testfälle wiederverwenden, gezielt geänderte Pfade prüfen. Keine allgemeine Wiederholung der nativen Erprobung. Quellen: https://github.com/baem-oss/THEOAgent/tree/5d9ec669b9d3dcaadd9a58ceb57864b5b4546087/docs/drs-ki und https://github.com/baem-oss/THEOAgent/blob/5d9ec669b9d3dcaadd9a58ceb57864b5b4546087/tests/runs/2026-11-20-THEOAGENT-AB-MODELLBENCHMARK-PO-PRAXISBEWERTUNG.md.

## Nachreview

QE prüft die Änderungen gegenüber 54a074f, insbesondere beide Blocker, harte Grenzen, Nachweisstufen, Messregeln, Datenschutz und RANF-07/08. Prüfe kritisch, ob die obligatorische Pipe ohne erzwungene fachliche Abläufe und restriktive Gates konsistent spezifiziert ist. Keine erneute vollständige Reviewkampagne, sofern keine neuen systematischen Verluste erkennbar sind. Keine Repository-Änderungen oder Freigabe durch QE.
