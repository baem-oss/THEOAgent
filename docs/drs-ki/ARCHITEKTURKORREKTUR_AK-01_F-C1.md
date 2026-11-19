# Architekturkorrektur AK-01 – QE-Finding F-C1

**Projekt:** THEOAgent / DRS:KI  
**Datum:** 13.11.2026  
**Branch:** `drs-ki-test`  
**Status:** Technische Findings-Disposition und Architekturkorrektur zur PO-Prüfung; **keine** Produktfreigabe  
**PO-Klarstellung 13.11.2026:** Integration auf **DRS:KI DEV mit Developerzugriff**; Endnutzer hat ausschließlich Zugriff auf das bereitgestellte Modell. Ob der Developer konkret Pipes/Functions integrieren darf, ist gesondert festzustellen.  
**Referenzen:** [Requirements v1.2.0](../requirements/BASELINE.md), [QE-Review](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md), [historischer Entwurf](ARCHITEKTURVORSCHLAG_2026-11-13.md)

## 1. Festgestellter Fehler

Der historische DRS:KI-Architekturentwurf sieht als eigene THEOBald-Komponente eine zunächst promptgesteuerte Einordnung in `TREFFER`, `AUSZUG`, `ORIGINALTEXT_GEPRUEFT`, `NICHT_BELEGT` vor. Diese Einordnung kann **nicht als technisch durchgesetzte Quellenverifikation** gelten. Eine sichtbare Passage plus Fundstelle und ein Modellurteil belegen noch keine garantiert tatsächlich ausgeführte, zur Aussage passende Originallektüre.

**Finding F-C1: akzeptiert.** Die entsprechende Passage des ursprünglichen Architekturentwurfs ist **für die weitere Planung verworfen**. Der historische Entwurf bleibt als Reviewgegenstand unverändert erhalten; dieses Dokument ist die Korrektur.

## 2. Verbindliche Baseline

- `FANF-05`: Einschlägige Originalpassage einschließlich der für die Aussage relevanten Bedingungen und Gegenpositionen im Textzusammenhang lesen.
- `FANF-07/08`: konkrete überprüfbare Fundstelle und Prüfung der Übereinstimmung mit der belegten Aussage.
- `GR-02`: Suchtreffer, Inhaltsverzeichnisse und Metadaten sind kein Originallektürenachweis.
- `GR-03`: Exakte Zitate und spezifische Locatoren erst nach Verifikation.
- `NFANF-13`: Im festgelegten Abnahmekorpus null irrtümlich als überprüft/verifiziert ausgegebene, nicht geprüfte oder falsch zugeordnete Belege; **keine** Garantie allgemeiner Fehlerfreiheit.
- `DAT-02`: Seiten-, Absatz- und Werk-Locatoren nicht verwechseln.
- `SP-02/03`: Fremdtext darf keine vorrangigen Anweisungen erzeugen; externe Abrufe müssen sichere Ziele und Redirects gewährleisten.

## 3. Korrigierte Komponentenentscheidung

**Referenzimplementierung:** bestehender `sourceguard/sourceguard.py` v0.5.5-dev3 im THEOBald-Branch `review/sourceguard-integrated-v0.5.5-dev3`, **kein** freigegebenes Release. Die Statusdokumentation vom 10.11.2026 nennt 259 bestandene CI-Tests und neun übersprungene PDF-Tests; ein integrierter Agenten-R01-Livetest ist nicht erfolgreich belegt.

**Betrieb A – Erkundung ohne SourceGuard:** vorhandene DRS:KI-Werkzeuge dürfen für Treffer, Snippets und ausgelesene Textausschnitte nur innerhalb ihrer nachgewiesenen Zugriffsrechte verwendet werden. Das Modell darf diese Ergebnisse fachlich besprechen; seine Quellenklassifikation ist aber **nicht technisch erzwungen**. Ein entsprechender Prompt ist nur Risikominderung, keine Verifikationssperre. Der Pilot ist nicht als quellenverifizierend freigegeben.

**Betrieb B – technisch prüfender Assistent:** erst erwägen, wenn eine auf DRS:KI zulässige und ausführbare SourceGuard-Durchsetzung einschließlich tatsächlicher Tool-Callables, Adapter, Belegprotokoll und Negativtests nachgewiesen ist. Sie darf weder aus der Existenz eines Menüpunkts noch aus statischem Code abgeleitet werden. SourceGuard-Release-/Abnahmebedingungen bleiben offen.

**Nicht beschlossen:** Neue Pipe installieren, neuen SourceGuard entwickeln, Requirements absenken oder bestehende DRS:KI-Werkzeuge verändern.

## 4. Offene technische Fragen / Gates

| Gate | Nachweis | Status |
|---|---|---|
| SG-01 | Kann der Developer auf DRS:KI DEV eine Pipe/Function entwickeln, integrieren und dem Endnutzermodell zuweisen? | NICHT GEPRÜFT |
| SG-02 | Erhält die Pipe die benötigten `__tools__`-Callables? Welche Namen/Formate? | NICHT GEPRÜFT |
| SG-03 | Können DRS:KI-Faster/Outline/Bibel/MediaWiki/TYPO3 die für SourceGuard benötigten Original-Leseevents bereitstellen? | NICHT GEPRÜFT |
| SG-04 | Wird bei 0 Leseevents sowie bei Snippet/Fehlabruf ein Verifikationsanspruch tatsächlich unterbunden? | NICHT GEPRÜFT |
| SG-05 | Sind Berechtigungen, Lizenzen, Datenflüsse und Netzwerksicherheit ausreichend geklärt? | NICHT GEPRÜFT |
| SG-06 | Bestehender SourceGuard besteht passenden Live-, Positiv- und Negativkorpus auf DRS:KI | NICHT GEPRÜFT |

**Gates zuerst:** SG-01 und SG-02. Ein negativer Befund zur **DEV-Integration** verhindert die geplante technisch verifizierende Modellbereitstellung; die fachlich klar begrenzte Erkundung auf DEV bleibt möglich.

## 5. Abnahme und Nachweis

Das Finding wird als **architektonisch dispositioniert**, nicht als technisch behoben gewertet. Technische Umsetzung und funktionale Abnahme bleiben offen. Kein Merge nach `main`, keine Änderung der PO-freigegebenen Requirements durch diese Korrektur.

**Nachfolge:** [P0-Machbarkeit und übrige Findings](P0_MACHBARKEIT_UND_FINDINGS.md), danach nachgewiesene DRS:KI-Toolschnittstellen und mögliche Wiederverwendung der bestehenden Pipe evaluieren.
