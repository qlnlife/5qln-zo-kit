#!/usr/bin/env bash
# 5QLN for Zo Computer — One-Line Installer
#
# Usage (from Zo Terminal):
#   curl -fsSL https://raw.githubusercontent.com/qlnlife/5qln-zo-kit/main/install.sh | bash
#
# What this does:
#   1. Downloads the full 5qln-zo-kit (boot/ + skills/) from GitHub
#   2. Runs bootstrap.sh (Codex, Kernel, Workspace, Skills, Runtime)
#   3. Runs verify-all.sh (integrity checks)
#   4. Prints Zo config instructions
set -euo pipefail

REPO_RAW="https://raw.githubusercontent.com/qlnlife/5qln-zo-kit/main"
KIT_DIR="/tmp/5qln-zo-kit"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║  5QLN for Zo Computer — Installer       ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Step 1: Clone the repo (gets full directory structure)
echo "[1/4] Downloading kit from GitHub..."
rm -rf "$KIT_DIR"
git clone -q --depth 1 https://github.com/qlnlife/5qln-zo-kit.git "$KIT_DIR" 2>/dev/null && echo "  ✓ Full kit cloned" || {
    echo "  ⚠ git clone failed, trying sparse curl download..."
    # Fallback: manually download essential files
    mkdir -p "$KIT_DIR"/{boot/{scripts,assets,references},skills/{core,journal}}

    download_file() {
        local src="$1" dst="$2"
        if curl -fsSL "$src" -o "$dst" 2>/dev/null; then
            return 0
        else
            echo "  ⚠ $dst (skipped)"
            return 1
        fi
    }

    # Boot files
    for f in SKILL.md scripts/bootstrap.sh scripts/verify-all.sh \
             assets/codex.txt assets/init.py \
             assets/AGENTS.md.template assets/SOUL.md.template \
             assets/persona-prompt.md references/ARCHITECTURE.md; do
        download_file "$REPO_RAW/boot/$f" "$KIT_DIR/boot/$f"
    done
    chmod +x "$KIT_DIR/boot/scripts/bootstrap.sh" "$KIT_DIR/boot/scripts/verify-all.sh" 2>/dev/null || true

    # Core skills — download SKILL.md for each
    for skill in 5qln-orchestrate 5qln-open-template-stack 5qln-corruption-codex \
                 5qln-membrane-protocol-runtime 5qln-project-space 5qln-alpha-library \
                 5qln-skill-evolve 5qln-skill-refine 5qln-research \
                 5qln-selfimprove 5qln-skillgen; do
        mkdir -p "$KIT_DIR/skills/core/$skill"
        download_file "$REPO_RAW/skills/core/$skill/SKILL.md" "$KIT_DIR/skills/core/$skill/SKILL.md"
    done

    # Journal skills
    for skill in S-skill G-skill Q-skill P-skill V-skill; do
        download_file "$REPO_RAW/skills/journal/$skill.md" "$KIT_DIR/skills/journal/$skill.md"
    done
}

# Step 2: Run bootstrap
echo ""
echo "[2/4] Running bootstrap..."
BOOT_DIR="$KIT_DIR/boot" bash "$KIT_DIR/boot/scripts/bootstrap.sh" all

# Step 3: Verify
echo ""
echo "[3/4] Verifying integrity..."
bash "$KIT_DIR/boot/scripts/verify-all.sh"

# Step 4: Print Zo config
echo ""
echo "[4/4] Setup complete."
echo ""
echo "╔══════════════════════════════════════════╗"
echo "║  5QLN INSTALLED                         ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "  Codex:   feaa46b4 (9 lines, 217 bytes)"
echo "  Kernel:  ~/.5qln/init.py"
echo "  Skills:  /home/workspace/Skills/"
echo ""
echo "  Next steps (do these in Zo UI):"
echo "  ────────────────────────────────"
echo "  1. Create a Persona named '5qln' using:"
echo "     $KIT_DIR/boot/assets/persona-prompt.md"
echo ""
echo "  2. Create a Rule: Settings → AI → Rules"
echo "     Condition: session_start"
echo "     Run: python3 ~/.5qln/init.py status"
echo ""
echo "  3. Set the '5qln' persona as active."
echo ""
echo "  Then start a new conversation."
echo ""

# Cleanup
rm -rf "$KIT_DIR"
echo ""
