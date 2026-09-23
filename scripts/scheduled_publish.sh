#!/usr/bin/env bash
# One scheduled run: publish 1–2 days and push. Intended for systemd timer or cron wrapper.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="${ROOT}/scripts/publish.log"
LOCK="${ROOT}/scripts/.publish.lock"
PYTHON="${PYTHON:-python3}"

exec 9>"${LOCK}"
if ! flock -n 9; then
  printf '%s skip: another publish is running\n' "$(date -Iseconds)" >>"${LOG}"
  exit 0
fi

cd "${ROOT}"

if [[ ! -f "${ROOT}/scripts/publish_state.json" ]]; then
  cp "${ROOT}/scripts/publish_state.example.json" "${ROOT}/scripts/publish_state.json"
fi

# One calendar run → 1 or 2 lessons (matches daily_cap in state).
COUNT=$((1 + RANDOM % 2))

{
  echo "======== $(date -Iseconds) scheduled_publish count=${COUNT} ========"
  "${PYTHON}" "${ROOT}/scripts/daily_publish.py" --count "${COUNT}"
} >>"${LOG}" 2>&1
