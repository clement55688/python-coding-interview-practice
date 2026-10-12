# 31 — Configurable phase cycle

Implement `PhaseCycle(phases)` as an extensible state machine.

`phases` is an ordered list such as `[('GREEN', 3), ('YELLOW', 1), ('RED', 2)]`. A phase remains active for its configured number of ticks before advancing cyclically.

- Start at the first phase with elapsed time `0`.
- `tick(count=1)` advances time and returns a snapshot.
- `update_duration(name, duration)` changes a phase's duration.
- If the current phase's new duration is less than or equal to elapsed time, advance immediately and carry excess elapsed time through later phases.
- `snapshot()` returns `phase`, `elapsed`, `remaining`, and a defensive copy of phase configuration.
- Validate unique non-empty names, positive integer durations/counts, and reject booleans.
- Design `tick` so very large counts do not require one loop per tick.

Explain the current index/elapsed invariant and how total-cycle arithmetic reduces large tick counts.

Follow-up: insert or remove phases without losing the meaning of the current state.
