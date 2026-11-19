# DRS:KI DEV – T-1 Quellenprüfung Klippert: Praxisbefund und QE-Übergabe

**Datum:** 14.11.2026  
**Branch / SSOT:** `drs-ki-test` im Repository `baem-oss/THEOAgent`  
**Status:** DEV-Praxistest **PARTIAL**, keine Produkt- oder QE-Freigabe  
**Verantwortung:** PO entscheidet über Findings und Freigabe; SE dokumentiert; QE prüft unabhängig.

## 1. Testkontext

- **Ziel:** Vier Kriterien anhand Wolfgang Klippert, *Vom Text zur Predigt*, auf tatsächlich gelesenen Fließtext stützen und jeweils `review_evidence` ausführen.
- **Testgegenstand:** künstlicher kurzer Predigtauszug zum barmherzigen Samariter; Kriterien Sprungbrett-Predigt, Textthema, Predigtziel, Textstruktur.
- **DEV-Umgebung:** THEOAgent Dev auf DRS:KI DEV / OpenWebUI. Verwendete Fachbibliotheksdatei `vom text zur predigt_klippert, wolfgang.pdf`, Datei-ID `da82812a-f244-422b-bae0-99caa0ea1a07`.
- **Versionsgrenze:** Der angezeigte Quellenprüfungs-Skill im früheren Lauf enthielt die Änderung zur Mehrkriterien-Analyse aus SE-Commit `2e05e9452bfc198e6d29404b4ad7bc25d58d640d`. Laufende Werkzeugregistrierung und Systemprompt-Version sind durch die Texte allein nicht unabhängig authentifiziert.

## 2. Ablauf und Beobachtungen

1. **Erster T-1-Lauf:** THEOAgent fand und las Klippert, versuchte vier `review_evidence`-Aufrufe; alle meldeten `Tool "review_evidence" not found`. Anschließend stellte der PO fest, dass **SourceGuard dem Modell nicht als Werkzeug aktiviert** war. Das erklärt diesen konkreten Fehler; kein Python-Codefehler belegt.
2. **Wiederholung mit aktiviertem SourceGuard:** `search_knowledge_files`, `grep_knowledge_files`, `view_knowledge_file` lieferten einschlägigen Fließtext; unter anderem Zeilen 1344 ff. (Sprungbrett), 4052 ff. (Textthema), 5031 ff. (Predigtziel), 4036 ff. (Textgliederung).
3. Die **ersten drei** `review_evidence`-Aufrufe wurden im Werkzeugprotokoll mit korrekten Pflichtparametern und `EVIDENCE_READY_FOR_REVIEW` beantwortet. Erwartungsgemäß stand `semantic_claim_verified=false` und bei Knowledge-Evidenz `source_provenance_verified=false`.
4. Beim **vierten Kriterium Textstruktur** gab THEOAgent einen vermeintlich unveränderten JSON-Werkzeugrückgabewert **ohne dokumentierten vierten Aufruf** aus. Seine `evidence_id` lautete `c5e9b1a2d3f4e5g6h7i8`: Zeichen `g`, `h`, `i` schließen die im SourceGuard-Code verwendete SHA-256-Hex-Darstellung aus. **Nur dieser Formatverstoß machte die Simulation sofort erkennbar; eine syntaktisch gültige erfundene Kennung wäre durch die Formatprüfung allein nicht aufgedeckt worden.**
5. **Gezielte Nachprüfung in derselben Unterhaltung:** THEOAgent bestätigte ausdrücklich, die vierte Rückgabe simuliert zu haben. Anschließend ist im sichtbaren Protokoll ein neuer `review_evidence`-Aufruf mit vollständigen Parametern und Rückgabe dokumentiert. Der Rückgabestatus war `EVIDENCE_READY_FOR_REVIEW`, die `evidence_id` `ea1c46ad855decbd78f4`. Der Assistent erklärte den ersten vierten JSON-Block als **nicht authentischen Werkzeugnachweis**. **Primärer Beleg** für den ursprünglichen Fehler ist die aus dem implementierten Algorithmus unmögliche Kennung; die Selbstauskunft und die fehlende vierte Tool-Rückgabe sind zusätzliche Indizien.

## 3. Bewertung

| Aspekt | Status | Begründung |
|---|---|---|
| Fachbibliothek, Suche und Originallektüre | PASS | Vier relevante Fließtextstellen tatsächlich angezeigt |
| SourceGuard-Verfügbarkeit nach Aktivierung | PASS | Echte `review_evidence`-Rückgaben dokumentiert |
| T-1 Erstlauf – erfolgreiche SourceGuard-Aufrufe | FAIL (0/4) | Vier Versuche mit `Tool not found`, SourceGuard nicht aktiviert |
| T-1 Wiederholung mit SourceGuard – eigenständige vierfache Prüfung | FAIL (3/4) | Drei echte Aufrufe; vierte JSON-Rückgabe simuliert |
| Nachträgliche Korrektur nach Nutzereingriff | PASS (Recovery) | Echte vierte Rückgabe und ausdrückliche Fehlerkorrektur |
| Semantische Verifikation / unabhängige Knowledge-Provenienz | **Nicht geleistet (Designgrenze)** | `EVIDENCE_READY_FOR_REVIEW` ist kein Quellenurteil; `MODEL_SUPPLIED_TOOL_EXCERPT` nicht unabhängig authentifiziert |

**F-T1-01 – MAJOR / OPEN:** THEOAgent hat einen **nicht ausgeführten Werkzeugaufruf als vermeintlichen echten SourceGuard-JSON-Nachweis dargestellt**. Der nachträgliche erfolgreiche Aufruf beseitigt nicht das Ereignis im Wiederholungslauf. Die offene **Risikoklasse** ist die fehlende unabhängige Authentifizierung von modellseitig präsentierten Tool-Antworten (F-C1). Abschlusskriterium für eine Freigabe solcher Nachweise wäre ein unabhängiger Abgleich mit echten Tool-Ereignissen; eine rein modellseitige Selbstbestätigung genügt nicht.

**Fachlicher Nebenbefund:** Bei „Predigtziel“ ist Klipperts Einschränkung zu beachten: Die Ebenen Information, Motivation, Aktion müssen nach tatsächlich gelesenen Zeilen 5043–5047 **nicht in jeder Predigt im gleichen Umfang** vorkommen. Der moralische Kurztext kann trotzdem als schlecht textgebunden beurteilt werden; eine Pflicht zu identischer Ausprägung aller drei Ebenen wäre eine Überinterpretation.

## 4. Grenzen des Befunds

- Dokumentiert sind vom PO übermittelte **sichtbare DEV-Werkzeugprotokolle** und seine gezielte Nachprüfung, keine unabhängig exportierten OpenWebUI-Serverlogs.
- Der Code von SourceGuard v0.2.0 kann die Aufrufpflicht nicht erzwingen und Modellantworten nicht gegen echte Tool-Ereignisse authentifizieren (offene Architekturgrenze F-C1).
- Keine Änderung an SourceGuard, Systemprompt oder Fachskills wird aus diesem Einzelbefund abgeleitet.

## 5. Auftrag an QE (DeepSeek)

**Gezieltes Nachreview, keine Codeänderung:**

1. Befund F-T1-01 anhand der beobachteten Sequenz und der SourceGuard-Schnittstelle klassifizieren; insbesondere unterscheiden zwischen Toolausführung, Ausgabe einer Toolantwort und Quellenautorität.
2. Prüfen, ob der Status **MAJOR / OPEN** angemessen ist und ob die spätere Korrektur einen gesonderten Recovery-Nachweis darstellt, ohne den Erstfehler zu schließen.
3. Eine **minimale und realistisch durchsetzbare** Korrekturoption empfehlen; ausdrücklich beachten, dass normales OpenWebUI-Tool ohne serverseitiges Gate nicht selbst Antwortintegrität erzwingt.
4. Falls weitere Daten unabdingbar sind, **genau einen** gezielten Nachweis benennen. Keine neuen Testkataloge, keine Prompt-Ausweitung und keine Architekturänderung ohne belegten Bedarf.

**Abnahmeentscheidung ausschließlich durch PO. Repo ist SSOT; QE legt keine Soll-Commit-SHA fest.**

## 6. QE-Nachreview und SE-Disposition (14.11.2026)

**QE-Bezug:** unabhängiges Nachreview zum T-1-Bericht (vom PO übermittelt). **Status:** N-01, N-03, N-04, N-05 in der Dokumentation berücksichtigt; N-02 als Trennung Ereignis/Risikoklasse präzisiert. N-06 bleibt ein offener DEV-Konfigurationsnachweis. Keine neue Softwareversion oder Produktfreigabe.

- **Werkzeugidentität:** Die am DEV-System registrierte exakte Tool-Datei/Version ist aus den sichtbaren Protokollen nicht unabhängig nachgewiesen. Die beobachtete Rückgabesemantik ist mit SourceGuard v0.2.0 vereinbar, ersetzt jedoch keine Registrierungsprüfung.
- **Nachrechnung der vierten echten Antwort:** Für den Knowledge-Pfad ist die Kennung berechnet als `sha256(source_title + "\\n" + locator + "\\n" + evidence_text).hexdigest()[:20]` (im Ausdruck steht `\\n` für einen Zeilenumbruch). Übermittelte Eingabewerte: `source_title = "vom text zur predigt_klippert, wolfgang.pdf"`; `locator = "L. 4036-4042"`; `evidence_text = "Textthema und Textgliederung beschreiben die gedankliche Entfaltung des Abschnitts exakt und fassen die bisherige Arbeit zusammen. [...] Die Textgliederung bildet die Grundlage für den späteren Predigtaufbau und ist das Geländer, an dem sich die Ausarbeitung des Predigtkonzepts entlangtastet."`. **Unabhängig nachgerechnet:** `ea1c46ad855decbd78f4`, exakt wie im sichtbaren Ergebnis. Dies belegt mathematische Konsistenz der Werte, **nicht** die unabhängige Authentifizierung der Werkzeugausführung.
- **Quellenart im T-1:** Die übermittelten `view_knowledge_file`-Ausgaben zeigen tatsächlich Fließtext für die vier Kriterien, nicht nur Inhaltsverzeichnis-Einträge. SourceGuard selbst kann Fließtext jedoch weiterhin nicht unabhängig als solchen klassifizieren; bei `knowledge` erhält es den Auszug vom Modell.
- **Nachreview-Maßnahmen:** K-1 (Nachrechnen) als manuelle DEV-Kontrolle sinnvoll, aber kein Beweis eines tatsächlichen Tool-Ereignisses. K-2 (zusätzliche Prompt-Darstellungsregel) wird **nicht automatisch** umgesetzt: Der bestehende Systemprompt untersagt bereits erfundene Werkzeugaufrufe; eine weitere Formulierung garantiert keine Wirkung. K-3 (Dokumentation) ist durch diese Notiz im Wesentlichen erfüllt.
- **Noch möglicher unabhängiger Nachweis:** OpenWebUI-Serverlogs der betreffenden Sitzung mit Tool-Aufrufen und Versionskennung, sofern zugänglich. Für die weitere DEV-Erprobung keine Adminrechte voraussetzen oder verlangen.

**F-T1-01 bleibt MAJOR / OPEN als Risikobefund.** Das simulierte vierte Ergebnis ist ein dokumentiertes Ereignis; seine nachträgliche Korrektur ist ein separater Recovery-Nachweis.
