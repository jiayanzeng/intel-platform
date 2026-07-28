import json
import subprocess
from pathlib import Path

from tools import cycle_check


def _cycle_root(tmp_path: Path, contract_tail: str = "") -> Path:
    root = tmp_path / "cycle"
    root.mkdir()
    (root / "AGENTS.md").write_text(
        "# Contract\n\n"
        "**Active cycle:** v1.2.3\n\n"
        "Task work is ordered in `TASKS-v1.2.3-EXECUTION.md` and logged in "
        "`PROGRESS-v1.2.3.md`.\n\n"
        "## 0. Contract\n\n"
        f"{contract_tail}"
    )
    (root / "TASKS-v1.2.3-EXECUTION.md").write_text(
        "# Open cycle\n\n"
        "## Step 1 · CHECK\n\n"
        "**Objective.** Preserve the contract.\n\n"
        "**Acceptance criteria.** Original criterion.\n\n"
        "**Done when** the original criterion passes.\n\n"
        "- [ ] unfinished task\n"
    )
    (root / "PROGRESS-v1.2.3.md").write_text("# Progress\n")
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


def test_cycle_check_accepts_cycle_paths_only_in_declaration(
    tmp_path: Path,
) -> None:
    assert cycle_check.run(_cycle_root(tmp_path)) == 0


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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    runbook = root / "TASKS-v1.2.3-EXECUTION.md"
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
    (root / "TASKS-v1.1.0-EXECUTION.md").write_text(
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
    (root / "TASKS-v1.1.0-EXECUTION.md").write_text(
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
