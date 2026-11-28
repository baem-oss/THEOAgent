# AP2.1 – Native Tool Calling: Live-Nachweis

Datum: 28.11.2026. Status: LIVE PASS im definierten synthetischen Test.
Prüfstand: [1f090cd](https://github.com/baem-oss/THEOAgent/tree/1f090cd2ad4e785c94a920fec78f75b4ceddd46b), Probe v0.1.0.
Umgebung laut PO: Raspberry Pi 5, OpenWebUI v0.11.4, google/gemma-4-31b-it via OpenRouter direkt.
Quelle: vom PO übermitteltes Laufprotokoll. Keine unabhängige Ausführung durch SE; vollständige sichtbare Modellantwort nicht separat übermittelt. Tokenvergleich erfolgt im Probe-Code.

```json
{
  "version": "0.1.0",
  "events": [
    {
      "event": "model_response_1",
      "finish_reason": "tool_calls",
      "native_calls": 1
    },
    {
      "event": "tool_executed",
      "call_id": "call_01a221abf1a877239eea884ab94b8a2a",
      "name": "probe_nonce",
      "token": "SGV2-778c6ebd490a540e8fcfa18b"
    },
    {
      "event": "tool_result_submitted",
      "call_id": "call_01a221abf1a877239eea884ab94b8a2a"
    },
    {
      "event": "model_response_2",
      "finish_reason": "stop",
      "token_match": true,
      "native_calls": 0
    }
  ],
  "status": "PASS",
  "reason": "Round trip complete",
  "duration_ms": 2066.9
}
```

## SE-Bewertung

Alle Kriterien aus [AP2_NATIVE_TOOL_PROBE.md](../../docs/architecture/AP2_NATIVE_TOOL_PROBE.md) laut übermitteltem Protokoll erfüllt. Der Code prüft auch leere Argumente und gültige native Aufrufstruktur vor der Token-Erzeugung. Zwei Modellaufrufe, eine synthetische Werkzeugausführung, 2066,9 ms. Keine Aussage über allgemeine Latenz oder Zuverlässigkeit.

Native Tool Calls über generate_chat_completion innerhalb der obligatorischen Pipe sind im getesteten Umfang machbar. SE-Entscheidung: native Kommunikation als Ausgangspunkt für AP2; kein eigenes JSON-Steuerungsprotokoll oder obligatorische getrennte Antwortphase. Standardisierte Werkzeugargumente bleiben. Keine Produktfreigabe.

Offen: tatsächliche native Knowledge-/Skill-Callables und Schemas, mehrere Werkzeugrunden, fehlerhafte Tool-Aufrufe und Fehlerreaktion, Kontext/Anhänge/Provenienz, ACL/SSRF, Freeze, W2-Konfiguration, fachliche Qualität. Offline-Tests bisher NOT_RUN. Kein Nachweis, dass sämtliche Plattformtools unverändert durchgereicht werden können. Nächster Schritt: gezielte Probe der tatsächlichen Werkzeug-Injektion und eines zulässigen synthetischen Knowledge- bzw. Skill-Zugriffs; keine Wiederholung isolierter SourceGuard-Erreichbarkeitstests. Danach Zielarchitektur und Claude-Review.
