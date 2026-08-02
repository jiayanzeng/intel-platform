from __future__ import annotations

import json
import re
import subprocess
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
        status, output, expected_line = invariant_scan.exercise_fail_before(
            ROOT,
            rule,
            control,
        )
        assert status == 1
        assert (
            invariant_scan.expected_control_finding(
                rule,
                control,
                expected_line,
            )
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
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    original = invariant_scan.CHECKS["R7"]

    def report_every_finding_one_line_late(root: Path) -> list[str]:
        shifted = []
        for finding in original(root):
            file_name, line, message = finding.split(":", 2)
            shifted.append(f"{file_name}:{int(line) + 1}:{message}")
        return shifted

    monkeypatch.setitem(
        invariant_scan.CHECKS,
        "R7",
        report_every_finding_one_line_late,
    )

    assert invariant_scan.self_test(ROOT, RULES, {"R7"}) == 1
    output = capsys.readouterr().out
    assert "missing expected finding" in output
    assert "crates/store/src/sqlite.rs:411" in output


def run_registry_self_test(registry: Path, rule_id: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            str(ROOT / "run"),
            "invariant-scan",
            "--rules",
            str(registry),
            "--rule",
            rule_id,
            "--self-test",
        ],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


@pytest.mark.parametrize(
    ("anchor", "occurrences"),
    [
        ("this anchor is absent from the constructed mutant", 0),
        (
            "        let changed = assign_canonical_ids_tx(&tx, max_distance)?;",
            2,
        ),
    ],
)
def test_real_entry_point_rejects_non_unique_mutant_anchors(
    tmp_path: Path,
    anchor: str,
    occurrences: int,
) -> None:
    payload = json.loads(RULES.read_text())
    payload["rules"][0]["fail_before"][0]["expected_anchor"] = anchor
    payload["rules"][0]["fail_before"][0].pop(
        "expected_anchor_line_offset",
        None,
    )
    registry = tmp_path / f"anchor-{occurrences}.json"
    registry.write_text(json.dumps(payload) + "\n")

    result = run_registry_self_test(registry, "R1")

    assert result.returncode == 1
    assert (
        "crates/store/src/sqlite.rs: expected_anchor occurs "
        f"{occurrences} times in constructed mutant; expected exactly 1"
        in result.stdout
    )


def test_anchor_present_only_in_replacement_resolves_against_mutant(
    tmp_path: Path,
) -> None:
    payload = json.loads(RULES.read_text())
    r3 = next(rule for rule in payload["rules"] if rule["id"] == "R3")
    r3["fail_before"][0]["expected_anchor"] = "use async_openai::Client;"
    r3["fail_before"][0].pop("expected_anchor_line_offset", None)
    registry = tmp_path / "mutant-only-anchor.json"
    registry.write_text(json.dumps(payload) + "\n")

    result = run_registry_self_test(registry, "R3")

    assert result.returncode == 0, result.stdout + result.stderr
    assert "SELF-TEST PASS (1/1 rules, 1 controls)" in result.stdout


def test_anchor_present_only_in_original_is_rejected_after_mutation(
    tmp_path: Path,
) -> None:
    payload = json.loads(RULES.read_text())
    r7 = next(rule for rule in payload["rules"] if rule["id"] == "R7")
    r7["fail_before"][0]["expected_anchor"] = (
        "    fn documents_by_ids(&self, ids: &[&str]) "
        "-> rusqlite::Result<Vec<Document>> {"
    )
    r7["fail_before"][0].pop("expected_anchor_line_offset", None)
    registry = tmp_path / "original-only-anchor.json"
    registry.write_text(json.dumps(payload) + "\n")

    result = run_registry_self_test(registry, "R7")

    assert result.returncode == 1
    assert (
        "crates/store/src/sqlite.rs: expected_anchor occurs 0 times in "
        "constructed mutant; expected exactly 1"
        in result.stdout
    )


def test_registered_anchors_are_not_substrings_only_of_replacement() -> None:
    rules = invariant_scan.load_rules(RULES)

    assert all(
        control.expected_anchor not in "".join(control.replace_with)
        for rule in rules
        for control in rule.fail_before
    )


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

    status, output, expected_line = invariant_scan.exercise_fail_before(
        ROOT,
        rule,
        control,
    )

    assert status == 1
    assert control.expected_fail in output
    assert (
        invariant_scan.expected_control_finding(
            rule,
            control,
            expected_line,
        )
        not in output.splitlines()
    )
    assert "apps/cored/src/main.rs:1298" in output


def test_malformed_registry_exits_two(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    registry = tmp_path / "rules.json"
    registry.write_text(
        json.dumps({"schema_version": 4, "rules": "not-an-array"}) + "\n"
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


def test_r10_derives_every_exemption_without_pinning_its_count() -> None:
    report = invariant_scan.r10_report(ROOT)

    assert report.findings == ()
    assert report.local_jobs == 20
    assert report.local_checks == 24
    assert report.blocking_jobs == 6
    assert report.hosted_checks == 23
    assert len(report.exemptions) == len(report.exemption_bases)
    structural = set(invariant_scan.EXEMPTION_CRITERIA)
    residual_prefix = "named-local-check:"
    assert all(
        basis in structural or basis.startswith(residual_prefix)
        for basis in report.exemption_bases
    )
    assert {
        basis.removeprefix(residual_prefix)
        for basis in report.exemption_bases
        if basis.startswith(residual_prefix)
    } == set(invariant_scan.RESIDUAL_LOCAL_CHECK_EXEMPTIONS)
    assert any(
        "protected database bytes are operator-local evidence" in exemption
        for exemption in report.exemptions
    )
    assert any(
        invariant_scan.EXEMPTION_CRITERIA["report-only-job"] in exemption
        for exemption in report.exemptions
    )

    run_text = (ROOT / "run").read_text()
    functions = invariant_scan._bash_functions(run_text)
    dispatch = {
        match.group("command"): match.group("target")
        for match in invariant_scan.RUN_DISPATCH.finditer(run_text)
    }
    workflow = invariant_scan.parse_ci_workflow(
        ROOT / ".github" / "workflows" / "ci.yml"
    )
    for job in workflow:
        if job.report_only:
            continue
        for index, step in enumerate(job.steps):
            decision = invariant_scan._hosted_step_exemption(job, index)
            checks = invariant_scan._workflow_step_check_ids(
                step,
                functions,
                dispatch,
            )
            assert not (decision is not None and checks), (
                f"{job.id}/{step.name} moved a parity check into an "
                f"exemption class: {sorted(checks)}"
            )
            assert decision is not None or checks, (
                f"{job.id}/{step.name} is neither parity-covered nor exempt"
            )

    setup = invariant_scan.WorkflowStep(
        job="control",
        name="new setup action",
        line=1,
        run_line=None,
        run=None,
        uses="example/setup-runner@v1",
        condition=None,
        source="- uses: example/setup-runner@v1",
    )
    command = invariant_scan.WorkflowStep(
        job="control",
        name="check",
        line=2,
        run_line=2,
        run="./run version-check",
        uses=None,
        condition=None,
        source="- name: check\n  run: ./run version-check",
    )
    receipt = invariant_scan.WorkflowStep(
        job="control",
        name="new receipt persistence",
        line=3,
        run_line=3,
        run='printf "%s\\n" "$CI_RECEIPT_PATH"',
        uses=None,
        condition="always()",
        source=(
            "- name: new receipt persistence\n"
            "  if: always()\n"
            '  run: printf "%s\\n" "$CI_RECEIPT_PATH"'
        ),
    )
    control_job = invariant_scan.WorkflowJob(
        id="control",
        line=1,
        report_only=False,
        matrix=(),
        steps=(setup, command, receipt),
    )
    assert invariant_scan._hosted_step_exemption(
        control_job,
        0,
    ) == invariant_scan.ExemptionDecision(
        "runner-setup-action",
        invariant_scan.EXEMPTION_CRITERIA["runner-setup-action"],
    )
    assert invariant_scan._hosted_step_exemption(
        control_job,
        2,
    ) == invariant_scan.ExemptionDecision(
        "receipt-attestation-persistence",
        invariant_scan.EXEMPTION_CRITERIA[
            "receipt-attestation-persistence"
        ],
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
