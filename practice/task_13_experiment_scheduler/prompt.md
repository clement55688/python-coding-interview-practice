# Module 13: Experiment dependency scheduler

Original practice exercise; not an actual Benchling interview question.

Implement `schedule(tasks)` where `tasks` is a list of dictionaries with `id`, `depends_on` (list of IDs), and integer `priority`.

Return a valid execution order. Whenever multiple tasks are ready, choose higher priority first, then lexicographically smaller ID. Reject duplicate IDs, missing dependency IDs, self-dependencies, non-integer priorities, and cycles with `ValueError`. Do not mutate inputs.

Explain why a global sort by priority is insufficient.
