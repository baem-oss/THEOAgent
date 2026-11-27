# Unabhängiger QE-Reviewauftrag – Requirements-Baseline v2.0.0 Draft

Stand: 27.11.2026. Auftraggeber: PO/SE. Der QE prüft unabhängig und empfiehlt; Freigabe und Änderungen liegen beim PO bzw. beauftragten SE. Keine Repository-Schreiboperation erforderlich.

## Prüfgegenstand

Repository baem-oss/THEOAgent, Branch local-dev, Prüfbasis Commit 4d38a96855c4aa1540bad6c676b1b1938a508cad.

- docs/requirements/v2.0.0-draft/BASELINE.md
- docs/requirements/v2.0.0-draft/ACCEPTANCE_PROFILE.md
- docs/requirements/v2.0.0-draft/MIGRATION.md
- gültige Referenz: docs/requirements/BASELINE.md, ACCEPTANCE_PROFILE.md, TRACEABILITY.md (v1.2.0).

HEAD und geprüfte Dateistände selbst verifizieren. Die alte Baseline bleibt gültig. Keine technische Architektur ist vorgegeben.

## Anlass

Die SourceGuard-Entwicklung erreichte gute Offline-Testergebnisse (dev14: 35 PASS, 0 FAIL, 11 PARTIAL, 1 INFO im historischen Korpus), aber sechs aufeinanderfolgende Live-Fehler in dev14/dev15. Ursachen: Zitatzuordnung, vorzeitiger Rechercheabschluss ohne Originallektüre, Budgetgrenze, ungültige Skill-ID und Sperre eines kreativen Fürbittenentwurfs. Die abgewiesenen Entwürfe sind nicht verfügbar; tatsächliche inhaltliche Fehler oder Falschpositive sind daher nicht bewiesen. Ziel des PO: 90-%-Qualitätsregel und 100-%-Antwortziel bei technisch bearbeitbaren Aufträgen; Schutzgrenzen nicht aufweichen. Der SE schlägt vor, vor der technischen Neugestaltung Anforderungen zu konsolidieren.

## Prüffragen

1. Ist die Produktvision fachlich stimmig? Ist die Trennung harter Grenzen, funktionaler Pflichten, Qualitätsziele und Randbedingungen sinnvoll? Widersprich ausdrücklich, wo ein anderer Ansatz besser ist.
2. Sind alle 27 US und 80 Altanforderungen semantisch erhalten oder Änderungen ausdrücklich ausgewiesen? Prüfe die 107 Zuordnungen, nicht nur das Vorhandensein der IDs. Suche insbesondere nach verlorenen Zustandsregeln, Bedingungen, Ausnahmen und Rechteanforderungen.
3. Sind die Änderungen zu FANF-02/03/06/07, GR-03/17/18 sachlich gerechtfertigt? Prüfe die Grenze zwischen allgemeiner Paraphrase, konkreter Zuschreibung, Originalzitat, konkreter Fundstelle und verbindlicher Norm. Verhindert F-05 die Gleichsetzung einer Leseliste mit einem Aussagebeleg? Ist die Freigabe gekennzeichneter ungeprüfter Referenzhinweise vertretbar?
4. Sind 90 % fachliche Gebrauchstauglichkeit und 100 % Antwortquote operationalisiert, ohne bloße Einschränkungen als Erfolg zu zählen oder fehlgeschlagene Fälle aus dem Nenner zu entfernen? Prüfe Q-01–Q-12, Korpus, Messregeln, Wiederholungen und die Trennung von Qualitäts-, Schutz- und Abdeckungszielen. Wo sind Schwellen zu ändern oder offen zu halten?
5. Bleiben NFANF-12/13, Datenschutz, Rechte, Freeze, Quellenbeschränkungen und pastorale Schutzgrenzen ohne Kompensation erhalten? Prüfe gemischte Aufgaben und Fallbacks, insbesondere fehlende Originallektüre bei exklusivem Quellenauftrag.
6. Sind Teilergebnisse und Fehlertransparenz konkret genug, ohne eine Architektur oder unnötige Prüfmechanismen zu erzwingen? Ist der Entwurf KISS-gerecht, verständlich, widerspruchsfrei, testbar und fachlich vollständig?
7. Welche Anforderungen, Regeln oder Abschnitte würdest du zusammenlegen, streichen, ergänzen oder anders priorisieren? Unterscheide echte Produktanforderung, Qualitätsziel und mögliche Implementierung. Keine Empfehlung allein aufgrund bestehender Pipe-Mechanismen.
8. Beurteile den Entwurf als Grundlage eines späteren Architekturrefactorings, nicht als Code-Abnahme. Welche PO-Entscheidungen sind vor Freigabe zwingend?

## Ergebnisformat

Kurzes unabhängiges Gesamturteil; Findings mit ID, Priorität (Blocker/hoch/mittel/niedrig), genauer Fundstelle, fachlicher Begründung, kleinstem sinnvollen Änderungsvorschlag und gegebenenfalls konkretem Abnahmekriterium. Unterscheide nachgewiesene Widersprüche, Risiken und offene Entscheidungen. Gib eine Empfehlung: freigabefähig, nach Korrekturen freigabefähig oder grundsätzlich neu zu entwerfen. Keine Freigabe erteilen, keine Baseline überschreiben, keine Tests behaupten, die nicht ausgeführt wurden.

Der QE soll ausdrücklich auch die grundlegende Richtung kritisch beurteilen, nicht nur redaktionelle Fehler suchen.
