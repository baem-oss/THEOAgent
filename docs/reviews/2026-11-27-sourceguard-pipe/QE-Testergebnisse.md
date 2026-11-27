SHA-256 Testobjekt: d69af656ba5fc6ba811ae8b7b82a73226de4cda41454405ba34fd0f641ba5ba0
| ID | Art | Gegenstand | Erwartet | Tatsächlich | Ergebnis |
|---|---|---|---|---|---|
| B-01 | Unit (simuliert) | [S1] | erkannt, Freigabe, S1 im Quellenverzeichnis | FREIGEGEBEN; Verzeichnis ['S1'] | PASS |
| B-02 | Unit (simuliert) | [S1] [S2] | beide erkannt | FREIGEGEBEN; Verzeichnis ['S1', 'S2'] | PASS |
| B-03 | Unit (simuliert) | [S1, S2] (einziger Beleg) | beide erkannt, Freigabe | GESPERRT: Keine aussagebezogenen Quellenkennungen im Fließtext | FAIL |
| B-04 | Unit (simuliert) | [S1, S2, S3] (einziger Beleg) | alle erkannt, Freigabe | GESPERRT: Keine aussagebezogenen Quellenkennungen im Fließtext | FAIL |
| B-05 | Unit (simuliert) | [S1] … [S1, S99] | Sperre wegen S99 | FREIGEGEBEN | FAIL |
| B-06 | Unit (simuliert) | [S99] [S1] | Sperre wegen S99 | GESPERRT: Nicht gelesene Quellenkennung: S99 | PASS |
| B-07 | Unit (simuliert) | ausschließlich kombinierte Belege | vollständige Validierung, Freigabe | GESPERRT: Keine aussagebezogenen Quellenkennungen im Fließtext | FAIL |
| B-08 | Unit (simuliert) | Kennung nur im Quellenverzeichnis | Sperre | GESPERRT: Keine aussagebezogenen Quellenkennungen im Fließtext | PASS |
| B-09 | Unit (simuliert) | nicht registrierte Absatznummer (S1 hat Nr. 12) | Sperre | GESPERRT: Absatznummer 13 gehört nicht zur zitierten Quelle [S1] | PASS |
| B-09b | Unit (simuliert) | registrierte Absatznummer | Freigabe | FREIGEGEBEN | PASS |
| B-10 | Unit (simuliert) | falsche Werkzuordnung (final.work ≠ gelesenes Werk) | Sperre | GESPERRT: Werkangabe der Antwort stimmt nicht mit geprüfter Quelle überein | PASS |
| B-10b | Unit (simuliert) | falsche Werkzuordnung nur in kombiniertem Beleg (S3 deklariert Klippert, gelesen Mueller) | Sperre | FREIGEGEBEN | FAIL |
| B-11 | Unit (simuliert) | erfundenes Wortzitat mit gültiger Kennung | Sperre oder Kennzeichnung (GR-03) | FREIGEGEBEN | FAIL |
| B-12 | Unit (simuliert) | Aussage B [S1 und S99]. | Sperre (nicht registrierte Kennung) | FREIGEGEBEN | FAIL |
| B-13 | Unit (simuliert) | Aussage B [S1–S9]. | Sperre (nicht registrierte Kennung) | FREIGEGEBEN | FAIL |
| B-14 | Unit (simuliert) | Aussage B (vgl. S99). | Sperre (nicht registrierte Kennung) | FREIGEGEBEN | FAIL |
| B-15 | Unit (simuliert) | Aussage B [S 99]. | Sperre (nicht registrierte Kennung) | FREIGEGEBEN | FAIL |
| B-16 | Unit (simuliert) | gemischt: [S1] … [S1, S2] → Quellenverzeichnis | S1 und S2 im Verzeichnis | FREIGEGEBEN; Verzeichnis ['S1'] | FAIL |
| B-17 | Unit (simuliert) | kombinierte Kennung im Textbearbeitungs-Pfad | Sperre (Kennungen bei Textbearbeitung unzulässig) | OHNE QUELLENPFLICHT | FAIL |
| A-01 | Unit (simuliert) | gültige Websuche | Trefferliste zur Nutzerauswahl | WEBQUELLE AUSWÄHLEN: SOURCEGUARD AGENT: WEBQUELLE AUSWÄHLEN  Webtreffer (noch nicht im Orig / Runden 1, Aufrufe 1 | PASS |
| A-02 | Unit (simuliert) | fehlendes query | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-03 | Unit (simuliert) | leerer Suchausdruck | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-04 | Unit (simuliert) | falscher Datentyp (Liste) | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-07 | Unit (simuliert) | 181 Zeichen | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-07b | Unit (simuliert) | Nutzerfrage DV 12 wörtlich als Suchausdruck | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-07c | Unit (simuliert) | query auf Aktionsebene statt in args | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-07d | Unit (simuliert) | "arguments" statt "args" | kontrollierte Fehlerbehandlung mit unterscheidbarer Ursache (QE-Soll: eine Korrekturchance) | NICHT FREIGEGEBEN: Suchausdruck fehlt oder ist zu lang / Runden 1, Aufrufe 0 | PARTIAL |
| A-06 | Unit (simuliert) | 180 Zeichen | Validierung bestanden, Ausführung | WEBQUELLE AUSWÄHLEN: SOURCEGUARD AGENT: WEBQUELLE AUSWÄHLEN  Webtreffer (noch nicht im Orig / Runden 1, Aufrufe 1 | PASS |
| A-08 | Unit (simuliert) | zusätzliches Argument count (Teil der nativen Signatur) | Korrekturchance oder Ignorieren des optionalen Arguments | NICHT FREIGEGEBEN: Unzulässiges Werkzeug oder Werkzeugargument / Runden 1, Aufrufe 0 | PARTIAL |
| A-09 | Unit (simuliert) | Webwerkzeug nicht verfügbar (Websuche im Chat aus) | kontrollierte Sperre, Ursache sichtbar | NICHT FREIGEGEBEN: Modell bestätigt nicht, dass die Quellen ausreichen / Runden 2, Aufrufe 1 | PASS |
| A-10 | Unit (simuliert) | search_web zusammen mit weiterer Aktion | Korrekturhinweis statt Totalabbruch | NICHT FREIGEGEBEN: Websuche muss ein eigener Schritt sein | PARTIAL |
| A-11 | Unit (simuliert) | Modell ruft view_skill (vom Systemprompt v0.3.11 verlangt) | kontrollierte Behandlung ohne Totalabbruch | NICHT FREIGEGEBEN: Unzulässiges Werkzeug oder Werkzeugargument | PARTIAL |
| A-12 | Unit (simuliert) | fehlerhafter Originalabruf (fetch_url liefert Fehler) | keine Freigabe | NICHT FREIGEGEBEN: Keine Originalstelle durch ein Lese-Werkzeug nachgewiesen | PASS |
| F-01 | Unit (simuliert) | kein Lesezugriff | Sperre | NICHT FREIGEGEBEN: Keine Originalstelle durch ein Lese-Werkzeug nachgewiesen | PASS |
| F-02 | Unit (simuliert) | erfundene Datei-ID | Sperre | NICHT FREIGEGEBEN: Datei-ID nicht aus einem Werkzeugergebnis nachgewiesen | PASS |
| F-03 | Unit (simuliert) | leere Originalpassage (Fenster hinter Dateiende) | Sperre | NICHT FREIGEGEBEN: Keine Originalstelle durch ein Lese-Werkzeug nachgewiesen | PASS |
| F-04 | Unit (simuliert) | Lesefenster ist Inhaltsverzeichnis | keine Registrierung, Sperre | NICHT FREIGEGEBEN: Keine Originalstelle durch ein Lese-Werkzeug nachgewiesen | PASS |
| F-05 | Unit (simuliert) | gültige Lektüre eines fremden Werks bei Klippert-Auftrag | Sperre | NICHT FREIGEGEBEN: Keine Originalstelle durch ein Lese-Werkzeug nachgewiesen | PASS |
| F-06 | Unit (simuliert) | Lesebudget (MAX_READS=8) überschritten | kontrollierte Sperre | NICHT FREIGEGEBEN: Sicherheitsbudget für Originallektüre erreicht | PASS |
| F-07 | Unit (simuliert) | Rundenbudget (MAX_ROUNDS=10) erreicht | kontrollierte Sperre | NICHT FREIGEGEBEN: Maximale Zahl der Recherche-Runden erreicht | PASS |
| F-08 | Unit (simuliert) | zweimal ungültige strukturierte Modellausgabe | kontrollierte Sperre | NICHT FREIGEGEBEN: Modellausgabe trotz einmaliger Formatkorrektur ungültig: Keine JSON-Struktur | PASS |
| F-09 | Unit (simuliert) | quellenpflichtige Anfrage mit Textbearbeitungs-Verb: Kürze den Absatz und ergänze, was Dei Verbum 12 über die Sch… | Quellenpflicht bleibt bestehen | OHNE QUELLENPFLICHT | FAIL |
| F-09b | Unit (simuliert) | quellenpflichtige Anfrage mit Textbearbeitungs-Verb: Korrigiere meinen Satz: Klippert fordert in seinem Buch, das… | Quellenpflicht bleibt bestehen | OHNE QUELLENPFLICHT | FAIL |
| F-10 | Unit (simuliert) | frühe Abschlussantwort ohne Lektüre, dann Lektüre, dann Freigabe (P-03-Muster) | Diagnose kennzeichnet frühere Prüfmeldung als überholt | FREIGEGEBEN; Diagnose enthält 'Antwortprüfung: Keine Originalstelle…' ohne Einordnung | PARTIAL |
| F-11 | Unit (simuliert) | drei überlappende Lesefenster | eine Fundstelle oder Überlappung erkennbar | FREIGEGEBEN; ['Extraktzeilen 2002–2047 (ohne Absatznummer)', 'Extraktzeilen 2004–2049 (ohne Absatznummer)', 'Extraktzeilen 2011–2056 (ohne Absatznummer)'] | INFO |
| I-01 | Pipe-Integration (gestubbt) | Weitergabe Systemprompt (20.916 Z.) bei angehängter Wissenssammlung | vollständiger Systemprompt erreicht das Modell | 3 Nachrichten; 1. Systemnachricht 12000 Zeichen (Systemprompt-Anteil 12000 von 20916) | FAIL |
| I-02 | Pipe-Integration (gestubbt) | Gesprächskontext bei Folgefrage | Vorkontext (Klippert) verfügbar | Modell erhält nur: ['Nutzerauftrag:\nUnd was sagt er zur Anwendung?'] | FAIL |
Counter({'PASS': 19, 'FAIL': 16, 'PARTIAL': 11, 'INFO': 1})