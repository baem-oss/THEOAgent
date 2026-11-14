# SourceGuard Web v0.2.0-dev – Installation und Abnahme auf DRS:KI DEV

**Datum:** 13.11.2026 · **Branch:** `drs-ki-test`  
**Status:** Entwicklungsversion, **nicht** produktiv freigegeben  
**Bezug:** [P-03a KKK 2267](POC_P-03A_KKK2267_VERSIONSBEFUND_2026-11-13.md), [F-C1/F-C2](SCHNITTSTELLENPRUEFUNG_AK-02_F-C2.md).

## DEV-Befund P-03b (14.11.2026) – erste Ausführung

**Tatsächlicher Toolaufruf:** `compare_kkk_2267_versions(historical_url, current_url)` auf THEOAgent DEV. Ausgabe: `status=INCOMPLETE`, erster Unterabruf `SECTION_NOT_LOCATED`; der zweite Unterabruf wurde wegen Fail-Closed nicht gestartet. THEOAgent hat das korrekt offengelegt.

**Ursache:** Die vorherige Regex in `read_source` suchte nach `2267` mit nachfolgendem Satzzeichen. Auf der amtlichen älteren KKK-Webseite lautet die Originalstelle `2267 Soweit unblutige Mittel ...` (ohne Punkt). Daher false negative bei der Lokalisierung, **kein** gesicherter Abruffehler. Korrektur am 14.11.2026 in `tools/drs_ki/sourceguard_web_poc_v0_2_0.py` (Commit `7eaab7a`), Regressionstest ergänzt (Commit `9cba78c`).

**Folge:** Das zuvor auf DEV installierte Tool ist **noch nicht aktualisiert**. Die korrigierte Datei erneut vollständig in den Werkzeugeditor übernehmen, speichern, und P-03b wiederholen. Tests sind vorbereitet, aber nicht als lokal/CI ausgeführt bestätigt. **P-03b: FAIL bis erneut getestet.**

## Änderungen gegenüber v0.1.0

1. `read_source(url, section)` bleibt als API bestehen. HTML/Text wird mit BOM, deklariertem HTTP-/Meta-Charset und Fallbacks in strikter Decodierung gelesen; ersetzt fehlerhafte Zeichen nicht stillschweigend durch `�`. **Die genaue Ursache der Umlaute beim Test mit IntraText ist noch nicht live verifiziert**.
2. Zusätzliche Methode `compare_kkk_2267_versions(historical_url, current_url)` ruft beide URLs unabhängig über dasselbe geprüfte HTTPS-/DNS-/Allowlist-Verfahren ab und prüft charakteristische Formulierungen. Ausgaben:
   - `VERSION_CONFLICT`: vermeintlich historische Seite enthält ebenfalls die Formulierung seit 2018;
   - `DISTINCT_WORDINGS_OBSERVED`: verschiedene Wortlaute vor/nach 2018 erkannt, aber **kein Editionsjahr bewiesen**;
   - `VERSION_UNDETERMINED` oder `INCOMPLETE`: kein verlässlicher Versionsvergleich.
3. Die Methode meldet `version_verified=false` und `semantic_claim_verified=false` **immer**. Eine Jahreszahl lässt sich nicht aus URL, HTML-Titel oder dem Wortlautmuster allein historisch beweisen.
4. Keine neue Berechtigung, keine Abhängigkeit von Embeddings, keine zusätzlichen Drittbibliotheken gegenüber v0.1.0. Tool ist **keine** Pipe.

## Drei Originalquellen für die DEV-Prüfung

| Rolle | URL | Interpretation |
|---|---|---|
| **Historischer Wortlaut-Kandidat, amtlicher Vatikan-Host** | `https://www.vatican.va/archive/catechism_ge/p3s2c2a5_ge.htm` | Früherer KKK-Text zu Nr. 2267 („Soweit unblutige Mittel ...“); genaues Editionsjahr **nicht** durch die URL bewiesen |
| **Neufassung 2018, Vatikan** | `https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_20180801_catechismo-penadimorte_ge.html` | Amtliche deutsche Veröffentlichung der Änderung |
| **Negativkontrolle / falscher Historien-Kandidat** | `https://www.vatican.va/archive/DEU0035/__P86.HTM` | Im DEV-Test vom 13.11.2026 trotz Archivtitel „1997“ bereits mit Neufassung 2018, daher **nicht** historischer Wortlaut |

Unterstützend für die frühere Lehre: amtliches [Schreiben der Glaubenskongregation 2018](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_20180801_lettera-vescovi-penadimorte_ge.html), insbesondere Nr. 3; dies ist **nicht** der vollständige alte KKK-Absatz.

## Installation (nur DRS:KI DEV)

1. **Vorher:** Vorhandenen Werkzeugcode der funktionierenden v0.1.0 lokal sichern. Keine Änderung am Produktivmodell.
2. Unter **Arbeitsbereich → Werkzeuge** das DEV-SourceGuard-Webwerkzeug bearbeiten. Den vollständigen Inhalt von [`tools/drs_ki/sourceguard_web_poc_v0_2_0.py`](../../tools/drs_ki/sourceguard_web_poc_v0_2_0.py) in den Codeeditor übernehmen und speichern. Alternativ unter neuem Namen anlegen, wenn v0.1.0 als Rückfall erhalten bleiben soll.
3. In **THEOAgent DEV → Modell bearbeiten** die neue Werkzeugfassung zuweisen, `Faster – No Summary` für Recherche belassen. Valves: `www.vatican.va` bereits standardmäßig erlaubt, zunächst unverändert lassen.
4. Die Rohantworten der Toolaufrufe vollständig anzeigen und protokollieren. **Keine** reine Modellzusammenfassung als Nachweis verwenden.

## P-03b Positivprobe

> Rufe ausschließlich `SourceGuard Web.compare_kkk_2267_versions` auf.  
> `historical_url=https://www.vatican.va/archive/catechism_ge/p3s2c2a5_ge.htm`  
> `current_url=https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_20180801_catechismo-penadimorte_ge.html`  
> Melde wortgetreu `status`, die beiden `classification`-Werte, `boundary_method`, `version_verified` und `semantic_claim_verified`. Erläutere, warum dies **kein vollständiger editionshistorischer Beweis** ist. Verwende keine Websuche.

**Erwartung bei geeigneten Live-Texten:** `DISTINCT_WORDINGS_OBSERVED`, `PRE_2018_WORDING` und `POST_2018_WORDING`, `version_verified=false`.

## P-03c Negativprobe

> Rufe ausschließlich `SourceGuard Web.compare_kkk_2267_versions` auf.  
> `historical_url=https://www.vatican.va/archive/DEU0035/__P86.HTM`  
> `current_url=https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_con_cfaith_doc_20180801_catechismo-penadimorte_ge.html`  
> Nenne den technischen Status und entscheide, ob die erste URL den historischen Wortlaut belegt. Verwende keine Websuche.

**Erwartung, sofern gleichlautende Fassungen geliefert werden:** `VERSION_CONFLICT`. Auf fehlerfreie Umlaute achten. Falls ein Decode-/Abruffehler auftritt, `INCOMPLETE` statt fälschlich PASS.

## Regressionen und Status

Offline-Tests: `python -m unittest discover -s tests/drs_ki -p 'test_sourceguard_web_poc_v0_2.py' -v`

Diese Tests sind als Quellcode vorhanden, **nicht als erfolgreich ausgeführt dokumentiert**. DEV-Teststatus **OPEN**. Kein Release, bis Decode, Versionsfälle, SSRF-Regressionsfälle und unveränderter Dei-Verbum-Abruf geprüft sind. QE F-C1 (technisch erzwungene Prüfung aller Antworten) bleibt offen.

**Sicherheitsgrenze:** Weder Host-Allowlist noch DNS-/TLS-Pinning für Testzwecke entfernen. Kein DRS-Drittquellcode in das öffentliche Repository kopieren.
