# T-04 – Variante B: nutzerseitige direkte Werkzeugsteuerung

**Stand:** 12.11.2026 · **Branch:** `drs-ki-test` · **Gesamtstatus:** **FAIL – 6/8** bei erfolgreicher sichtbarer Dokumentenlektüre.

## Testaufbau

Der PO übermittelte den DRS:KI-Allrounder-Chat „Prüfung von Fachbehauptungen“ mit einem Anhang `belegkorpus.md` (2,9 KB). Nutzerseitig wurde **vor** den acht unveränderten T-04-Behauptungen eingefügt:

> Lies die beigefügte Datei `belegkorpus.md` zuerst mit dem Werkzeug `view_knowledge_file`. Verwende für diese Lektüre nicht `analyze_uploaded_documents`.

Danach folgte der ursprüngliche T-04-Auftrag mit acht Behauptungen, ohne inhaltliche Änderung. Es handelt sich um **eine diagnostische Promptvariante**, nicht um eine exakte Wiederholung des fixierten T-04-Nutzerprompts. Laut vorausgehender Planung sollte der Systemprompt **v0.2.3** verwendet werden; seine tatsächliche aktive Einbringung wurde im übermittelten Verlauf **nicht unabhängig verifiziert**.

**Sichtbarer erster Werkzeugaufruf:** „Ergebnis von `view_knowledge_file` ansehen“. Ein vorheriger Aufruf von `analyze_uploaded_documents` ist nicht sichtbar. Das Tool-Rohpayload und die Datei-ID liegen nicht vor.

## Antwort / Soll-Ist

| Nr. | Orakel | Antwort | Bewertung |
|---|---|---|---|
| 1 | belegt | belegt, § 2.1 | PASS |
| 2 | widerlegt | widerlegt, § 2.2 | PASS |
| 3 | widerlegt | widerlegt, § 3.2 | PASS |
| 4 | belegt | belegt, § 4.1 | PASS |
| 5 | **widerlegt** | **nicht überprüfbar**, obwohl ausdrücklich auf das Fehlen empirischer Befunde hingewiesen wird | **FAIL** |
| 6 | nicht überprüfbar | nicht überprüfbar, externes Werk nicht enthalten | PASS |
| 7 | **widerlegt** | **belegt**, obwohl zutreffend auf § 4.1 statt behauptetem § 3.1 hingewiesen wird | **FAIL** |
| 8 | widerlegt | widerlegt, § 4.2 | PASS |

Die Fundstellenbezüge und inhaltlichen Zusammenfassungen sind überwiegend korrekt. **Zwei Klassifikationen sind nach dem unveränderten Orakel falsch**.

## Auffällige Befunde

**F-05 – Schlussfolgerungsfehler:** Bei Behauptung 5 erkennt der Testling korrekt: Die bloße Nennung „Digitale Predigtformen“ belegt keine empirischen Wirksamkeitsnachweise, und der Korpus schließt solche Befunde in § 5 ausdrücklich aus. Trotzdem lautet seine Klassifikation `nicht überprüfbar` statt `widerlegt`.

**F-07 – Quellenzuordnungsfehler:** Bei Behauptung 7 erkennt der Testling den Satz wörtlich in § 4.1 und stellt ausdrücklich fest, dass die Nutzerzuordnung zu § 3.1 falsch ist. Dennoch lautet die Klassifikation `belegt` statt `widerlegt`.

**Werkzeugverhalten:** Der nutzerseitige Hinweis führte in diesem Lauf direkt zum sichtbaren Einsatz von `view_knowledge_file`. Damit ist ein praktisch möglicher Workaround belegt, **nicht** dessen Reproduzierbarkeit über mehrere Läufe oder die Kausalwirkung allein des Nutzersatzes.

## Vergleich

| Lauf | Werkzeug | Fachstatus |
|---|---|---|
| T-04-R1 (v0.2.2) | `view_knowledge_file` direkt | FAIL, 6/8 (Nr. 5, 7) |
| T-04-R2 (v0.2.3) | `analyze_uploaded_documents` | BLOCKED |
| T-04-R2-D1 nach Intervention | `view_knowledge_file` | PASS, 8/8 |
| Variante A (planmäßig v0.2.3) | `analyze_uploaded_documents` | BLOCKED |
| **Variante B (planmäßig v0.2.3)** | **`view_knowledge_file` direkt** | **FAIL, 6/8 (Nr. 5, 7)** |

## Schlussfolgerung und Grenzen

**Zwei getrennte Grenzen:** Der Standard-Werkzeugweg ist unzuverlässig; ein expliziter Nutzerhinweis war hier erfolgreich. Die Klassifikation vollständiger Behauptungen bleibt selbst bei offenbar erfolgreicher Originallektüre instabil, besonders bei falschen Fundstellen und ausdrücklich widerlegten Inhaltsbehauptungen.

Die Testvarianten unterscheiden sich im Nutzerprompt. Promptrollen, Modell-/Backendversion, Tool-Schema und verborgene Kontextfaktoren sind nicht vollständig dokumentiert. **Keine kausale Zuschreibung** und keine Änderung des fixierten Orakels. Der Test belegt nur die konkrete beobachtete Ausführung.

**SSOT:** `drs-ki-test`; `main`, Promptdateien, Testfixture und Orakel unverändert.
