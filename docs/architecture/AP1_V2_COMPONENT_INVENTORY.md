# AP1 – Technische Bestandsaufnahme THEOAgent v2

Stand: 28.11.2026. Status: SE-Bestandsaufnahme abgeschlossen (statische Prüfung); AP2-Schnittstellennachweise offen. Keine Implementierung, kein neuer Laufzeittest, keine Produktabnahme.

## Quellen und Grenzen

- Verbindliche Baseline / Abnahmeprofil: [7021562](https://github.com/baem-oss/THEOAgent/tree/7021562d0d638455f29e37c8da156c130c5b6139).
- Historische Codebasis [local-dev 71a4c81](https://github.com/baem-oss/THEOAgent/tree/71a4c811b1f682e2ec3b3200836411de8adb016e): [dev5](https://github.com/baem-oss/THEOAgent/blob/71a4c811b1f682e2ec3b3200836411de8adb016e/tools/local_dev/sourceguard_pipe_v0_5_5_dev5.py) (Blob aa9903be3c3b3d1409cb52418b251cc058251596; 3719 Zeilen inkl. abschließender Leerzeile, 193642 Zeichen), [dev15](https://github.com/baem-oss/THEOAgent/blob/71a4c811b1f682e2ec3b3200836411de8adb016e/tools/local_dev/sourceguard_pipe_v0_5_5_dev15.py) (Blob ff749614933c5d1f9e2a6e02bac0afd59a4b6618; 4056 Zeilen, 221068 Zeichen). Beide Dateien vollständig per Connector abgerufen; Funktionsinventar und relevante Codebereiche statisch ausgewertet, keine lückenlose Sicherheitsprüfung.
- Historische [AP1-Abnahme](https://github.com/baem-oss/THEOAgent/blob/71a4c811b1f682e2ec3b3200836411de8adb016e/docs/reviews/2026-11-27-sourceguard-pipe/AP1-Abnahme.md), [QE dev12](https://github.com/baem-oss/THEOAgent/blob/71a4c811b1f682e2ec3b3200836411de8adb016e/docs/reviews/2026-11-27-sourceguard-pipe/QE-Review-dev12.md), PO-Entscheidung dev14, SE-Disposition dev3, test_ap1.py Funktionsinventar. Historische Befunde nicht als neue Tests zählen.
- [Frühere Komponentenaufnahme](COMPONENT_INVENTORY.md), [DRS-Konfiguration](../../config/drs-ki/README.md), [Prompt v0.3.11](../drs-ki/THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md), [Web-Tool 0.2.3](../../tools/drs_ki/sourceguard_web_poc_v0_2_3.py).
- HEADs vor AP1: main/dev-v2 7021562d0d638455f29e37c8da156c130c5b6139; local-dev 71a4c811b1f682e2ec3b3200836411de8adb016e; drs-ki-test 5d9ec669b9d3dcaadd9a58ceb57864b5b4546087. Kein Zugriff auf laufenden Homeserver. Live-Konfiguration nicht neu verifiziert.

## Historische Evidenz

dev5: PO-AP1-Abnahme 27.11.; Klippert initial 23.2225 s, 8 Modellrunden, 17 Werkzeuge, 4 registrierte Lesezugriffe; Folgefrage 16.6121 s, 5 Runden, 17 Werkzeuge, 3 registrierte Lesezugriffe. Promptpräfix 24836 Zeichen, sieben Skills im Inventar, ein Skill nachgewiesen geladen. Folgekontext und LOCAL_ONLY im getesteten Umfang übernommen. Kein Nachweis sämtlicher Skillaufrufe, providerseitiger vollständiger Promptverarbeitung oder fachlicher Vollprüfung. Historischer QE dev12 weist Formatbudget-/Verlaufprobleme nach; dev14-PO-Vermerk dokumentiert zwei dev13-Sperren trotz je vier registrierter Originalstellen. Historische Zweiphasenempfehlung bezog sich auf v1.2.0; keine Bindung für v2.

## Wiederverwendungsentscheidungen (SE)

| Komponente | Entscheidung | Fundstelle / Begründung |
|---|---|---|
| OpenWebUI Pipe, Benutzerkontext, Zielmodell | Übernehmen als Adaptermuster | dev5 3560–3690; dev15 3858–3917, 3953–3978; historisch erprobt; interner API-Vertrag versionsabhängig |
| Modelltransport | OpenWebUI generate_chat_completion als erste Option | Keine separate OpenRouter-HTTP-Integration; keine erzwungene Temperatur 0; native tool_calls noch nicht nachgewiesen |
| Skillmanifest und native Callables | Übernehmen, technisch prüfen | dev15 3918–3922, 3553–3575; keine eigene Skillverwaltung |
| Werkzeugargumente | Vereinfachen | dev15 3231–3276; Schema, gültige IDs, Fenster und Sicherheitsgrenzen; keine semantische Klassifikation |
| Dokumente und Knowledge | Native Plattform wiederverwenden | dev15 3590–3596, 3673–3688; Nutzeranhänge nicht pauschal entfernen; vollständige Bereitstellung aller vorgesehenen Formate noch offen |
| Ereignisse, Messwerte | Vereinfachen | dev15 3293–3307, 3956–3978; alle tatsächlichen Aufrufe einschl. Fehler/Abweisungen erfassen; keine Rohtexte/Geheimnisse in Diagnose; keine Zählung bloßer Modellbehauptung |
| Evidenzregister | Einfaches Register der tatsächlich zurückgegebenen und ans Modell übergebenen Textpassagen | dev15 3673–3688, 3721–3735; Datei/URL, echte Rückgabegrenzen, Aufruf-ID, Status; keine geschätzte Druckseite oder Absatznummer als verifiziert; Suche/TOC/Skill keine tragfähige Originallektüre |
| Kontext und Provenienz über Folgefragen | Überarbeiten | dev15 3928–3951; keine pauschalen 4000/12000-Zeichenverluste; frühere Belege eindeutig zuordnen oder Nichtverfügbarkeit offenlegen; keine neue DB voraussetzen |
| Quellenanzeige | Überarbeiten | dev15 3815–3856; kein globaler Freigabestatus, keine pauschale Regex-Entfernung; kompakte Herkunft und explizite Nachweise gemäß N0–N4 |
| Freeze | Neu: kleinster eindeutig adressierbarer Schutz | Keine gesicherte technische Altimplementierung nachgewiesen; keine semantische Änderungsdetektion versprechen |
| Webschutz | Native Schutzwirkung prüfen, vorhandenen sicheren Abruf als Reserve | dev15 1986–2007, 3692–3695; Web-Tool 0.2.3 107–169, 349–412 bietet DNS/IP-Pinning, TLS, Redirect-, Größen- und MIME-Kontrollen; HTML/Text und Host-Allowlist begrenzen Einsatz. Kein gesamtes Tool übernehmen, keine globale Allowlist für fachliche Recherche erzwingen. |
| Fehlerbehandlung | Neu ausrichten auf F-06 | dev15 3775–3777, 3873–3883, 4019–4022; betroffene unzulässige Aktion sperren, erlaubte Teilleistung erhalten; vollständiger Pipe-Ausfall kein Bypass |
| Legacy und AGENT_TEST_MODE | Nicht übernehmen | dev15 1–1844 und 4030–4055; zwei Pipelines unnötig |
| Klassifikatoren, coverage, globale Antwortgates | Nicht übernehmen | dev15 3095–3214, 3347–3366; RANF-07 |
| Obligatorische Werkidentitäts-/Kontext-Zweitlektüre | Nicht übernehmen | dev15 3615–3668; Modell entscheidet Recherchebedarf; belegbare Identität/Quellengrenzen bleiben Pflicht |
| Eigenes Steuerungs-JSON / getrennte Antwortphase | Native Alternative priorisiert; Ablösung noch nicht nachgewiesen | dev15 1888–1931, 3953–4008; keine zusätzliche Antwortphase erzwingen; AP2-Schnittstellenspike entscheidet; keine Wiederbelebung restriktiver Gates |
| Alte Tests | Als Historie und gezielte Regression wiederverwenden | local-dev tests/local_dev; alte Gate-Erwartungen nicht als neue Akzeptanz übernehmen |

## Findings

1. Automatische zusätzliche Kontextlektüre und Werkidentitätsaufrufe erhöhen Aufwand; tatsächlicher fachlicher Nutzen nicht pauschal belegt. Werkidentitäts-Hilfsaufruf läuft in dev5 verify_named_work direkt über Callable und ist nicht durch einen einheitlichen Ereigniswrapper garantiert erfasst.
2. HTTPS-Syntaxprüfung der lokalen Pipe allein verhindert keine DNS-Umbindung oder Redirect-Zugriffe; nachträglicher URL-Abgleich kommt zu spät. Native Schutzwirkung offen. Vorhandener DRS-Downloader kann als Reserve dienen.
3. Aus Suchergebnissen extrahierte bekannte Datei-ID ist keine ACL. Autorisierung vor Zugriff anhand Plattform-/Betreiberrechte prüfen; kein Vertrauen in Modellmetadaten.
4. Alte Kontextbegrenzung und Austausch von Belegkennungen verlieren Information; Provenienz für Folgefragen fehlt als zuverlässig adressierbarer Bestand.
5. Globaler Freigabestatus ist trotz Disclaimer keine semantische Verifikation. Nur konkrete technische Tatsachen berichten; Leseabruf, tatsächlich an das Modell gelieferte Passage, Zuordnung und fachliche Tragfähigkeit getrennt.
6. Fachliche Konfiguration kann nicht blind unverändert übernommen werden: DRS-Prompt v0.3.11 enthält explizite Verträge für read_source/review_evidence und einen Nutzer-Workaround zur optionalen SG-Aktivierung. Für v2 technische Widersprüche minimal bereinigen, fachliche Regeln und sieben Skills zunächst erhalten; Skills auf dieselben veralteten Schnittstellen gezielt prüfen (AP2/AP3, AP5 für fachliche Überarbeitung). Live-Prompt nicht als identisch mit Repositoryfassung unterstellen.

## AP2: offene Schnittstellennachweise und Entscheidungen

- Kleine native Tool-Calling-Probe im obligatorischen Pipe-Pfad (konfigurierte OpenWebUI-Version, bereitgestelltes Referenzmodell, harmloser synthetischer Callable): tool_calls, Call-ID, tool result, abschließender Text; Nachweis realer Ausführung. Keine erneute isolierte SG-Erreichbarkeitsprüfung, kein Benchmark.
- Tatsächliche verfügbare Tool-Schemas/Callables, Systemprompt-/Skill-/Datei-Kontext, ACL und SSRF-Schutz der nativen Wege feststellen. Nicht verifizierte Netzwerk-/Zugriffsaktionen nicht freischalten.
- Q-11: prüfen, ob bereitgestelltes Zielmodell und Quellenanzeige durch W2 konfigurierbar sind; bisherige administrative Pipe-Valves sind kein Nachweis. Keine globale Adminänderung als Voraussetzung für fachliche Standardänderung.
- Referenzumgebung laut historischer Dokumentation: OpenWebUI 0.11.4, google/gemma-4-31b-it über direktes OpenRouter; PO muss aktuelle Konfiguration für Probe bestätigen, wenn erforderlich. Kein Modellwechsel ohne Grund. Keine privaten Texte in Probe.
- Freeze-/Provenienzmechanismus ohne zusätzliche DB spezifizieren. Fehlerreaktion ohne globale Sperre; keine Pflichtrecherche, keine neue semantische Klassifikation, maximal eine begründete zusätzliche Korrekturphase.
- AP2-Zielarchitektur danach Claude zum fokussierten Review vorlegen. Keine QE-Freigabehoheit.

AP1 liefert die Wiederverwendungsentscheidungen; native Tool-Calling, aktuelle Live-Konfiguration und Schutzwirkung sind AP2-Nachweise, keine bereits bestandenen Tests. Keine Änderung historischer Artefakte oder freigegebener Requirements.
