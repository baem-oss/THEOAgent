# P1 – DRS:KI-T-04: drei unabhängige Erstläufe mit eingefrorenem Prompt v0.2.3

**Datum Planung:** 12.11.2026 · **Status:** NOT_RUN · **Branch/SSOT:** `drs-ki-test`

## Entscheidungsgrundlage und Freeze

Für die nächste Untersuchung ist **v0.2.3 unveränderliche Test-Baseline**, nicht als fachlich freigegebene Version. Repositorypfad: `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.2.3.md`; **Git-Blob-SHA:** `8621ce811139d1308715e63e6946e7964cb33b1f`; Länge **10.000 Zeichen**. Der Freeze bezieht sich auf diese Datei und den Testinhalt; er untersagt nicht, dass der PO systempromptseitig in einem Chat editieren kann. Für einen gültigen Lauf muss die hinterlegte Fassung beim Testaufruf mit der Baseline übereinstimmen.

**Weitere feste Referenzen:**
- Nutzerauftrag (nur Abschnitt „Nutzerprompt“): `docs/testing/T04_DRS_PROMPT.md` (Blob `287ee70142501d00c6a927a3bd362e31cf0ff38b`)
- Einziger Upload: `tests/fixtures/t04/belegkorpus.md` (Blob `1a7393fc5467197d949a1d6a259f42fc11fec75b`, 2.835 Zeichen, synthetisch, DRS-UI bisher 2,9 KB)
- Internes, dem Testling **nicht** gezeigtes Orakel: `tests/oracles/T04_DRS_ORACLE.md`
- Keine nachträglichen Anpassungen an Testtext, Prüforakel, Promptversion oder Bewertungskriterien.

## Technischer Befund vor P1

In vorherigen DRS-Chats meldete der sichtbare Aufruf von `analyze_uploaded_documents`: `No usable text was found in the uploaded documents.` Der synthetische Korpus enthält nachweisbar Text. `view_knowledge_file` ermöglichte in anderen DRS-Läufen eine korrekte Dokumentenlektüre. Das ist ein **beobachteter Zugriffspfadfehler ungeklärter Ursache**, kein sicher nachgewiesener Plattform- oder Dateidefekt. Ob `view_knowledge_file` im konkreten Chat verfügbar ist, muss jeweils beobachtet werden.

## Durchführung: drei unabhängige Läufe P1-01, P1-02, P1-03

Für **jeden** der drei Läufe einzeln:

1. **Neuen DRS:KI-Allrounder-Chat** öffnen. Dort den einen verfügbaren Systemprompt mit dem kompletten `v0.2.3`-Text hinterlegen; er ist technisch auch nachträglich editierbar, soll aber **zwischen Teststart und Erstantwort unverändert** bleiben.
2. **Konfigurationsnachweis vor Testbeginn:** Screenshot des tatsächlich aktiven Systemprompt-Feldes mit v0.2.3-Kopfzeile und charakteristischem Abschnitt-2-Satz „Prüfe die ganze Behauptung“. Nach Möglichkeit sichern, dass das Feld tatsächlich für diesen Chat gespeichert/aktiv ist. Die Screenshots beweisen **die angezeigte Konfiguration**, nicht unsichtbare Backend-Prioritäten. Bei fehlender Einsicht `CONFIG_UNVERIFIED` melden; niemals bloß aus dem Verhalten eine Version ableiten.
3. Nur `belegkorpus.md` hochladen; Upload-/Extraktionsanzeige (falls sichtbar) notieren. **Keinen** Werkzeugnamen in die Nutzernachricht schreiben. Kein zusätzlicher Hinweis, keine Nachfrage, kein Testorakel.
4. **Wortgleich** den Abschnitt „Nutzerprompt“ aus `T04_DRS_PROMPT.md` als einzige Test-Nutzernachricht schicken.
5. Bis zur **kompletten Erstantwort** keine Intervention. Sichern: (a) erster und weitere sichtbare Werkzeugaufrufe, (b) Toolnamen, Eingaben einschließlich ggf. Dateiverweis/ID, **wortgleiche Rohausgaben**, (c) komplette Allrounder-Antwort samt Quellenanzeige. Wenn die UI bestimmte Details nicht zeigt, **nicht sichtbar** statt „existiert nicht“ protokollieren.
6. **Erstlauf abschließen und bewerten**; keine Reparatur im selben Lauf. Eventuelle Folgeintervention separat als Diagnose `-D1` bezeichnen.

## Bewertungsregeln

- Werkzeugdimension: `view_knowledge_file` zuerst / `analyze_uploaded_documents` zuerst, dann Recovery / anderer Pfad / unklar. Die reine Sichtbarkeit eines Tools garantiert keine vollständige Lektüre.
- Bei fehlendem verwertbaren Dateizugriff: **BLOCKED**, **keine** scheinbar gemessene Fachquote 0/8 oder 8/8.
- Nachgewiesener Originalzugriff: alle acht Aussagen gegen das vorab fixierte Orakel prüfen. Soll: `1 belegt; 2 widerlegt; 3 widerlegt; 4 belegt; 5 widerlegt; 6 nicht überprüfbar; 7 widerlegt; 8 widerlegt`. `PASS` ausschließlich bei 8/8 und tragfähigen Fundstellen.
- **T-04-FAIL nach Orakel** von **NFANF-13-Verletzung** trennen. NFANF-13 betrifft erfundene, falsch zugeordnete oder unbegründet als überprüft ausgegebene Belege; nicht jede falsche Klassifikation ist automatisch Fabrikation. Insbesondere Nr. 7 kann eine falsche Zuschreibung, Nr. 5 einen Schlussfolgerungs-/Etikettierungsfehler darstellen.
- Beobachtete Zahl der erfolgreichen Toolwahlen aus drei Läufen rein **deskriptiv** berichten, nicht als belastbare Zuverlässigkeitsrate interpretieren.

## Protokollvorlage pro Lauf

```text
Run-ID: P1-0[1–3]
Datum/Uhrzeit:
Chat-Titel:
Systemprompt-Feld sichtbar v0.2.3: ja/nein/unklar
Konfigurationsbeleg: Screenshot/Transkript/keiner
Systemprompt nachträglich geändert während des Laufs: nein/ja/unklar
Modell-/Backendkennung (falls sichtbar):
Anhang: belegkorpus.md / UI-Extraktion:
Erster sichtbarer Werkzeugaufruf:
Weitere Werkzeugaufrufe:
Roheingabe/-ausgabe des ersten Werkzeugs:
Zugriff auf konkrete Korpusstellen nachgewiesen: ja/nein/unklar
Antwort und Quellenanzeige: gesichert ja/nein
Fachlicher Soll-Ist-Abgleich: 8 Ergebnisse oder BLOCKED
T-04-Status:
NFANF-13: verletzt/nicht verletzt/nicht bewertbar
Fehlerklasse: Werkzeug / Fabrikation / Fehlzuschreibung / Klassifikation / keine
Einschränkungen:
```

## Entscheidung nach den drei Läufen

- Bei mehrfachen Blockaden und `analyze_uploaded_documents` als Erstwerkzeug: technische Eskalation bzw. pragmatischen Nutzersatz `view_knowledge_file` als **separaten Workaround** verfolgen; keine zusätzliche fachliche Promptregel ableiten.
- Bei wiederholten falschen Bewertungen **nach nachgewiesener Lektüre**: unabhängige Mini-Beispiele für die Fälle „belegter Satz, falsche Fundstelle“ und „Korpus verneint ausdrücklich Befund“ entwerfen; separat gegen das fixierte T-04-Orakel und einen unabhängigen Kontrollkorpus testen (P3).
- Zweistufige C-Variante bleibt eine alternative Diagnose **nach P1**, nicht ein Ersatz für die drei unveränderten Erstläufe.

**Keine der drei P1-Testausführungen hat mit der Erstellung dieses Dokuments stattgefunden.** `main` unverändert.
