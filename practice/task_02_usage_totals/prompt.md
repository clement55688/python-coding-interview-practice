# Module 02: Reagent usage totals

Original practice exercise; not an actual Benchling interview question.

## Prompt

A lab records reagent usage as dictionaries with `record_id`, `reagent`, and integer `quantity` fields. Implement `usage_totals(records)` to return a dictionary mapping each reagent name to the sum of its quantities.

Some `record_id` values may repeat. Count only the **first record** with a given ID; ignore later records with that ID even if their reagent or quantity differs. Records and fields are valid, quantities are nonnegative integers, and IDs and reagent names are nonempty strings. Do not modify the input. Empty input returns `{}`.

Example:

```python
records = [
    {"record_id": "r1", "reagent": "buffer", "quantity": 3},
    {"record_id": "r2", "reagent": "buffer", "quantity": 4},
    {"record_id": "r1", "reagent": "enzyme", "quantity": 90},
]
# Expected: {"buffer": 7}
```

## Before coding

Restate which duplicate is counted. Describe what must be remembered to deduplicate and what must be accumulated. Identify an empty-input test and a duplicate-ID test.

Implement in [starter.py](starter.py). Add assertions to [test_task.py](test_task.py) for the example, empty input, and a case where a repeated ID has conflicting data. Explain time and space complexity. Budget 25 minutes for implementation and 10 minutes for review.

## Follow-up

If the caller also wants the number of distinct records counted for each reagent, what state would you add, and what should happen to a duplicate ID?
