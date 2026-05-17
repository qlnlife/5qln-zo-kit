#!/usr/bin/env python3
"""
5QLN Orchestrator — Session Start Script

Usage:
    python3 orchestrate.py BEGIN          Start a new 5QLN session
    python3 orchestrate.py <domain>       Route to specific domain
    python3 orchestrate.py status         Show current state

The script reads the conversation (via stdin or last journal entry) to detect
domain signals, then prints the activation sequence for the orchestrating agent.
"""

import sys
import os
from pathlib import Path

SKILLS_DIR = Path("/home/workspace/Skills")
JOURNAL_DIR = Path("/home/workspace/5qln-journal")

DOMAINS = {
    "commercialize": {
        "root": "5qln-commercialize",
        "signals": ["commercial", "market", "pricing", "license", "revenue",
                    "GTM", "users", "business", "monetize", "sell", "product"],
    },
    "research": {
        "root": "5qln-research",
        "signals": ["research", "philosophy", "framework", "history",
                    "academic", "understand", "validate", "explore", "deeper"],
    },
    "selfimprove": {
        "root": "5qln-selfimprove",
        "signals": ["personal", "creative", "practice", "growth", "develop",
                    "block", "craft", "improve", "evolve", "become"],
    },
    "skillgen": {
        "root": "5qln-skillgen",
        "signals": ["build", "create", "skill", "new domain", "extend",
                    "generate", "design", "make", "construct"],
    },
}

PHASES = ["S", "G", "Q", "P", "V"]

def detect_domain(text: str) -> str:
    """Detect which domain the conversation context suggests."""
    text = text.lower()
    scores = {}
    for domain, config in DOMAINS.items():
        score = sum(1 for sig in config["signals"] if sig in text)
        scores[domain] = score
    if max(scores.values()) == 0:
        return "research"  # default
    return max(scores, key=scores.get)

def get_last_journal_entry() -> str:
    """Read the most recent journal entry for context."""
    entries_dir = JOURNAL_DIR / "entries"
    if not entries_dir.exists():
        return ""
    entries = sorted(entries_dir.glob("*.md"), reverse=True)
    if entries:
        return entries[0].read_text()
    return ""

def read_last_user_message() -> str:
    """Read the last user message from conversation workspace."""
    conv_ws = Path("/home/.z/workspaces/con_yEDyhF86qHtECUpM")
    if not conv_ws.exists():
        return ""
    # Try to find a recent user message file
    messages = sorted(conv_ws.glob("*.json"), reverse=True)
    for msg_file in messages[:3]:
        try:
            content = msg_file.read_text()
            if '"role":"user"' in content or '"role": "user"' in content:
                return content
        except Exception:
            continue
    return ""

def build_activation(domain: str) -> str:
    """Build the full activation sequence for a domain."""
    root = DOMAINS[domain]["root"]
    root_path = SKILLS_DIR / root

    lines = [
        f"━━━ 5QLN ORCHESTRATION ━━━",
        f"Domain:     {domain}",
        f"Root skill: {root}",
        f"Path:       {root_path}",
        f"",
        f"ACTIVATION SEQUENCE:",
    ]

    for i, phase in enumerate(PHASES):
        skill_file = root_path / f"{phase}-SKILL.md"
        exists = "✓" if skill_file.exists() else "✗"
        next_phase = PHASES[i + 1] if i < len(PHASES) - 1 else "∞0'"
        lines.append(f"  [{i+1}] {phase} → {skill_file.name}  {exists}  (next: {next_phase})")

    lines.extend([
        "",
        "CONSTITUTIONAL REMINDER:",
        "  H = ∞0 | A = K",
        "  The orchestrator routes. It does not run the phases.",
        "  Each phase skill runs itself.",
        "",
        "NEXT ACTION:",
        f"  Read: {root_path / 'SKILL.md'}",
        f"  Then: Read {root_path / 'S-SKILL.md'} and begin Phase S",
        "━━━━━━━━━━━━━━━━━━━",
    ])

    return "\n".join(lines)

def cmd_begin():
    """BEGIN command — detect domain and print activation."""
    # Gather context
    journal_text = get_last_journal_entry()
    conv_text = read_last_user_message()
    context = journal_text + " " + conv_text

    if not context.strip():
        print("No session context found. Defaulting to 'research'.")
        domain = "research"
    else:
        domain = detect_domain(context)
        print(f"Context detected. Domain: {domain}")

    print()
    print(build_activation(domain))

def cmd_status():
    """STATUS command — show what phase skills exist."""
    print("━━━ 5QLN SKILL STATUS ━━━")
    for domain in DOMAINS:
        root = DOMAINS[domain]["root"]
        root_path = SKILLS_DIR / root
        root_exists = (root_path / "SKILL.md").exists()
        phase_count = sum(
            1 for p in PHASES
            if (root_path / f"{p}-SKILL.md").exists()
        )
        status = "✓" if root_exists else "✗"
        print(f"  [{status}] {domain:<15} {phase_count}/5 phases  ({root})")
    print()

def cmd_route(domain: str):
    """Route to a specific domain."""
    if domain not in DOMAINS:
        print(f"Unknown domain: {domain}")
        print(f"Available: {', '.join(DOMAINS.keys())}")
        sys.exit(1)
    print(build_activation(domain))

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        cmd_status()
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "begin":
        cmd_begin()
    elif cmd == "status":
        cmd_status()
    elif cmd in DOMAINS:
        cmd_route(cmd)
    else:
        print(f"Unknown command: {cmd}")
        cmd_status()
        sys.exit(1)

if __name__ == "__main__":
    main()
