# Cursor stop hook: commit all workspace changes when the agent finishes a turn.
$ErrorActionPreference = 'SilentlyContinue'

try {
    [void][Console]::In.ReadToEnd()
} catch {}

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
Set-Location -LiteralPath $repoRoot

if (-not (Test-Path -LiteralPath (Join-Path $repoRoot '.git'))) {
    exit 0
}

$dirty = & git status --porcelain 2>$null
if (-not $dirty) {
    exit 0
}

& git add -A 2>$null
$staged = & git diff --cached --name-only 2>$null
if (-not $staged) {
    exit 0
}

$msg = "chore: auto-commit (cursor agent $(Get-Date -Format 'yyyy-MM-dd HH:mm'))"
& git commit -m $msg 2>$null
exit 0
