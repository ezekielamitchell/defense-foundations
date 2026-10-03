# Codex task: defense-foundations architecture map v3

Live, 3D, endr-styled, generated from the repository itself.

---

## 0. How to use this prompt

1. Read the whole prompt once before touching anything.
2. Work in the phases in section 14, in order. Do not skip a phase.
3. After each phase, post the status block from section 14.2. Stop at the stop points listed there.
4. Everything in section 16 is already decided. Do not re-ask it.
5. When this prompt and `AGENTS.md` disagree, `AGENTS.md` wins. Say so in your status block.

---

## 1. Mission

Build v3 of the interactive architecture map for this repository.

Output: `docs/architecture/index.html`. It is one self-contained HTML file that shows how evidence moves (or fails to move) through defense-foundations toward the Phase 0 gate.

It must do four things:

- **3D board in endr's style.** Render the pipeline as a clean 3D board in endr's visual language: warm paper, olive ink, serif display type, bracketed mono labels.
- **Generated, not hand-drawn.** A generator extracts the map from the real repository files. Every claim carries a source that is anchored to file content.
- **Live updates.** The map updates while a local dev server runs. When a file changes, the map re-extracts, re-runs the safe checks and animates exactly what changed. The camera does not move.
- **Beats v2.** It must be easier to follow than v2: cleaner edges, better figures, readable at every supported size.

---

## 2. Ground truth you start from

### Repository

| Field | Value at v2 generation (re-read these; do not copy) |
|---|---|
| Name | `defense-foundations` |
| Branch | `codex/aegis-beginner-reset-2026-09-19` |
| HEAD | `2e13798` "Validate capacity for the authorized daily reading schedule" |
| Worktree | dirty: about 80 changed paths, including 5 deleted Invaders audio files that must stay deleted |

The repo is a curriculum and governance repository, not runtime software. The map models the process that governs it: how private schedule authority, curriculum policy and learner work become (or fail to become) verified Phase 0 evidence.

### v2 (what exists now)

`docs/architecture/index.html` is v2. It embeds:

```js
const MODEL = { meta, tiers, zones, nodes, edges, payloads, tour }
```

**Inventory:**

- 34 nodes: 8 planned, 3 stub, 17 implemented, 6 tested, 0 deployed. 6 nodes are inferred.
- 54 edges: 24 data, 21 config, 7 control, 2 telemetry. 7 edges are inferred.
- 4 blocked edges, each with a short rule label:

  | Edge | Label |
  |---|---|
  | `calendar -> receipts` | Schedule ≠ proof |
  | `endr -> receipts` | No company credit |
  | `exercises -> receipts` | No duplicate credit |
  | `routeval -> gate` | Admin ≠ proof |

- 21 payloads.
- 8 tour stops:
  1. Authority lives outside the repo
  2. A hash-stamped projection is published
  3. Policy routes the learner
  4. One human operator
  5. Project 0: the only product code
  6. The evidence firewall
  7. Fail-closed verification
  8. The gate is starved

**Engine and features:**

- Canvas 2D with a hand-rolled yaw/pitch projection.
- Controls: orbit, Rotate, Plan view, blast radius, ⌘K palette, guided tour, "What it does" and "How it's built" tabs.

**Checks observed at v2 generation:**

- Beginner-policy tests: 7 of 7 pass.
- Integrity tests: 10 pass and 10 error when the private vault is absent.
- `node --check` passes on `mobile/app.js` and `mobile/sw.js`.

Re-observe all of these. Never copy them forward.

**Use v2 as the seed, not as truth.** Extract its `MODEL` into `tools/archmap/seed_model.json` and re-verify every citation against the current files.

### Protected file

`docs/architecture.html` is a different file. It is a projection consumer that is hard-coded in `tools/validate_phase0_integrity.py:325` and `tests/test_phase0_integrity.py:212`. Never modify it, move it or regenerate it.

---

## 3. Non-negotiables

### 3A. Repository safety (from `AGENTS.md`)

- **Git is read-only.** Allowed: `git status`, `git rev-parse`, `git log`, `git show`, `git diff`. Forbidden: commit, push, branch switch, stash, checkout, restore, reset, clean, rebase, worktree, and any other command that writes to `.git`.
- **Preserve all pre-existing dirty work.** Do not restore, replace or reinterpret the five deleted Invaders audio files.
- **Projections are publisher-owned.** Never hand-edit `AEGIS:PHASE0_PROJECTION` regions or `docs/aegis-phase0-projection.json`. Never run the projection exporter.
- **Write scope is exactly:**
  - `tools/archmap/**` (new)
  - `docs/architecture/index.html` (generated)

  Anything else needs my approval first. This includes `tests/`, `tools/validate_*`, `curriculum/`, `progress/`, `projects/`, `mobile/`, the root `.gitignore` and `docs/architecture.html`.
- **Leave this prompt in place.** It lives at `docs/architecture/CODEX_PROMPT.md`.
- **Read inside the repo root only.** Never read the private Aegis vault or any path outside the repo. The only permitted view of authority is `docs/aegis-phase0-projection.json`. When a check subprocess prints an absolute path outside the repo, replace it with `<outside-repo>` before storing or displaying it.
- **The map is administrative.** It never writes proof receipts, and nothing it shows earns Foundation credit. The page says so in the "How it's built" tab.

### 3B. Truth rules

- **Everything is sourced.** Every node, edge, payload, tour stop, risk and displayed number traces to real files through `sources`. Each source has a content anchor (section 6.2).
- **Mark inference.** Anything the repo does not state directly gets `inferred: true` and renders dashed.
- **Never invent metrics, latencies, rates or example values.** Only these numbers may appear:
  - counts derived from files (lines, files, tests collected, passed, failed, errored)
  - git-derived facts (dirty path count, commit time)
  - timestamps of observations

  Every displayed number shows its derivation on hover. Particle speed is labeled "not to scale".
- **Exactly one maturity state per node,** from `planned | stub | implemented | tested | deployed`. It is derived by the rules in section 6.4. An override requires `reason` and `sources`, and it is shown in the node's details panel.
- **Zero tests is not "tested".** A passing command that collected zero tests is not evidence. Neither is a checked task, a scheduled block, a generated page or a green dashboard (`AGENTS.md`).

### 3C. Output rules

- **One self-contained HTML file.** CSS, JS and fonts (base64 WOFF2) are inline. Opened from `file://`, it makes zero network requests.
- **One exception, live mode:** same-origin requests to the local dev server on `127.0.0.1`.
- **No fake branding.** No fake classification banners, no unit insignia, no logos or branding of other companies.
- **Title is the repo's real name:** `defense-foundations`.
- **endr styling is authorized.** endr's visual language (palette, type, motifs) is authorized by its owner. Do not place the endr wordmark or logo on the page.
- **No frameworks or tracking.** No React or Vue, no analytics, no telemetry, no remote fonts or images.
- **Storage.** `localStorage` holds UI preferences only (panel collapsed, last tab), wrapped in `try/catch`. It never holds state that matters.
- **Content boundary.** This is a training-governance map: no weapons, targeting or operational content.

---

## 4. The brief: what "better than v2" means

### v2 problems to fix

1. **Edge hairball.** 54 edges draw at once as long diagonals that cross through the center. Crossings are not minimized, and there is no bundling.
2. **Labels vanish.** At 1024×700 and 390×844 many titles are hidden by collision. At 1440, 2 of the 4 blocked-edge labels are hidden.
3. **Weak figures.** Slabs are small and similar, and there is no visual hierarchy. The nodes that matter most look like everything else: Proof receipts, Integrity validator, P0 gate review.
4. **Fonts fall back offline.** The repo file cannot load endr's fonts. Fix this by embedding subset fonts.
5. **Citations drift.** Sources are bare `path:line` ranges that break as files change.
6. **Static.** It is a snapshot. Nothing updates when the repo changes, and checks are not re-run.
7. **Weak accessibility.** Canvas text is not selectable or accessible, and there is no outline equivalent.
8. **Zone tabs float.** Zone tabs sometimes sit far from their plates, and plates visually overlap.

### Goals, in priority order

1. **Truthful.** Every mark on screen is backed by an anchored source or an observed check.
2. **Easy to follow.** A first-time viewer understands the evidence path in 30 seconds. The resting view shows the main evidence path clearly, and the other edges appear on focus.
3. **Clean.** Layered layout, bundled and rounded edges, consistent spacing, no collisions.
4. **Live.** Changes in the repo appear in the page within 2 seconds while `serve.py` runs.
5. **3D and tactile.** Real depth, soft shadows, smooth orbit and zoom, crisp type.
6. **Fast.** First frame under 300 ms, and smooth at 60 fps.

---

## 5. System architecture

### Pipeline

```
repo files ──► extract.py ──► model (curated + derived) ──► layout.py ──► build.py ──► docs/architecture/index.html
                  ▲                     │
                  │                     └──► serve.py (watch + checks + SSE) ──► browser applies live patches
             checks.py (whitelisted, read-only)
```

### File tree to create

```
tools/archmap/
  README.md             build, serve, test, and the truth rules in one page
  .gitignore            node_modules/  .artifacts/  __pycache__/
  package.json          pinned devDependencies only: three, esbuild
  curated.json          hand-authored nodes, edges, payloads, tour, copy; every source anchored
  seed_model.json       v2 MODEL, extracted verbatim (read-only reference)
  extract.py            repo -> model (stdlib only, Python 3.10+)
  checks.py             whitelisted read-only check runner
  layout.py             deterministic layered layout
  diff.py               model diff -> patch operations
  build.py              model + web/ -> single HTML  (--watch, --check, --strict)
  serve.py              localhost dev server: watch, checks, SSE
  web/
    main.js             entry; bundled to one IIFE by esbuild
    engine3d.js         three.js scene, camera, picking
    engine2d.js         Canvas 2D fallback (plan view)
    labels.js           DOM label layout + level of detail
    edges.js            routing, bundling, dash animation, particles
    ui.js               header, panel, palette, tour, blast, outline, changes drawer
    live.js             SSE client, patch application, reconnect
    style.css
    template.html
  vendor/
    fonts/*.woff2 + OFL.txt
  tests/
    test_extract.py  test_anchors.py  test_maturity.py  test_blast.py
    test_layout.py   test_diff.py     test_checks.py    test_serve.py
    e2e/            Playwright specs (section 13.2 and 13.3)
docs/architecture/index.html   generated
```

### Commands the README must document

```sh
python3 tools/archmap/build.py                # write docs/architecture/index.html
python3 tools/archmap/build.py --strict       # fail on any stale anchor or unverifiable claim
python3 tools/archmap/build.py --check        # exit 1 if the committed HTML is stale (ignores the generated timestamp)
python3 tools/archmap/serve.py                # live mode at http://127.0.0.1:8765
python3 -m unittest discover -s tools/archmap/tests -p "test_*.py"
```

---

## 6. Model specification

### 6.1 Schema

```jsonc
{
  "meta": {
    "repo": "defense-foundations",
    "branch": "…", "commit": "…", "commitDate": "…",
    "dirtyCount": 80,            // from `git status --porcelain`; derived, never typed
    "generated": "ISO-8601 UTC",
    "rev": 0,                    // increments per live patch
    "modeled": "…", "thesis": "…"
  },
  "tiers":  [{ "id": "authority", "label": "Authority", "icon": "lock", "hue": "#…" }],
  "zones":  [{ "id": "z-proof", "label": "Evidence", "lane": 1, "sources": [] }],
  "nodes": [{
    "id": "receipts",
    "title": "Proof receipts",
    "short": "Receipts",         // 14 characters or fewer, used at low zoom
    "role": "one line, plain language",
    "tier": "observe", "zone": "z-proof",
    "primary": true,             // visually emphasized
    "owns": ["progress/proofs/**"],   // globs; drive metric and maturity
    "maturity": "planned",       // derived; exactly one
    "maturityWhy": "No receipt files match progress/proofs/*.json",
    "override": null,            // or { "maturity": "…", "reason": "…", "sources": [] }
    "inferred": false,
    "metric": { "kind": "lines", "value": 0, "files": 0, "derivation": "…" },
    "checks": ["integrity-tests"],
    "sources": [ /* 6.2 */ ],
    "provenance": "ok"           // ok | stale
  }],
  "edges": [{
    "id": "e-receipts-integrity", "from": "receipts", "to": "integrity",
    "kind": "data",              // data | control | config | telemetry
    "payload": "p-receipt",
    "blocked": false, "short": null,   // blocked edges carry a short rule label
    "feedback": false, "inferred": false,
    "sources": []
  }],
  "payloads": [{ "id": "p-receipt", "label": "…", "schema": "…", "sources": [] }],
  "tour": [{ "id": "t6", "title": "The evidence firewall", "focus": ["receipts"], "body": "…", "sources": [] }],
  "checks": [ /* 6.6 */ ],
  "risks":  [{ "id": "…", "text": "…", "derivedFrom": "rule id", "sources": [] }]
}
```

### 6.2 Sources and anchors

Every source is an object:

```json
{ "path": "tools/validate_phase0_integrity.py",
  "anchor": "for relative in [*documents, \"docs/architecture.html\"]",
  "span": 1 }
```

The fields work like this:

- `anchor` is a literal substring that must appear in the file.
- `span` is how many lines to cite, starting at the anchor line.

The extractor resolves each anchor to the current line numbers and stores `lines: "325"` or `lines: "132-364"`.

**Failure cases:**

| Case | Result |
|---|---|
| Anchor not found | `provenance: "stale"`, an amber "stale source" badge on the node, and a build failure under `--strict` |
| Path does not exist | Same as a missing anchor |
| Anchor matches more than once | Pick the first match, record a warning, and fix the anchor |

Seed anchors from v2's `path:line` citations. For each one, take the cited line's text as the anchor, confirm that it still says what the node claims, and record any mismatch in the phase 1 report.

### 6.3 Curated vs derived

| Curated (hand-authored in `curated.json`) | Derived (computed by `extract.py` on every run) |
|---|---|
| ids, titles, short titles, roles, tiers, zones, `primary` | resolved line numbers, `provenance` |
| edges, kinds, payloads, blocked rules and labels | metric values (lines, files) |
| `owns` globs, `checks` bindings | maturity and `maturityWhy` |
| tour copy, panel copy | git ref, sha, dirty count, commit date |
| `inferred` flags | check results, risks, SPOFs |

### 6.4 Maturity rules

Apply these in order, top to bottom. The first rule that matches wins.

| # | State | Rule |
|---|---|---|
| 1 | `override` | If `override` is present, use it and show `reason` in the node's details panel. |
| 2 | `deployed` | Never, unless a curated source proves a deployment. Currently none. |
| 3 | `tested` | A whitelisted check bound to this node ran in this build or session, collected at least 1 test, and at least 1 of them passed. Show failures and errors as a risk badge, not as a different state. |
| 4 | `stub` | Owned files exist, but they are placeholders. Detect placeholders with explicit, unit-tested signatures (for example, the entry point only prints a greeting and there are no tests), or with a curated `stubSignature` anchor. |
| 5 | `implemented` | Owned files exist and are not stubs. |
| 6 | `planned` | No owned files exist, or the node is described only in planning documents. |

Nodes outside the repo (`z-outside`, and the ledger) have no owned files. Their maturity comes from curated sources and they are always `inferred: true`.

### 6.5 Metric and figure size

- **Height.** Slab height = `8 + 10 * log10(1 + lines)` world units, where `lines` counts non-blank lines in owned files.
- **Outside the repo:** flat, height 4.
- **Footprint:** base size, or 1.5× for `primary` nodes.

The legend states the formula. The hover card shows the lines, the file count and the glob.

### 6.6 Checks (whitelist, read-only)

| id | command (cwd = repo root, no shell) | binds to |
|---|---|---|
| `integrity` | `python3 tools/validate_phase0_integrity.py` | integrity |
| `route` | `python3 tools/validate_curriculum_route.py` | routeval, route |
| `beginner` | `python3 tools/validate_beginner_policy.py` | policyval, beginner |
| `unit-beginner` | `python3 -m unittest -v tests.test_beginner_policy` | policyval |
| `unit-integrity` | `python3 -m unittest -v tests.test_phase0_integrity` | integrity, projection |
| `node-app` | `node --check mobile/app.js` | mobile |
| `node-sw` | `node --check mobile/sw.js` | mobile |
| `diff-check` | `git diff --check` | syntax |

**Before wiring any check,** read its source and confirm it does not write files. If it writes, leave it out and report it.

**How each check runs:**

- `subprocess.run([...], shell=False, timeout=60)`.
- Environment variable `PYTHONDONTWRITEBYTECODE=1`, so no new `__pycache__` appears.

**What each run stores:**

- `id`, `command`, `ranAt`, `exitCode`
- `collected`, `passed`, `failed`, `errored` (parsed from unittest `-v` output; null when not applicable)
- `firstFailure` (redacted, 300 characters or fewer)

Do not store or display durations.

**Integrity tests without the vault.** The integrity tests error when the private vault is absent. Show that as observed ("10 errored: vault not present") and list it as a risk. Never hide it.

### 6.7 Blast radius semantics (keep v2's, and unit-test them)

- **Dead.** A node is dead if it is offline or starved.
- **Starved.** A node is starved when every one of its primary inputs comes from a dead node. Primary inputs are its data inputs; if it has none, its control inputs; if none, all its inputs.
- **Blocked and feedback edges** carry nothing.
- **SPOF.** A single point of failure is a node whose loss alone starves `gate`.

Test the implementation against a brute-force reference on the real graph and on 3 synthetic graphs.

---

## 7. Live updates

### 7.1 `serve.py` (stdlib only: `http.server`, `threading`)

**Binding and access**

- Bind `127.0.0.1` only, on default port `8765` (`--port`). Refuse `0.0.0.0`.
- Serve the page built in memory from the current model at `/`, with an injected flag:

  ```js
  window.__ARCHMAP_LIVE__ = { rev, token }
  ```

**Endpoints**

| Method | Path | Behavior |
|---|---|---|
| GET | `/` | Serve the page |
| GET | `/api/health` | Health check |
| GET | `/api/model` | Current model |
| GET | `/events` | Server-Sent Events stream |
| POST | `/api/run-checks` | Run the whitelisted checks. Requires header `X-Archmap-Token`, a random value per server start. |

Everything else returns 404. There are no path parameters and no static file serving.

**Security**

- Reject requests whose `Host` header is not `127.0.0.1:<port>` or `localhost:<port>` (DNS-rebinding guard).
- Send no CORS headers.

**Watching and patching**

1. Poll modification times of every file the model depends on (sources, `owns` globs, `curated.json`) every 1 s.
2. Debounce 400 ms after the last change.
3. Re-extract, diff, bump `rev`, and push an SSE `model-patch` event:

   ```json
   { "rev": 14, "at": "ISO", "trigger": ["projects/hello-stats/src/main.rs"],
     "changes": [ { "op": "node.metric", "id": "hellostats", "from": 13, "to": 41 },
                  { "op": "node.maturity", "id": "hellostats", "from": "stub", "to": "implemented" } ],
     "model": { } }
   ```

**Checks and heartbeat**

- Auto-run the checks 2 s after changes settle. One run at a time; when changes arrive mid-run, queue the latest request only.
- Push `checks-started` and `checks-finished` events. Results flow into maturity and risks, and produce a second `model-patch`.
- Send a heartbeat comment every 15 s.

### 7.2 Page behavior in live mode

**Detecting the mode.** Live mode is on when `__ARCHMAP_LIVE__` exists and `/api/health` responds. Otherwise the page is a static snapshot.

**Status badge** (in the header strip):

| State | Badge |
|---|---|
| Live | `「 LIVE 」 rev 14 · 3s ago` |
| Disconnected | `「 RECONNECTING 」` |
| File | `「 SNAPSHOT 」 generated 2026-09-22 21:39Z` |

**Applying a patch** (animated unless reduced motion is on):

- **Changed metric:** height tweens over 400 ms and the node pulses once.
- **Maturity transition:**
  1. A thin olive ring expands once.
  2. An inline tag `stub → implemented` shows for 4 s.
  3. The node restyles to its new state.
- **Added node or edge:** fades in over 300 ms.
- **Removed node or edge:** fades out over 300 ms.
- **Changed check verdict:** the bound edge flashes. A failure shows a brick bar with the failing check id.
- **Preserved across a patch:** camera, selection, hover, tour position, panel tab and scroll, and palette state.

**Layout stability.** A content-only change (metrics, maturity, checks) must not move any node. Only a topology change (a node or edge added or removed) may re-layout, and it does so incrementally: ranks and orders stay unless they must change, and moved nodes glide over 520 ms.

**Changes drawer.** Opened with the `Changes` button or the `C` key. It holds up to 200 entries, newest first. Each entry shows:

- time (UTC)
- node title
- a plain-language change, for example "hello-stats grew from 13 to 41 lines" or "Integrity validator: 10 passed, 10 errored"
- the trigger file(s)
- the source link

**Screen reader updates.** An `aria-live="polite"` region summarizes at most 1 update per 10 s.

**Reconnect.** Back off exponentially from 1 s up to 10 s, and never show a blank page. On reconnect, fetch `/api/model` and reconcile.

**Run checks.** A `「 Run checks 」` button appears only in live mode.

### 7.3 Static builds

- `build.py --watch` rebuilds the file on change for people who open it through `file://`. The page cannot reload itself; the README says to use `serve.py` for live updates.
- The generated HTML is deterministic apart from `meta.generated`. `--check` depends on this.

---

## 8. Visual design: endr's visual language

### 8.1 Tokens

These were extracted from endrhq.com computed styles on 2026-09-22. Use them as the source of truth. Fetch nothing at runtime.

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#F5F2EB` | page, ground plane |
| `--paper-2` | `#F1F0E7` | slab tops, cards |
| `--panel` | `#ECEEE3` | zone plates, side panel |
| `--inspector` | `#E6E9DC` | inspector block |
| `--ink` | `#1A1A1A` | display text |
| `--ink-2` | `#25291F` | strong UI text |
| `--ink-3` | `#303729` | controls, labels |
| `--body` | `#555F4B` | body copy |
| `--quiet` | `#5E6555` | secondary text (lowest allowed for text) |
| `--olive` | `#526444` | primary accent, active traces, data |
| `--sage` | `#81906F` | brackets, decorative strokes only; never text |
| `--line` | `#B1BAA5` | resting edges, inferred strokes |
| `--rule` | `#D9DBCE` | hairlines, grid major |
| `--border` | `#C3CABA` | control borders |
| `--press` | `#DFE4D5` | pressed button |
| `--hover` | `#E7E9DE` | hover fill |
| `--amber` | `#8C692F` | control edges, starved, stale |
| `--brick` | `#9D4B3B` | blocked rule bar, offline |
| `--tested` | `#3F6B3A` | tested seal |
| `--config` | `#7D8A6C` | config/state payload |

### 8.2 Type (embedded, offline)

| Role | Font | Weights |
|---|---|---|
| Display | Cormorant Garamond | 500 |
| UI and body | Inter | 400, 500, 600 |
| Labels, controls, metadata | IBM Plex Mono | 400, 500 |

**How to build the embedded fonts:**

1. Get the files from `github.com/google/fonts` (`ofl/cormorantgaramond`, `ofl/inter`, `ofl/ibmplexmono`). All are SIL OFL.
2. Instance the variable fonts:

   ```sh
   fonttools varLib.instancer
   ```

3. Subset with `pyftsubset` (pip: `fonttools brotli`) to Basic Latin plus these used glyphs: U+00B7, U+2190, U+2192, U+2260, U+2013, U+2014, U+2018, U+2019, U+201C, U+201D, U+2026, U+00D7 and digits. Output WOFF2 and embed it as base64 `@font-face`.
4. For `「 」`, subset U+300C and U+300D from Noto Sans JP Light (OFL). Name it `endr-brackets` and apply it with `unicode-range`.
5. Store the sources and `OFL.txt` in `tools/archmap/vendor/fonts/`.

**Budget:** 220 KB or less for all fonts combined.

**If pip or the network is unavailable,** use the system fallbacks. The stacks are:

```css
--serif: "Cormorant Garamond", "EB Garamond", "Iowan Old Style", Palatino, Georgia, serif;
--ui:    Inter, ui-sans-serif, -apple-system, "Segoe UI", system-ui, sans-serif;
--mono:  "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
```

### 8.3 Motifs

- **Shape and line:** radius 0 everywhere, 1 px hairlines.
- **Header separator:** a radial-gradient rule, `rgba(81,93,70,.14)` fading to transparent.
- **Bracketed labels:** `「 LABEL 」` for eyebrows, zone tabs and buttons. The brackets are sage pseudo-elements, so `innerText` of a button stays exact.
- **Eyebrows:** uppercase mono, 11 px, 1.1 px tracking.
- **Traces:** dashed `4 4` animated trace on the active path.
- **Space:** generous whitespace. Density comes from alignment, not from packing.

### 8.4 The 3D board

**Engine.** three.js with a pinned exact version from npm, bundled with esbuild into one IIFE:

```sh
esbuild --bundle --format=iife --minify --legal-comments=inline --target=es2020
```

Keep the MIT license comment.

**Fallbacks:**

- If WebGL2 is unavailable at runtime, render the Canvas 2D plan view from `engine2d.js`. Every panel and interaction still works.
- If npm is unavailable at build time, port and upgrade v2's Canvas 2D projection engine instead, and say so in the report.

**Camera**

- Perspective, field of view 30° or less, so it reads like a drafting board.
- Default yaw about -5°, pitch about 61° above the horizon.
- Orbit limits: pitch 20° to 89°, yaw ±60°. Zoom 0.25× to 3×.
- Plan view is an orthographic top-down camera.
- Inertia: velocity cap, then decay (v2 used cap 0.0015 rad/ms and decay 0.86 per frame).
- Every camera transition takes 520 ms with cubic ease-out.

**Ground**

- Paper plane with a drafting grid of 1 rank major (`--rule`) and quarter-rank minor (`--rule` at 50% alpha), with a soft vignette at the edges.

**Zones**

- Plates 2 to 3 units thick in `--panel` at 60 to 80% alpha, with a 1 px `--border` top edge.
- A bracketed mono tab is anchored inside the plate's back-left corner, never floating off it.
- Plates never overlap. Keep a gutter of at least 0.5 rank between them.

**Nodes (the "figures")**

Each node is a beveled module:

- **Faces:** top face `--paper-2`; sides shaded by one directional light at 45° plus ambient, staying within the palette.
- **Shadow:** a soft contact shadow from a baked radial texture.
- **Top face marks:**
  - a line icon per tier: lock, doc, branch, person, code, receipt, shield, flag, globe (1.25 px stroke at 1×)
  - a maturity mark
  - a small out-port ring on the downstream edge
- **Primary nodes** have a 1.5× footprint and a thin olive underline plate: `receipts`, `integrity`, `gate`, `filestats`, `hellostats`.
- **Hover:** lifts 2 units, with a 180 ms ease.
- **Selected:** a 2 px olive outline and a faint olive column of light down to the plate.

**Maturity encoding** (exactly one visual state each):

| State | Figure |
|---|---|
| planned | ghost: no fill, dashed `--line` outline, floating 2 units above the plate |
| stub | hollow shell: walls only, hatched top at 45°, low opacity |
| implemented | solid module |
| tested | solid + seal (a check inside a circle, `--tested`) at the top-right corner |
| deployed | solid + filled dot (currently none) |

**Inferred nodes** have dashed top-face edges and an "inferred" tag in the node's details panel.

### 8.5 Connections (the main visual upgrade)

**Routing**

1. Ports sit on node faces: inputs on the upstream face, outputs on the downstream face.
2. Edges run through lane gutters as orthogonal paths with rounded corners (radius 18 to 28 units). A smooth spline constrained to the gutters is acceptable instead.
3. Edges that share a corridor are bundled: parallel tracks 3 to 4 units apart, splitting within 1 rank of their targets.
4. Edges lift to plate top + 1.5 units, so they never clip slabs.
5. The feedback edge takes a dedicated side lane.

**Drawing**

- Screen-space constant width: 1.25 px at rest, 2 px when focused, round caps and joins.
- Chevron arrowheads at 85% of the arc length.

**States**

| State | Look |
|---|---|
| Rest | `--line` at 55% alpha |
| Dimmed (when something else is focused) | 15% alpha |
| Focused | `--olive`, dash `4 4` flowing at a fixed screen speed |
| Blocked | ends at 56% of its length with a 2 px brick bar and a bracketed label, for example `「 NO DUPLICATE CREDIT 」`. It never animates past the bar. |
| Inferred | dashed `2 3` |

**Default visibility.** At rest the page shows:

- the main evidence path: projection, policy, learner, Project 0, command runs, receipts, integrity, gate
- the 4 blocked edges

All other edges draw at rest opacity. Focus reveals the full upstream and downstream sets.

**Particles**

- One glyph per payload kind: data is a circle, control a diamond, config a square, telemetry a ring.
- 150 at most, moving at constant screen speed along the arcs.
- The legend says "Particle speed · not to scale".

### 8.6 Labels

- **DOM overlay, not canvas text,** so labels are crisp, selectable and accessible.
  - Titles: Inter 600, 13 px, `--ink-2`, with a 2 px paper halo.
  - Subtitles: mono 10 px, `--quiet`.
- **Placement.** Pick from 13 candidate positions around the projected footprint, and never overlap:
  - another label
  - a zone tab
  - the HUD
  - the panel edge
- **Level of detail by zoom:**

  | Zoom | Label |
  |---|---|
  | 0.8× or more | full title |
  | 0.5× to 0.8× | `short` title |
  | below 0.5× | dot only, with a tooltip |

- **Never truncate with an ellipsis.** Hide a label rather than shrink it below 11 px.
- **Pass targets:**
  - 1440×900 at fit: 100% of titles and all 4 blocked labels visible.
  - 1024×700: at least 90% of titles, full or short.

### 8.7 Layout (`layout.py`, deterministic)

Use a Sugiyama-style layered layout:

1. Assign ranks by the longest path from the sources (edges point toward the gate), respecting zone lanes.
2. Minimize crossings with barycenter ordering: at least 24 sweeps, and deterministic tie-breaks by node id.
3. Assign coordinates on a rank grid (column width 255 units, row height 150, as in v2), then compact.

Curated `pin: {rank, order}` may fix positions. Identical input produces byte-identical positions.

### 8.8 Header, HUD, responsive

**Header (64 px)**

- h1 `defense-foundations` in Cormorant 26 px.
- Metadata strip in mono 11 px:

  ```
  「 ARCHITECTURE 」 · branch · short sha · dirty count · generated · live badge · UTC clock
  ```

**Controls (mono, bracketed):** Pause/Resume the flow, Trace one step, Reset view, Blast radius, Search ⌘K, Changes (live only), panel toggle.

**Scene overlays**

- A "Modeled · the evidence-governance process, not runtime software" note at the top left.
- Rotate and Plan view at the top right.
- Scalebar ("1 rank").
- Minimap: 168×124 plan view with the camera frustum drawn. Click it to move the view. It auto-hides when it would cover a node.
- Collapsible legend band.

**Breakpoints**

| Width | Behavior |
|---|---|
| 1500 px or less | hide the optional strip items |
| 1180 px or less | hide the eyebrow and the kbd hint; tighten control padding to 6 px |
| 1080 px or less | hide the strip |
| under 900 px | the panel becomes a bottom sheet at 46% height and scrolls |
| 600 px or less | hide the brand; open in Plan view with short titles; orbit stays available but is not the default |

**Never** allow horizontal page scroll, and never let the header text and controls overlap. Test every breakpoint.

### 8.9 Motion

- Camera: 520 ms cubic ease-out.
- Hover: 180 ms.
- Rotate mode: 0.12 rad/s. It stops on any user input.

**With `prefers-reduced-motion: reduce`:**

- no camera tweens (jump cuts)
- static particle markers
- no auto-rotate
- no pulses (use a static 2 px outline for 4 s instead)
- no dash flow (static dashes)

---

## 9. Interaction specification

### Exact labels (tests assert on `innerText`)

| Control | Label(s) |
|---|---|
| Flow toggle | "Pause the flow" / "Resume the flow" |
| Tour step | "Trace one step" |
| Reset | "Reset view" |
| Blast | "Blast radius" |
| Search | "Search" plus kbd "⌘K" (or "Ctrl K" off Mac) |
| View | "Rotate", "Plan view" |
| Live | "Changes", "Run checks" |
| Panel tabs | "What it does", "How it's built" |

### Keyboard

| Key | Action |
|---|---|
| Space | Toggle flow (ignored when focus is on a control) |
| → / ← | Next / previous tour stop (ignored on tabs) |
| R | Reset view |
| B | Toggle blast radius |
| / or ⌘K / Ctrl-K | Open the search palette |
| Esc | Close the palette, then exit blast, then clear the selection (one per press) |
| 1-9 | Jump to tier N |
| P | Plan view |
| O | Outline view |
| C | Changes drawer (live) |
| Tab | Moves through nodes in reading order when the canvas has focus; Enter selects |

### Pointer and touch

- Drag orbits.
- Shift-drag, middle-drag or right-drag pans.
- The wheel zooms around the cursor.
- Pinch zooms.
- Tap selects; tapping empty ground clears the selection.
- Double-click frames the node.

### Hover card

Title, maturity with its reason, metric with its derivation, and the top 2 sources. It is never clipped by the viewport.

### Selecting a node

Selecting a node focuses its upstream and downstream sets and opens the node's details panel (section 10). The panel includes **Trace to gate**, which:

- highlights the shortest path from the node to `gate`
- names the first blocker on it (a blocked rule, a starved node, or a planned node)

### Tour

- 8 stops, with the copy from v2 re-verified.
- Each stop frames its nodes, dims everything else and shows its body text in the inspector.
- "Trace one step" advances. The last stop ends at "The gate is starved".

### Blast radius

- Click nodes to take them offline.
- Starved nodes turn amber and offline nodes brick.
- The panel lists the offline, starved and degraded nodes and the SPOFs.
- The results match the unit-tested algorithm.

### Search palette

- Fuzzy multi-token AND search over nodes, payloads, files and tour stops.
- Arrow keys and Enter select a result. The input keeps focus.
- "receipt" returns "Proof receipts" first.

### Outline view

The accessible equivalent of the map:

- a nested list, zone → node, showing each node's maturity, metric and sources
- keyboard navigable
- selecting a node syncs the 3D view

---

## 10. Panel content

### Inspector (default overview)

- Eyebrow: `「 OVERVIEW · DEFENSE-FOUNDATIONS 」`
- Cormorant headline: "Evidence pipeline. Nothing reaches the gate yet." This headline is derived: it changes when the gate is no longer starved.
- Maturity chips with live counts.
- One mono paragraph on how to use the map.

### "What it does" (250 words or fewer, plain language, for a mixed audience)

Reuse and re-verify v2's copy:

**Lede:** "Proof in. Credit out. Nothing else counts."

**How work flows** (7 steps):

1. A private vault sets the schedule and publishes a hash-stamped copy into the repo.
2. Curriculum policy picks the tracks and the learner's next checkpoint.
3. The learner builds Project 0: the same file-counting tool in Python and in Rust.
4. Both tools run against six shared test inputs, and the output is captured.
5. Each observed run becomes a proof receipt.
6. A strict validator rejects any receipt without real tests or real output.
7. Only verified receipts reach the Phase 0 gate review. Phases 1-12 wait behind it.

**Sections that follow:**

- "Real today, planned next": derived from maturity.
- "Look here first": links to the node with the highest blast impact on `gate`.

### "How it's built"

Cards covering:

- data model and provenance (anchors)
- extraction
- maturity rules
- layout
- rendering and fallback
- live updates and the check whitelist
- what the map deliberately does not claim (no Foundation credit; administrative only)

The tab ends with **"Risks & open questions"**. Each risk is computed from the model where possible, with sources. Expected at the start:

- The gate is starved.
- No proof receipts exist.
- Both Project 0 tools are stubs.
- CI is planned only.
- The integrity tests error without the vault.
- 6 nodes are inferred.
- Any stale anchors.

### Node details panel

Shows:

- title, role
- maturity with `maturityWhy`
- metric with its derivation
- owned globs and matched files
- bound checks with their last results
- sources as `path:lines` with a copy button
- inputs and outputs with payloads
- Trace to gate

In live mode, a "Recent changes" list for the node is added.

### Payload details

Label, schema or shape (quoted from the source, never invented), producers, consumers and sources.

---

## 11. Engineering budgets

| Area | Budget |
|---|---|
| First frame | 300 ms or less at 1440×900, measured as `performance.mark('archmap:first-frame')` from navigation start |
| Frame time | Target 60 fps with 150 particles. p95 frame of 20 ms or less over 5 s in headed Chromium. Headless numbers are informative only. |
| Rendering | Render on demand: no rAF loop while static and paused. Pause entirely when `document.hidden`. |
| Pixel ratio | Cap device pixel ratio at 2 |
| File size | HTML 1.5 MB or less, including engine and fonts |
| Picking | Raycast against node bounding boxes; screen-space spatial hash in the 2D fallback |
| Console | Zero errors or warnings in any test run |
| Test hook | `window.__ARCHMAP` exposes read-only state plus the test actions (select, step, reset, setBlast, setPlan, fitAll, applyPatch). Document it in the README. |

---

## 12. Accessibility

- **Contrast:** at least 4.5:1 for all text; 3:1 for display text at 24 px and above. `--sage` is never used for text.
- **Focus:** a visible 2 px olive focus ring on every interactive element.
- **Keyboard:** full keyboard operation. The Outline view is the non-visual equivalent of the map.
- **Canvas:** `role="img"` with a useful `aria-label`. DOM labels carry `aria-hidden="true"` when they duplicate Outline entries.
- **Touch:** targets of 40 px or more.
- **Reduced motion:** honored as in section 8.9.

---

## 13. Verification

### 13.1 Unit tests (stdlib `unittest`, in `tools/archmap/tests/`)

- **Anchors:** every anchor resolves, every path exists, and every span is within the file's length.
- **Maturity:** rules for each state, including zero collected tests not counting as tested, and overrides requiring a reason.
- **Metrics:** match an independent line count.
- **Blast and SPOF:** match the brute-force reference (section 6.7).
- **Layout:**
  - Deterministic: two runs are byte-identical.
  - Stable: a content-only change moves no node.
  - No plate overlap.
- **Diff:** the patch operations are complete and minimal, and applying a patch to the old model equals the new model.
- **Checks:**
  - Only whitelisted commands run, with `shell=False`.
  - Paths outside the repo are redacted.
  - Durations are never stored.
- **Server:**
  - Binds `127.0.0.1` only.
  - Rejects a bad `Host` header.
  - Rejects `POST` without the token.
  - Returns 404 on unknown paths and on traversal attempts.

### 13.2 End-to-end (Playwright)

Run at 1440×900, 1024×700 and 390×844, opening the file via `file://`.

**Network and page health**

- [ ] Zero network requests apart from the document itself and `data:` URIs.
- [ ] Zero console errors or warnings.
- [ ] No horizontal scroll at any size.
- [ ] No overlap between header text and controls at 1440, 1280, 1180, 1100, 1024, 960 and 900 widths.

**Labels and truth**

- [ ] Label pass targets from section 8.6. Visible label boxes do not intersect each other or the HUD.
- [ ] Every node has sources, and exactly one maturity. Inferred nodes and edges render dashed (check through `__ARCHMAP` state).
- [ ] No number appears in the page text that is not in the model (scan the text nodes).

**Controls**

- [ ] Button `innerText` values match section 9 exactly.
- [ ] Space pauses and resumes the flow, and the particles stop and start.
- [ ] → and ← walk the 8 tour stops, and the camera moves.
- [ ] R resets both the view angle and zoom.
- [ ] Orbit changes yaw and pitch. Shift-drag pans without changing yaw.
- [ ] The wheel zoom clamps at 0.25 and 3.
- [ ] Plan view reaches pitch 90° and orthographic.
- [ ] Rotate turns the view and stops on input.

**Features**

- [ ] Blast radius: taking `receipts` offline starves exactly the set computed independently, and the SPOFs match.
- [ ] The palette returns "Proof receipts" first for "receipt". Arrow keys and Enter select.
- [ ] The Outline view lists all nodes, and selecting one syncs the 3D view.
- [ ] "What it does" has 250 words or fewer. "How it's built" ends with "Risks & open questions".

**Motion, fallback, accessibility and performance**

- [ ] Reduced motion: no particle movement, no camera tween, no auto-rotate.
- [ ] WebGL disabled (`--disable-3d-apis`): the 2D fallback renders, and selection and panels work.
- [ ] Contrast scan passes. The focus ring is visible.
- [ ] `archmap:first-frame` is 300 ms or less (report the observed value).

### 13.3 Live end-to-end

**Never mutate the real repo in tests.**

**Setup**

- Copy the repo to a temp directory, excluding `node_modules` and `.artifacts`:

  ```sh
  rsync -a --exclude node_modules --exclude .artifacts ./ "$TMP/"
  ```

- Start `serve.py --root "$TMP" --port <free>`.
- Leave the temp copy's `.git` read-only in spirit: never run a writing git command there either.

**Checks**

- [ ] Append 20 lines to `$TMP/projects/hello-stats/src/main.rs`. Within 2 s:
  - the `rev` increments
  - hello-stats' height tweens
  - a Changes entry appears naming the file
  - the camera matrix is unchanged
  - the selection and panel scroll are unchanged
- [ ] Add a well-formed receipt to `$TMP/progress/proofs/`, then a malformed one. The checks run, and the verdicts appear on the receipts to integrity edge exactly as the validator reports them.
- [ ] Kill the server: the badge shows RECONNECTING and the page stays intact. Restart it: the page reconciles to the current model.
- [ ] A `POST` without the token returns 403. A bad `Host` header returns 403.

### 13.4 Final repo safety check

1. Compare `git status --short` at the end with the start. The only differences allowed are:
   - new paths under `tools/archmap/`
   - modified `docs/architecture/index.html`
2. `docs/architecture/CODEX_PROMPT.md` is unchanged.
3. The five Invaders audio files are still deleted.
4. `docs/architecture.html` is byte-identical to the start.
5. Run the safe checks from `AGENTS.md` and report each exit code:

   ```sh
   python3 tools/validate_phase0_integrity.py
   python3 tools/validate_curriculum_route.py
   node --check mobile/app.js
   node --check mobile/sw.js
   git diff --check
   ```

### 13.5 Screenshots

Save to `tools/archmap/.artifacts/` (gitignored):

- 1440, 1024 and 390 at fit
- tour stop 6
- blast radius with receipts offline
- Plan view
- Outline view
- a live change mid-animation
- the reduced-motion view

---

## 14. Work plan

### 14.1 Phases and stop points

| Phase | Work | Exit criteria | Stop and report if |
|---|---|---|---|
| 1. Recon (read-only) | Read `AGENTS.md`, `CLAUDE.md`, `README.md`, this prompt and v2. Extract the v2 `MODEL` to `seed_model.json`. Re-verify every citation and every maturity claim against the current files. Record the starting `git status --short`. | Discrepancy table (claim, file, what the file says now). | More than 10% of citations fail, or any maturity claim is wrong. |
| 2. Model | `curated.json` with anchors, `extract.py`, maturity rules, metrics, `checks.py`, risks. Unit tests. | `--strict` extraction passes; unit tests green. | A check writes files, or needs access outside the repo. |
| 3. Pipeline + 2D | `layout.py`, `build.py`, template, 2D fallback renderer rendering the real model. | `build.py` writes a working offline file; `--check` works. | |
| 4. 3D + design | three.js engine, figures, edges, labels, fonts, HUD, responsive. | Section 8 visuals; label targets met at 1440 and 1024. | npm or pip is unavailable (then take the documented fallback, then continue). |
| 5. Interactions + panels | Everything in sections 9 and 10. | Section 13.2 checklist passes. | |
| 6. Live | `serve.py`, `diff.py`, `live.js`, Changes drawer, Run checks. | Section 13.3 passes. | |
| 7. Verify + polish | Full unit + e2e runs, screenshots, safety check, README. | Everything green, or failures explained. | |

### 14.2 Status block (post after every phase)

```
PHASE <n>: <name>  [done | blocked]
Changed:  <paths written this phase>
Evidence: <exact command> -> exit <code>; <observed summary, e.g. "unittest: 41 run, 41 passed">
Findings: <anything surprising about the repo, with path:lines>
Open:     <known issues, deviations from this prompt and why>
Next:     <first action of the next phase>
```

Report only what you observed. Do not write "should pass" or "expected to work": either run it or say it was not run.

---

## 15. Final report format

1. **One sentence** describing what was built.
2. **How to read the map:** 6 bullets or fewer.
3. **How to run it:** the three commands (build, serve, test).
4. **Top 3 findings about the repository,** each with `path:lines`.
5. **Verification:** each command with its exit code and counts. Include the first-frame time and p95 frame time as observed, with the machine they were observed on.
6. **What could not be determined** or was left inferred, and why.
7. **Files written:** the exact list.

---

## 16. Decisions already made (do not re-ask)

- **System modeled:** the evidence-governance pipeline, not runtime software.
- **Output:** `docs/architecture/index.html`, overwriting v2. Tooling goes in `tools/archmap/`.
- **Style:** endr's visual language (section 8). No endr logo or wordmark.
- **Engine:** three.js, vendored and bundled into the single file. Canvas 2D is the fallback.
- **Fonts:** embedded subset WOFF2 (OFL), with system stacks as the fallback.
- **Live mode:** stdlib dev server on `127.0.0.1` with SSE. The static file shows a snapshot badge.
- **Git:** no commit or push. I review and commit myself.

**Ask me only if:**

- a truth claim conflicts with the repository in a way the rules above cannot settle
- a change is needed outside the write scope in section 3A

---

## Appendix A: v2 seed node list (cross-check in phase 1)

| id | title | zone | tier | v2 maturity | inferred |
|---|---|---|---|---|---|
| authority | Aegis phase authority | z-outside | authority | implemented | yes |
| exporter | Projection exporter | z-outside | authority | implemented | yes |
| calendar | Calendar and Todoist | z-outside | authority | implemented | yes |
| projection | Phase 0 projection | z-publish | publish | tested | |
| markers | Generated marker blocks | z-publish | publish | implemented | |
| courses | Course platforms | z-outside | external | planned | |
| endr | endr company lane | z-outside | external | implemented | yes |
| agents | Repository contract | z-route | route | implemented | |
| route | Curriculum route v2 | z-route | route | tested | |
| policy | Parallel policy v1 | z-route | route | implemented | |
| beginner | Beginner policy v1 | z-route | route | tested | |
| starthere | Start Here + sprint | z-route | route | implemented | |
| coursemap | Parallel course map | z-route | route | implemented | |
| issues | Issue ledger | z-route | route | implemented | |
| mobile | Mobile PWA | z-publish | operator | implemented | |
| archpage | Architecture page | z-publish | operator | implemented | |
| learner | Learner | z-op | operator | implemented | yes |
| contract | CLI contract + fixtures | z-route | build | planned | |
| filestats | file_stats (Python) | z-p0 | build | stub | |
| hellostats | hello-stats (Rust) | z-p0 | build | stub | |
| parity | Parity comparison | z-p0 | build | planned | |
| exercises | Course exercises | z-hist | build | implemented | |
| invaders | invaders (Rust) | z-hist | build | stub | |
| commands | Observed command runs | z-p0 | observe | planned | |
| receipts | Proof receipts | z-proof | observe | planned | |
| ledger | Private ledger | z-proof | external | implemented | yes |
| schema | Proof schema v1 | z-verify | verify | implemented | |
| policyval | Beginner policy check | z-verify | verify | tested | |
| routeval | Route validator | z-verify | verify | tested | |
| syntax | Syntax and diff checks | z-verify | verify | implemented | |
| ci | CI workflow | z-verify | verify | planned | |
| integrity | Integrity validator | z-verify | verify | tested | |
| gate | P0 gate review | z-gate | decide | planned | |
| later | P1-P12 phases | z-gate | decide | planned | |

**Zones:**

| id | Label |
|---|---|
| z-outside | External |
| z-publish | Published |
| z-hist | Coursework |
| z-route | Policy |
| z-op | Operator |
| z-p0 | Project 0 |
| z-proof | Evidence |
| z-gate | Gate |
| z-verify | Validators |

**Tier icons:**

| Tier | Icon |
|---|---|
| authority | lock |
| publish | doc |
| route | branch |
| operator | person |
| build | code |
| observe | receipt |
| verify | shield |
| decide | flag |
| external | globe |
