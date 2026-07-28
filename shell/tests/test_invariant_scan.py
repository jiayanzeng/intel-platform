from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from tools import invariant_scan


ROOT = Path(__file__).resolve().parents[2]
RULES = ROOT / "config" / "invariant-rules.json"
PARAMETERIZED_RULE_IDS = tuple(
    rule.id for rule in invariant_scan.load_rules(RULES)
)
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
        "invariant-scan: R6 FAIL: docs/intel-platform-OPERATIONS.md: "
        "model-profile authorization block differs from AGENTS.md"
    ),
}


def assert_complete_rule_parameterization(
    rules: list[invariant_scan.Rule],
    parameterized_rule_ids: tuple[str, ...],
) -> None:
    registered = {rule.id for rule in rules}
    covered = set(parameterized_rule_ids)
    assert covered == registered, (
        "registered invariant rules missing from control parameterization: "
        f"{sorted(registered - covered)}; unexpected ids: "
        f"{sorted(covered - registered)}"
    )


@pytest.mark.parametrize("rule_id", PARAMETERIZED_RULE_IDS)
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
        assert (
            invariant_scan.expected_control_finding(rule, control)
            in output.splitlines()
        )


def test_control_parameterization_covers_every_registered_rule() -> None:
    rules = invariant_scan.load_rules(RULES)
    assert_complete_rule_parameterization(rules, PARAMETERIZED_RULE_IDS)
    assert all(rule.fail_before for rule in rules)


def test_control_parameterization_rejects_an_uncovered_rule() -> None:
    rules = invariant_scan.load_rules(RULES)
    uncovered = tuple(rule.id for rule in rules[:-1])

    with pytest.raises(AssertionError, match=rules[-1].id):
        assert_complete_rule_parameterization(rules, uncovered)


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


def test_control_rejects_a_failure_reported_at_the_wrong_site(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    payload = json.loads(RULES.read_text())
    r7 = next(rule for rule in payload["rules"] if rule["id"] == "R7")
    r7["fail_before"][1]["expected_line"] += 1
    registry = tmp_path / "wrong-site-rules.json"
    registry.write_text(json.dumps(payload) + "\n")

    assert invariant_scan.self_test(ROOT, registry, {"R7"}) == 1
    output = capsys.readouterr().out
    assert "missing expected finding" in output
    assert "apps/cored/src/main.rs:1136" in output


def test_overbroad_matcher_cannot_pass_a_control_at_an_unrelated_site(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    matcher = re.compile(
        r"(?:\.|::)\s*(?P<name>documents_by_ids)"
        r"(?=_in_sectors\s*\()"
    )
    monkeypatch.setattr(
        invariant_scan,
        "DOCUMENT_ID_HYDRATION_CALL",
        matcher,
    )
    rules = invariant_scan.load_rules(RULES)
    rule = next(item for item in rules if item.id == "R7")
    control = rule.fail_before[1]

    status, output = invariant_scan.exercise_fail_before(ROOT, rule, control)

    assert status == 1
    assert control.expected_fail in output
    assert (
        invariant_scan.expected_control_finding(rule, control)
        not in output.splitlines()
    )
    assert "apps/cored/src/main.rs:1182" in output


def test_malformed_registry_exits_two(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    registry = tmp_path / "rules.json"
    registry.write_text(
        json.dumps({"schema_version": 3, "rules": "not-an-array"}) + "\n"
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


def test_r10_reports_derived_scope_and_counted_exemptions() -> None:
    report = invariant_scan.r10_report(ROOT)

    assert report.findings == ()
    assert report.local_jobs == 20
    assert report.local_checks == 24
    assert report.blocking_jobs == 6
    assert report.hosted_checks == 23
    assert len(report.exemptions) == 45
    assert any(
        "protected database bytes are operator-local evidence" in exemption
        for exemption in report.exemptions
    )
    assert any(
        "continue-on-error=true makes it report-only" in exemption
        for exemption in report.exemptions
    )


def test_ci_workflow_parser_derives_current_blocking_identities() -> None:
    identities = invariant_scan.blocking_job_identities(
        ROOT / ".github" / "workflows" / "ci.yml"
    )

    assert identities == {
        ("core", None),
        ("golden", None),
        ("lint", None),
        ("msrv", None),
        ("net", None),
        ("shell", "python=3.11"),
        ("shell", "python=3.12"),
    }
