# THEOBald DRS – erstes Zwischenfazit und Ableitung v0.2.0

**Stand:** 12.11.2026 · **Branch:** `drs-ki-test` · **Status:** Zwischenfazit und Prompt-Änderungsbegründung; v0.2.0 ist **Testkandidat**, keine Freigabe.

## 1. Grundlage

Evidenz: `tests/runs/2026-11-11-DRS-K01-K05-EXPLORATORY.md` (K-01 bis K-05), außerdem ursprüngliche DRS-Läufe T-01 bis T-08 einschließlich T-04-K1, T-05 und T-08-R1. Ausgangsprompt: `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.1.2.md`. Zielprompt: `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.2.0.md`.

**Kontrollgrenzen:** Kurztests explorativ; DRS-Tool-Rohdaten und Klippert-Originaldateien lagen dem Prüfer nicht vor; genauer Prompt-Kanal, Modell und Provider unbekannt. Aus einigen gelungenen/fehlgeschlagenen Läufen keine Kausal- oder Statistikbehauptung ableiten.

## 2. Zwischenfazit

**Stärken:**
- Grundlegendes theologisches Argumentieren und unabhängiges Urteil in T-08 zuverlässig innerhalb des beobachteten Paarvergleichs.
- Direkte Chattexte deutlich zuverlässiger als ungesicherte Dateilektüre (T-04-K1 versus T-04).
- Im K-01 korrekter EÜ-Wortlaut mit sichtbarer Websuche; in K-04 angemessene Zurückhaltung ohne Originalzugriff.
- Im PDF-Versuch K-05b ist eine konkrete Textverarbeitung plausibel.

**Schwachstellen:**
- K-02: Vermischung von religiös-sozialer Abgrenzung, kultischer Unreinheit und behauptetem Hilfsverbot; unzureichend gestützte historische Generalisierungen und misslungener Widerspruch zur vorgegebenen Falschbehauptung.
- K-03: Unklare/vermischte Bibliografie sowie aus Handelsbeschreibungen extrapolierte Werkmethodik.
- K-05a: EPUB extrahiert, für Modell nicht nutzbar (PO-Beobachtung); Ursache nicht geklärt.
- K-05b/c: PDF-Analyse liefert zwar konkrete Fragmente, aber Seiten-/Belegprovenienz bleibt nicht nachgewiesen. Testling meldet **80.000-Zeichen-Limit** ohne für den Reviewer einsehbare Rohdaten; Zeichenlimit beweist weder Seitenzählung noch Vollständigkeit. Selbstdeklarierte „alle Zitate geprüft“ und „keine eigenen Interpretationen“ widersprechen der Erklärungsleistung der ersten Antwort.
- T-05: Freeze wurde trotz eigener Statusanzeige verletzt; nicht als durch Prompt allein geheilt ansehen.
- T-03: Ohne tatsächliche Primärquellenlektüre keine aktuelle, präzise Normauskunft absichern.

**Kernbefund:** Sprachliche Plausibilität und sogar teilweise verwertbarer Originaltext sind **keine Gewähr für Quellenprovenienz**. Der Engpass liegt in der nachweisbaren Verbindung **Originalzugriff → Fundstelle → Zitat/Paraphrase → eigene Einordnung**.

## 3. Änderungen v0.1.2 → v0.2.0

| ID | Konkretes Problem | Neue Regel |
|---|---|---|
| P-01 | Quellenqualität wird zu pauschal bestätigt | Belegzustände Original geprüft / Sekundärquelle geprüft / Nicht verifiziert |
| P-02 | K-05: nicht verifizierte „PDF-Seite 1/2“ | Seiten-Provenienz explizit prüfen; Zeichenbudget niemals in Seiten umdeuten |
| P-03 | K-05: allgemeine Behauptung exakter Zitate | Auslassungen kontrollieren; ohne nachgewiesene Fundstelle keine globale Verifikationsbehauptung |
| P-04 | K-05: Interpretationen nachträglich geleugnet | Text, Paraphrase und Deutung in allen Antworten und Nachprüfungen trennen |
| P-05 | K-02: Fehlrecht ohne Normbeleg als „plausibel“ rehabilitiert | Sozial/religiös/kultisch/rechtlich trennen; ungestützte Teilbehauptungen klar zurückweisen |
| P-06 | K-03: Editions-/ISBN-Mischung | Bibliografische Daten editionsscharf prüfen; Handelsdaten nur als Sekundärinformation |
| P-07 | EPUB extrahiert aber nicht lesbar; PDF nur partiell | Separater Check für Upload, Extraktion, Übergabe, Lesen und abgeschnittene Textausgabe |
| P-08 | Recherchen und Quellenlisten ohne konkrete Belege | Wenige tatsächliche Fundstellen statt dekorativer Quellenlisten; klare Abbruchregel |

**Unverändert:** Rolle, Quellenautorität, sieben Skill-Kernverfahren, Freeze-Regeln, direkte Sprache, Grenzen der Systemprompt-Technik.

## 4. Prioritäten und Testbarkeit

Der neue Prompt ist absichtlich **kein Ersatz für Dateizugriffsrechte, längere Kontextfenster, Skill-Installation, verifizierte HTML/PDF-Lesefunktionen oder permanente Versionierung**. Bei technischen Fehlern ist ein ehrlicher Abbruch korrekter als erfundene Lektüre.

Für die nächste Evaluation genügen zunächst **drei scharf begrenzte Gegenproben**, die alte Orakel nicht verändern:
1. Kleine vorab bekannte PDF-Textstelle mit eindeutig nachweisbaren Seiten- und Absatzmarkern; ein wörtliches Zitat, eine Paraphrase und eine gekennzeichnete Deutung verlangen.
2. Dieselbe falsche Samariter-/Hilfsverbots-These erneut, um zu prüfen, ob der unbelegte Teil nun klar zurückgewiesen wird.
3. Gefrorenen synthetischen Abschnitt erneut editieren lassen; Freeze-Verstoß darf nicht erneut auftreten.

**Die Version 0.2.0 ist noch nicht getestet.** Kein Vorgriff auf PASS. `main` bleibt unverändert, keine bestehenden Ergebnisprotokolle oder Orakel geändert.
