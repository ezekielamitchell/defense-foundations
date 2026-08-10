# Curriculum Timeline

This timeline is a projection of Aegis Nexus `01_Daily/_Phase Config.md` as of **2026-08-09**. The vault config is the sole hard-date authority. P1–P12 remain undated until an explicit gate promotion.

> **Current reset (Aegis Nexus DD #85, reset ID `A20-2026-08-09-complete-hard-reset`):** P0 Day 0 and the gate clock begin Sunday **2026-08-09 at 16:00 America/Los_Angeles**. Condensed Week 1 is Aug 9 only; Week 2 begins Monday Aug 10. The six-week minimum gate is Aug 30 and the eight-week maximum gate is Sep 13. Work before the cutover remains audit-valid history but earns zero active credit across foundations, projects, courses, samplers, agent work, endr, and career conversion.
>
> **Operating envelope:** Monday–Friday **09:30–23:00**, Saturday **09:30–18:15**, Sunday **09:30–18:00** (America/Los_Angeles), with 15-minute cross-domain transitions. Protected daily: sleep 00:00–04:30, gym 05:00–06:15, breakfast 07:00–08:00, lunch 12:00–13:00, dinner 18:30–20:00.
>
> **Daily model:** Primary Build → Support Work → Research → Weekly Sampler. One dominant artifact per day. No daily Python, Rust, CV, agent, or paper lane.
>
> **Non-gate overlays (DD #85/#78):** the **Hugging Face AI Agents Course** runs at most **two linked blocks per full week** (90-minute COURSE + up to 120-minute LAB), consuming the deterministic-sampler allocation — no fifth lane, no new percentage bucket, no gate credit. Scope is tools, messages, Thought → Action → Observation, ReAct, and typed bounded read-only tools; LangGraph depth, RAG, MCP production work, LlamaIndex depth, GAIA, fine-tuning, and multi-agent orchestration are deferred to later phases. A **daily research paper** runs 60 minutes at 08:00–09:00 on the Research calendar. Neither overlay satisfies the Python/Rust/Linux/Git exit gate.

### Superseded resets — historical record only

These anchors are retained for audit and are **not** the current plan:

> **DD #70 (superseded):** P0 Day 0/1 at 2026-08-01 10:00; condensed Week 1 through Aug 2; Week 2 from Aug 3; envelope Mon–Fri 08:00–23:00, Sat 10:00–17:00, Sun 15:00–17:00; agent overlay at ~25–30% with LangGraph/MCP/RAG in active scope.
>
> **DD #55 (superseded):** P0 Day 0/1 at 2026-07-17, compressed ramp through 2026-07-19, gate clock from 2026-07-20.

## Hard dates

| Milestone | Date |
|---|---|
| Commencement walk complete | 2026-06-14 |
| Networking outreach + internship/contract option historical start | 2026-06-22 |
| P0 Day 0 / reset begins | **2026-08-09 at 16:00** |
| Gate clock / condensed Week 1 begins | **2026-08-09** |
| Condensed Week 1 ends | **2026-08-09** |
| First full Monday–Sunday week (Week 2) | **2026-08-10 → 2026-08-16** |
| Resume, LinkedIn, and GitHub verified-claim audit | 2026-08-02 |
| GitHub profile aligned | 2026-08-02 |
| Midpoint reachability check | **2026-08-23** |
| P0 six-week minimum gate | **2026-08-30** |
| GDARS/CASEset promotion or date re-decision | 2026-08-30 |
| First gate-dependent application wave | 2026-08-31 |
| P0 eight-week maximum gate | **2026-09-13** |
| Final Seattle University ML course | Sep–Dec 2026 |
| Degree conferred | Fall 2026 term end, approximately Dec 2026 |
| Early offer (optional Path B fallback only) | 2026-12-07 |
| KL go/no-go decision | 2026-12-20 |
| KL preparation | 2027-01-01 → 2027-02-28 |
| Kuala Lumpur move window | 2027-03-01 → 2027-05-31 |
| Offer-signed target | 2027-07-07 |
| Full-time start target | 2027-09-07 |

## Active operating scope

Foundations are the only active curriculum lane:

- Python and small CLIs.
- Rust, Cargo, and Rustlings.
- Linux shell and development tools.
- Git/GitHub workflow.
- Tests, README quality, reproducibility, and repo hygiene.

There is no automatic PyTorch, YOLO, ROS 2/Nav2, autonomous consequential-agent, swarm, MARL, or robotics ramp. The only active specialization exceptions are the three **non-gate** items defined in DD #85/#78: a bounded weekly OpenCV sampler, a bounded weekly Hugging Face Agents block, and the daily research paper. LangGraph, RAG, MCP, LlamaIndex, and multi-agent orchestration are **not** active P0 scope. GDARS and CASEset remain maintenance-only and receive no fixed P0 delivery dates.

## Phase 0 plan — paired file-statistics CLI

The Phase 0 artifact is a **paired Python/Rust file-statistics CLI**: `projects/file_stats` (Python) and `projects/hello-stats` (Rust). Week 1 is the one-day cutover on Sunday Aug 9 from 16:00, with endr as the only remaining work block. Week 2 resumes the full Monday–Sunday cadence on Aug 10.

| Week | Dates | Primary Build focus | Support + weekly samplers | Required proof or decision |
|---|---|---|---|---|
| Week 1 | Aug 9 | Zero-state cutover; no curriculum backfill | **No sampler**; endr 16:00–18:00 only | active denominators remain zero; exact Monday command recorded |
| Week 2 | Aug 10–16 | Rust CLI happy path; Python validation surface | shell/grep/find proof · OpenCV I/O · HF Unit 1 typed read-only tool | Both CLIs run on a valid fixture; `cargo test` and `pytest` pass |
| Week 3 | Aug 17–23 | Reconcile the Python/Rust output contract; schema validation | branch/diff/PR workflow · OpenCV frame iteration · HF deterministic T-A-O router | Midpoint reachability check Aug 23 |
| Week 4 | Aug 24–30 | Harden malformed input, CI checks, deterministic replay | **create `.github/workflows/`** · OpenCV metadata record · HF replay harness | Six-week minimum gate Aug 30: PASS / PARTIAL PASS / REMEDIATION REQUIRED |
| Week 5 | Aug 31–Sep 6 | Cold-run recreation and benchmarks; close minimum-gate gaps | clean-runner verification · OpenCV classical pipeline · bounded smolagents run | Gate-dependent applications only if permitted; no automatic phase activation |
| Week 6 | Sep 7–13 | Remediate remaining gate evidence; assemble the decision package | fresh-clone re-run in tmux · OpenCV malformed input · HF tool-use evaluation harness | Eight-week maximum gate Sep 13: written promotion or written extension |

Reaching the maximum date does not promote the phase, and no gate review schedules P1.

## Evidence and history boundary

Work before 2026-08-09 at 16:00 remains audit-valid history but is excluded from every active denominator. Completed courses, Rustlings progress, agent work, endr artifacts, and earlier CLIs may inform diagnosis, but none pre-checks the reset trackers. Planning, dashboard work, Calendar work, and this reset are not curriculum evidence.

**Evidence source rule:** until `.github/workflows/` exists (a Week 4 task), acceptable proof is **local check/test output** with the exact command line. A GitHub Actions run URL may only be cited after the workflow is committed.

## Later-phase scheduling rule

P1–P12 and specialization modules are intentionally undated. Assign a date only after an evidence gate passes and the lane is explicitly promoted during a review. A failed or delayed P0 gate causes scope cuts or a written extension, not another anchor reset or an automatic advanced-lane ramp.
