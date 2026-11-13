# DRS:KI-Erprobung – THEOAgent

**Stand:** 13.11.2026  
**Status:** Übernommener Arbeitsstand zur weiteren Erprobung, **keine Architektur- oder Produktfreigabe**  
**Arbeitsbranch:** `drs-ki-test`  
**SSOT:** `baem-oss/THEOAgent`, gemäß [Projektprozess](../WORKFLOW.md).

## Verbindliche Grundlage

- [Requirements-Baseline v1.2.0](../requirements/BASELINE.md) (PO-freigegeben am 10.11.2026).
- [Traceability](../requirements/TRACEABILITY.md), [Abnahmeprofil](../requirements/ACCEPTANCE_PROFILE.md).
- Die bestehenden THEOBald-Komponenten, insbesondere der experimentelle SourceGuard, sind **Referenzimplementierungen** im Repository [baem-oss/THEOBald](https://github.com/baem-oss/THEOBald). Die dortige Branch-/Pipe-Situation ist getrennt von der THEOAgent-Requirements-SSOT zu behandeln.

## Übernommene Unterlagen

1. [Architekturvorschlag vom 13.11.2026](ARCHITEKTURVORSCHLAG_2026-11-13.md) – nicht freigegeben; durch den QE teilweise beanstandet.
2. [Unabhängiger QE-Architektur-Review vom 13.11.2026](reviews/QE_ARCHITEKTUR_REVIEW_2026-11-13.md) – historischer Reviewbeleg, unverändert übernommen; maßgebliche Findings F-C1 (kritisch) sowie F-A1, F-C2 bis F-C7.
3. **Quellcode-Belege (separates, nicht öffentliches Reviewpaket)** – sieben DRS:KI-Implementierungen, davon sechs aus Nutzeruploads, eine als Chat-Abschrift. Sie sind wegen ungeklärter Nutzungsrechte **nicht** Bestandteil des öffentlichen GitHub-Repositories. Ursprünglicher Dateiname: `THEOBald_DRS-KI_QE_Quellcodes_2026-11-13.zip`.
4. [Herkunft des QE-Pakets](evidence/README_QE_PAKET.md).
5. [Findings-Disposition und P0-Plan](P0_MACHBARKEIT_UND_FINDINGS.md) – Arbeitsvorschlag, keine PO-Abnahme.

Das Review-ZIP enthält nur eine Faster-Fassung (identische Dublette ausgeschlossen). **Keiner der fremden Quellcodes wird im öffentlichen Repository als Datei bereitgestellt.** Früher versehentlich committe Reviewkopien wurden aus dem Branch-Arbeitsbaum entfernt; da Git-Historie bestehen bleibt, bedarf eine gegebenenfalls notwendige Historienbereinigung einer gesondert abgestimmten Maßnahme.

## Fachlicher Zwischenstand

- Die Werkzeuge gestatten in unterschiedlichem Umfang Treffer-, Snippet-, Originalauszugs- und Dokumentzugriff.
- Keine der gesichteten DRS:KI-Werkzeugimplementierungen belegt allein die SourceGuard-konforme, technisch erzwungene Prüfung.
- Das vorgeschlagene promptbasierte Verifikationsverfahren genügt **nicht** als Ersatz für den bestehenden SourceGuard (QE F-C1).
- Auf DRS:KI ist ein **Erkundungspilot** mit als ungesichert bezeichneten Evidenzstufen denkbar. Ein **quellenverifizierter Betrieb** ist nicht freigegeben.
- Rechte, Tool Callbacks, Funktions-/Pipe-Installation, Modellverhalten, Datenflüsse und Lizenzrechte sind noch praktisch bzw. organisatorisch zu prüfen.

## Regeln für die Weiterarbeit

1. Keine Änderungen an der freigegebenen Requirements-Baseline durch die Übernahme.
2. Keine Übernahme fremden DRS:KI-Codes in produktive Komponenten ohne Rechteklärung. Das Verzeichnis `evidence/sources/` dient ausschließlich der Prüfung.
3. Unterscheidung von `TREFFER`, `AUSZUG` und `TECHNISCH_VERIFIZIERT`; letzteres nur bei technischem Nachweis. Eine promptbasierte Selbstdeklaration ist keine Garantie.
4. SourceGuard nicht neu erfinden: Eignung der bestehenden Implementierung und notwendige Adapter zuerst prüfen.
5. Kein Adminzugriff voraussetzen und keine Laufzeitergebnisse behaupten, die nicht auf DRS:KI erhoben wurden.
6. QE findet und begründet Beanstandungen; der PO entscheidet über fachliche Baselines und Freigaben. Der QE setzt keine Commit-SHAs.

## Fortsetzung

Zuerst den [P0-Machbarkeitstest](P0_MACHBARKEIT_UND_FINDINGS.md) durchführen. Erst danach Architekturentscheidungen treffen.
