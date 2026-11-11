> **Übergabevermerk.** Dieser Prüfbericht wird weisungsgemäß ausschließlich als Open-WebUI-Notiz abgelegt, nicht als Datei im Repository; der Reviewer nimmt keine GitHub-Änderungen vor und vergibt keine Prüfsummen. Maßgeblich für den Projektstand ist das Repository `baem-oss/THEOAgent`. Der Text ist zur Übernahme durch den Software Engineer geeignet.

# QS-Review – Diagnostisches Testkonzept T-01 bis T-03

**Datum:** 11.11.2026  
**Verfasser:** Unabhängiger Quality Engineer (QE), Projekt THEOAgent  
**Auftrag:** Arbeitsauftrag des Product Owners (PO) vom 11.11.2026 – unabhängiges Review des Testkonzepts T-01 bis T-03 (Prüfantworte A bis F)  
**Grenzen:** keine Implementierung, keine Architekturvorschläge ohne nachgewiesenen Bedarf, keine Repository-Änderungen, keine erneute Grundsatzprüfung der bereits freigegebenen Baseline v1.2.0

* * *

## 1. Prüfgegenstand

| Punkt | Inhalt |
| --- | --- |
| Repository | `baem-oss/THEOAgent` |
| Branch | `test/t01-t03-diagnostics-v1` |
| Geprüfter Commit | `fec545c56f388c1b611c96a6120bf5d273e9ae69` (Kürzel `fec545c`), Commit-Zeit 2026-11-10T21:01:39Z, Nachricht „test(diagnostics): fix T-01–T-03 plan, synthetic fixtures and oracles", Parent `17c63e8d` |
| Änderungsumfang | neun hinzugefügte Dateien, 209 Zeilen hinzugefügt, 0 gelöscht; keine Änderung an bestehenden Dateien |
| Referenzstand `main` | `17c63e8d8e001be4a3a2f313181fb29101471d01` (2026-11-10T17:25:04Z, „docs(reviews): record PO approval and closure of N-01 and F-14"); Baseline v1.2.0 über PR #1 und Merge `5c041389` in `main` |
| Geprüfte Dateien (alle neun) | `docs/testing/T01-T03_DIAGNOSTIC_PLAN.md`; `tests/oracles/T01-T03_ORACLES.md`; `tests/runs/T01-T03_RUN_TEMPLATE.md`; `tests/fixtures/t01/README.md`; `tests/fixtures/t01/document_six_pages.pdf`; `tests/fixtures/t01/image_only.pdf`; `tests/fixtures/t02/predigt.md`; `tests/fixtures/t02/fachpapier.md`; `tests/fixtures/t03/README.md` |
| Referenzierte Dokumente (Volltext geprüft) | `docs/requirements/BASELINE.md` (v1.2.0), `docs/requirements/ACCEPTANCE_PROFILE.md` (v1.2.0), `docs/requirements/TRACEABILITY.md` (v1.2.0), `docs/architecture/COMPONENT_INVENTORY.md`, `docs/WORKFLOW.md` |
| Testausführung | **keine**. Ich habe keinen Testlauf durchgeführt und keine Testumgebung; eine Prüfung des Testkonzepts ist kein Nachweis ausgeführter End-to-End-Tests |

Verbindliche Quellen im Repository:

*   `https://github.com/baem-oss/THEOAgent/commit/fec545c56f388c1b611c96a6120bf5d273e9ae69`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/docs/testing/T01-T03_DIAGNOSTIC_PLAN.md`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/oracles/T01-T03_ORACLES.md`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/runs/T01-T03_RUN_TEMPLATE.md`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/fixtures/t01/README.md`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/fixtures/t01/document_six_pages.pdf`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/fixtures/t01/image_only.pdf`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/fixtures/t02/predigt.md`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/fixtures/t02/fachpapier.md`
    
*   `https://raw.githubusercontent.com/baem-oss/THEOAgent/fec545c56f388c1b611c96a6120bf5d273e9ae69/tests/fixtures/t03/README.md`
    
*   Referenz auf `main`: `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/requirements/BASELINE.md`, `.../ACCEPTANCE_PROFILE.md`, `.../TRACEABILITY.md`, `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/architecture/COMPONENT_INVENTORY.md`, `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/WORKFLOW.md`
    

* * *

## 2. Prüfgrundlagen

**Verbindliche Anforderungsgrundlagen (PO-freigegeben, nicht erneut geprüft):**

*   `BASELINE.md` v1.2.0 – 27 US, 34 FANF, 13 NFANF, 6 RANF, 18 GR, 5 SP, 4 DAT; NFANF-12/-13 mit harten Nullkriterien; F-01 (Grenzwerte/Korpora NFANF-01…-11) ausdrücklich offen.
    
*   `ACCEPTANCE_PROFILE.md` v1.2.0 – Abnahmefälle T-01 bis T-08, Messverfahren NFANF-01…-13, Nachweisschema, Bewertungsstufen `PASS`/`PARTIAL`/`FAIL`/`BLOCKED`/`NOT_RUN`; §1 trennt technisch nachgewiesene Existenz/Lektüre von der inhaltlichen Tragfähigkeit der Zuschreibung.
    
*   `TRACEABILITY.md` v1.2.0 – US→FANF-Matrix.
    
*   `COMPONENT_INVENTORY.md` – dokumentierte Testumgebung und beobachtete Vorläuferbefunde (u. a. I01 FAIL/PARTIAL bei kombinierter PDF-Predigtprüfung, I02 Gesamt-FAIL wegen unbelegter amtlicher Quellenzuordnung, QP01/QP03 FAIL bei autonomer Websuche, kein Nachweis einer Freeze-/Versionsfunktion).
    
*   `WORKFLOW.md` – SSOT-Regel, Rollen, Umgang mit Commit-/Blob-Kennungen, Ablaufregel „ein grüner CI-Lauf ist keine Abnahme".
    

**Prüfkriterien des Auftrags:** A Anforderungsabdeckung; B Testdaten und Prüforakel (einschließlich technischer Korrektheit beider PDFs); C diagnostische Aussagekraft und Trennung technischer Lektüre von inhaltlich korrekter Quellenverwendung; D Bewertungskriterien und Falsch-PASS-Risiko; E praktische Durchführbarkeit mit vorhandenen Open-WebUI-Mitteln; F fachliche/rechtliche Korrektheit, Schwerpunkt T-03.

* * *

## 3. Durchführung und Nachweise

Tatsächlich ausgeführte Prüfhandlungen (keine weiteren):

1.  **Metadaten und Umfang des Commits** über die GitHub-API abgerufen: neun hinzugefügte Dateien, 209/0 Zeilen, Parent `17c63e8d`; keine Änderung an bestehenden Dateien.
    
2.  **Volltextabruf aller sieben Textdateien** über `raw.githubusercontent.com` am genannten Commit. Bewusst **nicht** aus der Patch-Darstellung der API geurteilt: Diese kann Zeichen verschlucken (in diesem Projekt bereits einmal Ursache eines drohenden Fehlbefunds). Die Volltexte wurden zusätzlich gegen die Patch-Darstellung abgeglichen; im inhaltlich relevanten Text keine Abweichung.
    
3.  `document_six_pages.pdf`: Abruf über `raw.githubusercontent.com`. Der Extraktor lieferte den vollständigen Text **aller sechs Seiten**; jede Seite trägt die Fußzeile „PDF-Seite N von 6 | SYN-T01-PDF-01". Seitenweiser Abgleich gegen das Orakel (Seite 1 „Bernstein"/„KELCH-29"; Seite 3 „22. April 2032"/„violett"; Seite 6 „dreifacher Sichtung"/„FIRN-46"); Seiten 2, 4, 5 enthalten die im Orakel genannten Distraktoren, insbesondere „FELS-12 ist kein Abschlusskennwort" (Seite 5) und „Diese Seite enthält absichtlich keinen neuen Termin" (Seite 4).
    
4.  `image_only.pdf`: Abruf über `raw.githubusercontent.com` ergab **keinen extrahierbaren Text**. Zusätzlich Strukturprüfung über das Git-Blob-Objekt (`https://api.github.com/repos/baem-oss/THEOAgent/git/blobs/3e95cf01f4a45cb90383fb8eccc7a1fec3032cff`) durch Decodierung der Base64-Auslieferung. Ergebnis der Dekodierung: wohlgeformte PDF-Struktur mit genau einer Seite (`/Count 1`); eine Bild-XObject-Ressource `Im1` (47 × 7 Pixel, `/DeviceGray`, `/ASCIIHexDecode`); **keine** `/Font`-Ressource und **kein** Textoperator – der Seiteninhalt besteht ausschließlich aus `q 465 0 0 90 65 552 cm /Im1 Do Q`. Damit ist die Angabe „ohne PDF-Textoperator" **bestätigt**. Der im Raster sichtbare Inhalt („SCAN 481") ist **nicht verifiziert** – siehe Abschnitt 8.
    
5.  **Amtliche Quellen zu T-03:**
    *   Codex Iuris Canonici, Buch III, Cann. 762–772 (Vatikan, deutsch): `https://www.vatican.va/archive/cod-iuris-canonici/deu/documents/cic_libro3_cann762-772_ge.html` – can. 766 und can. 767 § 1 im Wortlaut abgerufen.
        
    *   Dikasterium für den Gottesdienst und die Sakramentenordnung, Landeseite zum Schreiben: `https://www.cultodivino.va/en/attivita/2026/request-for-an-indult-concerning-the-possibility-of-entrusting-t.html` – bestätigt Datum 17. Juni 2026 und Gegenstand (Indultantrag).
        
    *   Englische Fassung des Schreibens Prot. N. 276/26: `https://www.cultodivino.va/content/dam/cultodivino/attivit%C3%A0/2026/276-26/276_26-Presidente-Conferenza-Episcopale-Tedesca-ENG.pdf` – Volltext abgerufen und ausgewertet.
        
    *   Deutsche Original-PDF (gleicher Pfad, `…-GER.pdf`) lieferte **keinen extrahierbaren Inhalt** (siehe Finding M-06).
        
    *   Deutsche Bischofskonferenz, Brief an Kardinal Roche: `https://www.dbk.de/fileadmin/redaktion/diverse_downloads/dossiers_2026/2026-06-23_Brief-VOR_Dikasterium-fuer-Gottesdienst-und-Sakramentenordnung_Predigtordnung_30-03.pdf` – Volltext abgerufen und ausgewertet.
        
6.  **Keine** Testausführung, **keine** Nutzung einer Testinstanz, **keine** lokale PDF-Werkzeugkette (pdftotext/qpdf/pdffonts standen mir nicht zur Verfügung); die PDF-Prüfungen erfolgten über Abruf-Extraktion und Strukturanalyse des Git-Objekts.
    

* * *

## 4. Bewertung nach Prüfauftrag (A bis F)

**A – Anforderungsabdeckung.** Die drei Testfälle decken die einschlägigen Anforderungen sachgerecht ab, und die Negativfälle sind sinnvoll gewählt. T-01 trifft US-27/FANF-33/RANF-06 einschließlich der ausdrücklichen OCR-Grenze; T-02 trifft US-03/US-10/FANF-05/FANF-08/FANF-16/FANF-32 und operationalisiert die seit F-14 geforderte Lesepflicht; T-03 trifft US-04/US-13/US-15/US-16, FANF-03/FANF-07/FANF-22 sowie GR-03. Die Negativfälle prüfen zusätzlich FANF-09, GR-01/GR-02/GR-16/GR-18 und NFANF-03/NFANF-11. Es werden **keine** Anforderungen über die Baseline hinaus erhoben; die Fixierung erfolgt ausschließlich über synthetische oder öffentlich-amtliche Quellen, was RANF-03/SP-01/DAT-01 entspricht. Nicht ausdrücklich mit IDs versehen sind die Negativfälle – siehe Abschnitt 8, Anmerkung 1 (keine Baseline-Änderung erforderlich).
**B – Testdaten und Prüforakel.** Die Testdaten sind reproduzierbar (Bezug auf einen festen Commit), synthetisch und hinreichend anspruchsvoll. Entscheidend ist, dass die Erwartungswerte **nicht aus Modellwissen ableitbar** sind: „KELCH-29", „22. April 2032", „violett", „FIRN-46", „SCAN 481" sind frei erfunden und nur über die bereitgestellten Dateien erreichbar. Das Orakel ist vor der Ausführung fixiert (`NOT_RUN`), nennt Seiten bzw. Abschnitte und schließt nachträgliches Anpassen an beobachtete Antworten ausdrücklich aus. Beide PDFs sind technisch geprüft (siehe Abschnitt 3 Nr. 3 und 4); die im Orakel behaupteten Werte stimmen mit dem tatsächlichen PDF-Inhalt überein. Die inhaltliche Konsistenz von Predigt und Fachquelle ist gegeben: Die Predigt vertauscht in P2 tatsächlich Priester und Samariter, P3 enthält tatsächlich die werkegerechte Zusage; das Fachpapier ist als fiktiv gekennzeichnet und nennt in Abschnitt B die für die Reichweite entscheidende Einschränkung. Einzige Unschärfen: M-01, M-03, M-05.
**C – Diagnostische Aussagekraft.** Ja. Die Planung trennt die Fehlerklassen ausdrücklich in (a) Datei/Extraktion, (b) Retrieval/Modellkontext, (c) Werkzeugaktivierung/Abruf, (d) Quellen- und Fachurteil, und überlässt unklare Ursachen ausdrücklich der Kennzeichnung als unklar. Die Trennung „technische Quellenlektüre" von „inhaltlich korrekter Quellenverwendung" ist angemessen umgesetzt: T-01 prüft Bereitstellung/Extraktion von PDF, T-02 die kombinierte Nutzung von Nutzerdokument und Knowledge-Quelle im selben Lauf einschließlich der entscheidenden Kontextpassage B, T-03 den autonomen amtlichen Abruf. Die in `COMPONENT_INVENTORY.md` dokumentierten Vorläuferprobleme (unvollständige PDF-Bereitstellung, nicht zuverlässige integrierte Lektüre, ausgefallene autonome Websuche, unbelegte amtliche Quellenzuordnung) werden von genau diesen Prüffällen adressiert. Der Kontext-Orakel-Ansatz in T-02 ist das treffende Instrument gegen die in F-14 beanstandete Praxis, Treffer ohne Kontextprüfung zu verwerten.
**D – Bewertungskriterien.** Die Stufen sind definiert und mit dem PO-freigegebenen Nachweisschema des Abnahmeprofils kompatibel; `FAIL` schließt die „fälschlich behauptete Lektüre/Verifikation" ausdrücklich ein, `PASS` verlangt Sollpunkte **plus** Ausführungsnachweis. Die Lauf-Vorlage hält zusätzlich fest, dass eine bloße Modell-Selbstauskunft kein technischer Nachweis ist, und sieht den Lauf mit `NOT_RUN` im Ausgangszustand vor. Ein systematischer Falsch-PASS ist damit nicht angelegt. Zwei Restpunkte: das Verhältnis von `BLOCKED` zu den Negativfällen (M-02) und ein nicht ausdrücklich ausgeschlossener Bezugsweg über das öffentliche Repository (M-05).
**E – Praktische Durchführbarkeit.** Die Tests sind mit vorhandenen Open-WebUI-Mitteln durchführbar: PDF-Anhang und Extraktion (T-01), Nutzerdokument plus dedizierte Knowledge-Sammlung (T-02), aktivierte bzw. deaktivierte Websuche/Abruf (T-03). Es werden keine neue Pipe, kein Dienst, keine Datenbank und keine zusätzliche Implementierung vorausgesetzt; der Plan schließt dies ausdrücklich aus. Zwei Vorbedingungen sind zu protokollieren, nicht zu ändern: die Abwählbarkeit der Knowledge-Sammlung für den Negativfall und die Umstellung der Webfunktion für T-03-N (beide sind im Protokoll als „aktivierte Tools/Konfiguration" vorgesehen). Die Beweislage kann begrenzt sein, wenn die Plattform die Extraktionsansicht nicht zeigt; dafür greift die Stufung des Orakels: kein `PASS` ohne Nachweis, aber `PARTIAL` bei korrekter Antwort ohne vollständigen Bereitstellungsnachweis.
**F – Fachliche und rechtliche Korrektheit (Schwerpunkt T-03).** Geprüft und **bestätigt**:

*   can. 766 der abgerufenen deutschen Fassung: Zulassung von Laien zur Predigt in Kirche oder Kapelle „nach Maßgabe der Vorschriften der Bischofskonferenz und vorbehaltlich von can. 767 § 1" – deckungsgleich mit dem Orakel.
    
*   can. 767 § 1: „Unter den Formen der Predigt ragt die Homilie hervor, die Teil der Liturgie selbst ist und dem Priester oder dem Diakon vorbehalten wird" – deckungsgleich mit dem Orakel; die geforderte Unterscheidung von Predigt und Homilie ist damit amtlich belegt.
    
*   Schreiben Prot. N. 276/26 vom 17. Juni 2026: Es stellt fest, dass **keine** Dispens durch Indult von can. 767 § 1 erteilt werden kann, und lehnt die Unterscheidung zwischen „Homilie" und einer Laien übertragenen „Predigt" ausdrücklich ab, weil Ort (unmittelbar nach dem Evangelium) und Funktion mit der Homilie übereinstimmen; es verweist u. a. auf Redemptionis Sacramentum Nr. 64–66, GIRM Nr. 66 und can. 766. Die Sollangaben des Orakels – Ablehnung des Indults, Unbeachtlichkeit der bloßen Umbenennung, Vorbehalt der Homilie – sind damit **inhaltlich tragfähig**.
    
*   Brief der Deutschen Bischofskonferenz, Bonn, 30. März 2026 (AZ PA V 3027/26): verifiziert als **Bitte um Erteilung eines Indults**, ausdrücklich als Empfehlung der Bischofskonferenz und nicht als Normsetzung. Die Kennzeichnung im Orakel und in `tests/fixtures/t03/README.md` („Antrag ist keine Normsetzung/Genehmigung") ist korrekt.
    
*   Der normative Vorbehalt des Orakels (Rechtsstand am Ausführungstag erneut prüfen) ist sachgerecht und entspricht FANF-22.
    
*   T-02: Der Hinweis, dass die Fachquelle synthetisch ist und keine homiletische Autorität beansprucht, ist im Fixture selbst, im Orakel und in der Predigtkennzeichnung konsistent umgesetzt; die P3-Passage wird nicht als lehramtliche Feststellung, sondern als zu markierender unbegründeter Schluss behandelt – das entspricht GR-05/GR-13.
    

* * *

## 5. Findings

**Keine BLOCKER, keine MAJOR.** Sechs MINOR-Befunde, sämtlich Spezifizierungs- bzw. Nachweisschärfungen ohne Eingriff in die Prüflogik.

### M-01 | MINOR | `tests/oracles/T01-T03_ORACLES.md`, Abschnitt T-01-N

*   **Beobachtung:** Das Orakel regelt den PASS-Fall („ohne belegten OCR-/Visionzugang keine erfundene Textlektüre behauptet und die Grenze genannt") und erlaubt eine „korrekt belegte visuelle Lesung". Es regelt nicht, wie eine **behauptete** visuelle Lesung **ohne** beobachtbaren Bildzugang zu bewerten ist.
    
*   **Nachweis:** Volltext des Orakels, Abschnitt T-01-N. Die Lauf-Vorlage enthält nur die allgemeine Regel, dass eine bloße Selbstauskunft „ich habe gelesen" kein technischer Nachweis ist.
    
*   **Auswirkung:** Der Fehlerpfad, den T-01-N überhaupt prüft (unbelegte Lektürebehauptung bei nicht lesbarer Quelle), bleibt im Einzelorakel unbewertet. Ein Tester kann eine Sichtlesungsbehauptung ohne Evidenz als PASS protokollieren.
    
*   **Korrektur (kleinste):** Ein Satz in T-01-N: „Eine behauptete visuelle Lesung ohne beobachtbaren Bildzugang oder gleichwertige Evidenz gilt als unbelegte Lektürebehauptung und ist als `FAIL` zu bewerten."
    

### M-02 | MINOR | `tests/oracles/T01-T03_ORACLES.md`, Abschnitt „Ergebnisbeurteilung" im Verhältnis zu T-01-N, T-02-N, T-03-N

*   **Beobachtung:** `BLOCKED` ist definiert als „Test nicht durchführbar (Provider/Tool/Dokument nicht verfügbar)". In den drei Negativfällen ist die fehlende Fähigkeit (kein OCR/Visionzugang, Fachquelle nicht freigegeben, Webzugang deaktiviert) jedoch die **vorgesehene** Ausgangslage und wird dort als PASS gewertet.
    
*   **Nachweis:** Wortlaut der Ergebnisbeurteilung gegen die Abschnitte T-01-N, T-02-N, T-03-N.
    
*   **Auswirkung:** Zwei Auslegungen sind möglich – derselbe Lauf kann `PASS` oder `BLOCKED` erhalten. Das erschwert die Vergleichbarkeit der Protokolle und die Fehlerzuordnung nach Kategorie (c).
    
*   **Korrektur (kleinste):** Ein Satz vor der Tabelle: „In T-01-N, T-02-N und T-03-N ist die fehlende Fähigkeit die vorgesehene Bedingung; `BLOCKED` gilt dort nur, wenn der Fall nicht durchgeführt werden konnte."
    

### M-03 | MINOR | `docs/testing/T01-T03_DIAGNOSTIC_PLAN.md`, §2 (Zeile T-02-P, Spalte „Nachweise") gegen `tests/oracles/T01-T03_ORACLES.md`, T-02-P Nr. 5

*   **Beobachtung:** Der Plan verlangt eine „konkrete Bewertung der Predigtstellen **P1–P5**"; das Orakel verlangt Fundstellen „**P2/P3/P4**" und beschreibt P1; P5 ist dort nicht als erforderlich benannt.
    
*   **Nachweis:** Wortlaut beider Stellen im Volltext.
    
*   **Auswirkung:** Zwei Prüfreichweiten für denselben Fall. Ein Tester kann das Fehlen einer P5-Bewertung als Sollmangel protokollieren und ein falsches `PARTIAL` erzeugen.
    
*   **Korrektur (kleinste):** Angleichung – im Orakel „P1/P2/P3/P4" nennen und P5 als nicht bewertungsrelevant kennzeichnen, oder im Plan auf P1–P4 verkürzen.
    

### M-04 | MINOR | `tests/oracles/T01-T03_ORACLES.md`, Abschnitt T-03-P, „Soll gemäß dokumentierter Quellenlage"

*   **Beobachtung:** `PASS` ist an „alle für den jeweiligen Testfall definierten Sollpunkte" gebunden. Das Soll umfasst fünf Bullets, darunter die Indult-Ablehnung vom 17.06.2026 sowie der Hinweis auf lokales/diözesanes Recht. Welche Punkte PASS-kritisch sind, ist nicht kenntlich.
    
*   **Nachweis:** Wortlaut T-03-P; Definition `PASS` in der Ergebnisbeurteilung.
    
*   **Auswirkung:** Ein inhaltlich richtiges und quellenbelegtes Ergebnis (can. 767 § 1, keine Laienhomilie unmittelbar nach dem Evangelium) ohne Kenntnis des Schreibens vom 17.06.2026 wäre formal kein `PASS`. Die Bewertung hinge damit an einem Zusatzaspekt statt am Normkern – Risiko unverhältnismäßiger Bewertung.
    
*   **Korrektur (kleinste):** PASS-Kern und Zusatz ausdrücklich trennen. Kern: zutreffende Norm (can. 766 vorbehaltlich can. 767 § 1), zutreffendes Ergebnis für den konkreten Ort, Benennung von amtlicher Quelle, Datum und Fundstelle. Zusatz (dokumentierte, nicht PASS-kritische Differenzierung): Indult-Historie und DBK-Vorgang.
    

### M-05 | MINOR | `tests/oracles/T01-T03_ORACLES.md` (Werte T-01) und `tests/fixtures/t01/README.md` im Verhältnis zu `docs/testing/T01-T03_DIAGNOSTIC_PLAN.md` §3 Nr. 5

*   **Beobachtung:** Die Erwartungswerte („KELCH-29", „22. April 2032", „violett", „FIRN-46", „SCAN 481") stehen im öffentlichen Repository; `tests/fixtures/t01/README.md` verweist ausdrücklich auf `tests/oracles/T01-T03_ORACLES.md`. T-03-P verlangt aktivierten Webzugriff. Werden T-01/T-02 in derselben Konfiguration gefahren, ist ein Abruf der Orakel- bzw. Fixture-Dateien aus dem Repository technisch möglich.
    
*   **Nachweis:** Orakel- und Fixture-Datei im selben öffentlichen Repository; die Lauf-Vorlage erfasst URLs, schließt einen solchen Abruf aber nicht aus. Das Orakel T-01-P verlangt faktisch einen Extraktionsnachweis, benennt den Repo-Bezugsweg jedoch nicht als Ausschlussgrund.
    
*   **Auswirkung:** Ein Lauf, der die Werte aus dem Repository statt aus der bereitgestellten Datei bezieht, kann bei oberflächlicher Protokollführung als Lektürenachweis gelesen werden. Damit wäre der Kernnachweis von T-01/T-02 umgehbar – ein Falsch-PASS-Pfad, der im Protokoll nicht zwingend auffällt.
    
*   **Korrektur (kleinste):** T-01 und T-02 ohne externen Webzugriff fahren (Konfigurationsentscheidung, keine Implementierung) **oder** in Orakel und Lauf-Vorlage einen Satz aufnehmen: „Ein Abruf von Orakel-, Fixture- oder Repository-Dateien gilt nicht als Lektürenachweis; der Lauf ist in diesem Fall ungültig."
    

### M-06 | MINOR | `tests/oracles/T01-T03_ORACLES.md`, T-03-P Quellenliste Nr. 2; `tests/fixtures/t03/README.md`

*   **Beobachtung:** Die dort verlinkte deutsche Original-PDF des Schreibens Prot. N. 276/26 lieferte bei meinem Abruf keinen extrahierbaren Inhalt; die englische Fassung am gleichen Pfad lieferte den Volltext. Die Angabe „besonders PDF-Seiten 1, 3 und 4" konnte ich deshalb nicht überprüfen (die englische Fassung umfasst fünf Seiten).
    
*   **Nachweis:** Abruf der beiden Sprachfassungen im selben Verzeichnis (siehe Abschnitt 3 Nr. 5). Die Ursache – Dateiname, Zugriffsbeschränkung oder fehlende Textebene – ließ sich mit meinen Mitteln nicht bestimmen; die Feststellung ist daher als Risiko, nicht als Fehler gewertet.
    
*   **Auswirkung:** Die Prüferreferenz enthält einen Link, der in meiner Umgebung nicht belastbar ist; eine Seitenangabe im Orakel stützt sich auf ein von mir nicht verifizierbares Dokument.
    
*   **Korrektur (kleinste):** Link und Seitenangabe vor dem Lauf prüfen; die englische Fassung als belegte Ausweichreferenz aufnehmen; die Abrufbarkeit der deutschen Original-PDF im Protokoll vermerken.
    

* * *

## 6. Positive Befunde (tatsächlich geprüft)

1.  **Erwartungswerte sind nicht aus Modellwissen ableitbar.** Alle Schlüsselwerte in T-01 und T-02 sind frei erfunden; die Antwort kann nur aus der bereitgestellten Datei bzw. Knowledge-Quelle stammen. Damit ist der in `COMPONENT_INVENTORY.md` dokumentierte Fehlerpfad (Antwort aus Modellwissen statt Originallektüre) konstruktiv adressiert.
    
2.  **Distraktoren verhindern bequemes Erfüllen.** Seite 5 stellt ausdrücklich fest, dass „FELS-12 kein Abschlusskennwort" ist; Seite 4 enthält „absichtlich keinen neuen Termin"; Seite 2 hält fest, dass die Registrierkennung dort nicht wiederholt wird. Ein Treffer-zufällig-richtig-Szenario wird dadurch sichtbar.
    
3.  **Eindeutige Seitenzuordnung.** Jede Seite der sechsseitigen PDF trägt die Fußzeile „PDF-Seite N von 6 | SYN-T01-PDF-01"; `tests/fixtures/t01/README.md` hält fest, dass nur die PDF-Seitenzahlen zählen und keine Druckseiten. Das entspricht der Regel in DAT-02, PDF-Seite und Druckseite nicht gleichzusetzen.
    
4.  **Beide PDFs sind technisch korrekt für ihren Zweck.** `document_six_pages.pdf` ist textbasiert und in allen sechs Seiten auslesbar; die Orakelwerte stimmen seitenweise exakt. `image_only.pdf` hat eine Seite, keine Font-Ressource und keinen Textoperator – der Seiteninhalt zeichnet ausschließlich das Rasterbild. Die Negativprobe prüft damit wirklich ehrliches Fehlermanagement und keine OCR-Pflicht; das entspricht der RANF-06-Grenze und der Klarstellung im Diagnoseplan.
    
5.  **T-02 setzt die Schließung von F-14 operativ um.** Die erforderliche Kontextstelle B ist synthetisch und nicht erratbar; das Orakel erklärt ausdrücklich, dass ein Lauf ohne die für die Bewertung relevante Passage B kein `PASS` erhält. Das ist die passende Umsetzung der Pflicht aus FANF-05, Bedingungen und Einschränkungen im Textzusammenhang zu lesen.
    
6.  **Die Fixture-Inhalte passen exakt zu den Orakelangaben.** Die Rollenvertauschung in P2 (Priester hilft, Samariter geht vorbei) und der werkegerechte Schluss in P3 stehen wortgleich so im Predigttext; das Fachpapier ist im Kopf ausdrücklich als fiktiv und „nicht Wolfgang Klippert" gekennzeichnet und verlangt in Abschnitt D selbst die Offenlegung seiner Grenzen.
    
7.  **T-03 ist fachlich und rechtlich tragfähig.** can. 766 und can. 767 § 1 wurden am amtlichen Wortlaut bestätigt; das Schreiben Prot. N. 276/26 vom 17.06.2026 stellt die Unmöglichkeit eines Indults und die Unbeachtlichkeit der Umbenennung ausdrücklich fest; der DBK-Brief vom 30.03.2026 ist verifiziert eine Bitte um Indult und keine Normsetzung. Die Unterscheidung von Predigt und Homilie ist damit amtlich gedeckt und im Orakel korrekt abgebildet.
    
8.  **Bewertungslogik ist gegen Falsch-PASS abgesichert.** `PASS` verlangt Sollpunkte plus Ausführungsnachweis; `FAIL` umfasst ausdrücklich die fälschlich behauptete Lektüre; die Lauf-Vorlage verwirft die bloße Selbstauskunft als Nachweis; der Ausgangszustand ist `NOT_RUN`. Eine richtige Antwort aus Modellwissen ist für T-03 ausdrücklich als nicht ausreichend erklärt.
    
9.  **Keine Überzeichnung des Ergebnisses.** Der Plan stellt ausdrücklich fest, dass aus T-01 bis T-03 keine Produkt- oder MVP-Freigabe folgt und T-04 bis T-08 separate Abnahmefälle bleiben. Das deckt sich mit der Regel des Abnahmeprofils und mit `WORKFLOW.md` (kein grüner Lauf als Abnahme).
    
10.  **Änderungsdisziplin.** Fixierte Orakel dürfen nicht an beobachtete Antworten angepasst werden; Änderungen nur über einen neuen Commit. Der Umfang des Commits (neun neue Dateien, keine Änderung an bestehenden Dateien) stützt diese Trennung.
     
11.  **Fehlerzuordnung und Trennung der Ebenen.** Die vier Fehlerkategorien des Plans und die Zwei-Ebenen-Regel des Abnahmeprofils (technisch nachgewiesene Lektüre gegen inhaltliche Tragfähigkeit der Zuschreibung) sind konsistent und in der Lauf-Vorlage abgefragt.
     

* * *

## 7. Gesamturteil

**Freigabefähig mit Hinweisen.**
Das Testkonzept T-01 bis T-03 ist als erste diagnostische End-to-End-Gruppe geeignet. Es prüft die drei im Vorgängerprojekt tatsächlich aufgetretenen Fehlerpfade (unvollständige Dokumentbereitstellung, nicht nachgewiesene integrierte Originallektüre, ausgefallene autonome amtliche Recherche) mit synthetischen, nicht aus Modellwissen beantwortbaren Eingaben, fixierten Orakeln, Negativfällen und einer protokollierbaren Fehlerzuordnung. Es setzt keine Implementierung und keine zusätzliche Architektur voraus.
Kein BLOCKER und kein MAJOR-Befund. Die sechs MINOR-Hinweise M-01 bis M-06 sind vor dem ersten Lauf mit geringem Aufwand umsetzbar; M-05 und M-06 sollten wegen ihrer Wirkung auf den Nachweischarakter vorrangig behandelt werden.
Ausdrücklich festgehalten:

*   Es wurden **keine** Tests ausgeführt. Dieses Urteil betrifft ausschließlich die Eignung des Testkonzepts und ist **kein** Nachweis erfolgreich ausgeführter End-to-End-Tests.
    
*   Die Baseline v1.2.0 wurde nicht erneut geprüft; sie ist PO-freigegeben. Die offenen Punkte F-01 (Qualitätsgrenzwerte) und F-18 (verbindliche Fachstandardfassung) bleiben unberührt.
    
*   Dieses Urteil ist eine Empfehlung. Die fachliche Freigabe des Testkonzepts obliegt ausschließlich dem Product Owner.
    

* * *

## 8. Offene Fragen, Anmerkungen und nicht verifizierte Punkte

**Anmerkungen (keine Nacharbeit verlangt):**

1.  Die Negativfälle sind im Plan nicht mit Anforderungs-IDs versehen; ihre Deckung ergibt sich aus dem Abnahmeprofil. Eine Referenzspalte im Plan wäre hilfreich, erfordert aber keine Änderung an der Baseline.
    
2.  Der Dateiname des DBK-Briefes trägt „2026-06-23", das Schreiben selbst ist auf den 30.03.2026 datiert. Die Orakelangabe „Brief vom 30. März 2026" ist korrekt; die Abweichung dürfte das Veröffentlichungsdatum betreffen und ist im Protokoll zu unterscheiden.
    
3.  Die abgerufene deutsche CIC-Fassung kennzeichnet can. 767 mit einem Asteriskus (Änderungshinweis). Die Bedeutung habe ich nicht geprüft; für die im Orakel geforderte Fassungsangabe ist sie im Protokoll zu vermerken.
    
4.  T-02-N und T-03-N setzen eine Änderung der Testkonfiguration voraus (Knowledge-Sammlung abwählbar, Webfunktion deaktiviert). Beides ist mit den vorhandenen Mitteln möglich, muss aber im Protokoll als Konfiguration des Laufs dokumentiert werden, weil es die Aussagekraft des jeweiligen Laufs bestimmt.
    

**Nicht verifiziert (keine Bewertung möglich):**  
5. Der **Rasterinhalt** von `image_only.pdf` (angeblich „SCAN 481"): Das Bild ist 47 × 7 Pixel groß und wird auf 465 × 90 Punkt skaliert. Ob die Zeichenfolge für ein bildfähiges Modell tatsächlich lesbar ist, kann nur der Lauf zeigen. Das Orakel ist darauf nicht angewiesen, weil es beide Ausgänge zulässt (keine erfundene Lektüre bzw. belegte visuelle Lesung) – die Bewertungslogik bleibt davon unberührt.  
6. **Plattformverhalten** in der konkreten Open-WebUI-Konfiguration: Sichtbarkeit der Extraktionsansicht bei Chat-Anhängen, Verhalten des Knowledge-Retrievals bei der Kontextstelle B, tatsächliche Weiterleitung von Bildinhalten an das Modell. Nur im Lauf feststellbar; der Plan behandelt die fehlende Sichtbarkeit bereits korrekt („kein PASS" ohne Nachweis, `PARTIAL` bei korrekter Antwort ohne vollständigen Bereitstellungsnachweis).  
7. **Deutsche Original-PDF** des Schreibens Prot. N. 276/26 und die darin genannten PDF-Seiten 1, 3 und 4 (siehe M-06).  
8. **Grenze der eigenen Prüfung:** Meine technische Prüfung der PDFs erfolgte über Abruf-Extraktion bzw. Strukturanalyse des Git-Objekts, nicht mit einer lokalen PDF-Werkzeugkette. Tiefer gehende Prüfungen (Schriftprogramme, XRef-Konsistenz, Rendering) wurden nicht vorgenommen.
**Entscheidungsrelevante offene Fragen an den Product Owner bzw. Software Engineer:**

1.  Sollen T-01 und T-02 ohne externen Webzugriff gefahren werden (M-05), um den Bezugsweg über das öffentliche Repository auszuschließen?
    
2.  Welche Sprachfassung des Schreibens Prot. N. 276/26 dient als maßgebliche Prüferreferenz, wenn die deutsche Original-PDF nicht abrufbar ist (M-06)?
    
3.  Soll T-02 bis zur Klärung der Nutzungsrechte bei der synthetischen Fachquelle bleiben, wie im Abnahmeprofil vorgesehen („später reale Fachquelle nur bei geklärten Nutzungsrechten")? Das berührt F-18 und die spätere Qualitätsabnahme.
    
4.  Sollen die Hinweise M-01 bis M-06 vor dem ersten Lauf eingearbeitet werden, oder wird das Konzept in der vorliegenden Fassung ausgeführt und die Hinweise nur im Protokoll berücksichtigt? Beides ist vertretbar; M-05 sollte nicht offen bleiben, weil er den Nachweischarakter der Tests betrifft.
    

* * *

## 9. Beleglage (Quellen dieses Berichts)

| Gegenstand | Quelle |
| --- | --- |
| Prüf-Commit | `https://github.com/baem-oss/THEOAgent/commit/fec545c56f388c1b611c96a6120bf5d273e9ae69` |
| Branch | `https://github.com/baem-oss/THEOAgent/tree/test/t01-t03-diagnostics-v1` |
| Diagnoseplan | `docs/testing/T01-T03_DIAGNOSTIC_PLAN.md` (Commit `fec545c`) |
| Prüforakel | `tests/oracles/T01-T03_ORACLES.md` (Commit `fec545c`) |
| Testprotokoll-Vorlage | `tests/runs/T01-T03_RUN_TEMPLATE.md` (Commit `fec545c`) |
| Fixtures T-01 (Text-PDF, Raster-PDF, README) | `tests/fixtures/t01/` (Commit `fec545c`) |
| Fixtures T-02 (Predigt, Fachpapier) | `tests/fixtures/t02/` (Commit `fec545c`) |
| Fixture T-03 (README) | `tests/fixtures/t03/README.md` (Commit `fec545c`) |
| Baseline v1.2.0 | `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/requirements/BASELINE.md` |
| Abnahmeprofil v1.2.0 | `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/requirements/ACCEPTANCE_PROFILE.md` |
| Traceability v1.2.0 | `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/requirements/TRACEABILITY.md` |
| Bestandsaufnahme | `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/architecture/COMPONENT_INVENTORY.md` |
| Arbeitsregeln | `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/WORKFLOW.md` |
| can. 766, can. 767 § 1 (deutsch) | `https://www.vatican.va/archive/cod-iuris-canonici/deu/documents/cic_libro3_cann762-772_ge.html` |
| Schreiben Prot. N. 276/26, 17.06.2026 (Landeseite) | `https://www.cultodivino.va/en/attivita/2026/request-for-an-indult-concerning-the-possibility-of-entrusting-t.html` |
| Schreiben Prot. N. 276/26, englische Fassung | `https://www.cultodivino.va/content/dam/cultodivino/attivit%C3%A0/2026/276-26/276_26-Presidente-Conferenza-Episcopale-Tedesca-ENG.pdf` |
| DBK-Brief vom 30.03.2026 | `https://www.dbk.de/fileadmin/redaktion/diverse_downloads/dossiers_2026/2026-06-23_Brief-VOR_Dikasterium-fuer-Gottesdienst-und-Sakramentenordnung_Predigtordnung_30-03.pdf` |

**Methodenhinweis:** Alle Feststellungen beruhen auf im Volltext abgerufenen Repository-Dateien am genannten Commit bzw. auf den abgerufenen amtlichen Quellen – nicht auf Patch-Darstellungen, Chat-Texten oder Zusammenfassungen. Es wurden keine Tests ausgeführt; es werden keine PASS-Aussagen Dritter übernommen. Der Prüfgegenstand ist der Commit `fec545c`, nicht der aktuelle Stand von `main`.