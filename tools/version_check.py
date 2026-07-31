#!/usr/bin/env python3
"""Bind release identity and the executable offline Rust floor."""

from __future__ import annotations

import ast
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parents[1]
CARGO_TOML = ROOT / "apps/cored/Cargo.toml"
PYTHON_INIT = ROOT / "shell/intel_shell/__init__.py"
FASTAPI_APP = ROOT / "shell/intel_shell/app.py"
STATE = ROOT / "STATE.md"
CHANGELOG = ROOT / "CHANGELOG.md"
TAG_SOURCE = "git describe --tags --abbrev=0"
RUST_VERSION = r"[0-9]+(?:\.[0-9]+){1,2}"


class RustVersionSpec(NamedTuple):
    path: str
    label: str
    pattern: re.Pattern[str]
    kind: str


class ExtractedRustVersion(NamedTuple):
    path: str
    label: str
    raw: str
    normalized: str


class OfflineMsrvReport(NamedTuple):
    derived: str
    pins: tuple[ExtractedRustVersion, ...]
    restatements: tuple[ExtractedRustVersion, ...]


OFFLINE_MSRV_AUTHORITIES = (
    RustVersionSpec(
        "run",
        "offline MSRV rustup commands",
        re.compile(
            rf'(?m)^\s*RUSTFLAGS="" rustup run '
            rf"(?P<version>{RUST_VERSION}) cargo (?:check|test) "
            r"--workspace --locked\s*$"
        ),
        "executable pins",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "offline MSRV job toolchain",
        re.compile(
            rf"(?ms)^  msrv:\n"
            rf"(?:(?!^  [A-Za-z0-9_-]+:\s*$).)*?"
            rf"^[ \t]+toolchain:\s*[\"']?(?P<version>{RUST_VERSION})"
            r"[\"']?\s*$"
        ),
        "executable pins",
    ),
)

# Semantics cannot identify present-tense prose reliably. This named registry
# is the permanent, hand-maintained current-restatement obligation. Dated
# history is deliberately outside it and is listed separately below.
OFFLINE_MSRV_RESTATEMENTS = (
    RustVersionSpec(
        "run",
        "missing-cargo diagnostic",
        re.compile(
            rf"offline build needs >= (?P<version>{RUST_VERSION}); "
            r"--features net needs"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "run",
        "ci-local locked-check label",
        re.compile(
            rf"(?m)^Rust (?P<version>{RUST_VERSION}) locked check"
            r"\|ci_msrv_check$"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "run",
        "ci-local locked-test label",
        re.compile(
            rf"(?m)^Rust (?P<version>{RUST_VERSION}) locked test"
            r"\|ci_msrv_test$"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "run",
        "offline usage heading",
        re.compile(
            rf"Offline \(needs only Rust >= (?P<version>{RUST_VERSION}) "
            r"\+ Python"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "offline-job heading",
        re.compile(
            rf"offline path: everything except live fetching\. MSRV floor is "
            rf"(?P<version>{RUST_VERSION})"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "lint compatibility comment",
        re.compile(
            rf"offline MSRV floor above the declared "
            rf"(?P<version>{RUST_VERSION})"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "MSRV rationale heading",
        re.compile(
            rf"MSRV floor for the OFFLINE build is \*\*"
            rf"(?P<version>{RUST_VERSION})\*\*"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "sustainable-floor conclusion",
        re.compile(
            rf"actually true and actually sustainable: \*\*"
            rf"(?P<version>{RUST_VERSION})\*\*"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "MSRV job label",
        re.compile(
            rf"name: MSRV floor \(offline builds on "
            rf"(?P<version>{RUST_VERSION})\)"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "MSRV cargo-check step label",
        re.compile(
            rf"name: cargo check --workspace --locked "
            rf"\((?P<version>{RUST_VERSION})\)"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        ".github/workflows/ci.yml",
        "MSRV cargo-test step label",
        re.compile(
            rf"name: cargo test --workspace --locked "
            rf"\((?P<version>{RUST_VERSION})\)"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "rust-toolchain.toml",
        "offline/default declaration",
        re.compile(
            rf"offline / default build : needs >= "
            rf"(?P<version>{RUST_VERSION})"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "rust-toolchain.toml",
        "lockfile-floor declaration",
        re.compile(
            rf"The offline floor is (?P<version>{RUST_VERSION}) because"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "rust-toolchain.toml",
        "CI enforcement declaration",
        re.compile(
            rf"CI's `msrv` job enforces the "
            rf"(?P<version>{RUST_VERSION}) floor"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "README.md",
        "offline toolchain table",
        re.compile(
            rf"default / offline \(fixtures\) \| rustc \*\*"
            rf"(?P<version>{RUST_VERSION})\+\*\*"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "AGENTS.md",
        "dependency-gate floor",
        re.compile(
            rf"offline build must stay ≥ (?P<version>{RUST_VERSION})"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "AGENTS.md",
        "offline build-command heading",
        re.compile(
            rf"# offline path \(MSRV floor "
            rf"(?P<version>{RUST_VERSION})\)"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "crates/compliance/src/lib.rs",
        "compliance compatibility comment",
        re.compile(
            rf"This crate's floor is (?P<version>{RUST_VERSION}) "
            r"\(STATE §5"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "crates/ingest/src/arxiv_oai.rs",
        "ingest compatibility comment",
        re.compile(
            rf"This crate's floor is (?P<version>{RUST_VERSION}) "
            r"\(STATE §5"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "crates/store/examples/cosine_bench.rs",
        "store benchmark compatibility comment",
        re.compile(
            rf"offline Rust (?P<version>{RUST_VERSION}) floor"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "crates/compliance/Cargo.toml",
        "rejected-dependency baseline",
        re.compile(
            rf"raised the OFFLINE build floor from "
            rf"(?P<version>{RUST_VERSION})"
        ),
        "current restatements",
    ),
    RustVersionSpec(
        "STATE.md",
        "current run-reference correction",
        re.compile(
            rf"current correction: offline needs >= "
            rf"(?P<version>{RUST_VERSION})"
        ),
        "current restatements",
    ),
)

OFFLINE_MSRV_HISTORICAL_EXCLUSIONS = (
    "docs/cycles/**",
    "docs/state-archive/**",
    "CHANGELOG.md",
    "evidence/** and observations/**",
    "dated narrative in STATE.md outside the current run-reference correction",
    "historical clauses inside current AGENTS.md, README.md, "
    "rust-toolchain.toml, and workflow commentary",
)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def normalized_rust_version(raw: str) -> str:
    match = re.fullmatch(RUST_VERSION, raw)
    if match is None:
        raise ValueError(f"invalid Rust version {raw!r}")
    parts = [int(part) for part in raw.split(".")]
    if len(parts) == 3 and parts[-1] == 0:
        parts.pop()
    return ".".join(str(part) for part in parts)


def _spec_text(
    root: Path,
    spec: RustVersionSpec,
    text_overrides: dict[str, str],
) -> str:
    if spec.path in text_overrides:
        return text_overrides[spec.path]
    return (root / spec.path).read_text()


def _extract_rust_versions(
    root: Path,
    spec: RustVersionSpec,
    text_overrides: dict[str, str],
) -> tuple[ExtractedRustVersion, ...]:
    text = _spec_text(root, spec, text_overrides)
    matches = list(spec.pattern.finditer(text))
    if not matches:
        raise ValueError(
            f"{spec.path}: {spec.label} yielded zero extracted {spec.kind}"
        )
    return tuple(
        ExtractedRustVersion(
            path=spec.path,
            label=spec.label,
            raw=match.group("version"),
            normalized=normalized_rust_version(match.group("version")),
        )
        for match in matches
    )


def offline_msrv_report(
    root: Path = ROOT,
    *,
    text_overrides: dict[str, str] | None = None,
) -> OfflineMsrvReport:
    overrides = {} if text_overrides is None else text_overrides
    pins = tuple(
        version
        for spec in OFFLINE_MSRV_AUTHORITIES
        for version in _extract_rust_versions(root, spec, overrides)
    )
    normalized_pins = {pin.normalized for pin in pins}
    if len(normalized_pins) != 1:
        detail = ", ".join(
            f"{pin.path} {pin.raw}->{pin.normalized}" for pin in pins
        )
        raise ValueError(
            "offline MSRV executable pins disagree after normalization: "
            f"{detail}"
        )
    derived = next(iter(normalized_pins))

    restatements = tuple(
        version
        for spec in OFFLINE_MSRV_RESTATEMENTS
        for version in _extract_rust_versions(root, spec, overrides)
    )
    # Invariant R12 control site: offline MSRV restatement binding.
    for restatement in restatements:
        if restatement.normalized != derived:
            raise ValueError(
                f"{restatement.path}: {restatement.label} states "
                f"{restatement.raw}->{restatement.normalized}, but executable "
                f"offline MSRV pins derive {derived}"
            )
    return OfflineMsrvReport(derived, pins, restatements)


def literal_string(node: ast.AST, path: Path, label: str) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    raise ValueError(f"{relative(path)}: {label} must be a string literal")


def python_package_version() -> str:
    tree = ast.parse(PYTHON_INIT.read_text(), filename=str(PYTHON_INIT))
    values = [
        literal_string(node.value, PYTHON_INIT, "__version__")
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "__version__"
            for target in node.targets
        )
    ]
    if len(values) != 1:
        raise ValueError(
            f"{relative(PYTHON_INIT)}: expected exactly one __version__, "
            f"found {len(values)}"
        )
    return values[0]


def fastapi_version() -> str:
    tree = ast.parse(FASTAPI_APP.read_text(), filename=str(FASTAPI_APP))
    values: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "FastAPI":
            continue
        for keyword in node.keywords:
            if keyword.arg == "version":
                values.append(
                    literal_string(keyword.value, FASTAPI_APP, "FastAPI version=")
                )
    if len(values) != 1:
        raise ValueError(
            f"{relative(FASTAPI_APP)}: expected exactly one FastAPI version=, "
            f"found {len(values)}"
        )
    return values[0]


def state_version() -> str:
    matches = re.findall(
        r"^\*\*As of:\*\* [^\n]*? · \*\*Version:\*\* v([0-9]+\.[0-9]+\.[0-9]+) "
        r"\(core-shell\)",
        STATE.read_text(),
        flags=re.MULTILINE,
    )
    if len(matches) != 1:
        raise ValueError(
            f"{relative(STATE)}: expected exactly one versioned As-of header, "
            f"found {len(matches)}"
        )
    return matches[0]


def changelog_version() -> str:
    matches = re.findall(
        r"^## v([0-9]+\.[0-9]+\.[0-9]+)(?:\s|$)",
        CHANGELOG.read_text(),
        flags=re.MULTILINE,
    )
    if not matches:
        raise ValueError(
            f"{relative(CHANGELOG)}: expected at least one ## vX.Y.Z heading"
        )
    return matches[0]


def git_output(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def nearest_tag() -> tuple[str, bool] | None:
    described = git_output("describe", "--tags", "--abbrev=0")
    if described.returncode != 0:
        detail = described.stderr.strip() or "no reachable tag"
        print(f"version-check: WARNING: {TAG_SOURCE} unavailable: {detail}")
        return None

    tag = described.stdout.strip()
    match = re.fullmatch(r"v([0-9]+\.[0-9]+\.[0-9]+)", tag)
    if match is None:
        raise ValueError(f"{TAG_SOURCE}: expected vX.Y.Z, found {tag!r}")

    exact = git_output("describe", "--tags", "--exact-match", "HEAD")
    return match.group(1), exact.returncode == 0 and exact.stdout.strip() == tag


def main() -> int:
    try:
        msrv = offline_msrv_report()
        cargo_data = tomllib.loads(CARGO_TOML.read_text())
        versions = {
            relative(CARGO_TOML): cargo_data["package"]["version"],
            relative(PYTHON_INIT): python_package_version(),
            relative(FASTAPI_APP): fastapi_version(),
            relative(STATE): state_version(),
            relative(CHANGELOG): changelog_version(),
        }
        tag = nearest_tag()
    except (KeyError, OSError, SyntaxError, tomllib.TOMLDecodeError, ValueError) as error:
        print(f"version-check: ERROR: {error}", file=sys.stderr)
        return 1

    for path, version in versions.items():
        print(f"{path}: {version}")
    raw_pin_forms = ", ".join(sorted({pin.raw for pin in msrv.pins}))
    print(
        f"offline MSRV authorities: pins={len(msrv.pins)}, "
        f"raw=[{raw_pin_forms}], normalized={msrv.derived}"
    )
    print(
        "offline MSRV current restatements: "
        f"{len(msrv.restatements)} all derive {msrv.derived}; "
        "registry=OFFLINE_MSRV_RESTATEMENTS"
    )

    canonical_path = relative(CARGO_TOML)
    canonical_version = versions[canonical_path]
    mismatches = [
        (path, version)
        for path, version in versions.items()
        if version != canonical_version
    ]
    if mismatches:
        print(
            f"version-check: ERROR: expected {canonical_version} "
            f"from {canonical_path}; disagreeing file(s):",
            file=sys.stderr,
        )
        for path, version in mismatches:
            print(f"  {path}: {version}", file=sys.stderr)
        return 1

    if tag is not None:
        tag_version, exact = tag
        state = "exact HEAD tag" if exact else "nearest ancestor; HEAD is ahead"
        print(f"{TAG_SOURCE}: {tag_version} ({state})")
        if exact and tag_version != canonical_version:
            print(
                f"version-check: ERROR: exact HEAD tag is {tag_version}, "
                f"but {canonical_path} is {canonical_version}",
                file=sys.stderr,
            )
            return 1
        if not exact:
            if tag_version == canonical_version:
                detail = f"version remains {canonical_version}"
            else:
                detail = (
                    f"tag is {tag_version}; working tree version is "
                    f"{canonical_version}"
                )
            print(f"version-check: WARNING: HEAD is ahead of its tag; {detail}")

    print(f"version-check: PASS ({canonical_version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
