# Repository architecture map

A generated, offline-first evidence-governance map for `defense-foundations`: a paper-and-olive vector board that upgrades to WebGL2, with a Canvas 2D fallback, anchored sources, an accessible Outline, and an optional live repository watcher. This is administrative tooling; it never creates evidence or grants Foundation credit.

## Run from the repository root

```sh
npm ci --prefix tools/archmap
python3 tools/archmap/build.py --strict
python3 tools/archmap/serve.py
python3 -m unittest discover -s tools/archmap/tests -p 'test_*.py'
```

Open `http://127.0.0.1:8765` for live updates, or `docs/architecture/index.html` directly for the snapshot. The HTML contains the model, engine, CSS, fonts and licenses; the snapshot makes no network requests.

```sh
python3 tools/archmap/build.py          # regenerate the standalone file
python3 tools/archmap/build.py --check  # 0 = current, 1 = stale
python3 tools/archmap/build.py --watch  # rebuild on changes; reload file:// manually
python3 tools/archmap/extract.py --strict
```

Python's standard library handles extraction, checks, layout, patches and HTTP. The implementation runs on the observed Python 3.9 runtime and newer; Python 3.10+ is recommended. Production build dependencies are pinned to three 0.186.0 and esbuild 0.28.2. Fonts are already vendored; rebuilding does not download them. `vendor/fonts/manifest.json` records source revision, URLs, digests and subset sizes. Each family retains its OFL notice; three's MIT notice is embedded in the HTML.

## Read and operate the map

- The olive route is the main modeled evidence path. Other connections become prominent on selection. A brick terminator is a blocked rule, not a working data connection.
- Height encodes non-blank owned lines, not quality or maturity. Large footprints mark the primary evidence components. Dashed objects are inferred or planned; hatching means stub; the check seal means an observed bound test passed.
- Drag to orbit, shift/middle/right-drag to pan, wheel or pinch to zoom. Double-click frames a module. Plan view uses an orthographic camera. Rotate stops on input. The bottom zoom controls show camera magnification; Fit frames the complete architecture.
- Select a module for ownership, check results and anchored sources. Trace to gate names the first modeled blocker. Hover a connection for its role and endpoints; click its path or receipt verdict for its payload. Search accepts multiple fuzzy AND tokens.
- Space toggles flow; arrows traverse the tour; R resets; B toggles blast; P toggles Plan; O opens Outline; C opens live Changes; slash or Cmd/Ctrl-K searches. Escape closes the palette, exits blast, or clears selection. Canvas Tab traverses modules; Enter selects. Outline provides the complete keyboard-readable graph.
- Blast mode models dependency loss. Data inputs are primary, else control inputs, else all inputs. A node starves only when all primary suppliers are dead. Blocked and feedback edges do not carry dependencies. SPOFs are computed against the gate and verified against an independent reference.

Connection paths use deterministic orthogonal routing around padded module footprints, separate boundary ports and rounded corners. Primary paths have stronger strokes; context paths recede until hovered or selected. Module silhouettes occlude paths, and dynamic camera clipping prevents surface depth artifacts.

## Truth and scope

`seed_model.json` preserves the original v2 data. `curated.json` stores explicit roles, literal anchors, spans, ownership globs, edges, tour copy and sourced overrides. Extraction resolves anchors to current line ranges and hashes. Missing or ambiguous anchors fail strict mode; a non-strict live extraction exposes stale provenance.

Maturity precedence is: sourced override → explicit deployment evidence → observed bound check with collected and passed tests → exact placeholder signature → owned files → planned. Zero collected tests cannot establish `tested`. External roles remain inferred. File presence does not prove completed behavior. Gate readiness is only a modeled condition and cannot authorize promotion.

The exact command whitelist is in `checks.py`. Each command uses `shell=False`, a timeout and `PYTHONDONTWRITEBYTECODE=1`. Durations and raw subprocess output are not retained. Outside paths in check errors are redacted. Integrity, route and integrity-unit checks are **unavailable** because they access private authority and/or write fixtures. They are never silently substituted or represented by historical counts. The separate receipt observer invokes only the audited repository-local `validate_proof` function; a PASS means receipt-contract acceptance, not verified authority, observed implementation or gate credit.

Source excerpts are capped at the first 12 lines / 1,000 characters; anchors retain the full span and exact current line range. Displayed facts derive from sources, file/test counts, Git or observation timestamps. UI identifiers and visual encodings—P0, tour IDs, source line numbers, view scales, WebGL2, and the height formula—are explicitly not measured system performance. Every quantitative metric exposes its derivation. Local storage contains only panel and tab preferences.

## Live mode

The server binds **127.0.0.1 only** and accepts only its exact loopback or localhost Host header. It serves `/`, `/api/health`, `/api/model`, `/events`, and token-protected `POST /api/run-checks`; there is no arbitrary static-file handler or CORS access. It watches source and ownership inputs, including new receipts, polls every second, and debounces for 400 ms. Checks run two seconds after a settled extraction; a running check has at most one latest queued rerun. A persistent status strip distinguishes current, scanning, checking, reconnecting and extraction-error states. Scan observations are broadcast every five seconds without changing model revisions or moving the camera. SSE transport heartbeats occur every 15 seconds; an independent 15-second health probe reconciles missed revisions and detects disconnected servers. Reconnect backs off from one to ten seconds and reconciles the model without clearing the view.

Content patches preserve node positions, camera, selected object, hover, tour, tab, panel scroll and palette. Height transitions last 400 ms, topology movement 520 ms, and additions/removals fade over 300 ms. Metric/maturity changes receive a brief outline and transition tag. The newest 200 observations remain in Changes. Check errors and local receipt verdicts appear on their routes. Reduced motion uses static markers and outlines, immediate camera changes and no automatic rotation. Paused static and hidden pages do not run a render loop.

The first visible frame is a usable Canvas board. GPU initialization occurs after its presentation so a cold graphics driver cannot block initial use. The final renderer is WebGL2 when available. Performance reports distinguish that initial usable frame from GPU initialization, and headed frame timing from informative headless timing.

`--check` ignores both `meta.generated` and each check's `ranAt`: these are fresh observation timestamps. All semantic data and bundled bytes must match. This intentionally extends the brief's single-timestamp normalization; preserving actual check observation times is more truthful than fabricating deterministic ones.

## Browser tests (optional development tooling)

Browser tooling stays outside the production package manifest. Install it in the ignored artifact directory, then point the harness at a Chromium executable if necessary:

```sh
npm install --prefix tools/archmap/.artifacts/test-runtime --no-save --package-lock=false playwright@1.58.2
ARCHMAP_CHROMIUM='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' node tools/archmap/tests/e2e/run.cjs
ARCHMAP_CHROMIUM='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' node tools/archmap/tests/e2e/live.cjs
```

The default is headed Chrome on macOS; `ARCHMAP_HEADLESS=1` is optional. `ARCHMAP_PLAYWRIGHT` can point to another installed Playwright module. Screenshots and JSON reports go under `.artifacts/`. The live suite copies authored repository files and Git metadata into `.artifacts/live-repo`, excluding dependency/build caches. It only mutates that copy. Its synthetic receipts explicitly claim **no implementation evidence**. No test invokes a writing Git command.

### Read-only browser test hook

`window.__ARCHMAP.state` returns a deeply frozen snapshot, including the model, camera matrix, renderer, visible label boxes, particle positions, frame samples and current UI state. Mutating it cannot modify the application. The intentional actions are:

- `select(nodeId)`, `step(direction = 1)`, `reset()`
- `setBlast([nodeIds])` to enable / set the offline set; `setBlast(false)` to exit
- `setPlan(boolean)`, `fitAll()`
- `applyPatch({model, changes, trigger, at})`, with a complete replacement model and descriptive field operations

The hook is an in-page test interface, not a server command endpoint. `diff.py` separately verifies complete, minimal field patches by applying them and comparing the exact resulting model.

## Preservation and provenance

Only `tools/archmap/**` and the generated `docs/architecture/index.html` are task outputs. The separate `docs/architecture.html`, prompt, publisher projections, existing dirty work and deleted Invaders audio remain preserved. Git is read-only. `RECON.md` and `recon_report.json` retain the original paused checkpoint; their historical status is superseded by the completed continuation documented in `VERIFICATION.md`.
