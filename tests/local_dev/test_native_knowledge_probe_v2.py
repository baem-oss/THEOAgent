import asyncio
import importlib.util
import json
from pathlib import Path
import unittest

p = Path(__file__).resolve().parents[2] / "tools/local_dev/native_knowledge_probe_v2.py"
spec = importlib.util.spec_from_file_location("probe", p)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

def response(message, reason="stop"):
    return {"choices":[{"message":message,"finish_reason":reason}]}

def call(name, args, cid="c1"):
    return {"id":cid,"type":"function","function":{"name":name,"arguments":json.dumps(args)}}

def entry(name, fn):
    return {"spec":{"name":name,"parameters":{"type":"object","properties":{"file_id":{"type":"string"}},"required":["file_id"]}},"callable":fn}

class TestProbe(unittest.TestCase):
    def test_real_callable_roundtrip(self):
        seen=[]
        async def read(file_id):
            seen.append(file_id)
            return {"content":"synthetic proof"}
        async def complete(messages, schemas, allow):
            self.assertEqual(schemas[0]["function"]["name"],"view_knowledge_file")
            if not seen:
                return response({"content":None,"tool_calls":[call("view_knowledge_file",{"file_id":"test"})]},"tool_calls")
            self.assertEqual(messages[-1]["tool_call_id"],"c1")
            self.assertIn("synthetic proof",messages[-1]["content"])
            return response({"content":"Answer"})
        out=asyncio.run(probe.run_probe([],{"view_knowledge_file":entry("view_knowledge_file",read)},complete))
        self.assertEqual(seen,["test"])
        self.assertIn('"status": "COMPLETED"',out)
        self.assertNotIn("synthetic proof",out)
    def test_failed_tool_preserves_response(self):
        async def read(file_id):
            raise RuntimeError("private error")
        async def complete(messages,schemas,allow):
            if not messages:
                return response({"tool_calls":[call("view_knowledge_file",{"file_id":"test"})]},"tool_calls")
            self.assertIn("RuntimeError",messages[-1]["content"])
            return response({"content":"Teilantwort mit Einschränkung"})
        out=asyncio.run(probe.run_probe([],{"view_knowledge_file":entry("view_knowledge_file",read)},complete))
        self.assertIn("Teilantwort mit Einschränkung",out)
        self.assertNotIn("private error",out)
    def test_unapproved_tool_not_invoked(self):
        seen=[]
        def read(**kwargs):
            seen.append(True)
        async def complete(messages,schemas,allow):
            if not messages:
                return response({"tool_calls":[call("fetch_url",{})]},"tool_calls")
            return response({"content":"Kein Webzugriff"})
        out=asyncio.run(probe.run_probe([],{"view_knowledge_file":entry("view_knowledge_file",read),"fetch_url":entry("fetch_url",read)},complete))
        self.assertEqual(seen,[])
        self.assertIn('"tool_calls": 0',out)
    def test_no_tools(self):
        async def complete(*args):
            self.fail("No model call expected")
        out=asyncio.run(probe.run_probe([],{},complete))
        self.assertIn("no_tools",out)

if __name__=="__main__":
    unittest.main()
