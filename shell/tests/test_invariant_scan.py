from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from tools import invariant_scan


ROOT = Path(__file__).resolve().parents[2]
RULES = ROOT / "config" / "invariant-rules.json"
LEGACY_FAIL_BEFORE_NOTES = {
    "R1": (
        "invariant-scan: R1 FAIL: apps/cored/src/main.rs:1267: "
        "production assign_canonical_ids call outside the store"
    ),
    "R2": (
        "invariant-scan: R2 FAIL: apps/cored/src/main.rs:1267: "
        "TcpListener bind outside the validated bind_addresses path"
    ),
    "R3": (
        "invariant-scan: R3 FAIL: crates/core/src/lib.rs:16: "
        "LLM client import"
    ),
    "R4": (
        "invariant-scan: R4 FAIL: README.md:1: "
        "provider-key-shaped value"
    ),
    "R5": (
        "invariant-scan: R5 FAIL: crates/store/src/sqlite.rs:33: "
        "second canonical-distance constant SECOND_DEDUP_MAX_DISTANCE=17"
    ),
    "R6": (
        "invariant-scan: R6 FAIL: intel-platform-OPERATIONS.md: "
        "model-profile authorization block differs from AGENTS.md"
    ),
}


@pytest.mark.parametrize("rule_id", [f"R{number}" for number in range(1, 8)])
def test_each_registered_rule_passes_clean_and_fires_its_controls(
    rule_id: str,
) -> None:
    rules = invariant_scan.load_rules(RULES)
    rule = next(item for item in rules if item.id == rule_id)

    assert invariant_scan.CHECKS[rule.id](ROOT) == []
    for control in rule.fail_before:
        status, output = invariant_scan.exercise_fail_before(
            ROOT,
            rule,
            control,
        )
        assert status == 1
        assert control.expected_fail in output


def test_every_legacy_fail_before_string_is_preserved_as_a_note() -> None:
    rules = invariant_scan.load_rules(RULES)
    by_id = {rule.id: rule for rule in rules}
    assert {
        rule_id: by_id[rule_id].fail_before_note
        for rule_id in LEGACY_FAIL_BEFORE_NOTES
    } == LEGACY_FAIL_BEFORE_NOTES


def test_self_test_rejects_a_rule_whose_regex_cannot_match(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(invariant_scan, "PROVIDER_KEY", re.compile(r"(?!)"))

    assert invariant_scan.self_test(ROOT, RULES, {"R4"}) == 1
    assert "mutation did not make the rule fail" in capsys.readouterr().out


def test_malformed_registry_exits_two(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    registry = tmp_path / "rules.json"
    registry.write_text(
        json.dumps({"schema_version": 2, "rules": "not-an-array"}) + "\n"
    )

    assert invariant_scan.run(ROOT, registry) == 2
    assert "CONFIG FAIL" in capsys.readouterr().out


def test_rule_id_without_an_implemented_check_exits_two(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    payload = json.loads(RULES.read_text())
    payload["rules"][0]["id"] = "R99"
    registry = tmp_path / "rules.json"
    registry.write_text(json.dumps(payload) + "\n")

    assert invariant_scan.run(ROOT, registry) == 2
    assert "no implemented check for R99" in capsys.readouterr().out
