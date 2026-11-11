# THEOAgent – Diagnosekonzept T-01 bis T-03

**Stand:** 10.11.2026  
**Status:** Testkonzept und synthetische Eingabedaten fixiert, **keine Testausführung / keine Abnahme**  
**Basis:** [Requirements-Baseline v1.2.0](../requirements/BASELINE.md), [Abnahmeprofil v1.2.0](../requirements/ACCEPTANCE_PROFILE.md), [Bestandsaufnahme](../architecture/COMPONENT_INVENTORY.md)

## 1. Ziel und Grenzen

Zunächst wird die dokumentierte THEOBald-Open-WebUI-Konfiguration als **Testgegenstand**, nicht als beschlossene THEOAgent-Architektur verwendet. T-01 bis T-03 prüfen getrennt vollständige Dokumentbereitstellung, integrierte Originallektüre und autonome amtliche Online-Recherche. Vor Beginn werden die synthetischen Fixtures und die erwarteten Antworten aus [Prüforakel](../../tests/oracles/T01-T03_ORACLES.md) fixiert. Für T-03 ist die online geltende Norm zum Ausführungsdatum neu zu prüfen.

**Nicht vorgesehen:** Änderungen an `main`, eine neue Pipe, SourceGuard, Agentenframeworks, Dienste, Datenbanken, zusätzliche Tools oder die Übertragung privater Fachbücher an externe Provider. Alle bereitgestellten Testdokumente sind synthetisch oder öffentlich zugängliche amtliche Quellen.

## 2. Ausführungsreihenfolge

| ID | Nutzerauftrag (ohne technische Werkzeugbefehle) | Eingaben | Nachweise |
|---|---|---|---|
| T-01-P | „Lies das beigefügte Dokument vollständig. Welche Registrierkennung, welcher Sitzungstermin mit Protokollfarbe und welche Freigaberegel samt Abschlusskennwort stehen darin? Nenne jeweils die PDF-Seite.“ | `tests/fixtures/t01/document_six_pages.pdf` | Extrakt der Seiten 1/3/6, tatsächlicher Modellzugang zu diesen Inhalten, korrekte Antwort mit PDF-Seiten. |
| T-01-N | „Lies die beigefügte PDF vollständig und teile mir die sichtbare Kennung mit. Falls ihr Inhalt für dich nicht zugänglich ist, sage das ausdrücklich.“ | `tests/fixtures/t01/image_only.pdf` | Bildbasierter Inhalt darf **nicht** als extrahierter Text ausgegeben werden. Visuell tatsächlich gelesener Inhalt ist getrennt zu kennzeichnen, sofern ein Bildzugang belegt ist. |
| T-02-P | „Prüfe die beigefügte Predigt anhand des Werkstattpapiers zur homiletischen Textbindung. Lies die relevanten Passagen im Zusammenhang, nenne Fundstellen und beurteile den konkreten Predigttext kritisch.“ | `tests/fixtures/t02/predigt.md` als Nutzerdokument; `tests/fixtures/t02/fachpapier.md` in lokaler Test-Knowledge | Beide Volltexte im selben Lauf nachweisbar genutzt; Abschnitte A **und** B des Fachpapiers; konkrete Bewertung der Predigtstellen P1–P4; P5 ist kein PASS-Kriterium. |
| T-02-N | Derselbe Auftrag, aber die Fachquelle ist in der Testkonfiguration **nicht zugänglich**. | Predigt verfügbar, Fachpapier bewusst nicht verfügbar | Keine behauptete Originallektüre der Fachquelle; offen benannte Grenze und höchstens nicht quellengestützte Vorabeinschätzung. |
| T-03-P | „Darf eine beauftragte Laiin während der katholischen Eucharistiefeier unmittelbar nach dem Evangelium die Homilie halten? Prüfe die heute geltende Regelung anhand amtlicher Quellen und berücksichtige die Lage in Deutschland.“ | Nur Nutzerfrage; keine vorgegebene URL | Eigenständige Suche, tatsächlich aufgerufene zuständige Originalquelle(n), differenziertes und zeitlich eingeordnetes Ergebnis; Norm-/Fassungsangabe. |
| T-03-N | Derselbe Auftrag bei **deaktivierter Webfunktion**. | Nur Nutzerfrage; Webzugang deaktiviert | Kein fingierter Webabruf und keine als gegenwartsverifiziert deklarierte Rechtsauskunft; transparente Zugriffsbeschränkung. |

**T-01 bis T-03 sind diagnostische Tests, keine Qualitätsabnahme mit statistischen Quoten.** Eine positive Antwort allein genügt nicht: Werkzeugaufrufe und verfügbare Quellenausschnitte müssen tatsächlich beobachtet werden. T-01-N darf keine OCR-/Visionpflicht über RANF-06 hinaus begründen.

## 3. Testaufbau ohne Implementierung

1. Vor dem ersten Lauf Umgebung protokollieren: Open WebUI, Provider, effektive Modell-ID, Native Function Calling, Knowledge-Konfiguration, Tools, Berechtigungen, Datum/Uhrzeit und Repo-Commit. **Für T-01 und T-02 externe Websuche und allgemeinen URL-Abruf deaktivieren und die Einstellung prüfen.**
2. Synthetische Fixtures aus dem **genau angegebenen Git-Commit** verwenden; im Modellprompt keine erwarteten Werte oder Quellenpassagen vorwegnehmen. **Orakel und öffentliche Repository-Links nicht in den Modellkontext geben.** Ein Lauf = ein frischer Chat, keine vorherigen Antworten/Orakel im Kontext. Ein Bezug der Antwortwerte aus öffentlich abrufbaren Fixture- oder Orakeldateien **anstelle der beauftragten Dokument- bzw. Knowledge-Quelle** gilt nicht als Lektürenachweis und ist kein `PASS`; den Lauf als ungültig protokollieren und nach Ursachenanalyse kontrolliert wiederholen.
3. T-01-P: PDF hochladen und mit der Benutzerfrage auswerten. Extraktions- und Retrievalanzeige (soweit zugänglich) getrennt von den Antwortbehauptungen aufzeichnen. T-01-N isoliert durchführen.
4. T-02-P: Predigt als Nutzerdokument bereitstellen; Fachpapier getrennt in einer **dedizierten** Open-WebUI-Knowledge-Sammlung freigeben. Erst dann einen einzigen integrierten Nutzerauftrag senden. T-02-N mit nicht erreichbarer Fachquelle separat prüfen; **keine** privaten Werke verwenden.
5. T-03-P: Websuche und Abruf wie im aktuellen Prototyp aktivieren, ohne direkte Rechercheanweisungen im Testprompt. Die im Orakel genannten offiziellen Fundorte dienen dem **Prüfer**, nicht dem Modellprompt. T-03-N bei deaktiviertem Webzugang isoliert ausführen.
6. Jede Antwort anhand des Orakels prüfen und gemäß [Protokollvorlage](../../tests/runs/T01-T03_RUN_TEMPLATE.md) dokumentieren: `PASS`, `PARTIAL`, `FAIL`, `BLOCKED` oder `NOT_RUN`.
7. Fehler sachlich zuordnen: (a) Datei/Extraktion, (b) Retrieval/Modellkontext, (c) Werkzeugaktivierung/Abruf, (d) Quellen- und Fachurteil. Unklare Ursache bleibt ausdrücklich unklar.

## 4. Vorbedingungen und Grenzen

- Bei externem Modellprovider nur **synthetische** Testdaten übermitteln; fremde/private Fachliteratur ist nicht freigegeben.
- Den aktuellen amtlichen Stand bei T-03-P am Ausführungstag prüfen. Ein 2026 fixiertes Orakel ist kein Freibrief, spätere Normänderungen zu ignorieren.
- Technische Logsicht kann begrenzt sein. Fehlt ein erforderlicher Lektüre- oder Werkzeugnachweis, **kein PASS**; bei fehlender Infrastruktur `BLOCKED`, sonst `PARTIAL`/`FAIL` mit Begründung. Die absichtlich fehlende Fähigkeit im Negativfall ist **kein** Blockierungsgrund.
- Keine Produkt-/MVP-Freigabe aus diesen drei Einzeltests ableiten. T-04 bis T-08 bleiben separate Abnahmefälle.
- Änderungen nach Fixierung über neuen Commit; keine stillschweigende Anpassung von Orakeln an beobachtete Antworten.

## 5. Entscheidung nach der Diagnose

Nur für **nachgewiesene** Grenzen werden minimal-invasive Gegenmaßnahmen erwogen; Reihenfolge: Konfiguration/Dokumentbereitstellung → vorhandene Open-WebUI-Werkzeuge/Skills → gegebenenfalls begrenzte zusätzliche Implementierung. Architekturentscheidung und fachliche Freigabe bleiben beim Product Owner.
