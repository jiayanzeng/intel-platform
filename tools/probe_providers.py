#!/usr/bin/env python3
"""Bounded, secret-safe capability probe for the resolved model roles."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import urllib.parse
from dataclasses import dataclass
from typing import Callable

import httpx

from intel_shell.llm import (
    ChatClient,
    EmbedClient,
    LlmError,
    chat_from_env,
    embed_from_env,
)


PASS = "PASS"
TRANSPORT_BLOCKED = "TRANSPORT BLOCKED"
IDENTITY_CHANGED = "IDENTITY CHANGED"
CAPABILITY_FAILED = "CAPABILITY FAILED"
MAX_BODY_CHARS = 2_000


@dataclass(frozen=True)
class ProbeResult:
    classification: str
    embedding_dimension: int | None = None

    @property
    def exit_code(self) -> int:
        return 0 if self.classification == PASS else 1


class ProbeFailure(RuntimeError):
    def __init__(self, classification: str, detail: str):
        super().__init__(detail)
        self.classification = classification


def _safe_url(raw: str) -> str:
    parsed = urllib.parse.urlsplit(raw)
    host = parsed.hostname or ""
    if ":" in host and not host.startswith("["):
        host = f"[{host}]"
    netloc = host
    if parsed.port is not None:
        netloc = f"{netloc}:{parsed.port}"
    return urllib.parse.urlunsplit(
        (parsed.scheme, netloc, parsed.path, "", "")
    ).rstrip("/")


def _api_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"


def _health_url(base_url: str) -> str:
    parsed = urllib.parse.urlsplit(base_url)
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, "/health", "", "")
    )


def _configured_secrets(
    chat: ChatClient,
    embed: EmbedClient,
) -> tuple[str, ...]:
    secrets: set[str] = set()
    for client in (chat._c, embed._c):
        authorization = client.headers.get("Authorization")
        if not authorization:
            continue
        secrets.add(authorization)
        if authorization.lower().startswith("bearer "):
            secrets.add(authorization[7:])
    return tuple(sorted((value for value in secrets if value), key=len, reverse=True))


def _redact(text: str, secrets: tuple[str, ...]) -> str:
    redacted = text
    for secret in secrets:
        redacted = redacted.replace(secret, "[REDACTED]")
    return re.sub(
        r"(?i)\bbearer\s+[^\s\"',}]+",
        "Bearer [REDACTED]",
        redacted,
    )


def _body(response: httpx.Response, secrets: tuple[str, ...]) -> str:
    compact = " ".join(response.text.split())
    if len(compact) > MAX_BODY_CHARS:
        compact = f"{compact[:MAX_BODY_CHARS]}…[truncated]"
    return _redact(compact or "<empty>", secrets)


def _request(
    client: httpx.Client,
    role: str,
    operation: str,
    method: str,
    url: str,
    secrets: tuple[str, ...],
    write: Callable[[str], None],
    *,
    json_body: dict | None = None,
) -> httpx.Response:
    safe_route = _safe_url(url)
    try:
        response = client.request(method, url, json=json_body)
    except httpx.TransportError as error:
        write(
            f"{role} {operation}: route={safe_route} status=none body=none "
            f"error={type(error).__name__}: "
            f"{_redact(str(error), secrets)}"
        )
        raise ProbeFailure(
            TRANSPORT_BLOCKED,
            f"{role} {operation} could not complete on {safe_route}",
        ) from error
    write(
        f"{role} {operation}: route={safe_route} status={response.status_code} "
        f"body={_body(response, secrets)}"
    )
    return response


def _json_object(response: httpx.Response, operation: str) -> dict:
    try:
        value = response.json()
    except json.JSONDecodeError as error:
        raise ProbeFailure(
            CAPABILITY_FAILED,
            f"{operation} did not return JSON",
        ) from error
    if not isinstance(value, dict):
        raise ProbeFailure(
            CAPABILITY_FAILED,
            f"{operation} returned a non-object JSON body",
        )
    return value


def _require_success(response: httpx.Response, operation: str) -> None:
    if not 200 <= response.status_code < 300:
        raise ProbeFailure(
            CAPABILITY_FAILED,
            f"{operation} returned HTTP {response.status_code}",
        )


def _model_ids(response: httpx.Response, operation: str) -> list[str]:
    _require_success(response, operation)
    body = _json_object(response, operation)
    data = body.get("data")
    if not isinstance(data, list):
        raise ProbeFailure(
            CAPABILITY_FAILED,
            f"{operation} omitted the model data list",
        )
    ids = [
        item.get("id")
        for item in data
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    ]
    if len(ids) != len(data):
        raise ProbeFailure(
            CAPABILITY_FAILED,
            f"{operation} returned a model entry without an id",
        )
    return ids


def _require_identity(
    response: httpx.Response,
    operation: str,
    expected_model: str,
) -> None:
    observed = _model_ids(response, operation)
    if expected_model not in observed:
        raise ProbeFailure(
            IDENTITY_CHANGED,
            f"{operation} expected model {expected_model!r}; "
            f"observed {observed!r}",
        )


def _require_chat_embedding_diagnosis(response: httpx.Response) -> None:
    text = response.text.lower()
    known_diagnosis = (
        "embedding" in text
        and ("--embeddings" in text or "not_supported" in text)
    )
    if response.status_code != 501 or not known_diagnosis:
        raise ProbeFailure(
            CAPABILITY_FAILED,
            "chat embeddings probe did not return the known HTTP 501 "
            "unsupported-capability diagnosis",
        )


def _embedding_dimension(
    response: httpx.Response,
    expected_model: str,
) -> int:
    _require_success(response, "embedding embeddings")
    body = _json_object(response, "embedding embeddings")
    response_model = body.get("model")
    if response_model is not None and response_model != expected_model:
        raise ProbeFailure(
            IDENTITY_CHANGED,
            f"embedding response expected model {expected_model!r}; "
            f"observed {response_model!r}",
        )
    data = body.get("data")
    if not isinstance(data, list) or len(data) != 1:
        observed = len(data) if isinstance(data, list) else "non-list"
        raise ProbeFailure(
            CAPABILITY_FAILED,
            f"embedding response expected one item; observed {observed}",
        )
    item = data[0]
    if not isinstance(item, dict) or item.get("index") != 0:
        raise ProbeFailure(
            CAPABILITY_FAILED,
            "embedding response did not contain exactly index 0",
        )
    vector = item.get("embedding")
    if not isinstance(vector, list) or not vector:
        raise ProbeFailure(
            CAPABILITY_FAILED,
            "embedding response did not contain a non-empty vector",
        )
    if any(
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        for value in vector
    ):
        raise ProbeFailure(
            CAPABILITY_FAILED,
            "embedding response contained a non-finite or non-numeric value",
        )
    return len(vector)


def probe_providers(
    chat: ChatClient,
    embed: EmbedClient,
    expected_embedding_dimension: int,
    *,
    write: Callable[[str], None] = print,
) -> ProbeResult:
    secrets = _configured_secrets(chat, embed)
    try:
        chat_health = _request(
            chat._c,
            "chat",
            "health",
            "GET",
            _health_url(chat.base_url),
            secrets,
            write,
        )
        _require_success(chat_health, "chat health")
        chat_models = _request(
            chat._c,
            "chat",
            "models",
            "GET",
            _api_url(chat.base_url, "models"),
            secrets,
            write,
        )
        _require_identity(chat_models, "chat models", chat.model)
        chat_embeddings = _request(
            chat._c,
            "chat",
            "embeddings",
            "POST",
            _api_url(chat.base_url, "embeddings"),
            secrets,
            write,
            json_body={"model": chat.model, "input": ["probe"]},
        )
        _require_chat_embedding_diagnosis(chat_embeddings)

        embed_health = _request(
            embed._c,
            "embedding",
            "health",
            "GET",
            _health_url(embed.base_url),
            secrets,
            write,
        )
        _require_success(embed_health, "embedding health")
        embed_models = _request(
            embed._c,
            "embedding",
            "models",
            "GET",
            _api_url(embed.base_url, "models"),
            secrets,
            write,
        )
        _require_identity(embed_models, "embedding models", embed.model)
        embed_response = _request(
            embed._c,
            "embedding",
            "embeddings",
            "POST",
            _api_url(embed.base_url, "embeddings"),
            secrets,
            write,
            json_body={"model": embed.model, "input": ["probe"]},
        )
        dimension = _embedding_dimension(embed_response, embed.model)
        if dimension != expected_embedding_dimension:
            raise ProbeFailure(
                IDENTITY_CHANGED,
                f"embedding dimension expected {expected_embedding_dimension}; "
                f"observed {dimension}",
            )
    except ProbeFailure as failure:
        write(f"{failure.classification}: {failure}")
        return ProbeResult(failure.classification)

    write(
        f"{PASS}: chat_model={chat.model} embedding_model={embed.model} "
        f"embedding_dimension={dimension}"
    )
    return ProbeResult(PASS, dimension)


def _expected_dimension(raw: str | None) -> int | None:
    if raw is None or not raw.strip():
        return None
    try:
        value = int(raw)
    except ValueError as error:
        raise LlmError(
            "LLM_EMBED_EXPECTED_DIMENSION must be a positive integer"
        ) from error
    if value <= 0:
        raise LlmError(
            "LLM_EMBED_EXPECTED_DIMENSION must be a positive integer"
        )
    return value


def print_config(
    chat: ChatClient | None,
    embed: EmbedClient | None,
    expected_dimension: int | None,
) -> None:
    print(
        "chat configured endpoint:",
        _safe_url(chat.provider_base_url) if chat else "(unset)",
    )
    print("chat effective endpoint:", _safe_url(chat.base_url) if chat else "(unset)")
    print("chat model:", chat.model if chat else "(unset)")
    print(
        "chat timeout:",
        f"{chat.timeout_seconds:g}s" if chat else "(unset)",
    )
    print(
        "embedding configured endpoint:",
        _safe_url(embed.provider_base_url) if embed else "(unset)",
    )
    print(
        "embedding effective endpoint:",
        _safe_url(embed.base_url) if embed else "(unset)",
    )
    print("embedding model:", embed.model if embed else "(unset)")
    print(
        "embedding timeout:",
        f"{embed.timeout_seconds:g}s" if embed else "(unset)",
    )
    print(
        "embedding expected dimension:",
        expected_dimension if expected_dimension is not None else "(unset)",
    )
    print("keys: redacted")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Probe the configured chat and embedding provider roles."
    )
    parser.add_argument(
        "--config-only",
        action="store_true",
        help="print effective redacted provider configuration without requests",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    chat: ChatClient | None = None
    embed: EmbedClient | None = None
    try:
        chat = chat_from_env()
        embed = embed_from_env()
        expected_dimension = _expected_dimension(
            os.environ.get("LLM_EMBED_EXPECTED_DIMENSION")
        )
        print_config(chat, embed, expected_dimension)
        if args.config_only:
            return 0
        if chat is None:
            print(f"{CAPABILITY_FAILED}: no chat provider identity resolved")
            return 1
        if embed is None:
            print(f"{CAPABILITY_FAILED}: no embedding provider identity resolved")
            return 1
        if expected_dimension is None:
            print(
                f"{CAPABILITY_FAILED}: set LLM_EMBED_EXPECTED_DIMENSION "
                "to the last wire-measured dimension before probing"
            )
            return 1
        result = probe_providers(chat, embed, expected_dimension)
        return result.exit_code
    except LlmError as error:
        print(f"{CAPABILITY_FAILED}: {error}")
        return 1
    finally:
        if chat is not None:
            chat._c.close()
        if embed is not None:
            embed._c.close()


def cli() -> None:
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print(f"{TRANSPORT_BLOCKED}: interrupted", file=sys.stderr)
        raise SystemExit(130) from None


if __name__ == "__main__":
    cli()
