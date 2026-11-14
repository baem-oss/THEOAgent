"""Offline regression checks for the GENERIC SourceGuard Web v0.2.0 tool.

Run: python -m unittest discover -s tests/drs_ki -p 'test_sourceguard_web_poc_v0_2.py' -v
Mocks prevent network requests. Real DRS:KI DEV integration is separate.
"""
import importlib.util
import json
import pathlib
import unittest
from unittest.mock import patch

SOURCE = pathlib.Path(__file__).resolve().parents[2] / "tools" / "drs_ki" / "sourceguard_web_poc_v0_2_0.py"
spec = importlib.util.spec_from_file_location("sourceguard_web_poc", SOURCE)
sg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sg)


class SourceGuardWebV02Tests(unittest.TestCase):
    def setUp(self):
        self.tool = sg.Tools()
        self.a = "https://www.vatican.va/a"
        self.b = "https://www.vatican.va/b"

    def mock_read(self, url, section, text):
        with patch.object(sg, "_download", return_value=(url, text)):
            return json.loads(self.tool.read_source(url, section))

    def test_generic_number_without_period(self):
        result = self.mock_read(self.a, "2267",
            "2266 Anmerkung\n2267 Soweit unblutige Mittel ausreichen, "
            "werden sie verwendet.\n2268 Folgender Absatz.")
        self.assertEqual(result["status"], "TEXT_RETRIEVED")
        self.assertEqual(result["section_boundary"], "NEXT_NUMBER")
        self.assertTrue(result["section_text"].startswith("2267 Soweit"))
        self.assertNotIn("2268", result["section_text"])

    def test_generic_number_with_period(self):
        result = self.mock_read(self.a, "12",
            "11. Einführung\n12. Im selben Geist auszulegen. "
            "Schrift und Überlieferung.\n13. Ende.")
        self.assertEqual(result["status"], "TEXT_RETRIEVED")
        self.assertIn("12. Im selben Geist", result["section_text"])

    def test_generic_canon_heading(self):
        result = self.mock_read(self.a, "can. 767",
            "Abschnitt A\ncan. 767 § 1 Die Homilie ist Teil der Liturgie.\nAbschnitt B")
        self.assertEqual(result["status"], "TEXT_RETRIEVED")
        self.assertIn("Homilie", result["section_text"])

    def test_index_heading_is_not_section(self):
        result = self.mock_read(self.a, "2267",
            "Neue Formulierung der Nr. 2267 im Katechismus. " * 8)
        self.assertEqual(result["status"], "SECTION_NOT_LOCATED")

    def test_ambiguous_locator_fails_closed(self):
        result = self.mock_read(self.a, "12",
            "12. Erster Text\nWörter\n12. Zweiter Text\nZusätzlicher Text")
        self.assertEqual(result["status"], "LOCATOR_AMBIGUOUS")
        self.assertEqual(result["excerpt"], "")

    def test_compare_different_texts_no_domain_knowledge(self):
        def fixture(url, *_):
            return url, ("9. Vorher\n10. Alpha und Beta.\n11. Nachher"
                         if url == self.a else
                         "9. Vorher\n10. Alpha und Gamma.\n11. Nachher")
        with patch.object(sg, "_download", side_effect=fixture):
            result = json.loads(self.tool.compare_sources(self.a, self.b, "10"))
        self.assertEqual(result["status"], "DIFFERENT_TEXT")
        self.assertFalse(result["version_verified"])
        self.assertFalse(result["semantic_claim_verified"])
        self.assertEqual(result["comparisons"][0]["section_boundary"], "NEXT_NUMBER")

    def test_compare_same_text_no_chronology_inference(self):
        with patch.object(sg, "_download", side_effect=lambda url,*_:
                          (url,"9. Vorher\n10. Gleicher Text.\n11. Nachher")):
            result = json.loads(self.tool.compare_sources(self.a, self.b, "10"))
        self.assertEqual(result["status"], "SAME_TEXT")
        self.assertFalse(result["version_verified"])

    def test_compare_missing_locator_reports_incomplete(self):
        with patch.object(sg, "_download", side_effect=lambda url,*_:
                          (url,"9. Vorher\n10. Text\n11. Nachher"
                           if url == self.a else "Anderes Dokument ohne Fundstelle")):
            result = json.loads(self.tool.compare_sources(self.a, self.b, "10"))
        self.assertEqual(result["status"], "INCOMPLETE")

    def test_exact_quote_only_is_not_semantic_verification(self):
        text = "10. Alpha und Beta sind gemeinsam genannt.\n11. Nachher."
        with patch.object(sg, "_download", return_value=(self.a,text)):
            result = json.loads(self.tool.verify_evidence("Alpha und Beta", self.a, "10"))
        self.assertEqual(result["status"], "QUOTE_FOUND")
        self.assertFalse(result["semantic_claim_verified"])

    def test_paraphrase_not_falsely_verified(self):
        text = "10. Alpha und Beta sind gemeinsam genannt.\n11. Nachher."
        with patch.object(sg, "_download", return_value=(self.a,text)):
            result = json.loads(self.tool.verify_evidence("Alpha ist besser als Beta", self.a, "10"))
        self.assertNotEqual(result["status"], "QUOTE_FOUND")
        self.assertFalse(result["semantic_claim_verified"])

    def test_decoding_utf8_and_windows1252(self):
        html = '<meta charset="windows-1252"><p>Rückgriff und Würde</p>'
        self.assertIn("Rückgriff", sg._decode_document(html.encode("windows-1252"), "text/html"))
        utf8 = '<meta charset="utf-8"><p>Würde</p>'
        self.assertIn("Würde", sg._decode_document(utf8.encode("utf-8"), "text/html"))

    def test_url_restrictions(self):
        allowed = {"www.vatican.va"}
        for url in ("http://www.vatican.va/a","https://localhost/a",
                    "https://www.vatican.va.evil.com/a",
                    "https://u:p@www.vatican.va/a","https://www.vatican.va:8443/a",
                    "https://www.vatican.va/a\nX-Injected: yes"):
            with self.subTest(url=url), self.assertRaises(sg.RetrievalError):
                sg._parse_url(url, allowed)

    def test_private_dns_and_mixed_ips_blocked(self):
        for answers in (["10.0.0.1"], ["127.0.0.1"],
                        ["93.184.216.34","10.0.0.2"], ["::1"]):
            records = [(None,None,None,None,(addr,443)) for addr in answers]
            with patch.object(sg.socket,"getaddrinfo",return_value=records):
                with self.assertRaises(sg.RetrievalError):
                    sg._public_ip("www.vatican.va")

    def test_network_failure_not_verification(self):
        with patch.object(sg,"_download",side_effect=sg.RetrievalError("Blocked")):
            result = json.loads(self.tool.read_source(self.a,"10"))
        self.assertFalse(result["semantic_claim_verified"])
        self.assertEqual(result["status"], "RETRIEVAL_FAILED")


if __name__ == "__main__":
    unittest.main()
