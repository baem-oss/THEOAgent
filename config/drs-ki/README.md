# THEOAgent DRS:KI – aktueller Systemprompt, SourceGuard und Fachskills

**Dokumentationsstand: 19.11.2026.** Dieser Einstieg beschreibt den zuletzt vom PO gemeldeten **DRS:KI-DEV-Teststand**; er bestätigt keine unabhängige Synchronisierung mit der laufenden DEV-Instanz und keine Produktivfreigabe. `main` führt ab jetzt den aktuellen Repository-Stand. Ältere Versionen bleiben unverändert als Historie erhalten.

## Aktive Referenzen (DEV)

- **Systemprompt:** [THEOAgent DEV v0.3.11](../../docs/drs-ki/THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md). Der vollständige einzusetzende Prompt beginnt im Dokument nach der Abschnittsmarkierung `SYSTEMPROMPT – ab hier vollständig in THEOAgent DEV verwenden`.
- **SourceGuard:** [Version 0.2.3](../../tools/drs_ki/sourceguard_web_poc_v0_2_3.py), vier Werkzeugfunktionen. Ein technisch erzwungenes Output-Gate ist **nicht nachgewiesen** (F-C1 offen).
- **Websuche:** `Websuche_und_Dokument (Fast – Summary In One Go)` an; `Force_Tool_Usage` aus (zuletzt mitgeteilte DEV-Einstellung).
- **Fachbibliothek und Skills:** Unverändert gegenüber dem dokumentierten DEV-Stand; Originallektüre aus Knowledge bei bestimmten Anfragen weiterhin nicht zuverlässig.
- **Nachweise und Grenzen:** [Übergabestand 18.11.2026](../../docs/drs-ki/TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md).

## Sieben Fachskills

Die folgenden Dateien sind die aktuellen im Repository dokumentierten Skill-Fassungen. Die DEV-Anzeigenamen tragen das Präfix `THEOAgent - `.

- [Theologische Grundlagen](skills/theologische-grundlagen/SKILL.md)
- [Theologische Quellenprüfung](skills/theologische-quellenpruefung/SKILL.md)
- [Exegese–homiletischer Arbeitsgang](skills/exegese-homiletischer-arbeitsgang/SKILL.md)
- [Homiletik](skills/homiletik/SKILL.md)
- [Liturgische Texte](skills/liturgische-texte/SKILL.md)
- [Pastorale Sensibilität](skills/pastorale-sensibilitaet/SKILL.md)
- [Qualitätskontrolle](skills/qualitaetskontrolle/SKILL.md)

## Verwendung und Status

1. Die vollständige v0.3.11-Fassung verwenden, nicht den historischen [Systemprompt v0.3.0](SYSTEMPROMPT_v0.3.0.md).
2. Die sieben Skills im DRS:KI-Modellprofil separat zuweisen. Die Repository-Dateien allein aktivieren keine Skills im Zielsystem.
3. SourceGuard 0.2.3 und die genannten Web-/Knowledge-Werkzeuge in der tatsächlichen DEV-Konfiguration abgleichen. Keine automatische Installation oder Versionsübernahme aus GitHub behaupten.
4. Offene Qualitätsbefunde [F-C1, WEB-01, KNOW-01](../../docs/drs-ki/TESTSTAND_KNOWLEDGE_WEBSUCHE_SOURCEGUARD_2026-11-18.md) bleiben bestehen.

Der [THEOBald-Fachstandard](../../docs/requirements/THEOBald_Fachstandard.md) ist die Ausgangsreferenz aus RANF-04; die Requirements-Baseline v1.2.0 bleibt unverändert freigegeben.
