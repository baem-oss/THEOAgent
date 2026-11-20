# THEOAgent – Weiterentwicklungsplan und vollständiger QE-Reviewauftrag (Entwurf)

**Stand:** 20.11.2026  
**Status:** Überarbeiteter SE-Vorschlag **nach QE-Review**; zur PO-Disposition, **keine** Entwicklungsbaseline, technische Abnahme oder Produktivfreigabe. Die ursprüngliche QE-Prüffassung bleibt als separates Dokument erhalten.  
**SSOT:** [baem-oss/THEOAgent](https://github.com/baem-oss/THEOAgent). Prüfbasis: `drs-ki-test` @ `1e959394f176370247420cb86bab76fb2c1e7ec3`; `main` war bei der Nachprüfung @ `ebb710206d8851dcb04331f3e87cb9ca1426d72b` (Merge 19.11.2026). Der DEV-Stand ist bereits teilweise in `main` integriert; **Änderungen an `main` dennoch nur nach neuer ausdrücklicher PO-Freigabe**. Neue Arbeit zunächst auf `drs-ki-test`; Dokumentverweise stets branch-/commitbezogen interpretieren.  
**Auftraggeber/Entscheidung:** PO; **Umsetzung:** SE; **QE:** unabhängiger Reviewer ohne Freigabe-, Commit-SHA- oder Repository-Hoheit.

## 1. Was der QE vor seiner Beurteilung lesen muss

Dies ist **kein isolierter Verbesserungsprompt**, sondern eine Review-Übergabe. Unterscheide dokumentierte Praxisbeobachtung, Baseline-Anforderung, historische QE-Einschätzung, Hypothese und Live-Nachweis.

### Verbindliche Grundlagen
1. [Requirements v1.2.0](../requirements/BASELINE.md) – PO-freigegeben; alle MUSS-Anforderungen gelten weiter, insbesondere FANF-05, FANF-07–09, NFANF-12/13, GR-02/03, Schutzanforderungen.
2. [Abnahmeprofil v1.2.0](../requirements/ACCEPTANCE_PROFILE.md) und [Traceability](../requirements/TRACEABILITY.md) – Testkriterien T-01–T-08. **PO-gewichteter Praxis-PASS ist keine formale End-to-End-Abnahme**.
3. [Projektworkflow](../WORKFLOW.md) und [DRS:KI-Projektstatus](README.md) – Branch-/Freigabegrenzen, Rechte und Zielumgebung. **Achtung:** Der README enthält historisch überholte Freeze-/Branch-Aussagen; tatsächliche Branches und Commitstände aus GitHub haben Vorrang.
4. [THEOBald-Fachstandard](../requirements/THEOBald_Fachstandard.md) – nicht eigenmächtig verändern.

### Aktuelle Praxisevidenz
5. [A/B-Modellbenchmark 15 Fälle, PO-bewertet](../../tests/runs/2026-11-20-THEOAGENT-AB-MODELLBENCHMARK-PO-PRAXISBEWERTUNG.md) – **A: 9 PASS/3 PARTIAL/3 FAIL**, **B: 2 PASS/3 PARTIAL/10 FAIL**; ursprüngliche strengere Bewertung separat dokumentiert. R-07 bei A noch PARTIAL/vorläufig. Modell A bevorzugt, nicht produktiv freigegeben.
6. [A/B-Testfragenkatalog](../../tests/runs/2026-11-20-THEOAGENT-AB-TESTFRAGENKATALOG.md) – einige A/B-Prompts verschieden; B-Originalfragen teils nicht mehr vollständig belegt. **Kein statistisch kontrollierter Modellvergleich**.
7. [Knowledge/Websuche/SourceGuard-Teststand](TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md) – frühere K-03/K-04: Suchtreffer ohne zusammenhängende `view_knowledge_file`-Lektüre; W-02/W-03: SourceGuard wird autonom aufgerufen, Originalabruf mit unterschiedlichem Erfolg.
8. [Eherechtliche Praxistests E-01–E-03](PRAXISTEST_EHESCHLIESSUNG_E01_E03_2026-11-18.md) – E-01 PARTIAL, E-02 FAIL, E-03 PARTIAL; Rechtsrisiko bleibt trotz neuerer A/B-Ergebnisse relevant.
9. [Vertraulichkeitsbefund einschließlich Nachtests V-04-R1/R2 und V-01/V-05](../../tests/drs_ki/CONFIDENTIALITY_FINDING_V04_V038.md), [unveränderte V-01–V-06-Testeingaben](../../tests/drs_ki/CONFIDENTIALITY_REGRESSION_V036.md), [WEB-01](WEB_01_WEBSUCHZUSAMMENFASSUNG_OHNE_ORIGINALLEKTUERE_2026-11-18.md), [SourceGuard/Klippert-Befund](T1_KLIPPERT_SOURCEGUARD_PRAXISBEFUND_2026-11-14.md).
10. [Vorheriger QE-Architekturreview](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md) und [F-C1/SG-01-Integrationsgate](F_C1_SG01_INTEGRATION_GATE_2026-11-17.md). **Historische QE-Befunde (z. B. zur damaligen Branch-Existenz) nicht ungeprüft als aktuellen Ist-Zustand übernehmen.**

### Zu prüfende technische Artefakte, nicht aus Erinnerung ableiten
- [Dokumentierter DEV-Systemprompt v0.3.11](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md), [tatsächliche Fachskills](../../config/drs-ki/skills/), [SourceGuard v0.2.3](../../tools/drs_ki/sourceguard_web_poc_v0_2_3.py), [Übergabestand 18.11.](TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md). **`config/drs-ki/README.md` beschreibt ältere Stände (u. a. Prompt v0.3.2/SourceGuard 0.2.0) und darf nicht als aktuelle Versionsquelle benutzt werden.**
- Tatsächlicher, live aktivierter DRS:KI-Stand **nicht unabhängig über Serverlogs verifiziert**. Laut zuletzt mitgeteilter DEV-Konfiguration: `Force_Tool_Usage=aus`, `Websuche_und_Dokument=Fast – Summary In One Go`, SourceGuard 0.2.3, Systemprompt v0.3.11; Konfigurationsangaben sind PO-Berichte, keine serverseitigen Belege.
- DRS:KI DEV: PO besitzt Developerzugriff; keine belegten Adminrechte bzw. Berechtigung für serverseitige Pipes. Endnutzer können das Modell nutzen, nicht Skills/Pipes konfigurieren.
- Die **explizite Aufrufbarkeit von SourceGuard wurde mehrfach nachgewiesen und soll nicht nochmals isoliert getestet werden**. Offen ist die verlässliche autonome Lektüre, korrekte Belegzuordnung und mögliche technische Durchsetzung.
- Nutzungsrechte an fremden Tools und urheberrechtlich geschützten Lehrbriefen sind **nicht durch den QE zu erteilen**; Entscheidung liegt beim PO.

## 2. Problem- und Risikobild, nach Belegen priorisiert

| Priorität | Finding | Befund / Testevidenz | Was nicht bewiesen ist |
|---|---|---|---|
| P0 (Diagnose zuerst) | **Vertraulichkeit beim Verfassen öffentlicher Texte** | A/B R-01: beide FAIL. **Gegenbefund:** Unter v0.3.8 mit aktualisiertem Liturgie-Skill V-04-R1/R2 PASS mit Vorbehalt/Einschränkung; V-01/V-05 PASS. Identischer V-04-Eingabekern, aber Modell-/Konfiguration nicht sicher gleich. | Ursache des erneuten Fehlers und tatsächliche Skill-Ladung im A/B-Lauf; kein belegter externer Datenabfluss. |
| P0 | **Zitat-/Quellenwahrheit** | A R-04 FAIL, B R-04 PARTIAL; ungesicherte Bibelübersetzungs- und Papstzitate. R-15/WEB-01: behauptete Originalprüfung ohne passendes sichtbares Leseevent, veralteter Normtext. | Dass jede Quellenart gleich unzuverlässig ist. |
| P0/P1 | **Fachliche Korrektheit bei folgenreichen Aussagen** | A/B R-09 FAIL: nicht belegte Motive von Priester/Levit; E-02 FAIL für Gültigkeit/Erlaubtheit/Formdispens; A R-07/A R-15 PARTIAL. | Eine einzelne universelle Fehlerursache; die Eherechts-Praxistests und neue A/B-Serie sind unterschiedliche Versuche. |
| P1 | **Knowledge-Originallektüre und Provenienz** | K-03/K-04: `grep` lieferte Textausschnitte, aber kein `view_knowledge_file`; automatische Quellenliste teils sachfremd. A R-14 zeigt später erfolgreiche Lektüre, daher **intermittierend/kontextabhängig**, nicht generell unzugänglich. | Backend-Provenienz/Urheber der automatischen Quellenliste. |
| P1 / Architektur-Gate | **F-C1 – keine erzwungene Quellenkontrolle** | SourceGuard ist reguläres Werkzeug; ein Tool-Aufruf ist kein gesichertes Ausgabe-Gate. SG-01 (Admin-/Betriebsfähigkeit einer Pipe oder gleichwertigen Instanz) bleibt offen. | Ob DRS:KI-Betrieb serverseitige Lösung erlauben kann. Nicht von fehlendem UI auf Unmöglichkeit schließen. |
| P2 | **Effizienz und Reproduzierbarkeit** | Mehrere Suchen/Snippets, teilweise fehlende B-Originalprompts; keine kontrollierte Paarstudie. | Kein belegter globaler Effizienzengpass oder Bedarf neuer Architektur. |

**Wichtig:** Die PO-Praxisbewertung mildert einige PARTIAL-Urteile zu PASS (A05, A11, A12, A13; B11). Die dort dokumentierten Quellen-/Verfahrensmängel sind **nicht behoben** und verletzen ggf. Anforderungen der formalen Baseline. Der QE darf diese Ebenen weder vermischen noch die PO-Urteile eigenmächtig abändern.

## 3. Vorgeschlagene Entwicklungsfolge – kleinste geeignete Maßnahmen

### Phase 0 – Ist-Zustand bestätigen und Fehlerhypothesen sortieren (keine Implementierung)

**Ziel:** Nachweisbar trennen zwischen Modellfehler, Prompt/Skill-Steuerung, Quellenzugriff/SourceGuard und Plattform-/Berechtigungsgrenze.

**Arbeit SE:** Prüft auf `drs-ki-test` den GitHub-Stand der vorhandenen Prompt-, Skill- und Toolregeln. Ordnet Befunde R-01, R-04, R-09, R-15 sowie KNOW-01/WEB-01 den jeweiligen Regel- und Werkzeugpfaden zu. Sucht vorhandene Regel vor neuer Regel; dokumentiert **belegt / plausibel / ungetestet**. Keine Wiederholung bekannter expliziter Tool-Aufrufbarkeitsproben.

**QE prüft:** Sind Prioritäten angemessen? Wird Ursachenhypothese von Nachweis getrennt? Welche der Probleme lassen sich mit **einer** vorhandenen Regel beheben? Welche sind echte technische Integrations- oder Plattformfragen?

**Ergebnis:** Kurze Fehler→Ursachehypothese→minimale Maßnahme→Nachtest-Tabelle, maximal 3 konkrete Änderungen für die erste Runde.

### Phase 1 – Zwei akute Qualitätsrisiken gezielt adressieren (P0)

**1A Vertraulichkeit (R-01): Diagnose vor Änderung.** Die V-04- und R-01-Frage ist wortgleich; die [historische Regression](../../tests/drs_ki/CONFIDENTIALITY_FINDING_V04_V038.md) enthält unter v0.3.8/aktualisiertem Skill bereits positive, jedoch eingeschränkte Live-Nachtests. **Zuerst** vollständige R-01-A/B-Protokolle auf echte `view_skill`-Aufrufe (`THEOAgent - Liturgische Texte` und `Pastorale Sensibilitaet`), Text des tatsächlich geladenen Skills, Modell, Promptversion und Zeitpunkt prüfen. Fehlen diese Angaben: Ursache **nicht verifiziert**; keine neue Regel daraus ableiten. Danach **nur bei belegtem Defizit** bestehende Schutzregel korrigieren. Regression mit unverändertem V-04/R-01 und **bereits vorhandenem V-05** (erlaubte Freigabe; kein neuer Positivfall); keine vertraulichen realen Daten extern übertragen. Anforderungen: US-17, FANF-28, NFANF-07; **spezifischer Schutz vor Offenlegung gegenüber Dritten ist nicht explizit als eigene Baseline-Anforderung benannt** (Traceability-Frage für PO).

**1B Zitatdisziplin (R-04):** Bereits vorhandene §-1-Regel im Systemprompt (Zitatdisziplin) und § 4 (Quellenstatus) prüfen. **Minimaler Kandidat:** eine Zeile zur ausdrücklichen Trennung von **wörtlich verifiziertem Zitat** und **klar gekennzeichneter Paraphrase / Vorschlag**; Quellenprüfungs-Skill nicht zusätzlich duplizieren. Nachtest: Bibelvers EÜ2016 + zugeschriebenes Papstzitat bei erfolgreichem und gescheitertem Abruf; keine Behauptung „verifiziert“ aus bloßem Trefferstatus.

**QE prüft:** Sind die Änderungen minimal, verständlich und wirksam, ohne legitime seelsorgliche Assistenz bzw. praktisch nutzbare Texte zu blockieren?

### Phase 2 – Fachliche Normen und Exegese verlässlich begrenzen (P0/P1)

**2A Exegese (R-09):** Im bestehenden **Systemprompt § 1** fehlen in der kurzen Negativaufzählung ausdrücklich „erfundene Motive, Handlungsgründe oder historische Details“; dort wäre **eine minimale Textpräzisierung** zunächst geeigneter als eine weitere Regel im Exegese-Skill. Grundlagen-Skill 1.1 („Welche Deutungen gibt der Text nicht her?“) beibehalten. Nachtest: barmherziger Samariter mit expliziter Beleggrenze und klar belegter Kontrastfall.

**2B Kirchenrecht (R-06/R-07/R-15 + E-02):** Vorhandenen **Grundlagen-Skill § 1.3** bei belegtem Bedarf um „Gültigkeit, Erlaubtheit, Dispens, Zuständigkeit“ ergänzen. **Eine** gezielte CIC-Prüfung mit cann. 1086, 1108, 1124–1127 und ggf. DRS-Partikularrecht umfasst zugleich die Marker-/Sektionsdiagnose aus Phase 3; **keine doppelte CIC-Probe**. Konkret dokumentiertes Versionsproblem: ein nach der Änderung durch *Omnium in mentem* veralteter Passus in der abgerufenen Vatikan-HTML-Fassung von can. 1124 (laut A/B-R-15-Protokoll; externer Originalabgleich im QE-Review nicht erfolgt). Keine pauschale Behauptung, sämtliche genannten Canones seien aktuell geändert. Beim ungeklärten Einzelfall keine voreilige Ehegültigkeitsfeststellung; bestehendes Fachverfahren nutzen, keine eigene Rechtsdatenbank.

**QE prüft:** Sind Normen korrekt, aktuell, hinreichend trennscharf? Sind Warnungen angemessen, ohne bei unkritischen Alltagstexten zu dominieren?

### Phase 3 – SourceGuard/Knowledge nachhaltig, aber nur nach Machbarkeitsklärung (P1)

**3A Ohne Adminzugriff:** Der Knowledge-Lesepfad `search_knowledge_files/grep_knowledge_files → view_knowledge_file` ist **grundsätzlich vorhanden, wird aber nicht zuverlässig ausgelöst** (K-03/K-04 ohne, R-14 Modell A mit tatsächlicher Lektüre). Fachbibliothek: Der dokumentierte [Systemprompt v0.3.11](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md) behauptet **nur Klippert sei eingebunden**; dies ist laut [Bestand 18.11.](WISSENSKORPUS_BESTAND_2026-11-18.md) überholt (187 vom DEV-Modell gemeldete Dateien, keine unabhängig geprüfte Vollinventur). **Günstigste konkrete Anpassungskandidatin ist die Korrektur dieses einen Satzes**, vor aufwendiger Quellenarbeits-Reorganisation; kausaler Einfluss auf KNOW-01 zunächst Hypothese. Ursprung und Status automatisch gezeigter Quellenlisten bleiben ungeklärt. Eine Kranemann-Probe zur Lektüre/Belegzuordnung; **CIC-Sektionsdiagnose ausschließlich in Phase 2B**, hier nicht wiederholen.

**3B F-C1 / SG-01 – früh stellen, getrennt bearbeiten:** Bereits **in Phase 0** eine einmalige Frage an den DRS:KI-Betrieb gemäß [SG-01](F_C1_SG01_INTEGRATION_GATE_2026-11-17.md): Kann eine administrativ bereitgestellte Pipe oder gleichwertige Instanz bei jedem Modellaufruf vor Ausgabe eingreifen? **PASS** nur mit tatsächlichem Interceptor-Test; **FAIL** nur bei verbindlicher Absage; sonst **NOT_TESTED**. Nach PASS ggf. bestehende SourceGuard-Referenz und SG-02 (Tool-Events) prüfen. Diese externe Klärung **blockiert nicht** die DEV-Verbesserungen, wohl aber jede Behauptung technisch erzwungener Quellenverifikation bzw. die entsprechende formale Freigabe. Kein neues Gate ohne Betriebsnachweis und PO-Entscheidung.

**QE prüft:** Existiert ein schlankerer vorhandener Mechanismus? Ist die vorgeschlagene Testgrenze beweiskräftig? Was bleibt ohne Gate prinzipiell unlösbar?

## 4. Minimales Prüfpaket nach freigegebenen Änderungen

Kein vollständiger 15er-Benchmark nach jeder kleinen Änderung. Die Regressionen sind *risikoorientiert*:

| Test | Akzeptanzhinweis | Primäre Prüfebene |
|---|---|---|
| R-01 / V-04 / V-05 | Zuerst R-01-Toolspur/Skill-Ladung und Versionskontext mit V-04-Nachtest vergleichen; keine vertraulichen Angaben ohne Freigabe im öffentlichen Text, zulässig freigegebene Informationen verwendbar | Vertraulichkeit; Live DEV; US-17/FANF-28/NFANF-07 (spezifischer Drittoffenlegungsschutz als offene Traceability-Frage) |
| R-04 | Keine ungesicherten Wortzitate; konkrete Quelle/Fassung oder ehrlicher Nichtverifizierbarkeitsstatus | Quellenwahrheit; Toolspur |
| R-09 | Keine unbelegten historischen Motive als Texttatsachen | Exegese/fachlich |
| R-15 bzw. E-02 | Gültigkeit ≠ Erlaubtheit, Rechtsfassung/kanonische Form korrekt; tatsächliche Originallektüre nicht behaupten ohne Ereignis | Kirchenrecht/Toolspur |
| K-03/K-04 oder R-14 | Relevanter `view_knowledge_file`-Haupttext statt nur Inhaltsverzeichnis/Treffer | Knowledge |
| W-02 oder R-13 | Geltenden Originaltext gelesen; alte Fassung bzw. weitere Normen nur bei tatsächlichem Nachweis | Web/SourceGuard |
| R-17/R-18 | Bei Prompt-/Skilländerung als leichter Schutz gegen unerwünschte Nebeneffekte | Textschutz/kritischer Dialog |

Für jede Ausführung: **exakter Prompt/Dateien**, aktives Modell, Prompt-/Skill-/Tool-Version, Run-Umgebung, aufrufbare/ausgeführte Tools, konkreter Originalauszug, Ergebnis und Fehlerstatus. Wo B-Originalprompts fehlen, **keinen exakten Paarvergleich behaupten**. Unkritische Tests nur, wenn der geänderte Pfad betroffen ist. Keine erfundenen Durchführungen.

**Formale Abnahme:** Baseline-[Abnahmeprofil](../requirements/ACCEPTANCE_PROFILE.md) bleibt maßgeblich und fordert zusätzlich T-01–T-08 und besonders bei Quellenprüfungen tatsächlich nachgewiesene Lesepfade. Eine PO-gewichtete Benchmark-PASS-Quote ersetzt diese Abnahme nicht.

## 5. Entscheidungs- und Änderungsgrenzen

- QE **reviewt diesen Plan**, implementiert oder pusht nicht, verändert keine Requirements-Baseline, legt keine Commit-SHAs fest, bewertet PO-Entscheidungen nicht als falsch oder freigibt keine Releases.
- SE wartet auf fachliche PO-Disposition dieses Entwurfs, bevor er produktwirksame Prompt-/Skill-/Tooländerungen in `drs-ki-test` vornimmt. Technische Teilaufgaben danach in kleinen Commits, tatsächliche Tests und Regressionsbelege.
- **Main-Merge und Produktivsetzung ausschließlich nach PO-Freigabe**. Bestehende Reviews und historische Testartefakte unverändert.
- Rechteklärung für Fachbibliothek und fremde Tools bleibt beim PO. Keine vertraulichen Testdaten in öffentlichen Repo-Dateien.

## 6. Konkreter Auftrag an den Quality Engineer

Bitte beantworte anhand der verlinkten **Originaldokumente im Repository** – nicht bloß anhand dieses Plans:

1. Sind die Phasen und Prioritäten angesichts der A/B-Befunde und der Anforderungen v1.2.0 angemessen? Nenne nur nachgewiesene Widersprüche oder relevante Lücken.
2. Für R-01/R-04/R-09/R-15 und KNOW-01/WEB-01: Welche bereits vorhandenen Regeln/Funktionen sollten **wiederverwendet** werden? Wo ist die kleinste konkrete Änderung zu erwarten? Ordne Hypothese/Nachweis.
3. Welche vorgeschlagenen Schritte sind redundant, nicht testbar oder unnötig teuer? Streiche sie statt neue Agenten/Schichten vorzuschlagen.
4. Sind die Abnahmekriterien ausreichend präzise, ohne die Requirements-Baseline stillschweigend abzuschwächen? Trenne PO-Praxisurteil von technischer/fachlicher Abnahme.
5. Ist F-C1/SG-01 ein externer, separater Architektur-Gate oder eine Blockade für **jede** DEV-Verbesserung? Begründe die technisch realistische Trennung.
6. Gib einen **priorisierten, maximal fünf Findings umfassenden** Reviewbericht: ID, Schweregrad (kritisch/wesentlich/geringfügig), betroffene Datei/Anforderung, konkreter Beleg, Risiko, kleinste empfohlene Korrektur und prüfbarer Nachweis. Formuliere anschließend eine klare Empfehlung **freigeben / mit Auflagen / überarbeiten**, ausschließlich bezogen auf den *Plan*.

**Review-Beschränkungen:** Keine erfundenen Toolaufrufe, Laufzeitergebnisse, Implementierungsstände oder Commits. Wenn GitHub-Dokumente nicht erreichbar sind, die nicht geprüften Aussagen ausweisen. Keine selbstständigen Änderungen oder Freigaben im Repository.

## 7. QE-Findings-Disposition und nächste PO-Entscheidung (20.11.2026)

**Reviewquelle:** vom PO im Gespräch übermittelter „QS-Planreview Weiterentwicklungsplan THEOAgent DRS:KI (Commit 1e95939)“, Notiz-ID `1ed967f8`. Der SE hat die relevanten Repositorydateien eigenständig gelesen und die Branch-HEADs geprüft; ein vollständiges unabhängiges Nachspielen aller 31 vom QE genannten Lektüren oder Live-Tests erfolgte nicht. **Originaler Reviewtext liegt hier als PO-Übermittlung vor; kein eigenständiger GitHub-Reviewcommit behauptet.**

| QE-Finding | SE-Disposition | Konsequenz |
|---|---|---|
| F-01 (wesentlich) | **Akzeptiert.** V-04-R1/R2 positive, eingeschränkte Live-Resultate nach Skill-Fix; A/B R-01 erneut FAIL. Ohne tatsächliche Toolspur/Versionsgleichheit keine kausale Aussage. | Skill-Ladung und Konfiguration vergleichen, bevor Prompt/Skill geändert wird; vorhandene V-05-Regression nutzen. |
| F-02 (wesentlich) | **Akzeptiert.** `main` @ `ebb7102` beinhaltet Merge vom 19.11.; `drs-ki-test` @ `1e95939` ist der Review-Prüfstand. Frühere Freeze-/Branchhinweise sind teils historisch. | Belege branch-/commitgenau lesen; keine stille Änderung/Übernahme nach `main`. |
| F-03 (wesentlich) | **Akzeptiert.** Code v0.2.3 vorhanden, frühere Referenz v0.2.0 für aktuellen Stand falsch; Config-README historisch. | Code- und Kontextlinks aktualisiert. |
| F-04 (wesentlich) | **Akzeptiert.** Knowledge-Lesepfad ist nicht zuverlässig ausgelöst. | Satz berichtigt; Kranemann-Lesetest statt pauschaler Erfolgsvoraussetzung. |
| F-05 (geringfügig) | **Teilweise akzeptiert.** US-17, FANF-28, NFANF-07 tragen die pastorale Einordnung. Eigenständiger Normtatbestand „Verbot der Drittoffenlegung im öffentlichen Text“ ist damit nicht explizit als MUSS-Bedingung definiert. | Traceability im Plan benannt. **PO entscheidet separat**, ob später eine Präzisierung der formalen Requirements-Baseline nötig ist. Keine stillschweigende Baseline-Änderung. |

**PO-Disposition noch ausstehend:** Freigabe des überarbeiteten Plans als Entwicklungsarbeitsgrundlage? Gesonderte Entscheidung zur Baseline-Traceability bei R-01. **Bis dahin keine produktwirksamen Änderungen.**
