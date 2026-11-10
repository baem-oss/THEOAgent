# THEOAgent – Technische Komponenten und Wiederverwendbarkeit

**Stand:** 10.11.2026  
**Status:** Bestandsaufnahme auf Grundlage öffentlich überprüfbarer Repository-Artefakte; **keine** neue Architekturentscheidung, Implementierungsabnahme oder Aussage über den heutigen Livezustand des Homeservers.  
**Anforderungsbasis:** [THEOAgent v1.1.0](../requirements/BASELINE.md)  
**Referenzrepository:** [baem-oss/THEOBald](https://github.com/baem-oss/THEOBald)

## 1. Referenzstände und Betriebsumgebung

| Referenz | Commit | Inhalt |
|---|---|---|
| THEOBald `main` | `6cef508cead1f2cc879d15455bfd4da704479317` | Open-WebUI-Grundarchitektur, Skills, Prompt, RAG- und Testdokumentation; kein `sourceguard/`-Verzeichnis |
| THEOBald `review/sourceguard-integrated-v0.5.5-dev3` | `a5338e229a781df8ebb670c392b815531b0d7c5f` | Fortgeschriebenes modulares Profil, experimentelle SourceGuard-Pipe, Tests und Integrationsprotokolle |

**Dokumentierte lokale Testumgebung:** Raspberry Pi 5 (ARM64) mit Docker und Open WebUI v0.11.4. Open-WebUI-Modellprofil `THEOBald – Modular`, Google Gemma 4 31B IT über die direkte OpenRouter-API, **Native Function Calling**. Im THEOBald-Datenpfad ist **kein LiteLLM** vorgesehen; globale Open-WebUI-/Docker-/LiteLLM-Änderungen sind für den bisherigen Prototyp nicht erforderlich.

**Fachinformationen:** lokale private Open-WebUI-Knowledge-Sammlungen mit PDF/EPUB-Material sowie Webwerkzeuge für öffentliche Quellen. Die ursprüngliche Fachbibliothek umfasste 67 Dateien und 486.575.819 Byte; dies ist **keine** bestätigte aktuelle Bestandszahl.

**Quellen:** [Architektur](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/docs/architecture.md), [Entwicklungsstatus](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/docs/STATUS_2026-11-07.md), [Bibliotheksinventar](https://github.com/baem-oss/THEOBald/blob/main/docs/baseline-v1.2.0.md).

## 2. Komponenten

| Komponente | Vorhandener Gegenstand | Nachweisstand | Bezug zur Baseline |
|---|---|---|---|
| Modellprofil und Kernprompt | `THEOBald – Modular`; [modularer Prompt](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/openwebui/system_prompt_modular_candidate.md) | Lokal laut Projektstatus eingerichtet; Promptversion im Liveprofil nicht vollständig unabhängig verifiziert | US-01, US-08–20, US-25 |
| Sieben fachliche Skills | `skills/*/SKILL.md`: Grundlagen, Quellenprüfung, Exegese/Homiletik, Homiletik, Liturgie, Pastoral, Qualität | Alle laut Nutzer im Modell integriert; 4 fachliche Einzeltests PASS, 3 PARTIAL; **keine nachgewiesene separate Skillaktivierung** | US-08–18, US-19, US-25 |
| Knowledge/RAG | `list_knowledge`, `grep_knowledge_files`, `query_knowledge_files`, `view_knowledge_file` | Isolierte Originallektüre Böttigheimer/Klippert belegt; Abruf im integrierten Nutzerauftrag nicht zuverlässig | US-02–07, US-26 |
| Externe Quellen | `search_web`, `fetch_url`; offizielle Webquellen im Quellenprüfungs-Skill | Technischer Webzugriff nachgewiesen; autonome Aktivierung bei amtlichen Fragen in QP01/QP03 ausgefallen | US-02–07, US-13, US-15, US-16 |
| Dokumenteneingabe | Open-WebUI-PDF-Anhänge, Dokumentextraktion und Retrieval | Vollständige PDF-Bereitstellung bei I01 nicht nachgewiesen; direkte Übergabe des extrahierten Textes funktionierte im Kontrollfall | US-10, US-18, US-27 |
| SourceGuard | `sourceguard/sourceguard.py`, Python/Pydantic, Open-WebUI-Pipe mit Legacy- und Agentenmodus | Branch-only, experimentell; CI mit synthetischen Tests vorhanden; Agenten-R01 nicht erfolgreich abgenommen | Potenziell US-03, US-04, US-07 |
| Text-Freeze / Arbeitsfassungen | Explizite Regeln im Anforderungskatalog | Kein unabhängiger technischer Nachweis einer dauerhaften, verlässlich geschützten Freeze-/Versionsfunktion | US-11, US-21, US-23 |

Die vorhandene **modulare Modellprofil-Variante** und die später entwickelte **Pipe-Variante** sind unterschiedliche technische Ausführungen. Die Existenz beider Varianten ist **keine** Entscheidung, beide zu übernehmen oder parallel zu betreiben.

## 3. Beobachtete Tests und Grenzen

| Prüffall | Befund |
|---|---|
| S01–S07: sieben Fachskills | **4 PASS / 3 PARTIAL** für fachliche Antworten; separate Tool-/Skillaktivierung jeweils nicht nachgewiesen |
| S02: Böttigheimer `sacra doctrina` | Originallektüre über `grep_knowledge_files` und `view_knowledge_file` mit überprüften Buchseiten 42–44: **PASS** |
| I01: hochgeladenes Predigt-PDF + Klippert | Integrierte Fachaufgabe **FAIL**, späterer Versuch **PARTIAL**; vollständiges Dokument beziehungsweise einschlägige Klippert-Lektüre im kombinierten Auftrag nicht zuverlässig nachgewiesen |
| Isolierte Klippert-Recherche | Vier echte `view_knowledge_file`-Aufrufe und gegengeprüfte Textstellen: **PASS**; kein Nachweis für die integrierte PDF-Predigtprüfung |
| I02: Kyrie/Fürbitte mit amtlicher Quellenprüfung | Pastoraler Text brauchbar, **Gesamt-FAIL** wegen unbelegter beziehungsweise falscher amtlicher Quellenzuordnung; keine Werkzeugaufrufe |
| QP01/QP03: amtliche Recherche | **FAIL** bei autonomer Aktivierung der erforderlichen Websuche |
| SourceGuard 0.5.5-dev3 / Agent 0.2.0-dev7 | **259 CI-Tests PASS, 9 wegen fehlender Original-PDF übersprungen** (268 insgesamt); kein bestandener Agenten-R01-Livetest belegt |

**Quellen:** [Skill-Evaluation](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/tests/SKILL_EVALUATION_RESULTS_2026-11-07.md), [I01](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/tests/INTEGRATION_I01_2026-11-07.md), [I02](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/tests/INTEGRATION_I02_PLAN_2026-11-07.md), [SourceGuard-Status](https://github.com/baem-oss/THEOBald/blob/review/sourceguard-integrated-v0.5.5-dev3/sourceguard/CURRENT_STATUS.md).

## 4. Offene technische Nachweise (Priorität)

| ID | Priorität | Gegenstand | Minimaler Nachweis ohne neue Implementierung |
|---|---|---|---|
| T-01 | Hoch | Vollständige Nutzerdokumente | Für ein mehrseitiges PDF muss der Text aller relevanten Seiten im Modellkontext nachweisbar sein; Dokumentextraktion, Retrieval und tatsächliche Auswertung getrennt beurteilen |
| T-02 | Hoch | Kombination Nutzertext + angeordnete Fachquelle | Kurzer natürlicher Auftrag „Prüfe diese Predigt nach Klippert“; vollständiger Text, relevante Originalstelle und textbezogenes Urteil müssen im **selben Lauf** vorliegen |
| T-03 | Hoch | Amtliche Onlinequellen | Eine natürliche Frage mit erforderlicher aktueller amtlicher Fundstelle muss Webabruf, Originalprüfung, richtige Fundstelle oder ausdrücklich fehlenden Zugriff ergeben |
| T-04 | Hoch | Quelle und Behauptung | Belegprüfung darf technisch nachgewiesene Lektüre nicht mit inhaltlicher Übereinstimmung verwechseln; Gegenprobe mit falscher Zuschreibung |
| T-05 | Mittel | Text-Freeze | Nach ausdrücklichem Einfrieren bleibt eine nicht beauftragte Passage bei einer selektiven Revision byte- beziehungsweise textidentisch |
| T-06 | Hoch vor externen privaten Dokumenten | Datenschutz | Zulässigkeit der Weitergabe der konkret abgerufenen Bibliothekspassagen an den gewählten externen Modellprovider nachweisen |

**Keine festgelegte technische Lösung:** Die Bestandsaufnahme begründet weder eine neue Pipe noch die Übernahme des alten SourceGuard-Codes. Neue Komponenten sind erst gerechtfertigt, wenn ein dokumentierter Testfall mit vorhandenen Open-WebUI-Mitteln nicht erfüllt wird und eine konkrete technische Ursache eingegrenzt ist.

## 5. Nächster Engineering-Schritt

**Einen kompakten, realitätsnahen Akzeptanz-/Diagnosetest für T-01 bis T-03 definieren und in der vorhandenen Open-WebUI-Testkonfiguration durchführen.** Zunächst nur die jeweils tatsächlich bereitgestellten Dokumentteile und Werkzeugaufrufe feststellen. Fachliche Bewertung und Fehlerursache anschließend getrennt beurteilen. Keine globalen Konfigurationsänderungen, kein neuer Code und kein Import privater Volltexte nach GitHub.

Die Resultate bilden die Grundlage dafür, welche vorhandenen THEOBald-Komponenten übernommen werden können und ob eine zusätzliche technische Durchsetzung für einzelne Quellenpflichten überhaupt notwendig ist.
