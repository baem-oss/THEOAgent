# THEOAgent DEV – SourceGuard v0.2.0 Arbeitsprofil (Erprobungsprototyp)

**Stand:** 14.11.2026 · **Branch:** `drs-ki-test` · **Status:** Konfigurationsvorschlag für einen nutzbaren DEV-Prototyp, keine Produktions- oder QE-Freigabe.

## Absicht und Grenze

Der PO will **mit THEOAgent arbeiten und Erfahrungen sammeln**, statt weitere Testfälle zu entwerfen. Der bestehende DEV-Systemprompt und die sieben THEOAgent-Fachskills bleiben erhalten. Ergänzt wird ein knapper Quellenarbeitsgang über **bereits vorhandene** OpenWebUI-Knowledge-/DRS-Werkzeuge sowie **SourceGuard v0.2.0**.

SourceGuard ist ein Open-WebUI-Tool, **keine** Pipe. Es erzwingt keine Toolaufrufe oder Antwortsperre (offenes QE-Finding F-C1). Im Knowledge-/DRS-Pfad erhält es den Auszug durch das Modell: Weder Dateiherkunft noch Toolausführung werden technisch unabhängig authentifiziert. Das muss auch für den Benutzer klar bleiben.

## DRS-Werkzeuge sinnvoll einsetzen – P-02 als Grundlage

[DRS-Toolvergleich P-02](POC_P-02_DRS_TOOLS_VERGLEICH.md) bleibt Referenz für Auswahl und Grenzen. **Kein zusätzlicher DRS-Werkzeugadapter**, solange vorhandene Funktionen den Leseweg erfüllen.

| Weg | Aktiviertes Werkzeug / vorhandene Funktion | Wann geeignet | Belegstatus |
|---|---|---|---|
| Fachbibliothek | `search_knowledge_files`, `grep_knowledge_files`, `view_knowledge_file` | **Derzeit nur Wolfgang Klippert, *Vom Text zur Predigt***; tatsächlich gelesene Passage über `view_knowledge_file` | `knowledge`, `original_excerpt`; Herkunft des übergebenen Textes nicht unabhängig authentifiziert |
| Webrecherche | **`Websuche_und_Dokument (Faster - No Summary No Fulltext)`** | URL finden, Treffer und gegebenenfalls Auszüge für Navigation | Treffer/Snippets nicht als vollständige Originallektüre |
| Weboriginal (SourceGuard) | **`read_source`** | Freigegebene öffentliche HTML-/Textquelle mit konkreter URL und Fundstelle | Direkter URL-Abruf, keine semantische Behauptungsprüfung |
| PDF/DOCX | **`Outline Document Tools (DrsKita)`** | Nur bei zugänglicher und tatsächlich gelesener Dokumentpassage | `document`/`tool_excerpt`; PDF-Seite ist keine Druckseite |
| Bibel | **`Bibel-Tool`** | Biblische Passagen, genaue Übersetzung und Fundstelle gesondert prüfen | `tool_excerpt`; Anzeigename beweist nicht die interne Implementierung oder Fassung |
| DRS-Wiki | **`Mcp_mediawiki`** | Einschlägige Wiki-Informationen | `tool_excerpt`; Wiki nicht automatisch amtlicher Normtext |
| DRS-TYPO3 | **`TYPO3 Document Tools (VZ Orga)`** | Konkrete DRS-Dokumente bei vorhandenen Rechten | `document`/`tool_excerpt`, nur tatsächlich gelesene Inhalte |

Die Anzeigenamen stammen aus der aktiven Werkzeugauswahl von THEOAgent DEV vom 14.11.2026. Die im [historischen P-02-Vergleich](POC_P-02_DRS_TOOLS_VERGLEICH.md) genannten Versionsbezeichnungen sind **nicht** als Identitätsnachweis für diese DEV-Werkzeuge zu verstehen. Insbesondere ist **`Bibel-Tool` nicht nachweislich identisch mit `Single Domain Web Search v2.0.1`**. Das dortige Finding F-A1 darf nur nach technischer Identitätsprüfung auf das aktivierte Bibel-Tool übertragen werden. Aktivierung ist kein End-to-End-Ausführungsnachweis.

## SourceGuard-Schnittstelle

**Bestehende Funktionen:** `read_source(url, section)`, `compare_sources(url_a, url_b, locator)`, `verify_evidence(claim, url, locator)`.

**Neue gemeinsame Funktion:** `review_evidence(claim, source_type, source_title, locator, evidence_text="", source_url="", evidence_reference="", source_tool="", evidence_kind="original_excerpt")`.

- Für `source_type=web`: **eigener** Originalabruf über `source_url` und `locator`; übergebener `evidence_text` wird **nicht** als Abrufbeleg benutzt.
- Für `source_type=knowledge`, `document` oder `tool_excerpt`: Modell übergibt **ausschließlich** den tatsächlich gelesenen Passagenauszug, die Quelle, Fundstelle und Tool-Referenz. `source_tool` bezeichnet das real verwendete OpenWebUI-/DRS-Werkzeug. Ohne die Pflichtfelder bleibt die Evidenz unvollständig.
- `evidence_kind=search_snippet` und `evidence_kind=summary` führen bei übergebenen Werkzeugtexten zu `INSUFFICIENT_EVIDENCE`.
- Bei brauchbarer Evidenz lautet der technische Status `EVIDENCE_READY_FOR_REVIEW`: Der Text steht dem Modell zur Verfügung, **die Behauptung wurde noch nicht semantisch geprüft**. `claim_assessment=REQUIRES_MODEL_JUDGEMENT` und `semantic_claim_verified=false`.
- `exact_wording_found` beschreibt ausschließlich einen lexikalischen Treffer. `source_provenance_verified=false` bei Knowledge und anderen Werkzeugauszügen; `MODEL_SUPPLIED_TOOL_EXCERPT` ist **kein** unabhängiger Originalnachweis.
- Leere Referenzen, nicht zugängliche Seiten, nicht gefundene Fundstellen und Toolfehler nicht als belegt ausgeben.

### Beispiel: Klippert / Fachbibliothek

1. THEOAgent ermittelt die einschlägige Stelle mit `search_knowledge_files` oder `grep_knowledge_files`.
2. THEOAgent liest die Stelle tatsächlich über `view_knowledge_file`.
3. THEOAgent übergibt die **im Tool sichtbare** Passage und Referenz an `review_evidence`:
   - `claim`: die zu überprüfende Aussage über Klipperts Predigtverständnis,
   - `source_type="knowledge"`,
   - `source_title`: bibliografisch zutreffender Werktitel,
   - `locator`: tatsächlich gezeigte Kapitel-/Abschnittsangabe, keine erfundene Druckseite,
   - `evidence_text`: tatsächlich gelesener Auszug,
   - `source_tool="view_knowledge_file"`,
   - `evidence_reference`: die im Tool vorliegende Dateireferenz/Fundstelle,
   - `evidence_kind="original_excerpt"`.
4. THEOAgent urteilt **selbst anhand der Passage**: *belegt / widerlegt / nicht überprüfbar*, begründet und unterscheidet Klippert-Text von eigener homiletischer Bewertung.

## Systemprompt für THEOAgent DEV

**Vollständige Arbeitsfassung:** [THEOAgent DEV – Systemprompt v0.3.2](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.2.md).

Zur Einrichtung den Systemprompt **ab der Überschrift „SYSTEMPROMPT – ab hier vollständig in THEOAgent DEV verwenden“** als zusammenhängenden Text einsetzen. **Keine zusätzlichen älteren SourceGuard-Ergänzungsblöcke einkopieren** – die Quellenarbeitsregeln sind bereits enthalten.

Die sieben eigenständigen, bestehenden Fachskills mit Anzeigenamenspräfix `THEOAgent - ` bleiben aktiviert und unverändert.

## Einstieg in den produktiven DEV-Arbeitsprototyp

**Einrichten (nur DEV):** Werkzeugcode [SourceGuard v0.2.0](../../tools/drs_ki/sourceguard_web_poc_v0_2_0.py) im bestehenden DEV-Tool aktualisieren, `review_evidence` erscheint als neue Funktion. Dem Modell `THEOAgent DEV` zuweisen; vorhandene Knowledge-Werkzeuge und fachlich relevante DRS-Werkzeuge beibehalten. den vollständigen konsolidierten Systemprompt v0.3.2 einsetzen; keine ältere Zusatzpassage anhängen. Endnutzer muss **kein** Werkzeug konfigurieren.

**Praktisch nutzen:** Normale Arbeitsaufgaben stellen (Predigtanalyse anhand Klippert, Exegese anhand Dei Verbum, Liturgierecht, DRS-Ordnungen). Auf tatsächliche Toolaufrufe und Quellenbelege achten; Fehlverhalten knapp dokumentieren. **Auf PO-Wunsch werden jetzt keine weiteren Testdateien, Testmatrizen oder Regressionstests verfasst.**

**Status:** QE-Nachbesserungen F-01/02/03/04/06/07 im Branch eingearbeitet; F-05 sachlich zurückgewiesen. Implementiert und dokumentiert; die neue gemeinsame Funktion und die aktualisierte Konfiguration sind auf DRS:KI DEV noch **nicht** live bestätigt. Keine Behauptung einer unabhängigen Knowledge-Provenienz oder einer technischen SourceGuard-Gate-Funktion. QE kann den Prototyp später am konkreten Repo-Stand prüfen; der PO entscheidet über Freigabe.
