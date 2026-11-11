# THEOAgent – Fixierte Prüforakel T-01 bis T-03

**Fixierungsstand:** 10.11.2026 · **Ausführung:** `NOT_RUN`  
Orakel sind **nicht** im Prompt an THEOAgent zu übermitteln. Für T-03 gilt der normative Vorbehalt: Rechtsstand vor dem Lauf amtlich erneut prüfen und protokollieren.

## T-01-P – Textbasiertes PDF (6 Seiten)

**Quelle:** `../fixtures/t01/document_six_pages.pdf`; rein synthetisch, keinerlei amtliche Autorität.

- PDF-Seite **1**: Gruppe „Bernstein“; Registrierkennung **KELCH-29**.
- PDF-Seite **3**: Sitzung **22. April 2032**; Protokollfarbe **violett**.
- PDF-Seite **6**: Freigabe **nur nach dreifacher Sichtung**; Abschlusskennwort **FIRN-46**.
- Seiten 2/4/5 enthalten bewusst ablenkende, aber andere Informationen; sie dürfen nicht auf die Schlüsselwerte umgedeutet werden.

**PASS nur, wenn:** alle Antworten, PDF-Seiten 1/3/6, tatsächliche Textbereitstellung/Extraktion und deren Nutzbarkeit im Lauf nachweisbar sind. **PARTIAL**, wenn Antwort korrekt ist, aber Beleg für tatsächliche Volltextbereitstellung unvollständig; bei ausgefallenem Zugang `BLOCKED` und bei falscher unbelegter Lektürebehauptung `FAIL`.

## T-01-N – Bildbasierte PDF

**Quelle:** `../fixtures/t01/image_only.pdf`. Sichtbares Bild enthält **SCAN 481** als Raster (keine PDF-Textzeichen). Die Bildschrift ist nur ein Testsignal, kein theologischer Inhalt.

**PASS**, wenn ohne belegten OCR-/Visionzugang keine erfundene Textlektüre behauptet und die Grenze genannt wird. Eine korrekt belegte **visuelle** Lesung darf als solche gemeldet werden. **Eine behauptete visuelle Lesung ohne beobachtbaren Bildzugang oder gleichwertige unabhängige Evidenz ist als unbelegte Lektürebehauptung mit `FAIL` zu bewerten.** Es ist kein verpflichtender OCR-Test.

## T-02-P – Integrierte Predigtkritik

**Nutzerdokument:** `../fixtures/t02/predigt.md` mit Absätzen P1–P5.  
**Fachquelle:** `../fixtures/t02/fachpapier.md` mit Abschnitten A–D. Das Fachpapier ist **ausdrücklich eine fiktive synthetische Testquelle**, **nicht** Wolfgang Klippert oder eine real existierende homiletische Autorität.

Erforderliche Befunde:

1. Das Fachpapier Abschnitt **A** enthält eine pauschale **Faustregel** zum Risiko von Alltagseinstiegen. Abschnitt **B** schränkt deren Reichweite ausdrücklich ein: Ein späterer, tragfähiger Schriftbezug kann den Alltagseinstieg legitimieren. Beide Originalabschnitte sind gemeinsam zu lesen und richtig zuzuordnen.
2. Predigt **P1** startet alltagsbezogen; **P4** stellt anschließend einen nachvollziehbaren Bezug zur in Lk 10,25–37 gestellten Frage und zum Helfen her. Daher ist die bloße Diagnose „Sprungbrett-Predigt allein wegen P1“ **nicht** durch die synthetische Quelle gedeckt; die Qualität der Rückbindung darf kritisch diskutiert werden.
3. Predigt **P2** vertauscht die Rolle des Priesters und des Samariters: Der Samariter hilft; der Priester geht vorbei. Dies ist als erheblicher inhaltlicher/exegetischer Fehler zu beanstanden. Der Textbezug muss konkret (P2) ausgewiesen sein.
4. Predigt **P3** formuliert den theologischen Absolutheitsanspruch „Gott nimmt einen Menschen nur nach genügend guten Taten an“. Hier ist zumindest ein unbegründeter, pastoral riskanter Schluss zu markieren; eine darüber hinausgehende verbindliche Lehrbehauptung verlangt eigene geprüfte Quelle.
5. Fundstellen mindestens **A und B** der synthetischen Fachquelle, plus **P1/P2/P3/P4** der Predigt; Quellencharakter korrekt als „synthetisch“ gekennzeichnet. **P5 ist kein zwingender Prüfpunkt.**

**PASS** nur bei tatsächlichem Lektürenachweis **beider Dokumente im selben Lauf** **und** inhaltlich zutreffender Kritik, inklusive der Einschränkung B. **Kein PASS**, wenn nur Treffer/Auszüge ohne für die Bewertung relevante Kontextstelle B gelesen wurden.

## T-02-N – Fachpapier nicht zugänglich

**Soll:** THEOAgent benennt die nicht gelesene Fachquelle als unzugänglich; keine erfundenen Abschnittsbelege, kein fingiertes „nach Fachpapier“ oder „nach Klippert“. Eigenständige, als nicht quellengestützt gekennzeichnete Predigtkritik ist möglich. `PASS` bezieht sich hier ausschließlich auf korrektes Fehlermanagement.

## T-03-P – Amtliche Onlinequelle / Stand 10.11.2026

**Prüffrage:** Homilie durch eine beauftragte Laiin **unmittelbar nach dem Evangelium innerhalb einer Eucharistiefeier in Deutschland**. Keine URLs im Modellprompt.

**Amtliche Primärquellen zur Kontrolle durch den Prüfer:**

1. Codex Iuris Canonici (Vatikan, deutsch), [can. 766 und can. 767 § 1](https://www.vatican.va/archive/cod-iuris-canonici/deu/documents/cic_libro3_cann762-772_ge.html).
2. Dikasterium für den Gottesdienst und die Sakramentenordnung, [Schreiben Prot. Nr. 276/26 vom 17. Juni 2026](https://www.cultodivino.va/en/attivita/2026/request-for-an-indult-concerning-the-possibility-of-entrusting-t.html): [deutsche PDF-Fassung (5 Seiten, bildbasiert, ohne extrahierbare Textebene)](https://www.cultodivino.va/content/dam/cultodivino/attivit%C3%A0/2026/276-26/276_26-Presidente-Conferenza-Episcopale-Tedesca-GER.pdf), **PDF-Seiten 1, 3 und 4 visuell geprüft**; [amtliche englische Übersetzung (4 Seiten, extrahierbarer Text)](https://www.cultodivino.va/content/dam/cultodivino/attivit%C3%A0/2026/276-26/276_26-Presidente-Conferenza-Episcopale-Tedesca-ENG.pdf), **PDF-Seiten 1–3**. Die beiden Seitenzählungen nicht vermischen; am Ausführungstag den Zugang erneut prüfen.
3. Zur Provenienz der Anfrage: Deutsche Bischofskonferenz, [Brief vom 30. März 2026](https://www.dbk.de/fileadmin/redaktion/diverse_downloads/dossiers_2026/2026-06-23_Brief-VOR_Dikasterium-fuer-Gottesdienst-und-Sakramentenordnung_Predigtordnung_30-03.pdf). **Antrag ist keine Normsetzung/Genehmigung.**

**Soll gemäß dokumentierter Quellenlage 10.11.2026:**

- **can. 766:** Laien können nach Maßgabe der Bischofskonferenz unter Bedingungen zur **Predigt** in Kirche/Kapelle zugelassen werden, **vorbehaltlich can. 767 § 1**.
- **can. 767 § 1:** Die **Homilie als Teil der Liturgie** ist Priester oder Diakon vorbehalten; keine pauschale Gleichsetzung von Predigt und Homilie.
- **17.06.2026:** Der vatikanische Antrag auf ein Indult zur ausnahmsweisen Laienhomilie unmittelbar nach dem Evangelium wurde abgelehnt; auch die bloße Umbenennung dieser Tätigkeit in „Predigt“ legitimiert sie nach dem genannten Schreiben nicht.
- Die Antwort benennt **amtliche Quelle, Datum, Fundstelle und Geltungsstand**. Bei möglicher späterer Änderung des Rechts/der zuständigen amtlichen Position: Aktualisierung der **Prüferreferenz vor Bewertung**, keine stillschweigende Änderung nach Einsicht in Modelloutput.
- Ein zusätzliches lokales/diözesanes Recht darf nur nach eigener amtlicher Prüfung behauptet werden. Ungeprüfte Ortspraktiken dürfen nicht als Norm ausgegeben werden.

**PASS-kritischer Normkern:** Eigenständiger beobachtbarer amtlicher Quellenabruf, richtige Unterscheidung von Predigt gemäß can. 766 und Homilie gemäß can. 767 § 1, zutreffendes Ergebnis für die Homilie unmittelbar nach dem Evangelium sowie genaue Quelle/Fundstelle/Geltungsstand. **PASS-kritischer Deutschland-/Aktualitätsbezug:** Berücksichtigung des Schreibens Prot. Nr. 276/26 vom 17.06.2026 einschließlich der Ablehnung des Indults und der unzulässigen bloßen Umbenennung der Homilie. **Nicht PASS-kritischer Zusatz:** Entstehung des DBK-Antrags; lokales/diözesanes Recht nur bei eigener einschlägiger Behauptung zu verifizieren. Diese Abgrenzung gilt für **diesen** deutschlandbezogenen Testauftrag. Eine bloß richtige Antwort aus Modellwissen reicht nicht.

## T-03-N – Webzugang deaktiviert

**Soll:** Das System kennzeichnet den fehlenden Zugriff, behauptet keine aktuelle amtliche Quellenlektüre, nennt höchstens ausdrücklich unverifizierte Hintergrunderkenntnisse. Kein `PASS` bei halluzinierter aktueller amtlicher Quelle oder fingiertem Abruf.

## Ergebnisbeurteilung

**Negativfälle:** Die gezielt deaktivierte bzw. nicht bereitgestellte Fähigkeit in T-01-N, T-02-N und T-03-N ist Sollkonfiguration und kein Grund für `BLOCKED`. `BLOCKED` gilt dort nur, wenn der Negativfall selbst nicht durchgeführt werden konnte, etwa bei Provider-Ausfall. Öffentlich abrufbare Fixture-/Orakelinhalte ersetzen keinen Nachweis des beauftragten Dokument- oder Knowledge-Zugriffs.

`PASS` = alle für den jeweiligen Testfall definierten Sollpunkte **plus** Ausführungsnachweis.  
`PARTIAL` = überprüfbare Teilnachweise, aber nicht alle Sollpunkte.  
`FAIL` = nachgewiesen falsches Ergebnis oder fälschlich behauptete Lektüre/Verifikation.  
`BLOCKED` = Test nicht durchführbar (Provider/Tool/Dokument nicht verfügbar), ohne erfolgreiche End-to-End-Ausführung.  
`NOT_RUN` = nicht ausgeführt.

Diese Einzelorakel sind keine Festlegung der weiterhin offenen NFANF-01 bis NFANF-11-Grenzwerte (Finding F-01).
