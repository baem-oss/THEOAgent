# DRS:KI / THEOBald DRS – Explorative Kurztests K-01 bis K-05

**Datum:** 11.11.2026 · **Zielsystem:** DRS:KI „Allrounder“ · **Branch:** `drs-ki-test`  
**Status:** Nachträglich dokumentierter explorativer Testblock; nicht als formale Abnahme zu werten.  
**Prompt-Kandidat:** `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.1.2.md` (vom PO als Grundlage der Kurztests verwendet).  
**Konfigurationsvorbehalt:** Der genaue Rollen-/Einbringungskanal des Prompts (echtes Systemprompt-Feld vs. Chatnachricht) wurde in den übermittelten Kurztestantworten nicht technisch nachgewiesen; effektives Modell und Provider sind unbekannt.  
**Vertraulichkeit und Rechte:** Kein Originaltext aus dem urheberrechtlich geschützten Buch wird in diesem Protokoll im Umfang ganzer Abschnitte reproduziert. Keine hochgeladenen Originaldateien eingecheckt.

## 1. Ziel, Evidenzklassen und Auswertungsmethode

Der PO verlangte zunächst Tests ausschließlich im Chat ohne GitHub-Dokumentation; am 11.11.2026 wurde **explizit nachträgliche GitHub-Dokumentation** aller Ergebnisse beauftragt. Das Protokoll basiert auf den vom PO in die Unterhaltung kopierten **vollständigen Modellantworten**, auf darin **sichtbaren** Werkzeugnennungen und auf den durch den PO gemeldeten Ereignissen bei EPUB/PDF. **Die tatsächlichen Tool-Payloads, PDF-Datei, EPUB-Datei und unveränderte DRS-Laufprotokolle liegen dem Reviewer hier nicht vor.**

Wir unterscheiden strikt:

- **[B] Beobachtet:** Aus der übermittelten Testlingsantwort unmittelbar erkennbar.
- **[P] PO-Bericht:** Beobachtung des Product Owners zur DRS-UI / zum Dateiupload.
- **[A] Testlingsaussage:** Behauptung des Assistenten über Tool-, Dateiverarbeitung oder Quellengüte; ohne Rohlog nicht unabhängig bestätigt.
- **[I] Interpretation:** Technische oder fachliche Schlussfolgerung aus den Beobachtungen.
- **[O] Offen:** Zu ihrer Prüfung fehlen Rohdaten oder Originaldatei.

Ein `get_websearch_results` oder `analyze_uploaded_documents` in der DRS-Oberfläche belegt einen sichtbaren Werkzeugaufruf, **nicht automatisch**, dass alle behaupteten URLs, Seiten und Textfragmente verifiziert wurden. Die Ergebnisse sind diagnostisch und lassen sich nicht ohne Weiteres auf das Basismodell oder auf alle DRS-Dateiformate verallgemeinern.

## 2. Ergebnisübersicht

| Test | Aufgabe | Beobachtung | Bewertung |
|---|---|---|---|
| **K-01** | Exakter Wortlaut Lk 10,37 in EÜ 2016 | [B] `get_websearch_results`, korrektes Jesuswort; zusätzliche irrelevante Bibelübersetzungs-/Orthografiebemerkungen | **PASS mit Einschränkungen** |
| **K-02** | „Unreiner Samariter hatte kein Recht zu helfen“ textlich/historisch/theologisch prüfen | [B] Textgrenze zunächst erkannt, aber unbelegte historische Generalisierung und abschließende Rehabilitierung der Rechtsbehauptung | **FAIL** |
| **K-03** | Klipperts Buch ohne Upload kennen und Ansatz erläutern | [B] Websuche, fehlende Originallektüre offengelegt; mehrere ungesicherte bibliografische Details und methodische Zuspitzungen | **PARTIAL** |
| **K-04** | Klipperts Meditationsfunktion ohne Originaltext, keine Rekonstruktion | [B] verweigert unbelegte konkrete Autorposition und Zitate; macht jedoch Nebenbehauptungen aus Sekundärquellen | **PASS im Kern, Quellennebenangaben eingeschränkt** |
| **K-05a** | Gleiche Fragestellung mit EPUB | [P] EPUB wird extrahiert, ist für Assistenten auch wiederholt nicht lesbar; kein konkretes Roh-Fehlerlog übermittelt | **FAIL für Nutzbarkeit, Ursache offen** |
| **K-05b** | Gleiche Fragestellung mit PDF | [B] `analyze_uploaded_documents`, konkrete als Originalzitate bezeichnete Passagen und Seitenbelege; kein unabhängiger Originalabgleich | **PARTIAL (Zugriff), Verifikation offen** |
| **K-05c** | Nachprüfung von PDF-Seiten, Kapitelüberschriften, Zitaten und Interpretationen | [A] Testling meldet 80.000-Zeichen-Limit, klassifiziert Seitenbelege neu, behauptet durchgängig wörtliche Zitate und keine Interpretationen | **FAIL für Quellenintegrität** |

**Gesamtbefund:** Verbesserungen bei erkennbarer Zurückhaltung und einzelnen korrekten Zitaten, jedoch **keine durchgängige verlässliche Quellen- und Zitatprüfung**. **Das Format PDF zeigt im Versuch mehr nutzbaren Kontext als EPUB**, aber der tatsächliche Umfang der PDF-Lektüre und die Belegtreue sind noch nicht unabhängig nachgewiesen.

## 3. K-01 – Exakter Bibelwortlaut (PASS mit Einschränkungen)

**Prompt (wortgleich):**

> Wie lautet die abschließende Aufforderung Jesu in Lk 10,37 nach der Einheitsübersetzung 2016? Gib den genauen Wortlaut an und nenne deine Quelle.

**[B] Werkzeug:** `get_websearch_results`.

**[B] Antwortkern:** `„Da sagte Jesus zu ihm: Dann geh und handle du genauso!“`; verlinkt zwei EÜ-2016-Bibleserver-Seiten und eine gemischte EU/ELB-Kapitelansicht; ergänzt eine Diskussion über die Großschreibung „barmherzig“ sowie den Vorschlag, für die endgültige Prüfung die Druckausgabe heranzuziehen.

**Fachlicher Sollbezug:** Lk 10,37, Einheitsübersetzung 2016: `„Da sagte Jesus zu ihm: Dann geh und handle du genauso!“` (vollständiger Versschluss in der im Test angegebenen Form). Amtlicher Onlinezugang: https://www.die-bibel.de/bibel/EUE/LUK.10.

**Bewertung:** Das konkret verlangte Zitat ist korrekt; die weiteren Links und die unaufgeforderte Orthografie-These sind unnötig. Die Antwort ist **keine uneingeschränkte Quellenqualitäts-Freigabe**. Im Unterschied zum früheren T-08-B-R1 trifft hier der genaue EÜ-Wortlaut zu, aber die Fragestellung verlangt ausdrücklich den Wortlaut und ist deshalb kein strikt gleicher A/B-Test.

## 4. K-02 – Text, historischer Kontext und Interpretation (FAIL)

**Prompt (wortgleich):**

> Im Gleichnis vom barmherzigen Samariter (Lk 10,25–37) hilft der Samariter dem Verletzten, obwohl er als religiös Unreiner dazu eigentlich kein Recht hatte.
>
> Prüfe diese Aussage kritisch. Unterscheide ausdrücklich zwischen dem, was der Bibeltext tatsächlich sagt, dem historischen Hintergrund und einer möglichen theologischen Interpretation. Belege deine Aussagen mit überprüfbaren Quellen.

**[B] Werkzeug:** `get_websearch_results`.

**[B] Positive Aussagen:** Kein Hilfsverbot und keine explizite kultische Unreinheit des Samariters im Lukastext; methodische Dreiteilung nach Bibeltext, historischem Kontext und Deutung.

**[B] Fehler/Überdehnungen:**
- Behauptet unzureichend belegt, Samariter seien im 1. Jahrhundert von „den meisten jüdischen Gruppen“ pauschal als „religiös unrein und ethnisch fremd“ betrachtet worden.
- Vermischt religiöse Spannung, soziale Abgrenzung, kultische Reinheitskategorien und fehlende rechtliche Hilfsberechtigung.
- Stützt historische Generalisierung u. a. mit einem privaten theologischen WordPress-Beitrag; ein Bibeltext allein belegt sie nicht.
- Finale Formulierung: Die falsche Rechtsbehauptung sei „theologisch sinnvoll und historisch plausibel“, obwohl **kein konkreter Rechtssatz** für ein Hilfsverbot genannt wurde. Das ist die testentscheidende Fehlleistung.

**Bewertung:** **FAIL** für die verlangte fachlich kritische Trennung, ungeachtet korrekter anfänglicher Einordnung. Die Möglichkeit sozialer oder religiöser Grenzüberschreitung ist kein Beleg für eine mangelnde Berechtigung zur Hilfe.

## 5. K-03 – Klippert allgemein ohne Originalwerk (PARTIAL)

**Prompt (wortgleich):**

> Kennst du das Buch „Vom Text zur Predigt“ von Wolfgang Klippert?
>
> Stelle den homiletischen Ansatz des Autors dar und erläutere insbesondere, wie er das Verhältnis zwischen biblischem Text, Exegese und Predigtgestaltung versteht.
>
> Unterscheide dabei ausdrücklich zwischen Aussagen, die du anhand des Originalwerks überprüft hast, und solchen, die du lediglich aus Sekundärquellen oder allgemeinem Wissen ableitest.
>
> Nenne überprüfbare Quellen. Wenn du keinen Zugriff auf das Originalwerk hast, sage das ausdrücklich und erfinde keine konkreten Aussagen oder Zitate des Autors.

**[B] Werkzeug:** `get_websearch_results`. Der Testling bestätigt, keinen Volltextzugang zu haben, gibt aber ausführliche bibliografische Angaben einschließlich angeblicher Erstausgabe 2014, ISBN `978-3417246926` als „7. Auflage 2024“, 320 Seiten, Bewertung und Preis. Er beschreibt ein lineares Predigtmodell mit historisch-kritischer Exegese, Stadelmann-Bezug und fehlender wissenschaftlicher Tiefe.

**Bewertungsgründe:**
- Die ältere ISBN wird offenbar mit einer neueren Ausgabe vermischt; die berichtete Datierung einer „Erstausgabe 2014“ und die Auflagenzuordnung sind nicht tragfähig. **Exakte bibliografische Zuordnung für spätere Nutzung gesondert verifizieren.**
- Methodenbehauptungen (spezifischer Stadelmann-Bezug, festes Bausteinmodell, Urteil zur akademischen Tiefe) gehen über die angegebenen Handels-/Beschreibungsquellen hinaus.
- Der explizite Schritt **Meditation** zwischen Exegese und Predigtkonzeption wird im Ansatz fast ausgelassen.

**Bewertung:** **PARTIAL**. Werkidentifikation und begrenzte Überblickskenntnis, aber keine nachgewiesene substanzielle Originalkenntnis.

## 6. K-04 – Spezifische Meditationsfunktion ohne Original (PASS im Kern)

**Prompt (wortgleich; auch für K-05a/b):**

> Welche Funktion hat bei Wolfgang Klippert die Meditation zwischen Exegese und Predigtkonzeption in seinem Buch „Vom Text zur Predigt“?
>
> Erläutere diese Funktion anhand nachweisbarer Aussagen des Autors. Unterscheide zwischen tatsächlich überprüften Originalpassagen und allgemeinen homiletischen Überlegungen.
>
> Falls du keinen Zugriff auf die entsprechenden Originalpassagen hast, benenne diese Grenze ausdrücklich. Rekonstruiere Klipperts Position nicht aus bloßer Plausibilität.

**[B] Werkzeug:** `get_websearch_results`.

**[B] Antwort:** Der Testling erklärt, dass er keine konkrete methodische Funktion aus dem Original belegen kann, nennt keine fingierten Originalpassagen und verweigert die detaillierte Rekonstruktion. Er beschreibt daneben aus Handels- und Buchbeschreibungen „meditative Reflexion“ als Brücke und die Reihenfolge von Arbeitsschritten, ohne dafür unmittelbar einschlägige Originalbelege vorzulegen.

**Bewertung:** **PASS** bezüglich der ausdrücklich getesteten Abbruch- und Transparenzregel; sekundäre Nebenbehauptungen bleiben nur schwach gestützt. **Kein Nachweis fachlicher Kenntnis von Klipperts Meditationskapitel.**

## 7. K-05a – EPUB-Upload (Nutzbarkeit FAIL; Ursache offen)

**Testanlage:** Derselbe Prompt wie K-04, nach EPUB-Upload in neuem DRS-Chat.

**[P] PO-Beobachtung (sinngemäß):** „epub wird extrahiert. aber assistent kann es nicht lesen. auch wiederholt nicht“.

**Was daraus folgt:**
- Anscheinend ist mindestens ein Extraktionsprozess angelaufen oder sichtbar erfolgreich gewesen.
- Das Modell kann den relevanten Inhalt nicht verlässlich in die Antwort übernehmen.
- **Nicht belegt**: dass eine für das Modell lesbare Textdatei tatsächlich fertig extrahiert, korrekt indexiert und referenzierbar war; dass ein bestimmtes Berechtigungsproblem vorliegt; dass jeder EPUB-Typ betroffen ist.

**Bewertung:** **FAIL** für die konkrete end-to-end-Aufgabe des Nutzers. **Root Cause: OPEN.** Keine Tool-Fehlerpayloads vorliegend.

## 8. K-05b – PDF-Upload, erster Lauf (PARTIAL beim Zugriff)

**Testanlage:** Entsprechende PDF-Fassung in DRS hochgeladen; gleicher K-04-Prompt.

**[B] Werkzeug:** `analyze_uploaded_documents`.

**[B] Antwortbefund:** Der Testling behauptet nun, sich „ausschließlich“ auf nachweisbare Originalpassagen zu stützen, und liefert zahlreiche kurze als wörtlich bezeichnete Fragmente: Kapitel „DEN TEXT INS LEBEN FÜHREN“, Stichwörter zu Besinnung, Gebet, Gegenwart Gottes und Reifenlassen von Einsichten; außerdem Zitate zur gründlichen Exegese und Kontrolle von Predigermotiven. Fast alle Stellen werden als „PDF-Seite 1“ oder „PDF-Seite 2“ verortet.

**[I] Plausibler technischer Fortschritt:** Das Werkzeug lieferte offenbar verwertbare Textinformationen aus dem PDF oder einem damit verknüpften extrahierten Kontext. Im Unterschied zum EPUB-Test entsteht eine inhaltlich konkrete Antwort.

**[O] Nicht bewiesen:** Exakte Zitatübereinstimmung, Vollständigkeit des Auszugs, echte gedruckte Seitenzahlen, tatsächlicher Kapitelkontext. Insbesondere sind Bezeichnungen „spiritueller Reset“, „verbindlicher Schritt“ und „göttlich wirksam“ **eigene Deutungen** des Assistenten, keine nachgewiesenen Wortlautaussagen Klipperts.

**Zwischenbewertung:** **PARTIAL** für den technischen Dokumentenzugriff; **keine Quellenintegritätsfreigabe**.

## 9. K-05c – Kontrollfrage zur Quellenprovenienz (FAIL)

**Nachfrage im selben PDF-Chat (wortgleich):**

> Du hast deine Aussagen auf PDF-Seite 1 und PDF-Seite 2 gestützt.
>
> Prüfe bitte nochmals, ob es sich dabei um die tatsächlichen PDF-Seiten eines vollständigen Buches oder um die Seiten eines extrahierten Ausschnitts handelt.
>
> Nenne außerdem die exakten Kapitelüberschriften, unter denen du die Aussagen zur Meditation gefunden hast.
>
> Unterscheide ausdrücklich zwischen wörtlichen Zitaten, sinngemäßen Zusammenfassungen und deinen eigenen Interpretationen. Falls du diese Angaben nicht anhand des Dokuments überprüfen kannst, kennzeichne sie als nicht verifiziert.

**[A] Tool-/Kontextlimit laut Testling, wörtlich:**

```text
vom text zur predigt_klippert, wolfgang.pdf: analyzed only the first 80000 characters because of the configured processing budget.
```

**Wichtige Beweisgrenze:** Diese Meldung wird **vom Testling als aus dem Dokumentenkontext stammend zitiert**; die rohe `analyze_uploaded_documents`-Ausgabe liegt nicht vor. Deshalb das 80.000-Zeichen-Limit als **reported**, nicht als unabhängig bestätigte Toolkonfiguration dokumentieren.

**[A] Neubewertung der Seiten:** Die früheren „PDF-Seiten 1/2“ seien „erste beiden Seiten des extrahierten Textes“ und keine echten Buchseiten. Das folgt **nicht** allein aus der 80.000-Zeichen-Obergrenze. Ob der Extraktor überhaupt eigenständige Seitenkennungen lieferte, ist offen.

**[B] Weitere Antwortprobleme:**
1. Die zuvor als wörtlich bezeichneten Textstellen enthalten teils Auslassungspunkte. Ohne Originalpassage kann weder exakter Wortlaut noch zulässige Kürzung verifiziert werden.
2. Der Assistent erklärt ausdrücklich **alle** aufgeführten Zitate für „verifiziert“, ohne Seiten-/Zeilenreferenzen oder Rohpassagen verfügbar zu machen. Für Reviewer nicht unabhängig prüfbar.
3. Er behauptet, keinerlei Paraphrasen oder Interpretationen hinzugefügt zu haben. Das steht im Widerspruch zu seinen Interpretationsbegriffen „spiritueller Reset“, „göttlich wirksam“ usw. im ersten PDF-Lauf.
4. Das Kapitel „DEN TEXT INS LEBEN FÜHREN“ wird als „Kapitel 4“ eingeordnet; ohne Originalsichtung bleibt auch diese exakte Zuschreibung offen.

**Bewertung:** **FAIL für Belegprovenienz und transparente Trennung von Zitat, Paraphrase, Interpretation.** Nicht gleichzusetzen mit dem Beweis, dass jedes einzelne Zitat falsch ist. Der dokumentierte Fehler ist vielmehr die **unbelegte Behauptung vollständiger Verifikation** und die widersprüchliche Selbstauskunft.

## 10. Querbefunde und Folgerungen

### 10.1 Aussagekraft für den Systemprompt

Der Prompt `v0.1.2` fördert im K-01 und K-04 vermutlich erwünschte Zurückhaltung. **Kausalität nicht bewiesen**: anderer Fragetyp, unbestätigter Prompt-Einbringungskanal, unbekanntes Modell und keine kontrollierten mehrfachen Durchläufe. K-02 und K-05c zeigen, dass Formeln zur Quellenredlichkeit kein Ersatz für echte Verifikation sind.

### 10.2 Besondere Risiken für THEOBald

- **Zugriff vs. Nachweis:** Extraktion, Dateianalyse und nachgewiesene Originallektüre sind verschiedene Stufen.
- **Provenienz:** „PDF-Seite“, Druckseite, Tool-Seite, Textfenster, Suchtreffer und Zeichenbudget niemals gleichsetzen.
- **Zitatdisziplin:** Exaktzitate erfordern tatsächliche Originalpassage und verifizierbare Position; fehlenden Originalvergleich ausdrücklich offenlegen.
- **Interpretationsgrenze:** Der Assistent muss eigenständige Deutung als solche kennzeichnen, selbst wenn sie auf einem Originalzitat basiert.
- **Schleifenvermeidung:** Wiederholte identische EPUB-Zugriffsversuche ohne Diagnose sind nicht zielführend.
- **Urheberrecht:** Das vollständige Klippert-Werk gehört nicht in ein öffentliches Code-Repository; Logs sollten nur minimal erforderliche kurze Auszüge enthalten.

### 10.3 Technisch nächste sinnvolle Prüfschritte (noch nicht ausgeführt)

1. Originale DRS-Toolausgabe zu `analyze_uploaded_documents` prüfen, insbesondere Dateibezeichner, extrahierter Bereich, tatsächliche Page-Marker, 80.000-Zeichen-Meldung.
2. Gegen das lokale, rechtmäßig verfügbare Buch-PDF fünf gezielte Kurzstellen samt tatsächlicher physischer PDF-Seite/gedruckter Buchseite abgleichen. **Nicht ungeprüft alle bisherigen neun Zitate als falsch markieren.**
3. Einen Ausschnitt aus Kapitel 4 als kontrollierte kleine Textprobe in den Chat geben und denselben Auftrag wiederholen, um Retrievalfehler und Quelleninterpretation zu trennen.
4. Prüfen, ob DRS/Allrounder mehr als nur den Anfangsbereich des PDFs über Werkzeuge adressieren kann; andernfalls PDF in sinnvoll abgegrenzte Einzelkapitel zerlegen (nur in erlaubter privater Testumgebung).
5. Bei erneutem EPUB-Test Fehlerpayload und Dateiverweis erfassen, nicht nur Ergebnistext.

## 11. Bezug zu bisherigen DRS-Abnahmetests

- `tests/runs/2026-11-11-DRS-T02-P.md` – Dokumentenzugriff nach Nutzerintervention.
- `tests/runs/2026-11-11-DRS-T04.md` – Dokumentbelege, Halluzinationen.
- `tests/runs/2026-11-11-DRS-T04-K1.md` – gleicher Text direkt im Chat: 8/8.
- `tests/runs/2026-11-11-DRS-T08-B-R1-OVERALL.md` – früherer Quellen- und Zitatfehler bei EÜ 2016.

**Abschluss:** K-01 bis K-05 sind **explorative Befunde**, kein formal akkreditierter Qualitätsnachweis und keine generelle Aussage, dass PDF immer und EPUB nie funktioniert. **SSOT bleibt GitHub auf dem Branch `drs-ki-test`; `main` unverändert.**
