# Entwicklungshistorie: SourceGuard Web v0.2.0 – zunächst nur Webquellen

**Achtung:** Durch den aktuellen PO-Auftrag **überholt**: SourceGuard v0.2.0 unterstützt jetzt auch die Evidenzaufbereitung für die Fachbibliothek und geeignete DRS-Werkzeugauszüge. Gültiges Arbeitsprofil: [THEOAgent DEV – SourceGuard v0.2.0](THEOAGENT_DEV_SOURCEGUARD_V0_2_0_ARBEITSPROTOTYP.md). Die nachfolgenden früheren Aussagen zu ausschließlichem Webzugriff und Regressionen beschreiben den bisherigen Stand. Auf PO-Wunsch werden keine weiteren Tests erstellt.\n\n**Stand:** 14.11.2026 · **Branch:** `drs-ki-test`  
**Status:** Implementation im Repository, noch keine bestandenen Tests dieser generischen Revision auf DRS:KI DEV. **Keine Produktfreigabe.**

## Architekturentscheidung des PO

SourceGuard wird **nicht** auf KKK, CIC, Dei Verbum oder ein anderes Werk spezialisiert. Die im frühen Stand 0.2.0 vorhandenen KKK-spezifischen Funktionen `compare_kkk_2267_versions`, `_kkk_2267_classification` und `_kkk_2267_paragraph` sind vollständig entfallen. Die historische P-03-Dokumentation bleibt als Fehler- und Lernbefund erhalten, nicht als normative API.

## Tool-Oberfläche

- `read_source(url, section="")`: Nur HTTPS/konfigurierte Host-Allowlist, IP-Pinning, sichere Weiterleitungen, TLS, Timeout und Datenlimit; liefert Originaltextauszug sowie bei anzugebender Fundstelle `section_text`, `section_boundary`, `section_window_truncated`. Abschnittssuche ist **rein lexikalisch**, nummerierte Abschnitte mit/ohne Punkt sowie wörtliche Überschriften sind möglich. Mehrdeutige Locator-Matches ergeben `LOCATOR_AMBIGUOUS`, nicht einen zufällig gewählten Beleg.
- `compare_sources(url_a, url_b, locator)`: Ruft zwei URLs unabhängig ab, vergleicht nur die jeweiligen Abschnittstextfenster nach Whitespace-Normalisierung. Ergebnisse `SAME_TEXT`, `DIFFERENT_TEXT`, `INCOMPLETE`. **Keine Datierung, Editionsauthentifizierung oder semantische Gleichwertigkeitsprüfung.** Unterschiedliche Textfenster beweisen allein eine Textabweichung in der jeweiligen Extraktion.
- `verify_evidence(claim, url, locator)`: Prüft lediglich, ob der angegebene Claim **wörtlich** im abgerufenen Abschnitt steht. `QUOTE_FOUND` bedeutet ausdrücklich **keine semantische Verifikation** und bei gekürzten Textfenstern ist `QUOTE_NOT_FOUND_IN_EXCERPT` nicht abschließend.

`semantic_claim_verified=false` und `version_verified=false` sind in relevanten Ausgaben fest. Alle Toolfunktionen dienen der Evidenzbereitstellung; sie erzwingen nicht die Verwendung des Tools vor der finalen Modellantwort (**QE F-C1 offen**).

## Aktuelle Grenzen

- HTML-Text-Extraktion, **kein** PDF-Parser; Seitenzahlen/Druckeditionen nicht nachweisbar.
- Fundstellenformatierung variabel; Zeilenbeginn-Heuristik kann Fälle übersehen oder bei mehrfach wiederholten Überschriften bewusst als mehrdeutig zurückweisen.
- `section_boundary=NEXT_NUMBER` setzt voraus, dass direkt die numerisch folgende Absatznummer existiert; wo nicht, lautet der Status `DOCUMENT_END_OR_UNKNOWN`. Der Text ist dort **nicht** automatisch ein vollständiger Abschnitt.
- Echte semantische Claim-Prüfung, Versionsauthentizität und Pipeline-Gate sind **nicht** Teil dieser Tool-Version.
- Frühere DEV-Ergebnisse mit der alten v0.2.0-KKK-Funktion sind **nicht** regressionsgültig für diese neue v0.2.0.

## Installation auf DEV

1. Bestehende Werkzeugfassung als Sicherung exportieren; das neue v0.2.0 ersetzt die alte **im DEV-Werkzeugeditor**.
2. Den vollständigen [Python-Code](../../tools/drs_ki/sourceguard_web_poc_v0_2_0.py) in **Arbeitsbereich → Werkzeuge** übernehmen, speichern und dem DEV-Modell zuweisen. Vorheriges `compare_kkk_2267_versions` ist danach **nicht mehr verfügbar**; Modellkonfiguration auf neue Funktionen abstimmen.
3. Die Valves unverändert lassen, sofern der benötigte Host bereits freigegeben ist. `Faster – No Summary` für Quellensuche beibehalten.
4. [Offline-Tests](../../tests/drs_ki/test_sourceguard_web_poc_v0_2.py): `python -m unittest discover -s tests/drs_ki -p 'test_sourceguard_web_poc_v0_2.py' -v` (noch nicht als ausgeführt belegt).

## DEV-Testmatrix (werkunabhängig)

| Test | Eingabe | Erwarteter Nachweis |
|---|---|---|
| G-01 | `read_source`, Vatikan-Dei-Verbum, `section="12"` | `TEXT_RETRIEVED`; Nr. 12 lesbar; Abschnittsgrenze begründet oder offen |
| G-02 | `read_source`, ältere KKK-Seite, `section="2267"` | Nr. 2267 ohne Punkt lexikalisch gefunden |
| G-03 | `compare_sources`, ältere und geänderte KKK-URL, `locator="2267"` | Textabweichung als `DIFFERENT_TEXT` nur bei hinreichendem Fenster; **kein** vorgebliches Editionsjahr |
| G-04 | `read_source`, amtlicher CIC, passender Canon-Locator | Locator tatsächlich gefunden, kein rein erfundenes Zitat |
| G-05 (negativ) | `read_source`, nicht vorhandene Nummer | `SECTION_NOT_LOCATED` |
| G-06 (negativ) | Mehrfach vorkommender identischer Abschnitts-Locator am Zeilenanfang | `LOCATOR_AMBIGUOUS` statt beliebiger Treffer |
| G-07 (negativ) | `verify_evidence` mit abweichender Paraphrase | Kein `semantic_claim_verified=true` |
| G-08 (Security) | Nicht erlaubte Hosts, Redirect zu internem IP-Ziel | technischer Fehler statt Abruf |

**Abnahmebedingung:** Die generischen Offline-Regressionen und die DEV-Liveproben müssen noch ausgeführt und protokolliert werden. Keine Änderung an der PO-freigegebenen Requirements-Baseline.
