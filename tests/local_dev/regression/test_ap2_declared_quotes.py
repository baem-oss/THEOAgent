"""Explicit quote declarations: preserve historical tests and test the new protocol."""
import os
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev9.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

E = [h.ev(1, content="Die Predigt folgt dem Text. Die Anwendung bleibt textgebunden."),
     h.ev(2, content="Die Gemeinde hört zu.")]
def validate(answer, quotes):
    return h.A["validate_final"]("Was sagt die Quelle zur Predigt?",
        {"answer":answer, "sources_sufficient":True, "quotes":quotes}, E)
def q(text, source="S1"):
    return {"text":text, "source":source}
def reject(answer, quotes):
    try:
        validate(answer, quotes)
    except h.GuardError:
        return
    raise AssertionError("Unexpected release: " + answer)

text = "Die Predigt folgt dem Text."
assert validate("„"+text+"“, so schreibt der Autor.", [q(text)]) == "„"+text+"“ [S1], so schreibt der Autor."
assert validate("„"+text+"“ [S1]", [q(text)]) == "„"+text+"“ [S1]"
assert validate("„"+text+"“ Eine andere Aussage [S2].", [q(text)]) == "„"+text+"“ [S1] Eine andere Aussage [S2]."
assert validate("**„"+text+"“**", [q(text)]) == "**„"+text+"“** [S1]"
assert validate("Eine Paraphrase [S1].", []) == "Eine Paraphrase [S1]."
assert validate("„"+text+"“\n„Die Gemeinde hört zu.“", [q(text),q("Die Gemeinde hört zu.","S2")])
print("AP2 explicit quote rendering PASS")
for answer, quotes in [
    ("„"+text+"“ [S1]", []),
    ("„"+text+"“ [S1]", [q(text),q(text)]),
    ("„"+text+"“ [S1]", [q("Die Anwendung bleibt textgebunden.")]),
    ("„"+text+"“ [S1]", [q(text,"S99")]),
    ("„"+text+"“ [S1]", [q(text,"S2")]),
    ("„"+text+"“ [S2]", [q(text)]),
    ("„Erfundenes Zitat“ [S1]", [q("Erfundenes Zitat")]),
    ("„Die Predigt folgt dem Text. […] Die Gemeinde hört zu.“ [S1, S2]", [q("Die Predigt folgt dem Text. […] Die Gemeinde hört zu.")]),
    ("„"+text+"“ [S1]", None),
    ("„"+text+"“ [S1]", [q(text, [])]),
    ("„"+text+"“ [S1] „"+text+"“ [S1]", [q(text)]),
    ("„"+text+" [S1]", []),
]:
    reject(answer, quotes)
print("AP2 explicit quote coverage and rejection PASS")
