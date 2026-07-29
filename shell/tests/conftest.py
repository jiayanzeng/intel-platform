from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest


SUMMARY_PREFIX = "test-population-summary: "
TESTS_DIR = Path(__file__).resolve().parent


def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("test population")
    group.addoption(
        "--population-summary",
        action="store_true",
        help="emit one stable JSON summary of the selected test population",
    )


def _skip_reason(longrepr: object) -> str:
    if isinstance(longrepr, tuple) and len(longrepr) == 3:
        reason = str(longrepr[2])
    else:
        reason = str(longrepr)
    return reason.removeprefix("Skipped: ").strip()


class PopulationSummary:
    def __init__(self, config: pytest.Config) -> None:
        self.config = config
        self.items: dict[str, pytest.Item] = {}
        self.passed: set[str] = set()
        self.failed: set[str] = set()
        self.skipped: dict[str, str] = {}

    def pytest_collection_finish(self, session: pytest.Session) -> None:
        self.items = {item.nodeid: item for item in session.items}

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        node_id = report.nodeid
        if report.skipped:
            self.skipped[node_id] = _skip_reason(report.longrepr)
            return
        if report.failed:
            self.failed.add(node_id)
            return
        if report.when == "call" and report.passed:
            self.passed.add(node_id)

    def pytest_sessionfinish(self) -> None:
        skipped = []
        for node_id, reason in sorted(self.skipped.items()):
            item = self.items.get(node_id)
            markers = (
                sorted({marker.name for marker in item.iter_markers()})
                if item is not None
                else []
            )
            skipped.append(
                {
                    "markers": markers,
                    "node_id": node_id,
                    "reason": reason,
                }
            )
        failed = self.failed - set(self.skipped)
        passed = self.passed - failed - set(self.skipped)
        summary: dict[str, Any] = {
            "collected": len(self.items),
            "failed": len(failed),
            "on_site": sorted(
                node_id
                for node_id, item in self.items.items()
                if item.get_closest_marker("on_site") is not None
            ),
            "passed": len(passed),
            "schema_version": 1,
            "skipped": skipped,
        }
        line = SUMMARY_PREFIX + json.dumps(
            summary,
            sort_keys=True,
            separators=(",", ":"),
        )
        reporter = self.config.pluginmanager.getplugin("terminalreporter")
        if reporter is None:
            sys.stdout.write(line + "\n")
        else:
            reporter.write_line(line)


def pytest_configure(config: pytest.Config) -> None:
    requested_paths = [
        Path(argument.split("::", 1)[0]).resolve()
        for argument in config.args
    ]
    if (
        config.getoption("--population-summary")
        and requested_paths == [TESTS_DIR]
    ):
        config.pluginmanager.register(
            PopulationSummary(config),
            "test-population-summary",
        )
