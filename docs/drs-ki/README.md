# DRS:KI-Erprobung – THEOAgent

**Stand:** 16.11.2026  
**Status:** **Praktische DEV-Erprobung (PO-Entscheidung vom 14.11.2026)**, Konfigurations-/Code-Freeze für den Prototyp; **keine Architektur-, Produkt- oder Quellenverifikationsfreigabe**  
**Arbeitsbranch:** `drs-ki-test`  
**SSOT:** `baem-oss/THEOAgent`, gemäß [Projektprozess](../WORKFLOW.md).

**Verbindliche Rollen-/Umgebungsklarstellung (PO, 13.11.2026):** Entwicklung und Tests finden auf **DRS:KI DEV** mit **Developerzugriff** statt. Der spätere **Endnutzer ruft ausschließlich das bereitgestellte Modell auf**; er konfiguriert weder Tools noch Skills noch Pipes. Die technische Integrationsfähigkeit ist daher mit Developerrechten zu prüfen; konkrete Installations- bzw. Deploymentbefugnisse sind damit noch nicht nachgewiesen.

## Aktueller Arbeitsmodus – praktische DEV-Erprobung (PO, 14.11.2026)

**PO-Entscheidung:** THEOAgent Dev jetzt als theologischen **Arbeitsprototyp** in realen Aufgaben einsetzen. Die bisherigen isolierten Tests werden nicht als fortlaufende Testkampagne weitergeführt. Entwicklung erfolgt **befundgetrieben** nach KISS; Änderungen nur bei belegtem, hinreichend relevantem Bedarf. Dies ist **keine** Produkt-/Release-Abnahme und kein Merge nach `main`.

**Vorläufig eingefrorene DEV-Konfiguration im Repository:** [Systemprompt v0.3.3](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.3.md), sieben THEOAgent-Fachskills (mit der [Mehrkriterien-Abbruchregel](../../config/drs-ki/skills/theologische-quellenpruefung/SKILL.md) aus Commit `2e05e94`), [SourceGuard v0.2.0](../../tools/drs_ki/sourceguard_web_poc_v0_2_0.py). Der auf DEV eingesetzte exakte Versions-/Artefaktstand ist nicht unabhängig mit Serverlogs belegt. Keine weiteren Prompt-, Skill- oder Codeänderungen ohne konkreten Praxisbefund.

**Praxisfelder:** Exegese, Predigtvorbereitung und -kritik, liturgische Texte, theologische Fachrecherche sowie kirchliche Quellen- und Normenfragen. Die Anfragen sollen **normal formuliert** werden, nicht mit vorgegebenen Toolsequenzen; so wird die eigenständige Nutzbarkeit beobachtet.

**Qualitätssicherung im Gebrauch:** Nur neue, relevante Beobachtungen dokumentieren. Bagatellen direkt im Dialog verbessern. Wiederkehrende Fehler oder schwerwiegende Einzelereignisse mit tatsächlichem Werkzeugprotokoll als Finding unter `drs-ki-test` festhalten und ggf. gezielt an QE übergeben. Quellenbelege bei fachlich oder rechtlich folgenreichen Aussagen am Original kontrollieren. Keine Behauptung technisch authentifizierter Quellen allein aus modellgenerierten Antworten oder `EVIDENCE_READY_FOR_REVIEW`.

**Offenes Risiko:** [T-1 Praxisbefund F-T1-01 – MAJOR / OPEN](T1_KLIPPERT_SOURCEGUARD_PRAXISBEFUND_2026-11-14.md). Im Test wurde der vierte SourceGuard-Werkzeugnachweis vom Modell zunächst simuliert, nach Nutzerintervention korrekt nachgeholt. Toolaktivierung, Originallektüre und SourceGuard-Aufrufe wurden grundsätzlich gezeigt; die Integrität modellseitig wiedergegebener Tool-Rückgaben ist nicht technisch garantiert (F-C1). QE-Nachreview bestätigt MAJOR; DEV-Erprobung bleibt vertretbar, **quellenverifizierter Einsatz nicht freigegeben**.

**Änderungsauslöser:** (1) belegtes Verhalten, (2) fachliche/operative Relevanz, (3) realistisch wirksame minimale Abhilfe. Bei neuer Änderung: SSOT-Commit im Branch, darauf begrenzte Nachprüfung, Entscheidung durch PO. Keine zusätzlichen Testkataloge.

## Verbindliche Grundlage

- [Requirements-Baseline v1.2.0](../requirements/BASELINE.md) (PO-freigegeben am 10.11.2026).
- [Traceability](../requirements/TRACEABILITY.md), [Abnahmeprofil](../requirements/ACCEPTANCE_PROFILE.md).
- [THEOBald-Fachstandard](../requirements/THEOBald_Fachstandard.md) als prüfsummengleiche Ausgangsreferenz zu RANF-04.
- [DEV-Konfiguration und Fachskills](../../config/drs-ki/README.md).
- Die bestehenden THEOBald-Komponenten, insbesondere der experimentelle SourceGuard, sind **Referenzimplementierungen** im Repository [baem-oss/THEOBald](https://github.com/baem-oss/THEOBald). Die dortige Branch-/Pipe-Situation ist getrennt von der THEOAgent-Requirements-SSOT zu behandeln.

## Übernommene Unterlagen

1. [Architekturvorschlag vom 13.11.2026](ARCHITEKTURVORSCHLAG_2026-11-13.md) – nicht freigegeben; durch den QE teilweise beanstandet.
2. [Unabhängiger QE-Architektur-Review vom 13.11.2026](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md) – historischer Reviewbeleg, unverändert übernommen; maßgebliche Findings F-C1 (kritisch) sowie F-A1, F-C2 bis F-C7.
3. **Quellcode-Belege (separates, nicht öffentliches Reviewpaket)** – sieben DRS:KI-Implementierungen, davon sechs aus Nutzeruploads, eine als Chat-Abschrift. Sie sind wegen ungeklärter Nutzungsrechte **nicht** Bestandteil des öffentlichen GitHub-Repositories. Ursprünglicher Dateiname: `THEOBald_DRS-KI_QE_Quellcodes_2026-11-13.zip`.
4. [Herkunft des QE-Pakets](evidence/README_QE_PAKET.md).
5. [Architekturkorrektur AK-01 – F-C1](ARCHITEKTURKORREKTUR_AK-01_F-C1.md) – ersetzt die promptbasierte Verifikationsannahme des historischen Entwurfs; technische Verifikation weiterhin offen.
6. [Findings-Disposition und P0-Plan](P0_MACHBARKEIT_UND_FINDINGS.md) – Arbeitsvorschlag, keine PO-Abnahme.

Das Review-ZIP enthält nur eine Faster-Fassung (identische Dublette ausgeschlossen). **Keiner der fremden Quellcodes wird im öffentlichen Repository als Datei bereitgestellt.** Früher versehentlich committe Reviewkopien wurden aus dem Branch-Arbeitsbaum entfernt; da Git-Historie bestehen bleibt, bedarf eine gegebenenfalls notwendige Historienbereinigung einer gesondert abgestimmten Maßnahme.

## Fachlicher Zwischenstand

- Die Werkzeuge gestatten in unterschiedlichem Umfang Treffer-, Snippet-, Originalauszugs- und Dokumentzugriff.
- Keine der gesichteten DRS:KI-Werkzeugimplementierungen belegt allein die SourceGuard-konforme, technisch erzwungene Prüfung.
- Das vorgeschlagene promptbasierte Verifikationsverfahren genügt **nicht** als Ersatz für den bestehenden SourceGuard (QE F-C1).
- Auf DRS:KI ist ein **Erkundungspilot** mit als ungesichert bezeichneten Evidenzstufen denkbar. Ein **quellenverifizierter Betrieb** ist nicht freigegeben.
- Konkrete **Developer-/Deploymentbefugnisse**, Tool Callbacks, Funktions-/Pipe-Integration, Modellverhalten, Datenflüsse und Lizenzrechte sind noch praktisch bzw. organisatorisch zu prüfen. Endnutzer-Konfigurationsrechte sind **kein** Prüfgegenstand.

## Regeln für die Weiterarbeit

1. Keine Änderungen an der freigegebenen Requirements-Baseline durch die Übernahme.
2. Keine Übernahme fremden DRS:KI-Codes in produktive Komponenten ohne Rechteklärung. Das Verzeichnis `evidence/sources/` dient ausschließlich der Prüfung.
3. Unterscheidung von `TREFFER`, `AUSZUG` und `TECHNISCH_VERIFIZIERT`; letzteres nur bei technischem Nachweis. Eine promptbasierte Selbstdeklaration ist keine Garantie.
4. SourceGuard nicht neu erfinden: Eignung der bestehenden Implementierung und notwendige Adapter zuerst prüfen.
5. **Developerzugriff auf DRS:KI DEV ist gegeben**; weitergehende Admin-/Installationsrechte nicht unterstellen. Keine Laufzeitergebnisse behaupten, die nicht auf DRS:KI DEV erhoben wurden.
6. QE findet und begründet Beanstandungen; der PO entscheidet über fachliche Baselines und Freigaben. Der QE setzt keine Commit-SHAs.

## Fortsetzung

**Systemprompt für den aktuellen DEV-Prototyp:** [THEOAgent DEV v0.3.3 mit Skill-Orchestrierungs-Workaround und SourceGuard v0.2.0](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.3.md). Sieben vorhandene Skills mit Namenspräfix `THEOAgent - ` bleiben separat; die aktuelle v0.3.0 war im Repo nicht als vollständiger Wortlaut archiviert, deshalb ist dies eine konsolidierte Neufassung und kein behaupteter exakter Diff.

**Aktueller PO-Auftrag (14.11.2026):** Ein **arbeitsfähiger THEOAgent-DEV-Prototyp** mit **SourceGuard v0.2.0 als gemeinsamer Belegaufbereitung** für Web, Fachbibliothek und geeignete DRS-Werkzeugauszüge. [Konfiguration, konkrete DRS-Werkzeugauswahl und Systemprompt-Ergänzung](THEOAGENT_DEV_SOURCEGUARD_V0_2_0_ARBEITSPROTOTYP.md). Keine neuen Tests beauftragt. Die ältere Bezeichnung `SourceGuard Web` und ältere KKK-Tests sind Entwicklungshistorie; das aktuelle Tool bleibt unter demselben Python-Dateipfad.

**Aktueller Entwicklungsstand (PO-Entscheid 14.11.2026):** SourceGuard Web **v0.2.0 generisch**, [Implementierung](../../tools/drs_ki/sourceguard_web_poc_v0_2_0.py), [Tests](../../tests/drs_ki/test_sourceguard_web_poc_v0_2.py), [API und DEV-Testplan](SOURCEGUARD_WEB_V0_2_0_GENERIC.md). KKK-spezifischer Versionscode ist aus v0.2.0 entfernt; die vorherige P-03b-Anleitung ist historisch. Lokale und DEV-Regressionen dieser Revision noch offen.

**PoC-Erweiterung:** [P-02: Vergleich der vorhandenen DRS:KI-Werkzeuge mit SourceGuard Web](POC_P-02_DRS_TOOLS_VERGLEICH.md). Zuerst DRS-Faster an KKK 2267, CIC can. 767 § 1 und Soziallehre Nr. 160–163 testen, Outline/MediaWiki/TYPO3 nur bei einschlägiger Quelle. Der eigene [Webadapter](../../tools/drs_ki/sourceguard_web_poc_v0_1_0.py) dient als gezielter Vergleich für einen sicheren Originalabruf, nicht als Ersatz der technischen Antwortdurchsetzung. Die [Offline-Regressionsfälle](../../tests/drs_ki/test_sourceguard_web_poc.py) sind hinzugefügt, aber noch nicht als ausgeführt bestätigt.

**Historische PO-Priorisierung (durch die praktische DEV-Erprobung vom 14.11.2026 abgelöst):** [Schneller PoC P-01](POC_P-01_SCHNELLTEST.md) mit dem bestehenden DRS-Prompt v0.2.3 und bereits funktionierenden Werkzeugen. Eine allgemeine Tool-/Berechtigungsinventur ist **keine** Voraussetzung. Der [P0-Machbarkeits- und Findingsplan](P0_MACHBARKEIT_UND_FINDINGS.md) bleibt für gezielte technische Nachprüfungen und die spätere SourceGuard-Integration verfügbar. Der PoC belegt ausdrücklich noch keine technisch erzwungene Quellenverifikation.
