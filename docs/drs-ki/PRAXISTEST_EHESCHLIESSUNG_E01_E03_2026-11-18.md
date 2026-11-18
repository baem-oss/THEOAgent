# THEOAgent DEV – Praxistests Eheschließung E-01 bis E-03

**Testdatum:** 18.11.2026  
**Umgebung:** DRS:KI DEV · THEOAgent Dev  
**Arbeitsbranch / SSOT:** `drs-ki-test` · `baem-oss/THEOAgent`  
**Dokumenttyp:** Ergebnisprotokoll (keine Produktfreigabe, kein technischer Quellenverifikationsnachweis)  
**Bewertungsbasis:** Drei vom PO bereitgestellte vollständige Chat-Exporte mit sichtbarer Werkzeugspur; Auswertung im SE-Chat am 18.11.2026. Die Live-Artefaktversion von THEOAgent Dev ist nicht unabhängig ermittelt; der verwendete Quellenhinweis entspricht der v0.3.10-Regel.

## 1. Zusammenfassung

| Test | Aufgabe | Bewertung | Wichtigster Befund |
|---|---|---|---|
| E-01 | Erstes Traugespräch, beide katholisch und unverheiratet | **PARTIAL** | Pastoral gut; Rolle/Traubefugnis des Diakons und kirchenrechtliche Präzision verbesserungsfähig |
| E-02 | Katholisch-evangelische Trauung mit Diakon und evangelischer Pfarrerin | **FAIL** | Erlaubtheit/Gültigkeit sowie kanonische Form/Formdispens verwechselt |
| E-03 | Katholische Eheschließung nach Scheidung einer nur standesamtlich geschlossenen Vorehe | **PARTIAL** | Möglichen Formmangel erkannt, Ehefreiheit aber vorschnell festgestellt |

**Querschnitt:** Pastorale Nutzbarkeit in allen drei Fällen überzeugend; rechtsverbindliche Einzelfallauskünfte noch nicht verlässlich. Der allgemeine Quellenhinweis wurde in allen drei Antworten ausgegeben. Das bereits bekannte Finding **F-C1 (CRITICAL / OPEN)** bleibt bestehen; die drei Tests sind keine neue Prüfung der expliziten Tool-Aufrufbarkeit.

## 2. E-01 – Erstes Traugespräch

**Unveränderter Testprompt:**  
> Ein junges Paar möchte katholisch heiraten. Beide sind katholisch und bisher nicht verheiratet. Sie bitten mich als Diakon um ein erstes Traugespräch. Was sollte ich mit ihnen besprechen? Welche kirchenrechtlichen Voraussetzungen müssen erfüllt sein, und wie kann ich das Gespräch pastoral sinnvoll gestalten?

**Nachgewiesene Aufrufe:** `view_skill` ×2 (Theologische Grundlagen, Pastorale Sensibilität), `get_websearch_results` ×1. Kein sichtbarer `read_source`, `verify_evidence` oder `review_evidence`-Aufruf.

**PASS:** Verständlicher, zugewandter Gesprächsaufbau (Beziehung, Glaube und Ehe, Formalitäten, Liturgie); Grundverständnis der katholischen Ehe weitgehend richtig; Hinweis zur eigenständigen Quellenprüfung vorhanden.

**E-01-F1 – MAJOR:** Die konkrete Rolle des Diakons und seine gültige Trauassistenz einschließlich erforderlicher territorialer Befugnis/Delegation wurden nur verkürzt dargestellt. DRS-Rechtssammlung Abschnitt 3.1 ist hierfür einschlägig.

**E-01-F2 – MINOR:** Die Nennung von cann. 1083–1087 CIC deckt das ebenfalls erwähnte Verwandtschaftshindernis (insbesondere can. 1091) nicht ab.

**Ergebnis:** **PARTIAL**; gute pastorale Gebrauchstauglichkeit, keine belastbare rechtsverbindliche Einzelfallberatung.

## 3. E-02 – Konfessionsverschiedene Ehe

**Unveränderter Testprompt:**  
> Eine katholische Frau und ein evangelischer Mann möchten kirchlich heiraten. Sie wünschen sich eine ökumenisch gestaltete Trauung, bei der sowohl ich als katholischer Diakon als auch die evangelische Pfarrerin mitwirken. Was ist kirchenrechtlich und liturgisch möglich? Welche Genehmigungen sind erforderlich, und wie sollte ich das Paar beraten?

**Nachgewiesene Aufrufe:** `view_skill` ×4 (Theologische Grundlagen, Liturgische Texte, Pastorale Sensibilität, Qualitätskontrolle), `get_websearch_results` ×1. Keine sichtbaren SourceGuard-Lese-/Verifikationsaufrufe.

**PASS:** Zwei grundsätzlich mögliche Formen (katholische Trauung mit evangelischer Mitwirkung oder nichtkatholische Feier mit katholischer Mitwirkung) wurden erkannt; pastorale Beratung und Koordinationsvorschlag sinnvoll; Quellenhinweis vorhanden.

**E-02-F1 – MAJOR:** Die Erlaubnis zur konfessionsverschiedenen Ehe wurde als Gültigkeitsvoraussetzung dargestellt. Nach can. 1124 CIC betrifft sie grundsätzlich die **Erlaubtheit**. Die pauschale Zuständigkeitszuweisung an das Offizialat übergeht die DRS-Regelung, wonach Seelsorger mit allgemeiner Traubefugnis die Erlaubnis grundsätzlich selbst erteilen können (DRS 2.10).

**E-02-F2 – MAJOR:** THEOAgent verknüpfte die Formdispens zu pauschal mit dem *Ort* (evangelische Kirche). Für die Einordnung ist entscheidend, in welcher Form und durch wen der Konsens entgegengenommen wird. Die Frage des Trauortes ist davon zu unterscheiden (DRS 3.2–3.3; cann. 1108, 1127 CIC).

**E-02-F3 – MINOR:** Erklärungen und Verpflichtungen nach can. 1125 CIC (Glaubensbewahrung, Kinder, Kenntnis des nichtkatholischen Partners, Eheverständnis) wurden nicht hinreichend dargestellt.

**E-02-F4 – MINOR:** Das Verbot einer doppelten Konsenserfragung durch beide Geistlichen (can. 1127 § 3 CIC) hätte ausdrücklich genannt werden sollen.

**Ergebnis:** **FAIL** wegen zweier folgenrelevanter Rechtsfehler trotz gefundener DRS-Quelle.

## 4. E-03 – Vorehe, Scheidung, möglicher Formmangel

**Unveränderter Testprompt:**  
> Ein katholischer Mann und eine katholische Frau möchten kirchlich heiraten. Die Frau war bereits standesamtlich mit einem evangelischen Mann verheiratet, ist inzwischen geschieden und hatte damals keine kirchliche Trauung. Der Mann war bisher nicht verheiratet. Beide gehen davon aus, dass die frühere Ehe kirchenrechtlich keine Rolle spielt, weil sie nur standesamtlich geschlossen wurde. Wie muss ich als Diakon diese Situation beurteilen, welche Fragen sind zu klären und wie kann ich das Paar pastoral begleiten?

**Nachgewiesene Aufrufe:** `view_skill` ×3 (Theologische Grundlagen, Pastorale Sensibilität, Qualitätskontrolle). **Keine sichtbare Webrecherche, Originallektüre oder SourceGuard-Prüfung.**

**PASS:** THEOAgent erkennt, dass die standesamtliche Vorehe rechtlich zu prüfen ist; unterscheidet grundsätzlich kanonische Formpflicht und mögliche Dispens; behandelt die Beteiligten respektvoll und bietet praktische Gesprächsfragen; Quellenhinweis vorhanden.

**E-03-F1 – MAJOR:** Aus der möglichen Abwesenheit einer Formdispens wurde zu unmittelbar die Ehefreiheit abgeleitet. Erforderlich sind Status- und Dokumentenprüfung sowie die zuständige kirchliche Feststellung eines Formmangels; die Feststellung darf nicht allein durch den beratenden Diakon ersetzt werden. Historisches Datum und gegebenenfalls damaliger formaler Kirchenaustritt können eine Rolle spielen (geänderte Formpflicht seit April 2010).

**E-03-F2 – MINOR:** Der Hinweis „kurze Dokumentation der Formungültigkeit → normale Trauungsvorbereitung“ ist verfahrensrechtlich zu knapp; insbesondere die verbindliche Trauterminzusage muss bis zur Klärung der Ehefreiheit zurückstehen.

**Ergebnis:** **PARTIAL**; sachgerechte Ausgangsfrage, aber rechtlich zu weitgehende Schlussfolgerung.

## 5. Querschnittsfindings und Einordnung

| ID | Befund | Relevanz / Status |
|---|---|---|
| F-C1 (bestehend) | Tatsächliche Quellenlektüre und Toolereignisse werden nicht technisch verbindlich durchgesetzt; Web-Digest oder Skill-Lektüre ersetzen keine Originalquellenprüfung | **CRITICAL / OPEN; unverändert** |
| E-RECHT-01 | Unzureichende Anwendung des konkreten DRS-Partikularrechts und fehlende Trennung von Erlaubtheit, Gültigkeit, Dispens und Zuständigkeit | **MAJOR; Beobachtung aus E-01/E-02** |
| E-RECHT-02 | Zu frühe statusrechtliche Schlussfolgerung ohne amtliche Feststellung bei Vorehe | **MAJOR; E-03** |

**Methodische Grenze:** Diese Bewertung ist eine fachliche Analyse der sichtbaren Modellantworten und Werkzeugspur. Sie ist weder ein vollständiger DRS:KI-Serverlognachweis noch eine Aussage darüber, was die Plattform technisch hätte aufrufen können. Fehlender sichtbarer Aufruf wird als **nicht nachgewiesen** bewertet, nicht als universelle Unmöglichkeit.

## 6. Entscheidung / weiteres Vorgehen

1. **Ehe-Testreihe E-01 bis E-03 zunächst abschließen.** Kein weiterer ähnlicher Test ohne konkreten neuen Erkenntnisbedarf.
2. **Keine pauschale Prompt- oder Skillverschärfung auf Verdacht.** Die Rechtsfindings sind dokumentiert; vor einem Fix bestehende Verfahren und DRS-Quellenintegration prüfen.
3. **F-C1 unabhängig weiterführen:** Bereits nachgewiesene explizite SourceGuard-Aufrufbarkeit nicht erneut testen. Server-Gate SG-01 und ggf. SG-02 bleiben offen.
4. **Keine Freigabe:** DRS:KI DEV ist ein pastoraler Arbeitsprototyp; für belastbare kirchenrechtliche Auskünfte ist die Kontrolle des geltenden Originalrechts weiterhin notwendig.
5. **Keine Änderung** an Requirements v1.2.0, `main`, bestehenden Reviews, Werkzeugen oder Skills durch dieses Protokoll.

## 7. Quellen und Evidenz

**Primärquellen zur fachlichen Sollbewertung (nicht als von THEOAgent selbst gelesen ausgeben):**
- [Kommentierte Rechtssammlung DRS, 4.2.7 Ehe](https://rechtssammlung.drs.de/rechtssammlung/4-heiligungsdienst-liturgie-und-sakramente/42-sakramente/427-ehe.html), insbesondere 2.10 und 3.1–3.3.
- [CIC, cann. 1108–1123](https://www.vatican.va/archive/cod-iuris-canonici/deu/documents/cic_libro4_cann1108-1123_ge.html).
- [CIC, cann. 1124–1129](https://www.vatican.va/archive/cod-iuris-canonici/deu/documents/cic_libro4_cann1124-1129_ge.html).
- [DRS-Offizialat: Erläuterungen zu Eheverfahren](https://recht.drs.de/fileadmin/user_files/117/Dokumente/Offizialat/eheverfahren_erlaeuterungen.pdf).
- [Erzbistum Köln: Formmangel](https://www.erzbistum-koeln.de/erzbistum/offizialat/wiederheirat/gruende/formaler_mangel/formmangel/index.html) (historische Formpflicht/Verfahrenshinweise).

**Testevidenz:** Drei vollständige PO-Uploads am 18.11.2026 (jeweils Testprompt, sichtbare `view_skill`-/Web-Schnittstelle und Modellantwort), ausgewertet im SE-Chat. Die Uploads sind kein Bestandteil dieses GitHub-Commits und werden nicht als Repository-Artefakte ausgegeben.

**Dokumentationsstatus:** Ergebnisprotokoll; fachliche Findings dokumentiert, keine Implementierung und keine Nachtests vorgenommen.
