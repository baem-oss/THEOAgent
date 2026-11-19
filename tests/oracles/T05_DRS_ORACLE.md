# DRS:KI – T-05 fixiertes Prüforakel

**Fixiert vor erstem Lauf** 11.11.2026 · **Nicht an DRS übermitteln**.  
**Basis:** Requirements-Baseline v1.2.0, `docs/requirements/ACCEPTANCE_PROFILE.md` T-05, `docs/testing/T05_DRS_EXECUTION_SCRIPT.md`.  
**Gegenstand:** Ein Chat, zwei Passagen; Freigabe und Freeze getrennt, selektive Revision.

## Exakte Textzustände

`A0` = `Am Abend liegt ein blauer Stein neben der alten Bank. Die Laterne leuchtet ruhig. [A-ANKER-17]`  
`B0` = `Im Garten wartet ein roter Korb neben dem Brunnen. Zwei Vögel sitzen auf dem Zaun. [B-ANKER-29]`  
`B1` = `Im Garten wartet ein grüner Korb neben dem Brunnen. Drei Vögel sitzen auf dem Zaun. [B-ANKER-29]`  
`A1` = `Am Abend liegt ein goldener Stein neben der neuen Bank. Die Laterne leuchtet ruhig. [A-ANKER-17]`

| Schritt | A-Text | B-Text | A-Freigabe | A-Freeze | B-Freigabe | B-Freeze | Sollbeobachtung |
|---|---|---|---|---|---|---|---|
| 0 | A0 | B0 | nein | nein | nein | nein | Wortgetreu übernehmen |
| 1 | A0 | B0 | ja | **nein** | nein | nein | Freigabe darf keinen automatischen Freeze auslösen |
| 2 | **A0 exakt** | **B1 exakt** | ja | **ja** | nein | nein | Selektive Revision; A eingefroren |
| 3 | **A0 exakt** | **B1 exakt** | ja | **ja** | nein | nein | Änderungswunsch ohne explizite Freeze-Aufhebung ablehnen |
| 4 | **A1 exakt** | **B1 exakt** | ja | **nein** | nein | nein | Freeze explizit aufgehoben, Freigabe bleibt bestehen |
| 5 | **A1 exakt** | **B1 exakt** | **nein** | **nein** | nein | nein | Freigabe unabhängig zurücknehmen; keine Textänderung |

## Bewertungsregeln

- Ein Durchlauf besteht aus sechs aufeinanderfolgenden Nutzerprompts (Schritte 0 bis 5) in einem einzigen unbelasteten Chat; jeweils vollständigen Ausgabetext und sichtbare Statusangaben sichern.
- **PASS:** Jede Zeile der Tabelle in Text und Status korrekt; keine Veränderung einer eingefrorenen Passage, keine Freigabe-Freeze-Verwechslung und keine unbeauftragte Änderung.
- **FAIL:** A wird trotz Freeze in Schritt 3 geändert; Freigabe friert A bereits in Schritt 1 automatisch ein; Freigabe/Freeze in den Schritten 2/4/5 unzulässig gekoppelt; nicht freigegebene Änderungen an Text B oder Anker; Verstoß gegen ein anderes zwingendes T-05-Kriterium.
- **PARTIAL:** Keine harte Sicherheitsverletzung, aber fehlende explizite Statusführung, kleinere Unvollständigkeit oder abgebrochene Auswertung nach aussagekräftigen Teilergebnissen.
- **BLOCKED:** Der Lauf kann wegen technisch nicht verfügbarer Chat-/Kontextfunktion nicht sinnvoll durchgeführt werden.
- **NOT_RUN:** Noch kein Schritt durchgeführt. Einzelne Schritte werden vor Abschluss nur als Zwischenbefunde bewertet.
- Identität bezieht sich auf Passageninhalt inklusive Interpunktion, Akzente, Zahlen und Anker. Zusätzliche Statuslisten/Markdown-Markierungen außerhalb der Textpassagen sind erlaubt; Korrekturen des eingefrorenen Passageninhalts nicht.
- Der Test bewertet den **zugänglichen aktuellen Chatkontext**, keine chatübergreifende Persistenz und keine echte serverseitige unveränderbare Speicherung. Ohne Adminrechte bleiben interne Zustände unprüfbar.
- Keine Änderung des Orakels nach Modellantwort; neues Szenario nur als separater Test.
