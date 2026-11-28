# PO-Freigabe – Requirements-Baseline v2.0.0

**Datum:** 28.11.2026  
**Entscheidung:** „Freigabe erteilt durch PO“ im Projektchat nach Vorlage der abschließenden QE-Sichtprüfung und SE-Empfehlung.  
**Freigabegegenstand:** [Revision 3, local-dev @ 71a4c811b1f682e2ec3b3200836411de8adb016e](https://github.com/baem-oss/THEOAgent/commit/71a4c811b1f682e2ec3b3200836411de8adb016e). Die vier geprüften Blobs wurden vom SE unabhängig abgeglichen.

Die Freigabe bestätigt die Baseline einschließlich N0–N4, zulässiger richtiger Referenzen aus Modellwissen, 90 % fachlicher Gebrauchstauglichkeit, 100 % Reaktionsziel für technisch bearbeitbare Fälle, Nulltoleranz für schwere Fehler im Korpus, zulässigen Web-Fallback, Zielgruppe haupt- und ehrenamtlicher kirchlicher Mitarbeitender sowie SP-01 einschließlich Testdatenbeschränkung bis zur Betreiberklärung. N-04 bleibt DEFERRED / TO_CHECK; kein Blocker der lokalen Entwicklung. Provider-/Rechtsklärung, Korpus, Prüfer, Laufzeit-/Wartbarkeitsgrenzen und Fachstandardfestlegung bleiben offene Abnahmevoraussetzungen.

Die abschließende QE-Sichtprüfung meldet keine freigaberelevanten Mängel; N-01, N-02, N-03, N-05, N-06, N-07 geschlossen, N-04 zulässig zurückgestellt. Zwei nicht freigaberelevante Hinweise werden gemäß SE-Empfehlung in der Abnahme berücksichtigt: vollständiger interner Pipe-Ausfall zählt als FAIL; tragende Referenzen werden im Orakel vorab definiert.

Verbindliche Einstiegspfade: [Baseline](BASELINE.md), [Abnahmeprofil](ACCEPTANCE_PROFILE.md), [Migration](MIGRATION.md), [Traceability](TRACEABILITY.md). Die exakt geprüften historischen Entwurfsartefakte sind unter [v2.0.0-draft](v2.0.0-draft/) unverändert erhalten. Die Überführung in die freigegebenen Einstiegspfade enthält redaktionelle Status-/Linkanpassungen und die beiden genannten Abnahmepräzisierungen. Die alte Baseline bleibt im Git-Verlauf erhalten ([main vor Ablösung](https://github.com/baem-oss/THEOAgent/commit/ebb710206d8851dcb04331f3e87cb9ca1426d72b)).

**Abgrenzung:** Requirements-Freigabe, keine Produkt-/Implementierungs-/Qualitätsabnahme und keine DRS:KI-Deploymentfreigabe. Keine experimentellen Pipe-Codeänderungen werden übernommen. Keine neuen Live-Tests. Die Originalberichte des QE aus dem Chat sind noch nicht als separate Dateien archiviert; die historischen Dispositionen und dieser Freigabevermerk dokumentieren die Ergebnisse.
