# Architecture map v3 — completed verification

## Built

A self-contained endr-styled vector-like 3D architecture board, with source-derived maturity, search, trace, tours, dependency simulation, an accessible Outline, and live repository updates.

The live map is running at **http://127.0.0.1:8766/** and was visibly confirmed in the Codex in-app browser. Port 8765 was already occupied and its process was left untouched. The static output is `docs/architecture/index.html`.

## September 22 refinement

- All 54 connections use deterministic orthogonal routes around padded module footprints, with separate boundary ports, rounded corners, crossing separation and module occlusion. New geometric tests reject any route crossing a module interior.
- Modules now use solid top and side surfaces, clearer icons, subtle status rails and hover elevation. Camera clipping follows viewing distance to eliminate the depth artifacts visible in the earlier build.
- Connection paths themselves support hover explanations and payload selection. Added zoom in/out, magnification readout and Fit controls; softened grid, labels, toolbar and panel treatments.
- Persistent live status reports scans, pending changes, checks, connection loss and source errors. One-second scans / 400 ms debounce remain; five-second scan announcements do not create revisions or change the camera. A 15-second independent health probe reconciles missed updates.
- Browser tests additionally cover the zoom dock, direct path interaction and scan freshness without model/camera changes. Reduced-motion hover transitions are immediate and zero-duration transitions terminate safely.

## How to read it

- Olive is the main evidence path; brick terminators identify blocked rules.
- Height means owned non-blank lines. Maturity is a separate sourced classification.
- Select a module for inputs, outputs, files, checks and exact source anchors.
- Trace to gate finds the first blocker; Blast radius simulates primary-input loss.
- Drag to orbit, shift-drag to pan, wheel/pinch to zoom; Plan view is orthographic.
- Outline and Search expose the complete graph when fit-view labels are suppressed.

## Commands

From `/Users/house/Developer/defense-foundations`:

```sh
python3 tools/archmap/build.py --strict
python3 tools/archmap/serve.py --port 8766
python3 -m unittest discover -s tools/archmap/tests -p 'test_*.py'
```

The server command starts another instance only after the existing instance is stopped, or on a different free port. See README for pinned dependencies and browser test setup.

## Top repository findings

1. **Both Project 0 entry points are stubs.** Python prints a greeting (`projects/file_stats/main.py:1-6`); Rust prints a greeting and a multiplication result (`projects/hello-stats/src/main.rs:1-13`). Direct execution returned greetings; the Rust test binary collected zero tests. These observations do not earn Foundation credit.
2. **No receipt JSON files exist in the real `progress/proofs/` directory.** Its rule requires observed artifacts and commands, and prohibits filling dates with invented receipts (`progress/proofs/README.md:3-11`). The live tests used synthetic, explicitly unverified fixtures only in the isolated copy.
3. **The first CI workflow remains planned.** Issue `P0-W1-L` is `not-started` (`docs/ISSUES.md:42`); no `.github/workflows/*.yml` or `.yaml` files were found. No Actions result was invented.

The earlier route/route-validator `tested` labels were also corrected: the whitelist does not run their `--self-test` branch (`tools/validate_curriculum_route.py:104-110`).

## Verification

All commands below ran from the repository root unless the row identifies the isolated copy.

| Command | Exit | Observed result |
|---|---:|---|
| `python3 tools/archmap/extract.py --strict` | 0 | 34 nodes, 54 edges; zero stale/ambiguous diagnostics |
| `python3 tools/archmap/build.py --strict` | 0 | Generated the standalone HTML |
| `python3 tools/archmap/build.py --check` | 0 | CURRENT; final comparison repeated after polish |
| `python3 -m unittest discover -s tools/archmap/tests -p 'test_*.py'` | 0 | 40 run, 40 passed |
| `node tools/archmap/tests/e2e/run.cjs` | 0 | 17/17 checks passed |
| `node tools/archmap/tests/e2e/live.cjs` | 0 | Live header breakpoints, patch/state preservation, receipts, automatic checks, HTTP guards and reconnect passed in an isolated copy |
| `python3 tools/validate_beginner_policy.py` | 0 | PASS; no test count |
| `python3 -m unittest -v tests.test_beginner_policy` | 0 | 7 collected, 7 passed |
| `node --check mobile/app.js` | 0 | No syntax errors |
| `node --check mobile/sw.js` | 0 | No syntax errors |
| `git diff --check` | 0 | No whitespace errors in the tracked diff |
| `python3 tools/validate_phase0_integrity.py` | Not run | Reads private authority outside the task's read boundary |
| `python3 tools/validate_curriculum_route.py` | Not run | Reads private vault phase documents |
| `python3 -m unittest -v tests.test_phase0_integrity` | Not run | Reads private authority and writes fixtures |

| Viewport | Visible titles | Blocked labels | First usable frame |
|---|---:|---:|---:|
| 1440×900 | 34/34 | 4/4 | 64.4 ms |
| 1024×700 | 32/34 | 4/4 | 63.1 ms |
| 390×844 | 28/34 | 4/4 | 60.9 ms |

- Headed Chrome on **darwin arm64 Apple M4 Pro**: **17.4 ms p95** over five seconds / 300 frame intervals, with **150 particles**. This is a measured local result, not a guarantee on other hardware.
- The first usable frame is the complete Canvas preview; WebGL2 starts after its first presentation. All regular headed runs reached WebGL2. Disabling 3D APIs exercised the Canvas fallback.
- Final standalone size: **1,157,839 bytes**. Embedded WOFF2 total: **116,572 bytes**.
- Latest isolated live edit appeared in **1434 ms**, below the two-second target. Height changed; positions, camera matrix, selection and inspector scroll did not. Reconnect preserved the search query and reconciled an edit made while offline.
- Both receipt verdicts exactly matched direct local `validate_proof` results. A well-formed unverified fixture returned PASS; a malformed fixture returned FAIL with the exact missing-field diagnostic. Automatic checks subsequently observed seven passing beginner tests.
- Missing token and bad Host returned **403**. Unknown and traversal paths returned **404** in unit tests; no CORS headers were sent.
- Offline runs made zero network requests beyond the document/data URLs, with zero console warnings/errors. Live tests observed zero page exceptions. Expected transport failures occur while deliberately disconnecting the test server.
- Header overlap/page-scroll checks passed at 1440, 1280, 1180, 1100, 1024, 960 and 900 widths in both static and live mode. Visible labels did not intersect other labels, zone labels, blocked labels or HUD regions at the three required viewports.
- Tests exercised exact labels, flow pause/resume and idle rendering, camera controls, all tour stops, independently computed blast/SPOFs, fuzzy search ordering, Outline selection, source hover, keyboard canvas traversal, panel content, numeric provenance, contrast/focus, topology fade transitions, reduced motion, fallback and patch preservation. The live suite additionally verified scan announcements without revision or camera changes.

### Screenshots and machine-readable records

All are under `tools/archmap/.artifacts/` (gitignored):

- `fit-1440.png`, `fit-1024.png`, `fit-390.png`
- `tour-6.png`, `blast-receipts.png`, `plan.png`, `outline.png`
- `live-mid-animation.png`, `reduced-motion.png`, `fallback.png`
- `e2e-report.json`, `live-report.json`, `command-report.json`, `safety-report.json`

## Limits and deliberate deviations

- Private authority was not read. Its existence, current integrity and full validator results are unknown. Unavailable checks are not reported as failed or absent-vault errors. Historical pass/error counts were not reused.
- External roles, human responsibilities, some relationships, zone groupings and tour explanations remain sourced interpretations. Inferred nodes: **authority, exporter, calendar, courses, endr, learner, ledger**.
- A receipt-contract PASS does not establish that its asserted commands actually ran, verify private authority, promote a phase, or grant Foundation credit.
- `--check` normalizes both generation and check-observation timestamps. The brief requested only generation-time normalization; keeping real `ranAt` observations requires this additional normalization.
- The combined frame is WebGL2 figures plus Canvas vector routes and DOM labels. Initial use is progressively rendered before the GPU starts. This meets the measured first-frame target without pretending GPU startup is instantaneous.
- Fit view intentionally suppresses some labels at smaller sizes. All 34 nodes remain available through Outline and Search; desktop and tablet visibility targets passed.
- Test-only browser/runtime dependencies and temporary copies live in `.artifacts/`; the production package manifest has only the two requested pinned devDependencies.

## Repository preservation

- Git branch: `codex/aegis-beginner-reset-2026-09-19`; HEAD: `2e13798e4fdc3bc2e476ab6938e0c5cd261066b3`. No writing Git operation was used.
- Comparing `git status --short` to the saved baseline added only `?? tools/archmap/`; no pre-existing status entry disappeared. The generated index was already inside the baseline's untracked architecture directory.
- All five Invaders audio deletions remain deleted.
- Protected SHA-256 values are unchanged:

- `docs/architecture.html`: `5e123fb04cfd38257598930f6cec4fd16f6582b644cb658bdbf62cc0d10e90b7`
- `docs/architecture/CODEX_PROMPT.md`: `6e3057fdab888f1ae83a728f90fe3efeda08ce3c41f8a82a4feebbae18f84dc8`
- `docs/aegis-phase0-projection.json`: `e96b35ec9d43329a8f465facadca664e4576b21816a8404df9040c4e57bf0516`

## Exact persistent file inventory

This includes the preserved Phase 1 seed/audit and all created or updated task files. Dependency caches, compiled bytecode, test copies and screenshots are excluded from the persistent inventory and are contained under the ignored directories described above. `files-written.txt` contains the same paths.

```text
docs/architecture/index.html
tools/archmap/.gitignore
tools/archmap/README.md
tools/archmap/RECON.md
tools/archmap/VERIFICATION.md
tools/archmap/build.py
tools/archmap/checks.py
tools/archmap/curated.json
tools/archmap/diff.py
tools/archmap/extract.py
tools/archmap/files-written.txt
tools/archmap/layout.py
tools/archmap/package-lock.json
tools/archmap/package.json
tools/archmap/recon_report.json
tools/archmap/routing.py
tools/archmap/seed_model.json
tools/archmap/serve.py
tools/archmap/tests/e2e/copy_repo.py
tools/archmap/tests/e2e/inspect-headed.cjs
tools/archmap/tests/e2e/inspect.cjs
tools/archmap/tests/e2e/live.cjs
tools/archmap/tests/e2e/run.cjs
tools/archmap/tests/support.py
tools/archmap/tests/test_anchors.py
tools/archmap/tests/test_blast.py
tools/archmap/tests/test_checks.py
tools/archmap/tests/test_diff.py
tools/archmap/tests/test_extract.py
tools/archmap/tests/test_layout.py
tools/archmap/tests/test_maturity.py
tools/archmap/tests/test_routing.py
tools/archmap/tests/test_serve.py
tools/archmap/vendor/THREE-LICENSE.txt
tools/archmap/vendor/build_fonts.py
tools/archmap/vendor/fonts/OFL.txt
tools/archmap/vendor/fonts/cormorantgaramond-500.woff2
tools/archmap/vendor/fonts/ibmplexmono-400.woff2
tools/archmap/vendor/fonts/ibmplexmono-500.woff2
tools/archmap/vendor/fonts/inter-400.woff2
tools/archmap/vendor/fonts/inter-500.woff2
tools/archmap/vendor/fonts/inter-600.woff2
tools/archmap/vendor/fonts/manifest.json
tools/archmap/vendor/fonts/notosansjp-300.woff2
tools/archmap/vendor/fonts/sources/cormorantgaramond/CormorantGaramond[wght].ttf
tools/archmap/vendor/fonts/sources/cormorantgaramond/OFL.txt
tools/archmap/vendor/fonts/sources/ibmplexmono/IBMPlexMono-Medium.ttf
tools/archmap/vendor/fonts/sources/ibmplexmono/IBMPlexMono-Regular.ttf
tools/archmap/vendor/fonts/sources/ibmplexmono/OFL.txt
tools/archmap/vendor/fonts/sources/inter/Inter[opsz,wght].ttf
tools/archmap/vendor/fonts/sources/inter/OFL.txt
tools/archmap/vendor/fonts/sources/notosansjp/NotoSansJP[wght].ttf
tools/archmap/vendor/fonts/sources/notosansjp/OFL.txt
tools/archmap/web/edges.js
tools/archmap/web/engine2d.js
tools/archmap/web/engine3d.js
tools/archmap/web/labels.js
tools/archmap/web/live.js
tools/archmap/web/main.js
tools/archmap/web/style.css
tools/archmap/web/template.html
tools/archmap/web/ui.js
```
