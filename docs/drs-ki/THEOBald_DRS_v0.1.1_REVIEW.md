# Review – DRS-Vorschlag Systemprompt v0.1.1 → optimierte v0.1.2

**Datum:** 2026-11-11 · **Branch:** `drs-ki-test` · **Status:** Review und Entwurf, keine Produktivfreigabe, keine neuen DRS-Läufe.

## Prüfbasis

Vom PO gelieferter Text `THEOBald DRS – Systemprompt v0.1.1 (Testkandidat)`, insbesondere neue Regelgruppe 7.1–7.5. Ausgangsbasis v0.1.0: `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.1.0.md`. Zielartefakt: `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.1.2.md`.

## Review-Findings

| ID | Befund | Maßnahme v0.1.2 |
|---|---|---|
| R-01 | V0.1.1 verbietet selbst vorsichtig gekennzeichnete, aufgabennotwendige Annahmen über Absichten/Gefühle; Rückfragenpauschale fördert Leerlauf. | Keine unbelegten Zuschreibungen; bedingte Annahmen klar markieren, gezielte Rückfragen nur wenn wesentlich. |
| R-02 | Absolute Verbote jeder Höflichkeit/Entschuldigung sind übersteuert und stehen der pastoralen Rolle entgegen. | Floskeln vermeiden; angemessene Höflichkeit, konkrete Fehlerkorrektur und seltene knappe Entschuldigung erlauben. |
| R-03 | Verbot des Lösungsangebotes bei fehlender Tool-Aktion verwechselt Entwurf, Anleitung und tatsächliche Ausführung. | Drei Handlungsebenen unterscheiden; realistische Entwürfe und Anleitungen zulassen. |
| R-04 | `verletzlich`, `kein Helfer`, `Syphatik`/Schreibfehler sind unklar bzw. rollenfremd. | Nüchternheit, Korrigierbarkeit, Wahrhaftigkeit und klare Rollenbeschreibung. |
| R-05 | V0.1.0/1.1 Freeze-Regel „nur ausdrücklich freigegebene Zielpassagen“ widerspricht T-05-Schritt 2: B darf trotz fehlender inhaltlicher Freigabe geändert werden. | Bearbeitung bei explizitem Auftrag und fehlendem Freeze erlauben; Freigabe und Änderungsberechtigung getrennt. |
| R-06 | T-08-B-R1 zeigte ein sinngemäßes Bibelwort fälschlich als wörtliches EÜ-2016-Zitat. | Exakte Übersetzungszuschreibung nur mit geprüftem Originalwortlaut, sonst ausdrücklich Paraphrase. |

## unverändert

Fachliche sieben Skills im Kern, Quellenautorität, keine erfundenen URLs, keine behauptete Originallese ohne Abruf, vorhandene Werkzeuge statt erfundener Schnittstellen, Status- und Freeze-Trennung, Grenzen des Prompts.

## Bewertung / Freigabe

`v0.1.2` ist ein **zu prüfender Kandidat**, keine produktive oder fachlich empirisch validierte Verbesserung. Gegenüber den eingefrorenen Regressionstests ist das eine **neue Prompt-Version** und muss in einer separaten, sauber gekennzeichneten Testreihe bewertet werden. Frühere v0.1.0-Runs nicht auf v0.1.2 umetikettieren. `main`, T-08/T-05-Orakel und Testfixtures unverändert.
