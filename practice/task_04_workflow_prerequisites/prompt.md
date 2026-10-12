# Module 04: Workflow prerequisites

Original practice exercise; not an actual Benchling interview question.

## Prompt

A workflow is represented by a dictionary mapping each step name to a list of prerequisite step names. Implement `can_run_all(steps)` returning `True` if every step can eventually run, and `False` if the workflow contains a cycle or names a prerequisite that is not a key in the dictionary.

An empty workflow is valid. A repeated prerequisite in one list counts only once. A step with an empty prerequisite list can run immediately.

Example:

```python
steps = {
    "analyze": ["prepare"],
    "prepare": ["collect"],
    "collect": [],
}
# Expected: True
```

## Before coding

Explain what it means for all steps to be runnable. Use a tiny cycle to show why a workflow can be blocked forever. Decide how you will track prerequisites that are still unmet and steps that are ready.

Implement in [starter.py](starter.py). Test a valid chain, an independent step, a cycle, an unknown prerequisite, and a repeated edge in [test_task.py](test_task.py). Explain time and space in terms of steps and dependency edges.

## Follow-up

If the caller asks for one valid execution order rather than a boolean, what should your function return? How would you handle a cycle in that return contract?
