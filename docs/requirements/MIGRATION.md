# Migration und Traceability v1.2.0 → v2.0.0

Stand: 28.11.2026, Revision 3 nach QE-Nachreview. Freigegebene Migrationszuordnung nach QE-Sichtprüfung; kein Nachweis vollständiger semantischer Gleichwertigkeit oder Implementierungsabnahme. [Altstand](https://github.com/baem-oss/THEOAgent/blob/bfabf68264a3ae049a07679b3722a0a1dbe032bf/docs/requirements/BASELINE.md) · [Freigegebene Baseline](BASELINE.md).

## Vollständige Vorwärtszuordnung

Alle 27 User Stories und 80 Anforderungen des Altstands sind einzeln zugeordnet. Die User Stories bleiben Bedarfskatalog; sie werden nicht als neue zusätzliche Anforderungen dupliziert. Konsolidierung bezeichnet die Absicht, nicht einen bereits abgenommenen Erhalt sämtlicher Details.

| Alt-ID | Neu-ID | Disposition |
|---|---|---|
| US-01 | F-01, F-02 | Bedarf erhalten. |
| US-02 | F-03 | Bedarf erhalten. |
| US-03 | F-04 | Bedarf erhalten. |
| US-04 | F-05 | Bedarf erhalten. |
| US-05 | F-08 | Bedarf erhalten. |
| US-06 | F-03 | Bedarf erhalten. |
| US-07 | F-05, F-06, F-07 | Bedarf erhalten. |
| US-08 | F-09 | Bedarf erhalten. |
| US-09 | F-09, F-10 | Bedarf erhalten. |
| US-10 | F-10 | Bedarf erhalten. |
| US-11 | F-16 | Bedarf erhalten. |
| US-12 | F-11 | Bedarf erhalten. |
| US-13 | F-11, F-13 | Bedarf erhalten. |
| US-14 | F-11 | Bedarf erhalten. |
| US-15 | F-02 | Bedarf erhalten. |
| US-16 | F-13 | Bedarf erhalten. |
| US-17 | F-12 | Bedarf erhalten. |
| US-18 | F-12, F-16 | Bedarf erhalten. |
| US-19 | F-08 | Bedarf erhalten. |
| US-20 | F-01 | Bedarf erhalten. |
| US-21 | F-17, H-04 | Bedarf erhalten. |
| US-22 | F-11 | Bedarf erhalten. |
| US-23 | F-17 | Bedarf erhalten. |
| US-24 | F-14 | Bedarf erhalten. |
| US-25 | F-08 | Bedarf erhalten. |
| US-26 | F-01, F-03 | Bedarf erhalten. |
| US-27 | F-18 | Bedarf erhalten. |
| FANF-01 | F-01, F-02 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-02 | F-03 | Änderung: Recherchebedarf statt bloßer Verfügbarkeit; lokale und externe Recherche nicht pauschal verpflichtend. |
| FANF-03 | F-03 | Änderung: Webrecherche bedarfsabhängig, nicht allein bei Zulässigkeit. |
| FANF-04 | F-04 | Benannte Quellen im Recherche-/Prüfauftrag; bloße Erwähnung eines Autors als Kontext nicht automatisch Rechercheauftrag. Abgrenzung in F-04 präzisiert. |
| FANF-05 | F-04 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-06 | F-03, F-06 | Präzisiert: alternativer Suchweg soweit zulässig und verfügbar; bei Abbruch F-06. |
| FANF-07 | F-05 | Änderung: kompakte Herkunft bei gewöhnlicher Paraphrase; eindeutiger Aussagebezug bei konkreten/expliziten Nachweisen. PO muss Abschwächung ausdrücklich billigen. |
| FANF-08 | F-05 | Inhaltliche Prüfung bleibt Pflicht; kein deterministischer Vollprüfer vorgeschrieben. |
| FANF-09 | F-06 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-10 | F-08 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-11 | F-09 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-12 | F-09 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-13 | F-09 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-14 | F-10 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-15 | F-01 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-16 | F-10 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-17 | F-16 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-18 | F-17, H-04 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-19 | F-17 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-20 | F-11 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-21 | F-11 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-22 | F-13 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-23 | F-14 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-24 | F-11 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-25 | F-11 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-26 | F-02 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-27 | F-13 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-28 | F-12 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-29 | F-12 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-30 | F-08 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-31 | F-01 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-32 | F-01, F-03, F-04 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-33 | F-18 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| FANF-34 | F-08 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| NFANF-01 | Q-02 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-02 | Q-03 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-03 | Q-01, Q-06 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-04 | Q-07 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-05 | Q-08 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-06 | Q-08 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-07 | Q-08, H-05 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-08 | Q-09 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-09 | Q-10 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-10 | Q-11 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-11 | Q-06 | Messziel konsolidiert; Schwellen siehe Abnahmeprofil. |
| NFANF-12 | Q-05 | Null-Fehler-Kriterium unverändert. |
| NFANF-13 | Q-04 | Null-Fehler-Kriterium in abgegrenztem Korpus unverändert. |
| GR-01 | F-04 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-02 | H-03 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-03 | H-02, F-05 | Änderung: ungeprüfte Referenzhinweise erkennbar zulässig; keine ungeprüfte Verifikation oder tragende Zuschreibung. PO muss diese Auslegung ausdrücklich billigen. |
| GR-04 | F-03 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-05 | F-02 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-06 | F-09 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-07 | F-13 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-08 | F-13 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-09 | H-04 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-10 | F-01 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-11 | F-08 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-12 | F-11 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-13 | H-05 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-14 | H-05 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-15 | H-03 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-16 | F-06, H-02 | Konsolidiert, fachlicher Gehalt beizubehalten. |
| GR-17 | F-15, F-03, Q-07 | Erweitert: kreative Entwürfe ohne konkrete Quellenbehauptung; gemischte Aufträge getrennt behandeln. |
| GR-18 | F-06 | Verstärkt: sinnvolle Teilergebnisse statt vollständiger Sperre; Einschränkung bei objektiv fehlender Grundlage. |
| RANF-01 | RANF-01 | Wortlaut übernommen. |
| RANF-02 | RANF-02 | Wortlaut übernommen. |
| RANF-03 | RANF-03 | Wortlaut übernommen. |
| RANF-04 | RANF-04 | Herkunft redaktionell präzisiert; Freigabe des Fachstandards weiterhin offen. |
| RANF-05 | RANF-05 | Wortlaut übernommen. |
| RANF-06 | RANF-06 | Wortlaut übernommen. |
| SP-01 | SP-01 | Erweitert: Chat-Eingaben, Betreiber-Datenfluss und Anonymisierung vor Übermittlung. |
| SP-02 | SP-02 | Wortlaut übernommen. |
| SP-03 | SP-03 | Wortlaut übernommen. |
| SP-04 | SP-04 | Wortlaut übernommen. |
| SP-05 | SP-05 | Wortlaut übernommen. |
| DAT-01 | DAT-01 | Wortlaut übernommen. |
| DAT-02 | DAT-02 | Wortlaut übernommen. |
| DAT-03 | DAT-03 | Wortlaut übernommen. |
| DAT-04 | DAT-04 | Wortlaut übernommen. |

## Bewusste Änderungen zur PO-Entscheidung

1. Recherchepflicht ist aufgabenbezogen, nicht durch Toolverfügbarkeit ausgelöst (FANF-02/03/06).
2. Kompakte Herkunftsangabe bei gewöhnlicher Paraphrase statt zwingendem Einzelnachweis (FANF-07). Bei N2, prüfpflichtigen N3-Aussagen und N4 bleibt die eindeutige Zuordnung zwingend; richtige präzise Referenzen ohne Prüfanspruch oder tragende Belegfunktion erfordern nicht automatisch einen Laufzeitabruf. Siehe F-05/H-02. Eine Leseliste allein beweist keine Aussage. QE prüft insbesondere, ob F-05 diese Grenze hinreichend klar zieht.
3. Nicht verifizierte, begründete und nicht erfundene Referenzhinweise sind klar gekennzeichnet möglich; zugeschriebene Wortzitate nur geprüft (GR-03). Keine falsche Verifikationsbehauptung, kein erfundenes Zitat, kein Ersatz für verlangte Originallektüre.
4. Kreative Aufträge ohne konkrete Quellenbehauptung werden ohne obligatorische Recherche bearbeitbar (GR-17).
5. Teilantwort und gezielte Einschränkung erhalten Vorrang gegenüber vollständiger fachlicher Sperre (GR-18). Sicherheitsgrenzen bleiben unverändert.
6. Antwortquote und fachliche Qualität werden getrennt gemessen. Schwellen sind Vorschläge, keine Freigabe. H-01–H-06, Q-04/Q-05/Q-12 und SP bleiben nicht kompensierbar.

## Neue beziehungsweise expliziter formulierte Pflichten

F-06: Reaktion auf beherrschbare technische Fehler; F-07: historische Provenienz ohne Scheinzuordnung; F-15: kreative Aufträge und gemischte Aufgaben; Q-01: Antwortquote; Q-12: Schutzgrenzen nicht statistisch kompensierbar.

## Offene Punkte

- QE soll die 107 Zuordnungen auf fachlichen Erhalt, unbeabsichtigte Verluste und Mehrdeutigkeiten prüfen.
- Begriffe und Zustandsregeln aus v1.2.0 sind in die Baseline übernommen; alle 27 User Stories stehen in Anhang A.
- Korpus, Bewertungsraster, Effizienz- und Wartbarkeitsgrenzen, fachlicher Standard und Übermittlungsrechte bleiben Abnahmevoraussetzungen. RANF-07 legt für den lokalen Zyklus die obligatorische nicht restriktive Pipe fest; RANF-08 verlangt Modellqualifikation. Keine Produktivfreigabe oder behauptete DRS:KI-Deploymentfähigkeit.

## Ergänzungen nach QE-Review

- H-05: Akutgefährdung, professionelle Hilfe und Missbrauch; SP-06: direkte und indirekte Drittoffenlegung vertraulicher Angaben (DRS:KI R-01/V-04/V-05).
- Q-02: Null schwere fachliche/pastorale Fehler im vereinbarten Korpus; Q-04: keine erfundenen Hinweise auch bei Unsicherheitskennzeichnung.
- RANF-07/08: obligatorische, nicht restriktive Pipe im lokalen Entwicklungszyklus und Modellqualifikation. Probabilistische Facharbeit bleibt frei; technische Schutzgrenzen bleiben verbindlich.
- Die 107 Altzuordnungen bleiben erhalten. QE-Nachprüfung der geänderten Passagen abgeschlossen; keine erneute Vollprüfung der 107 Zuordnungen.

## Präzisierungen Revision 3 (28.11.2026)

- GR-03 / H-02 / F-05 / Q-04: Richtigkeit einer Referenz von behaupteter Originalprüfung trennen. Zugeschriebene Wortzitate, ausdrückliche Nachweise und tragende Belege bleiben prüfpflichtig. Freie biblische Wiedergaben in kreativen Texten sind keine beanspruchten exakten Übersetzungszitate.
- RANF-07: begrenzter Interventionskatalog, sicherer Rückfall bei Fehlern der Qualitätsfunktionen; kein Umgehen von Schutzgrenzen. DRS:KI-Integration DEFERRED / TO_CHECK (PO 28.11.2026), kein Blocker des lokalen Refactorings.
- §2: harte Abnahmekriterien sind nicht automatisch technische Laufzeitgates. SP-01: Betreiber-/Konfigurationsebene; keine generelle semantische Nachrichtensperre. F-13: Hinweis auf zuständige Stelle bei rechtlich folgenreichen Einzelfällen.
- Abnahmeprofil: kleine Teilkorpora vorab poolen; neue Regressionen für N-01 bis N-07. Alle 107 Altzuordnungen bleiben erhalten.
