# THEOAgent

THEOAgent ist ein theologischer Arbeitsassistent für Bibelauslegung, Predigtarbeit, Liturgie, Katechese, Kirchenrecht, Quellenrecherche und kritische Textprüfung.

## Projektstand

- `main` bündelt die freigegebene Requirements-Baseline v2.0.0, die dokumentierte THEOAgent-DEV-Konfiguration und deren Entwicklungs- und Testhistorie. **Die Übernahme der DEV-Artefakte ist keine Produktiv- oder Qualitätsfreigabe.**
- `dev-v2` ist der aktive Entwicklungsbranch für SourceGuard v2. AP1 und AP2 sind konzeptionell abgeschlossen; AP3a-Core v0.1.0 implementiert, synthetische Offline-Tests PASS; Live-Smoke-Test ausstehend.
- `local-dev` und `drs-ki-test` bleiben historische Referenzstände. Der dokumentierte DRS:KI-DEV-Teststand stammt vom 18.11.2026.
- **Historischer dokumentierter DRS:KI-DEV-Stand:** [Systemprompt v0.3.11](docs/drs-ki/THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md), [SourceGuard v0.2.3](tools/drs_ki/sourceguard_web_poc_v0_2_3.py), [sieben Fachskills](config/drs-ki/README.md), [Test-/Übergabestand](docs/drs-ki/TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md).
- [MCP-Integrationsarchitektur für DRS KI:W.E.G. v0.1.0](docs/drs-ki/MCP_INTEGRATIONSARCHITEKTUR_DRS_KI_WEG_v0.1.0.md) – technischer Diskussionsentwurf.

## SourceGuard v2 – Entwicklungsstand (28.11.2026)

| Arbeitspaket | Stand |
|---|---|
| AP1 – Bestandsaufnahme | Abgeschlossen ([Inventar](docs/architecture/AP1_V2_COMPONENT_INVENTORY.md)) |
| AP2.1 – Native Modellkommunikation | Live-Kommunikationsnachweis PASS |
| AP2.2 – Skill-/Knowledge-Integration | Kommunikationspfad PASS; fachliche Testläufe PARTIAL, konkrete Leseprovenienz offen |
| AP2.3 – Schutz- und Provenienzkonzept | Entwurf abgeschlossen; Schutzvalidierung NOT_RUN |
| AP2.4 – Zielarchitektur | Revision 3, Claude-Review disponiert; PO-Entscheidung zur vertrauenswürdigen Zielumgebung berücksichtigt |
| AP3a – Core | [Core v0.1.0](tools/local_dev/sourceguard_v2_core.py), [Offline-Teststand](tests/runs/2026-11-28-AP3A-CORE-OFFLINE.md): 10/10 PASS; Live-Smoke NOT_RUN |
| AP3b/c – Knowledge, Arbeitskontext und Web | Geplant |
| AP4–7 – Frühtests, Fachkonfiguration, Optimierung, Abnahme | Offen |

Maßgebliche Entwicklungsreferenz: [Zielarchitektur AP2.4, Revision 3](docs/architecture/AP2_4_TARGET_ARCHITECTURE.md), insbesondere Abschnitt 9 (PO-Entscheidung). [Fundstellengenauigkeit](docs/architecture/PO_FUNDSTELLENGENAUIGKEIT_2026-11-28.md): identifizierbarer Abschnitt statt obligatorischer Buchseite. Keine eigene Sicherheitsinfrastruktur, kryptografische Provenienz, zusätzliche Datenbank oder restriktive Antwortgates; vorhandene Plattformfunktionen nutzen. Die vertrauenswürdige Zielumgebung ist eine Architekturannahme, kein Sicherheitsnachweis. Baseline unverändert; lokale externe Datenflüsse und Nutzungsrechte bleiben zu klären. Offline-Tests der Probes und praktische Schutzvalidierung NOT_RUN. Keine Produktfreigabe.

## Dokumentation

- [Requirements-Baseline v2.0.0 (freigegeben)](docs/requirements/BASELINE.md)
- [Theologischer Fachstandard – Ausgangsreferenz zu RANF-04](docs/requirements/THEOBald_Fachstandard.md) · SHA-256 `cc5a4dd89eb2279ba61fea105eea33ce45767b783eb572475fef9903c778174c`
- [Migration v1.2.0 → v2.0.0](docs/requirements/MIGRATION.md)
- [Traceability-Matrix v2.0.0](docs/requirements/TRACEABILITY.md)
- [Abnahmeprofil v2.0.0 und offene Abnahmeparameter](docs/requirements/ACCEPTANCE_PROFILE.md)
- [Historische Bestandsaufnahme der THEOBald-Komponenten (10.11.2026)](docs/architecture/COMPONENT_INVENTORY.md)
- [Projektprozess, SSOT und Rollen](https://github.com/baem-oss/THEOAgent/blob/main/docs/WORKFLOW.md)

| Kategorie | Anzahl |
|---|---:|
| User Stories (US) | 27 |
| Harte Grenzen (H) | 6 |
| Funktionale Anforderungen (F) | 18 |
| Qualitätsanforderungen (Q) | 12 |
| Randbedingungen (RANF) | 8 |
| Sicherheits- und Datenschutzanforderungen (SP) | 6 |
| Datenanforderungen (DAT) | 4 |

Der Fachstandard ist die unveränderte THEOBald-Referenz, die in RANF-04 über ihre Prüfsumme identifiziert ist. Die fachliche Festlegung als verbindlicher THEOAgent-Standard steht aus.

**Rolle:** Nutzer von THEOAgent.

**Anforderungsformulierung:** Funktionale Anforderungen nach SOPHIST-FunktionsMASTER, nichtfunktionale Anforderungen nach EigenschaftsMASTER. Fehlende Grenzwerte sind als offen gekennzeichnet.

**Status:** Requirements-Baseline v2.0.0 am 28.11.2026 vom Product Owner freigegeben ([Freigabevermerk](docs/requirements/PO_APPROVAL_V2.0.0.md)). Implementierungs- und Qualitätsabnahme stehen aus. Die Zielarchitektur für das lokale Refactoring der obligatorischen, nicht restriktiven SourceGuard-Pipe liegt vor; DRS:KI-Integration ist DEFERRED / TO_CHECK.

**Single Source of Truth:** Ausschließlich der versionierte, vom Product Owner freigegebene Repository-Stand ist verbindlich. Der QE prüft dokumentierte Git-Stände, legt aber weder Git-SHAs noch freizugebende Inhalte fest. Siehe [Projektprozess](https://github.com/baem-oss/THEOAgent/blob/main/docs/WORKFLOW.md).
