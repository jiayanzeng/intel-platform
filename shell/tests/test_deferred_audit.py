from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

import tools.audit_deferred as audit_deferred
from tools.audit_deferred import (
    attestation_boundary_measurement,
    control_measurements,
    evaluate,
)


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "audit_deferred.py"
COMMITTED_RECEIPT = (
    ROOT / "evidence" / "v0.10.1" / "deferred-audit" / "report.json"
)


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


def _receipt(
    path: Path,
    sha: str,
    *,
    job: str = "core",
    conclusion: str = "success",
    run_id: str = "123",
    run_attempt: str = "1",
    repository: str = "example/repo",
    workflow: str = "CI",
) -> None:
    path.write_text(
        json.dumps(
            {
                "run_id": run_id,
                "run_attempt": run_attempt,
                "job": job,
                "workflow": workflow,
                "repository": repository,
                "event_sha": sha,
                "sha": sha,
                "conclusion": conclusion,
                "runner_os": "Linux",
                "completed_at": "2026-07-26T00:00:00Z",
            }
        )
        + "\n"
    )


def _receipt_matrix(
    root: Path,
    sha: str,
    *,
    omit: str | None = None,
    split_job: str | None = None,
) -> list[Path]:
    jobs = ("core", "golden", "lint", "msrv", "net", "shell", "shell")
    paths: list[Path] = []
    omitted = False
    for index, job in enumerate(jobs):
        if job == omit and not omitted:
            omitted = True
            continue
        path = root / f"{index}-{job}.json"
        _receipt(
            path,
            sha,
            job=job,
            run_id="other-run" if job == split_job else "123",
        )
        paths.append(path)
    return paths


def test_non_release_ancestor_receipt_is_rejected(tmp_path: Path) -> None:
    repo, ancestor, _, head = _synthetic_repository(tmp_path)
    receipt = tmp_path / "ancestor.json"
    _receipt(receipt, ancestor)

    measurement = audit_deferred.runner_receipt_measurement(
        [receipt],
        repository=repo,
        audited_head=head,
        released_commit=head,
        logical_receipt_root=tmp_path,
    )
    measurements = control_measurements()
    measurements["ci_runner"] = measurement
    row = next(
        row
        for row in evaluate(measurements)
        if row["id"] == "CI-runner evidence"
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["runner_receipts"] == [
        "evidence/ci-runs/ancestor.json"
    ]
    assert measurement["accepted_runner_receipts"] == []
    assert measurement["rejected_runner_receipts"][0]["reason"] == (
        f"sha does not equal released commit {head}"
    )
    assert measurement["workflow_configuration_counts_as_execution"] is False
    assert row["disposition"] == "defer"


def test_foreign_runner_receipt_is_visibly_rejected(tmp_path: Path) -> None:
    repo, _, foreign, head = _synthetic_repository(tmp_path)
    receipt = tmp_path / "foreign.json"
    _receipt(receipt, foreign)

    measurement = audit_deferred.runner_receipt_measurement(
        [receipt],
        repository=repo,
        audited_head=head,
        released_commit=head,
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


def test_failed_receipt_is_visibly_rejected(tmp_path: Path) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    _receipt(
        receipts[0],
        head,
        job="core",
        conclusion="failure",
    )

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
    )

    assert measurement["observed_runner_executions"] == 0
    assert any(
        item["reason"] == "conclusion is not success: failure"
        for item in measurement["rejected_runner_receipts"]
    )


@pytest.mark.parametrize(
    ("omit", "split_job", "finding"),
    [
        ("golden", None, "job counts"),
        (None, "golden", "single run_id/run_attempt"),
    ],
)
def test_partial_or_multi_run_matrix_does_not_promote(
    tmp_path: Path,
    omit: str | None,
    split_job: str | None,
    finding: str,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(
        tmp_path,
        head,
        omit=omit,
        split_job=split_job,
    )

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
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
    assert any(
        finding in item for item in measurement["matrix_findings"]
    )
    assert row["disposition"] == "defer"


def test_complete_release_matrix_from_one_run_promotes(tmp_path: Path) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
    )
    measurements = control_measurements()
    measurements["ci_runner"] = measurement
    row = next(
        row
        for row in evaluate(measurements)
        if row["id"] == "CI-runner evidence"
    )

    assert measurement["observed_runner_executions"] == 7
    assert len(measurement["accepted_runner_receipts"]) == 7
    assert measurement["rejected_runner_receipts"] == []
    assert measurement["matrix_findings"] == []
    assert row["disposition"] == "promote"


def test_authenticated_matrix_requires_every_bundle(tmp_path: Path) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
        attestation_bundles_dir=tmp_path,
        require_attestations=True,
        expected_repository="example/repo",
        expected_workflow=(
            "github.com/example/repo/.github/workflows/ci.yml"
        ),
        attestation_verifier=lambda *_: None,
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["accepted_runner_receipts"] == []
    assert len(measurement["rejected_runner_receipts"]) == 7
    assert all(
        "required attestation bundle is missing" in item["reason"]
        for item in measurement["rejected_runner_receipts"]
    )


def test_authenticated_complete_matrix_promotes(tmp_path: Path) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    for receipt in receipts:
        receipt.with_name(f"{receipt.name}.sigstore").write_text(
            "synthetic signed bundle\n"
        )
    verified: list[tuple[Path, Path, str, str]] = []

    def verifier(
        receipt: Path,
        bundle: Path,
        repository: str,
        workflow: str,
    ) -> None:
        verified.append((receipt, bundle, repository, workflow))

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
        attestation_bundles_dir=tmp_path,
        require_attestations=True,
        expected_repository="example/repo",
        expected_workflow=(
            "github.com/example/repo/.github/workflows/ci.yml"
        ),
        attestation_verifier=verifier,
    )

    assert measurement["observed_runner_executions"] == 7
    assert len(measurement["accepted_runner_receipts"]) == 7
    assert all(
        receipt["attestation_verified"]
        for receipt in measurement["accepted_runner_receipts"]
    )
    assert len(verified) == 7
    assert {call[2] for call in verified} == {"example/repo"}
    assert {call[3] for call in verified} == {
        "github.com/example/repo/.github/workflows/ci.yml"
    }


def test_authenticated_matrix_rejects_invalid_bundle(tmp_path: Path) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    for receipt in receipts:
        receipt.with_name(f"{receipt.name}.sigstore").write_text(
            "invalid bundle\n"
        )

    def reject_bundle(*_: object) -> None:
        raise audit_deferred.AuditFailure(
            "GitHub attestation verification failed: invalid bundle"
        )

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
        attestation_bundles_dir=tmp_path,
        require_attestations=True,
        expected_repository="example/repo",
        expected_workflow=(
            "github.com/example/repo/.github/workflows/ci.yml"
        ),
        attestation_verifier=reject_bundle,
    )

    assert measurement["observed_runner_executions"] == 0
    assert len(measurement["rejected_runner_receipts"]) == 7
    assert all(
        item["reason"]
        == "GitHub attestation verification failed: invalid bundle"
        for item in measurement["rejected_runner_receipts"]
    )


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
    assert workflow.count("uses: actions/attest-build-provenance@v4") == 7
    assert workflow.count("steps.attest.outputs.bundle-path") == 7
    assert "publish_evidence:" in workflow
    assert "id-token: write" in workflow
    assert "attestations: write" in workflow
    assert workflow.count("- name: re-derive pinned deferred evidence") == 1
    assert (
        "--rederive evidence/v0.10.1/deferred-audit/report.json"
        in workflow
    )
    assert (
        'receipts = sorted((ROOT / "evidence" / "ci-runs").glob("*.json"))'
        in source
    )


def test_source_deterministic_receipt_rederivation_passes() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--rederive",
            str(COMMITTED_RECEIPT),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "re-derivation: PASS" in result.stdout
    assert "rows=7" in result.stdout
    assert "source_dispositions=5" in result.stdout
    assert "triggers=7" in result.stdout


def test_source_rederivation_rejects_planted_disposition(
    tmp_path: Path,
) -> None:
    report = json.loads(COMMITTED_RECEIPT.read_text())
    row = next(
        row
        for row in report["triggers"]
        if row["id"] == "T7 robots single-flight"
    )
    row["disposition"] = "promote"
    changed = tmp_path / "changed-receipt.json"
    changed.write_text(json.dumps(report) + "\n")

    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--rederive",
            str(changed),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "REDERIVATION MISMATCH source_dispositions" in result.stderr
    assert '"T7 robots single-flight": "promote"' in result.stderr


@pytest.mark.skipif(
    not (
        (ROOT / "data" / "core.db").is_file()
        and (ROOT / "data" / "live-smoke.db").is_file()
        and (ROOT / "target" / "debug" / "cored").is_file()
    ),
    reason="on-site production audit requires protected corpora and built cored",
)
def test_on_site_production_measurements_match_committed_receipt() -> None:
    report = json.loads(COMMITTED_RECEIPT.read_text())
    expected = audit_deferred.committed_rederivation_snapshot(report)

    measured = audit_deferred.production_measurements(
        released_commit=report["subject"]["head_commit"]
    )
    actual = audit_deferred.measurements_rederivation_snapshot(measured)

    assert audit_deferred.rederivation_mismatches(expected, actual) == []
