# Curriculum Index

The curriculum is organized into 13 evidence-gated phases. Its purpose is not to consume content in order; it is to build inspectable capability through projects, measurements, and written limitations. The phases are an execution order; the capability they assemble into is the [autonomy capability map](../README.md#autonomy-capability-map)—foundations, systems, perception, agents, robotics, autonomy, capstone—and the target is an integrated autonomous system, not a portfolio of isolated models.

## Category groups

- **Foundations:** [P0](phases/00-foundations/README.md)–[P1](phases/01-math-linux-git/README.md)
- **Perception core:** [P2](phases/02-core-ml/README.md)–[P3](phases/03-computer-vision-deep-learning/README.md)
- **Systems and distributed:** [P4](phases/04-rust-systems/README.md)–[P5](phases/05-robotics-embedded/README.md) — networking, async services, telemetry, and embedded control: the distributed substrate that carries data between autonomous platforms.
- **Edge and robotics middleware:** [P6](phases/06-edge-ai-deployment/README.md)–[P8](phases/08-ros2-sensor-fusion/README.md) — on-device inference and ROS 2, the autonomy middleware that wires perception, navigation, and telemetry into one running graph.
- **Autonomy and HMT:** [P9](phases/09-multi-agent-swarm/README.md)–[P10](phases/10-gaze-hmt/README.md) — multi-agent coordination, mission planning, and human-machine teaming: deciding and acting, not just perceiving.
- **Doctrine and capstone:** [P11](phases/11-doctrine-ethics/README.md)–[P12](phases/12-research-capstone/README.md)
- **Specialization:** [Agent Engineering Sprint](modules/agent-engineering-sprint/README.md) — tool use, planning, memory, and orchestration for mission-execution agents.

## Cross-phase build chains

- Python sensor-data analysis → Rust sensor-data CLI.
- Model training → edge deployment → Rust ONNX inference service.
- Python multi-agent simulation → deterministic Rust simulation backend.
- Transformer perception experiment → research capstone.
- Gaze-directed control prototype → meaningful-human-control essay.
- Agent sprint → bounded ISR-triage workflows during the later overlay.
- Rust telemetry service → ROS 2 telemetry bridge → distributed mesh telemetry across multiple platforms.
- Nav2 behavior trees → task allocation across agents → a mission-planning console with a human in the loop.

These chains exist because the target role rewards integration over specialization (operating rule 7): a perception model that never leaves a notebook is worth less than a smaller model wired through ROS 2, telemetry, and a mission decision.

## Promotion rule

A phase becomes active only after its prerequisites are demonstrated and a concrete output has been selected. Parallel exposure does not change phase status. Every phase README records the minimum proof required to move on.
