#!/bin/sh
set -eu
project_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "${1:-today}" = "agent" ]; then
    exec codex -C "$project_root" 'Act as my coding interview coach. Read AGENTS.md, README.md, ONGOING_PRACTICE_PLAN.md, progress.md, and .practice-progress.json if present. Choose the next exercise using recorded evidence, ask one focused question, and follow the hint ladder. Do not reveal a full solution before an attempt. Record only actual reported or tested results.'
fi
if [ "$#" -eq 0 ]; then
    set -- today
fi
exec python3 "$project_root/tools/practice_coach.py" "$@"
