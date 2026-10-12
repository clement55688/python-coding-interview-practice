# 20 — Maximum students on one bench

Implement `max_students_on_bench(records)` where each record is `(student_id, bench_id)`.

- Count a student only once per bench, even if the pair repeats.
- The same student may count once on several benches.
- Return the largest number of unique students assigned to any bench.
- Return `0` for empty input.
- Raise `ValueError` if a record is not a two-item tuple or either ID is an empty string.
- Do not mutate the input.

Interview explanation target: identify the dictionary-of-sets pattern, explain why a set handles duplicates, and state O(n) average time and O(n) space.

Follow-up: how would you return every bench tied for the maximum while preserving first-seen bench order?
