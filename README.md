# THEOAgent

THEOAgent ist ein theologischer Arbeitsassistent für Bibelauslegung, Predigtarbeit, Liturgie, Katechese, Kirchenrecht, Quellenrecherche und kritische Textprüfung.

## Projektstand

- `main` enthält die freigegebene Requirements-Baseline v1.2.0 und die bisherige Diagnosedokumentation. [T-02](docs/testing/T02_PO_CLOSURE_2026-11-11.md) ist als Diagnose abgeschlossen.
- Die praktische Erprobung in DRS:KI DEV läuft auf [`drs-ki-test`](https://github.com/baem-oss/THEOAgent/blob/drs-ki-test/docs/drs-ki/README.md).

## Dokumentation

- [Requirements-Baseline v1.2.0 (freigegeben)](docs/requirements/BASELINE.md)
- [Theologischer Fachstandard – Ausgangsreferenz zu RANF-04](docs/requirements/THEOBald_Fachstandard.md) · SHA-256 `cc5a4dd89eb2279ba61fea105eea33ce45767b783eb572475fef9903c778174c`
- [Traceability-Matrix: User Stories → funktionale Anforderungen](docs/requirements/TRACEABILITY.md)
- [Abnahmeprofil für den MVP und offene Qualitätsgrenzwerte](docs/requirements/ACCEPTANCE_PROFILE.md)
- [Historische Bestandsaufnahme der THEOBald-Komponenten (10.11.2026)](docs/architecture/COMPONENT_INVENTORY.md)
- [Projektprozess, SSOT und Rollen](https://github.com/baem-oss/THEOAgent/blob/main/docs/WORKFLOW.md)

| Kategorie | Anzahl |
|---|---:|
| User Stories (US) | 27 |
| Funktionale Anforderungen (FANF) | 34 |
| Nichtfunktionale Anforderungen (NFANF) | 13 |
| Randbedingungen (RANF) | 6 |
| Fachregeln (GR) | 18 |
| Sicherheits- und Datenschutzanforderungen (SP) | 5 |
| Datenanforderungen (DAT) | 4 |

Der Fachstandard ist die unveränderte THEOBald-Referenz, die in RANF-04 über ihre Prüfsumme identifiziert ist. Die fachliche Festlegung als verbindlicher THEOAgent-Standard steht aus.

**Rolle:** Nutzer von THEOAgent.

**Anforderungsformulierung:** Funktionale Anforderungen nach SOPHIST-FunktionsMASTER, nichtfunktionale Anforderungen nach EigenschaftsMASTER. Fehlende Grenzwerte sind als offen gekennzeichnet.

**Status:** Requirements-Baseline v1.2.0 am 10.11.2026 vom Product Owner fachlich freigegeben. Eine Abnahme von Implementierung, Produktqualität und Qualitätsgrenzwerten steht aus.

**Single Source of Truth:** Ausschließlich der versionierte, vom Product Owner freigegebene Repository-Stand ist verbindlich. Der QE prüft dokumentierte Git-Stände, legt aber weder Git-SHAs noch freizugebende Inhalte fest. Siehe [Projektprozess](https://github.com/baem-oss/THEOAgent/blob/main/docs/WORKFLOW.md).
