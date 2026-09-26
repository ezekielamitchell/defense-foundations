# First learning week — Python, Rust and agent basics

Use one full relative week to start all three foundations in parallel. The
starting point is self-reported very beginner Python knowledge; a short
diagnostic determines what to skip. An earlier course, code file or scheduled
block does not establish current recall. The private Aegis schedule owns exact
dates, order within each day and capacity.

**Python primary:** [Python Crash Course, 3rd Edition on O’Reilly](https://www.oreilly.com/library/view/python-crash-course/9781098156664/), selected Part I concepts and exercises.
**Rust primary:** [Nathan Stocks — Ultimate Rust Crash Course](https://www.udemy.com/course/ultimate-rust-crash-course/), selected lessons and compiler practice; use the [Rust Book](https://doc.rust-lang.org/book/) for current-language explanations.
**Agent primary:** [Vanderbilt — AI Agents and Agentic AI with Python & Generative AI](https://www.coursera.org/learn/ai-agents-python), selected introductory concepts. Trace toy systems on paper before API or framework demonstrations.
There is no mandatory Angela Yu Day 1 or linear 100 Days of Code assignment.
Access is unverified; use the official references below if a paid source is unavailable.

| Order | Python lesson and check | Rust lesson and check | Agent lesson and check |
|---|---|---|---|
| 1 · Locate and explain | In at most 25 minutes, predict and write a tiny function using a list or dictionary. Explain changed and empty input; return to PCC Chapters 3–8 only for a failed concept. | Use Cargo to run a tiny function with variables and types. Predict changed output and explain one compiler message. | Draw **goal → observation → allowed action → new observation → stop** for a synthetic file-organizing helper; name who authorizes the action. |
| 2 · Handle ordinary failure | Read one short UTF-8 file with a function and handle a missing path deliberately. Explain input, output and error. | Use a reference/borrow in a tiny function, then read a short file using `Result`; explain and repair one compiler or file error. | Manually trace two steps with a small allowed-action list. At each step record input, selected action, result and a stop condition; no API call is needed. |
| 3 · Check and resume | Write a meaningful test for a pure count function; make it fail with changed input, repair it and verify at least one test was collected. | Test a pure function and one ordinary error path. Explain the ownership or `Result` choice without copying. | Test the paper trace with an unavailable action and a maximum-step limit. Show that the helper stops and asks for human review rather than inventing a new action. |

These are three **lesson steps per track**, not nine mandatory daily blocks. Use
the next step when that track's existing 2–3-hour studio occurs; a one-hour
supporting reading stays inside its existing reservation. The first full week
also includes a short cross-track review: state one demonstrated skill, one
uncertain concept and the next small action for each track. Python and Rust
can occupy different days. The agent trace is introductory study and earns no
Foundation implementation credit.

Do not call an empty test command proof: the inspected Python starter has no
collected tests, and the Rust starter's passing `cargo test` currently runs
zero tests. Preserve those historical files; learner-written behavior and
meaningful tests are the next checks. A short provider lesson can explain a
gap, but videos and certificates do not satisfy any check above.

## After the introduction

Python and Rust studios focus on the smallest unproved Project 0 behavior:
empty and ordinary input, counts and Unicode, file/stdin handling, deliberate
errors and exit status, then CLI output and reproduction. Use a short matching
lesson when a real gap blocks the next behavior. Do not restart a whole intro
course after a missed session.

Keep the existing code and dirty work. Build and explain each language
independently before comparing identical fixtures. A date on the calendar is
permission to attempt the next slice, not evidence that prerequisites passed.
If a skill is still missing after the first week, make it a targeted practice
item inside the next studio. Do not add catch-up hours or promote a phase.

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
- **Agent loop and limits:** use the Vanderbilt introduction for vocabulary and a paper trace. Frameworks, paid APIs and real-world actions wait until Python basics and explicit action boundaries are demonstrated.

Classes and advanced abstractions are introduced only when the current example
needs them. Battlefield-AI context, warfare/law, paper reading and endr remain
separate lanes; they do not replace language proof or agent safety checks.
