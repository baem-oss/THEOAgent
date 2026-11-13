# Schnittstellenprüfung AK-02 – QE-Finding F-C2

**Stand:** 13.11.2026  
**Branch:** `drs-ki-test`  
**Status:** Statischer Kompatibilitätsbefund, keine DRS:KI-Laufzeitprüfung, keine Implementierung  
**Review:** [QE-F-C2](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md)  
**Referenz:** [THEOBald SourceGuard v0.5.5-dev3](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/sourceguard/sourceguard.py)

## 1. SourceGuard-Vertrag

`sourceguard/sourceguard.py` erwartet via `pipe(..., __tools__=...)` ein Dictionary aus Einträgen `{werkzeugname: {"callable": aufrufbare_funktion, ...}}`. `tool_call` weist fehlende oder nicht aufrufbare Werkzeuge zurück. In der Legacy-Pipe und im eingebetteten Agenten sind folgende Namen relevant:

| Toolname | Erwartete Funktion / Parameter | Rolle |
|---|---|---|
| `list_knowledge` | Bibliotheksinventar und Dateikennungen | Bestandsabgleich, keine Originallektüre |
| `query_knowledge_files` | `query`, `count` (Legacy); Agent optional | Semantische Suchanker, keine Originallektüre |
| `grep_knowledge_files` | `pattern`, `file_id` optional, `case_insensitive`, `count_only` | Fundstellensuche, keine Originallektüre |
| `view_knowledge_file` | `file_id`, `start_line`, `end_line`, optional `anchor_line`, `topic`, `work` | **Originallektüre / Zeilennachweis** |
| `search_web` | `query` | Quellenentdeckung, keine Originallektüre |
| `fetch_url` | `url`, im Agenten optional `topic`, `work` | **Originallektüre von Webtext** |

Die tatsächliche Verfügbarkeit und das Rückgabeformat sind nicht durch die Toolnamen allein belegt. Insbesondere setzt die Prüfung eine strukturierte Leseevidenz aus originalem, ausreichend vollständigem Text voraus; im Agenten existieren zusätzliche Argument- und Provenienzprüfungen. Das technische Gate prüft Zitier-/Nachweisstruktur, **keine semantische Vollprüfung**.

## 2. DRS:KI-Kandidaten – vorläufige Adaptermatrix

| DRS:KI-Tool | Bekannte öffentliche Funktion(en) | Mögliche Zuordnung | Befund |
|---|---|---|---|
| Faster–No Summary v2.1.0 | `get_websearch_results(query)`; `analyze_uploaded_documents(query,__files__)` | `search_web` **nur mit Parser** | Gibt URLs sowie max. 4.500 Zeichen Webseiten-Auszug/Snippet aus; kein beliebiges `fetch_url(url)`, Dokumentmodus zusammengefasst |
| Fast–Summary v2.1.0 | `get_websearch_results(query)` | Allenfalls `search_web` | LLM-Zusammenfassung kein Lektürenachweis |
| Websuche/Dokument v2.0.0 | `get_websearch_results(query)` | Allenfalls `search_web` | LLM-Synthese kein Lektürenachweis |
| Single Domain v2.0.1 | `get_websearch_results(query)` | Eingeschränkte `search_web`-Spezialquelle | Auf `bibleserver.com` voreingestellt, keine beliebige URL-Lektüre; automatische Redirects (QE F-A1) |
| Outline v0.1.0 | `analyze_document(url,question)`, `search_document(url,query,max_hits)`, `document_info(url)`, weitere | Teilweise `fetch_url`-ähnliche Dokumentlektüre | Nur erlaubte Downloadhosts; PDF-Seiten ≠ SourceGuard-Zeilenanker; Ausgabe prosebasiert |
| TYPO3 v0.3.2 | `analyze_typo3_files(records_json,...)` | Spezifischer Dokumentadapter | Vorgeschalteter MCP-Aufruf, JSON-Dateiliste, keine generische Such-/Lese-API; Chat-Abschrift |
| MediaWiki v1.5.0 | `search_mediawiki(query1,query2,query3)` | Such- plus Wiki-Leseadapter | Ergebnisse mit Originalauszug (bis 12.000 Zeichen), aber Suche und Lektüre gekoppelt, keine beliebige Seiten-/Zeilen-Leseoperation |
| DRS:KI-native Knowledge-Werkzeuge | Nicht im gelieferten Quellcode dokumentiert | Mögliches `list/grep/view/query` | **Nicht überprüft** |

**Schlussfolgerung:** Die vorhandenen DRS:KI-Custom-Tools erfüllen den bestehenden SourceGuard-Vertrag **nach statischer Codelektüre nicht direkt**. Ein bloßes Umbenennen von Funktionen und Parametern genügt nicht. Ob auf DRS:KI zusätzlich native, kompatible Knowledge- bzw. Web-Funktionen existieren, ist unbekannt.

## 3. Gefährliche Scheinadapter

**Nicht zulässig:** `fetch_url(url)` als wiederholte thematische SearXNG-Suche nach URL simulieren; ein Treffer ist kein Abruf der verlangten Originalquelle.

**Nicht zulässig:** Dokument-Zusammenfassungen aus `analyze_uploaded_documents` als `view_knowledge_file` deklarieren.

**Nicht zulässig:** Textfenster mit PDF-Seitennummern als SourceGuard-Zeilennummern ausgeben, wenn keine stabile zeilenbezogene Provenienz besteht.

**Nicht zulässig:** Gelesen-Status allein aus der Existenz von URL, Titel, Citation-Event oder vom Modell behauptetem `sufficient` ableiten.

## 4. Minimaler Weg ohne neue Implementierung

1. Prüfen, ob ein normaler DRS:KI-Account eine SourceGuard-Pipe installieren/ausführen darf (**P0 SG-01**).
2. In der realen Open-WebUI-Umgebung protokollieren, welche `__tools__`-Namen, Aufrufparameter und Antwortformen der Pipe zur Verfügung stünden (**P0 SG-02**). Keine sensiblen Inhalte oder Zugangsdaten in Protokolle aufnehmen.
3. Pro Leseweg einen kontrollierten Originaltext-Test (kurzer verifizierbarer Absatz, gezielt falscher Locator, fehlgeschlagener Abruf) durchführen.
4. Falls Werkzeuge/Callables fehlen: **Erkundungsmodus** mit transparenter Unsicherheit, **kein verifizierender SourceGuard-Betrieb**.
5. Erst bei tatsächlicher Erreichbarkeit der Pipe und der Lesewege entscheiden, ob ein kleiner Adapter möglich ist. Abgleich mit SourceGuard-Tests und Security-Requirements ist zwingend.

## 5. Disposition

**F-C2: akzeptiert, statisch belegt, technisch offen.** Der Befund wird mit dieser Schnittstellenmatrix konkretisiert, **nicht geschlossen**. Keine Änderung an Requirements, Produktionskonfiguration oder bestehender SourceGuard-Implementierung. Keine Veröffentlichung fremder Werkzeugquellcodes.

## 6. Nächster Test

`SG-01`: In DRS:KI mit dem persönlichen normalen Konto klären, ob unter Workspace / Funktionen oder ähnlicher Benutzeroberfläche eine **eigene Pipe/Function** erstellt bzw. aktiviert werden darf. Nur Oberflächen- und Rechtebeleg erfassen; nichts installieren.
