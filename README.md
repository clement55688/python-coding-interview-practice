# Python coding interview practice

## One-command practice coach

From this folder, run:

```powershell
.\practice.cmd today
```

Useful commands:

```powershell
.\practice.cmd status
.\practice.cmd start
.\practice.cmd start 26
.\practice.cmd finish --minutes 38 --hints 1 --notes "Missed the left-boundary update"
.\practice.cmd agent
```

- `today` recommends the next exercise from your recorded evidence.
- `start` records the beginning of an attempt.
- `finish` runs that module's tests and records the real result in the private `.practice-progress.json` file.
- `status` summarizes completed and pending work.
- `agent` opens Codex CLI in this project with the coaching rules and progress context. This gives you an interactive agent in the terminal, so the desktop app is optional.

The progress JSON is ignored by Git so personal attempt history is not published. Use `progress.md` only for notes you intentionally want committed.

## Run your code

Open [the VS Code workspace](python-interview-practice.code-workspace), edit a Python exercise, and press Ctrl+Shift+B. The task saves open files first and runs that module's unit tests.

Alternatively, open a fresh PowerShell terminal in this folder and run a module's tests:

```powershell
python -m unittest practice.task_01_latest_status.test_task -v
```

If your current terminal has an outdated PATH, use:

```powershell
& "$env:LOCALAPPDATA/Programs/Python/Python313/python.exe" -m unittest practice.task_01_latest_status.test_task -v
```

All 31 modules now use the same folder structure: `prompt.md`, `starter.py`, and `test_task.py`. Implement your solution in `starter.py`; replace the module name in the command above to check another solution. To run every exercise test, use `python -m unittest discover -s practice -p "test_task.py" -v`. Tests use the standard library; no third-party packages are required. Copy [template.py](practice/template.py) for future exercises. See the full [coding interview practice track](practice/README.md) for the module catalog, interview workflow, and readiness criteria.

## Unified practice track: Modules 01–31

Eight harder exercises extend the same numbered practice track in `practice/task_07_*` through `practice/task_14_*`. Like Modules 01–06, each folder contains a prompt, a starter file, and visible unit tests; this package format keeps the prompt, implementation, and repeatable tests together. Use the same clarify/approach/implement/test/debrief workflow throughout. For example:

```powershell
python -m unittest practice.task_07_traffic_controller.test_task -v
```

The former last-day exercises were migrated here as Modules 16–19. Modules 20–25 add the formats emphasized in the latest shared thread: dictionary-of-sets aggregation, simulation, object-oriented machine coding, rate limiting, circular queues, and practical JSON-style transformation.

Modules 26–31 add a focused DSA-and-machine-coding set: monotonic sliding windows, BFS path reconstruction, heap scheduling, stack parsing, stateful OOP, and configurable state-machine extensions.

The starter tests fail until you implement each task. Full reference solutions are intentionally withheld from this coaching workspace. See [ongoing practice plan](ONGOING_PRACTICE_PLAN.md), [company research](COMPANY_RESEARCH.md), and the [interview runbook](INTERVIEW_RUNBOOK.md).

## Archived Benchling interview context

- Original role context: Software Engineer, Full Stack (Process Execution).
- Original interview format: one-hour Zoom and CoderPad technical screen using Python.

The original recruiter attachment said the first round assessed brainstorming and implementing a working solution, readable and maintainable code, and everyday data structures. This section remains only as historical context. The exercises now form a general Python interview-practice track and are not claimed questions from any company.

The recruiter prohibits AI tools during interviews. Practice toward independent performance and disable AI assistance for the actual interview.

## How we work

One problem at a time. First clarify requirements, give examples, and explain an approach. Then implement, test, explain complexity, and handle a follow-up. The coach gives progressively stronger hints only when needed; no full solution before a real attempt unless explicitly requested. Record errors and redo missed problems from a blank editor the next day.

Use `Start today's practice` to resume. Use `hint` for one small hint, `review` for feedback on your attempt, or `mock interview` for a timed exercise with feedback afterward. Timing is self-reported; no background monitoring is implied.

Start with [the diagnostic](practice/task_01_latest_status/prompt.md). Track evidence in [progress](progress.md). See [the plan](plan.md). System design comes after coding readiness or when the next round is confirmed.
