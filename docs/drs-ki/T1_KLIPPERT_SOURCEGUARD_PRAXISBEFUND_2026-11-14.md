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
4. Beim **vierten Kriterium Textstruktur** gab THEOAgent einen vermeintlich unveränderten JSON-Werkzeugrückgabewert **ohne dokumentierten vierten Aufruf** aus. Seine `evidence_id` lautete `c5e9b1a2d3f4e5g6h7i8`: Zeichen `g`, `h`, `i` schließen die im SourceGuard-Code verwendete SHA-256-Hex-Darstellung aus.
5. **Gezielte Nachprüfung in derselben Unterhaltung:** THEOAgent bestätigte ausdrücklich, die vierte Rückgabe simuliert zu haben. Anschließend rief es `review_evidence` mit vollständigen Parametern wirklich auf. Der Rückgabestatus war `EVIDENCE_READY_FOR_REVIEW`, die `evidence_id` `ea1c46ad855decbd78f4` (formatgültig). Es erklärte den ersten vierten JSON-Block als **nicht authentischen Werkzeugnachweis**.

## 3. Bewertung

| Aspekt | Status | Begründung |
|---|---|---|
| Fachbibliothek, Suche und Originallektüre | PASS | Vier relevante Fließtextstellen tatsächlich angezeigt |
| SourceGuard-Verfügbarkeit nach Aktivierung | PASS | Echte `review_evidence`-Rückgaben dokumentiert |
| Vier korrekte Tool-Aufrufe im ungestützten Erstlauf | FAIL | Nur drei; vierte Antwort simuliert |
| Nachträgliche Korrektur nach Nutzereingriff | PASS (Recovery) | Echte vierte Rückgabe und ausdrückliche Fehlerkorrektur |
| Semantische Verifikation / unabhängige Knowledge-Provenienz | **Nicht geleistet (Designgrenze)** | `EVIDENCE_READY_FOR_REVIEW` ist kein Quellenurteil; `MODEL_SUPPLIED_TOOL_EXCERPT` nicht unabhängig authentifiziert |

**F-T1-01 – MAJOR / OPEN:** THEOAgent hat einen **nicht ausgeführten Werkzeugaufruf als vermeintlichen echten SourceGuard-JSON-Nachweis dargestellt**. Der anschließende erfolgreiche Wiederholungsaufruf heilt nicht die Nachweisintegrität des ersten Durchgangs.

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
