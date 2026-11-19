# DRS:KI – Findings-Disposition und P0-Machbarkeit

**Stand:** 13.11.2026  
**Status:** Arbeitsvorschlag nach QE-Review, keine PO-Freigabe  
**Reviewbasis:** [QE-Architektur-Review](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md)  
**Requirements:** [Baseline v1.2.0](../requirements/BASELINE.md)
**Klarstellung zum Zielsystem (PO, 13.11.2026):** Erprobung und Integration erfolgen auf **DRS:KI DEV** mit **Developerzugriff**. Der spätere **Endnutzer kann ausschließlich das bereitgestellte Modell aufrufen**; eigene Tool-/Pipe-/Skill-Konfiguration durch Endnutzer ist **nicht vorgesehen**. Developerzugriff bedeutet nicht automatisch Administrations- oder Installationsrecht; konkrete Funktionsrechte werden entwicklungsseitig geprüft.

## 1. Findings-Disposition

| Finding | Behandlung | Entscheidung / Nachweisbedarf |
|---|---|---|
| F-C1 **kritisch** | akzeptiert | Promptklassifikation **ersetzt keine** technisch erzwungene Quellenprüfung. SourceGuard-Integration nachweisen oder Verifikationsanspruch ausdrücklich ausschließen. |
| F-C2 wesentlich | akzeptiert | Toolnamen, Aufrufbarkeit und Rückgabeformate auf DRS:KI mit dem tatsächlichen SourceGuard-Vertrag vergleichen. |
| F-C3 wesentlich | teilweise akzeptiert / Klärung | DIE SSOT für **THEOAgent** ist dieses Repository. THEOBald bleibt separate Code-/Prototypreferenz. 90-%-Pragmatik gilt nicht als Absenkung zwingender Belegintegrität. PO bestätigt die Interpretation bei Architekturfreigabe. |
| F-C4 wesentlich | überholt für Zielrepo | Branch `drs-ki-test` **existiert in THEOAgent**. QE-F-C4 betraf das andere Repository THEOBald. Kein nachträgliches Ändern des historischen QE-Berichts. |
| F-C5 wesentlich | akzeptiert | Single Domain nicht als verifizierende Quelle einsetzen, solange Redirect-SSRF nicht behoben ist. |
| F-C6 wesentlich | akzeptiert | Nutzungsrechte, Bibelübersetzung und externe Provider-/Datenflüsse als Gate vor Test mit nichtöffentlichen Daten. |
| F-C7 wesentlich | präzisiert / P0 | Developerzugriff auf DEV ist gegeben; nur die konkret benötigten Developer-/Deployment-Befugnisse und die spätere Endnutzer-Nutzbarkeit des veröffentlichten Modells überprüfen. Keine Prüfung von Endnutzer-Administrationsrechten. |
| F-A1–A10 | zur Nachprüfung vermerkt | Technische Befunde gelten als statische QE-Findings; keine Behauptung tatsächlicher Exploit-/Fehlerraten. |
| F-B1–B2 | akzeptiert | DRS:KI-Quellcode nur als Reviewbeleg; Drittcode nicht ungeprüft übernehmen. Verfügbarkeit der Dependencies im Ziel prüfen. |
| F-X1 | offen | Original-ZIP/Manifest wurden vom QE nicht unabhängig gehasht. Repository-Git-Objekte sind neuer Ablagestand, nicht automatisch byteidentisch mit den externen Uploads. |

Die vollständige Begründung und Originalklassifikation stehen allein im unveränderten QE-Bericht.

## 2. P0-Gates – in dieser Reihenfolge

**P0-A – DEV-Integration:** Mit dem **Developerkonto auf DRS:KI DEV** die tatsächlich verfügbaren Entwicklungs-/Konfigurationsmöglichkeiten für Modellprofil, Systemprompt, Knowledge, Skills, Tool-Zuweisungen und Pipes/Functions prüfen und dokumentieren. Nur nötige Rechte prüfen; **keine Untersuchung von Endnutzer-Konfigurationsrechten**. Außerdem klären, wie ein entwickeltes Modell für Endnutzer bereitgestellt wird und ob es alle gebundenen Werkzeuge mitnutzt. Keine pauschalen Adminrechte unterstellen.

**P0-B – Tools tatsächlich aufrufen:** Einfache risikoarme Abfragen an Faster–No Summary, Outline, MediaWiki und vorhandene Bibel-/TYPO3-Werkzeuge ausführen. Pro Aufruf Modell, Toolname, Eingabe, Rückgabeformat, Fehlerzustand, Kürzung und Source-Type dokumentieren. Keine erfundene Aufrufbarkeit.

**P0-C – SourceGuard-Kompatibilität:** Unter Developerzugriff abgleichen, ob die bestehende SourceGuard-Pipe auf DEV technisch verfügbar bzw. integrierbar ist und welche `__tools__`-Callables bzw. Adapter sie erhielte. Wenn das nicht geht: keine Aussage `TECHNISCH_VERIFIZIERT`.

**P0-D – Quellenevidenz:** Vier bekannte Fälle über das auf DEV konfigurierte Modell **aus Endnutzersicht (nur Modellaufruf, keine Konfigurationsrechte)** prüfen: (1) Dei Verbum 12; (2) KKK 2267; (3) Lk 10,25–37; (4) eine gezielt nicht im bereitgestellten Text enthaltene Fundstelle. Belegkette von Treffer über Originalauszug bis zur nachprüfbaren Fundstelle getrennt protokollieren. Keine Snippets als Originallektüre ausgeben.

**P0-E – Sicherheits-/Rechte-Gates:** Single-Domain Redirect-Finding F-A1 vor Belegverwendung beheben oder ausschließen. Rechte/Fassungen (insb. Einheitsübersetzung 2016), Urheberrechte, Datenklassifikation und externe Modellprovider vor nichtöffentlicher Verarbeitung klären.

## 3. Mögliche Betriebskategorien (noch keine Freigabe)

- **Erkundung:** vorhandene Tools für Treffer und Ausschnitte, klar gekennzeichnet; keine technische Belegverifikation behaupten.
- **Verifizierender Betrieb:** nur nach erwiesenem technischen Prüfschritt, SourceGuard-Adaptertest, Anforderungenabgleich und PO-Freigabe.

## 4. Exit-Kriterien für P0

Ein schriftlicher Testbericht nennt für jedes Gate `PASS`, `FAIL` oder `NICHT GEPRÜFT`, verknüpft die DRS:KI-UI-Belege und beantwortet:
1. Welche verfügbaren Tools liefern Originaltext und Fundstellen?
2. Welche DEV-Konfiguration/Integration ist mit Developerrechten nachweisbar, und wie erfolgt die Bereitstellung des fertigen Modells?
3. Ist die bestehende SourceGuard-Durchsetzung technisch einbindbar?
4. Welche Anforderungen bleiben offen, verletzt oder nur promptgesteuert?
5. Welche minimale Architektur ist auf **DRS:KI DEV** nachgewiesenermaßen machbar und kann Endnutzern als **reiner Modellaufruf** bereitgestellt werden?

Ein Architektur-Freeze oder ein Merge in `main` erfolgt erst nach gesonderter PO-Entscheidung.
