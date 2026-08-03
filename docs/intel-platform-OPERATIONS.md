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
