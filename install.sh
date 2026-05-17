#!/usr/bin/env bash
# 5QLN for Zo Computer — One-Line Installer
# 
# Usage (from Zo Terminal):
#   curl -fsSL https://raw.githubusercontent.com/qlnlife/5qln-zo-kit/main/install.sh | bash
#
# This script:
#   1. Downloads the boot skill to /home/workspace/Skills/5qln-boot/
#   2. Runs bootstrap.sh (installs Codex, Kernel, workspace defaults)
#   3. Runs verify-all.sh (21