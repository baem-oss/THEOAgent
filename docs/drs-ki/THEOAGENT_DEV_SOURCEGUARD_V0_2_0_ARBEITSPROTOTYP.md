# THEOAgent DEV – SourceGuard v0.2.0 Arbeitsprofil (Erprobungsprototyp)

**Stand:** 14.11.2026 · **Branch:** `drs-ki-test` · **Status:** Konfigurationsvorschlag für einen nutzbaren DEV-Prototyp, keine Produktions- oder QE-Freigabe.

## Absicht und Grenze

Der PO will **mit THEOAgent arbeiten und Erfahrungen sammeln**, statt weitere Testfälle zu entwerfen. Der bestehende DEV-Systemprompt und die sieben THEOAgent-Fachskills bleiben erhalten. Ergänzt wird ein knapper Quellenarbeitsgang über **bereits vorhandene** OpenWebUI-Knowledge-/DRS-Werkzeuge sowie **SourceGuard v0.2.0**.

SourceGuard ist ein Open-WebUI-Tool, **keine** Pipe. Es erzwingt keine Toolaufrufe oder Antwortsperre (offenes QE-Finding F-C1). Im Knowledge-/DRS-Pfad erhält es den Auszug durch das Modell: Weder Dateiherkunft noch Toolausführung werden technisch unabhängig authentifiziert. Das muss auch für den Benutzer klar bleiben.

## DRS-Werkzeuge sinnvoll einsetzen – P-02 als Grundlage

[DRS-Toolvergleich P-02](POC_P-02_DRS_TOOLS_VERGLEICH.md) bleibt Referenz für Auswahl und Grenzen. **Kein zusätzlicher DRS-Werkzeugadapter**, solange vorhandene Funktionen den Leseweg erfüllen.

| Weg | Werkzeug | Wann geeignet | Belegstatus |
|---|---|---|---|
| Fachbibliothek | `search_knowledge_files`, `grep_knowledge_files`, `view_knowledge_file` | Klippert, Böttigheimer und andere indexierte Werke; möglichst direkte Passage mit `view_knowledge_file` lesen | `knowledge`, `original_excerpt` nach beobachteter Originallektüre |
| Öffentliche Webrecherche | **Faster – No Summary v2.1.0** | Quelle finden, URL und Anfangsauszug gewinnen | Suchtreffer oder gekürztes `PAGE_EXCERPT` nicht als vollständige Originallektüre |
| Öffentliche Weboriginale | `SourceGuard.read_source` | Zugelassenes HTML/Text-Dokument mit genauer URL und Fundstelle | `web`, tatsächlicher HTTPS-Abruf |
| PDF/DOCX | **Outline Document Tools v0.1.0** | Falls konkretes öffentliches Dokument abrufbar und Host erlaubt | `document` oder `tool_excerpt`, nur tatsächlich gelesener Kontext; PDF-Seite ≠ Druckseite |
| DRS-Wiki | **MediaWiki MCP v1.5.0** | Nur wenn eine entsprechende interne DRS-Wikiseite fachlich einschlägig ist | `tool_excerpt`, Wiki nicht als amtlich verbindlichen Normtext behandeln |
| TYPO3-Dateien | **TYPO3 Document Tools v0.3.2** | Nur bei konkreter DRS-Quelle und vorhandenen Leserechten; ggf. `vzorgaoauth_ReadTable` | `document` oder `tool_excerpt`, tatsächlicher Auszug statt Dateidump |
| Synthese | **Fast – Summary v2.1.0** | Bei Bedarf für Orientierung | `summary`, ausdrücklich **kein** Originalbeleg |
| Single-Domain-Suche | **Single Domain Web Search v2.0.1** | Nicht im Belegpfad, solange Redirect-SSRF-Finding F-A1 offen | Kein gesicherter Originalbeleg |

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

## Ergänzung zum bestehenden THEOAgent-DEV-Systemprompt

Die folgenden Absätze **zusätzlich zum vorhandenen Systemprompt und den sieben Fachskills** einsetzen, nicht deren Regeln ersetzen:

> **Quellenarbeit mit SourceGuard v0.2.0 (DEV-Prototyp):** Verwende bestehende Knowledge-, DRS- und Web-Werkzeuge gezielt nach Quellenart. Klippert und andere Fachbibliothekswerke über `search_knowledge_files`/`grep_knowledge_files` finden und die relevante Passage über `view_knowledge_file` tatsächlich lesen; für öffentliche Webseiten zuerst nötigenfalls mit Faster suchen und dann bei erlaubter HTML-Quelle `read_source` nutzen. Outline nur für geeignete PDF-/DOCX-Originale; MediaWiki und TYPO3 nur bei wirklich einschlägigen DRS-Quellen. Weder Snippets noch Indexe noch LLM-Zusammenfassungen sind ein Originalbeleg. Unbekannte DRS-Toolparameter niemals erfinden.
>
> Wenn eine konkrete Autorposition, Norm oder Textbehauptung entscheidend ist, übergib den **tatsächlich gelesenen** Auszug mit Werk, Fundstelle, Werkzeugname und vorhandener Toolreferenz an `review_evidence`. Bei Webquellen verwende die Original-URL statt vom Modell eingefügter Webzitate. `EVIDENCE_READY_FOR_REVIEW` bedeutet nur, dass Evidenz für **dein fachliches Urteil** vorliegt; es ist **keine** technische Bestätigung von Inhalt, Autorenschaft oder Editionsjahr. Bewerte die vollständige Aussage als *belegt*, *widerlegt* oder *nicht überprüfbar*, mit begründeter Fundstelle, und kennzeichne Grenzen. Behaupte niemals einen durch SourceGuard erzwungenen Prüfprozess. Keine doppelten oder aussichtslosen Werkzeugaufrufe. Für einfache, nicht belegpflichtige Formulierungen unnötige Prüfung vermeiden.

## Einstieg in den produktiven DEV-Arbeitsprototyp

**Einrichten (nur DEV):** Werkzeugcode [SourceGuard v0.2.0](../../tools/drs_ki/sourceguard_web_poc_v0_2_0.py) im bestehenden DEV-Tool aktualisieren, `review_evidence` erscheint als neue Funktion. Dem Modell `THEOAgent DEV` zuweisen; vorhandene Knowledge-Werkzeuge und fachlich relevante DRS-Werkzeuge beibehalten. Ergänzung zum Systemprompt eintragen. Endnutzer muss **kein** Werkzeug konfigurieren.

**Praktisch nutzen:** Normale Arbeitsaufgaben stellen (Predigtanalyse anhand Klippert, Exegese anhand Dei Verbum, Liturgierecht, DRS-Ordnungen). Auf tatsächliche Toolaufrufe und Quellenbelege achten; Fehlverhalten knapp dokumentieren. **Auf PO-Wunsch werden jetzt keine weiteren Testdateien, Testmatrizen oder Regressionstests verfasst.**

**Status:** Implementiert und dokumentiert; die neue gemeinsame Funktion und die aktualisierte Konfiguration sind auf DRS:KI DEV noch **nicht** live bestätigt. Keine Behauptung einer unabhängigen Knowledge-Provenienz oder einer technischen SourceGuard-Gate-Funktion. QE kann den Prototyp später am konkreten Repo-Stand prüfen; der PO entscheidet über Freigabe.
