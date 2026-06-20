# Rust in 9 Months — Systems & CLI Track

**For:** A Python programmer learning Rust from scratch **Time budget:** 2 hours/day, ~6 days/week (~10–12 hrs/week) **End goal:** Confident building command-line tools and systems-level programs in Rust **Target version:** Rust 1.85+ with `edition = "2024"` (the 2024 edition is the current default as of 2025)

---

## How to use this plan

Each day, split your 2 hours roughly **60% reading/watching, 40% writing code**. Reading without typing does not work for Rust — the compiler is your teacher, and you learn the borrow checker by fighting it. Two rules:

1. **Type out every example yourself.** Don't copy-paste. The friction is the point.
2. **Keep a `rust-journal/` folder.** One short note per day: what confused you, what clicked. The borrow checker concepts that baffle you in month 1 will feel obvious by month 4, and the journal proves it.

A quick note for your Python brain: Rust will feel slow and pedantic at first. Things Python does invisibly (memory, ownership, error handling) are explicit here. That explicitness _is_ the feature — lean into it instead of fighting it.

---

## Setup (Day 1, before anything else)

Install the toolchain and editor support so you never battle tooling later.

- Install via **rustup**: [https://rustup.rs](https://rustup.rs/) — gives you `rustc`, `cargo`, `rustup`
- Editor: **VS Code + rust-analyzer** extension, or any editor with rust-analyzer LSP — [https://rust-analyzer.github.io](https://rust-analyzer.github.io/)
- Learn the daily commands: `cargo new`, `cargo run`, `cargo build`, `cargo test`, `cargo clippy`, `cargo fmt`
- Bookmark: **The Rust Playground** for quick experiments — [https://play.rust-lang.org](https://play.rust-lang.org/)

---

## Phase 1 — Foundations (Months 1–3)

Goal: read and write idiomatic Rust, internalize ownership/borrowing, stop fighting the compiler.

### Month 1 — The language core

Work through **The Rust Book** chapters 1–10 slowly. This is the single most important resource in the whole plan; do not rush it.

- **The Rust Programming Language ("the Book")** — [https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/)
- **Brown University interactive edition** (same book + quizzes + ownership visualizations — better for self-study) — [https://rust-book.cs.brown.edu](https://rust-book.cs.brown.edu/)
- **Rustlings** (small compiler-driven exercises that track the Book) — [https://github.com/rust-lang/rustlings](https://github.com/rust-lang/rustlings)
- **Rust by Example** (runnable companion snippets) — [https://doc.rust-lang.org/rust-by-example/](https://doc.rust-lang.org/rust-by-example/)

Coverage: variables/mutability, data types, functions, control flow, **ownership & borrowing** (ch. 4 — spend extra days here), structs, enums, pattern matching, modules/packages, common collections (`Vec`, `String`, `HashMap`), generics, traits, lifetimes intro.

**Month 1 mini-project:** A CLI temperature converter or a number-guessing game (the Book's ch. 2 project). Small, but compile-clean and committed to git.

### Month 2 — Error handling, traits, generics in depth

Book chapters 9–13 plus daily Rustlings.

- Continue **The Rust Book** (error handling with `Result`/`?`, generic types, traits, lifetimes, closures, iterators)
- **Rust by Example** sections on error handling and traits
- For the iterator/closure mindset (very different from Python loops): the iterators chapter, done as exercises

Coverage: `Result` vs `panic!`, the `?` operator, custom error types, trait bounds, `impl Trait`, iterators and closures (map/filter/collect — your Python comprehensions translate here), `Option` combinators.

**Month 2 mini-project:** A CLI word/line counter (a tiny `wc` clone) that reads a file, handles missing-file errors gracefully, and prints counts. Reading args + file I/O + error handling all at once.

### Month 3 — Standard library, testing, and the toolchain

Book chapters 11, 14–15 plus broaden into the ecosystem.

- **The Rust Book** — testing (ch. 11), Cargo & crates.io (ch. 14), smart pointers `Box`/`Rc`/`RefCell` (ch. 15)
- **The Cargo Book** (workspaces, dependencies, profiles) — [https://doc.rust-lang.org/cargo/](https://doc.rust-lang.org/cargo/)
- **Std library docs** — get comfortable reading these; you'll live here — [https://doc.rust-lang.org/std/](https://doc.rust-lang.org/std/)
- **Rust API Guidelines** (what idiomatic public APIs look like) — [https://rust-lang.github.io/api-guidelines/](https://rust-lang.github.io/api-guidelines/)

Coverage: unit & integration tests, `cargo test`, doc tests, smart pointers and interior mutability, when to reach for `Rc<RefCell<T>>`, organizing a multi-file project.

**Month 3 capstone:** A small but _complete_ CLI tool — e.g. a Markdown-to-HTML converter or a todo-list manager that persists to a JSON file. Requirements: argument parsing, file I/O, error handling, at least 5 tests, README, runs as an installed binary. This proves Phase 1 stuck.

---

## Phase 2 — Systems & CLI specialization (Months 4–6)

Goal: build real command-line tools the way professionals do, and understand the systems-level concepts (memory layout, unsafe, FFI) that make Rust a systems language.

### Month 4 — Production-grade CLI tooling

This is the heart of your chosen track. Learn the crates the whole ecosystem uses.

- **Command Line Applications in Rust** (free official-style guide) — [https://rust-cli.github.io/book/](https://rust-cli.github.io/book/)
- **clap** — argument parsing, the de facto standard — [https://docs.rs/clap/](https://docs.rs/clap/)
- **anyhow** (easy app error handling) + **thiserror** (library error types) — [https://docs.rs/anyhow/](https://docs.rs/anyhow/) / [https://docs.rs/thiserror/](https://docs.rs/thiserror/)
- **serde** + **serde_json** (serialization — your `json`/`dataclasses` replacement) — [https://serde.rs](https://serde.rs/)
- Supporting crates to meet: `indicatif` (progress bars), `colored`/`owo-colors` (terminal color), `assert_cmd` (CLI testing)

Coverage: subcommands, flags, config files, structured logging (`tracing` or `log` + `env_logger`), exit codes, testing a binary end to end.

**Month 4 project:** Rebuild a Unix tool well — a `grep` clone with flags (the Book's ch. 12 `minigrep`, then extend it with `clap`, color output, and recursive directory search). Compare your design to **ripgrep**'s source for inspiration — [https://github.com/BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep).

### Month 5 — Memory, unsafe, and how Rust actually works

Go under the hood. This is what separates "I can write Rust" from "I understand systems."

- **The Rustonomicon** (the dark arts: unsafe, raw pointers, memory layout) — read selectively, not cover to cover — [https://doc.rust-lang.org/nomicon/](https://doc.rust-lang.org/nomicon/)
- **Rust Atomics and Locks** by Mara Bos (free online; the best concurrency/memory book) — [https://marabos.nl/atomics/](https://marabos.nl/atomics/)
- **std::mem** and the memory chapters of the Nomicon for layout, alignment, `size_of`
- FFI basics: calling C from Rust and vice versa (Nomicon FFI chapter)

Coverage: stack vs heap revisited, what `unsafe` actually permits (and doesn't), raw pointers, `mem::swap`/`replace`, `Drop`, transmutes (and why to avoid them), C interop with `extern "C"` and `bindgen`.

**Month 5 project:** Write a small data structure that requires `unsafe` done correctly — e.g. a simple growable buffer or a singly-linked list. Pair this with **"Learn Rust With Entirely Too Many Linked Lists"** — [https://rust-unofficial.github.io/too-many-lists/](https://rust-unofficial.github.io/too-many-lists/) — the best hands-on unsafe tutorial in existence.

### Month 6 — Concurrency and parallelism

Rust's "fearless concurrency" — the payoff for all the ownership pain.

- **The Rust Book** ch. 16 (threads, channels, `Send`/`Sync`, `Arc`/`Mutex`)
- **Rust Atomics and Locks** (continue from month 5 — channels, mutexes, atomics in depth)
- **rayon** (data parallelism — turn a `.iter()` into `.par_iter()`) — [https://docs.rs/rayon/](https://docs.rs/rayon/)
- **crossbeam** (scoped threads, better channels) — [https://docs.rs/crossbeam/](https://docs.rs/crossbeam/)

Coverage: `thread::spawn`, message passing, shared state with `Arc<Mutex<T>>`, data races prevented at compile time, when to parallelize, `Send`/`Sync` marker traits.

**Month 6 capstone:** A parallel CLI tool — e.g. a multithreaded file hasher, a parallel directory-size analyzer (a `du`/`dust` clone), or a parallel log-line processor. Must use a thread pool or `rayon`, handle errors across threads, and show a measurable speedup over the single-threaded version.

---

## Phase 3 — Depth, async, and a real portfolio (Months 7–9)

Goal: async Rust, a substantial project, and the professional habits (profiling, benchmarking, publishing) that make you employable in Rust.

### Month 7 — Async Rust

Even for CLI/systems work, async matters (network tools, concurrent I/O). The 2024 edition and the Book's 3rd edition added dedicated async coverage.

- **The Rust Book** async chapter (ch. 17 in the current edition) — [https://doc.rust-lang.org/book/ch17-00-async-await.html](https://doc.rust-lang.org/book/ch17-00-async-await.html)
- **The Async Book** (deeper model: futures, executors, pinning) — [https://rust-lang.github.io/async-book/](https://rust-lang.github.io/async-book/)
- **Tokio tutorial** (the dominant async runtime) — [https://tokio.rs/tokio/tutorial](https://tokio.rs/tokio/tutorial)
- Crates to know: `tokio`, `reqwest` (HTTP client), `futures`

Coverage: `async`/`await`, futures and how they're polled, the executor model, `tokio` tasks, async I/O, `select!`, structured concurrency, when async is _not_ worth it (CPU-bound work — use threads/rayon instead).

**Month 7 project:** An async network CLI — e.g. a concurrent URL health-checker, a parallel downloader, or a small port scanner. Fetches many endpoints concurrently with `tokio` + `reqwest` and reports results.

### Month 8 — Performance, profiling, and robustness

Make your tools fast and bulletproof — the systems-engineer skillset.

- **The Rust Performance Book** — [https://nnethercote.github.io/perf-book/](https://nnethercote.github.io/perf-book/)
- **criterion** (statistical benchmarking) — [https://docs.rs/criterion/](https://docs.rs/criterion/)
- Profiling: `cargo flamegraph`, `perf`, `samply` — [https://github.com/flamegraph-rs/flamegraph](https://github.com/flamegraph-rs/flamegraph)
- Fuzzing & property testing: **proptest** ([https://docs.rs/proptest/](https://docs.rs/proptest/)) and `cargo-fuzz`
- **Clippy** lints in depth — treat every warning as a lesson — [https://doc.rust-lang.org/clippy/](https://doc.rust-lang.org/clippy/)

Coverage: measuring before optimizing, reading flamegraphs, avoiding needless allocations/clones, `&str` vs `String`, benchmark-driven optimization, property-based tests, handling edge cases and untrusted input.

**Month 8 work:** Take your month-6 or month-7 project and make it production quality — add benchmarks, profile and fix the top hotspot, add property tests, get it Clippy-clean, write real docs.

### Month 9 — Capstone, publishing, and ecosystem fluency

Tie it all together into something you'd put on a résumé or GitHub.

- **crates.io publishing guide** (Cargo Book ch. on publishing) — [https://doc.rust-lang.org/cargo/reference/publishing.html](https://doc.rust-lang.org/cargo/reference/publishing.html)
- **This Week in Rust** (stay current with the ecosystem) — [https://this-week-in-rust.org](https://this-week-in-rust.org/)
- Read real source code: **ripgrep**, **bat**, **fd**, **eza** — top-tier Rust CLI tools to learn idioms from — [https://github.com/sharkdp/bat](https://github.com/sharkdp/bat), [https://github.com/sharkdp/fd](https://github.com/sharkdp/fd)
- **GitHub Actions for Rust** — set up CI (build, test, clippy, fmt) on your repo

**Month 9 capstone project (pick one, go deep):**

- A genuinely useful CLI tool you'd use yourself (a better `find`, a project scaffolder, a log analyzer, a config linter)
- A small interpreter or parser (try **"Crafting Interpreters"** ported to Rust, or the **`nom`** parser-combinator crate)
- A systems utility (a tiny key-value store, a file-sync tool, a process monitor)

**Requirements for the capstone:** clap-based CLI, robust error handling, tests + at least one benchmark, CI pipeline, polished README with examples, published to crates.io or released as a binary on GitHub. This is your proof of competence.

---

## Recurring practice (do these _throughout_, not as separate blocks)

- **Rustlings** in months 1–3, then switch to **Exercism's Rust track** (mentored, idiomatic feedback) — [https://exercism.org/tracks/rust](https://exercism.org/tracks/rust)
- **Advent of Code** past puzzles (great for daily 30–60 min drills, any month) — [https://adventofcode.com](https://adventofcode.com/)
- **Read one piece of real Rust source per week** from month 4 onward — idioms transfer by osmosis
- Run `cargo clippy` on everything and read every lint — it's free senior-engineer mentorship

---

## Milestone checklist

- [ ] **End of Month 3:** Ownership/borrowing feel natural; you can build a tested multi-file CLI without panicking on errors.
- [ ] **End of Month 6:** You build production-style CLI tools with `clap`/`serde`, understand `unsafe`, and can write correct multithreaded code.
- [ ] **End of Month 9:** You've shipped a polished, benchmarked, CI-backed project publicly — and you can read most Rust code in the wild.

---

## A few honest expectations

- **Months 1–2 are the hardest.** The borrow checker will reject code that "obviously works." This is universal. Push through; it clicks around week 6–8.
- **Don't skip the projects.** Reading the Book twice teaches you less than building one messy CLI tool.
- **Your Python instincts will mislead you sometimes** — Rust prefers iterators over index loops, `Result` over exceptions, and explicit types over duck typing. Unlearn deliberately.
- **It's fine to fall behind the schedule.** The phases matter more than the exact month boundaries. Adjust pace, keep the order.

---

### Key resources at a glance

| Area                 | Primary resource                                                                   |
| -------------------- | ---------------------------------------------------------------------------------- |
| Core language        | The Rust Book — [https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/) |
| Interactive practice | Rustlings, Exercism, Brown interactive Book                                        |
| CLI development      | Command Line Apps in Rust + `clap`, `serde`, `anyhow`                              |
| Unsafe / internals   | The Rustonomicon + Too Many Linked Lists                                           |
| Concurrency          | Rust Atomics and Locks + `rayon`, `tokio`                                          |
| Async                | The Async Book + Tokio tutorial                                                    |
| Performance          | The Rust Performance Book + `criterion`                                            |
| Staying current      | This Week in Rust                                                                  |