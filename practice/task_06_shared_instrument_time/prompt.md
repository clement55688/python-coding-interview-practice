# Module 06: Earliest shared instrument time (timed mock)

Original practice exercise; not an actual Benchling interview question.

## Mock rules

Set a 60-minute timer. Use a plain editor without AI completion or coaching. Do not read the follow-up until the core task is implemented and tested. Narrate your reasoning as if a teammate is listening. Ask for clarification before coding when a requirement is unclear; use only the prompt's stated assumptions.

## Prompt

Two labs have lists of available instrument windows. Each window is a half-open interval `(start, end)`, with integer times and `start < end`. Within each list, windows are sorted by start and do not overlap.

Implement `earliest_shared_start(first, second, duration)` returning the earliest integer start time at which both labs have an uninterrupted shared window at least `duration` units long. Return `None` if no such time exists. `duration` is a positive integer. A slot ending exactly at a window's end is valid. Do not modify either input.

Example:

```python
first = [(1, 5), (8, 14)]
second = [(2, 4), (9, 12)]
duration = 3
# Expected: 9
```

## Suggested timeboxes

- 5 minutes: introductions and clarification
- 10 minutes: examples, approach, and complexity
- 30 minutes: implementation and tests
- 10 minutes: follow-up
- 5 minutes: debrief notes

## Follow-up (open only after the core task)

Return the earliest shared window itself as `(start, end)` rather than only its start. Then explain what additional change would be needed to return every shared window of at least the requested duration.

After the mock, write down actual elapsed time, any hints (there should be none during the mock), bugs found, tests run, and the next retry. Run the checks in [test_task.py](test_task.py). Do not award yourself independent readiness based only on this prompt: the target is two fresh timed tasks with working code, relevant tests, and a clear complexity explanation.
