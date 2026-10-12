# Module 07: Traffic controller state machine

Original practice exercise; not an actual Benchling interview question.

Implement `TrafficController` for an intersection. It begins in `RED`.

- `timer`: `RED -> GREEN -> YELLOW -> RED`.
- `pedestrian`: record a pending pedestrian request; do not change color immediately.
- A pending request is served when `GREEN` receives `timer`: transition to `YELLOW` and increment `served_pedestrians`.
- `emergency`: immediately enter `RED` and emergency mode. Repeated emergency events are idempotent.
- While in emergency mode, `timer` and `pedestrian` do not change normal state; pedestrian requests remain pending.
- `clear`: leave emergency mode in `RED`. Calling it outside emergency mode raises `ValueError`.
- Any unknown event raises `ValueError`.

`handle(event)` returns a new snapshot dictionary after processing the event. `snapshot()` also returns a new dictionary with `color`, `emergency`, `pedestrian_pending`, and `served_pedestrians`.

Extension discussion: how would you support multiple intersections without making invalid transitions possible?
