# Python and Rust fundamentals sprint

Use a seven-day introduction, then learn through Project 0. The starting point is
self-reported very beginner Python knowledge. A short diagnostic determines what
to skip; it does not assume that previous course attendance proved a skill.
The private Aegis schedule owns the dates and exact reservations.

**Python primary:** [Python Crash Course, 3rd Edition on O’Reilly](https://learning.oreilly.com/library/view/python-crash-course/9781098156664/), selected Part I concepts and exercises.
**Rust primary:** [Nathan Stocks — Ultimate Rust Crash Course](https://www.udemy.com/course/ultimate-rust-crash-course/), selected lessons and compiler practice.
There is no mandatory Angela Yu Day 1 or linear 100 Days of Code assignment.
Access is unverified; use the official references below if a paid source is unavailable.

| Sprint day | Reserved programming focus | Independent check |
|---|---|---|
| 1 | Python diagnostic, functions and collections; Rust Cargo, types and functions | In at most 25 minutes, write a word-count function and a dictionary frequency count; explain empty input. In Rust, run a small function, predict its output and explain one compiler error. Skip only independently recalled basics. |
| 2 | Rust ownership, borrowing, collections and Result; Python files, imports and recoverable errors; Python reading | Explain and repair a borrow error. Read one UTF-8 file, return a result and handle a missing file. Read the Python section matching the current gap. |
| 3 | Consolidate inside an existing AI-agent exercise | Trace data through one small function and explain its inputs, output and stopping condition. No extra language block and no Foundation credit from agent work. |
| 4 | Python tests and basic CLI input | Observe a meaningful test pass, break it deliberately, observe failure and repair it. Run one basic CLI input case. |
| 5 | Rust file I/O and tests | Read a tiny file, handle a failure, test a pure function and explain borrowing/Result from recall. |
| 6 | Shared first-fixture lab | State expected counts for a tiny fixture and prove the next unproved behavior independently in each language. |
| 7 | Introduction review within the existing review reservation | List demonstrated skills and remaining gaps; choose the next Project 0 step. No extra programming reservation. |

The six language studios provide **14 hours** and the shared lab adds **2½ hours**.
The one-hour supporting reading uses its existing reservation. Instruction,
practice, breaks and the final log all fit inside each block. Day 3 uses the
already planned agent lesson; it adds no obligation.

## After the introduction

Python and Rust studios focus on the smallest unproved Project 0 behavior:
empty and ordinary input, counts and Unicode, file/stdin handling, deliberate
errors and exit status, then CLI output and reproduction. Use a short matching
lesson when a real gap blocks the next behavior. Do not restart a whole intro
course after a missed session.

Keep the existing code and dirty work. Build and explain each language
independently before comparing identical fixtures. A date on the calendar is
permission to attempt the next slice, not evidence that prerequisites passed.
If a skill is still missing after seven days, make it a targeted practice item
inside the next studio. Do not add catch-up hours or promote a phase.

For every code check, save the artifact, exact working directory, command,
exit code, observed output, changed paths, verdict, blocker and next command.
An assistant-written solution or a test run that collected no tests does not
prove the learner's understanding.

## References by gap

- **Python collections/functions:** PCC Chapters 3–8; [Python control flow and functions](https://docs.python.org/3/tutorial/controlflow.html).
- **Python files/errors:** PCC Chapter 10; [Python file I/O](https://docs.python.org/3/tutorial/inputoutput.html) and [exceptions](https://docs.python.org/3/tutorial/errors.html).
- **Python tests:** PCC Chapter 11; use the test tool already appropriate to the repository.
- **Rust basics/ownership:** [Rust Book](https://doc.rust-lang.org/book/), Chapters 1, 3 and 4.
- **Rust errors/files/tests:** Rust Book Chapters 9, 11 and selected sections of 12; do not assign the entire CLI chapter before its prerequisites.

Classes and advanced abstractions are introduced only when the current example
needs them. Concurrent agents, battlefield AI, warfare, paper reading and endr
continue in their separate lanes; they do not replace language proof.
