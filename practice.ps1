param(
    [Parameter(Position = 0)]
    [string]$Command = "today",

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingArgs
)

$ProjectRoot = $PSScriptRoot

if ($Command -eq "agent") {
    $Prompt = @"
Act as my coding interview coach for this repository. Read AGENTS.md, README.md,
ONGOING_PRACTICE_PLAN.md, progress.md, and .practice-progress.json if it exists.
Choose the highest-value next exercise based on actual recorded evidence. Tell me
the task number, ask one focused clarification question, and follow the hint ladder.
Do not reveal a full solution before I attempt it. Record real results only after I
report my attempt or run the tests.
"@
    & codex -C $ProjectRoot $Prompt
    exit $LASTEXITCODE
}

$KnownPython = Join-Path $env:LOCALAPPDATA "Programs\Python\Python313\python.exe"
if (Test-Path $KnownPython) {
    & $KnownPython (Join-Path $ProjectRoot "tools\practice_coach.py") $Command @RemainingArgs
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 (Join-Path $ProjectRoot "tools\practice_coach.py") $Command @RemainingArgs
} else {
    & python (Join-Path $ProjectRoot "tools\practice_coach.py") $Command @RemainingArgs
}
exit $LASTEXITCODE
