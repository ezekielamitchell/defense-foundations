"""Evidence — file-processing script for Python Crash Course (Part I).

Reads a log file, summarizes it by level, and reports malformed lines.
Standard library only; built from Chapters 1-8 concepts plus reading a file.

Usage:
    python3 process_log.py <path-to-log-file>

Completion bar (see ../README.md): read a path, handle malformed input,
produce useful results.
"""

import sys

KNOWN_LEVELS = ("INFO", "WARN", "ERROR")


def parse_line(line):
    """Return (level, message) for a valid line, or None if malformed."""
    line = line.strip()
    if not line or ":" not in line:
        return None
    level, message = line.split(":", 1)
    level = level.strip().upper()
    if level not in KNOWN_LEVELS:
        return None
    return level, message.strip()


def summarize(path):
    """Read the file at `path` and return (counts_by_level, malformed_lines)."""
    counts = {level: 0 for level in KNOWN_LEVELS}
    malformed = []
    with open(path, encoding="utf-8") as log_file:
        for lineno, raw_line in enumerate(log_file, start=1):
            parsed = parse_line(raw_line)
            if parsed is None:
                if raw_line.strip():  # ignore blank lines, report real garbage
                    malformed.append((lineno, raw_line.strip()))
                continue
            level, _message = parsed
            counts[level] += 1
    return counts, malformed


def main():
    if len(sys.argv) != 2:
        print("usage: python3 process_log.py <path-to-log-file>", file=sys.stderr)
        return 1

    path = sys.argv[1]
    try:
        counts, malformed = summarize(path)
    except FileNotFoundError:
        print(f"error: no such file: {path}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: could not read {path}: {exc}", file=sys.stderr)
        return 1

    total = sum(counts.values())
    print(f"{path}: {total} valid log line(s)")
    for level in KNOWN_LEVELS:
        print(f"  {level:<5} {counts[level]}")
    if malformed:
        print(f"  {len(malformed)} malformed line(s):")
        for lineno, text in malformed:
            print(f"    line {lineno}: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
