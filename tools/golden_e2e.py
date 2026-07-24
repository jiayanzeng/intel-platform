#!/usr/bin/env python3
"""Executable assertions for the deterministic golden end-to-end pipeline.

The lifecycle belongs to ``./run golden``. This helper drives the already
started core, mock model, and public API over their real loopback HTTP seams,
runs both subscriber pipelines, and turns every documented golden value into a
named pass/fail result.
"""

from __future__ import annotations

import argparse
import contextlib
import io
from dataclasses import dataclass, field
from typing import Any

import httpx

from intel_shell import pipeline


ACME_AUTH = {"Authorization": "Bearer ak_acme_7f3d9c"}
QUANT_AUTH = {"Authorization": "Bearer ak_quant_2b81aa"}


@dataclass
class Checks:
    passed: int = 0
    failures: list[str] = field(default_factory=list)

    def check(self, label: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS  {label}")
            return
        self.failures.append(label)
        print(f"FAIL  {label}: {detail}")


def _pipeline_run(
    client: str,
    subscriptions: str,
    data_dir: str,
    core_url: str,
) -> tuple[int, str]:
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
        result = pipeline.run(
            client,
            subscriptions,
            data_dir,
            core_url,
            llm_enrich=False,
        )
    return result, captured.getvalue()


def _json(response: httpx.Response) -> Any:
    response.raise_for_status()
    return response.json()


def run(args: argparse.Namespace) -> int:
    checks = Checks()
    timeout = httpx.Timeout(30.0)
    with (
        httpx.Client(base_url=args.core_url, timeout=timeout, trust_env=False) as core,
        httpx.Client(base_url=args.api_url, timeout=timeout, trust_env=False) as api,
    ):
        initial = _json(
            core.post(
                "/ingest",
                json={"sectors": ["science", "technology"]},
            )
        )
        checks.check(
            "initial fixture ingest fetched=13, new=13",
            initial.get("fetched") == 13 and initial.get("new") == 13,
            f"observed fetched={initial.get('fetched')}, new={initial.get('new')}",
        )

        acme_code, acme_output = _pipeline_run(
            "acme-research",
            args.subscriptions,
            args.data_dir,
            args.core_url,
        )
        checks.check(
            "acme pipeline completes over the real core/model seams",
            acme_code == 0,
            f"exit={acme_code}\n{acme_output.rstrip()}",
        )

        view = _json(core.get("/view", params={"sectors": "science,technology"}))
        checks.check(
            "documents_analyzed == 12",
            view.get("documents_analyzed") == 12,
            f"observed {view.get('documents_analyzed')}",
        )

        expected_drop = {
            "dropped_id": "techwire::tw-004",
            "kept_id": "osdaily::osd-004",
            "distance": 12,
        }
        checks.check(
            "near-duplicate drops techwire::tw-004, keeps osdaily::osd-004 at hamming 12",
            view.get("near_duplicates") == [expected_drop],
            f"observed {view.get('near_duplicates')!r}",
        )

        deepseek = [
            signal
            for signal in view.get("signals", [])
            if signal.get("kind") == "RisingEntity"
            and signal.get("entity_ids") == ["deepseek"]
        ]
        deepseek_sources = (
            {e.get("source_id") for e in deepseek[0].get("evidence", [])}
            if len(deepseek) == 1
            else set()
        )
        checks.check(
            "DeepSeek is RISING at z=10.0 with three corroborating sources",
            len(deepseek) == 1
            and deepseek[0].get("score") == 10.0
            and deepseek_sources == {"arxiv-cs", "osdaily", "techwire"},
            (
                f"observed signals={deepseek!r}, "
                f"sources={sorted(str(s) for s in deepseek_sources)}"
            ),
        )

        second_acme = _json(
            core.post(
                "/ingest",
                json={"sectors": ["science", "technology"]},
            )
        )
        checks.check(
            "second acme ingest adds 0",
            second_acme.get("fetched") == 13 and second_acme.get("new") == 0,
            (
                f"observed fetched={second_acme.get('fetched')}, "
                f"new={second_acme.get('new')}"
            ),
        )

        quant_code, quant_output = _pipeline_run(
            "quant-desk",
            args.subscriptions,
            args.data_dir,
            args.core_url,
        )
        quant_signals = _json(api.get("/v1/signals", headers=QUANT_AUTH))
        checks.check(
            "quant-desk sees exactly 1 document",
            quant_code == 0 and quant_signals.get("documents_analyzed") == 1,
            (
                f"pipeline exit={quant_code}, "
                f"documents={quant_signals.get('documents_analyzed')}\n"
                f"{quant_output.rstrip()}"
            ),
        )

        ask = _json(
            api.get(
                "/v1/ask",
                params={"q": "What is DeepSeek-V4?"},
                headers=ACME_AUTH,
            )
        )
        checks.check(
            "/v1/ask returns 4 citations and suppresses techwire::tw-004",
            len(ask.get("citations", [])) == 4
            and ask.get("context_suppressed") == ["techwire::tw-004"],
            (
                f"observed citations={len(ask.get('citations', []))}, "
                f"suppressed={ask.get('context_suppressed')!r}"
            ),
        )

        acme_search = _json(
            api.get("/v1/search", params={"q": "deepseek"}, headers=ACME_AUTH)
        )
        quant_search = _json(
            api.get("/v1/search", params={"q": "deepseek"}, headers=QUANT_AUTH)
        )
        acme_hits = acme_search.get("hits", [])
        quant_hits = quant_search.get("hits", [])
        index_only_hits = [
            hit for hit in acme_hits if hit.get("license") == "IndexOnly"
        ]
        checks.check(
            "all IndexOnly search hits have snippet=null",
            bool(index_only_hits)
            and all(hit.get("snippet") is None for hit in index_only_hits),
            f"observed IndexOnly hits={index_only_hits!r}",
        )
        checks.check(
            "entitlement-disjoint deepseek search is acme=6, quant=0",
            len(acme_hits) == 6 and len(quant_hits) == 0,
            f"observed acme={len(acme_hits)}, quant={len(quant_hits)}",
        )

        bad_key = api.get(
            "/v1/signals",
            headers={"Authorization": "Bearer deliberately-bad-key"},
        )
        checks.check(
            "bad API key returns 401",
            bad_key.status_code == 401,
            f"observed HTTP {bad_key.status_code}",
        )

    total = checks.passed + len(checks.failures)
    if checks.failures:
        print(
            f"golden result: FAIL ({checks.passed}/{total} passed; "
            f"failed: {', '.join(checks.failures)})"
        )
        return 1
    print(f"golden result: PASS ({checks.passed}/{total} checks)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-url", required=True)
    parser.add_argument("--api-url", required=True)
    parser.add_argument("--data-dir", required=True)
    parser.add_argument(
        "--subscriptions",
        default="config/subscriptions.hashed.json",
    )
    return run(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
