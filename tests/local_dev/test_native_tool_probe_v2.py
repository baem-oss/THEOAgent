"""Offline protocol test. Does not exercise OpenWebUI or provider."""
import asyncio
import importlib.util
import json
from pathlib import Path
import unittest

p = Path(__file__).resolve().parents[2] / "tools/local_dev/native_tool_probe_v2.py"
spec = importlib.util.spec_from_file_location("probe", p)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

def response(message, reason):
    return {"choices": [{"message": message, "finish_reason": reason}]}

def native_call():
    return response({"content": None, "tool_calls": [{"id": "stub-1", "type": "function", "function": {"name": "probe_nonce", "arguments": "{}"}}]}, "tool_calls")

class ProbeTests(unittest.TestCase):
    def test_round_trip(self):
        async def complete(messages, first):
            if first:
                return native_call()
            self.assertEqual(messages[-1]["tool_call_id"], "stub-1")
            self.assertEqual(messages[-2]["tool_calls"][0]["id"], "stub-1")
            return response({"content": json.loads(messages[-1]["content"])["token"]}, "stop")
        out = asyncio.run(probe.run_probe(complete))
        self.assertIn('"status": "PASS"', out)
        self.assertIn('"token_match": true', out)

    def test_no_native_call(self):
        async def complete(messages, first):
            return response({"content": "I called a tool"}, "stop")
        self.assertIn('"status": "FAIL"', asyncio.run(probe.run_probe(complete)))

    def test_wrong_token(self):
        async def complete(messages, first):
            return native_call() if first else response({"content": "wrong"}, "stop")
        self.assertIn('"status": "FAIL"', asyncio.run(probe.run_probe(complete)))

    def test_exception(self):
        async def complete(messages, first):
            raise RuntimeError("synthetic")
        self.assertIn('"status": "FAIL"', asyncio.run(probe.run_probe(complete)))

if __name__ == "__main__":
    unittest.main()
