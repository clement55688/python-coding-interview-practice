# 25 — Transform experiment event data

Implement `summarize_runs(events)`.

Each event has `event_id`, `run_id`, `sample_id`, `status`, and numeric `timestamp`.

- Ignore repeated `event_id` values after their first occurrence.
- For each `(run_id, sample_id)`, retain the event with the greatest timestamp.
- If timestamps tie, the later event in input order wins.
- Group retained samples by run.
- Return runs sorted by `run_id`.
- Each output item is:

```python
{
    "run_id": "r1",
    "sample_ids": ["s1", "s2"],
    "status_counts": {"complete": 1, "failed": 1},
}
```

- Sort `sample_ids` and status keys lexicographically.
- Validate required fields, non-empty string IDs/status, and numeric non-boolean timestamps.
- Do not mutate input dictionaries.

Explain the two dictionary keys you use, deterministic ordering, and O(n + r log r + s log s) style costs.

Follow-up: produce the same output from a stream too large to keep entirely in memory.
