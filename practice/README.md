# Coding interview practice track

These are original Python interview exercises, not actual or claimed questions from any company. The track emphasizes implementing a working solution, explaining your thinking, readable code, everyday data structures, collaborative debugging, and extensibility. It focuses on coding first; system design can follow once coding readiness is demonstrated or an interview scope requires it.

## Start here

1. Read the prompt for the current module; don't open other modules during a timed attempt.
2. Before coding, explain the contract, one example, the simplest approach, and what state you need to track.
3. Implement the exercise in that module's `starter.py`. Modules 01–06 preserve your existing attempts; use a blank scratch file for a retrieval retry. Leave the supplied tests intact and add your own cases to `test_task.py`.
4. To check one solution, open any file in its module and press **Ctrl+Shift+B**, or run `python -m unittest practice.task_01_latest_status.test_task -v` from the project root (replace the module name as needed). To run every module's tests, use `python -m unittest discover -s practice -p "test_task.py" -v`.
5. Tests use Python's standard `unittest` library. A passing suite means the implementation meets those tested cases; also check correctness against the full prompt, explain complexity, and try your own edge cases. If `python` is unavailable, use the interpreter command in the project `README.md`.
6. Explain correctness and complexity out loud. Record actual time, hints, mistakes, and the next retry in the project [progress log](../progress.md).

Ask for a hint when stuck. Hints are given one at a time: clarify the example, identify an invariant, suggest a data structure, then pseudocode only if needed. Ask for a review after making a real attempt. During a mock interview, coaching is withheld until the debrief unless you explicitly end the mock.

## Modules 01–06: core sequence

| Day | Module | Core practice | Exit evidence |
| --- | --- | --- | --- |
| Oct 6 | [01 — Latest sample status](task_01_latest_status/prompt.md) | Rebuild from blank; add the timestamp/status follow-up | Correct tie behavior; tests; explain O(n) time and O(k) space |
| Oct 7 | [02 — Usage totals](task_02_usage_totals/prompt.md) | Aggregate quantities while ignoring duplicate record IDs | Explain the duplicate rule and state; test conflicting duplicate data |
| Oct 8 | [03 — Reservation windows](task_03_reservation_windows/prompt.md) | Sort and merge overlapping intervals | Explain endpoint semantics, mutation, and O(n log n) time |
| Oct 9 | [04 — Workflow prerequisites](task_04_workflow_prerequisites/prompt.md) | Detect whether all steps can run given dependencies | Handle cycles, missing nodes, duplicate edges; explain graph traversal |
| Oct 10 | [05 — Debugging counts](task_05_debugging_counts/prompt.md) | Diagnose a failing implementation, repair it, and add tests | State the bug, the invariant, a regression test, and complexity |
| Oct 11 | [06 — Shared instrument time](task_06_shared_instrument_time/prompt.md) | Timed mock using two-pointer interval traversal | Clarify assumptions, implement and test independently, debrief candidly |

## Modules 07–14: additional challenge bank

These modules are original practice exercises derived from public interview themes. They are not claimed company questions. Use the same `prompt.md` + `starter.py` + `test_task.py` format as Modules 01–06.

| Module | Exercise | Main signal | Target |
| --- | --- | --- | ---: |
| 07 | [Traffic controller](task_07_traffic_controller/prompt.md) | State machine and invariants | 45 min |
| 08 | [Gene segment chains](task_08_gene_chains/prompt.md) | Sorting and interval merging | 45 min |
| 09 | [Expiring LRU cache](task_09_expiring_lru/prompt.md) | Data structures and edge cases | 60 min |
| 10 | [JSON schema validator](task_10_json_validator/prompt.md) | Recursion and interface design | 60 min |
| 11 | [Search engine repair](task_11_search_repair/prompt.md) | Debugging and extension | 50 min |
| 12 | [Versioned lab notebook](task_12_versioned_notebook/prompt.md) | Data modeling and immutability | 55 min |
| 13 | [Experiment scheduler](task_13_experiment_scheduler/prompt.md) | Graphs and deterministic output | 50 min |
| 14 | [Microplate allocator](task_14_plate_allocator/prompt.md) | Constraints and backtracking | 60 min |
| 15 | [Two-direction traffic light simulation](task_15_traffic_light_simulation/prompt.md) | Simulation, state transitions, and boundaries | 45 min |

Example command from the project root:

```powershell
python -m unittest practice.task_07_traffic_controller.test_task -v
```

Prioritize 07, 09, 10, 11, and 15. Module 15 is an original, tick-based adaptation of a publicly shared candidate experience, not a verified company question. Use 08 and 13 for algorithm reinforcement; save 12 and 14 for later architecture and data-modeling preparation.

## Modules 16–25: practical coding and machine coding

Modules 16–19 were migrated from the separate last-day practice folder. Modules 20–25 extend the track using the mix recommended in the October 12 shared discussion: DSA, simulations, object-oriented implementation, practical transformations, and explanation under changing requirements.

| Module | Exercise | Main signal | Target |
| --- | --- | --- | ---: |
| 16 | [Paginated API](task_16_api_pagination/prompt.md) | Pagination, retries, validation | 45 min |
| 17 | [DNA n-gram search](task_17_dna_ngram_search/prompt.md) | Sets, inverted index, strings | 50 min |
| 18 | [Nested HTML ranges](task_18_html_range_tags/prompt.md) | Boundary events and nesting | 45 min |
| 19 | [Search debugging mock](task_19_search_debugging_mock/prompt.md) | Debugging and extension | 50 min |
| 20 | [Maximum students per bench](task_20_max_students_bench/prompt.md) | Dictionary of sets | 25 min |
| 21 | [Robot navigator](task_21_robot_navigator/prompt.md) | Simulation and state | 40 min |
| 22 | [Elevator controller](task_22_elevator_controller/prompt.md) | OOP and extensibility | 55 min |
| 23 | [Sliding-window limiter](task_23_sliding_window_limiter/prompt.md) | Deques and system behavior | 45 min |
| 24 | [Circular queue](task_24_circular_queue/prompt.md) | Array-backed data structure | 35 min |
| 25 | [Experiment summary](task_25_experiment_summary/prompt.md) | JSON-style transformation | 45 min |

Use [the ongoing plan](../ONGOING_PRACTICE_PLAN.md) to balance these against ordinary DSA practice. Completing more modules is not the goal; independent implementation, targeted tests, clear complexity analysis, and adapting to one follow-up are the readiness evidence.

## Modules 26–31: focused DSA and extensibility

| Module | Exercise | Main signal | Target |
| --- | --- | --- | ---: |
| 26 | [Stable sensor window](task_26_stable_reading_window/prompt.md) | Sliding window and monotonic deques | 40 min |
| 27 | [Shortest workflow path](task_27_shortest_workflow_path/prompt.md) | BFS and path reconstruction | 35 min |
| 28 | [Instrument scheduler](task_28_instrument_scheduler/prompt.md) | Heap and event simulation | 45 min |
| 29 | [Grouped formula parser](task_29_formula_parser/prompt.md) | Stack parsing | 40 min |
| 30 | [Vending machine](task_30_vending_machine/prompt.md) | Stateful OOP and validation | 50 min |
| 31 | [Configurable phase cycle](task_31_configurable_cycle/prompt.md) | Extensible state machine | 45 min |

Suggested order: 20 as a short warm-up, then 26, 27, 28, 30, 29, and 31. Use Module 31 specifically to rehearse changing requirements after an initial traffic-light design.

The schedule is a coaching recommendation, not a forecast of interview questions. If a session takes longer, repeat the weak skill rather than rushing ahead. A six-hour study day can use the blocks below; if less time is available, preserve the timed attempt and review, and shorten the drills.

## Daily structure (up to six hours)

- **45 min retrieval:** rebuild yesterday's core idea from a blank editor; explain the invariant before typing.
- **75 min guided coding:** today's prompt, one focused hint at a time, then a code review.
- **75 min practical variation:** add the stated follow-up or invent a boundary test; don't copy a finished solution.
- **60 min independent attempt:** fresh problem or mock segment with no hints or AI completions.
- **30 min debrief:** review correctness, tests, readability, complexity, and communication; update progress.
- **30 min Python fluency:** drill only relevant fundamentals (dictionary membership and updates, sets, tuple unpacking, sorting with a key, or `collections.deque`).
- Take breaks between blocks. The six-hour plan includes breaks as described in the project [plan](../plan.md).

## Interview loop to rehearse

1. **Clarify:** inputs, output, ordering/tie behavior, invalid or empty cases, and mutation expectations.
2. **Example:** walk through a representative case and one edge case.
3. **Approach:** describe a straightforward algorithm and the state/data structure it needs.
4. **Complexity:** name the input size and retained-state size; account for sorting separately.
5. **Implement:** write small, readable steps; narrate decisions without rushing.
6. **Test:** run the example and targeted assertions; inspect a failing case before changing code.
7. **Extend:** handle one new requirement without breaking the original contract.

## Readiness checks

The target is evidence, not a guarantee: complete two fresh timed tasks with working code, relevant assertions, clear complexity analysis, and no substantive hints. Score each area from 0 (not demonstrated) to 3 (independent): clarification, approach, implementation, testing/debugging, complexity, and communication. A correctness failure is recorded even if the other scores are strong. Retry missed tasks from a blank editor the next day.

On Oct 12, do only a short warm-up, check the interview environment, and join a few minutes early. The recruiter prohibits AI tools during the interview; practice independently and follow that rule.
