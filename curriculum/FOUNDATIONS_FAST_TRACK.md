# Rust, Python and AI — compressed introduction

**Current teaching amendment: October 2, 2026. Finish the introductory sweep by Sunday, October 11.** “Next week” is interpreted as October 5–11, with the already reserved October 3 on-ramp. This supersedes earlier October 2–8 and full-source sequential pacing. It changes teaching scope, not the October 2 13:30 reset boundary, counters or phase gates.

The goal is working familiarity with essential concepts and small independent exercises. It is not every beginner topic, whole-book/course completion, or mastery by a date. Zero inherited learning credit remains; preserve historical work and log only newly observed results. Start with orientation, then selected essentials; omit repetitive exercises and defer nonessential projects. Do not restart after a missed studio.

## Learning sequence

Exact reservations and personal capacity stay in the private Aegis calendar. This public sequence preserves the selected topics without publishing personal times or task identities. Project work fits within the existing allocation.

| Order | Session |
|---|---|
| 1 | Rust sprint 1 — setup, values, functions and control flow |
| 2 | Python sprint 1 — values, collections and control flow |
| 3 | Rust sprint 2 — ownership, borrowing and strings |
| 4 | Rust sprint 3 — collections, structs, enums and Option |
| 5 | Python sprint 2 — functions, files, errors and first test |
| 6 | Rust sprint 4 — Result, file input and meaningful tests |
| 7 | AI sprint — goals, tools, state, feedback and stopping |
| 8 | AI sprint — ML, LLMs, data, evaluation and limitations |
| 9 | Rust sprint 5 — combine the basics in a tiny CLI |
| 10 | Python sprint 3 — independent Project 0 CLI and tests |
| 11 | Rust sprint 6 — independent CLI proof and parity attempt |
| 12 | Sunday checkpoint — close intro sprint, choose project gaps |

## Session instructions

### Rust sprint 1 — setup, values, functions and control flow

**Source:** Duke: orientation/setup and selected fundamentals; Rust Book Chapters 1 and 3 for gaps.

**Do:** Run a tiny Cargo program; change a variable, function argument, branch and loop. Predict output before running. Save one compiler error and its repair.

### Python sprint 1 — values, collections and control flow

**Source:** PCC introduction and selected Chapters 1–7.

**Do:** Run a script, then write a small loop over a list and dictionary with a conditional. Explain inputs, types and output. Use one exercise per concept; omit repetitive drills.

### Rust sprint 2 — ownership, borrowing and strings

**Source:** Duke selected ownership/borrowing lessons; Rust Book Chapter 4.

**Do:** Pass a string by reference, distinguish owned String from borrowed str, and repair a move/borrow error. Explain why the repair works.

### Rust sprint 3 — collections, structs, enums and Option

**Source:** Duke selected fundamentals and structs/types/enums lessons.

**Do:** Build a tiny in-memory record, iterate a vector, match an enum and handle a missing value with Option. Explain each using changed input.

### Python sprint 2 — functions, files, errors and first test

**Source:** PCC selected Chapter 8, basic imports, Chapter 10 and first testing example in Chapter 11; brief Chapter 9 vocabulary only.

**Do:** Write a function that reads a small UTF-8 file and returns one result. Handle a missing path. Write and run one meaningful test, make it fail deliberately, then repair it.

### Rust sprint 4 — Result, file input and meaningful tests

**Source:** Duke applying-Rust lessons; Rust Book Chapters 9, 11 and selected file-reading examples in 12.

**Do:** Read a tiny UTF-8 file, return Result, handle a missing path, and collect a meaningful test. Deliberately break the expected behavior and repair it.

### AI sprint — goals, tools, state, feedback and stopping

**Source:** Vanderbilt selected introductory concepts and tools/actions lessons. Later framework implementation is deferred.

**Do:** Use one synthetic toy: define goal, observation/state, allowed tool and input/output, feedback, and step limit. Trace one allowed result and one refused/failed tool call; stop correctly. Implement a local stub only if Python functions/dictionaries/errors are understood; otherwise complete the manual trace. No paid API needed.

### AI sprint — ML, LLMs, data, evaluation and limitations

**Source:** IBM Introduction to AI: selected introductory concepts, terminology and ethics lessons.

**Do:** Explain AI vs ML vs deep learning vs generative AI; training vs inference; data quality, hallucinations, evaluation and human review. Sketch how prompts, retrieval and tools differ. Choose a baseline, success measure and failure example for the same synthetic toy. This is conceptual introduction, not model-training proficiency.

### Rust sprint 5 — combine the basics in a tiny CLI

**Source:** Selected Duke application lessons and official Rust reference only for the current gap.

**Do:** Combine arguments, a pure counting function, file input, Result and tests in the existing Project 0 context. Explain stdout, stderr and exit status. Preserve the exact shared count contract; repair a specific gap without replaying the course.

### Python sprint 3 — independent Project 0 CLI and tests

**Source:** PCC selected Chapters 8, 10 and 11 as needed; existing Project 0 contract.

**Do:** Independently implement or explain the smallest Project 0 behavior. Exercise empty input, ordinary UTF-8 input and a missing path with meaningful tests. Show one deliberately failing assertion and its repair. Save precise gaps, not invented completion.

### Rust sprint 6 — independent CLI proof and parity attempt

**Source:** Duke and Rust Book only for a concrete implementation gap; existing Project 0 contract.

**Do:** Independently demonstrate a Rust function, ownership choice, file/error handling and meaningful test. Compare identical fixtures with Python only when both work independently. Use the same weekly pair_cycle_id; parity does not waive per-language proof.

## Sunday checkpoint and the following week

Use the existing October 11 review, 17:45–18:30. Review the evidence from the coding sessions rather than attempting three full builds in 45 minutes. For each item record **demonstrated**, **needs practice**, or **blocked**:

- Rust: explain values/functions/control flow; ownership and borrowing; an Option/Result choice; one file/error path; a meaningful collected test and repaired failure.
- Python: explain collections/loops/functions; imports; one file/error path; a meaningful collected test and repaired failure.
- AI: distinguish AI/ML/deep learning/generative AI, training/inference, prompting/retrieval/tools; explain data and evaluation limits; trace one allowed action, one failure/refusal and a finite stop rule.

The introduction closes Sunday even if some items need more practice. Carry each specific gap into the next project session; never mark an unproved skill complete. From October 12, language sessions start with Project 0 and agent sessions with the same bounded toy. Use a focused 20–30 minute explanation when blocked, apply it immediately, and log a precise next action. A harder prerequisite can use further practice within the studio; no automatic catch-up hours or source restart.

The later weekly topic cards are application prompts, not mandatory time spent on basics. Move to the next unmet criterion in P0 when a behavior is demonstrated. Higher-phase promotion still requires explicit evidence-backed authorization. The first-50 freshly observed Rustlings requirement remains inside Rust time; this sprint does not promise to finish it or all of Project 0.

Preserve the existing UTF-8, ASCII-whitespace, LF, byte-count, stdout/stderr and exit-status contract. Use the weekly pair_cycle_id; independent proof in each language precedes parity. Record artifact, exact working directory, command, exit code, observed output, changed paths, verdict, blocker and next command. Zero collected tests, copied solutions and watched videos do not establish independent implementation proof.

## Sources and boundaries

- [Duke Rust Fundamentals](https://www.coursera.org/learn/rust-fundamentals): primary Rust course; [Rust Book](https://doc.rust-lang.org/book/) is an implementation reference.
- [Python Crash Course, 3e on O’Reilly](https://www.oreilly.com/library/view/python-crash-course/9781098156664/): selected Part I concepts. Classes receive vocabulary-level coverage when needed; the book's game/web/data projects are deferred.
- [Vanderbilt AI Agents with Python](https://www.coursera.org/learn/ai-agents-python): selected concepts and tool-loop lessons. Framework implementation, paid APIs and real external actions are not beginner requirements. Use a manual trace or deterministic local stub; do not describe a stub as a trained model.
- [IBM Introduction to AI](https://www.coursera.org/learn/introduction-to-ai/): selected AI concepts, data/evaluation and limitations. No claim of model-training proficiency.

O’Reilly and Coursera remain the assigned providers. Enrollment and saved books are not completion. Warfare, ICRC and doctrine reading retain their separate current route. AI/domain study earns no Foundation credit. M.A.L. stays in its separate company lane and implementation language; synthetic virtual data-center work follows v0.2 acceptance. This teaching change authorizes no new product, deployment, paid service or phase promotion.
