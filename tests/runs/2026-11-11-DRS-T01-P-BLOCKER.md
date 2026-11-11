# DRS:KI – T-01-P kontrollierter PDF-Lesetest (11.11.2026)

**Test-ID:** T-01-P  
**Endstatus:** `PASS` (diagnostischer End-to-End-Test aus Benutzerperspektive)  
**Branch:** `drs-ki-test`  
**Prüfgrundlage:** Requirements-Baseline v1.2.0, fixiertes Orakel `tests/oracles/T01-T03_ORACLES.md`  
**Testkandidat:** DRS:KI / Open WebUI, sichtbarer Assistentenname `Allrounder`; effektive Modell-ID/Provider nicht einsehbar. Kein Nachweis, dass derselbe Konfigurationsstand wie der lokale THEOBald genutzt wird.

## Testeingabe

Datei: `tests/fixtures/t01/document_six_pages.pdf` (synthetisch, 6 Seiten, 3,8 KB). Original aus dem Repository; keine erwarteten Antworten oder Orakel im DRS-Prompt.

Wortgleicher Nutzerprompt:

> Lies das beigefügte Dokument vollständig. Welche Registrierkennung, welcher Sitzungstermin mit Protokollfarbe und welche Freigaberegel samt Abschlusskennwort stehen darin? Nenne jeweils die PDF-Seite.

## Beobachtete Dateiverarbeitung

Die Open-WebUI-Dateivorschau meldete **34 extrahierte Zeilen** und zeigte sämtliche sechs PDF-Seiten in der richtigen Reihenfolge. Darunter die entscheidenden Informationen der Seiten 1/3/6; die Seite 5 enthielt ausdrücklich den nicht als Abschlusskennwort geltenden Ablenkungscode `FELS-12`.

Der Antwort war die sichtbare Werkzeuganzeige **„Ergebnis von view_knowledge_file ansehen“** vorgeschaltet. Die Antwort nannte die Quelle `document_six_pages.pdf` (1 Quelle).

## Vollständige beobachtete Modellantwort

> Hier sind die gesuchten Informationen aus dem Dokument „document_six_pages.pdf“:
>
> - **Registrierkennung**: KELCH-29 — auf **Seite 1** (Zeile 5)
> - **Sitzungstermin mit Protokollfarbe**: 22. April 2032, violett — auf **Seite 3** (Zeilen 14–15)
> - **Freigaberegel samt Abschlusskennwort**: Freigabe nur nach dreifacher Sichtung, Abschlusskennwort: FIRN-46 — auf **Seite 6** (Zeilen 30–31)
>
> Bitte beachten Sie: Das Dokument ist als synthetischer Testfall gekennzeichnet und enthält keine echten oder verbindlichen Daten.

## Soll-Ist- und Nachweisvergleich

| Prüfkriterium | Fixiertes Soll | Beobachtetes Ist | Resultat |
|---|---|---|---|
| Registrierkennung | Seite 1, `KELCH-29` | korrekt, S. 1 | PASS |
| Sitzungstermin | Seite 3, 22. April 2032 | korrekt, S. 3 | PASS |
| Protokollfarbe | Seite 3, violett | korrekt, S. 3 | PASS |
| Freigaberegel | Seite 6, nur nach dreifacher Sichtung | korrekt, S. 6 | PASS |
| Abschlusskennwort | Seite 6, `FIRN-46` | korrekt, S. 6 | PASS |
| Ablenkung | `FELS-12` (S. 5) nicht verwenden | nicht verwechselt | PASS |
| Zugangsnachweis | Extraktion, Modell-/Toolzugang und Antwort getrennt beurteilen | UI-Extraktion, sichtbare `view_knowledge_file`-Anzeige und fundstellenrichtige Antwort | PASS aus Benutzersicht |

**Nachweisgrenze:** Interne Serverlogs und der exakte Modellkontext sind mangels Administratorrechten nicht einsehbar; der sichtbare Werkzeughinweis beweist nicht isoliert den Umfang der intern gelesenen Zeilen. Die Kombination aus 34 extrahierten Zeilen, sichtbarem Dokumentwerkzeug und korrekt zugeordneten Antworten genügt hier für das diagnostische `PASS`; keine Behauptung über interne Konfigurationsdetails.

## Separater technischer Zwischenfall

Vor bzw. während der Vorbereitung war eine UI-Meldung sichtbar:

```text
Database error: error returned from database:
(code: 14) unable to open database file
```

SQLite-Code 14 bezeichnet `SQLITE_CANTOPEN`. Zeitpunkt und Ursache sind nicht geklärt. Die spätere nachgewiesene PDF-Extraktion und korrekte Modellantwort zeigen, dass **dieser konkrete Testlauf nicht dauerhaft blockiert** war. Die frühere vorläufige Wertung `BLOCKED` wird für T-01-P daher durch das endgültige `PASS` ersetzt. Die Fehlermeldung bleibt als eigenständige technische Beobachtung bestehen.

## Ergebnis und Governance

T-01-P ist diagnostisch `PASS`, **keine Gesamtfreigabe** von THEOAgent oder DRS:KI. Orakel, Requirements und `main` bleiben unverändert. T-01-N wird erst nach PO-Aufforderung gestartet.
