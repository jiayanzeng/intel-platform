"""Scheduler: run the pipeline automatically, on a per-source cadence.

This is the STATE.md "scheduler in the shell (pipeline.py on an interval /
systemd timer) with per-source cadence" step, and like everything else in the
shell it needs no `cargo build`. Two ways to run it:

  * **In-process loop** — `python3 -m intel_shell.scheduler` ticks forever,
    firing each job when it comes due. Good for a container/`nohup`.
  * **One-shot** — `python3 -m intel_shell.scheduler --once` runs whatever is
    due right now and exits. Point a systemd timer (or cron) at this and the
    OS owns the clock; see deploy/ for a ready unit + timer.

Since the core's `/ingest` now accepts a `sources` filter, cadence can be
expressed per *source* — two feeds in the same sector can run on independent
clocks. A job spec fans out into one ingest job per named source (`sources`)
and/or one per named sector (`sectors`), plus one client-level "refresh" job
that re-analyzes the archive and re-renders the brief:

    {"default_interval_seconds": 3600,
     "state_path": "data/scheduler_state.json",
     "jobs": [
       {"client": "acme-research", "interval_seconds": 1800,
        "sources": {"techwire": 900, "osdaily": 1800},  # source id -> cadence
        "sectors": {"science": 3600}},                  # sector id -> cadence
       {"client": "quant-desk", "interval_seconds": 7200}
     ]}

Here `techwire` and `osdaily` both live in the `technology` sector yet tick on
their own intervals — the true-per-source cadence the sector-granular v0.5
scheduler couldn't express. A spec with neither `sources` nor `sectors`
becomes a single full-run job.

The scheduling core (`Job`, `due_jobs`, `Scheduler.tick`) is pure and
time-injected, so it is unit-tested without sleeping or a running core.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
from dataclasses import dataclass, field
from typing import Callable, Protocol

from . import config, pipeline


# --- pure scheduling core -------------------------------------------------------


@dataclass
class Job:
    name: str
    interval: float  # seconds
    action: Callable[[], object]
    next_run: float = 0.0


def due_jobs(jobs: list[Job], now: float) -> list[Job]:
    """Jobs whose next_run has arrived, in stable (name) order."""
    return sorted((j for j in jobs if j.next_run <= now), key=lambda j: j.name)


# --- runners --------------------------------------------------------------------


class Runner(Protocol):
    """What a scheduler needs to be able to invoke. Injectable for tests."""

    def full(self, client: str, llm_enrich: bool) -> object: ...
    def refresh(self, client: str, llm_enrich: bool) -> object: ...
    def ingest(
        self,
        client: str,
        sectors: list[str] | None = None,
        sources: list[str] | None = None,
    ) -> object: ...


@dataclass
class PipelineRunner:
    """The production runner: binds pipeline entry points to fixed paths."""

    subs_path: str | None = None
    data_dir: str = "data"
    core_url: str = config.CORE_URL

    def full(self, client: str, llm_enrich: bool) -> object:
        return pipeline.run(client, self.subs_path, self.data_dir, self.core_url,
                            llm_enrich)

    def refresh(self, client: str, llm_enrich: bool) -> object:
        return pipeline.run(client, self.subs_path, self.data_dir, self.core_url,
                            llm_enrich, skip_ingest=True)

    def ingest(
        self,
        client: str,
        sectors: list[str] | None = None,
        sources: list[str] | None = None,
    ) -> object:
        return pipeline.ingest_only(
            client, self.subs_path, self.core_url, sectors=sectors, sources=sources
        )


# --- schedule config ------------------------------------------------------------


@dataclass
class JobSpec:
    client: str
    interval: float
    llm_enrich: bool = False
    sources: dict[str, float] = field(default_factory=dict)  # source id -> cadence
    sectors: dict[str, float] = field(default_factory=dict)  # sector id -> cadence


@dataclass
class ScheduleConfig:
    default_interval: float = 3600.0
    state_path: str | None = None
    jobs: list[JobSpec] = field(default_factory=list)


def load_schedule(path: str) -> ScheduleConfig:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    default = float(raw.get("default_interval_seconds", 3600))
    specs = []
    for j in raw.get("jobs", []):
        specs.append(
            JobSpec(
                client=j["client"],
                interval=float(j.get("interval_seconds", default)),
                llm_enrich=bool(j.get("llm_enrich", False)),
                sources={k: float(v) for k, v in j.get("sources", {}).items()},
                sectors={k: float(v) for k, v in j.get("sectors", {}).items()},
            )
        )
    return ScheduleConfig(
        default_interval=default,
        state_path=raw.get("state_path"),
        jobs=specs,
    )


def build_jobs(schedule: ScheduleConfig, runner: Runner) -> list[Job]:
    """Turn a schedule into concrete Jobs bound to `runner`.

    Each named source (`sources`) becomes one `…:ingest-source:<id>` Job on its
    own clock; each named sector (`sectors`) becomes one `…:ingest:<id>` Job.
    Any spec with at least one of those also gets a client `…:refresh` Job that
    re-analyzes the archive. A spec with neither becomes a single `…:full` Job.
    """
    jobs: list[Job] = []
    for spec in schedule.jobs:
        for source, cadence in spec.sources.items():
            jobs.append(
                Job(
                    name=f"{spec.client}:ingest-source:{source}",
                    interval=cadence,
                    action=(lambda c=spec.client, s=source: runner.ingest(c, sources=[s])),
                )
            )
        for sector, cadence in spec.sectors.items():
            jobs.append(
                Job(
                    name=f"{spec.client}:ingest:{sector}",
                    interval=cadence,
                    action=(lambda c=spec.client, s=sector: runner.ingest(c, sectors=[s])),
                )
            )
        if spec.sources or spec.sectors:
            jobs.append(
                Job(
                    name=f"{spec.client}:refresh",
                    interval=spec.interval,
                    action=(lambda c=spec.client, e=spec.llm_enrich: runner.refresh(c, e)),
                )
            )
        else:
            jobs.append(
                Job(
                    name=f"{spec.client}:full",
                    interval=spec.interval,
                    action=(lambda c=spec.client, e=spec.llm_enrich: runner.full(c, e)),
                )
            )
    return jobs


# --- the scheduler ---------------------------------------------------------------


class Scheduler:
    def __init__(
        self,
        jobs: list[Job],
        state_path: str | None = None,
        now_fn: Callable[[], float] = time.time,
        sleep_fn: Callable[[float], None] = time.sleep,
        log: Callable[[str], None] = print,
    ):
        self.jobs = jobs
        self.state_path = state_path
        self._now = now_fn
        self._sleep = sleep_fn
        self._log = log
        self._seed_next_runs()

    def _seed_next_runs(self) -> None:
        """Set each job's next_run from persisted last-run times.

        A job we've never seen runs at the first tick; a job we have seen runs
        one interval after it last ran (so a restart doesn't stampede, and a
        job that came due while we were down fires immediately).
        """
        state = self._load_state()
        now = self._now()
        for job in self.jobs:
            last = state.get(job.name)
            job.next_run = (last + job.interval) if last is not None else now

    def _load_state(self) -> dict[str, float]:
        if not self.state_path or not os.path.exists(self.state_path):
            return {}
        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                return {k: float(v) for k, v in json.load(f).items()}
        except (ValueError, OSError):
            return {}

    def _save_state(self, last_runs: dict[str, float]) -> None:
        if not self.state_path:
            return
        directory = os.path.dirname(os.path.abspath(self.state_path))
        os.makedirs(directory, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=directory, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(last_runs, f, indent=2)
            os.replace(tmp, self.state_path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)

    def tick(self, now: float | None = None) -> list[str]:
        """Run every due job once; reschedule and persist. Returns names run."""
        now = self._now() if now is None else now
        ran: list[str] = []
        last_runs = self._load_state()
        for job in due_jobs(self.jobs, now):
            self._log(f"[scheduler] running {job.name}")
            try:
                job.action()
            except Exception as e:  # noqa: BLE001 — one bad job never stops the loop
                self._log(f"[scheduler] job {job.name} failed: {e}")
            job.next_run = now + job.interval
            last_runs[job.name] = now
            ran.append(job.name)
        if ran:
            self._save_state(last_runs)
        return ran

    def run_once(self) -> list[str]:
        return self.tick()

    def run_forever(self, tick_seconds: float = 60.0) -> None:
        self._log(
            f"[scheduler] starting: {len(self.jobs)} job(s), "
            f"tick every {tick_seconds:.0f}s. Ctrl-C to stop."
        )
        try:
            while True:
                self.tick()
                self._sleep(tick_seconds)
        except KeyboardInterrupt:
            self._log("[scheduler] stopped.")

    def describe(self) -> list[str]:
        now = self._now()
        return [
            f"{j.name}: every {j.interval:.0f}s, next in {max(0.0, j.next_run - now):.0f}s"
            for j in sorted(self.jobs, key=lambda j: j.name)
        ]


# --- CLI ------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="intel-platform scheduler (shell)")
    ap.add_argument("--config", default="config/schedule.json",
                    help="path to schedule.json")
    ap.add_argument("--subs", default=None, help="path to subscriptions.json")
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--core-url", default=config.CORE_URL)
    ap.add_argument("--tick", type=float, default=60.0,
                    help="seconds between ticks in loop mode")
    ap.add_argument("--once", action="store_true",
                    help="run all currently-due jobs once and exit (for cron/systemd)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the schedule and exit without running anything")
    args = ap.parse_args(argv)

    try:
        schedule = load_schedule(args.config)
    except FileNotFoundError:
        print(f"error: schedule config not found at {args.config}", file=sys.stderr)
        return 1

    runner = PipelineRunner(subs_path=args.subs, data_dir=args.data_dir,
                            core_url=args.core_url)
    jobs = build_jobs(schedule, runner)
    if not jobs:
        print("error: schedule has no jobs", file=sys.stderr)
        return 1

    scheduler = Scheduler(jobs, state_path=schedule.state_path)

    if args.dry_run:
        print("schedule:")
        for line in scheduler.describe():
            print(f"  {line}")
        return 0

    if args.once:
        ran = scheduler.run_once()
        print(f"[scheduler] ran {len(ran)} job(s): {', '.join(ran) or '(none due)'}")
        return 0

    scheduler.run_forever(tick_seconds=args.tick)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
