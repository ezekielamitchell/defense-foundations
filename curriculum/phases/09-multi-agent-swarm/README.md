# P9 — Multi-Agent and Swarm Autonomy

**Status:** not started  
**Estimated duration:** 8–10 weeks at 10–15 hours/week

## Focus

Reinforcement learning, MARL, decentralized control, consensus, and communication-constrained coordination. This is the multi-agent core of mission planning: task allocation, consensus, and coordination under degraded communications are exactly what a swarm reconnaissance or distributed ISR mission requires, and they connect directly to the mission-planning and human-machine-teaming layers above. This is distinct from LLM-agent orchestration—the agent sprint handles the latter—but both answer the same question of how multiple autonomous actors divide and execute a mission.

## Topics

MDPs, DQN, PPO, SAC, MAPPO, QMIX, MADDPG, decentralized POMDPs, flocking, communication graphs, Bellman equations, policy gradients, and game-theory basics.

## Materials

See [Autonomy and swarms](../../../learning-materials/09-autonomy-swarms/README.md) and [RL/MARL research](../../../research/rl-marl-swarms/README.md).

## Evidence target

A seeded multi-agent search simulation with baselines and ablations, plus a deterministic Rust backend for fast replay.

## Exit gate

Select an appropriate algorithm, debug a non-learning policy, explain CTDE, and report results across seeds.
