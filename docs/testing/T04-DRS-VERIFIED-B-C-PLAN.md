# T-04 – Kontrollierte Folgetests B2 und C (Systemprompt v0.2.3)

**Stand:** 12.11.2026 · **Branch:** `drs-ki-test` · **Status:** NOT_RUN.

## Ausgangslage

- T-04-R1 (v0.2.2 laut Planung): `view_knowledge_file` autonom, **FAIL 6/8** (Nr. 5/7).
- T-04-R2 (v0.2.3 laut Planung): `analyze_uploaded_documents`, **BLOCKED**.
- R2-D1 (nach Nutzerintervention): `view_knowledge_file`, **PASS 8/8**.
- Variante A (v0.2.3 laut Planung): `analyze_uploaded_documents`, **BLOCKED**.
- Variante B (v0.2.3 laut Planung): `view_knowledge_file` nach nutzerseitigem Hinweis, **FAIL 6/8** (Nr. 5/7).

Ein Nachweis der **tatsächlich hinterlegten** Promptversion steht für die Laufprotokolle aus. Die genannten Versionen sind geplante, keine unabhängigen Backend-Metadaten. Die kleinen Stichproben belegen keine Zuverlässigkeitsquote.

## Vorbedingungen für jeden Test

1. In der DRS:KI-Oberfläche das **separate Anweisungs-/Systemprompt-Feld** aufrufen, falls vorhanden, und v0.2.3 aus `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.2.3.md` frisch und vollständig einfügen. **Nicht** als gewöhnliche Chatnachricht senden. Wenn ein solches Feld nicht existiert oder nicht wirksam für den Allrounder-Chat ist, **CONFIG_UNVERIFIED** protokollieren und nicht so tun, als sei der Systemprompt gesetzt.
2. Soweit möglich den Speichervorgang bzw. Wiederöffnen des Feldes und die **Kopfzeile samt Versionsnummer** sowie eine **charakteristische Regel aus Abschnitt 2** als Screenshot oder Textnachweis festhalten; keine personenbezogenen Daten miterfassen. Ein Screenshot belegt den sichtbaren Konfigurationsstand, **nicht** die technische Rollen-Priorität im Modell-Backend.
3. Frischen Chat öffnen, dieselbe `tests/fixtures/t04/belegkorpus.md` (2,9 KB) hochladen, Extraktionsanzeige dokumentieren, keine weiteren Dateien.
4. Modellbezeichnung/Datum/UI-Variante soweit sichtbar dokumentieren, **ersten Werkzeugnamen und Roh-Toolausgabe** sichern. Keine Leseintervention vor Sicherung der Erstantwort.

## B2 – Direkter Nutzerhinweis (Replikation mit geprüfter Konfiguration)

**Ziel:** Wiederholung der bisherigen Variante B mit sichtbar gesichertem Promptstand v0.2.3.

- Als erste und einzige Nutzernachricht nach Upload: wortgleicher Nutzerprompt der bereits dokumentierten Variante B aus `tests/runs/2026-11-12-DRS-T04-B-EXPLICIT-READER-v0.2.3.md`: ein einleitender Satz „Lies die beigefügte Datei `belegkorpus.md` zuerst mit dem Werkzeug `view_knowledge_file`. Verwende für diese Lektüre nicht `analyze_uploaded_documents`.“; danach **wortgleich** der ursprüngliche T-04-Auftrag samt acht Behauptungen aus `docs/testing/T04_DRS_PROMPT.md`.
- **Bewertung:** Toolpfad separat PASS (direkt `view_knowledge_file`) oder nicht; fachliches Ergebnis wie gewohnt strikt gegen `tests/oracles/T04_DRS_ORACLE.md`. Für 8/8 sind Nr. 5 **widerlegt**, Nr. 6 **nicht überprüfbar**, Nr. 7 **widerlegt**. Bei anderem Werkzeugpfad eine fehlgeschlagene Lektüre nicht als fachlichen Fehlklassifikationsversuch ausgeben.
- **Methodik:** Diagnostischer Nutzerprompt, kein identischer Original-T-04-Akzeptanztest; die aktive Promptversion bleibt nur soweit verifiziert wie die Oberfläche es erlaubt.

## C – Zweistufige Originallektüre und spätere Klassifikation

**Ziel:** Unter **demselben sichtbar gesicherten v0.2.3-Konfigurationsstand** prüfen, ob eine eigenständige Textlektüre vor der Klassifikation Nr. 5 und Nr. 7 verbessert.

Neuer separater Chat, dieselbe Datei; keine Konfiguration zwischen B2 und C ändern.

**Turn C1 – eigenständige Lektüre:**

> Lies die hochgeladene `belegkorpus.md` mit `view_knowledge_file`. Gib die Abschnitte 2.1, 2.2, 3.1, 3.2, 4.1, 4.2 und 5 mit ihren Abschnittskennungen wieder. Unterscheide exakte Zitate von eventuellen Auslassungen. Noch keine Bewertung der acht Behauptungen.

Hinweis: Die Bitte um wörtliche Wiedergabe ist auf den synthetischen, projektspezifischen Prüfkorpus beschränkt. Für lizenzierte Fremdwerke ist eine solche Volltextwiedergabe nicht generell zulässig.

**Turn C2 – Klassifikation:**

> Prüfe jetzt die acht Behauptungen aus dem folgenden unveränderten T-04-Nutzerauftrag ausschließlich anhand der in diesem Chat gelesenen Fachnotizen. [Hier den vollständigen Abschnitt „Nutzerprompt“ aus `docs/testing/T04_DRS_PROMPT.md` **wortgleich und vollständig** einfügen, nicht den Text in eckigen Klammern senden.]

- Erste Tool-/Lesefrage, Vollständigkeit der C1-Ausgabe, eventuelle Toolfehler und **C2-Ausgabe** separat sichern. C1 kann die korrekten Fundstellen vorwegnehmen; das ist **Absicht der Diagnose** und kein unabhängiger Blindtest.
- Fachliche Sollklassifikationen bleiben im internen Orakel unverändert, das Orakel wird dem DRS-Allrounder **nicht** zur Verfügung gestellt.
- **Auswertung:** C1-Lektüre korrekt/teilweise/fehlgeschlagen; C2-Klassifikation 0–8 gemäß Orakel; Status niemals mit dem autonomen Erstlauf von T-04-R2 vermengen.

## Interpretation

Ein einzelner B2-/C-PASS belegt **Funktion unter den konkret beobachteten Bedingungen**. Ob Systempromptversion, Nutzerhinweis, zweiter Turn, Modellstochastik oder andere Umstände ursächlich sind, bleibt ohne kontrollierte Wiederholungen unentschieden. Wenn B2 6/8 und C 8/8 erreicht, ist Zweistufigkeit ein **plausibler** Workaround, noch kein statistischer Beweis. Frühere Dateien, Testkorpus, Orakel und `main` nicht verändern.
