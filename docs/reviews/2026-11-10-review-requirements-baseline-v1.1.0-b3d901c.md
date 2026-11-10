# Reviewbericht – THEOAgent Requirements-Baseline v1.1.0

**Prüfer:** unabhängiger technischer Reviewer / Quality Engineer (Rolle nach Auftragsdokument)
**Datum:** 2026-11-10
**Auftrag:** unabhängiger Review der THEOAgent-Requirements-Baseline v1.1.0 sowie Prüfung, ob die im Vorgängerrepository THEOBald dokumentierten technischen Rahmenbedingungen korrekt und ausreichend berücksichtigt sind.

---

## Vorbemerkung zum Zugriff

Zugriff auf die Originaldateien bestand:

- `baem-oss/THEOAgent`, Branch `main`
  - `docs/requirements/BASELINE.md` – Version 1.1.0, Stand 10.11.2026
  - `docs/requirements/TRACEABILITY.md` – Version 1.1.0
  - `README.md`
- `baem-oss/THEOBald`, Branch `main`
  - `docs/architecture.md` (ADR-0001), `docs/baseline-v1.2.0.md`, `docs/roadmap.md`,
    `docs/openwebui-setup.md`, `docs/rag-acceptance.md`, `README.md`, `skills/`

**Commit-Pinning (nachgetragen):** Geprüfter Stand ist `main` = `b3d901c8252e1ac95c8cd0cfc2dda78ea7810ab6` (Kürzel `b3d901c`, Commit-Zeit 2026-11-10T16:25:41Z). Nachträglich wurden `BASELINE.md` und `TRACEABILITY.md` erneut **am Commit `b3d901c`** abgerufen und mit dem ursprünglich geprüften Inhalt verglichen: Versionsangabe, Abschnittsstruktur, alle 27 US, alle 33 FANF samt Rückverfolgbarkeitsspalte sowie die in den Findings zitierten NFANF-, GR- und DAT-Formulierungen sind unverändert. Es wurden **keine Tests ausgeführt**; im THEOAgent-Repository existieren weder Quelltext noch Tests. Der experimentelle Branch `review/sourceguard-integrated-v0.5.5-dev3` wurde auftragsgemäß **nicht** als verbindlich behandelt.

---

## 1. Prüfgegenstand

| Punkt | Inhalt |
|---|---|
| Repository | `baem-oss/THEOAgent`, Branch `main` |
| Commit-SHA | `b3d901c8252e1ac95c8cd0cfc2dda78ea7810ab6` (Kürzel `b3d901c`), Commit-Zeit 2026-11-10T16:25:41Z |
| Geprüfte Dateien | `docs/requirements/BASELINE.md` – Git-Blob `585c99dcc0ab2dbfd1dd5bf9f9dccedc74a94a09`, 23.147 Byte, v1.1.0, Stand 10.11.2026; `docs/requirements/TRACEABILITY.md` – Git-Blob `55b1ba78675847dba06f9e05e93d554f626068d6`, 1.979 Byte, v1.1.0; `README.md` (Abruf vor `b3d901c`, siehe Abschnitt 9, N2) |
| Vollständigkeit | `docs/requirements/` enthält genau diese zwei Dateien; im Repository kein Quelltext, keine Tests, kein CI-Nachweis |
| Nicht geprüft | `docs/architecture/COMPONENT_INVENTORY.md` – Git-Blob `824b1c970db9204a1c7ee650f079792a0531f961`, 8.371 Byte, nach dem Review angelegt; nicht Gegenstand dieses Berichts, siehe Abschnitt 9, N3/N4 |
| Referenzgegenstand | THEOBald `main`: ADR-0001, `baseline-v1.2.0.md`, `roadmap.md`, `openwebui-setup.md`, `rag-acceptance.md`, `README.md`, `skills/` – **Abruf am 2026-11-10 ohne Commit-Pinning**; diese Angaben sind nicht an einen Commit gebunden (Restunsicherheit, siehe Abschnitt 9, N1) |
| Verfügbare Tests | keine |
| Tatsächlich ausgeführte Tests | keine |

Die Aufgabenteile **C (Code-Review)** und **D (Test-Review)** sind gegenstandslos – es liegt noch kein Implementierungs- oder Testartefakt vor. Die Feststellung „Implementierung und Realtests sind noch nicht abgenommen“ ist korrekt.

---

## 2. Gesamturteil

**Nicht freigabefähig – als Architektur- und Abnahmegrundlage.**
Als *fachlicher Anforderungsumfang* ist die Baseline dagegen tragfähig und in sich weitgehend konsistent.

Begründung: Die Baseline ist formal sauber (Zählungen, Typentrennung und beidseitige Traceability stimmen – siehe Abschnitt 8), sie ist aber **nicht messbar** (11 von 12 NFANF ohne Schwellenwert), für drei zentrale Fachfunktionen fehlt das Datenmodell (Arbeitsfassung/Freeze, Fundstellengranularität, Formatumfang), und ihre sicherheitskritischste Eigenschaft – keine erfundenen Fundstellen – ist nur als Fachregel, nicht als abnehmbare Qualitätsanforderung formuliert. Ein Architekturentwurf, der gegen diese Baseline „erfüllt“ werden soll, kann nicht verifiziert werden.

---

## 3. Findings

### 3.1 BLOCKER

#### F-01 | BLOCKER | BASELINE §4, NFANF-01 … NFANF-11

| Feld | Inhalt |
|---|---|
| ID | F-01 |
| Priorität | BLOCKER |
| Fundstelle | `docs/requirements/BASELINE.md`, §4 (NFANF-01 … NFANF-11), §9 |
| Befund | 11 der 12 nichtfunktionalen Anforderungen tragen als Prüfmaß „Mindestwert und Korpus offen“ bzw. „… offen“. Nur NFANF-12 ist unmittelbar messbar. |
| Nachweis | Volltextabgleich §4; §9 verschiebt Akzeptanzfälle und Grenzwerte ausdrücklich auf „vor der Implementierungsabnahme“. |
| Auswirkung | Keine Anforderung der Qualitätskategorie ist derzeit prüfbar. Weder Testableitung noch Architekturverifikation sind möglich; jede Architekturentscheidung wäre gegen einen unbestimmten Maßstab zu verteidigen. Die geforderte Typentrennung ist formal erfüllt, NFANF aber funktional leer. |
| Empfehlung | Vor Architektursign-off einen kurzen **Abnahme-Anhang** (Korpus, Bewertungsverfahren, Schwellenwert je NFANF) festlegen. Alternativ: nicht belegbare NFANF in v1.2.0 auf die abnehmbaren reduzieren. KISS: kleiner Anhang statt neuer Anforderungsstruktur. |

#### F-02 | BLOCKER | BASELINE GR-02, GR-03, NFANF-02, NFANF-11

| Feld | Inhalt |
|---|---|
| ID | F-02 |
| Priorität | BLOCKER |
| Fundstelle | `BASELINE.md` §6 (GR-02, GR-03), §4 (NFANF-02, NFANF-11); `TRACEABILITY.md` US-04/US-07 |
| Befund | Es gibt **keine** messbare Anforderung gegen *erfundene* Belege. GR-02 („Suchtreffer … nicht als Lektürenachweis“) und GR-03 („exakte Zitate … nur nach Verifikation“) sind Regeln ohne NFANF-Gegenstück. NFANF-02 misst nur den *Anteil belegter Aussagen mit Fundstelle* – die Anwesenheit von Belegen, nicht die Abwesenheit fabrizierter Belege. NFANF-11 betrifft nur fehlgeschlagene Quellenzugriffe, nicht stillschweigend erfundene. |
| Nachweis | Wortlautabgleich §4/§6; Traceability US-04/US-07 → FANF-07/08/09 enthält kein NFANF. Empirisch: die THEOBald-Basistests T01 und T05 sind als „PARTIAL PASS, Quellen-Fail“ protokolliert – genau dieser Fehlerpfad ist bereits real aufgetreten. |
| Auswirkung | Die fachlich kritischste Eigenschaft des Werkzeugs ist nicht abnehmbar. Ein System könnte alle NFANF erfüllen und dennoch Zitate erfinden. |
| Empfehlung | Eine NFANF ergänzen, analog zu NFANF-12 hart formuliert: „Anzahl der als verifiziert ausgegebenen, tatsächlich nicht verifizierbaren Fundstellen = 0“, mit Negativkorpus nach dem bereits vorhandenen Muster R03. Kein neues Konzept nötig – Muster und Testdatei existieren im Vorgängerprojekt. |

#### F-03 | BLOCKER | BASELINE US-21, US-23, FANF-18, FANF-19, DAT-03, DAT-04, §1

| Feld | Inhalt |
|---|---|
| ID | F-03 |
| Priorität | BLOCKER |
| Fundstelle | `BASELINE.md` §1, §2 (US-21, US-23), §3 (FANF-18, FANF-19), §6 (GR-09), §8 (DAT-03, DAT-04) |
| Befund | Für „eingefrorene“ Textfassungen und „frühere Arbeitsfassungen“ existiert **kein Datenmodell**. DAT-03 fordert eine Statuszuordnung, aber keine DAT definiert Zustandsraum, Ablage, Lebensdauer, Adressierbarkeit oder Geltungsbereich (pro Chat / pro Nutzer / sitzungsübergreifend). FANF-19 setzt eine „zugängliche frühere Arbeitsfassung“ voraus, ohne zu sagen, wodurch sie zugänglich wird. Zusätzlich uneinheitliche Terminologie: §1 definiert nur Freeze; US-21 und DAT-03 sprechen von „Freigabe- **oder** Freeze-Status“; GR-09 kennt nur Freeze. |
| Nachweis | Wortlautabgleich §1/§2/§3/§6/§8; Traceability US-21 → FANF-18, US-23 → FANF-19. |
| Auswirkung | US-21 und US-23 sind ohne Architekturentscheidung nicht implementierbar; NFANF-12 („null unbeauftragte Änderungen an eingefrorenen Passagen“) ist ohne definierten Zustandsbegriff nicht prüfbar. Dies ist der einzige Fall, in dem die Baseline eine Architekturentscheidung erzwingt, ohne die Entscheidungsgrundlage zu liefern. |
| Empfehlung | DAT-03 zu einer echten Datenanforderung ausbauen (Zustände Entwurf / freigegeben / eingefroren, Übergänge, Ablage, Lebensdauer, Zugriffsbereich) und §1 um die Definitionen „Arbeitsfassung“, „Freigabe“, „Freeze“ ergänzen. |

### 3.2 MAJOR

#### F-04 | MAJOR | BASELINE DAT-02, FANF-07, FANF-08

| Feld | Inhalt |
|---|---|
| ID | F-04 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §8 (DAT-02), §3 (FANF-07, FANF-08) |
| Befund | „Überprüfbare Fundstelle“ ist weder in der Auflösung (Seite / Abschnitt / Absatz / Canon / KKK-Nummer) noch im Ausgabeformat definiert. DAT-02 fordert nur die Zuordnung von Quelle + Fundstelle. |
| Nachweis | Wortlaut DAT-02. THEOBald benennt das Problem ausdrücklich („keine behauptete Seitenzahl bei Markdown-Datei“, `rag-acceptance.md`); PDF-/Text-Extraktion ist dort noch nicht abgenommen (`roadmap.md`). |
| Auswirkung | Das zentrale Wertversprechen (Nachvollziehbarkeit, US-04) ist nicht prüfbar; Seitenzitate sind über PDF-Extraktion technisch unzuverlässig, solange die Granularität nicht festgelegt ist. |
| Empfehlung | DAT-02 um Granularitätsstufen und ein Mindest-Zitierformat erweitern; NFANF-02 an die geforderte Granularität binden. |

#### F-05 | MAJOR | BASELINE US-25 ↔ FANF-10, FANF-12

| Feld | Inhalt |
|---|---|
| ID | F-05 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §2 (US-25), §3 (FANF-10, FANF-12); `TRACEABILITY.md` US-25 |
| Befund | US-25 verlangt, „Glaubensaussagen, Interpretationen und empirische Behauptungen unterscheidbar“ zu machen und „relevante Gegenpositionen“ einzubeziehen. Zugeordnet sind FANF-10 (Quellenvergleich fachlicher Positionen) und FANF-12 (mehrere Deutungen *eines Bibeltexts*). Weder die Unterscheidung der Aussagearten noch die Einbeziehung von Gegenpositionen ist als Funktion formuliert. |
| Nachweis | Abgleich des US-25-„damit“-Ziels gegen die Zuordnung in TRACEABILITY und gegen FANF-10/12. Inhaltlich getragen wird das Ziel allenfalls von GR-05, das aber keine Funktion ist. |
| Auswirkung | Die Traceability ist formal vollständig, inhaltlich aber nicht: eine Anforderung ohne deckende Funktion. Typischer Blindfleck bei der Abnahme. |
| Empfehlung | US-25 auf eine passende Funktion abbilden – entweder GR-05 in einer FANF operationalisieren (Aussageart ausweisen, Gegenposition benennen) oder die Zuordnung korrigieren. |

#### F-06 | MAJOR | BASELINE US-20 ↔ FANF-14

| Feld | Inhalt |
|---|---|
| ID | F-06 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §2 (US-20), §3 (FANF-14); `TRACEABILITY.md` US-20 |
| Befund | US-20 verlangt die Steuerung von Arbeitsschritt und Bearbeitungstiefe **allgemein**. FANF-14 spezifiziert die Wahl zwischen Teilschritten und vollständigem Entwurf jedoch ausschließlich für „eine Predigt“. Für Exegese, Liturgie, Katechese und Textprüfung fehlt die entsprechende Funktion. |
| Nachweis | Wortlaut FANF-14 („eine Predigt“); Zuordnung US-20 → FANF-14, FANF-31. |
| Auswirkung | Eine als generell zugesagte Nutzererwartung ist nur in einem Anwendungsfall spezifiziert; spätere Nachforderungen sind vorprogrammiert. |
| Empfehlung | FANF-14 verallgemeinern („einen Auftrag wahlweise in Teilschritten oder vollständig …“) – kleinste sachgerechte Korrektur, kein neues Anforderungsobjekt. |

#### F-07 | MAJOR | BASELINE FANF-33, US-27

| Feld | Inhalt |
|---|---|
| ID | F-07 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §3 (FANF-33), §2 (US-27) |
| Befund | FANF-33 spricht von „unterstützten Dateiformaten“, ohne dass eine DAT/RANF den Formatumfang festlegt. Auch die Verarbeitung von PDF (textbasiert vs. gescannt/OCR) und der Modalitätspfad sind nicht adressiert. |
| Nachweis | Volltextabgleich §3/§5/§8 – keine Formatliste. ADR-0001 hält fest, dass ein multimodales Modell PDF-Seiten nur dann „sieht“, wenn der Verarbeitungspfad die Modalität überträgt. |
| Auswirkung | US-27 nicht testbar; der Umfang der Dokumentverarbeitung bleibt offen, obwohl die Fachbibliothek (67 Dokumente, 486.575.819 Byte) überwiegend PDF sein dürfte. |
| Empfehlung | Eine RANF/DAT „unterstützte Formate“ mit Mindestliste und ausdrücklicher Grenze (z. B. kein OCR in v1) ergänzen. |

#### F-08 | MAJOR | BASELINE GR-09 ↔ FANF-17

| Feld | Inhalt |
|---|---|
| ID | F-08 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §6 (GR-09), §3 (FANF-17), §4 (NFANF-12) |
| Befund | Regelkonflikt möglich. GR-09 verbietet die Änderung eingefrorener Passagen ohne „ausdrückliche erneute Nutzerfreigabe“; FANF-17 verlangt, vom Nutzer benannte Passagen zu bearbeiten. Ob die Benennung in einem Revisionsauftrag als erneute Freigabe gilt, ist nicht geregelt. |
| Nachweis | Wortlautvergleich GR-09 und FANF-17; NFANF-12 verlangt zugleich null unbeauftragte Änderungen. |
| Auswirkung | NFANF-12 ist nicht eindeutig prüfbar; das Systemverhalten in genau dem Konfliktfall, für den Freeze existiert, ist ambivalent. |
| Empfehlung | GR-09 präzisieren: Freeze-Aufhebung nur durch explizite, eigene Aktion; ein Änderungsauftrag nach FANF-17 hebt einen Freeze nicht stillschweigend auf. |

#### F-09 | MAJOR | BASELINE SP-03, FANF-02, FANF-03, SP-01

| Feld | Inhalt |
|---|---|
| ID | F-09 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §7 (SP-01, SP-03), §3 (FANF-02, FANF-03) |
| Befund | SP-03 verlangt die Verhinderung „unzulässige[r] Zugriffe auf interne Netzwerkziele und unsichere[r] Weiterleitungen“, ohne dass ein Zulässigkeits- oder Netzwerkrahmen definiert ist. Ebenso bleibt in FANF-02/FANF-03 offen, wer oder was eine Quelle bzw. die Bibliothek „zulässt“ – ein Berechtigungsmodell existiert nicht, obwohl SP-01 von „erteilten Zugriffs- und Verarbeitungsberechtigungen“ ausgeht. |
| Nachweis | Wortlaut SP-03, FANF-02, FANF-03, SP-01; keine DAT/RANF zu Netzwerk- oder Quellenzulassung im Dokument. |
| Auswirkung | Eine Sicherheitsanforderung ist nicht abnehmbar; die Bedingung „falls zugelassen“ macht FANF-02/03 von einer undefinierten Instanz abhängig. |
| Empfehlung | RANF/DAT „Netzwerk- und Quellenzulassung“ ergänzen (erlaubte Domains, Verbot privater IP-Bereiche, Redirect-Regeln, wer Freigaben erteilt). Kein Architekturentwurf, sondern eine Randbedingung. |

#### F-10 | MAJOR | BASELINE SP-05, RANF-03, DAT-01

| Feld | Inhalt |
|---|---|
| ID | F-10 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §7 (SP-05), §5 (RANF-03), §8 (DAT-01) |
| Befund | Nutzungsrechte sind als MUSS gefordert (SP-05, RANF-03), aber es gibt **kein Merkmal und keinen Prozess**: DAT-01 führt „Herkunft“, aber keine Lizenz bzw. keinen Nutzungsrechtestatus und keine Zulässigkeit externer Verarbeitung. |
| Nachweis | Wortlaut SP-05/RANF-03/DAT-01. Im Vorgängerprojekt ist die Rechtefrage ausdrücklich offen – „vor Fachliteratur-Tests Rechte, Datenfluss, Provider-Routing und Aufbewahrungsbedingungen klären“ (ADR-0001, `openwebui-setup.md`); „externe Weitergabe von Retrievalpassagen über OpenRouter ist nicht genehmigt/geprüft“ (`roadmap.md`). |
| Auswirkung | SP-05 und RANF-03 sind nicht prüfbar; das Risiko der unzulässigen Weitergabe geschützter Passagen bleibt ungesteuert, obwohl der Datenpfad extern über OpenRouter führt. |
| Empfehlung | DAT-01 um „Lizenz/Nutzungsrechte“ und „Zulässigkeit externer Verarbeitung“ erweitern und die im ADR dokumentierte Vorbedingung als RANF aufnehmen. |

#### F-11 | MAJOR | BASELINE RANF-04

| Feld | Inhalt |
|---|---|
| ID | F-11 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §5 (RANF-04); Referenz: THEOBald `docs/baseline-v1.2.0.md`, `docs/roadmap.md` |
| Befund | RANF-04 fordert einen „verbindlichen theologischen Fachstandard in einer versionierten Fassung“, benennt aber weder Artefakt noch Herkunft, Version oder Änderungsverfahren. Faktisch existiert das Artefakt bereits: `Prompts/THEOBald_Fachstandard.md`, 15.074 Byte, SHA-256 dokumentiert; GR-01 … GR-18 der neuen Baseline entsprechen inhaltlich diesem Fachstandard. |
| Nachweis | Wortlaut RANF-04 gegen `docs/baseline-v1.2.0.md` und `docs/roadmap.md`. |
| Auswirkung | Die zentrale fachliche Randbedingung bleibt vage; die Bindung der 18 Fachregeln an ein nachweisbares Artefakt fehlt – und damit die Nachvollziehbarkeit des fachlichen Kerns. |
| Empfehlung | RANF-04/DAT um Artefaktname, Ausgangsversion, Ablage und Änderungsverfahren ergänzen (z. B. `THEOBald_Fachstandard.md` v1.2.0 als Ausgangsfassung). Wichtigster Anknüpfungspunkt zum Vorgängerprojekt. |

#### F-12 | MAJOR | BASELINE GR-03, DAT-01

| Feld | Inhalt |
|---|---|
| ID | F-12 |
| Priorität | MAJOR |
| Fundstelle | `BASELINE.md` §6 (GR-03), §8 (DAT-01) |
| Befund | Keine Anforderung verpflichtet, die verwendete Ausgabe zu *benennen*: Bibelübersetzung (z. B. Einheitsübersetzung), KKK-Ausgabe (lateinische Editio typica vs. deutschsprachige Ausgabe mit abweichender Nummerierung) und CIC-Fassung. GR-03 verlangt verifizierte „Bibelstellen, Dokumenttitel, KKK-Nummern, Canones und Absatznummern“ – ohne Ausgabenbindung ist die Verifikation nicht eindeutig. |
| Nachweis | Wortlaut GR-03 und DAT-01 („Ausgabe, Geltungsstand“). DAT-01 erlaubt eine Ausgabenangabe, verlangt sie aber nicht und bezieht sie nicht auf Bibel/KKK/CIC. |
| Auswirkung | Fachliche Korrektheit (NFANF-01) ist im sensibelsten Bereich – Zitatgenauigkeit – nicht abgesichert; falsche KKK-Nummern sind ein realistischer Fehlerpfad. |
| Empfehlung | Eine GR/DAT-Regel ergänzen: „verwendete Ausgabe (Bibelübersetzung, KKK-Ausgabe, CIC-Fassung) ist anzugeben und bei Belegen zu führen“. |

### 3.3 MINOR

#### F-13 | MINOR | BASELINE §1, US-21, DAT-03, GR-09

| Feld | Inhalt |
|---|---|
| ID | F-13 |
| Priorität | MINOR |
| Fundstelle | `BASELINE.md` §1, §2 (US-21), §8 (DAT-03), §6 (GR-09) |
| Befund | Terminologie „Freigabe“ vs. „Freeze“ uneinheitlich; „Arbeitsfassung“ nicht definiert. |
| Nachweis | Wortlautabgleich §1/§2/§6/§8. |
| Auswirkung | Begriffsunklarheit in einem sicherheitsrelevanten Mechanismus (Überschneidung mit F-03). |
| Empfehlung | Begriffsklärung in §1. |

#### F-14 | MINOR | BASELINE FANF-05

| Feld | Inhalt |
|---|---|
| ID | F-14 |
| Priorität | MINOR |
| Fundstelle | `BASELINE.md` §3 (FANF-05) |
| Befund | „in ausreichendem Kontext lesen“ ist nicht quantifiziert und damit nach SOPHIST nicht testbar. |
| Nachweis | Wortlaut FANF-05. |
| Auswirkung | Keine eindeutige Abnahmefähigkeit der Originallektüre-Anforderung. |
| Empfehlung | Mindestkontext definieren (z. B. vollständiger Absatz bzw. Kapitelabschnitt); Kriterium: die belegte Aussage muss im gelieferten Kontext überprüfbar sein. |

#### F-15 | MINOR | BASELINE FANF-30

| Feld | Inhalt |
|---|---|
| ID | F-15 |
| Priorität | MINOR |
| Fundstelle | `BASELINE.md` §3 (FANF-30) |
| Befund | „unabhängig von der Nutzermeinung … bewerten“ ist ohne Prüfverfahren nicht messbar. |
| Nachweis | Wortlaut FANF-30; kein Testverfahren definiert. |
| Auswirkung | US-19 (kritischer Dialog) ist nicht abnehmbar. |
| Empfehlung | Prüfverfahren festlegen: identische Position mit entgegengesetztem Nutzer-Framing muss zum gleichen Urteil führen. |

#### F-16 | MINOR | BASELINE DAT-01, DAT-02

| Feld | Inhalt |
|---|---|
| ID | F-16 |
| Priorität | MINOR |
| Fundstelle | `BASELINE.md` §8 (DAT-01, DAT-02) |
| Befund | Kann-Formulierung („zuordnen können“) statt MUSS schwächt die Verbindlichkeit. |
| Nachweis | Wortlaut DAT-01/DAT-02 gegen die im Dokument selbst gesetzte Verbindlichkeitsregel („Alle MUSS-Anforderungen sind verbindlich“). |
| Auswirkung | Verbindlichkeitsgrad der Datenanforderungen unklar. |
| Empfehlung | Auf „muss … zuordnen“ umstellen. |

#### F-17 | MINOR | BASELINE GR-17 ↔ NFANF-04; GR-09/FANF-18 ↔ NFANF-12

| Feld | Inhalt |
|---|---|
| ID | F-17 |
| Priorität | MINOR |
| Fundstelle | `BASELINE.md` §6 (GR-17, GR-09), §4 (NFANF-04, NFANF-12) |
| Befund | Doppelungen zwischen Fachregel und Qualitätsanforderung. |
| Nachweis | Gegenüberstellung der Regel- und Qualitätsebene. |
| Auswirkung | Gering – die Doppelung ist sachlich vertretbar (Regel + messbare Qualität), die Grenzziehung ist aber nicht ausdrücklich dokumentiert. |
| Empfehlung | Die Grenze GR ↔ NFANF im Dokument einmal ausdrücklich benennen. **Keine inhaltliche Änderung erforderlich.** |

#### F-18 | MINOR | Nachweis der Herkunft des Fachstandards (Vorgängerrepo)

| Feld | Inhalt |
|---|---|
| ID | F-18 |
| Priorität | MINOR |
| Fundstelle | THEOBald `README.md` vs. `docs/baseline-v1.2.0.md` vs. `docs/roadmap.md`; mittelbar `BASELINE.md` §5 (RANF-04) |
| Befund | Herkunft des Fachstandards im Vorgängerrepo widersprüchlich dokumentiert: `README.md` sagt „Der Integritätsvergleich gegen SHA256SUMS.txt steht noch aus“ und „Stand: Phase 0 … keine Modelltests“, während `docs/baseline-v1.2.0.md` „82/82 PASS“ meldet und `docs/roadmap.md` Phase 1 als PASS sowie Inferenz- und RAG-P0-Tests als durchlaufen führt. |
| Nachweis | Textvergleich der drei Dokumente im Referenzrepo. |
| Auswirkung | RANF-04 stützt sich auf einen Herkunftsnachweis, dessen Dokumentationsstand unstimmig ist. |
| Empfehlung | Vor Architektursign-off klären, welche Fassung des Fachstandards verbindlich ist (Nutzerentscheidung, nicht Entwicklerentscheidung). |

---

## 4. Bewertung der THEOBald-Randbedingungen (Teilauftrag §7)

### 4.1 Korrekt und ausreichend berücksichtigt

- Open WebUI als Laufzeitumgebung → RANF-01, deckt ADR-0001.
- Lokaler Docker-Homeserver → RANF-02, deckt ADR-0001.
- Keine geschützten Volltexte im öffentlichen Repo → RANF-03, deckt die Sicherheits- und Lizenzgrenzen des Vorgängerprojekts.
- OpenRouter als externe Modell-API → RANF-05; ADR-0001 und `openwebui-setup.md` sind inhaltlich konsistent.
- Die Formulierungshilfe zu RANF-01/-02/-05 („beschreiben die aktuelle Erprobungsumgebung, nicht die fachliche Notwendigkeit“) ist sachlich richtig und verhindert eine unbeabsichtigte technische Vorwegnahme.

### 4.2 Nicht oder nicht ausreichend berücksichtigt

| THEOBald-Randbedingung | Fundstelle im Vorgängerrepo | Status in THEOAgent v1.1.0 |
|---|---|---|
| Kein LiteLLM im THEOBald-Datenpfad; bestehende LiteLLM-Dienste unverändert | ADR-0001, `openwebui-setup.md` | **nicht erwähnt** |
| Open WebUI Version v0.11.4 (Reproduzierbarkeit) | `roadmap.md` | **keine Versionsbindung** |
| Externe Verarbeitung von Prompt- und Bibliothekspassagen; Rechte/Datenfluss vor Bibliothekstests klären | ADR-0001, `openwebui-setup.md` | nur teilweise (SP-01/SP-05), ohne Vorbedingung → F-10 |
| Realistisches Ausgabetokenlimit (angefordert 32.768, zulässig 21.052; HTTP-402) | `roadmap.md` | **nicht erwähnt**; NFANF-08 ohne Bezug zur tatsächlichen Umgebung |
| Lokale Inferenz großer Modelle auf Raspberry Pi nicht praktikabel | ADR-0001 | nur als Negativabgrenzung erwähnt |
| PDF-Extraktion/Modalitätspfad, Seitenzitatgrenzen | ADR-0001, `rag-acceptance.md` | → F-04, F-07 |
| Keine Nachbaupakete/Secrets/Fachbibliothek ins Repo; Testbelege ohne geschützte Volltexte | `baseline-v1.2.0.md`, `README.md` | RANF-03/SP-04 decken dies; **nicht** ausdrücklich für Testbelege |

Ergebnis: Die *fachlichen* Rahmenbedingungen sind übernommen, die *technisch-operativen* nur teilweise. Das ist konsistent mit dem Anspruch, keine technische Lösung vorwegzunehmen – für F-07, F-09, F-10 und die Versionsbindung ist die Lücke aber architekturrelevant und nicht bloß Dokumentationskosmetik.

---

## 5. Bewertung der fünf Leitfragen

### a) Vor dem Architekturentwurf zu präzisieren
F-01 (Schwellen/Korpora), F-02 (Fabrikations-Null), F-03 (Arbeitsfassungs-/Freeze-Datenmodell), F-04 (Fundstellengranularität), F-07 (Dateiformate), F-09 (Netzwerk-/Zulassungspolicy), F-10 (Rechte-Merkmal). Diese sieben entscheiden über Schnittstellen und damit über die Architektur. F-05, F-06, F-11, F-12 können nachgezogen werden, ohne den Entwurf zu blockieren.

### b) Tatsächlich verbindliche technische Randbedingungen
RANF-01, RANF-02, RANF-03 und RANF-04 sind verbindlich; RANF-05 nur erprobungsgebunden (ADR-0001 bindet OpenRouter ausdrücklich als PoC und erklärt die KRZ-/DRS-Zielumgebung für separat zu bewerten). Ergänzend faktisch verbindlich, aber nicht spezifiziert: Open-WebUI-Version, kein LiteLLM im Datenpfad, Rechte-/Datenfluss-Gate vor Bibliothekstests, Tokenlimit-Realität, Grenzen der PDF-Extraktion.

### c) Offenzuhaltende Architekturentscheidungen
- Modell- und Providerwahl (ADR-0001 führt bewusst Testkandidaten, keine Rangfolge).
- Retrieval-Architektur (Open-WebUI-eigene Knowledge Base vs. externer Speicher – THEOBald nutzt die native Knowledge Base).
- Ob überhaupt ein agentischer Werkzeug-Loop für FANF-32 nötig ist oder Prompting plus native Werkzeuge genügen (KISS).
- Ablage und Geltungsbereich des Freeze-/Versionsspeichers (erst nach F-03 entscheidbar).
- Ort des Fachstandards (Systemprompt, RAG, Skill).

Die Baseline lässt all dies zu Recht offen – sie ist hier technologieneutral.

### d) Für einen ersten MVP wesentlich
Der Engpass ist nicht die Textproduktion, sondern die Belegkette – belegt durch „PARTIAL PASS, Quellen-Fail“ in T01/T05.

- **MVP-Kern:** US-01, US-02, US-03, US-04, US-05, US-06, US-07, US-26, US-27 mit FANF-01 … FANF-10, FANF-32, FANF-33; GR-01 … GR-05, GR-15, GR-16, GR-18; SP-01 … SP-04; NFANF-02, NFANF-11, NFANF-12 plus der neuen Fabrikations-Null aus F-02.
- **MVP-Stufe 2:** Predigtkette US-08, US-09, US-10, US-11, US-20, US-21, US-23.
- **Zurückzustellen:** US-12 … US-16, US-22, US-24 (Liturgie, Katechese, Kirchenrecht, Gesamtkonzept). Diese hängen an FANF-22 (Prüfung der *geltenden* Normfassung) und an der ungelösten Rechtsfrage (F-10); für AH 215 ist im Vorgängerprojekt ausdrücklich vermerkt, dass es sich um eine Vorabpublikation von 2007 handelt und keine automatische Annahme heutiger Normgültigkeit zulässig ist.

### e) Potenziell wiederverwendbare THEOBald-Komponenten

| Komponente | Fundstelle | Eignung |
|---|---|---|
| `Prompts/THEOBald_Fachstandard.md` (15.074 Byte, SHA-256 dokumentiert) | `baseline-v1.2.0.md` | **Hohe Priorität** – inhaltliche Quelle von GR-01 … GR-18; Vorlage für RANF-04 (F-11) |
| `Prompts/Instructions_aktuell.md` (12.485 Byte) | `baseline-v1.2.0.md` | hoch – Rollen-/Instruktionsgerüst; host-spezifische Pfade und YAML-Frontmatter müssen entfernt werden |
| `scripts/prepare_from_archive.py` | `baseline-v1.2.0.md`, `roadmap.md` | hoch – SHA-Prüfung + Erzeugung versionierter Prompt-Artefakte |
| `scripts/audit_pdf_sources.py`, `docs/p1-theology-source-audit.md` | `roadmap.md` | mittel – Quellenprüfung der Bibliothek |
| `scripts/openrouter_preflight.py`, `docs/openrouter-preflight.md` | `roadmap.md` | mittel – Modell-ID-/Verbindungsprüfung ohne Kosten |
| `tests/fixtures/rag-control-01.md` + R01–R03 | `roadmap.md`, `rag-acceptance.md` | **hoch** – synthetisch, GitHub-freigegeben, direkt als Negativ-/Halluzinationstest nutzbar (Muster für F-02) |
| `docs/openwebui-setup.md` | `openwebui-setup.md` | hoch – Installations- und Test-Runbook, 1:1 übertragbar |
| `docs/architecture.md` (ADR-0001) | `architecture.md` | hoch – Randbedingungs- und Risikokatalog |
| `docs/test-results/…T01, T03, T05` | `roadmap.md` | hoch – bereits vorhandene Basisevidenz; belegt den MVP-Fokus |
| 7 Skills (`exegese-homiletischer-arbeitsgang`, `homiletik`, `liturgische-texte`, `pastorale-sensibilitaet`, `qualitaetskontrolle`, `theologische-grundlagen`, `theologische-quellenpruefung`) | `skills/` | **hoch** – bilden US-08/09/10/12/17/18 und GR-01 … GR-07 ab; stärkster Kandidat für Wiederverwendung statt Neuentwicklung |

**Nicht als verbindlich zu übernehmen:** die SourceGuard-Entwicklung des experimentellen Branches – die Baseline erwähnt sie zu Recht nicht, und der Auftrag stellt klar, dass ein grüner CI-Lauf keine fachliche Abnahme ist.

---

## 6. Offene Fragen

Nur Fragen, deren Klärung eine fachliche oder technische Entscheidung blockiert:

1. Ist die Rolle „Nutzer“ ausreichend differenziert? GR-14 (keine Amtsautorität) und US-16 (Zuständigkeiten) setzen voraus, dass Amtsinhaber und Nicht-Amtsinhaber unterscheidbar sind – ein einheitliches Rollenmodell trägt das möglicherweise nicht.
2. Ist Portabilität auf die DRS-/KRZ-Zielumgebung (Modell- und Plattformunabhängigkeit der Fachkonfiguration) eine Anforderung oder ausdrücklich außerhalb dieser Baseline? ADR-0001 nennt die lokale Architektur „kein[en] Nachweis der Funktionsgleichheit mit der KRZ-Umgebung“ – das ist eine Entscheidung des Product Owners.
3. Wer stellt den Nutzungsrechtestatus einer Quelle fest, und wo wird er geführt (F-10)?
4. Welche Fassung des Fachstandards ist verbindlich, und wie wird sie versioniert (F-11, F-18)?
5. Soll NFANF-12 als Qualitätsanforderung oder als Fachregel geführt werden? Sachlich vertretbar, aber die Kategorisierung sollte einmal entschieden sein.
6. Ist die Beschränkung der Sprechbarkeit (NFANF-06) auf Predigt- und Liturgietexte beabsichtigt – Katechese (US-14) bleibt außen vor?
7. Gibt es eine Mehrbenutzer-/Mehrrollen-Perspektive? SP-01 setzt Zugriffs- und Verarbeitungsberechtigungen voraus, die nirgends definiert sind.

---

## 7. Abnahmeempfehlung

**Einer Freigabe der Baseline als Architektur- und Abnahmegrundlage stehen entgegen:**

1. **F-01** – 11 von 12 NFANF ohne Schwellenwert und Korpus; ohne Abnahme-Anhang ist keine Anforderung verifizierbar.
2. **F-02** – keine messbare Anforderung gegen erfundene Fundstellen, obwohl dieser Fehlerpfad im Vorgängerprojekt bereits real aufgetreten ist.
3. **F-03** – fehlendes Datenmodell für Arbeitsfassung, Freigabe und Freeze; US-21/US-23 und NFANF-12 sind ohne es nicht implementier- bzw. prüfbar.

**Vor einem Architektursign-off zusätzlich zu klären (nicht blockierend für den fachlichen Umfang, blockierend für Schnittstellen):** F-04, F-07, F-09, F-10, F-11.

**Ausdrücklich festgehalten:** Als *fachlicher Anforderungsumfang* ist die Baseline v1.1.0 freigabefähig mit den genannten Hinweisen. Die Typentrennung US/FANF/NFANF/RANF/GR/SP/DAT ist eingehalten, die Anforderungen sind weitgehend technologie-neutral formuliert, und die Traceability ist beidseitig vollständig und widerspruchsfrei. Es wird **keine** Überarbeitung der Anforderungsstruktur empfohlen, sondern ein schlanker Abnahme-Anhang sowie die punktuellen Präzisierungen F-02 bis F-12. Eine eigene Architektur wird auftragsgemäß nicht vorgelegt.

---

## 8. Was nachweislich trägt (Positivbefunde)

- **Zählungen stimmen:** 27 US, 33 FANF, 12 NFANF, 5 RANF, 18 GR, 5 SP, 4 DAT – in `README.md` und `BASELINE.md` identisch und durch Auszählung der Tabellen bestätigt.
- **Traceability ist beidseitig vollständig:** Jede US-01 … US-27 ist mindestens einer FANF zugeordnet, jede FANF-01 … FANF-33 mindestens einer US. Zusätzlich stimmt die Rückverfolgbarkeitsspalte in §3 mit der Traceability-Matrix in **allen 33 Fällen** überein – bei gewachsenen Spezifikationen keineswegs selbstverständlich.
- **Saubere Technologieneutralität:** Die Baseline schreibt keine Implementierung vor; die Nennung von Open WebUI, Docker und OpenRouter ist ausdrücklich als Erprobungsumgebung gekennzeichnet und durch den Hinweis auf die Nicht-Verbindlichkeit von Plattform, Modellversion und Pipe-Struktur abgesichert.
- **Fachlich tragfähige Regelsetzung:** GR-02, GR-03, GR-13, GR-14 und GR-18 treffen die fachlich heiklen Punkte (Lektürenachweis, Zitatverifikation, Leiddeutung, Amtsautorität, Teilergebnisse) sachlich richtig – sie decken sich mit den im Vorgängerprojekt dokumentierten Regeln zu Quellenhierarchie und sensiblen Situationen.
- **Sicherheitsgrenzen konsistent:** RANF-03, SP-02, SP-03, SP-04 entsprechen den Sicherheits- und Lizenzgrenzen des Vorgängerprojekts.
- **Der MVP-Fokus ist empirisch belegt:** Die dokumentierten THEOBald-Basistests zeigen, dass Textproduktion funktioniert, die Belegkette aber nicht – die Baseline trifft mit US-04/US-07/GR-02/GR-03 genau den richtigen Risikobereich.

---

## 9. Nachträge nach Abfassung des Berichts

Dieser Abschnitt wurde nach dem Erstbericht ergänzt. Er ändert **kein** Urteil und **keinen** Befund, dokumentiert aber drei nachträglich festgestellte Verschiebungen.

**N1 | Commit-Pinning nachgetragen.** Der Bericht war ursprünglich ohne Commit-SHA abgefasst und damit nicht reproduzierbar zitierbar. Der geprüfte Stand ist jetzt auf `b3d901c8252e1ac95c8cd0cfc2dda78ea7810ab6` festgelegt; die Git-Blob-Kennungen der beiden Anforderungsdateien sind in Abschnitt 1 aufgeführt. Die THEOBald-Referenzen sind **nicht** in gleicher Weise gebunden – insoweit bleibt eine benannte Restunsicherheit, die vor einem Architektursign-off durch Nachziehen der Commit-SHA geschlossen werden sollte.

**N2 | README-Versionsdrift, ohne Befundfolge.** Der zur Reviewzeit abgerufene `README.md` trug die Überschrift „## Anforderungsspezifikation“ und verwies nur auf BASELINE und TRACEABILITY. Der Stand `b3d901c` trägt „## Dokumentation“ und verweist zusätzlich auf `docs/architecture/COMPONENT_INVENTORY.md`. **Kein Finding ist betroffen:** Nur die Zählprüfung (Abschnitt 8) stützt sich auf den README, und die Zählungen in `BASELINE.md` sind unverändert.

**N3 | Neue Architekturdokumentation, die mehrere Findings unabhängig stützt.** `docs/architecture/COMPONENT_INVENTORY.md` (Stand 10.11.2026) wurde nach dem Review angelegt. Sie ist nicht Gegenstand dieses Berichts, überschneidet sich aber mit mehreren Befunden:

| Befund | Unabhängige Stützung durch die Inventarisierung |
|---|---|
| F-02 (keine messbare Anforderung gegen erfundene Belege) | I02 „Gesamt-FAIL wegen unbelegter beziehungsweise falscher amtlicher Quellenzuordnung; keine Werkzeugaufrufe“; QP01/QP03 „FAIL bei autonomer Aktivierung der erforderlichen Websuche“ – der Fehlerpfad aus F-02 ist erneut real belegt |
| F-03 (fehlendes Freeze-Datenmodell) | Für Text-Freeze/Arbeitsfassungen wird „kein unabhängiger technischer Nachweis einer dauerhaften, verlässlich geschützten Freeze-/Versionsfunktion“ festgestellt; T-05 verlangt genau den Nachweis, dessen Datenanforderung fehlt |
| F-10 (Nutzungsrechte ohne Merkmal und Prozess) | T-06 fordert den Nachweis der „Zulässigkeit der Weitergabe der konkret abgerufenen Bibliothekspassagen an den gewählten externen Modellprovider“ – deckungsgleich mit der Vorbedingung in F-10 |
| F-07 (Dateiformate, Dokumenteingabe) | T-01 verlangt, Dokumentextraktion, Retrieval und tatsächliche Auswertung getrennt zu beurteilen; bei I01 wird keine vollständige PDF-Bereitstellung berichtet |
| F-01 (fehlende Schwellenwerte) | **nicht** aufgelöst – auch die Inventarisierung nennt nur Diagnosetests, keine Grenzwerte |

**N4 | Vorläufige Beobachtung zur Inventarisierung (noch kein geprüftes Finding).** Die Inventarisierung beschreibt die aktuelle lokale Testumgebung (Modellprofil `THEOBald – Modular`, Gemma 4 31B IT, Native Function Calling, Raspberry Pi 5) und belegt diese Angaben mit Dokumenten des experimentellen Branches `review/sourceguard-integrated-v0.5.5-dev3` (Commit `a5338e2…`). Der Auftrag stellt fest, dass experimentelle Implementierungen keine verbindlichen Architekturvorgaben sind [1]. Aussagen über den Ist-Zustand werden damit aus einem nicht verbindlichen Branch abgeleitet, dessen eigener Status mit „Lokal laut Projektstatus eingerichtet; Promptversion im Liveprofil nicht vollständig unabhängig verifiziert“ als ungeprüft bezeichnet wird. Das ist eine Vermischung von verifizierten und berichteten Angaben. Eine Bewertung als Finding setzt die Prüfung der zitierten Bezugsdokumente voraus; eine Architektur-/Inventar-Review war **nicht** Teil dieses Auftrags und wird hier nicht vorgezogen.

**Positiv anzuerkennen:** Die Inventarisierung kennzeichnet SourceGuard selbst als experimentell, verortet die 259 CI-Tests korrekt („kein bestandener Agenten-R01-Livetest belegt“) und trägt die CI-Zahl **nicht** als fachliche Abnahme vor. Das deckt sich mit der Vorgabe, dass ein grüner CI-Lauf keine fachliche Abnahme ist [1].

---

## Anhang: Bezugsquellen (abgerufen am 2026-11-10)

| ID | Quelle |
|---|---|
| Q1 | `https://github.com/baem-oss/THEOAgent` (README, `main`) |
| Q2 | `https://github.com/baem-oss/THEOAgent/blob/main/docs/requirements/BASELINE.md` (v1.1.0) |
| Q3 | `https://github.com/baem-oss/THEOAgent/blob/main/docs/requirements/TRACEABILITY.md` (v1.1.0) |
| Q4 | `https://github.com/baem-oss/THEOBald/blob/main/docs/architecture.md` (ADR-0001) |
| Q5 | `https://github.com/baem-oss/THEOBald/blob/main/docs/baseline-v1.2.0.md` |
| Q6 | `https://github.com/baem-oss/THEOBald/blob/main/docs/roadmap.md` |
| Q7 | `https://github.com/baem-oss/THEOBald/blob/main/docs/openwebui-setup.md` |
| Q8 | `https://github.com/baem-oss/THEOBald/blob/main/docs/rag-acceptance.md` |
| Q9 | `https://github.com/baem-oss/THEOBald` (README, `main`), `skills/` |
| Q10 | `https://api.github.com/repos/baem-oss/THEOAgent/commits/main` (Commit-SHA des geprüften Stands) |
| Q11 | `https://api.github.com/repos/baem-oss/THEOAgent/contents/docs/requirements?ref=b3d901c8252e1ac95c8cd0cfc2dda78ea7810ab6` (Git-Blob-Kennungen) |
| Q12 | `https://raw.githubusercontent.com/baem-oss/THEOAgent/b3d901c8252e1ac95c8cd0cfc2dda78ea7810ab6/docs/requirements/BASELINE.md` und `…/TRACEABILITY.md` (Nachkontrolle am gepinnten Commit) |
| Q13 | `https://raw.githubusercontent.com/baem-oss/THEOAgent/main/docs/architecture/COMPONENT_INVENTORY.md` (nicht geprüft, siehe 9 N3/N4) |

**Methodenhinweis:** Alle Befunde beruhen auf Volltextabgleich der abgerufenen Originaldateien, nicht auf Zusammenfassungen oder Chat-Text. Die Anforderungsdateien wurden am gepinnten Commit `b3d901c` nachkontrolliert; gebunden sind sie über die Git-Blob-Kennungen in Abschnitt 1. Es wurden keine Tests ausgeführt; PASS-Aussagen Dritter werden als „berichtet“ gekennzeichnet und nicht als verifiziert übernommen. Nicht geprüft: `COMPONENT_INVENTORY.md` (Abschnitt 9, N3/N4) sowie alle dort zitierten Bezugsdokumente.
