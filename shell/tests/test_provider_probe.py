"""Failure-capable controls for the real-provider probe harness."""

from __future__ import annotations

import json
import threading
import time
from contextlib import ExitStack, contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Iterator

from intel_shell.llm import ChatClient, EmbedClient
from tools.probe_providers import (
    CAPABILITY_FAILED,
    IDENTITY_CHANGED,
    PASS,
    TRANSPORT_BLOCKED,
    probe_providers,
)


@contextmanager
def _provider_double(
    role: str,
    model: str,
    *,
    mode: str = "pass",
    dimension: int = 4,
) -> Iterator[str]:
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:
            return

        def _json(self, status: int, body: dict) -> None:
            encoded = json.dumps(body).encode()
            self.send_response(status)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(encoded)))
            self.end_headers()
            try:
                self.wfile.write(encoded)
            except BrokenPipeError:
                pass

        def do_GET(self) -> None:
            if mode == "stall" and self.path == "/health":
                time.sleep(0.2)
            if self.path == "/health":
                self._json(
                    200,
                    {
                        "status": "ok",
                        "authorization": self.headers.get("authorization"),
                    },
                )
                return
            if self.path == "/v1/models":
                observed_model = "wrong-model" if mode == "wrong-model" else model
                self._json(200, {"object": "list", "data": [{"id": observed_model}]})
                return
            self._json(404, {"error": "not found"})

        def do_POST(self) -> None:
            content_length = int(self.headers.get("content-length", "0"))
            if content_length:
                self.rfile.read(content_length)
            if self.path != "/v1/embeddings":
                self._json(404, {"error": "not found"})
                return
            if role == "chat":
                self._json(
                    501,
                    {
                        "error": {
                            "code": 501,
                            "message": (
                                "This server does not support embeddings. "
                                "Start it with `--embeddings`"
                            ),
                            "type": "not_supported_error",
                        }
                    },
                )
                return
            if mode == "short":
                self._json(200, {"model": model, "data": []})
                return
            width = dimension + 1 if mode == "wrong-dimension" else dimension
            self._json(
                200,
                {
                    "model": model,
                    "data": [{"index": 0, "embedding": [0.25] * width}],
                },
            )

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}/v1"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


def _run(
    *,
    chat_mode: str = "pass",
    embed_mode: str = "pass",
    timeout_seconds: float = 1,
) -> tuple[str, int, str]:
    with ExitStack() as stack:
        chat_base = stack.enter_context(
            _provider_double("chat", "expected-chat", mode=chat_mode)
        )
        embed_base = stack.enter_context(
            _provider_double(
                "embedding",
                "expected-embed",
                mode=embed_mode,
                dimension=4,
            )
        )
        chat = ChatClient(
            chat_base,
            "chat-secret",
            "expected-chat",
            timeout_seconds,
        )
        embed = EmbedClient(
            embed_base,
            "embed-secret",
            "expected-embed",
            timeout_seconds,
        )
        lines: list[str] = []
        try:
            result = probe_providers(chat, embed, 4, write=lines.append)
        finally:
            chat._c.close()
            embed._c.close()
    return result.classification, result.exit_code, "\n".join(lines)


def test_probe_passes_known_chat_diagnosis_and_one_embedding() -> None:
    classification, exit_code, output = _run()

    assert classification == PASS
    assert exit_code == 0
    assert "status=501" in output
    assert "embedding_dimension=4" in output
    assert "chat-secret" not in output
    assert "embed-secret" not in output
    assert output.count("[REDACTED]") >= 2


def test_probe_classifies_wrong_model_as_identity_changed() -> None:
    classification, exit_code, output = _run(chat_mode="wrong-model")

    assert classification == IDENTITY_CHANGED
    assert exit_code != 0
    assert "wrong-model" in output
    assert output.rstrip().endswith("observed ['wrong-model']")


def test_probe_classifies_short_embedding_data_as_capability_failed() -> None:
    classification, exit_code, output = _run(embed_mode="short")

    assert classification == CAPABILITY_FAILED
    assert exit_code != 0
    assert output.rstrip().endswith(
        "embedding response expected one item; observed 0"
    )


def test_probe_classifies_wrong_dimension_as_identity_changed() -> None:
    classification, exit_code, output = _run(embed_mode="wrong-dimension")

    assert classification == IDENTITY_CHANGED
    assert exit_code != 0
    assert output.rstrip().endswith(
        "embedding dimension expected 4; observed 5"
    )


def test_probe_classifies_stalled_response_as_transport_blocked() -> None:
    started = time.monotonic()
    classification, exit_code, output = _run(
        embed_mode="stall",
        timeout_seconds=0.05,
    )
    elapsed = time.monotonic() - started

    assert classification == TRANSPORT_BLOCKED
    assert exit_code != 0
    assert "ReadTimeout" in output
    assert "status=none body=none" in output
    assert elapsed < 1.5
