"""QE-Harness: lädt sourceguard_pipe_v0_5_5_dev3.py UNVERÄNDERT und macht die inneren
Agent-Funktionen über Closure-Zellen zugänglich. Open WebUI wird nur gestubbt."""
import asyncio, importlib.util, json, sys, types

import os
PIPE_PATH = os.environ.get("SG_PIPE", "tools/local_dev/sourceguard_pipe_v0_5_5_dev3.py")

# --- Open-WebUI-Stubs (nur für Pipe.pipe-Ende-zu-Ende-Tests) ---------------------------
_script = {"outputs": [], "prompts": []}

class _User:  # minimaler Benutzer
    id = "u1"

class _Users:
    @staticmethod
    def get_user_by_id(uid):
        return _User()

async def _generate_chat_completion(request, payload, user):
    _script["prompts"].append(payload["messages"])
    out = _script["outputs"].pop(0)
    if callable(out):
        out = out(payload["messages"])
    content = out if isinstance(out, str) else json.dumps(out, ensure_ascii=False)
    return {"choices": [{"message": {"content": content}}]}

for name in ("open_webui", "open_webui.models", "open_webui.utils"):
    sys.modules.setdefault(name, types.ModuleType(name))
m_users = types.ModuleType("open_webui.models.users"); m_users.Users = _Users
m_chat = types.ModuleType("open_webui.utils.chat"); m_chat.generate_chat_completion = _generate_chat_completion
sys.modules["open_webui.models.users"] = m_users
sys.modules["open_webui.utils.chat"] = m_chat

spec = importlib.util.spec_from_file_location("sg_dev3", PIPE_PATH)
sg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sg)


def _collect(fn, out, seen):
    if id(fn) in seen:
        return
    seen.add(id(fn))
    code = getattr(fn, "__code__", None)
    if code is None or fn.__closure__ is None:
        return
    for name, cell in zip(code.co_freevars, fn.__closure__):
        try:
            val = cell.cell_contents
        except ValueError:
            continue
        out.setdefault(name, val)
        if callable(val) and hasattr(val, "__code__"):
            _collect(val, out, seen)


A = {}
_collect(sg._AgentPipe.pipe, A, set())
for k in ("run_research", "render_result"):
    _collect(A[k], A, set())
for k in list(A):
    if callable(A[k]) and hasattr(A[k], "__code__"):
        _collect(A[k], A, set())

GuardError = A["GuardError"]


# --- Synthetische Fachbibliothek ---------------------------------------------------------
def prose_lines(n, seed="Predigt"):
    base = [
        f"Die {seed} muss sich an der Struktur des biblischen Textes orientieren und darf ihn nicht nur als Anlass benutzen.",
        "Wer predigt, erschließt zunächst den Wortlaut, die Gattung und den Zusammenhang der Perikope in ihrem Kontext.",
        "Daraus ergibt sich eine Gliederung, die dem Gedankengang des Textes folgt und ihn für die Hörer öffnet.",
        "Eine bloße Sprungbrett-Predigt verfehlt diesen Anspruch, weil sie den Text nur als Absprungpunkt verwendet.",
        "Die Anwendung bleibt an die Aussage des Textes gebunden und wird nicht von außen an ihn herangetragen.",
    ]
    return [base[i % len(base)] for i in range(n)]


class FakeLibrary:
    def __init__(self):
        self.files = {
            "f-klip": ("Klippert - Vom Text zur Predigt.pdf",
                       ["Vom Text zur Predigt", "Wolfgang Klippert", ""] + prose_lines(3000)),
            "f-other": ("Mueller - Andere Homiletik.pdf",
                        ["Andere Homiletik", "Hans Mueller", ""] + prose_lines(600, "Rede")),
        }
        self.calls = []

    def tools(self, with_web=False, fetch_text=None, web_hits=None):
        lib = self

        async def list_knowledge(**kw):
            lib.calls.append(("list_knowledge", kw))
            return json.dumps({"knowledge_bases": [], "files": [
                {"id": fid, "filename": fn} for fid, (fn, _) in lib.files.items()]})

        async def grep_knowledge_files(pattern, file_id=None, case_insensitive=False, count_only=False):
            lib.calls.append(("grep_knowledge_files", dict(pattern=pattern, file_id=file_id)))
            rows = []
            for fid, (fn, lines) in lib.files.items():
                if file_id and fid != file_id:
                    continue
                for i, line in enumerate(lines, 1):
                    if pattern.casefold() in line.casefold():
                        rows.append(f"{fid}  {fn}:{i}: {line}")
                        if len(rows) >= 5:
                            break
            return "\n".join(rows)

        async def query_knowledge_files(query, knowledge_ids=None, count=5):
            lib.calls.append(("query_knowledge_files", dict(query=query)))
            return json.dumps([{"file_id": "f-klip", "source": lib.files["f-klip"][0],
                                "content": lib.files["f-klip"][1][900]}])

        async def view_knowledge_file(file_id, start_line=None, end_line=None, **kw):
            lib.calls.append(("view_knowledge_file", dict(file_id=file_id, start_line=start_line, end_line=end_line)))
            if file_id not in lib.files:
                return json.dumps({"error": "File not found"})
            fn, lines = lib.files[file_id]
            s = max(1, int(start_line)) - 1
            e = min(len(lines), int(end_line) if end_line else s + 100)
            content = "\n".join(f"{s + i + 1}: {l}" for i, l in enumerate(lines[s:e]))
            return json.dumps({"id": file_id, "filename": fn, "content": content,
                               "total_lines": len(lines), "showing_lines": f"{s+1}-{e}"}, ensure_ascii=False)

        t = {n: {"callable": f} for n, f in [
            ("list_knowledge", list_knowledge), ("grep_knowledge_files", grep_knowledge_files),
            ("query_knowledge_files", query_knowledge_files), ("view_knowledge_file", view_knowledge_file)]}
        if with_web:
            async def search_web(query, count=None):
                lib.calls.append(("search_web", dict(query=query)))
                return json.dumps(web_hits if web_hits is not None else [
                    {"title": "Dei Verbum", "link": "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651118_dei-verbum_ge.html", "snippet": "..."}])

            async def fetch_url(url):
                lib.calls.append(("fetch_url", dict(url=url)))
                return fetch_text or ""
            t["search_web"] = {"callable": search_web}
            t["fetch_url"] = {"callable": fetch_url}
        return t


def scripted(outputs):
    """infer-Ersatz für run_research: liefert vorgegebene Modellausgaben der Reihe nach."""
    outs = list(outputs)
    seen = []

    async def infer(history):
        seen.append(history)
        out = outs.pop(0)
        if callable(out):
            out = out(history)
        return out
    infer.seen = seen
    return infer


def run(question, tools, outputs, **kw):
    infer = scripted(outputs)
    result = asyncio.run(A["run_research"](question, tools, infer, **kw))
    result["_infer"] = infer
    return result


def ev(i, content="Die Predigt folgt dem Text. Sie erschließt ihn. Sie wendet ihn an.", nums=(), work=None):
    return {"id": f"S{i}", "title": "Datei", "locator": "Extraktzeilen", "url": "",
            "paragraph_numbers": list(nums), "content": content, "_key": ("view", "f", i, i),
            "_work": work}