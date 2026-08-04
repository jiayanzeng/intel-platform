# intel-platform local operations reference

Status: VERIFIED — Tier A creation and every profile transition executed
successfully on 2026-07-27 (Asia/Shanghai)

This is the operator reference for running intel-platform's model services on
the Ubuntu `5080` server, and for switching the server between the
**intel-platform** and **Athenaeum** projects. It is modeled on Athenaeum's
`OPERATIONS.md` so an agent can operate both projects with one mental model:
containers are created once with `docker run -d --name`, then switched with
`docker start`/`docker stop` over SSH. Never use `docker run --rm` for routine
operation, and never recreate an existing named container — resume it.

## Quick control from the MacBook

The preferred interface is now one command from the intel-platform checkout:

```bash
cd ~/intel-platform

./run models status
./run models intel
./run models athenaeum
./run models athenaeum-bulk
./run models stop
```

These commands control both sides of the boundary: the named server containers
and the managed Mac tunnels. A switch first retires the old project's tunnel,
then stops conflicting GPU roles, starts the requested profile in VRAM-safe
order, polls the real server-local `/health` endpoints, proves the inactive GPU
port is down where applicable, and creates only the requested project's local
tunnel. It never calls `docker run`, `docker rm`, `docker pull`, or modifies a
model. A missing named container, foreign local listener, or failed health
check is a refusal. A profile switch also refuses partial or overlapping GPU
state; `models stop` is the explicit safe recovery for that state.

After a Mac reboot, run the command in **Terminal.app**. It creates the shared
port-2222 bridge when absent and then completes the switch. Once the bridge
exists, the same command also works inside Codex. If asked in chat to switch or
resume a project, Codex may launch the command in Terminal.app and verify the
result; the operator does not need to prepare the models manually.

`./run models stop` is the all-project pause: it stops all five named model
containers, closes both project model tunnels, and closes the shared SSH
bridge. Containers, images, models, repositories, and configuration remain
intact, so either project can later be restored with one profile command.

The all-five inventory dependency is deliberate cross-project coupling. This
single controller must be able to stop every conflicting role before selecting
either project's profile, so a missing one of the five named containers means
the known inventory is incomplete and routine switching refuses rather than
narrowing its view. Malformed remote inventory is likewise reported as
`ProfileError`, never leaked as a parser exception.

The `./run models` dispatch deliberately calls bare `python3` instead of
`ensure_venv`. The controller is standard-library-only recovery tooling and
must work immediately after a reboot, before this repository's virtual
environment exists.

### Measured one-click results

| Command | Actual result on 2026-07-27 |
|---|---|
| `./run models intel` | 8080 + 8081 healthy; 18080 + 18081 healthy; Athenaeum GPU roles stopped |
| `./run models athenaeum` | 8080 + 8082 healthy; 8081 down; 28080 + 28082 healthy; intel roles stopped |
| `./run models athenaeum-bulk` | 8081 + 8082 healthy; 8080 down; 28081 + 28082 healthy; all generation stopped |
| `./run models stop` | all five containers stopped; ports 2222, 18080–18081, and 28080–28082 released; control sockets removed |
| Terminal.app resume with no bridge | bridge recreated; intel pair and tunnel restored; both tunneled health checks HTTP 200 |

---

## 0. The one rule: profiles are mutually exclusive

Both projects claim host ports **8080** and **8081**, and both need the GPU.
The two projects are never developed concurrently, so the server is always in
exactly one profile:

| Profile | Running containers | Host ports in use |
|---|---|---|
| **Athenaeum serving** | `athenaeum-gen`, `athenaeum-embed-cpu` | 8080, 8082 |
| **Athenaeum bulk** | `athenaeum-embed-gpu`, `athenaeum-embed-cpu` | 8081, 8082 |
| **intel-platform** | `intel-gen`, `intel-embed` (+ `athenaeum-embed-cpu` may stay up) | 8080, 8081 (8082) |

Switching profiles always **stops the other project's GPU containers first**,
then starts this project's. Stopped named containers do not hold their ports.
If two profiles are ever started together by mistake, Docker fails loudly at
port bind — treat that as the safety net, not a workflow.

`athenaeum-embed-cpu` (CPU-only, port 8082, `--restart unless-stopped`)
conflicts with nothing and normally stays running through all switches. Stop it
only if you need its RAM back.

---

## 1. Ubuntu Server 26.04 — reference

| Item | Value |
|---|---|
| Host | `192.168.0.192` |
| SSH user | `jia` |
| Models | `/data/models` |
| Chat container | `intel-gen`, host port 8080, GPU |
| Embedding container | `intel-embed`, host port 8081, GPU |

### First-creation command: chat model

**Tier A — run once, only if `docker ps -a` shows no `intel-gen`.** A stopped
existing container must be resumed with `docker start`, never recreated.
Flags are byte-identical to the previous manual workflow; only `--rm` is
replaced by `-d --name` so the container persists across sessions.

```bash
docker run -d --name intel-gen --gpus all \
  -v /data/models:/models \
  -p 8080:8080 \
  ghcr.io/ggml-org/llama.cpp:server-cuda13 \
  -m /models/gemma4-26B/gemma-4-26B-A4B-it-UD-IQ4_XS.gguf \
  -ngl 99 --parallel 1 -c 32768 \
  --flash-attn on \
  --host 0.0.0.0 --port 8080
```

Note: this is the same GGUF and image as `athenaeum-gen`, but a **separate
container** — the context size (32768 vs 8192) and flash-attn settings differ.
Do not reuse or modify `athenaeum-gen` for intel-platform work.

### First-creation command: embedding model

**Tier A — run once, only if no `intel-embed` exists.** The llama.cpp model
flags are preserved verbatim from the manual workflow (embeddinggemma's pooling
comes from its GGUF metadata; no `--pooling` flag was used before and none is
added now). The Docker-level health override is the measured correction
explained below.

```bash
docker run -d --name intel-embed --gpus all \
  -v /data/models:/models \
  -p 8081:8081 \
  --health-cmd 'curl -f http://localhost:8081/health' \
  ghcr.io/ggml-org/llama.cpp:server-cuda13 \
  -m /models/embeddinggemma-300M-Q8_0.gguf \
  --embeddings --host 0.0.0.0 --port 8081 -c 2048
```

The health override is the one correction discovered by Tier A execution. The
image's inherited check is hard-coded to internal port 8080. The container
created on 2026-07-27 correctly listens on 8081 and returns HTTP 200 with
`{"status":"ok"}`, but Docker labels that already-created container
`unhealthy` because its inherited probe repeatedly curls the wrong port.
Routine operation must use the explicit HTTP gate, as `./run models` does; do
not recreate the working named container merely to change this cosmetic label.
The corrected reference command above prevents the false label if disaster
recovery ever requires first creation again.

Neither GPU container gets a `--restart` policy — deliberately, matching the
Athenaeum convention. After a server reboot everything GPU is down until a
switch command deliberately establishes a profile; a reboot can never start a
GPU container into the wrong profile.

### VRAM note

The manual workflow ran both containers concurrently (26B IQ4_XS + 300M Q8 on
one 16 GB card), so the switch commands below start both. Start order is
`intel-gen` first (largest allocation), then `intel-embed`. If llama.cpp ever
fails allocation after a driver or model change, start `intel-gen` alone,
confirm health, then start `intel-embed`.

### Server-local verification

```bash
docker ps --format 'table {{.Names}}\t{{.Ports}}\t{{.Status}}'
curl -fsS http://127.0.0.1:8080/health
curl -fsS http://127.0.0.1:8081/health
```

Both health responses should be `{"status":"ok"}`. Model load after
`docker start` can take tens of seconds; poll rather than assuming failure.
For the existing `intel-embed`, this HTTP result is authoritative over Docker's
known wrong-port health label.

---

## 2. Switching projects (from the Mac)

Use the Quick control commands above for routine work. The lower-level SSH
sequences in this section remain recovery/reference commands and deliberately
do not manage Mac tunnels by themselves. If an operator uses a lower-level
sequence, they must also stop the old project tunnel; otherwise a local intel
alias can silently begin forwarding to Athenaeum after port 8080 changes
owners.

### Read-only preflight — run before any switch

```bash
ssh -o ConnectTimeout=8 jia@192.168.0.192 \
  "docker ps -a --filter name=athenaeum- --filter name=intel- \
  --format 'table {{.Names}}\t{{.Ports}}\t{{.Status}}'"
```

If SSH reports `No route to host`, stop: confirm the server is powered on and
still owns `192.168.0.192`. Do not run lifecycle commands blind.

### Switch to intel-platform

Stops both Athenaeum GPU roles (whichever profile was active), then starts the
intel pair in VRAM order:

```bash
cd ~/intel-platform
./run models intel
```

Lower-level server-only recovery form:

```bash
ssh jia@192.168.0.192 \
  'set -e
   docker stop athenaeum-gen athenaeum-embed-gpu >/dev/null 2>&1 || true
   docker start intel-gen
   docker start intel-embed'
```

Then verify:

```bash
curl -fsS http://192.168.0.192:8080/health
curl -fsS http://192.168.0.192:8081/health
```

### Switch back to Athenaeum (serving profile)

```bash
cd ~/intel-platform
./run models athenaeum
```

Lower-level server-only recovery form:

```bash
ssh jia@192.168.0.192 \
  'set -e
   docker stop intel-gen intel-embed >/dev/null 2>&1 || true
   docker start athenaeum-gen athenaeum-embed-cpu'
```

Then verify:

```bash
curl -fsS http://192.168.0.192:8080/health
curl -fsS http://192.168.0.192:8082/health
```

(For Athenaeum's bulk-embedding profile, use Athenaeum's own OPERATIONS.md —
the intel containers must be stopped first there too.) The integrated command
is:

```bash
cd ~/intel-platform
./run models athenaeum-bulk
```

### Restart one intel service

```bash
ssh jia@192.168.0.192 "docker restart intel-gen"
ssh jia@192.168.0.192 "docker restart intel-embed"
```

### Stop all intel-platform containers

For a complete all-project pause, including Mac tunnels and the shared bridge:

```bash
cd ~/intel-platform
./run models stop
```

Server-only recovery form for stopping just the intel pair:

```bash
ssh jia@192.168.0.192 "docker stop intel-gen intel-embed"
```

---

## 3. Mac tunnels — managed form

The previous manual tunnel (`ssh -N -L 18080:... -L 18081:...`) is unmanaged:
a failed port bind leaves a silent background process, and repeated invocations
accumulate zombies (this exact failure was observed on the Athenaeum side).
Keep the same local ports — **18080 → server 8080, 18081 → server 8081** — but
use a control socket so the tunnel can be checked and stopped deterministically.
The integrated controller creates it through the shared port-2222 bridge, so
the same form works from Terminal.app and Codex. Routine users should run
`./run models intel`; the commands below are the manual equivalent.

Start:

```bash
intel_tunnel_socket="${TMPDIR%/}/intel-llama-tunnel.sock"

lsof -nP -iTCP:18080 -sTCP:LISTEN   # must be empty before starting
lsof -nP -iTCP:18081 -sTCP:LISTEN

ssh -4 -p 2222 -f -N -M -S "$intel_tunnel_socket" \
  -o ExitOnForwardFailure=yes \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -L 18080:127.0.0.1:8080 \
  -L 18081:127.0.0.1:8081 \
  jia@127.0.0.1
```

Verify and stop:

```bash
intel_tunnel_socket="${TMPDIR%/}/intel-llama-tunnel.sock"

ssh -p 2222 -S "$intel_tunnel_socket" -O check jia@127.0.0.1
curl -fsS http://127.0.0.1:18080/health
curl -fsS http://127.0.0.1:18081/health

ssh -p 2222 -S "$intel_tunnel_socket" -O exit jia@127.0.0.1
```

Client configuration on the Mac is unchanged: generation at
`http://127.0.0.1:18080`, embeddings at `http://127.0.0.1:18081` (or the
direct LAN `http://192.168.0.192:8080` / `:8081` when tunnelling is
unnecessary). No local ports collide with Athenaeum's tunnels (8080–8082) or
its Codex-bridge alternates (28080–28082).

Port separation prevents bind conflicts; it does not prevent semantic
misrouting. Because both projects reuse server port 8080, an intel tunnel left
alive during an Athenaeum switch would begin exposing Athenaeum under the local
intel alias. `./run models` therefore closes both project model tunnels before
every server transition and starts only the selected project's tunnel.

---

## 4. Codex terminal access

The Codex terminal cannot route directly to `192.168.0.192`; Terminal.app can.
This distinction is literal. Tier A execution proved that
`osascript do shell script "ssh …"` still runs in the restricted subprocess
context and returns `No route to host`; the command must actually be entered in
Terminal.app (manually or with `tell application "Terminal" to do script`).
Both projects share **one** SSH bridge on localhost port 2222 — check for an
existing listener before creating another:

```bash
lsof -nP -iTCP:2222 -sTCP:LISTEN
```

If absent, create it from the normal Mac terminal (identical to the Athenaeum
bridge — reuse the same socket name so there is only ever one):

```bash
athenaeum_ssh_socket="${TMPDIR%/}/athenaeum-server-ssh.sock"

ssh -f -N -M -S "$athenaeum_ssh_socket" \
  -o ExitOnForwardFailure=yes \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -L 2222:127.0.0.1:22 \
  jia@192.168.0.192
```

For a post-reboot one-click resume requested from Codex, launch the integrated
command in Terminal.app:

```bash
osascript \
  -e 'tell application "Terminal"' \
  -e 'activate' \
  -e 'do script "cd ~/intel-platform && ./run models intel"' \
  -e 'end tell'
```

Replace the final profile with `athenaeum`, `athenaeum-bulk`, or `stop` as
needed. The command creates the bridge only when absent and verifies the full
result. Once port 2222 is healthy, Codex can run `./run models …` directly.

Inside the Codex terminal, every command in section 2 works by replacing the
SSH prefix `ssh jia@192.168.0.192` with `ssh -p 2222 jia@127.0.0.1`. For
example, the lower-level intel server switch is:

```bash
ssh -p 2222 jia@127.0.0.1 \
  'set -e
   docker stop athenaeum-gen athenaeum-embed-gpu >/dev/null 2>&1 || true
   docker start intel-gen
   docker start intel-embed'

ssh -p 2222 jia@127.0.0.1 "curl -fsS http://127.0.0.1:8080/health"
ssh -p 2222 jia@127.0.0.1 "curl -fsS http://127.0.0.1:8081/health"
```

---

+## Review-source projection of the protected manifest

The integrity authority remains `config/protected-artifacts.json`; the project-root
review export excludes that mixed-use manifest and carries this exact projection
instead. The projection retains every non-pin field and only those pin records
whose referenced bytes are themselves present in the review source set.
`./run export-check` derives both populations from tracked repository bytes and
fails if this block is stale, if its source remains exported, or if a configured
review-manifest exclusion has no matching projection.

<!-- REVIEW_SOURCE_PROJECTION:START source="config/protected-artifacts.json" -->
```json
{
  "schema_version": 2,
  "lifecycle": {
    "policy": "immutable_evidence",
    "live_harvest": "fresh_path_only",
    "admission": "append_only_chained_records_with_wire_evidence_and_operator_approval"
  },
  "artifacts": [
    {
      "path": "data/core.db",
      "sha256": "db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0",
      "bytes": 6729728,
      "purpose": "Protected live arXiv archive used for corpus migration and HC1 attestation evidence.",
      "provenance": "Live arXiv OAI-PMH archive with 1,764 documents; a later zero-document operator harvest advanced only the recorded cursor timestamp before these immutable bytes were admitted.",
      "admission": {
        "records": [
          {
            "task_id": "v0.10/A2",
            "date": "2026-07-25",
            "sha256": "db2f186e291c64192e567c9dfb979dd9877eb32b13c2ce2724a4acf1761a37a0",
            "prior_sha256": null,
            "wire_evidence": [
              {
                "command": "./run harvest-arxiv",
                "output_ref": "git:6005a19878d72518e2f982b5859d68520a4a9503:PROGRESS-v0.8.md#2026-07-20-T2-partial"
              },
              {
                "command": "shasum -a 256 data/core.db",
                "output_ref": "git:e616957680a280a13aa275f0759f4cabd82dfa58:PROGRESS-v0.8.md#2026-07-24-B0.1"
              }
            ],
            "operator_approval": {
              "approved_by": "repository operator",
              "approval_ref": "operator instruction to execute TASKS-v0.10-EXECUTION.md, including retroactive A2 records, on 2026-07-25"
            },
            "retroactive": true
          }
        ]
      },
      "expected": {
        "documents": 1764,
        "integrity_check": "ok",
        "null_simhash": 0,
        "null_canonical_id": 0,
        "cursors": [
          {
            "source_id": "arxiv-cs",
            "cursor": null,
            "high_water": "2026-07-20",
            "pending_high_water": null,
            "updated_at": "2026-07-23 12:08:13"
          }
        ]
      }
    },
    {
      "path": "data/live-smoke.db",
      "sha256": "94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a",
      "bytes": 9490432,
      "purpose": "Protected two-page live arXiv interruption-resume wire evidence.",
      "provenance": "Two capped live OAI-PMH runs fetched 1,300 documents each; the second run resumed from the first run's token and durably advanced to the recorded continuation state.",
      "admission": {
        "records": [
          {
            "task_id": "v0.10/A2",
            "date": "2026-07-25",
            "sha256": "94f03e9e8662dddfa5c80b63a9845d9926a1fa10060b83638ee094e0a0462c4a",
            "prior_sha256": null,
            "wire_evidence": [
              {
                "command": "HARVEST_MAX_PAGES=1 CORE_DB=data/live-smoke.db ./run harvest-arxiv",
                "output_ref": "git:059738677e375c24cc312d59b7d45e7bf6327e6c:PROGRESS-v0.8.md#2026-07-23-T2"
              },
              {
                "command": "shasum -a 256 data/live-smoke.db",
                "output_ref": "git:e616957680a280a13aa275f0759f4cabd82dfa58:PROGRESS-v0.8.md#2026-07-24-B0.1"
              }
            ],
            "operator_approval": {
              "approved_by": "repository operator",
              "approval_ref": "operator instruction to execute TASKS-v0.10-EXECUTION.md, including retroactive A2 records, on 2026-07-25"
            },
            "retroactive": true
          }
        ]
      },
      "expected": {
        "documents": 2600,
        "integrity_check": "ok",
        "null_simhash": 0,
        "null_canonical_id": 0,
        "cursors": [
          {
            "source_id": "arxiv-cs",
            "cursor": "verb%3DListRecords%26metadataPrefix%3Doai_dc%26from%3D2026-07-22%26until%3D2026-07-22%26set%3Dcs%26skip%3D88",
            "high_water": null,
            "pending_high_water": "2026-07-22",
            "updated_at": "2026-07-22 23:45:38"
          }
        ]
      }
    },
    {
      "path": "data/live-20260803T195324Z-37051.db",
      "sha256": "fb1046b79e7501d51e2dde3fd89fb7dfe0094defa6205b12afb39a21dff06044",
      "bytes": 253952,
      "purpose": "Protected first-window SEC EDGAR US GAAP RSS admission archive.",
      "provenance": "Grant-B-authorized fresh-path production harvest on 2026-08-04 local time fetched and stored 200 current finance documents after the live SEC robots policy allowed the configured RSS path; the one-shot harness shut down cleanly and the archive was admitted only after DR12 compatibility and subscription-isolation measurements passed.",
      "admission": {
        "records": [
          {
            "task_id": "v0.38/WIRE-ADMISSION",
            "date": "2026-08-04",
            "sha256": "fb1046b79e7501d51e2dde3fd89fb7dfe0094defa6205b12afb39a21dff06044",
            "prior_sha256": null,
            "wire_evidence": [
              {
                "command": "Grant B evidence capture: one no-redirect/no-retry GET each for SEC robots, published access terms, and configured US GAAP RSS feed",
                "output_ref": "sha256:c8e1cba80252d1fa209ed07cf842696adfe21b514fa45c5982e8caec42c42d54"
              },
              {
                "command": "./run harvest-sec",
                "output_ref": "sha256:c000a22aab26ce21b5fb100028e79d4be94c50d5395ea141938117a76b961818"
              },
              {
                "command": "shasum -a 256 data/live-20260803T195324Z-37051.db",
                "output_ref": "sha256:c000a22aab26ce21b5fb100028e79d4be94c50d5395ea141938117a76b961818"
              }
            ],
            "operator_approval": {
              "approved_by": "repository operator",
              "approval_ref": "Initiating request recorded verbatim before execution in docs/cycles/PROGRESS-v0.38.md on 2026-08-04: Before the task begins, I will first authorize you to \"publish v0.17.4\" and \"SEC EDGAR wire and admission.\""
            },
            "retroactive": false
          }
        ]
      },
      "expected": {
        "documents": 200,
        "integrity_check": "ok",
        "null_simhash": 0,
        "null_canonical_id": 0,
        "cursors": []
      }
    }
  ],
  "pinned_files": [
    {
      "path": "run",
      "grade": "authorization",
      "sha256": "e436d59b05f060a8ce78dd3fb23282ad99fbc8bd263abd73224978c74afeeadb",
      "bytes": 50378,
      "purpose": "Hash-pinned entry point for operator-authorized operational command surfaces.",
      "provenance": "Operator selected L1 on 2026-07-27 and approved the Steps 7-8 atomic admission boundary. Operator-directed v0.17 HARVEST-PREFLIGHT on 2026-07-28 replaced v0.16's forward run hash f62a5d4f0b8f07d48c194e2d8e3959b5bfe82a3e61a45413452a284ab4dd348d (41862 bytes) after adding the protected-artifact verification call only at cmd_harvest_arxiv before environment setup and reachability. v0.18 WIRE-FINDINGS on 2026-07-28 replaced v0.17's hash 7351f2ffb7eb6def34c99c812a61a10690b6f690e9e1e44cee88790ca6dcc455 (41959 bytes) after making cmd_harvest_arxiv stop its managed core before returning and correcting its lifecycle output. Operator-directed v0.20 EXPORT-CHECK on 2026-07-29 replaced v0.18's hash caae4e8007fc885241bf1ac7c844e397a149970048e036be285e356449030678 (42056 bytes) after adding only the operator-local derived export check, its help text, and its dispatch. v0.24 POPULATION-EXPLICIT replaced v0.20's forward hash 0fc7f0be0ea2d8c68ff63be55dd0b73cc1385ce966b8307506a5387543f18779 (43044 bytes) after adding one comment that identifies shell/pytest.ini as the common local/hosted population-summary authority; the command, dispatch, model-profile functions, tools/model_profiles.py, authorization policy, and every historical manifest remain unchanged. v0.35 NET-FLOOR replaced v0.24's hash 44314ddfc182de68d4aaa444f2c6bd074fe08858d8d46f98aafa461dd6672397 (43125 bytes) after adding only the paired local live-fetch floor success and declared-MSRV refutation lanes; the command dispatch, model-profile functions, tools/model_profiles.py, and authorization policy remain unchanged. v0.35 Step 5A replaced NET-FLOOR's hash a05562dd1612678aa7c78f1aa8efe09e4c2e4392175c2363b25778577f36b818 (43907 bytes) after adding effective cargo/rustc release proof to exactly the four existing local floor entries; the command dispatch, model-profile functions, tools/model_profiles.py, and authorization policy remain unchanged. v0.35 attestation preflight replaced Step 5A's hash 1f87371243698cb60fb24c07b21caf8ce7a86f927a46443b0b89f71de978ad7b (44795 bytes) after adding only the standing v0.34 7/7 positive verifier preflight, its wrong-signer negative control, help text, and dispatch; model-profile functions, tools/model_profiles.py, and authorization policy remain unchanged. v0.38 REHEARSAL-COMPLETE replaces the v0.35 hash 5ff56fc76a5a33f17b2fbd4b0dfddeb8e6dbef0ad8b63e5f652a5b06b9ad4c55 (45409 bytes) after adding only the `harvest-sec` operational entry point and command help/dispatch, generalizing the protected-target suggestion to name the invoking harvest, and leaving the arXiv, model-profile, attestation, export, and every other command behavior unchanged. The SEC entry point verifies protected artifacts before selecting and protecting a fresh archive, requires the monitored-contact environment, starts the committed source configuration, filters ingestion to `sec-edgar-usgaap`, requires a nonempty first-window result, derives license/integrity/fingerprint facts, consumes no observation file, and owns its process cleanup. Its source-structure test plants missing-preflight and wrong-source mutations; no publisher request was made during rehearsal."
    },
    {
      "path": "tools/model_profiles.py",
      "grade": "authorization",
      "sha256": "1920761c97ffa6fc7b5242c16384fb6f1b0727937f9e1cfd7e00826c913554df",
      "bytes": 28297,
      "purpose": "Hash-pinned controller for the operator-authorized model-profile lifecycle.",
      "provenance": "OPS-FAILCLOSED deliberately replaced the admitted 2026-07-27 L1 hash b7b84261a6bc45706f93f338682108a31c3b88ad00ad4c91061a90f77ed74292 with pure, offline-tested refusal decisions; the pin makes later controller edits visible to manifest validation."
    },
    {
      "path": "observations/v0.25/feed-shape/.gitattributes",
      "grade": "observation",
      "sha256": "01be878b7d5393273981278a686f5940127adb400d121b1e8d91c7710a933c42",
      "bytes": 213,
      "purpose": "Byte-treatment declaration for the v0.25 SEC EDGAR wire observation.",
      "provenance": "Captured as part of the operator-authorized bounded v0.25 SEC observation on 2026-07-30; this pin detects change but does not independently establish what the publisher served."
    },
    {
      "path": "observations/v0.25/feed-shape/sec-edgar-feed-shape.md",
      "grade": "observation",
      "sha256": "87677a7c4721f3262f646f5b138406b5c296edc32dd06ad64a5439bafb27e936",
      "bytes": 4654,
      "purpose": "Wire-command, response-header, hash, and feed-shape record for the v0.25 SEC EDGAR observation.",
      "provenance": "Captured as part of the operator-authorized bounded v0.25 SEC observation on 2026-07-30; this pin detects change but does not independently establish what the publisher served."
    },
    {
      "path": "observations/v0.25/feed-shape/sec-edgar-robots.txt",
      "grade": "observation",
      "sha256": "72d6196b3f20737396e566ddeb769fb4174b44f334985a1267a59ae0f08c2f2f",
      "bytes": 2622,
      "purpose": "Publisher robots response body captured for the v0.25 SEC EDGAR wire observation.",
      "provenance": "Captured as part of the operator-authorized bounded v0.25 SEC observation on 2026-07-30; this pin detects change but does not independently establish what the publisher served."
    },
    {
      "path": "observations/v0.25/terms-gate/sec-edgar-terms-determination.md",
      "grade": "observation",
      "sha256": "103d29edd3a9ab005981a8ccd22eb8118040d992474e6a33491a51bde9ddbb2c",
      "bytes": 3549,
      "purpose": "Terms-gate determination that authorized the bounded v0.25 SEC EDGAR observation.",
      "provenance": "Captured as part of the operator-authorized bounded v0.25 SEC observation on 2026-07-30; this pin detects change but does not independently establish what the publisher served."
    },
    {
      "path": "observations/v0.38/sec-edgar-wire-2026-08-04/.gitattributes",
      "grade": "observation",
      "sha256": "7af8b91da22ea95a727a1b9f0cad9e4879037612869541554144152935fc37c9",
      "bytes": 248,
      "purpose": "Binary treatment for the three raw v0.38 SEC publisher responses.",
      "provenance": "Grant B authorized the dated observation capture on 2026-08-04; this local attribute file prevents Git normalization from changing publisher response bytes."
    },
    {
      "path": "observations/v0.38/sec-edgar-wire-2026-08-04/sec-edgar-evidence-comparison.md",
      "grade": "observation",
      "sha256": "c8e1cba80252d1fa209ed07cf842696adfe21b514fa45c5982e8caec42c42d54",
      "bytes": 4463,
      "purpose": "Dated per-artifact DR12 compatibility comparison for SEC robots, terms, and RSS feed evidence.",
      "provenance": "One Grant-B-authorized request per publisher URL completed without redirect or retry on 2026-08-04 local time; the report records exact response facts and the offline file-to-file material-compatibility decision before harvest."
    },
    {
      "path": "observations/v0.38/sec-edgar-wire-2026-08-04/sec-edgar-admission-report.md",
      "grade": "observation",
      "sha256": "c000a22aab26ce21b5fb100028e79d4be94c50d5395ea141938117a76b961818",
      "bytes": 5560,
      "purpose": "Dated Grant B production-harvest, fresh-archive, entitlement, licensing, and admission measurement.",
      "provenance": "The bounded one-shot production path consumed the live configured SEC feed into a fresh database on 2026-08-04 local time; the report records exact stdout, archive, public-shell isolation, scope limits, and the compatible admission disposition without exposing the monitored contact."
    }
  ]
}
```
<!-- REVIEW_SOURCE_PROJECTION:END -->

## 5. Standing authorization for Codex (adopted 2026-07-27)

The following policy is mirrored in `AGENTS.md`. It grants autonomy for exactly
the routine lifecycle and nothing else:

<!-- MODEL_PROFILE_AUTHORITY:START -->
**Server model-profile authority — L1 now, L2 scheduled.** The operator selected
L1 on 2026-07-27 because it is offline-testable and makes the current controller
refuse remote commands outside a compiled construction allowlist. Codex may run
`./run models status|intel|athenaeum|athenaeum-bulk|stop` without a per-command
authorization request, including launching that exact command in Terminal.app
when the Mac-created port-2222 bridge is absent.

Every remote command produced by `tools/model_profiles.py` passes one allowlist
before SSH. `docker start|stop|restart` may name only `intel-gen`,
`intel-embed`, `athenaeum-gen`, `athenaeum-embed-gpu`, and
`athenaeum-embed-cpu`; `docker ps` and `docker ps -a` may inspect inventory;
`curl` may query only `/health` or `/v1/models` on loopback ports 8080–8082;
and the remaining exact read-only commands are `nvidia-smi`, `ip -br address`,
and `git status`. Anything else raises `ProfileError` before SSH. The `run` and
`tools/model_profiles.py` bytes are hash-pinned in
`config/protected-artifacts.json`.

The authorization also covers creating, checking, reusing, and cleanly exiting
the documented shared SSH bridge and intel/Athenaeum model-tunnel control
sockets, plus local `lsof` inspection of their documented forwards. Before a
switch, Codex inspects and reports the actual named-container state. After a
switch, it reports server-local and forwarded health. A missing named container,
foreign listener, health failure, or partial/overlapping GPU state is a refusal;
`models stop` is the authorized safe recovery for the last state and may stop
all five named containers plus close only the managed tunnels and bridge.

Everything else on the server remains ask-first, especially `docker run`,
`docker rm`, `docker rmi`, `docker pull`, any image or tag change, edits under
`/data/models`, package installation, reboots, and irreversible actions. The
routine controller never creates, removes, or recreates a container, and never
removes an image, model, repository, or configuration.

L1 cannot prevent an agent that edits `tools/model_profiles.py` from changing
what runs; only L2 can make the server authorization survive an edited
controller. L2 is scheduled for the next operator-authorized
server-administration session and must be installed and refusal-tested before
any additional model profile is admitted: an `authorized_keys`
forced-command wrapper will make the server reject commands outside the same
lifecycle set.
<!-- MODEL_PROFILE_AUTHORITY:END -->

<!-- CYCLE_AUTONOMY_AUTHORITY:START -->
**Cycle execution authority — standing, granted 2026-08-03.** Within a declared
cycle, Codex decides and records rather than asking. This covers: selecting
among design options the active cycle's execution runbook presents or leaves
open; choosing implementation seams; setting `accepted_by` on exemption,
deferral, and disposition records to the authorizing runbook named in the
declaration above; selecting a release disposition and version by the runbook's
stated rule; selecting a value inside an already-accepted boundary or ceiling;
registering new invariant rules and planted controls; editing any tracked file
the cycle's declared scope reaches, with the justification the relevant document
requires; and re-pinning `authorization`-grade bytes in
`config/protected-artifacts.json` after a legitimate edit to the file they pin.

A recorded decision naming its basis and what would have changed it is complete
work. A question routed to the operator inside this scope is not.

Evidence-ref pushes are covered when all of these hold: the ref is under
`refs/heads/codex/` and names the active cycle and a short commit id; `git
ls-remote` confirms immediately beforehand that it does not exist, and the
result is recorded; the push is non-force and creates exactly that one ref; and
`main` and every tag are untouched. A pre-existing ref is a finding, not a
detail.

**Ask first — this list is exhaustive and is not widened by convenience:**
publishing `main` or any release tag; admitting a publisher under the
`append_only_chained_records_with_wire_evidence_and_operator_approval`
lifecycle; writing, replacing, or re-pinning any protected database,
`observation`-grade byte, or structural-archive byte; moving an accepted
boundary or ceiling rather than selecting inside it; adding a retraction; any
change that moves an entitlement or licensing outcome for a configured
subscription; and any live publisher request against a real wire.

Decision gates are unchanged. A tripped gate still stops its task and is
recorded; this authority never converts a gate into a workaround. Autonomy is
permission to decide, never permission to proceed past a measurement.
<!-- CYCLE_AUTONOMY_AUTHORITY:END -->

`tools/model_profiles.py` in the intel-platform repository is the single source
of truth for both projects' routine profile switching. Athenaeum operations
delegate to this controller; do not keep a second executable copy.

---

## Recovery checklist

1. Use Terminal.app for the first post-reboot command; a shell spawned by
   `osascript do shell script` does not gain Terminal.app's LAN route.
2. `lsof -nP -iTCP:2222 -sTCP:LISTEN` / `-iTCP:18080` / `-iTCP:18081` — reuse
   healthy managed tunnels. `./run models` moves stale socket files aside but
   refuses foreign listeners; never kill an unknown process merely to make a
   switch pass.
3. On the server: `docker ps -a --filter name=athenaeum- --filter name=intel-`
   to see which profile the machine is actually in.
4. A port-bind failure on `docker start` means the other project's container
   still holds the port — run the full switch sequence, not a bare start.
5. Slow health after `docker start` is model load, not failure — poll.
6. Ignore the existing `intel-embed` Docker `unhealthy` label only when the
   explicit port-8081 HTTP probe passes; its inherited image check targets the
   wrong internal port. Any real HTTP failure still stops the switch.
7. After any intel session that will be followed by Athenaeum work, run
   `./run models athenaeum`; this closes the intel tunnel as well as switching
   server roles.
