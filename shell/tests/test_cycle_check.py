import json
import subprocess
from pathlib import Path

from tools import cycle_check
from tools.cycle_identity import (
    cycle_documents_dir,
    cycle_progress_path,
    cycle_runbook_path,
    execution_runbooks,
)


def _runbook(root: Path, cycle: str = "v1.2.3") -> Path:
    return cycle_runbook_path(root, cycle)


def _progress(root: Path, cycle: str = "v1.2.3") -> Path:
    return cycle_progress_path(root, cycle)


def _cycle_root(tmp_path: Path, contract_tail: str = "") -> Path:
    root = tmp_path / "cycle"
    root.mkdir()
    cycle_documents_dir(root).mkdir(parents=True)
    (root / "AGENTS.md").write_text(
        "# Contract\n\n"
        "**Active cycle:** v1.2.3\n\n"
        "Task work is ordered in "
        "`docs/cycles/TASKS-v1.2.3-EXECUTION.md` and logged in "
        "`docs/cycles/PROGRESS-v1.2.3.md`.\n\n"
        "## 0. Contract\n\n"
        f"{contract_tail}"
    )
    _runbook(root).write_text(
        "# Open cycle\n\n"
        "## Step 1 · CHECK\n\n"
        "**Objective.** Preserve the contract.\n\n"
        "**Acceptance criteria.** Original criterion.\n\n"
        "**Done when** the original criterion passes.\n\n"
        "- [ ] unfinished task\n"
    )
    _progress(root).write_text("# Progress\n")
    config = root / "config"
    config.mkdir()
    (config / "cycle-history.json").write_text(
        json.dumps({"schema_version": 1, "artifacts": {}}) + "\n"
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


def _publication_errors(root: Path) -> list[str]:
    errors: list[str] = []
    cycle_check.check_publication_status(
        root, execution_runbooks(root), errors
    )
    return errors


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


def test_cycle_check_accepts_cycle_paths_only_in_declaration(
    tmp_path: Path,
) -> None:
    assert cycle_check.run(_cycle_root(tmp_path)) == 0


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


def test_cycle_check_rejects_unassigned_active_deferral_row(
    tmp_path: Path,
    capsys,
) -> None:
    root = _cycle_root(tmp_path)
    runbook = _runbook(root)
    runbook.write_text(
        runbook.read_text().replace(
            "## Step 1 · CHECK",
            "## Deferred means deferred\n\n"
            "| Deferred item | Unchanged trigger | v1.2.3 action |\n"
            "|---|---|---|\n"
            "| Runner evidence | release changes | "
            "re-measure at the new release commit |\n\n"
            "## Step 1 · CHECK",
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
            "## Step 1 · CHECK",
            "## Deferred means deferred\n\n"
            "| Deferred item | Unchanged trigger | v1.2.3 action |\n"
            "|---|---|---|\n"
            "| Runner evidence | release changes | "
            "re-measure — discharged by Step 2 |\n\n"
            "## Step 1 · CHECK",
        )
        + "\n## Step 2 · RE-MEASURE\n\n"
        "**Objective.** Re-measure the release commit.\n\n"
        "**Acceptance criteria.** Hosted counts captured.\n\n"
        "**Done when** the counts are recorded.\n"
    )

    assert cycle_check.run(root) == 0


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

    assert cycle_check.run(root) == 1
    assert "annotated tag 'v1.1.0' does not resolve" in capsys.readouterr().err

    assert cycle_check.run(root, verify_local_tag_refs=False) == 0


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
