# MCP als Integrationsarchitektur für die Diözese Rottenburg-Stuttgart

**Technische Analyse, Architekturkonzept und Handlungsempfehlungen im Projekt DRS KI:W.E.G.**

**Version:** 0.1.0 – Diskussionsentwurf  
**Stand:** 19. November 2026  
**Status:** Technisches Konzeptpapier, keine Architekturfreigabe  
**Kontext:** DRS KI:W.E.G. – Werte. Erproben. Gestalten.

---

## Abstract

Die Diözese Rottenburg-Stuttgart (DRS) verfügt über unterschiedliche digitale Wissensbestände und Fachsysteme, deren Informationen für KI-gestützte Anwendungen nutzbar gemacht werden können. Im Rahmen von DRS KI:W.E.G. entstehen auf Basis der bestehenden DRS-KI-Plattform verschiedene fachliche KI-Anwendungen.

Eine wesentliche Herausforderung besteht darin, diese Anwendungen mit vorhandenen Informationsquellen zu verbinden, ohne für jedes Teilprojekt eigene, dauerhaft zu wartende Integrationen zu entwickeln.

Das Model Context Protocol (MCP) bietet einen standardisierten Ansatz, um KI-Anwendungen den kontrollierten Zugriff auf externe Werkzeuge, Datenquellen und Dienste zu ermöglichen. Für eine Organisation mit zahlreichen Fachabteilungen und unterschiedlichen Berechtigungskontexten eröffnet MCP die Möglichkeit einer gemeinsamen, wiederverwendbaren Integrationsarchitektur.

Das vorliegende Paper untersucht die Eignung von MCP für die DRS. Grundlage sind eine statische Codeanalyse vorhandener DRS:KI-Werkzeuge, die technische MCP-Spezifikation sowie die dokumentierten Integrationsmöglichkeiten von OpenWebUI.

Die Analyse kommt zu dem Ergebnis, dass eine zentral verwaltete, fachlich gegliederte MCP-Infrastruktur ein aussichtsreiches Zielbild darstellt. Die vorhandenen Werkzeuge zeigen, dass bereits erste MCP-basierte Integrationen existieren. Für eine diözesanweite Nutzung sind jedoch insbesondere die Berechtigungsarchitektur, die Standardisierung der Schnittstellen, die Betriebsverantwortung und die Protokollkompatibilität zu untersuchen.

Empfohlen wird eine begrenzte technische Machbarkeitsstudie mit exemplarischem Integrationsnachweis. Ziel ist nicht der Aufbau einer vollständigen Integrationsplattform innerhalb von DRS KI:W.E.G., sondern eine belastbare Architekturentscheidung für deren mögliche Weiterentwicklung.

**Schlüsselbegriffe:** Model Context Protocol, MCP, OpenWebUI, Systemintegration, Wissensmanagement, KI-Architektur, RAG, Identity and Access Management, Diözese Rottenburg-Stuttgart.

---

## 1. Problemstellung und Zielsetzung

### 1.1 Ausgangssituation

Die Diözese Rottenburg-Stuttgart setzt mit DRS-KI eine auf OpenWebUI basierende Plattform für den Einsatz generativer KI ein. Im Projekt DRS KI:W.E.G. werden unterschiedliche fachliche Anwendungen entwickelt beziehungsweise erprobt.

Dazu gehören unter anderem KI-Assistenten für die Unterstützung fachlicher Wissensarbeit. Mit THEOAgent liegt außerdem ein theologischer KI-Assistent als Entwicklungsprototyp vor.

Die Qualität und der praktische Nutzen solcher Anwendungen hängen wesentlich davon ab, in welchem Umfang sie auf aktuelle, relevante und berechtigt zugängliche Informationen zurückgreifen können.

In einer großen kirchlichen Organisation verteilen sich solche Informationen auf unterschiedliche Systeme und Verantwortungsbereiche. Dazu können beispielsweise Dokumentenmanagementsysteme, Wikis, Content-Management-Systeme, Fachanwendungen und strukturierte Datenbestände gehören.

Die hier genannten Systemkategorien sind mögliche Integrationsziele. Welche konkreten Systeme und Schnittstellen in der DRS zur Verfügung stehen, ist im Rahmen einer Bestandsaufnahme festzustellen.

### 1.2 Zentrales Problem

Werden externe Wissensquellen für jeden KI-Assistenten separat integriert, können mehrere Nachteile entstehen:

- Wiederholte Entwicklung ähnlicher Schnittstellen
- Unterschiedliche Implementierungen von Zugriffs- und Sicherheitsmechanismen
- Redundante Pflege von Verbindungen zu denselben Fachsystemen
- Hohe Abhängigkeit von einzelnen Entwicklern oder Anwendungen
- Uneinheitliche Qualität und Nachvollziehbarkeit der bereitgestellten Informationen
- Zusätzlicher Aufwand bei Änderungen an Fachsystemen oder KI-Plattformen

Diese Probleme sind insbesondere dann relevant, wenn die Zahl der KI-Anwendungen und der eingebundenen Fachsysteme wächst.

### 1.3 Zielsetzung

Ziel ist die Untersuchung einer Integrationsarchitektur, die bestehende Wissensbestände und Fachsysteme standardisiert, sicher und wiederverwendbar für unterschiedliche KI-Anwendungen erschließt.

Dabei sind folgende Fragestellungen zu beantworten:

1. Inwieweit eignet sich MCP als gemeinsamer Integrationsstandard für die DRS?
2. Welche vorhandenen Werkzeuge und Integrationen können wiederverwendet werden?
3. Welche Architektur ermöglicht eine fachlich angemessene Trennung von Systemen und Berechtigungen?
4. Welche Anforderungen ergeben sich an Sicherheit, Betrieb und Wartbarkeit?
5. Welche technische Machbarkeitsstudie ermöglicht eine belastbare Entscheidung mit vertretbarem Aufwand?

Die Untersuchung umfasst zunächst lesende Zugriffe auf vorhandene Informationsquellen. Schreibende oder transaktionale Zugriffe auf Fachsysteme werden als mögliche spätere Erweiterung betrachtet.

## 2. Technologische Grundlagen

### 2.1 Das Model Context Protocol

Das Model Context Protocol ist ein offener Standard zur Verbindung von KI-Anwendungen mit externen Funktionen und Informationsquellen.

Die Architektur unterscheidet im Wesentlichen zwischen MCP-Hosts, MCP-Clients und MCP-Servern.

Ein MCP-Host ist eine Anwendung, die KI-Funktionalität bereitstellt. Über MCP-Clients kann der Host mit MCP-Servern kommunizieren. Ein MCP-Server stellt definierte Fähigkeiten bereit.

Das Protokoll kennt insbesondere:

- **Tools:** Aufrufbare Funktionen, etwa zur Suche oder zur Abfrage eines Fachsystems.
- **Resources:** Strukturierte Bereitstellung von Informationen, die von einem Client gelesen werden können.
- **Prompts:** Wiederverwendbare, serverseitig bereitgestellte Promptvorlagen.

Für die Integration diözesaner Fachsysteme sind vor allem Tools und Resources relevant.

MCP stellt keine eigene Wissensdatenbank dar. Auch ersetzt es nicht die APIs, Datenbanken oder Berechtigungssysteme der angebundenen Anwendungen. Vielmehr bildet es eine standardisierte Schnittstelle zwischen KI-Anwendungen und diesen Systemen.

### 2.2 Abgrenzung von REST-APIs, MCP und RAG

Die drei Konzepte erfüllen unterschiedliche Aufgaben.

| Technologie | Primäre Funktion |
|---|---|
| REST-API | Programmgesteuerter Zugriff auf Funktionen und Daten eines Systems |
| MCP | Standardisierte Bereitstellung von Werkzeugen und Ressourcen für KI-Anwendungen |
| RAG | Erweiterung der KI-Antwortgenerierung um abgerufene externe Informationen |

MCP kann vorhandene REST-APIs kapseln. Ein MCP-Server kann beispielsweise eine Suchfunktion bereitstellen, die intern mehrere API-Aufrufe an ein Dokumentenmanagementsystem ausführt.

RAG kann wiederum über MCP-Werkzeuge realisiert werden. Die Verwendung von MCP setzt jedoch kein RAG-System voraus.

Für die DRS ergibt sich daraus ein wichtiger Grundsatz: Bestehende Fachsysteme und APIs sollen grundsätzlich erhalten bleiben. MCP kann ergänzend eine einheitliche Zugangsschicht für KI-Anwendungen bereitstellen.

### 2.3 MCP-Unterstützung in OpenWebUI

OpenWebUI unterstützt native MCP-Anbindungen über Streamable HTTP. Die aktuelle OpenWebUI-Dokumentation beschreibt die Konfiguration externer MCP-Server und entsprechende Autorisierungsverfahren.

Die Einrichtung solcher Serververbindungen ist administrativ privilegiert.

Daraus folgt eine klare Einschränkung für DRS KI:W.E.G.: Aus der grundsätzlichen Unterstützung von MCP in OpenWebUI kann nicht geschlossen werden, dass sämtliche Integrationsfunktionen auch im konkreten DRS:KI-Testsystem aktiviert oder für Entwickler zugänglich sind.

Die tatsächlichen Möglichkeiten der vorhandenen DRS:KI-Installation müssen gesondert festgestellt werden.

### 2.4 Protokollentwicklung und Kompatibilität

Die aktuelle MCP-Spezifikation trägt den Versionsstand vom 28. Juli 2026.

Gegenüber älteren Fassungen wurden unter anderem der HTTP-Transport und das Sitzungsmodell verändert. Die aktuelle Spezifikation verwendet ein zustandsloses Kommunikationsmodell und verzichtet auf die zuvor eingesetzten protokollseitigen Sitzungskennungen.

Das ist für die DRS relevant, weil bestehende MCP-Adapter noch ältere Protokollfassungen implementieren können.

Eine langfristige Integrationsarchitektur benötigt deshalb eine definierte Strategie für Protokollversionen, Kompatibilität und Migration.

## 3. Analyse vorhandener DRS:KI-Werkzeuge

### 3.1 Untersuchungsgrundlage und Methodik

Untersucht wurden folgende Werkzeugimplementierungen:

| Werkzeug | Version | Zweck |
|---|---|---|
| Simple MediaWiki MCP Tool with Citations | 1.5.0 | Suche und Abruf von MediaWiki-Inhalten |
| Outline Document Tools | 0.1.0 | Analyse und Suche in Dokumenten und Outline-Anhängen |
| TYPO3 Document Tools | 0.3.2 | Verarbeitung von TYPO3-Dateireferenzen |

Die Untersuchung umfasst den vorliegenden Python-Quellcode, dokumentierte Schnittstellen, Datenflüsse und erkennbare technische Einschränkungen.

Für MediaWiki und Outline wurde zusätzlich die Python-Syntax erfolgreich geprüft.

**Nicht Bestandteil der Untersuchung** waren vollständige Integrationstests im DRS:KI-Zielsystem, Lasttests, Penetrationstests oder eine unabhängige Prüfung der jeweiligen Backend-Systeme.

Die folgenden Aussagen sind entsprechend als statische Befunde zu verstehen.

### 3.2 MediaWiki MCP Tool

Das MediaWiki-Werkzeug ist ein OpenWebUI-Adapter, der einen externen MCP-Server anspricht.

Der Code definiert standardmäßig folgenden Endpunkt:

`http://mcp_mediawiki:8080/mcp`

Das Werkzeug baut zunächst eine MCP-Verbindung auf und führt anschließend zwei wesentliche Operationen aus:

1. `search-page` zur Suche geeigneter Wiki-Seiten
2. `get-page` zum Abruf ihrer Inhalte

Die Implementierung erlaubt mehrere Suchanfragen und begrenzt die Ergebnisanzahl sowie den Umfang zurückgegebener Texte.

**Positiv zu bewerten sind:**

Die Trennung zwischen Suche und Seitenabruf, die Bereitstellung von Titel und URL, die Integration von Quellenereignissen in OpenWebUI sowie die Möglichkeit, einen vorhandenen MCP-Server über einen vergleichsweise schlanken Adapter zu verwenden.

**Technische Einschränkungen:**

Erstens ersetzt das Werkzeug fehlende Originalseiteninhalte gegebenenfalls durch Such-Snippets oder Rohdaten des Suchergebnisses. Damit ist die Herkunft des zurückgegebenen Textes nicht in allen Fällen ausreichend klar gekennzeichnet.

Zweitens werden längere Seiten gekürzt, ohne dass die Kürzung eindeutig als eigener Evidenzstatus ausgewiesen wird.

Drittens verwendet der Code die MCP-Protokollversion `2024-11-05` und verlangt einen `Mcp-Session-Id`-Header. Dies entspricht nicht dem aktuellen zustandslosen MCP-Transportmodell.

Viertens werden im vorliegenden Adapter keine ausdrücklichen Autorisierungsmechanismen für unterschiedliche Nutzeridentitäten implementiert. Ob solche Mechanismen anderweitig bereitgestellt werden, lässt sich aus dem Adaptercode nicht beurteilen.

**Bewertung:** Der MediaWiki-Adapter bestätigt, dass MCP-basierte Integration innerhalb der DRS:KI-Werkzeuglandschaft vorgesehen ist. Er eignet sich als technischer Referenzfall, nicht jedoch ohne weitere Prüfung als Muster einer produktionsreifen, organisationsweiten MCP-Integration.

### 3.3 Outline Document Tools

Das Outline-Werkzeug verarbeitet Dokumente und Anhänge, deren URLs aus einer vorgelagerten Wissensabfrage stammen können.

Es unterstützt PDF-, DOCX-, XLSX- und textbasierte Dateien.

Zu den bereitgestellten Funktionen gehören Dokumentanalyse, Volltextsuche innerhalb eines einzelnen Dokuments, Ausgabe von Metadaten und Verarbeitung von Anhängen aus Outline-Artikeln.

Der Adapter stellt keinen eigenen MCP-Server dar. Er kann jedoch Inhalte weiterverarbeiten, die zuvor über eine separate Outline-MCP-Anbindung bereitgestellt wurden.

Die Implementierung verwendet eine Host-Allowlist und begrenzt Downloadgrößen sowie extrahierte Textmengen.

Die vorhandenen Extraktionsfunktionen stellen einen grundsätzlich wiederverwendbaren technischen Baustein dar.

Zu den Einschränkungen gehören fehlende OCR-Unterstützung, mögliche Abweichungen zwischen PDF-Seitenzählung und gedruckten Seitenzahlen sowie die Notwendigkeit zusätzlicher Maßnahmen gegen bestimmte netzwerkbezogene Angriffe.

**Bewertung:** Outline zeigt, dass Dokumentenextraktion und MCP-basierte Fachsystemanbindung unterschiedliche Aufgaben sind. Eine zukünftige Architektur sollte diese Funktionen möglichst getrennt und wiederverwendbar behandeln.

### 3.4 TYPO3 Document Tools

Das TYPO3-Werkzeug verarbeitet JSON-Datensätze, die insbesondere Dateireferenzen und Download-URLs enthalten.

Laut Schnittstellenbeschreibung stammen diese Informationen aus einem vorgelagerten Aufruf von `vzorgaoauth_ReadTable`.

Das Werkzeug selbst führt keine MCP-Kommunikation aus, sondern übernimmt die Dokumentenverarbeitung nach dem externen Datenabruf.

Die Extraktionsverfahren entsprechen weitgehend denen des Outline-Werkzeugs.

In der vorliegenden Implementierung bleiben der Parameter `max_hits_per_file` und die eigentliche Filterfunktion von `query` ungenutzt. Zudem wird das vorgesehene Gesamtbudget für die Textausgabe nicht wirksam über alle verarbeiteten Dateien hinweg begrenzt.

**Bewertung:** Der TYPO3-Adapter bestätigt den Nutzen vorhandener Fachsystem-Schnittstellen, zeigt aber zugleich die Grenzen individuell entwickelter Werkzeugimplementierungen.

### 3.5 Zusammenfassende Bewertung

Die drei Werkzeuge verdeutlichen, dass die DRS:KI-Werkzeuglandschaft bereits mehrere Integrationsmuster verwendet.

| Integrationsmuster | Vorhandener Referenzfall | Erkenntnis |
|---|---|---|
| MCP-Client zu Fachserver | MediaWiki | Standardisierte Werkzeugkommunikation grundsätzlich angelegt |
| Dokumentverarbeitung nach vorgelagerter Wissensabfrage | Outline | Dokumentenextraktion kann unabhängig von der Suchschnittstelle erfolgen |
| API-/MCP-Datenübergabe an Spezialadapter | TYPO3 | Fachsystemzugriff und Inhaltsaufbereitung sind bereits getrennt |

Es bestehen somit konkrete Anknüpfungspunkte für eine gemeinsame Integrationsstrategie.

Gleichzeitig ist nicht nachgewiesen, ob bereits eine übergreifende Verwaltung von MCP-Servern, Berechtigungen und Werkzeugversionen existiert.

## 4. Anforderungen an eine diözesane Integrationsarchitektur

### 4.1 Organisatorische Wiederverwendbarkeit

Eine geeignete Integrationsarchitektur muss Wissensquellen für mehrere Anwendungen zugänglich machen können.

Ein einmal angebundenes Fachsystem soll nicht für jeden neuen Assistenten erneut integriert werden müssen.

Dabei ist zwischen der gemeinsamen technischen Bereitstellung einer Schnittstelle und der individuellen Berechtigung zur Nutzung ihrer Daten zu unterscheiden.

### 4.2 Identitäts- und Berechtigungsmanagement

Die Diözese verfügt über organisatorisch unterschiedliche Verantwortungsbereiche. Die Integrationsarchitektur muss deshalb die jeweiligen Berechtigungsgrenzen berücksichtigen.

Insbesondere darf die Berechtigung eines KI-Assistenten zum Aufruf eines Werkzeugs nicht automatisch den Zugriff auf sämtliche Daten des angebundenen Fachsystems ermöglichen.

Zu untersuchen sind insbesondere:

- Zuordnung von Nutzeridentitäten zu Werkzeugaufrufen
- Durchsetzung fachsystemspezifischer Zugriffsrechte
- Technische Dienstidentitäten und deren Berechtigungsumfang
- Umgang mit Zugriffstokens
- Nachvollziehbarkeit autorisierter und abgewiesener Zugriffe
- Trennung öffentlich zugänglicher und interner Informationsbestände

Die Berechtigungsprüfung darf nicht allein dem Sprachmodell oder dessen Systemprompt überlassen werden.

### 4.3 Sicherheit der Werkzeugaufrufe

MCP erweitert die Handlungsmöglichkeiten einer KI-Anwendung. Daraus ergeben sich zusätzliche Sicherheitsanforderungen.

Besonders relevant sind unzulässige Zugriffe auf interne Netzwerkressourcen, Prompt Injection durch externe Inhalte, missbräuchliche Werkzeugaufrufe, unzureichende Eingabevalidierung und die unbeabsichtigte Weitergabe vertraulicher Informationen.

Die Sicherheitsarchitektur sollte deshalb auf mehreren Ebenen wirken:

**Netzwerk:** Erreichbare Systeme und Kommunikationswege müssen begrenzt werden.

**Werkzeug:** Parameter, Zielressourcen und zulässige Operationen müssen geprüft werden.

**Identität:** Jeder Zugriff benötigt eine angemessene Berechtigungsgrundlage.

**Daten:** Die fachliche Vertraulichkeit und der Schutz sensibler Inhalte müssen auch nach der Übergabe an KI-Anwendungen berücksichtigt werden.

**Protokollierung:** Sicherheitsrelevante Werkzeugaufrufe müssen nachvollziehbar sein, ohne unnötig sensible Inhalte zu speichern.

Die MCP-Spezifikation enthält entsprechende Autorisierungsmechanismen. Ihre bloße Verwendung garantiert allerdings noch keine sichere Implementierung.

### 4.4 Quellenqualität und Nachvollziehbarkeit

Für wissensbasierte Anwendungen genügt es nicht, einen Text technisch erfolgreich abzurufen.

Die Architektur sollte nach Möglichkeit strukturierte Quelleninformationen liefern:

- Identität und Herkunft des Quelldokuments
- Dokumenttitel und gegebenenfalls Versionsstand
- Exakte Fundstelle
- Tatsächlich abgerufener Textbereich
- Kennzeichnung unvollständiger Auszüge
- Unterscheidung von Suchtreffer, Auszug und Originaltext
- Fehler- und Zugriffstatus

Diese Anforderungen sind insbesondere für Anwendungen mit theologischen, rechtlichen oder verwaltungsbezogenen Aussagen relevant.

Die fachliche Bewertung einer Quelle bleibt davon unabhängig. Ein korrekt funktionierender MCP-Server beweist nicht, dass eine aus der Quelle abgeleitete Aussage inhaltlich richtig ist.

### 4.5 Betriebsfähigkeit

Für einen dauerhaften Betrieb müssen Verantwortlichkeiten für Konfiguration, Aktualisierung, Überwachung und Fehlerbehebung geklärt werden.

Dazu gehören insbesondere:

- Zuständigkeit für einzelne MCP-Dienste
- Verwaltung von Zugangsdaten
- Versions- und Kompatibilitätsmanagement
- Monitoring und Fehlerprotokollierung
- Verfügbarkeit und Wiederherstellbarkeit
- Änderungen an angebundenen Fachsystemen
- Dokumentation technischer Schnittstellen

Ein MCP-Server schafft zusätzlichen Betriebsaufwand. Dieser ist nur gerechtfertigt, wenn er durch Wiederverwendung, Standardisierung oder bessere Kontrollierbarkeit einen entsprechenden Nutzen erzeugt.

## 5. Architekturvarianten

### 5.1 Variante A: Individuelle API-Anbindungen

Jeder KI-Assistent greift über eigene Werkzeuge unmittelbar auf benötigte Fachsysteme zu.

**Vorteile:** Geringer Anfangsaufwand bei wenigen Anwendungen, direkte Nutzung vorhandener APIs, keine zusätzliche MCP-Infrastruktur notwendig.

**Nachteile:** Mögliche Doppelentwicklungen, uneinheitliche Berechtigungs- und Fehlerbehandlung, steigender Wartungsaufwand bei vielen Anwendungen.

Diese Variante ist für begrenzte Einzelanwendungen geeignet, bietet aber nur eingeschränkte Vorteile für eine organisationsweite Integrationsstrategie.

### 5.2 Variante B: Ein zentraler MCP-Server

Ein gemeinsamer MCP-Server stellt Zugriffe auf verschiedene diözesane Fachsysteme bereit.

**Vorteile:** Einheitlicher technischer Zugang, zentrale Verwaltung, geringe Anforderungen an die Konfiguration einzelner KI-Anwendungen.

**Nachteile:** Gefahr einer zunehmend komplexen Integrationskomponente, enge Kopplung unterschiedlicher Fachsysteme, mögliche Konzentration von Berechtigungen und Betriebsrisiken.

Ein zentraler MCP-Server kann für wenige eng verwandte Systeme sinnvoll sein. Für eine umfassende diözesane Integration besteht jedoch das Risiko eines schwer wartbaren Integrationsmonolithen.

### 5.3 Variante C: Föderierte MCP-Dienste mit gemeinsamer Verwaltung

Fachlich zusammengehörige Systeme werden über geeignete MCP-Dienste angebunden.

Die Dienste werden nach gemeinsamen technischen, organisatorischen und sicherheitsbezogenen Vorgaben betrieben.

Eine übergreifende Verwaltung sorgt für Transparenz über verfügbare Werkzeuge, Versionen, Zuständigkeiten und Berechtigungen.

Dafür kann gegebenenfalls ein MCP-Gateway eingesetzt werden. Ein solches Gateway ist jedoch kein zwingender Bestandteil der Architektur.

**Vorteile:** Fachliche Trennung, bessere Wiederverwendbarkeit, flexiblere Erweiterung, klarere Betriebszuständigkeiten, geringere direkte Kopplung an einzelne KI-Anwendungen.

**Nachteile:** Zusätzlicher Abstimmungsbedarf, Anforderungen an eine gemeinsame Verwaltung und mögliche Komplexität bei organisationsübergreifender Identitätsübertragung.

**Bewertung:** Diese Variante erscheint für die DRS als langfristiges Zielbild besonders geeignet. Ihre tatsächliche Wirtschaftlichkeit und technische Machbarkeit müssen jedoch anhand der vorhandenen Systemlandschaft geprüft werden.

### 5.4 Architekturvergleich

| Bewertungskriterium | A: Einzel-APIs | B: Zentraler MCP-Server | C: Föderierte MCP-Dienste |
|---|---|---|---|
| Einfachheit beim ersten Anwendungsfall | Hoch | Mittel | Mittel |
| Wiederverwendung über viele Anwendungen | Begrenzt | Hoch | Hoch |
| Trennung fachlicher Zuständigkeiten | Abhängig von Einzelimplementierungen | Erschwert | Gut abbildbar |
| Erweiterbarkeit | Mit wachsendem Integrationsaufwand | Gefahr zentraler Komplexität | Modular |
| Zentraler Betriebsaufwand | Geringer Einstieg, verteilt | Konzentriert | Koordiniert |
| Plattformunabhängigkeit | Abhängig von Implementierung | Grundsätzlich möglich | Grundsätzlich möglich |

Die Bewertungen sind qualitative Architekturabschätzungen, keine empirisch gemessenen Ergebnisse.

**Vorläufige Präferenz:** Variante C als strategisches Zielbild, kombiniert mit der Wiederverwendung vorhandener direkter APIs und Werkzeuge, wo dies einfacher und ausreichend ist.

## 6. Vorgeschlagene Zielarchitektur

### 6.1 Architekturprinzip

Die vorgeschlagene Architektur trennt vier Ebenen:

**Ebene 1 – KI-Anwendungen:** THEOAgent sowie weitere Fachassistenten und zukünftige KI-Anwendungen.

**Ebene 2 – KI-Plattform:** DRS-KI als bestehende OpenWebUI-basierte Laufzeitumgebung mit Werkzeugsteuerung und Modellzugriff.

**Ebene 3 – Integrationsdienste:** Vorhandene und bei Bedarf ergänzte MCP-Dienste beziehungsweise API-Adapter, die fachliche Funktionen standardisiert bereitstellen.

**Ebene 4 – Fachsysteme:** Bestehende Dokumenten-, Wissens- und Anwendungssysteme der Diözese.

Querschnittlich wirken Identitätsmanagement, Berechtigungssteuerung, Protokollierung und Betriebsüberwachung.

### 6.2 Fachlich gegliederte Integrationsdienste

Die Aufteilung der MCP-Dienste sollte sich an vorhandenen Systemgrenzen, technischen Verantwortlichkeiten und Berechtigungsdomänen orientieren.

Denkbar sind Integrationen für Dokumenten- und Wissenssysteme, öffentliche diözesane Informationsquellen oder spezifische interne Fachsysteme.

Eine eigene MCP-Instanz für jede Abteilung oder Kirchengemeinde ist dafür nicht erforderlich. Entscheidend ist die sinnvolle Trennung fachlich und technisch unterschiedlicher Zugriffskontexte.

### 6.3 Wiederverwendbare technische Funktionen

Mehrere Integrationen benötigen ähnliche Grundfunktionen.

Dazu zählen Dokumentenabruf, Text- und Metadatenextraktion, Ergebnisbegrenzung, Fehlerkennzeichnung und Quellenreferenzierung.

Diese Funktionen sollten soweit möglich durch bestehende Komponenten bereitgestellt werden.

Gerade die untersuchten Outline- und TYPO3-Werkzeuge zeigen erhebliches Potenzial für eine gemeinsame Dokumentenverarbeitung.

Eine umfassende Neuentwicklung solcher Funktionen sollte vermieden werden.

### 6.4 Plattformunabhängigkeit

Ein wesentliches Architekturziel ist die Entkopplung fachlicher Integrationen von der konkreten KI-Oberfläche.

Fachsystemzugriffe sollten nicht ausschließlich als proprietäre Python-Werkzeuge einer bestimmten OpenWebUI-Installation realisiert werden, wenn sie von mehreren KI-Anwendungen benötigt werden.

MCP könnte hierfür eine geeignete standardisierte Schnittstelle bilden.

Die tatsächliche Austauschbarkeit ist jedoch nur gegeben, wenn Protokollversionen, Authentifizierung, Werkzeugverträge und Clientunterstützung kompatibel sind.

## 7. Technische Machbarkeitsstudie

### 7.1 Ziel

Innerhalb von DRS KI:W.E.G. soll ein begrenzter Proof of Concept (PoC) durchgeführt werden.

Ziel ist der Nachweis, dass eine vorhandene diözesane Wissensquelle über MCP zuverlässig, berechtigungsgerecht und nachvollziehbar von einer KI-Anwendung genutzt werden kann.

Die Untersuchung soll zugleich zeigen, welche Teile der Integrationslösung auf weitere Anwendungen übertragbar sind.

### 7.2 Untersuchungsgegenstand

Als bevorzugter Ausgangspunkt bietet sich die bereits dokumentierte MediaWiki-MCP-Anbindung an.

Sie ist besonders geeignet, weil der vorliegende Adapter eine direkte MCP-Kommunikation implementiert und damit grundlegende Architekturfragen untersucht werden können.

Voraussetzung ist, dass der entsprechende Server und ein geeigneter, freigegebener Testdatenbestand in DRS:KI DEV tatsächlich verfügbar sind.

Alternativ kann eine andere bereits vorhandene MCP-Integration eingesetzt werden.

### 7.3 Durchführung

**Schritt 1: Bestandsaufnahme**

Erfassung der tatsächlich vorhandenen MCP-Server, ihrer Protokollversionen, Transportverfahren, Konfigurationsmöglichkeiten und Betriebszuständigkeiten.

**Schritt 2: Verbindungsprüfung**

Nachweis, dass die vorhandene DRS:KI-Installation den ausgewählten MCP-Dienst technisch erreichen und dessen Werkzeuge aufrufen kann.

**Schritt 3: Fachlicher Abruf**

Exemplarische Suche und Lektüre eines freigegebenen Dokuments einschließlich Titel, Quellenreferenz und Textauszug.

**Schritt 4: Berechtigungsprüfung**

Prüfung mindestens eines erlaubten und eines nicht erlaubten Zugriffs mit geeigneten Testidentitäten beziehungsweise kontrollierten Testberechtigungen.

**Schritt 5: Fehler- und Evidenzprüfung**

Untersuchung des Verhaltens bei fehlenden Dokumenten, nicht erreichbaren Diensten, gekürzten Inhalten und unzureichenden Berechtigungen.

**Schritt 6: Wiederverwendungsnachweis**

Nutzung derselben Integrationsfunktion durch zwei unterschiedliche fachliche Anwendungskontexte, soweit die vorhandene Umgebung dies unterstützt.

### 7.4 Erfolgskriterien

Der PoC gilt als technisch erfolgreich, wenn folgende Punkte nachgewiesen sind:

1. Der MCP-Dienst kann aus DRS:KI DEV tatsächlich aufgerufen werden.
2. Ein relevantes Dokument kann zuverlässig abgerufen werden.
3. Herkunft und Abrufstatus der Informationen sind nachvollziehbar.
4. Nicht autorisierte Zugriffe werden wirksam verhindert.
5. Die Schnittstelle ist ohne individuelle Neuentwicklung für mindestens einen weiteren Anwendungskontext wiederverwendbar.
6. Die Betriebs- und Integrationsvoraussetzungen sind dokumentiert.

Eine erfolgreiche Kommunikation allein genügt nicht als Nachweis für die Erfüllung aller Kriterien.

### 7.5 Abgrenzung

Nicht Gegenstand dieses PoC sind:

- Der Aufbau einer vollständigen diözesanen MCP-Serverlandschaft
- Die Migration sämtlicher vorhandener Wissenssysteme
- Die Entwicklung eines neuen übergreifenden Identitätsmanagements
- Die flächendeckende Produktivsetzung von MCP-Diensten
- Schreibende Eingriffe in produktive Fachsysteme
- Die vollständige fachliche Abnahme darauf aufbauender KI-Anwendungen

## 8. Risiken und offene Architekturentscheidungen

### 8.1 Identitäts- und Rechteübertragung

Die wichtigste offene Frage betrifft die zuverlässige Durchsetzung bestehender Zugriffsrechte über mehrere Systemgrenzen hinweg.

Ohne eine geeignete Berechtigungsarchitektur könnte eine standardisierte Schnittstelle unbeabsichtigt den Zugriff auf Informationen erleichtern, die nur bestimmten Nutzergruppen zur Verfügung stehen dürfen.

### 8.2 Protokollkompatibilität

Die vorhandene MediaWiki-Implementierung verwendet eine ältere MCP-Protokollfassung.

Die Kompatibilität mit aktuellen MCP-Clients und einer zukünftigen Infrastruktur ist nicht nachgewiesen.

Vor einer Migration müssen Server, Client und Transportverfahren gemeinsam betrachtet werden.

### 8.3 Integration in die bestehende DRS-KI

Die aktuelle OpenWebUI-Dokumentation beschreibt Möglichkeiten zur nativen MCP-Anbindung.

Welche davon in DRS:KI DEV tatsächlich bereitstehen, ist noch zu prüfen.

Insbesondere dürfen Developerrechte nicht mit administrativen Rechten zur Registrierung und zum Betrieb zusätzlicher MCP-Dienste gleichgesetzt werden.

### 8.4 Qualität und Sicherheit der Datenübergabe

Externe Dokumente und Fachsystemantworten können fehlerhafte, unvollständige oder manipulative Inhalte enthalten.

MCP garantiert nicht die fachliche Richtigkeit solcher Inhalte.

Deshalb muss die Quellenqualität unabhängig vom technischen Transport bewertet werden.

Für anspruchsvolle Fachanwendungen wie THEOAgent bleiben die bereits definierten Anforderungen an Originallektüre, Quellenangaben und Evidenzprüfung maßgeblich.

### 8.5 Langfristiger Betrieb

Ein MCP-Server benötigt definierte Verantwortlichkeiten und dauerhaft verfügbare Betriebsressourcen.

Eine Integration ist nur dann nachhaltig, wenn Pflege und Weiterentwicklung organisatorisch geklärt sind.

Für eine mögliche diözesane Infrastruktur sind deshalb DRS-IT, KRZ und die verantwortlichen Fachsystembetreiber einzubeziehen.

## 9. Handlungsempfehlungen

### 9.1 MCP strategisch als Integrationsstandard untersuchen

MCP sollte nicht auf ein technisches Detail einzelner KI-Assistenten reduziert werden.

Für die DRS besitzt es Potenzial als standardisierte Verbindungsschicht zwischen bestehenden Fachsystemen und unterschiedlichen KI-Anwendungen.

### 9.2 Bestehende Integrationen konsequent wiederverwenden

Die vorhandenen DRS:KI-Werkzeuge und MCP-Dienste sind Ausgangspunkt der weiteren Entwicklung.

Neue Schnittstellen sollen nur dann entstehen, wenn die vorhandenen technischen Möglichkeiten nicht ausreichen oder eine gemeinsame Lösung einen nachweisbaren Mehrwert bietet.

### 9.3 Föderierte Architektur als Zielhypothese verwenden

Eine fachlich gegliederte MCP-Infrastruktur mit gemeinsamer Verwaltung erscheint langfristig zweckmäßig.

Eine verbindliche Architekturentscheidung darf jedoch erst nach einer Bestandsaufnahme der tatsächlichen Systemlandschaft und ihrer Betriebsanforderungen erfolgen.

### 9.4 Sicherheit und Berechtigungen früh überprüfen

Berechtigungsdurchsetzung ist keine nachgelagerte Optimierung.

Sie ist eine zentrale Voraussetzung für den Einsatz von MCP in einer Organisation mit unterschiedlichen fachlichen Zuständigkeiten und Vertraulichkeitsanforderungen.

### 9.5 Mit einem begrenzten PoC beginnen

Als erster Untersuchungsgegenstand wird eine vorhandene MCP-Anbindung empfohlen, vorzugsweise MediaWiki.

Die technische Untersuchung soll möglichst vorhandene Komponenten nutzen und sich auf einen reproduzierbaren Integrationsnachweis konzentrieren.

### 9.6 Ergebnisse organisationsweit nutzbar machen

Der Mehrwert für DRS KI:W.E.G. liegt nicht allein im Erfolg eines einzelnen Werkzeugs.

Entscheidend ist eine wiederverwendbare Erkenntnis darüber, welche Integrationsarchitektur für weitere Fachabteilungen geeignet ist und unter welchen Voraussetzungen sie betrieben werden kann.

## 10. Fazit

Die Integration bestehender Wissensquellen und Fachsysteme ist eine zentrale technische Voraussetzung für den nachhaltigen Einsatz fachlicher KI-Anwendungen in der Diözese Rottenburg-Stuttgart.

Die bisher untersuchten DRS:KI-Werkzeuge zeigen, dass bereits unterschiedliche Zugriffs- und Integrationsmechanismen existieren. Insbesondere die MediaWiki-Anbindung bestätigt die praktische Relevanz von MCP innerhalb der vorhandenen Werkzeuglandschaft.

Für eine diözesanweite Perspektive ist jedoch eine über den einzelnen KI-Assistenten hinausgehende Betrachtung erforderlich.

**Die bevorzugte Architekturhypothese ist eine gemeinsam verwaltete, fachlich gegliederte MCP-Infrastruktur, die vorhandene Fachsysteme über standardisierte und kontrollierte Schnittstellen für unterschiedliche KI-Anwendungen erschließt.**

Dabei ist zwischen einem gemeinsamen Integrationsstandard und einem einzigen zentralen MCP-Server zu unterscheiden.

Die technische Architektur muss Wiederverwendbarkeit, Berechtigungssteuerung, Quellenqualität, Wartbarkeit und langfristigen Betrieb gleichermaßen berücksichtigen.

Für DRS KI:W.E.G. empfiehlt sich eine begrenzte Machbarkeitsstudie, die vorhandene MCP-Komponenten untersucht und mindestens eine wiederverwendbare Integration exemplarisch nachweist.

Das Ergebnis soll eine belastbare technische Entscheidungsgrundlage für die weitere Entwicklung der DRS-KI bilden.

Eine vollständige diözesane MCP-Infrastruktur ist dagegen als mögliche längerfristige Entwicklung und nicht als unmittelbares Lieferergebnis des Projekts zu betrachten.

---

## Literatur und technische Quellen

**[1] Model Context Protocol:** *Specification, Version 2026-07-28*.  
https://modelcontextprotocol.io/specification/2026-07-28

**[2] Model Context Protocol:** *Streamable HTTP Transport, Version 2026-07-28*.  
https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http

**[3] Model Context Protocol:** *Authorization Security Considerations, Version 2026-07-28*.  
https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations

**[4] OpenWebUI:** *Model Context Protocol (MCP) – Documentation*.  
https://docs.openwebui.com/features/extensibility/mcp/

**[5] OpenWebUI:** *Tools – Documentation*.  
https://docs.openwebui.com/features/extensibility/plugin/tools/

**[6] DRS:KI:** *Simple MediaWiki MCP Tool with Citations*, Version 1.5.0, Autor: Fedor. Bereitgestellter Python-Quellcode, statisch untersucht am 19.11.2026.

**[7] DRS:KI:** *Outline Document Tools*, Version 0.1.0, Autor: BKurschatke. Bereitgestellter Python-Quellcode, statisch untersucht am 19.11.2026.

**[8] DRS:KI:** *TYPO3 Document Tools*, Version 0.3.2, Autor: BKurschatke. Im Projekt bereitgestellter Python-Quellcode, statisch untersucht am 19.11.2026.

**[9] THEOAgent:** *Architekturvorschlag – THEOBald auf DRS:KI*, 13.11.2026. GitHub-Repository `baem-oss/THEOAgent`, Branch `drs-ki-test`.  
https://github.com/baem-oss/THEOAgent/blob/drs-ki-test/docs/drs-ki/ARCHITEKTURVORSCHLAG_2026-11-13.md

**[10] THEOAgent:** *P-02 – DRS:KI-Werkzeuge im SourceGuard-Web-PoC vergleichen*, 13.11.2026. GitHub-Repository `baem-oss/THEOAgent`, Branch `drs-ki-test`.  
https://github.com/baem-oss/THEOAgent/blob/drs-ki-test/docs/drs-ki/POC_P-02_DRS_TOOLS_VERGLEICH.md

---

*Ende des technischen Konzeptpapiers – Version 0.1.0, Diskussionsentwurf.*
