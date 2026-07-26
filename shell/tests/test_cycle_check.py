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
