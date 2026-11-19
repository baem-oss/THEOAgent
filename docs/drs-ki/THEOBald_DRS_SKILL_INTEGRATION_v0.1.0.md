# THEOBald DRS – Skill-Integration und Grenzen (Entwurf v0.1.0)

**Stand:** 11.11.2026. **Zielplattform:** DRS:KI „Allrounder“ mit benutzerseitig bearbeitbarem Systemprompt, Datei-Uploads und sichtbaren nativen Funktionen; ohne Adminrechte, ohne nachgewiesenes Skill-Management oder Fachbibliothek-Zuordnung. **Status:** konzeptionell, ungetestet; bestehende T-01…T-08-Baseline bleibt unangetastet. **Prompt:** [THEOBald_DRS_SYSTEMPROMPT_v0.1.0.md](THEOBald_DRS_SYSTEMPROMPT_v0.1.0.md)

## Quellen für die Übernahme

- THEOBald: `openwebui/system_prompt_modular_candidate.md` (Testkandidat v0.2)
- THEOBald: `skills/theologische-grundlagen/SKILL.md`
- THEOBald: `skills/exegese-homiletischer-arbeitsgang/SKILL.md`
- THEOBald: `skills/homiletik/SKILL.md`
- THEOBald: `skills/liturgische-texte/SKILL.md`
- THEOBald: `skills/pastorale-sensibilitaet/SKILL.md`
- THEOBald: `skills/qualitaetskontrolle/SKILL.md`
- THEOBald: `skills/theologische-quellenpruefung/SKILL.md`

Die Original-Skills stehen in `baem-oss/THEOBald`, nicht als freigeschaltete Features auf DRS. Aus dem lokalen Quellenprüfungs-Skill wurden die Grundsätze übernommen, **nicht** dessen native Tool-Signaturen, Indexzeilen-Konventionen, automatischen 160-Zeilen- oder acht-Tool-Regeln. Der Prompt behauptet keine auf DRS nicht nachgewiesene API.

## Integrierbarkeit

| Skill | Fachlicher Kern im Systemprompt | Separater DRS-Skill nötig? | Einschränkung |
|---|---|---|---|
| `theologische-grundlagen` | ja | nein | aktueller Normstand weiterhin extern prüfen |
| `exegese-homiletischer-arbeitsgang` | ja | nein | Fachliteratur nur bei tatsächlichem Zugriff |
| `homiletik` | ja | nein | Qualitätsurteil weiterhin Modellleistung |
| `liturgische-texte` | ja | nein | bindende liturgische Normen nur nach Prüfung |
| `pastorale-sensibilitaet` | ja | nein | kein Ersatz für professionelle Hilfsstellen |
| `qualitaetskontrolle` | ja | nein | reine Selbstprüfung, keine formale Garantie |
| `theologische-quellenpruefung` | Grundregeln ja | eigenständiger Skill bei verfügbarer Skillverwaltung optional | Originallesen, Webseiten-Verifikation und Seitennachweis hängen von echten Werkzeugen ab |

## Technische Optionen – keine unbestätigten Plattformfähigkeiten voraussetzen

**Option A (sofort ohne Adminrechte, empfohlen):** Alle sieben Kernverfahren als kondensierte Abschnitte im benutzerseitig bearbeitbaren Systemprompt. Es entsteht **kein ausführbarer Skill** und keine automatische Tool-Berechtigung. Dies ist gegenwärtig der einzige auf DRS belegte, eigenständig kontrollierbare Integrationsweg.

**Option B (falls der Nutzer eine Skill-Verwaltung sieht):** Originaldateien als eigenständige Skills importieren, den Systemprompt als verbindliche Kurzfassung behalten, Verfügbarkeit von `view_skill` und tatsächliche Skillaktivierung getrennt nachweisen. Die derzeitige DRS-Berechtigung dazu ist **nicht belegt**; deshalb keine Importzusage.

**Option C (durch DRS-Administratoren):** Modellgebundenes THEOBald-Profil mit persistent zugeordneter Fachbibliothek, Skills und kontrollierten Werkzeugen. Auf aktuellem Konto nicht selbst umsetzbar.

## Warum nicht Originalprompt + alle Skills unverändert anhängen?

- Der lokale THEOBald-Prompt setzt teils `grep_knowledge_files`, `view_knowledge_file`, native Skill-Verwaltung und Fachbibliothek voraus; DRS zeigt nicht alle dieser Ressourcen.
- Redundante, zu lange Instruktionen können die Prioritäten abschwächen.
- Ein Systemprompt kann keine echte Access-Control, dokumentenzuverlässige Extraktion, Web-Validierung oder unveränderliche Freeze-Speicherung erzwingen.
- Die DRS-Baseline zeigte 404-/nicht tragfähige URLs in T-08, fehlerhaften Uploadtext-Zugriff in T-04 und einen Freeze-Verstoß in T-05. Der neue Prompt adressiert Verhaltensentscheidungen, nicht die technische Ursache.

## Künftige kontrollierte Evaluation (ausgesetzt bis ausdrücklicher Start)

- Alte Baseline in neuen Chats, exakt gleiche Testprompts; daneben neue Chats mit DRS-Prompt; sonst identische Bedingungen.
- Vorab gleiche fachliche Orakel, keine Anpassung nach Sichtung.
- Primäre Kriterien: nicht erfundene Quellen, korrekter Verifikationsstatus; daneben Textänderungssicherheit, Unabhängigkeit.
- Das Ist-Modell und der Systemrollen-Vorrang sind im DRS-„Allrounder“ nicht einsehbar, deshalb als Unsicherheiten protokollieren.
- **Tests derzeit pausiert**. Keine aktiven Tests gestartet, keine produktive Freigabe, keine Änderungen an `main`.

## Änderungsstand

Entwurf `v0.1.0`. Alle sieben fachlichen Skill-Kerne in Promptform integriert, keine Behauptung einer technischen Skill-Installation. Produktentscheid über spätere Testfreigabe beim PO.
