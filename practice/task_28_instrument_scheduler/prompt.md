# 28 — Priority instrument scheduler

Implement `schedule_instrument(jobs)` for one non-preemptive instrument.

Each job is:

```python
{"id": "j1", "arrival": 0, "duration": 4, "priority": 2}
```

- At any decision time, choose the arrived job with the greatest priority.
- Break priority ties by earlier arrival, then lexicographically smaller ID.
- A running job is never interrupted.
- If no job is ready, jump time to the next arrival.
- Return dictionaries containing `id`, `start`, and `end` in execution order.
- Validate unique non-empty IDs, nonnegative numeric arrivals, positive numeric durations, and integer non-boolean priorities.
- Do not mutate jobs.
- Target O(n log n) time using a sorted arrival list and a heap.

Explain the two ordered views of the data and why every job enters the heap once.

Follow-up: add a cooldown time between jobs.
