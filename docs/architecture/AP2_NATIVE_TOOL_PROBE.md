# AP2.1 – Native Tool-Calling-Probe

Stand 28.11.2026. Referenzumgebung vom PO bestätigt: OpenWebUI v0.11.4, Raspberry Pi 5, google/gemma-4-31b-it über OpenRouter direkt. Kein LiteLLM im Datenpfad.

## Durchführung

1. Separate Pipe-Funktion in OpenWebUI unter Admin / Functions anlegen, z. B. theoagent_v2_native_probe. Inhalt: tools/local_dev/native_tool_probe_v2.py. Nicht global aktivieren; bestehende THEOAgent-Pipe unverändert lassen.
2. Funktion speichern und aktivieren, TARGET_MODEL_ID in Valves auf exakte bestehende Zielmodell-ID setzen (nicht die Pipe selbst). Standard google/gemma-4-31b-it.
3. Neuer Chat mit dem Probe-Modell, keine Fachbibliothek oder Skills erforderlich. Beliebige synthetische Eingabe, z. B. "Starte den Schnittstellentest." Die Probe verwendet absichtlich einen festen internen Testprompt, nicht die Nutzereingabe.
4. Vollständige Ausgabe mit JSON-Diagnose übermitteln. Zweiten unabhängigen Chat nur bei Bedarf zur Reproduktion verwenden.
5. Probe danach deaktivieren.

PASS: genau ein native tool_calls-Eintrag mit gültiger Call-ID, erwarteter Funktionsname und leeres Argumentobjekt; tatsächliche Erzeugung eines vorher unbekannten Zufallscodes; tool-Rolle mit korrelierter ID zurückgesendet; abschließende Antwort enthält exakt diesen Code und endet mit stop ohne weitere Tool Calls. Keine nachträgliche Änderung des Orakels. FAIL ist Diagnosebefund, kein Produkturteil.

Offline-Test: python3 -m unittest discover -s tests/local_dev -p test_native_tool_probe_v2.py -v (pydantic erforderlich). Stub-Tests prüfen nur Protokoll und Orakel. Live-Status NOT_RUN bis PO-Ausgabe vorliegt.

Die Probe nutzt die bestehende generate_chat_completion-Schnittstelle. Sie testet bewusst nur einen synthetischen Callable, noch nicht die nativen Knowledge-/Skill-Tools, ACL, SSRF, Streaming oder fachliche Qualität. Zweiter Aufruf nutzt tool_choice=none, erster auto. Kein eigenes Steuerungs-JSON im Modelltext. JSON-Argumente des Standard-Tool-Protokolls bleiben. Keine produktive Architekturentscheidung allein aus diesem Test.
