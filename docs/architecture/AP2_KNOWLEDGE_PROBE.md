# AP2.2b – Integrierte native Werkzeugausführung

Stand 28.11.2026. Referenzumgebung PO-bestätigt: OpenWebUI 0.11.4, Gemma 4 31B IT, OpenRouter direkt, Raspberry Pi 5. AP2.1 und AP2.2a PASS laut PO-Protokollen. Diese Probe ist kein Produktivcode.

## Installation

Separate Function als Pipe mit ID theoagent_v2_knowledge_probe und Anzeigename THEOAgent v2 – Knowledge Integration Probe anlegen. Code tools/local_dev/native_knowledge_probe_v2.py einfügen, speichern, aktivieren, nicht global. Separates Modellprofil auf Basis dieser Pipe erstellen. Vorhandene sieben Fachskills und die für diesen Test zulässige Knowledge-Sammlung zuweisen; keine weiteren Sammlungen oder Nutzerdokumente. Kein alter SourceGuard-Systemprompt mit proprietärem Toolvertrag erforderlich. Valves TARGET_MODEL_ID auf tatsächlich bereitgestellte ID prüfen. AUTHORIZED_TEST_DATA nur aktivieren, wenn die zugewiesenen Inhalte einschließlich Skills und Buchauszügen für die konkrete Übermittlung an den Provider freigegeben sind. Andernfalls synthetischen Testbestand verwenden. Formale Datenschutzklärung lokal zurückgestellt; keine pauschale Rechtefreigabe abgeleitet. Keine privaten Gesprächsdaten eingeben. Kein Webtool in der Probe exponiert.

Neuer Chat, Prompt:

> Welche wissenschaftstheoretischen Grundsätze kennzeichnen nach Christoph Böttigheimer das Verhältnis von Glaube und Vernunft bei Thomas von Aquin? Nutze ausschließlich Böttigheimers Originalwerk aus deiner Fachbibliothek. Erläutere die Ergebnisse in eigenen Worten und nenne die konkreten Fundstellen.

Vollständige Antwort und JSON-Diagnose an SE übermitteln; keine Rohtexte der Tool-Rückgaben zusätzlich veröffentlichen.

## Vorab festgelegtes fachliches Prüforakel

Referenz: Christoph Böttigheimer, Lehrbuch der Fundamentaltheologie. Die Rationalität der Gottes-, Offenbarungs- und Kirchenfrage, 4. Aufl., Herder 2022. Vom PO bereitgestelltes PDF, 886 Seiten; Buchseiten 43–45 entsprechen PDF-Seiten 44–46. Abschnitt Grundlegung I.1.2 b. Die folgenden paraphrasierten Kernaussagen sind anhand dieses Abschnitts geprüft. Keine Originalpassagen im Repo.

| ID | Erwartete Kernaussage | Buchseite |
|---|---|---|
| K1 | Thomas nutzt den aristotelischen Wissenschaftsbegriff, ohne Offenbarung auf Vernunfterkenntnis zu reduzieren. | 43 |
| K2 | Christliche Theologie setzt im frei angenommenen Offenbarungsglauben an; sie ist eine der göttlichen Wissenschaft untergeordnete Wissenschaft. | 43–44 |
| K3 | Glaubensartikel fungieren als Prinzipien rationaler, argumentativer, intersubjektiv vermittelbarer Erkenntnis. | 44 |
| K4 | Philosophische Theologie arbeitet aus Vernunftprinzipien, Glaubenswissenschaft aus Offenbarung; beide besitzen eigenes Existenzrecht. | 44–45 |
| K5 | Vernunft und Glauben haben unterschiedliche Vorrangbereiche (Wissen bzw. Heil); Philosophie und Theologie stehen in notwendiger Verbindung, ohne identisch zu sein. | 45 |

Weitere zutreffende Aussagen aus anderen tatsächlich gelesenen Stellen zulässig. Nicht auf eine Wortlaut-Musterantwort prüfen. Keine Behauptung, Thomas' Originalwerke seien selbst gelesen. Böttigheimer ist Originalquelle für seine eigene Darstellung, Sekundärquelle zu Thomas.

## Auswertung

Technischer Integrationsnachweis: mindestens ein tatsächlich ausgeführter erfolgreicher Skill-Aufruf, Knowledge-Suche oder Inventar, nichtleerer Originaltextabruf zum bezeichneten Werk, korrelierte Tool-Call-IDs und Rückgabe an Modell, abschließende Markdown-Antwort mit finish_reason stop. Keine festgelegte Werkzeugreihenfolge. COMPLETED bedeutet nur regulärer Modellabschluss, nicht PASS der Fachqualität. Metadaten ohne Originaltext beweisen nicht allein fachlich richtige Lektüre oder Fundstelle. Fachliche Bewertung separat anhand K1–K5 und tatsächlicher Fundstellen. Zugriffsschutz und Zuordnung des gelesenen Dokuments ggf. separat anhand lokaler Tooldetails nachweisen.

Probe begrenzt Modellrunden und Toolaufrufe, exponiert ausschließlich fünf Knowledge-/Skill-Werkzeuge, übernimmt deren native spec und Callable; keine Netzabrufe, keine eigene Steuerungssprache, keine Coverage- oder Zitatgates. Toolfehler werden zurückgemeldet; keine vollständige Produktions-ACL, SSRF-, Freeze-, Kontext- oder Provenienzlösung. Trace enthält keine Tool-Rohtexte, keine Datei-IDs oder Nutzereingaben, nur Aufruf-ID, Name, Status, Größen und Zeiten. Keine automatische Bestätigung von Quellenlektüre. Offline-Test: python3 -m unittest discover -s tests/local_dev -p test_native_knowledge_probe_v2.py -v. Status bis tatsächliche Ausführung NOT_RUN.
