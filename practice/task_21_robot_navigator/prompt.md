# 21 — Robot movement simulation

Implement `run_robot(width, height, obstacles, commands, start=(0, 0), heading="N")`.

- Coordinates satisfy `0 <= x < width` and `0 <= y < height`.
- Commands are `L`, `R`, and `F`.
- `L` and `R` rotate without moving.
- `F` advances one cell in the current direction.
- A forward move that would hit a wall or obstacle is ignored.
- Return `{"position": (x, y), "heading": heading, "visited": [...]}`.
- `visited` includes the starting cell and every successfully entered cell; turns and blocked moves add nothing.
- Reject invalid dimensions, positions, headings, obstacles, or commands with `ValueError`.
- Do not mutate the obstacle collection or command list.

Explain what state changes for each command and why processing is O(c) time for `c` commands with a set of obstacles.

Follow-up: add a `B` command that moves backward without changing heading.
