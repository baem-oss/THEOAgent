# P-03a – KKK 2267: Gegenprobe der beiden URL-Fassungen

**Datum:** 13.11.2026  
**System:** DRS:KI DEV / THEOAgent Dev  
**Werkzeug:** `SourceGuard Web v0.1.0`, `read_source`  
**Beleg:** Vom PO bereitgestellter vollständiger Tool-/Chat-Export `Eingefügter Text(20261113-191328).txt` (nicht im öffentlichen Repository veröffentlicht).  
**Status:** **PARTIAL** – beide Abrufe technisch erfolgreich; historischer Versionsnachweis fehlgeschlagen. Keine Produktfreigabe.

## Tatsächlich beobachtet

| Parameter | Test 1: vermeintliche Fassung 1997 | Test 2: Neufassung 2018 |
|---|---|---|
| URL | `https://www.vatican.va/archive/DEU0035/__P86.HTM` | `https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_20180801_catechismo-penadimorte_ge.html` |
| section | `2267` | `2267` |
| status | `TEXT_RETRIEVED` | `TEXT_RETRIEVED` |
| section_marker_found | `true` | `true` |
| semantic_claim_verified | `false` | `false` |
| evidence_id | `ce8530bd29b6393513a7` | `c77f48cfecd191302295` |
| truncated | `true` | `false` |
| Textfassung | Inhalt **entspricht Neufassung 2018**, einschließlich Verweis auf Franziskus 2017 | Neufassung 2018 |
| Kodierung | Fehlerhafte Unicode-Ersatzzeichen `�` | Im beobachteten Ausschnitt korrekt |

**Ausschlaggebend:** Die `/archive/DEU0035/__P86.HTM`-Seite kann trotz Aufschrift „1997“ und Archivpfad **nicht** als Beweis für den alten Wortlaut vor 2018 dienen, denn der tatsächlich abgerufene Absatz enthält die geänderte Fassung. `TEXT_RETRIEVED` bestätigt allein den Abruf, keine historische Fassung.

**LLM-Befund:** Die Modellantwort gibt beide abgerufenen Textblöcke aus, erkennt aber nicht ausdrücklich, dass die als historisch bezeichnete Stelle inhaltlich mit 2018 übereinstimmt. Das ist ein inhaltlicher Plausibilitäts-/Versionsvergleichsfehler, nicht primär ein Transportfehler.

## Befund und Behandlung

- **P03A-F1 (fachlich, hoch): Versionsbehauptung ungeprüft.** Metadaten, Dokumenttitel und URL-Pfad sind keine beweiskräftigen Versionsanker. Der Code darf kein `version_verified=true` aus Host, Titel oder `section_marker_found` ableiten.
- **P03A-F2 (technisch, mittel): Zeichensatzfehler.** Die beschädigten Umlaute in Test 1 deuten auf fehlerhafte Dekodierung bei HTML/HTTP-Charset oder auf bereits fehlerhafte Quelldaten. Es darf nicht stillschweigend behauptet werden, die genaue Ursache sei bekannt. Tatsächliche Content-Type-/Meta-Charset-Werte im gesonderten DEV-Test prüfen; dann Parser anpassen.
- **P03A-F3 (fachlich, mittel): Fehlende Konfliktmeldung durch Modell.** Zwei vermeintlich unterschiedliche Fassungen mit sachlich gleichem Text müssen als `VERSION_CONFLICT` bzw. „historisch nicht verifiziert“ ausgewiesen werden, statt einen historischen Unterschied zu erfinden.

## Nächste Tests

1. **Quellenversion isolieren:** Für den historischen Wortlaut eine tatsächlich **vor dem 2018er Änderungsdatum belegte, datierte** Primärquelle (z. B. authentische archivierte Fassung / ältere amtliche Ausgabe) beschaffen. Das CDF-Begleitschreiben von 2018 zitiert den früheren Wortlaut nur teilweise und ist daher kein Ersatz für einen vollständigen historischen Originaltext.
2. **Negativtest:** Absichtlich eine `1997` etikettierte URL mit 2018er Wortlaut vorlegen; erwartete Modellreaktion: „Versionskonflikt, historischer Originaltext nicht nachgewiesen“.
3. **Charset-Diagnose:** HTTP-Header, HTML-Meta, Rohbytes einer unkritischen Textpassage prüfen und mit passender Charset-Erkennung wiederholen. Kein Eingriff in allgemeine SSRF-Gates.
4. **Quellenstatus differenzieren:** `TEXT_RETRIEVED` und `section_marker_found` beibehalten; eine gesonderte historische Versionsprüfung nur mit beweiskräftigem, externem Versionsanker.

**Abgrenzung:** Der Test prüft weder semantische Vollverifikation noch eine technisch erzwungene Kontrolle aller Antworten (QE F-C1 bleibt offen). Die bestehende THEOBald-Pipe wird nicht als ersetzt betrachtet.
