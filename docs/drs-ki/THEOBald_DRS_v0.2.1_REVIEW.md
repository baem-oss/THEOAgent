# THEOBald DRS – Werkzeug- und Längenreview v0.2.1

**Stand:** 12.11.2026 · **Branch:** `drs-ki-test` · **Status:** ungetesteter Testkandidat.

## Entscheidung nach PO-Feedback

1. **Leseweg:** Die DRS-Baseline T-02-P dokumentiert, dass `analyze_uploaded_documents` mehrfach unzureichend war, die anschließende, nach Nutzerwiderspruch beobachtete Nutzung von zwei `view_knowledge_file`-Aufrufen aber eine korrekte Lektüre ermöglicht hat. Darum wird `view_knowledge_file` **bedingt bevorzugt** und nach Analysefehlern als gezielter alternativer Leseweg angewiesen. Werkzeugverfügbarkeit ist im jeweiligen Chat zu prüfen; es gibt keine generelle Zusage, dass die Funktion verfügbar ist.
2. **Keine Scheindiagnose:** Eine Unlesbarkeits-/Budgetmeldung von `analyze_uploaded_documents` beschreibt zunächst nur **diesen Werkzeugpfad**, nicht den Dateiinhalt oder die Dateiqualität.
3. **Länge:** v0.2.0 umfasst **17.879 Zeichen**, v0.2.1 **9065 Zeichen**, eine Kürzung um **49.3 %**. Wiederholte Erläuterungen und Stilregeln wurden verdichtet, nicht die fachlichen sieben Kernverfahren entfernt.

## Bewusst erhalten

- Belegstatus Original geprüft / Sekundärquelle geprüft / nicht verifiziert
- Zitiergenauigkeit, keine erfundenen Seiten und keine Vermischung von PDF-, Druckseiten oder Zeichenbudget
- Kritische Trennung historischer, kultischer, rechtlicher und exegetischer Aussagen
- Fachverfahren aller sieben THEOBald-Skills
- Freigabe-/Freeze-Trennung
- Transparente System- und Werkzeuggrenzen

## Einordnung

Die Funktion `view_knowledge_file` wurde in einem früheren Test **tatsächlich beobachtet**. Ihre Verfügbarkeit über alle Uploads, Formate, Chatinstanzen oder Benutzerprofile ist nicht bestätigt. Die Priorisierung ist eine **zu prüfende Hypothese**, kein bereits bewiesener Fix. Kürzung ist ebenfalls nicht gleichbedeutend mit besserer Genauigkeit. V0.2.0 und die bestehenden Testberichte/Orakel bleiben unverändert. `main` unverändert.
