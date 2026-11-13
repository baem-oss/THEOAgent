# THEOAgent DRS:KI – Systemprompt und Skills getrennt

**Stand:** 13.11.2026 · **Status:** PoC-Konfiguration, keine Abnahme  
**Ziel:** DRS:KI DEV, Developerzugriff; Endnutzer ruft nur das fertig konfigurierte Modell auf.

## Dateien

- [Systemprompt v0.3.0](SYSTEMPROMPT_v0.3.0.md): eigenständiger, kompakter Orchestrierungs- und Sicherheits-Prompt.
- [Theologische Grundlagen](skills/theologische-grundlagen/SKILL.md)
- [Theologische Quellenprüfung](skills/theologische-quellenpruefung/SKILL.md)
- [Exegese–homiletischer Arbeitsgang](skills/exegese-homiletischer-arbeitsgang/SKILL.md)
- [Homiletik](skills/homiletik/SKILL.md)
- [Liturgische Texte](skills/liturgische-texte/SKILL.md)
- [Pastorale Sensibilität](skills/pastorale-sensibilitaet/SKILL.md)
- [Qualitätskontrolle](skills/qualitaetskontrolle/SKILL.md)

## Herkunft und Kompatibilität

Die sieben SKILL.md-Dateien wurden **unverändert** aus `baem-oss/THEOBald` Branch `review/sourceguard-integrated-v0.5.5-dev3` nach `baem-oss/THEOAgent` übernommen. Deshalb nennen manche Dateien weiterhin **THEOBald**; es handelt sich um die dokumentierte Herkunft der Fachstandards. Der Systemprompt ist dagegen eine neue, für THEOAgent auf DRS:KI geschriebene Fassung.

**Wichtiger offener Punkt:** Der Originalskill `theologische-quellenpruefung` enthält konkrete native Open-WebUI-Toolnamen (`grep_knowledge_files`, `view_knowledge_file`), Lesezeilen- und Aufrufbudgets und lokal dokumentierte Testanker. Dies setzt **keine** entsprechende Funktion auf DRS:KI voraus. Vor produktivem Einsatz ist die Anpassung an die tatsächlich zugewiesenen DRS:KI-Werkzeuge und die bestehende SourceGuard-Evidenzprüfung erforderlich. Keine Änderung der Fachregeln aus stillschweigender Toolkompatibilität ableiten.

Die SKILL-Dateien werden **nicht** dadurch ausgeführt, dass sie im Repository liegen oder im Systemprompt erwähnt werden. Sie müssen im DEV-System als Skills tatsächlich verfügbar gemacht und dem Modell zugewiesen werden. Eine Verfügbarkeit von separatem Skill-Management ist noch nicht getestet. Falls diese Funktion im DRS:KI DEV fehlt, muss die konkrete Alternative **bewusst** geplant werden – nicht behaupten, sieben Skills seien installiert.

## Einrichtung in DEV

1. Eigenständiges Modell `THEOAgent DEV` anlegen.
2. Inhalt von `SYSTEMPROMPT_v0.3.0.md` (ohne den Markdown-Dokumenttitel) als Systemprompt setzen.
3. Sieben `SKILL.md` **separat** importieren und zuweisen, falls die DRS:KI-Skillverwaltung dies unterstützt.
4. Vorhandene Knowledge- und Such-/Dokumentwerkzeuge modellgebunden konfigurieren.
5. Mit einem testbaren Quellenauftrag starten und tatsächliche Skill- sowie Toolaufrufe dokumentieren.

**PoC-Grenze:** Ohne wirksam integrierten SourceGuard keine technisch durchgesetzte Belegverifikation behaupten. Der unveränderte historische Prompt v0.2.3 ist ein anderer, integrierter Ansatz und soll nicht zusätzlich als zweiter Systemprompt geladen werden.
