"""Small local CLI for selecting exercises and recording real practice evidence."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRACTICE_DIR = ROOT / "practice"
STATE_FILE = Path(os.environ.get("PRACTICE_PROGRESS_FILE", ROOT / ".practice-progress.json"))
RECOMMENDED_ORDER = [20, 26, 27, 28, 30, 29, 31, 21, 23, 24, 25, 17, 18, 19, 22]


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def task_map() -> dict[int, Path]:
    result: dict[int, Path] = {}
    for path in PRACTICE_DIR.glob("task_[0-9][0-9]_*"):
        try:
            number = int(path.name.split("_", 2)[1])
        except (IndexError, ValueError):
            continue
        result[number] = path
    return result


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"active": None, "sessions": []}
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"Cannot read {STATE_FILE}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("sessions", []), list):
        raise SystemExit(f"Invalid progress file: {STATE_FILE}")
    data.setdefault("active", None)
    data.setdefault("sessions", [])
    return data


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def module_name(path: Path) -> str:
    return f"practice.{path.name}.test_task"


def task_title(path: Path) -> str:
    prompt = path / "prompt.md"
    if prompt.exists():
        for line in prompt.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                title = re.sub(r"^\d+\s+[—–-]\s+", "", line[2:].strip())
                return title.replace("—", "-").replace("–", "-")
    return path.name


def completed_numbers(state: dict) -> set[int]:
    return {
        int(session["task"])
        for session in state["sessions"]
        if session.get("passed") is True and isinstance(session.get("task"), int)
    }


def recommend(state: dict, tasks: dict[int, Path]) -> int:
    completed = completed_numbers(state)
    order = RECOMMENDED_ORDER + sorted(set(tasks) - set(RECOMMENDED_ORDER))
    for number in order:
        if number in tasks and number not in completed:
            return number
    return order[0]


def print_assignment(number: int, path: Path) -> None:
    relative_prompt = path.relative_to(ROOT) / "prompt.md"
    print(f"Task {number:02d}: {task_title(path)}")
    print(f"Prompt: {relative_prompt}")
    print(f"Edit:   {path.relative_to(ROOT) / 'starter.py'}")
    print(f"Test:   python -m unittest {module_name(path)} -v")
    print("Target: clarify -> approach -> code -> tests -> complexity -> one follow-up")


def command_today(_: argparse.Namespace) -> int:
    state, tasks = load_state(), task_map()
    if state.get("active"):
        number = int(state["active"]["task"])
        print("Resume the active attempt:")
    else:
        number = recommend(state, tasks)
        print("Recommended next practice:")
    print_assignment(number, tasks[number])
    return 0


def command_start(args: argparse.Namespace) -> int:
    state, tasks = load_state(), task_map()
    number = args.task if args.task is not None else recommend(state, tasks)
    if number not in tasks:
        raise SystemExit(f"Unknown task: {number}")
    if state.get("active"):
        active = state["active"]
        raise SystemExit(f"Task {active['task']} is already active. Finish it before starting another.")
    state["active"] = {"task": number, "started_at": now()}
    save_state(state)
    print("Attempt started. Work without AI if this is a timed mock.")
    print_assignment(number, tasks[number])
    return 0


def command_finish(args: argparse.Namespace) -> int:
    state, tasks = load_state(), task_map()
    active = state.get("active")
    number = args.task if args.task is not None else (active or {}).get("task")
    if number is None:
        raise SystemExit("No active task. Pass a task number or run `practice start` first.")
    number = int(number)
    if number not in tasks:
        raise SystemExit(f"Unknown task: {number}")
    print(f"Running Task {number:02d} tests...\n")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", module_name(tasks[number]), "-v"],
        cwd=ROOT,
        check=False,
    )
    session = {
        "task": number,
        "finished_at": now(),
        "started_at": active.get("started_at") if active and int(active["task"]) == number else None,
        "minutes": args.minutes,
        "hints": args.hints,
        "passed": result.returncode == 0,
        "notes": args.notes.strip(),
    }
    state["sessions"].append(session)
    if active and int(active["task"]) == number:
        state["active"] = None
    save_state(state)
    print(f"\nRecorded: {'PASS' if session['passed'] else 'NEEDS RETRY'}")
    print("Run `practice today` for the next recommendation.")
    return result.returncode


def command_status(_: argparse.Namespace) -> int:
    state, tasks = load_state(), task_map()
    sessions = state["sessions"]
    passed = completed_numbers(state)
    print(f"Exercises: {len(tasks)} | Recorded sessions: {len(sessions)} | Passed: {len(passed)}")
    if state.get("active"):
        active = state["active"]
        print(f"Active: Task {int(active['task']):02d}, started {active['started_at']}")
    if sessions:
        print("Recent sessions:")
        for session in sessions[-5:]:
            outcome = "PASS" if session.get("passed") else "RETRY"
            details = f"{session.get('minutes')} min" if session.get("minutes") is not None else "time unreported"
            print(f"  Task {int(session['task']):02d}: {outcome}, {details}, hints={session.get('hints', 0)}")
    next_number = recommend(state, tasks)
    print(f"Next recommendation: Task {next_number:02d} - {task_title(tasks[next_number])}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="practice", description="Choose exercises and track practice evidence.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("today", help="Show the recommended task").set_defaults(func=command_today)
    subparsers.add_parser("status", help="Show recorded progress").set_defaults(func=command_status)
    start = subparsers.add_parser("start", help="Start a timed attempt")
    start.add_argument("task", nargs="?", type=int)
    start.set_defaults(func=command_start)
    finish = subparsers.add_parser("finish", help="Run tests and record the result")
    finish.add_argument("task", nargs="?", type=int)
    finish.add_argument("--minutes", type=int)
    finish.add_argument("--hints", type=int, default=0)
    finish.add_argument("--notes", default="")
    finish.set_defaults(func=command_finish)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if getattr(args, "minutes", None) is not None and args.minutes < 0:
        raise SystemExit("--minutes must be nonnegative")
    if getattr(args, "hints", 0) < 0:
        raise SystemExit("--hints must be nonnegative")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
