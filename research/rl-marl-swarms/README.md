# RL, MARL, and Swarm Research

> **Prepared beginner route:** Research is a later, question-driven reference. No paper or topic here is a prerequisite for beginning P0. The existing paper schedule is unchanged until the separate reset; [the revised route](../../curriculum/COMPETENCY_PATHWAY.md) proposes optional beginner research and keeps advanced topics gated.


## Queue

DQN, TRPO, PPO, SAC, MADDPG, QMIX, MAPPO, and vision-based nano-quadrotor swarms.

## Evidence extraction

Record environment, observation/action spaces, reward design, baseline strength, seeds, variance, communication assumptions, and evaluation horizon. A single successful rollout is not evidence.

## Curriculum connection

P9 owns the bounded single-policy baseline; P10 owns multi-agent coordination and communication-degradation ablations. A Rust batch-simulation backend is justified only when it improves deterministic replay or evaluation throughput.
