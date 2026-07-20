#!/usr/bin/env python3
"""Deterministic mock of an OpenAI-compatible API for offline testing.

Serves:
  POST /v1/embeddings        -- 32-dim hashed bag-of-words vectors. Not
                                semantic, but cosine similarity behaves
                                genuinely (shared vocabulary => proximity),
                                which is enough to verify retrieval plumbing
                                and ranking end-to-end.
  POST /v1/chat/completions  -- templated answer that cites the first [n]
                                reference found in the prompt, so citation
                                flow is verifiable.

Usage:
  python3 tools/mock_openai.py [port]          # default 8899
  python3 tools/mock_openai.py --leak [port]   # deliberately copy IndexOnly text
  LLM_BASE_URL=http://127.0.0.1:8899/v1 PYTHONPATH=shell python3 -m intel_shell.pipeline
  LLM_BASE_URL=http://127.0.0.1:8899/v1 PYTHONPATH=shell uvicorn intel_shell.app:app

Swap LLM_BASE_URL to DeepSeek's API or your own vLLM / llama.cpp server and
nothing else changes.
"""
import argparse
import hashlib
import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

DIM = 32
MIN_LEAK_TOKENS = 16


def embed(text: str):
    v = [0.0] * DIM
    for w in re.findall(r"[a-z0-9]+", text.lower()):
        v[int(hashlib.md5(w.encode()).hexdigest(), 16) % DIM] += 1.0
    n = sum(x * x for x in v) ** 0.5 or 1.0
    return [x / n for x in v]


def _index_only_bodies(user: str) -> list[str]:
    return [
        match.strip()
        for match in re.findall(
            r"^\[\d+\][^\n]*license: IndexOnly\)\n(.*?)(?=^\[\d+\]|\Z)",
            user,
            flags=re.MULTILINE | re.DOTALL,
        )
        if match.strip()
    ]


def leaking_sentence(user: str) -> str | None:
    """Return source wording the attestation guard must refuse.

    Prefer a complete substantive sentence. The fallback deliberately returns
    the visible body itself, so --leak can still violate the guard when a source
    has punctuation-free text.
    """
    for body in _index_only_bodies(user):
        sentences = re.split(r"(?<=[.!?])\s+", body)
        candidates = [
            sentence.strip()
            for sentence in sentences
            if len(re.findall(r"[\w]+", sentence, flags=re.UNICODE))
            >= MIN_LEAK_TOKENS
        ]
        if candidates:
            return candidates[0]
        return body
    return None


def chat_content(user: str, leak: bool = False) -> str:
    if leak and (sentence := leaking_sentence(user)) is not None:
        return f"MOCK-LEAK: {sentence}"

    refs = re.findall(r"\[(\d+)\]", user)
    if refs:
        cite = "".join(f"[{r}]" for r in sorted(set(refs))[:3])
        return (
            "MOCK-ANSWER: synthesized from the retrieved context; "
            f"primary support {cite}. Replace LLM_BASE_URL with a real "
            "model endpoint for substantive answers."
        )
    return (
        "MOCK-ANSWER: the retrieved context contains no relevant "
        "documents for this question."
    )


class Handler(BaseHTTPRequestHandler):
    leak = False

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = json.loads(self.rfile.read(length) or b"{}")

        if self.path.rstrip("/").endswith("/embeddings"):
            inputs = body.get("input", [])
            if isinstance(inputs, str):
                inputs = [inputs]
            resp = {
                "object": "list",
                "model": body.get("model", "mock-embed"),
                "data": [
                    {"object": "embedding", "index": i, "embedding": embed(t)}
                    for i, t in enumerate(inputs)
                ],
            }
        elif self.path.rstrip("/").endswith("/chat/completions"):
            user = ""
            for m in body.get("messages", []):
                if m.get("role") == "user":
                    user = m.get("content", "")
            content = chat_content(user, leak=self.leak)
            resp = {
                "choices": [
                    {"message": {"role": "assistant", "content": content}}
                ]
            }
        else:
            self.send_response(404)
            self.end_headers()
            return

        out = json.dumps(resp).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def log_message(self, *args):  # keep test output quiet
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("port", nargs="?", type=int, default=8899)
    parser.add_argument("--leak", action="store_true")
    args = parser.parse_args()
    Handler.leak = args.leak
    mode = "leaking" if args.leak else "normal"
    print(
        f"mock openai-compatible api on http://127.0.0.1:{args.port}/v1 "
        f"({mode} mode)"
    )
    HTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
