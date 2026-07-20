"""OpenAI-compatible chat + embedding clients (was crates/llm in Rust).

Moving this to the shell is the point of the whole refactor: model choice,
provider, temperature, retries — all product decisions that change weekly.
The Rust core neither knows nor cares which model answered.

One client shape covers every provider that matters here:
- DeepSeek's hosted API,
- a self-hosted vLLM / llama.cpp server on the LAN,
- tools/mock_openai.py for deterministic offline tests.

Env:
  LLM_BASE_URL     e.g. https://api.deepseek.com/v1
                   or   http://192.168.0.192:8000/v1
                   or   http://127.0.0.1:8899/v1   (the mock)
  LLM_API_KEY      optional Bearer token
  LLM_CHAT_MODEL   chat model name    (fallback LLM_MODEL, then "default")
  LLM_EMBED_MODEL  embedding model    (fallback LLM_MODEL, then "default")

The constraint check, once more: these models PROCESS documents the
platform already legally ingested. They are analysis tools, not data
sources — no data gatekeeper is involved.
"""

from __future__ import annotations

import os

import httpx


class LlmError(RuntimeError):
    pass


def _model_from_env(var: str) -> str:
    return os.environ.get(var) or os.environ.get("LLM_MODEL") or "default"


class ChatClient:
    def __init__(self, base_url: str, api_key: str | None = None, model: str = "default"):
        self.model = model
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self._c = httpx.Client(
            base_url=base_url.rstrip("/"), headers=headers, timeout=120.0
        )

    def chat(self, system: str, user: str) -> str:
        try:
            r = self._c.post(
                "/chat/completions",
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    "temperature": 0,
                },
            )
            r.raise_for_status()
            data = r.json()
        except httpx.HTTPError as e:
            raise LlmError(f"chat endpoint error: {e}") from e
        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            raise LlmError(f"bad chat response shape: {e}") from e


class EmbedClient:
    def __init__(self, base_url: str, api_key: str | None = None, model: str = "default"):
        self.model = model
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self._c = httpx.Client(
            base_url=base_url.rstrip("/"), headers=headers, timeout=120.0
        )

    def embed(self, texts: list[str]) -> list[list[float]]:
        try:
            r = self._c.post("/embeddings", json={"model": self.model, "input": texts})
            r.raise_for_status()
            data = r.json()
        except httpx.HTTPError as e:
            raise LlmError(f"embeddings endpoint error: {e}") from e
        items = sorted(data.get("data", []), key=lambda i: i.get("index", 0))
        if len(items) != len(texts):
            raise LlmError(f"expected {len(texts)} embeddings, got {len(items)}")
        return [i["embedding"] for i in items]


def chat_from_env() -> ChatClient | None:
    base = os.environ.get("LLM_BASE_URL")
    if not base:
        return None
    return ChatClient(base, os.environ.get("LLM_API_KEY"), _model_from_env("LLM_CHAT_MODEL"))


def embed_from_env() -> EmbedClient | None:
    base = os.environ.get("LLM_BASE_URL")
    if not base:
        return None
    return EmbedClient(base, os.environ.get("LLM_API_KEY"), _model_from_env("LLM_EMBED_MODEL"))
