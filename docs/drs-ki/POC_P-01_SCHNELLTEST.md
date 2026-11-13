# DRS:KI DEV – schneller PoC (P-01)

**Stand:** 13.11.2026  
**Status:** Sofort ausführbarer Testplan; kein bestandener Test, keine Produktfreigabe  
**Zielsystem:** DRS:KI DEV mit Developerzugriff; Endnutzer ruft ausschließlich das fertig konfigurierte Modell auf  
**Requirements:** [v1.2.0](../requirements/BASELINE.md)  
**Vorhandener Prompt:** [THEOBald DRS v0.2.3](THEOBald_DRS_SYSTEMPROMPT_v0.2.3.md)

## Entscheidung: Kein Tool-Inventar als Vorbedingung

Der PO hat klargestellt, dass auf DRS:KI DEV bereits Werkzeuge aufrufbar sind. Deshalb **entfallen vorgezogene Rechte- und Toolregistrierungsdiagnosen**. Der bereitgestellte Tool-Contract-Probe ist eine optionale spätere Diagnose, **nicht** Voraussetzung dieses PoC. Technische Details werden nur dann nachgeprüft, wenn ein konkreter Test scheitert.

## PoC-Ziel

Ein einziges auf DEV entwickeltes Modell mit dem vorhandenen THEOBald-DRS-Systemprompt soll eine konkrete Quellenfrage **eigenständig** recherchieren und fachlich sauber beantworten. Dazu werden Toolaufrufe, Originallektüre, Fundstelle und Beleggrenzen im selben Lauf dokumentiert.

**PoC-Prompt (wörtlich):**

> Prüfe anhand des Originaltextes von *Dei Verbum* Nr. 12, welche drei hermeneutischen Gesichtspunkte das Zweite Vatikanische Konzil für die Auslegung der Heiligen Schrift nennt. Recherchiere die Quelle selbstständig, verwende nach Möglichkeit die amtliche Fassung, nenne die genaue Fundstelle und unterscheide Textbefund und eigene Zusammenfassung. Wenn du nur Suchtreffer oder Sekundärquellen erhältst, kennzeichne das ausdrücklich.

## Vorbereitung (nur 3 Schritte)

1. Auf **DRS:KI DEV** ein separates Modellprofil **THEOAgent – PoC DRS** aus einer funktionierenden Modell-/Toolkombination erstellen (bestehendes produktives Modell nicht überschreiben).
2. Den bereits vorhandenen [DRS-Systemprompt v0.2.3](THEOBald_DRS_SYSTEMPROMPT_v0.2.3.md) eintragen; vorhandene allgemeine Websuche und erforderliche Quellenwerkzeuge zuweisen. Kein fremder Quellcode nötig.
3. In einem neuen Chat exakt den oben stehenden PoC-Prompt ausführen. Keine manuelle Toolwahl durch den Endnutzer.

## Minimalprotokoll (für einen Lauf)

| Punkt | Feststellung |
|---|---|
| Modell-ID / DEV-Profil | Noch einzutragen |
| Systemprompt | v0.2.3 |
| Tools zugewiesen | Noch einzutragen |
| Tatsächlich aufgerufene Tools und Reihenfolge | Noch einzutragen |
| Amtlicher Originaltext von Dei Verbum 12 nachweislich abgerufen? | JA / NEIN / UNKLAR |
| Genaue Fundstelle und Textbezug richtig? | JA / NEIN / UNKLAR |
| Bloßes Snippet irrtümlich als Originallektüre bezeichnet? | JA / NEIN |
| Ergebnis | PASS / PARTIAL / FAIL |
| Tool-Ausgaben / Screenshots (ohne Geheimnisse) | Link / Ablage |

**PoC PASS** bedeutet nur: die konkret getestete Suche und Antwort gelingen; **kein Nachweis einer technischen SourceGuard-Durchsetzung**. Für letztere bleibt QE-Finding F-C1 und die [AK-01-Korrektur](ARCHITEKTURKORREKTUR_AK-01_F-C1.md) offen. Bei einem FAIL untersuchen wir **den konkreten Fehlerpfad** und entwickeln nur bei Bedarf einen Adapter.

## Danach, aber nicht vor P-01

- Eine Falschbehauptung/Negativprobe zu derselben Quelle, um fehlende Evidenz oder falsche Fundstellen zu erkennen.
- Erst danach die bestehende SourceGuard-Pipe auf DEV einbinden, falls das im PoC festgestellte Verhalten den technischen Schutz erforderlich macht und ihre Integration möglich ist.
- Kein allgemeines „verifiziert“-Versprechen allein auf Basis dieses PoC.

**Arbeitsregel:** Der PoC wird durch einen einzigen, beobachtbaren Lauf entschieden; keine neue Architekturiteration ohne Befund.
