#!/usr/bin/env python3
"""file_stats — count lines, words, and bytes from a file or from stdin.

Python half of Project 0 (paired with the Rust ``hello-stats``). Phase 0
foundations: ``argparse``, ``pathlib``, file I/O, and clean error handling
(a missing file exits non-zero with a useful message instead of a traceback).

Usage:
    python file_stats.py <path>      # read a file
    python file_stats.py             # read stdin
    cat file | python file_stats.py  # read stdin via pipe
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def count_bytes(data: bytes) -> tuple[int, int, int]:
    """Return (lines, words, bytes) for a raw byte buffer.

    Bytes are counted raw; lines and words are counted on a UTF-8 decode
    (undecodable bytes are replaced so counting never crashes).
    """
    text = data.decode("utf-8", errors="replace")
    lines = len(text.splitlines())
    words = len(text.split())
    return lines, words, len(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="file_stats",
        description="Count lines, words, and bytes in a file or from stdin.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="file to read; if omitted, read from stdin",
    )
    args = parser.parse_args(argv)

    if args.path is not None:
        path = Path(args.path)
        try:
            data = path.read_bytes()
        except FileNotFoundError:
            print(
                f"file_stats: cannot open '{args.path}': No such file or directory",
                file=sys.stderr,
            )
            return 1
        except OSError as exc:
            reason = exc.strerror or str(exc)
            print(f"file_stats: cannot open '{args.path}': {reason}", file=sys.stderr)
            return 1
        source = args.path
    else:
        data = sys.stdin.buffer.read()
        source = "<stdin>"

    lines, words, nbytes = count_bytes(data)
    print(f"{'lines':>8} {'words':>8} {'bytes':>8}  source")
    print(f"{lines:>8} {words:>8} {nbytes:>8}  {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
