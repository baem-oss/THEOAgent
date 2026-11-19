# DRS:KI-Toolquellen – QE-Reviewpaket

Stand: 13.11.2026. Enthält **7 unterschiedliche Quellcodes**, davon **6 unveränderte Upload-Inhalte** und **1 als Abschrift gekennzeichneten Chat-Quellcode** (TYPO3). Dateien dienen allein dem Review; keine Laufzeittests oder Rechtsfreigabe zur Veröffentlichung/Codeübernahme.

## Vollständigkeit und Provenienz

Alle Dateien unter `sources/uploaded/` sind Byte-für-Byte-Kopien der Nutzereingaben (nur der Dateiname ist aussagekräftiger gewählt). `sources/chat_transcription/08_typo3_document_tools_v0_3_2_CHAT_ABSCHRIFT.py` ist aus dem im Chat eingefügten Code übernommen und deshalb **keine Originaldatei**. Prüfsummen siehe `MANIFEST.json`.

**Bewusst ausgelassen:** `Eingefügter Text(20261113-130910).txt` ist byte-identisch mit `Eingefügter Text(20261113-130520).txt` (SHA-256: `de29ea08cfc4b9d4f5136fd7ebe3246886b2cd98b9364fffe4077c75120c413c`). Das Faster-Werkzeug liegt nur einmal bei.

## Reviewauftrag

1. Implementierungsbefunde pro Tool gegen Quellcode verifizieren, keine Aussagen zur Laufzeitfähigkeit aus bloßer Codeansicht ableiten.
2. THEOBald-Nutzung auf DRS:KI unter fehlenden Adminrechten und bestehende Tools gegen eigenständige Entwicklungen abgrenzen.
3. Sicherheitsrisiken (SSRF/Redirects, DNS-Rebinding, Konfiguration), Belegbarkeit (Snippet vs. Originaltext, Kürzungen), Kontextbudget und Fehlerzustände prüfen.
4. Rechtliche Lizenzlage offen lassen, sofern kein Lizenznachweis vorliegt.
5. Architekturvorschlag in `ARCHITEKTURVORSCHLAG.md` unabhängig reviewen.

**SSOT:** Das THEOBald-GitHub-Repository, Branch `drs-ki-test`. Dieses ZIP ist ein Review-Anhang, kein eigenständiger SSOT.