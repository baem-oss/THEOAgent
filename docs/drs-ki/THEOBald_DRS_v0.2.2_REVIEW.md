# THEOBald DRS – Review und gezielte Korrektur v0.2.2

**Stand:** 12.11.2026 · **Branch:** `drs-ki-test` · **Status:** ungetesteter Promptkandidat; keine Produktivfreigabe.

## Auslöser

PO-Review des Commits `eac71f2`: v0.2.1 (9.065 Zeichen) verkürzt den fachlichen Teil relativ stärker als die Werkzeugregeln und enthält weiterhin die T-04-Negativfall- und T-05-Statuslücken. Das ist nachvollziehbar und wurde gezielt korrigiert.

## Änderungen

- **Fachverfahren:** Wiederherstellung von Klage/Ambivalenz und Suizid, liturgischen Grenzen, homiletischen Prüfkriterien, Erhalt der Nutzerstimme und seriöser Auslegungsvielfalt.
- **T-04 Aussage 6:** Fehlen eines Werks oder einer Aussage im Korpus ⇒ nicht überprüfbar, nicht automatisch widerlegt; Gegenbeleg kann widerlegen.
- **T-05:** Freeze-Verstoß auch in Statusmeldungen transparent machen, letzte verifizierte Fassung soweit möglich wiederherstellen; keinen Freeze-Erfolg behaupten.
- **Datei-ID:** Datei-ID-Ermittlung ausdrücklich als verfügbarenfalls; kein unbewiesenes list_knowledge oder andere namentliche Funktionen voraussetzen.

## Begründung der Werkzeugpriorität – mehrere Befunde

- **T-01-P:** Dokumentenzugriff über `view_knowledge_file` im positiven PDF-Basistest (nach früherer Testdokumentation).
- **T-02-P:** Wiederholte Fehlannahmen von `analyze_uploaded_documents` über hochgeladene Markdown-Dateien; später erfolgreiche Lektüre nach Nutzerintervention mit zwei `view_knowledge_file`-Aufrufen.
- **T-04:** `analyze_uploaded_documents` meldete zunächst keinen verwertbaren Dokumenttext; spätere falsche Zitate und Fundstellen belegen, dass ein Dateizugriff nicht mit überprüfter Originallektüre gleichzusetzen ist.
- **K-05:** EPUB nach PO-Aussage extrahiert, aber nicht verwertbar; PDF brachte mit `analyze_uploaded_documents` konkretere Texte, jedoch ungesicherte Seitenprovenienz und nach Testlingsaussage ein Zeichenbudget. Das ist **kein** Beweis, dass `view_knowledge_file` für EPUB funktioniert.

**Grenze:** `view_knowledge_file` ist aus T-02-P belegt, aber nicht in jedem DRS-Chat oder für jedes Format garantiert. Die Existenz einer Datei-ID-Suche ist weiterhin **nicht nachgewiesen**. IDs dürfen nicht erraten werden.

## Größe

v0.2.0: **17.879 Zeichen**. v0.2.1: **9.065 Zeichen**. v0.2.2: **9986 Zeichen**; weiterhin 44.1 % kürzer als v0.2.0. Der geringe Wiederanstieg ist bewusst fachlich priorisiert.

## Methodische Einschränkung

Schon v0.2.1 änderte zwei Variablen zugleich (Werkzeugreihenfolge und Promptlänge). v0.2.2 stellt zusätzlich fachliche Schutzregeln und Statusregeln wieder her. Aus einem künftigen PASS allein lässt sich **nicht kausal** die Wirkung der Werkzeugreihenfolge oder der Kürzung bestimmen. Bestehende Orakel und Test-Fixures bleiben unverändert.

## Verweis zum nächsten Test

`docs/testing/T04-R1_DRS_v0.2.2_PLAN.md` beschreibt den nächsten **noch nicht durchgeführten** gezielten Test auf `drs-ki-test` unter unverändertem T-04-Prompt, -Korpus und -Orakel. Kein Anspruch auf vorhandene Administratorrechte.
