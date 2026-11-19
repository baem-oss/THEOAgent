# THEOAgent DEV – Wissenskorpus: vorläufige Bestandsaufnahme

**Stand:** 18.11.2026  
**Umgebung:** DRS:KI DEV · THEOAgent Dev  
**Branch:** `drs-ki-test`  
**Status:** PO-übermittelte Werkzeugauswertung; Teilinventar, **keine vollständige Inventarisierung und kein unabhängig geprüfter Live-Zugriff des SE**.

## 1. Wichtigste Korrektur

Die frühere Aussage im [Systemprompt v0.3.11](THEOAGENT_DEV_SYSTEMPROMPT_v0.3.11.md), in der Fachbibliothek sei ausschließlich Wolfgang Klippert verfügbar, ist nach den jüngsten DEV-Berichten **sachlich überholt**. Der historische Systemprompt bleibt als Version unverändert. Diese Notiz dokumentiert die Abweichung; eine Änderung der Live-Konfiguration ist damit nicht verbunden.

Die vom DEV-Modell mittels `list_knowledge_bases` gemeldete Sammlung **`THEOAgent - Fachbibliothek`** (ID `db2d49a6-f7fb-43ab-b4e8-4f244e1968f4`) enthält **187 Dateien**. Diese Anzahl beruht auf dem PO-übermittelten Toolbericht, nicht auf einer vom SE selbst ausgeführten DRS-Abfrage.

**Abgrenzung:** Andere Knowledge-Sammlungen (u. a. Amtsblatt und AVOKA) sind nicht Teil dieses Fachbibliotheksinventars.

## 2. Identifizierte Beispiele (unvollständiges Teilinventar)

Die folgenden Dateinamen wurden in den übermittelten DEV-Ergebnissen berichtet; Dateinamen sind kein Beweis für inhaltliche Vollständigkeit oder Geltungsstand.

**Grundkurs:**
- `GK-LB 21 Die katholische Kirche im 20.Jahrhundert - Prof. Dr. Wolfgang Weis.md`
- `GK-LB 23 Handeln aus christlicher Verantwortung - Prof. DDr. Peter Fonk.md`
- `GK-LB 20 Kirchengeschichte - Altertum, Mittelalter, Neuzeit - Prof. Dr. Manfred Eder.md`
- `GK-LB 18 Gottesdienst der Kirche - Feier des Glaubens - Prof. Dr. Winfried Haunerland.md`
- `GK-LB 19 Sakramente - Gestalten des Reiches Gottes auf Erden - Prof. Dr. Thomas Ruster.md`
- `GK-LB03_Die_Bibel_verstehen_Biblische_Hermeneutik_THEOBald.md`

**Aufbaukurs:**
- `AK-LB 21 Liturgie der Sakramente - Prof. Dr. Benedikt Kranemann .md`
- `AK-LB 18 Christliche Lebenskunst und Alltagsmoral - Prof. Dr. Thomas Weiser .md`
- `AK-LB 20 Diakonie als Wesensvollzug der Kirche - Prof. Dr. Klaus Baumann .md`
- `AK-LB 17 Verantwortung fur das Leben - Prof. Dr. Elmar Kos.md`
- `AK-LB 22 Spirituelle Aufbruche im 20. Jahrhundert - Prof. Dr. Joachim Schmiedl .md`
- `AK-LB 19 Kirchenrecht - Prof. Dr. Dr. Helmuth Pree.md`
- `AK-LB 16 Christliche Sozialethik - Prof. Dr. Marianne Heimbach-Steins .md`

**Weitere nachgewiesene Dateinamen:**
- `01_Bibel_Textverstehen.md`
- `02_3_Liturgie.md`
- `vom text zur predigt_klippert, wolfgang.pdf`
- `02_1_Erneuerte_Homiletik.md`
- `02_4_Predigt_als_Ereignis.md`
- `Gemeindepastoral_INDEX.md`
- `Gemeindepastoral_004.md`, `Gemeindepastoral_005.md`, `Gemeindepastoral_006.md`, `Gemeindepastoral_007.md`

Das vorliegende Textinventar weist **23 unterscheidbare Dateinamen** aus. THEOAgent meldete **32 eindeutig identifizierte Dateien**, aber dieser Wert lässt sich anhand der vom PO hier übermittelten Tabelle nicht vollständig nachvollziehen; er wird deshalb nicht als verifiziert übernommen. Die in der Ausgabe verkürzten Datei-IDs sind **keine vollständigen Identifikatoren**.

## 3. Werkzeuggrenzen

Laut PO-übermittelter Prüfung der tatsächlich verfügbaren Signaturen:

- `list_knowledge_bases(count, skip)`: Sammlungen, **keine Dateiliste**.
- `search_knowledge_files`: `knowledge_id`, `count`, `skip` und verpflichtender Suchparameter `query`; keine bestätigte ungefilterte Komplettliste.
- `list_knowledge`: in dieser DEV-Umgebung nicht verfügbar.
- `view_knowledge_file`: in einem vorgelegten Durchlauf für sieben exemplarische Dateien tatsächlich aufgerufen; dies stützt die Zugänglichkeit dieser Stichprobe, nicht aller 187 Dateien.

Ein ungefilterter Komplett-Export ist nach PO-Angabe in der DRS:KI-Oberfläche nicht möglich. Eine vollständige Aufzählung der 187 Dateien ist somit **nicht nachgewiesen**. Ein pauschales `*` oder Leerquery-Verhalten ist weder getestet noch bestätigt.

## 4. Konsequenz für die Qualitätssicherung

Die Fachbibliothek ist umfangreicher als bislang dokumentiert, ihr **Einfluss auf die Antworten** ist aber offen. Korpusexistenz, erfolgreiche Suche, tatsächliche Originallektüre und fachlich richtige Nutzung sind getrennte Prüfschritte.

**Empfohlener kleinster nächster Test:** Eine inhaltlich begrenzte kirchenrechtliche Frage stellen, bei der der gefundene `AK-LB 19 Kirchenrecht` sachlich einschlägig sein könnte. Den unveränderten Normalprompt verwenden, Toolspur erfassen und prüfen, ob THEOAgent (a) den Text autonom findet, (b) eine einschlägige Passage liest, (c) sie korrekt anwendet und (d) bei der Rechtslage zwischen Lehrbrief und aktuell maßgeblichen amtlichen Normen unterscheidet. Die ältere E-02-Aufgabe eignet sich als Vergleichsfall, **nicht** als kausaler A/B-Nachweis, solange keine kontrollierte Konfiguration ohne Korpus verfügbar ist.

Keine Änderungen an Prompt, Skills, Knowledge-Inhalt oder `main`; keine Freigabe und keine Erledigung von F-C1 durch diese Bestandsnotiz.
