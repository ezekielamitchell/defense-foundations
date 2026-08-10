# Agent Engineering Sprint

**Status:** the full sprint is **deferred to P8**. Only a bounded slice runs during P0, reset to 0% under Aegis Nexus DD #85 on 2026-08-09 at 16:00 — scheduled ≠ complete
**Length in P0:** at most **two linked blocks per full week** (90-minute COURSE + up to 120-minute LAB), consuming the deterministic-sampler allocation — not a weekly percentage, not a lane
**Schedule:** calendared 2026-08-09 16:00 → 2026-09-13 on the Research calendar; Hugging Face restarts at Unit 0, foundations remain the controlling gate lane, and overlay evidence never satisfies the P0 exit gate

This is a specialization module, not a numbered curriculum phase. It trains bounded LLM-agent skills for the later defense-agent overlay and remains distinct from P9 MARL.

## Prerequisites

Python scripting and environments, Git/README discipline, safe API-key handling, and enough foundation confidence that the sprint will not displace P0.

## What runs during P0 — bounded slice only

The Hugging Face AI Agents Course is the sole P0 agent route. Eligible scope:

1. Agent vs. workflow concepts; tools, actions, observations, messages.
2. Thought → Action → Observation loops and ReAct concepts.
3. Typed tool inputs and outputs; simple Python tools; basic `smolagents` usage.
4. Deterministic or bounded loops, structured traces, failure handling, read-only tools.
5. Observability and evaluation concepts.

Each block must produce one bounded artifact — typed tool, FSM, trace, evaluation harness, read-only project tool, or structured workflow — with a stated capability boundary, a deterministic test input, a malformed-input test, and an explicit statement of what the tool is not authorized to do. **No standalone "watch course" block may be scheduled.**

## Deferred to P8 — not active P0 scope

1. Markdown/agentic RAG: loaders, chunks, embeddings, retrieval, citations.
2. LangGraph state, nodes, edges, conditional routing, and recovery.
3. MCP servers, tools, resources, transports, and capability boundaries.
4. LlamaIndex depth and the GAIA final project.
5. Fine-tuning for function calling.
6. Repository-write agents, hooks, and write boundaries.
7. FastAPI/Docker deployment and production agent operation.
8. Multi-agent orchestration.

Ed Donner's Complete Agent & MCP Course and Eden Marco's LangGraph course are pull-only P8 references and are **not independently schedulable**.

## Materials

See [Agent engineering](../../../learning-materials/12-agent-engineering/README.md).

## Completion evidence

**P0 (bounded):** one small artifact per scheduled weekly block — typed read-only tool, deterministic router, replay harness, bounded `smolagents` run, or tool-use evaluation harness — each with typed I/O, a full trace, a deterministic test, a malformed-input test, and a written capability boundary. None of it counts toward the P0 foundation gate.

**P8 (full sprint):** a local-first research assistant over at least ten documents, with typed outputs, visible state, evaluation, citations, and honest failure modes.

## Safety rules

Typed I/O at boundaries, deterministic replay for serious demos, least-privilege tools, human approval for consequential actions, and no generic chatbot framing.
