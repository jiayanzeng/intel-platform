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
        "# Open cycle\n\n- [ ] unfinished task\n"
    )
    (root / "PROGRESS-v1.2.3.md").write_text("# Progress\n")
    return root


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
