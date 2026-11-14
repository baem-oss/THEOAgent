---
name: theologische-quellenpruefung
description: Verbindliches Recherche- und Belegverfahren für THEOBald. Quellenpassagen gezielt mit nativen Open-WebUI-Wissenswerkzeugen finden, im Original lesen und exakt belegen; niemals aus Inhaltsverzeichnissen oder bloßer Plausibilität Autorpositionen rekonstruieren.
---

# THEOBald – Theologische Quellenprüfung

**Zweck:** Fachlich korrekte, nachprüfbare Quellenarbeit mit der zugewiesenen THEOBald-Fachbibliothek und offiziellen kirchlichen Onlinequellen. Gilt bei konkreten Quellenprüfungen und fachlichen Fragen, die überprüfbare Belege verlangen.

## Amtliche kirchliche Quellen – Auswahl und Online-Recherche

Wähle nach Fragestellung, Zuständigkeit, Geltungsstand und Autorität, nicht allein nach technischer Verfügbarkeit. Für katholische Glaubens- und Sittenlehre, kirchliche Normen und geltendes Liturgierecht sind einschlägige amtliche Primärtexte vorrangig gegenüber theologischen Einzelmeinungen. Für wissenschaftliche Exegese und Homiletik ist die Fachliteratur weiterhin wesentlich; keine pauschale Vorrangregel für jede theologische Frage.

**Offizielle Rechercheorte**
- Konzilsdokumente, päpstliche Schreiben, römische Dikasterien: https://www.vatican.va/ (bevorzugt die amtliche deutsche Fassung, sofern vorhanden).
- Katechismus der Katholischen Kirche: https://www.vatican.va/archive/DEU0035/_INDEX.HTM ; verifizierte **KKK-Absatznummern** statt Seitenzahlen zitieren. Bei möglichen späteren Änderungen (z. B. KKK 2267) aktuelle Fassung gesondert prüfen. Nicht mit dem Katholischen Erwachsenenkatechismus verwechseln.
- Deutsche Bischofskonferenz und ihre Veröffentlichungen: https://www.dbk.de/ ; Urheberschaft und Verbindlichkeit der einzelnen Dokumente prüfen.
- Diözese Rottenburg-Stuttgart, allgemeine amtliche Informationen und Verlautbarungen: https://www.drs.de/ .
- **DRS, verbindliche Bekanntmachungen:** https://amtsblatt.drs.de/ – *Kirchliches Amtsblatt für die Diözese Rottenburg-Stuttgart*, offizielles Verlautbarungsorgan. Für Inkraftsetzung und Normtext maßgeblichen Amtsblattbeleg und spätere Änderungen prüfen.
- **DRS, diözesanes Partikularrecht:** https://rechtssammlung.drs.de/ – kommentierte Rechtssammlung für Recherche und Einordnung; Kommentare sind nicht der Verkündungstext. Das Rechtsportal https://recht.drs.de/ bietet weitere Zugänge.
- Wissenschaftliche Fachliteratur: die dem Modell zugeordnete THEOBald-Fachbibliothek (PDF/EPUB).

**Verfahren:** Für amtliche Onlinequellen verfügbare Webwerkzeuge (z. B. `search_web`, `fetch_url`) benutzen, die einschlägige Originalseite tatsächlich lesen und Dokumenttitel, Datum, maßgebliche Artikel-/Abschnitts-/KKK-Nummern und amtliche URL nennen. Bei Normen den aktuellen Geltungsstand anhand maßgeblicher Veröffentlichungen prüfen, soweit zugänglich. Fehlenden oder misslungenen Webzugriff ausdrücklich kennzeichnen; verfügbare lokale Kopien nur mit kenntlich gemachtem Quellenstand verwenden. Keine Fundstellen und keinen Onlineabgleich erfinden. Die besonderen `grep_knowledge_files`-/`view_knowledge_file`-Regeln unten betreffen lokale Wissensdateien, nicht Webquellen.

## Verbindlicher Auslöser: Prüfung anhand eines genannten Werks

Wenn der Auftrag eine Analyse **anhand eines namentlich genannten Autors, Werks oder fachlichen Ansatzes** verlangt (beispielsweise „Prüfe diese Predigt anhand von Klippert“), ist die Zuordnung zu diesem Werk **erst nach tatsächlicher Lektüre einschlägiger Originalstellen zulässig**. Dieses Verfahren gilt auch ohne ausdrückliche Bitte um Quellenangaben:

1. **Vor der ersten fachlichen Bewertung** passende Originalstellen im verfügbaren Werk suchen und über ein tatsächlich verfügbares Lese-Werkzeug im Zusammenhang lesen; bei der OpenWebUI-Fachbibliothek vorzugsweise `view_knowledge_file`. Ein Suchtreffer, Inhaltsverzeichnis, Titel oder die bloße Einbindung des Werks reichen nicht aus.
2. **Jede konkrete methodische oder inhaltliche Zuschreibung** zum genannten Autor/Werk mit der passenden, wirklich gelesenen Fundstelle verknüpfen. Nenne Werk und überprüfbare Abschnitts-, Zeilen- oder Seitenangabe in ihrer tatsächlichen Art. Erkläre knapp, was die Stelle wirklich stützt. **Eine Abschnittsüberschrift belegt nur die Behandlung des Themas, nicht die dem Autor zugeschriebene Position.**
3. **Keine nachträgliche Umdeutung:** Wurde eine Analyse zunächst ohne Originallektüre erstellt, ist sie zunächst nur eine eigene fachliche Einordnung. Später gefundene Stellen können diese stützen oder korrigieren, belegen aber nicht rückwirkend eine zuvor nicht erfolgte Quellenarbeit.
4. **Bei fehlendem Lesezugriff:** Keine scheinbar werkgebundene Analyse auf Basis allgemeinen Modellwissens ausgeben. Quellenzugriffsgrenze benennen und eine ausdrücklich als eigenständig gekennzeichnete Analyse nur als Alternative anbieten.

Bei einer reinen sprachlichen Überarbeitung nach bereits belegter Analyse müssen nicht dieselben Originalstellen erneut abgerufen werden, sofern sie im Gespräch tatsächlich vorliegen; zusätzliche fachliche Behauptungen sind aber erneut zu prüfen.

## Koordination mit anderen Fachskills

Die Nutzung eines homiletischen oder exegetischen Skills **ersetzt keine Originallektüre** des vom Nutzer ausdrücklich genannten Autors oder Werks. Kategorien aus `THEOAgent - Homiletik` und `THEOAgent - Exegese Homiletischer Arbeitsgang` sind zunächst **THEOAgent-interne Kriterien** und dürfen nicht automatisch als „nach Klippert“ oder „von Klippert gefordert“ ausgegeben werden.

Bei einer solchen Analyse gilt die Reihenfolge **Werkstelle lesen → konkrete Autorposition mit passender Fundstelle belegen → eigene Predigtbewertung anhand dieser belegten Position**. Gib die tatsächlich nachgelesenen Originalstellen in der Antwort an. Eine gelesene Kapitelüberschrift oder die bloße Quellenliste reicht nicht als Nachweis des Inhalts; eine `view_knowledge_file`-Ausführung ohne zugänglichen relevanten Text begründet ebenfalls keine autorbezogene Zuschreibung.

Belege zu anderen Autoren oder Normtexten sind jeweils eigenständig zu prüfen. Wird eine Position nicht belegt, entferne die Zuschreibung oder kennzeichne sie als nicht überprüfbar; verweise nicht stattdessen auf einen anderen Fachskill als vermeintlichen Originalbeleg.

## Verfahren (verbindlich)

1. **Quellenlage feststellen.** Wähle je nach Quellenart die zugeordnete Wissensbasis oder die zuständige offizielle Webseite und prüfe, ob das angefragte Dokument verfügbar ist. Nutze bei Bedarf `search_knowledge_files`, `query_knowledge_files` und die Dateiansicht. Wenn eine Quelle nicht verfügbar ist, benenne diese Grenze, ohne Inhalt zu erfinden.
2. **Fundstelle lokalisieren.** Verwende `grep_knowledge_files` für Titel, Überschriften, eindeutige Fachbegriffe und gegebenenfalls alternative Schreibweisen. Behandle Treffer im Inhaltsverzeichnis, Register, Literaturverzeichnis und Fließtext als unterschiedliche Fundstellentypen. Scheitert `grep_knowledge_files` (z. B. Timeout), suche mit einem engeren, prägnanten Begriff **innerhalb der bereits identifizierten Datei-ID** weiter; nutze ergänzend `query_knowledge_files`, wenn eine gezielte Textsuche keinen Fließtexttreffer liefert. Ein Suchfehler ist weder ein Beleg noch ein Grund, das Inhaltsverzeichnis als gelesenen Originalabschnitt zu behandeln.
3. **Original lesen.** Rufe den tatsächlichen Fließtext mit `view_knowledge_file` auf; lies genügend Zeilen davor und danach, um den Gedankengang zu erfassen. Ein Inhaltsverzeichnis oder Vektorsuchtreffer allein ist **kein** Beleg für inhaltliche Behauptungen. Folge bei Seitenumbrüchen, Fußnoten und abgeschnittenen Werkzeugausgaben den Fortsetzungen, bis die Belegstelle vollständig ist.
4. **Aussagen prüfen.** Trenne konsequent (a) wörtlich im Original Belegtes, (b) textnahe Paraphrase, (c) eigene theologische Einordnung und (d) verbindliche kirchliche Lehre. Schreibe einer Autorin oder einem Autor nur Aussagen zu, die in den tatsächlich gelesenen Textpassagen gedeckt sind.
5. **Zitate und Fundstellen abgleichen.** Wörtliche Zitate exakt am abgerufenen Original prüfen. Druckseiten nur angeben, wenn eindeutig im Text erkannt oder mit verlässlicher Seitenzuordnung verifiziert; PDF-Seiten, Buchseiten und Werkzeug-Zeilennummern dürfen nicht gleichgesetzt werden. Bei Text über Seiten-/Zeilengrenzen hinweg den vollständigen belegenden Bereich angeben, gegebenenfalls mehrere Bereiche. Trennstriche und Zeilenumbrüche dürfen leserlich normalisiert werden, nicht der Aussagegehalt.
6. **Antwort mit Quellenstatus.** Quelle (Autor, Werk, Edition soweit nachgewiesen) und tatsächlich überprüfte Druckseiten/Fundstellen nennen. Fehlende exakte Angaben als **nicht verifiziert** kennzeichnen. Bei unvollständigem Zugriff keine rekonstruierte Autorposition als geprüfte Lektüre ausgeben.

## Speziell bei großen Büchern

- Inhaltsverzeichnis nur als Navigationshilfe verwenden; aus der dortigen Druckseitenangabe die Fließtextstelle über `grep_knowledge_files` lokalisieren.
- Bei mehreren Treffern den Treffer im Haupttext statt Register/Inhaltsverzeichnis auswählen.
- `view_knowledge_file` gezielt in kurzen, zusammenhängenden Intervallen aufrufen; nicht von Zeile 1 fortlaufend durch zehntausende Zeilen blättern.
- Semantisch unpassende Treffer nicht allein wegen hoher Relevanzwerte als Beweis verwenden.
- Kein unbegrenztes Suchen: Wenn nach angemessenen Suchvarianten keine Primärstelle greifbar ist, die Einschränkung transparent benennen.

## Werkzeugsteuerung und Abbruchregeln

Diese Regeln gelten für **jeden** Rechercheauftrag mit nativen Wissenswerkzeugen:

- **Zuerst `grep_knowledge_files`** für eine bekannte Überschrift oder prägnante Formulierung; semantische Suche nur ergänzend, falls nötig. Nach einem Timeout die Suche **mit kurzer Zeichenfolge und `file_id`** auf die bereits gefundene Datei einschränken; nicht ungeprüft zur Antwort oder zur Lektüre nur des Inhaltsverzeichnisses übergehen. Den Treffer **im Fließtext** auswählen.
- **Werkzeug-Zeilennummern sind keine Buchseiten.** Wenn `grep_knowledge_files` beispielsweise eine Überschrift in Werkzeugzeile 1782 und im Inhaltsverzeichnis Buchseite 42 meldet, muss `view_knowledge_file` mit `start_line` nahe **1782** arbeiten, niemals mit `start_line: 42` aufgrund der Buchseite.
- **Große, zielgerichtete Lesebereiche:** für das Haupttextfenster gewöhnlich 100–250 Werkzeugzeilen abrufen. Für einen kurzen Abschnitt reichen in der Regel 1–3 gezielte `view_knowledge_file`-Aufrufe, ergänzt um einen kurzen Nachleseaufruf zur Belegprüfung.
- **Keine Wiederholungen:** denselben oder einen weitgehend überlappenden Bereich niemals erneut lesen, solange kein konkreter fehlender Text begründet werden kann. Nach einem Inhaltsverzeichnis-Treffer direkt zur Haupttext-Fundstelle wechseln.
- **Harter Abbruch zur Kostensicherung:** Höchstens **8 Wissens-Werkzeugaufrufe insgesamt** je einfacher Einzelquellenfrage. Sind innerhalb dieser Grenze nicht genügend originale Textbelege verfügbar, den Stand offenlegen und mit einer Teilantwort oder Fehlermeldung abschließen; keine Suchschleife. Bei nachweislich sehr umfangreicher Quellenfrage zunächst knapp über den zusätzlichen Bedarf informieren, nicht unbegrenzt weitersuchen.
- **Vor jedem weiteren Aufruf:** Prüfen, ob eine neue Information zu erwarten ist. Wenn drei zentrale Aussagen bereits durch gelesenen Originaltext belegt sind, **sofort antworten**.
- Keine absolute Fundstellenposition aus einem früheren Test als allgemeingültig verwenden; die aktuelle `grep_knowledge_files`-Ausgabe ist maßgeblich.

## Abschlusskontrolle (intern vor Ausgabe)

- Habe ich **den Originalabschnitt** tatsächlich gelesen, nicht nur ein Verzeichnis?
- Stützt jede zugeschriebene Aussage der abgerufene Wortlaut?
- Stimmen kurze Zitate mit der Quelle überein?
- Sind Druckseiten und Zeilenbelege korrekt zugeordnet und vollständig, einschließlich Fortsetzungen?
- Habe ich nicht belegte Interpretationen ausdrücklich von Quellenaussagen getrennt?

**Negativregel:** Niemals bibliografische Details, Zitate, Seitenangaben oder Aussagen bestimmter Autoren aus allgemeinen Modellkenntnissen ergänzen, wenn die Anfrage Quellenverifikation verlangt.

## Testanker

Böttigheimer, *Lehrbuch der Fundamentaltheologie*, 4. Auflage: Abschnitt „b) Christliche Theologie als »sacra doctrina«“, Druckseiten 42–45. Im dokumentierten Probelauf lag die Überschrift im eigentlichen Text bei Indexzeile 1782, nicht beim Inhaltsverzeichnistreffer 76. Diese **Zeilenpositionen sind lediglich ein Testbeispiel**, keine allgemeingültigen Fundstellen und dürfen nach Neuindexierung nicht fest vorausgesetzt werden.
