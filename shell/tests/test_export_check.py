import subprocess
from pathlib import Path

from tools import export_check


def _repository(tmp_path: Path) -> tuple[Path, set[str]]:
    root = tmp_path / "repository"
    root.mkdir()
    paths = {
        *export_check.REQUIRED_PATHS,
        "apps/cored/src/main.rs",
        "crates/core/src/lib.rs",
        "shell/intel_shell/app.py",
        "tools/check.py",
    }
    for raw_path in paths:
        path = root / raw_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{raw_path}\n")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    return root, paths


def _write_export(path: Path, included: set[str]) -> None:
    entries = "\n".join(
        f'<file path="{raw_path}">\ncontents\n</file>'
        for raw_path in sorted(included)
    )
    path.write_text(f"<repository_files>\n{entries}\n</repository_files>\n")


def test_complete_export_uses_the_git_derived_source_set(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    _write_export(export, paths)

    sources, actual, errors = export_check.check_export(root, export)

    assert sources == {
        "apps/cored/src/main.rs",
        "crates/core/src/lib.rs",
        "shell/intel_shell/app.py",
        "tools/check.py",
    }
    assert actual == paths
    assert errors == []


def test_new_tracked_source_is_required_without_changing_a_count(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    _write_export(export, paths)
    new_source = root / "tools" / "new_check.py"
    new_source.write_text("new source\n")
    subprocess.run(["git", "add", str(new_source)], cwd=root, check=True)

    _, _, errors = export_check.check_export(root, export)

    assert errors == ["missing derived source path: tools/new_check.py"]


def test_missing_cargo_lock_is_a_named_failure(
    tmp_path: Path,
    capsys,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    _write_export(export, paths - {"Cargo.lock"})

    assert export_check.run(root, export) == 1
    error = capsys.readouterr().err
    assert "export-check: ERROR: missing required path: Cargo.lock" in error
    assert "export-check: FAIL" in error
