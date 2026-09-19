# P3 — Computer Vision and Deep Learning

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** optional depth · **Prerequisites:** P2

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P2 evaluation gate plus vectors/matrices, derivatives/gradients and array-shape literacy.

## Learn

Images/tensors, simple classical image baseline, datasets/loaders, one training loop, loss/optimizer, checkpointing, transfer learning, calibration and domain shift. Pick classification or detection, not every task.

## Build

An optional perception input for the shared harness/runtime. Use a small public licensed dataset, one classical baseline and one model. Prefer a CPU-feasible first experiment; document any justified GPU use.

## Acceptance evidence

Dataset/split provenance, reproducible evaluation, leakage checks, measured operating point, latency, one controlled ablation, confidence/failure slices and explicit unsupported claims.

## Source and scope

PyTorch Learn the Basics, OpenCV documentation and the selected model's primary paper/documentation.

**Defer:** Tracking, foundation-model fine-tuning, VLA and large training runs unless the specific experiment needs them. No compulsory YOLO version.

## Next

Feed the measured adapter into P4/P6 when useful. This module does not gate the core runtime.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
