# P2 — Quantitative Reasoning and Trustworthy Evaluation

**Curriculum v2 · prepared 2026-09-19**
**Status:** not started
**Route:** main route · **Prerequisites:** P1

No new dates or phase promotion follow from this preparation. Numeric IDs are
stable references; use prerequisites rather than completing every ID in order.

## Entry

P1 reproducible input/output harness. Check algebra, functions, units and simple plots; remediate before adding statistics.

## Learn

Mean/variance, sampling, conditional probability, train/validation/test separation, leakage, imbalance, precision/recall, thresholds, calibration, uncertainty and resource-aware comparison. Learn enough arrays and plotting to inspect results.

## Build

Finish Flagship I's evaluation contract using a small synthetic alert stream and a trivial rule baseline, then one simple classifier if appropriate. Preserve split/config provenance. Relate false alarms, missed events and latency to an explicit toy cost.

## Acceptance evidence

Hand-check a confusion matrix; keep held-out data untouched; compare the rule and candidate on identical inputs; report failure slices and uncertainty without claiming statistical confidence from an arbitrary seed count.

## Source and scope

scikit-learn's introductory and evaluation guides; targeted math lessons for any failed prerequisite. Degree ML material may inform understanding with ownership kept separate.

**Defer:** No model zoo, deep networks, threat-classification claim, expensive dataset collection or exhaustive math curriculum.

## Next

P4 on the main route. P3 is optional perception depth after this gate.

See [the route](../../COMPETENCY_PATHWAY.md), [beginner guide](../../START_HERE.md),
[resource spine](../../RESOURCE_SPINE.md), and [reset handoff](../../RESET_HANDOFF.md).
