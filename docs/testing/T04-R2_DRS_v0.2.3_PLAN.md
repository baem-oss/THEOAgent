# T-04-R2 – Regression mit THEOBald DRS v0.2.3

**Status:** NOT_RUN · **Datum:** 12.11.2026 · **Branch:** `drs-ki-test`

## Unveränderter Aufbau

1. Neuer DRS:KI-Allrounder-Chat mit `docs/drs-ki/THEOBald_DRS_SYSTEMPROMPT_v0.2.3.md` als Nutzer-Systemprompt; Einbringungskanal soweit sichtbar dokumentieren.
2. Nur `tests/fixtures/t04/belegkorpus.md` hochladen; Upload- und Extraktionsanzeige sichern.
3. Wortgleich ausschließlich den Abschnitt **Nutzerprompt** aus `docs/testing/T04_DRS_PROMPT.md` senden, ohne Hinweise oder Orakel.
4. Die Erstantwort samt erstem sichtbaren Werkzeugnamen, Quellenanzeige und Fundstellen vollständig sichern, bevor interveniert wird.
5. **Unverändertes Prüforakel:** `tests/oracles/T04_DRS_ORACLE.md` (nie an Allrounder senden).

## Prüfkriterien

- Nr. 5: **widerlegt**, weil § 5 empirische Befunde ausdrücklich verneint.
- Nr. 6: **nicht überprüfbar**, weil das externe Werk im Korpus nicht behandelt wird.
- Nr. 7: **widerlegt**, weil der Satz in § 4.1 statt § 3.1 steht.
- Alle übrigen Nummern: gemäß fixiertem Orakel. **PASS nur bei 8/8** korrekten Klassifikationen ohne erfundene Zitate oder Fundstellen und mit tatsächlichem Lesezugriff.
- Werkzeugsteuerung unabhängig einordnen: `view_knowledge_file` direkt / nach Recovery / anderes / unklar.

## Grenzen

Ein Lauf erlaubt keine kausale Zuschreibung an die Promptänderung. Modell und Werkzeugverfügbarkeit soweit sichtbar erfassen; keine Änderung an Fixture, Orakel oder `main`.
