# QS-Architektur-Review: THEOBald-Integration in DRS:KI

**Art:** Architektur- und Code-Review (kein Implementierungsauftrag) [1][3]  
**Datum:** 2026-11-13 · **Prüfer:** Quality Engineer (unabhängig)  
**Prüfpaket:** THEOBald_DRS-KI_QE_Quellcodes_2026-11-13.zip (7 Werkzeugquellen, README, MANIFEST) + ARCHITEKTURVORSCHLAG.md [2]

* * *

## 1. Prüfgegenstand

**Repository (laut Auftrag SSOT):** `baem-oss/THEOBald`
| Gegenstand | Stand | Bewertung |
| --- | --- | --- |
| `main` | `6cef508cead1f2cc879d15455bfd4da704479317` | geprüft |
| `review/sourceguard-integrated-v0.5.5-dev3` | `a5338e229a781df8ebb670c392b815531b0d7c5f` | SourceGuard-Doku geprüft |
| Branch `drs-ki-test` | **existiert nicht** | **F-C4 (wesentlich)** |

**Ergänzend herangezogen:** `baem-oss/THEOAgent` `main` @ `5dc0a245958a50f0318574e3d70b4f35df144538` (formale Requirements-Baseline v1.2.0).
**Geprüfte Quellcodes:** Fast–Summary v2.1.0, Faster–No Summary v2.1.0, Websuche/Dokument v2.0.0, Outline Document Tools v0.1.0, MediaWiki MCP v1.5.0, Single Domain Web Search v2.0.1, TYPO3 Document Tools v0.3.2 (Chat-Abschrift).

* * *

## 2. Prüfgrundlagen

*   Auftrag QE [1][3].
    
*   THEOAgent **Requirements-Baseline v1.2.0** (PO-freigegeben 10.11.2026) [25], Abnahmeprofil [26], Traceability [27].
    
*   THEOBald **SourceGuard-Architektur v0.1** [17], **REQ-SG-001** [18], **CURRENT_STATUS** (10.11.2026) [19], TECHNIK_UND_RISIKEN [20].
    
*   THEOBald Skills Quellenprüfung [10] / theologische Grundlagen [14], openwebui-setup [12], modularer Kernprompt [21], Status 07.11.2026 [23], Tool-Guard [15].
    

**SSOT-Hinweis:** Der Auftrag bezeichnet `THEOBald` als SSOT für „Requirements". Die _formale, PO-freigegebene_ Requirements-Baseline v1.2.0 liegt jedoch im Repo `THEOAgent` [25]. Diese Divergenz ist als F-C3 erfasst und vor weiteren Abnahmen durch den PO zu klären.

* * *

## 3. Durchführung

Tatsächlich durchgeführt:

*   Vollständige **statische** Codelektüre aller sieben Werkzeugquellen; Prüfung je Werkzeug auf implementierte Funktionen, Quellenzugriff/Auszug/Zusammenfassung/Fundstellen, technische Grenzen und Sicherheitsverhalten.
    
*   Abgleich der Aussagen des Architekturvorschlags gegen den Quellcode.
    
*   Abruf und Lektüre der oben genannten Repository-Dokumente (GitHub API/raw).
    

**Einschränkungen (verbindlich offenzulegen):**

*   **Keine Laufzeittests**, keine Ausführung der Werkzeuge, kein Open-WebUI-v0.11.4-/DRS:KI-Zugang. Alle Aussagen zum Laufzeitverhalten sind **aus dem Code abgeleitet** oder **erst durch Praxistests prüfbar**.
    
*   Integrität des ZIP (SHA-256) **nicht unabhängig nachgerechnet** (kein Hash-Werkzeug in dieser Sitzung); MANIFEST/README sind intern konsistent.
    
*   TYPO3-Quelle ist eine **Chat-Abschrift**, keine Originaldatei; Befunde dazu sind schwächer belastbar.
    

* * *

## 4. Findings

Schweregrade gemäß Auftrag: **kritisch / wesentlich / geringfügig**.

### 4.1 Auftrag A – Codeanalyse

**F-A1 (wesentlich) – Single Domain: Redirect-SSRF trotz „Safety Policy".**  
`_fetch_page_text_and_links` ruft `self.session.get(..., allow_redirects=True)` auf und prüft die Ziel-URL erst **nach** dem Abruf (`final_url`). Damit wird die interne Adresse durch den Redirect bereits kontaktiert; zusätzlich besteht DNS-Rebinding-TOCTOU (Prüfung via `socket.getaddrinfo`, erneute Auflösung durch `requests`). Nachweis: Quellcode `sources/uploaded/07_single_domain_web_search_v2_0_1.py`. Auswirkung: Verstoß gegen **SP-03** („gefährliche Umleitungen … unterbinden"). Korrektur: Auto-Redirects deaktivieren und jeden Hop wie in Outline v0.1.0 vorab validieren, oder auf aufgelöste IP festnageln.
**F-A2 (wesentlich) – TYPO3: dokumentierte Suchfunktion nicht implementiert; kein Gesamtbudget.**  
`analyze_typo3_files(..., query="", max_files=10, max_hits_per_file=10)` akzeptiert `query` und `max_hits_per_file`, verwendet sie aber im Rumpf nicht; die Variable `budget` wird gesetzt, aber im Dateilauf nicht verbraucht. Es werden bis zu `max_files` volle Dateidumps ausgegeben. Platzhalterkommentar („Hier wird die Iteration … fortgesetzt"). Nachweis: `08_typo3_document_tools_v0_3_2_CHAT_ABSCHRIFT.py`. Auswirkung: Kontextüberflutung, irreführende Funktionsbeschreibung. Korrektur: Filter implementieren oder Parameter entfernen; globales Budget durchsetzen.
**F-A3 (wesentlich) – Rohinhalte ohne technische Neutralisierung (SP-02).**  
Faster (PAGE_EXCERPT), Single Domain (PAGE_CONTENT), Outline und MediaWiki geben extrahierten Fremdtext **roh** in den Modellkontext zurück; „untrusted" wird nur in den _Zusammenfassungs_-Prompts der Summary-Werkzeuge gesetzt. Eine technische Vorrangregel (Dokumentinhalt ≠ Anweisung) fehlt. Auswirkung: Restrisiko indirekter Prompt-Injection gegen **SP-02**. Korrektur: mindestens harte Delimiter/Kennzeichnung als Datenblock; Restrisiko dokumentieren.
**F-A4 (wesentlich) – Fundstellen-Semantik: PDF-Seite ≠ Druckseite.**  
Outline etikettiert PDF-Seiten als „Seite N" (`f"Seite {i+1}"`) und Textdateien als „Dokument"/„Text" ohne explizite PDF-Kennzeichnung. Auswirkung: Gefahr, dass das Modell PDF-Seiten als Buch-/Druckseiten zitiert → **DAT-02/GR-03**. Korrektur: Label „PDF-Seite N" und Verbot der Druckseiten-Inferenz.
**F-A5 (wesentlich) – „No Summary" gilt nur für die Websuche.**  
Faster–No Summary v2.1.0 gibt Webinhalte roh aus, fasst aber `analyze_uploaded_documents` weiterhin per Map/Reduce zusammen (max. 3600 Zeichen Ausgabe). Wer das Werkzeug als Dokument-Belegquelle nutzt, erhält Zusammenfassungen, keinen Originaltext. Korrektur: Geltungsbereich klarstellen bzw. Rohmodus für Dokumente ergänzen.
**F-A6 (wesentlich) – Keine strukturierte Fundstellen-Extraktion.**  
Kein Werkzeug extrahiert KKK-Absatznummern, Canones oder Bibelstellen als strukturierten Locator; Belege bleiben URL, PDF-Seite oder Textfenster. Die Fundstelle hängt damit am Modell → Risiko für **GR-03/DAT-02**. Korrektur: Werkzeuge um Locator-Felder erweitern (optional) bzw. Modell darf nicht gesehene Locatoren nicht ausgeben.
**F-A7 (geringfügig) – Fast/Websuche:** `check_no_credentials` **ist toter Code.**  
Definiert, aber nie aufgerufen (die Prüfung erfolgt inline). Nachweis: `01_...py`, `02_...py`, `04_...py`. Korrektur: entfernen oder verwenden.
**F-A8 (geringfügig) – Websuche/Dokument v2.0.0: veränderliches Default-Argument.**  
`analyze_uploaded_documents(..., __files__: List[dict] = [], ...)` — Anti-Pattern (keine Mutation im Code, daher geringe Wirkung). Korrektur: `None`.
**F-A9 (geringfügig) – MediaWiki: Metadaten-Inkonsistenzen.**  
Citation-Event setzt `document: [url]` (nicht den Inhalt), `clientInfo.version` = „1.4.0" bei Werkzeugversion 1.5.0, `protocolVersion` fest „2024-11-05". Korrektur: Versionen angleichen; Protokollversion konfigurierbar.
**F-A10 (geringfügig, Hinweis) – Fast/Faster/Websuche folgen keinen Redirects.**  
`allow_redirects=False` ohne manuelles Nachführen → viele Ziele liefern keinen Auszug, es greift der Snippet-Fallback. Kein Sicherheitsmangel, aber eine Belegbarkeits-/Abdeckungsgrenze.
**Positiv (Auftrag A.1/A.2):** Die im Architekturvorschlag gemachten Funktionsaussagen sind im Quellcode überwiegend **bestätigt** (siehe Abschnitt 6).

### 4.2 Auftrag B – Wiederverwendbarkeit

**F-B1 (wesentlich) – Lizenzlage ungeklärt; Codeübernahme unzulässig.**  
Keine Lizenz-/Copyright-Header in den Quellen; Autoren „BKurschatke (drsBK26)" (Outline, TYPO3) und „Fedor" (MediaWiki, Single Domain). README: „keine Rechtsfreigabe zur Veröffentlichung/Codeübernahme". Auswirkung: **Keine Codeübernahme** ohne Rechteklärung (**SP-05**; sinngemäß **RANF-03**). Zulässig bleibt die **Konzeptadaption** (eigene Neuimplementierung nach Idee).
**F-B2 (wesentlich) – Abhängigkeiten ohne Installationsrecht.**  
Die Werkzeuge benötigen `requests`, `bs4`, `pymupdf`, `python-docx`, `openpyxl`, `pypdf`, `pydantic`. Ohne Administrations-/Installationsrechte auf DRS:KI ist unklar, ob diese Werkzeuge überhaupt verfügbar sind — dann greift die gesamte Analyse nicht. Vor Implementierung zu klären (F-C8).
**Einordnung (Auftrag B):**

*   _Unveränderte Nutzung_ bestehender DRS:KI-Werkzeuge: nur nach Rechte-/Verfügbarkeitsklärung.
    
*   _Konzeptadaption_ (empfohlen, kein Codekopie): Outline (Allowlist + Redirect-Revalidierung + Größencaps + Kontextfenster-Suche), Faster (Typkennzeichnung Auszug/Snippet), Websuche (Kandidaten-Nachladen + Protokollierung), Single Domain (Domainbindung + Folgerunden — **ohne** dessen Redirect-Handling), MediaWiki (MCP-Handshake search→get), Fast/Websuche (Map/Reduce-Chunking).
    
*   _Eigene Komponente_: Der durchsetzende Prüfschritt existiert bereits als `sourceguard/sourceguard.py` v0.5.5-dev3 — **nicht neu bauen**, sondern Wiederverwendung prüfen.
    

### 4.3 Auftrag C – Architekturvorschlag

**F-C1 (kritisch) – Prompt-gesteuerter „SourceGuard-Prüfschritt" erfüllt die verbindliche Quellenprüfung nicht.**  
Der Vorschlag ersetzt die im Repo dokumentierte **technisch durchgesetzte** Quellenpflicht (SourceGuard-Pipe, „90-%-Pragmatik … nicht zulässig" [17]; REQ-SG-001 [18]) durch eine **promptgesteuerte Klassifikation**. Genau dieser Ansatz ist laut REQ-SG-001 das **Ausgangsproblem** („Modellprompts und Skills allein garantieren keine Originallektüre") und scheiterte in QP01/QP03 [23]. Damit sind **NFANF-13** (null falsch als geprüft ausgegebene Belege) und **GR-02** nicht erreichbar. Unter der Randbedingung „keine Adminrechte" (keine Pipe-/Function-Installation) ist die geforderte Verifikation derzeit **nicht realisierbar**. Korrektur: entweder Rechte für den durchsetzenden Prüfschritt beschaffen **oder** die Ausgabekategorie „ORIGINALTEXT_GEPRUEFT/verifiziert" technisch sperren und nur „Treffer/Auszug" zulassen.
**F-C2 (wesentlich) – Werkzeugvertrag passt nicht zum SourceGuard.**  
SourceGuard erwartet die nativen Werkzeuge `search_knowledge_files`, `grep_knowledge_files`, `view_knowledge_file`, `search_web`, `fetch_url` [17][18]. Die DRS:KI-Werkzeuge sind **eigene** Tools mit anderem Namen/Rückgabeformat. Ob SourceGuard auf DRS:KI diese Callables überhaupt erhält, ist **unbewiesen** und muss im P0-Probe-Pipe geklärt werden.
**F-C3 (wesentlich) – Widersprüchliche SSOT-Vorgaben; Requirements-Ablage unklar.**  
(a) `STATUS_2026-11-07.md` verwirft „Filter/Quellenrouter" und akzeptiert eine „pragmatische 90-%-Lösung" [23]; `SOURCEGUARD_ARCHITEKTUR_V0_1.md` und `CURRENT_STATUS.md` (10.11.) fordern technische Durchsetzung per Pipe [17][19]. (b) Der Auftrag nennt THEOBald als Requirements-SSOT, die freigegebene Baseline v1.2.0 liegt aber in THEOAgent [25]. Beide Punkte sind vor Abnahmen durch den PO zu entscheiden.
**F-C4 (wesentlich) – Branch** `drs-ki-test` **existiert nicht.**  
Weder als Prüfbasis noch als vorgesehener Ablageort vorhanden. Der Auftrag ist insoweit nicht erfüllbar wie beschrieben.
**F-C5 (wesentlich) – SP-03 im Zielbild verletzt.**  
Die Empfehlung, Single Domain für die Bibelrecherche einzusetzen, importiert die Redirect-Schwäche (F-A1) in den Belegpfad. Single Domain ist für Belegzwecke auszuschließen oder erst nach Fix zu verwenden.
**F-C6 (wesentlich) – Rechte-/Datenfluss-Gate (SP-01/SP-05/DAT-01, T-06) für DRS:KI fehlt.**  
Bibeltext über bibleserver.com und externe Modellprovider: Nutzungsrechte, Fassung (Einheitsübersetzung 2016?) und Provider-Datenfluss sind ungeklärt. Der Vorschlag benennt das Risiko, führt aber kein Gate.
**F-C7 (wesentlich) – Realismus „ohne Adminrechte" ungelöst.**  
Ungeklärt: Zuweisung von Tools, Modell-/Assistenzkonfiguration, Knowledge-/Skill-Rechte, Funktionsfähigkeit der Modelle mit Tool Calls. Der Vorschlag listet dies als P0, löst es aber nicht; dies ist der Kern der Machbarkeitsfrage.
**F-C8 (geringfügig) – Redundanz.**  
Fast–Summary und Websuche/Dokument liefern beide nur LLM-Synthesen; ein paralleler Einsatz ist redundant. Der Vorschlag behandelt das weitgehend korrekt (Fast nur für Überblicksfragen).

### 4.4 Übergreifend

**F-X1 (wesentlich) – Keine unabhängige Integritätsprüfung des Pakets möglich.**  
SHA-256-Werte im MANIFEST konnten in dieser Sitzung nicht nachgerechnet werden. Die im MANIFEST dokumentierte Byte-Identität der beiden Faster-Uploads ist plausibel, aber nicht nachgerechnet.

* * *

## 5. Positive Befunde (bestätigt)

*   Die **Funktions- und Grenzbeschreibungen** des Architekturvorschlags treffen den Quellcode überwiegend korrekt: Faster (4500 Zeichen, Snippet-Fallback), Single Domain (Domainbindung, 3 Runden, Suffizienz-LLM), Outline (Originaltext, PDF-Seiten, Host-Allowlist), MediaWiki (Originalauszug ≤ 12000), TYPO3 (Parameter ignoriert, kein Gesamtbudget), Websuche/Dokument (nur LLM-Synthese), Fast (nur Zusammenfassung).
    
*   Der Vorschlag ist **selbstkritisch**: Er benennt Redirect-, SSRF-, Budget-, Lizenz- und Rechte-Risiken ausdrücklich und täuscht keine Quellensicherheit vor.
    
*   Outline v0.1.0 setzt SSRF-Minderung **sauber** um: HTTPS-Zwang, kein Credential/Port, `is_global`-Prüfung, manuelle Redirect-Revalidierung, Größenlimits (fail-closed bei leerer Allowlist).
    
*   Die KISS-Ausrichtung („kein Fork, kein sofortiger Neubau") deckt sich mit den Projektregeln [12][21].
    

* * *

## 6. Requirements-Abgleich (Auftrag D)

Grundlage: Requirements-Baseline v1.2.0 [25]. Bewertung nur soweit ohne Laufzeit prüfbar; „erfüllt" = durch die vorgeschlagene Architektur strukturell abgedeckt.
| Anforderung | Bewertung | Begründung |
| --- | --- | --- |
| FANF-01 (natürliche Sprache) | **erfüllt** | Prompt/Assistent |
| FANF-02/03 (Bibliothek/Web durchsuchen) | **teilweise** | Werkzeuge vorhanden; Bibliothek/Web-Auslösung unzuverlässig [23] |
| FANF-04/05 (gezielte Suche, Originallektüre) | **teilweise** | nur promptgesteuert, nicht erzwungen (F-C1) |
| FANF-06 (Weiterrecherche) | **erfüllt (strukturell)** | Single Domain, Folgerunden |
| FANF-07/08 (Fundstelle + Übereinstimmungsprüfung) | **teilweise** | keine technische Fundstellen-/Übereinstimmungsprüfung (F-A6) |
| FANF-09 (Kennzeichnung Unzugänglichkeit) | **teilweise** | im Prompt vorgesehen |
| FANF-32 (autonome Steuerung) | **teilweise** | modellabhängig |
| FANF-33 / RANF-06 (Dokumente) | **teilweise** | Formate ja; OCR nein; Roh- vs. Zusammenfassung beachten (F-A5) |
| GR-01/02 (Originallektüre, kein Treffer/TOC als Beleg) | **nicht erfüllt (technisch)** | nur promptgesteuert (F-C1) |
| GR-03 (exakte Nachweise) | **teilweise** | keine Locator-Extraktion (F-A6) |
| GR-16/18 (Unsicherheit/Teilergebnisse) | **teilweise** | im Prompt vorgesehen |
| **NFANF-13 (Belegintegrität = 0 Fehler)** | **nicht erfüllt** | promptgesteuert nicht garantierbar (F-C1) |
| NFANF-12 (Freeze) | **nicht überprüfbar** | nicht Gegenstand der Werkzeuganalyse |
| **SP-02** (keine Dokumentanweisungen ausführen) | **nicht erfüllt (technisch)** | F-A3 |
| **SP-03** (sichere Webziele) | **nicht erfüllt** | F-A1/F-C5 |
| SP-01/SP-05/DAT-01 (Rechte/Datenfluss) | **nicht überprüfbar** | Gate fehlt (F-C6) |
| DAT-02 (Fundstelle ≠ PDF-Seite/Buchseite) | **teilweise** | F-A4 |
| RANF-01/02 (Open WebUI, kein Eingriff) | **erfüllt (strukturell)** | Pilot |
| NFANF-01…11 | **nicht überprüfbar** | Grenzwerte/Korpora offen (F-01) [26] |

_Keine neuen Anforderungen erfunden._ Als **Vorschlag** (nicht Baseline): ein explizites Ausgabegate „ORIGINALTEXT_GEPRUEFT nur bei technischem Lese-Nachweis" wäre die minimale Ergänzung zu GR-02/NFANF-13.

* * *

## 7. Offene Prüfpunkte (für die DRS:KI-Praxistests)

1.  Welche Werkzeuge sind dem persönlichen Account **tatsächlich** zugewiesen und aufrufbar?
    
2.  Dürfen ein eigener Assistent/Systemprompt, Knowledge und Skills **ohne Adminrechte** angelegt/konfiguriert werden?
    
3.  Ist eine **Pipe/Function** (SourceGuard) installierbar — oder ist technische Durchsetzung auf DRS:KI ausgeschlossen?
    
4.  Erhält eine Pipe über `__tools__` die nötigen Callables, und **welche Namen/Rückgabeformate** haben die DRS:KI-Werkzeuge?
    
5.  Ist die Outline-Host-Allowlist und der TYPO3-MCP-Zugriff eingerichtet?
    
6.  Unterstützen die installierten Modelle zuverlässig Tool Calls?
    
7.  Redirect-Verhalten von Single Domain real (F-A1) — kontrollierter Test.
    
8.  Rechte-/Fassungsprüfung für bibleserver.com/Einheitsübersetzung 2016.
    
9.  Verhalten der Werkzeuge an Zeichenlimits (Abschneidung) — keine Negativbeweise.
    
10.  Prompt-Injection-Test mit präparierter Seite/Dokument (SP-02).
     

* * *

## 8. Architekturentscheidung / Abnahmefrage

**Empfohlene minimale Architektur (Abweichungen vom Vorschlag begründet):**

1.  **Recherche:** vorhandene DRS:KI-Werkzeuge **unverändert** nutzen, aber ausschließlich als **Treffer-/Auszugsquellen**: Outline (Dokumente, Originaltext mit PDF-Seiten-Kennzeichnung), MediaWiki (Wiki-Auszug), Faster–No Summary (offene Web-Auszüge), Single Domain (Bibel) — **nur nach Fix/Ersatz** wegen F-A1/F-C5.
    
2.  **Keine** Nutzung von Fast–Summary/Websuche/Dokument als Belegquelle (nur LLM-Synthese) — nur für Überblick.
    
3.  **Abweichung 1:** Der durchsetzende Prüfschritt darf **nicht** durch eine promptgesteuerte Klassifikation ersetzt werden (F-C1). Entweder die Rechte für den bestehenden SourceGuard (v0.5.5-dev3) beschaffen **oder** die Ausgabekategorie „geprüft/verifiziert" technisch unterbinden.
    
4.  **Abweichung 2:** Ausgabe strikt in Evidenzstufen **Treffer / gelesener Auszug / technisch nachgewiesener Originaltext** trennen; letztere nur bei vorliegendem Lese-Nachweis.
    
5.  **Abweichung 3:** Vor jeder externen Verarbeitung privater Texte ein Rechte-/Datenfluss-Gate (SP-01/SP-05, T-06).
    
6.  **Abweichung 4:** Keine Übernahme fremden Quellcodes (F-B1); nur Konzeptadaption.
    

**Antwort auf die Abnahmefrage:** Eine _minimal fachlich belastbare_ Architektur ist auf DRS:KI **nur** erreichbar, wenn (a) die technische Quellen-Durchsetzung installierbar ist **oder** (b) THEOBald ausdrücklich **ohne** Verifikationsanspruch betrieben und die Ausgabe auf „Treffer/Auszug" begrenzt wird. Ein „fachlich zuverlässiger, quellengeprüfter Betrieb" mit NFANF-13/GR-02 ist in der vorgeschlagenen promptgesteuerten Form **nicht** belegt.

* * *

## 9. Gesamturteil

**Freigabefähig mit Auflagen — ausschließlich für einen ausdrücklich als unverbindlich deklarierten Erkundungs-Pilot.**
Ausdrücklicher Vorbehalt: Ein **produktiver, quellengeprüfter Betrieb** ist in der vorliegenden Form **nicht freigabefähig** (F-C1, NFANF-13, GR-02, SP-03).
**Auflagen vor Start:**

1.  P0-Rechteprüfung abschließen (F-C7) — inkl. Klärung, ob eine Pipe/Function installierbar ist.
    
2.  Ausgabe-Kategorie „geprüft/verifiziert" sperren, solange keine technische Lese-Prüfung existiert (F-C1).
    
3.  Single Domain für Belegzwecke ausschließen oder Redirect-Schwäche beheben (F-A1/F-C5).
    
4.  Rechte-/Datenfluss-Gate für bibleserver.com und externe Provider (F-C6).
    
5.  Kein fremder Quellcode ins Repository; nur Konzeptadaption (F-B1).
    
6.  PO-Entscheidung zu den widersprüchlichen SSOT-Vorgaben und zur Requirements-Ablage (F-C3).
    

**Restrisiken / nicht verifiziert:** sämtliche Laufzeiteigenschaften, Paket-Integrität, tatsächliche Rechte- und Tool-Verfügbarkeit (F-X1, Abschnitt 3).
**Ablagehinweis:** Der Auftrag sieht die Ablage im Branch `drs-ki-test` vor; dieser existiert nicht (F-C4). Der Bericht wird daher entsprechend der QE-Ablageregelung als Open-WebUI-Notiz geführt; **kein** Repository-Commit durch den QE.