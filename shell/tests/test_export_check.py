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
        *cycle_paths,
        ".github/workflows/ci.yml",
        "AGENTS.md",
        "ARCHITECTURE.md",
        "Cargo.lock",
        "Cargo.toml",
        "apps/cored/src/main.rs",
        "config/protected-artifacts.json",
        "crates/core/src/lib.rs",
        "repomix.config.json",
        "run",
        "rust-toolchain.toml",
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
    attention_denominator = 1_000_000
    attention_boundary = (
        export_check.MAX_EXPORT_BYTES
        - export_check.EXPORT_ATTENTION_HEADROOM_CYCLES * attention_denominator
    )
    (root / "ARCHITECTURE.md").write_text(
        "# Architecture\n\n"
        "| subject | disposition | trigger | dated measured observation |\n"
        "|---|---|---|---|\n"
        "| review-export size and retention bound (fixture) | accepted | "
        "the export meets its attention boundary | v1.2.8 · 2026-08-04 — "
        "measured below boundary. Review-export attention boundary: "
        f"headroom_cycles=`{export_check.EXPORT_ATTENTION_HEADROOM_CYCLES}`; "
        f"denominator_bytes_per_cycle=`{attention_denominator}`; "
        f"boundary_bytes=`{attention_boundary}`. |\n"
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
    structural_archive = "docs/state-archive/archive.md"
    manifest_records = [
        {"path": raw_path, "grade": "observation"}
        for raw_path in excluded_paths
    ] + [{"path": structural_archive, "grade": "structural"}]
    (root / "config/protected-artifacts.json").write_text(
        json.dumps({"pinned_files": manifest_records})
    )
    (root / "repomix.config.json").write_text(
        json.dumps(
            {
                "ignore": {
                    "customPatterns": [
                        *excluded_paths,
                        "docs/state-archive/**",
                    ]
                }
            }
        )
    )
    for raw_path in excluded_paths:
        excluded_capture = root / raw_path
        excluded_capture.parent.mkdir(parents=True, exist_ok=True)
        excluded_capture.write_text("excluded wire body\n")
        (excluded_capture.parent / ".gitattributes").write_text(
            f"{excluded_capture.name} binary\n"
        )
        paths.add(
            (excluded_capture.parent / ".gitattributes")
            .relative_to(root)
            .as_posix()
        )
    archive = root / structural_archive
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text("structural archive\n")
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

    assert sources == export_check.derived_required_paths(root)
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

    assert errors == ["missing derived required path: tools/new_check.py"]


def test_missing_cargo_lock_is_a_named_failure(
    tmp_path: Path,
    capsys,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    _write_export(export, paths - {"Cargo.lock"})

    assert export_check.run(root, export) == 1
    error = capsys.readouterr().err
    assert (
        "export-check: ERROR: missing derived required path: Cargo.lock"
        in error
    )
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


def test_export_at_attention_boundary_requires_dated_disposition(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    boundary = export_check.export_attention_boundary(root).boundary_bytes
    _write_export(export, paths, padding=boundary)

    _, _, errors = export_check.check_export(root, export)

    assert any(
        f"meets or exceeds attention boundary {boundary}" in error
        and "requires a dated 'trigger-fired disposition:'" in error
        for error in errors
    )


def test_export_at_attention_boundary_accepts_dated_disposition(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    architecture = root / "ARCHITECTURE.md"
    architecture.write_text(
        architecture.read_text().replace(
            "measured below boundary.",
            "trigger-fired disposition: kind=`unheld-lever`; "
            "lever=`Grant E`; recoverable_bytes=`84896`.",
        )
    )
    export = tmp_path / "review.xml"
    boundary = export_check.export_attention_boundary(root).boundary_bytes
    _write_export(export, paths, padding=boundary)

    _, _, errors = export_check.check_export(root, export)

    assert not any("attention boundary" in error for error in errors)


def test_attention_boundary_rejects_uncomputed_value(tmp_path: Path) -> None:
    root, _ = _repository(tmp_path)
    architecture = root / "ARCHITECTURE.md"
    architecture.write_text(
        architecture.read_text().replace(
            "boundary_bytes=`1000000`",
            "boundary_bytes=`1000001`",
        )
    )

    try:
        export_check.export_attention_boundary(root)
    except export_check.ExportCheckError as error:
        assert "disagrees with 3000000 - (2 * 1000000) = 1000000" in str(error)
    else:
        raise AssertionError("uncomputed review-export boundary was accepted")


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


def test_untracked_export_entry_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    untracked = "docs/untracked-review-input.md"
    (root / untracked).parent.mkdir(parents=True, exist_ok=True)
    (root / untracked).write_text("not in Git\n")
    _write_export(export, paths | {untracked})

    _, _, errors = export_check.check_export(root, export)

    assert f"export contains untracked path: {untracked}" in errors


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


def test_exact_observation_exclusion_outside_derived_class_fails(
    tmp_path: Path,
) -> None:
    root, _ = _repository(tmp_path)
    report = root / "observations/capture-a/review-report.md"
    report.write_text("review source\n")
    config_path = root / "repomix.config.json"
    config = json.loads(config_path.read_text())
    config["ignore"]["customPatterns"].append(
        report.relative_to(root).as_posix()
    )
    config_path.write_text(json.dumps(config))

    try:
        export_check.excluded_export_paths(root)
    except export_check.ExportCheckError as error:
        assert "exact Repomix observation exclusion is not derived raw wire" in str(
            error
        )
    else:
        raise AssertionError("non-wire exact observation exclusion was accepted")


def test_derived_raw_wire_population_is_nonempty_and_exact(
    tmp_path: Path,
) -> None:
    root, _ = _repository(tmp_path)

    derived = export_check.derived_raw_wire_paths(root)
    configured = export_check.configured_raw_wire_exclusions(root)

    assert len(derived) == 2
    assert configured == derived
    assert export_check.raw_wire_exclusion_errors(derived, configured) == []


def test_excluded_state_archive_present_is_a_named_failure(
    tmp_path: Path,
) -> None:
    root, paths = _repository(tmp_path)
    export = tmp_path / "review.xml"
    prefix = next(iter(export_check.derived_structural_archive_prefixes(root)))
    excluded = f"{prefix}additional.md"
    _write_export(export, paths | {excluded})

    _, _, errors = export_check.check_export(root, export)

    assert (
        "excluded export prefix is present: "
        f"{prefix}"
    ) in errors
