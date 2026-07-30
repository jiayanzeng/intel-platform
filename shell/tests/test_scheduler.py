"""Tests for the scheduler — pure logic, injected clock, no sleeping/network."""

from __future__ import annotations

import json
from pathlib import Path

from intel_shell import scheduler
from intel_shell.scheduler import Job, JobSpec, ScheduleConfig, Scheduler, build_jobs, due_jobs


ROOT = Path(__file__).resolve().parents[2]


class FakeRunner:
    """Records calls instead of touching the pipeline or the core."""

    def __init__(self):
        self.calls: list[tuple[str, tuple]] = []

    def full(self, client, llm_enrich):
        self.calls.append(("full", (client, llm_enrich)))

    def refresh(self, client, llm_enrich):
        self.calls.append(("refresh", (client, llm_enrich)))

    def ingest(self, client, sectors=None, sources=None):
        self.calls.append(
            (
                "ingest",
                (client, tuple(sectors or ()), tuple(sources or ())),
            )
        )


def test_due_jobs_filters_by_next_run():
    a = Job("a", 10, lambda: None, next_run=5)
    b = Job("b", 10, lambda: None, next_run=15)
    assert [j.name for j in due_jobs([a, b], now=10)] == ["a"]
    assert [j.name for j in due_jobs([a, b], now=20)] == ["a", "b"]


def test_build_jobs_fans_out_per_sector():
    sched = ScheduleConfig(jobs=[
        JobSpec(client="acme", interval=1800, sectors={"science": 3600, "technology": 900}),
        JobSpec(client="quant", interval=7200),
    ])
    jobs = {j.name: j for j in build_jobs(sched, FakeRunner())}
    assert "acme:ingest:science" in jobs and jobs["acme:ingest:science"].interval == 3600
    assert "acme:ingest:technology" in jobs and jobs["acme:ingest:technology"].interval == 900
    assert "acme:refresh" in jobs and jobs["acme:refresh"].interval == 1800
    # No per-source/per-sector cadence -> a single full-run job.
    assert "quant:full" in jobs and jobs["quant:full"].interval == 7200


def test_build_jobs_fans_out_per_source():
    # techwire and osdaily both live in the `technology` sector, yet ask for
    # different intervals: the true-per-source cadence T3 unlocks.
    sched = ScheduleConfig(jobs=[
        JobSpec(client="acme", interval=1800,
                sources={"techwire": 900, "osdaily": 1800}),
    ])
    jobs = {j.name: j for j in build_jobs(sched, FakeRunner())}
    assert jobs["acme:ingest-source:techwire"].interval == 900
    assert jobs["acme:ingest-source:osdaily"].interval == 1800
    assert "acme:refresh" in jobs

    # They are genuinely independent clocks: after both fire at t0, only the
    # 900s source is due again at t0+900; both are due at t0+1800.
    clock = {"t": 0.0}
    s = Scheduler(list(jobs.values()), now_fn=lambda: clock["t"], log=lambda *_: None)
    assert set(s.tick(now=0.0)) == {
        "acme:ingest-source:techwire", "acme:ingest-source:osdaily", "acme:refresh",
    }
    assert s.tick(now=900.0) == ["acme:ingest-source:techwire"]
    assert set(s.tick(now=1800.0)) == {
        "acme:ingest-source:techwire", "acme:ingest-source:osdaily", "acme:refresh",
    }


def test_job_actions_call_the_runner_correctly():
    runner = FakeRunner()
    sched = ScheduleConfig(jobs=[
        JobSpec(client="acme", interval=1800, llm_enrich=True,
                sources={"techwire": 900}, sectors={"science": 3600}),
    ])
    jobs = {j.name: j for j in build_jobs(sched, runner)}
    jobs["acme:ingest-source:techwire"].action()
    jobs["acme:ingest:science"].action()
    jobs["acme:refresh"].action()
    # per-source ingest passes sources=[…]; per-sector passes sectors=[…]
    assert ("ingest", ("acme", (), ("techwire",))) in runner.calls
    assert ("ingest", ("acme", ("science",), ())) in runner.calls
    assert ("refresh", ("acme", True)) in runner.calls


def test_tick_runs_due_jobs_and_reschedules():
    runner = FakeRunner()
    jobs = build_jobs(
        ScheduleConfig(jobs=[JobSpec(client="acme", interval=100)]), runner
    )
    clock = {"t": 1000.0}
    s = Scheduler(jobs, now_fn=lambda: clock["t"], log=lambda *_: None)
    # First tick: due immediately.
    assert s.tick(now=1000.0) == ["acme:full"]
    # Not due one interval later minus a bit.
    assert s.tick(now=1050.0) == []
    # Due again at +interval.
    assert s.tick(now=1100.0) == ["acme:full"]
    assert len(runner.calls) == 2


def test_failing_job_does_not_stop_the_tick():
    def boom():
        raise RuntimeError("kaboom")

    ran = []
    jobs = [
        Job("bad", 10, boom, next_run=0),
        Job("good", 10, lambda: ran.append(1), next_run=0),
    ]
    s = Scheduler(jobs, now_fn=lambda: 0.0, log=lambda *_: None)
    names = s.tick(now=0.0)
    assert names == ["bad", "good"]  # both attempted despite the exception
    assert ran == [1]


def test_state_persists_and_reseeds(tmp_path):
    state = tmp_path / "state.json"
    runner = FakeRunner()

    def make():
        return build_jobs(
            ScheduleConfig(jobs=[JobSpec(client="acme", interval=100)]), runner
        )

    s1 = Scheduler(make(), state_path=str(state), now_fn=lambda: 1000.0,
                   log=lambda *_: None)
    s1.tick(now=1000.0)
    saved = json.loads(state.read_text())
    assert saved["acme:full"] == 1000.0

    # A fresh scheduler started later reseeds next_run = last_run + interval,
    # so it is NOT immediately due at t=1050 but IS due at t=1100.
    s2 = Scheduler(make(), state_path=str(state), now_fn=lambda: 1050.0,
                   log=lambda *_: None)
    assert s2.tick(now=1050.0) == []
    assert s2.tick(now=1100.0) == ["acme:full"]


def test_load_schedule_parses_json(tmp_path):
    path = tmp_path / "schedule.json"
    path.write_text(json.dumps({
        "default_interval_seconds": 3600,
        "state_path": "data/s.json",
        "jobs": [{"client": "acme", "interval_seconds": 1800,
                  "sources": {"techwire": 900}, "sectors": {"science": 600}}],
    }))
    sched = scheduler.load_schedule(str(path))
    assert sched.default_interval == 3600
    assert sched.state_path == "data/s.json"
    assert sched.jobs[0].client == "acme"
    assert sched.jobs[0].sources == {"techwire": 900}
    assert sched.jobs[0].sectors == {"science": 600}


def test_admitted_sec_source_has_an_explicit_resolvable_cadence():
    runner = FakeRunner()
    schedule = scheduler.load_schedule(str(ROOT / "config" / "schedule.json"))
    jobs = {job.name: job for job in build_jobs(schedule, runner)}

    sec = jobs["quant-desk:ingest-source:sec-edgar-usgaap"]
    filings = jobs["quant-desk:ingest-source:filings-digest"]
    refresh = jobs["quant-desk:refresh"]
    assert sec.interval == 600
    assert filings.interval == 7200
    assert refresh.interval == 7200
    assert "quant-desk:full" not in jobs

    sec.action()
    assert runner.calls == [
        ("ingest", ("quant-desk", (), ("sec-edgar-usgaap",)))
    ]
