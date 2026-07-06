"""Tests for file_stats.py (Python half of Project 0).

Covers basic counting and clean missing-file behavior. Run: ``pytest`` from the
repo root.
"""
import file_stats


def test_count_bytes_basic():
    lines, words, nbytes = file_stats.count_bytes(b"hello world\nsecond line\n")
    assert lines == 2
    assert words == 4
    assert nbytes == 24


def test_count_bytes_empty():
    assert file_stats.count_bytes(b"") == (0, 0, 0)


def test_missing_file_returns_1(capsys):
    rc = file_stats.main(["definitely_not_a_real_file_xyz.txt"])
    assert rc == 1
    err = capsys.readouterr().err
    assert "cannot open" in err
