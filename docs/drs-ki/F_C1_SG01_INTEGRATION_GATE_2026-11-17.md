# F-C1 – SG-01: Integrationsgate für technisch erzwungene Quellenprüfung

**Stand:** 17.11.2026  
**Branch:** `drs-ki-test`  
**Status:** Technische Analyse und gezielte Machbarkeitsklärung; **F-C1 CRITICAL / OPEN**. Keine PO-Freigabe, kein DEV-Livenachweis für eine Pipe.

## Ausgangslage und gesicherte Befunde

- [QE-Review F-C1](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md): Promptklassifikation garantiert keine tatsächlich ausgeführte Quellenprüfung; die technische Durchsetzung fehlt.
- [AK-01](ARCHITEKTURKORREKTUR_AK-01_F-C1.md): SG-01/SG-02 sind zuerst zu prüfen; ohne Integration keine technisch verifizierende Modellbereitstellung.
- [T-1](T1_KLIPPERT_SOURCEGUARD_PRAXISBEFUND_2026-11-14.md): Das Modell präsentierte ein simuliertes JSON-Ergebnis als SourceGuard-Werkzeugnachweis; der echte Aufruf erfolgte erst nach Nutzereingriff.
- SourceGuard 0.2.x als **normales OpenWebUI-Tool** kann Webquellen selbst abrufen und Auszüge verarbeiten, aber weder alle Aufrufe erzwingen noch vom Modell vorgelegte Knowledge-Auszüge unabhängig authentifizieren oder den endgültigen Antworttext sperren.
- Nach bisheriger PO-Angabe besitzt der Nutzer Developerzugriff auf DRS:KI DEV, aber keine Adminrechte; das Functions-Panel war für ihn nicht erreichbar. **Nicht nachgewiesen** ist, ob ein Administrator eine Pipe/Function im Auftrag bereitstellen und dem Modell zuweisen kann. Aus fehlendem UI-Zugriff darf nicht auf die generelle Unmöglichkeit serverseitiger Integration geschlossen werden.

## Zielzustand (nur Architekturhypothese, noch keine Implementierung)

Eine vertrauenswürdige, außerhalb des Modellausgabetextes laufende Kontrollinstanz verknüpft Behauptungen und Quellenbelege mit **tatsächlichen** Lese-/Tool-Ereignissen und unterbindet unzulässige Ausgaben mit dem Status „originalgeprüft“, wenn die erforderlichen Nachweise fehlen. Sie bewertet außerdem technische Fundstellenbezüge. Eine solche Instanz darf **semantische Gültigkeit** nicht allein aus Texttreffern behaupten; fachliche Bewertung und Originallektüre bleiben eigenständig zu prüfen.

## Einziger nächster Gate-Test: SG-01

**Zu klärende Frage an den DRS:KI-Betrieb / Administrator:**

> Kann in DRS:KI DEV eine von uns bereitgestellte OpenWebUI-Pipe (oder gleichwertige serverseitige Kontrollkomponente) durch einen Administrator testweise installiert, dem bestehenden THEOAgent-DEV-Modell zugewiesen und so betrieben werden, dass jeder Endnutzeraufruf über diese Kontrollinstanz läuft und diese vor der Ausgabe eingreifen kann? Falls nein: Welche vorhandene, administrativ zulässige Alternative kann die Antwortausgabe verbindlich kontrollieren?

**Nachweis als PASS:** Ein erlaubter, nachweislich aktiver Test-Interceptor kann bei einem Aufruf des bereitgestellten DEV-Modells eine festgelegte Testausgabe unterbinden oder markieren; beobachtetes Log/Artefakt und Modellbindung werden protokolliert.

**FAIL:** Der DRS:KI-Betrieb bestätigt, dass weder Pipe noch gleichwertiges serverseitiges Gate für das Modell eingebunden werden dürfen/können.

**NICHT GEPRÜFT:** Nur Entwickler-Menüs fehlen oder es liegt keine verbindliche Aussage und kein tatsächlicher Funktionstest vor.

## Nach SG-01

- **PASS:** SG-02 prüfen (tatsächliche Tool-Callables/Ereignisse); bestehende SourceGuard-Pipe als Referenz prüfen, keinen Neuaufbau vor Kompatibilitätsklärung. Danach eine kleine Negativprobe ohne Leseevent: keinerlei „originalgeprüft“ trotz Modellbehauptung.
- **FAIL:** F-C1 bleibt offen. DEV nur als nicht technisch quellenverifizierender Erkundungsbetrieb; das ist keine Absenkung von NFANF-13/GR-02 und keine Produktfreigabe. PO entscheidet über weiteren Architekturweg.
- **NICHT GEPRÜFT:** Keine neue Pipe, keine behauptete technische Garantie. Erst eine belastbare Betriebsantwort einholen.

## Änderungsgrenzen

Keine Änderung an `main`, Requirements v1.2.0, historischem QE-Review, dem funktionierenden SourceGuard-Tool oder dem aktuellen Systemprompt. Diese Notiz ist eine technische Gate-Vorbereitung, **kein implementierter Fix**.

## DEV-Workaround mit Nutzerprüfung (PO-Entscheidung 17.11.2026)

**Entscheidung:** Bis eine technische Antwortkontrolle verfügbar und nachgewiesen ist, soll THEOAgent bei Antworten mit konkreten Quellen, Zitaten oder Fundstellen einen kurzen, für Laien verständlichen Hinweis zur eigenständigen Quellenprüfung durch den Nutzer ausgeben. Der Nutzer kann sich die Originalquelle zeigen lassen und die entscheidende Textstelle selbst mit der Aussage vergleichen.

**Umsetzung:** [Systemprompt v0.3.9](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.9.md), Abschnitt 4.1. Keine Änderung an den Quellenprüfungs-Skills oder am SourceGuard-Werkzeug. Der Hinweis wird bei reinen Textentwürfen ohne Quellenbezug nicht ausgegeben.

**Abnahme der Hinweispflicht (minimaler DEV-Test):** Eine quellenbezogene Antwort (z. B. zu Dei Verbum 12) muss den verständlichen Hinweis tatsächlich enthalten. Eine Antwort ohne Quellenbezug darf ihn nicht enthalten. Eine anschließende Nutzerfrage nach der Originalstelle darf keine vorgetäuschten Toolaufrufe oder unbelegten Verifikationsbehauptungen erzeugen. Aus sichtbaren Modelltexten allein folgt kein technischer Aufrufnachweis.

**Grenze:** Der Workaround senkt nicht NFANF-13 oder GR-02 ab, behebt F-C1 nicht technisch und erlaubt keine Produktiv-/Quellenverifikationsfreigabe. SG-01 und SG-02 bleiben offen; der Nachweis einer serverseitigen Durchsetzung kann separat verfolgt werden.
