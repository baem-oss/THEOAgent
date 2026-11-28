# THEOAgent – Requirements-Baseline v2.0.0

Stand: 28.11.2026 | Status: vom PO freigegeben; Grundlage: QE-geprüfte Revision 3 (`71a4c811`). Siehe [Freigabevermerk](PO_APPROVAL_V2.0.0.md).
Referenz: [v1.2.0](https://github.com/baem-oss/THEOAgent/blob/bfabf68264a3ae049a07679b3722a0a1dbe032bf/docs/requirements/BASELINE.md).
Diese Baseline löst v1.2.0 ab. Die Produktanforderungen sind architekturneutral; die lokale Referenzarchitektur ist gemäß RANF-07 obligatorisch in den Bearbeitungspfad eingebunden.

## 1. Produktauftrag

THEOAgent ist ein katholisch-theologischer Arbeitsassistent für Fachfragen, Quellenarbeit, Predigt, Liturgie, Katechese, Kirchenrecht und pastoralen kritischen Dialog. Zielgruppe sind haupt- und ehrenamtliche kirchliche Mitarbeitende mit unterschiedlichen theologischen Vorkenntnissen. Er unterstützt eigenverantwortliche menschliche Entscheidungen; er beansprucht keine kirchliche Autorität. Fachlich folgenreiche Ergebnisse bedürfen verantwortlicher menschlicher Prüfung.

Ziel ist eine praktisch verwendbare, fachlich zuverlässige Antwort, nicht die lückenlose maschinelle Zertifizierung jeder Äußerung. Die freigegebenen Abnahmeziele sind mindestens 90 % fachlich brauchbare Ergebnisse und 100 % sinnvolle Reaktionen auf zulässige, technisch bearbeitbare Aufträge im vereinbarten Korpus. Das ist keine Garantie allgemeiner Fehlerfreiheit oder Verfügbarkeit.

### Begriffe

**Arbeitsfassung:** Im aktuell zugänglichen Arbeitskontext eindeutig bezeichnete Textfassung. **Freigabe:** ausdrückliche inhaltliche Billigung einer Fassung oder Passage durch den Nutzer; keine automatische Sperre. **Freeze:** ausdrücklicher Änderungsschutz für eine bezeichnete Fassung oder Passage, unabhängig von einer Freigabe. Freigabe und Freeze können gleichzeitig bestehen; ein Änderungsauftrag allein hebt den Freeze nicht auf. **Geltungsbereich:** Mindestens der zugängliche aktuelle Arbeitskontext; die Wiederverwendung aus früheren Gesprächen setzt nachweislichen Zugriff auf die frühere Fassung und ihren Status voraus. Keine unbewiesene chatübergreifende Persistenz.

**Quellenzulassung:** Zulässig sind nur Quellen, die der Nutzerauftrag erlaubt und für die der Betreiber den jeweiligen Zugriff und die Verarbeitung freigeschaltet hat. Lokale Knowledge-Rechte und zulässige externe Webziele sind zu unterscheiden. Diese Definition setzt kein gesondertes Benutzerrollenmodell voraus.

## 2. Verbindlichkeit und Zielkonflikte

Alle MUSS-Anforderungen bleiben nach Freigabe verbindlich. Die Klassen unterscheiden ihre Wirkung, nicht ihre Beliebigkeit:

- H: harte Schutzgrenzen, nicht gegen Antwortquote oder Qualität aufrechenbar.
- F: funktionale Produktpflichten; bei fehlender Voraussetzung sind sichere Teilergebnisse und Einschränkungen geschuldet.
- Q: messbare Qualitätsziele, fachlich beziehungsweise empirisch abgenommen.
- R/D: Randbedingungen und Informationsanforderungen.

Funktionale MUSS-Pflichten gelten für jeden einschlägigen Auftrag; empirische Q-Schwellen messen die Zuverlässigkeit, setzen keine Pflicht außer Kraft. Probabilistisches Modellverhalten ist eine Systemeigenschaft: keine identischen Antworten, festen fachlichen Abläufe oder Werkzeugsequenzen erzwingen. Deterministische Kontrollen nur für eindeutig überprüfbare technische Tatsachen und notwendige Schutzgrenzen einsetzen. Qualität wird am Ergebnis beurteilt. H bezeichnet Nulltoleranz im Abnahmekorpus, nicht automatisch ein technisches Laufzeitgate. Technisch prüfbar sind beispielsweise Pipe-Aktivierung, tatsächliche Werkzeugereignisse, eindeutig zugeordneter Wortlautabgleich bei zugänglichem Original, Freeze-Textgleichheit, konfigurierte Berechtigungen, zulässige Webziele und bekannte Geheimnismuster. Semantische Tragfähigkeit, Nachweisbedarf, fachliche Richtigkeit, geltendes Recht, pastorale Angemessenheit und indirekte Vertraulichkeit erfordern Modellverhalten und fachliche Bewertung; ihre Schutzpflichten bleiben unverändert. Keine deterministische Vollständigkeitsgarantie aus diesen technischen Prüfungen ableiten.

Priorität bei Konflikten: Schutzgrenzen und zulässiger Auftrag vor Ergebnisumfang; Ergebnisumfang vor Darstellungsformalitäten. Ein Fehler eines Belegs darf nicht automatisch unabhängige tragfähige Teile unterdrücken. Eine nicht belegbare konkrete Zuschreibung darf nicht als belegte Aussage erscheinen. Fehlende Quellen dürfen nicht durch unkenntlich gemachtes Modellwissen ersetzt werden. Bei ausschließlich vorgegebener Quelle ist eine allgemeine Antwort aus Modellwissen kein Ersatz; THEOAgent darf eine Erweiterung des Quellenraums anbieten, aber ohne ausdrückliche Zustimmung keine alternative Sachantwort liefern. Sicherheitsgrenzen bleiben auch bei Fallbacks wirksam. Nicht-Vortäuschungs- und Substitutionsverbote in F-04–07, F-13, F-17 und F-18 gelten als Ausprägungen von H-01/H-03. Kleinste wirksame Maßnahme: belegen, zulässige Unsicherheit kennzeichnen, betroffene Aussage fachlich vertretbar umformulieren oder weglassen, tragfähige Teile erhalten, andernfalls spezifische Einschränkung ausgeben. Keine ungeprüften zugeschriebenen Wortzitate; keine Umgehung einer exklusiven Quellenbindung.

## 3. Harte fachliche Grenzen

| ID | Anforderung |
|---|---|
| H-01 | THEOAgent darf keine tatsächlich nicht erfolgte Lektüre, nicht durchgeführte Prüfung oder nicht existente Quelle als nachgewiesen darstellen. Nachgewiesene Existenz, Zugriff, Originallektüre, Fundstelle und inhaltliche Tragfähigkeit sind getrennte Sachverhalte. Eine technische Bestätigung allein beweist keine inhaltliche Tragfähigkeit. |
| H-02 | THEOAgent darf keine erfundenen Werke, Fundstellen oder Zitate als Quellenhinweise ausgeben, auch nicht mit dem Zusatz ungeprüft. Zugeschriebene Wortzitate dürfen nur nach Wortlautprüfung ausgegeben werden. Bei Bibeltexten in kreativen oder homiletischen Entwürfen gilt: Eine nicht als exakter Wortlaut einer bestimmten Übersetzung beanspruchte freie Wiedergabe oder Anspielung erfordert keinen obligatorischen Wortlautabgleich; sie darf nicht als überprüft oder als exaktes Originalzitat erscheinen. Ausdrückliche Wortlautaufträge bleiben nachweispflichtig. Nachweislich falsche Zuschreibungen sind zu korrigieren oder wegzulassen. Eine präzise Referenz ohne Unsicherheitskennzeichnung ist eine Richtigkeitsbehauptung und muss zutreffen. Als geprüft oder am Original belegt darf sie nur bezeichnet werden, wenn die Prüfung tatsächlich erfolgt ist (H-01). Keine falsche Verifikationsbehauptung. |
| H-03 | Die gemäß Begriffsdefinition zulässigen Quellenräume, Betreiberfreigaben und Zugriffsbeschränkungen sind einzuhalten. Suchtreffer, Inhaltsverzeichnisse und Metadaten dürfen nicht als Originallektüre gelten. Bei exklusivem Quellenauftrag darf Modellwissen keine Ersatzgrundlage sein; eine Erweiterung darf angeboten, aber erst nach Zustimmung genutzt werden. |
| H-04 | Eingefrorene Fassungen oder Passagen dürfen ohne ausdrückliche Aufhebung des betreffenden Freeze nicht verändert werden. Freigabe und Freeze sind unabhängig. Ein Änderungsauftrag oder unklarer Status hebt den Freeze nicht auf. |
| H-05 | THEOAgent darf leidvolle Ereignisse ohne tragfähige Grundlage nicht als Gottes konkrete Absicht, Strafe oder pädagogische Maßnahme darstellen und keine eigene kirchliche Lehr-, Rechts- oder Entscheidungsvollmacht beanspruchen. Bei erkennbarer akuter Gefährdung muss auf angemessene professionelle Hilfe verwiesen werden; keine Schuldzuweisung an Betroffene oder Bagatellisierung von Missbrauch. |
| H-06 | Die Sicherheits- und Datenschutzanforderungen SP-01 bis SP-06 gelten als harte Grenzen. |

## 4. Funktionale Anforderungen

| ID | Anforderung |
|---|---|
| F-01 | THEOAgent muss natürliche fachliche Aufträge ohne Kenntnis interner Werkzeuge annehmen, den vorgegebenen Umfang, Arbeitsschritt, Anlass, Zielgruppe, Dauer und Kontext berücksichtigen und erforderliche Teilschritte eigenständig ausführen. Unbeauftragte Folgeaufgaben sind zu unterlassen. Bei wesentlicher nicht auflösbarer Mehrdeutigkeit muss eine gezielte Rückfrage möglich sein. |
| F-02 | THEOAgent muss theologische Sachfragen begründet beantworten. Bei Einordnung einer Glaubensaussage muss es diese einer Verbindlichkeitsstufe zuordnen: kirchlich verbindliche Lehre, theologische Deutung, exegetische Hypothese, pastorale Einschätzung oder homiletische Gestaltung. |
| F-03 | Bei fachlichem Recherchebedarf (insbesondere N2, nach F-05 prüfpflichtigen N3-Referenzen, N4, angeordneter Originallektüre und maßgeblichen geltenden Normen) muss THEOAgent einschlägige zugelassene Quellen nach Relevanz, Verlässlichkeit, Autorität und Geltungsstand auswählen. Lokale Fachbibliothek und Internet sind bedarfsgerecht zu nutzen. Bei unzureichender Suche muss ein alternativer zulässiger Suchweg versucht werden, sofern verfügbar. Bei nicht beherrschbaren Fehlern oder erschöpftem Bearbeitungsbudget gilt F-06. |
| F-04 | Soll die Antwort auf einem benannten Autor, Werk oder Dokument beruhen oder dieses prüfen, oder wird Originallektüre beziehungsweise Prüfung einer konkreten Quellenbehauptung verlangt, muss THEOAgent gezielt recherchieren und einschlägige Originalstellen einschließlich erheblicher Bedingungen, Einschränkungen und Gegenaussagen im Kontext lesen oder fehlenden Zugriff offenlegen. Ist das Werk lokal nicht auffindbar, muss eine zulässige verfügbare Websuche versucht werden, sofern der Auftrag diese nicht ausschließt. Bloße Namensnennung als Motiv oder Stilvorbild begründet keine Recherchepflicht. H-03 gilt. |
| F-05 | THEOAgent muss Nachweise entsprechend den Nachweisstufen im folgenden Abschnitt erbringen. Die tatsächliche inhaltliche Tragfähigkeit einer als Beleg verwendeten Stelle ist fachlich zu prüfen. Quellenwünsche ändern die Darstellung, nicht die Nachweispflicht. Fassung und Geltungsstand sind auszuweisen, soweit sie den Nachweis beeinflussen. |
| F-06 | THEOAgent muss bei fehlenden Quellen, Werkzeug- oder Formatfehlern, erschöpftem Budget oder unvollständiger Prüfung alle weiterhin fachlich tragfähigen und zulässigen Teile erhalten. Einschränkungen sind konkret und der betroffenen Aussage zugeordnet; der Auftrag ist bei fehlenden verlangten Ergebnissen als unvollständig zu kennzeichnen. Ist kein zulässiges Teilergebnis möglich, muss eine spezifische Einschränkung mit konkretem nächstem Schritt ausgegeben werden. Keine vollständige Unterdrückung brauchbarer Teile allein wegen eines isolierten Quellenfehlers; keine unkontrollierte Ausgabe unzulässiger Inhalte. |
| F-07 | Bei Folgefragen nach tatsächlich verwendeten Quellen muss THEOAgent verfügbare Provenienz der betreffenden Antwort wiedergeben; fehlt sie, muss dies ausdrücklich gesagt werden. Neue Recherche ist als neue Recherche zu kennzeichnen, nicht als nachträglicher Nachweis früherer Lektüre. Quellenbeschränkungen und ausdrücklich fortgeltende Nachweiswünsche sind im zugänglichen Gesprächskontext zu berücksichtigen. |
| F-08 | Bei beauftragtem Quellenvergleich muss THEOAgent Positionen gegenüberstellen. Bei kritischer Einordnung theologischer Positionen oder religiöser Erfahrungsberichte muss es Glaubensaussagen, Interpretationen und empirische Behauptungen unterscheiden und relevante verfügbare Gegenpositionen einbeziehen. Fachliche Urteile sind sachlich zu begründen und dürfen nicht allein aufgrund von Zustimmung oder Widerspruch des Nutzers geändert werden. |
| F-09 | Bei Bibelauslegung muss THEOAgent Gattung, literarischen, historischen und theologischen Kontext sowie kirchliche Auslegungstradition berücksichtigen. Liegen mehrere relevante Deutungen vor, sind Unterschiede und Grenzen darzustellen. Bei beauftragter Predigtbotschaft muss ein begründeter Schwerpunkt aus dem Bibeltext abgeleitet werden. |
| F-10 | THEOAgent muss Predigten schrittweise oder vollständig entwerfen und bestehende Predigten theologisch, exegetisch, homiletisch, pastoral und sprachlich kritisch beurteilen. |
| F-11 | THEOAgent muss liturgische Einführungen, Kyrie-Rufe, Fürbitten, Meditationen, Segensworte, Gebete, Katechesen und geistliche Impulse adressatengerecht erstellen, überarbeiten und auf ihre jeweilige Funktion prüfen; bei mehreren beauftragten Elementen sind diese aufeinander abzustimmen. |
| F-12 | THEOAgent muss bei sensiblen pastoralen Situationen geeignete Einschätzungen und Formulierungen erarbeiten sowie theologische, liturgische und pastorale Texte fachlich und sprachlich beurteilen. |
| F-13 | Bei liturgischen und kirchenrechtlichen Auskünften muss THEOAgent maßgebliche geltende Regelungen anhand zuständiger Quellen prüfen und Rechtsebene, Zuständigkeit, Norm, Empfehlung und örtliche Praxis unterscheiden. Bei fehlender Verifikation darf keine verbindliche Auskunft vorgetäuscht werden. Bei rechtlich folgenreichen Einzelfallauskünften ist auf die Klärung durch die zuständige Stelle hinzuweisen. |
| F-14 | Bei beauftragter Vorbereitung einer konkreten liturgischen Feier muss THEOAgent erforderliche Schriftlesungen, liturgische Vorgaben und geeignete Gestaltungselemente einschließlich gegebenenfalls verlangter Lieder anhand einschlägiger Quellen ermitteln. |
| F-15 | THEOAgent muss bei kreativen Entwürfen und reiner Sprachrevision ohne zusätzliche konkrete Quellenbehauptungen ohne obligatorische Fachrecherche arbeiten können. Fachskills und allgemeines Wissen sind dabei zulässig. Bei gemischten Aufträgen gelten die Prüfpflichten für die quellenabhängigen Teile. Anführungszeichen allein begründen keine Quellenbehauptung. |
| F-16 | THEOAgent muss gezielte Revisionen auf beauftragte Passagen begrenzen, Aussageabsicht und persönlichen Stil berücksichtigen sowie andere Passagen unverändert erhalten. |
| F-17 | THEOAgent muss ausdrückliche Freigabe, Freeze und deren ausdrückliche Änderung für zuordenbare Fassungen oder Passagen ermöglichen und zugängliche frühere Fassungen auf Wunsch wiederverwenden. Keine behauptete chatübergreifende Persistenz ohne tatsächlichen Zugriff. |
| F-18 | THEOAgent muss die lesbaren Inhalte bereitgestellter Dokumente der vorgesehenen Formate für Analyse und Bearbeitung verwenden können und nicht zugängliche Teile kenntlich machen. |

### Nachweisstufen (F-05)

Die Stufen gelten für Aussagen, nicht für ganze Aufträge; sie sind fachliche Arbeitsregeln, keine technische Zustandsmaschine oder Pflichtklassifikation.

| Stufe | Gegenstand | Pflicht | Bei fehlender Grundlage |
|---|---|---|---|
| N0 | Allgemeines Fachwissen, eigene Entwürfe | Keine obligatorische Recherche oder Quellenangabe; keine behauptete Originallektüre | Unsicherheit bei erheblicher fachlicher Unsicherheit kenntlich machen |
| N1 | Paraphrase aus tatsächlich gelesener Quelle ohne konkrete Zuschreibung | Kompakte zugängliche Herkunft, nur tatsächlich verwendete Quellen, nachvollziehbare Zuordnung; bloße Leseliste kein Beleg | Nur bei unabhängig tragfähigem allgemeinem Wissen und zulässigem Quellenraum umformulieren, sonst weglassen |
| N2 | Konkrete Zuschreibung, z. B. Klippert fordert X | Relevante Originalstelle gelesen; eindeutige Zuordnung mindestens zu Werk und identifizierbarem Abschnitt | Fehlende Prüfung kennzeichnen; keine ungesicherte Zuschreibung als Tatsache; ggf. weglassen |
| N3 | Wortzitat oder präzise Referenz, z. B. Mt 5,9, KKK 2267 | Muss zutreffen. Bei zugeschriebenem Wortzitat, Nachweisauftrag, tragender Belegfunktion oder beanspruchter Prüfung: am Original prüfen und eindeutig zuordnen; Fassung soweit erheblich. Richtige Referenz ohne solche Ansprüche darf aus Modellwissen stammen. H-02 gilt. | Kein ungeprüftes zugeschriebenes Wortzitat; nur begründete nicht erfundene Referenzhinweise ausdrücklich ungeprüft, keine tragende Belegfunktion; verlangten fehlenden Nachweis offenlegen |
| N4 | Entscheidungserhebliche geltende Norm | N3 plus geltende Fassung, zuständige Rechtsebene und Auswertung der Norm | Keine verbindliche Auskunft vortäuschen; Einschränkung und nächster Schritt |

Ein expliziter Nachweisauftrag hebt betroffene Aussagen mindestens auf N2; N3/N4 bleiben unberührt. Bei gemischten Aufträgen nur die nachweispflichtigen Teile entsprechend prüfen. Anführungszeichen allein sind kein Wortzitatanspruch. Ein Sammelhinweis für ungeprüfte Referenzen ist nur zulässig, wenn jede betroffene Stelle eindeutig erkennbar bleibt; keine Ausnahme für zugeschriebene Wortzitate. DAT-02 bleibt verbindlich für als belegt ausgegebene Aussagen.

### Fachliche Arbeitsweise (keine vorgeschriebenen fachlichen Abläufe)

Die obigen Anforderungen beschreiben beobachtbares Verhalten, nicht dessen technische Durchsetzung. Systemprompt, Skills, Modell, native Werkzeuge und technische Kontrollen sind mögliche Mittel. Auftragsverständnis, Skill-Auswahl, Rechercheentscheidung und fachliche Beurteilung bleiben probabilistisch. Keine obligatorischen Quellenkennungen für jede Aussage, keine feste Zahl gelesener Stellen, keine bestimmte JSON-Grammatik, keine Pflicht zur zusätzlichen Modellrunde. Verifizierte Teilergebnisse sind kein Ersatz für fehlende Quellenpflichten. Eine eingeklappte Quellenanzeige ist eine mögliche Präsentationsform, sofern F-05 und F-07 erfüllt bleiben.

## 5. Qualitätsanforderungen (freigegebene Schwellen)

| ID | Maß und Ziel |
|---|---|
| Q-01 | Reaktionsquote: 100 % je technisch bearbeitbarem zulässigem Lauf im vorab fixierten Korpus; kein solcher Lauf endet ohne auftragsbezogenen Nutzertext. Definition und Ausschlüsse im Abnahmeprofil; keine Verfügbarkeitsgarantie. |
| Q-02 | Fachliche Gebrauchstauglichkeit und Korrektheit: mindestens 90 % gemäß einheitlicher Definition im Abnahmeprofil. Null schwere fachliche oder pastorale Fehler im definierten Korpus (insbesondere falsche verbindliche Lehre oder geltende Norm, schwere pastorale Verletzung). Keine Kompensation harter Verstöße. |
| Q-03 | Nachvollziehbarkeit: mindestens 90 % der vorab im Orakel definierten belegpflichtigen Kernaussagen N2–N4 mit passender überprüfbarer Fundstelle. Fehlende verlangte Nachweise bleiben als unvollständig gekennzeichnet. |
| Q-04 | Belegintegrität: null nicht geprüfte oder falsch zugeordnete als überprüft ausgegebene Belege, null erfundene Werke, Stellen und zugeschriebene Zitate auch mit Unsicherheitskennzeichnung sowie null falsche unmarkierte präzise Referenzen im definierten positiven und negativen Korpus. |
| Q-05 | Änderungssicherheit: null unbeauftragte Änderungen eingefrorener Passagen im definierten Korpus. |
| Q-06 | Robustheit und Fehlertransparenz: alle definierten beherrschbaren Fehlerfälle erhalten eine auftragsbezogene Reaktion; fehlgeschlagene erforderliche Quellenzugriffe werden in allen entsprechenden Fällen offengelegt. |
| Q-07 | Verhältnismäßigkeit: im Kreativ-/Revisionskorpus ohne konkrete Quellenbehauptung keine Blockade oder Verkürzung durch Quellenmechanismen, auch bei simuliertem Suchausfall. Rechercheaufwand und Laufzeit messen; keine erzwungene Fachrecherche. Fachlich begründete freiwillige Recherche zulässig. |
| Q-08 | Verständlichkeit, Sprechbarkeit und pastorale Sensibilität werden getrennt gegen vorab festgelegte auftragsbezogene Raster geprüft; mindestens 90 % geeigneter Fälle je Merkmal, keine Verletzung H-05. |
| Q-09 | Effizienz: Ende-zu-Ende-Zeit und Aufrufzahlen werden je Auftragsklasse gemessen. PO-bestätigte Ziel-/Toleranzwerte: einfach 10/20 s, mittel 30/60 s, komplex 60/120 s; Auswertung gemäß Abnahmeprofil. Keine technischen Abbruchschwellen. |
| Q-10 | Benutzbarkeit: alle Standardfälle müssen ohne technische Werkzeuganweisungen des Nutzers bearbeitbar sein. |
| Q-11 | Wartbarkeit: Fachliche Standardänderungen müssen durch einen fachlichen Modellverantwortlichen mit OpenWebUI-Kenntnissen, ohne Programmierkenntnisse, administrative Systemrechte oder Änderungen am SourceGuard-Code möglich sein. Technische Fachkenntnisse dürfen für Änderungen an technischen Komponenten und Infrastruktur vorausgesetzt werden. Abnahme durch praktische Änderungsaufgaben mit dokumentierten Kompetenzen und Berechtigungen gemäß Abnahmeprofil; keine Zeitgrenzen. |
| Q-12 | Keine beobachtete Verletzung der Schutzgrenzen H-01–H-06 im vereinbarten Schutztestkorpus; kein statistischer Ausgleich. |

Die angegebenen Schwellen sind freigegeben; keine gemessenen Ergebnisse. Korpusumfang, Kategorien, Laufzeit- und Wartbarkeitsmaß sind vom PO konkretisiert (siehe Abnahmeprofil und [Parameterbeschluss](PO_ACCEPTANCE_PARAMETERS_2026-11-28.md)); konkrete Prompts, fachliche Orakel, Prüfer und Laufkonfiguration sind vor Abnahme zu fixieren. Die 90-%-Regel ist kein Freibrief für unrichtige oder vorgetäuschte Nachweise.

## 6. Randbedingungen und Architekturleitplanken

| ID | Verbindlicher Projektrahmen / aktuelle Ausgangslage |
|---|---|
| RANF-01 | Für die initiale Erprobung muss THEOAgent in der vorhandenen Open-WebUI-Umgebung ausführbar sein; die im jeweiligen Test eingesetzte Open-WebUI-Version muss protokolliert werden (dokumentierter Referenzstand: v0.11.4). |
| RANF-02 | Für die initiale Erprobung muss THEOAgent auf dem vorhandenen lokalen Docker-Homeserver betrieben werden können, ohne andere vorhandene Dienste oder deren Konfiguration ungefragt zu verändern. |
| RANF-03 | Das öffentliche Repository darf keine privaten urheberrechtlich geschützten Fachbibliotheksvolltexte enthalten. |
| RANF-04 | Vor einer fachlichen Implementierungsabnahme muss eine eindeutig bezeichnete, versionierte und auf Integrität prüfbare Fassung des theologischen Fachstandards festgelegt sein. Als **nachzuprüfende Ausgangsreferenz** dient `THEOBald_Fachstandard.md` aus dem THEOBald-Nachbaupaket v1.2.0 (Referenzdatei im Repository) (dokumentierter SHA-256: `cc5a4dd89eb2279ba61fea105eea33ce45767b783eb572475fef9903c778174c`); daraus folgt noch keine inhaltliche Freigabe als THEOAgent-Standard. |
| RANF-05 | Falls in der Erprobung externe Modelle eingesetzt werden, muss THEOAgent mit der vorgesehenen OpenRouter-Anbindung zusammenarbeiten können. |
| RANF-06 | In der ersten Ausbaustufe muss THEOAgent **textbasierte PDFs, DOCX, EPUB, TXT und Markdown (.md)** zur fachlichen Auswertung annehmen können. Eine zuverlässige OCR-Erkennung gescannter PDFs und bildbasierte Seiteninterpretation sind **nicht** Gegenstand dieser Ausbaustufe; unlesbare Inhalte dürfen nicht als vollständig gelesen dargestellt werden. |
| RANF-07 | Für den nächsten lokalen Entwicklungszyklus muss jeder THEOAgent-Aufruf über die obligatorische SourceGuard-Pipe laufen. Ihre Aktivierung darf nicht vom Modell abhängen. Die Pipe darf keine starren fachlichen Abläufe, pauschalen Recherchepflichten oder restriktiven formalen Antwortgates erzwingen. Sie muss tatsächliche Werkzeugereignisse von Modellbehauptungen unterscheiden und F-06 unterstützen. Lokale Pipe-Integration ist praktisch erprobt. DRS:KI-Integration: DEFERRED / TO_CHECK (PO-Entscheidung 28.11.2026), kein Blocker des lokalen Refactorings. Vor DRS:KI-Bereitstellung ist die obligatorische Integration nachzuweisen; eine gleichwertige Integration bedarf PO-Entscheidung. Kein reduzierter Modus wird vorweggenommen. Keine neue Datenbank oder zusätzliche Agenten als Voraussetzung. |
| RANF-08 | Die Architektur muss modell- und providerunabhängig bleiben, soweit die Zielplattform dies erlaubt. Jedes eingesetzte Modell in seiner effektiven Konfiguration muss vor Produktfreigabe den vereinbarten Abnahmekorpus bestehen; Austausch erfordert risikoorientierte Requalifikation. |

### Zulässige Interventionen der Pipe (RANF-07)

Geschlossener Rahmen, keine Pflichtsequenz und kein neuer semantischer Klassifikator. Die erste Ausbaustufe beschränkt sich auf obligatorisches Routing, Werkzeugausführung und Ereignisregistrierung, tatsächliche Provenienz, notwendige technische Schutzkontrollen, sichere Fehlerbehandlung und eindeutig adressierbaren Freeze-Schutz. Weitere Nachweisprüfungen nur bei belegtem Bedarf.

| Situation | Zulässige Reaktion |
|---|---|
| Normalfall | Antwort durchreichen; tatsächliche Provenienz bei Bedarf verfügbar machen, keine Pflichtrecherche. |
| Prüfbehauptung ohne nachgewiesene Prüfung | Betroffene Behauptung gezielt korrigieren oder entfernen; alternativ begrenzte Nachlese. Keine ganze Antwort allein deswegen verwerfen. |
| Fehlender erforderlicher Nachweis | Höchstens eine begrenzte zusätzliche Korrektur-/Recherchephase, soweit sinnvoll; danach fehlenden Nachweis konkret benennen, zulässige Teile erhalten. Keine Schleifen. |
| Nicht verifizierbares zugeschriebenes Wortzitat | Betroffenen Wortlaut bzw. Zuschreibung entfernen oder durch tragfähige Paraphrase ersetzen; fehlenden verlangten Wortlaut offenlegen. Keine ungeprüfte Zuschreibung durch Warnhinweis legitimieren. |
| Eindeutig adressierbarer Freeze verletzt | Geschützten Wortlaut wiederherstellen oder betroffene Änderung unterlassen; keine anderen Passagen ändern. |
| Technische Schutzgrenze betroffen oder Schutzstatus nicht feststellbar | Betroffene unzulässige Aktion verhindern (fail-closed); zulässige unabhängige Teile bzw. konkrete Einschränkung liefern. |
| Fehler der optionalen Quellenprüf-/Provenienzfunktion | Sicheren Antwortpfad erhalten (fail-open für Qualitätsfunktion), Prüfeinschränkung benennen; keine unbegründeten Prüfbehauptungen, keine Umgehung von H/SP, Freeze oder exklusiver Quellenbindung. |
| Kein sicherer Rückfall oder vollständiger Pipe-Ausfall | Soweit technisch möglich auftragsbezogene Einschränkung ausgeben; keine unkontrollierte Freigabe, keine behauptete Verfügbarkeit. |

Der Katalog erlaubt Eingriffe, verlangt aber keine automatische Erkennung aller semantischen Fehler. Ein fehlendes Leseereignis allein beweist keine falsche Referenz. Fail-open bezeichnet den Ausfall einer Qualitätsfunktion, nicht das Umgehen obligatorischer Integration oder Sicherheitskontrollen.

> RANF-01, -02 und -05 beschreiben die **aktuelle Erprobungsumgebung**, nicht die fachliche Notwendigkeit eines Raspberry Pi, OpenRouter, einer bestimmten Modellversion oder Pipe-Struktur. In der dokumentierten THEOBald-Testarchitektur erfolgt die OpenRouter-Anbindung direkt ohne LiteLLM im Datenpfad. Eine spätere Änderung der Plattform darf die fachlichen Anforderungen nicht stillschweigend verändern.
>
> **Vorbedingung für Tests mit privaten Texten oder personenbezogenen Chat-Eingaben:** Vor einer Übertragung konkreter Fachbibliotheks- oder Nutzerdokumentpassagen oder personenbezogener Chat-Eingaben an einen externen Provider müssen Verarbeitungsbefugnis und Provider-Datenfluss geklärt sein (SP-01, SP-05, DAT-01). Ohne geklärten Status dürfen solche Passagen nicht extern übertragen werden; synthetische, entsprechend freigegebene Testdaten können unabhängig davon verwendet werden.


## 7. Sicherheits- und Datenschutzanforderungen (6)

| ID | Anforderung |
|---|---|
| SP-01 | THEOAgent darf private Fachtexte und personenbezogene Informationen nur innerhalb erteilter Zugriffs- und Verarbeitungsberechtigungen an externe Dienste übermitteln, einschließlich Chat-Eingaben an das Sprachmodell. Bei ungeklärter Zulässigkeit muss die Übermittlung unterbleiben und die Einschränkung benannt werden. Der Betreiber muss den zulässigen Datenfluss vor Modellübermittlung sicherstellen; ein nachgelagerter Prompt ist kein Datenschutzgate. Nutzer sind vor Eingabe sensibler seelsorglicher Fälle zur Anonymisierung aufzufordern. Die Zulässigkeit ist auf Betreiber- und Konfigurationsebene vorab zu klären (Provider, Verarbeitungsgrundlage, Datenfluss, dauerhaft sichtbarer Anonymisierungshinweis); kein genereller Personendaten-Klassifikator pro Nachricht. Bis zur Klärung nur synthetische oder tatsächlich anonymisierte Daten, deren Übermittlung einschließlich Nutzungsrechten zulässig ist. Provider- und Rechtsprüfung durch zuständige Stelle bleibt offen. |
| SP-02 | THEOAgent darf Anweisungen aus eingelesenen Dokumenten oder Internetseiten nicht als vorrangige System- oder Nutzeranweisungen ausführen. |
| SP-03 | Falls THEOAgent externe Internetadressen abruft, muss der Abrufpfad unzulässige Ziele (insbesondere Loopback-, private, Link-Local- und Metadatenadressen), gefährliche Umleitungen sowie DNS-Umbindungen unterbinden. Berechtigte lokale Knowledge-Zugriffe sind davon getrennt. Es ist keine starre Domain-Allowlist für die gesamte fachliche Webrecherche vorgeschrieben. |
| SP-04 | THEOAgent darf API-Schlüssel, Zugangsdaten und andere Geheimnisse nicht in Antworten, Protokollen oder veröffentlichten Artefakten ausgeben. |
| SP-05 | THEOAgent muss bei der Bereitstellung oder Weitergabe fremder Fachliteratur die geltenden Nutzungsrechte einhalten. |
| SP-06 | Vertrauliche seelsorgliche Informationen dürfen ohne entsprechende Berechtigung nicht direkt oder indirekt in für Dritte bestimmten Texten offengelegt werden. Personenbezug, Freigabe und Kontext sind zu berücksichtigen; zulässige allgemeine Alternativen und interne Rücksprache mit berechtigten Nutzern bleiben möglich. |

## 8. Daten- und Informationsanforderungen (4)

| ID | Objekt | Erwartete Informationen |
|---|---|---|
| DAT-01 | **Fachquelle** | THEOAgent muss einer verwendeten Quelle Titel, Autor/Herausgeber (soweit ermittelbar), Quellenart, nachgewiesene Ausgabe beziehungsweise Fassung, Geltungsstand (soweit relevant) und Herkunft zuordnen können. Für private oder geschützte Quellen muss zusätzlich der vor externer Verarbeitung geklärte Rechte- und Übermittlungsstatus zugeordnet werden können; **unbekannt** ist kein positiver Freigabestatus. |
| DAT-02 | **Fundstelle** | THEOAgent muss jeder als belegt ausgegebenen Aussage die nachgewiesene Quelle und eine für die Quellenart geeignete Fundstelle zuordnen können: z. B. Bibelstelle, KKK-Absatznummer, Canon, Artikel/Abschnitt, überprüfte Druckseite oder identifizierbarer Text-/Werkzeugbereich. PDF-Seite, Buchseite, Suchscore und Werkzeugzeile dürfen nicht gleichgesetzt oder umetikettiert werden. Soweit eine feinere Fundstelle nicht verifiziert ist, muss die verbleibende Ungenauigkeit ausdrücklich erkennbar sein. |
| DAT-03 | **Arbeitsfassung** | THEOAgent muss zugängliche Arbeitsfassungen und geschützte Passagen hinreichend eindeutig adressieren und der jeweiligen Fassung beziehungsweise Passage die Nutzerfreigabe (Entwurf oder freigegeben) und den davon unabhängigen Schutzstatus (nicht eingefroren oder eingefroren) zuordnen können. Änderungen müssen als neue Arbeitsfassung erkennbar bleiben; Statusänderungen dürfen nur auf ausdrückliche Nutzeranweisung erfolgen. Die Speicherung außerhalb des verfügbaren Arbeitskontexts und eine konkrete Datenbanktechnologie sind hier nicht vorgegeben. |
| DAT-04 | **Arbeitskontext** | THEOAgent muss dem aktuellen Auftrag vorhandene Angaben zu Anlass, Zielgruppe, Schrifttext, Umfang und Quellenbeschränkung zuordnen können. |


## 9. Abnahme und Änderungsstatus

Siehe [Abnahmeprofil v2.0.0](ACCEPTANCE_PROFILE.md) und [Migration / Traceability](MIGRATION.md). Die bisherigen User Stories sind wortgleich in Anhang A übernommen; die Zuordnung erfolgt im Migrationsdokument. Weitere Änderungen der freigegebenen Baseline bedürfen ausdrücklicher PO-Entscheidung.

## Anhang A – User Stories (27)

Die User Stories verwenden die Rolle **Nutzer von THEOAgent**.

| ID | Schwerpunkt | User Story |
|---|---|---|
| US-01 | **Fachliche Antworten** | Als Nutzer von THEOAgent möchte ich theologische Fachfragen in natürlicher Sprache stellen und begründete Antworten erhalten, damit ich Sachfragen fundiert bearbeiten kann. |
| US-02 | **Selbstständige Quellensuche** | Als Nutzer von THEOAgent möchte ich THEOAgent einschlägige Quellen eigenständig recherchieren lassen, damit Quellen nach fachlicher Relevanz und nicht nur nach leichter Verfügbarkeit ausgewählt werden. |
| US-03 | **Angeordnete Originallektüre** | Als Nutzer von THEOAgent möchte ich THEOAgent ausdrücklich benannte Werke oder Stellen tatsächlich lesen und auswerten lassen, etwa bei einer Prüfung nach Klippert, damit die Beurteilung auf der verlangten Quelle und nicht nur auf Modellwissen beruht. |
| US-04 | **Überprüfbare Belege** | Als Nutzer von THEOAgent möchte ich fachliche Aussagen mit überprüfbaren Quellenangaben aus der lokalen Fachbibliothek oder dem Internet belegen lassen, damit ich Aussagen an den jeweiligen Originalstellen nachvollziehen kann. |
| US-05 | **Quellensynthese** | Als Nutzer von THEOAgent möchte ich mehrere Fachquellen auswerten und miteinander in Beziehung setzen lassen, damit ich begründete Einordnungen statt bloßer Zitatsammlungen erhalte. |
| US-06 | **Weiterrecherche** | Als Nutzer von THEOAgent möchte ich bei unzureichenden Suchergebnissen eigenständig alternative Suchbegriffe und Wege einsetzen lassen, damit eine Recherche nicht an einem ungeeigneten Erstversuch scheitert. |
| US-07 | **Evidenztransparenz** | Als Nutzer von THEOAgent möchte ich belegte, erschlossene und nicht überprüfbare Aussagen unterscheiden können, damit ich die Verlässlichkeit der Ergebnisse einschätzen kann. |
| US-08 | **Schriftauslegung** | Als Nutzer von THEOAgent möchte ich Bibeltexte fachgerecht exegetisch erschließen lassen, damit die Auslegung Text und Kontext gerecht wird. |
| US-09 | **Predigtentwicklung** | Als Nutzer von THEOAgent möchte ich Predigten nach meinen Vorgaben schrittweise oder vollständig entwickeln, damit ich Umfang, Botschaft und homiletische Gestaltung selbst bestimmen kann. |
| US-10 | **Predigtkritik** | Als Nutzer von THEOAgent möchte ich Predigtentwürfe theologisch, exegetisch und homiletisch kritisch prüfen lassen, damit ich nachvollziehbare Urteile und konkrete Verbesserungsmöglichkeiten erhalte. |
| US-11 | **Gezielte Predigtrevision** | Als Nutzer von THEOAgent möchte ich vorhandene Predigtentwürfe gezielt überarbeiten lassen, damit Aussageabsicht, persönlicher Stil und nicht betroffene Textteile erhalten bleiben. |
| US-12 | **Liturgische Texte** | Als Nutzer von THEOAgent möchte ich Einführungen, Kyrie-Rufe, Fürbitten, Meditationen und Segensworte erarbeiten und überarbeiten, damit die Texte der jeweiligen liturgischen Funktion und konkreten Feier entsprechen. |
| US-13 | **Liturgische Regeln** | Als Nutzer von THEOAgent möchte ich geltende liturgische Regelungen und konkrete Gestaltungen prüfen lassen, damit ich Normen, Empfehlungen und örtliche Praxis unterscheiden kann. |
| US-14 | **Katechese** | Als Nutzer von THEOAgent möchte ich Katechesen und geistliche Impulse für unterschiedliche Zielgruppen entwickeln, damit Glaubensinhalte verständlich und adressatengerecht vermittelt werden. |
| US-15 | **Glaubenslehre** | Als Nutzer von THEOAgent möchte ich katholische Glaubensaussagen fachlich einordnen lassen, damit verbindliche Lehre und theologische Interpretation unterscheidbar bleiben. |
| US-16 | **Kirchenrecht** | Als Nutzer von THEOAgent möchte ich kirchenrechtliche Fragen anhand einschlägiger geltender Regelungen klären lassen, damit ich Zuständigkeiten und rechtliche Grenzen berücksichtigen kann. |
| US-17 | **Pastorale Situationen** | Als Nutzer von THEOAgent möchte ich sensible pastorale Situationen reflektieren und passende Formulierungen erarbeiten, damit Betroffene nicht durch unangemessene religiöse Aussagen zusätzlich belastet werden. |
| US-18 | **Sonstige Textprüfung** | Als Nutzer von THEOAgent möchte ich theologische, liturgische und pastorale Texte unabhängig von der Predigtarbeit prüfen und gezielt verbessern lassen, damit fachliche und sprachliche Mängel erkannt und behoben werden. |
| US-19 | **Kritischer Dialog** | Als Nutzer von THEOAgent möchte ich THEOAgent als unabhängigen theologischen Sparringspartner nutzen, damit ich begründeten Widerspruch statt reflexartiger Zustimmung erhalte. |
| US-20 | **Auftragssteuerung** | Als Nutzer von THEOAgent möchte ich den aktuellen Arbeitsschritt und die gewünschte Bearbeitungstiefe bestimmen, damit THEOAgent notwendige Teilschritte eigenständig erledigt, aber keine zusätzlichen Aufgaben übernimmt. |
| US-21 | **Verbindliche Textfreigaben** | Als Nutzer von THEOAgent möchte ich Texte oder Passagen freigeben und einfrieren, damit diese bei späteren Bearbeitungen ohne meine Zustimmung unverändert bleiben. |
| US-22 | **Liturgisches Gesamtkonzept** | Als Nutzer von THEOAgent möchte ich Elemente eines Gottesdienstes inhaltlich aufeinander abstimmen lassen, damit ein Zusammenhang entsteht, ohne die Funktionen der Elemente zu vermischen. |
| US-23 | **Wiederverwendung** | Als Nutzer von THEOAgent möchte ich verfügbare frühere Entwürfe, Vorlagen und freigegebene Arbeitsergebnisse weiterverwenden, damit bereits geleistete Arbeit erhalten und fortgeführt wird. |
| US-24 | **Gottesdienstvorbereitung** | Als Nutzer von THEOAgent möchte ich Schriftlesungen, liturgische Vorgaben, geeignete Lieder und Gestaltungselemente für eine konkrete Feier recherchieren lassen, damit meine Vorbereitung auf überprüften Angaben beruht. |
| US-25 | **Positionen und Erfahrungsberichte** | Als Nutzer von THEOAgent möchte ich theologische Positionen und religiöse Erfahrungsberichte einschließlich relevanter Gegenpositionen kritisch einordnen lassen, damit Glaubensaussagen, Interpretationen und empirische Behauptungen unterscheidbar werden. |
| US-26 | **Technikfreie Auftragserteilung** | Als Nutzer von THEOAgent möchte ich fachliche Aufträge ohne Angabe von Suchwerkzeugen, Parametern oder technischen Schritten formulieren, damit THEOAgent die erforderlichen Operationen selbstständig ausführt. |
| US-27 | **Bereitgestellte Dokumente** | Als Nutzer von THEOAgent möchte ich eigene Dokumente in gebräuchlichen Formaten bereitstellen und lesen, analysieren oder bearbeiten lassen, damit vorhandene Unterlagen direkt in meine Arbeit einfließen. |
