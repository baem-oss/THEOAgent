"""AP2.2/2.3 regression checks using the historical QE harness."""
import os
import sys
from pathlib import Path
root = Path(__file__).resolve().parents[3]
os.environ.setdefault("SG_PIPE", str(root / "tools/local_dev/sourceguard_pipe_v0_5_5_dev7.py"))
sys.path.insert(0, str(root / "tests/local_dev/qe_reference"))
import harness as h

A = h.A
E = [h.ev(1, content="Die Predigt folgt dem Text. Die Auslegung ist die Basis aller Verkündigung. "
                   "Die Anwendung bleibt textgebunden. Der Glaube trägt."),
     h.ev(2, content="Die Hoffnung ist lebendig. Die Gemeinde hört zu."),
     h.ev(3, content="Die Verkün\u00addigung folgt dem Text. Die Bibel\nspricht.")]
def validate(text, question="Was sagt die Quelle zur Predigt?", evidence=E):
    return A["validate_final"](question, {"answer": text, "sources_sufficient": True}, evidence)
def reject(text, question="Was sagt die Quelle zur Predigt?", evidence=E):
    try:
        validate(text, question, evidence)
    except h.GuardError:
        return
    raise AssertionError("Unexpected release: " + text)

for text in (
    "Klippert schreibt: „Die Predigt folgt dem Text.“ [S1]",
    "Er nennt die „Basis aller Verkündigung“ [S1].",
    "Er spricht vom „Glaube“ [S1].",
    "Er sagt: »Die Hoffnung ist lebendig.« [S2]",
    "Er sagt: \"Die Gemeinde hört zu.\" [S2]",
    "Er sagt: ‚Die Gemeinde hört zu.‘ [S2]",
    "Er sagt: „Die Predigt folgt dem Text. […] Die Anwendung bleibt textgebunden.“ [S1]",
    "Er sagt: „Die Anwendung bleibt textgebunden.“ [S1, S2]",
    "Er sagt: „Die Verkündigung folgt dem Text.“ [S3]",
    "Er sagt: „Die Bibel spricht.“ [S3]",
    "Die Auslegung ist wichtig [S1].",
    "*Vom Text zur Predigt* ist ein Werktitel [S1].",
):
    assert validate(text)
print("AP2.2 positive quotes PASS")

for text in (
    "Er schreibt: „Die Predigt ist eine Plauderei über das Wetter.“ [S1]",
    "Er schreibt: „Hoffnung“ [S1].",
    "Er schreibt: „Glaub“ [S1].",
    "Er schreibt: „Die Predigt folgt dem Text.“ [S2]",
    "Er schreibt: „Die Predigt folgt dem Text. […] Die Gemeinde hört zu.“ [S1, S2]",
    "Er schreibt: „Die Anwendung bleibt textgebunden. […] Die Predigt folgt dem Text.“ [S1]",
    "Er schreibt: „Die Predigt folgt dem Text.“\nAussage [S1].",
    "Er schreibt: „Die Predigt folgt dem Text.“ Eine neue Aussage [S1].",
    "Aussage [S1]. Er schreibt: „Die Predigt folgt dem Text.“",
    "Er schreibt: „Die Predigt folgt dem Text. [S1]",
    "Er schreibt: „die Predigt folgt dem Text.“ [S1]",
):
    reject(text)
print("AP2.2 negative quotes PASS")

for question in (
    "Kürze den Absatz und ergänze, was Dei Verbum 12 lehrt: Die Bibel ist Gottes Wort.",
    "Korrigiere meinen Satz: Klippert fordert drei Predigtpunkte.",
    "Überarbeite den Text sprachlich und ergänze eine theologische Aussage: Der Glaube trägt.",
    "Korrigiere den folgenden Text rein sprachlich und ergänze ein Zitat: Der Glaube trägt.",
):
    reject("Eine neue Aussage.", question, [])
print("AP2.3 substantive tasks remain source-bound PASS")

q = "Korrigiere den folgenden Text rein sprachlich: Das Wort „Glaube“ steht hier."
assert validate("Hier steht das Wort „Glaube“.", q, [])
reject("Hier steht das Wort „Hoffnung“.", q, [])
reject("Hier steht das Wort „Glaube“. [S1]", q, [])
print("AP2.3 explicit language revision PASS")
