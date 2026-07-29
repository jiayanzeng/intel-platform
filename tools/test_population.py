#!/usr/bin/env python3
"""Compare local and hosted pytest populations without transcribing counts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, NamedTuple


SUMMARY_PREFIX = "test-population-summary: "
COMPARE_PREFIX = "test-population-compare: "


class PopulationError(ValueError):
    """A population summary or comparison is invalid."""


class Skip(NamedTuple):
    node_id: str
    reason: str
    markers: tuple[str, ...]


class Summary(NamedTuple):
    collected: int
    passed: int
    failed: int
    on_site: tuple[str, ...]
    skipped: tuple[Skip, ...]


def _integer(payload: dict[str, Any], field: str, label: str) -> int:
    value = payload.get(field)
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise PopulationError(f"{label}: {field} must be a non-negative integer")
    return value


def _string_list(value: object, field: str, label: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise PopulationError(f"{label}: {field} must be a list of named strings")
    if len(value) != len(set(value)):
        raise PopulationError(f"{label}: {field} contains duplicate names")
    return tuple(value)


def parse_summary(payload: object, label: str) -> Summary:
    if not isinstance(payload, dict):
        raise PopulationError(f"{label}: summary must be a JSON object")
    expected = {
        "schema_version",
        "collected",
        "passed",
        "failed",
        "on_site",
        "skipped",
    }
    if set(payload) != expected:
        raise PopulationError(
            f"{label}: summary keys must be exactly {sorted(expected)}"
        )
    if payload["schema_version"] != 1:
        raise PopulationError(f"{label}: schema_version must be 1")

    collected = _integer(payload, "collected", label)
    passed = _integer(payload, "passed", label)
    failed = _integer(payload, "failed", label)
    on_site = _string_list(payload["on_site"], "on_site", label)
    raw_skips = payload["skipped"]
    if not isinstance(raw_skips, list):
        raise PopulationError(f"{label}: skipped must be a list")

    skipped: list[Skip] = []
    seen_skips: set[str] = set()
    for index, raw_skip in enumerate(raw_skips):
        where = f"{label}: skipped[{index}]"
        if not isinstance(raw_skip, dict) or set(raw_skip) != {
            "node_id",
            "reason",
            "markers",
        }:
            raise PopulationError(
                f"{where} keys must be exactly markers, node_id, and reason"
            )
        node_id = raw_skip["node_id"]
        reason = raw_skip["reason"]
        if not isinstance(node_id, str) or not node_id:
            raise PopulationError(f"{where}: node_id must be named")
        if node_id in seen_skips:
            raise PopulationError(f"{where}: duplicate node_id {node_id!r}")
        if not isinstance(reason, str) or not reason.strip():
            raise PopulationError(f"{where}: reason must be present")
        markers = _string_list(raw_skip["markers"], "markers", where)
        # Invariant R12 control site: test-population equivalence.
        if "on_site" not in markers:
            raise PopulationError(
                f"{where}: skipped node {node_id!r} is not marked on_site"
            )
        if node_id not in on_site:
            raise PopulationError(
                f"{where}: skipped node {node_id!r} is absent from on_site"
            )
        seen_skips.add(node_id)
        skipped.append(Skip(node_id, reason.strip(), markers))

    if collected != passed + failed + len(skipped):
        raise PopulationError(
            f"{label}: collected {collected} does not equal passed {passed} + "
            f"failed {failed} + skipped {len(skipped)}"
        )
    return Summary(
        collected=collected,
        passed=passed,
        failed=failed,
        on_site=on_site,
        skipped=tuple(skipped),
    )


def load_summary(path: Path, label: str) -> Summary:
    try:
        text = path.read_text()
    except OSError as error:
        raise PopulationError(f"{label}: cannot read {path}: {error}") from error
    try:
        return parse_summary(json.loads(text), label)
    except json.JSONDecodeError:
        candidates = [
            line.partition(SUMMARY_PREFIX)[2]
            for line in text.splitlines()
            if SUMMARY_PREFIX in line
        ]
        if len(candidates) != 1:
            raise PopulationError(
                f"{label}: expected exactly one {SUMMARY_PREFIX.strip()!r} "
                f"record, found {len(candidates)}"
            )
        try:
            payload = json.loads(candidates[0])
        except json.JSONDecodeError as error:
            raise PopulationError(
                f"{label}: population record is not valid JSON: {error}"
            ) from error
        return parse_summary(payload, label)


def compare_populations(local: Summary, hosted: Summary) -> dict[str, Any]:
    if local.failed or hosted.failed:
        raise PopulationError(
            "test failures prevent population equivalence: "
            f"local failed {local.failed}, hosted failed {hosted.failed}"
        )
    if local.collected != hosted.collected:
        raise PopulationError(
            "collected mismatch: "
            f"local {local.collected}, hosted {hosted.collected}"
        )
    hosted_on_site_skips = len(hosted.skipped)
    equivalent_passed = hosted.passed + hosted_on_site_skips
    if local.passed != equivalent_passed:
        raise PopulationError(
            "passed population mismatch: "
            f"local {local.passed}, hosted {hosted.passed} + "
            f"hosted on_site skips {hosted_on_site_skips}"
        )
    return {
        "collected": local.collected,
        "equivalent": True,
        "equivalent_passed": equivalent_passed,
        "hosted": {
            "on_site_skipped": hosted_on_site_skips,
            "passed": hosted.passed,
            "skipped": [
                {
                    "node_id": skip.node_id,
                    "reason": skip.reason,
                }
                for skip in hosted.skipped
            ],
        },
        "local": {
            "passed": local.passed,
            "skipped": len(local.skipped),
        },
        "schema_version": 1,
    }


def verify_hosted_claim(
    comparison: dict[str, Any],
    claimed_passed: int,
    claimed_skipped: int,
) -> None:
    hosted = comparison["hosted"]
    actual_passed = hosted["passed"]
    actual_skipped = hosted["on_site_skipped"]
    if (claimed_passed, claimed_skipped) != (actual_passed, actual_skipped):
        raise PopulationError(
            "hosted claim mismatch: "
            f"claimed passed {claimed_passed}, skipped {claimed_skipped}; "
            f"comparator derived passed {actual_passed}, skipped {actual_skipped}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("local", type=Path, help="local summary or pytest log")
    parser.add_argument("hosted", type=Path, help="hosted summary or pytest log")
    parser.add_argument("--claim-hosted-passed", type=int)
    parser.add_argument("--claim-hosted-skipped", type=int)
    args = parser.parse_args(argv)
    if (args.claim_hosted_passed is None) != (
        args.claim_hosted_skipped is None
    ):
        parser.error("both hosted claim fields must be supplied together")

    try:
        local = load_summary(args.local, "local")
        hosted = load_summary(args.hosted, "hosted")
        comparison = compare_populations(local, hosted)
        if args.claim_hosted_passed is not None:
            verify_hosted_claim(
                comparison,
                args.claim_hosted_passed,
                args.claim_hosted_skipped,
            )
    except PopulationError as error:
        print(f"test-population-compare: FAIL: {error}", file=sys.stderr)
        return 1

    print(
        COMPARE_PREFIX
        + json.dumps(comparison, sort_keys=True, separators=(",", ":"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
