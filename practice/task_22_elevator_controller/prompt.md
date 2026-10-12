# 22 — Elevator controller

Implement `ElevatorController(floor_count)`.

The elevator starts at floor `0` with direction `IDLE`.

- `request(floor)` adds a destination. Duplicate requests have no additional effect.
- `step()` moves at most one floor and returns a snapshot.
- When idle, choose the closest requested floor; ties prefer the lower floor.
- While moving, continue in the same direction while any request remains in that direction.
- Service a requested floor upon arriving and remove it from pending requests.
- Reverse only when no request remains in the current direction.
- If the current floor is requested, service it without moving.
- `snapshot()` returns a new dictionary with `floor`, `direction`, and sorted `pending`.
- Reject invalid floor counts and requests with `ValueError`.

Discuss state invariants, deterministic tie-breaking, and how you would replace the pending set if requests reached millions.
