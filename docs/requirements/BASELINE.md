# THEOAgent – Fachliche Requirements-Baseline

**Version:** 1.1.0  
**Stand:** 10.11.2026  
**Status:** Fachlich verbindliche Anforderungsspezifikation; Implementierung und Tests nicht abgenommen  
**Geltungsbereich:** Theologischer Arbeitsassistent THEOAgent, einschließlich Predigtarbeit, Liturgie, Katechese, Kirchenrecht, Quellenarbeit und kritischem Dialog.

## 1. Begriffe und Abgrenzung

**Rolle – Nutzer:** Person, die THEOAgent mit theologischen oder liturgischen Aufgaben beauftragt. Anlass, Zielgruppe, liturgische Funktion und kirchliche Zuständigkeit sind Kontextmerkmale.

**Anforderungstypen:** US = User Story; FANF = funktionale Anforderung; NFANF = nichtfunktionale Qualitätsanforderung; RANF = Projekt-/Umgebungsrandbedingung; GR = verbindliche fachliche/Geschäftsregel; SP = Security-/Privacy-Anforderung; DAT = Daten-/Informationsanforderung.

**Verbindlichkeit:** Alle MUSS-Anforderungen sind verbindlich. Ihre Erfüllung ist erst nach erfolgreichen Akzeptanzprüfungen nachgewiesen.

## 2. User Stories (27)

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

## 3. Funktionale Anforderungen (33)

Die funktionalen Anforderungen verwenden die SOPHIST-Unterscheidung zwischen Benutzerinteraktion, Systemaktivität und bedingter Funktion. Sie schreiben keine Implementierung vor.

| ID | Anforderung | Rückverfolgbarkeit |
|---|---|---|
| FANF-01 | THEOAgent muss dem Nutzer die Möglichkeit bieten, eine theologische Fachfrage in natürlicher Sprache zu übermitteln. | US-01, US-26 |
| FANF-02 | Falls die lokale Fachbibliothek für den Auftrag zugelassen und zugänglich ist, muss THEOAgent sie nach einschlägigen Fachquellen durchsuchen. | US-02 |
| FANF-03 | Falls die Recherche Internetquellen zulässt, muss THEOAgent öffentlich zugängliche Internetquellen nach einschlägigen Fachquellen durchsuchen. | US-02, US-04 |
| FANF-04 | Falls der Nutzer einen Autor, ein Werk oder ein Dokument benennt, muss THEOAgent gezielt nach dieser Quelle suchen. | US-03 |
| FANF-05 | Falls der Nutzer eine Originallektüre verlangt oder eine konkrete Quellenbehauptung zu prüfen ist, muss THEOAgent die einschlägige Originalpassage in ausreichendem Kontext lesen. | US-03, US-04 |
| FANF-06 | Falls eine Suche keine einschlägigen Ergebnisse liefert und weitere zulässige Suchwege verfügbar sind, muss THEOAgent eine veränderte Suchanfrage ausführen. | US-06 |
| FANF-07 | Falls THEOAgent eine Aussage auf eine konkrete Quelle stützt, muss THEOAgent die zugehörige überprüfbare Fundstelle in der Antwort ausweisen. | US-04, US-07 |
| FANF-08 | Falls THEOAgent eine Fundstelle als Beleg verwendet, muss THEOAgent deren Inhalt auf Übereinstimmung mit der belegten Aussage prüfen. | US-04, US-07 |
| FANF-09 | Falls eine benötigte Quelle unzugänglich oder eine Quellenbehauptung nicht überprüfbar ist, muss THEOAgent diese Einschränkung in der Antwort kennzeichnen. | US-07 |
| FANF-10 | Falls der Nutzer einen Quellenvergleich beauftragt, muss THEOAgent die fachlichen Positionen der Quellen gegenüberstellen. | US-05, US-25 |
| FANF-11 | Falls der Nutzer einen Bibeltext auslegen lässt, muss THEOAgent den Text unter Berücksichtigung seines literarischen, historischen und theologischen Kontextes interpretieren. | US-08 |
| FANF-12 | Falls zu einem Bibeltext mehrere relevante Deutungen vorliegen, muss THEOAgent deren Unterschiede und Grenzen darstellen. | US-08, US-25 |
| FANF-13 | Falls der Nutzer eine Predigtbotschaft zu einem Bibeltext erarbeiten lässt, muss THEOAgent einen begründeten Predigtschwerpunkt aus dem Text ableiten. | US-09 |
| FANF-14 | THEOAgent muss dem Nutzer die Möglichkeit bieten, eine Predigt wahlweise in Teilschritten oder als vollständigen Entwurf erarbeiten zu lassen. | US-09, US-20 |
| FANF-15 | Falls der Nutzer für einen Entwurf Anlass, Zielgruppe, Dauer oder pastoralen Kontext vorgibt, muss THEOAgent diese Angaben bei der Textgestaltung berücksichtigen. | US-09, US-12, US-14 |
| FANF-16 | Falls der Nutzer einen Predigtentwurf zur Prüfung vorlegt, muss THEOAgent diesen anhand theologischer, exegetischer, homiletischer, pastoraler und sprachlicher Kriterien beurteilen. | US-10 |
| FANF-17 | Falls der Nutzer die Änderung bestimmter Textpassagen beauftragt, muss THEOAgent die benannten Passagen bearbeiten und die übrigen Passagen unverändert lassen. | US-11, US-18 |
| FANF-18 | THEOAgent muss dem Nutzer die Möglichkeit bieten, eine Textfassung oder einzelne Textpassagen als eingefroren zu kennzeichnen. | US-21 |
| FANF-19 | Falls eine frühere Arbeitsfassung zugänglich ist und der Nutzer ihre Wiederverwendung verlangt, muss THEOAgent diese als Arbeitsgrundlage verwenden. | US-23 |
| FANF-20 | THEOAgent muss dem Nutzer die Möglichkeit bieten, liturgische Einführungen, Kyrie-Rufe, Fürbitten, Meditationen und Segensworte erstellen oder überarbeiten zu lassen. | US-12 |
| FANF-21 | Falls der Nutzer einen liturgischen Text prüfen lässt, muss THEOAgent dessen Übereinstimmung mit der liturgischen Funktion beurteilen. | US-12, US-13 |
| FANF-22 | Falls eine konkrete liturgische oder kirchenrechtliche Norm für eine Auskunft maßgeblich ist, muss THEOAgent deren geltende Fassung anhand einer zuständigen Quelle prüfen. | US-13, US-16 |
| FANF-23 | Falls der Nutzer eine konkrete liturgische Feier vorbereitet, muss THEOAgent deren Schriftlesungen und geeignete Gestaltungselemente anhand einschlägiger Quellen ermitteln. | US-24 |
| FANF-24 | Falls der Nutzer mehrere Teile einer liturgischen Feier beauftragt, muss THEOAgent diese unter Beachtung ihrer jeweiligen Funktion aufeinander abstimmen. | US-22 |
| FANF-25 | THEOAgent muss dem Nutzer die Möglichkeit bieten, eine Katechese oder einen geistlichen Impuls für eine vorgegebene Zielgruppe erstellen zu lassen. | US-14 |
| FANF-26 | Falls der Nutzer eine Glaubensaussage zur Einordnung vorlegt, muss THEOAgent diese einer in GR-05 definierten Verbindlichkeitsstufe zuordnen. | US-15 |
| FANF-27 | Falls der Nutzer eine kirchenrechtliche Frage stellt, muss THEOAgent die einschlägigen geltenden Bestimmungen der zuständigen Rechtsebene auswerten. | US-16 |
| FANF-28 | THEOAgent muss dem Nutzer die Möglichkeit bieten, eine fachliche Einschätzung oder einen Text zu einer sensiblen pastoralen Situation erarbeiten zu lassen. | US-17 |
| FANF-29 | THEOAgent muss dem Nutzer die Möglichkeit bieten, einen theologischen oder pastoralen Text auf fachliche und sprachliche Stimmigkeit prüfen zu lassen. | US-18 |
| FANF-30 | Falls der Nutzer eine fachliche Position zur Beurteilung vorlegt, muss THEOAgent sie unabhängig von der Nutzermeinung anhand sachlicher Gründe bewerten. | US-19 |
| FANF-31 | Falls der Nutzer den aktuellen Arbeitsschritt oder Arbeitsumfang festlegt, muss THEOAgent die Bearbeitung auf diesen Umfang begrenzen. | US-20 |
| FANF-32 | Falls ein Auftrag Recherche oder Originallektüre erfordert, muss THEOAgent die erforderlichen Such- und Leseoperationen ohne technische Einzelanweisungen des Nutzers steuern. | US-26 |
| FANF-33 | THEOAgent muss dem Nutzer die Möglichkeit bieten, bereitgestellte Dokumente in unterstützten Dateiformaten für die fachliche Bearbeitung zu verwenden. | US-27 |

## 4. Nichtfunktionale Anforderungen (12)

Die Anforderungen verwenden den EigenschaftsMASTER. Noch nicht vereinbarte Testkorpora und Grenzwerte sind als **offen** bezeichnet; ihre Festlegung ist Voraussetzung einer messbaren Abnahme.

| ID | Qualität | Soll-Anforderung |
|---|---|---|
| NFANF-01 | **Fachliche Korrektheit** | Der Anteil fachlich korrekter Antworten im festzulegenden Testkorpus muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Mindestwert und Korpus offen. |
| NFANF-02 | **Nachvollziehbarkeit** | Der Anteil belegpflichtiger Aussagen mit überprüfbarer Fundstelle muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Mindestwert und Prüfkorpus offen. |
| NFANF-03 | **Robustheit** | Die Erfolgsquote bei definierten technisch beherrschbaren Werkzeug- und Formatfehlern muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Fehlerklassen und Mindestwert offen. |
| NFANF-04 | **Verhältnismäßigkeit** | Der Rechercheaufwand für Aufgaben ohne fachlichen Recherchebedarf muss die vereinbarte Aufwandgrenze einhalten. **Prüfmaß:** Aufwandmaß und Grenze offen. |
| NFANF-05 | **Verständlichkeit** | Der Anteil der von der Zielgruppe als verständlich bewerteten Texte muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Bewertungsverfahren und Mindestwert offen. |
| NFANF-06 | **Sprechbarkeit** | Der Anteil der bei mündlichen Proben als sprechbar bewerteten Predigt- und Liturgietexte muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Prüfverfahren und Mindestwert offen. |
| NFANF-07 | **Pastorale Sensibilität** | Der Anteil der Texte, die das fachlich vereinbarte Verfahren zur Prüfung pastoraler Sensibilität bestehen, muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Prüfverfahren und Mindestwert offen. |
| NFANF-08 | **Effizienz** | Die Bearbeitungsdauer definierter Standardaufträge muss die vereinbarte Zeitgrenze einhalten. **Prüfmaß:** Auftragsklassen und Zeitgrenzen offen. |
| NFANF-09 | **Benutzbarkeit** | Der Anteil der Standardaufträge, die ohne Kenntnis interner Werkzeuge erteilt werden können, muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Standardaufträge und Mindestwert offen. |
| NFANF-10 | **Wartbarkeit** | Der Änderungsaufwand für definierte Standardänderungen muss die vereinbarte Aufwandsgrenze einhalten. **Prüfmaß:** Standardänderungen und Grenze offen. |
| NFANF-11 | **Fehlertransparenz** | Der Anteil fehlgeschlagener Quellenzugriffe, die dem Nutzer als fehlgeschlagen angezeigt werden, muss den vereinbarten Mindestwert erreichen. **Prüfmaß:** Testkorpus und Mindestwert offen. |
| NFANF-12 | **Änderungssicherheit** | Die Anzahl unbeauftragter Änderungen an eingefrorenen Passagen muss in den Abnahmetests gleich null sein. **Prüfmaß:** Null unbeauftragte Änderungen. |

## 5. Randbedingungen (5)

| ID | Verbindlicher Projektrahmen / aktuelle Ausgangslage |
|---|---|
| RANF-01 | Für die initiale Erprobung muss THEOAgent in der bestehenden Open-WebUI-Umgebung ausführbar sein. |
| RANF-02 | Für die initiale Erprobung muss THEOAgent auf dem vorhandenen lokalen Docker-Homeserver betrieben werden können. |
| RANF-03 | Das öffentliche Repository darf keine privaten urheberrechtlich geschützten Fachbibliotheksvolltexte enthalten. |
| RANF-04 | Vor einer fachlichen Implementierungsabnahme muss der verbindliche theologische Fachstandard in einer versionierten Fassung verfügbar sein. |
| RANF-05 | Falls in der Erprobung externe Modelle eingesetzt werden, muss THEOAgent mit der vorgesehenen OpenRouter-Anbindung zusammenarbeiten können. |

> RANF-01, -02 und -05 beschreiben die **aktuelle Erprobungsumgebung**, nicht die fachliche Notwendigkeit eines Raspberry Pi, OpenRouter, einer bestimmten Modellversion oder Pipe-Struktur. Eine spätere Änderung der Plattform darf die fachlichen Anforderungen nicht stillschweigend verändern.

## 6. Fachliche Regeln (18)

| ID | Regel | Verbindliche Auslegung |
|---|---|---|
| GR-01 | **Originallektüre** | Falls der Nutzer die Prüfung eines bestimmten Werkes oder einer bestimmten Passage beauftragt, muss THEOAgent die einschlägige Originalstelle lesen oder die fehlende Zugriffsmöglichkeit offenlegen. |
| GR-02 | **Lektürenachweis** | THEOAgent darf Suchtreffer, Inhaltsverzeichnisse und bibliografische Metadaten nicht als Nachweis einer Originallektüre ausgeben. |
| GR-03 | **Exakte Nachweise** | THEOAgent darf exakte Zitate, Bibelstellen, Dokumenttitel, KKK-Nummern, Canones und Absatznummern nur nach Verifikation ausgeben. |
| GR-04 | **Quellenauswahl** | THEOAgent muss die Auswahl zugelassener Fachquellen an Relevanz, Verlässlichkeit, zuständiger Autorität und Geltungsstand ausrichten. |
| GR-05 | **Verbindlichkeitsstufen** | THEOAgent muss kirchlich verbindliche Lehre, theologische Deutung, exegetische Hypothese, pastorale Einschätzung und homiletische Gestaltung unterscheiden. |
| GR-06 | **Bibeltexttreue** | THEOAgent muss bei Bibelauslegungen Gattung, Textzusammenhang, historischen Kontext und kirchliche Auslegungstradition berücksichtigen. |
| GR-07 | **Liturgische Normen** | THEOAgent muss geltende liturgische Vorschriften von Empfehlungen, Arbeitshilfen und Gewohnheiten unterscheiden. |
| GR-08 | **Rechtsebenen** | THEOAgent muss bei kirchenrechtlichen Aussagen Rechtsebene und zuständige Entscheidungsinstanz berücksichtigen. |
| GR-09 | **Freeze** | Solange eine Textfassung oder Passage eingefroren ist, darf THEOAgent sie ohne ausdrückliche erneute Nutzerfreigabe nicht verändern. |
| GR-10 | **Auftragsgrenze** | THEOAgent darf die für einen Auftrag erforderlichen Teilschritte ausführen, aber ohne Beauftragung keine zusätzlichen Folgeaufgaben übernehmen. |
| GR-11 | **Unabhängiges Urteil** | THEOAgent muss fachliche Urteile sachlich begründen und darf sie nicht allein aufgrund von Zustimmung oder Widerspruch des Nutzers ändern. |
| GR-12 | **Liturgische Funktion** | THEOAgent muss bei der Erstellung liturgischer Texte deren jeweilige liturgische Funktion berücksichtigen. |
| GR-13 | **Pastorale Verantwortung** | THEOAgent darf leidvolle Ereignisse ohne tragfähige Grundlage nicht als Gottes konkrete Absicht, Strafe oder pädagogische Maßnahme darstellen. |
| GR-14 | **Keine Amtsautorität** | THEOAgent darf keine eigene kirchliche Lehr-, Rechts- oder Entscheidungsvollmacht behaupten. |
| GR-15 | **Quellenbeschränkung** | Falls der Nutzer bestimmte Werke oder Quellenräume verbindlich vorgibt, muss THEOAgent die Recherche darauf begrenzen. |
| GR-16 | **Unsicherheit** | Falls eine Aussage nicht verifiziert werden kann, muss THEOAgent die Unsicherheit kenntlich machen. |
| GR-17 | **Verhältnismäßigkeit** | THEOAgent muss den Prüfaufwand an den fachlichen Auftrag anpassen; eine reine Sprachrevision ohne zusätzliche Quellenbehauptung erfordert keine neue Fachrecherche. |
| GR-18 | **Teilergebnisse** | Falls die notwendige Quellenprüfung nicht vollständig möglich ist, muss THEOAgent verifizierte und nicht verifizierte Ergebnisse unterscheiden und den Gesamtauftrag als unvollständig kennzeichnen. |

## 7. Sicherheits- und Datenschutzanforderungen (5)

| ID | Anforderung |
|---|---|
| SP-01 | THEOAgent darf private Fachtexte und personenbezogene Informationen nur innerhalb der erteilten Zugriffs- und Verarbeitungsberechtigungen an externe Dienste übermitteln. |
| SP-02 | THEOAgent darf Anweisungen aus eingelesenen Dokumenten oder Internetseiten nicht als vorrangige System- oder Nutzeranweisungen ausführen. |
| SP-03 | Falls THEOAgent Internetadressen aufruft, muss THEOAgent unzulässige Zugriffe auf interne Netzwerkziele und unsichere Weiterleitungen verhindern. |
| SP-04 | THEOAgent darf API-Schlüssel, Zugangsdaten und andere Geheimnisse nicht in Antworten, Protokollen oder veröffentlichten Artefakten ausgeben. |
| SP-05 | THEOAgent muss bei der Bereitstellung oder Weitergabe fremder Fachliteratur die geltenden Nutzungsrechte einhalten. |

## 8. Daten- und Informationsanforderungen (4)

| ID | Objekt | Erwartete Informationen |
|---|---|---|
| DAT-01 | **Fachquelle** | THEOAgent muss einer verwendeten Quelle die verfügbaren Angaben zu Titel, Autor oder Herausgeber, Quellenart, Ausgabe, Geltungsstand und Herkunft zuordnen können. |
| DAT-02 | **Fundstelle** | THEOAgent muss einer als belegt ausgegebenen Aussage die entsprechende Quelle und eine überprüfbare Fundstelle zuordnen können. |
| DAT-03 | **Arbeitsfassung** | THEOAgent muss einer zugänglichen Arbeitsfassung ihren vom Nutzer gesetzten Freigabe- oder Freeze-Status zuordnen können. |
| DAT-04 | **Arbeitskontext** | THEOAgent muss dem aktuellen Auftrag vorhandene Angaben zu Anlass, Zielgruppe, Schrifttext, Umfang und Quellenbeschränkung zuordnen können. |

## 9. Abnahmegrenze

Diese Spezifikation legt das geforderte Verhalten fest. Akzeptanzfälle und noch offene Qualitätsgrenzwerte werden vor der Implementierungsabnahme festgelegt. Die Zuordnung der User Stories zu funktionalen Anforderungen steht in [TRACEABILITY.md](TRACEABILITY.md).

## 10. Formulierungsreferenzen

- [SOPHIST: Anforderungen richtig formulieren – FunktionsMASTER (2026)](https://blog.sophist.de/2026/08/26/anforderungen-richtig-formulieren-die-satzschablone-master-mit-beispielen/)
- [SOPHIST: Nicht-funktionale Anforderungen und EigenschaftsMASTER (2026)](https://blog.sophist.de/2026/10/19/nicht-funktionale-anforderungen/)
