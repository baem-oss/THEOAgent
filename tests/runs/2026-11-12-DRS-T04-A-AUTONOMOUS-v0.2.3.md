# T-04 – Variante A: autonome Werkzeugwahl

**Datum:** 12.11.2026 · **Branch:** `drs-ki-test` · **Status:** **BLOCKED** (Dokumentenzugriff)

## Testaufbau und Evidenz

Der PO berichtet einen neuen DRS:KI-Allrounder-Chat „Prüfung von Behauptungen“ mit angehängter Datei `belegkorpus.md` (2,9 KB) und dem unveränderten T-04-Testprompt mit acht Aussagen aus `docs/testing/T04_DRS_PROMPT.md`.

**Promptversion:** In der vorangehenden Testvereinbarung wurde Variante A mit **v0.2.3** vorgesehen, nachdem der QE ursprünglich v0.2.1 angeregt hatte. Ein separater technischer Nachweis, dass v0.2.3 tatsächlich im Systemprompt-Feld aktiv war, liegt für diesen Chat nicht vor; dies bleibt ein Konfigurationsvorbehalt.

## Beobachtete Erstantwort

**Sichtbarer Werkzeugaufruf:** `analyze_uploaded_documents`. Ein `view_knowledge_file`-Aufruf ist in der übermittelten Chatansicht nicht sichtbar. Es wurde keine Werkzeug-Eingabe-/Ausgabe-Payload übermittelt.

> Die beigefügte Datei „belegkorpus.md“ enthält keinen lesbaren Textinhalt. Daher kann keine der acht Behauptungen anhand dieser Quelle geprüft werden.
>
> **Ergebnis für alle Behauptungen: „nicht überprüfbar“**
>
> Begründung: Da das Dokument keine lesbaren Passagen enthält, lässt sich weder bestätigen noch widerlegen, ob die genannten Aussagen im Text stehen oder nicht. Es ist kein Zugriff auf Abschnitte, Zitate oder Inhalte möglich. Eine Prüfung der Behauptungen anhand dieser Quelle ist daher nicht durchführbar.
>
> Bitte laden Sie eine lesbare Version der Datei hoch, falls Sie eine Prüfung anhand des Textes wünschen.

## Bewertung

- **Autonome Werkzeugwahl:** `analyze_uploaded_documents` als erster sichtbarer Pfad; **kein** beobachteter Wechsel zu `view_knowledge_file`.
- **Dokumentzugriff:** keine nachgewiesene Originallektüre. Aussage über einen angeblich unlesbaren Dateiinhalt ist unzulässiger Schluss aus nicht erfolgreichem Werkzeugzugriff; der im Repository vorhandene synthetische Korpus enthält lesbaren Text.
- **T-04-Orakel:** **BLOCKED**. Die acht pauschalen „nicht überprüfbar“ sind kein fachlich bewertbarer 0/8- oder 8/8-Lauf, weil der Korpus nicht gelesen wurde.
- **Grenzen:** Die Verfügbarkeit von `view_knowledge_file` in dieser Sitzung, interne Dateibindung, Modellversion und tatsächlich aktive Systemprompt-Rolle sind aus der übermittelten Ansicht nicht nachgewiesen. Keine kausale Aussage darüber, warum der Werkzeugwechsel ausgeblieben ist.

## Folgeschritt

**Variante B** in einem separaten, frischen Chat: gleicher Systemprompt (v0.2.3, ausdrücklich überprüfen), identische Datei und derselbe Acht-Aussagen-Auftrag, aber davor ein ausdrücklicher nutzerseitiger Hinweis zur Erstlektüre mit `view_knowledge_file`. **Diagnostischer Vergleich, kein streng identischer Orakel-Test**, da Nutzerprompt geändert.

**SSOT:** `drs-ki-test`; `main`, bisherige Testberichte, Testkorpus und Orakel unverändert.
