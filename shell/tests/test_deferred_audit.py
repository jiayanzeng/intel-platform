from __future__ import annotations

import json
import shutil
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
from tools.invariant_scan import parse_ci_workflow


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "audit_deferred.py"
RUN = ROOT / "run"
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
    (repo / "AGENTS.md").write_text("**Active cycle:** v1.2.3\n")
    tracked = repo / "tracked.txt"
    tracked.write_text("base\n")
    _git(repo, "add", "AGENTS.md", "tracked.txt")
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
    matrix: str | None = None,
) -> None:
    receipt = {
        "run_id": run_id,
        "run_attempt": run_attempt,
        "job": job,
        "workflow": workflow,
        "repository": repository,
        "event_sha": sha,
        "sha": sha,
        "conclusion": conclusion,
        "runner_os": "Linux",
        "rustc_release": "1.91.0",
        "completed_at": "2026-07-26T00:00:00Z",
    }
    if matrix is not None:
        receipt["matrix"] = matrix
    path.write_text(
        json.dumps(receipt) + "\n"
    )


def _receipt_matrix(
    root: Path,
    sha: str,
    *,
    omit: str | None = None,
    split_job: str | None = None,
) -> list[Path]:
    identities = sorted(
        audit_deferred.expected_runner_job_identities(),
        key=lambda identity: (identity[0], identity[1] or ""),
    )
    paths: list[Path] = []
    omitted = False
    for index, (job, matrix) in enumerate(identities):
        if job == omit and not omitted:
            omitted = True
            continue
        path = root / f"{index}-{job}.json"
        _receipt(
            path,
            sha,
            job=job,
            run_id="other-run" if job == split_job else "123",
            matrix=matrix,
        )
        paths.append(path)
    return paths


def _workflow_variant(tmp_path: Path, suffix: str) -> Path:
    path = tmp_path / "ci.yml"
    source = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
    path.write_text(source.rstrip() + "\n" + suffix)
    return path


def test_added_blocking_job_is_derived_without_python_edit(
    tmp_path: Path,
) -> None:
    workflow = _workflow_variant(
        tmp_path,
        """\
  derived-extra:
    runs-on: ubuntu-latest
    steps:
      - name: extra blocking check
        run: ./run version-check
""",
    )

    identities = audit_deferred.expected_runner_job_identities(workflow)

    assert ("derived-extra", None) in identities


def test_job_level_continue_on_error_is_the_report_only_criterion(
    tmp_path: Path,
) -> None:
    workflow = _workflow_variant(
        tmp_path,
        """\
  derived-report:
    runs-on: ubuntu-latest
    continue-on-error: true
    steps:
      - name: informational check
        run: ./run version-check
""",
    )

    identities = audit_deferred.expected_runner_job_identities(workflow)

    assert ("derived-report", None) not in identities


def test_removed_workflow_job_reports_historical_identity_narrowing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    workflow = tmp_path / "ci.yml"
    source = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
    golden_start = source.index("  golden:\n")
    drift_start = source.index("  drift:\n")
    workflow.write_text(source[:golden_start] + source[drift_start:])
    monkeypatch.setattr(audit_deferred, "CI_WORKFLOW", workflow)

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["accepted_runner_receipts"] == []
    assert any(
        "identity set narrowed relative to protected historical evidence"
        in finding
        and "('golden', None)" in finding
        for finding in measurement["matrix_findings"]
    )


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
        {
            "path": str(receipt),
            "logical_path": "evidence/ci-runs/ancestor.json",
        }
    ]
    assert measurement["accepted_runner_receipts"] == []
    assert measurement["rejected_runner_receipts"][0]["reason"] == (
        f"sha does not equal released commit {head}"
    )
    assert measurement["workflow_configuration_counts_as_execution"] is False
    assert row["disposition"] == "defer"


def test_indexed_evidence_repository_records_real_relative_path(
    tmp_path: Path,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipt = (
        repo
        / "evidence"
        / "ci-runs"
        / "123-1"
        / "123-1-core.json"
    )
    receipt.parent.mkdir(parents=True)
    _receipt(receipt, head)
    _git(repo, "add", str(receipt.relative_to(repo)))

    measurement = audit_deferred.runner_receipt_measurement(
        [receipt],
        repository=repo,
        audited_head=head,
        released_commit=head,
        evidence_repository=repo,
    )

    assert measurement["runner_receipts"] == [
        {"path": "evidence/ci-runs/123-1/123-1-core.json"}
    ]
    assert "logical_path" not in measurement["runner_receipts"][0]


def test_indexed_evidence_repository_rejects_untracked_or_changed_path(
    tmp_path: Path,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipt = repo / "evidence" / "ci-runs" / "untracked.json"
    receipt.parent.mkdir(parents=True)
    _receipt(receipt, head)

    with pytest.raises(
        audit_deferred.AuditFailure,
        match="recorded evidence path is not indexed by Git",
    ):
        audit_deferred.runner_receipt_measurement(
            [receipt],
            repository=repo,
            audited_head=head,
            released_commit=head,
            evidence_repository=repo,
        )

    _git(repo, "add", str(receipt.relative_to(repo)))
    receipt.write_text(receipt.read_text() + "changed after staging\n")
    with pytest.raises(
        audit_deferred.AuditFailure,
        match="recorded evidence path differs from its Git index entry",
    ):
        audit_deferred.runner_receipt_measurement(
            [receipt],
            repository=repo,
            audited_head=head,
            released_commit=head,
            evidence_repository=repo,
        )


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
    ("rustc_release", "reason"),
    [
        (None, "missing/invalid fields: rustc_release"),
        ("1.91", "rustc_release is not a numeric Rust release"),
    ],
)
def test_current_receipt_requires_numeric_rustc_release(
    tmp_path: Path,
    rustc_release: str | None,
    reason: str,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipt = tmp_path / "rustc-release.json"
    _receipt(receipt, head)
    payload = json.loads(receipt.read_text())
    if rustc_release is None:
        payload.pop("rustc_release")
    else:
        payload["rustc_release"] = rustc_release
    receipt.write_text(json.dumps(payload) + "\n")

    measurement = audit_deferred.runner_receipt_measurement(
        [receipt],
        repository=repo,
        audited_head=head,
        released_commit=head,
    )

    assert measurement["accepted_runner_receipts"] == []
    assert measurement["rejected_runner_receipts"][0]["reason"] == reason


@pytest.mark.parametrize(
    ("omit", "split_job", "finding"),
    [
        ("golden", None, "identities"),
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

    assert measurement["observed_runner_executions"] == 9
    assert len(measurement["accepted_runner_receipts"]) == 9
    assert measurement["rejected_runner_receipts"] == []
    assert measurement["matrix_findings"] == []
    assert {
        (receipt["job"], receipt["matrix"])
        for receipt in measurement["accepted_runner_receipts"]
    } == audit_deferred.expected_runner_job_identities()
    assert all(
        {
            "matrix",
            "workflow",
            "repository",
            "event_sha",
        }.issubset(receipt)
        for receipt in measurement["accepted_runner_receipts"]
    )
    assert row["disposition"] == "promote"


def test_authenticated_duplicated_shell_leg_does_not_promote(
    tmp_path: Path,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    shell_311 = receipts[-2]
    shell_312 = receipts[-1]
    shutil.copyfile(shell_311, shell_312)
    for receipt in receipts:
        receipt.with_name(f"{receipt.name}.sigstore").write_text(
            "synthetic signed bundle\n"
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
        expected_source_digest=head,
        expected_source_ref="refs/heads/main",
        attestation_verifier=lambda *_: {
            "certificate_identity": "https://example.test/workflow",
            "signer_digest": head,
            "source_digest": head,
            "source_ref": "refs/heads/main",
        },
    )
    measurements = control_measurements()
    measurements["ci_runner"] = measurement
    row = next(
        row
        for row in evaluate(measurements)
        if row["id"] == "CI-runner evidence"
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["single_run_matrix_complete"] is False
    assert measurement["accepted_runner_receipts"] == []
    assert any(
        "duplicate runner receipt subject" in finding
        for finding in measurement["matrix_findings"]
    )
    assert any(
        "duplicate runner receipt content digest" in finding
        for finding in measurement["matrix_findings"]
    )
    assert row["disposition"] == "defer"


@pytest.mark.parametrize(
    ("job", "matrix", "reason"),
    [
        ("shell", None, "matrix job shell is missing required matrix"),
        (
            "shell",
            "python=3.13",
            "matrix job shell has unknown matrix value: python=3.13",
        ),
        (
            "core",
            "python=3.11",
            "single-leg job core must not carry matrix",
        ),
    ],
)
def test_matrix_shape_is_validated_with_distinct_reasons(
    tmp_path: Path,
    job: str,
    matrix: str | None,
    reason: str,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    target = next(
        receipt
        for receipt in receipts
        if json.loads(receipt.read_text())["job"] == job
    )
    _receipt(target, head, job=job, matrix=matrix)

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["single_run_matrix_complete"] is False
    assert measurement["accepted_runner_receipts"] == []
    assert any(
        rejected["reason"] == reason
        for rejected in measurement["rejected_runner_receipts"]
    )


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
        expected_source_digest=head,
        expected_source_ref="refs/heads/main",
        attestation_verifier=lambda *_: {
            "certificate_identity": "https://example.test/workflow",
            "signer_digest": head,
            "source_digest": head,
            "source_ref": "refs/heads/main",
        },
    )

    assert measurement["observed_runner_executions"] == 0
    assert measurement["accepted_runner_receipts"] == []
    assert len(measurement["rejected_runner_receipts"]) == 9
    assert all(
        "required attestation bundle is missing" in item["reason"]
        for item in measurement["rejected_runner_receipts"]
    )


def test_authenticated_complete_matrix_promotes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    for receipt in receipts:
        receipt.with_name(f"{receipt.name}.sigstore").write_text(
            "synthetic signed bundle\n"
        )
    verified: list[tuple[Path, Path, str, str, str, str]] = []

    def verifier(
        receipt: Path,
        bundle: Path,
        repository: str,
        workflow: str,
        source_digest: str,
        source_ref: str,
    ) -> dict[str, str]:
        verified.append(
            (
                receipt,
                bundle,
                repository,
                workflow,
                source_digest,
                source_ref,
            )
        )
        return {
            "certificate_identity": "https://example.test/workflow",
            "signer_digest": source_digest,
            "source_digest": source_digest,
            "source_ref": source_ref,
        }

    verifier_contract = {
        "command": "gh attestation verify",
        "required_cli_version": "2.96.0",
        "observed_cli_version": "2.96.0",
        "bundle_input_format": "canonical single-bundle JSON",
        "signer_workflow_format": (
            "[host/]owner/repository/.github/workflows/<file>"
        ),
    }
    monkeypatch.setattr(
        audit_deferred,
        "gh_attestation_cli",
        lambda: ("/usr/bin/gh", verifier_contract),
    )
    monkeypatch.setattr(
        audit_deferred,
        "verify_attestation_bundle",
        verifier,
    )

    measurement = audit_deferred.runner_receipt_measurement(
        receipts,
        repository=repo,
        audited_head=head,
        released_commit=head,
        attestation_bundles_dir=tmp_path,
        require_attestations=True,
        expected_repository="example/repo",
        expected_workflow=".github/workflows/ci.yml",
        expected_source_digest=head,
        expected_source_ref="refs/heads/main",
    )

    assert measurement["observed_runner_executions"] == 9
    assert len(measurement["accepted_runner_receipts"]) == 9
    assert all(
        receipt["attestation_verified"]
        for receipt in measurement["accepted_runner_receipts"]
    )
    assert len(verified) == 9
    assert {call[2] for call in verified} == {"example/repo"}
    assert {call[3] for call in verified} == {
        "example/repo/.github/workflows/ci.yml"
    }
    assert {call[4] for call in verified} == {head}
    assert {call[5] for call in verified} == {"refs/heads/main"}
    assert all(
        {
            "certificate_identity",
            "signer_digest",
            "source_digest",
            "source_ref",
        }.issubset(receipt)
        for receipt in measurement["accepted_runner_receipts"]
    )
    assert measurement["expected_workflow"] == (
        "example/repo/.github/workflows/ci.yml"
    )
    assert measurement["attestation_verifier"] == verifier_contract


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
        expected_source_digest=head,
        expected_source_ref="refs/heads/main",
        attestation_verifier=reject_bundle,
    )

    assert measurement["observed_runner_executions"] == 0
    assert len(measurement["rejected_runner_receipts"]) == 9
    assert all(
        item["reason"]
        == "GitHub attestation verification failed: invalid bundle"
        for item in measurement["rejected_runner_receipts"]
    )


def test_authenticated_matrix_rejects_mismatched_source_digest(
    tmp_path: Path,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    receipts = _receipt_matrix(tmp_path, head)
    for receipt in receipts:
        receipt.with_name(f"{receipt.name}.sigstore").write_text(
            "synthetic signed bundle\n"
        )

    def reject_source_digest(
        _: Path,
        __: Path,
        ___: str,
        ____: str,
        source_digest: str,
        source_ref: str,
    ) -> dict[str, str]:
        assert source_ref == "refs/heads/main"
        if source_digest != head:
            raise audit_deferred.AuditFailure(
                "GitHub attestation verification failed: "
                "source digest mismatch"
            )
        return {
            "certificate_identity": "https://example.test/workflow",
            "signer_digest": source_digest,
            "source_digest": source_digest,
            "source_ref": source_ref,
        }

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
        expected_source_digest="0" * 40,
        expected_source_ref="refs/heads/main",
        attestation_verifier=reject_source_digest,
    )

    assert measurement["observed_runner_executions"] == 0
    assert len(measurement["rejected_runner_receipts"]) == 9
    assert all(
        item["reason"].endswith("source digest mismatch")
        for item in measurement["rejected_runner_receipts"]
    )


def test_sigstore_bundle_is_reemitted_as_documented_single_json(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    receipt = tmp_path / "receipt.json"
    receipt.write_text('{"receipt": true}\n')
    bundle = tmp_path / "receipt.json.sigstore"
    bundle.write_text('{\n  "bundle": true\n}\n')
    verified_bundle: Path | None = None

    def verify(args: list[str], **_: object) -> subprocess.CompletedProcess:
        nonlocal verified_bundle
        verified_bundle = Path(args[args.index("--bundle") + 1])
        assert verified_bundle.name.endswith(".json")
        assert verified_bundle.read_text() == '{"bundle":true}\n'
        assert args[args.index("--signer-workflow") + 1] == (
            "example/repo/.github/workflows/ci.yml"
        )
        output = [
            {
                "verificationResult": {
                    "signature": {
                        "certificate": {
                            "subjectAlternativeName": (
                                "https://example.test/workflow"
                            ),
                            "sourceRepositoryDigest": "a" * 40,
                            "sourceRepositoryRef": "refs/heads/main",
                            "buildSignerDigest": "a" * 40,
                        }
                    }
                }
            }
        ]
        return subprocess.CompletedProcess(
            args,
            0,
            json.dumps(output),
            "",
        )

    monkeypatch.setattr(
        audit_deferred,
        "gh_attestation_cli",
        lambda: ("/usr/bin/gh", {}),
    )
    monkeypatch.setattr(audit_deferred.subprocess, "run", verify)

    audit_deferred.verify_attestation_bundle(
        receipt,
        bundle,
        "example/repo",
        ".github/workflows/ci.yml",
        "a" * 40,
        "refs/heads/main",
    )

    assert verified_bundle is not None
    assert not verified_bundle.exists()


def test_sigstore_verifier_pins_source_revision_and_returns_identity(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    receipt = tmp_path / "receipt.json"
    receipt.write_text('{"receipt": true}\n')
    bundle = tmp_path / "receipt.json.sigstore"
    bundle.write_text('{"bundle": true}\n')
    certificate_identity = (
        "https://github.com/example/repo/.github/workflows/"
        "ci.yml@refs/heads/main"
    )

    def verify(args: list[str], **_: object) -> subprocess.CompletedProcess:
        assert args[args.index("--source-digest") + 1] == "a" * 40
        assert args[args.index("--source-ref") + 1] == "refs/heads/main"
        assert args[args.index("--signer-digest") + 1] == "a" * 40
        assert args[args.index("--format") + 1] == "json"
        output = [
            {
                "verificationResult": {
                    "signature": {
                        "certificate": {
                            "subjectAlternativeName": certificate_identity,
                            "sourceRepositoryDigest": "a" * 40,
                            "sourceRepositoryRef": "refs/heads/main",
                            "buildSignerDigest": "a" * 40,
                        }
                    }
                }
            }
        ]
        return subprocess.CompletedProcess(
            args,
            0,
            json.dumps(output),
            "",
        )

    monkeypatch.setattr(
        audit_deferred,
        "gh_attestation_cli",
        lambda: ("/usr/bin/gh", {}),
    )
    monkeypatch.setattr(audit_deferred.subprocess, "run", verify)

    identity = audit_deferred.verify_attestation_bundle(
        receipt,
        bundle,
        "example/repo",
        "github.com/example/repo/.github/workflows/ci.yml",
        "a" * 40,
        "refs/heads/main",
    )

    assert identity == {
        "certificate_identity": certificate_identity,
        "signer_digest": "a" * 40,
        "source_digest": "a" * 40,
        "source_ref": "refs/heads/main",
    }


def test_gh_attestation_cli_records_the_exact_pin(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        audit_deferred.shutil,
        "which",
        lambda _: "/usr/bin/gh",
    )
    monkeypatch.setattr(
        audit_deferred.subprocess,
        "run",
        lambda args, **_: subprocess.CompletedProcess(
            args,
            0,
            "gh version 2.96.0 (2026-07-02)\n",
            "",
        ),
    )

    executable, contract = audit_deferred.gh_attestation_cli()

    assert executable == "/usr/bin/gh"
    assert contract["required_cli_version"] == "2.96.0"
    assert contract["observed_cli_version"] == "2.96.0"
    assert contract["bundle_input_format"] == "canonical single-bundle JSON"


def test_gh_attestation_cli_rejects_version_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        audit_deferred.shutil,
        "which",
        lambda _: "/usr/bin/gh",
    )
    monkeypatch.setattr(
        audit_deferred.subprocess,
        "run",
        lambda args, **_: subprocess.CompletedProcess(
            args,
            0,
            "gh version 2.95.0 (2026-06-01)\n",
            "",
        ),
    )

    with pytest.raises(
        audit_deferred.AuditFailure,
        match=(
            "GitHub CLI attestation verifier version mismatch: required "
            "2.96.0, observed 2.95.0"
        ),
    ):
        audit_deferred.gh_attestation_cli()


def test_production_rejects_wrong_head_before_measurement(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, ancestor, _, head = _synthetic_repository(tmp_path)
    output = tmp_path / "wrong-head.json"
    measured = False

    def fail_if_measured(*_: object, **__: object) -> dict[str, object]:
        nonlocal measured
        measured = True
        raise AssertionError("measurement ran before subject validation")

    monkeypatch.setattr(audit_deferred, "ROOT", repo)
    monkeypatch.setattr(
        audit_deferred,
        "production_measurements",
        fail_if_measured,
    )

    with pytest.raises(
        audit_deferred.AuditFailure,
        match=rf"subject HEAD mismatch: expected {ancestor}, actual {head}",
    ):
        audit_deferred.run_production(
            output,
            expected_head=ancestor,
            evidence_grade="structural",
        )

    assert measured is False
    assert not output.exists()


def test_production_rejects_dirty_tree_before_measurement(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    (repo / "tracked.txt").write_text("dirty\n")
    output = tmp_path / "dirty.json"
    measured = False

    def fail_if_measured(*_: object, **__: object) -> dict[str, object]:
        nonlocal measured
        measured = True
        raise AssertionError("measurement ran before subject validation")

    monkeypatch.setattr(audit_deferred, "ROOT", repo)
    monkeypatch.setattr(
        audit_deferred,
        "production_measurements",
        fail_if_measured,
    )

    with pytest.raises(
        audit_deferred.AuditFailure,
        match="subject worktree is dirty.*tracked.txt",
    ):
        audit_deferred.run_production(
            output,
            expected_head=head,
            evidence_grade="structural",
        )

    assert measured is False
    assert not output.exists()


def test_production_clean_matching_subject_writes_report(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, _, _, head = _synthetic_repository(tmp_path)
    output = tmp_path / "clean.json"
    measurements = control_measurements()
    measurements["multi_host"]["progress_files_scanned"] = []
    measured_with: dict[str, object] = {}

    def measure(*_: object, **kwargs: object) -> dict[str, object]:
        measured_with.update(kwargs)
        return measurements

    monkeypatch.setattr(audit_deferred, "ROOT", repo)
    monkeypatch.setattr(audit_deferred, "production_measurements", measure)
    monkeypatch.setattr(
        audit_deferred,
        "git_subject",
        lambda: {
            "head_commit": head,
            "worktree_dirty": False,
            "worktree_status": [],
        },
    )

    assert (
        audit_deferred.run_production(
            output,
            expected_head=head,
            evidence_grade="structural",
        )
        == 0
    )

    report = json.loads(output.read_text())
    assert report["task"] == "v1.2.3 RECEIPT"
    assert report["evidence_grade"] == "structural"
    assert report["attestations_required"] is False
    assert report["subject"]["head_commit"] == head
    assert report["subject"]["worktree_dirty"] is False
    assert measured_with["released_commit"] == head


def test_production_cli_requires_expected_head(tmp_path: Path) -> None:
    output = tmp_path / "unguarded.json"
    result = subprocess.run(
        [sys.executable, str(TOOL), "--output", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 2
    assert (
        "audit-deferred: FAIL: --expected-head is required "
        "for production audits"
    ) in result.stderr
    assert not output.exists()


def test_production_cli_requires_evidence_grade(tmp_path: Path) -> None:
    output = tmp_path / "ungraded.json"
    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--output",
            str(output),
            "--expected-head",
            "0" * 40,
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 2
    assert (
        "audit-deferred: FAIL: --evidence-grade is required "
        "for production audits"
    ) in result.stderr
    assert not output.exists()


def test_release_grade_requires_authentication_inputs(
    tmp_path: Path,
) -> None:
    output = tmp_path / "release.json"

    with pytest.raises(
        audit_deferred.AuditFailure,
        match="release evidence requires",
    ):
        audit_deferred.run_production(
            output,
            expected_head="0" * 40,
            evidence_grade="release",
        )

    assert not output.exists()


def test_rederivation_rejects_release_grade_without_attestations(
    tmp_path: Path,
) -> None:
    report = json.loads(COMMITTED_RECEIPT.read_text())
    report["evidence_grade"] = "release"
    report["attestations_required"] = False
    changed = tmp_path / "false-release-posture.json"
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
    assert "REDERIVATION MISMATCH attestations_required" in result.stderr


def test_rederivation_rejects_tampered_legacy_authentication_posture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    report = json.loads(
        (
            ROOT
            / "evidence"
            / "v0.10.2"
            / "deferred-audit"
            / "report.json"
        ).read_text()
    )
    report["measurements"]["ci_runner"]["attestations_required"] = False
    changed = tmp_path / "tampered-legacy-posture.json"
    changed.write_text(json.dumps(report) + "\n")
    monkeypatch.setattr(
        audit_deferred,
        "source_deterministic_measurements",
        lambda current, _: current["measurements"],
    )

    assert audit_deferred.run_rederivation(changed) == 1


def test_release_grade_rederivation_passes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    report = json.loads(COMMITTED_RECEIPT.read_text())
    report["evidence_grade"] = "release"
    report["attestations_required"] = True
    report["measurements"]["ci_runner"]["attestations_required"] = True
    for receipt in report["measurements"]["ci_runner"][
        "accepted_runner_receipts"
    ]:
        receipt["attestation_bundle"] = f"{receipt['path']}.sigstore"
        receipt["attestation_verified"] = True
    release_report = tmp_path / "release.json"
    release_report.write_text(json.dumps(report) + "\n")
    monkeypatch.setattr(
        audit_deferred,
        "source_deterministic_measurements",
        lambda current, _: current["measurements"],
    )

    assert audit_deferred.run_rederivation(release_report) == 0


def test_run_wrapper_defaults_to_released_commit() -> None:
    source = RUN.read_text()

    assert (
        'DEFERRED_AUDIT_RELEASE_COMMIT="'
        'e5af6bc5df8261cc004bd4d3247b70f8cbe930bb"'
    ) in source
    assert '--expected-head "$DEFERRED_AUDIT_RELEASE_COMMIT"' in source
    assert "--evidence-grade structural" in source


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
    workflow_path = ROOT / ".github" / "workflows" / "ci.yml"
    workflow = workflow_path.read_text()
    source = TOOL.read_text()
    workflow_job_count = len(parse_ci_workflow(workflow_path))

    assert workflow.count("- name: emit CI-runner receipt") == workflow_job_count
    assert (
        workflow.count("- name: persist CI-runner receipt")
        == workflow_job_count
    )
    assert (
        workflow.count("uses: actions/upload-artifact@v6")
        == workflow_job_count
    )
    assert (
        workflow.count("ref: ${{ inputs.audit_sha || github.sha }}")
        == workflow_job_count
    )
    assert workflow.count("if: always()") >= workflow_job_count * 2
    assert (
        workflow.count("uses: actions/attest-build-provenance@v4")
        == workflow_job_count
    )
    assert (
        workflow.count("steps.attest.outputs.bundle-path")
        == workflow_job_count
    )
    assert workflow.count('"matrix": "python=${{ matrix.python-version }}"') == 1
    assert workflow.count('"rustc_release": "$rustc_release"') == workflow_job_count
    assert "publish_evidence:" in workflow
    assert "id-token: write" in workflow
    assert "attestations: write" in workflow
    assert (
        workflow.count(
            "run: ./run cycle-check --skip-local-tag-verification"
        )
        == 1
    )
    assert workflow.count("- name: re-derive pinned deferred evidence") == 1
    assert "historical-artifact deferred-audit-baseline" in workflow
    assert '--rederive "$baseline"' in workflow
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


@pytest.mark.on_site
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
        released_commit=report["subject"]["head_commit"],
        legacy_job_counts=audit_deferred.LEGACY_RUNNER_JOB_COUNTS,
    )
    actual = audit_deferred.measurements_rederivation_snapshot(
        measured,
        report=report,
    )

    assert audit_deferred.rederivation_mismatches(expected, actual) == []
