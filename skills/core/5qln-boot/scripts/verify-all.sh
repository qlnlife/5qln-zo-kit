#!/usr/bin/env bash
# 5QLN Boot — Post-Install Integrity Verification
# Usage: bash verify-all.sh
# Exits 0 if all checks pass, non-zero if any fail.
set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PASS=0
FAIL=0

check() {
    local label="$1"
    if eval "$2" &>/dev/null; then
        echo -e "  ${GREEN}[PASS]${NC} $label"
        ((PASS++))
    else
        echo -e "  ${RED}[FAIL]${NC} $label"
        ((FAIL++))
    fi
}

header() {
    echo ""
    echo "━━━ $1 ━━━"
}

echo "╔══════════════════════════════════════════╗"
echo "║  5QLN BOOT — INTEGRITY VERIFICATION     ║"
echo "╚══════════════════════════════════════════╝"

# ══════════════════════════════════════════
# L0: CODEX
# ══════════════════════════════════════════
header "L0: Codex"

CODEX_HASH="feaa46b4147d4e023cdd3fd59c051d063e8ec654ee7b38a481dcd5e4c781859b"

check "Codex file exists" '[ -f "$HOME/.5qln/codex.txt" ]'
check "Codex SHA-256 matches" '[ "$(sha256sum "$HOME/.5qln/codex.txt" | cut -d" " -f1)" = "$CODEX_HASH" ]'
check "Codex is 9 lines" '[ "$(wc -l < "$HOME/.5qln/codex.txt")" -eq 9 ]'
check "Codex is 217 bytes" '[ "$(wc -c < "$HOME/.5qln/codex.txt")" -eq 217 ]'
check "Codex contains U+22C2 (⋂) on line 5" 'grep -q "⋂" "$HOME/.5qln/codex.txt"'

# ══════════════════════════════════════════
# L1: KERNEL
# ══════════════════════════════════════════
header "L1: Kernel"

check "Kernel file exists" '[ -f "$HOME/.5qln/init.py" ]'
check "Kernel is executable" '[ -x "$HOME/.5qln/init.py" ]'
check "Kernel verify passes" 'python3 "$HOME/.5qln/init.py" verify 2>&1 | python3 -c "import json,sys; d=json.load(sys.stdin); exit(0 if d.get(\"verified\") else 1)"'
check "Kernel status returns S phase" 'python3 "$HOME/.5qln/init.py" status 2>&1 | grep -q "S"'

# ══════════════════════════════════════════
# L3: WORKSPACE DEFAULTS
# ══════════════════════════════════════════
header "L3: Workspace"

check "AGENTS.md exists" '[ -f "/home/workspace/AGENTS.md" ]'
check "AGENTS.md contains Codex hash" 'grep -q "feaa46b4" /home/workspace/AGENTS.md'
check "SOUL.md exists" '[ -f "/home/workspace/SOUL.md" ]'

# ══════════════════════════════════════════
# L4: CORE SKILLS
# ══════════════════════════════════════════
header "L4: Core Skills"

check "5qln-orchestrate exists" '[ -d "/home/workspace/Skills/5qln-orchestrate" ]'
check "5qln-open-template-stack exists" '[ -d "/home/workspace/Skills/5qln-open-template-stack" ]'
check "5qln-corruption-codex exists" '[ -d "/home/workspace/Skills/5qln-corruption-codex" ]'
check "5qln-project-space exists" '[ -d "/home/workspace/Skills/5qln-project-space" ]'

# Evolution pipeline (optional)
for skill in 5qln-alpha-library 5qln-skill-evolve 5qln-skill-refine; do
    if [ -d "/home/workspace/Skills/$skill" ]; then
        echo -e "  ${GREEN}[PASS]${NC} $skill exists"
        ((PASS++))
    else
        echo -e "  ${RED}[FAIL]${NC} $skill exists (OPTIONAL — full mode only)"
    fi
done

# ══════════════════════════════════════════
# L5: RUNTIME
# ══════════════════════════════════════════
header "L5: Runtime"

check "Events directory exists" '[ -d "/home/workspace/5qln-journal/events" ]'
check "Events directory writable" '[ -w "/home/workspace/5qln-journal/events" ]'
check "Evolution directory exists" '[ -d "/home/workspace/5qln-evolution" ]'
check "Candidates file exists" '[ -f "/home/workspace/5qln-evolution/candidates.json" ]'
check "Alpha library directory exists" '[ -d "/home/workspace/5qln-alpha-library" ]'

# ══════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "  ${GREEN}PASSED: $PASS${NC}"
if [ $FAIL -gt 0 ]; then
    echo -e "  ${RED}FAILED: $FAIL${NC}"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $FAIL -gt 0 ]; then
    echo ""
    echo "Some checks failed. Review above and re-run bootstrap.sh for the failed layer."
    exit 1
fi

echo ""
echo "All integrity checks passed. 5QLN is running clean."
exit 0
