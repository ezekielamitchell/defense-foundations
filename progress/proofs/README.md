# Phase 0 proof receipts

Store observed Foundation receipts here as `YYYY-MM-DD.json` only after the cited commands have actually run. Each file must conform to [`phase0-proof.v1`](../../docs/phase0-proof.schema.json) and pass:

```sh
python3 tools/validate_phase0_integrity.py --proof progress/proofs/YYYY-MM-DD.json
```

A receipt is a compact pointer to observed repository evidence, not a replacement for code, tests, output, or the private Aegis evidence ledger. Calendar reservations, Todoist state, generated documentation, elapsed time, paper reading, agent exercises, and endr activity cannot populate a verified Foundation receipt.

Do not create a receipt merely to fill a date. If no qualifying proof exists, close the day in Aegis with the blocker and exact next command; leave this directory unchanged.
