# QE-Findings-Disposition – SourceGuard v0.2.0 (14.11.2026)

**Projekt:** THEOAgent · **SSOT:** Repository `baem-oss/THEOAgent` · **Branch:** `drs-ki-test`

**Grundlage:** Unabhängiges statisches DeepSeek-QE-Review vom 14.11.2026 am vorgefundenen Branch-Head `418e52e3c09d08cbf22302e6ff28a7e4f80ffd71`, Code-Blob `af185c06cfc3262a153bcb0d36fc3a5824ebd4ab`. Das QE-Ergebnis wurde im Chat durch den PO übermittelt. Der QE hat keine Tests ausgeführt. Der folgende Text dokumentiert die SE-Bearbeitung; er ersetzt nicht den unabhängigen Reviewbericht.

**PO-Auftrag:** Findings gezielt korrigieren, keine neue Architektur und **keine neuen Tests**. `VERSION = "0.2.0"` bleibt unverändert.

| Finding | SE-Disposition | Umsetzung |
|---|---|---|
| F-01 MAJOR – leerer Locator → `SAME_TEXT` | **Übernommen, behoben** | `compare_sources` und `verify_evidence` lehnen leere/ungültige Locators ab (`INVALID_LOCATOR`); `SAME_TEXT` erfordert zusätzlich zwei nichtleere Fundstellentexte |
| F-02 MINOR – Web-Provenienzgrenzen | **Übernommen, behoben** | `review_evidence` nennt bei Webtext ausdrücklich technische URL-Lektüre ohne Editions-/Autor-/Behauptungsbestätigung |
| F-03 MINOR – ungleiche Locator-Limits und fehlende Fehlerursache | **Übernommen, behoben** | `read_source` akzeptiert bis zu 100 Zeichen, entsprechend `_locator_pattern`; bei Webfehler Weitergabe von `retrieval_error`/`retrieval_error_type` |
| F-04 MINOR – permissiver Latin-1-Fallback | **Teilweise übernommen, konservativ korrigiert** | ISO-8859-1 bleibt aus Kompatibilitätsgründen, `read_source` meldet `charset_used` und `charset_uncertain` bei undeklariertem Latin-1-Fallback. **Keine garantierte Mojibake-Erkennung**; falsche explizite Charset-Angaben bleiben Restrisiko |
| F-05 MINOR – vermeintlich totes `re.escape`-Leerzeichen | **Zurückgewiesen** | Python `re.escape("can. 767")` liefert einen Backslash vor dem Leerzeichen (`can\\.\\ 767`); die bestehende Ersetzung von `\\ ` durch `\\s+` ist funktional. Keine Codeänderung |
| F-06 MINOR – nicht korrekte DEV-Werkzeugnamen | **Übernommen, behoben** | [Arbeitsprofil](THEOAGENT_DEV_SOURCEGUARD_V0_2_0_ARBEITSPROTOTYP.md) mit aktivierter DEV-Auswahl aktualisiert: `Websuche_und_Dokument (Faster - No Summary No Fulltext)`, `Outline Document Tools (DrsKita)`, `TYPO3 Document Tools (VZ Orga)`, `Bibel-Tool`, `Mcp_mediawiki`. Nur **Klippert** ist in der Fachbibliothek |
| F-07 MINOR – uneinheitliche Evidenzkennungen | **Teilweise übernommen** | `review_evidence` und `verify_evidence` kennzeichnen die `evidence_id_origin` ausdrücklich (`DIRECT_WEB_RETRIEVAL` bzw. `MODEL_SUPPLIED_TOOL_EXCERPT`). Die bestehenden Statusnamen bleiben zwecks API-Kompatibilität; weitergehende Konsolidierung zurückgestellt |

## Grenzen und unmittelbarer nächster Schritt

- **Keine neuen Tests geschrieben und keine Tests als erfolgreich behauptet.** Reine Code-/Dokumentationsbearbeitung; das aktualisierte Tool wurde noch nicht auf DRS:KI DEV ausgeführt.
- Das kritische Architektur-Finding **F-C1** (kein technisch erzwungener Check vor jeder Antwort) bleibt offen. `EVIDENCE_READY_FOR_REVIEW` ist kein semantischer Verifikationsnachweis.
- DEV-Prototyp: Quellcode im OpenWebUI-Tool aktualisieren und vorhandenen Systemprompt gemäß [Arbeitsprofil](THEOAGENT_DEV_SOURCEGUARD_V0_2_0_ARBEITSPROTOTYP.md) ergänzen. Danach praktische Arbeitsaufgaben mit Klippert und Web-/DRS-Quellen bearbeiten, ohne formalen Testplan.
- Der QE kann den konkret versionierten Nachbesserungsstand bei Bedarf unabhängig nachprüfen. **Nur PO entscheidet über Freigaben.**
