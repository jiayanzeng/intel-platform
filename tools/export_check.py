#!/usr/bin/env python3
"""Verify that a Repomix review export contains every required source path."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.cycle_identity import (
    CycleIdentityError,
    execution_runbooks,
    progress_for_runbook,
    resolve_cycle,
)

FILE_PATH_RE = re.compile(r'^<file path="([^"]+)">\r?$', re.MULTILINE)
REVIEW_SOURCE_PROJECTION_RE = re.compile(
    r'^<!-- REVIEW_SOURCE_PROJECTION:START source="([^"]+)" -->\r?\n'
    r'```json\r?\n(.*?)\r?\n```\r?\n'
    r'<!-- REVIEW_SOURCE_PROJECTION:END -->$',
    re.MULTILINE | re.DOTALL,
)
CYCLE_DOCUMENT_RE = re.compile(
    r"^docs/cycles/(?:TASKS|PROGRESS)-"
    r"v[0-9]+(?:\.[0-9]+)*(?:-EXECUTION)?\.md$"
)
EXECUTION_RUNBOOK_PATH_RE = re.compile(
    r"^docs/cycles/TASKS-(v[0-9]+(?:\.[0-9]+)*)-EXECUTION\.md$"
)
MAX_EXPORT_BYTES = 3_000_000
CYCLE_RETENTION_DEPTH = 2
EXPORT_ATTENTION_HEADROOM_CYCLES = 2
GLOB_META = frozenset("*?[]{}")
EXPORT_ATTENTION_BOUNDARY_RE = re.compile(
    r"Review-export attention boundary: headroom_cycles=`([0-9]+)`; "
    r"denominator_bytes_per_cycle=`([0-9]+)`; boundary_bytes=`([0-9]+)`\."
)
TRIGGER_FIRED_DISPOSITION_PREFIX_RE = re.compile(
    r"\btrigger-fired disposition:",
    re.IGNORECASE,
)
TRIGGER_MEASURED_CHANGE_DISPOSITION_RE = re.compile(
    r"\btrigger-fired disposition:\s*kind=`?measured-change`?;\s*"
    r"subject=`?([^`;\n]+)`?;\s*baseline_bytes=`?([0-9]+)`?;\s*"
    r"current_bytes=`?([0-9]+)`?\.",
    re.IGNORECASE,
)
TRIGGER_UNHELD_LEVER_DISPOSITION_RE = re.compile(
    r"\btrigger-fired disposition:\s*kind=`?unheld-lever`?;\s*"
    r"lever=`?([^`;\n]+)`?;\s*recoverable_bytes=`?([1-9][0-9]*)`?\.",
    re.IGNORECASE,
)
ISO_DATE_RE = re.compile(r"\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b")


class ExportCheckError(RuntimeError):
    """The export or its repository source set could not be inspected."""


class ExportAttentionBoundary(NamedTuple):
    headroom_cycles: int
    denominator_bytes_per_cycle: int
    boundary_bytes: int


class ReviewProjectionRecord(NamedTuple):
    host_path: str
    source_path: str
    projection_text: str


class ReviewProjectionPopulation(NamedTuple):
    manifests: int
    total_pins: int
    retained_pins: int
    omitted_pins: int


def valid_iso_date(raw: str) -> bool:
    try:
        return dt.date.fromisoformat(raw).isoformat() == raw
    except ValueError:
        return False


def governed_export_measured_cell(root: Path) -> str:
    architecture_path = root / "ARCHITECTURE.md"
    try:
        lines = architecture_path.read_text().splitlines()
    except OSError as error:
        raise ExportCheckError(
            f"cannot read review-export boundary from {architecture_path}: {error}"
        ) from error
    rows = [
        line
        for line in lines
        if line.startswith("| review-export size and retention bound")
    ]
    if len(rows) != 1:
        raise ExportCheckError(
            "Architecture must contain exactly one governed review-export row"
        )
    cells = [cell.strip() for cell in rows[0].strip().strip("|").split("|")]
    if len(cells) != 4:
        raise ExportCheckError("governed review-export row must have four cells")
    return cells[3]


def export_attention_boundary(root: Path) -> ExportAttentionBoundary:
    measured = governed_export_measured_cell(root)
    matches = list(EXPORT_ATTENTION_BOUNDARY_RE.finditer(measured))
    if len(matches) != 1:
        raise ExportCheckError(
            "governed review-export row requires exactly one executable "
            "attention boundary"
        )
    headroom_cycles, denominator, boundary = (
        int(value) for value in matches[0].groups()
    )
    if headroom_cycles != EXPORT_ATTENTION_HEADROOM_CYCLES:
        raise ExportCheckError(
            f"review-export attention reserve must be "
            f"{EXPORT_ATTENTION_HEADROOM_CYCLES} governed growth cycles; "
            f"found {headroom_cycles}"
        )
    expected = MAX_EXPORT_BYTES - (headroom_cycles * denominator)
    if denominator <= 0 or not 0 < expected < MAX_EXPORT_BYTES:
        raise ExportCheckError(
            "review-export attention boundary derivation must use a positive "
            "denominator and land strictly inside the ceiling"
        )
    if boundary != expected:
        raise ExportCheckError(
            f"review-export attention boundary {boundary} disagrees with "
            f"{MAX_EXPORT_BYTES} - ({headroom_cycles} * {denominator}) = "
            f"{expected}"
        )
    return ExportAttentionBoundary(headroom_cycles, denominator, boundary)


def export_attention_errors(
    export_bytes: int,
    boundary_bytes: int,
    measured: str,
) -> list[str]:
    errors: list[str] = []
    # Invariant R12 control site: review-export pre-failure attention boundary.
    if export_attention_fires(export_bytes, boundary_bytes):
        has_valid_date = any(
            valid_iso_date(raw) for raw in ISO_DATE_RE.findall(measured)
        )
        if (
            not has_valid_date
            or not has_substantive_trigger_fired_disposition(measured)
        ):
            errors.append(
                f"export size {export_bytes} meets or exceeds attention "
                f"boundary {boundary_bytes}; governed row requires a dated "
                "'trigger-fired disposition:' in measured-change or "
                "unheld-lever form"
            )
    return errors


def has_substantive_trigger_fired_disposition(measured: str) -> bool:
    """Require one later-testable measured-change or unheld-lever answer."""
    prefixes = TRIGGER_FIRED_DISPOSITION_PREFIX_RE.findall(measured)
    forms: list[tuple[str, re.Match[str]]] = [
        ("measured-change", match)
        for match in TRIGGER_MEASURED_CHANGE_DISPOSITION_RE.finditer(measured)
    ]
    forms.extend(
        ("unheld-lever", match)
        for match in TRIGGER_UNHELD_LEVER_DISPOSITION_RE.finditer(measured)
    )
    # Invariant R12 control site: governed trigger disposition substance.
    if len(prefixes) != 1 or len(forms) != 1:
        return False
    kind, match = forms[0]
    if kind == "measured-change":
        baseline = int(match.group(2))
        current = int(match.group(3))
        return baseline != current
    return True


def export_attention_fires(export_bytes: int, boundary_bytes: int) -> bool:
    """Return the single executable review-export attention predicate."""
    return export_bytes >= boundary_bytes


def tracked_repository_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ExportCheckError(
            f"git ls-files failed with exit {result.returncode}"
            f"{f': {detail}' if detail else ''}"
        )
    return {
        raw.decode(errors="strict")
        for raw in result.stdout.split(b"\0")
        if raw
    }


def required_paths_before_review_projection(root: Path) -> set[str]:
    """Derive the source set before mixed-use manifest projection."""
    tracked = tracked_repository_paths(root)
    retained_cycles = expected_retained_cycle_paths(root)
    excluded_cycles = tracked_cycle_paths(root) - retained_cycles
    excluded_raw_wire = derived_raw_wire_paths(root)
    excluded_prefixes = (
        derived_bulk_evidence_prefixes(root)
        | derived_structural_archive_prefixes(root)
    )
    excluded_by_prefix = {
        path
        for path in tracked
        if any(path.startswith(prefix) for prefix in excluded_prefixes)
    }
    return tracked - excluded_cycles - excluded_raw_wire - excluded_by_prefix


def derived_required_paths(root: Path) -> set[str]:
    """Derive review-critical paths without a hand-maintained path list."""
    sources = required_paths_before_review_projection(root)
    return sources - derived_review_manifest_paths(root)


def tracked_cycle_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "docs/cycles"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ExportCheckError(
            f"git ls-files for cycle documents failed with exit "
            f"{result.returncode}{f': {detail}' if detail else ''}"
        )
    return {
        path
        for raw in result.stdout.split(b"\0")
        if raw
        if (path := raw.decode(errors="strict"))
        if CYCLE_DOCUMENT_RE.fullmatch(path) is not None
    }


def exported_paths(export_path: Path) -> set[str]:
    try:
        text = export_path.read_text()
    except OSError as error:
        raise ExportCheckError(f"cannot read export {export_path}: {error}") from error
    paths = set(FILE_PATH_RE.findall(text))
    if not paths:
        raise ExportCheckError(
            f"{export_path}: no Repomix <file path=\"...\"> entries found"
        )
    return paths


def cycle_name_version(name: str) -> tuple[int, ...]:
    match = re.fullmatch(r"v([0-9]+(?:\.[0-9]+)*)", name)
    if match is None:
        raise ExportCheckError(f"invalid cycle name {name!r}")
    return tuple(int(part) for part in match.group(1).split("."))


def expected_retained_cycle_paths(root: Path) -> set[str]:
    root = root.resolve()
    try:
        identity = resolve_cycle(root)
    except CycleIdentityError as error:
        raise ExportCheckError(str(error)) from error
    active_version = cycle_name_version(identity.name)
    tracked_cycles = tracked_cycle_paths(root)
    candidates = sorted(
        (
            version,
            root / raw_path,
        )
        for raw_path in tracked_cycles
        if EXECUTION_RUNBOOK_PATH_RE.fullmatch(raw_path) is not None
        if (
            (version := cycle_name_version(
                EXECUTION_RUNBOOK_PATH_RE.fullmatch(raw_path).group(1)
            ))
            <= active_version
        )
    )
    if (
        len(candidates) < CYCLE_RETENTION_DEPTH
        or candidates[-1][1].resolve() != identity.runbook.resolve()
    ):
        raise ExportCheckError(
            f"cannot derive {CYCLE_RETENTION_DEPTH}-cycle retention set "
            f"ending at {identity.name}"
        )
    expected: set[str] = set()
    for _, runbook in candidates[-CYCLE_RETENTION_DEPTH:]:
        progress = progress_for_runbook(root, runbook)
        if progress is None:
            raise ExportCheckError(
                f"no progress record resolves for {runbook.relative_to(root)}"
            )
        runbook_path = runbook.relative_to(root).as_posix()
        progress_path = progress.relative_to(root).as_posix()
        if progress_path not in tracked_cycles:
            raise ExportCheckError(
                f"retained progress record is not tracked: {progress_path}"
            )
        expected.add(runbook_path)
        expected.add(progress_path)
    return expected


def repomix_custom_patterns(root: Path) -> tuple[str, ...]:
    root = root.resolve()
    config_path = root / "repomix.config.json"
    try:
        config = json.loads(config_path.read_text())
        patterns = config["ignore"]["customPatterns"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise ExportCheckError(
            f"cannot read Repomix exclusions from {config_path}: {error}"
        ) from error
    if not isinstance(patterns, list) or not all(
        isinstance(pattern, str) for pattern in patterns
    ):
        raise ExportCheckError("Repomix customPatterns must be a string list")
    return tuple(patterns)


def pinned_file_records(root: Path) -> tuple[dict[str, object], ...]:
    manifest_path = root / "config/protected-artifacts.json"
    try:
        raw = json.loads(manifest_path.read_text())
        records = raw["pinned_files"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise ExportCheckError(
            f"cannot read pinned-file records from {manifest_path}: {error}"
        ) from error
    if not isinstance(records, list) or not all(
        isinstance(record, dict) for record in records
    ):
        raise ExportCheckError("protected pinned_files must be an object list")
    return tuple(records)


def review_projection_staleness_errors(
    expected_text: str,
    actual_text: str,
) -> list[str]:
    # Invariant R12 control site: review-source projection staleness.
    if actual_text != expected_text:
        return ["review-source projection is stale against its manifest"]
    return []


def _projection_object(
    root: Path,
    source_path: str,
    visible_paths: set[str],
) -> tuple[dict[str, object], int, int]:
    source = root / source_path
    try:
        raw = json.loads(source.read_text())
        pins = raw["pinned_files"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise ExportCheckError(
            f"cannot derive review projection from {source_path}: {error}"
        ) from error
    if not isinstance(raw, dict) or not isinstance(pins, list) or not pins:
        raise ExportCheckError(
            f"review projection source {source_path} requires a nonempty "
            "pinned_files object list"
        )
    pin_paths: list[str] = []
    for record in pins:
        if not isinstance(record, dict) or not isinstance(
            record.get("path"), str
        ):
            raise ExportCheckError(
                f"review projection source {source_path} has a pin without a path"
            )
        pin_paths.append(record["path"])
    retained = [
        record
        for record, path in zip(pins, pin_paths, strict=True)
        if path in visible_paths and path != source_path
    ]
    if not retained or len(retained) == len(pins):
        raise ExportCheckError(
            f"review projection source {source_path} must have both visible "
            "and non-visible pinned paths"
        )
    projection = dict(raw)
    projection["pinned_files"] = retained
    return projection, len(pins), len(retained)


def render_review_projection(
    root: Path,
    source_path: str,
) -> str:
    visible = required_paths_before_review_projection(root.resolve())
    projection, _, _ = _projection_object(root.resolve(), source_path, visible)
    encoded = json.dumps(projection, ensure_ascii=False, indent=2)
    return (
        f'<!-- REVIEW_SOURCE_PROJECTION:START source="{source_path}" -->\n'
        "```json\n"
        f"{encoded}\n"
        "```\n"
        "<!-- REVIEW_SOURCE_PROJECTION:END -->"
    )


def review_projection_records(root: Path) -> tuple[ReviewProjectionRecord, ...]:
    root = root.resolve()
    records: list[ReviewProjectionRecord] = []
    for host_path in sorted(tracked_repository_paths(root)):
        if not host_path.endswith(".md"):
            continue
        try:
            text = (root / host_path).read_text()
        except OSError as error:
            raise ExportCheckError(
                f"cannot inspect review projection host {host_path}: {error}"
            ) from error
        starts = text.count("<!-- REVIEW_SOURCE_PROJECTION:START")
        ends = text.count("<!-- REVIEW_SOURCE_PROJECTION:END -->")
        matches = list(REVIEW_SOURCE_PROJECTION_RE.finditer(text))
        if starts != len(matches) or ends != len(matches):
            raise ExportCheckError(
                f"review projection markers are malformed in {host_path}"
            )
        records.extend(
            ReviewProjectionRecord(host_path, match.group(1), match.group(2))
            for match in matches
        )
    return tuple(records)


def derived_review_manifest_paths(root: Path) -> set[str]:
    """Derive mixed-use manifest exclusions from tracked exact projections."""
    root = root.resolve()
    tracked = tracked_repository_paths(root)
    visible = required_paths_before_review_projection(root)
    derived: set[str] = set()
    for record in review_projection_records(root):
        if record.host_path not in visible:
            raise ExportCheckError(
                f"review projection host is not review-visible: {record.host_path}"
            )
        if record.source_path not in tracked or record.source_path in derived:
            raise ExportCheckError(
                f"review projection source must be unique and tracked: "
                f"{record.source_path}"
            )
        expected, _, _ = _projection_object(
            root, record.source_path, visible
        )
        expected_text = json.dumps(expected, ensure_ascii=False, indent=2)
        staleness = review_projection_staleness_errors(
            expected_text, record.projection_text
        )
        if staleness:
            raise ExportCheckError(
                f"{record.host_path}: {staleness[0]} {record.source_path}"
            )
        derived.add(record.source_path)
    return derived


def _is_pinned_manifest(path: Path) -> bool:
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return False
    return (
        isinstance(raw, dict)
        and isinstance(raw.get("pinned_files"), list)
        and bool(raw["pinned_files"])
    )


def configured_review_manifest_exclusions(root: Path) -> set[str]:
    root = root.resolve()
    configured: set[str] = set()
    for raw_path in repomix_custom_patterns(root):
        if any(character in raw_path for character in GLOB_META):
            continue
        path = root / raw_path
        if path.is_file() and _is_pinned_manifest(path):
            configured.add(raw_path)
    return configured


def review_manifest_exclusion_errors(
    derived: set[str],
    configured: set[str],
) -> list[str]:
    errors: list[str] = []
    # Invariant R12 control site: derived review-manifest exclusion population.
    if len(derived) == 0:
        errors.append("derived review-manifest exclusion class is empty")
    # Invariant R12 control site: every derived review manifest is excluded.
    errors.extend(
        f"derived review manifest lacks an exact Repomix exclusion: {path}"
        for path in sorted(derived.difference(configured))
    )
    # Invariant R12 control site: every exact review-manifest exclusion is derived.
    errors.extend(
        f"exact Repomix review-manifest exclusion is not derived: {path}"
        for path in sorted(configured.difference(derived))
    )
    return errors


def excluded_review_manifest_paths(root: Path) -> set[str]:
    derived = derived_review_manifest_paths(root)
    configured = configured_review_manifest_exclusions(root)
    errors = review_manifest_exclusion_errors(derived, configured)
    if errors:
        raise ExportCheckError("; ".join(errors))
    return derived


def review_projection_population(root: Path) -> ReviewProjectionPopulation:
    root = root.resolve()
    visible = required_paths_before_review_projection(root)
    records = review_projection_records(root)
    total = 0
    retained = 0
    for record in records:
        _, source_total, source_retained = _projection_object(
            root, record.source_path, visible
        )
        total += source_total
        retained += source_retained
    return ReviewProjectionPopulation(
        len(records), total, retained, total - retained
    )


def derived_raw_wire_paths(root: Path) -> set[str]:
    """Derive pinned raw publisher bodies from their byte-preservation marks."""
    root = root.resolve()
    candidates = sorted(
        path
        for record in pinned_file_records(root)
        if record.get("grade") == "observation"
        if isinstance(path := record.get("path"), str)
        if path.startswith("observations/")
    )
    if not candidates:
        return set()
    result = subprocess.run(
        ["git", "check-attr", "-z", "binary", "--", *candidates],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.decode(errors="replace").strip()
        raise ExportCheckError(
            f"git check-attr failed with exit {result.returncode}"
            f"{f': {detail}' if detail else ''}"
        )
    fields = result.stdout.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 3 != 0:
        raise ExportCheckError("git check-attr returned malformed binary records")
    derived: set[str] = set()
    for index in range(0, len(fields), 3):
        path, attribute, value = (
            field.decode(errors="strict") for field in fields[index : index + 3]
        )
        if attribute != "binary":
            raise ExportCheckError(
                f"git check-attr returned unexpected attribute {attribute!r}"
            )
        if value == "set":
            derived.add(path)
    return derived


def configured_raw_wire_exclusions(root: Path) -> set[str]:
    configured: set[str] = set()
    for raw_path in repomix_custom_patterns(root):
        if not raw_path.startswith("observations/"):
            continue
        if any(character in raw_path for character in GLOB_META):
            continue
        if not (root / raw_path).is_file():
            raise ExportCheckError(
                f"invalid exact Repomix observation exclusion: {raw_path}"
            )
        configured.add(raw_path)
    return configured


def raw_wire_exclusion_errors(
    derived: set[str],
    configured: set[str],
) -> list[str]:
    errors: list[str] = []
    # Invariant R12 control site: derived raw-wire exclusion population.
    if not derived:
        errors.append("derived raw-wire exclusion class is empty")
    # Invariant R12 control site: every derived raw-wire body is excluded.
    errors.extend(
        f"derived raw-wire body lacks an exact Repomix exclusion: {path}"
        for path in sorted(derived - configured)
    )
    # Invariant R12 control site: every exact observation exclusion is raw wire.
    errors.extend(
        f"exact Repomix observation exclusion is not derived raw wire: {path}"
        for path in sorted(configured - derived)
    )
    return errors


def excluded_export_paths(root: Path) -> set[str]:
    derived = derived_raw_wire_paths(root)
    configured = configured_raw_wire_exclusions(root)
    errors = raw_wire_exclusion_errors(derived, configured)
    if errors:
        raise ExportCheckError("; ".join(errors))
    return derived | excluded_review_manifest_paths(root)


def derived_structural_archive_prefixes(root: Path) -> set[str]:
    return {
        f"{Path(path).parent.as_posix()}/"
        for record in pinned_file_records(root)
        if record.get("grade") == "structural"
        if isinstance(path := record.get("path"), str)
        if not path.startswith("evidence/")
    }


def derived_bulk_evidence_prefixes(root: Path) -> set[str]:
    patterns = set(repomix_custom_patterns(root))
    prefixes: set[str] = set()
    for record in pinned_file_records(root):
        path = record.get("path")
        if not isinstance(path, str) or "/" not in path:
            continue
        prefix = f"{path.split('/', 1)[0]}/"
        if f"{prefix}**" in patterns:
            prefixes.add(prefix)
    return prefixes


def configured_structural_archive_prefixes(root: Path) -> set[str]:
    patterns = set(repomix_custom_patterns(root))
    expected = derived_structural_archive_prefixes(root)
    configured = {
        prefix
        for prefix in expected
        if f"{prefix}**" in patterns
    }
    if configured != expected:
        missing = ", ".join(sorted(expected - configured))
        raise ExportCheckError(
            f"missing derived structural-archive Repomix exclusion: {missing}"
        )
    return configured


def untracked_export_errors(
    tracked: set[str],
    actual: set[str],
) -> list[str]:
    # Invariant R12 control site: review export contains only Git-tracked bytes.
    return [
        f"export contains untracked path: {path}"
        for path in sorted(actual - tracked)
    ]


def check_export(
    root: Path,
    export_path: Path,
) -> tuple[set[str], set[str], list[str]]:
    root = root.resolve()
    export_path = export_path.resolve()
    tracked = tracked_repository_paths(root)
    sources = derived_required_paths(root)
    actual = exported_paths(export_path)
    expected_cycles = expected_retained_cycle_paths(root)
    excluded_paths = excluded_export_paths(root)
    actual_cycles = {
        path for path in actual if CYCLE_DOCUMENT_RE.fullmatch(path) is not None
    }
    errors = [
        f"missing derived required path: {path}"
        for path in sorted(sources - actual)
    ]
    errors.extend(untracked_export_errors(tracked, actual))
    export_bytes = export_path.stat().st_size
    attention = export_attention_boundary(root)
    measured = governed_export_measured_cell(root)
    errors.extend(
        export_attention_errors(export_bytes, attention.boundary_bytes, measured)
    )
    if export_bytes > MAX_EXPORT_BYTES:
        errors.append(
            f"export size {export_bytes} exceeds ceiling {MAX_EXPORT_BYTES}"
        )
    errors.extend(
        f"missing retained cycle document: {path}"
        for path in sorted(expected_cycles - actual_cycles)
    )
    errors.extend(
        f"unexpected cycle document outside retention depth "
        f"{CYCLE_RETENTION_DEPTH}: {path}"
        for path in sorted(actual_cycles - expected_cycles)
    )
    errors.extend(
        f"excluded export path is present: {path}"
        for path in sorted(excluded_paths)
        if path in actual
    )
    archive_prefixes = configured_structural_archive_prefixes(root)
    errors.extend(
        f"excluded export prefix is present: {prefix}"
        for prefix in archive_prefixes
        if any(path.startswith(prefix) for path in actual)
    )
    return sources, actual, errors


def run(root: Path, export_path: Path) -> int:
    try:
        sources, actual, errors = check_export(root, export_path)
        attention = export_attention_boundary(root)
        projection = review_projection_population(root)
    except ExportCheckError as error:
        print(f"export-check: ERROR: {error}", file=sys.stderr)
        print("export-check: FAIL (inspection unavailable)", file=sys.stderr)
        return 2
    for error in errors:
        print(f"export-check: ERROR: {error}", file=sys.stderr)
    if errors:
        print(
            f"export-check: FAIL ({len(errors)} defect(s); "
            f"derived_required={len(sources)}, exported={len(actual)})",
            file=sys.stderr,
        )
        return 1
    attention_state = (
        "trigger-fired-disposed"
        if export_path.stat().st_size >= attention.boundary_bytes
        else "clear"
    )
    print(
        "export-check: PASS "
        f"(derived_required={len(sources)}, "
        f"exported={len(actual)}, bytes={export_path.stat().st_size}, "
        f"retained_cycles={CYCLE_RETENTION_DEPTH}, "
        f"review_manifests={projection.manifests}, "
        f"review_pins={projection.retained_pins}/{projection.total_pins}, "
        f"attention_boundary={attention.boundary_bytes}, "
        f"attention_state={attention_state})"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check a freshly written Repomix export against Git paths."
    )
    parser.add_argument("export", type=Path)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root used for git ls-files (default: this checkout)",
    )
    args = parser.parse_args()
    return run(args.root.resolve(), args.export.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
