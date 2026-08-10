# Python CLI Tooling

**Sources:** [argparse](https://docs.python.org/3/library/argparse.html), [pathlib](https://docs.python.org/3/library/pathlib.html), [pytest](https://docs.pytest.org/), and [uv](https://docs.astral.sh/uv/)  
**Activation:** pulled on demand to unblock a named `P0-W*` Python issue; see [docs/ISSUES.md](../../../docs/ISSUES.md)

## Focus

Argument parsing, path-safe file access, useful exit behavior, environment/dependency setup, and basic tests. Keep the interface small and predictable.

## Evidence

`projects/file_stats` — the Python half of the paired file-statistics CLI — with help text, invalid-path handling, example output, a `tests/` suite, and a reproducible run command. (`csv_summary` belonged to a superseded plan and is not the current target.)
