# Module 05: Debug status counts

Original practice exercise; not an actual Benchling interview question.

## Prompt

The function in [starter.py](starter.py) is intentionally incorrect. It should return a dictionary mapping each status to the number of events with that status.

Run the Module 05 tests and inspect the failure. Do not immediately rewrite the function. First:

1. Identify the smallest input that demonstrates the bug.
2. State what `counts[status]` should mean after processing each event.
3. Make the smallest correction that restores that invariant.
4. Add tests for empty input, one event, and repeated statuses to [test_task.py](test_task.py).

Events have a valid string `status` field. Do not mutate the input. Explain why the original implementation failed and give time and space complexity. After correcting the bug, rerun the Module 05 unittest command from the project root.

## Follow-up

Add a second result containing the number of distinct sample IDs for each status. First clarify whether the same sample may appear under multiple statuses and what exactly is being counted.

Budget 15 minutes for diagnosis and repair, 15 minutes for the follow-up, and 10 minutes for review.
