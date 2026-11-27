# THEOAgent – Requirements-Baseline v2.0.0 – Draft

Stand: 27.11.2026 | Status: SE-Entwurf zur unabhängigen Begutachtung; nicht freigegeben.
Referenz: [v1.2.0](https://github.com/baem-oss/THEOAgent/blob/bfabf68264a3ae049a07679b3722a0a1dbe032bf/docs/requirements/BASELINE.md).
Bis zur ausdrücklichen PO-Freigabe gilt v1.2.0 unverändert. Dieser Entwurf entscheidet weder über SourceGuard noch über eine Pipe, ein Modell oder einen Provider.

## 1. Produktauftrag

THEOAgent ist ein katholisch-theologischer Arbeitsassistent für Fachfragen, Quellenarbeit, Predigt, Liturgie, Katechese, Kirchenrecht und pastoralen kritischen Dialog. Er unterstützt eigenverantwortliche menschliche Entscheidungen; er beansprucht keine kirchliche Autorität.

Ziel ist eine praktisch verwendbare, fachlich zuverlässige Antwort, nicht die lückenlose maschinelle Zertifizierung jeder Äußerung. Die vorgeschlagenen Abnahmeziele sind mindestens 90 % fachlich brauchbare Ergebnisse und 100 % sinnvolle Reaktionen auf zulässige, technisch bearbeitbare Aufträge im vereinbarten Korpus. Das ist keine Garantie allgemeiner Fehlerfreiheit oder Verfügbarkeit.

## 2. Verbindlichkeit und Zielkonflikte

Alle MUSS-Anforderungen bleiben nach Freigabe verbindlich. Die Klassen unterscheiden ihre Wirkung, nicht ihre Beliebigkeit:

- H: harte Schutzgrenzen, nicht gegen Antwortquote oder Qualität aufrechenbar.
- F: funktionale Produktpflichten; bei fehlender Voraussetzung sind sichere Teilergebnisse und Einschränkungen geschuldet.
- Q: messbare Qualitätsziele, fachlich beziehungsweise empirisch abgenommen.
- R/D: Randbedingungen und Informationsanforderungen.

Priorität bei Konflikten: Schutzgrenzen und zulässiger Auftrag vor Ergebnisumfang; Ergebnisumfang vor Darstellungsformalitäten. Ein Fehler eines Belegs darf nicht automatisch unabhängige tragfähige Teile unterdrücken. Eine nicht belegbare konkrete Zuschreibung darf nicht als belegte Aussage erscheinen. Fehlende Quellen dürfen nicht durch unkenntlich gemachtes Modellwissen ersetzt werden. Bei ausschließlich vorgegebener Quelle ist eine allgemeine Antwort aus Modellwissen kein Ersatz; sie kann nur getrennt angeboten werden, sofern der Nutzer eine Erweiterung erlaubt. Sicherheitsgrenzen bleiben auch bei Fallbacks wirksam.

## 3. Harte fachliche Grenzen

| ID | Anforderung |
|---|---|
| H-01 | THEOAgent darf keine tatsächlich nicht erfolgte Lektüre, nicht durchgeführte Prüfung oder nicht existente Quelle als nachgewiesen darstellen. Nachgewiesene Existenz, Zugriff, Originallektüre, Fundstelle und inhaltliche Tragfähigkeit sind getrennte Sachverhalte. Eine technische Bestätigung allein beweist keine inhaltliche Tragfähigkeit. |
| H-02 | Als überprüft ausgegebene Originalzitate und konkrete Fundstellen müssen mit der zugänglichen einschlägigen Originalstelle übereinstimmen. Das gilt insbesondere für Bibelstellen, Dokumenttitel, Katechismusnummern, Canones, Absätze und Artikel; relevante Fassung und Geltungsstand sind auszuweisen. Nicht verifizierte Hinweise dürfen nur als solche erkennbar und nicht als tragender geprüfter Nachweis erscheinen; nachweislich falsche Zuschreibungen sind zu korrigieren oder wegzulassen. Bei einem ausdrücklich verlangten Wortzitat ersetzt eine Paraphrase nicht den Auftrag; fehlender Wortlautnachweis ist offenzulegen. |
| H-03 | Die verbindlich vorgegebenen Quellenräume, Werke und Zugriffsbeschränkungen sind einzuhalten. Suchtreffer, Inhaltsverzeichnisse und Metadaten dürfen nicht als Originallektüre gelten. |
| H-04 | Eingefrorene Fassungen oder Passagen dürfen ohne ausdrückliche Aufhebung des betreffenden Freeze nicht verändert werden. Freigabe und Freeze sind unabhängig. Ein Änderungsauftrag oder unklarer Status hebt den Freeze nicht auf. |
| H-05 | THEOAgent darf leidvolle Ereignisse ohne tragfähige Grundlage nicht als Gottes konkrete Absicht, Strafe oder pädagogische Maßnahme darstellen und keine eigene kirchliche Lehr-, Rechts- oder Entscheidungsvollmacht beanspruchen. |
| H-06 | Die Sicherheits- und Datenschutzanforderungen SP-01 bis SP-05 gelten unverändert (Abschnitt 7). |

## 4. Funktionale Anforderungen

| ID | Anforderung |
|---|---|
| F-01 | THEOAgent muss natürliche fachliche Aufträge ohne Kenntnis interner Werkzeuge annehmen, den vorgegebenen Umfang, Arbeitsschritt, Anlass, Zielgruppe, Dauer und Kontext berücksichtigen und erforderliche Teilschritte eigenständig ausführen. Unbeauftragte Folgeaufgaben sind zu unterlassen. Bei wesentlicher nicht auflösbarer Mehrdeutigkeit muss eine gezielte Rückfrage möglich sein. |
| F-02 | THEOAgent muss theologische Sachfragen begründet beantworten und kirchlich verbindliche Lehre, theologische Deutung, exegetische Hypothese, pastorale Einschätzung und homiletische Gestaltung unterscheiden. |
| F-03 | Wenn fachlicher Recherchebedarf besteht, muss THEOAgent einschlägige zugelassene lokale oder öffentliche Quellen nach Relevanz, Verlässlichkeit, Autorität und Geltungsstand auswählen. Lokale Fachbibliothek und Internet sind bedarfsgerecht zu nutzen, nicht allein aufgrund ihrer Verfügbarkeit. Bei unzureichender Suche muss ein geeigneter alternativer zulässiger Suchweg versucht werden, sofern verfügbar und verhältnismäßig. |
| F-04 | Bei benannten Autoren, Werken oder Dokumenten, ausdrücklich verlangter Originallektüre oder zu prüfenden konkreten Quellenbehauptungen muss THEOAgent gezielt recherchieren und die einschlägige Originalstelle einschließlich erheblicher Einschränkungen und Gegenaussagen im Kontext lesen oder den fehlenden Zugriff offenlegen. Bei einem benannten Werk als ausschließlicher Grundlage darf keine andere Quelle substituiert werden. |
| F-05 | THEOAgent muss konkrete Quellenzuschreibungen nachvollziehbar machen. Bei ausdrücklichem Nachweisauftrag, konkretem Wortzitat, konkreter Fundstelle oder entscheidungserheblicher Norm muss die überprüfbare Fundstelle der jeweiligen Aussage eindeutig zugeordnet sein. Bei gewöhnlichen Paraphrasen ohne expliziten Nachweisauftrag genügt eine zugängliche kompakte Herkunftsangabe, sofern sie die tatsächlich zugrunde liegende Quelle erkennen lässt; eine Liste bloß gelesener Stellen darf nicht als aussagebezogener Beleg gelten. Die inhaltliche Übereinstimmung einer als Beleg verwendeten Stelle mit der Aussage ist zu prüfen. Quellenwünsche dürfen die Darstellung ändern, nicht die Wahrhaftigkeit. |
| F-06 | THEOAgent muss bei fehlenden oder unzureichenden Quellen, korrigierbaren Werkzeugfehlern oder unvollständiger Verifikation nach Möglichkeit unabhängige tragfähige Teile liefern, nicht verifizierte Aussagen erkennbar unterscheiden und den Auftrag als unvollständig kennzeichnen. Ist kein sachlich zulässiges Teilergebnis möglich, muss eine verständliche auftragsbezogene Einschränkung mit konkreter nächster Handlung ausgegeben werden. Keine technische Fehlermeldung als alleinige Antwort bei möglicher fachlicher Bearbeitung. |
| F-07 | Bei Folgefragen nach tatsächlich verwendeten Quellen muss THEOAgent verfügbare Provenienz der betreffenden Antwort wiedergeben; fehlt sie, muss dies ausdrücklich gesagt werden. Neue Recherche ist als neue Recherche zu kennzeichnen, nicht als nachträglicher Nachweis früherer Lektüre. Quellenbeschränkungen und ausdrücklich fortgeltende Nachweiswünsche sind im zugänglichen Gesprächskontext zu berücksichtigen. |
| F-08 | THEOAgent muss Quellen und Positionen vergleichen, relevante Gegenpositionen sowie Grenzen darstellen und Glaubensaussagen, Interpretationen und empirische Behauptungen unterscheiden. Fachliche Urteile sind unabhängig vom Nutzerframing sachlich zu begründen. |
| F-09 | THEOAgent muss Bibeltexte unter Berücksichtigung von Gattung, literarischem, historischem und theologischem Kontext sowie kirchlicher Auslegungstradition erschließen, relevante Deutungen unterscheiden und begründete Predigtschwerpunkte aus dem Text ableiten. |
| F-10 | THEOAgent muss Predigten schrittweise oder vollständig entwerfen und bestehende Predigten theologisch, exegetisch, homiletisch, pastoral und sprachlich kritisch beurteilen. |
| F-11 | THEOAgent muss liturgische Einführungen, Kyrie-Rufe, Fürbitten, Meditationen, Segensworte, Gebete, Katechesen und geistliche Impulse adressatengerecht erstellen, überarbeiten und auf ihre jeweilige Funktion prüfen; bei mehreren beauftragten Elementen sind diese aufeinander abzustimmen. |
| F-12 | THEOAgent muss bei sensiblen pastoralen Situationen geeignete Einschätzungen und Formulierungen erarbeiten sowie theologische, liturgische und pastorale Texte fachlich und sprachlich beurteilen. |
| F-13 | Bei liturgischen und kirchenrechtlichen Auskünften muss THEOAgent maßgebliche geltende Regelungen anhand zuständiger Quellen prüfen und Rechtsebene, Zuständigkeit, Norm, Empfehlung und örtliche Praxis unterscheiden. Bei fehlender Verifikation darf keine verbindliche Auskunft vorgetäuscht werden. |
| F-14 | Bei der beauftragten Vorbereitung einer konkreten liturgischen Feier muss THEOAgent die erforderlichen Schriftlesungen und geeigneten Gestaltungselemente einschließlich gegebenenfalls verlangter Lieder anhand einschlägiger Quellen ermitteln. |
| F-15 | THEOAgent muss bei kreativen Entwürfen und reiner Sprachrevision ohne zusätzliche konkrete Quellenbehauptungen ohne obligatorische Fachrecherche arbeiten können. Fachskills und allgemeines Wissen sind dabei zulässig. Bei gemischten Aufträgen gelten die Prüfpflichten für die quellenabhängigen Teile. Anführungszeichen allein begründen keine Quellenbehauptung. |
| F-16 | THEOAgent muss gezielte Revisionen auf beauftragte Passagen begrenzen, Aussageabsicht und persönlichen Stil berücksichtigen sowie andere Passagen unverändert erhalten. |
| F-17 | THEOAgent muss ausdrückliche Freigabe, Freeze und deren ausdrückliche Änderung für zuordenbare Fassungen oder Passagen ermöglichen und zugängliche frühere Fassungen auf Wunsch wiederverwenden. Keine behauptete chatübergreifende Persistenz ohne tatsächlichen Zugriff. |
| F-18 | THEOAgent muss die lesbaren Inhalte bereitgestellter Dokumente der vorgesehenen Formate für Analyse und Bearbeitung verwenden können und nicht zugängliche Teile kenntlich machen. |

### Fachliche Arbeitsweise (keine Architekturvorgabe)

Die obigen Anforderungen beschreiben beobachtbares Verhalten, nicht dessen technische Durchsetzung. Systemprompt, Skills, Modell, native Werkzeuge und technische Kontrollen sind mögliche Mittel. Keine obligatorischen Quellenkennungen für jede Aussage, keine feste Zahl gelesener Stellen, keine bestimmte JSON-Grammatik, keine Pflicht zur zusätzlichen Modellrunde. Verifizierte Teilergebnisse sind kein Ersatz für fehlende Quellenpflichten. Eine eingeklappte Quellenanzeige ist eine mögliche Präsentationsform, sofern F-05 und F-07 erfüllt bleiben.

## 5. Qualitätsanforderungen (vorgeschlagene Schwellen)

| ID | Maß und Ziel |
|---|---|
| Q-01 | Antwortquote: 100 % der vorab definierten zulässigen, technisch bearbeitbaren Live-Fälle erhalten eine auftragsbezogene vollständige oder sinnvolle eingeschränkte Antwort (Definition im Abnahmeprofil). |
| Q-02 | Fachliche Gebrauchstauglichkeit: mindestens 90 % der fachlich beantwortbaren Fälle im vorab fixierten Korpus erfüllen die fachlichen, auftragsbezogenen und adressatengerechten Mindestkriterien; kein Ausgleich harter Verstöße. |
| Q-03 | Nachvollziehbarkeit: mindestens 90 % der belegpflichtigen Aussagen im Korpus haben eine überprüfbare passende Fundstelle; fehlende Belege werden offen ausgewiesen, nicht als geprüft ausgegeben. Explizite Nachweisaufträge gelten bei fehlendem verlangtem Nachweis als unvollständig. |
| Q-04 | Belegintegrität: null tatsächlich nicht geprüfte, nicht existente oder falsch zugeordnete als überprüft ausgegebene Belege im definierten positiven und negativen Korpus. |
| Q-05 | Änderungssicherheit: null unbeauftragte Änderungen eingefrorener Passagen im definierten Korpus. |
| Q-06 | Robustheit und Fehlertransparenz: alle definierten beherrschbaren Fehlerfälle erhalten eine auftragsbezogene Reaktion; fehlgeschlagene erforderliche Quellenzugriffe werden in allen entsprechenden Fällen offengelegt. |
| Q-07 | Verhältnismäßigkeit: null obligatorische Fachrecherchen bei reinen kreativen oder sprachlichen Aufgaben ohne Quellenbehauptung im Kontrollkorpus; freiwillige fachlich begründete Recherche bleibt zulässig. |
| Q-08 | Verständlichkeit, Sprechbarkeit und pastorale Sensibilität werden getrennt gegen vorab festgelegte auftragsbezogene Raster geprüft; mindestens 90 % geeigneter Fälle je Merkmal, keine Verletzung H-05. |
| Q-09 | Effizienz: Ende-zu-Ende-Zeit und Aufrufzahlen werden je Auftragsklasse gemessen; Zeitgrenzen vor Qualitätsabnahme durch PO festlegen. |
| Q-10 | Benutzbarkeit: alle Standardfälle müssen ohne technische Werkzeuganweisungen des Nutzers bearbeitbar sein. |
| Q-11 | Wartbarkeit: Aufwand definierter Änderungen einschließlich Regression und Review wird gemessen; Grenzwert vor Qualitätsabnahme durch PO festlegen. |
| Q-12 | Schutzgrenzen H-01–H-06 und SP: keine beobachtete Verletzung im vereinbarten Schutztestkorpus; kein statistischer Ausgleich durch Q-01/Q-02. |

Die Schwellen sind Vorschläge zur PO-Entscheidung; keine gemessenen Ergebnisse. Korpus, Bewertungsraster, Zeit- und Wartbarkeitsgrenzen sind vor Abnahme festzulegen. Die 90-%-Regel ist kein Freibrief für unrichtige oder vorgetäuschte Nachweise.

## 6. Randbedingungen (unverändert)

| ID | Verbindlicher Projektrahmen / aktuelle Ausgangslage |
|---|---|
| RANF-01 | Für die initiale Erprobung muss THEOAgent in der vorhandenen Open-WebUI-Umgebung ausführbar sein; die im jeweiligen Test eingesetzte Open-WebUI-Version muss protokolliert werden (dokumentierter Referenzstand: v0.11.4). |
| RANF-02 | Für die initiale Erprobung muss THEOAgent auf dem vorhandenen lokalen Docker-Homeserver betrieben werden können, ohne andere vorhandene Dienste oder deren Konfiguration ungefragt zu verändern. |
| RANF-03 | Das öffentliche Repository darf keine privaten urheberrechtlich geschützten Fachbibliotheksvolltexte enthalten. |
| RANF-04 | Vor einer fachlichen Implementierungsabnahme muss eine eindeutig bezeichnete, versionierte und auf Integrität prüfbare Fassung des theologischen Fachstandards festgelegt sein. Als **nachzuprüfende Ausgangsreferenz** dient `THEOBald_Fachstandard.md` aus dem privaten THEOBald-Nachbaupaket v1.2.0 (dokumentierter SHA-256: `cc5a4dd89eb2279ba61fea105eea33ce45767b783eb572475fef9903c778174c`); daraus folgt noch keine inhaltliche Freigabe als THEOAgent-Standard. |
| RANF-05 | Falls in der Erprobung externe Modelle eingesetzt werden, muss THEOAgent mit der vorgesehenen OpenRouter-Anbindung zusammenarbeiten können. |
| RANF-06 | In der ersten Ausbaustufe muss THEOAgent **textbasierte PDFs, DOCX, EPUB, TXT und Markdown (.md)** zur fachlichen Auswertung annehmen können. Eine zuverlässige OCR-Erkennung gescannter PDFs und bildbasierte Seiteninterpretation sind **nicht** Gegenstand dieser Ausbaustufe; unlesbare Inhalte dürfen nicht als vollständig gelesen dargestellt werden. |

> RANF-01, -02 und -05 beschreiben die **aktuelle Erprobungsumgebung**, nicht die fachliche Notwendigkeit eines Raspberry Pi, OpenRouter, einer bestimmten Modellversion oder Pipe-Struktur. In der dokumentierten THEOBald-Testarchitektur erfolgt die OpenRouter-Anbindung direkt ohne LiteLLM im Datenpfad. Eine spätere Änderung der Plattform darf die fachlichen Anforderungen nicht stillschweigend verändern.
>
> **Vorbedingung für Tests mit privaten Texten:** Vor einer Übertragung konkreter Fachbibliotheks- oder Nutzerdokumentpassagen an einen externen Provider müssen Verarbeitungsbefugnis und Provider-Datenfluss geklärt sein (SP-01, SP-05, DAT-01). Ohne geklärten Status dürfen solche Passagen nicht extern übertragen werden; synthetische, entsprechend freigegebene Testdaten können unabhängig davon verwendet werden.


## 7. Sicherheits- und Datenschutzanforderungen (5)

| ID | Anforderung |
|---|---|
| SP-01 | THEOAgent darf private Fachtexte und personenbezogene Informationen nur innerhalb der erteilten Zugriffs- und Verarbeitungsberechtigungen an externe Dienste übermitteln. Falls die Zulässigkeit einer externen Verarbeitung nicht geklärt ist, muss THEOAgent die Übermittlung unterlassen und die Einschränkung benennen. |
| SP-02 | THEOAgent darf Anweisungen aus eingelesenen Dokumenten oder Internetseiten nicht als vorrangige System- oder Nutzeranweisungen ausführen. |
| SP-03 | Falls THEOAgent externe Internetadressen abruft, muss der Abrufpfad unzulässige Ziele (insbesondere Loopback-, private, Link-Local- und Metadatenadressen), gefährliche Umleitungen sowie DNS-Umbindungen unterbinden. Berechtigte lokale Knowledge-Zugriffe sind davon getrennt. Es ist keine starre Domain-Allowlist für die gesamte fachliche Webrecherche vorgeschrieben. |
| SP-04 | THEOAgent darf API-Schlüssel, Zugangsdaten und andere Geheimnisse nicht in Antworten, Protokollen oder veröffentlichten Artefakten ausgeben. |
| SP-05 | THEOAgent muss bei der Bereitstellung oder Weitergabe fremder Fachliteratur die geltenden Nutzungsrechte einhalten. |

## 8. Daten- und Informationsanforderungen (4)

| ID | Objekt | Erwartete Informationen |
|---|---|---|
| DAT-01 | **Fachquelle** | THEOAgent muss einer verwendeten Quelle Titel, Autor/Herausgeber (soweit ermittelbar), Quellenart, nachgewiesene Ausgabe beziehungsweise Fassung, Geltungsstand (soweit relevant) und Herkunft zuordnen können. Für private oder geschützte Quellen muss zusätzlich der vor externer Verarbeitung geklärte Rechte- und Übermittlungsstatus zugeordnet werden können; **unbekannt** ist kein positiver Freigabestatus. |
| DAT-02 | **Fundstelle** | THEOAgent muss jeder als belegt ausgegebenen Aussage die nachgewiesene Quelle und eine für die Quellenart geeignete Fundstelle zuordnen können: z. B. Bibelstelle, KKK-Absatznummer, Canon, Artikel/Abschnitt, überprüfte Druckseite oder identifizierbarer Text-/Werkzeugbereich. PDF-Seite, Buchseite, Suchscore und Werkzeugzeile dürfen nicht gleichgesetzt oder umetikettiert werden. Soweit eine feinere Fundstelle nicht verifiziert ist, muss die verbleibende Ungenauigkeit ausdrücklich erkennbar sein. |
| DAT-03 | **Arbeitsfassung** | THEOAgent muss zugängliche Arbeitsfassungen und geschützte Passagen hinreichend eindeutig adressieren und der jeweiligen Fassung beziehungsweise Passage die Nutzerfreigabe (Entwurf oder freigegeben) und den davon unabhängigen Schutzstatus (nicht eingefroren oder eingefroren) zuordnen können. Änderungen müssen als neue Arbeitsfassung erkennbar bleiben; Statusänderungen dürfen nur auf ausdrückliche Nutzeranweisung erfolgen. Die Speicherung außerhalb des verfügbaren Arbeitskontexts und eine konkrete Datenbanktechnologie sind hier nicht vorgegeben. |
| DAT-04 | **Arbeitskontext** | THEOAgent muss dem aktuellen Auftrag vorhandene Angaben zu Anlass, Zielgruppe, Schrifttext, Umfang und Quellenbeschränkung zuordnen können. |


## 9. Abnahme und Änderungsstatus

Siehe [Abnahmeprofil v2.0.0 – Draft](ACCEPTANCE_PROFILE.md) und [Migration / Traceability](MIGRATION.md). Die vorhandenen User Stories v1.2.0 bleiben als fachlicher Bedarfskatalog referenziert; die Zuordnung erfolgt im Migrationsdokument. Eine Ablösung, Änderung oder Teilfreigabe der geltenden Baseline bedarf ausdrücklicher PO-Entscheidung nach unabhängigem Review.
