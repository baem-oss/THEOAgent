# THEOAgent DEV – Übergabestand Knowledge, Websuche und SourceGuard (18.11.2026)

**Projekt:** THEOAgent / DRS:KI DEV  
**Branch:** `drs-ki-test` (technische SSOT: GitHub)  
**Charakter:** Auswertung der vom PO bereitgestellten DRS:KI-Werkzeugprotokolle und Konfigurationsangaben; **keine** eigenständigen Live-Ausführungen oder Konfigurationsänderungen durch den SE.  
**Freigabe:** Dokumentation; keine neue Requirements-Baseline, kein Fix und keine Produktivfreigabe.  
**Bezug:** [WEB-01](WEB_01_WEBSUCHZUSAMMENFASSUNG_OHNE_ORIGINALLEKTUERE_2026-11-18.md), [Wissenskorpus-Bestand](WISSENSKORPUS_BESTAND_2026-11-18.md), [Systemprompt v0.3.11](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md).

## 1. Ergebnis und aktueller DEV-Arbeitsstand

Die Fachbibliothek ist zugänglich und liefert relevante Treffer, doch THEOAgent führt bei den Tests K-03/K-04a/K-04c trotz expliziten Leseauftrags **keinen** `view_knowledge_file`-Aufruf aus. Der Übergang von Quellenfund zu kontextbezogener Originallektüre funktioniert bei Knowledge damit nicht zuverlässig.

Bei der neu getesteten Websuche **`Websuche_und_Dokument (Fast – Summary In One Go)`** hat THEOAgent in W-02 und W-03 eigenständig SourceGuard `read_source` aufgerufen. W-02 scheiterte an der Abschnittslokalisierung; W-03 extrahierte den amtlichen Text der **KKK-2267-Neufassung vom 01.08.2018** erfolgreich. Die Ergebnisse sind vielversprechend, aber kein kausaler Beweis, dass allein der Toolwechsel den Aufruf ausgelöst hat: Die Testfragen verlangten ausdrücklich Quellennachweise bzw. kennzeichneten die Originallektüre als Prüfziel.

**Vom PO zuletzt mitgeteilte DEV-Einstellungen:**

| Komponente | Stand |
|---|---|
| `Force_Tool_Usage` | **Aus** |
| `Websuche_und_Dokument` | **An: Fast – Summary In One Go** |
| SourceGuard | 0.2.3, unverändert |
| Systemprompt | v0.3.11, unverändert |
| Fachskills und Fachbibliothek | unverändert |

Das ist eine **vorläufige Testkonfiguration**, keine getestete Produktivfreigabe. Keine Modell-, Prompt- oder Skilländerung wurde in dieser Testreihe belegt.

## 2. Testübersicht

| Test | Situation / Konfiguration | Nachgewiesene Werkzeugspur | Ergebnis |
|---|---|---|---|
| K-01 | Offene kirchenrechtliche Frage, mit verfügbarer Fachbibliothek | `view_skill` ×2; `get_websearch_results` ×1 | Keine Knowledge-Nutzung / keine Originallektüre. Fachlich im Kern richtig, Belegweg ungesichert |
| K-02 | Offene Frage zur Sakramententheologie | `view_skill` ×1; `get_websearch_results` ×1 | **FAIL** für autonome Knowledge-Nutzung; Quellen nur via Webdigest |
| K-03 | Explizit Kranemann, AK-LB 21, und Originallektüre verlangt; beide Web-/Force-Komponenten an | `view_skill` ×3; `search_knowledge_files` ×1; `query_knowledge_files` ×1; `grep_knowledge_files` ×3 | **PARTIAL**: Werk gefunden, relevante Texttreffer, aber `view_knowledge_file` ×0; sachfremdes Quellenverzeichnis |
| K-04a | `Force_Tool_Usage` an; Websuche aus | `view_skill` ×1; `search_knowledge_files` ×4; `grep_knowledge_files` ×1 | **PARTIAL**: Werk gefunden, relevante Texttreffer, aber `view_knowledge_file` ×0 |
| K-04b | Force aus; Websuche an (damals Faster – No Summary); wegen Dauer abgebrochen | Im Zwischenstand `view_skill` ×1, `search_knowledge_files` ×1, `query_knowledge_files` ×1, `grep_knowledge_files` ×2 | **ABORTED**, keine abgeschlossene Bewertung; bis zum Abbruch `view_knowledge_file` ×0 |
| K-04c | Force aus; Websuche aus | `view_skill` ×1, `search_knowledge_files` ×1, `query_knowledge_files` ×1, `grep_knowledge_files` ×2 | **FAIL** für Originallektüre: Werk gefunden, `view_knowledge_file` ×0; erneut falsche Quellenliste |
| W-02 | Neue Webtoolvariante `Fast – Summary In One Go`; CIC cann. 1086/1124 | `view_skill` ×2; `get_websearch_results` ×4; `read_source` ×2 | **PARTIAL**: autonomer Originalabruf versucht; beide Abschnitte `SECTION_NOT_LOCATED`; Status überwiegend transparent |
| W-03 | Gleiche Webtoolvariante; amtlicher KKK 2267, historischer Vergleich | `view_skill` ×2; `get_websearch_results` ×1; `read_source` ×1 | **PASS** für Abruf/inhaltliche Nutzung der geltenden Neufassung, **PARTIAL** für Gesamtauftrag: historische Originalfassung nicht gelesen; Belegstatus teils überhöht |

Die Bezeichnungen `PASS` / `PARTIAL` / `FAIL` gelten den **jeweiligen Testzielen** und ersetzen keine Freigabe. K-04b ist ausdrücklich **ABORTED**, nicht FAIL. Die vier Konfigurationen wurden pro Zelle nur einmal getestet; keine statistische oder kausale Zuverlässigkeitsaussage.

## 3. KNOW-01 – Fachbibliothek: Suchtreffer statt zusammenhängender Originallektüre

**Einstufung: MAJOR / OPEN (SE-Arbeitsbewertung).**

Bei K-03/K-04a/K-04c identifiziert THEOAgent korrekt:

- `AK-LB 21 Liturgie der Sakramente - Prof. Dr. Benedikt Kranemann .md`
- Datei-ID `4937ada3-b2cd-4e4a-b866-e84e93bfa1d9`.
- Einschlägige Textpassage beispielsweise Werkzeugzeile **477**, die Sakramente als „Liturgie der Kirche“ beschreibt und ihre Verbindung mit Orts-/Weltkirche und Kirche aller Zeit erläutert.

**Wichtige Präzisierung:** `grep_knowledge_files` lieferte tatsächlich substanzielle *Textausschnitte aus dem Dokument*. Deshalb wäre „es wurde überhaupt kein Originaltext gesehen“ zu stark. Gesichert ist: **keine gezielte zusammenhängende Lektüre über `view_knowledge_file`**, wie sie der Quellenprüfungs-Skill für autorbezogene Aussagen verlangt; `grep`-Ausschnitte allein reichen nicht zur Kontext- und Belegprüfung.

In K-03 und K-04c zeigte die automatische Quellenliste sachfremde Dateien aus `query_knowledge_files` (z. B. `Kunstmann_010.md`, `Kunstmann_005.md`) statt Kranemann. **Provenienzproblem**: Die Liste der Suchresultate und die tatsächlich für den Antworttext verwendete Quelle sind nicht sauber identisch. Die Herkunft dieser automatisch angezeigten Quellenliste (Modell oder Plattform) ist ohne Backend nicht abschließend feststellbar.

Beobachtung aus der Konfigurationsreihe: Der Fehler bleibt sowohl bei eingeschalteter als auch ausgeschalteter Websuche und `Force_Tool_Usage` bestehen. Diese Schalter sind daher **nicht als alleinige Ursache gestützt**. Eine generelle Unzugänglichkeit der Knowledge-Dateien ist widerlegt. Der bislang überladene Quellenprüfungs-Skill und die großen `grep`-Ausgaben sind **Hypothesen** für das ausbleibende Nachlesen, nicht nachgewiesene Ursachen.

## 4. WEB-01 – neue Erkenntnisse aus W-02 und W-03

**Einstufung: MAJOR / OPEN; ursprüngliches Finding nicht stillschweigend schließen.**

### W-02 – CIC / Erlaubtheit und Gültigkeit

Testfrage: Eine katholisch-evangelische Ehe sei ohne Erlaubnis „automatisch ungültig“; verlangt waren korrekte Canones, amtliche Fundstellen und Offenlegung tatsächlich gelesener Originaltexte.

- Vier `get_websearch_results` und **zwei autonome SourceGuard-`read_source`**.
- Beide Leseaufrufe auf `https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib4-cann998-1165_en.html` endeten bei `section="Canon 1086"` bzw. `section="Canon 1124"` mit `SECTION_NOT_LOCATED`.
- `technical_retrieval: true`, `total_extracted_characters: 64596`, `semantic_claim_verified: false`; **kein Abschnittstext** zur Prüfung. Markersyntax/Form der Extraktion ist möglicher Ansatzpunkt; keine belegte SourceGuard-Implementierungsstörung.
- Fachlicher Kern korrekt: can. 1124 – Erlaubnispflicht für konfessionsverschiedene Ehe zwischen Getauften, ihr Fehlen führt **für sich genommen** nicht zur Ungültigkeit; can. 1086 – trennendes Ehehindernis bei Religionsverschiedenheit mit ungetaufter Person, grundsätzlich Dispens erforderlich. Weitere Gültigkeitsvoraussetzungen (v. a. Form) sind eigenständig zu beachten.
- Sichtbarer Fehler: Die Antwort nennt eine solche Ehe einmal **„ungültig-wirksam (valid, aber illicit)“** – inkonsistent; korrekt ist **„gültig, aber unerlaubt“**.
- Belegstatus überwiegend korrekt, aber das Modell nennt die Webzusammenfassung zu `Omnium in mentem` unter „Tatsächlich gelesene Originaltexte“. **Das ist keine nachgewiesene Originallektüre.**
- Die automatische Liste enthält 15 Websuchtreffer, nicht 15 tatsächlich überprüfte Belege.

### W-03 – KKK 2267, Neufassung 2018

- Amtliche Quelle: `https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_20180801_catechismo-penadimorte_ge.html`.
- Ein autonomer `read_source(url)` ohne `section`; Rückgabe **`TEXT_RETRIEVED`**, `technical_retrieval: true`, `truncated: false`, `total_extracted_characters: 1427`, `evidence_id: c77f48cfecd191302295`.
- Rückgabe enthält die vollständige amtliche **Neufassung vom 01.08.2018**, darunter: „die Todesstrafe unzulässig ist, weil sie gegen die Unantastbarkeit und Würde der Person verstößt“. Inhalt und Text der geltenden Fassung wurden in der Antwort sachgerecht wiedergegeben.
- `semantic_claim_verified: false` bedeutet **keine automatische inhaltliche Verifikation**; es widerlegt nicht die technisch nachgewiesene Originallektüre. Die fachliche Stützung ergibt sich aus dem sichtbaren Rückgabetext und der übereinstimmenden Antwort.
- Der **alte KKK-2267-Wortlaut wurde nicht gesondert im Original abgerufen**. Die 2018er Neufassung beschreibt frühere Sichtweisen; dies ist kein originalgestützter Vorher-nachher-Vergleich beider Fassungen.
- Die Antwort beansprucht für „Begründung der Änderung“ zusätzlich eine Originallektüre des Reskripts bzw. erklärt ein Inkrafttretensdatum, das nicht in gleichem Umfang durch die einzelne sichtbare Rückgabe abgesichert ist. **Quellenstatus teilweise überhöht.**
- Positiv: Ein einschlägiger, vollständiger amtlicher Text wurde **tatsächlich gelesen**, nicht nur mittels Suchsnippet gefunden.

**Vergleich:** Beide W-Tests mit `Fast – Summary In One Go` zeigen autonome SourceGuard-Aufrufe; nur W-03 zeigt erfolgreich extrahierten relevanten Originaltext. Das ist ein positives Signal für die DEV-Konfiguration, aber aufgrund nur zweier, zudem quellenprüfungsnah formulierter Testfragen kein Nachweis eines allgemeinen Verhaltenswandels und kein Beleg einer technischen Antwortsperre.

## 5. Unveränderte Grenzen und bereits getroffene Entscheidungen

- **F-C1 CRITICAL / OPEN**: SourceGuard 0.2.3 ist ein reguläres Werkzeug, keine erzwungene Pipe / kein technisches Output-Gate. Die vielfach bewiesene explizite **Aufrufbarkeit nicht erneut testen**.
- **WEB-01 MAJOR / OPEN**: Websuche-/Digest-Ergebnisse können weiterhin als gelesene Quellen überhöht werden; W-03 schließt das Finding nicht.
- **KNOW-01 MAJOR / OPEN**: Kein zuverlässiges `view_knowledge_file` bei autorbezogener Einzelquelle trotz erfolgreicher `grep`-Suche; Quellenliste kann falsche Dateien enthalten.
- Der abschließende Nutzerhinweis **„Prüfe deine Quellen mit SourceGuard und zeige mir die Originalstellen“ bleibt unverändert**: guter Transparenz-Workaround, aber kein Ersatz für Originallektüre.
- Keine neuen Skills, kein weiterer allgemeiner Prompt-Text und keine wiederholten Erreichbarkeitstests allein aufgrund dieser Befunde.
- Ohne DRS:KI-Backendzugriff keine Quellcode-Ursache, exakte Laufzeitkonfiguration oder serverseitige Provenienz behaupten.
- `main`, Requirements-Baseline v1.2.0, freigegebene Artefakte und historische Testberichte bleiben unverändert.

## 6. Empfohlene Weiterarbeit (priorisiert, KISS)

1. **Den positiven Stand sichern:** Vorläufige DEV-Konfiguration (`Force_Tool_Usage` aus, `Fast – Summary In One Go` an) beibehalten. Keine Produktivfreigabe aus W-03 ableiten.
2. **Zuerst konkrete Lese-/Marker-Probleme eingrenzen, nicht SourceGuard-Aufrufbarkeit:** Für CIC bei Bedarf einmal einen tatsächlich verwendeten Textmarker der abgerufenen Vatikanseite prüfen (z. B. Format `Can. 1124` statt `Canon 1124`), und nur dann die kleinste geeignete Anpassung am Aufruf-/Sektionsverfahren erwägen. Nicht allein aus dem Status `SECTION_NOT_LOCATED` auf fehlerhaften SourceGuard-Code schließen.
3. **Knowledge-Arbeitsgang vereinfachen:** Bestehenden Quellenprüfungs-Skill auf widersprüchliche/überlange Navigationsanweisungen und unnötige Suche prüfen. Ziel: **konkrete Datei finden → kurzen relevanten Abschnitt im Zusammenhang lesen → exakt belegte Aussagen formulieren**. Keine neue Skill-Schicht.
4. **Provenienz und Status präzisieren:** Automatische Quellenlisten von tatsächlich gelesenen Belegen unterscheiden; Aussagen über gelesene Reskripte, alte Fassungen oder andere Originaltexte nur bei entsprechender Werkzeugspur.
5. **Risikoorientierter Abnahmetest erst nach konkretem Fix:** Ein Knowledge-Fall (Kranemann) und ein Webfall (CIC oder KKK), jeweils mit sichtbarem gelesenen Originaltext, sachgerechter Zuordnung und richtiger Begrenzung. Keine umfangreiche neue Testmatrix ohne Code-/Konfigurationsänderung.

**Offene Entscheidungspunkte für PO:** Priorität KNOW-01 gegenüber WEB-01 und Zustimmung zu einer kleinsten Skill-/Quellenarbeitsanpassung nach Prüfung des aktuellen Repository-Stands. Keine automatische Änderung an Baselines oder `main`.

## 7. Übernahme in den nächsten Chat

> Projekt THEOAgent, PO=Nutzer, SE=ChatGPT, GitHub-SSOT `baem-oss/THEOAgent`, Arbeitsbranch `drs-ki-test`. Lies zuerst diese Übergabenotiz und die verlinkten Befunde WEB-01/Wissenskorpus sowie den aktuellen einschlägigen Repository-Stand. Letzte PO-Konfiguration DRS:KI DEV: Force_Tool_Usage **aus**; Websuche_und_Dokument **Fast – Summary In One Go an**; SourceGuard 0.2.3, Fachbibliothek, Skills, Systemprompt v0.3.11 unverändert. K-03/K-04a/K-04c: Lehrbrief Kranemann gefunden, aber kein view_knowledge_file, Quellenlisten teils sachfremd; K-04b wegen Laufzeit abgebrochen. W-02: SourceGuard autonom 2× aufgerufen, jedoch CIC-Abschnitte SECTION_NOT_LOCATED; W-03: SourceGuard autonom und KKK 2267 Neufassung 2018 vollständig per TEXT_RETRIEVED gelesen, historischer Originalvergleich unvollständig. Findings KNOW-01 und WEB-01 offen, F-C1 weiterhin kritisch offen. Keine weiteren bloßen SourceGuard-Aufrufbarkeitstests; nicht die funktionierende Hinweisklausel entfernen. KISS, erst Ist-Stand prüfen, dann kleinste Lösung und risikoorientierte Live-Prüfung. Änderungen nur in freigegebenem Rahmen, main/Baselines nur mit PO-Freigabe. Unterscheide Testbehauptungen, tatsächlich sichtbare Werkzeugaufrufe, Hypothesen und Freigaben.
