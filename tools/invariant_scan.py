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
import ast
import contextlib
import importlib.util
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
EXTRACT = Path("crates/extract/src/lib.rs")
VIEW = Path("crates/view/src/lib.rs")
CORE_MAIN = Path("apps/cored/src/main.rs")
AUTHORITY_FILES = (
    Path("AGENTS.md"),
    Path("docs/intel-platform-OPERATIONS.md"),
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
VIEW_DEFAULT_DISTANCE = re.compile(
    r"(?ms)impl\s+Default\s+for\s+ViewParams\s*\{.*?"
    r"dedup_max_distance:\s*(\d+)\s*,"
)
DEDUP_FEATURE_FLOOR_DECL = re.compile(
    r"(?m)^\s*(?:pub(?:\([^)]*\))?\s+)?const\s+"
    r"(DEDUP_MIN_FEATURES)\s*:\s*usize\s*=\s*(\d+)"
)
DEDUP_ELIGIBILITY_BODY = re.compile(
    r"(?ms)pub\s+fn\s+dedup_eligible\s*\("
    r"\s*left_features:\s*usize,\s*right_features:\s*usize\s*\)"
    r"\s*->\s*bool\s*\{\s*"
    r"left_features\s*>=\s*DEDUP_MIN_FEATURES\s*&&\s*"
    r"right_features\s*>=\s*DEDUP_MIN_FEATURES\s*\}"
)
DEDUP_ELIGIBILITY_CALL = re.compile(
    r"\b(?P<qualified>intel_extract::)?dedup_eligible\s*\("
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
    condition: str | None
    source: str


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
class CiLocalJob:
    label: str
    target: str
    line: int


@dataclass(frozen=True)
class ParityReport:
    findings: tuple[str, ...]
    local_jobs: int
    local_checks: int
    blocking_jobs: int
    hosted_checks: int
    exemptions: tuple[str, ...]
    exemption_bases: tuple[str, ...]


@dataclass(frozen=True)
class ExemptionDecision:
    basis: str
    reason: str


JOB_HEADER = re.compile(r"^  (?P<id>[A-Za-z0-9_-]+):\s*$")
STEP_HEADER = re.compile(
    r"^      - (?P<field>name|uses):\s*(?P<value>.+?)\s*$"
)
FUNCTION_HEADER = re.compile(
    r"(?m)^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\(\)\s*\{\s*$"
)
CI_LOCAL_JOB_TABLE = re.compile(
    r"(?ms)^\s*cat <<'JOBS'\n(?P<body>.*?)^JOBS$"
)
CI_LOCAL_JOB_SPEC = re.compile(
    r"(?P<label>[^|\n]+)\|(?P<target>[A-Za-z_][A-Za-z0-9_]*)"
)
RUN_DISPATCH = re.compile(
    r"(?m)^\s{2}(?P<command>[a-z0-9][a-z0-9-]*)\)\s+"
    r"(?P<target>[A-Za-z_][A-Za-z0-9_]*)\b"
)
CARGO_INVOCATION = re.compile(
    r"\bcargo\s+(?P<verb>check|test|clippy|fmt|run)\s+"
    r"(?P<args>[^\n;&|]+)"
)
RESIDUAL_LOCAL_CHECK_EXEMPTIONS = {
    "evidence-artifacts:verify": (
        "protected database bytes are operator-local evidence and are absent "
        "from hosted runners; hosted CI validates the manifest schema"
    ),
}
EXEMPTION_CRITERIA = {
    "report-only-job": (
        "the job declares job-level continue-on-error: true"
    ),
    "runner-setup-action": (
        "the step is an unconditional uses: action before the job's first "
        "command-bearing step"
    ),
    "constrained-python-install": (
        "the command installs the committed shell requirements under the "
        "committed constraints file"
    ),
    "receipt-attestation-persistence": (
        "the step belongs to the terminal contiguous always() block and "
        "references the canonical CI_RECEIPT_PATH"
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
            condition: str | None = None
            for offset, line in enumerate(step_block):
                condition_match = re.match(r"^        if:\s*(.+?)\s*$", line)
                if condition_match is not None:
                    condition = condition_match.group(1)
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
                    condition=condition,
                    source="\n".join(step_block),
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


def parse_ci_local_jobs(text: str) -> tuple[CiLocalJob, ...]:
    """Derive the executable local-CI matrix from run's sole job table."""
    functions = _bash_functions(text)
    body = functions.get("ci_local_jobs")
    if body is None:
        raise ConfigError("run: missing ci_local_jobs function")
    table = CI_LOCAL_JOB_TABLE.search(body)
    if table is None:
        raise ConfigError("run: ci_local_jobs has no parseable JOBS table")

    function_start = next(
        match.start()
        for match in FUNCTION_HEADER.finditer(text)
        if match.group("name") == "ci_local_jobs"
    )
    table_start = text.find(table.group("body"), function_start)
    jobs: list[CiLocalJob] = []
    seen_targets: set[str] = set()
    offset = table_start
    for raw_line in table.group("body").splitlines(keepends=True):
        line_text = raw_line.rstrip("\n")
        line = text.count("\n", 0, offset) + 1
        offset += len(raw_line)
        match = CI_LOCAL_JOB_SPEC.fullmatch(line_text)
        if match is None:
            raise ConfigError(f"run:{line}: malformed ci-local job specification")
        target = match.group("target")
        if target in seen_targets:
            raise ConfigError(f"run:{line}: duplicate ci-local target {target}")
        seen_targets.add(target)
        jobs.append(CiLocalJob(match.group("label"), target, line))
    if not jobs:
        raise ConfigError("run: ci_local_jobs table is empty")
    return tuple(jobs)


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


def _receipt_persistence_indices(job: WorkflowJob) -> frozenset[int]:
    indices: set[int] = set()
    for index in range(len(job.steps) - 1, -1, -1):
        step = job.steps[index]
        if (
            step.condition
            not in {
                "always()",
                "always() && inputs.publish_evidence == true",
            }
            or "CI_RECEIPT_PATH" not in step.source
        ):
            break
        indices.add(index)
    return frozenset(indices)


def _is_constrained_python_install(step: WorkflowStep) -> bool:
    if step.run is None:
        return False
    collapsed = " ".join(step.run.split())
    return bool(
        re.fullmatch(
            r"pip install -c shell/constraints\.txt "
            r"-r shell/requirements\.txt",
            collapsed,
        )
    )


def _hosted_step_exemption(
    job: WorkflowJob,
    index: int,
) -> ExemptionDecision | None:
    step = job.steps[index]
    receipt_indices = _receipt_persistence_indices(job)
    if index in receipt_indices:
        basis = "receipt-attestation-persistence"
    else:
        first_command = next(
            (
                position
                for position, candidate in enumerate(job.steps)
                if candidate.run is not None
            ),
            len(job.steps),
        )
        if (
            step.uses is not None
            and step.condition is None
            and index < first_command
        ):
            basis = "runner-setup-action"
        elif _is_constrained_python_install(step):
            basis = "constrained-python-install"
        else:
            return None
    return ExemptionDecision(basis, EXEMPTION_CRITERIA[basis])


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
            exemption_bases=(),
        )
    dispatch = {
        match.group("command"): match.group("target")
        for match in RUN_DISPATCH.finditer(run_text)
    }

    findings: list[str] = []
    local_sites: list[CheckSite] = []
    try:
        local_jobs = parse_ci_local_jobs(run_text)
    except ConfigError as error:
        return ParityReport(
            findings=(f"run:1: cannot derive CI parity scope: {error}",),
            local_jobs=0,
            local_checks=0,
            blocking_jobs=0,
            hosted_checks=0,
            exemptions=(),
            exemption_bases=(),
        )
    for job in local_jobs:
        check_ids = _function_check_ids(job.target, functions)
        if not check_ids:
            findings.append(
                f"run:{job.line}: local ci-local check {job.label!r} target "
                f"{job.target} is unclassified"
            )
            continue
        local_sites.extend(
            CheckSite(check_id, "run", job.line, job.label)
            for check_id in sorted(check_ids)
        )

    exemptions: list[str] = []
    exemption_bases: list[str] = []
    hosted_sites: list[CheckSite] = []
    blocking_jobs = 0
    for job in workflow:
        if job.report_only:
            basis = "report-only-job"
            exemptions.append(
                f".github/workflows/ci.yml:{job.line}: hosted job {job.id}: "
                f"{EXEMPTION_CRITERIA[basis]}"
            )
            exemption_bases.append(basis)
            continue
        blocking_jobs += 1
        job_checks = 0
        for index, step in enumerate(job.steps):
            decision = _hosted_step_exemption(job, index)
            if decision is not None:
                exemptions.append(
                    f".github/workflows/ci.yml:{step.line}: hosted step "
                    f"{job.id}/{step.name}: {decision.reason}"
                )
                exemption_bases.append(decision.basis)
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
        reason = RESIDUAL_LOCAL_CHECK_EXEMPTIONS.get(check_id)
        if reason is not None:
            exemptions.append(
                f"{site.file}:{site.line}: local check {site.label}: {reason}"
            )
            exemption_bases.append(f"named-local-check:{check_id}")
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
        local_jobs=len(local_jobs),
        local_checks=len(local_by_id),
        blocking_jobs=blocking_jobs,
        hosted_checks=len(hosted_by_id),
        exemptions=tuple(exemptions),
        exemption_bases=tuple(exemption_bases),
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
    feature_floors: list[tuple[Path, str, re.Match[str]]] = []
    eligibility_calls: list[tuple[Path, str, re.Match[str], str]] = []
    for path in rust_files(root):
        text = production_text(path.relative_to(root), path.read_text())
        declarations.extend(
            (path, text, match) for match in THRESHOLD_DECL.finditer(text)
        )
        feature_floors.extend(
            (path, text, match)
            for match in DEDUP_FEATURE_FLOOR_DECL.finditer(text)
        )
        for match in DEDUP_ELIGIBILITY_CALL.finditer(text):
            prefix = text[max(0, match.start() - 32) : match.start()]
            if re.search(r"\bfn\s*$", prefix):
                continue
            declaration = _enclosing_function(text, match.start())
            caller = (
                declaration.group("name")
                if declaration is not None
                else "<module>"
            )
            eligibility_calls.append((path, text, match, caller))
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
    ]
    if len(expected) != 1:
        findings.append(
            f"{STORE}: expected one private DEDUP_MAX_DISTANCE: u32 declaration"
        )
    for path, text, match in declarations:
        if (
            path.resolve() != (root / STORE).resolve()
            or match.group(1) != "DEDUP_MAX_DISTANCE"
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
    view_path = root / VIEW
    view_text = production_text(VIEW, view_path.read_text())
    view_defaults = list(VIEW_DEFAULT_DISTANCE.finditer(view_text))
    if len(view_defaults) != 1:
        findings.append(
            f"{VIEW}: expected one ViewParams default dedup_max_distance"
        )
    if len(expected) == 1 and len(view_defaults) == 1:
        store_value = expected[0][2].group(2)
        view_value = view_defaults[0].group(1)
        if store_value != view_value:
            findings.append(
                f"{location(root, view_path, view_text, view_defaults[0].start(1))}: "
                f"view default dedup_max_distance={view_value} differs from "
                f"store DEDUP_MAX_DISTANCE={store_value}"
            )

    extract_path = root / EXTRACT
    extract_text = production_text(EXTRACT, extract_path.read_text())
    expected_floor = [
        item
        for item in feature_floors
        if item[0].resolve() == extract_path.resolve()
    ]
    if len(expected_floor) != 1:
        findings.append(
            f"{EXTRACT}:24: expected one public DEDUP_MIN_FEATURES: usize declaration"
        )
    for path, text, match in feature_floors:
        if path.resolve() != extract_path.resolve():
            findings.append(
                f"{location(root, path, text, match.start())}: second "
                f"DEDUP_MIN_FEATURES declaration={match.group(2)}"
            )
    if len(feature_floors) != 1:
        findings.append(
            f"{EXTRACT}:24: production Rust contains {len(feature_floors)} "
            "DEDUP_MIN_FEATURES declarations; expected 1"
        )
    if len(expected_floor) == 1 and expected_floor[0][2].group(2) != "26":
        path, text, match = expected_floor[0]
        findings.append(
            f"{location(root, path, text, match.start(2))}: "
            f"DEDUP_MIN_FEATURES={match.group(2)} differs from measured floor 26"
        )

    guard_bodies = list(DEDUP_ELIGIBILITY_BODY.finditer(extract_text))
    if len(guard_bodies) != 1:
        guard_definition = next(
            (
                declaration
                for declaration in RUST_FUNCTION.finditer(extract_text)
                if declaration.group("name") == "dedup_eligible"
            ),
            None,
        )
        guard_line = (
            location(root, extract_path, extract_text, guard_definition.start())
            if guard_definition is not None
            else f"{EXTRACT}:58"
        )
        findings.append(
            f"{guard_line}: dedup_eligible must compare both feature counts "
            "to DEDUP_MIN_FEATURES"
        )

    expected_eligibility_sites = {
        (EXTRACT, "dedup_near", False),
        (STORE, "assign_canonical_ids_tx", True),
    }
    seen_eligibility_sites: set[tuple[Path, str, bool]] = set()
    for path, text, match, caller in eligibility_calls:
        site = (
            path.relative_to(root),
            caller,
            match.group("qualified") is not None,
        )
        if site not in expected_eligibility_sites:
            findings.append(
                f"{location(root, path, text, match.start())}: unexpected "
                f"dedup_eligible call in {caller}"
            )
        seen_eligibility_sites.add(site)
    for relative, caller, qualified in sorted(
        expected_eligibility_sites - seen_eligibility_sites,
        key=lambda item: (str(item[0]), item[1], item[2]),
    ):
        path = root / relative
        text = production_text(relative, path.read_text())
        declaration = next(
            (
                item
                for item in RUST_FUNCTION.finditer(text)
                if item.group("name") == caller
            ),
            None,
        )
        line = (
            location(root, path, text, declaration.start())
            if declaration is not None
            else f"{relative}:1"
        )
        qualification = "intel_extract::" if qualified else ""
        findings.append(
            f"{line}: {caller} must call {qualification}dedup_eligible"
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


CORE_OWNED_CONFIG_REFERENCES = {
    "config/core.json",
    "config/entities.json",
    "CORE_CONFIG",
    "CORE_ENTITIES",
}
PYTHON_READ_METHODS = {"open", "read_bytes", "read_text"}


def _core_owned_config_reference(node: ast.AST | None) -> str | None:
    if node is None:
        return None
    for child in ast.walk(node):
        if (
            isinstance(child, ast.Constant)
            and isinstance(child.value, str)
            and child.value in CORE_OWNED_CONFIG_REFERENCES
        ):
            return child.value
    return None


def _assigned_names(node: ast.Assign | ast.AnnAssign | ast.NamedExpr) -> set[str]:
    if isinstance(node, ast.Assign):
        targets = node.targets
    else:
        targets = [node.target]
    return {
        target.id
        for target in targets
        if isinstance(target, ast.Name)
    }


def r11_findings(root: Path) -> list[str]:
    """Reject production shell filesystem reads sourced from core config."""
    findings: list[str] = []
    shell_root = root / "shell" / "intel_shell"
    for path in sorted(shell_root.glob("*.py")):
        relative = path.relative_to(root)
        try:
            text = path.read_text()
            tree = ast.parse(text, filename=str(relative))
        except (OSError, SyntaxError) as error:
            raise ConfigError(f"{relative}: cannot parse production shell: {error}") from error

        tainted: dict[str, str] = {}
        assignments = [
            node
            for node in ast.walk(tree)
            if isinstance(node, (ast.Assign, ast.AnnAssign, ast.NamedExpr))
        ]
        changed = True
        while changed:
            changed = False
            for assignment in assignments:
                value = assignment.value
                reference = _core_owned_config_reference(value)
                if reference is None and value is not None:
                    reference = next(
                        (
                            tainted[child.id]
                            for child in ast.walk(value)
                            if isinstance(child, ast.Name) and child.id in tainted
                        ),
                        None,
                    )
                if reference is None:
                    continue
                for name in _assigned_names(assignment):
                    if tainted.get(name) != reference:
                        tainted[name] = reference
                        changed = True

        for call in (node for node in ast.walk(tree) if isinstance(node, ast.Call)):
            if isinstance(call.func, ast.Name):
                is_read = call.func.id == "open"
            elif isinstance(call.func, ast.Attribute):
                is_read = call.func.attr in PYTHON_READ_METHODS
            else:
                is_read = False
            if not is_read:
                continue

            reference = _core_owned_config_reference(call)
            if reference is None:
                reference = next(
                    (
                        tainted[child.id]
                        for child in ast.walk(call)
                        if isinstance(child, ast.Name) and child.id in tainted
                    ),
                    None,
                )
            if reference is not None:
                findings.append(
                    f'{relative}:{call.lineno}: production shell reads core-owned '
                    f'configuration "{reference}" directly'
                )
    return findings


PUBLICATION_CONTROL_MARKERS = {
    "tagged-closing-protocol": (
        "Invariant R12 control site: tagged-closing protocol."
    ),
    "tag-type": (
        "Invariant R12 control site: annotated closing-tag type."
    ),
    "tagged-closing-parent": (
        "Invariant R12 control site: tagged-closing parent agreement."
    ),
    "tagged-closing-tree": (
        "Invariant R12 control site: tagged-closing tree agreement."
    ),
    "origin-main": "Invariant R12 control site: origin-main prohibition.",
    "tag-ref-unavailable": (
        "Invariant R12 control site: unavailable annotated-tag ref."
    ),
    "tag-target-unavailable": (
        "Invariant R12 control site: unavailable annotated-tag target."
    ),
    "ancestry-unavailable": (
        "Invariant R12 control site: unavailable publication ancestry."
    ),
    "pending-publication": (
        "Invariant R12 control site: pending-publication prohibition."
    ),
    "tag-object-assertion": (
        "Invariant R12 control site: required and fresh immutable assertions."
    ),
    "tag-target-assertion": (
        "Invariant R12 control site: required and fresh immutable assertions."
    ),
    "release-commit-assertion": (
        "Invariant R12 control site: required and fresh immutable assertions."
    ),
    "post-push-record": (
        "Invariant R12 control site: required and fresh post-push record."
    ),
    "declared-scope": (
        "Invariant R12 control site: declared cycle scope."
    ),
    "review-export-retention": (
        "Invariant R12 control site: review-export retention configuration."
    ),
    "trigger-freshness": (
        "Invariant R12 control site: trigger freshness."
    ),
    "trigger-carry-forward": (
        "Invariant R12 control site: deferred trigger carry-forward."
    ),
    "test-population": (
        "Invariant R12 control site: test-population equivalence."
    ),
    "coverage-detection": (
        "Invariant R12 control site: pre-insert per-source coverage detection."
    ),
}


def _load_cycle_check_for_control(root: Path):
    path = root / "tools" / "cycle_check.py"
    spec = importlib.util.spec_from_file_location(
        "_invariant_scan_cycle_check",
        path,
    )
    if spec is None or spec.loader is None:
        raise ConfigError(f"{path.relative_to(root)}: cannot load cycle checker")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except (OSError, SyntaxError) as error:
        raise ConfigError(
            f"{path.relative_to(root)}: cannot execute cycle checker: {error}"
        ) from error
    return module


def _load_test_population_for_control(root: Path):
    path = root / "tools" / "test_population.py"
    spec = importlib.util.spec_from_file_location(
        "_invariant_scan_test_population",
        path,
    )
    if spec is None or spec.loader is None:
        raise ConfigError(
            f"{path.relative_to(root)}: cannot load test-population comparator"
        )
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except (OSError, SyntaxError) as error:
        raise ConfigError(
            f"{path.relative_to(root)}: cannot execute test-population "
            f"comparator: {error}"
        ) from error
    return module


def r12_findings(root: Path) -> list[str]:
    """Exercise lifecycle, population, and coverage rules against planted failures."""
    cycle_check = _load_cycle_check_for_control(root)
    test_population = _load_test_population_for_control(root)
    tag = "publication-control-tag"
    tag_object = "a" * 40
    tag_target = "b" * 40
    stale_object = "c" * 40
    stale_target = "d" * 40
    release_commit = "e" * 40
    descendant = "f" * 40
    valid_legacy_header = (
        "**As of:** published. Annotated tag object is "
        f"`{tag_object}`; release commit is `{tag_target}`.\n"
    )
    legacy_scenarios = (
        (
            "origin-main",
            "origin-main",
            valid_legacy_header.replace(
                "**As of:** published.",
                f"**As of:** published. origin/main is `{tag_target}`.",
            ),
            tag_object,
            tag_target,
            (0, ""),
            "publication status header must not assert a literal origin/main hash",
        ),
        (
            "tag-object-required",
            "tag-object-assertion",
            f"**As of:** published. Release commit is `{tag_target}`.\n",
            tag_object,
            tag_target,
            (0, ""),
            "publication assertion required: status header must assert the "
            "annotated tag object",
        ),
        (
            "tag-object-freshness",
            "tag-object-assertion",
            valid_legacy_header.replace(tag_object, stale_object),
            tag_object,
            tag_target,
            (0, ""),
            "publication assertion freshness: annotated tag object asserts",
        ),
        (
            "tag-target-required",
            "tag-target-assertion",
            f"**As of:** published. Annotated tag object is `{tag_object}`.\n",
            tag_object,
            tag_target,
            (0, ""),
            "publication assertion required: status header must assert the "
            "tag target",
        ),
        (
            "tag-target-freshness",
            "tag-target-assertion",
            valid_legacy_header.replace(tag_target, stale_target),
            tag_object,
            tag_target,
            (0, ""),
            "publication assertion freshness: tag target asserts",
        ),
        (
            "pending-publication",
            "pending-publication",
            valid_legacy_header.replace(
                "**As of:** published.",
                "**As of:** publication is pending.",
            ),
            tag_object,
            tag_target,
            (0, ""),
            "publication disposition agreement",
        ),
        (
            "tag-ref-unavailable",
            "tag-ref-unavailable",
            valid_legacy_header,
            None,
            tag_target,
            (0, ""),
            "publication verification unavailable: annotated tag ref",
        ),
        (
            "tag-target-unavailable",
            "tag-target-unavailable",
            valid_legacy_header,
            tag_object,
            None,
            (0, ""),
            "publication verification unavailable: annotated tag target",
        ),
        (
            "ancestry-unavailable",
            "ancestry-unavailable",
            valid_legacy_header,
            tag_object,
            tag_target,
            (128, "fatal: planted shallow-history control"),
            "publication ancestry verification unavailable",
        ),
    )
    tagged_runbook_text = (
        "# Closed cycle\n\n"
        "- [x] completed task\n\n"
        "## Cycle closing record\n\n"
        "- **Cycle closed:** 2026-07-29\n"
        "- **Release disposition:** release (as of 2026-07-29)\n"
        f"- **Release:** `{tag}`\n"
        f"- **Release commit:** `{release_commit}`\n"
    )
    valid_tagged_header = (
        f"**As of:** published. Release commit is `{release_commit}`.\n"
    )
    valid_post_push = (
        "- **Post-push verification date:** 2026-07-29\n"
        f"- **Post-push release:** `{tag}`\n"
        f"- **Post-push annotated tag object:** `{tag_object}`\n"
        f"- **Post-push closing commit:** `{tag_target}`\n"
        "- **Post-push hosted run:** `123456`\n"
    )
    tagged_scenarios = (
        (
            "release-commit-required",
            "release-commit-assertion",
            "**As of:** published.\n",
            "",
            "tag",
            release_commit,
            tagged_runbook_text,
            tag_target,
            "publication assertion required: status header must assert the "
            "release commit",
        ),
        (
            "release-commit-freshness",
            "release-commit-assertion",
            valid_tagged_header.replace(release_commit, stale_target),
            "",
            "tag",
            release_commit,
            tagged_runbook_text,
            tag_target,
            "publication assertion freshness: release commit asserts",
        ),
        (
            "tag-type",
            "tag-type",
            valid_tagged_header,
            "",
            "commit",
            release_commit,
            tagged_runbook_text,
            tag_target,
            "must resolve to an annotated tag object",
        ),
        (
            "tagged-closing-parent",
            "tagged-closing-parent",
            valid_tagged_header,
            "",
            "tag",
            stale_target,
            tagged_runbook_text,
            tag_target,
            "tagged-closing parent agreement",
        ),
        (
            "tagged-closing-tree",
            "tagged-closing-tree",
            valid_tagged_header,
            "",
            "tag",
            release_commit,
            "# Open cycle\n\n- [ ] unfinished\n",
            tag_target,
            "tagged-closing tree agreement",
        ),
        (
            "post-push-required",
            "post-push-record",
            valid_tagged_header,
            "",
            "tag",
            release_commit,
            tagged_runbook_text,
            descendant,
            "publication post-push record required",
        ),
        (
            "post-push-date-invalid",
            "post-push-record",
            valid_tagged_header,
            valid_post_push.replace("2026-07-29", "2026-02-30"),
            "tag",
            release_commit,
            tagged_runbook_text,
            descendant,
            "invalid post-push verification date",
        ),
        (
            "post-push-object-freshness",
            "post-push-record",
            valid_tagged_header,
            valid_post_push.replace(tag_object, stale_object),
            "tag",
            release_commit,
            tagged_runbook_text,
            descendant,
            "publication post-push freshness: annotated tag object",
        ),
        (
            "post-push-target-freshness",
            "post-push-record",
            valid_tagged_header,
            valid_post_push.replace(tag_target, stale_target),
            "tag",
            release_commit,
            tagged_runbook_text,
            descendant,
            "publication post-push freshness: closing commit",
        ),
        (
            "post-push-run-required",
            "post-push-record",
            valid_tagged_header,
            valid_post_push.replace(
                "- **Post-push hosted run:** `123456`\n",
                "",
            ),
            "tag",
            release_commit,
            tagged_runbook_text,
            descendant,
            "publication post-push record required",
        ),
    )

    missed: dict[str, list[str]] = {}
    with tempfile.TemporaryDirectory(prefix="invariant-scan-R12-status-") as raw:
        fixture = Path(raw)
        state_path = fixture / "STATE.md"
        runbook = fixture / "publication-control-runbook.md"
        runbook.write_text("# planted publication control\n")

        cycle_check.newest_closed_release = lambda _files: (
            cycle_check.ClosedRelease(
                runbook=runbook,
                tag=tag,
                release_commit=tag_target,
                recorded_tag_object=tag_object,
            )
        )
        for (
            name,
            group,
            header,
            measured_object,
            measured_target,
            ancestry,
            expected,
        ) in legacy_scenarios:
            state_path.write_text(f"# State\n\n{header}\n")

            def measured_legacy_ref(
                _root: Path,
                *args: str,
            ) -> str | None:
                if args == ("rev-parse", tag):
                    return measured_object
                if args == ("rev-parse", f"{tag}^{{}}"):
                    return measured_target
                if args == ("cat-file", "-t", tag_object):
                    return "tag"
                raise AssertionError(f"unexpected planted git query: {args}")

            cycle_check.git_output = measured_legacy_ref
            cycle_check.git_status = lambda _root, *_args: ancestry
            errors: list[str] = []
            cycle_check.check_publication_status(
                fixture,
                [runbook],
                errors,
            )
            if not any(expected in error for error in errors):
                missed.setdefault(group, []).append(name)

        cycle_check.newest_closed_release = lambda _files: (
            cycle_check.ClosedRelease(
                runbook=runbook,
                tag=tag,
                release_commit=release_commit,
                recorded_tag_object=None,
            )
        )
        for (
            name,
            group,
            header,
            body,
            measured_type,
            measured_parent,
            target_text,
            head,
            expected,
        ) in tagged_scenarios:
            state_path.write_text(f"# State\n\n{header}\n{body}")

            def measured_tagged_ref(
                _root: Path,
                *args: str,
            ) -> str | None:
                if args == ("rev-parse", tag):
                    return tag_object
                if args == ("rev-parse", f"{tag}^{{}}"):
                    return tag_target
                if args == ("cat-file", "-t", tag_object):
                    return measured_type
                if args == ("rev-parse", f"{tag_target}^"):
                    return measured_parent
                if args == ("show", f"{tag_target}:{runbook.name}"):
                    return target_text
                if args == ("rev-parse", "HEAD"):
                    return head
                raise AssertionError(f"unexpected planted git query: {args}")

            cycle_check.git_output = measured_tagged_ref
            cycle_check.git_status = lambda _root, *_args: (0, "")
            errors = []
            cycle_check.check_publication_status(
                fixture,
                [runbook],
                errors,
            )
            if not any(expected in error for error in errors):
                missed.setdefault(group, []).append(name)

        legacy_section = (
            "\n- **Cycle closed:** 2026-07-29\n"
            "- **Release disposition:** release (as of 2026-07-29)\n"
            f"- **Release:** `{tag}`\n"
            f"- **Release commit:** `{release_commit}`\n"
            f"- **Annotated tag object:** `{tag_object}`\n"
        )

        def recorded_commit_type(_root: Path, *args: str) -> str | None:
            if args == ("cat-file", "-t", release_commit):
                return "commit"
            raise AssertionError(f"unexpected planted git query: {args}")

        cycle_check.git_output = recorded_commit_type
        errors = []
        cycle_check.check_release_record(
            runbook,
            legacy_section,
            fixture,
            1,
            errors,
            verify_local_tag_refs=False,
            require_dated_disposition=True,
            require_tagged_closing_commit=True,
        )
        expected = "declared closed cycle must use the tagged-closing protocol"
        if not any(expected in error for error in errors):
            missed.setdefault("tagged-closing-protocol", []).append(
                "prechange-active-tag-object"
            )

        scope_path = fixture / "scope-control-runbook.md"
        declaration = cycle_check.ScopeDeclaration(
            version=1,
            disposition_intent="release",
            allow=("AGENTS.md",),
            release_authorities=("Cargo.toml",),
            forbid=("apps/**", "Cargo.lock"),
        )
        errors = []
        cycle_check.validate_declared_scope(
            declaration,
            (
                "Cargo.toml",
                "apps/cored/Cargo.toml",
                "Cargo.lock",
            ),
            (
                "apps/cored/Cargo.toml",
                "Cargo.lock",
            ),
            set(),
            False,
            scope_path,
            fixture,
            errors,
        )
        expected_scope_failures = (
            "release-authority set rejects apps/cored/Cargo.toml",
            "release-authority set rejects Cargo.lock",
            "diff rejects apps/cored/Cargo.toml",
            "diff rejects Cargo.lock",
        )
        if not all(
            any(expected in error for error in errors)
            for expected in expected_scope_failures
        ):
            missed.setdefault("declared-scope", []).append(
                "v0.22-release-paths"
            )

        active_retention_cycle = cycle_check.resolve_cycle(root).name
        valid_retention_pattern = (
            cycle_check.expected_review_export_retention_pattern(
                active_retention_cycle
            )
        )
        (fixture / "repomix.config.json").write_text(
            json.dumps(
                {
                    "ignore": {
                        "customPatterns": [
                            f"{valid_retention_pattern}.stale"
                        ]
                    }
                }
            )
            + "\n"
        )
        errors = []
        cycle_check.check_review_export_retention_pattern(
            fixture,
            active_retention_cycle,
            errors,
        )
        if not any(
            "review-export retention pattern for " in error
            for error in errors
        ):
            missed.setdefault("review-export-retention", []).append(
                "stale-retention-pattern"
            )

        trigger_path = fixture / "trigger-control.md"
        trigger_cycle_parts = cycle_check.TRIGGER_IDENTITY_FORWARD_BOUNDARY
        active_trigger_cycle = "v" + ".".join(
            str(part) for part in trigger_cycle_parts
        )
        prior_trigger_cycle = (
            f"v{trigger_cycle_parts[0]}.{trigger_cycle_parts[1] - 1}"
        )
        legacy_trigger_text = (
            "# Trigger control\n\n"
            "### Dated operational-residual dispositions\n\n"
            "| subject | disposition | trigger | measured observation |\n"
            "|---|---|---|---|\n"
            "| planted event | deferred | an operator session | "
            "no operator session occurred |\n"
        )
        errors = []
        trigger_rows = cycle_check.check_trigger_table(
            trigger_path,
            legacy_trigger_text,
            cycle_check.DATED_DISPOSITIONS_HEADING,
            "subject",
            fixture,
            errors,
        )
        expected_trigger_failure = (
            "trigger-bearing row 'planted event' requires a valid dated "
            "measured observation"
        )
        if trigger_rows != 1 or not any(
            expected_trigger_failure in error for error in errors
        ):
            missed.setdefault("trigger-freshness", []).append(
                "missing-trigger-measurement-date"
            )

        trigger_text = (
            "# Trigger control\n\n"
            "### Dated operational-residual dispositions\n\n"
            "| subject | disposition | trigger | Measured 2026-07-30 |\n"
            "|---|---|---|---|\n"
            "| planted event | deferred | an operator session | "
            f"{active_trigger_cycle} — no operator session occurred |\n"
        )
        errors = []
        trigger_rows = cycle_check.check_trigger_table(
            trigger_path,
            trigger_text,
            cycle_check.DATED_DISPOSITIONS_HEADING,
            "subject",
            fixture,
            errors,
            active_trigger_cycle,
        )
        if trigger_rows != 1 or not any(
            expected_trigger_failure in error for error in errors
        ):
            missed.setdefault("trigger-freshness", []).append(
                "header-only-trigger-measurement-date"
            )

        stale_trigger_text = trigger_text.replace(
            f"{active_trigger_cycle} — no operator session occurred",
            f"{prior_trigger_cycle} · 2026-07-30 — "
            "no operator session occurred",
        )
        errors = []
        trigger_rows = cycle_check.check_trigger_table(
            trigger_path,
            stale_trigger_text,
            cycle_check.DATED_DISPOSITIONS_HEADING,
            "subject",
            fixture,
            errors,
            active_trigger_cycle,
        )
        expected_cycle_failure = (
            "trigger-bearing row 'planted event' requires a measured "
            f"observation naming active cycle {active_trigger_cycle!r}"
        )
        if trigger_rows != 1 or not any(
            expected_cycle_failure in error for error in errors
        ):
            missed.setdefault("trigger-freshness", []).append(
                "stale-trigger-cycle-identity"
            )

        cycles = fixture / "docs" / "cycles"
        cycles.mkdir(parents=True)
        prior_runbook = (
            cycles
            / f"TASKS-{prior_trigger_cycle}-EXECUTION.md"
        )
        active_runbook = (
            cycles
            / f"TASKS-{active_trigger_cycle}-EXECUTION.md"
        )
        prior_runbook.write_text(
            "# Prior trigger control\n\n"
            "## Deferred means deferred\n\n"
            "| Deferred item | Unchanged trigger | measured observation |\n"
            "|---|---|---|\n"
            "| planted carry-forward | still active | "
            f"{prior_trigger_cycle} · 2026-07-30 — measured |\n"
        )
        active_text = (
            "# Active trigger control\n\n"
            "## Deferred means deferred\n\n"
            "| Deferred item | Unchanged trigger | measured observation |\n"
            "|---|---|---|\n"
            "| active baseline | still active | "
            f"{active_trigger_cycle} · 2026-07-30 — measured |\n"
        )
        active_runbook.write_text(active_text)
        errors = []
        cycle_check.check_deferred_carry_forward(
            active_runbook,
            active_text,
            fixture,
            errors,
        )
        expected_carry_failure = (
            "deferred subject 'planted carry-forward' from immediately prior "
        )
        if not any(
            expected_carry_failure in error for error in errors
        ):
            missed.setdefault("trigger-carry-forward", []).append(
                "silently-dropped-trigger-subject"
            )

    population_node = "tests/test_population.py::test_on_site"
    local_population = {
        "schema_version": 1,
        "collected": 1,
        "passed": 1,
        "failed": 0,
        "on_site": [population_node],
        "skipped": [],
    }
    unmarked_hosted_population = {
        "schema_version": 1,
        "collected": 1,
        "passed": 0,
        "failed": 0,
        "on_site": [population_node],
        "skipped": [
            {
                "node_id": population_node,
                "reason": "planted on-site environment difference",
                "markers": ["skipif"],
            }
        ],
    }
    try:
        local_summary = test_population.parse_summary(
            local_population,
            "local planted control",
        )
        hosted_summary = test_population.parse_summary(
            unmarked_hosted_population,
            "hosted planted control",
        )
        test_population.compare_populations(local_summary, hosted_summary)
    except test_population.PopulationError:
        pass
    else:
        missed.setdefault("test-population", []).append("unmarked-skip")

    coverage_path = root / "apps/cored/src/main.rs"
    coverage_source = production_text(
        coverage_path.relative_to(root),
        coverage_path.read_text(),
    )
    assessment_call = ".assess_source_window_coverage_before_insert("
    append_call = ".append_new("
    assessment_position = coverage_source.find(assessment_call)
    append_position = coverage_source.find(append_call)
    if (
        coverage_source.count(assessment_call) != 1
        or append_position < 0
        or assessment_position > append_position
    ):
        missed.setdefault("coverage-detection", []).append(
            "overlap-before-insert"
        )
    partitioned_call = (
        ".assess_source_window_coverage_before_insert(sel.source.id(), &docs)"
    )
    if coverage_source.count(partitioned_call) != 1:
        missed.setdefault("coverage-detection", []).append(
            "per-source-partition"
        )

    findings: list[str] = []
    for group, names in missed.items():
        marker = PUBLICATION_CONTROL_MARKERS[group]
        if group == "test-population":
            source_relative = "tools/test_population.py"
        elif group == "coverage-detection":
            source_relative = "apps/cored/src/main.rs"
        else:
            source_relative = "tools/cycle_check.py"
        source_path = root / source_relative
        source = source_path.read_text()
        if source.count(marker) != 1:
            raise ConfigError(
                f"{source_relative}: R12 marker {marker!r} must occur once"
            )
        line = source.count("\n", 0, source.index(marker)) + 1
        if group == "test-population":
            finding_kind = "test-population planted controls"
        elif group == "coverage-detection":
            finding_kind = "coverage-detection planted controls"
        elif group == "review-export-retention":
            finding_kind = "review-export-retention planted controls"
        else:
            finding_kind = "publication planted controls"
        findings.append(
            f"{source_relative}:{line}: {finding_kind} "
            f"were not detected: {', '.join(names)}"
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
    "R11": r11_findings,
    "R12": r12_findings,
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
