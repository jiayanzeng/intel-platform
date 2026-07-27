#!/usr/bin/env python3
"""Static repository invariant checks.

R1 deliberately scans production Rust outside ``crates/store/src/sqlite.rs``.
The store implementation and its ``#[cfg(test)]`` module are out of scope:
boundary/differential tests may name alternate numeric distances, while no
production caller outside the store may call ``assign_canonical_ids`` at all.
Rust files under a ``tests`` directory and text after the conventional
``#[cfg(test)] mod tests`` boundary are classified as test-only.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STORE = Path("crates/store/src/sqlite.rs")
ASSIGN_CALL = re.compile(r"\bassign_canonical_ids\s*\(")
TEST_MODULE = re.compile(r"(?m)^#\[cfg\(test\)\]\s*\nmod\s+tests\s*\{")


def production_text(path: Path, text: str) -> str:
    """Return the production portion covered by R1."""
    if "tests" in path.parts:
        return ""
    boundary = TEST_MODULE.search(text)
    return text if boundary is None else text[: boundary.start()]


def rust_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.rs")
        if ".git" not in path.parts and "target" not in path.parts
    )


def r1_findings(root: Path) -> list[str]:
    findings: list[str] = []
    store = (root / STORE).resolve()
    for path in rust_files(root):
        if path.resolve() == store:
            continue
        text = production_text(path.relative_to(root), path.read_text())
        for match in ASSIGN_CALL.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append(
                f"{path.relative_to(root)}:{line}: "
                "production assign_canonical_ids call outside the store"
            )
    return findings


def run(root: Path) -> int:
    findings = r1_findings(root.resolve())
    if findings:
        for finding in findings:
            print(f"invariant-scan: R1 FAIL: {finding}")
        return 1
    print(
        "invariant-scan: R1 PASS "
        "(no production assign_canonical_ids call outside the store)"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    return run(args.root)


if __name__ == "__main__":
    raise SystemExit(main())
