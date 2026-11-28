# THEOAgent

THEOAgent ist ein theologischer Arbeitsassistent für Bibelauslegung, Predigtarbeit, Liturgie, Katechese, Kirchenrecht, Quellenrecherche und kritische Textprüfung.

## Projektstand

- `main` bündelt die freigegebene Requirements-Baseline v2.0.0, die dokumentierte THEOAgent-DEV-Konfiguration und deren Entwicklungs- und Testhistorie. **Die Übernahme der DEV-Artefakte ist keine Produktiv- oder Qualitätsfreigabe.**
- `drs-ki-test` bleibt als bisheriger DEV-Arbeitsbranch und historischer Referenzstand erhalten. Der dokumentierte DEV-Teststand stammt vom 18.11.2026.
- **Aktueller dokumentierter DEV-Stand:** [Systemprompt v0.3.11](docs/drs-ki/THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md), [SourceGuard v0.2.3](tools/drs_ki/sourceguard_web_poc_v0_2_3.py), [sieben Fachskills](config/drs-ki/README.md), [Test-/Übergabestand](docs/drs-ki/TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md).
- [MCP-Integrationsarchitektur für DRS KI:W.E.G. v0.1.0](docs/drs-ki/MCP_INTEGRATIONSARCHITEKTUR_DRS_KI_WEG_v0.1.0.md) – technischer Diskussionsentwurf.

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

**Status:** Requirements-Baseline v2.0.0 am 28.11.2026 vom Product Owner freigegeben ([Freigabevermerk](docs/requirements/PO_APPROVAL_V2.0.0.md)). Implementierungs- und Qualitätsabnahme stehen aus. Lokales Refactoring der obligatorischen, nicht restriktiven SourceGuard-Pipe folgt; DRS:KI-Integration ist DEFERRED / TO_CHECK.

**Single Source of Truth:** Ausschließlich der versionierte, vom Product Owner freigegebene Repository-Stand ist verbindlich. Der QE prüft dokumentierte Git-Stände, legt aber weder Git-SHAs noch freizugebende Inhalte fest. Siehe [Projektprozess](https://github.com/baem-oss/THEOAgent/blob/main/docs/WORKFLOW.md).
