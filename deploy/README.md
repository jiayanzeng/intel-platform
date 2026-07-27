# Deploying the scheduler

The shell scheduler (`intel_shell.scheduler`) automates pipeline runs on a
per-source cadence. Pick one of two ways to drive it.

## Option A — systemd timer (recommended)

Let the OS own the clock and run the scheduler one-shot each firing:

```bash
sudo cp deploy/intel-pipeline.service /etc/systemd/system/
sudo cp deploy/intel-pipeline.timer   /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now intel-pipeline.timer
systemctl list-timers intel-pipeline.timer      # confirm next run
journalctl -u intel-pipeline.service -f          # watch runs
```

Each firing runs `python3 -m intel_shell.scheduler --once`, which executes only
the jobs whose cadence (from `config/schedule.json`) has come due. The timer
tick can be finer than any job cadence without over-fetching.

## Option B — in-process loop

For a container or a quick `nohup`, run the scheduler as a long-lived process:

```bash
PYTHONPATH=shell python3 -m intel_shell.scheduler --tick 60
```

It ticks every `--tick` seconds and fires due jobs itself. `data/scheduler_state.json`
records last-run times so a restart resumes the cadence instead of stampeding.

## Preview without running

```bash
PYTHONPATH=shell python3 -m intel_shell.scheduler --dry-run
```

## Notes

- Adjust `WorkingDirectory`, `User`/`Group`, and the `Environment=` lines in the
  service unit to your install path and secrets (`CORE_URL`, `CORE_TOKEN`,
  `LLM_BASE_URL`, `API_KEY_PEPPER`).
- A net-enabled `cored` also requires
  `INTEL_CRAWLER_CONTACT=<operator-email-or-contact-URL>`. It refuses startup
  when the value is missing, empty, or a placeholder; keep the
  `intel-platform` product token structural so robots group selection matches
  the exact User-Agent sent on the wire.
- Cadence granularity is per **sector**, which is what the core's `/ingest`
  endpoint exposes. True per-*source* cadence (multiple feeds within one sector
  on different clocks) would need the core to accept source ids on `/ingest`;
  that is a core change, out of scope for the shell.
