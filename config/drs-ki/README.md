# THEOAgent DRS:KI – Systemprompt und Fachskills

**Stand 15.11.2026.** Die Anleitung gilt für DRS:KI DEV mit Developerzugriff. Endnutzer rufen das bereitgestellte Modell auf.

## Dokumentierte DEV-Konfiguration

- [Systemprompt v0.3.2](../../docs/drs-ki/THEOAGENT_DEV_SYSTEMPROMPT_v0.3.2.md)
- [SourceGuard v0.2.0 und die Werkzeuge des DEV-Profils](../../docs/drs-ki/THEOAGENT_DEV_SOURCEGUARD_V0_2_0_ARBEITSPROTOTYP.md)
- [Erprobungsstatus und Konfigurationsstand](../../docs/drs-ki/README.md)

## Fachskills

- [Theologische Grundlagen](skills/theologische-grundlagen/SKILL.md)
- [Theologische Quellenprüfung](skills/theologische-quellenpruefung/SKILL.md)
- [Exegese–homiletischer Arbeitsgang](skills/exegese-homiletischer-arbeitsgang/SKILL.md)
- [Homiletik](skills/homiletik/SKILL.md)
- [Liturgische Texte](skills/liturgische-texte/SKILL.md)
- [Pastorale Sensibilität](skills/pastorale-sensibilitaet/SKILL.md)
- [Qualitätskontrolle](skills/qualitaetskontrolle/SKILL.md)

Die Skills gehen auf `baem-oss/THEOBald`, Branch `review/sourceguard-integrated-v0.5.5-dev3`, zurück. Für die Erprobung gilt der auf `drs-ki-test` dokumentierte Stand der sieben Skills, einschließlich der [Mehrkriterien-Abbruchregel](skills/theologische-quellenpruefung/SKILL.md). Die DEV-Anzeigenamen tragen das Präfix `THEOAgent - `.

## DEV-Konfiguration abgleichen

1. Den im [Systemprompt v0.3.2](../../docs/drs-ki/THEOAGENT_DEV_SYSTEMPROMPT_v0.3.2.md) bezeichneten Prompt-Abschnitt als zusammenhängende Arbeitsfassung verwenden.
2. Die sieben Fachskills im Modellprofil separat zuweisen. Ältere Werkzeugnamen in den Skilltexten mit den tatsächlich verfügbaren DEV-Werkzeugen abgleichen.
3. Die Modellzuordnung der Knowledge-, Such- und Dokumentwerkzeuge sowie von SourceGuard anhand des [Arbeitsprofils](../../docs/drs-ki/THEOAGENT_DEV_SOURCEGUARD_V0_2_0_ARBEITSPROTOTYP.md) prüfen.

Der exakt auf DEV eingetragene Stand ist nicht unabhängig bestätigt. SourceGuard bereitet Evidenz auf. Die fachliche Beurteilung der Behauptung erfolgt durch THEOAgent. Der [THEOBald-Fachstandard](../../docs/requirements/THEOBald_Fachstandard.md) ist die Ausgangsreferenz aus RANF-04.

Der [Systemprompt v0.3.0](SYSTEMPROMPT_v0.3.0.md) dokumentiert den früheren PoC-Stand.
