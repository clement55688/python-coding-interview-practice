# Module 14: 96-well microplate allocator

Original practice exercise; not an actual Benchling interview question.

Implement `allocate(samples, reserved=None)`.

A 96-well plate has rows `A`-`H` and columns `1`-`12`. `samples` contains dictionaries with a unique non-empty string `id` and `replicates` from 1 to 8. `reserved` is an optional collection of well names.

Assign every replicate to an unused, non-reserved well. Replicates of the same sample must use different rows. Return `{sample_id: [well, ...]}` in sample input order, with each list in column-major well order (`A1, B1, ..., H1, A2, ...`). Choose the lexicographically earliest valid complete allocation under that well order. Raise `ValueError` for malformed input/reservations or when no allocation exists. Do not mutate inputs.

Start with a clear correct approach; discuss how you would optimize for many plates later.
