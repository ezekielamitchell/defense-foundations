//! hello-stats — count lines, words, and bytes from a file or from stdin.
//!
//! Rust half of Project 0 (paired with the Python `file_stats.py`). Phase 0
//! foundations: `Result`-based error handling, no `unwrap()` on user input or
//! file I/O, clean exit on bad paths.
//!
//! Usage:
//!   hello-stats <path>     # read a file
//!   hello-stats            # read stdin
//!   cat file | hello-stats # read stdin via pipe

use std::env;
use std::error::Error;
use std::fs::File;
use std::io::{self, Read};
use std::process;

/// Line / word / byte counts for a single input.
struct Stats {
    lines: usize,
    words: usize,
    bytes: usize,
}

/// Count lines, words, and bytes from any reader. Propagates I/O errors instead
/// of panicking, so the caller can report them cleanly.
fn count<R: Read>(mut reader: R) -> io::Result<Stats> {
    let mut data = Vec::new();
    reader.read_to_end(&mut data)?;
    Ok(count_bytes(&data))
}

/// Count raw bytes, while treating undecodable UTF-8 bytes as replacement
/// characters for line/word counting. This matches the Python implementation's
/// `errors="replace"` behavior.
fn count_bytes(data: &[u8]) -> Stats {
    let text = String::from_utf8_lossy(data);
    Stats {
        lines: text.lines().count(),
        words: text.split_whitespace().count(),
        bytes: data.len(),
    }
}

/// Real work. Returns `Err` on bad args or unreadable input; `main` turns that
/// into a clean stderr message and a non-zero exit code.
fn run() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = env::args().collect();

    let (stats, source) = if args.len() > 1 {
        let path = &args[1];
        let file =
            File::open(path).map_err(|e| format!("hello-stats: cannot open '{path}': {e}"))?;
        (count(file)?, path.clone())
    } else {
        let stdin = io::stdin();
        (count(stdin.lock())?, String::from("<stdin>"))
    };

    println!("{:>8} {:>8} {:>8}  {}", "lines", "words", "bytes", "source");
    println!(
        "{:>8} {:>8} {:>8}  {}",
        stats.lines, stats.words, stats.bytes, source
    );
    Ok(())
}

fn main() {
    if let Err(e) = run() {
        eprintln!("{e}");
        process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Cursor;

    #[test]
    fn counts_lines_words_bytes() {
        let input = b"hello world\nsecond line\n";
        let s =
            count(Cursor::new(&input[..])).expect("counting an in-memory buffer should not fail");
        assert_eq!(s.lines, 2);
        assert_eq!(s.words, 4);
        assert_eq!(s.bytes, 24);
    }

    #[test]
    fn empty_input_is_all_zero() {
        let s = count(Cursor::new(&b""[..])).expect("counting empty input should not fail");
        assert_eq!((s.lines, s.words, s.bytes), (0, 0, 0));
    }

    #[test]
    fn invalid_utf8_is_replaced_for_text_counts() {
        let input = [0xff, b' ', b'a', b'\n'];
        let s = count(Cursor::new(&input[..]))
            .expect("invalid utf-8 should not break raw byte counting");
        assert_eq!((s.lines, s.words, s.bytes), (1, 2, 4));
    }
}
