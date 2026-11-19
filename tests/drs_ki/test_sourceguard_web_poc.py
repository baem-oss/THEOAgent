"""Regression checks for the DRS:KI SourceGuard Web PoC.
Run from repository root: python -m unittest discover -s tests/drs_ki -p 'test_sourceguard_web_poc.py' -v
No network access is used.
"""
import importlib.util
import json
import pathlib
import unittest
from unittest.mock import patch

SOURCE = pathlib.Path(__file__).resolve().parents[2] / "tools" / "drs_ki" / "sourceguard_web_poc_v0_1_0.py"
spec = importlib.util.spec_from_file_location("sourceguard_web_poc", SOURCE)
sg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sg)


class SourceGuardWebPoCTests(unittest.TestCase):
    def setUp(self):
        self.tool = sg.Tools()

    def test_url_allowlist_and_schemes(self):
        allowed = {"www.vatican.va"}
        self.assertEqual(sg._parse_url("https://www.vatican.va/a.html", allowed)[0], "www.vatican.va")
        for url in (
            "http://www.vatican.va/a",
            "https://localhost/a",
            "https://127.0.0.1/a",
            "https://www.vatican.va.evil.com/a",
            "https://user:pw@www.vatican.va/a",
            "https://www.vatican.va:8443/a",
            "https://www.vatican.va/a\nInjected-Header: yes",
        ):
            with self.subTest(url=url), self.assertRaises(sg.RetrievalError):
                sg._parse_url(url, allowed)

    def test_public_ip_rejects_private_or_mixed_dns(self):
        for answers in (["10.0.0.7"], ["127.0.0.1"], ["169.254.169.254"],
                        ["93.184.216.34", "10.2.3.4"], ["::1"]):
            fake = [(None, None, None, None, (ip, 443)) for ip in answers]
            with patch.object(sg.socket, "getaddrinfo", return_value=fake):
                with self.subTest(answers=answers), self.assertRaises(sg.RetrievalError):
                    sg._public_ip("www.vatican.va")

    def test_public_ip_uses_checked_ip(self):
        fake = [(None, None, None, None, ("93.184.216.34", 443))]
        with patch.object(sg.socket, "getaddrinfo", return_value=fake):
            self.assertEqual(sg._public_ip("www.vatican.va"), "93.184.216.34")

    def test_html_extraction_ignores_scripts(self):
        parser = sg.TextExtractor()
        parser.feed("<html><body><p>Quelle A</p><script>ignore_me()</script>"
                    "<p>Quelle B</p></body></html>")
        output = "".join(parser.parts)
        self.assertIn("Quelle A", output)
        self.assertIn("Quelle B", output)
        self.assertNotIn("ignore_me", output)

    def test_success_reports_no_semantic_verification(self):
        text = ("Einleitung\n" + "2267. Die Kirche lehrt eine klare Aussage. " +
                "Zusammenhang des Abschnitts. " * 30)
        with patch.object(sg, "_download", return_value=("https://www.vatican.va/test", text)):
            result = json.loads(self.tool.read_source("https://www.vatican.va/test", "2267"))
        self.assertEqual(result["status"], "TEXT_RETRIEVED")
        self.assertTrue(result["technical_retrieval"])
        self.assertFalse(result["semantic_claim_verified"])
        self.assertTrue(result["section_marker_found"])
        self.assertIn("2267", result["excerpt"])

    def test_absent_section_fails_closed(self):
        text = ("Dies ist ein gültiger Originaltext ohne die benannte Nummer. " * 30)
        with patch.object(sg, "_download", return_value=("https://www.vatican.va/test", text)):
            result = json.loads(self.tool.read_source("https://www.vatican.va/test", "2267"))
        self.assertEqual(result["status"], "SECTION_NOT_LOCATED")
        self.assertFalse(result["section_marker_found"])
        self.assertEqual(result["excerpt"], "")
        self.assertFalse(result["semantic_claim_verified"])

    def test_fetch_failure_never_returns_verified(self):
        with patch.object(sg, "_download", side_effect=sg.RetrievalError("Blocked")):
            result = json.loads(self.tool.read_source("https://www.vatican.va/test", "2267"))
        self.assertEqual(result["status"], "RETRIEVAL_FAILED")
        self.assertFalse(result["technical_retrieval"])
        self.assertFalse(result["semantic_claim_verified"])


if __name__ == "__main__":
    unittest.main()
