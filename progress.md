# Practice evidence

Daily availability: 6 hours per day, confirmed by Clement. Language: Python.
Current baseline: Module 01 was completed with substantial coaching. Module 02's implementation and provided checks pass; elapsed time and independence were not reported.
Next action: correct Module 20's grouping direction, then retry Module 26 from a blank editor and explain deque operations without a reference solution.

| Date | Task | Minutes | Hints | Correctness / tests | Main gap | Retry date |
| --- | --- | --- | --- | --- | --- | --- |
| Oct 5 | Latest sample status plus timestamp/status follow-up | Not reported | Substantial: data to retain, comparison, comprehension syntax, output shape, and complexity | Example and empty/older-event assertions passed; coach updated the expected values; later run passed | Needed support moving return outside the loop, writing a dictionary comprehension, and distinguishing O(n) scan time / O(k) retained states from O(n*k) | Oct 6: rebuild the core version from a blank file before Module 02 |
| Oct 5 | Module 02: reagent usage totals | Not reported | Clarified that duplicate record IDs count only on their first occurrence | Current implementation passes example, empty-input, and conflicting-duplicate assertions; no assertion yet checks input non-mutation | Time/space explanation and degree of independence not reported | Before Module 03: explain expected complexity; retry independently if this was coached |
| Oct 6 | Module 04: workflow prerequisites | Not reported | Guided through edge direction, adjacency lists, remaining-prerequisite counts, and queue-based processing; learner reported finding a template | Implemented Kahn-style traversal with missing-prerequisite rejection and duplicate-edge deduplication; all provided checks pass | Identified O(V) for steps but needed a prompt to account for edges and space | Reimplement from a blank file without the template, then explain O(V + E) time/space |
| Oct 6 | Module 05: debug status counts | Not reported | Explained named assertion methods vs plain `assert`; clarified `is False` vs comparing to `False` and reminded that the specified return type is a dictionary | Empty, single-event, and repeated-status assertions pass when running the file | Assertion messages have minor typos/inconsistent wording; bug explanation and follow-up not yet covered | Explain the original bug and time/space complexity; then clarify and implement the distinct-sample follow-up |
| Oct 7 | Module 06: shared instrument time | Not reported | Defined sweep line; identified pointer and syntax issues; clarified merge-per-list preprocessing; provided the requested helper implementation after learner began a stub | Integrated preprocessing for both inputs; example, touching-window duration-4, exact-fit, empty, and non-mutation assertions all pass | Helper name `helper` is vague; complexity explanation not yet given | Rename helper descriptively and explain O(n + m) time and auxiliary space, including the merged lists |

Score each dimension 0–3 after an attempt: 0 not demonstrated, 1 substantial help, 2 minor help, 3 independent. Dimensions: clarification, approach, implementation, testing/debugging, complexity, communication. Record examples supporting scores; do not average away correctness failures.

## October 12 migration status

- The former `benchling-last-day-python-practice` folder was migrated into this project as Modules 16–19; the original folder is preserved under `archive/previous-last-day-folder`.
- Module 16 (API pagination) currently passes all 4 supplied tests. Elapsed time, hints, explanation quality, and independence were not recorded, so no readiness score is assigned.
- Modules 17 and 18 still contain unimplemented starters. Module 19 remains the intentionally buggy debugging starter. These are pending, not failed attempts.
- Modules 20–25 were added from the coding-format practice plan and are unattempted.
- Modules 26–31 were added as focused DSA and extensibility practice and are unattempted.

## Mistake log

For each mistake: symptom → root cause → prevention rule → evidence from a fresh retry.

- Return/comprehension: initially returned inside the event loop and had invalid comprehension syntax → indentation and `{key: value for ...}` structure were not yet secure → place final aggregation after the loop and identify key/value/iteration variables before typing → fresh retry pending.
- Complexity: estimated O(n*k) time and space because every event is visited → mixed input work with retained state → count one-pass dictionary operations separately from the number of distinct keys → fresh retry pending.

## October 12 desktop practice

- Module 20: saved the learner's implementation. All 4 supplied tests pass, but review found the grouping reversed: `(student_id, bench_id)` should add the student to the bench's set. Current code instead counts benches per student. For `[('A', 'X'), ('B', 'X')]`, the required answer is 2 but the implementation returns 1. Correction and a regression test are pending. Elapsed time and hint count were not reported; independence is not assessed.
- Module 26: all 4 supplied tests pass. Substantial coaching included validation, sliding-window movement, indexes versus values, monotonic deque candidates, front versus back removal, a six-reading dry run, and the complete solution supplied at the learner's request. Reviewed and corrected the learner's float validation and appending values instead of indexes. The learner recognized the sliding-window-plus-two-deques pattern. Elapsed time and exact hint count were not reported; this is not an independent completion.
- Next practice: independently rebuild Module 26 and explain why back removals discard dominated candidates, front removals discard expired indexes, and total deque operations are O(n). LeetCode 239 was suggested as a one-deque reinforcement exercise; no LeetCode attempt was observed.
- Environment: added the Mac `practice.sh` launcher and Python 3 workspace test task; automatic completions are disabled while Copilot Chat remains available. Local zsh shortcuts `task20` and `ptest NUMBER` were installed on this computer; they are not part of the repository.
