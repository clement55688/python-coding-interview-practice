# Module 03: Merge instrument reservation windows

Original practice exercise; not an actual Benchling interview question.

## Prompt

An instrument has reservation windows represented as `(start, end)` integer pairs. Implement `merge_reservations(windows)` returning a new list of windows in ascending start-time order, merging windows that overlap. Windows use half-open semantics: `[start, end)` includes `start` but excludes `end`. Therefore, `(1, 4)` and `(4, 7)` are adjacent but do **not** overlap and must remain separate.

Input windows have `start < end`. The input may be unsorted. Do not mutate the input. Empty input returns `[]`.

Example:

```python
windows = [(8, 10), (1, 4), (3, 6), (4, 7)]
# Expected: [(1, 7), (8, 10)]
```

## Before coding

Clarify why `(1, 4)` and `(4, 7)` stay separate. Explain why ordering the windows helps, and identify what the output's last window represents while you scan.

Implement in [starter.py](starter.py). Test empty input, already sorted input, unsorted overlaps, adjacency, and that the input remains unchanged in [test_task.py](test_task.py). Explain sorting and scan costs separately. Budget 30 minutes for implementation and 10 minutes for review.

## Follow-up

If adjacent reservations should be coalesced too, which comparison changes? What test would prove the changed endpoint rule?
