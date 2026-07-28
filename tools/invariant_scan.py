#!/usr/bin/env python3
"""Execute registered static repository invariants.

The scanner reads source, config, and Git worktree text only. It never loads a
built binary, opens an archive, or touches the network.

R1 enumerates the five production store callers that rematerialize canonical
identity and rejects every other production call to that helper. Boundary and
differential tests may name alternate numeric distances, so test-only Rust is
excluded. Rust files under a ``tests`` directory, text after the conventional
``#[cfg(test)] mod tests`` boundary, and individually ``#[cfg(test)]``-gated
items are classified as test-only.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import tomllib
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
RULES_FILE = Path("config/invariant-rules.json")
STORE = Path("crates/store/src/sqlite.rs")
CORE_MAIN = Path("apps/cored/src/main.rs")
AUTHORITY_FILES = (
    Path("AGENTS.md"),
    Path("intel-platform-OPERATIONS.md"),
)
AUTHORITY_START = "<!-- MODEL_PROFILE_AUTHORITY:START -->"
AUTHORITY_END = "<!-- MODEL_PROFILE_AUTHORITY:END -->"
TEST_MODULE = re.compile(r"(?m)^#\[cfg\(test\)\]\s*\nmod\s+tests\s*\{")
TCP_BIND = re.compile(r"\b(?:tokio::net::)?TcpListener::bind\s*\(")
CRAWLER_IDENTITY_CONSTRUCTION = re.compile(r"\bbuild_robots_cache\s*\(")
ROBOTS_CACHE_BINDING = re.compile(r"(?m)^[ \t]*let[ \t]+robots_cache[ \t]*=")
TOML_TABLE = re.compile(r"^[ \t]*\[([^\]]+)\][ \t]*(?:#.*)?$")
TEST_SUPPORT = re.compile(r"(?<![A-Za-z0-9_-])test-support(?![A-Za-z0-9_-])")
TEST_SUPPORT_FEATURE_DEFINITION = re.compile(
    r"^[ \t]*[\"']?test-support[\"']?[ \t]*="
)
RUST_FUNCTION = re.compile(
    r"(?m)^[ \t]*(?:pub(?:\([^)]*\))?[ \t]+)?"
    r"(?:async[ \t]+)?fn[ \t]+(?P<name>[A-Za-z_][A-Za-z0-9_]*)[ \t]*(?:<|\()"
)
LLM_MARKERS = (
    (
        "LLM client import",
        re.compile(
            r"(?mi)^\s*use\s+[^\n;]*(?:openai|anthropic|llm)[^\n;]*;"
        ),
    ),
    (
        "LLM/provider base-URL constant",
        re.compile(
            r"(?mi)^\s*(?:pub(?:\([^)]*\))?\s+)?(?:const|static)\s+"
            r"[A-Z0-9_]*(?:LLM|OPENAI|ANTHROPIC)[A-Z0-9_]*"
        ),
    ),
    (
        "LLM provider call",
        re.compile(
            r"(?i)api\.openai\.com|/v1/(?:chat/)?completions|"
            r"/v1/responses|\.chat_completions\s*\(|\.responses\s*\("
        ),
    ),
)
THRESHOLD_DECL = re.compile(
    r"(?m)^\s*(?:pub(?:\([^)]*\))?\s+)?const\s+"
    r"([A-Z0-9_]*(?:DEDUP|CANONICAL)[A-Z0-9_]*"
    r"(?:DISTANCE|THRESHOLD)[A-Z0-9_]*)\s*:\s*u32\s*=\s*(\d+)"
)
CANONICAL_DISTANCE_CALL = re.compile(
    r"\b(?P<name>assign_canonical_ids(?:_tx)?|"
    r"rematerialize_canonical_ids_with_distance)\s*\("
)
CANONICAL_IDENTITY_CALLERS = {
    "append_new",
    "update_document",
    "delete_document",
    "rematerialize_canonical_ids",
    "commit_harvest_page",
}
DOCUMENT_ID_HYDRATION_CALL = re.compile(
    r"(?:\.|::)\s*(?P<name>documents_by_ids(?:_in_sectors)?)\s*\("
)
PUBLIC_UNSCOPED_HYDRATION = re.compile(
    r"(?m)^[ \t]*pub(?:\([^)]*\))?[ \t]+fn[ \t]+documents_by_ids[ \t]*\("
)
PRIVATE_KEY_HEADER = re.compile(
    r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"
)
PROVIDER_KEY = re.compile(
    r"\b(?:"
    r"sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}|"
    r"AKIA[0-9A-Z]{16}|"
    r"gh[opsu]_[A-Za-z0-9]{20,}|"
    r"xox[baprs]-[A-Za-z0-9-]{10,}|"
    r"AIza[0-9A-Za-z_-]{35}"
    r")\b"
)
AUTHORIZATION_VALUE = re.compile(
    r"(?i)\bAuthorization[\"']?\s*[:=]\s*[\"']?\s*"
    r"Bearer\s+([A-Za-z0-9._~+/\-=]{24,})"
)
SECRET_ASSIGNMENT = re.compile(
    r"(?m)^\s*(?:export\s+)?"
    r"[A-Z][A-Z0-9_]*(?:API_KEY|TOKEN|SECRET|PASSWORD)"
    r"[ \t]*=[ \t]*([^\s#]+)"
)
RAW_SECRET_FIELD = re.compile(
    r"(?i)[\"'](?:api_key|access_token|refresh_token|client_secret|password)"
    r"[\"']\s*:\s*[\"']([^\"']{20,})[\"']"
)
SECRET_PLACEHOLDERS = {
    "...",
    "…",
    "change-me",
    "replace-me",
    "replace-with-your-key",
}


class ConfigError(ValueError):
    """The rule registry cannot support the claim it declares."""


@dataclass(frozen=True)
class FailBefore:
    file: str
    find: str
    replace_with: tuple[str, ...]
    expected_fail: str
    expected_file: str
    expected_line: int


@dataclass(frozen=True)
class Rule:
    id: str
    claim: str
    source: str
    scope: str
    fail_before: tuple[FailBefore, ...]
    fail_before_note: str


@dataclass(frozen=True)
class WorkflowStep:
    job: str
    name: str
    line: int
    run_line: int | None
    run: str | None
    uses: str | None


@dataclass(frozen=True)
class WorkflowJob:
    id: str
    line: int
    report_only: bool
    matrix: tuple[tuple[str, tuple[str, ...]], ...]
    steps: tuple[WorkflowStep, ...]


@dataclass(frozen=True)
class CheckSite:
    id: str
    file: str
    line: int
    label: str


@dataclass(frozen=True)
class ParityReport:
    findings: tuple[str, ...]
    local_jobs: int
    local_checks: int
    blocking_jobs: int
    hosted_checks: int
    exemptions: tuple[str, ...]


JOB_HEADER = re.compile(r"^  (?P<id>[A-Za-z0-9_-]+):\s*$")
STEP_HEADER = re.compile(
    r"^      - (?P<field>name|uses):\s*(?P<value>.+?)\s*$"
)
FUNCTION_HEADER = re.compile(
    r"(?m)^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\(\)\s*\{\s*$"
)
CI_LOCAL_INVOCATION = re.compile(
    r'(?m)^(?P<indent>\s*)ci_local_job\s+"(?P<label>[^"]+)"\s+'
    r"(?P<target>[A-Za-z_][A-Za-z0-9_]*)\s+\|\|\s+return\s+\$\?\s*$"
)
RUN_DISPATCH = re.compile(
    r"(?m)^\s{2}(?P<command>[a-z0-9][a-z0-9-]*)\)\s+"
    r"(?P<target>[A-Za-z_][A-Za-z0-9_]*)\b"
)
CARGO_INVOCATION = re.compile(
    r"\bcargo\s+(?P<verb>check|test|clippy|fmt|run)\s+"
    r"(?P<args>[^\n;&|]+)"
)
LOCAL_CHECK_EXEMPTIONS = {
    "evidence-artifacts:verify": (
        "protected database bytes are operator-local evidence and are absent "
        "from hosted runners; hosted CI validates the manifest schema"
    ),
}
HOSTED_ACTION_EXEMPTIONS = {
    "actions/checkout@v4": "runner source checkout",
    "actions/setup-python@v5": "runner interpreter setup",
    "dtolnay/rust-toolchain@master": "runner Rust toolchain setup",
    "Swatinem/rust-cache@v2": "runner build-cache setup",
    "actions/attest-build-provenance@v4": "release-evidence attestation",
    "actions/upload-artifact@v4": "release-evidence persistence",
}
HOSTED_STEP_EXEMPTIONS = {
    "install": "runner Python environment setup",
    "emit CI-runner receipt": "release-evidence receipt emission",
    "persist CI-runner attestation bundle": (
        "release-evidence bundle persistence"
    ),
}


def parse_ci_workflow(path: Path) -> tuple[WorkflowJob, ...]:
    """Parse the checked-in CI subset without adding a YAML dependency."""
    try:
        lines = path.read_text().splitlines()
    except OSError as error:
        raise ConfigError(f"{path}: cannot read workflow: {error}") from error
    try:
        jobs_line = next(
            index for index, line in enumerate(lines) if line == "jobs:"
        )
    except StopIteration as error:
        raise ConfigError(f"{path}: missing top-level jobs mapping") from error

    headers = [
        (index, match.group("id"))
        for index, line in enumerate(lines[jobs_line + 1 :], jobs_line + 1)
        if (match := JOB_HEADER.match(line)) is not None
    ]
    if not headers:
        raise ConfigError(f"{path}: jobs mapping contains no jobs")

    jobs: list[WorkflowJob] = []
    for position, (start, job_id) in enumerate(headers):
        end = headers[position + 1][0] if position + 1 < len(headers) else len(lines)
        block = lines[start:end]
        report_only = any(
            line == "    continue-on-error: true" for line in block
        )

        axes: list[tuple[str, tuple[str, ...]]] = []
        matrix_indent: int | None = None
        for line_number, line in enumerate(block, start=start + 1):
            if line == "      matrix:":
                matrix_indent = 6
                continue
            if matrix_indent is None:
                continue
            indent = len(line) - len(line.lstrip(" "))
            if line.strip() and indent <= matrix_indent:
                matrix_indent = None
                continue
            axis = re.match(
                r"^        (?P<name>[A-Za-z0-9_-]+):\s*(?P<values>\[.*\])\s*$",
                line,
            )
            if axis is None:
                continue
            try:
                values = json.loads(axis.group("values"))
            except json.JSONDecodeError as error:
                raise ConfigError(
                    f"{path}:{line_number}: matrix values must be a JSON-style "
                    f"inline array: {error}"
                ) from error
            if not isinstance(values, list) or not values or any(
                not isinstance(value, (str, int, float, bool))
                for value in values
            ):
                raise ConfigError(
                    f"{path}:{line_number}: matrix axis must be a non-empty "
                    "scalar array"
                )
            axes.append(
                (axis.group("name"), tuple(str(value) for value in values))
            )

        steps: list[WorkflowStep] = []
        step_starts = [
            (index, match.group("field"), match.group("value"))
            for index, line in enumerate(block)
            if (match := STEP_HEADER.match(line)) is not None
        ]
        for step_position, (relative_start, field, value) in enumerate(
            step_starts
        ):
            relative_end = (
                step_starts[step_position + 1][0]
                if step_position + 1 < len(step_starts)
                else len(block)
            )
            step_block = block[relative_start:relative_end]
            name = value if field == "name" else value
            uses = value if field == "uses" else None
            run_text: str | None = None
            run_line: int | None = None
            for offset, line in enumerate(step_block):
                scalar = re.match(r"^        run:\s*(.*?)\s*$", line)
                if scalar is None:
                    nested_uses = re.match(r"^        uses:\s*(.+?)\s*$", line)
                    if nested_uses is not None:
                        uses = nested_uses.group(1)
                    continue
                run_line = start + relative_start + offset + 1
                value_text = scalar.group(1)
                if value_text in {"|", ">"}:
                    body: list[str] = []
                    for body_line in step_block[offset + 1 :]:
                        if body_line.startswith("          "):
                            body.append(body_line[10:])
                    run_text = "\n".join(body)
                else:
                    run_text = value_text
                break
            steps.append(
                WorkflowStep(
                    job=job_id,
                    name=name,
                    line=start + relative_start + 1,
                    run_line=run_line,
                    run=run_text,
                    uses=uses,
                )
            )
        jobs.append(
            WorkflowJob(
                id=job_id,
                line=start + 1,
                report_only=report_only,
                matrix=tuple(axes),
                steps=tuple(steps),
            )
        )
    return tuple(jobs)


def blocking_job_identities(
    path: Path,
) -> frozenset[tuple[str, str | None]]:
    """Derive receipt identities from non-report-only jobs and matrix values."""
    identities: set[tuple[str, str | None]] = set()
    for job in parse_ci_workflow(path):
        if job.report_only:
            continue
        if not job.matrix:
            identities.add((job.id, None))
            continue
        templates = [
            match.group("template")
            for step in job.steps
            if step.run is not None
            for match in re.finditer(
                r'"matrix"\s*:\s*"(?P<template>[^"]*\$\{\{'
                r'\s*matrix\.[^}]+\}\}[^"]*)"',
                step.run,
            )
        ]
        if len(templates) != 1:
            raise ConfigError(
                f"{path}:{job.line}: matrix job {job.id} must emit exactly "
                f"one receipt matrix template; found {len(templates)}"
            )
        names = [name for name, _values in job.matrix]
        value_sets = [values for _name, values in job.matrix]
        for combination in product(*value_sets):
            matrix = templates[0]
            for name, value in zip(names, combination):
                matrix = re.sub(
                    r"\$\{\{\s*matrix\." + re.escape(name) + r"\s*\}\}",
                    value,
                    matrix,
                )
            if "${{" in matrix:
                raise ConfigError(
                    f"{path}:{job.line}: matrix receipt template for {job.id} "
                    "contains an unresolved expression"
                )
            identities.add((job.id, matrix))
    return frozenset(identities)


def _bash_functions(text: str) -> dict[str, str]:
    lines = text.splitlines()
    functions: dict[str, str] = {}
    for match in FUNCTION_HEADER.finditer(text):
        start_line = text.count("\n", 0, match.end()) + 1
        end_line = next(
            (
                index
                for index in range(start_line, len(lines))
                if lines[index] == "}"
            ),
            None,
        )
        if end_line is None:
            raise ConfigError(f"run: unterminated function {match.group('name')}")
        functions[match.group("name")] = "\n".join(lines[start_line:end_line])
    return functions


def _canonical_cargo_commands(text: str) -> set[str]:
    commands: set[str] = set()
    collapsed = re.sub(r"\\\n[ \t]*", " ", text)
    for match in CARGO_INVOCATION.finditer(collapsed):
        try:
            arguments = shlex.split(match.group("args"))
        except ValueError:
            continue
        retained: list[str] = []
        for token in arguments:
            if token in {"2>&1", "||", "&&"}:
                break
            if token.startswith(("$", '"$', "'$")):
                break
            retained.append(token)
        if "--example" in retained:
            example_index = retained.index("--example")
            if example_index + 1 < len(retained):
                commands.add(
                    "cargo-example:" + retained[example_index + 1]
                )
                continue
        commands.add(
            "cargo:" + match.group("verb") + ":" + " ".join(retained)
        )
    return commands


def _direct_check_ids(text: str) -> set[str]:
    source = "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )
    checks = _canonical_cargo_commands(source)
    patterns = (
        ("version-check", r"tools/version_check\.py"),
        ("cycle-check", r"(?:tools\.cycle_check|tools/cycle_check\.py)"),
        ("checklist-audit", r"tools/checklist_audit\.py"),
        ("invariant-scan", r"tools/invariant_scan\.py"),
        ("deferred-audit", r"tools/audit_deferred\.py"),
        (
            "evidence-artifacts:validate",
            r"tools/evidence_artifacts\.py[^\n]*(?:validate)|"
            r"tools/evidence_artifacts\.py\s+\\\n[^\n]*validate",
        ),
        (
            "evidence-artifacts:verify",
            r"tools/evidence_artifacts\.py[^\n]*(?:\bverify\b)",
        ),
        ("python-constraints", r"tools/python_constraints\.py"),
        ("python-byte-compile", r"\bpy_compile\b"),
        ("shellcheck-presence", r"command\s+-v\s+shellcheck|shellcheck\s+--version"),
        ("shellcheck-run", r"shellcheck\s+(?:\./)?run\b"),
        ("shell-tests", r"-m\s+pytest\s+shell/tests(?:[/\s]|$)"),
        ("golden", r"tools/golden_e2e\.py"),
        ("progress-check", r"tools\.progress_check|tools/progress_check\.py"),
    )
    for check_id, pattern in patterns:
        if re.search(pattern, source):
            checks.add(check_id)
    return checks


def _function_check_ids(
    target: str,
    functions: dict[str, str],
    seen: set[str] | None = None,
) -> set[str]:
    visited = set() if seen is None else set(seen)
    if target in visited or target not in functions:
        return set()
    visited.add(target)
    body = functions[target]
    checks = _direct_check_ids(body)
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        for candidate in functions:
            if re.search(r"\b" + re.escape(candidate) + r"\b", stripped):
                checks.update(
                    _function_check_ids(candidate, functions, visited)
                )
    return checks


def _workflow_step_check_ids(
    step: WorkflowStep,
    functions: dict[str, str],
    dispatch: dict[str, str],
) -> set[str]:
    if step.run is None:
        return set()
    checks = _direct_check_ids(step.run)
    for command in re.findall(r"(?:^|\s)\./run\s+([a-z0-9-]+)", step.run):
        target = dispatch.get(command)
        if target is not None:
            checks.update(_function_check_ids(target, functions))
    return checks


def _hosted_step_exemption(step: WorkflowStep) -> str | None:
    if step.uses is not None:
        return HOSTED_ACTION_EXEMPTIONS.get(step.uses)
    return HOSTED_STEP_EXEMPTIONS.get(step.name)


def r10_report(root: Path) -> ParityReport:
    run_path = root / "run"
    workflow_path = root / ".github" / "workflows" / "ci.yml"
    try:
        run_text = run_path.read_text()
        functions = _bash_functions(run_text)
        workflow = parse_ci_workflow(workflow_path)
    except (OSError, ConfigError) as error:
        return ParityReport(
            findings=(f"run:1: cannot derive CI parity scope: {error}",),
            local_jobs=0,
            local_checks=0,
            blocking_jobs=0,
            hosted_checks=0,
            exemptions=(),
        )
    dispatch = {
        match.group("command"): match.group("target")
        for match in RUN_DISPATCH.finditer(run_text)
    }

    findings: list[str] = []
    local_sites: list[CheckSite] = []
    invocations = list(CI_LOCAL_INVOCATION.finditer(functions.get("cmd_ci_local", "")))
    cmd_start = next(
        (
            index
            for index, line in enumerate(run_text.splitlines(), start=1)
            if line == "cmd_ci_local() {"
        ),
        1,
    )
    for invocation in invocations:
        line = cmd_start + functions["cmd_ci_local"][: invocation.start()].count("\n") + 1
        label = invocation.group("label")
        target = invocation.group("target")
        check_ids = _function_check_ids(target, functions)
        if not check_ids:
            findings.append(
                f"run:{line}: local ci-local check {label!r} target "
                f"{target} is unclassified"
            )
            continue
        local_sites.extend(
            CheckSite(check_id, "run", line, label)
            for check_id in sorted(check_ids)
        )

    exemptions: list[str] = []
    hosted_sites: list[CheckSite] = []
    blocking_jobs = 0
    for job in workflow:
        if job.report_only:
            exemptions.append(
                f".github/workflows/ci.yml:{job.line}: hosted job {job.id}: "
                "job-level continue-on-error=true makes it report-only"
            )
            continue
        blocking_jobs += 1
        job_checks = 0
        for step in job.steps:
            reason = _hosted_step_exemption(step)
            if reason is not None:
                exemptions.append(
                    f".github/workflows/ci.yml:{step.line}: hosted step "
                    f"{job.id}/{step.name}: {reason}"
                )
                continue
            check_ids = _workflow_step_check_ids(step, functions, dispatch)
            if not check_ids:
                findings.append(
                    f".github/workflows/ci.yml:{step.run_line or step.line}: "
                    f"blocking hosted step {job.id}/{step.name!r} is "
                    "unclassified and not exempt"
                )
                continue
            job_checks += len(check_ids)
            hosted_sites.extend(
                CheckSite(
                    check_id,
                    ".github/workflows/ci.yml",
                    step.run_line or step.line,
                    f"{job.id}/{step.name}",
                )
                for check_id in sorted(check_ids)
            )
        if job_checks == 0:
            findings.append(
                f".github/workflows/ci.yml:{job.line}: blocking hosted job "
                f"{job.id} contains no parity-covered check"
            )

    local_by_id: dict[str, CheckSite] = {}
    for site in local_sites:
        local_by_id.setdefault(site.id, site)
    hosted_by_id: dict[str, CheckSite] = {}
    for site in hosted_sites:
        hosted_by_id.setdefault(site.id, site)

    for check_id in sorted(set(local_by_id) - set(hosted_by_id)):
        site = local_by_id[check_id]
        reason = LOCAL_CHECK_EXEMPTIONS.get(check_id)
        if reason is not None:
            exemptions.append(
                f"{site.file}:{site.line}: local check {site.label}: {reason}"
            )
            continue
        findings.append(
            f"{site.file}:{site.line}: local check {site.label!r} "
            f"({check_id}) has no blocking hosted counterpart"
        )
    for check_id in sorted(set(hosted_by_id) - set(local_by_id)):
        site = hosted_by_id[check_id]
        findings.append(
            f"{site.file}:{site.line}: blocking hosted check {site.label!r} "
            f"({check_id}) has no local ci-local counterpart"
        )

    return ParityReport(
        findings=tuple(findings),
        local_jobs=len(invocations),
        local_checks=len(local_by_id),
        blocking_jobs=blocking_jobs,
        hosted_checks=len(hosted_by_id),
        exemptions=tuple(exemptions),
    )


def r10_findings(root: Path) -> list[str]:
    return list(r10_report(root).findings)


def production_text(path: Path, text: str) -> str:
    """Return the production portion covered by the Rust rules."""
    if "tests" in path.parts:
        return ""
    boundary = TEST_MODULE.search(text)
    return text if boundary is None else text[: boundary.start()]


def rust_files(root: Path, base: Path | None = None) -> list[Path]:
    search_root = root if base is None else root / base
    if not search_root.is_dir():
        return []
    return sorted(
        path
        for path in search_root.rglob("*.rs")
        if ".git" not in path.parts and "target" not in path.parts
    )


def location(root: Path, path: Path, text: str, offset: int) -> str:
    line = text.count("\n", 0, offset) + 1
    return f"{path.relative_to(root)}:{line}"


def tracked_texts(root: Path) -> list[tuple[Path, str]]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.decode(errors="replace").strip()
        raise ConfigError(f"git ls-files failed for {root}: {message}")

    tracked: list[tuple[Path, str]] = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        relative = Path(raw_path.decode())
        path = root / relative
        try:
            payload = path.read_bytes()
        except OSError as error:
            raise ConfigError(f"{relative}: {error}") from error
        if b"\0" in payload:
            continue
        try:
            text = payload.decode()
        except UnicodeDecodeError:
            continue
        tracked.append((path, text))
    return tracked


def _enclosing_function(
    text: str,
    offset: int,
) -> re.Match[str] | None:
    declarations = list(RUST_FUNCTION.finditer(text, 0, offset))
    return declarations[-1] if declarations else None


def r1_findings(root: Path) -> list[str]:
    findings: list[str] = []
    expected = {
        (STORE, caller, "assign_canonical_ids_tx")
        for caller in CANONICAL_IDENTITY_CALLERS
    }
    seen = {site: 0 for site in expected}

    for path in rust_files(root):
        relative = path.relative_to(root)
        text = production_text(relative, path.read_text())
        for match, _token in _canonical_distance_calls(text):
            declaration = _enclosing_function(text, match.start())
            caller = (
                declaration.group("name")
                if declaration is not None
                else "<module>"
            )
            site = (relative, caller, match.group("name"))
            if site in expected and seen[site] == 0:
                seen[site] += 1
                continue
            findings.append(
                f"{location(root, path, text, match.start())}: canonical "
                "identity helper call is outside the production caller "
                f"allow-list; found {match.group('name')} in {caller}"
            )

    store_text = production_text(STORE, (root / STORE).read_text())
    store_declarations = {
        match.group("name"): match for match in RUST_FUNCTION.finditer(store_text)
    }
    for site, count in sorted(seen.items(), key=lambda item: item[0][1]):
        _path, caller, helper = site
        if count == 1:
            continue
        declaration = store_declarations.get(caller)
        if declaration is None:
            findings.append(
                f"{STORE}:1: expected production caller {caller} is absent"
            )
            continue
        findings.append(
            f"{location(root, root / STORE, store_text, declaration.start())}: "
            f"expected exactly one {helper} call in production caller {caller}; "
            f"found {count}"
        )
    return findings


def r2_findings(root: Path) -> list[str]:
    findings: list[str] = []
    matches: list[tuple[Path, str, re.Match[str]]] = []
    for path in rust_files(root):
        text = production_text(path.relative_to(root), path.read_text())
        matches.extend((path, text, match) for match in TCP_BIND.finditer(text))

    expected = (root / CORE_MAIN).resolve()
    for path, text, match in matches:
        allowed = (
            path.resolve() == expected
            and text.startswith(
                "tokio::net::TcpListener::bind(&bind_addresses[..])",
                match.start(),
            )
        )
        if not allowed:
            findings.append(
                f"{location(root, path, text, match.start())}: "
                "TcpListener bind outside the validated bind_addresses path"
            )

    main = (root / CORE_MAIN).read_text()
    production = production_text(CORE_MAIN, main)
    expected_call = "tokio::net::TcpListener::bind(&bind_addresses[..])"
    validation = "loopback_only(&bind)"
    if production.count(expected_call) != 1:
        findings.append(
            f"{CORE_MAIN}: expected exactly one validated TcpListener bind"
        )
    if production.count(validation) != 1:
        findings.append(
            f"{CORE_MAIN}: expected exactly one loopback_only validation"
        )
    if (
        expected_call in production
        and validation in production
        and production.index(validation) > production.index(expected_call)
    ):
        findings.append(f"{CORE_MAIN}: loopback validation occurs after bind")
    if len(matches) != 1:
        findings.append(
            f"production Rust contains {len(matches)} TcpListener binds; expected 1"
        )
    return findings


def r3_findings(root: Path) -> list[str]:
    findings: list[str] = []
    for path in rust_files(root, Path("crates")):
        text = production_text(path.relative_to(root), path.read_text())
        for label, pattern in LLM_MARKERS:
            for match in pattern.finditer(text):
                findings.append(
                    f"{location(root, path, text, match.start())}: {label}"
                )
    return findings


def r4_findings(root: Path) -> list[str]:
    findings: list[str] = []
    for path, text in tracked_texts(root):
        relative = path.relative_to(root)
        name = relative.name
        if name == ".env" or (
            name.startswith(".env.") and name != ".env.example"
        ):
            findings.append(f"{relative}: tracked secret-bearing environment file")

        patterns = (
            ("private-key header", PRIVATE_KEY_HEADER),
            ("provider-key-shaped value", PROVIDER_KEY),
            ("concrete Authorization bearer value", AUTHORIZATION_VALUE),
            ("raw secret-bearing response field", RAW_SECRET_FIELD),
        )
        for label, pattern in patterns:
            for match in pattern.finditer(text):
                findings.append(
                    f"{location(root, path, text, match.start())}: {label}"
                )

        for match in SECRET_ASSIGNMENT.finditer(text):
            value = match.group(1).strip("\"'")
            if (
                not value
                or value in SECRET_PLACEHOLDERS
                or "…" in value
                or "..." in value
                or value.startswith(("$", "<", "os.environ"))
            ):
                continue
            findings.append(
                f"{location(root, path, text, match.start())}: "
                "non-placeholder secret assignment"
            )
    return findings


def _matching_paren(text: str, open_offset: int) -> int | None:
    depth = 0
    quote: str | None = None
    escaped = False
    for offset in range(open_offset, len(text)):
        char = text[offset]
        if quote is not None:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in {'"', "'"}:
            quote = char
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return offset
    return None


def _top_level_arguments(arguments: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depths = {"(": 0, "[": 0, "{": 0}
    closing = {")": "(", "]": "[", "}": "{"}
    quote: str | None = None
    escaped = False
    for offset, char in enumerate(arguments):
        if quote is not None:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in {'"', "'"}:
            quote = char
        elif char in depths:
            depths[char] += 1
        elif char in closing:
            opener = closing[char]
            depths[opener] = max(0, depths[opener] - 1)
        elif char == "," and all(depth == 0 for depth in depths.values()):
            parts.append(arguments[start:offset].strip())
            start = offset + 1
    parts.append(arguments[start:].strip())
    return parts


def _cfg_test_item_ranges(text: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    marker = re.compile(r"(?m)^[ \t]*#\[cfg\(test\)\][ \t]*\n")
    for match in marker.finditer(text):
        brace = text.find("{", match.end())
        if brace == -1:
            continue
        depth = 0
        for offset in range(brace, len(text)):
            if text[offset] == "{":
                depth += 1
            elif text[offset] == "}":
                depth -= 1
                if depth == 0:
                    ranges.append((match.start(), offset + 1))
                    break
    return ranges


def _inside_ranges(offset: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= offset < end for start, end in ranges)


def _canonical_distance_calls(
    text: str,
) -> list[tuple[re.Match[str], str]]:
    calls: list[tuple[re.Match[str], str]] = []
    test_ranges = _cfg_test_item_ranges(text)
    for match in CANONICAL_DISTANCE_CALL.finditer(text):
        if _inside_ranges(match.start(), test_ranges):
            continue
        prefix = text[max(0, match.start() - 32) : match.start()]
        if re.search(r"\bfn\s*$", prefix):
            continue
        close = _matching_paren(text, match.end() - 1)
        if close is None:
            calls.append((match, "<unclosed call>"))
            continue
        arguments = _top_level_arguments(text[match.end() : close])
        distance_index = (
            1 if match.group("name") == "assign_canonical_ids_tx" else 0
        )
        token = (
            arguments[distance_index]
            if distance_index < len(arguments) and arguments[distance_index]
            else "<missing>"
        )
        calls.append((match, token))
    return calls


def r5_findings(root: Path) -> list[str]:
    findings: list[str] = []
    declarations: list[tuple[Path, str, re.Match[str]]] = []
    for path in rust_files(root):
        text = production_text(path.relative_to(root), path.read_text())
        declarations.extend(
            (path, text, match) for match in THRESHOLD_DECL.finditer(text)
        )
        for match, token in _canonical_distance_calls(text):
            if token != "DEDUP_MAX_DISTANCE":
                findings.append(
                    f"{location(root, path, text, match.start())}: "
                    f"{match.group('name')} distance argument must be "
                    f"DEDUP_MAX_DISTANCE; found {token}"
                )

    expected = [
        item
        for item in declarations
        if item[0].resolve() == (root / STORE).resolve()
        and item[2].group(1) == "DEDUP_MAX_DISTANCE"
        and item[2].group(2) == "16"
    ]
    if len(expected) != 1:
        findings.append(
            f"{STORE}: expected one private DEDUP_MAX_DISTANCE: u32 = 16"
        )
    for path, text, match in declarations:
        if (
            path.resolve() != (root / STORE).resolve()
            or match.group(1) != "DEDUP_MAX_DISTANCE"
            or match.group(2) != "16"
        ):
            findings.append(
                f"{location(root, path, text, match.start())}: second "
                f"canonical-distance constant {match.group(1)}={match.group(2)}"
            )
    if len(declarations) != 1:
        findings.append(
            "production Rust contains "
            f"{len(declarations)} DEDUP/CANONICAL distance constants; expected 1"
        )
    return findings


def _authority_block(root: Path, relative: Path) -> tuple[str | None, list[str]]:
    path = root / relative
    try:
        text = path.read_text()
    except OSError as error:
        return None, [f"{relative}: cannot read authorization block: {error}"]
    if text.count(AUTHORITY_START) != 1 or text.count(AUTHORITY_END) != 1:
        return None, [
            f"{relative}: expected exactly one model-profile authorization block"
        ]
    start = text.index(AUTHORITY_START)
    end = text.index(AUTHORITY_END, start) + len(AUTHORITY_END)
    return text[start:end], []


def r6_findings(root: Path) -> list[str]:
    findings: list[str] = []
    blocks: dict[Path, str] = {}
    for relative in AUTHORITY_FILES:
        block, errors = _authority_block(root, relative)
        findings.extend(errors)
        if block is not None:
            blocks[relative] = block
    if len(blocks) == len(AUTHORITY_FILES):
        reference = blocks[AUTHORITY_FILES[0]]
        for relative in AUTHORITY_FILES[1:]:
            if blocks[relative] != reference:
                candidate = blocks[relative]
                reference_lines = reference.splitlines()
                candidate_lines = candidate.splitlines()
                difference = next(
                    (
                        index
                        for index in range(
                            max(len(reference_lines), len(candidate_lines))
                        )
                        if (
                            index >= len(reference_lines)
                            or index >= len(candidate_lines)
                            or reference_lines[index] != candidate_lines[index]
                        )
                    ),
                    0,
                )
                text = (root / relative).read_text()
                block_line = text.count(
                    "\n", 0, text.index(AUTHORITY_START)
                ) + 1
                findings.append(
                    f"{relative}:{block_line + difference}: model-profile "
                    f"authorization block differs from {AUTHORITY_FILES[0]}"
                )
    return findings


def r7_findings(root: Path) -> list[str]:
    findings: list[str] = []
    store = (root / STORE).resolve()
    for path in rust_files(root):
        if path.resolve() == store:
            continue
        text = production_text(path.relative_to(root), path.read_text())
        for match in DOCUMENT_ID_HYDRATION_CALL.finditer(text):
            if match.group("name") != "documents_by_ids_in_sectors":
                findings.append(
                    f"{location(root, path, text, match.start())}: "
                    "production document hydration must call "
                    "documents_by_ids_in_sectors; found "
                    f"{match.group('name')}"
                )

    store_text = (root / STORE).read_text()
    for match in PUBLIC_UNSCOPED_HYDRATION.finditer(store_text):
        findings.append(
            f"{location(root, root / STORE, store_text, match.start())}: "
            "documents_by_ids must not be public"
        )
    return findings


def r8_findings(root: Path) -> list[str]:
    path = root / CORE_MAIN
    text = production_text(CORE_MAIN, path.read_text())
    main_declarations = [
        match
        for match in RUST_FUNCTION.finditer(text)
        if match.group("name") == "main"
    ]
    if len(main_declarations) != 1:
        return [
            f"{CORE_MAIN}:1: expected exactly one production main function; "
            f"found {len(main_declarations)}"
        ]

    main_start = main_declarations[0].start()
    main_text = text[main_start:]
    identity_calls = list(CRAWLER_IDENTITY_CONSTRUCTION.finditer(main_text))
    bind_calls = list(TCP_BIND.finditer(main_text))
    findings: list[str] = []

    if len(identity_calls) != 1:
        if len(identity_calls) == 0:
            binding = ROBOTS_CACHE_BINDING.search(main_text)
            offset = binding.start() if binding is not None else 0
        else:
            offset = identity_calls[1].start()
        findings.append(
            f"{location(root, path, text, main_start + offset)}: expected "
            "exactly one build_robots_cache call in production main; "
            f"found {len(identity_calls)}"
        )

    if len(bind_calls) != 1:
        offset = bind_calls[0].start() if bind_calls else 0
        findings.append(
            f"{location(root, path, text, main_start + offset)}: production "
            f"main contains {len(bind_calls)} TcpListener::bind calls; "
            "expected exactly one"
        )

    if (
        identity_calls
        and bind_calls
        and bind_calls[0].start() < identity_calls[0].start()
    ):
        findings.append(
            f"{location(root, path, text, main_start + bind_calls[0].start())}: "
            "TcpListener::bind occurs before build_robots_cache"
        )
    return findings


def _workspace_manifests(root: Path) -> list[Path]:
    workspace_manifest = root / "Cargo.toml"
    try:
        workspace = tomllib.loads(workspace_manifest.read_text())
        members = workspace["workspace"]["members"]
    except (OSError, tomllib.TOMLDecodeError, KeyError, TypeError) as error:
        raise ConfigError(f"Cargo.toml: cannot enumerate workspace: {error}") from error
    if not isinstance(members, list) or any(
        not isinstance(member, str) for member in members
    ):
        raise ConfigError("Cargo.toml: workspace.members must be a string array")
    return [workspace_manifest, *(root / member / "Cargo.toml" for member in members)]


def r9_findings(root: Path) -> list[str]:
    findings: list[str] = []
    for path in _workspace_manifests(root):
        relative = path.relative_to(root)
        try:
            text = path.read_text()
            tomllib.loads(text)
        except (OSError, tomllib.TOMLDecodeError) as error:
            raise ConfigError(f"{relative}: cannot parse workspace manifest: {error}") from error

        section = ""
        for line_number, line in enumerate(text.splitlines(), start=1):
            table = TOML_TABLE.match(line)
            if table is not None:
                section = table.group(1).strip()
                continue
            if line.lstrip().startswith("#") or TEST_SUPPORT.search(line) is None:
                continue

            allowed_dev_edge = section == "dev-dependencies" or section.endswith(
                ".dev-dependencies"
            )
            feature_definition = TEST_SUPPORT_FEATURE_DEFINITION.match(line)
            allowed_feature_definition = (
                section == "features"
                and feature_definition is not None
                and TEST_SUPPORT.search(line[feature_definition.end() :]) is None
            )
            if allowed_dev_edge or allowed_feature_definition:
                continue
            findings.append(
                f"{relative}:{line_number}: test-support is enabled outside "
                f"[dev-dependencies]; found section [{section or '<root>'}]"
            )
    return findings


CHECKS: dict[str, Callable[[Path], list[str]]] = {
    "R1": r1_findings,
    "R2": r2_findings,
    "R3": r3_findings,
    "R4": r4_findings,
    "R5": r5_findings,
    "R6": r6_findings,
    "R7": r7_findings,
    "R8": r8_findings,
    "R9": r9_findings,
    "R10": r10_findings,
}


def load_rules(path: Path) -> list[Rule]:
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise ConfigError(f"{path}: {error}") from error
    if not isinstance(raw, dict) or set(raw) != {"schema_version", "rules"}:
        raise ConfigError(
            f"{path}: root keys must be exactly schema_version and rules"
        )
    if raw["schema_version"] != 3:
        raise ConfigError(f"{path}: schema_version must be 3")
    if not isinstance(raw["rules"], list) or not raw["rules"]:
        raise ConfigError(f"{path}: rules must be a non-empty array")

    rules: list[Rule] = []
    seen: set[str] = set()
    fields = {
        "id",
        "claim",
        "source",
        "scope",
        "fail_before",
        "fail_before_note",
    }
    control_fields = {
        "file",
        "find",
        "replace_with",
        "expected_fail",
        "expected_file",
        "expected_line",
    }
    for index, item in enumerate(raw["rules"]):
        where = f"{path}:rules[{index}]"
        if not isinstance(item, dict) or set(item) != fields:
            raise ConfigError(f"{where}: keys must be exactly {sorted(fields)}")
        for field in fields - {"fail_before"}:
            if not isinstance(item[field], str) or not item[field].strip():
                raise ConfigError(f"{where}.{field}: must be a non-empty string")
        if item["id"] in seen:
            raise ConfigError(f"{where}.id: duplicate rule {item['id']}")
        if item["id"] not in CHECKS:
            raise ConfigError(f"{where}.id: no implemented check for {item['id']}")

        controls_raw = item["fail_before"]
        if not isinstance(controls_raw, list) or not controls_raw:
            raise ConfigError(f"{where}.fail_before: must be a non-empty array")
        controls: list[FailBefore] = []
        for control_index, control in enumerate(controls_raw):
            control_where = f"{where}.fail_before[{control_index}]"
            if not isinstance(control, dict) or set(control) != control_fields:
                raise ConfigError(
                    f"{control_where}: keys must be exactly "
                    f"{sorted(control_fields)}"
                )
            for field in {"file", "find", "expected_fail", "expected_file"}:
                if (
                    not isinstance(control[field], str)
                    or not control[field].strip()
                ):
                    raise ConfigError(
                        f"{control_where}.{field}: must be a non-empty string"
                    )
            relative = Path(control["file"])
            if relative.is_absolute() or ".." in relative.parts:
                raise ConfigError(
                    f"{control_where}.file: must be a safe relative path"
                )
            expected_relative = Path(control["expected_file"])
            if (
                expected_relative.is_absolute()
                or ".." in expected_relative.parts
            ):
                raise ConfigError(
                    f"{control_where}.expected_file: must be a safe "
                    "relative path"
                )
            if control["expected_file"] != control["file"]:
                raise ConfigError(
                    f"{control_where}.expected_file: must equal the mutated "
                    "file"
                )
            if (
                not isinstance(control["expected_line"], int)
                or isinstance(control["expected_line"], bool)
                or control["expected_line"] < 1
            ):
                raise ConfigError(
                    f"{control_where}.expected_line: must be a positive integer"
                )
            replacement = control["replace_with"]
            if (
                not isinstance(replacement, list)
                or not replacement
                or any(not isinstance(part, str) for part in replacement)
            ):
                raise ConfigError(
                    f"{control_where}.replace_with: must be a non-empty "
                    "array of strings"
                )
            if "".join(replacement) == control["find"]:
                raise ConfigError(
                    f"{control_where}: replacement must change the file"
                )
            controls.append(
                FailBefore(
                    file=control["file"],
                    find=control["find"],
                    replace_with=tuple(replacement),
                    expected_fail=control["expected_fail"],
                    expected_file=control["expected_file"],
                    expected_line=control["expected_line"],
                )
            )
        seen.add(item["id"])
        rules.append(
            Rule(
                id=item["id"],
                claim=item["claim"],
                source=item["source"],
                scope=item["scope"],
                fail_before=tuple(controls),
                fail_before_note=item["fail_before_note"],
            )
        )
    return rules


def run_rules(root: Path, rules: list[Rule]) -> int:
    failed = False
    for rule in rules:
        resolved_root = root.resolve()
        findings = CHECKS[rule.id](resolved_root)
        if findings:
            failed = True
            for finding in findings:
                print(f"invariant-scan: {rule.id} FAIL: {finding}")
        else:
            suffix = ""
            if rule.id == "R10":
                report = r10_report(resolved_root)
                suffix = (
                    f" (local_jobs={report.local_jobs}, "
                    f"local_checks={report.local_checks}, "
                    f"blocking_jobs={report.blocking_jobs}, "
                    f"hosted_checks={report.hosted_checks}, "
                    f"exemptions={len(report.exemptions)})"
                )
            print(f"invariant-scan: {rule.id} PASS: {rule.claim}{suffix}")
    if failed:
        return 1
    print(f"invariant-scan: PASS ({len(rules)}/{len(rules)} registered rules)")
    return 0


def select_rules(rules: list[Rule], rule_ids: set[str] | None) -> list[Rule]:
    if rule_ids is None:
        return rules
    known = {rule.id for rule in rules}
    unknown = sorted(rule_ids - known)
    if unknown:
        raise ConfigError(f"requested rule is not registered: {', '.join(unknown)}")
    return [rule for rule in rules if rule.id in rule_ids]


def run(
    root: Path,
    rules_path: Path,
    rule_ids: set[str] | None = None,
) -> int:
    try:
        rules = load_rules(rules_path)
        selected = select_rules(rules, rule_ids)
    except ConfigError as error:
        print(f"invariant-scan: CONFIG FAIL: {error}")
        return 2
    return run_rules(root, selected)


def _tracked_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.decode(errors="replace").strip()
        raise ConfigError(f"git ls-files failed for {root}: {message}")
    return [
        Path(raw.decode())
        for raw in result.stdout.split(b"\0")
        if raw
    ]


def _copy_tracked_tree(root: Path, destination: Path) -> None:
    destination.mkdir(parents=True)
    for relative in _tracked_paths(root):
        source = root / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_symlink():
            os.symlink(os.readlink(source), target)
        else:
            shutil.copy2(source, target)

    for command in (["git", "init", "-q"], ["git", "add", "-A"]):
        result = subprocess.run(
            command,
            cwd=destination,
            check=False,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            raise ConfigError(
                f"{' '.join(command)} failed in self-test copy: "
                f"{result.stderr.strip()}"
            )


def _apply_control(root: Path, control: FailBefore) -> None:
    path = root / control.file
    try:
        text = path.read_text()
    except OSError as error:
        raise ConfigError(
            f"{control.file}: cannot apply fail-before: {error}"
        ) from error
    occurrences = text.count(control.find)
    if occurrences != 1:
        raise ConfigError(
            f"{control.file}: fail-before find text occurs {occurrences} "
            "times; expected exactly 1"
        )
    path.write_text(text.replace(control.find, "".join(control.replace_with), 1))


def exercise_fail_before(
    root: Path,
    rule: Rule,
    control: FailBefore,
) -> tuple[int, str]:
    with tempfile.TemporaryDirectory(prefix=f"invariant-scan-{rule.id}-") as raw:
        copied_root = Path(raw) / "tree"
        _copy_tracked_tree(root, copied_root)
        _apply_control(copied_root, control)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = run_rules(copied_root, [rule])
        return status, output.getvalue()


def expected_control_finding(rule: Rule, control: FailBefore) -> str:
    return (
        f"invariant-scan: {rule.id} FAIL: {control.expected_file}:"
        f"{control.expected_line}: {control.expected_fail}"
    )


def self_test(
    root: Path,
    rules_path: Path,
    rule_ids: set[str] | None = None,
) -> int:
    try:
        rules = load_rules(rules_path)
        selected = select_rules(rules, rule_ids)
    except ConfigError as error:
        print(f"invariant-scan: CONFIG FAIL: {error}")
        return 2

    if run_rules(root, selected) != 0:
        print("invariant-scan: SELF-TEST FAIL: unmutated tree is not clean")
        return 1

    controls_run = 0
    for rule in selected:
        for index, control in enumerate(rule.fail_before, start=1):
            controls_run += 1
            try:
                status, output = exercise_fail_before(root, rule, control)
            except ConfigError as error:
                print(
                    f"invariant-scan: SELF-TEST {rule.id}/{index} FAIL: {error}"
                )
                return 1
            if status == 0:
                print(
                    f"invariant-scan: SELF-TEST {rule.id}/{index} FAIL: "
                    "mutation did not make the rule fail"
                )
                return 1
            if status != 1:
                print(
                    f"invariant-scan: SELF-TEST {rule.id}/{index} FAIL: "
                    f"rule exited {status}, expected 1"
                )
                return 1
            expected_finding = expected_control_finding(rule, control)
            if expected_finding not in output.splitlines():
                print(
                    f"invariant-scan: SELF-TEST {rule.id}/{index} FAIL: "
                    f"missing expected finding {expected_finding!r}"
                )
                return 1
            print(
                f"invariant-scan: SELF-TEST {rule.id}/{index} PASS: "
                f"{control.expected_file}:{control.expected_line}: "
                f"{control.expected_fail}"
            )

    print(
        "invariant-scan: SELF-TEST PASS "
        f"({len(selected)}/{len(selected)} rules, {controls_run} controls)"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--rules", type=Path, dest="rules_path")
    parser.add_argument("--rule", action="append", dest="rule_ids")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    rules_path = (
        args.rules_path.resolve()
        if args.rules_path is not None
        else root / RULES_FILE
    )
    selected = set(args.rule_ids) if args.rule_ids else None
    # No-argument execution is the CI path (through ``./run invariant-scan``).
    # Keep the executable controls on by default so the existing local/hosted
    # job cannot accidentally regress to clean-tree checks alone.
    if args.self_test or (args.rules_path is None and args.rule_ids is None):
        return self_test(root, rules_path, selected)
    return run(root, rules_path, selected)


if __name__ == "__main__":
    raise SystemExit(main())
