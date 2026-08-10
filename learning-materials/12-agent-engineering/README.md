# Agent Engineering

**Activation:** bounded P0 overlay under Aegis Nexus DD #85/#78; A20 reset begins 2026-08-09 at 16:00. **Only the Hugging Face AI Agents Course is schedulable during P0** — at most two linked blocks per full week (90-minute COURSE + up to 120-minute LAB), consuming the deterministic-sampler allocation, with no gate credit. Every other folder here is a pull-only P8 reference and is **not independently schedulable**. Later expansion requires a separate promotion decision.

**Progress:** Hugging Face restarts at Unit 0 with 0% active credit; no existing note, code file, or prior viewing pre-checks a course item. The Udemy courses (#5, #12–16) carry no P0 progress tracking because none of them is schedulable during P0.

**Important:** LLM agents are distinct from P9 MARL and do not replace deterministic state machines or behavior trees.

This is the agent layer of mission planning: tool use, planning, memory, and orchestration are how an autonomous system turns operator intent into a sequence of executed actions—an ISR assistant or mission-planning console, with a human approving the consequential ones. The skills here connect upward to human-machine teaming and outward to the perception and ROS 2 layers they coordinate; they are not a general-chatbot exercise.

## Catalog courses

There is **no multi-day agent sprint during Phase 0** and no course here is assigned a sprint day. Exactly one route is schedulable.

### Active — bounded P0 route

- [Hugging Face AI Agents Course](hugging-face-agents-course/README.md) — `scheduled_on_demand`. The official free spine and the **only** schedulable agent route in P0: at most two linked blocks per full week (90-minute COURSE + up to 120-minute LAB), consuming the deterministic-sampler allocation, with **no Phase 0 gate credit**.

### Pull-only — later-phase depth

Reference material. **Not independently schedulable**, no calendar block, no sprint day. Pull only from inside an issue that already has its own artifact and acceptance test, and only once the phase gating it is active.

- [#15 Complete Agent & MCP Course](complete-agent-mcp/README.md) — Ed Donner. P8 MCP depth. MCP is not active Phase 0 scope.
- [#13 LangGraph Agents](langgraph-agents/README.md) — Eden Marco. P8 LangGraph depth, available only after a deterministic typed tool and replay harness exist. LangGraph is not active Phase 0 scope.

### Archived reference — not scheduled

Retained for the record. Overlapping or superseded; requires an explicit promotion decision before any future use.

- [#12 LangChain Agentic AI Engineering](langchain-agentic-ai/README.md) — archived reference.
- [#14 Production AI Agents](production-ai-agents/README.md) — archived reference; production deployment is not active Phase 0 scope.
- [#16 AI Agents Bootcamp](ai-agents-bootcamp/README.md) — archived reference; RAG is not active Phase 0 scope.
- [#5 Agentic AI Bootcamp](agentic-ai-bootcamp-naik/README.md) — archived reference; multi-agent orchestration is not active Phase 0 scope.

## Learning order

**P0 (active, bounded):** Hugging Face agent fundamentals → typed tool calling → deterministic Thought-Action-Observation loops → tracing and evaluation concepts.

**P8 (deferred, not current scope):** local Markdown/agentic RAG → LangGraph state machines → MCP → LlamaIndex depth → GAIA project → fine-tuning → deployment, multi-agent orchestration, and production safety.

## Guardrails

Typed I/O, deterministic replay, least-privilege tools, human approval for consequential actions, local-first data handling, and an explicit explanation of why an LLM is needed.
