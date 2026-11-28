# THEOAgent – Rollen, GitHub und verbindlicher Arbeitsstand

**Stand:** 28.11.2026  
**Status:** Verbindliche Projektarbeitsregel

## 1. Single Source of Truth (SSOT)

**Das Repository [`baem-oss/THEOAgent`](https://github.com/baem-oss/THEOAgent) ist die einzige verbindliche Quelle für den dokumentierten Projektstand.** Chatverläufe, externe Review-Notizen, übermittelte Dateien und lokale Arbeitskopien ersetzen diesen Stand nicht.

- **`main`:** maßgeblicher, vom Product Owner freigegebener Arbeitsstand. Ein Merge oder Commit auf `main` ist nicht automatisch eine fachliche Produkt- oder Testabnahme.
- **Review-/Entwicklungsbranches:** versionierte Vorschläge und Arbeitsstände; keine stillschweigende Ablösung von `main`.
- **Reviews unter `docs/reviews/`:** nachvollziehbare Prüfbelege und Empfehlungen, keine eigenständige normative Quelle für Requirements, Architektur, Code oder Releases.
- Bei Widersprüchen gilt der im Repository tatsächlich versionierte und vom Product Owner freigegebene Stand. Offene Abweichungen werden als Findings dokumentiert, nicht durch externe Notizen aufgelöst.

## 2. Zuständigkeiten

| Rolle | Zuständigkeit | Keine Zuständigkeit |
|---|---|---|
| **Product Owner** | Ziele, Prioritäten, fachliche Entscheidungen, Freigabe von Baselines und Releases | Keine Pflicht zur operativen Git-Pflege |
| **Software Engineer (ChatGPT)** | Änderungen entwerfen, implementieren, dokumentieren, Tests durchführen und wahrheitsgemäß protokollieren, im Repo committen, Review-Findings bearbeiten | Keine selbst erteilte fachliche Produktfreigabe |
| **Quality Engineer / Reviewer (Claude)** | Den **tatsächlich vorliegenden Repositorystand** unabhängig prüfen, konkrete Findings und reproduzierbare Nachweise berichten, Freigabe empfehlen oder ablehnen | **Keine Hoheit über Repositoryinhalt, Git-Commit-SHAs, Git-Blob-SHAs, externe SHA-256-Vorgaben, Commits, Merges oder PO-Freigaben** |

Ein Review-Urteil ist fachlicher Input für Entscheidungen des Product Owners. Es setzt die Spezifikation nicht außer Kraft und ändert das Repository nicht.

## 3. SHAs und Prüfsummen: Identifikatoren, keine QE-Vorgaben

- **Commit-SHAs und Git-Blob-SHAs werden durch Git aus den tatsächlichen Repositoryobjekten bestimmt.** Niemand legt diese Werte vorab als Sollwert fest. Insbesondere bestimmt oder genehmigt der QE keine Git-SHA.
- Der QE **darf und soll** den **vorgefundenen** Commit-SHA und gegebenenfalls Datei-/Blob-IDs als **Prüfreferenz** nennen. Das dient allein der Reproduzierbarkeit: „Welchen Stand habe ich geprüft?“
- Eine vom QE errechnete oder gemeldete **SHA-256-Prüfsumme einer Übergabedatei** ist eine optionale zusätzliche Transportkontrolle, **keine** normative Freigabebedingung und **kein** Ersatz für den im Repository gespeicherten Inhalt.
- Bei einem Widerspruch zwischen Upload, externem Prüfsummenhinweis und Repository wird die Abweichung offengelegt. Der Engineer legt den vom Product Owner zur Ablage bestimmten Inhalt korrekt im Repository ab; anschließend sind **Repositorypfad, Commit und dort gespeicherter Inhalt** maßgeblich. Es wird keine Übereinstimmung mit einer abweichenden externen Prüfsumme behauptet.
- Bereits archivierte Reviewberichte bleiben als historische Prüfbelege unverändert. Sachliche Korrekturen erfolgen über neue Berichte bzw. klar gekennzeichnete Folgedokumente; ein externer QE darf solche Korrekturen nicht im Repo erzwingen.

**Kurzregel: Der QE überprüft Git-Stände. Git-Stände richten sich nicht nach dem QE.**

## 4. Ablauf

1. Der Software Engineer erstellt Änderungen auf einem nachvollziehbaren Branch, dokumentiert Prüfungen und legt den Stand im Repository ab.
2. Der QE prüft genau diesen Stand, nennt die tatsächlich gesichteten Pfade und Commit-IDs und meldet begründete Findings; er kann eine Freigabe empfehlen, aber nicht selbst aussprechen.
3. Der Software Engineer bewertet und bearbeitet Findings; fachliche Konflikte und nicht begründbare Qualitätsgrenzen gehen an den Product Owner.
4. Nur der Product Owner entscheidet über die fachliche Baseline-/Releasefreigabe. Der Software Engineer setzt die Entscheidung im Repository um und dokumentiert sie.
5. Test- und Implementierungsabnahmen benötigen tatsächliche Nachweise. Weder ein grüner CI-Lauf noch ein positives QE-Urteil allein ist eine Produktabnahme.

**Änderungsprinzip:** Kleine, nachvollziehbare Änderungen; keine nachträgliche Umdeutung historischer Reviewberichte und keine externe „Schatten-Baseline“.
