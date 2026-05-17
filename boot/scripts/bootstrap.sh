#!/usr/bin/env bash
# 5QLN Boot — Bootstrap Script
# Installs L0 (Codex), L1 (Kernel), L3 (Workspace), L4 (Skills), L5 (Runtime)
# Usage: bash bootstrap.sh [codex|kernel|workspace|runtime|all]
set -euo pipefail

# CONSTANTS
CODEX_HASH="feaa46b4147d4e023cdd3fd59c051d063e8ec654ee7b38a481dcd5e4c781859b"
KERNEL_NORMALIZED_HASH="24b7e65f767e10c780af81c88b10dd43ee94620716dd741009e845c97f6ddc6c"
BOOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ASSETS_DIR="$BOOT_DIR/assets"
KERNEL_DIR="$HOME/.5qln"
WORKSPACE_DIR="/home/workspace"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

log()  { echo -e "${GREEN}[BOOT]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
fail() { echo -e "${RED}[FAIL]${NC} $1"; exit 1; }

# ═══════════════════════════════════════════════════════════════
# L0: CODEX
# ═══════════════════════════════════════════════════════════════

install_codex() {
    log "Installing L0: Codex"
    mkdir -p "$KERNEL_DIR"

    cp "$ASSETS_DIR/codex.txt" "$KERNEL_DIR/codex.txt"

    local actual
    actual=$(sha256sum "$KERNEL_DIR/codex.txt" | cut -d' ' -f1)

    if [ "$actual" != "$CODEX_HASH" ]; then
        fail "Codex hash mismatch. Expected $CODEX_HASH, got $actual"
    fi

    # Verify 9 lines, 217 bytes
    local lines bytes
    lines=$(wc -l < "$KERNEL_DIR/codex.txt")
    bytes=$(wc -c < "$KERNEL_DIR/codex.txt")

    if [ "$lines" -ne 9 ]; then
        fail "Codex line count: expected 9, got $lines"
    fi
    if [ "$bytes" -ne 217 ]; then
        fail "Codex byte count: expected 217, got $bytes"
    fi

    log "Codex installed: 9 lines, 217 bytes, SHA-256: ${actual:0:8}..."
}

# ═══════════════════════════════════════════════════════════════
# L1: KERNEL
# ═══════════════════════════════════════════════════════════════

install_kernel() {
    log "Installing L1: Kernel"

    mkdir -p "$KERNEL_DIR"
    cp "$ASSETS_DIR/init.py" "$KERNEL_DIR/init.py"
    chmod 755 "$KERNEL_DIR/init.py"

    log "Running kernel self-verify..."
    local verify_out
    verify_out=$(python3 "$KERNEL_DIR/init.py" verify 2>&1) || fail "Kernel verify failed: $verify_out"

    local verified
    verified=$(echo "$verify_out" | python3 -c "import json,sys; print(json.load(sys.stdin).get('verified',False))")
    if [ "$verified" != "True" ]; then
        fail "Kernel self-verify: verification failed"
    fi

    local normalized_actual
    normalized_actual=$(sha256sum "$KERNEL_DIR/init.py" | cut -d' ' -f1)

    log "Kernel installed. SHA-256: ${normalized_actual:0:8}..."
    log "Kernel self-verify: PASSED"

    # Run status for visual confirmation
    python3 "$KERNEL_DIR/init.py" status
}

# ═══════════════════════════════════════════════════════════════
# L3: WORKSPACE DEFAULTS
# ═══════════════════════════════════════════════════════════════

install_workspace() {
    local human="${1:-}"
    local mode="${2:-standard}"
    local question="${3:-}"

    log "Installing L3: Workspace defaults"

    if [ ! -f "$ASSETS_DIR/AGENTS.md.template" ]; then
        fail "AGENTS.md.template not found"
    fi
    if [ ! -f "$ASSETS_DIR/SOUL.md.template" ]; then
        fail "SOUL.md.template not found"
    fi

    # If AGENTS.md already exists, back it up
    if [ -f "$WORKSPACE_DIR/AGENTS.md" ]; then
        warn "AGENTS.md exists, backing up to AGENTS.md.bak-$(date +%Y%m%d%H%M%S)"
        cp "$WORKSPACE_DIR/AGENTS.md" "$WORKSPACE_DIR/AGENTS.md.bak-$(date +%Y%m%d%H%M%S)"
    fi

    # Copy and personalize templates
    local install_date
    install_date=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    sed -e "s/{{HUMAN_NAME}}/${human:-Human}/g" \
        -e "s/{{FOUNDING_QUESTION}}/${question:-What question brings you here?}/g" \
        -e "s/{{SETUP_MODE}}/${mode}/g" \
        -e "s/{{INSTALL_DATE}}/${install_date}/g" \
        -e "s/{{CODEX_HASH}}/${CODEX_HASH:0:8}/g" \
        "$ASSETS_DIR/AGENTS.md.template" > "$WORKSPACE_DIR/AGENTS.md"

    sed -e "s/{{HUMAN_NAME}}/${human:-Human}/g" \
        -e "s/{{SETUP_MODE}}/${mode}/g" \
        "$ASSETS_DIR/SOUL.md.template" > "$WORKSPACE_DIR/SOUL.md"

    log "AGENTS.md written"
    log "SOUL.md written"
}

# ═══════════════════════════════════════════════════════════════
# L5: RUNTIME DIRECTORIES
# ═══════════════════════════════════════════════════════════════

install_runtime() {
    log "Installing L5: Runtime directories"

    mkdir -p "$WORKSPACE_DIR/5qln-journal/events"
    mkdir -p "$WORKSPACE_DIR/5qln-evolution"
    mkdir -p "$WORKSPACE_DIR/5qln-alpha-library"

    # Initialize candidates.json if empty
    if [ ! -f "$WORKSPACE_DIR/5qln-evolution/candidates.json" ]; then
        echo '{"candidates":[],"generated_at":"'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'","events_analyzed":0,"skills_tracked":0}' > "$WORKSPACE_DIR/5qln-evolution/candidates.json"
    fi

    # Initialize library.json if empty
    if [ ! -f "$WORKSPACE_DIR/5qln-alpha-library/library.json" ]; then
        echo '{"entries":[],"meta":{"created":"'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'","version":"1.0.0"}}' > "$WORKSPACE_DIR/5qln-alpha-library/library.json"
    fi

    log "Runtime directories created"
}

# ═══════════════════════════════════════════════════════════════



# ═══════════════════════════════════════════════════════════════
# L4: SKILLS
# ═══════════════════════════════════════════════════════════════

install_skills() {
    log "Installing L4: Core skills"

    local skills_src="$BOOT_DIR/../skills"

    # Core skills (from kit download)
    if [ -d "$skills_src/core" ]; then
        log "  Core skills..."
        for skill_dir in "$skills_src/core"/*/; do
            local skill_name
            skill_name=$(basename "$skill_dir")
            local dst="$WORKSPACE_DIR/Skills/$skill_name"
            mkdir -p "$dst"
            if [ -d "$skill_dir" ]; then
                # Copy FULL skill directory — scripts, references, assets
                cp -r "$skill_dir"* "$dst"/
                echo "    ✓ $skill_name"
            fi
        done
    else
        warn "  Core skills not found at $skills_src/core — skipping"
    fi

    # Journal phase skills
    if [ -d "$skills_src/journal" ]; then
        log "  Journal skills..."
        mkdir -p "$WORKSPACE_DIR/5qln-journal/skills"
        for skill_file in "$skills_src/journal"/*.md; do
            local skill_name
            skill_name=$(basename "$skill_file")
            cp "$skill_file" "$WORKSPACE_DIR/5qln-journal/skills/$skill_name"
            echo "    ✓ $skill_name"
        done
    else
        warn "  Journal skills not found at $skills_src/journal — skipping"
    fi

    log "Skills installed"
}

# ═══════════════════════════════════════════════════════════════
# L2: ZO CONFIGURATION (informational)
# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

show_zo_config() {
    echo ""
    log "══════════ ZO CONFIGURATION (L2) ══════════"
    echo ""
    echo "The following must be configured by the AI running this boot skill:"
    echo ""
    echo "1. PERSONA:"
    echo "   create_persona using assets/persona-prompt.md"
    echo "   Name: '5qln', Scopes: all"
    echo "   set_active_persona('c1aa98da-...')"
    echo ""
    echo "2. RULE:"
    echo "   create_rule with condition 'session_start':"
    echo "   'python3 ~/.5qln/init.py status'"
    echo ""
    echo "3. MCP SERVERS (optional):"
    echo "   5qln-watcher-mcp, 5qln-mcp, 5qln-skills-mcp"
    echo ""
    echo "══════════════════════════════════════════════"
}

# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

usage() {
    echo "Usage: bash bootstrap.sh [codex|kernel|workspace|skills|runtime|all|zo-config]"
    echo "  codex      Install L0 (Codex) only"
    echo "  kernel     Install L1 (Kernel) only"
    echo "  workspace  Install L3 (Workspace defaults)"
    echo "  skills     Install L4 (Core skills) only"
    echo "  runtime    Install L5 (Runtime directories)"
    echo "  all        Install L0+L1+L3+L4+L5 (complete filesystem setup)"
    echo "  zo-config  Show L2 instructions (persona + rule)"
    echo ""
    echo "Workspace env vars:"
    echo "  HUMAN_NAME          Your name/handle (default: 'Human')"
    echo "  SETUP_MODE          minimal|standard|full (default: standard)"
    echo "  FOUNDING_QUESTION   Your founding question"
}

main() {
    local cmd="${1:-all}"

    case "$cmd" in
        codex)
            install_codex
            ;;
        kernel)
            install_codex  # kernel depends on codex
            install_kernel
            ;;
        workspace)
            local human="${HUMAN_NAME:-}"
            local mode="${SETUP_MODE:-standard}"
            local q="${FOUNDING_QUESTION:-}"
            install_workspace "$human" "$mode" "$q"
            ;;
        runtime)
            install_runtime
            ;;
        all)
            install_codex
            install_kernel
            local human="${HUMAN_NAME:-}"
            local mode="${SETUP_MODE:-standard}"
            local q="${FOUNDING_QUESTION:-}"
            install_workspace "$human" "$mode" "$q"
            install_runtime
            install_skills
            show_zo_config
            ;;
        zo-config)
            show_zo_config
            ;;
        *)
            usage
            exit 1
            ;;
    esac

    echo ""
    log "Bootstrap complete."
}

main "$@"
