#!/usr/bin/env bash
set -euo pipefail

SERVICE_NAME="quant-ml-daily-publish"
UNIT_DIR="${HOME}/.config/systemd/user"

systemctl --user disable --now "${SERVICE_NAME}.timer" 2>/dev/null || true
rm -f "${UNIT_DIR}/${SERVICE_NAME}.service" "${UNIT_DIR}/${SERVICE_NAME}.timer"
systemctl --user daemon-reload
echo "Removed ${SERVICE_NAME} user timer."
