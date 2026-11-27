# SE-Disposition – SourceGuard v0.5.5-dev3

Stand: 27.11.2026
Status: Entwicklungsplan durch PO freigegeben.
Reviewbasis: ab93b8128651c4daea3281c20ae461759634e61c
Requirements: v1.2.0, unverändert.

## Referenzlauf
QE: 47 Fälle, 19 PASS, 16 FAIL, 11 PARTIAL, 1 INFO.
PO meldet identische Verteilung vom Homeserver. Einzelfallvergleich und SHA-256 des lokalen Testobjekts nicht übermittelt; keine vollständige unabhängige Verifikation behauptet.
QE-Artefakte archiviert, letzter Archivierungscommit 1f0126c5bfe5b61dd00c252e1a1794b9db03f4f5.

## Disposition
| Finding | Priorität | Maßnahme |
|---|---|---|
| QE-01 | P0 | Einheitliche Beleggrammatik, unbekannte und nichtkanonische Kennungen kontrollieren. |
| QE-02 | P0 | Wortlautprüfung expliziter Originalzitate ohne willkürliche Mindestwortzahl. |
| QE-03 | P0 | Quellenpflicht bei fachlichen Ergänzungen und Korrekturen erhalten; bloße Zitat-/Kennungssperre genügt nicht. |
| QE-04 | P0 | Vollständiger Systemprompt, native Fachskills, widerspruchsfreie Werkzeugsteuerung. |
| QE-05 | P0 | Begrenzte Argumentkorrektur, differenzierte Diagnose. |
| QE-06 | P0 | Web- und Skill-Preflight; native Werkzeuge bevorzugen. |
| QE-07 | P1 | Verständliche Nicht-Freigabe; technisch geprüfte Teilergebnisse gemäß Baseline. |
| QE-08 | P1 | Überholte Diagnosemeldungen kennzeichnen. |
| QE-09 | P2 | Überlappende Evidenzfenster nur bei Bedarf konsolidieren. |
| QE-10 | P2 | Heuristiken nur bei nachgewiesener Beeinträchtigung ändern. |
| QE-11 | P1 | Datei-ID-Registrierung auf autorisierte strukturierte Werkzeugdaten begrenzen. |
| QE-12 | P1 | Vertraulichkeit und Zugriffskontrolle; zwingend vor Praxistests mit vertraulichen Daten. |
| QE-13 | P0 | Gesprächskontext und fortgeltende Quellenbeschränkungen erhalten. |
| QE-14 | P1 | Legacy nach gesicherten Regressionen aus aktiver Implementierung entfernen; historische Artefakte erhalten. |

## Freigegebene Reihenfolge
AP 0: Archivierung, Referenzlauf, SE-Disposition.
AP 1: THEOAgent-Integration (QE-04, QE-13).
AP 2: Quellenintegrität (QE-01, QE-02, QE-03).
AP 3: Werkzeugsteuerung (QE-05, QE-06, QE-07, QE-08).
AP 4: Vertraulichkeit und Zugriff (QE-11, QE-12).
AP 5: Konsolidierung (QE-09, QE-10, QE-14).

Nächste Arbeitsversion v0.5.5-dev4 auf local-dev. Keine Änderung an main, drs-ki-test oder Requirements-Baseline. Keine Produktivfreigabe. Historische QE-Tests unverändert archivieren; Soll-Regressionen separat pflegen. Live-Tests und fachliche Abnahme bleiben erforderlich.

Ziel: zuverlässiger theologischer Arbeitsassistent, nicht eine isoliert maximierte SourceGuard-Komponente. Modell entscheidet semantisch, Code setzt technisch prüfbare Anforderungen durch. Reuse before Build.
