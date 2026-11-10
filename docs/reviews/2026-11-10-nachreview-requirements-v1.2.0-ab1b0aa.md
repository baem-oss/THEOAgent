# QS-Nachreview THEOAgent Requirements v1.2.0 – Findings-Disposition

**Datum:** 2026-11-10
**Verfasser:** Unabhängiger technischer Reviewer / Quality Engineer, Projekt THEOAgent
**Auftrag:** Nachreview der Requirements-Revision v1.2.0 (Branch `review/requirements-v1.2.0-qs`) gegen die Findings F-01 bis F-18 des QS-Berichts zur Baseline v1.1.0
**Abgrenzung:** keine Implementierung, keine Änderungen an GitHub, keine alternative Gesamtarchitektur
**Berichtsstatus:** vollständiger Bericht, keine Auszüge; Belege als Links, damit der Text ohne Kontextverlust weitergegeben werden kann

---

## 1. Prüfgegenstand

| Punkt | Inhalt |
|---|---|
| Repository | `baem-oss/THEOAgent` |
| Branch | `review/requirements-v1.2.0-qs` |
| Geprüfter Commit | `ab1b0aae936d1d5ba9a5641edf1c0bf85dc7e497`, Commit-Zeit 2026-11-10T16:56:05Z |
| Branchbasis | `main` = `74eab17`; die Revision besteht aus sechs Commits (`334b1c0e`, `45a27496`, `c5129045`, `205fa172`, `1f1c3ca3`, `ab1b0aa`) |
| Geprüfte Dateien | `docs/requirements/BASELINE.md`, Git-Blob `976cd28cec51f73f944e80a72fa4c0b8d93a215f`, 29.069 Byte, Version 1.2.0 (Review-Kandidat); `docs/requirements/TRACEABILITY.md`, Git-Blob `6e29b5bfa5609951427b28e72db3d9392cf1d919`, 2.006 Byte; `docs/requirements/ACCEPTANCE_PROFILE.md`, Git-Blob `cf8dd21bf06baf6f09ec55fe3ccb4bbfd31f4705`, 9.791 Byte; `README.md` am selben Commit |
| Vergleichsstände | `docs/requirements/BASELINE.md` v1.1.0 am Commit `b3d901c`; Vorgängerrepo `baem-oss/THEOBald`, `main` (`docs/baseline-v1.2.0.md`, `README.md`) |
| Verfügbare Tests | keine im Repository |
| Tatsächlich ausgeführte Tests | **keine.** Kein Testauftrag und kein Testartefakt; es werden keine PASS-Angaben übernommen und keine Testergebnisse behauptet |

**Methodik:** Alle Aussagen beruhen auf Volltextabgleich der abgerufenen Dateien am genannten Commit, nicht auf Chat-Zusammenfassungen. Die Prüfung ist über Commit-SHA und Git-Blob-Kennungen reproduzierbar.

---

## 2. Gesamturteil

**Freigabefähig mit nicht blockierenden Hinweisen – als fachliche Anforderungsgrundlage (Requirements-Freigabe).**
**Nicht freigabefähig – als Implementierungs- oder Qualitätsabnahme.**

Alle drei BLOCKER des Erstberichts sind geschlossen oder in einen benannten, vom Product Owner zu entscheidenden Rest überführt; alle neun MAJOR-Findings sind geschlossen. Offen sind ausschließlich zwei MINOR-Punkte und zwei Teilerledigungen.

---

## 3. Eigene Nachkontrollen (nicht übernommen, selbst geprüft)

| Prüfung | Ergebnis |
|---|---|
| Zählungen | 27 US, 34 FANF, 13 NFANF, 6 RANF, 18 GR, 5 SP, 4 DAT – Abschnittsüberschriften der Baseline und README-Tabelle stimmen überein |
| Beidseitige Abdeckung | maschinell geprüft: 27/27 US mindestens einer FANF zugeordnet, 34/34 FANF mindestens einer US; keine Lücke |
| Rückverfolgbarkeitsspalte §3 der Baseline gegen `TRACEABILITY.md` | in allen 34 Fällen identisch |
| Keine Abschwächung gegenüber v1.1.0 | GR-09, GR-03, SP-01, SP-03, DAT-01 bis DAT-04, FANF-31, FANF-33 wurden verschärft bzw. präzisiert; Umfang 33 auf 34 FANF, 12 auf 13 NFANF, 5 auf 6 RANF; keine Anforderung gestrichen oder aufgeweicht |
| RANF-04-Integritätswert | `cc5a4dd89eb2279ba61fea105eea33ce45767b783eb572475fef9903c778174c` stimmt mit dem im Vorgängerrepo für `Prompts/THEOBald_Fachstandard.md` dokumentierten SHA-256 überein. Das Artefakt selbst ist privat; seine Integrität ist vom Reviewer **nicht** unabhängig verifizierbar |

---

## 4. Findings-Disposition F-01 bis F-18

| ID | Priorität | Status | Begründung / Nachweis |
|---|---|---|---|
| F-01 | BLOCKER | **PARTIAL** | Messverfahren für NFANF-01 bis NFANF-11 im Abnahmeprofil §3 vollständig beschrieben; NFANF-12 und NFANF-13 mit harten Nullkriterien; elf Grenzwerte und Korpora ausdrücklich offen (Baseline §9, Abnahmeprofil §3). Siehe Abschnitt 5 |
| F-02 | BLOCKER | **CLOSED** | NFANF-13 „Belegintegrität" (Null Fehler im Negativ- und Positivkorpus); Abnahmefall T-04 mit falschen Absatznummern, nicht existierenden Werken und Inhaltsverzeichnis-Treffern; GR-03 erweitert |
| F-03 | BLOCKER | **CLOSED** | §1 definiert Arbeitsfassung, Freigabe, Freeze und Geltungsbereich und trennt Freigabe von Freeze; DAT-03 mit Adressierbarkeit, zwei unabhängigen Statusdimensionen, Statusänderung nur auf ausdrückliche Nutzeranweisung, ohne Technologievorgabe; GR-09, NFANF-12, T-05 |
| F-04 | MAJOR | **CLOSED** | DAT-02 nennt quellenartgerechte Fundstellen (Bibelstelle, KKK-Absatznummer, Canon, Artikel/Abschnitt, überprüfte Druckseite, Text-/Werkzeugbereich), verbietet Gleichsetzung und Umetikettierung von PDF-Seite, Buchseite, Suchscore und Werkzeugzeile und verlangt Kennzeichnung verbleibender Ungenauigkeit |
| F-05 | MAJOR | **CLOSED** | neue FANF-34 deckt beide Teile von US-25 (Aussagearten unterscheiden, Gegenpositionen einbeziehen); Mapping US-25 auf FANF-10, FANF-12, FANF-34 |
| F-06 | MAJOR | **CLOSED** | FANF-31 verallgemeinert: v1.1.0 „Arbeitsschritt oder Arbeitsumfang … begrenzen" wird zu v1.2.0 „Arbeitsschritt, Bearbeitungstiefe oder Arbeitsumfang … ausrichten und darüber hinausgehende Folgeaufgaben unterlassen". US-20 damit generell gedeckt. FANF-14 bleibt predigtspezifisch – sachgerecht, weil nur US-09 schrittweises Arbeiten verlangt |
| F-07 | MAJOR | **CLOSED** | neue RANF-06: textbasierte PDF, DOCX, EPUB, TXT und Markdown; OCR und Bildseitenanalyse ausdrücklich ausgenommen; unlesbare Inhalte dürfen nicht als vollständig gelesen dargestellt werden |
| F-08 | MAJOR | **CLOSED** | GR-09: Änderung setzt ausdrückliche Aufhebung des Freeze voraus; bloße Änderungsanweisung gilt nicht als stillschweigende Aufhebung; bei unklarem Status keine Unterstellung. Abnahmefall T-05 prüft genau diesen Fall |
| F-09 | MAJOR | **CLOSED** | §1 definiert Quellenzulassung (Nutzerauftrag und Betreiberfreigabe); SP-03 nennt Loopback-, private, Link-Local- und Metadatenadressen, gefährliche Umleitungen und DNS-Umbindung und trennt lokale Knowledge-Zugriffe; Abnahmefall T-07 |
| F-10 | MAJOR | **CLOSED** | SP-01: bei ungeklärter Zulässigkeit externe Übermittlung unterlassen und Einschränkung benennen; DAT-01 mit Rechte- und Übermittlungsstatus, „unbekannt ist kein positiver Freigabestatus"; Vorbedingung in §5, gebunden an SP-01, SP-05 und DAT-01 (keine verwaiste Pflicht); Abnahmefall T-06 |
| F-11 | MAJOR | **CLOSED** | RANF-04 benennt Artefakt, Herkunftspaket v1.2.0 und SHA-256 und kennzeichnet die Referenz als „nachzuprüfende Ausgangsreferenz" ohne inhaltliche Freigabe; Hash gegen Vorgängerrepo konsistent |
| F-12 | MAJOR | **CLOSED** | GR-03 verlangt Benennung der überprüften Textfassung (Bibelübersetzung, Katechismusfassung, CIC-Fassung, maßgebliches Partikularrecht) und Kennzeichnung fehlenden Nachweises; DAT-01 „nachgewiesene Ausgabe beziehungsweise Fassung" |
| F-13 | MINOR | **CLOSED** | §1 definiert Arbeitsfassung, Freigabe und Freeze samt Koexistenz; DAT-03 trennt Nutzerfreigabe von Schutzstatus |
| F-14 | MINOR | **OPEN** | FANF-05 in v1.2.0 wortgleich zu v1.1.0 („in ausreichendem Kontext lesen"); „ausreichend" ist weder in der Baseline noch im Abnahmeprofil definiert. Teilweise berührt durch NFANF-02 („zur Behauptung passende Quellenstelle") und T-02 („irrelevante Anfangszeilen") |
| F-15 | MINOR | **CLOSED** | Abnahmefall T-08 setzt das geforderte Verfahren um: identische Position mit zustimmendem und ablehnendem Nutzerframing muss zu konsistent begründeter Bewertung führen |
| F-16 | MINOR | **OPEN** | DAT-01 und DAT-02 verwenden weiterhin „zuordnen können" statt „muss … zuordnen". Formal, nicht blockierend; siehe Abschnitt 6 |
| F-17 | MINOR | **OPEN** | Die Grenze GR zu NFANF (GR-17/NFANF-04, GR-09/NFANF-12) ist weiterhin nicht ausdrücklich benannt. Nach eigener Empfehlung im Erstbericht war „keine inhaltliche Änderung erforderlich" |
| F-18 | MINOR | **PARTIAL** | THEOAgent-Seite erledigt: RANF-04 benennt eine nachzuprüfende Referenz mit Hash, ohne inhaltliche Freigabe. Die Widersprüchlichkeit im Vorgängerrepo besteht fort: `docs/baseline-v1.2.0.md` meldet „82/82 PASS", während `README.md` weiter „Der Integritätsvergleich gegen SHA256SUMS.txt steht noch aus" und „keine Modelltests" führt. Die Auswahl der verbindlichen Fassung ist eine PO-Entscheidung |

**Bilanz:** 13 CLOSED, 2 PARTIAL (F-01, F-18), 3 OPEN (F-14, F-16, F-17). Die drei offenen Punkte waren sämtlich MINOR der Ersteinstufung; kein BLOCKER und kein MAJOR bleibt offen.

---

## 5. Beurteilung der F-01-Abgrenzung (ausdrücklich)

Die Abgrenzung ist sachgerecht und wird als richtige Entscheidung bewertet.

1. F-01 verlangte wörtlich einen Abnahme-Anhang mit Korpus, Bewertungsverfahren und Schwellenwert je NFANF. Verfahren und Prüffälle sind jetzt vollständig beschrieben; die Werte fehlen. Die Maßnahme ist damit zur Hälfte umgesetzt – das entspricht PARTIAL und wird auch so deklariert, nicht als erledigt ausgegeben.
2. **Keine Zahlen zu erfinden** ist richtig: Ein Mindestwert ohne empirische Grundlage wäre Scheingenauigkeit und würde später gegen die eigene Spezifikation arbeiten. Die Formulierung des Abnahmeprofils, dass eine fehlende Grenzwertfestlegung nicht als PASS protokolliert werden darf, schließt die Lücke prozedural.
3. **Korrektur der eigenen Einstufung:** F-01 war als BLOCKER gegen die Architektur- und Abnahmegrundlage gerichtet. Nach Vorliegen des Abnahmeprofils ist der verbleibende Teil keine Spezifikationslücke mehr, sondern eine Abnahmeentscheidung des Product Owners, die auf erste Testergebnisse gestützt werden soll. Der Rest wird deshalb von BLOCKER auf MAJOR herabgestuft – blockierend für die Qualitätsabnahme, nicht für die Requirements-Freigabe. Das ist eine Folge der geänderten Faktenlage, kein Entgegenkommen.
4. **Ein Formalismus bleibt:** Das Messverfahren für NFANF-07 ist im Anforderungstext als „Anteil der Texte, die das Verfahren bestehen" und im Abnahmeprofil als „Anteil der Texte ohne festgelegte schwere pastorale Verletzungen" beschrieben – zwei verschiedene Metriken. Da beide Seiten offen sind, entsteht daraus kein Finding; bei der Grenzwertfestlegung ist eine der beiden Formulierungen zu wählen.

---

## 6. Neue Mängel

| ID | Priorität | Fundstelle | Befund | Nachweis | Auswirkung | Empfehlung (kleinste sachgerechte Korrektur) |
|---|---|---|---|---|---|---|
| N-01 | MAJOR | `BASELINE.md` §2 US-21, §3 FANF-18, §8 DAT-03; `TRACEABILITY.md` US-21 | US-21 verspricht zwei Nutzermöglichkeiten („freigeben **und** einfrieren"). Funktionalisiert ist nur das Einfrieren: FANF-18 bietet ausschließlich das Kennzeichnen als „eingefroren". Die Freigabe erscheint nur als Datenmerkmal in DAT-03 („Statusänderungen dürfen nur auf ausdrückliche Nutzeranweisung erfolgen"); DAT-03 ist in der Matrix nicht mit US-21 verknüpft. Kein Abnahmefall prüft die Freigabe (T-05 deckt Freeze und Aufhebung) | Volltextabgleich aller 34 FANF auf den Begriff „Freigabe"; Prüfung der Zuordnung US-21 auf FANF-18 | Eine zugesagte Nutzermöglichkeit ist nicht implementierbar spezifiziert; dieselbe Fehlerklasse wie das geschlossene F-05, nur enger. Ohne sie ist DAT-03 nicht auslösbar | FANF-18 um einen Halbsatz erweitern: „… eine Textfassung oder einzelne Textpassagen als freigegeben oder als eingefroren zu kennzeichnen und diesen Status nur auf ausdrückliche Nutzeranweisung zu ändern"; Zuordnung US-21 um DAT-03 ergänzen. Keine neue FANF nötig |
| N-02 | MINOR | `BASELINE.md` §2 US-23, §3 FANF-19 | US-23 nennt drei Gegenstände („frühere Entwürfe, Vorlagen und freigegebene Arbeitsergebnisse"); FANF-19 deckt nur „frühere Arbeitsfassung". „Vorlage" ist weder in §1 definiert noch sonst referenziert | Volltextabgleich §1, §2, §3 | Der Begriff erzeugt bei der Umsetzung Nachfragen; ein Teil der US ist nicht rückverfolgbar | Entweder „Vorlagen" in §1 als Sonderfall einer Arbeitsfassung definieren oder in US-23 streichen. Eine Zeile |
| N-03 | MINOR | `BASELINE.md` §5 RANF-06 | RANF-06 mischt Umfangsbestimmung (Formate, OCR-Grenze) mit einem Verhaltensverbot („unlesbare Inhalte dürfen nicht als vollständig gelesen dargestellt werden"). Randbedingungen sind im Dokument als „Projektrahmen / aktuelle Ausgangslage" definiert – ein Verbot gehört in die Regel- oder Qualitätsebene | Typenvergleich §1 gegen §5 gegen §6 | Wird die Ausgangslage später geändert, kann die Verhaltensregel mit der Randbedingung entfallen; sie ist als Anforderung nicht zählbar und nicht adressierbar | Satz nach GR-18 (Teilergebnisse) oder GR-16 (Unsicherheit) verschieben; RANF-06 auf den Formatumfang begrenzen. Teilweise abgedeckt durch NFANF-03 („nichtlesbares Format") und T-01 |

---

## 7. Offene Fragen

1. **Grenzwerte und Korpora NFANF-01 bis NFANF-11** – Festlegung durch den Product Owner nach ersten Testergebnissen; ohne sie ist keine Qualitätsabnahme möglich (Rest aus F-01).
2. **Verbindliche Fassung des Fachstandards** – die Vorgängerdokumentation widerspricht sich („82/82 PASS" gegen „steht noch aus"); RANF-04 bindet eine Referenz, gibt sie aber ausdrücklich nicht frei.
3. **N-01 und N-02** – Korrektur in v1.2.0 vor der Freigabe oder Nachziehen in v1.2.1? Beides vertretbar; N-01 sollte vor dem Architektursign-off geschlossen sein.
4. **Reichweite von US-23** – §1 begrenzt den Geltungsbereich auf den „zugänglichen aktuellen Arbeitskontext" und verbietet unbewiesene chatübergreifende Persistenz. Damit ist die Wiederverwendung auf den nachweislich zugänglichen Bestand begrenzt. Ob das die Nutzererwartung trifft, ist eine PO-Entscheidung; als bewusste Abgrenzung ist sie sauber formuliert.
5. **Ausgabetokenlimit der Erprobungsumgebung (angefordert 32.768, zulässig 21.052)** – bleibt in v1.2.0 unerwähnt. Wird **nicht** als Finding erhoben: NFANF-08 verlangt nun die Dokumentation der Modell-, Provider- und Werkzeugkonfiguration, und eine Aufnahme in die Baseline wäre eine technische Vorgabe, die das Dokument zu Recht vermeidet.

---

## 8. Abnahmeempfehlung

**Requirements-Freigabe: ja.** v1.2.0 ist als fachliche Grundlage für den nächsten Entwicklungsschritt freigabefähig – mit den nicht blockierenden Hinweisen aus Abschnitt 4 und 6. Die Revision behebt alle drei BLOCKER sachlich und ohne unnötige Architektur: Sie präzisiert, statt neu zu strukturieren, sie erfindet keine Zahlen, sie gibt keine Technologie vor und sie kennzeichnet Offenes als offen.

**Implementierungs- und Qualitätsabnahme: nein.** Es wurden keine Tests ausgeführt; die Qualitätsgrenzwerte fehlen; die Nachweisstände der technischen Bestandsaufnahme (Nachtrag N4 des Erstberichts) bleiben ungeklärt. Ein bestandener Synthetiktest wäre keine fachliche Abnahme.

- **Vor dem Architektursign-off zu schließen:** N-01 (Freigabe-Funktion), F-14 (Kontextbegriff).
- **Zu entscheiden:** F-01-Grenzwerte, F-18-Fachstandardfassung.
- **Ohne Nacharbeit:** F-16 und F-17 – Formfragen, auf die nicht gedrängt wird.

---

## 9. Belege

- Branch: https://github.com/baem-oss/THEOAgent/tree/review/requirements-v1.2.0-qs
- Commit: https://github.com/baem-oss/THEOAgent/commit/ab1b0aae936d1d5ba9a5641edf1c0bf85dc7e497
- Baseline v1.2.0: https://github.com/baem-oss/THEOAgent/blob/ab1b0aae936d1d5ba9a5641edf1c0bf85dc7e497/docs/requirements/BASELINE.md
- Traceability v1.2.0: https://github.com/baem-oss/THEOAgent/blob/ab1b0aae936d1d5ba9a5641edf1c0bf85dc7e497/docs/requirements/TRACEABILITY.md
- Abnahmeprofil v1.2.0: https://github.com/baem-oss/THEOAgent/blob/ab1b0aae936d1d5ba9a5641edf1c0bf85dc7e497/docs/requirements/ACCEPTANCE_PROFILE.md
- README v1.2.0: https://github.com/baem-oss/THEOAgent/blob/ab1b0aae936d1d5ba9a5641edf1c0bf85dc7e497/README.md
- Baseline v1.1.0 (Vergleichsstand): https://github.com/baem-oss/THEOAgent/blob/b3d901c8252e1ac95c8cd0cfc2dda78ea7810ab6/docs/requirements/BASELINE.md
- Vorgänger-Integritätsnachweis: https://github.com/baem-oss/THEOBald/blob/main/docs/baseline-v1.2.0.md
- Vorgänger-README (widersprüchlicher Status): https://github.com/baem-oss/THEOBald/blob/main/README.md

*Arbeitsregeln dieses Berichts: ausschließlich Volltextabruf der Repo-Dateien am genannten Commit, keine Beurteilung aus eingefügtem Chat-Text; keine Tests ausgeführt; keine fremden PASS-Aussagen übernommen; keine Änderungen an GitHub.*

---

## 10. Ablagevermerk

**Primäre Ablageform:** diese Open-WebUI-Notiz mit dem vollständigen Markdown-Bericht – der Product Owner gibt den Inhalt an den Software Engineer weiter.

**Identische Dateifassung für den Repo-Commit:** `docs/reviews/2026-11-10-nachreview-requirements-v1.2.0-ab1b0aa.md`
Umfang 16.219 Byte, LF, endet mit Newline, SHA-256 `04484ea4809ba6b39ed5d281cef0d34a6cf36675bb8d70b3c201874c1e465320`.
Der Commit erfolgt durch den Software Engineer (Ablegeweg laut `docs/reviews/INDEX.md`); der Reviewer legt im Repo nichts selbst ab. Nach dem Commit werden Notiz- und Repo-Fassung auf Byte-Identität geprüft und der Permalink nachgewiesen.
