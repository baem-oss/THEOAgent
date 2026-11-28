# AP2.2a – Native Werkzeug-Injektion

28.11.2026. PO-Live-Protokoll, Probe v0.1.0, Prüfstand [22c7141](https://github.com/baem-oss/THEOAgent/commit/22c71418c646ecb3570e751225079fc9dd8d1f13). Umgebung wie AP2.1. Status: INVENTORY PASS (nur Schnittstelleninventar).

37 injizierte Werkzeuge; die sieben untersuchten Einträge sind jeweils present=true, callable=true, schema_candidates.spec.parameters_present=true. Modellaufrufe 0, Werkzeugaufrufe 0. Parameter laut PO-Protokoll:

| Tool | Parameter (Typ) | Pflicht |
|---|---|---|
| view_skill | id string | id |
| list_knowledge | knowledge_id string, skip integer, count integer | keine |
| grep_knowledge_files | pattern string, file_id string, case_insensitive boolean, count_only boolean | pattern |
| query_knowledge_files | query string, knowledge_ids array, count integer | query |
| view_knowledge_file | file_id string, offset integer, max_chars integer, line_numbers boolean, start_line integer, end_line integer | file_id |
| search_web | query string, count integer | query |
| fetch_url | url string | url |

SE: Native spec und callable als Adapterbasis verwenden; nur freigegebene Werkzeuge exponieren. Inventar erfasst bewusst keine vollständigen Schemas (z.B. Defaults, Constraints, Array-Items), keine tatsächliche Ausführung, keine ACL/SSRF-Evidenz. Nicht alle 37 Werkzeuge automatisch freigeben. Keine neue pauschale 180-Zeilen-Vorgabe aus Altcode ableiten. Native Tool-Calling-Roundtrip mit synthetischem Werkzeug wurde in AP2.1 nachgewiesen, Kombination mit echten Knowledge-/Skill-Callables noch offen. Nächster gezielter Nachweis mit isoliertem, freigegebenem synthetischem Knowledge-Dokument und Skill, keine private Fachliteratur an Provider senden. Keine erneute isolierte SourceGuard-Erreichbarkeitsprüfung.

Installation: Function in Admin-Liste als PIPE aktiv, Anzeigename native_tool_inventory_v2.py statt geplantem Namen; anfängliches Auffindbarkeitsproblem durch Suche nach anderem Namen erklärt, kein Codefix erforderlich. Keine vollständige Live-Konfigurationsprüfung durch SE.
