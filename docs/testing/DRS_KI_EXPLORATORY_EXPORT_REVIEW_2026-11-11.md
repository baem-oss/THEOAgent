# DRS:KI – Explorative Beobachtungen aus einem Chat-Export (11.11.2026)

**Status:** Explorative Sichtung, **keine formale Ausführung/Abnahme** nach dem fixierten Testplan.  
**System:** DRS:KI (Open WebUI), sichtbare Chatbezeichnung „Allrounder“; effektive Modell-ID, Provider und Konfiguration nicht verifiziert.  
**Evidenz:** Vom PO bereitgestellter, gekürzter/aufbereiteter Textexport der Benutzerinteraktion; der vollständige Export wird wegen möglicher personenbezogener bzw. nicht synthetischer Inhalte **nicht** in das öffentliche Repository übernommen.  
**Maßstab:** Requirements-Baseline v1.2.0, `docs/testing/T01-T03_DIAGNOSTIC_PLAN.md`, `tests/oracles/T01-T03_ORACLES.md`. Orakel unverändert.

## Methodische Einschränkungen
- Testplan, Requirements-Text und einzelne Testanweisungen standen bereits im Chatkontext. Keine isolierten frischen Chats pro Test nachgewiesen.
- Kontrollierte Websuche-Deaktivierung für T-01/T-02 wurde vom Assistenten behauptet, aber nicht durch UI-/Systembefund nachgewiesen.
- Datei- und Werkzeugzugriffe sind nur punktuell sichtbar. Modellbehauptungen („gelesen“, „deaktiviert“) sind kein selbstständiger Nachweis.
- Selbstbewertungen des Testkandidaten sind **nicht** die SE-Bewertung.
- Folglich **keine** dieser Beobachtungen als formales PASS/FAIL des kontrollierten Abnahmeverfahrens übernehmen. Fachlich festgestellte Fehler als explorative Findings erfassen.

## Beobachtete Fälle

| Fall | Selbstaussage DRS | Explorative SE-Einschätzung | Formale Einstufung |
|---|---|---|---|
| T-01-P | PASS | **Inhaltlich fehlgeschlagen**: DRS nennt REG-2026-001, 15.03.2026 / Blau und VERTRAULICH2026; das fixierte Orakel verlangt KELCH-29, 22.04.2032 / violett, dreifache Sichtung und FIRN-46. Keine belegte Extraktion. | Ungültiger/nicht kontrollierter Lauf; wiederholen |
| T-01-N | PASS | Grenze für bildbasierte PDF ehrlich benannt, kein erfundener Scantext; kein OCR-/Bildzugriff unabhängig belegt. | Positiver Teilbefund; kontrolliert wiederholen |
| T-02-P | PASS | P2 und P3 als problematisch erkannt. Angebliche Beschreibung von Fachpapier A/B entspricht nicht dem fixierten Orakel; die kontextentscheidende Einschränkung B fehlt. Kein belastbarer Nachweis beider Originallektüren. | Ungültiger/nicht kontrollierter Lauf; wiederholen |
| T-02-N | PASS | Negativbedingung nicht kontrolliert: Verlauf zeigt auch Bereitstellung von `fachpapier.md`; zugleich behauptete Nichtverfügbarkeit. | Ungültiger Lauf; kein PASS |
| T-03-P | Inhaltlich eindeutige Verneinung | Sichtbar ist `get_websearch_results`. Fachliche Kernaussage weitgehend plausibel, aber zitierte Belege sind journalistische Sekundärquellen statt amtlich nachgewiesener Originallektüre; keine verifizierte genaue Fundstelle im vatikanischen Schreiben vom 17.06.2026. | Explorativ PARTIAL; **kein** formales PASS |
| T-03-N | – | Nicht beobachtet. | NOT_RUN |

## Weitere relevante Beobachtungen
1. Der Assistent behauptete in einer Selbsteinschätzung pauschal 100 % Erfüllung sämtlicher fachlicher, funktionaler, nichtfunktionaler und Sicherheitsanforderungen, ohne Akzeptanzprüfungen. **Nicht belastbar.**
2. In der Umgebungsaufnahme widersprach er der sichtbaren Open-WebUI-Oberfläche („Open WebUI nicht aktiv“) und behauptete, Websuche sei deaktiviert, weil sie nicht standardmäßig aufgerufen werde. **Nicht verifiziert und logisch unzutreffend.**
3. Frühere bibliografische Aussagen zu Wolfgang Klippert enthielten präzise Verlag-/ISBN-/Fundstellenbehauptungen ohne sichtbaren tatsächlichen Bibliografieabruf. **Überprüfungsbedarf; hier keine eigenständige bibliografische Verifikation.**
4. UI-Sicht des PO: Keine Modell-/Profilauswahl, keine eigenen Projekte/Workspace; Eingabefeld für Standard-Systemprompt; Datei-Uploadmenü sichtbar. Rechte und effektive Hintergrundeinstellungen bleiben unbekannt.
5. Der Export bezeichnet den Chatassistenten sichtbar als **„Allrounder“**, nicht als verifizierten THEOBald-Konfigurationsstand. Eine Gleichsetzung mit dem lokalen THEOBald ist unzulässig.

## Vorgehen
- Bestehenden Standard-Systemprompt unverändert lassen; keine Konfiguration ohne Nachweis ändern.
- **T-01-P zuerst** als kontrollierten Neustart in einem frischen DRS-Chat mit ausschließlich der festgelegten synthetischen PDF und dem wortgleichen Prompt durchführen. Kein Testplan, Orakel oder GitHub-Link in den Modellkontext.
- Vollständige Antwort und tatsächlich sichtbare Datei-/Quellenanzeige sichern, ohne sensible Daten öffentlich abzulegen.
- Danach erst den nächsten Fall mit PO-Aufforderung beginnen.
- `main`, Requirements und Orakel bleiben unverändert.
