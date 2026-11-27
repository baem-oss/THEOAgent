# AP 1 – Technische Abnahme

Datum: 27.11.2026
PO-Freigabe: ausdrücklich im Projektchat erteilt.
Entwicklungsreferenz: v0.5.5-dev5, Agent 0.2.0-dev9, Commit 39e96646c1265eb0e9c4b6d903d1316071c65c9f.

## Nachweise
- dev4: fünf AP1-Prüfblöcke laut PO PASS.
- dev4/dev5: QE-Referenzverteilung 21 PASS, 14 FAIL, 11 PARTIAL, 1 INFO laut PO. Kein vollständiger Einzelfallvergleich; separater AP1-Lauf für dev5 nicht übermittelt.
- dev5 Live-Erstanfrage Klippert: FREIGEGEBEN, 8 Runden, 17 Werkzeugaufrufe, 4 registrierte Lesezugriffe, 23222,5 ms; S1–S4 registriert und beansprucht.
- dev5 Live-Folgefrage zur Anwendung: FREIGEGEBEN, 5 Runden, 17 Werkzeugaufrufe, 3 Lesezugriffe, 16612,1 ms; S1–S3 registriert, S1–S2 beansprucht.
- Beide: Systemprompt-Präfix 24836 Zeichen, SHA-256 6c627ad4dd4f82e67618a84774e6757fb0fbfc74b20afe99613b4e3d7ddc9680; sieben Skills im Inventar; view_skill verfügbar; theologische-quellenprufung erfolgreich geladen.
- Folgefrage: zwei Gesprächsnachrichten übernommen, LOCAL_ONLY aus Verlauf aktiv.

## Umfang und Grenzen
Technische AP1-Abnahme für den getesteten Umfang. Kein Nachweis der vollständigen providerseitigen Promptverarbeitung, aller sieben Skill-Aufrufe oder fachlichen Richtigkeit der Originalzitate. Allgemeine Quellenbeschränkungen und deren Aufhebung nicht vollständig implementiert. Kein Produktivrelease.

Offen: doppeltes Quellenverzeichnis (AP2), Beleggrammatik, Zitatprüfung und Quellenpflicht (AP2), Werkzeugargumente, grep-Fehler und veraltete Diagnosen (AP3). Skill-Auswahl beobachten. Requirements v1.2.0 unverändert.
