import json
import subprocess
from fnmatch import fnmatchcase
from pathlib import Path

import pytest

from tools import cycle_check
from tools.cycle_identity import (
    cycle_documents_dir,
    cycle_progress_path,
    cycle_runbook_path,
    execution_runbooks,
    resolve_cycle,
)


def _runbook(root: Path, cycle: str = "v1.2.3") -> Path:
    return cycle_runbook_path(root, cycle)


def _progress(root: Path, cycle: str = "v1.2.3") -> Path:
    return cycle_progress_path(root, cycle)


def _state_with_regions(status: str) -> str:
    return (
        "# State\n\n"
        f"**As of:** {status}\n\n"
        "Fixture dated append.\n\n"
        f"{cycle_check.STATE_PERMANENT_TAIL_MARKER}\n"
        "## 1. Fixture permanent tail\n"
    )


def _cycle_root(tmp_path: Path, contract_tail: str = "") -> Path:
    fixture_export_bytes = len("cycle-check governed export fixture")
    fixture_export_tree = "a" * 40
    fixture_prior_export_bytes = fixture_export_bytes - 10
    fixture_margin_numerator = cycle_check.MAX_EXPORT_BYTES - fixture_export_bytes
    fixture_margin_cycles = fixture_margin_numerator / 10
    fixture_state_boundary = 2_048
    fixture_manifest_boundary = 2_048
    root = tmp_path / "cycle"
    root.mkdir()
    cycle_documents_dir(root).mkdir(parents=True)
    (cycle_documents_dir(root) / "PROGRESS-v1.2.1.md").write_text(
        "# Prior governed margin fixture\n\n"
        "- governed review-export measurement: "
        f"tree=`{'8' * 40}`; bytes=`{fixture_prior_export_bytes}`\n"
    )
    (cycle_documents_dir(root) / "PROGRESS-v1.2.2.md").write_text(
        "# Current governed margin fixture\n\n"
        "- governed review-export measurement: "
        f"tree=`{'9' * 40}`; bytes=`{fixture_export_bytes}`\n"
    )
    _runbook(root, "v1.2.2").write_text(
        "# Closed fixture cycle\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-29\n"
        "- **Release disposition:** no-release (as of 2026-07-29)\n\n"
        "Intentionally unreleased implementation commits:\n"
    )
    (root / "AGENTS.md").write_text(
        "# Contract\n\n"
        "**Active cycle:** v1.2.3\n\n"
        "Task work is ordered in "
        "`docs/cycles/TASKS-v1.2.3-EXECUTION.md` and logged in "
        "`docs/cycles/PROGRESS-v1.2.3.md`.\n\n"
        "## 0. Contract\n\n"
        f"{contract_tail}"
    )
    (root / "ARCHITECTURE.md").write_text(
        "# Architecture\n\n"
        "### Dated operational-residual dispositions\n\n"
        "| subject | disposition | trigger | dated measured observation |\n"
        "|---|---|---|---|\n"
        "| baseline | refuted | none | no measurement required |\n"
        "| trigger baseline | active | active condition | "
        "v1.2.3 · 2026-07-30 — measured |\n"
        "| protected evidence-manifest growth (fixture) | accepted | "
        "the manifest reaches its governed artifact byte boundary, or two "
        "consecutive clean ./run verify-artifacts runs each take ≥1.00 s real "
        "| v1.2.3 · 2026-07-30 — measured |\n"
        "| review-export size and retention bound (fixture) | accepted | "
        "export ceiling | v1.2.3 · 2026-07-30 — fixture export of "
        f"**{fixture_export_bytes} bytes / 1 file**. Governed review-export "
        f"bytes: `{fixture_export_bytes}`. Review-export margin: "
        "kind=`governed→governed`; "
        "prior_progress=`docs/cycles/PROGRESS-v1.2.1.md`; "
        f"prior_bytes=`{fixture_prior_export_bytes}`; "
        "current_progress=`docs/cycles/PROGRESS-v1.2.2.md`; "
        f"current_bytes=`{fixture_export_bytes}`; "
        "evaluated_progress=`docs/cycles/PROGRESS-v1.2.3.md`; "
        f"evaluated_bytes=`{fixture_export_bytes}`; "
        "denominator_bytes_per_cycle=`10`; "
        f"numerator_bytes=`{fixture_margin_numerator}`; "
        f"cycles=`{fixture_margin_cycles:.2f}`. |\n"
    )
    _runbook(root).write_text(
        "# Open cycle\n\n"
        "## Declared scope\n\n"
        "| Scope class | Path or value |\n"
        "|---|---|\n"
        "| `scope_version` | `1` |\n"
        "| `disposition_intent` | `release` |\n"
        "| `allow` | `**` |\n"
        "| `release_authority` | `Cargo.toml` |\n"
        "| `release_authority` | `Cargo.lock` |\n"
        "| `release_authority` | `README.md` |\n"
        "| `release_authority` | `CHANGELOG.md` |\n"
        "| `release_authority` | `shell/intel_shell/__init__.py` |\n"
        "| `release_authority` | `shell/intel_shell/app.py` |\n\n"
        "### Governed artifact byte-boundary authority\n\n"
        "- governed artifact byte boundary: path=`STATE.md`; bytes=`"
        f"{fixture_state_boundary}`\n"
        "- governed artifact byte boundary: "
        "path=`config/protected-artifacts.json`; bytes=`"
        f"{fixture_manifest_boundary}`\n\n"
        "## Deferred means deferred\n\n"
        "| Deferred item | Unchanged trigger | Measured 2026-07-29 | "
        "v1.2.3 action |\n"
        "|---|---|---|---|\n"
        "| Baseline item | none | no measurement required | none |\n"
        "| Trigger baseline | active condition | "
        "v1.2.3 · 2026-07-30 — measured | none |\n"
        "| Second `STATE.md` archival | the export ceiling trigger fires, or "
        "`STATE.md` reaches its governed artifact byte boundary | "
        "v1.2.3 · 2026-07-30 — measured | none |\n\n"
        "## Step 1 · CHECK\n\n"
        "**Objective.** Preserve the contract.\n\n"
        "**Acceptance criteria.** Original criterion.\n\n"
        "**Done when** the original criterion passes.\n\n"
        "- [ ] unfinished task\n"
    )
    _progress(root).write_text(
        "# Progress\n\n"
        "- governed review-export measurement: "
        f"tree=`{fixture_export_tree}`; bytes=`{fixture_export_bytes}`\n"
    )
    config = root / "config"
    config.mkdir()
    (root / "STATE.md").write_text(_state_with_regions("fixture state."))
    (config / "protected-artifacts.json").write_text("{}\n")
    (config / "cycle-history.json").write_text(
        json.dumps({"schema_version": 1, "artifacts": {}}) + "\n"
    )
    _commit_cycle_root(root)
    retained_cycles = cycle_check.expected_retained_cycle_paths(root)
    (root / "repomix.config.json").write_text(
        json.dumps(
            {
                "ignore": {
                    "customPatterns": [
                        cycle_check.expected_review_export_retention_pattern(
                            "v1.2.3",
                            retained_cycles,
                        )
                    ]
                }
            }
        )
        + "\n"
    )
    return root


def _commit_cycle_root(root: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "commit",
            "-qm",
            "initial runbook",
        ],
        cwd=root,
        check=True,
    )


def _commit_all(root: Path, message: str) -> str:
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "commit",
            "-qm",
            message,
        ],
        cwd=root,
        check=True,
    )
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


def _cross_fixture_artifact_boundaries(
    root: Path,
    *,
    disposed: bool,
) -> None:
    runbook = _runbook(root)
    runbook_text = cycle_check.GOVERNED_ARTIFACT_BOUNDARY_RE.sub(
        lambda match: (
            "- governed artifact byte boundary: "
            f"path=`{match.group(1)}`; bytes=`1`"
        ),
        runbook.read_text(),
    )
    if disposed:
        runbook_text = runbook_text.replace(
            "`STATE.md` reaches its governed artifact byte boundary | "
            "v1.2.3 · 2026-07-30 — measured | none |",
            "`STATE.md` reaches its governed artifact byte boundary | "
            "v1.2.3 · 2026-07-30 — trigger-fired disposition: archive "
            "decision recorded | none |",
        )
        architecture = root / "ARCHITECTURE.md"
        architecture.write_text(
            architecture.read_text().replace(
                "consecutive clean ./run verify-artifacts runs each take "
                "≥1.00 s real | v1.2.3 · 2026-07-30 — measured |",
                "consecutive clean ./run verify-artifacts runs each take "
                "≥1.00 s real | v1.2.3 · 2026-07-30 — trigger-fired "
                "disposition: retention decision recorded |",
            )
        )
    runbook.write_text(runbook_text)


def test_cycle_check_reports_below_artifact_byte_boundaries(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    expected_tree = subprocess.run(
        ["git", "rev-parse", "HEAD^{tree}"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()

    assert cycle_check.run(root) == 0
    output = capsys.readouterr().out
    state_bytes = len((root / "STATE.md").read_bytes())
    assert (
        f"artifact-boundary: path=STATE.md bytes={state_bytes} boundary=2048 "
        f"state=bound checked_tree=HEAD-tree:{expected_tree} "
        "timing=not-applicable"
    ) in output
    assert (
        "artifact-boundary: path=config/protected-artifacts.json bytes=3 "
        f"boundary=2048 state=bound checked_tree=HEAD-tree:{expected_tree} "
        "timing=out-of-scope"
    ) in output


def test_cycle_check_rejects_duplicate_artifact_boundary_authority(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    authority = (
        "- governed artifact byte boundary: path=`STATE.md`; bytes=`2048`"
    )
    runbook.write_text(
        runbook.read_text().replace(authority, authority + "\n" + authority)
    )
    _commit_cycle_root(root)

    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert "boundary for 'STATE.md' is declared more than once" in error


def test_cycle_check_rejects_missing_governed_artifact_row(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Second `STATE.md` archival | the export ceiling trigger fires, "
            "or `STATE.md` reaches its governed artifact byte boundary | "
            "v1.2.3 · 2026-07-30 — measured | none |\n",
            "",
        )
    )
    _commit_cycle_root(root)

    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert "expected exactly one governed trigger row" in error
    assert "Second STATE.md archival" in error


def test_cycle_check_rejects_crossed_artifact_boundaries_without_disposition(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _cross_fixture_artifact_boundaries(root, disposed=False)
    _commit_cycle_root(root)

    assert cycle_check.run(root) == 1
    captured = capsys.readouterr()
    state_bytes = len((root / "STATE.md").read_bytes())
    assert f"path=STATE.md bytes={state_bytes} boundary=1" in captured.out
    assert (
        "path=config/protected-artifacts.json bytes=3 boundary=1"
        in captured.out
    )
    assert captured.err.count("requires a dated 'trigger-fired disposition:'") == 2


def test_cycle_check_accepts_crossed_artifact_boundaries_with_disposition(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _cross_fixture_artifact_boundaries(root, disposed=True)
    _commit_cycle_root(root)

    assert cycle_check.run(root) == 0
    output = capsys.readouterr().out
    assert output.count("state=trigger-fired-disposed") == 2
    assert "artifact_boundaries=trigger-fired-disposed,trigger-fired-disposed" in output


def _publication_root(tmp_path: Path) -> tuple[Path, str, str]:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "tag",
            "-a",
            "v1.1.0",
            "-m",
            "release",
        ],
        cwd=root,
        check=True,
    )
    tag_object = subprocess.run(
        ["git", "rev-parse", "v1.1.0"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    subprocess.run(
        ["git", "update-ref", "refs/remotes/origin/main", commit],
        cwd=root,
        check=True,
    )
    _runbook(root, "v1.1.0").write_text(
        "# Closed cycle\n\n"
        "- [x] completed task\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-28\n"
        "- **Release disposition:** release (as of 2026-07-28)\n"
        "- **Release:** `v1.1.0`\n"
        f"- **Release commit:** `{commit}`\n"
        f"- **Annotated tag object:** `{tag_object}`\n"
    )
    return root, commit, tag_object


def _tagged_closing_root(
    tmp_path: Path,
) -> tuple[Path, str, str, str]:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    release_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "- [ ] unfinished task",
            "- [x] finished task",
        )
        + "\n## Runbook amendments\n\n"
        "Step 1 — Record the closing checklist — 2026-07-29\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-29\n"
        "- **Release disposition:** release (as of 2026-07-29)\n"
        "- **Release:** `v1.2.3`\n"
        f"- **Release commit:** `{release_commit}`\n"
    )
    (root / "STATE.md").write_text(
        _state_with_regions(
            "v1.2.3 is published. "
            f"Release commit is `{release_commit}`."
        )
    )
    closing_commit = _commit_all(root, "close cycle")
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "tag",
            "-a",
            "v1.2.3",
            "-m",
            "release",
        ],
        cwd=root,
        check=True,
    )
    tag_object = subprocess.run(
        ["git", "rev-parse", "v1.2.3"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    return root, release_commit, closing_commit, tag_object


def _publication_errors(root: Path) -> list[str]:
    errors: list[str] = []
    cycle_check.check_publication_status(
        root, execution_runbooks(root), errors
    )
    return errors


def test_publication_status_admission_rejects_missing_state_file(
    tmp_path: Path,
) -> None:
    root, _, _ = _publication_root(tmp_path)
    (root / "STATE.md").unlink()

    assert _publication_errors(root) == [
        "STATE.md: publication admission file required: STATE.md is absent "
        "or is not a regular file"
    ]


def test_publication_status_selects_release_before_later_no_release(
    tmp_path: Path,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    later = root / "docs" / "cycles" / "TASKS-v1.2.0-EXECUTION.md"
    later.write_text(
        "# Later no-release cycle\n\n"
        "- [x] completed task\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-29\n"
        "- **Release disposition:** no-release (as of 2026-07-29)\n"
    )
    (root / "STATE.md").write_text(
        "# State\n\n"
        "**As of:** published. Annotated tag object is "
        f"`{tag_object}`; tag target is `{commit}`.\n"
    )

    assert _publication_errors(root) == []
    (root / "STATE.md").write_text("# State\n\nNo status header.\n")
    assert _publication_errors(root) == [
        "STATE.md: publication admission header required: STATE.md has no "
        "'**As of:**' status header"
    ]


def test_publication_status_admission_rejects_absent_as_of_header(
    tmp_path: Path,
) -> None:
    root, _, _ = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\nStatus paragraph without an as-of header.\n"
    )

    assert _publication_errors(root) == [
        "STATE.md: publication admission header required: STATE.md has no "
        "'**As of:**' status header"
    ]


def test_publication_status_admission_rejects_unmatched_as_of_header(
    tmp_path: Path,
) -> None:
    root, _, _ = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n**Recorded as of:** published.\n"
    )

    assert _publication_errors(root) == [
        "STATE.md: publication admission header shape: the leading as-of "
        "status header is present but does not match STATE_HEADER_RE's "
        "required '**As of:**' form"
    ]


def test_publication_status_rejects_pending_reachable_release(
    tmp_path: Path,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        "**As of:** publication is pending. "
        f"Annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n\n"
        "Historical body may say publication was pending.\n"
    )

    errors = _publication_errors(root)
    assert len(errors) == 1
    assert "publication disposition agreement" in errors[0]


def test_release_object_mismatch_intentionally_masks_pending_publication(
    tmp_path: Path,
    monkeypatch,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        "**As of:** publication is pending. "
        f"Annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n"
    )
    real_git_output = cycle_check.git_output
    wrong_object = "f" * 40

    def mismatched_object(repo: Path, *args: str) -> str | None:
        if args == ("rev-parse", "v1.1.0"):
            return wrong_object
        return real_git_output(repo, *args)

    monkeypatch.setattr(cycle_check, "git_output", mismatched_object)

    assert _publication_errors(root) == [
        "STATE.md: publication release-object agreement: v1.1.0 resolves to "
        f"tag object {wrong_object}, but docs/cycles/"
        f"TASKS-v1.1.0-EXECUTION.md records {tag_object}"
    ]


def test_publication_status_rejects_mutable_ref_literal_in_header(
    tmp_path: Path,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. `origin/main` and remote `main` are `{commit}`; "
        f"annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n"
    )

    errors = _publication_errors(root)
    assert errors == [
        "STATE.md: publication status header must not assert a literal "
        "origin/main hash; publishing the asserting commit moves that ref, "
        "so record mutable-ref measurements in a dated body append"
    ]

    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. origin/main is {commit}; "
        f"annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n"
    )
    assert _publication_errors(root) == errors


def test_publication_status_rejects_every_stale_immutable_header_ref(
    tmp_path: Path,
) -> None:
    root, _, _ = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Annotated tag object is `{'1' * 40}`; "
        f"tag target is `{'2' * 40}`.\n\n"
        "Historical body.\n"
    )

    errors = _publication_errors(root)
    assert len(errors) == 2
    assert all("publication assertion freshness" in error for error in errors)
    assert any("annotated tag object" in error for error in errors)
    assert any("tag target" in error for error in errors)


def test_publication_status_requires_every_immutable_header_ref(
    tmp_path: Path,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Remote annotated `v1.1.0` tag object "
        f"`{tag_object}`; release commit `{commit}`.\n"
    )

    errors = _publication_errors(root)
    assert errors == [
        "STATE.md: publication assertion required: status header must assert "
        "the annotated tag object in the required unambiguous phrasing"
    ]

    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Annotated tag object is `{tag_object}`.\n"
    )
    assert _publication_errors(root) == [
        "STATE.md: publication assertion required: status header must assert "
        "the tag target in the required unambiguous phrasing"
    ]


def test_publication_status_accepts_current_header_and_ignores_body(
    tmp_path: Path,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n\n"
        "Historical body: publication is pending; "
        f"`origin/main` was `{'0' * 40}`.\n"
    )

    assert _publication_errors(root) == []


def test_publication_status_reports_missing_tag_ref(tmp_path: Path) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n"
    )
    subprocess.run(["git", "tag", "-d", "v1.1.0"], cwd=root, check=True)

    errors = _publication_errors(root)
    assert len(errors) == 1
    assert "publication verification unavailable" in errors[0]
    assert "annotated tag ref 'v1.1.0' cannot be resolved" in errors[0]


def test_publication_status_reports_missing_tag_target(
    tmp_path: Path,
    monkeypatch,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n"
    )
    real_git_output = cycle_check.git_output

    def missing_target(repo: Path, *args: str) -> str | None:
        if args == ("rev-parse", "v1.1.0^{}"):
            return None
        return real_git_output(repo, *args)

    monkeypatch.setattr(cycle_check, "git_output", missing_target)

    errors = _publication_errors(root)
    assert len(errors) == 1
    assert "publication verification unavailable" in errors[0]
    assert "annotated tag target 'v1.1.0' cannot be resolved" in errors[0]


def test_publication_status_reports_unavailable_ancestry(
    tmp_path: Path,
    monkeypatch,
) -> None:
    root, commit, tag_object = _publication_root(tmp_path)
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Annotated tag object is `{tag_object}`; "
        f"tag target is `{commit}`.\n"
    )
    monkeypatch.setattr(
        cycle_check,
        "git_status",
        lambda _root, *_args: (128, "fatal: shallow history"),
    )

    errors = _publication_errors(root)
    assert len(errors) == 1
    assert "publication ancestry verification unavailable" in errors[0]
    assert "fatal: shallow history" in errors[0]


def test_cycle_check_accepts_tagged_closing_commit_protocol(
    tmp_path: Path,
) -> None:
    root, _, _, _ = _tagged_closing_root(tmp_path)

    assert cycle_check.run(root) == 0


def test_governed_export_binding_covers_release_close_and_post_push(
    tmp_path: Path,
    capsys,
) -> None:
    root, release_commit, closing_commit, tag_object = _tagged_closing_root(
        tmp_path
    )

    subprocess.run(
        ["git", "checkout", "-q", release_commit],
        cwd=root,
        check=True,
    )
    assert cycle_check.run(root) == 0
    assert "governed_export=exempt-open-latest-at-close" in capsys.readouterr().out

    subprocess.run(
        ["git", "checkout", "-q", closing_commit],
        cwd=root,
        check=True,
    )
    assert cycle_check.run(root, verify_local_tag_refs=False) == 0
    assert "governed_export=bound" in capsys.readouterr().out

    subprocess.run(
        ["git", "checkout", "-q", "v1.2.3^{}"],
        cwd=root,
        check=True,
    )
    assert cycle_check.run(root) == 0
    assert "governed_export=bound" in capsys.readouterr().out

    fixture_export_bytes = len("cycle-check governed export fixture")
    cycle_ending_bytes = fixture_export_bytes + len("cycle ending delta")
    progress = _progress(root)
    progress.write_text(
        progress.read_text()
        + _cycle_ending_export_audit(
            closing_commit,
            cycle_ending_bytes,
            cycle_ending_bytes - fixture_export_bytes,
        )
    )
    state = root / "STATE.md"
    hosted_run = str(len("post-push hosted run fixture"))
    state.write_text(
        state.read_text()
        + "\n- **Post-push verification date:** 2026-07-29\n"
        "- **Post-push release:** `v1.2.3`\n"
        f"- **Post-push annotated tag object:** `{tag_object}`\n"
        f"- **Post-push closing commit:** `{closing_commit}`\n"
        f"- **Post-push hosted run:** `{hosted_run}`\n"
    )
    _commit_all(root, "post-push audit")

    assert cycle_check.run(root) == 0
    assert (
        "governed_export=bound-with-cycle-ending-audit"
        in capsys.readouterr().out
    )


def test_cycle_check_rejects_prechange_active_tag_object_field(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    release_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "- [ ] unfinished task",
            "- [x] finished task",
        )
        + "\n## Runbook amendments\n\n"
        "Step 1 — Record the closing checklist — 2026-07-29\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-29\n"
        "- **Release disposition:** release (as of 2026-07-29)\n"
        "- **Release:** `v1.2.3`\n"
        f"- **Release commit:** `{release_commit}`\n"
        f"- **Annotated tag object:** `{'0' * 40}`\n"
    )

    assert cycle_check.run(root, verify_local_tag_refs=False) == 1
    assert (
        "TASKS-v1.2.3-EXECUTION.md: declared closed cycle must use the "
        "tagged-closing protocol and omit the Annotated tag object field; "
        "record that object in the dated post-push append"
        in capsys.readouterr().err
    )


def test_tagged_closing_protocol_requires_annotated_tag(
    tmp_path: Path,
    capsys,
) -> None:
    root, _, closing_commit, _ = _tagged_closing_root(tmp_path)
    subprocess.run(["git", "tag", "-d", "v1.2.3"], cwd=root, check=True)
    subprocess.run(
        ["git", "tag", "v1.2.3", closing_commit],
        cwd=root,
        check=True,
    )

    assert cycle_check.run(root) == 1
    assert (
        "must resolve to an annotated tag object"
        in capsys.readouterr().err
    )


def test_tagged_closing_protocol_requires_release_parent(
    tmp_path: Path,
    capsys,
) -> None:
    root, release_commit, _, _ = _tagged_closing_root(tmp_path)
    (root / "after-close.txt").write_text("intervening commit\n")
    later_commit = _commit_all(root, "intervening commit")
    subprocess.run(["git", "tag", "-d", "v1.2.3"], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "tag",
            "-a",
            "v1.2.3",
            later_commit,
            "-m",
            "moved release",
        ],
        cwd=root,
        check=True,
    )

    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert "tagged-closing parent agreement" in error
    assert f"not recorded release commit {release_commit}" in error


def test_tagged_closing_protocol_requires_closed_tag_tree(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    release_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    (root / "pre-close.txt").write_text("tagged before close\n")
    open_target = _commit_all(root, "open tag target")
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "tag",
            "-a",
            "v1.2.3",
            open_target,
            "-m",
            "premature release",
        ],
        cwd=root,
        check=True,
    )
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "- [ ] unfinished task",
            "- [x] finished task",
        )
        + "\n## Runbook amendments\n\n"
        "Step 1 — Record the closing checklist — 2026-07-29\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-29\n"
        "- **Release disposition:** release (as of 2026-07-29)\n"
        "- **Release:** `v1.2.3`\n"
        f"- **Release commit:** `{release_commit}`\n"
    )
    (root / "STATE.md").write_text(
        "# State\n\n"
        "**As of:** v1.2.3 is published. "
        f"Release commit is `{release_commit}`.\n"
    )
    _commit_all(root, "actual close")

    assert cycle_check.run(root) == 1
    assert "tagged-closing tree agreement" in capsys.readouterr().err


def test_tagged_closing_header_requires_fresh_release_commit(
    tmp_path: Path,
) -> None:
    root, release_commit, _, _ = _tagged_closing_root(tmp_path)
    (root / "STATE.md").write_text("# State\n\n**As of:** published.\n")

    assert _publication_errors(root) == [
        "STATE.md: publication assertion required: status header must assert "
        "the release commit in the required unambiguous phrasing"
    ]

    stale_commit = "f" * 40
    (root / "STATE.md").write_text(
        "# State\n\n"
        f"**As of:** published. Release commit is `{stale_commit}`.\n"
    )
    assert _publication_errors(root) == [
        "STATE.md: publication assertion freshness: release commit asserts "
        f"{stale_commit}, but the measured ref is {release_commit}"
    ]


def test_tagged_closing_descendant_requires_post_push_record(
    tmp_path: Path,
) -> None:
    root, _, closing_commit, tag_object = _tagged_closing_root(tmp_path)
    (root / "post-push.txt").write_text("after tagged close\n")
    _commit_all(root, "post-push descendant")

    assert _publication_errors(root) == [
        "STATE.md: publication post-push record required: expected exactly "
        "one complete record for v1.2.3; found 0"
    ]

    state = root / "STATE.md"
    state.write_text(
        state.read_text()
        + "\n- **Post-push verification date:** 2026-02-30\n"
        "- **Post-push release:** `v1.2.3`\n"
        f"- **Post-push annotated tag object:** `{tag_object}`\n"
        f"- **Post-push closing commit:** `{closing_commit}`\n"
        "- **Post-push hosted run:** `123456`\n"
    )
    assert _publication_errors(root) == [
        "STATE.md: invalid post-push verification date '2026-02-30'"
    ]

    state.write_text(
        state.read_text().replace("2026-02-30", "2026-07-29")
    )
    assert _publication_errors(root) == []


def test_tagged_closing_post_push_record_must_be_fresh(
    tmp_path: Path,
) -> None:
    root, _, closing_commit, _ = _tagged_closing_root(tmp_path)
    (root / "post-push.txt").write_text("after tagged close\n")
    _commit_all(root, "post-push descendant")
    stale_object = "e" * 40
    stale_target = "f" * 40
    state = root / "STATE.md"
    state.write_text(
        state.read_text()
        + "\n- **Post-push verification date:** 2026-07-29\n"
        "- **Post-push release:** `v1.2.3`\n"
        f"- **Post-push annotated tag object:** `{stale_object}`\n"
        f"- **Post-push closing commit:** `{stale_target}`\n"
        "- **Post-push hosted run:** `123456`\n"
    )

    errors = _publication_errors(root)
    assert len(errors) == 2
    assert any(
        "publication post-push freshness: annotated tag object" in error
        for error in errors
    )
    assert any(
        "publication post-push freshness: closing commit" in error
        for error in errors
    )
    assert closing_commit not in {stale_object, stale_target}


def test_cycle_check_accepts_cycle_paths_only_in_declaration(
    tmp_path: Path,
) -> None:
    assert cycle_check.run(_cycle_root(tmp_path)) == 0


def _governed_export_text(byte_count: int) -> str:
    return (
        "# Architecture\n\n"
        "### Dated operational-residual dispositions\n\n"
        "| subject | disposition | trigger | measured observation |\n"
        "|---|---|---|---|\n"
        "| review-export size and retention bound (fixture) | accepted | "
        "export ceiling | fixture export of "
        f"**{byte_count} bytes / 1 file**. Governed review-export bytes: "
        f"`{byte_count}`. |\n"
    )


def _governed_export_progress(
    measurements: list[tuple[str, int]],
) -> str:
    fields = "".join(
        "- governed review-export measurement: "
        f"tree=`{tree}`; bytes=`{byte_count}`\n"
        for tree, byte_count in measurements
    )
    return f"# Progress\n\n{fields}"


def _cycle_ending_export_audit(
    closing_tree: str,
    byte_count: int,
    audit_delta: int,
) -> str:
    return (
        "- cycle-ending review-export audit: "
        f"closing_tree=`{closing_tree}`; bytes=`{byte_count}`; "
        f"audit_delta=`{audit_delta:+d}`\n"
    )


def test_governed_export_margin_rejects_superseded_figure(
    tmp_path: Path,
) -> None:
    row_value = len("earlier governed export")
    latest_value = row_value + len("later")
    architecture = tmp_path / "ARCHITECTURE.md"
    progress = tmp_path / "PROGRESS.md"
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        architecture,
        _governed_export_text(row_value),
        progress,
        _governed_export_progress(
            [("a" * 40, row_value), ("b" * 40, latest_value)]
        ),
        "closed",
        tmp_path,
        errors,
    )

    assert status == "superseded"
    assert errors == [
        "ARCHITECTURE.md: governed review-export row is superseded: "
        f"row={row_value}, latest_progress={latest_value}, tree={'b' * 40}"
    ]


def test_governed_export_margin_names_open_empty_progress_exemption(
    tmp_path: Path,
) -> None:
    row_value = len("open governed export")
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(row_value),
        tmp_path / "PROGRESS.md",
        "# Progress\n",
        "open",
        tmp_path,
        errors,
    )

    assert status == "exempt-open-empty-progress"
    assert errors == []


def test_governed_export_margin_names_open_latest_exemption(
    tmp_path: Path,
) -> None:
    row_value = len("open governed export with measurement")
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(row_value),
        tmp_path / "PROGRESS.md",
        _governed_export_progress([("a" * 40, row_value)]),
        "open",
        tmp_path,
        errors,
    )

    assert status == "exempt-open-latest-at-close"
    assert errors == []


def test_governed_export_margin_rejects_closed_empty_progress(
    tmp_path: Path,
) -> None:
    row_value = len("closed governed export")
    progress = tmp_path / "PROGRESS.md"
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(row_value),
        progress,
        "# Progress\n",
        "closed",
        tmp_path,
        errors,
    )

    assert status == "missing-closed-progress-measurement"
    assert errors == [
        "PROGRESS.md: closed cycle has no governed review-export measurement; "
        "the open-cycle empty-progress exemption is unavailable"
    ]


def test_governed_export_margin_accepts_last_progress_figure(
    tmp_path: Path,
) -> None:
    prior_value = len("prior governed export")
    latest_value = prior_value + len("newer")
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(latest_value),
        tmp_path / "PROGRESS.md",
        _governed_export_progress(
            [("a" * 40, prior_value), ("b" * 40, latest_value)]
        ),
        "closed",
        tmp_path,
        errors,
    )

    assert status == "bound"
    assert errors == []


def test_governed_export_margin_names_cycle_ending_audit_path(
    tmp_path: Path,
) -> None:
    row_value = len("governed before cycle-ending audit")
    closing_value = row_value + len("closing tree delta")
    progress_text = _governed_export_progress(
        [("a" * 40, row_value)]
    ) + _cycle_ending_export_audit(
        "b" * 40,
        closing_value,
        closing_value - row_value,
    )
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(row_value),
        tmp_path / "PROGRESS.md",
        progress_text,
        "closed",
        tmp_path,
        errors,
    )

    assert status == "bound-with-cycle-ending-audit"
    assert errors == []


def test_governed_export_margin_rejects_misordered_cycle_ending_audit(
    tmp_path: Path,
) -> None:
    row_value = len("governed after premature audit")
    audit = _cycle_ending_export_audit(
        "a" * 40,
        row_value,
        row_value - row_value,
    )
    governed = _governed_export_progress([("b" * 40, row_value)])
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(row_value),
        tmp_path / "PROGRESS.md",
        audit + governed,
        "closed",
        tmp_path,
        errors,
    )

    assert status == "misordered-cycle-ending-audit"
    assert errors == [
        "PROGRESS.md: cycle-ending review-export audit must follow the last "
        "governed review-export measurement at the checked tree"
    ]


def test_governed_export_margin_rejects_written_figure_over_ceiling(
    tmp_path: Path,
) -> None:
    row_value = cycle_check.MAX_EXPORT_BYTES + len("over ceiling")
    errors: list[str] = []

    status = cycle_check.check_governed_export_margin(
        tmp_path / "ARCHITECTURE.md",
        _governed_export_text(row_value),
        tmp_path / "PROGRESS.md",
        _governed_export_progress([("a" * 40, row_value)]),
        "closed",
        tmp_path,
        errors,
    )

    assert status == "recorded-figure-over-ceiling"
    assert errors == [
        "ARCHITECTURE.md: recorded governed review-export figure "
        f"{row_value} exceeds the {cycle_check.MAX_EXPORT_BYTES}-byte ceiling; "
        "this constrains the written figure at the checked tree and does not "
        "measure an export"
    ]


def test_governed_export_margin_kind_accepts_recorded_governed_series(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    errors: list[str] = []

    report = cycle_check.check_governed_export_margin_kind(
        root / "ARCHITECTURE.md",
        (root / "ARCHITECTURE.md").read_text(),
        root,
        errors,
    )

    assert errors == []
    assert report == (
        "governed-export-margin-basis: "
        "selected=latest-positive-adjacent-governed-pair "
        "representativeness=unbounded(single adjacent pair carries no "
        "representativeness guarantee) "
        "structural_epoch=unobserved(checker cannot detect a basis "
        "predating a structural change)"
    )


def test_governed_export_margin_kind_rejects_mixed_recorded_series(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    current = cycle_documents_dir(root) / "PROGRESS-v1.2.2.md"
    current.write_text(current.read_text().replace("bytes=`35`", "bytes=`36`"))
    errors: list[str] = []

    cycle_check.check_governed_export_margin_kind(
        root / "ARCHITECTURE.md",
        (root / "ARCHITECTURE.md").read_text(),
        root,
        errors,
    )

    assert errors == [
        "ARCHITECTURE.md: governed export margin mixes or misstates "
        "measurement series: declared=25→35@35, recorded=25→36@35"
    ]


def test_governed_export_margin_kind_accepts_post_archive_evaluation(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    evaluated = _progress(root)
    evaluated_value = len("cycle-check governed export fixture") - 5
    evaluated.write_text(
        evaluated.read_text().replace(
            "bytes=`35`",
            f"bytes=`{evaluated_value}`",
        )
    )
    architecture = root / "ARCHITECTURE.md"
    text = architecture.read_text()
    numerator = cycle_check.MAX_EXPORT_BYTES - evaluated_value
    cycles = numerator / 10
    text = text.replace(
        "export of **35 bytes",
        f"export of **{evaluated_value} bytes",
    )
    text = text.replace(
        "Governed review-export bytes: `35`",
        f"Governed review-export bytes: `{evaluated_value}`",
    )
    text = text.replace(
        "evaluated_bytes=`35`",
        f"evaluated_bytes=`{evaluated_value}`",
    )
    text = text.replace(
        f"numerator_bytes=`{cycle_check.MAX_EXPORT_BYTES - 35}`",
        f"numerator_bytes=`{numerator}`",
    )
    text = text.replace(
        f"cycles=`{(cycle_check.MAX_EXPORT_BYTES - 35) / 10:.2f}`",
        f"cycles=`{cycles:.2f}`",
    )
    architecture.write_text(text)
    errors: list[str] = []

    cycle_check.check_governed_export_margin_kind(
        architecture,
        architecture.read_text(),
        root,
        errors,
    )

    assert errors == []


def test_governed_export_margin_kind_rejects_stale_positive_basis(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    stale = cycle_documents_dir(root) / "PROGRESS-v1.2.0.md"
    stale.write_text(
        "# Stale governed margin fixture\n\n"
        "- governed review-export measurement: "
        f"tree=`{'7' * 40}`; bytes=`20`\n"
    )
    architecture = root / "ARCHITECTURE.md"
    text = architecture.read_text()
    numerator = cycle_check.MAX_EXPORT_BYTES - 35
    text = text.replace(
        "prior_progress=`docs/cycles/PROGRESS-v1.2.1.md`; prior_bytes=`25`",
        "prior_progress=`docs/cycles/PROGRESS-v1.2.0.md`; prior_bytes=`20`",
    )
    text = text.replace(
        "current_progress=`docs/cycles/PROGRESS-v1.2.2.md`; current_bytes=`35`",
        "current_progress=`docs/cycles/PROGRESS-v1.2.1.md`; current_bytes=`25`",
    )
    text = text.replace(
        "denominator_bytes_per_cycle=`10`",
        "denominator_bytes_per_cycle=`5`",
    )
    text = text.replace(
        f"cycles=`{numerator / 10:.2f}`",
        f"cycles=`{numerator / 5:.2f}`",
    )
    architecture.write_text(text)
    errors: list[str] = []

    cycle_check.check_governed_export_margin_kind(
        architecture,
        architecture.read_text(),
        root,
        errors,
    )

    assert errors == [
        "ARCHITECTURE.md: governed export margin must use the latest positive "
        "adjacent-cycle governed pair; "
        "declared=docs/cycles/PROGRESS-v1.2.0.md→"
        "docs/cycles/PROGRESS-v1.2.1.md, "
        "latest=docs/cycles/PROGRESS-v1.2.1.md→"
        "docs/cycles/PROGRESS-v1.2.2.md"
    ]


def test_state_region_contract_derives_external_reference_inventory(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    (root / "README.md").write_text("Current design lives in STATE §1.\n")
    subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
    errors: list[str] = []

    report = cycle_check.check_state_archival_region_contract(
        root / "STATE.md",
        (root / "STATE.md").read_text(),
        root,
        errors,
    )

    assert errors == []
    assert report is not None
    assert "structural=bound" in report
    assert "semantic_owner=version-check" in report
    assert "top_sections=1" in report
    assert "numbering_gaps=none" in report
    assert "referenced_sections=1" in report
    assert "README.md:1=§1" in report


def test_state_region_contract_rejects_unresolved_external_reference(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    (root / "README.md").write_text("Missing design lives in STATE.md §2.\n")
    subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
    errors: list[str] = []

    report = cycle_check.check_state_archival_region_contract(
        root / "STATE.md",
        (root / "STATE.md").read_text(),
        root,
        errors,
    )

    assert report is None
    assert errors == [
        "STATE.md: external State section references do not resolve: "
        "README.md:1=§2"
    ]


def test_state_region_contract_rejects_missing_permanent_tail_marker(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    state = root / "STATE.md"
    state_text = state.read_text().replace(
        f"{cycle_check.STATE_PERMANENT_TAIL_MARKER}\n",
        "",
    )
    errors: list[str] = []

    report = cycle_check.check_state_archival_region_contract(
        state,
        state_text,
        root,
        errors,
    )

    assert report is None
    assert errors == [
        "STATE.md: State archival structural permanent-tail marker required "
        "exactly once; found 0; semantic current-restatement state=present "
        "remains delegated to version-check"
    ]


def test_state_region_contract_rejects_full_tail_without_semantic_floor(
    tmp_path: Path,
    monkeypatch,
) -> None:
    root = _cycle_root(tmp_path)
    state = root / "STATE.md"
    state_text = state.read_text()
    tail_start = state_text.index(cycle_check.STATE_PERMANENT_TAIL_MARKER)
    monkeypatch.setattr(
        cycle_check,
        "state_has_registered_current_restatement",
        lambda _root, _text: False,
    )
    errors: list[str] = []

    report = cycle_check.check_state_archival_region_contract(
        state,
        state_text[:tail_start],
        root,
        errors,
    )

    assert report is None
    assert errors == [
        "STATE.md: State archival structural permanent-tail marker required "
        "exactly once; found 0; semantic current-restatement state=absent "
        "remains delegated to version-check"
    ]


def test_state_region_contract_names_missing_structural_header(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    state = root / "STATE.md"
    errors: list[str] = []

    report = cycle_check.check_state_archival_region_contract(
        state,
        "# State\n\nDated append with no status header.\n",
        root,
        errors,
    )

    assert report is None
    assert errors == [
        "STATE.md: State archival structural admission requires the status "
        "header; semantic current-restatement membership remains delegated "
        "to version-check and was not evaluated"
    ]


def test_cycle_check_rejects_stale_review_export_retention_without_export(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    assert not list(root.glob("repomix-output-*.xml"))
    config_path = root / "repomix.config.json"
    config = json.loads(config_path.read_text())
    patterns = config["ignore"]["customPatterns"]
    patterns[0] = f"{patterns[0]}.stale"
    config_path.write_text(json.dumps(config) + "\n")

    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert "review-export retention pattern for v1.2.3 must be" in error
    assert ".stale" in error


def test_cycle_check_rejects_skipped_cycle_retention_without_export(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    identity = resolve_cycle(root)
    current_version = cycle_check.declared_scope_cycle_version(identity.name)
    for offset in range(cycle_check.CYCLE_RETENTION_DEPTH - 1, 0, -1):
        prior_name = "v" + ".".join(
            str(part)
            for part in (
                *current_version[:-1],
                current_version[-1] - offset,
            )
        )
        cycle_runbook_path(root, prior_name).write_text(
            "# Closed fixture cycle\n\n"
            "## Cycle closing record\n\n"
            "- **Cycle closed:** 2026-07-29\n"
            "- **Release disposition:** no-release (as of 2026-07-29)\n\n"
            "Intentionally unreleased implementation commits:\n"
        )
        cycle_progress_path(root, prior_name).write_text("# Progress\n")
    _commit_cycle_root(root)
    skipped_name = "v" + ".".join(
        str(part)
        for part in (*current_version[:-1], current_version[-1] + 1)
    )
    moved_runbook = cycle_runbook_path(root, skipped_name)
    moved_progress = cycle_progress_path(root, skipped_name)
    identity.runbook.rename(moved_runbook)
    identity.progress.rename(moved_progress)
    for path in (root / "AGENTS.md", root / "ARCHITECTURE.md", moved_runbook):
        path.write_text(path.read_text().replace(identity.name, skipped_name))
    config_path = root / "repomix.config.json"
    config = json.loads(config_path.read_text())
    config["ignore"]["customPatterns"] = [
        "docs/cycles/{TASKS,PROGRESS}-v1.2.{[0-2]}"
        "{.md,.*.md,-*.md}"
    ]
    config_path.write_text(json.dumps(config) + "\n")
    _commit_all(root, "plant skipped cycle")

    assert not list(root.glob("repomix-output-*.xml"))
    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert "agree with the tracked retained-cycle set" in error


def test_cycle_check_does_not_fallback_to_root_documents(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _runbook(root).rename(root / _runbook(root).name)
    _progress(root).rename(root / _progress(root).name)

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "docs/cycles/TASKS-v1.2.3-EXECUTION.md" in error
    assert "docs/cycles/PROGRESS-v1.2.3.md" in error


def test_cycle_check_preserves_runbook_history_across_location_move(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    legacy_runbook = root / _runbook(root).name
    legacy_progress = root / _progress(root).name
    _runbook(root).rename(legacy_runbook)
    _progress(root).rename(legacy_progress)
    _commit_cycle_root(root)
    subprocess.run(
        [
            "git",
            "mv",
            legacy_runbook.name,
            str(_runbook(root).relative_to(root)),
        ],
        cwd=root,
        check=True,
    )
    subprocess.run(
        [
            "git",
            "mv",
            legacy_progress.name,
            str(_progress(root).relative_to(root)),
        ],
        cwd=root,
        check=True,
    )

    assert cycle_check.run(root) == 0

    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Cycle Check",
            "-c",
            "user.email=cycle-check@example.invalid",
            "commit",
            "-qm",
            "move cycle documents",
        ],
        cwd=root,
        check=True,
    )
    assert cycle_check.run(root) == 0


def test_cycle_check_rejects_stale_contract_path(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(
        tmp_path,
        "Write the result to `PROGRESS-v1.2.md`.\n",
    )

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "AGENTS.md:9" in error
    assert "stale/cycle-specific progress path 'PROGRESS-v1.2.md'" in error


def test_cycle_check_rejects_cycle_literal_in_tools(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    tools = root / "tools"
    tools.mkdir()
    (tools / "stale.py").write_text('TASK = "v0.10.1"\n')

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "tools/stale.py:1" in error
    assert "cycle-specific literal 'v0.10.1'" in error


def test_cycle_check_rejects_stale_evidence_path_in_run(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    (root / "run").write_text(
        "audit evidence/v0.10.1/deferred-audit/report.json\n"
    )

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "run:1" in error
    assert "cycle-specific literal 'v0.10.1'" in error


def test_cycle_check_rejects_cycle_literal_in_workflow(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    workflows = root / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text("name: v0.10.1 stale\n")

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert ".github/workflows/ci.yml:1" in error
    assert "cycle-specific literal 'v0.10.1'" in error


def test_cycle_check_rejects_undisclosed_acceptance_edit(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "**Acceptance criteria.** Original criterion.",
            "**Acceptance criteria.** Quietly rewritten criterion.",
        )
    )

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "undisclosed runbook amendment" in error
    assert "Step 1 Acceptance criteria" in error


def test_cycle_check_accepts_disclosed_acceptance_edit(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "**Acceptance criteria.** Original criterion.",
            "**Acceptance criteria.** Disclosed rewritten criterion.",
        )
        + "\n## Runbook amendments\n\n"
        "Step 1 — Acceptance criteria clarified — 2026-07-26\n"
    )

    assert cycle_check.run(root) == 0


def test_runbook_contract_fields_keep_suffixed_steps_distinct() -> None:
    fields = cycle_check.runbook_contract_fields(
        "## Step 2 · REPLAY\n\n"
        "**Objective.** Replay bytes.\n\n"
        "**Acceptance criteria.** Replay passes.\n\n"
        "**Done when** replay is measured.\n\n"
        "## Step 2B · OBSERVATION-PIN\n\n"
        "**Objective.** Pin observations.\n\n"
        "**Acceptance criteria.** Pins pass.\n\n"
        "**Done when** observation changes fail.\n"
    )

    assert fields[("2", "Objective")] == "Replay bytes."
    assert fields[("2B", "Objective")] == "Pin observations."
    assert fields[("2", "Done when")] == "replay is measured."
    assert fields[("2B", "Done when")] == "observation changes fail."


def test_cycle_check_accepts_suffixed_deferred_step_reference(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Baseline item | none | no measurement required | none |",
            "| Baseline item | trigger | "
            "v1.2.3 · 2026-07-30 — measured | Step 1A |",
        )
        + "\n## Step 1A · FOLLOW-UP\n\n"
        "**Objective.** Discharge the deferred action.\n\n"
        "**Acceptance criteria.** The action is discharged.\n\n"
        "**Done when** the action is complete.\n\n"
        "## Runbook amendments\n\n"
        "Step 1A — fixture follow-up added — 2026-07-30\n"
    )

    assert cycle_check.run(root) == 0


def test_declared_scope_uses_repository_relative_globs() -> None:
    assert cycle_check.scope_pattern_matches(
        "shell/intel_shell/**",
        "shell/intel_shell/app.py",
    )
    assert not cycle_check.scope_pattern_matches(
        "shell/intel_shell/**",
        "shell/tests/test_cycle_check.py",
    )
    assert cycle_check.scope_pattern_matches(
        "crates/**/*.rs",
        "crates/store/src/sqlite.rs",
    )
    assert not cycle_check.scope_pattern_matches(
        "crates/*/Cargo.toml",
        "crates/store/src/Cargo.toml",
    )


def test_declared_scope_rejects_vacuous_annotated_pattern() -> None:
    vacuous = cycle_check.ScopeDeclaration(
        version=1,
        disposition_intent="no-release",
        allow=("`docs/cycles/**` (except active pair)",),
        release_authorities=(),
        forbid=(),
    )
    corrected = vacuous._replace(allow=("docs/cycles/**",))
    candidates = {"docs/cycles/TASKS-v0.39-EXECUTION.md"}

    errors = cycle_check.scope_pattern_population_errors(vacuous, candidates)

    assert errors == [
        "declared-scope allow pattern is not a literal repository glob: "
        "'`docs/cycles/**` (except active pair)'"
    ]
    assert cycle_check.scope_pattern_population_errors(
        corrected,
        candidates,
    ) == []


def test_v022_scope_fixture_rejects_both_release_paths(
    tmp_path: Path,
) -> None:
    root = tmp_path
    runbook = root / "TASKS-v0.22-EXECUTION.md"
    text = (
        "# Scope fixture\n\n"
        "## Declared scope\n\n"
        "| Scope class | Path or value |\n"
        "|---|---|\n"
        "| `scope_version` | `1` |\n"
        "| `disposition_intent` | `release` |\n"
        "| `allow` | `AGENTS.md` |\n"
        "| `release_authority` | `Cargo.toml` |\n"
        "| `forbid` | `apps/**` |\n"
        "| `forbid` | `Cargo.lock` |\n"
    )
    errors: list[str] = []
    declaration = cycle_check.parse_declared_scope(
        runbook,
        text,
        root,
        errors,
    )
    assert declaration is not None
    assert errors == []

    cycle_check.validate_declared_scope(
        declaration,
        (
            "Cargo.toml",
            "apps/cored/Cargo.toml",
            "Cargo.lock",
        ),
        (
            "apps/cored/Cargo.toml",
            "Cargo.lock",
        ),
        set(),
        False,
        runbook,
        root,
        errors,
    )

    assert any(
        "release-authority set rejects apps/cored/Cargo.toml" in error
        for error in errors
    )
    assert any(
        "release-authority set rejects Cargo.lock" in error
        for error in errors
    )
    assert any(
        "diff rejects apps/cored/Cargo.toml" in error
        for error in errors
    )
    assert any("diff rejects Cargo.lock" in error for error in errors)


def test_declared_scope_standing_status_paths_exclude_agents(
    tmp_path: Path,
) -> None:
    declaration = cycle_check.ScopeDeclaration(
        version=1,
        disposition_intent="no-release",
        allow=(".github/workflows/ci.yml",),
        release_authorities=(),
        forbid=(),
    )
    runbook = tmp_path / "TASKS-v0.23-EXECUTION.md"
    errors: list[str] = []

    cycle_check.validate_declared_scope(
        declaration,
        (),
        (
            "STATE.md",
            "docs/cycles/PROGRESS-v0.23.md",
            "docs/cycles/TASKS-v0.23-EXECUTION.md",
            "AGENTS.md",
        ),
        {
            "STATE.md",
            "docs/cycles/PROGRESS-v0.23.md",
            "docs/cycles/TASKS-v0.23-EXECUTION.md",
        },
        False,
        runbook,
        tmp_path,
        errors,
    )

    assert len(errors) == 1
    assert "diff rejects AGENTS.md" in errors[0]


def test_current_scope_release_forbid_overlap_matches_independent_derivation() -> None:
    root = Path(__file__).resolve().parents[2]
    identity = resolve_cycle(root)
    errors: list[str] = []
    declaration = cycle_check.parse_declared_scope(
        identity.runbook,
        identity.runbook.read_text(),
        root,
        errors,
    )

    assert declaration is not None
    assert errors == []
    authorities = cycle_check.release_authority_paths(root)
    assert len(authorities) == 17
    expected = tuple(
        authority
        for authority in authorities
        if any(
            fnmatchcase(authority, pattern)
            for pattern in declaration.release_authorities
        )
        and any(
            fnmatchcase(authority, pattern)
            for pattern in declaration.forbid
        )
    )
    assert cycle_check.scope_release_forbid_overlaps(
        declaration,
        authorities,
    ) == expected


def test_activation_anchor_is_exclusive_and_next_commit_is_checked(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| `allow` | `**` |",
            "| `allow` | `AGENTS.md` |\n"
            "| `allow` | `repomix.config.json` |",
        )
    )
    _commit_cycle_root(root)

    assert cycle_check.run(root) == 0

    (root / "outside.txt").write_text("outside declared scope\n")
    _commit_all(root, "outside scope")

    assert cycle_check.run(root) == 1
    assert "declared scope diff rejects outside.txt" in capsys.readouterr().err


def test_cycle_check_rejects_unassigned_active_deferral_row(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Baseline item | none | no measurement required | none |",
            "| Runner evidence | release changes | no release yet | "
            "re-measure at the new release commit |",
        )
    )

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "deferred row 'Runner evidence'" in error
    assert "non-none action but names no discharging Step N" in error


def test_cycle_check_accepts_assigned_active_deferral_row(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Baseline item | none | no measurement required | none |",
            "| Runner evidence | release changes | "
            "v1.2.3 · 2026-07-30 — no release yet | "
            "re-measure — discharged by Step 2 |",
        )
        + "\n## Step 2 · RE-MEASURE\n\n"
        "**Objective.** Re-measure the release commit.\n\n"
        "**Acceptance criteria.** Hosted counts captured.\n\n"
        "**Done when** the counts are recorded.\n\n"
        "## Runbook amendments\n\n"
        "Step 2 — fixture re-measure added — 2026-07-30\n"
    )

    assert cycle_check.run(root) == 0


def test_cycle_check_accepts_dated_negative_trigger_observation(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Baseline item | none | no measurement required | none |",
            "| L2 wrapper | an operator server session | "
            "v1.2.3 · 2026-07-30 — no operator server session has occurred | "
            "none |",
        )
    )

    assert cycle_check.run(root) == 0


def test_cycle_check_rejects_trigger_observation_without_valid_date(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Baseline item | none | no measurement required | none |",
            "| L2 wrapper | an operator server session | "
            "v1.2.3 — no operator server session has occurred | none |",
        )
    )

    assert cycle_check.run(root) == 1
    assert (
        "trigger-bearing row 'L2 wrapper' requires a valid dated measured "
        "observation"
        in capsys.readouterr().err
    )


def test_trigger_date_failure_is_independent_of_cycle_identity_requirement(
    tmp_path: Path,
) -> None:
    path = tmp_path / "trigger-table.md"
    text = (
        "# Trigger table\n\n"
        "### Dated operational-residual dispositions\n\n"
        "| subject | trigger | measured observation |\n"
        "|---|---|---|\n"
        "| planted row | an operator session | no session occurred |\n"
    )
    path.write_text(text)

    for required_cycle in (None, "v1.2.3"):
        errors: list[str] = []
        assert (
            cycle_check.check_trigger_table(
                path,
                text,
                cycle_check.DATED_DISPOSITIONS_HEADING,
                "subject",
                tmp_path,
                errors,
                required_cycle,
            )
            == 1
        )
        date_errors = [
            error
            for error in errors
            if "requires a valid dated measured observation" in error
        ]
        assert len(date_errors) == 1
        if required_cycle is None:
            assert len(errors) == 1
        else:
            assert len(errors) == 2
            assert any(
                "requires a measured observation naming active cycle"
                in error
                for error in errors
            )


def test_trigger_floor_before_freshness_reports_instead_of_raising(
    tmp_path: Path,
    capsys,
    monkeypatch,
) -> None:
    root = _cycle_root(tmp_path)
    monkeypatch.setattr(
        cycle_check,
        "TRIGGER_FRESHNESS_FORWARD_BOUNDARY",
        (1, 2, 4),
    )
    monkeypatch.setattr(
        cycle_check,
        "TRIGGER_FLOOR_FORWARD_BOUNDARY",
        (1, 2, 2),
    )

    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert (
        "TRIGGER_FLOOR_FORWARD_BOUNDARY must be greater than or equal to "
        "TRIGGER_FRESHNESS_FORWARD_BOUNDARY"
        in error
    )
    assert "UnboundLocalError" not in error


def test_forward_boundary_registry_derives_every_module_constant(
    monkeypatch,
) -> None:
    boundaries = cycle_check.module_forward_boundaries()
    relationships = cycle_check.FORWARD_BOUNDARY_RELATIONSHIPS
    assert boundaries
    assert set(boundaries) == set(relationships)
    for dependencies, reason in relationships.values():
        assert reason.strip()
        if not dependencies:
            assert reason.startswith("Independent:")

    planted = "PLANTED_UNREGISTERED_FORWARD_BOUNDARY"
    monkeypatch.setattr(cycle_check, planted, (0, 30), raising=False)
    errors: list[str] = []
    cycle_check.check_trigger_boundary_relationship(errors)
    assert errors == [
        "tools/cycle_check.py module-scoped forward-boundary registry is "
        f"missing {planted}"
    ]


def test_trigger_identity_cannot_precede_freshness(monkeypatch) -> None:
    monkeypatch.setattr(
        cycle_check,
        "TRIGGER_FRESHNESS_FORWARD_BOUNDARY",
        (1, 2, 4),
    )
    monkeypatch.setattr(
        cycle_check,
        "TRIGGER_IDENTITY_FORWARD_BOUNDARY",
        (1, 2, 2),
    )
    monkeypatch.setattr(
        cycle_check,
        "TRIGGER_FLOOR_FORWARD_BOUNDARY",
        (1, 2, 4),
    )
    monkeypatch.setattr(
        cycle_check,
        "GOVERNED_EXPORT_FORWARD_BOUNDARY",
        (1, 2, 4),
    )
    monkeypatch.setattr(
        cycle_check,
        "ARTIFACT_BYTE_BOUNDARY_FORWARD_BOUNDARY",
        (1, 2, 4),
    )
    monkeypatch.setattr(
        cycle_check,
        "STATE_REGION_CONTRACT_FORWARD_BOUNDARY",
        (1, 2, 4),
    )
    errors: list[str] = []
    cycle_check.check_trigger_boundary_relationship(errors)
    assert errors == [
        "TRIGGER_IDENTITY_FORWARD_BOUNDARY must be greater than or equal to "
        "TRIGGER_FRESHNESS_FORWARD_BOUNDARY"
    ]


def test_cycle_check_rejects_prior_cycle_trigger_observation(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "| Baseline item | none | no measurement required | none |",
            "| L2 wrapper | an operator server session | "
            "v0.27 · 2026-07-30 — no operator server session occurred | "
            "none |",
        )
    )

    assert cycle_check.run(root) == 1
    assert (
        "trigger-bearing row 'L2 wrapper' requires a measured observation "
        "naming active cycle 'v1.2.3'"
        in capsys.readouterr().err
    )


def test_cycle_check_ignores_rows_without_a_trigger(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "Measured 2026-07-29",
            "Measured observation",
        )
    )

    assert cycle_check.run(root) == 0


def test_current_trigger_freshness_tables_are_complete() -> None:
    root = Path(__file__).resolve().parents[2]
    identity = resolve_cycle(root)
    errors: list[str] = []

    counts = cycle_check.check_trigger_freshness(
        identity.runbook,
        identity.runbook.read_text(),
        root,
        errors,
    )
    expected = (
        len(
            cycle_check.governed_trigger_subjects(
                (root / "ARCHITECTURE.md").read_text(),
                cycle_check.DATED_DISPOSITIONS_HEADING,
                "subject",
            )
        ),
        len(
            cycle_check.governed_trigger_subjects(
                identity.runbook.read_text(),
                cycle_check.DEFERRED_HEADING,
                "Deferred item",
            )
        ),
    )

    assert counts == expected
    assert all(count > 0 for count in expected)
    assert errors == []


def test_cycle_check_rejects_zero_trigger_populations(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    architecture = root / "ARCHITECTURE.md"
    architecture.write_text(
        architecture.read_text().replace(
            "| trigger baseline | active | active condition |",
            "| trigger baseline | active | none |",
            ).replace(
                "| protected evidence-manifest growth (fixture) | accepted | "
                "the manifest reaches its governed artifact byte boundary, "
                "or two consecutive clean ./run verify-artifacts runs each "
                "take ≥1.00 s real |",
                "| protected evidence-manifest growth (fixture) | accepted | "
                "none |",
            ).replace(
                "| review-export size and retention bound (fixture) | "
            "accepted | export ceiling |",
            "| review-export size and retention bound (fixture) | "
            "accepted | none |",
        )
    )
    runbook = _runbook(root)
    runbook.write_text(
            runbook.read_text().replace(
                "| Trigger baseline | active condition |",
                "| Trigger baseline | none |",
            ).replace(
                "| Second `STATE.md` archival | the export ceiling trigger "
                "fires, or `STATE.md` reaches its governed artifact byte "
                "boundary |",
                "| Second `STATE.md` archival | none |",
            )
    )

    assert cycle_check.run(root) == 1
    error = capsys.readouterr().err
    assert (
        "'### Dated operational-residual dispositions' must contain at least "
        "one trigger-bearing row"
        in error
    )
    assert (
        "'## Deferred means deferred' must contain at least one "
        "trigger-bearing row"
        in error
    )


def test_deferred_carry_forward_rejects_silent_drop(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    prior = _runbook(root, "v1.2.2")
    prior.write_text(
        "# Prior cycle\n\n"
        "## Deferred means deferred\n\n"
        "| Deferred item | Unchanged trigger | Measured observation | action |\n"
        "|---|---|---|---|\n"
        "| Retired condition | still active | "
        "v1.2.2 · 2026-07-29 — measured | none |\n"
    )
    active = _runbook(root)
    errors: list[str] = []

    cycle_check.check_deferred_carry_forward(
        active,
        active.read_text(),
        root,
        errors,
    )

    assert any(
        "deferred subject 'Retired condition'" in error
        and "absent without a valid dated completion" in error
        for error in errors
    )


def test_deferred_carry_forward_accepts_dated_completions(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    prior = _runbook(root, "v1.2.2")
    prior.write_text(
        "# Prior cycle\n\n"
        "## Deferred means deferred\n\n"
        "| Deferred item | Unchanged trigger | Measured observation | action |\n"
        "|---|---|---|---|\n"
        "| First live SEC RSS harvest | authorization | "
        "v1.2.2 · 2026-07-29 — measured | none |\n"
        "| Observation-byte manifest coverage | schema gap | "
        "v1.2.2 · 2026-07-29 — measured | none |\n"
    )
    active = _runbook(root)
    active.write_text(
        active.read_text()
        + "\n## Deferred completions\n\n"
        "| Deferred item | Dated completion |\n"
        "|---|---|\n"
        "| First live SEC RSS harvest | "
        "2026-07-30 — completed by the prior cycle |\n"
        "| Observation-byte manifest coverage | "
        "2026-07-30 — completed by the prior cycle |\n"
    )
    errors: list[str] = []

    cycle_check.check_deferred_carry_forward(
        active,
        active.read_text(),
        root,
        errors,
    )

    assert errors == []


def test_current_deferred_carry_forward_is_complete() -> None:
    root = Path(__file__).resolve().parents[2]
    identity = resolve_cycle(root)
    errors: list[str] = []

    cycle_check.check_deferred_carry_forward(
        identity.runbook,
        identity.runbook.read_text(),
        root,
        errors,
    )

    assert errors == []


def test_cycle_check_rejects_cross_step_recorded_quantity(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text()
        + "\n## Step 2 · RE-MEASURE\n\n"
        "**Objective.** Compare current executions.\n\n"
        "**Acceptance criteria.** Hosted counts match Step 1's recorded "
        "values.\n\n"
        "**Done when** current executions agree.\n"
    )

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "TASKS-v1.2.3-EXECUTION.md:" in error
    assert "active Step 2 acceptance criterion cites Step 1's" in error
    assert "recorded/measured quantity" in error
    assert "same commit" in error


def test_cycle_check_accepts_same_commit_quantity_relation(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "**Acceptance criteria.** Original criterion.",
            "**Acceptance criteria.** Hosted counts equal local counts at "
            "the same commit.",
        )
        + "\n## Runbook amendments\n\n"
        "Step 1 — fixture criterion changed — 2026-07-30\n"
    )

    assert cycle_check.run(root) == 0


def _close_active_cycle(root: Path, disposition: str) -> None:
    _commit_cycle_root(root)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace("- [ ] unfinished task", "- [x] finished")
        + "\n## Runbook amendments\n\n"
        "Step 1 — Record the closing checklist — 2026-07-28\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-28\n"
        f"{disposition}\n"
        "- **Intentionally unreleased implementation commits:**\n"
        f"  - `{commit}`\n"
    )


def test_cycle_check_rejects_undated_active_disposition(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _close_active_cycle(
        root,
        "- **Release disposition:** no-release",
    )

    assert cycle_check.run(root) == 1

    error = capsys.readouterr().err
    assert "TASKS-v1.2.3-EXECUTION.md:" in error
    assert "release disposition must state an as-of date" in error
    assert "found undated '- **Release disposition:** no-release'" in error


def test_cycle_check_accepts_dated_active_disposition(
    tmp_path: Path,
) -> None:
    root = _cycle_root(tmp_path)
    _close_active_cycle(
        root,
        "- **Release disposition:** no-release (as of 2026-07-28)",
    )

    assert cycle_check.run(root) == 0


def test_cycle_check_portable_mode_retains_commit_checks_without_local_tag(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    _runbook(root, "v1.1.0").write_text(
        "# Closed cycle\n\n"
        "- [x] completed task\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-26\n"
        "- **Release disposition:** release\n"
        "- **Release:** `v1.1.0`\n"
        f"- **Release commit:** `{commit}`\n"
        f"- **Annotated tag object:** `{'0' * 40}`\n"
    )
    (root / "STATE.md").write_text(
        _state_with_regions("portable publication structure.")
    )

    assert cycle_check.run(root) == 1
    assert "annotated tag 'v1.1.0' does not resolve" in capsys.readouterr().err

    assert cycle_check.run(root, verify_local_tag_refs=False) == 0
    output = capsys.readouterr().out
    assert (
        "publication-status: local-tag-reconciliation=not-requested "
        "bound=portable hosted mode lacks historical local tag objects; "
        "State/header admission and closed-runbook structure remain enforced"
        in output
    )


def test_publication_status_names_no_release_bound(tmp_path: Path) -> None:
    root = tmp_path / "no-release"
    root.mkdir()
    errors: list[str] = []

    report = cycle_check.check_publication_status(root, [], errors)

    assert errors == []
    assert report == (
        "publication-status: local-tag-reconciliation=not-applicable "
        "bound=no reachable closed release exists, so there is no release "
        "ref to reconcile"
    )


def test_publication_status_names_legacy_protocol_bound(
    tmp_path: Path,
    monkeypatch,
) -> None:
    root = tmp_path / "legacy-release"
    root.mkdir()
    tag_object = "a" * 40
    tag_target = "b" * 40
    tag = "v1.0.0"
    runbook = root / "TASKS-v1.0.0-EXECUTION.md"
    runbook.write_text("# Legacy release fixture\n")
    (root / "STATE.md").write_text(
        "# State\n\n"
        "**As of:** published release; annotated tag object is "
        f"`{tag_object}` and tag target is `{tag_target}`.\n"
    )
    monkeypatch.setattr(
        cycle_check,
        "newest_closed_release",
        lambda _files: cycle_check.ClosedRelease(
            runbook=runbook,
            tag=tag,
            release_commit=tag_target,
            recorded_tag_object=tag_object,
        ),
    )

    def fake_git_output(_root: Path, *args: str) -> str | None:
        values = {
            ("rev-parse", tag): tag_object,
            ("rev-parse", f"{tag}^{{}}"): tag_target,
            ("cat-file", "-t", tag_object): "tag",
        }
        return values.get(args)

    monkeypatch.setattr(cycle_check, "git_output", fake_git_output)
    monkeypatch.setattr(cycle_check, "git_status", lambda *_args: (0, ""))
    errors: list[str] = []

    report = cycle_check.check_publication_status(root, [runbook], errors)

    assert errors == []
    assert report == (
        "publication-status: local-tag-reconciliation=verified "
        "protocol=legacy release=v1.0.0 bound=R-CLOSE post-push records do "
        "not apply to a legacy release"
    )


def test_cycle_check_portable_mode_still_rejects_missing_release_commit(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    _commit_cycle_root(root)
    _runbook(root, "v1.1.0").write_text(
        "# Closed cycle\n\n"
        "- [x] completed task\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-26\n"
        "- **Release disposition:** release\n"
        "- **Release:** `v1.1.0`\n"
        f"- **Release commit:** `{'1' * 40}`\n"
        f"- **Annotated tag object:** `{'0' * 40}`\n"
    )

    assert cycle_check.run(root, verify_local_tag_refs=False) == 1
    assert "recorded release commit" in capsys.readouterr().err
