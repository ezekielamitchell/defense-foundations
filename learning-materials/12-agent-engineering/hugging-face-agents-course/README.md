# Hugging Face AI Agents Course

**Source:** [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)

**Activation:** bounded Phase 0 agent overlay, A20 reset 2026-08-09 at 16:00. **Maximum two linked blocks per full week: one 90-minute COURSE and one LAB up to 120 minutes**, consuming the deterministic-sampler allocation. No fifth lane, no gate credit.

**Status:** active reset progress 0%; Unit 0 not started; a Calendar block or this folder does not count as completion

## What this is

This folder is the hands-on workspace for the free Hugging Face AI Agents Course. The course is the official spine for the bounded Aegis agent-engineering overlay.

**Active in P0:** agent loops, typed tools, messages, Thought → Action → Observation, ReAct concepts, basic `smolagents`, deterministic bounded loops, tracing, and observability/evaluation concepts.

**Deferred to P8:** agentic RAG, LangGraph depth, LlamaIndex depth, MCP production work, the GAIA final project, fine-tuning for function calling, multi-agent systems, and production deployment.

Progress, scheduling, and evidence decisions live in Aegis Nexus under `AI Agent Engineering Sprint`. This repository holds only code, commands, tests, evaluation output, and short implementation notes.

## Why it exists

The course provides a practical sequence from Python tool functions through agent frameworks to an evaluated final agent. Phase 0 uses only the early, bounded portion of that sequence. It supports the agent overlay without replacing the gate-controlling Python, Rust, Linux, Git, test, CI, and README work in Phase 0.

## Requirements

- Basic Python and LLM familiarity
- Python 3.11 or newer
- `uv` for isolated Python environments when an exercise needs dependencies
- A Hugging Face account only when a unit requires the Hub or a Space
- API keys supplied through environment variables and never committed

## Course route

### P0 route — one linked COURSE + LAB pair per full week

| Week | Course sections | Required artifact |
|---|---|---|
| Week 2 | Unit 1 — "What is an Agent?", "Messages and Special Tokens", "What are Tools?" | Typed read-only tool with a JSON-serializable return type and a stated capability boundary |
| Week 3 | Unit 1 — Thought-Action-Observation cycle; "Thought: Internal Reasoning and the ReAct Approach" | Deterministic tool router (no LLM in the loop) emitting a byte-identical trace across two runs |
| Week 4 | Unit 1 — "Actions"; "Observe: Integrating Feedback to Reflect and Adapt" | Replayable tool-invocation harness with deterministic and malformed fixtures |
| Week 5 | Unit 1 — "Dummy Agent Library"; Unit 2.1 — "Why use smolagents", "Building Agents That Use Code" (read-only scope) | Bounded `smolagents` run over the read-only tool, with a full trace and a permission list containing no write or network capability |
| Week 6 | Bonus Unit 2 — "Introduction", "What is Agent Observability and Evaluation?" | Tool-use evaluation harness reporting trace completeness and policy violations |

### Deferred — not scheduled during P0

| Course unit | Status |
|---|---|
| Unit 2.2 LlamaIndex · Unit 2.3 LangGraph | **Deferred to P8** |
| Unit 3 — agentic RAG | **Deferred to P8** |
| Unit 4 — GAIA final project | **Deferred to P8** |
| Bonus Unit 1 — fine-tuning for function calling | **Deferred to P8** |
| Bonus Unit 3 — agents in games | **Not scheduled** |

## Fresh progress tracker — A20 reset 2026-08-09 16:00

- [ ] Unit 0 — Welcome and course route
- [ ] Unit 1 — agent fundamentals, tools, messages
- [ ] Unit 1 — Thought-Action-Observation and ReAct
- [ ] Unit 1 — actions and observations
- [ ] Unit 1 — dummy agent library + bounded Unit 2.1 smolagents
- [ ] Bonus Unit 2 — observability and evaluation concepts

Existing files, notes, or prior browsing do not pre-check these items. **Course consumption alone is never evidence** — each checked item requires its bounded artifact.

Do not complete every framework merely for coverage. LlamaIndex, LangGraph, RAG, MCP, and paid-course instruction are out of P0 scope entirely.

## Setup

Unit 0 requires no local installation. When the first coding exercise begins, create the smallest unit-specific environment inside this folder:

```sh
cd ~/Developer/defense-foundations/learning-materials/12-agent-engineering/hugging-face-agents-course
uv init unit1-agent-fundamentals
cd unit1-agent-fundamentals
uv add pytest
```

Add framework packages only when the active course page requires them. Do not preinstall the whole agent stack.

## Run and test

There is no runnable course artifact yet. Each future unit folder must document its own exact commands. The expected baseline shape is:

```sh
uv run python main.py
uv run pytest
```

Replace these placeholders with observed commands and output when Unit 1 work exists. A watched page, empty scaffold, or dependency installation is not evidence.

## Evidence boundary

- Course completion is tracked only in the Aegis `AI Agent Engineering Sprint` module.
- Agent-course work never enters the Phase 0 foundations evidence ledger.
- Only runnable output, tests, traces, evaluation results, or a useful technical note count as overlay proof.
- The eventual `aegis-research-agent` portfolio project belongs in a separate repository.

## Current limitations

- Unit 0 has not been verified complete.
- No exercise code, tests, trace, benchmark, or certificate exists yet.
- No framework has been selected beyond the sequence authorized by the active Calendar blocks.

## Next improvement

Complete the scheduled Unit 0 introduction, record the exact stopping point in Aegis Nexus, then begin Unit 1 with the smallest two-tool Python exercise after the required foundation block remains protected.
