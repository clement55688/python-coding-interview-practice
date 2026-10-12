# 26 — Longest stable sensor window

Implement `longest_stable_window(readings, max_spread)`.

Return the half-open indexes `(start, end)` of the longest contiguous window where:

```text
max(window) - min(window) <= max_spread
```

- Break equal-length ties by choosing the earliest start.
- Return `(0, 0)` for empty input.
- Readings and `max_spread` must be numeric but not booleans.
- `max_spread` must be nonnegative.
- Do not mutate the input.
- Target O(n) time using two monotonic deques.

Explain what each deque stores, why obsolete indexes leave from the front, and why every index enters and leaves each deque at most once.

Follow-up: return the actual readings without exposing the caller's mutable list.
