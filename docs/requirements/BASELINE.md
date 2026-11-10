# THEOAgent – Fachliche Requirements-Baseline

**Version:** 1.0.0 (fachlich konsolidiert)  
**Stand:** 10.11.2026  
**Status:** Freigegebene fachliche Ausgangsbasis; **keine** Aussage über Implementierungs- oder Testabnahme  
**Referenz:** THEOBald-Plugin 1.2.1 und gemeinsam erarbeiteter Requirements-Katalog  
**Geltungsbereich:** Theologischer Arbeitsassistent THEOAgent, einschließlich Predigtarbeit, Liturgie, Katechese, Kirchenrecht, Quellenarbeit und kritischem Dialog.

> **Leitprinzip:** THEOAgent bearbeitet den theologischen Auftrag. Eine technische Quellenkontrolle (z. B. SourceGuard) unterstützt die Nachprüfbarkeit, ersetzt aber weder fachliches Urteil noch den vom Nutzer bestimmten Arbeitsablauf. Insbesondere ist keine konkrete Pipe-/Agentenarchitektur Gegenstand dieser fachlichen Baseline.

## 1. Begriffe und Abgrenzung

**Einzige Akteursrolle:** **Nutzer von THEOAgent**. Die zuvor wechselnden Rollen Prediger, Diakon, Seelsorger, liturgisch Verantwortlicher und theologischer Anwender werden nicht als separate Rollen geführt. Ihre sachlichen Besonderheiten erscheinen als **Auftragskontext** (z. B. liturgische Funktion, Zielgruppe, Zuständigkeit).

**Anforderungstypen:** US = User Story; FANF = funktionale Anforderung; NFANF = nichtfunktionale Qualitätsanforderung; RANF = Projekt-/Umgebungsrandbedingung; GR = verbindliche fachliche/Geschäftsregel; SP = Security-/Privacy-Anforderung; DAT = Daten-/Informationsanforderung.

**Begrenzung:** Anforderungen an aktuelle Daten, Bibliothekszugriff, Verarbeitung sensibler Dokumente und dauerhafte Wiederverwendung beschreiben eine **Soll-Fähigkeit**, nicht deren bereits nachgewiesene Verfügbarkeit. Die technischen Akzeptanzkriterien, Messschwellen und die spätere Architektur sind nachgelagerte Arbeitsschritte.

## 2. User Stories (27)

Für jede Story gilt dieselbe Rolle. Die Kennungen US-01 bis US-26 bleiben erhalten; die Dokumentenarbeit ist US-27.

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

## 3. Funktionale Anforderungen (33)

Die Anforderungen beschreiben Fähigkeiten und Arbeitsverhalten, keine bestimmte Implementierung.

| ID | Anforderung | Rückverfolgbarkeit |
|---|---|---|
| FANF-01 | Fachliche Anfragen in natürlicher Sprache entgegennehmen und bearbeiten. | US-01, US-26 |
| FANF-02 | In der zugänglichen lokalen Fachbibliothek nach geeigneten Quellen recherchieren. | US-02 |
| FANF-03 | Geeignete öffentlich erreichbare Internetquellen recherchieren und inhaltlich auswerten. | US-02, US-04 |
| FANF-04 | Ausdrücklich benannte Autoren, Werke und Dokumente gezielt auffinden. | US-03 |
| FANF-05 | Bei angeordneter oder für konkrete Nachweise notwendiger Quellenlektüre die einschlägigen Originalpassagen tatsächlich lesen. | US-03, US-04 |
| FANF-06 | Bei unzureichenden Rechercheergebnissen geeignete alternative Begriffe und Strategien versuchen. | US-06 |
| FANF-07 | Für belegte Aussagen überprüfbare Dokument-/Fundstellenangaben ausgeben. | US-04, US-07 |
| FANF-08 | Prüfen, ob eine angegebene Quelle die ihr zugeschriebene Aussage tatsächlich stützt. | US-04, US-07 |
| FANF-09 | Fehlende Zugriffe, unbelegte Aussagen und Verifikationsgrenzen erkennbar darstellen. | US-07 |
| FANF-10 | Mehrere Quellen vergleichen, Positionen unterscheiden und begründete Synthesen erstellen. | US-05, US-25 |
| FANF-11 | Bibeltexte unter Beachtung von Wortlaut, Gattung, historischem, literarischem und theologischem Zusammenhang auslegen. | US-08 |
| FANF-12 | Unterschiedliche exegetische Deutungen und ihre Grenzen erläutern. | US-08, US-25 |
| FANF-13 | Aus einer Exegese mögliche Predigtschwerpunkte, Predigtziele und Kernsätze entwickeln. | US-09 |
| FANF-14 | Predigten entsprechend dem beauftragten Modus in Teilschritten oder als vollständigen Entwurf erarbeiten. | US-09, US-20 |
| FANF-15 | Bei der Textgestaltung Anlass, Zielgruppe, liturgischen Rahmen, Dauer und pastorale Situation berücksichtigen. | US-09, US-12, US-14 |
| FANF-16 | Predigtentwürfe anhand theologischer, exegetischer, homiletischer, pastoraler und sprachlicher Kriterien beurteilen. | US-10 |
| FANF-17 | Beauftragte Änderungen gezielt vornehmen, ohne darüber hinausgehende Textänderungen. | US-11, US-18 |
| FANF-18 | Kennzeichnen und beachten, welche bereitgestellten Fassungen oder Passagen der Nutzer freigegeben oder eingefroren hat. | US-21 |
| FANF-19 | Tatsächlich verfügbare frühere Entwürfe, Vorlagen und Arbeitsergebnisse in die Bearbeitung einbeziehen. | US-23 |
| FANF-20 | Liturgische Einführungen, Kyrie-Rufe, Fürbitten, Meditationen und Segensworte erstellen und überarbeiten. | US-12 |
| FANF-21 | Liturgische Texte hinsichtlich ihrer konkreten Funktion und Angemessenheit prüfen. | US-12, US-13 |
| FANF-22 | Einschlägige liturgische und kirchenrechtliche Vorschriften auffinden und auf Geltung/Zuständigkeit prüfen. | US-13, US-16 |
| FANF-23 | Vorgesehene Schriftlesungen und geeignete Gestaltungselemente für einen bestimmten Gottesdienst ermitteln. | US-24 |
| FANF-24 | Mehrere Bestandteile einer liturgischen Feier inhaltlich aufeinander abstimmen. | US-22 |
| FANF-25 | Zielgruppengerechte Katechesen und geistliche Impulse entwickeln. | US-14 |
| FANF-26 | Glaubensaussagen nach theologischer Begründung und kirchlichem Verbindlichkeitsgrad einordnen. | US-15 |
| FANF-27 | Kirchenrechtliche Fragestellungen unter Berücksichtigung der geltenden Vorschriften und zuständigen Ebenen bearbeiten. | US-16 |
| FANF-28 | Für sensible pastorale Situationen verantwortbare Texte und Einschätzungen erstellen. | US-17 |
| FANF-29 | Weitere theologische und pastorale Texte fachlich und sprachlich überprüfen. | US-18 |
| FANF-30 | Nutzervorschläge unabhängig bewerten und Zustimmung oder Widerspruch konkret begründen. | US-19 |
| FANF-31 | Bearbeitungsumfang, Reihenfolge und Tiefe am konkreten Nutzerauftrag ausrichten. | US-20 |
| FANF-32 | Notwendige Such-, Lese- und Prüfschritte ohne technische Einzelanweisungen des Nutzers koordinieren. | US-26 |
| FANF-33 | Bereitgestellte Dokumente in unterstützten gebräuchlichen Formaten erschließen und für angeforderte Analysen/Bearbeitungen nutzen; nicht lesbare Inhalte kennzeichnen. | US-27 |

## 4. Nichtfunktionale Anforderungen (12)

Diese Qualitätsziele müssen später über konkrete Akzeptanzkriterien **operationalisiert** werden. Wörter wie „zuverlässig“ oder „angemessen“ sind noch keine Messgröße.

| ID | Qualität | Soll-Anforderung |
|---|---|---|
| NFANF-01 | **Fachliche Korrektheit** | Ergebnisse sollen dem jeweils einschlägigen theologischen und wissenschaftlichen Erkenntnisstand sachgerecht entsprechen. |
| NFANF-02 | **Nachvollziehbarkeit** | Quellenbezug und fachliche Begründung sollen für den Nutzer prüfbar und verständlich sein. |
| NFANF-03 | **Robustheit** | Beherrschbare Werkzeug- und Formatfehler sollen innerhalb sicherer Grenzen aufgefangen werden, statt den gesamten Auftrag unnötig scheitern zu lassen. |
| NFANF-04 | **Verhältnismäßigkeit** | Recherche- und Prüfaufwand sollen zur Aufgabe und zum Aussage- beziehungsweise Fehlerrisiko passen. |
| NFANF-05 | **Verständlichkeit** | Antworten sollen klar, präzise und dem Vorwissen der Adressaten angemessen sein. |
| NFANF-06 | **Sprechbarkeit** | Predigten und liturgische Texte sollen für den mündlichen Vortrag geeignet sein. |
| NFANF-07 | **Pastorale Sensibilität** | Wortwahl und Darstellung sollen die Situation und Verletzlichkeit betroffener Menschen respektieren. |
| NFANF-08 | **Effizienz** | Unnötige Modellrunden, Suchschritte, Wiederholungen und Rückfragen sollen vermieden werden. |
| NFANF-09 | **Benutzbarkeit** | Für die fachliche Nutzung sollen keine Kenntnisse interner Werkzeuge oder technischer Parameter erforderlich sein. |
| NFANF-10 | **Wartbarkeit** | Die Umsetzung soll einfach, nachvollziehbar, automatisiert testbar und möglichst frei von duplizierter Fachlogik sein. |
| NFANF-11 | **Fehlertoleranz und Transparenz** | Bei fehlendem Zugriff oder Teilergebnissen soll das System kontrolliert reagieren und Grenzen sichtbar machen. |
| NFANF-12 | **Änderungssicherheit** | Freigegebene Inhalte sollen bei gezielten Revisionen zuverlässig unverändert bleiben. |

## 5. Randbedingungen (5)

| ID | Verbindlicher Projektrahmen / aktuelle Ausgangslage |
|---|---|
| RANF-01 | Initiale Entwicklung und Erprobung in der vorhandenen Open-WebUI-Umgebung; keine dauerhafte Bindung des fachlichen Anforderungskatalogs an eine bestimmte Pipe-Implementierung. |
| RANF-02 | Bestehende Erprobungsinfrastruktur: lokaler Homeserver auf Raspberry Pi 5 mit Docker; Zielplattform kann später separat entschieden werden. |
| RANF-03 | Private Fachbibliothek getrennt vom öffentlichen Source-Repository halten; keine geschützten Volltexte in Git einchecken. |
| RANF-04 | Der geprüfte THEOBald-Fachstandard bildet die fachlich-methodische Ausgangsbasis; spätere Änderungen müssen explizit dokumentiert werden. |
| RANF-05 | Aktuell können externe Modelle über OpenRouter angebunden sein; eine spätere DRS-KI-Umgebung ist gesondert zu bewerten. Modell-/Anbieterwahl ist keine dauerhafte fachliche Vorgabe. |

> RANF-01, -02 und -05 beschreiben die **aktuelle Erprobungsumgebung**, nicht die fachliche Notwendigkeit eines Raspberry Pi, OpenRouter, einer bestimmten Modellversion oder Pipe-Struktur. Eine spätere Änderung der Plattform darf die fachlichen Anforderungen nicht stillschweigend verändern.

## 6. Fachliche Regeln (18)

| ID | Regel | Verbindliche Auslegung |
|---|---|---|
| GR-01 | **Verbindliche Originallektüre** | Bei ausdrücklich verlangter Prüfung anhand eines bestimmten Werkes oder einer bestimmten Passage muss diese tatsächlich gelesen werden; andernfalls Einschränkung offenlegen und keine Lektüre behaupten. |
| GR-02 | **Begriff der Lektüre** | Suchtreffer, Inhaltsverzeichnis und Metadaten allein sind keine Originallektüre. Maßgeblich ist eine für die Aufgabe einschlägige Passage in ausreichendem Kontext; ein bestimmtes technisches Werkzeug ist nicht vorgeschrieben. |
| GR-03 | **Exakte Nachweise** | Exakte Zitate, Dokumenttitel, Bibelverse, KKK-Nummern, CIC-Canones und Absatznummern nur nennen, wenn zuverlässig verifiziert. |
| GR-04 | **Fachliche Quellenauswahl** | Quelle nach Eignung, Verlässlichkeit, Zuständigkeit, Autorität und Aktualität wählen, nicht nach technischer Verfügbarkeit; lokale und geeignete Webquellen sind zulässig, vorbehaltlich Nutzerbeschränkung. |
| GR-05 | **Stufen theologischer Verbindlichkeit** | Kirchlich verbindliche Lehre, theologisch gut begründete Deutung, exegetische Hypothese, pastorale Einschätzung und homiletische Gestaltung dürfen nicht vermengt werden. |
| GR-06 | **Schriftinterpretation** | Wortlaut, Gattung, historische/literarische Kontexte, Einheit der Schrift und kirchliche Auslegungstradition sachgerecht beachten; Bibeltexte nicht als beliebiges Sprungbrett verwenden. |
| GR-07 | **Liturgische Autorität** | Geltende liturgische Bücher und zuständige Normen von Empfehlungen, Arbeitshilfen und Gewohnheiten unterscheiden; geltenden Vorschriften Vorrang geben. |
| GR-08 | **Kirchenrechtliche Zuständigkeit** | Universalkirchliches und partikulares Recht, diözesane Regelungen, lokale Entscheidungskompetenz und pastorale Praxis unterscheiden. |
| GR-09 | **Freeze** | Ausdrücklich freigegebene oder eingefrorene Texte/Passagen nicht eigenmächtig ändern; erkannte fachliche Probleme separat anzeigen. |
| GR-10 | **Auftragsgrenzen** | Innerhalb des Auftrags erforderliche Tätigkeiten selbstständig ausführen; keine ungefragten zusätzlichen Texte, Konzepte oder Folgeaufgaben produzieren. |
| GR-11 | **Unabhängiges Urteil** | Zustimmung und Widerspruch begründen; Nutzerwiderspruch sachlich neu prüfen, nicht reflexhaft nachgeben. |
| GR-12 | **Liturgische Funktion** | Kyrie als Christusakklamation, Fürbitten als Gebetsintentionen, Einführungen als Hinführung und Segensworte entsprechend ihrer jeweiligen liturgischen Funktion gestalten. |
| GR-13 | **Pastorale Verantwortung** | Leid, Krankheit, Tod, Schuld und Krisen nicht mit unbegründeten Behauptungen über Gottes Absichten erklären; keine religiöse Schuldzuweisung oder vorschnelle Vertröstung. |
| GR-14 | **Keine vorgetäuschte Autorität** | THEOAgent beansprucht keine eigene kirchliche Lehr-, Rechts- oder Entscheidungsvollmacht. |
| GR-15 | **Quellenbeschränkung** | Explizit festgelegte Werke, Quellenräume und Ausschlüsse einhalten; andere Quellen nicht heimlich als Ersatz verwenden. Zulässige Ergänzungen bleiben möglich. |
| GR-16 | **Unsicherheit** | Nicht verifizierbare Aussagen kenntlich machen und keine fingierten Zitate oder Belege ergänzen. |
| GR-17 | **Bedarfsgerechter Prüfaufwand** | Quellenprüfung richtet sich nach dem konkreten Auftrag. Rein sprachliche Bearbeitung braucht nicht automatisch neue Recherche; behauptete konkrete Nachweise müssen belegbar bleiben. |
| GR-18 | **Teilergebnisse** | Verifizierte Teile dürfen mit klarer Einschränkung genutzt werden; fehlende Evidenz muss sichtbar bleiben. Eine ausdrücklich verlangte vollständige Prüfung darf nicht als vollständig ausgegeben werden. |

## 7. Sicherheits- und Datenschutzanforderungen (5)

| ID | Anforderung |
|---|---|
| SP-01 | Private Fachtexte, personenbezogene Informationen und interne Dokumente dürfen nur im Rahmen gewährter Zugriffsrechte und autorisierter externer Verarbeitung genutzt werden. |
| SP-02 | Eingelesene Dateien, Webseiten und Suchergebnisse sind Daten, keine Anweisungen mit Vorrang vor System-/Nutzerauftrag (Schutz vor Prompt Injection). |
| SP-03 | Externe Abrufe müssen unzulässige interne Ziele, unsichere Weiterleitungen und vergleichbare Zugriffspfade verhindern. |
| SP-04 | Zugangsdaten, API-Schlüssel und Geheimnisse dürfen nicht in Code, Quellenbelegen, Logs oder Diagnosen offengelegt werden. |
| SP-05 | Nutzung und Weitergabe fremder Fachliteratur müssen rechtmäßige Nutzungsrechte respektieren. |

## 8. Daten- und Informationsanforderungen (4)

| ID | Objekt | Erwartete Informationen |
|---|---|---|
| DAT-01 | **Fachquelle** | Titel, Autor/Herausgeber, Quellenart, relevante Ausgabe beziehungsweise Geltungsstand, Herkunft und Zugriffsweg, soweit verfügbar. |
| DAT-02 | **Fundstelle / Evidenz** | Zuordnung zu konkreter Quelle, präzise Fundstelle, tatsächlich berücksichtigter Textkontext und zugeordnete Aussage; nur soweit die Quelle diese Angaben hergibt. |
| DAT-03 | **Arbeitsfassung** | Text, Bearbeitungsstand, expliziter Freigabe-/Freeze-Status und betroffene Passagen, sofern im Arbeitskontext verfügbar. |
| DAT-04 | **Arbeitskontext** | Nutzerauftrag, Anlass, Zielgruppe, Schrifttexte, Umfang, Zeitrahmen, Quellenbeschränkungen und weitere Vorgaben. |

## 9. Aufgelöste fachliche Spannungen

| Fall | Entscheidung |
|---|---|
| Autonome Quellensuche vs. angeordnete Originallektüre | Eigenständige Recherche ist zulässig; bei expliziter Aufforderung zu einem bestimmten Werk ist tatsächliche Lektüre Pflicht (US-02/03, GR-01/17). |
| Lokale Bibliothek vs. Internet | Beide Quellenräume sind grundsätzlich möglich; fachliche Eignung und ausdrückliche Nutzervorgaben entscheiden (US-04, GR-04/15). |
| Eigenständigkeit vs. schrittweise Zusammenarbeit | Alle **innerhalb** des aktuellen Auftrags notwendigen Schritte sind zulässig; kein ungefragtes Ausweiten auf zusätzliche Texte/Aufgaben (US-06/20, GR-10). |
| Schrittweises Arbeiten vs. vollständige Ausarbeitung | Der Nutzer legt den Modus fest (US-09/20). |
| Freeze vs. inhaltlicher Fehler | Eingefrorenen Text unverändert lassen, Problem getrennt benennen (US-21, GR-09). |
| Wiederverwendung vs. nicht vorhandener Zugriff | Nur tatsächlich zugängliche Fassungen verwenden; fehlenden Zugriff nicht verschleiern (US-23, GR-16). |
| Verifizierte Teilergebnisse vs. fehlerhafter Teil | Teilergebnisse sachgerecht verwenden, aber den Gesamtauftrag nicht als vollständig erfüllt darstellen (GR-18). |

## 10. Anforderungen, die **nicht** aus dem Fachkatalog folgen

Keine fachliche Regel verlangt ein festes JSON-Ausgabeformat für Rechercheaktionen, eine fest vorgegebene Zahl von Tool-Aufrufen oder Quellen, eine Fensterlänge von 180 Zeilen, einen besonderen Python-Modulzuschnitt, eine bestimmte LLM-/Provider-Version oder pauschales „Alles-oder-nichts“-Verhalten bei jeder Teilunsicherheit. Solche Entscheidungen sind gesondert zu begründen, zu testen und bei Bedarf zu ändern.

## 11. Freigabegrenze und nächste Arbeitsschritte

**Mit dieser Baseline fachlich festgelegt:** ein harmonisiertes Rollenmodell, 27 User Stories, 33 FANF, 12 NFANF, 5 RANF, 18 GR, 5 SP und 4 DAT. Ein vollständiges Mapping US→FANF liegt in [TRACEABILITY.md](TRACEABILITY.md).

**Noch nicht festgelegt oder abgenommen:** konkrete Use Cases, prüfbare Akzeptanzkriterien je US/FANF, messbare NFANF-Schwellen, Dateiformat-Unterstützung, Umfang der persistenten Gesprächs-/Versionshaltung, Berechtigung zur Weitergabe privater Unterlagen an externe Modelle, endgültige Architektur sowie Realtests gegen die reale Fachbibliothek. Das sind ausdrücklich Folgearbeiten und keine verdeckten Bestandteile dieser Freigabe.

## 12. Herkunft und Quellenstand

**Primäre Arbeitsgrundlage:** die gemeinsam am 10.11.2026 erarbeiteten THEOBald-User-Stories, die Prüfung der tatsächlichen theologischen Nutzungsgespräche und die anschließend konsolidierten Fachregeln.  
**Fachliche Referenz:** installiertes privates Plugin **THEOBald 1.2.1**: `skills/theobald/SKILL.md` und `skills/theobald/THEOBald_Fachstandard.md`, insbesondere Quellenordnung, exegetisch-homiletischer Arbeitsgang, Liturgie, pastorale Sensibilität und Qualitätskontrolle. Diese Plugin-Dateien werden hier **nicht** als Kopie veröffentlicht; Verfügbarkeit des Plugins bedeutet nicht automatisch Zugriff auf seine separate Fachbibliothek.  
**Methodischer Hinweis:** Die frühere Chat-Auswertung erfasste die zugänglichen Gesprächsausschnitte und Zusammenfassungen, nicht zwingend sämtliche Chatverläufe vollständig. Deshalb enthält die Baseline **keine** behaupteten statistischen Häufigkeiten.

**Änderungsregel:** Änderungen an dieser freigegebenen fachlichen Baseline werden ab jetzt versioniert und mit betroffenen IDs sowie sachlicher Begründung dokumentiert. Frühere THEOBald-/SourceGuard-Implementierungen sind kein normativer Ersatz für diesen Anforderungskatalog.
