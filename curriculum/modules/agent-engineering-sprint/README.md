# Agent Engineering Sprint

**Status:** not started; explicit scheduling decision required  
**Length:** one full-time week  
**Default window:** Dec 2026+, unless a P0 gate review deliberately promotes it earlier

This is a specialization module, not a numbered curriculum phase. It trains bounded LLM-agent skills for the later defense-agent overlay and remains distinct from P9 MARL.

## Prerequisites

Python scripting and environments, Git/README discipline, safe API-key handling, and enough foundation confidence that the sprint will not displace P0.

## Seven-day sequence

1. Agent loops, tool calling, and typed tool schemas.
2. Markdown RAG: loaders, chunks, embeddings, retrieval, and citations.
3. LangGraph state, nodes, edges, conditional routing, and recovery.
4. MCP servers, tools, resources, transports, and capability boundaries.
5. Repository instructions, agent files, hooks, and safe write boundaries.
6. FastAPI/Docker deployment, tracing, testing, injection defense, and evaluation.
7. Integrate the pieces into an Aegis research-agent capstone.

## Materials

See [Agent engineering](../../../learning-materials/12-agent-engineering/README.md).

## Completion evidence

Seven daily artifacts culminating in a local-first research assistant over at least ten documents, with typed outputs, visible state, evaluation, citations, and honest failure modes.

## Safety rules

Typed I/O at boundaries, deterministic replay for serious demos, least-privilege tools, human approval for consequential actions, and no generic chatbot framing.
