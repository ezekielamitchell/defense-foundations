# Python CLI Tooling

> **Curriculum v2 routing (2026-09-19):** This is a retained resource/exercise record. Use [Resource Spine](../../../curriculum/RESOURCE_SPINE.md) for current prepared teaching order and [Start Here](../../../curriculum/START_HERE.md) for the complete-beginner entry. Older course quotas, month bands and prior source priority below are reference history; existing sealed schedule rules persist only until the separate reset. Preserve historical exercise/completion facts.


**Sources:** [Python 3.11 argparse](https://docs.python.org/3.11/library/argparse.html), [Python 3.11 pathlib](https://docs.python.org/3.11/library/pathlib.html), [pytest](https://docs.pytest.org/en/stable/getting-started.html), [uv](https://docs.astral.sh/uv/guides/projects/), and [Ruff](https://docs.astral.sh/ruff/tutorial/)

**Activation:** pulled on demand to unblock a named `P0-W*` Python issue; see [docs/ISSUES.md](../../../docs/ISSUES.md)

## Focus

Argument parsing, path-safe file access, useful exit behavior, environment/dependency setup, and basic tests. Keep the interface small and predictable.

Match Python examples to the project's Python 3.11 compatibility and use the project lockfile. Ruff's version is declared in the project dev group; availability or a clean lint result is not runnable-test proof. Use [pytest exit-code semantics](https://docs.pytest.org/en/stable/reference/exit-codes.html): zero collected tests never earns a green Foundation verdict. No blanket environment upgrade or automatic lint fix is part of source maintenance.

## Evidence

`projects/file_stats` — the Python half of the paired file-statistics CLI — with help text, invalid-path handling, example output, a `tests/` suite, and a reproducible run command. (`csv_summary` belonged to a superseded plan and is not the current target.)
