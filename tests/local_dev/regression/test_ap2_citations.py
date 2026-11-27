"""AP2.1 regression checks; uses unchanged QE harness and simulated evidence."""
import os
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev6.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

A = h.A
E = [h.ev(1, nums=[12]), h.ev(2), h.ev(3)]
def validate(text, **extra):
    return A["validate_final"]("Was sagt die Quelle zur Predigt?",
        dict(answer=text, sources_sufficient=True, **extra), E)
def reject(text, **extra):
    try:
        validate(text, **extra)
    except h.GuardError:
        return
    raise AssertionError("Unexpected release: " + text)

for text in ("A [S1, S2].", "A [S1; S2].", "A (S1, S2).", "A ［S1, S2］."):
    assert validate(text) == "A [S1] [S2]."
for text in ("A [S1]. B [S1, S99].", "A [S1]. B [S1 und S99].",
             "A [S1]. B [S1–S9].", "A [S1]. B (vgl. S99).",
             "A [S1]. B [S 99].", "A [S1]. B [s99]."):
    reject(text)
print("AP2.1 canonical citations PASS")
reject("Aussage ohne Beleg.\n\nQuellen:\n[S1]")
reject("A [S1].\n\nQuellen:\n- [S99] Unbekannt")
reject("A [S1].\n\nQuellen:\n- [S1] Quelle\nWeiterer Sachtext")
body = validate("A [S1, S2].\n\n**Tatsächlich gelesene Originalstellen:**\n- [S1] Modellquelle\n- [S2] Modellquelle")
assert body == "A [S1] [S2]."
rendered = A["render_result"]({"status":"FREIGEGEBEN","answer":body,
                              "evidence":E,"diagnostic":[],"metrics":{}})
assert rendered.count("**Tatsächlich gelesene Originalstellen:**") == 1
assert "- [S1]" in rendered and "- [S2]" in rendered and "- [S3]" not in rendered
print("AP2.4 single source list PASS")
assert validate("Nach Nr. 12 gilt A [S1, S2].")
reject("Nach Nr. 13 gilt A [S1, S2].")
print("AP2.1 paragraph binding PASS")
