import asyncio
import json
import unittest
import importlib.util
from pathlib import Path

p = Path(__file__).resolve().parents[2] / 'tools/local_dev/sourceguard_v2_core.py'
spec = importlib.util.spec_from_file_location('core', p)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
run_core, Pipe = core.run_core, core.Pipe


def response(text=None, calls=None, reason='stop'):
    return {'choices': [{'message': {'content': text, 'tool_calls': calls}, 'finish_reason': reason}]}


def call(name='view_knowledge_file', args=None, cid='c1'):
    return {'id': cid, 'type': 'function', 'function': {'name': name, 'arguments': json.dumps({'file_id': 'a'} if args is None else args)}}


def tools(fn):
    return {'view_knowledge_file': {'spec': {'name': 'view_knowledge_file', 'parameters': {'type': 'object', 'properties': {'file_id': {'type': 'string'}}, 'required': ['file_id']}}, 'callable': fn}}


class CoreTests(unittest.IsolatedAsyncioTestCase):
    async def test_no_tools(self):
        async def complete(dialog, schemas, allow):
            self.assertFalse(allow)
            return response('Fürbitte')
        answer, trace = await run_core([], {}, complete)
        self.assertEqual(answer, 'Fürbitte')
        self.assertEqual(trace['model_calls'], 1)

    async def test_roundtrip(self):
        async def complete(dialog, schemas, allow):
            if not dialog:
                return response(calls=[call()], reason='tool_calls')
            self.assertEqual(dialog[-1]['tool_call_id'], 'c1')
            self.assertIn('synthetic', dialog[-1]['content'])
            return response('Answer')
        answer, trace = await run_core([], tools(lambda **kw: {'content': 'synthetic'}), complete, allow_tools=True)
        self.assertEqual(answer, 'Answer')
        e = next(e for e in trace['events'] if e['event'] == 'tool_result')
        self.assertTrue(e['executed'] and e['submitted'] and e['response_received'])
        self.assertNotIn('synthetic', json.dumps(trace))

    async def test_rejected_and_error(self):
        for bad in [call('fetch_url'), call(args={'file_id': 1}), call()]:
            def fail(**kw):
                raise RuntimeError('secret exception')
            async def complete(dialog, schemas, allow):
                if not dialog:
                    return response(calls=[bad], reason='tool_calls')
                self.assertIn('error', dialog[-1]['content'])
                self.assertNotIn('secret exception', dialog[-1]['content'])
                return response('Teilantwort')
            answer, trace = await run_core([], tools(fail), complete, allow_tools=True)
            self.assertEqual(answer, 'Teilantwort')
            self.assertEqual(trace['tool_calls'], int(bad == call()))

    async def test_invalid_ids(self):
        async def complete(dialog, schemas, allow):
            if allow:
                return response('not final', [call(), call()], 'tool_calls')
            self.assertFalse(any(m.get('tool_calls') for m in dialog))
            return response('Eingeschränkt')
        answer, trace = await run_core([], tools(lambda **kw: self.fail()), complete, allow_tools=True)
        self.assertIn('Eingeschränkt', answer)
        self.assertEqual(trace['status'], 'INCOMPLETE')
        self.assertEqual(trace['tool_calls'], 0)

    async def test_retry(self):
        attempts = []
        async def complete(*args):
            attempts.append(1)
            if len(attempts) == 1:
                raise TimeoutError()
            return response('OK')
        answer, trace = await run_core([], {}, complete, retry_delay=0)
        self.assertEqual(answer, 'OK')
        self.assertEqual(trace['model_calls'], 2)

    async def test_context(self):
        async def complete(*args):
            self.fail('must not send oversized input')
        _, trace = await run_core([{'role': 'user', 'content': 'x'*200}], {}, complete, input_bytes=100)
        self.assertEqual(trace['reason'], 'context_budget')

    async def test_budget(self):
        async def complete(dialog, schemas, allow):
            return response(calls=[call()], reason='tool_calls') if allow else response('Teil')
        answer, trace = await run_core([], tools(lambda **kw: 'text'), complete, allow_tools=True, max_calls=1)
        self.assertIn('Teil', answer)
        self.assertEqual(trace['status'], 'INCOMPLETE')

    async def test_secrets(self):
        async def complete(dialog, schemas, allow):
            self.assertNotIn('CANARY_SECRET', json.dumps(dialog))
            return response('CANARY_SECRET')
        answer, _ = await run_core([{'role': 'user', 'content': 'CANARY_SECRET'}], {}, complete, secrets=('CANARY_SECRET',))
        self.assertEqual(answer, '[REDACTED]')

    async def test_truncated_and_filter(self):
        for reason in ('length', 'content_filter'):
            async def complete(*args):
                return response('partial', reason=reason)
            answer, trace = await run_core([], {}, complete)
            self.assertEqual(trace['status'], 'INCOMPLETE')
            if reason == 'content_filter':
                self.assertNotIn('partial', answer)

    async def test_disabled_profile(self):
        self.assertIn('nicht freigegeben', await Pipe().pipe({}))

    async def test_read_provenance(self):
        async def complete(dialog, schemas, allow):
            if not dialog:
                return response(calls=[call()], reason='tool_calls')
            return response('Fachantwort')
        answer, trace = await run_core([], tools(lambda **kw: {
            'file_id': 'a', 'filename': 'Test.md', 'start_line': 2,
            'end_line': 5, 'content': 'synthetic passage'
        }), complete, allow_tools=True)
        self.assertEqual(answer, 'Fachantwort')
        summary = core.provenance_summary(trace)
        self.assertIn('Test.md', summary)
        self.assertIn('Werkzeugzeilen 2–5', summary)
        self.assertNotIn('synthetic passage', summary)
        self.assertNotIn('synthetic passage', json.dumps(trace))

    async def test_read_unknown_identity(self):
        async def complete(dialog, schemas, allow):
            if not dialog:
                return response(calls=[call()], reason='tool_calls')
            return response('Antwort')
        _, trace = await run_core([], tools(lambda **kw: {'content': 'text'}), complete, allow_tools=True)
        self.assertIn('Identität nicht bestätigt', core.provenance_summary(trace))
        self.assertNotIn('Werkzeugzeilen', core.provenance_summary(trace))

    async def test_no_provenance_for_error_or_oversize(self):
        async def complete(dialog, schemas, allow):
            if not dialog:
                return response(calls=[call()], reason='tool_calls')
            return response('Teilantwort')
        for result in ({'error': 'failed', 'content': 'text'}, {'content': 'x'*500}):
            _, trace = await run_core([], tools(lambda **kw: result), complete,
                                      allow_tools=True, max_result_chars=100)
            self.assertEqual(core.provenance_summary(trace), '')

    async def test_unsubmitted_read_not_displayed(self):
        async def complete(dialog, schemas, allow):
            return response(calls=[call()], reason='tool_calls') if allow else response('Teil')
        _, trace = await run_core([], tools(lambda **kw: {'content': 'x'*5000}),
                                  complete, allow_tools=True, input_bytes=2000)
        self.assertEqual(core.provenance_summary(trace), '')

    async def test_followup_no_new_read(self):
        history = [{'role': 'assistant', 'content': 'Dokumentabrufe dieser Antwort: Test.md'},
                   {'role': 'user', 'content': 'Welche Quelle war das?'}]
        async def complete(dialog, schemas, allow):
            self.assertEqual(dialog, history)
            return response('Laut bisherigem Verlauf Test.md; kein neuer Abruf.')
        answer, trace = await run_core(history, {}, complete)
        self.assertIn('kein neuer Abruf', answer)
        self.assertEqual(core.provenance_summary(trace), '')
        self.assertEqual(trace['tool_calls'], 0)


if __name__ == '__main__':
    unittest.main()
