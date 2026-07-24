"""CoreClient: the shell's only door into the Rust core.

Eleven methods over eleven endpoints — that is the entire seam between the two
layers. Anything the shell can't do through this client is, by design,
something the shell shouldn't be doing.

The `transport` parameter exists so tests can inject httpx.MockTransport
and exercise the whole shell without a running core.
"""

from __future__ import annotations

import ipaddress
from typing import Any
from urllib.parse import urlsplit

import httpx


class CoreError(RuntimeError):
    """The core returned an error or was unreachable."""

    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


def _is_loopback_url(base_url: str) -> bool:
    host = urlsplit(base_url).hostname
    if host is None:
        return False
    if host.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


class CoreClient:
    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        transport: httpx.BaseTransport | None = None,
        timeout: float = 120.0,
    ):
        headers = {"x-core-token": token} if token else {}
        # The core's supported deployment is loopback-internal. Letting httpx
        # inherit a macOS/system HTTP proxy for 127.0.0.1 produced real
        # "Server disconnected" failures even while curl proved cored healthy.
        # A future remote CORE_URL may legitimately need proxy settings, so only
        # loopback disables environment proxy discovery.
        self._c = httpx.Client(
            base_url=base_url,
            headers=headers,
            timeout=timeout,
            transport=transport,
            trust_env=not _is_loopback_url(base_url),
        )

    # -- plumbing ------------------------------------------------------------

    def _json(self, resp: httpx.Response) -> Any:
        if resp.status_code >= 400:
            raise CoreError(
                f"core returned {resp.status_code}: {resp.text[:300]}",
                status=resp.status_code,
            )
        return resp.json()

    def _get(self, path: str, **params: Any) -> Any:
        try:
            return self._json(self._c.get(path, params=params))
        except httpx.TransportError as e:
            raise CoreError(f"core unreachable: {e}") from e

    def _post(self, path: str, payload: dict) -> Any:
        try:
            return self._json(self._c.post(path, json=payload))
        except httpx.TransportError as e:
            raise CoreError(f"core unreachable: {e}") from e

    # -- the contract ----------------------------------------------------------

    def health(self) -> dict:
        return self._get("/health")

    def sectors(self) -> list[dict]:
        return self._get("/sectors")

    def ingest(self, sectors: list[str], sources: list[str] | None = None) -> dict:
        payload: dict[str, Any] = {"sectors": list(sectors)}
        # Omit `sources` entirely when unset so a sector-only request is
        # byte-identical to the pre-per-source body (the core reads it as
        # "run every source in these sectors").
        if sources is not None:
            payload["sources"] = list(sources)
        return self._post("/ingest", payload)

    def view(self, sectors: list[str]) -> dict:
        return self._get("/view", sectors=",".join(sectors))

    def search(self, q: str, sectors: list[str], limit: int = 10) -> list[dict]:
        return self._get("/search", q=q, sectors=",".join(sectors), limit=limit)

    def retrieve(
        self,
        q: str,
        sectors: list[str],
        k: int = 5,
        model: str | None = None,
        query_vector: list[float] | None = None,
    ) -> dict:
        payload: dict[str, Any] = {"q": q, "sectors": list(sectors), "k": k}
        if model is not None and query_vector is not None:
            payload["model"] = model
            payload["query_vector"] = query_vector
        return self._post("/retrieve", payload)

    def attest(self, answer: str, context_doc_ids: list[str]) -> dict:
        return self._post(
            "/attest",
            {"answer": answer, "context_doc_ids": list(context_doc_ids)},
        )

    def embeddings_missing(self, model: str) -> list[dict]:
        return self._get("/embeddings/missing", model=model)

    def embeddings_stats(self, model: str) -> dict:
        return self._get("/embeddings/stats", model=model)

    def upsert_embeddings(self, model: str, items: list[dict]) -> dict:
        """items: [{"doc_id": ..., "vector": [...]}, ...]"""
        return self._post("/embeddings", {"model": model, "items": items})

    def record_signals(
        self, client: str, window_end: str | None, signals: list[dict]
    ) -> dict:
        return self._post(
            "/signals/record",
            {"client": client, "window_end": window_end, "signals": signals},
        )

    def docs(self, ids: list[str]) -> list[dict]:
        return self._get("/docs", ids=",".join(ids))
