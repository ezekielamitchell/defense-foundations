# defense-foundations

Read `AGENTS.md` first. It is the provider-neutral repository contract and
controls if this compatibility note conflicts with it.

Active Phase 0 curriculum and foundation-code repository. Foundations, honest evidence, and small runnable Python/Rust artifacts control the work.

## Start here

1. Read `README.md`, `curriculum/phases/00-foundations/README.md`, `progress/README.md`, and `docs/ISSUES.md`.
2. For dates, daily progress, or gate credit, read the current Aegis Nexus `_Phase Config`, `Current Week`, and `Phase 0 Evidence Log`; the vault controls those facts.
3. Verify `docs/aegis-phase0-projection.json` and its owned document markers with `python3 tools/validate_phase0_integrity.py`; fail closed on drift.
4. Inspect the dirty worktree and preserve unrelated user work.

## Current commands

```bash
python3 projects/file_stats/main.py
cargo run --locked --manifest-path projects/hello-stats/Cargo.toml
```

These currently prove only that the stubs run. Do not imply file/statistics behavior or test coverage until implemented and verified.

Observed Foundation proof uses `phase0-proof.v1` receipts under `progress/proofs/`. A verified receipt must pass `python3 tools/validate_phase0_integrity.py --proof <receipt>`; zero collected tests, missing observed output, or schedule/task state cannot produce a verified verdict.

## Rules

- The curriculum architecture is in execution mode; do not renumber phases, redesign the roadmap, or activate advanced lanes without an explicit gate decision.
- Active foundation code now lives in this repository. The retired `defense-foundations-lab` routing is historical and must not control new work.
- Granular progress stays in Aegis Nexus; public repository status changes only after evidence and gate review.
- Preserve Python and Rust as separate, comparable proof paths. Keep the bounded agent overlay non-gate.
- Do not count planning, scheduling, resets, research notes, agent work, or `endr` work as foundation evidence.

Curriculum refresh prepared September 19, 2026: follow AGENTS.md's complete-beginner amendment and curriculum/START_HERE.md. The later reset is not executed by this preparation.
