#!/usr/bin/env bash
# Install a user systemd timer: fire once per day between 06:00 and 22:00 (random delay).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UNIT_DIR="${HOME}/.config/systemd/user"
SERVICE_NAME="quant-ml-daily-publish"
RUNNER="${ROOT}/scripts/scheduled_publish.sh"

chmod +x "${RUNNER}"

mkdir -p "${UNIT_DIR}"

cat >"${UNIT_DIR}/${SERVICE_NAME}.service" <<EOF
[Unit]
Description=100 Days of Quant ML — incremental lesson publish
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
WorkingDirectory=${ROOT}
ExecStart=${RUNNER}
Environment=PYTHON=${PYTHON:-python3}

[Install]
WantedBy=default.target
EOF

cat >"${UNIT_DIR}/${SERVICE_NAME}.timer" <<EOF
[Unit]
Description=Daily random publish window 06:00–22:00 (Asia/Shanghai wall clock)

[Timer]
# 06:00 Asia/Shanghai + uniform random 0–16h → window about 06:00–22:00.
OnCalendar=*-*-* 06:00:00
Timezone=Asia/Shanghai
RandomizedDelaySec=57600
Persistent=true
Unit=${SERVICE_NAME}.service

[Install]
WantedBy=timers.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now "${SERVICE_NAME}.timer"

echo "Installed user timer: ${SERVICE_NAME}.timer"
echo "  Next runs: systemctl --user list-timers ${SERVICE_NAME}.timer"
echo "  Log: ${ROOT}/scripts/publish.log"
echo ""
echo "If this machine should publish while you are logged out, run once:"
echo "  loginctl enable-linger ${USER}"
echo ""
systemctl --user list-timers "${SERVICE_NAME}.timer" --no-pager || true
