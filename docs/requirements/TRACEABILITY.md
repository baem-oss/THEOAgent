# THEOAgent – Traceability-Matrix

**Version:** 1.0.0 · **Stand:** 10.11.2026  
**Quelle:** [Fachliche Requirements-Baseline](BASELINE.md)  
**Zweck:** Jede US auf mindestens eine FANF zurückführen; Umsetzungs- und Testnachweise werden erst in einer weiteren Phase ergänzt.

| User Story | Fachlicher Schwerpunkt | Zugeordnete funktionale Anforderungen |
|---|---|---|
| US-01 | Fachliche Antworten | FANF-01 |
| US-02 | Selbstständige Quellensuche | FANF-02, FANF-03 |
| US-03 | Angeordnete Originallektüre | FANF-04, FANF-05 |
| US-04 | Überprüfbare Belege | FANF-03, FANF-05, FANF-07, FANF-08 |
| US-05 | Quellensynthese | FANF-10 |
| US-06 | Weiterrecherche | FANF-06 |
| US-07 | Evidenztransparenz | FANF-07, FANF-08, FANF-09 |
| US-08 | Schriftauslegung | FANF-11, FANF-12 |
| US-09 | Predigtentwicklung | FANF-13, FANF-14, FANF-15 |
| US-10 | Predigtkritik | FANF-16 |
| US-11 | Gezielte Predigtrevision | FANF-17 |
| US-12 | Liturgische Texte | FANF-15, FANF-20, FANF-21 |
| US-13 | Liturgische Regeln | FANF-21, FANF-22 |
| US-14 | Katechese | FANF-15, FANF-25 |
| US-15 | Glaubenslehre | FANF-26 |
| US-16 | Kirchenrecht | FANF-22, FANF-27 |
| US-17 | Pastorale Situationen | FANF-28 |
| US-18 | Sonstige Textprüfung | FANF-17, FANF-29 |
| US-19 | Kritischer Dialog | FANF-30 |
| US-20 | Auftragssteuerung | FANF-14, FANF-31 |
| US-21 | Verbindliche Textfreigaben | FANF-18 |
| US-22 | Liturgisches Gesamtkonzept | FANF-24 |
| US-23 | Wiederverwendung | FANF-19 |
| US-24 | Gottesdienstvorbereitung | FANF-23 |
| US-25 | Positionen und Erfahrungsberichte | FANF-10, FANF-12 |
| US-26 | Technikfreie Auftragserteilung | FANF-01, FANF-32 |
| US-27 | Bereitgestellte Dokumente | FANF-33 |

## Prüfergebnis

- **27/27 User Stories** besitzen mindestens eine FANF-Zuordnung.
- **33/33 FANF** sind mindestens einer User Story zugeordnet.
- **US-27** zur Dokumentenarbeit ist ausdrücklich durch **FANF-33** abgedeckt.
- NFANF, RANF, GR, SP und DAT wirken querschnittlich. Eine vollständige Regel→Test-Traceability wird erst mit den Akzeptanzkriterien erstellt; diese Datei behauptet keine Tests oder Abnahmen.

## Hinweise zur späteren Testableitung

Die folgenden drei Fälle eignen sich als **fachliche** Beispiele für spätere Abnahmetests, ohne hier bereits deren Testschritte festzulegen:

1. „Prüfe diesen Predigtentwurf nach Klippert“ → angeordnete Originallektüre plus begründete Textprüfung (US-03, US-10, GR-01/02).
2. „Erläutere Gemeinwohl, Subsidiarität und Solidarität aus dem Kompendium“ → selbstständige Recherche, tatsächlich nachvollziehbare Originalbelege und Synthese (US-01–07, GR-02/03/18).
3. „Überarbeite nur die zweite Fürbitte; alle anderen bleiben eingefroren“ → gezielte Revision und Freeze (US-11/20/21, GR-09/10).

Diese Szenarien sind **keine** Behauptung, dass eine bestehende SourceGuard-/Open-WebUI-Version sie bereits bestanden hätte.
