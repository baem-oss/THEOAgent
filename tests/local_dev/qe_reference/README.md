# QE-Testskripte SourceGuard v0.5.5-dev3 (Agent 0.2.0-dev7)

Isolierte Reproduktionstests zum QE-Review vom 27.11.2026. Die Pipe wird **unverändert** geladen;
Open WebUI wird gestubbt, Werkzeuge und Modell sind simuliert (keine Live-Tests).

Ausführen im Repository-Wurzelverzeichnis (Branch `local-dev`, Commit `ab93b81`):

    pip install pydantic
    SG_PIPE=tools/local_dev/sourceguard_pipe_v0_5_5_dev3.py python3 qe_tests.py

Ergebnis: Markdown-Tabelle (ID, Testart, Erwartet, Tatsächlich, PASS/FAIL/PARTIAL/INFO).
Referenzlauf: `qe_testergebnisse.md` (SHA-256 des Testobjekts in der ersten Zeile).