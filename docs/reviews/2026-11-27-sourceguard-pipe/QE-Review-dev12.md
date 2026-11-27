# Unabhängiger QE-Review – THEOAgent SourceGuard-Pipe dev12

Stand: 27.11.2026. Rolle: unabhängiger Quality Engineer. Keine Freigabe-, Merge- oder Baseline-Entscheidung; der PO entscheidet. Keine Schreiboperationen im Repository.

## 0. Prüfgegenstand und Prüfumgebung

| Punkt | Wert |
|---|---|
| Repository / Branch | baem-oss/THEOAgent, `local-dev`, HEAD `14916ba` (enthält Prüfstand `ef15f87`) |
| Prüfling | `tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py`, Git-Blob `8de0196214419bb38268c341fa95f2bd69f78718` – **verifiziert** (`git hash-object`) |
| Umgebung | Python 3.12.3, `pydantic` nachinstalliert (fehlt sonst; Import bricht vor jedem Test ab) |
| Live-Ausführung | **Nicht möglich** (kein Zugriff auf Open WebUI, OpenRouter, Homeserver, DRS:KI). Alle Live-Aussagen stützen sich ausschließlich auf die vom PO übermittelten Messwerte (Auftrag §1). |
| Eigene Testmittel | `qe_dev12_twophase.py` (QE-Arbeitskopie, realer Zweiphasen-Pipe-Pfad mit Provider-Stub inkl. `finish_reason`/`usage`), dev13-Kandidat als Diff `dev13_candidate_vs_dev12.diff` – beide nur zur Evidenz, kein Merge-Vorschlag |

Kennzeichnung im Bericht: **[N]** nachgewiesen (Code/Test), **[H]** plausible Hypothese, **[O]** offene Frage.

## 1. Kurzfazit

Die zweiphasige Schnittstelle (kompaktes Steuerungs-JSON, Markdown-Antwortphase, Python-Validierung) ist als kleinste robuste Architektur **tragfähig** und der richtige Weg; das zeigen Laufzeit (21,3 s), durchweg `finish_reason=stop` in der Steuerung und die fehlende JSON-Abschneidung in der Fachantwort. Die beiden aktuellen Ausfälle haben **keine architektonische Ursache**, sondern liegen in drei kleinen, isolierbaren Implementierungsdetails:

1. Die **Belegprüfung** stammt aus der dev5-Linie und erkennt gruppierte und nichtkanonische Kennungen nicht. Der Live-Defekt `[S4/Extrakt 1668]` ist damit vollständig erklärt und reproduziert. Die Lösung existiert bereits in dev10 und lässt sich unverändert übernehmen.
2. Das **Formatkorrekturbudget** gilt einmal pro Sitzung statt einmal pro Vorfall. Das ist die nachgewiesene unmittelbare Ursache der Folgefrage-Sperre.
3. Der **Folgekontext** wird ungefiltert als Assistant-Markdown (inkl. Quellenliste, alter Kennungen und ggf. Diagnoseblock) übergeben, und vor dem Steuerungsaufruf steht keine Phaseninstruktion. Das ist die plausibelste Ursache dafür, dass das Modell in der Steuerungsphase Prosa schreibt.

Ein dev13-Kandidat mit genau diesen drei Korrekturen (Reuse aus dev10 plus rund 25 neue Zeilen) besteht in der QE-Arbeitskopie alle vorhandenen Tests (dev12-Protokoll 7/7, historischer Korpus 35 PASS / 0 FAIL / 11 PARTIAL / 1 INFO, AP1, AP2-Zitierung und -Zitate, dev11-Metriken) und 22 von 24 bewerteten eigenen Zweiphasenfällen. Live ist er **nicht** geprüft.

## 2. Antworten auf die Leitfragen des PO

### 2.1 Warum gelingt die Erstanfrage, während die Folgefrage scheitert?

**[N] Unmittelbare Ursache: einmaliges Formatkorrekturbudget pro Sitzung.** In `run_research` wird `format_repairs` einmal auf 0 gesetzt und nie zurückgesetzt (`if format_repairs: raise GuardError(...)`). In der Folgefrage verbrauchte Runde 1 (1024 Tokens, `length` → `ModelOutputError`) das Budget; Runden 2 und 3 waren gültig; Runde 4 (Prosa ohne JSON) führte deshalb direkt zur Sperre. Test FB-02 reproduziert exakt dieses Muster (length → gültig → gültig → Prosa) mit dem Ergebnis NICHT FREIGEGEBEN nach 4 Provideraufrufen. Die Erstanfrage hatte ebenfalls genau einen Formatfehler (Runde 5) und wäre bei einem zweiten ebenso gescheitert. Der Erfolg der Erstanfrage ist daher **kein Beleg für Robustheit**, sondern lag unterhalb derselben Schwelle.

**[N] Strukturelle Unterschiede im Modellkontext der Folgefrage** (Prompt-Inspektion PI-01 bis PI-08 am realen Pipe-Pfad):

- Rollenfolge im Steuerungsaufruf: `system` (THEOBald-Prompt, ca. 21 000 Zeichen) → `system` (AGENT_PROMPT, ca. 3 800 Zeichen) → `user` → **`assistant` (vollständige frühere Fachantwort in Markdown)** → `user` („Nutzerauftrag: Und was sagt er zur Anwendung?“). Das Modell sieht damit unmittelbar vor der neuen Frage ein eigenes Antwortbeispiel im Markdown-Format.
- Die übergebene Vorantwort enthält die Statuszeile, das Quellenverzeichnis und, bei `SHOW_TIMINGS=true`, den gesamten DIAGNOSE-Block mit JSON-Messzeilen (im Test 7 Mess- und 4 Providerzeilen).
- Alte Kennungen `[S1]`–`[S4]` stehen im Kontext, während die neue Recherche den Kennungsraum erneut bei S1 beginnt (Kollision; siehe 2.4).
- Die letzte Nachricht vor jedem Steuerungsaufruf ist eine fachliche Frage; die Formatvorgabe steht nur im zweiten Systemblock hinter dem langen fachlichen Prompt.
- Die Folgefrage lud zwei homiletische Skills, deren Inhalte als `user`-„Werkzeugergebnisse“ mit Arbeits- und Gliederungsanweisungen in die Steuerungsphase gelangen (AP1-B).

**[H] Inhalt der fehlgeschlagenen Runden.** Runde 1 (3505 Zeichen bei 1024 Tokens, ca. 3,4 Zeichen pro Token) entspricht dem Profil deutscher Prosa, nicht einer Aktionsliste (gültige Aktionen lagen bei 79–670 Tokens). Runde 4 (809 Tokens, `stop`, 3153 Zeichen, kein JSON) entspricht dem Profil einer vollständigen Fachantwort nach abgeschlossener Lektüre. Beides ist mit „Modus-Verwechslung“ konsistent: Das Modell antwortet fachlich, statt zu steuern. Ohne Rohausgaben ist das nicht beweisbar.

**[H] Herkunft der Formatabweichung in Runde 5 der Erstanfrage.** Ein häufiges Muster ist das Weglassen der `final`-Hülle (`{"sources_sufficient":true,...}`). Test FB-07 zeigt, dass dev12 dieses Muster korrekt als Formatfehler behandelt und nach einer Korrektur freigibt.

**[O]** Wie der Provider (Gemma über OpenRouter) zwei aufeinanderfolgende Systemnachrichten zusammenführt, und ob der zusätzliche SourceGuard-Hinweis aus dem Systemprompt oder einem Skill stammt, ist offen.

### 2.2 Wie wird die Kommunikation zuverlässiger, ohne neue Architekturkomplexität?

Empfohlen werden vier kleine Maßnahmen innerhalb der bestehenden Pipe, keine neue Phase und kein Provider-Feature:

1. **Formatkorrektur pro Vorfall:** `format_repairs = 0` nach jeder gültigen Aktionsrunde. Die Gesamtschranke bleibt `MAX_ROUNDS = 10`. Das ist eine Zeile.
2. **Transiente Phaseninstruktion:** In `infer()` wird an die letzte `user`-Nachricht ein kurzer Block „[STEUERUNGSPHASE] Antworte jetzt ausschließlich mit EINEM JSON-Objekt …“ angehängt, nur für den Aufruf und nicht in der Historie. Dadurch steht die Formatvorgabe am Ort der stärksten Wirkung, und es entsteht keine zusätzliche Nachricht (Rollenalternierung bleibt erhalten).
3. **Bereinigte Gesprächshistorie:** Frühere Turns werden als **ein** `user`-Kontextblock („nur zur Klärung von Bezügen; keine Evidenz, kein Ausgabeformat“) übergeben, die Vorantwort ohne Statuszeile, Diagnoseblock und Quellenverzeichnis, alte Kennungen ersetzt durch „[früherer Beleg]“, je Nachricht auf 4000 Zeichen gekürzt statt Totalverlust. Die Kontextkontinuität (Bezug „er“ = Klippert, LOCAL_ONLY-Vererbung) bleibt erhalten; die LOCAL_ONLY-Vererbung wird weiterhin aus der ungekürzten Historie berechnet.
4. **Technischer JSON-Hinweis nur in der Steuerungsphase:** Der Präfixsatz „Die folgende Agenten-JSON-Schnittstelle …“ geht derzeit auch an die Antwortphase (PI-05) und widerspricht dort der Markdown-Vorgabe.

Wirkung im Stub (nachgewiesen nur für den Kontrollfluss, nicht für das Modellverhalten): FB-01, FB-02, PI-01 bis PI-08 wechseln von FAIL auf PASS; alle sieben dev12-Protokolltests bleiben PASS. Ob Maßnahme 2 und 3 die Modus-Verwechslung live tatsächlich senken, ist **[H]** und muss mit einer Live-Serie gemessen werden (siehe 5).

Ausdrücklich **nicht** empfohlen: Constrained Decoding oder Function-Calling als Pflicht (widerspricht der PO-Entscheidung zur Providerunabhängigkeit), eine dritte Phase, ein eigener JSON-Reparaturparser oder eine LLM-basierte Belegprüfung. Ein alternatives Steuerformat ist nicht nötig: Die Fehler waren keine JSON-Syntaxfehler, sondern Moduswechsel.

### 2.3 Welche Verbesserungen aus dev10 sollen wiederverwendet werden?

Aus dev10 (2f1446e) sollte **die Belegschicht unverändert übernommen werden, nicht das Protokoll** (die dev10-Probleme – 74 s, keine Originallektüre, ungültiges JSON am Ausgabeende – lagen in der einphasigen Kommunikation, die dev12 bereits gelöst hat).

| dev10-Baustein | Zweck | Status in dev12 |
|---|---|---|
| `normalize_citations` (Gruppen → `[S1] [S2]`) | einheitliche Kennungsgrammatik | fehlt (nur Varianten-Normalisierung) |
| Prüfung auf Rest-`S\d+` nach Entfernen kanonischer Kennungen | sperrt `[S4/Extrakt 1668]`, `(vgl. S99)`, `[S 99]` | fehlt |
| `cited_ids` / `in_text_citation_ids` in `validate_final` | prüft auch gruppierte Kennungen | in dev12 vorhanden, aber **nicht verwendet** (`validate_final` nutzt `CITE`) |
| `strip_model_sources` | modellgeschriebene Quellenlisten entfernen/sperren | fehlt |
| `QUOTE`, `literal_match`, `validate_quotations` | GR-03 für markierte Wortzitate | fehlt |
| `edit_input`, enges `is_text_edit`, `validate_edit_quotations` | reine Sprachrevision vs. fachlicher Auftrag | dev12 nutzt das breite dev5-Muster (F-09/F-09b FAIL) |
| `render_result` über `in_text_citation_ids` | Quellenverzeichnis inkl. gruppierter Kennungen | dev12 nutzt `CITE` (gruppierte fehlen) |

Nachweis: Mit diesen Bausteinen erreicht der Kandidat im historischen Korpus 35/0/11/1, also exakt das dev10-Ergebnis; `test_ap2_citations` und `test_ap2_quotes` laufen durch. `test_ap2_declared_quotes` scheitert auch an dev10 selbst und gehört zur bewusst entfernten dev8/9-Deklarationslösung; dieser Test ist kein Gate für dev13.

### 2.4 Wie wird Belegintegrität zuverlässig gewährleistet, ohne die Nutzbarkeit unverhältnismäßig einzuschränken?

Empfohlen wird eine klare Trennung zwischen dem, was Python deterministisch prüfen kann, und dem, was als Grenze offen ausgewiesen wird:

- **Technisch prüfbar und zu sperren:** ungelesene oder nichtkanonische Kennungen, auch in Gruppen; modellgeschriebene Quellenverzeichnisse; markierte Wortzitate ohne wörtliche Entsprechung in der zugeordneten Passage (GR-03); Absatznummern ohne Bindung; Werkidentität; Kennungen in Metadaten (`coverage`, `works`), die nicht registriert sind.
- **Nicht technisch prüfbar und transparent auszuweisen:** semantische Tragfähigkeit einer Paraphrase. Die bestehende Statuszeile „keine inhaltliche Vollprüfung“ ist dafür die richtige, schlanke Lösung.
- **Fundstellen liefert ausschließlich die Pipe:** Der Lokator (Datei, Extraktzeilen) erscheint im Quellenverzeichnis aus dem Leseprotokoll. Das Modell schreibt nur `[S1]` bzw. `[S1, S2]`. Diese Regel gehört explizit in den Systemtext der Antwortphase (dort fehlt sie bisher).
- **Kennungsraum pro Turn:** Alte Kennungen im Folgekontext neutralisieren (siehe 2.2), damit ein historisches `[S1]` nicht als neues `[S1]` validiert wird.

Nutzbarkeit: Die dev10-Zitatprüfung behandelt **alle** gepaarten Anführungszeichen als Wortzitat. Ein Hervorhebungsgebrauch wie „lebensnah“, der nicht wörtlich in der Passage steht, wird gesperrt (im Kandidaten nachgewiesen). Das ist mit GR-03 konsistent; die schlanke Abmilderung ist eine Promptregel („Anführungszeichen nur für geprüften Wortlaut, Hervorhebung kursiv“) plus die bereits vorhandene einmalige inhaltliche Korrekturrunde, nicht eine Lockerung der Prüfung.

## 3. Testergebnisse

### 3.1 Reproduktion gemäß Auftrag §3 (Prüfling unverändert)

| Test | dev12 | Bemerkung |
|---|---|---|
| `py_compile` | PASS | |
| `test_dev12_protocol.py` | 7/7 PASS | bestätigt PO-Angabe |
| `qe_tests.py` (historischer Korpus) | 21 PASS / 14 FAIL / 11 PARTIAL / 1 INFO | **Einzelfallvergleich durchgeführt:** Status und Ist-Text aller 47 Fälle identisch mit dev5 und dev11. dev10: 35 / 0 / 11 / 1 |
| `test_ap1.py` | 5/5 PASS | **teilweise falsch-positiv**, siehe Befund M2 |
| `test_dev11_metrics.py` | 4/4 PASS | prüft Metrikstrukturen, nicht das neue Protokoll |
| `test_ap2_citations.py`, `test_ap2_quotes.py` | Abbruch | erwartbar, dev5-Linie ohne AP2-Bausteine; dev10: PASS |

Die 14 Korpus-FAILs (B-03 bis B-05, B-07, B-10b bis B-17, F-09, F-09b) sind **keine neue Regression gegenüber dev11/dev5**, aber eine fortbestehende **Regression gegenüber dev10**.

### 3.2 Eigene Zweiphasentests am realen Pipe-Pfad (QE-Arbeitskopie)

PASS/FAIL bezieht sich auf das QE-Soll der Zeile.

| ID | Fall | dev12 | Kandidat |
|---|---|---|---|
| BI-01 | `[S1/Extrakt 1668]` neben gültigem `[S1]` (Live-Defekt) | **FAIL – freigegeben** | PASS (gesperrt) |
| BI-02 | nur nichtkanonische Kennung | PASS | PASS |
| BI-03 | `[S1, S99]` neben `[S1]` | **FAIL – ungelesenes S99 freigegeben** | PASS |
| BI-04 | nur gruppierte Kennung `[S1, S1]` | FAIL – fälschlich gesperrt | PASS |
| BI-05 | erfundenes Wortzitat mit gültiger Kennung (GR-03) | **FAIL – freigegeben** | PASS |
| BI-06 | „Nach Zeile 1668 …“ im Fließtext | FAIL | FAIL (Restrisiko) |
| BI-07 | eigenes Quellenverzeichnis mit `[S99]` | PASS | PASS |
| AM-01 | `final.work` ≠ gelesenes Werk | PASS | PASS |
| AM-02 | Werkauftrag ohne `final.work` | INFO (Freigabe über geprüfte Lesedeklaration) | INFO |
| AM-03 | `coverage` verweist auf ungelesenes S7 | FAIL | FAIL |
| FB-01 | gültig → Prosa → gültig → Prosa | **FAIL** | PASS |
| FB-02 | length → gültig → gültig → Prosa (Live-Muster) | **FAIL** | PASS |
| FB-03 | Antwortphase liefert JSON | PASS | PASS |
| FB-04 | Markdown mit eingebettetem JSON-Codeblock | INFO (freigegeben) | INFO (gesperrt durch Zitatprüfung der Codeanführungszeichen) |
| FB-05 | Antwortphase ohne `finish_reason`/`usage`, Satzabbruch | INFO (freigegeben ohne Hinweis) | INFO |
| FB-06 | `final` mit `answer`-Schlüssel | PASS | PASS |
| FB-07 | Metadaten ohne `final`-Hülle | PASS | PASS |
| PI-01 | keine Vorantwort in `assistant`-Rolle | FAIL | PASS |
| PI-02 | kein Diagnoseballast im Modellkontext | FAIL | PASS |
| PI-03/08 | alte Kennungen neutralisiert | FAIL | PASS |
| PI-04 | Phaseninstruktion unmittelbar vor Steuerungsaufruf | FAIL | PASS |
| PI-05 | kein JSON-Hinweis in der Antwortphase | FAIL | PASS |
| PI-07 | Vorkontext bleibt bei Vorantwort > 12 000 Zeichen erhalten | **FAIL – gesamter Vorkontext entfällt** | PASS |
| AP1-A | Skill autorisiert, Zweiphasenfreigabe, LOCAL_ONLY aus Verlauf | PASS | PASS |
| AP1-C | nicht inventarisierter Skill | PASS | PASS |
| AP1-D | Websuche trotz geerbtem LOCAL_ONLY | PASS | PASS |

Summe: dev12 9 PASS / 15 FAIL / 5 INFO; Kandidat 22 PASS / 2 FAIL / 5 INFO.

## 4. Befunde nach Schweregrad

### K1 – Kritisch: Ungelesene, nichtkanonische und zitierte Belege werden freigegeben

- **Anforderung:** GR-02, GR-03, Akzeptanzprofil T-04 (Belegintegrität)
- **Code:** `validate_final` (dev12 Z. 2981 ff.) nutzt `CITE = r"\[\s*(S\d+)\s*\]"` (Z. 1879) und `_citations_in_prose` (Z. 2948); `render_result` nutzt `set(CITE.findall(...))`.
- **Ist:** Gruppen und Zusätze sind für den Validator unsichtbar. `[S1, S99]` wird freigegeben, sofern irgendwo ein einfaches `[S1]` steht; `[S4/Extrakt 1668]` wird freigegeben und unverändert angezeigt; erfundene Wortzitate werden freigegeben; reine Gruppenbelege werden fälschlich gesperrt.
- **Soll:** Jede Kennung in jeder Schreibweise wird erkannt; nichtkanonische Formen und ungelesene Kennungen sperren; markierte Wortzitate werden am Original geprüft.
- **Evidenz:** BI-01, BI-03, BI-04, BI-05; Korpus B-03 bis B-17. Der Live-Defekt ist damit **nachgewiesen erklärt**.
- **Einordnung:** bekanntes Defizit der dev5-Linie, Regression gegenüber dev10, keine neue Regression gegenüber dev11.
- **Kleinster Fix:** dev10-Bausteine aus 2.3 unverändert übernehmen; in den Systemtext der Antwortphase die Kennungsgrammatik aufnehmen.
- **Restrisiko:** Zeilen- oder Seitenangaben im Fließtext bleiben ungeprüft (BI-06); Hervorhebungsanführungszeichen werden gesperrt; Wortzitate außerhalb der ersten 5000 Zeichen einer Passage (`MAX_SOURCE_CHARS`) oder über Zeilenpräfixe hinweg können fälschlich gesperrt werden **[O]**.

### H1 – Hoch: Formatkorrekturbudget gilt pro Sitzung

- **Anforderung:** Verfügbarkeit, GR-18 (kontrollierte Teilergebnisse statt Totalabbruch)
- **Code:** `run_research`, `format_repairs` (initial 0, nie zurückgesetzt; Sperre im `except ModelOutputError`-Zweig)
- **Ist / Soll:** Ein früher Fehler (z. B. Abschneidung in Runde 1) verbraucht die einzige Korrektur für die ganze Recherche. Soll: eine Korrektur pro Vorfall, gesamt begrenzt durch das Rundenbudget.
- **Evidenz:** FB-01, FB-02; Live-Verlauf der Folgefrage stimmt exakt mit FB-02 überein.
- **Einordnung:** strukturell seit dev11 vorhanden; in dev12 folgenschwerer, weil `length` in der Steuerung nun ebenfalls als Formatfehler zählt.
- **Kleinster Fix:** `format_repairs = 0` nach gültiger Aktionsrunde (eine Zeile).
- **Restrisiko:** Abwechselnde Fehler verlängern die Laufzeit bis höchstens `MAX_ROUNDS`; in den Metriken sichtbar.

### H2 – Hoch: Folgekontext begünstigt Modus-Verwechslung und Kennungskollision

- **Anforderung:** Kontextkontinuität bei Folgefragen, GR-02 (historische Antworten keine Evidenz), Datenschutz/Ballast
- **Code:** `Pipe.pipe`, Aufbau von `conversation` (Rolle und Inhalt unverändert), `completion()` (keine Phaseninstruktion)
- **Ist:** siehe 2.1 (PI-01 bis PI-04, PI-08).
- **Evidenz:** Kontextstruktur **[N]**; Ursächlichkeit für Runde 1 und 4 **[H]**.
- **Kleinster Fix:** Maßnahmen 2 und 3 aus 2.2 (zusammen rund 15 Zeilen).
- **Restrisiko:** Die Wirkung auf das Modellverhalten ist nur live messbar; Kürzung auf 4000 Zeichen je Turn kann bei sehr langen Vorantworten Details entfernen.

### M1 – Mittel: Widersprüchliche Anweisung und fehlende Kennungsgrammatik in der Antwortphase

- **Code:** `prefix += "Technische Ausführung: Die folgende Agenten-JSON-Schnittstelle …"` geht an beide Phasen; `compose()` ersetzt nur den AGENT_PROMPT-Block. Der Antwortphasentext nennt `[S1]`, verbietet aber keine Zusätze.
- **Evidenz:** PI-05 **[N]**; Beitrag zu `[S4/Extrakt 1668]` **[H]** (die Zeilenzahl 1668 stammt plausibel aus einem Such- oder Inventartreffer, nicht aus der registrierten Lektüre).
- **Kleinster Fix:** Hinweis nur in der Steuerungsphase anhängen; Grammatiksatz im `compose`-Systemtext.

### M2 – Mittel: Testaussagekraft für den Zweiphasenpfad ist gering

- **Code/Test:** `run_research(..., compose=None)` behält den alten einphasigen Pfad; `qe_tests.py`, `test_ap1.py` (AP1-06) und die AP2-Tests rufen ihn bzw. `validate_final` direkt. Der Harness-Stub liefert weder `finish_reason` noch `usage`.
- **Ist:** Die Gleichheit 21/14/11/1 ist zwar eine **Einzelfallidentität** mit dev5/dev11, belegt aber nichts über den produktiven Zweiphasenpfad. AP1-02/03 besteht unter dev12 nur, weil das alte Wire-Format abgewiesen wird und der Stub danach mit `IndexError` leerläuft (Diagnose: „Unbekannter Modellfehler: IndexError“) – **falsch-positiv**.
- **Kleinster Fix:** Harness um Provider-Stub mit `finish_reason`/`usage` erweitern (Vorlage: `qe_dev12_twophase.py`), AP1-Fixtures auf Metadaten-`final` plus Markdown umstellen, Assertions auf die konkrete Sperrursache schärfen; mittelfristig `compose` in der Pipe verpflichtend machen und den Altpfad nur noch für Validatortests nutzen.

### M3 – Mittel: Vollständiger Verlust des Vorkontexts bei langer Vorantwort

- **Code:** Schleife über `reversed(prior[-12:])` bricht bei der ersten Nachricht über dem Restbudget (12 000 Zeichen) ab.
- **Ist:** Ist die Vorantwort zu lang (etwa mit Diagnoseblock), entfallen **alle** früheren Nachrichten, auch die Ursprungsfrage; „er“ verliert den Bezug (PI-07).
- **Kleinster Fix:** je Nachricht kürzen statt abbrechen (im Kandidaten enthalten).

### N1 – Niedrig: Metadatenkennungen nur bei Pflichtaufzählungen geprüft

`coverage` mit ungelesenem S7 wird ohne Pflichtteilthemen akzeptiert (AM-03). Fix: unbekannte Kennungen in `coverage` und `works` generell sperren (wenige Zeilen).

### N2 – Niedrig: Fehlende Provider-Metadaten in der Antwortphase

Ohne `finish_reason` kann Abschneidung nicht erkannt werden; ein mitten im Satz endender Text wird freigegeben (FB-05). Der Fail-closed-Pfad für `length` ist korrekt. Fix im Sinne von KISS: Diagnosehinweis „Abschneidung nicht prüfbar (finish_reason fehlt)“, keine Heuristik.

### N3 – Niedrig: JSON-Erkennung der Antwortphase nur über das Präfix

Ein Markdown-Text mit eingebettetem JSON-Block passiert (FB-04). Vertretbar; nur beobachten.

### I1 – Info: Metriken

Korrekt zugeordnet (Phase, `max_tokens`, `finish_reason`, Token- und Zeichenzahlen je Aufruf; Rundenzählung schließt die Antwortphase ein, daher 7 Runden bei 6 Steuerrunden). Kein Rohinhalt, Systemprompt nur als Länge und SHA-256. Overhead vernachlässigbar. Einziger Datenschutz- und Ballastaspekt: Der sichtbare Diagnoseblock wird Teil der Chat-Historie und gelangte bisher zurück in den Modellkontext; durch H2-Fix behoben.

## 5. Empfehlung für dev13 (priorisiert nach Nutzen, Risiko, Aufwand)

| Prio | Maßnahme | Nutzen | Risiko | Aufwand |
|---|---|---|---|---|
| 1 | dev10-Belegschicht unverändert übernehmen (2.3) und Kennungsgrammatik im Antwortphasentext | schließt K1 inkl. Live-Defekt | niedrig, durch Korpus und AP2 abgesichert | S |
| 2 | Formatkorrektur pro Vorfall | behebt nachgewiesene Ursache der Folgefrage-Sperre | niedrig | XS |
| 3 | Folgekontext bereinigen, transiente Phaseninstruktion, JSON-Hinweis nur in Steuerung, Kürzung je Nachricht | adressiert H2, M1, M3 | niedrig bis mittel (Wirkung nur live messbar) | S |
| 4 | Testmigration: Zweiphasen-Stub mit Provider-Metadaten in die Regression, AP1-Assertions schärfen | macht künftige PASS-Ergebnisse aussagekräftig | keines | S |
| 5 | N1 und N2 | Restlücken | keines | XS |

Ein in der QE-Arbeitskopie erstellter Kandidat setzt Prio 1–3 um (Diff gegen dev12 beigefügt, rund 140 geänderte Zeilen, davon der überwiegende Teil unveränderter dev10-Code). Er ist ausschließlich Evidenz für Machbarkeit und Testwirkung, **kein Merge-Vorschlag**.

**Vorgeschlagene Live-Abnahme für dev13** (Entscheidung beim PO): je 10 Läufe von Klippert-Erstanfrage und Folgefrage im selben Chat, Websuche aus, einmal mit `SHOW_TIMINGS` an und aus. Zu erfassen: Freigabequote, Formatkorrekturen pro Lauf, Anzahl Steuerrunden, `finish_reason` je Aufruf, Gesamtlaufzeit sowie manuelle Stichprobe, ob jede Kennung im Text auf eine im Quellenverzeichnis genannte, tatsächlich passende Extraktstelle zeigt. Orientierungswert aus dev5: Erstanfrage um 23 s, Folgefrage um 17 s.

## 6. Offene Fragen

1. Inhalt der Runden 1 und 4 der Folgefrage. Vorschlag: bei Formatfehlern die ersten 200 Zeichen der Rohausgabe nur im Diagnosemodus protokollieren (Datenschutzabwägung durch PO).
2. Behandlung zweier aufeinanderfolgender Systemnachrichten durch den Provider bei Gemma.
3. Herkunft der Zeilenzahl 1668 (Such- bzw. Inventartreffer oder früheres Lesefenster).
4. Ob Zeilenangaben im Fließtext künftig deterministisch gegen den Lokator geprüft oder per Promptregel ausgeschlossen werden sollen (BI-06).
5. Ob Hervorhebungsanführungszeichen künftig zulässig sein sollen; aus QE-Sicht ist die strikte GR-03-Auslegung vorzuziehen.

## 7. Reproduktion der QE-Ergebnisse

```bash
# im Repository-Root, Branch local-dev
pip install pydantic
export SG_PIPE=tools/local_dev/sourceguard_pipe_v0_5_5_dev12.py
python -m py_compile "$SG_PIPE"
python tests/local_dev/regression/test_dev12_protocol.py
python tests/local_dev/qe_reference/qe_tests.py            # für Einzelfallvergleich mit SG_PIPE=dev5/dev10/dev11 wiederholen
THEOAGENT_ROOT=. python qe_dev12_twophase.py               # eigene Zweiphasentests
# Kandidat: Kopie von dev12 anlegen, Diff anwenden, SG_PIPE darauf setzen und dieselben Tests ausführen
cp "$SG_PIPE" /tmp/dev13_candidate.py && patch /tmp/dev13_candidate.py dev13_candidate_vs_dev12.diff
```
