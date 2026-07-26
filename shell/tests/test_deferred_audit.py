from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import tools.audit_deferred as audit_deferred
from tools.audit_deferred import (
    attestation_boundary_measurement,
    control_measurements,
    evaluate,
)


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "audit_deferred.py"


def test_synthetic_measurements_promote_all_seven() -> None:
    rows = {row["id"]: row for row in evaluate(control_measurements())}
    assert len(rows) == 7
    assert all(row["disposition"] == "promote" for row in rows.values())


def test_control_command_exits_nonzero_and_names_both_triggers() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--control",
            "all-seven",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode != 0
    for item in (
        "T7 robots single-flight",
        "Postgres",
        "pgvector",
        "Multi-host seam hardening",
        "A4 untrusted-shell attestation boundary",
        "CI-runner evidence",
        "/view materialization",
    ):
        assert f"PROMOTE {item}" in result.stdout
    assert "CONTROL FIRED: all seven" in result.stdout


def test_each_row_keeps_its_unchanged_trigger() -> None:
    rows = evaluate(control_measurements())
    assert len(rows) == 7
    assert all(row["unchanged_trigger"] for row in rows)


def test_registry_trigger_text_is_not_an_affirmative_hc1_claim() -> None:
    measurement = attestation_boundary_measurement()
    assert measurement["hc1_invariant_under_shell_replacement_claims"] == []


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def _synthetic_repository(tmp_path: Path) -> tuple[Path, str, str, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.name", "CI Receipt Test")
    _git(repo, "config", "user.email", "ci-receipt@example.test")
    tracked = repo / "tracked.txt"
    tracked.write_text("base\n")
    _git(repo, "add", "tracked.txt")
    _git(repo, "commit", "-m", "base")
    base = _git(repo, "rev-parse", "HEAD")

    _git(repo, "switch", "-c", "foreign")
    tracked.write_text("foreign\n")
    _git(repo, "commit", "-am", "foreign")
    foreign = _git(repo, "rev-parse", "HEAD")

    _git(repo, "switch", "main")
    tracked.write_text("head\n")
    _git(repo, "commit", "-am", "head")
    head = _git(repo, "rev-parse", "HEAD")
    return repo, base, foreign, head


def _receipt(path: Path, sha: str) -> None:
    path.write_text(
        json.dumps(
            {
                "run_id": "123",
                "run_attempt": "1",
                "job": path.stem,
                "sha": sha,
                "conclusion": "success",
                "runner_os": "Linux",
                "completed_at": "2026-07-26T00:00:00Z",
            }
        )
        + "\n"
    )


def test_ancestor_runner_receipt_promotes_ci_row(tmp_path: Path) -> None:
    repo, ancestor, _, head = _synthetic_repository(tmp_path)
    receipt = tmp_path / "ancestor.json"
    _receipt(receipt, ancestor)

    measurement = audit_deferred.runner_receipt_measurement(
        [receipt],
        repository=repo,
        audited_head=head,
        logical_receipt_root=tmp_path,
    )
    measurements = control_measurements()
    measurements["ci_runner"] = measurement
    row = next(
        row
        for row in evaluate(measurements)
        if row["id"] == "CI-runner evidence"
    )

    assert measurement["observed_runner_executions"] == 1
    assert measurement["rejected_runner_receipts"] == []
    assert measurement["runner_receipts"] == [
        "evidence/ci-runs/ancestor.json"
    ]
    assert measurement["accepted_runner_receipts"][0]["path"] == (
        "evidence/ci-runs/ancestor.json"
    )
    assert measurement["workflow_configuration_counts_as_execution"] is False
    assert row["disposition"] == "promote"
    assert (
        row["unchanged_trigger"]
        == "a runner execution receipt exists for the released commit"
    )


def test_foreign_runner_receipt_is_visibly_rejected(tmp_path: Path) -> None:
    repo, _, foreign, head = _synthetic_repository(tmp_path)
    receipt = tmp_path / "foreign.json"
    _receipt(receipt, foreign)

    measurement = audit_deferred.runner_receipt_measurement(
        [receipt],
        repository=repo,
        audited_head=head,
    )
    measurements = control_measurements()
    measurements["ci_runner"] = measurement
    row = next(
        row
        for row in evaluate(measurements)
        if row["id"] == "CI-runner evidence"
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["accepted_runner_receipts"] == []
    assert measurement["rejected_runner_receipts"] == [
        {
            "path": str(receipt),
            "sha": foreign,
            "reason": f"sha is not an ancestor of audited head {head}",
        }
    ]
    assert row["disposition"] == "defer"


def test_zero_runner_receipts_defer_under_restated_trigger() -> None:
    measurements = control_measurements()
    measurements["ci_runner"] = {
        "git_remote_entry_count": 2,
        "observed_runner_executions": 0,
    }
    row = next(
        row
        for row in evaluate(measurements)
        if row["id"] == "CI-runner evidence"
    )

    assert row["disposition"] == "defer"
    assert (
        row["unchanged_trigger"]
        == "a runner execution receipt exists for the released commit"
    )


def test_every_workflow_job_emits_and_persists_a_receipt() -> None:
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
    source = TOOL.read_text()

    assert workflow.count("- name: emit CI-runner receipt") == 7
    assert workflow.count("- name: persist CI-runner receipt") == 7
    assert workflow.count("uses: actions/upload-artifact@v4") == 7
    assert workflow.count("ref: ${{ inputs.audit_sha || github.sha }}") == 7
    assert workflow.count("if: always()") >= 14
    assert (
        'receipts = sorted((ROOT / "evidence" / "ci-runs").glob("*.json"))'
        in source
    )
