# P4 — Rust Systems

**Status:** not started  
**Estimated duration:** 8–10 weeks at 10–15 hours/week

## Focus

Move from Rust that compiles to services suitable for a fielded system. This is the distributed-systems layer of the autonomy stack: the networking, async services, and telemetry that move sensor data, health, and commands reliably between autonomous platforms. A perception model is only useful once its outputs survive an unreliable network and reach a mission decision—that path is built here, and it is what later turns single robots into sensor networks and coordinated fleets.

## Topics

Lifetimes, traits, async Tokio, channels, synchronization, TCP/UDP/HTTP, Serde, tracing, configuration, graceful shutdown, profiling, benchmarking, Axum/Actix, PyO3, and Maturin.

## Materials

See [Rust systems](../../../learning-materials/04-rust-systems/README.md).

## Evidence target

A dataset-validation or telemetry service with tests, structured logs, CI, graceful shutdown, and benchmarks.

## Exit gate

Design a Rust service without a template and ship an installable binary with a real README and CI.
