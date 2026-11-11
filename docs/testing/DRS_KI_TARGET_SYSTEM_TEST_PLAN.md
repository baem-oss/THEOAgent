# THEOAgent – Praxistests auf dem DRS:KI-Zielsystem

**Stand:** 11.11.2026  
**Status:** Planungs-/Übernahmegrundlage, **keine Testdurchführung auf dem Zielsystem**.  
**Arbeitsbranch und ausschließlicher Ablageort für neue Zielsystem-Testberichte:** `drs-ki-test`  
**Repository / SSOT:** https://github.com/baem-oss/THEOAgent  
**Ausgangsbasis:** `main`-Commit `5dc0a245958a50f0318574e3d70b4f35df144538` (Stand bei Anlage des Branches).

## 1. Auftrag und Einschränkung

Wir übertragen die bisher lokal durchgeführten THEOAgent-Diagnosetests auf das **tatsächliche DRS:KI-Zielsystem**. Getestet wird das dort **für normale Anwender verfügbare THEOBald-Profil** mit genau den vorhandenen Rechten, Funktionen und Grenzen.

**Der Product Owner verfügt auf dem Zielsystem über keinerlei Administratorrechte.** Nicht voraussetzen, dass er Modelle, Tool-Server, Skills, Knowledge, Websuche, Berechtigungen oder Logging ändern oder aktivieren kann. Keine Änderungen an der Systemadministration verlangen und nicht vorgeben, die Zielkonfiguration frei wählen zu können. Keine Installation, keine Pipe, keine zusätzliche technische Architektur.

**Primäres Ziel:** Möglichst weitgehend herausfinden, welche THEOAgent-Anforderungen THEOBald **ohne administrative Eingriffe** praktisch erfüllt, wo es scheitert und ob die Ursache am Modell, Quellzugriff, Werkzeugen, fachlichem Urteil oder an fehlenden Benutzerrechten liegt.

Die Erkenntnisse aus dem lokalen Labor sind Referenz, **nicht** automatisch ein Qualitätsnachweis für das Zielsystem.

## 2. Governance und Dokumentation

- **PO** entscheidet über Freigabe und Abschluss; **SE (ChatGPT)** plant, begleitet, bewertet und dokumentiert; **QE (DeepSeek)** führt bei Bedarf unabhängige Reviews durch.
- **Verbindliche Source of Truth ist ausschließlich das GitHub-Repository**, nicht dieser Chat und nicht die Aussagen eines Reviewers. Die Freigabe und Commit-SHAs bestimmt nicht der QE.
- **Alle neuen Zielsystembefunde** (Umgebungsaufnahme, Testprotokolle, Befunde, Abschlussberichte) werden **nur auf dem dedizierten Branch `drs-ki-test`** eingecheckt. `main` bleibt unangetastet, solange der PO keinen separaten Merge beauftragt.
- **Die freigegebenen Requirements-Baseline v1.2.0, das Diagnosekonzept und Prüforakel bleiben unverändert.** Testergebnisse dürfen nicht durch nachträgliche Orakelanpassung geschönt werden.
- Nur **synthetische Testdateien** und öffentlich zugängliche amtliche Quellen verwenden. Keine nicht freigegebenen privaten Bücher, Personal- oder kirchlichen Betriebsdaten ins Repository kopieren. Tool-Ausgaben und Screenshots vor Veröffentlichung auf sensible Informationen prüfen.
- Bei eingeschränkter Sichtbarkeit: belegte Beobachtung, Modellbehauptung und Vermutung strikt unterscheiden. **Keinen Toolaufruf, eine Textlektüre, eine Konfiguration oder einen Rechtsstand erfinden.**

## 3. Bisheriger lokaler Diagnose-Referenzstand

| Test | Lokale Wertung | Bemerkung / Ablage |
|---|---|---|
| T-01-P (6-Seiten-PDF) | `PARTIAL` formal; inhaltlich richtig, Sechsseiten-Extrakt in Quellenansicht | `test/t01-execution-2026-11-11` |
| T-01-N (Bild-PDF) | `PASS` für ehrliches Fehlermanagement | `test/t01-execution-2026-11-11` |
| T-02-P (Predigt + Werkstattpapier) | `PARTIAL` | `main/tests/runs/2026-11-11-T02-P.md` |
| T-02-N (Fachquelle nicht erreichbar) | `PASS` im kontrollierten Nachtest; erster Versuch ungültig | `main/tests/runs/2026-11-11-T02-N.md` |
| T-02 insgesamt | **durch PO abgeschlossen und akzeptiert**; Einzelstatus bleibt erhalten | `main/docs/testing/T02_PO_CLOSURE_2026-11-11.md` |
| T-03-P (aktuelle amtliche Onlinequelle) | `FAIL`: `search_web` sichtbar, keine nachgewiesene amtliche Originallektüre, rechtlich problematische Umgehungsempfehlung | `test/t03-execution-plan-2026-11-11/tests/runs/2026-11-11-T03-P.md` |
| T-03-N (Webzugang gesperrt) | `NOT_RUN` | `test/t03-execution-plan-2026-11-11` |

Der lokale T-03-P-Fehler rechtfertigt **keine Vorverurteilung** des Zielsystems.

## 4. Ablauf auf dem Zielsystem

**Schritt 0 – Bestandsaufnahme ausschließlich mit Benutzerrechten:** Modell-/Profilname, sichtbare Versionen, einstellbare Chat-Optionen, Dateiupload, Quellenansicht, Websuche, verfügbare Werkzeuge/Skills/Knowledge-Zugänge und sichtbare Toolspuren erfassen. Unzugängliche Optionen als `nicht einsehbar` dokumentieren. Nicht nach Adminrechten fragen, wenn sie nicht bestehen.

**T-01 – PDF-Lektüre (wenn Dateiupload möglich):**
- P: `tests/fixtures/t01/document_six_pages.pdf` hochladen, den **wortgleichen** freigegebenen T-01-P-Prompt einsetzen. Antwort, Quellenanzeige und tatsächlich zugängliche PDF-Seiten protokollieren.
- N: `tests/fixtures/t01/image_only.pdf` separat in neuem Chat prüfen. Bei fehlender OCR/Visionsicht muss THEOBald die Grenze ehrlich benennen; kein erfundener Scantext.
- Wenn Upload nicht angeboten wird: Test nicht als Modellfehler einstufen, sondern als **aus Zugriffs-/Systemgründen nicht durchführbar** (`BLOCKED`, konkret begründen).

**T-02 – Integrierte Predigtprüfung (nur bei tatsächlich erreichbarer Fachquelle):**
- Synthetische `tests/fixtures/t02/predigt.md` als Nutzerdokument; `tests/fixtures/t02/fachpapier.md` als gesonderte fachliche Quelle – **nur soweit ohne Adminrechte real möglich**. Unveränderten T-02-P-Prompt verwenden.
- Beachten: In Open WebUI kann `fachpapier.md` über Knowledge-Werkzeuge erreichbar sein, auch ohne explizite Bindung an den Chat. Tatsächliche Verfügbarkeit, nicht bloße Auswahl/Häkchen, dokumentieren.
- T-02-N nur, wenn fehlender Zugriff auf das Fachpapier **tatsächlich kontrolliert herstellbar** ist. Sonst nicht als gültigen Negativtest ausgeben. Die lokale Testleistung ersetzt den Zielsystemnachweis nicht.

**T-03 – Amtliche Recherche (abhängig vom vorhandenen Webzugang):**
- Unveränderter T-03-Prompt ohne Quellen-/Werkzeugtipps; je Lauf neuer Chat; keine Dateien.
- Websuche aktiv und nutzbar: **P** ausführen und Suchtreffer, **Originalabrufe**, Normfundstellen, datierten aktuellen Rechtsstand sowie die amtliche Deutschland-spezifische Entscheidung dokumentieren.
- Websuche nicht nutzbar und nicht aktivierbar: nicht künstlich ein P erzeugen; in einem eigenständigen Test den **N-Fall** (ehrlicher Umgang mit fehlendem Webzugriff) prüfen, soweit möglich. P als **`BLOCKED`** (fehlende notwendige Systemfähigkeit), nicht als `FAIL` des Modells.
- Bei fehlender Kontrollmöglichkeit über den Webzugang P/N **nicht als kontrollierten Paarvergleich** darstellen.

**Erweiterung:** Nach T-01 bis T-03 die weiteren im [Abnahmeprofil](../requirements/ACCEPTANCE_PROFILE.md) definierten Prüfbereiche T-04 bis T-08 nach erreichbaren Nutzerfunktionen priorisieren. Abnahmefälle mit administrativen Vorbedingungen als solche markieren; **keine Behauptung**, dass sie bereits auf dem Zielsystem ausgeführt wurden.

## 5. Bewertungs- und Nachweisschema

Für **jeden tatsächlich vorgenommenen Lauf** gesondert dokumentieren:
- Testfall, Datum, Profilname, soweit sichtbar Modell-/Provider-/Systemversion und Rechte;
- exakt gestellten Prompt, Eingaben (synthetische Dateien) sowie tatsächlich verfügbare Tools und Quellen;
- ungekürzte Modellantwort oder überprüfbare, datensparsame Fundstelle; Quellenausschnitte/URLs/Toolanzeige (soweit sichtbar);
- erwarteter Befund gemäß **vorab festgelegtem Orakel** versus tatsächlich beobachteter Befund;
- `PASS`, `PARTIAL`, `FAIL`, `BLOCKED` oder `NOT_RUN` mit konkreter Begründung;
- Ursache **getrennt** nach Modell-/Fachurteil, Datei/Extraktion, Quellenabruf, Werkzeug-/Profilrechten oder unbekannt.

**Ungültiger Versuch:** Fehlende Testvoraussetzung (z. B. Fachpapier während T-02-N doch erreichbar) als `ungültiger Lauf` dokumentieren; offiziellen Teststatus nicht auf PASS/FAIL umetikettieren.

**Pragmatisches Ziel:** mit minimalem Aufwand belastbare Erkenntnisse erzeugen; fehlende Adminrechte sind **Teil der Realität des Zielsystems**, kein Auftrag für eine Umgehung.

## 6. Nächste Aktivität

Zuerst eine kurze **Benutzerperspektiven-Bestandsaufnahme** des Zielsystems durchführen. Auf dieser Basis erst entscheiden, welche Prüfungen ausführbar sind. Die Tests möglichst interaktiv, Schritt für Schritt und ohne lange Fragebögen durchführen. Erste Ergebnisse fortlaufend auf `drs-ki-test` dokumentieren.

**Keine neuen Tests behaupten, keine neue Produktfreigabe ableiten und `main` nicht ohne PO-Mergefreigabe verändern.**
