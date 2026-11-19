# P-02 – DRS:KI-Werkzeuge im SourceGuard-Web-PoC vergleichen

**Stand:** 13.11.2026 · **Branch:** `drs-ki-test`  
**Status:** Testplan, keine Testergebnisse, keine Abnahme  
**Ziel:** Das bereits funktionierende DRS:KI-Tool-Calling wiederverwenden und nur belegte Lücken durch eigene Komponenten schließen.  
**Umgebung:** DRS:KI DEV, Developerrechte; Endnutzer bedient ausschließlich das Modell.  
**Voraussetzung:** THEOAgent-DEV-Systemprompt v0.3.0 und sieben zugewiesene Fachskills. Knowledge-Import kann wegen `429 /embeddings` noch scheitern; **kein** Abbruchgrund für direkte Webtests.

## 1. Werkzeugauswahl (KISS)

| DRS:KI-Werkzeug | Im PoC | Zweck | Nicht als Nachweis akzeptieren |
|---|---|---|---|
| **Faster – No Summary v2.1.0** | **Ja, zuerst** | Suche, URL, unverdichteter Web-Auszug, Kennzeichnung Snippet-Fallback | Snippet, gekürzter Auszug oder Treffer allein als vollständig geprüfte Originalstelle |
| **Outline Document Tools v0.1.0** | **Bedingt** | Gezielt verlinkte PDF-/DOCX-Dokumente mit Seiten- und Kontextauszügen | PDF-Seitennummer als Druckseite; Indexseite als Volltext; Werkzeug mit nicht freigegebener Host-Allowlist |
| **MediaWiki MCP v1.5.0** | **Bedingt** | DRS-interne Fachinformationen und Wiki-Originalauszüge, falls Quelle einschlägig | Wiki als amtlich verbindlicher Normtext |
| **TYPO3 Document Tools v0.3.2** | Später / nur bei konkreter DRS-Quelle | Anhänge aus TYPO3, mit vorgelagertem `vzorgaoauth_ReadTable` | ungefilterten Dateidump als verifizierte gesuchte Passage |
| **Fast – Summary v2.1.0** | Optional, Kontrolllauf | Verständliche Synthese zum Vergleich | LLM-Zusammenfassung als Originalbeleg |
| **Websuche/Dokument v2.0.0** | Nicht nötig für P-02 | Ähnlich zur Fast-Synthese | LLM-Synthese als Originalbeleg |
| **Single Domain Web Search v2.0.1** | **Nicht im Belegpfad** | Bibelrecherche erst nach Redirect-SSRF-Fix | Sicherheitsfreigabe; automatische Redirects (QE F-A1) |
| **SourceGuard Web v0.1.0 (eigenes Tool)** | **Vergleich, sobald im DEV-Tool-Editor ausführbar** | Expliziter HTTPS-Originalabruf, kontrollierte Hosts, Ausgabe von Evidenzstatus und Textkürzung | Behauptungswahrheit oder vollständige Quellenprüfung; keine Pipe |

Quellen für Funktionen und Grenzen: [statischer QE-Review](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md) und [Schnittstellenprüfung AK-02](SCHNITTSTELLENPRUEFUNG_AK-02_F-C2.md). Diese Aussagen sind **keine Live-Resultate**.

## 2. Drei fachliche Testfälle

**P-02a – KKK 2267:** Über eine tatsächlich gefundene und geöffnete KKK-Originalseite den Wortlaut von Nr. 2267 sowie die Fassung/Änderungslage prüfen. Dazu `Faster` (Treffer/Auszug) und, falls installiert, `SourceGuard Web.read_source(url, "2267")` verwenden. **Achtung:** Eine Indexseite genügt nicht; derselbe direkte Detail-Link ist für den Vergleich zu verwenden.

**P-02b – CIC can. 767 § 1:** Einschlägigen CIC-Originaltext öffnen, Normnummer und Absatz eindeutig unterscheiden. Bei verfügbarer passender Dokument-URL kann `Outline` ergänzend den Dokumentzugriff testen. Die exakte Fassung und der spezifische Text müssen tatsächlich im abgerufenen Inhalt nachgewiesen werden.

**P-02c – Kompendium der Soziallehre Nr. 160–163:** Öffentlich erreichbare Originalseite (gegebenenfalls englischer Text) über `Faster` und, wenn nutzbar, `SourceGuard Web` lesen. **Kein Knowledge-Import nötig.** Markierungen 160–163 und geprüfte Sprache/Fassung ausweisen; der vollständige Bereich muss im relevanten Auszug enthalten sein. Die zuvor übermittelte englischsprachige Vatikan-URL ist ein Testkandidat, ihre Abrufbarkeit **vom DRS:KI-Server aus** ist noch nicht nachgewiesen.

**MediaWiki/Typo3** werden nur ergänzt, wenn die Testfrage eine entsprechende interne DRS-Quelle wirklich benötigt. Nicht alle Werkzeuge zwangsläufig für denselben Auftrag aufrufen.

## 3. Testdurchführung

Für jeden der drei Fälle:

1. **Neuer Chat, gleiche Modell-/Promptfassung**, nur die für den Test relevanten Werkzeuge aktiv. Toolnamen und tatsächlich sichtbare Werkzeugaufrufe dokumentieren.
2. Durchlauf **A** mit DRS:KI-Werkzeug allein: originaler Prompt, Resultat, Treffer-/Snippet-/Originalstatus und Textfenster festhalten.
3. Durchlauf **B** mit DRS:KI-Recherche plus `SourceGuard Web`, **nur wenn dieses eigene Tool im DEV-System installiert und aufrufbar ist**. Identische Detail-URL verwenden. Einen fehlgeschlagenen Tool-Editor nicht als erfolgreichen Abruf protokollieren.
4. **Negativfall**: Nicht vorhandene Abschnittsnummer (z. B. KKK 99999) abfragen. Erwartung: Kein erfundener Fundstellentext oder Status `geprüft`.
5. Status anhand des tatsächlich sichtbaren Werkzeugergebnisses vergeben; **keine** Tool-Nutzung allein aus der Modellantwort ableiten.

## 4. Einheitliche Bewertung

| Kriterium | PASS | PARTIAL / FAIL |
|---|---|---|
| Aufruf | tatsächlicher Toolaufruf und Rohantwort nachgewiesen | nur Selbstbericht des Modells |
| Originalbezug | konkret benannte Detailseite / Dokument mit gelesenem relevanten Fließtext | Treffer, Index, Snippet oder LLM-Synthese |
| Fundstelle | richtige Textfassung, Artikel/Nr./Canon und passender Wortlaut | unklare oder erfundene Locator-Angabe |
| Vollständigkeit | alle für die Behauptung relevanten Sätze erfasst | Abschnitt gekürzt oder außerhalb des Auszugs |
| Sicherheit | keine verbotenen Ziele/Redirects; keine Datenlecks | Sicherheitsmangel oder nicht überprüft |
| Fehlertransparenz | technische Grenzen und Ausfälle korrekt benannt | Verifikation behauptet trotz fehlender Lektüre |
| Aufwand | vorhandenes DRS-Werkzeug löst Aufgabe ausreichend | eigener Adapter nur bei dokumentierter Lücke |

**Wichtig:** `technical_retrieval=true` beweist ausschließlich den technischen Abruf, **nicht** eine semantische Übereinstimmung und **nicht** die in F-C1 geforderte zwingende Kontrolle aller Modellantworten.

## 5. Entscheidungsregel

- **DRS-Werkzeug ausreichend:** unverändert weiterverwenden, SourceGuard-Webadapter nicht duplizierend ausbauen.
- **DRS-Werkzeug liefert nur Treffer/Snippet/Synthese:** eigener `read_source`-Adapter nur für belegpflichtigen Originalabruf gerechtfertigt.
- **Adapter scheitert ebenfalls oder hat Sicherheits-/Textgrenzen:** gezielt Fehlerursache beheben; nicht die SourceGuard-Pipe als bereits ersetzt betrachten.
- **Kein eigener Tool-Import wegen `loadPyodide is not defined`:** zunächst DRS-Baseline testen, Browser-/Editorproblem separat dokumentieren. Kein Schein-PASS.

**F-C1 und F-C2 bleiben technisch offen**, bis Integration und negative Gates nachgewiesen sind.

## 6. Minimaler Ergebniseintrag je Test

`Test-ID | Datum | Modell-ID | Promptversion | aktives Tool | tatsächlicher Aufruf | Detail-URL | Originaltextstelle | Fundstelle/Fassung | Kürzung | technischer Fehler | PASS/PARTIAL/FAIL | Beleg (redigierter Screenshot/Log)`

Kein ungeprüfter Codeimport von DRS:KI-Werkzeugen in das öffentliche Repository.
