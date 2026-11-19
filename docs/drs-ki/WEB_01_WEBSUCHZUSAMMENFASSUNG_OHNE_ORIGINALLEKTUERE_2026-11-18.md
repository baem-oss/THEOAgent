# WEB-01 – Websuchzusammenfassungen ohne nachgewiesene Originallektüre

**Datum:** 18.11.2026  
**Projekt/Umgebung:** THEOAgent DEV / DRS:KI DEV  
**Branch:** `drs-ki-test`  
**Einstufung:** MAJOR / OPEN (SE-Bewertung; keine separate QE-Abnahme)  
**Bezug:** F-C1 (technische Durchsetzung), F-C2 (Werkzeugschnittstellen), K-01, Q-01 sowie E-02  
**Änderung:** Dokumentations- und Ursachenanalyse, **kein Fix**, keine Produktfreigabe.

## 1. Beobachtung

THEOAgent übernimmt in kirchenrechtlichen Antworten Aussagen aus `get_websearch_results`-Ergebnissen, ohne dass in der sichtbaren Werkzeugspur ein gesonderter Aufruf zur Originallektüre folgt. Suchergebnisse enthalten einen generierten `WEB_RESEARCH_CONTEXT` mit `DETAILED_SUMMARY`, Evidenz-Digest, Quellenliste und Einschränkungen. Diese Zusammenfassung kann inhaltlich falsch sein, selbst wenn sie eine amtliche URL als Herkunft nennt.

Bei **E-02** enthielt der Recherche-Digest die unrichtige These, die fehlende Erlaubnis einer konfessionsverschiedenen Ehe mache die Ehe ungültig; die Endantwort übernahm diesen Fehler.

Bei **K-01** enthielt der Digest denselben Fehler, während die Endantwort die Unterscheidung von Erlaubtheit und Gültigkeit weitgehend richtig vornahm. Das ist kein Beleg einer erfolgten Originalprüfung.

Bei **Q-01** verlangte der Auftrag ausdrücklich die Prüfung der Aussage: „Eine katholisch-evangelische Ehe ist ohne die Erlaubnis nach can. 1124 CIC ungültig.“ THEOAgent lud den Quellenprüfungs- und Grundlagen-Skill, führte danach aber nur `get_websearch_results` aus. Es gab keinen sichtbaren `read_source`, `review_evidence` oder anderen Original-Leseaufruf. Die Antwort war in ihrem Hauptergebnis richtig, sprach aber von „Inhalt der Originalquelle (CIC)“ und präsentierte eine deutschsprachige, zitatartig gesetzte Normwiedergabe unter Verweis auf eine englischsprachige Quelle, ohne nachgewiesenen Wortlautabgleich.

**Quellenhinweis:** Der abschließende allgemeinverständliche Hinweis „Fragen Sie THEOAgent: Prüfe deine Quellen mit SourceGuard und zeige mir die Originalstellen“ war bei K-01 und Q-01 korrekt. **Nicht ändern.** Er ist ein nützlicher Workaround, ersetzt jedoch keine Erstlektüre.

## 2. Werkzeugnachweise (aus PO-Uploads)

| Fall | Sichtbare Aufrufe | Gesonderte Originallektüre nachgewiesen? | Fachliche Endantwort |
|---|---|---|---|
| E-02 | `view_skill` ×4, `get_websearch_results` ×1 | Nein | Fehler bei Gültigkeit / Erlaubtheit |
| K-01 | `view_skill` ×2, `get_websearch_results` ×1 | Nein | Im Kern korrekt, Zuständigkeit unvollständig |
| Q-01 | `view_skill` ×2, `get_websearch_results` ×1 | Nein | Im Kern korrekt, Prüf- und Zitatcharakter überhöht |

**Nachweisgrenze:** Die Auswertung beruht auf den vom PO bereitgestellten sichtbaren DRS:KI-Werkzeugprotokollen, nicht auf Backend-Logs. „Nicht nachgewiesen“ darf nicht ohne Zusatz als „technisch unmöglich“ gelesen werden. Der konkrete Websuch-Tooltyp hinter dem Funktionsnamen `get_websearch_results` wurde im aktuellen DEV-Test nicht über Installationsdaten oder Code-Hash bestimmt.

## 3. Ist-Architektur aus dem Repository

- [AK-02 / F-C2](SCHNITTSTELLENPRUEFUNG_AK-02_F-C2.md) vergleicht historische DRS:KI-Werkzeuge **statisch**, ohne Livebestätigung. `Faster – No Summary v2.1.0` liefert laut diesem Vergleich max. ca. 4.500 Zeichen Webauszug/Snippet und keine beliebige `fetch_url(url)`-Operation; andere Varianten liefern eine LLM-Synthese.
- [P-02](POC_P-02_DRS_TOOLS_VERGLEICH.md) behandelt die Websuche als Navigationsweg und fordert die Prüfung konkreter Textstellen; ausdrücklich **kein** Scheinbeleg durch Snippets oder Digest.
- [Systemprompt v0.3.11](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md), Abschnitt „Quellen finden und tatsächlich lesen“, sieht für öffentliche HTML-/Textquellen nach der URL-Findung einen gezielten `read_source(url, section)`-Aufruf oder `review_evidence(source_type="web", source_url=..., locator=...)` vor.
- [Skill Theologische Quellenprüfung](../../config/drs-ki/skills/theologische-quellenpruefung/SKILL.md) fordert ausdrückliche Originallektüre und die Trennung von Treffer, Quelle und Beleg.
- Der bestehende [SourceGuard 0.2.3](../../tools/drs_ki/sourceguard_web_poc_v0_2_3.py) ist ein normales Werkzeug und kann nicht erzwingen, dass das Modell ihn aufruft oder den Antworttext zurückhält. Die bereits bewiesene **explizite Aufrufbarkeit** ist nicht erneut zu testen.

## 4. Bewertung / Ursache

**Gesicherter Befund:** Die vorgeschriebene Quellenlektüre wurde in den genannten Antworten nicht durch einen sichtbaren eigenständigen Werkzeugaufruf nachgewiesen. In Q-01 wurde Quellenprüfung zugleich sprachlich suggeriert.

**Plausible, nicht bestätigte Ursachen:**
1. Das Modell behandelt den vom Websuchwerkzeug erzeugten ausführlichen Digest als bereits ausreichende Evidenz.
2. Die Werkzeug-/Skill-Orchestrierung übersetzt die vorhandene Quellenregel nicht zuverlässig in den tatsächlichen Original-Leseaufruf.
3. Das verwendete Websuchwerkzeug besitzt selbst keinen vollwertigen gezielten URL-/Abschnittsabruf (gilt für historisch untersuchte Varianten; **nicht** als genaue Live-Implementierung bestätigt).

**Nicht belegt:** Ein Fehler im Quellcode von SourceGuard, fehlende Aufrufbarkeit von SourceGuard, ein allgemeiner Fehler der Knowledge-Werkzeuge oder die kausale Wirkung einer konkreten Promptänderung.

## 5. Verfügbare Lesewege und Grenzen

| Pfad | Belegbare Fähigkeit / Rolle | Grenze |
|---|---|---|
| `get_websearch_results` | Suche nach URLs und ggf. Snippets/Auszügen/Digest | Funktionsname allein verrät nicht die installierte Variante; Digest nie als unabhängige Originallektüre deklarieren |
| SourceGuard `read_source(url, section)` | Gezielter Weboriginalabruf für zugelassene öffentliche HTML-/Textseiten | Kein garantierter automatischer Aufruf; Abschnitt/HTML-Extraktion und Host-Freigaben beachten |
| SourceGuard `review_evidence(source_type="web", ...)` | Belegaufbereitung mit internem SourceGuard-Webabruf | Keine Garantie semantischer Wahrheit, kein Antwort-Gate |
| `view_knowledge_file` | Lokale Fachbibliothek, gesonderter Original-Leseweg | Nicht Ersatz für aktuelle amtliche Onlinefassung; Knowledge-Provenienz nicht unabhängig durch SourceGuard authentifiziert |
| DRS Outline / MediaWiki / TYPO3 | Je nach Quellentyp passende Dokument-/interne Lesewege | Kein generischer `fetch_url`-Ersatz und keine pauschale Normautorität |

## 6. Kleinster sinnvoller nächster Schritt

**Keine neuen allgemeinen Regeln und keine zusätzlichen Skills.** Die Regel ist bereits im Systemprompt und im Quellenprüfungs-Skill enthalten.

1. **Einmalige Schnittstellenklärung im DEV-Modellprofil**: Exakten Anzeigenamen/Version des dem Modell zugeordneten Websuchwerkzeugs und, soweit sichtbar, die Rückgabeart des `get_websearch_results` sowie die aktivierten SourceGuard-Funktionen dokumentieren. Keine Adminrechte voraussetzen.
2. **Gezielte Diagnose derselben Norm:** Nur prüfen, ob THEOAgent nach einer normalen Websuche den bereits verfügbaren `read_source`-Leseweg selbstständig verwendet. Keine Wiederholung eines expliziten SourceGuard-Erreichbarkeitstests.
3. **Falls weiter kein Leseaufruf:** Eine einzelne minimale Änderung der bestehenden Arbeitsanweisung erwägen, die fehlende Originallektüre als nicht verifizierbar kennzeichnet und die Anforderung zur gezielten Weboriginallektüre bei normativen Aussagen schärft. Die Umsetzung erfolgt erst nach PO-Entscheidung; kein Scheinversprechen einer technischen Durchsetzung.
4. **Vergleich/Abnahme:** Ein bekannter Negativfall (can. 1124) reicht zunächst. PASS nur mit sichtbarem tatsächlich relevantem Originalabruf, korrekter Auslegung und zutreffender Offenlegung des Evidenzstatus. Anderenfalls **FAIL** bzw. **PARTIAL**, F-C1 bleibt unabhängig offen.

## 7. Status und Änderungsgrenzen

**WEB-01 MAJOR / OPEN**. Die fachliche Ursache ist noch nicht vollständig lokalisiert; keine Implementierung, kein Live-Fix und kein neuer DRS:KI-Test durch den SE erfolgt. **F-C1 CRITICAL / OPEN** bleibt eigenständig bestehen.

Es wurden **keine** Änderungen an `main`, Requirements v1.2.0, Systemprompt, Skills, SourceGuard oder einer DRS:KI-Konfiguration vorgenommen. Testreihen Eheschließung, Taufe und Trauer werden durch diese Analyse nicht wieder geöffnet.
