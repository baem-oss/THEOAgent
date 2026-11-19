# Architekturvorschlag – THEOBald auf DRS:KI

**Status:** Entwurf zur QE-Prüfung, 13.11.2026. Grundlage: statische Einsicht in sieben verschiedene DRS:KI-Toolimplementierungen. Keine Laufzeitverifikation.

## Ziel und Constraints

THEOBald soll als theologischer Fachassistent für Exegese, Homiletik und Liturgie **ohne Administratorrechte** in der vorhandenen DRS:KI-Open-WebUI-Umgebung nutzbar sein. KISS; Vorrang vorhandener Dienste. Strenge Trennung von Quelle, textlicher Evidenz, theologischer Interpretation und Verbindlichkeitsgrad. Keine Quellensicherheit vortäuschen.

## Zielbild – minimaler Pilot

```text
Nutzerfrage
   |
THEOBald-Fachprompt (Exegese -> Homiletik -> Liturgie; Quellenregeln)
   |
   +-- Vorhandene DRS:KI-Werkzeuge (soweit für Account freigeschaltet)
   |     +-- Faster No Summary v2.1.0: offene Webrecherche, 5 Treffer, max. 4500 Zeichen je Seite
   |     +-- Single Domain v2.0.1: Bibelrecherche bibleserver.com; 3 Runden
   |     +-- Outline: exakte Suche in erlaubten Dokumentanhängen, PDF-Seitenangaben
   |     +-- TYPO3 / MediaWiki: DRS-interne Inhalte, nur bei vorhandenem Zugriff
   |
   +-- THEOBald-eigene Prüflogik zunächst als Prompt-/Prüfprotokoll
   |     +-- Nachweisstufe: Suchtreffer / gelesener Auszug / nachgeprüfte Fundstelle
   |     +-- Autorität: amtliche kirchliche Norm vs. informelle/wiki-Fachinformation
   |     +-- Lücken und Textkürzungen explizit markieren
   |
Nachprüfbare Antwort mit Belegen, Grenzen und Kennzeichnung theologischer Deutung
```

## Komponentenentscheidung

| Vorhandenes Tool | Pilotentscheidung | Begründung |
|---|---|---|
| Faster – No Summary v2.1.0 | Primäre Webrecherche, mit Grenzen | Liefert ungeglättete Auszüge, jedoch nur erste 4500 Zeichen; Snippet-Fallback |
| Single Domain Web Search v2.0.1 | Bibelrecherche testen | feste Suche auf BibleServer/Einheitsübersetzung 2016; LLM-Suffizienz keine Verifikation |
| Outline Document Tools v0.1.0 | Dokument- und Fundstellensuche, wenn URLs erlaubt | Originaltext; PDF-Seitenangaben; nur konfigurierte Hosts |
| TYPO3 Document Tools v0.3.2 | Optionaler DRS-Adapter | MCP-Vorabruf nötig, `query`/`max_hits_per_file` nicht umgesetzt, kein wirksames Gesamtbudget |
| MediaWiki MCP v1.5.0 | Optionaler DRS-Adapter | Wiki-Originalauszug bis 12000 Zeichen; informelle Quelle, keine amtliche Autorität |
| Fast – Summary v2.1.0 | Nur Überblicksfragen | Vorverdichtung verliert Belegdetails |
| Websuche/Dokument v2.0.0 | Ergänzende Recherche, nicht Beweisführung | dynamisches Nachladen bis 25 Kandidaten; gibt nur LLM-Synthese zurück |

## Eigene THEOBald-Komponenten – nur bei nachgewiesenem Bedarf

1. **Fachprompt und Arbeitsprotokoll**: Muss ohne Adminrechte als eigener Assistent/Modellkonfiguration oder nutzbarer Nutzer-Prompt erprobbar sein. Keine Annahme, dass Skills/Tools selbst installiert werden dürfen.
2. **SourceGuard-Prüfschritt**: Vorläufig promptgesteuerte Klassifikation `TREFFER`, `AUSZUG`, `ORIGINALTEXT_GEPRUEFT`, `NICHT_BELEGT`. `ORIGINALTEXT_GEPRUEFT` nur bei sichtbarer konkreter Passage mit geeigneter Fundstelle und dokumentiertem Prüfumfang. Keine eigene technische Toolintegration voraussetzen.
3. **Eigener Quellenadapter nur falls nötig und erlaubt**: Suche -> gezielter URL-/Dokumentabruf -> strukturierte Fundstelle -> Evidenzprüfung. Die DRS-Werkzeuge können nicht ohne Weiteres gegenseitig programmatisch aufgerufen werden; durch Agenten gesteuerte Aufrufe sind zunächst nur zu testen.

## Technische Anleihen für eigene Tools

- Outline: Seitenextraktion mit PyMuPDF und Kontextfenster-Suche; beachten: PDF-Seite != Druckseitenzählung.
- MediaWiki: MCP `search-page` -> `get-page`, Deduplizierung und explizite Quellenkennungen; Aktualität des MCP-Protokolls prüfen.
- Websuche v2.0.0: Kandidatennachladung bei Fehlabruf; Auswahl, Reihenfolge und Gründe protokollieren.
- Single Domain: Domainbindung, Rechercherunden und Suchverfeinerung; Suffizienz-LMM niemals als formale Quellenbestätigung.
- Faster v2.1.0: Typkennzeichnung Auszug vs. Snippet und Verzicht auf Quellenzusammenfassung.
- TYPO3: vorliegendes MCP-JSON als Inputadapter; keine zweite Dokumentextraktion duplizieren.

## Wesentliche Risiken und Prüftests

- Fehlende Rechte (Toolzuteilung, Promptkonfiguration, Knowledge/Skills, Tool-Valves); erst UI nachweisen.
- Dokumente und Webseiten können am Zeichenlimit abgeschnitten werden; fehlende Stelle ist kein Negativbeweis.
- `Single Domain` folgt Redirects automatisch und prüft Ziel-URL erst nach Abruf: nicht als Sicherheitsvorbild übernehmen.
- SSRF/DNS-Rebinding in mehreren Werkzeugen trotz DNS-Checks möglich; Netzwerk-Egress braucht separate Sicherung.
- TYPO3-Tool ignoriert Suchparameter; Kontextbudget über mehrere Dateien nicht durchgesetzt.
- Bibeltext: Vollständigkeit, Version und Nutzungsrechte bei BibleServer gesondert prüfen.
- Lizenzlage der fremden Quellcodes ungeklärt; technische Konzepte können als Referenz dienen, Codekopie erst nach Rechteprüfung.

## Pilotplan mit Entscheidungspunkten

**P0 Zugang prüfen:** tatsächliche Berechtigung zum Anlegen/Konfigurieren eines THEOBald-Assistenten; Toolzuweisung; vorhandene Modellwahl; keine Adminabhängigkeiten voraussetzen.

**P1 Quellenpipeline testen:** DV 12, KKK 2267, Lk 10,25–37; bei jedem Fall Quellenkategorie, Abrufart und Fundstellenqualität ausgeben.

**P2 Facheignung testen:** Homilie-Rechtsfrage, Lk 15, Mt 25 und liturgische Erstellung; Ausgabe getrennt nach belegter Aussage und homiletischer Anwendung.

**P3 Gap-Analyse:** Nur festgestellte Lücken als Anforderungen für eigene Tools formulieren; mit bestehenden lokalen SourceGuard-Funktionen abgleichen; Umsetzungsberechtigung klären.

**P4 QE-Abnahme:** Review der Testprotokolle und Architekturentscheidung, dann Dokumentation im GitHub-Branch `drs-ki-test`; GitHub bleibt SSOT.

## Nicht entschiedene Fragen

- Welche spezifischen Werkzeuge sind dem persönlichen Account tatsächlich zugänglich und aufrufbar?
- Gibt es Benutzerrechte für eigene Assistenten/Systemprompts/Knowledge und Toolkonfiguration?
- Sind Outline-Host-Allowlist und TYPO3-MCP-Zugriff eingerichtet?
- Welche tatsächlich installierten Modelle funktionieren mit den Tool Calls?
- Sind die verbliebenen nicht vorliegenden DRS:KI-Tools für Exegese/Liturgie relevant?

**Empfehlung:** Kein Fork der DRS:KI-Werkzeuge, kein sofortiger SourceGuard-Neubau. Zunächst ein THEOBald-Pilotprofil mit vorhandenen Tools, belastbare Testfälle und ein explizites Evidenzprotokoll. Erweiterungen nur nach dokumentiertem Defizit.