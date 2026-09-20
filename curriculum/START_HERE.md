# Start Here — Programming Foundations

**Active September 19, 2026 · parallel beginner curriculum**

Start with the [seven-day Python/Rust sprint](FOUNDATIONS_FAST_TRACK.md).
You reported very beginner Python knowledge: use a short diagnostic to skip
what you can independently explain and change. Existing code and historical
records remain reference material; they are not automatically current proof.

This is your learning guide. [The route](COMPETENCY_PATHWAY.md) explains later
work. [The current course map](PARALLEL_COURSE_MAP.md) defines the parallel tracks.
The private Aegis authority owns the active schedule. Do not use calendar dates
to skip an unmastered concept.

## Setup check, only if needed

Open your terminal, go to the existing repository, and inspect its state:

```sh
cd /path/to/defense-foundations
pwd
git status --short
python3 --version
python3 projects/file_stats/main.py
```

The inspected starter prints `Hello from file-stats!`. This only demonstrates
that a script runs. Identify which file ran, what `print` does, and the
difference between the terminal and the Python file. Then type a tiny change,
predict its output, run it, and explain the result. Ask for a hint if you cannot
identify the line to change. Do not restore, erase, or rewrite unrelated files.

No new package, hardware, cloud account, agent framework, or paper is needed for
this first result. If Python cannot run, resolve that setup problem before
adding another tool. macOS is fine for initial lessons; actual Linux execution
is a later foundation check, not an installation obstacle on the first session.

## One primary source per track

Use the [parallel course map](PARALLEL_COURSE_MAP.md): selected O’Reilly PCC
concepts/exercises for Python, Udemy for Rust and Coursera for agents/AI/warfare.
The introductory sweep fits the seven-day sprint; subsequent studios apply
concepts to Project 0 and refresh specific gaps. PCC chapter references below
are a concept crosswalk, not a requirement to read the whole book. Official
documentation supplies a fallback when paid access is unavailable. No purchase
or certificate is required, and there is no Angela Yu Day 1 restart.

Rust starts in parallel with a guided bridge for programming vocabulary. Its
course and the Rust Book assume general programming concepts, so pause for an
explanation and a tiny exercise whenever an example assumes unfamiliar knowledge.

## Beginner checkpoints

These are learning checkpoints, not dates or session quotas. Repeat or split
any row. Early exercises stay in your own exercise area under the existing
learning-materials tree; one small exercise is not another portfolio project.

| Checkpoint | Learn | Do without copying the example | Ready to continue when |
|---|---|---|---|
| Z0 · Run and inspect | Editor, terminal, paths, save/run; PCC Chapter 1 | Change and run one small script | You can find the file and explain the observed output |
| Z1 · Values | PCC Chapter 2: variables, strings, numbers | Format a short summary from three values | You can predict a changed input and fix a simple error |
| Z2 · Collections and decisions | PCC Chapters 3–7: lists, loops, conditions, dictionaries, input | Count words in a literal string; summarize a small list | Empty and repeated values do not surprise you |
| Z3 · Functions | PCC Chapter 8 | Write a count function that returns a result rather than printing inside it | You can call it with two inputs and explain arguments vs return values |
| Z4 · Files and failures | PCC Chapter 10; `pathlib` as needed | Read a tiny file; handle a missing file deliberately | You can explain bytes vs decoded text and the failure path |
| Z5 · First tests | PCC Chapter 11; pytest getting started | Write a passing test, deliberately break the function, see failure, repair it | You can explain what the test actually proves |
| Z6 · Useful Python CLI | argparse docs; pytest temporary-file reference | Build the Project 0 file/stdin interface incrementally | The named success/error fixtures pass; README commands work |
| Z7 · Rust introduction | Rust Book Chapters 1–3, then 4–6, 8–9 and 11 as needed | Rebuild small familiar Python ideas in Rust; learn ownership and Result | You can explain a borrow error and return an ordinary error without panic |
| Z8 · Paired CLI | Rust Book Chapter 12; Command-Line Rust selected examples | Implement the same agreed contract in hello-stats | Both languages agree on counts, streams and exit status |
| Z9 · Reproduce and explain | Git, shell, packaging, CI | Recreate a small slice without the tutorial; run in a clean environment | Every P0 gate has observed evidence or a named gap |

PCC Chapter 9 (classes) is available when a concrete example needs it; no OOP
architecture is required for this CLI. Its game, visualization and web projects
are optional alternatives, not extra requirements.

Z0–Z6 describe Python competencies. Z7 describes the independent Rust skill set,
which may start alongside Z0; the number is an identifier, not a waiting period.
Z8 parity requires basic file handling in both languages. Preserve historical
Rustlings files and recheck recall instead of assuming the saved pointer is proof.

## How to study a small slice

1. Recall: explain yesterday's concept or predict a tiny example.
2. Learn: read one short section or watch the matching explanation.
3. Practice: type it, change an input, then solve one similar task yourself.
4. Check: run it, inspect output, and test one edge case when tests are familiar.
5. Close: record the source stop point, what ran, and one next action.

Current course and project studios last 2–3 hours, including short breaks.
Curriculum reading blocks last one hour. Alternate explanations and practice;
there is no inherited instruction-percentage cap. End with one small independently
explained result, not a promise to finish a whole lesson or chapter.

When stuck, reduce the example, read the last error, and try one hypothesis.
After roughly 15–20 unproductive minutes, request a hint or worked explanation.
Do a similar problem independently afterward. AI may explain, quiz, review, and
suggest a small test; a generated full solution does not prove your understanding.

## Project 0 contract, introduced gradually

Agree on this contract before comparing languages:

- Input: one file path or `-` for stdin; no recursive scanning.
- Decode UTF-8 strictly; invalid bytes produce a clean error.
- Bytes: raw byte length. Lines: number of LF bytes (a trailing fragment adds
  no line). Words: runs separated by ASCII whitespace (space, tab, LF, CR,
  vertical tab, form feed). Non-ASCII whitespace stays inside a word.
- Success: one line `lines=<n> words=<n> bytes=<n>\n` on stdout; exit 0.
- Usage error: exit 2. Read/decode failure: exit 1, diagnostic on stderr and
  no count result on stdout. Exact OS error wording need not match.
- Streaming and clever optimizations wait until a measured need; state the
  small-file memory limit honestly.

| Fixture | Lines | Words | Bytes |
|---|---:|---:|---:|
| empty | 0 | 0 | 0 |
| `alpha beta\n` | 1 | 2 | 11 |
| `alpha` without final LF | 0 | 1 | 5 |
| `a\r\nb\n` | 2 | 2 | 5 |
| UTF-8 `café\n` | 1 | 1 | 6 |
| ` \t\n` | 1 | 0 | 3 |

Also test invalid UTF-8, nonexistent path, directory input, missing/extra
arguments, file-versus-stdin parity, and non-ASCII whitespace. These are proposed
acceptance fixtures, not tests that already exist. This educational contract
uses explicit whitespace rules rather than claiming complete GNU wc equivalence.

## P0 exit gate

- Independently implement and explain both CLIs; all selected fixtures pass.
- Python: meaningful pytest collection, type-aware code, Ruff, usable README.
- Rust: meaningful tests, Clippy and formatting checks, usable README.
- Compare both programs on identical inputs; explain each mismatch or resolve it.
- Demonstrate basic shell/Git work and a Linux cold run; macOS is not Linux proof.
- Show CI evidence when a workflow has actually run; local output is labeled local.
- Retain the current first-50 Rustlings requirement; a drill count alone does
  not prove ownership, error handling, or testing. Reverify rather than erase history.
- Rebuild a small unfamiliar variation without copying. An oral explanation
  and a failing-then-passing test matter more than memorizing syntax.

You may consult API docs during normal engineering. The independence check tests
understanding, not perfect recall. If a gate fails, repeat the specific skill.
The [progress record](../progress/README.md) records artifact, directory,
command, exit, output, changes, verdict, blocker and next command.

## Parallel study without assumed mastery

AI agents, battlefield AI and warfare foundations now have their own introductory
tracks. Use manual traces, public-source comparisons and small synthetic exercises.
Advanced perception, ROS 2, embedded hardware and RL remain later material. Keep
one primary source per track and one main Project 0 build. Research and agent work
do not satisfy the Python/Rust gate. See [the course map](PARALLEL_COURSE_MAP.md).
