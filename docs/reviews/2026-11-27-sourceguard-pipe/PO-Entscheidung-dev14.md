# PO-Entscheidung: verhältnismäßige Qualitätssicherung (dev14)

Stand: 27.11.2026; PO-Freigabe im Projektchat erteilt. Keine Änderung der Requirements-Baseline v1.2.0, keine Produktivfreigabe.

Leitlinie: Ziel ist eine fachlich zuverlässige Antwort, nicht die maximal formal abgesicherte Antwort. Die SourceGuard-Pipe bleibt integraler Bestandteil der Verarbeitung; die technische Prüfung und die Ausgabe der Nachweise werden entkoppelt.

- Die zweiphasige Kommunikation (Steuerungs-JSON, Markdown) und die Evidenzregistrierung bleiben erhalten.
- Fachantworten bleiben quellenfundiert. Erforderliche Originallektüre, Werkidentität und vorhandene Quellenkennungen werden weiterhin geprüft. Eine geprüfte Originallektüre beweist keine semantische Vollprüfung.
- Bei gewöhnlichen Paraphrasen ohne expliziten Nachweisauftrag sind Belegkennungen optional; technische Belegkennungen und das automatisch erzeugte Quellenverzeichnis werden nicht angezeigt.
- Bei expliziten Nachweisaufträgen, wörtlichen Zitaten und konkreten Fundstellen bleiben erforderliche Belegbindung und Nachweisausgabe verbindlich (GR-01 bis GR-03). Nicht nachweisbare Wortzitate nicht ausgeben; fehlende notwendige Evidenz offenlegen.
- coverage nur bei tatsächlich verlangten Pflichtteilthemen. Nicht benötigte Abdeckungsmetadaten dürfen die Freigabe nicht blockieren. Werkidentitätsmetadaten werden nicht pauschal verworfen.
- Rein sprachliche Bearbeitung bleibt auftragsbezogen ohne neue Recherche möglich (GR-17).
- Bestehende Regeln für LOCAL_ONLY, Webauswahl, Werkzeuge, Budgets und Diagnose bleiben unverändert.
- Der QE prüft unabhängig, ob die Implementierung diese Entscheidung erfüllt und die Requirements-Baseline einhält. Er meldet Findings; Freigabe und Baseline bleiben beim PO.

Auslöser: Zwei dev13-Live-Erstanfragen zu Klippert mit explizitem Nachweisauftrag, vier registrierte Originalstellen je Lauf, keine Formatfehler/Abschneidungen, zweimalige coverage-Sperre pro Lauf, Laufzeiten 18,913 und 27,838 s. Die genaue fehlerhafte Metadatenform wurde nicht erfasst. Der allgemeine coverage-Check war in dev13 neu und auch ohne Pflichtteilthemen aktiv.

Implementierung: dev14, Commit 7186a39f7079d4110442970b251b51cd6e588da7. Umfang der Freigabe: Entwicklung und unabhängige Prüfung, nicht Produktivsetzung.
