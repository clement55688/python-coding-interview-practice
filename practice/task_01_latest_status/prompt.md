# Module 01: Latest sample status

Original practice exercise; not an actual Benchling interview question.

A lab system receives sample status events in arbitrary order. Each event has a nonempty string `sample_id`, an integer `timestamp`, and a string `status`.

Core task: implement `latest_status(events)` returning a dictionary from each sample ID to its most recent status. For equal timestamps for the same sample, the event appearing later in the input wins. Input records are valid. Do not modify the input. Empty input returns an empty dictionary.

Example:

```python
events = [
    {"sample_id": "A", "timestamp": 10, "status": "received"},
    {"sample_id": "B", "timestamp": 8, "status": "processing"},
    {"sample_id": "A", "timestamp": 7, "status": "queued"},
    {"sample_id": "A", "timestamp": 10, "status": "processing"},
]
# Expected: {"A": "processing", "B": "processing"}
```

Before coding: restate the tie rule, explain a straightforward approach, and identify what information must be retained for each sample.

Implement in [starter.py](starter.py), add any additional assertions to [test_task.py](test_task.py), and explain time and space complexity. Budget 25 minutes for the first attempt and 10 minutes for review.

## Follow-up: return the timestamp too

After the core task works, change the output so each sample maps to a `(timestamp, status)` pair. For the example above, the result becomes `{"A": (10, "processing"), "B": (8, "processing")}`. Update your expected values and tests to match the new contract.

The current [starter.py](starter.py) preserves your coached follow-up implementation. For a true retrieval retry, use a blank scratch file and implement the core status-only contract first, then attempt the follow-up without looking at the saved version.
