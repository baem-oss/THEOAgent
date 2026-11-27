# QE-Review SourceGuard v0.5.5-dev3 (THEOAgent)

Nov 27, 2026 · @BäM

## Executive Summary

Die agentische SourceGuard-Pipe ist eine tragfähige Entwicklungsgrundlage, aber noch nicht für Freigaben mit dem Hinweis „technisch geprüft“ geeignet. Vier bis fünf gezielte P0-Korrekturen genügen; eine Neuimplementierung ist nicht nötig.

**Was funktioniert:** Der fail-closed-Kern arbeitet zuverlässig. Alle acht Sperrfälle ohne oder mit unzureichender Lektüre wurden korrekt gesperrt (F-01 bis F-08). Werkidentitätsprüfung, Absatznummernbindung, Budgets und die Beschränkung auf die vom Nutzer gewählte URL arbeiten korrekt. Die agentische Recherche ist der Legacy-Pipeline deutlich überlegen.

**Wesentliche Risiken:** Die Pipe kann einen Beleg als geprüft anzeigen, obwohl er nicht gelesen oder sein Wortlaut erfunden wurde. Reproduziert wurden:

- Freigabe nicht registrierter Kennungen in kombinierten oder abweichenden Schreibweisen (`[S1, S99]`, `[S1 und S99]`, `[S1–S9]`).
- Freigabe eines erfundenen Wortzitats mit gültiger Kennung.
- Quellenpflichtige Aufträge mit Bearbeitungsverb laufen ohne Prüfung als „OHNE QUELLENPFLICHT“.

Das verletzt NFANF-13 (Null-Fehler-Kriterium) und GR-03. Zusätzlich erreichen Systemprompt und Fachskills das Agentenmodell nach Codelage nicht oder nur gekürzt, und fehlerhafte Werkzeugargumente beenden die gesamte Recherche sofort.

**Leitfrage:** Ja, die Architektur trägt. Vor weiterer fachlicher Erprobung sind QE-01 bis QE-05 zu beheben.

## Verifizierte Reviewbasis

Geprüft wurde der Stand `ab93b8128651c4daea3281c20ae461759634e61c` auf `local-dev`; er entspricht dem Ausgangscommit des Auftrags.

| Gegenstand | Verifizierter Stand |
| --- | --- |
| Repository / Branch | `baem-oss/THEOAgent`, `local-dev` |
| Aktuelle Implementierung | `tools/local_dev/sourceguard_pipe_v0_5_5_dev3.py`, 3.662 Zeilen, SHA-256 `d69af656ba5fc6ba811ae8b7b82a73226de4cda41454405ba34fd0f641ba5ba0` |
| Vergleichsimplementierung | `tools/local_dev/sourceguard_pipe_v0_5_3.py`, 1.452 Zeilen, SHA-256 `bdb59f41795a7d25dd529326dcb4ee3283ae4502f57e91afdf71c8ff0cae6484` |
| Requirements | `docs/requirements/BASELINE.md` v1.2.0, identisch auf `local-dev` und `main` |
| Systemprompt | `THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md`, 20.916 Zeichen |
| Open WebUI | Tag v0.11.4 (`8bd8b4fa…`): `utils/tools.py`, `utils/middleware.py`, `functions.py`, `tools/builtin.py`, `retrieval/web/utils.py`, `retrieval/utils.py` |
| Testumgebung | Python 3.12.3, pydantic 2.14.4; unveränderte Kopie (Hash geprüft); Open-WebUI-Importe gestubbt; Zugriff auf innere Agentenfunktionen über Closure-Zellen, ohne Codeänderung |

Die Fachbibliotheksvolltexte liegen nicht im Repository (RANF-03); die Tests nutzen daher eine synthetische Bibliothek.

## Findings

Zwei Findings sind CRITICAL, sechs MAJOR; alle betreffen Belegintegrität, Werkzeugsteuerung oder Kontextweitergabe, nicht die Grundarchitektur.

| ID | Schwere | Kurzbeschreibung | Anforderung | Evidenz |
| --- | --- | --- | --- | --- |
| QE-01 | CRITICAL | Zwei Belegkennungs-Grammatiken: unbekannte Kennungen freigegeben, gelesene fehlen im Verzeichnis | NFANF-13, DAT-02 | Code + Unit-Test |
| QE-02 | CRITICAL | Kein Wortlautabgleich für Zitate | GR-03, NFANF-13 | Code + Unit-Test |
| QE-03 | MAJOR | Textbearbeitungs-Klassifikation umgeht Quellenpflicht | GR-17, GR-03 | Code + Simulation |
| QE-04 | MAJOR | Systemprompt und Fachskills im Agent-Modus nicht wirksam | GR-05, SP-01 | Code + gestubbter Test; Live offen |
| QE-05 | MAJOR | Argumentfehler führen zum Totalabbruch; Diagnose undifferenziert | NFANF-03, FANF-06 | Code + Simulation |
| QE-06 | MINOR | Webwerkzeuge fehlen im Preflight | NFANF-11 | Code |
| QE-07 | MAJOR | Nicht-Freigabe verwirft Modellbegründung; keine Teilergebnisse | GR-18, FANF-09, NFANF-11 | Simulation |
| QE-08 | MINOR | Veraltete Prüfmeldung in Freigabe-Diagnose | NFANF-11 | Simulation |
| QE-09 | INFO | Überlappende Lesefenster als getrennte Belege | DAT-02 | Simulation |
| QE-10 | MINOR | Verbleibende lexikalische Heuristiken | FANF-05 | Code |
| QE-11 | MINOR | Datei-IDs aus Freitext registrierbar | SP-02, Quellenzulassung | Code |
| QE-12 | MAJOR | Keine technische Vertraulichkeitskontrolle für Suchanfragen | SP-01, SP-02 | Code |
| QE-13 | MAJOR | Gesprächskontext und Quellenbeschränkung gehen bei Folgefragen verloren | DAT-04, GR-15, FANF-19 | Gestubbter Test |
| QE-14 | INFO | Duplizierter Code, parallele Betriebsarten | NFANF-10 | Statische Analyse |

### QE-01 – Belegkennungen (CRITICAL)

**Ursache:** `CITE` (Z. 1876) erkennt nur Einzelkennungen und wird in `validate_final` (Z. 2979, 2987), `_citations_in_prose` (Z. 2938) und `render_result` (Z. 3521) verwendet. `CITATION` erkennt kombinierte Kennungen, wird aber nur in `check_number_binding` und `cited_ids` genutzt. Die vorhandene Funktion `in_text_citation_ids` (Z. 2597) wird im Agent-Modus nie aufgerufen.

**Reproduziert:**

- `[S1] … [S1, S99]` wird freigegeben (B-05), ebenso `[S1 und S99]`, `[S1–S9]`, `(vgl. S99)`, `[S 99]` (B-12 bis B-15), jeweils mit „Belegkennungen technisch geprüft“.
- Die Werkzuordnung entfällt für Kennungen, die nur kombiniert vorkommen (B-10b).
- S2 fehlt im Quellenverzeichnis (B-16) – das P-03-Symptom.
- Der Textbearbeitungs-Pfad akzeptiert `[S1, S2]` (B-17).
- Ausschließlich kombinierte Belege werden fälschlich gesperrt (B-03, B-04, B-07).

**SE-Fix:** deckt alle `CITE`-Pfade ab, wenn er in `normalize_citations` umgesetzt wird, weil `validate_final` zuerst normalisiert und das Ergebnis an `render_result` weitergibt. B-12 bis B-15 deckt er nicht ab.

**Empfehlung:** SE-Fix umsetzen und eine fail-closed-Restregel ergänzen: Jedes `\bS\d+\b` im Antworttext muss registriert sein und in kanonischer Form stehen, sonst eine Korrekturrunde, dann Sperre. `CITE.findall` durch `cited_ids` und `_citations_in_prose` durch `in_text_citation_ids` ersetzen (Reuse before Build). Regressionstests: B-01 bis B-17.

### QE-02 – Kein Wortlautabgleich (CRITICAL)

Keine Funktion vergleicht Zitate mit dem registrierten Originaltext. Ein erfundenes Zitat mit gültigem `[S1]` wird freigegeben (B-11) – exakt die Fehlerklasse aus R-01.

**Empfehlung (deterministisch, ca. 40–60 Zeilen):**

1. Zitate in „…“, "…", »…«, ‚…‘ ab etwa 5 Wörtern in Sätzen mit Belegkennung extrahieren.
2. Zitat und Quelle gleich normalisieren: NFKC, Anführungszeichen und Striche vereinheitlichen, weiche Trennstriche entfernen, Silbentrennung wie `join_lines`, Leerraum zusammenfassen.
3. An Auslassungen (`[…]`, `(…)`, `...`) segmentieren; jedes Segment muss im `content` einer im selben Satz zitierten Kennung stehen.
4. Bei Abweichung eine Korrekturrunde („wörtlich zitieren oder ohne Anführungszeichen paraphrasieren“), dann Sperre.

Grenze: Kurze Begriffe, Titel und Paraphrasen bleiben ungeprüft; das ist zu dokumentieren.

### QE-03 – Textbearbeitung umgeht Quellenpflicht (MAJOR)

`is_text_edit` (Z. 1972) klassifiziert nach dem Anfangsverb. „Kürze … und ergänze, was Dei Verbum 12 lehrt“ und „Korrigiere: Klippert fordert …“ laufen als „OHNE QUELLENPFLICHT“ ohne jede Prüfung (F-09, F-09b).

**Empfehlung:** Ausnahme behalten, aber im Textbearbeitungsmodus keine Kennungen (folgt aus QE-01) und Anführungszeichen-Inhalte nur zulassen, wenn sie im Nutzertext vorkommen.

### QE-04 – Systemprompt und Fachskills (MAJOR)

Der Agent verwirft jede Systemnachricht mit `<attached_knowledge>`. Open WebUI v0.11.4 hängt dieses Tag und `<available_skills>` an die erste Systemnachricht (`middleware.py` Z. \~3103–3123); `functions.py` (Z. 298) stellt den Modell-Systemprompt in dieselbe Nachricht. Ersatzweise wird `__metadata__["system_prompt"][:12000]` verwendet.

- Gestubbter Test I-01: Nur 12.000 von 20.916 Zeichen erreichen das Modell.
- v0.3.11 verlangt `view_skill`, `read_source`, `review_evidence`; ein `view_skill`-Aufruf beendet die gesamte Recherche (A-11).
- Folge: Fachskills sind im Agent-Modus praktisch nicht nutzbar; die Vertraulichkeitsregeln aus §1 erreichen das Modell möglicherweise nicht.

**Empfehlung:** nur die Tags entfernen statt der ganzen Nachricht; nicht stillschweigend kürzen; `view_skill` als nur-lesendes Werkzeug zulassen (Rückgabe = Daten, keine Evidenz); agentenspezifischer Systemprompt als PO-Entscheidung.

### QE-05 – Werkzeugargumente (MAJOR)

Jeder `GuardError` aus `_validate_args` beendet die Recherche. Reproduziert für fehlendes, leeres, falsch typisiertes und überlanges `query` (A-02 bis A-07), `query` auf Aktionsebene oder `arguments` statt `args` (A-07c, A-07d), das native Argument `count` (A-08) und `search_web` mit weiterer Aktion (A-10). Die P-04-Diagnose wurde identisch nachgebildet.

**P-04:** Der DV-12-Prompt hat 190 Zeichen; übernommen als Suchausdruck überschreitet er 180. Gleich plausibel ist ein falsch strukturierter Aufruf. Die Ursache ist nicht bestimmbar, weil abgewiesene Argumente nicht protokolliert werden. Der Agent-Prompt nennt weder die 180-Zeichen-Grenze noch die Regel „Websuche als eigener Schritt“.

**Empfehlung:**

- Den Korrekturmechanismus für Lesefenster auf alle Argumentfehler verallgemeinern: gemeinsamer Zähler, keine Ausführung, kein zweiter identischer Versuch.
- Fehlercodes unterscheiden (MISSING, TYPE, EMPTY, TOO\_LONG mit Länge, EXTRA\_ARG); nur Klasse und Länge protokollieren.
- Prompttext aus derselben `permitted`-Tabelle erzeugen; `count` begrenzt zulassen; Grenzen nicht lockern.

### QE-06 – Web-Preflight (MINOR)

Die Validierung läuft vor der Verfügbarkeitsprüfung; P-04 beweist daher weder Fehlen noch Vorhandensein der Webwerkzeuge. In OWUI v0.11.4 (`get_builtin_tools`) werden `search_web` und `fetch_url` nur bereitgestellt, wenn alle Bedingungen erfüllt sind:

- natives Function Calling mit Session (nicht `legacy`)
- `builtinTools.web_search` nicht deaktiviert
- `web.search.enable` aktiv
- Modellfähigkeit `web_search` vorhanden (Standard: true)
- Chat-Schalter `features.web_search` an
- Benutzerberechtigung vorhanden

Die Werkzeuge erreichen die Pipe über `metadata['tools']` als `__tools__` (`functions.py` Z. 282). Eine eigene Webanbindung ist nach Codelage nicht nötig. **Empfehlung:** `search_web`, `fetch_url` und `view_skill` in den Preflight aufnehmen.

### QE-07 – Begründete Nicht-Freigabe (MAJOR)

Bei `sources_sufficient=false` sieht der Nutzer nur „Modell bestätigt nicht, dass die Quellen ausreichen“. Die Begründung, die der Agent-Prompt ausdrücklich verlangt, wird verworfen; die eigentliche Ursache (z. B. „search\_web=Fehler“) steht nur in der Admin-Diagnose. **Empfehlung:** Begründung nach denselben Kennungs- und Zitatprüfungen anzeigen und um eine faktische Liste fehlgeschlagener Zugriffe ergänzen; Teilergebnisse nach GR-18 entscheidet der PO.

### QE-08 – Veraltete Prüfmeldung (MINOR)

Die P-03-Meldung „Keine Originalstelle…“ stammt aus einer ersten, korrigierten Abschlussantwort vor der Lektüre. Sie bleibt ohne Kennzeichnung in der Diagnose (F-10) und verbraucht das einzige Korrekturbudget. **Empfehlung:** Rundennummer und „(korrigiert in Runde n)“ ergänzen.

### QE-09 – Überlappende Lesefenster (INFO)

In P-03 überlappen die Kontextlektüren zu den Ankern 2062, 2064 und 2071; S2, S3 und S4 sind nahezu dieselbe Stelle. Registriert wird nach Anfragefenster, nicht nach Passage. **Empfehlung:** nach `(file_id, Passagenzeilen)` deduplizieren.

### QE-10 – Lexikalische Heuristiken (MINOR)

Im Agent-Modus greift die Themensperre nur, wenn das Thema ohnehin in den ersten 1.500 Zeichen steht; die P-02-Sperre ist damit weitgehend wirkungslos. Weiter aktiv: Prosa-Mindestquoten, mindestens 3 vollständige Sätze, Sperre beim Wort „Inhaltsverzeichnis“ irgendwo in der Passage, Rest-Themencheck auf 1.500 Zeichen. Die Relevanz der in P-02 verworfenen Passagen bleibt ungeprüft, da die Texte nicht verfügbar sind.

### QE-11 – Datei-ID-Registrierung (MINOR)

`view_knowledge_file` prüft in OWUI nur Benutzerrechte, nicht die dem Modell zugeordnete Sammlung; Administratoren sehen alles. Die Pipe schützt über das `known`-Gate, doch `_tool_known_files` (Z. 3042) übernimmt IDs auch aus Freitext und verschachtelten Feldern beliebiger Rückgaben – ein theoretischer Pfad für indirekte Injection. **Empfehlung:** IDs nur aus strukturierten Feldern von Inventar- und Grep-Ergebnissen übernehmen.

### QE-12 – Vertraulichkeit und Web (MAJOR)

Suchausdrücke werden technisch nicht auf vertrauliche Inhalte geprüft; der Agent-Prompt enthält keine Vertraulichkeitsregel, und der Systemprompt kommt eventuell nicht an (QE-04). SSRF (SP-03): Die Pipe prüft nur Syntax; der eigentliche Schutz ist `validate_url` in OWUI (DNS-Auflösung, Blockade nicht-globaler Adressen, Probe ohne Weiterleitung, Rebinding-Schutz) und gilt nur bei deaktiviertem `ENABLE_LOCAL_WEB_FETCH`. Die `final_url`-Prüfung der Pipe ist toter Code, weil `fetch_url` Text liefert.

### QE-13 – Gesprächskontext (MAJOR)

Der Agent erhält nur die letzte Nutzernachricht (I-02). Bei „Und was sagt er zur Anwendung?“ fehlen Werk und Quellenbeschränkung; eine zuvor verlangte Beschränkung auf die Fachbibliothek wird nicht mehr durchgesetzt. **Empfehlung:** begrenzten Verlauf übergeben (wie Legacy: 6 Runden / 12.000 Zeichen); ob Beschränkungen fortgelten, entscheidet der PO.

### QE-14 – Code-Duplikate (INFO)

- Legacy-Bereich 1.844 Zeilen, Agent-Bereich 1.787 Zeilen.
- 34 Hilfsfunktionen doppelt definiert, 25 davon AST-identisch (241 Zeilen), 9 abweichend.
- 3 Funktionen im Agent-Bereich nie verwendet: `is_substantive`, `citation_traces`, `in_text_citation_ids`.
- Die Duplikate sind die Ursache von QE-01.
- Eine Pipe ist eine Open-WebUI-Funktion; ohne Administrationsrechte ist sie auf DRS:KI nicht installierbar. Die Übertragbarkeit hängt von einer Betreiberentscheidung ab.

## Disposition der SE-Findings

Drei der vier SE-Findings sind bestätigt; SE-F01 und SE-F04 stufe ich auf CRITICAL hoch.

| SE-Finding | Disposition | Schwere QE | Begründung |
| --- | --- | --- | --- |
| SE-F01 | bestätigt, erweitert (→ QE-01) | CRITICAL (SE: MAJOR) | Der Hinweis „geprüft“ erscheint bei nicht registrierter Kennung; NFANF-13 ist ein Null-Fehler-Kriterium. Der Fix reicht ohne Restregel nicht für B-12 bis B-15. |
| SE-F02 | bestätigt, erweitert (→ QE-05) | MAJOR | Zusätzlich betroffen: `count`, Mehrfachaktionen, `view_skill`, falsch strukturierte Aufrufe. Die P-04-Ursache ist nicht bestimmbar. |
| SE-F03 | teilweise bestätigt (→ QE-10) | MINOR | Die harte Themensperre ist im Agent-Modus weitgehend wirkungslos; andere Heuristiken bleiben. Die P-02-Relevanz ist nicht prüfbar. |
| SE-F04 | bestätigt (→ QE-02) | CRITICAL | Kein Abgleich im Code; reproduziert durch B-11. Genau die R-01-Fehlerklasse. |

## Testergebnisse

47 Fälle wurden tatsächlich ausgeführt: 19 PASS, 16 FAIL, 11 PARTIAL, 1 INFO. Es gab keine Integrationstests mit echtem Open WebUI, keine Live-Tests und keine fachliche Abnahme.

| Testart | Fälle | PASS | FAIL | PARTIAL |
| --- | --- | --- | --- | --- |
| Unit-Tests: Belegkennungen | B-01 bis B-17 (19) | B-01, B-02, B-06, B-08, B-09, B-09b, B-10 | B-03, B-04, B-05, B-07, B-10b, B-11 bis B-17 | – |
| Simulierte Werkzeugrückgaben: Argumente | A-01 bis A-12 (13) | A-01, A-06 (Grenzwert 180), A-09, A-12 | – | A-02 bis A-04, A-07, A-07b bis A-07d, A-08, A-10, A-11 |
| Simulierte Werkzeugrückgaben: Freigabe | F-01 bis F-11 (13) | F-01 bis F-08 | F-09, F-09b | F-10 (F-11: INFO) |
| Pipe-Integration, gestubbt | I-01, I-02 | – | I-01, I-02 | – |

PARTIAL bei A-Fällen bedeutet: kontrolliert gesperrt, aber Totalabbruch ohne Korrekturchance und mit undifferenzierter Meldung. Der Fall „wiederholter identischer Fehler“ ist nicht anwendbar, weil schon der erste Fehler abbricht.

**Einschränkung:** Bibliothek synthetisch, Modell durch Skripte ersetzt. Die Tests weisen das Verhalten der Prüflogik nach, nicht das Verhalten von Gemma. Testskripte und Referenzlauf liegen als Dateien bei (`harness.py`, `qe_tests.py`, `qe_testergebnisse.md`).

## Priorisierte Korrekturmaßnahmen

Fünf P0-Maßnahmen sind vor weiterer fachlicher Erprobung nötig; alle sind mit geringem bis mittlerem Aufwand umsetzbar.

| Prio | Maßnahme | Findings | Nutzen | Aufwand | Risiko der Änderung |
| --- | --- | --- | --- | --- | --- |
| P0 | Eine Belegkennungs-Grammatik + fail-closed-Restregel | QE-01 | hoch | gering | gering |
| P0 | Deterministische Zitatprüfung | QE-02 | hoch | mittel (ca. 40–60 Zeilen) | gering bis mittel (Fehlsperren bei Normalisierungslücken) |
| P0 | Kennungs- und Zitatsperre im Textbearbeitungsmodus | QE-03 | hoch | gering | gering |
| P0 | Korrekturrunde für Argumentfehler, differenzierte Diagnose, Prompt aus Validierungskonstanten, Web-Preflight | QE-05, QE-06 | hoch (entsperrt P-04) | gering bis mittel | gering |
| P0 | Systemprompt ohne Verwerfen/Kürzen übergeben; Entscheidung zu `view_skill` | QE-04 | hoch | gering (Technik) + PO-Entscheidung | mittel (Prompt-Konflikte) |
| P1 | Begründete Nicht-Freigabe anzeigen | QE-07 | mittel | gering | gering |
| P1 | Begrenzten Gesprächsverlauf übergeben | QE-13 | mittel | gering | mittel (Quellenbeschränkung) |
| P1 | Vertraulichkeitsregel für Websuche | QE-12 | hoch | gering (Prompt) bis mittel (Technik) | gering |
| P1 | Datei-IDs nur aus strukturierten Feldern | QE-11 | gering | gering | gering |
| P1 | Diagnose-Kennzeichnung korrigierter Prüfmeldungen | QE-08 | gering | gering | gering |
| P2 | Duplikate entfernen, Legacy nach Regressionsset stilllegen | QE-14 | hoch (Wartbarkeit) | mittel | mittel |
| P2 | Evidenz-Deduplizierung, Heuristik-Feintuning | QE-09, QE-10 | gering | gering | gering |

Vor der Stilllegung des Legacy-Modus sind seine Invarianten als Tests zu sichern: Nachweispflicht für ausdrücklich verlangte Nummern (KKK-1499-Fall), Absatznummernbindung, Ablauf der Webauswahl.

## Entwicklungsreihenfolge

Belegintegrität zuerst, dann Werkzeugsteuerung, dann Live-Tests; Konsolidierung erst, wenn das Regressionsset grün ist.

1. Belegkennungen (QE-01) mit Regressionstests B-01 bis B-17.
2. Wortlautprüfung (QE-02) und Textbearbeitungsmodus (QE-03), mit B-11, F-09, F-09b.
3. Werkzeugargumente und Diagnose (QE-05, QE-06), mit A-02 bis A-11.
4. Live-Tests L-01 und L-02 (Websuche, DV 12).
5. Systemprompt und Skills (QE-04) nach PO-Entscheidung; Live-Test L-03.
6. Begründete Nicht-Freigabe, Gesprächskontext, Vertraulichkeit (QE-07, QE-13, QE-12).
7. Wiederholung von P-03 mit fachlichem Abgleich der Belege S1 bis S5.
8. Konsolidierung (QE-14) und Stilllegung des Legacy-Modus.

## Offene Punkte und Restrisiken

Sieben Live-Tests und acht PO-Entscheidungen sind offen; die Aussagen zu QE-04 beruhen bis dahin auf Code und gestubbtem Test.

**Erforderliche Live-Tests:**

| ID | Prüfgegenstand |
| --- | --- |
| L-01 | Preflight bei aktivierter Websuche mit kurzem Suchausdruck |
| L-02 | DV 12 mit verbesserter Diagnose, um die P-04-Ursache zu klären |
| L-03 | Länge und Hash des an das Agentenmodell übergebenen Systemprompts; Vorhandensein von `<available_skills>` |
| L-04 | Verhalten von Gemma bei zwei Systemnachrichten |
| L-05 | `ENABLE_LOCAL_WEB_FETCH` und `WEB_FETCH_FILTER_LIST` auf Homeserver und DRS:KI |
| L-06 | Folgefrage nach einer Klippert-Anfrage |
| L-07 | Fachliche Prüfung der in P-02 verworfenen Passagen und der Belege S1 bis S5 aus P-03 |

**Notwendige PO-Entscheidungen:**

- [ ] Teilergebnisse nach GR-18 und Anzeige begründeter Nicht-Freigaben
- [ ] Agentenspezifischer oder angepasster Systemprompt
- [ ] Nutzung von `view_skill` im Agent-Modus
- [ ] Fortgeltung von Quellenbeschränkungen über mehrere Gesprächsrunden
- [ ] Web-Vertraulichkeitsregel
- [ ] Mindestlänge geprüfter Zitate
- [ ] Stilllegung des Legacy-Modus
- [ ] Bereitstellung auf DRS:KI

**Nicht verifizierbar:** Die genaue Zusammensetzung von `metadata['system_prompt']` im laufenden Betrieb, also ob das Frontend den Modell-Systemprompt mitsendet.

Alle Korrekturvorschläge sind Empfehlungen; sie wurden weder implementiert noch als Prototyp getestet. Am Repository wurde nichts verändert.