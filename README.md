# Python coding interview practice

31 original Python exercises for coding interviews, each with a prompt, a starter, and standard-library unit tests.

## What's inside

`practice/` holds 31 exercise folders, `task_01` through `task_31`. Every folder contains `prompt.md`, `starter.py`, and `test_task.py`. The names and groups below match those folders. The longer catalog is in [practice/README.md](practice/README.md).

| Category | Exercises | Count |
| --- | --- | ---: |
| Core sequence | 01 latest sample status, 02 reagent usage totals, 03 reservation windows, 04 workflow prerequisites, 05 status-count debugging, 06 shared instrument time | 6 |
| Further challenges | 07 traffic-controller state machine, 08 gene chains, 09 expiring LRU cache, 10 JSON schema validator, 11 search-engine repair, 12 versioned lab notebook, 13 experiment scheduler, 14 microplate allocator, 15 traffic-light simulation | 9 |
| Practical and machine coding | 16 paginated API, 17 DNA n-gram search, 18 nested text ranges, 19 search-index debugging, 20 students per bench, 21 robot navigator, 22 elevator controller, 23 sliding-window limiter, 24 circular queue, 25 experiment summary | 10 |
| DSA and extensibility | 26 stable sensor window, 27 shortest workflow path, 28 instrument scheduler, 29 formula parser, 30 vending machine, 31 configurable phase cycle | 6 |

These are original practice exercises. Implement each one in its `starter.py`. [practice/template.py](practice/template.py) is a blank starter for a new exercise.

## Running the tests

From the repository root:

```bash
python3 -m unittest discover -s practice -p "test_task.py" -v
```

A full run reports failures by design. Unfinished starter exercises raise `NotImplementedError`, and modules 05, 11, and 19 are debugging exercises that fail on purpose.

Run one module by name:

```bash
python3 -m unittest practice.task_01_latest_status.test_task -v
```

`./practice.sh test 1` runs that same module and does not record an attempt. On Windows, `practice.cmd` calls `practice.ps1`, which runs `tools/practice_coach.py` with Python 3.13 when that install is present, otherwise `py -3`, otherwise `python` (`.\practice.cmd test 1`). Opening [python-interview-practice.code-workspace](python-interview-practice.code-workspace) and pressing Cmd+Shift+B (macOS) or Ctrl+Shift+B (Windows) runs `test_task.py` for the exercise folder of the active file.

## Requirements

- Python 3.10 or newer. Tasks 16 and 27 annotate with `X | Y` unions, which need 3.10. This suite was run with Python 3.12.3. There is no pinned runtime file. The Windows launcher prefers a local Python 3.13 install when `%LOCALAPPDATA%\Programs\Python\Python313\python.exe` exists.
- The Python standard library only. Tests use `unittest`. There is no `requirements.txt` and no third-party package.

## Project structure

```text
.
├── practice/                  # task_01 … task_31
│   ├── README.md              # exercise catalog and practice workflow
│   ├── template.py            # blank starter for a new exercise
│   └── task_NN_<name>/
│       ├── __init__.py
│       ├── prompt.md
│       ├── starter.py
│       └── test_task.py
├── tools/practice_coach.py    # today, start, test, finish, status
├── practice.sh                # macOS and Linux launcher
├── practice.cmd               # Windows launcher
├── practice.ps1
├── python-interview-practice.code-workspace
├── plan.md                    # six-day coding plan
├── ONGOING_PRACTICE_PLAN.md
├── progress.md                # committed practice notes
├── INTERVIEW_RUNBOOK.md
├── COMPANY_RESEARCH.md
├── research/PUBLIC_SOURCES.md
└── AGENTS.md                  # coaching rules for an assistant
```

`./practice.sh finish` records an attempt in `.practice-progress.json`. That file is gitignored. This repository has no LICENSE file.
