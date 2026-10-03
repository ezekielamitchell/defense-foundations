# Evidence — Python Crash Course

> **Curriculum v2 routing (2026-09-19):** This is a retained resource/exercise record. Use [Resource Spine](../../../../curriculum/RESOURCE_SPINE.md) for current prepared teaching order and [Start Here](../../../../curriculum/START_HERE.md) for the complete-beginner entry. Older course quotas, month bands and prior source priority below are reference history; existing sealed schedule rules persist only until the separate reset. Preserve historical exercise/completion facts.


The completion bar for this material (from the [chapter README](../README.md)):

> Turn the concepts into a file-processing script. Do not treat chapter
> exercises alone as completion; the output must read a path, handle malformed
> input, and produce useful results.

## Layout

- `process_log.py` — the script (starter stub). Reads a file path, parses each
  line, reports malformed lines, and prints a useful summary. Standard library
  only — everything here is reachable with Chapters 1–8 plus reading a file.
- `data/sample_log.txt` — a small sample with malformed lines to exercise the
  error handling.

## Run

    python3 evidence/process_log.py evidence/data/sample_log.txt

Make it your own: change the input format, the summary, or the failure
handling. The bar is reading a path, surviving bad input, and producing a
result worth reading — not this exact script.
