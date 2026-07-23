"""OpenAI-compatible chat + embedding clients (was crates/llm in Rust).

Moving this to the shell is the point of the whole refactor: model choice,
provider, temperature, retries — all product decisions that change weekly.
The Rust core neither knows nor cares which model answered.

One client shape covers every provider that matters here:
- DeepSeek's hosted API,
- a self-hosted vLLM / llama.cpp server on the LAN,
- tools/mock_openai.py for deterministic offline tests.

Env:
  LLM_CHAT_PROFILE       "lan" or "online"; selects one stored chat profile
  LLM_LAN_BASE_URL       LAN chat endpoint
  LLM_LAN_API_KEY        optional LAN Bearer token
  LLM_LAN_CHAT_MODEL     LAN chat model name
  LLM_ONLINE_BASE_URL    hosted chat endpoint
  LLM_ONLINE_API_KEY     hosted-provider Bearer token
  LLM_ONLINE_CHAT_MODEL  hosted chat model name

  LLM_CHAT_BASE_URL      direct chat endpoint when no profile is selected
  LLM_CHAT_API_KEY       direct chat Bearer token
  LLM_CHAT_MODEL         direct chat model name

  LLM_EMBED_BASE_URL     independent embedding endpoint
  LLM_EMBED_API_KEY      independent embedding Bearer token
  LLM_EMBED_MODEL        embedding model name

  LLM_BASE_URL / LLM_API_KEY / LLM_MODEL remain backward-compatible fallbacks
  for one provider that implements both chat and embeddings.

Chat and embeddings are separate deliberately. DeepSeek and many llama.cpp
servers implement chat completions but not POST /embeddings; pointing both roles
at such a server is a measured configuration failure, not graceful degradation.

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


def _chat_settings_from_env() -> tuple[str | None, str | None, str]:
    profile = os.environ.get("LLM_CHAT_PROFILE", "").strip().lower()
    if profile in {"lan", "online"}:
        prefix = f"LLM_{profile.upper()}"
        return (
            os.environ.get(f"{prefix}_BASE_URL") or None,
            os.environ.get(f"{prefix}_API_KEY") or None,
            os.environ.get(f"{prefix}_CHAT_MODEL")
            or _model_from_env("LLM_CHAT_MODEL"),
        )
    return (
        os.environ.get("LLM_CHAT_BASE_URL")
        or os.environ.get("LLM_BASE_URL")
        or None,
        os.environ.get("LLM_CHAT_API_KEY")
        or os.environ.get("LLM_API_KEY")
        or None,
        _model_from_env("LLM_CHAT_MODEL"),
    )


def _embed_settings_from_env() -> tuple[str | None, str | None, str]:
    return (
        os.environ.get("LLM_EMBED_BASE_URL")
        or os.environ.get("LLM_BASE_URL")
        or None,
        os.environ.get("LLM_EMBED_API_KEY")
        or os.environ.get("LLM_API_KEY")
        or None,
        _model_from_env("LLM_EMBED_MODEL"),
    )


class ChatClient:
    def __init__(self, base_url: str, api_key: str | None = None, model: str = "default"):
        self.base_url = base_url.rstrip("/")
        self.model = model
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self._c = httpx.Client(
            base_url=self.base_url, headers=headers, timeout=120.0
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
        self.base_url = base_url.rstrip("/")
        self.model = model
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self._c = httpx.Client(
            base_url=self.base_url, headers=headers, timeout=120.0
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
    base, api_key, model = _chat_settings_from_env()
    if not base:
        return None
    return ChatClient(base, api_key, model)


def embed_from_env() -> EmbedClient | None:
    base, api_key, model = _embed_settings_from_env()
    if not base:
        return None
    return EmbedClient(base, api_key, model)
