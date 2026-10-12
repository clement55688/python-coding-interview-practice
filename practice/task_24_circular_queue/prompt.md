# 24 — Fixed-capacity circular queue

Implement `CircularQueue(capacity)` without using `collections.deque`.

- `enqueue(value)` returns `True`, or `False` when full.
- `dequeue()` removes and returns the oldest value; raise `IndexError` when empty.
- `front()` and `rear()` return the oldest/newest value; raise `IndexError` when empty.
- `is_empty()`, `is_full()`, and `__len__()` report state.
- Capacity must be a positive integer; reject booleans.
- All operations must be O(1).
- Clear removed array slots so queued objects can be garbage collected.

Explain the head index, current size, and how modulo arithmetic handles wrap-around.

Follow-up: implement resizing while preserving queue order.
