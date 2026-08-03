import json
import subprocess
from pathlib import Path

from tools import export_check


def _repository(tmp_path: Path) -> tuple[Path, set[str]]:
    root = tmp_path / "repository"
    root.mkdir()
    active_patch = 8
    retained_cycles = [
        f"v1.2.{patch}"
        for patch in range(
            active_patch - export_check.CYCLE_RETENTION_DEPTH + 1,
            active_patch + 1,
        )
    ]
    cycle_paths = {
        path
        for cycle in retained_cycles
        for path in (
            f"docs/cycles/TASKS-{cycle}-EXECUTION.md",
            f"docs/cycles/PROGRESS-{cycle}.md",
        )
    }
    paths = {
        *export_check.REQUIRED_PATHS,
        *cycle_paths,
        "apps/cored/src/main.rs",
        "crates/core/src/lib.rs",
        "shell/intel_shell/app.py",
        "tools/check.py",
    }
    for raw_path in paths:
        path = root / raw_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{raw_path}\n")
    (root / "AGENTS.md").write_text(
        f"**Active cycle:** {retained_cycles[-1]}\n"
    )
    older_cycle = (
        f"v1.2.{active_patch - export_check.CYCLE_RETENTION_DEPTH}"
    )
    older_runbook = root / f"docs/cycles/TASKS-{older_cycle}-EXECUTION.md"
    older_runbook.write_text("# Older cycle\n")
    older_progress = root / f"docs/cycles/PROGRESS-{older_cycle}.md"
    older_progress.write_text("# Older progress\n")
    excluded_paths = (
        "observations/capture-a/sec-edgar-usgaap.rss.xml",
        "observations/capture-b/sec-edgar-usgaap.rss.xml",
    )
    (root / "repomix.config.json").write_text(
        json.dumps({"ignore": {"customPatterns": list(excluded_paths)}})
    )
    for raw_path in excluded_paths:
        excluded_capture = root / raw_path
        excluded_capture.parent.mkdir(parents=True, exist_ok=True)
        excluded_capture.write_text("excluded wire body\n")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    return root, paths


def _write_export(
    path: Path,
    included: set[str],
    *,
    padding: int = 0,
) -> None:
    entries = "\n".join(
        f'<file path="{raw_path}">\ncontents\n</file>'
        for raw_path in sorted(included)
    )
    path.write_text(
        f"<repository_files>\n{entries}\n</repository_files>\n"
        + ("x" * padding)
    )


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


def test_export_over_ceiling_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    _write_export(export, paths, padding=export_check.MAX_EXPORT_BYTES)

    _, _, errors = export_check.check_export(root, export)

    assert any(
        error.startswith("export size ")
        and f"exceeds ceiling {export_check.MAX_EXPORT_BYTES}" in error
        for error in errors
    )


def test_missing_retained_cycle_document_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    missing = sorted(export_check.expected_retained_cycle_paths(root))[0]
    _write_export(export, paths - {missing})

    _, _, errors = export_check.check_export(root, export)

    assert f"missing retained cycle document: {missing}" in errors


def test_dropped_cycle_document_present_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    retained = export_check.expected_retained_cycle_paths(root)
    dropped = next(
        path.relative_to(root).as_posix()
        for path in export_check.execution_runbooks(root)
        if path.relative_to(root).as_posix() not in retained
    )
    _write_export(export, paths | {dropped})

    _, _, errors = export_check.check_export(root, export)

    assert (
        "unexpected cycle document outside retention depth "
        f"{export_check.CYCLE_RETENTION_DEPTH}: {dropped}"
    ) in errors


def test_excluded_wire_capture_present_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    excluded = next(iter(export_check.excluded_export_paths(root)))
    _write_export(export, paths | {excluded})

    _, _, errors = export_check.check_export(root, export)

    assert f"excluded export path is present: {excluded}" in errors


def test_every_exact_excluded_wire_capture_is_required(
    tmp_path: Path,
) -> None:
    root, _ = _repository(tmp_path)
    configured = sorted(export_check.excluded_export_paths(root))
    missing = root / configured[-1]
    missing.unlink()

    try:
        export_check.excluded_export_paths(root)
    except export_check.ExportCheckError as error:
        assert str(error) == (
            f"invalid exact Repomix observation exclusion: {configured[-1]}"
        )
    else:
        raise AssertionError("missing exact exclusion was accepted")


def test_excluded_state_archive_present_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    excluded = f"{export_check.EXCLUDED_EXPORT_PREFIXES[0]}archived.md"
    _write_export(export, paths | {excluded})

    _, _, errors = export_check.check_export(root, export)

    assert (
        "excluded export prefix is present: "
        f"{export_check.EXCLUDED_EXPORT_PREFIXES[0]}"
    ) in errors
