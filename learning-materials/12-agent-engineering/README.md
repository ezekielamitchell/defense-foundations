# Agent Engineering

**Activation:** thin overlay from P4+; full one-week sprint only by explicit scheduling decision  
**Important:** LLM agents are distinct from P9 MARL and do not replace deterministic state machines or behavior trees.

This is the agent layer of mission planning: tool use, planning, memory, and orchestration are how an autonomous system turns operator intent into a sequence of executed actions—an ISR assistant or mission-planning console, with a human approving the consequential ones. The skills here connect upward to human-machine teaming and outward to the perception and ROS 2 layers they coordinate; they are not a general-chatbot exercise.

## Catalog courses

- [#5 Agentic AI Bootcamp](agentic-ai-bootcamp-naik/README.md) — long-running P4+ overlay.
- [#12 LangChain Agentic AI Engineering](langchain-agentic-ai/README.md) — sprint primary.
- [#13 LangGraph Agents](langgraph-agents/README.md) — Day 3 depth.
- [#14 Production AI Agents](production-ai-agents/README.md) — Day 6 depth.
- [#15 Complete Agent & MCP Course](complete-agent-mcp/README.md) — Day 4 depth.
- [#16 AI Agents Bootcamp](ai-agents-bootcamp/README.md) — Days 1–2 alternate.

## Learning order

Tool calling → structured outputs → local Markdown RAG → LangGraph state machines → MCP → evaluation/tracing → deployment and safety.

## Guardrails

Typed I/O, deterministic replay, least-privilege tools, human approval for consequential actions, local-first data handling, and an explicit explanation of why an LLM is needed.
