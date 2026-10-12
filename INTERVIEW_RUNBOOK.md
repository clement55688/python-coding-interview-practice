# One-hour technical interview runbook

## 0-5 minutes: align

- Restate the input, output, invalid-input behavior, and mutation rules.
- Ask which requirements are essential and which are extensions.
- Walk through one normal example and one edge case.

Useful wording: "I'll start with a small correct interface, then add the extension without changing callers."

## 5-10 minutes: choose the model

- Name the core data structure and why it fits.
- State one simpler alternative and why you are not starting there.
- Write function signatures and one tiny test/example.

## 10-40 minutes: implement vertically

- Make one end-to-end path work.
- Keep parsing, state changes, and formatting separate.
- Use descriptive names and small helpers.
- Pause after meaningful steps to summarize what now works.

## 40-52 minutes: test and debug

- Run normal, empty, duplicate/tie, invalid, and boundary cases.
- When a test fails: state expected vs. actual, isolate the smallest failing input, then change one thing.

## 52-60 minutes: close strongly

- Give time and space complexity.
- Identify the most important invariant.
- Explain one design tradeoff and one next extension.
- If unfinished, describe the exact remaining steps and risks.

## Python reminders

- Prefer `dict`, `set`, `list`, `deque`, `heapq`, `defaultdict`, and `OrderedDict` when they express the model clearly.
- Avoid third-party packages; CoderPad availability can be limited.
- Pass clocks/timestamps into time-sensitive code so tests stay deterministic.
- Return deterministic ordering even when dictionaries or sets are involved.
