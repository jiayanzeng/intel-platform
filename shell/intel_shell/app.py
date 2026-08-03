"""The public subscriber API (was apps/server in Rust).

Every endpoint follows the same three-step shape:
  1. auth: bearer key -> subscription (client + entitled sectors) — SHELL
  2. call the core with that explicit sector list                 — CORE
  3. shape/render the response for subscribers                    — SHELL

Run:  PYTHONPATH=shell uvicorn intel_shell.app:app --port 8787
"""

from __future__ import annotations

import json

from fastapi import FastAPI, Header, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse

from . import billing, config, prompts, security
from .adapters import stripe as stripe_adapter
from .auth import resolve
from .briefing import render_brief
from .config import BaseSubscriptionStore, SubscriptionStore
from .core_client import CoreClient, CoreError
from .llm import ChatClient, EmbedClient, chat_from_env, embed_from_env


def create_app(
    core: CoreClient,
    subscriptions: list[config.Subscription] | BaseSubscriptionStore,
    chat: ChatClient | None = None,
    embed: EmbedClient | None = None,
    billing_secret: str | None = None,
    stripe_secret: str | None = None,
) -> FastAPI:
    app = FastAPI(title="intel-platform shell", version="0.17.2")

    # A bare list still works (tests pass one); wrap it in an in-memory store
    # whose save() is a no-op so nothing accidentally writes to disk in tests.
    # Any backend implementing the store contract (JSON, SQLite) is accepted.
    store = (
        subscriptions
        if isinstance(subscriptions, BaseSubscriptionStore)
        else SubscriptionStore(list(subscriptions))
    )

    def _core_guard(fn, *args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except CoreError as e:
            status = 502 if e.status is None else 500
            raise HTTPException(status_code=status, detail=str(e)) from e

    # -- /health ---------------------------------------------------------------

    @app.get("/health")
    def health():
        try:
            core_health = core.health()
        except CoreError as e:
            return {"shell": "ok", "core": f"unreachable ({e})"}
        return {"shell": "ok", "core": core_health}

    # -- /v1/signals -------------------------------------------------------------

    @app.get("/v1/signals")
    def signals(authorization: str | None = Header(default=None)):
        sub = resolve(store.all(), authorization)
        view = _core_guard(core.view, list(sub.sectors))
        return {
            "client": sub.client,
            "sectors": list(sub.sectors),
            "window_end": view.get("window_end"),
            "documents_analyzed": view.get("documents_analyzed", 0),
            "near_duplicates_collapsed": len(view.get("near_duplicates", [])),
            "signals": view.get("signals", []),
            "graph": view.get("edges", [])[:12],
        }

    # -- /v1/search ---------------------------------------------------------------

    @app.get("/v1/search")
    def search(
        q: str,
        limit: int = Query(default=10, le=50),
        authorization: str | None = Header(default=None),
    ):
        sub = resolve(store.all(), authorization)
        try:
            hits = core.search(q, list(sub.sectors), limit)
        except CoreError as e:
            if e.status == 400:
                raise HTTPException(status_code=400, detail="invalid FTS5 query syntax")
            raise HTTPException(status_code=502, detail=str(e))
        return {"client": sub.client, "query": q, "hits": hits}

    # -- /v1/brief -----------------------------------------------------------------

    @app.get("/v1/brief")
    def brief(authorization: str | None = Header(default=None)):
        sub = resolve(store.all(), authorization)
        view = _core_guard(core.view, list(sub.sectors))
        text = render_brief(sub.client, list(sub.sectors), view, new_n=0)
        return PlainTextResponse(text, media_type="text/markdown; charset=utf-8")

    # -- /v1/ask ---------------------------------------------------------------------
    #
    # The Q&A layer: the SHELL embeds the query (LLM business), the CORE does
    # hybrid retrieval + near-dup suppression (math), the SHELL builds the
    # prompt and calls the chat model (LLM business again).

    @app.get("/v1/ask")
    def ask(
        q: str,
        k: int = Query(default=5, le=8),
        authorization: str | None = Header(default=None),
    ):
        sub = resolve(store.all(), authorization)
        if chat is None:
            raise HTTPException(
                status_code=503,
                detail=(
                    "ask requires a configured chat endpoint "
                    "(set LLM_CHAT_PROFILE/LLM_CHAT_BASE_URL; "
                    "legacy LLM_BASE_URL is also supported)"
                ),
            )

        extra_notes: list[str] = []
        model = None
        query_vector = None
        if embed is not None:
            try:
                query_vector = embed.embed([q])[0]
                model = embed.model
            except Exception as e:  # noqa: BLE001 — degrade, don't fail
                extra_notes.append(f"vector leg degraded: embed call failed ({e})")

        r = _core_guard(
            core.retrieve, q, list(sub.sectors), k=k, model=model, query_vector=query_vector
        )

        context, citations = prompts.build_context(r.get("context", []))
        user = prompts.build_ask_user(q, context)
        try:
            answer = chat.chat(prompts.ASK_SYSTEM, user)
        except Exception as e:  # noqa: BLE001
            raise HTTPException(status_code=502, detail=f"model endpoint error: {e}")

        # HC1 is enforced in core, against the license-bearing source rows. The
        # prompt remains useful guidance, but it is no longer the only barrier
        # between IndexOnly context and the public response.
        attestation = _core_guard(
            core.attest,
            answer,
            [citation["doc_id"] for citation in citations],
            list(sub.sectors),
        )
        answer = attestation["clean_answer"]

        return {
            "client": sub.client,
            "query": q,
            "answer": answer,
            "citations": citations,
            "context_suppressed": r.get("suppressed", []),
            "retrieval": {
                "bm25": r.get("bm25", []),
                "vector": r.get("vector", []),
                "fused": r.get("fused", []),
                "notes": r.get("notes", []) + extra_notes,
            },
        }

    # -- /v1/billing/webhook ---------------------------------------------------------
    #
    # A payment provider tells us a client's plan changed; we translate that
    # into entitled sectors and persist. Signature-verified, shell-only: the
    # core is never touched, so even a forged event can at most misgrant
    # sectors that the core would still filter against its own config.

    @app.post("/v1/billing/webhook")
    async def billing_webhook(
        request: Request,
        x_signature: str | None = Header(default=None),
    ):
        if not billing_secret:
            raise HTTPException(
                status_code=503,
                detail="billing webhook disabled (set BILLING_WEBHOOK_SECRET)",
            )
        raw = await request.body()
        if not security.verify_webhook_signature(billing_secret, raw, x_signature):
            raise HTTPException(status_code=401, detail="invalid webhook signature")

        try:
            body = json.loads(raw)
        except ValueError:
            raise HTTPException(status_code=400, detail="malformed JSON body")

        events = body.get("events") if isinstance(body, dict) else None
        if events is None:
            events = [body]
        elif not isinstance(events, list):
            raise HTTPException(status_code=400, detail="'events' must be a list")

        # Best-effort sector allow-list from the core (defense in depth). If the
        # core is unreachable we still apply the event but can't validate.
        known_sectors = None
        try:
            known_sectors = [s["id"] for s in core.sectors()]
        except CoreError:
            pass

        results = _apply_events(events, known_sectors)
        store.save()
        return {"received": len(events), "results": results}

    # -- /v1/billing/stripe ----------------------------------------------------------
    #
    # The same entitlement machinery, entered through a real provider's front
    # door. The adapter verifies Stripe's signature scheme and normalizes the
    # payload INTO the neutral events above — so this route adds a translation
    # layer, not a second entitlement model. Stripe event types we don't handle
    # are acknowledged and ignored: a 500 on an uninteresting event is how you
    # get your endpoint disabled by the provider's retry logic.

    @app.post("/v1/billing/stripe")
    async def billing_stripe(
        request: Request,
        stripe_signature: str | None = Header(default=None),
    ):
        if not stripe_secret:
            raise HTTPException(
                status_code=503,
                detail="stripe webhook disabled (set STRIPE_WEBHOOK_SECRET)",
            )
        raw = await request.body()
        if not stripe_adapter.verify_signature(stripe_secret, raw, stripe_signature):
            raise HTTPException(
                status_code=401, detail="invalid or stale stripe signature"
            )

        try:
            body = json.loads(raw)
        except ValueError:
            raise HTTPException(status_code=400, detail="malformed JSON body")
        if not isinstance(body, dict):
            raise HTTPException(status_code=400, detail="event must be an object")

        events = stripe_adapter.to_neutral_events(body)
        if not events:
            # Acknowledged, deliberately did nothing.
            return {
                "received": 1,
                "results": [
                    {"action": "ignored",
                     "reason": f"unhandled stripe event '{body.get('type')}'"}
                ],
            }

        known_sectors = None
        try:
            known_sectors = [s["id"] for s in core.sectors()]
        except CoreError:
            pass

        results = _apply_events(events, known_sectors)
        store.save()
        return {"received": 1, "results": results}

    def _apply_events(events: list, known_sectors: list[str] | None) -> list[dict]:
        """Validate a batch on detached state, then publish it in one mutation."""
        # Subscription records are frozen value objects, so this detached list
        # cannot mutate a record still visible through the live store.
        staged = SubscriptionStore(store.all())
        results = []
        try:
            for ev in events:
                if not isinstance(ev, dict):
                    raise HTTPException(
                        status_code=400, detail="each event must be an object"
                    )
                results.append(billing.apply_event(staged, ev, known_sectors))
        except billing.BillingError as e:
            raise HTTPException(status_code=400, detail=str(e))
        # Publish only after the whole batch validates. The route saves this
        # live snapshot immediately after return, preserving publish/save/result
        # ordering for both JSON and SQLite backends.
        store._subs = staged.all()
        return results

    return app


def _default_app() -> FastAPI:
    """Module-level app for `uvicorn intel_shell.app:app`."""
    return create_app(
        core=CoreClient(config.CORE_URL, token=config.CORE_TOKEN),
        subscriptions=config.load_subscription_store(),
        chat=chat_from_env(),
        embed=embed_from_env(),
        billing_secret=security.BILLING_WEBHOOK_SECRET,
        stripe_secret=stripe_adapter.STRIPE_WEBHOOK_SECRET,
    )


app = _default_app()
