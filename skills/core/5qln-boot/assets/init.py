#!/usr/bin/env python3
"""
5QLN Init — Bootstrap the constitutional grammar kernel from a single file.

Usage:
  python3 ~/.5qln/init.py                        # Interactive session
  python3 ~/.5qln/init.py status                 # Show current phase
  python3 ~/.5qln/init.py verify                 # Verify Codex integrity
  python3 ~/.5qln/init.py help                   # Show commands

This file IS the distributable. It self-verifies against the Codex.
It saves itself to ~/.5qln/init.py on first run.
No dependencies beyond Python 3.

THE CODEX — Nine Invariant Lines — is byte-identical to the foundation canonical.
Canonical source: https://raw.githubusercontent.com/qlnlife/5qln-foundation/main/codex/codex.txt
SHA-256: feaa46b4147d4e023cdd3fd59c051d063e8ec654ee7b38a481dcd5e4c781859b
"""

import json
import os
import sys
import fcntl
import hashlib
import re
import shutil
from pathlib import Path
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════════════════
# THE CODEX — 9 Invariant Lines, 217 bytes, byte-identical to foundation.
# Verified at every boot against canonical hash.
# ═══════════════════════════════════════════════════════════════════

CODEX_BYTES = (
    "1.  H = \u221e0 | A = K\n"
    "2.  S \u2192 G \u2192 Q \u2192 P \u2192 V\n"
    "3.  S = \u221e0 \u2192 ?\n"
    "4.  G = \u03b1 \u2261 {\u03b1'}\n"
    "5.  Q = \u03c6 \u22c2 \u03a9\n"
    "6.  P = \u03b4E/\u03b4V \u2192 \u2207\n"
    "7.  V = (L \u2229 G \u2192 B'') \u2192 \u221e0'\n"
    "8.  No V without \u221e0'\n"
    "9.  L1  L2  L3  L4  V\u2205\n"
)

CODEX_LINES = CODEX_BYTES.rstrip("\n").split("\n")

CANONICAL_CODEX_HASH = "feaa46b4147d4e023cdd3fd59c051d063e8ec654ee7b38a481dcd5e4c781859b"
CANONICAL_NORMALIZED_HASH = "24b7e65f767e10c780af81c88b10dd43ee94620716dd741009e845c97f6ddc6c"

# ═══════════════════════════════════════════════════════════════════
# BOOTSTRAP — Self-install on first run
# ═══════════════════════════════════════════════════════════════════

def bootstrap():
    kernel_path = Path.home() / ".5qln" / "init.py"

    if kernel_path.exists():
        if __file__ and Path(__file__).resolve() != kernel_path.resolve():
            if Path(__file__).stat().st_mtime > kernel_path.stat().st_mtime:
                shutil.copy(__file__, kernel_path)
                kernel_path.chmod(0o755)
                print("  [Updated: ~/.5qln/init.py]")
        return False

    kernel_path.parent.mkdir(parents=True, exist_ok=True)

    if __file__ and Path(__file__).exists():
        src = Path(__file__)
        if src.resolve() != kernel_path.resolve():
            shutil.copy(src, kernel_path)
            kernel_path.chmod(0o755)
            print("┌──────────────────────────────────────────────────────┐")
            print("│  5QLN Kernel installed to ~/.5qln/init.py           │")
            print("│  Codex: feaa46b4 (foundation canonical)              │")
            print("│  Relaunching from installed path...                  │")
            print("└──────────────────────────────────────────────────────┘")
            os.execv(sys.executable, [sys.executable, str(kernel_path)] + sys.argv[1:])
            return True
    else:
        print("┌──────────────────────────────────────────────────────┐")
        print("│  5QLN Kernel — save first, then run:                │")
        print("│    curl -sL " + DISTRIBUTABLE_URL + "              │")
        print("│      -o ~/.5qln/init.py                             │")
        print("│    python3 ~/.5qln/init.py                           │")
        print("└──────────────────────────────────────────────────────┘")
        sys.exit(0)

    return False


# ═══════════════════════════════════════════════════════════════════
# CODEX VERIFICATION — dual-hash integrity
# ═══════════════════════════════════════════════════════════════════

def verify_codex_integrity():
    """Hash the Codex bytes against canonical. Also file-integrity check
    via NORMALIZED_HASH (the file minus its own NORMALIZED_HASH)."""
    # Codex check
    codex_computed = hashlib.sha256(CODEX_BYTES.encode()).hexdigest()
    if codex_computed != CANONICAL_CODEX_HASH:
        print("┌──────────────────────────────────────────────────────┐")
        print("│  ❌ CODEX CORRUPTED                                 │")
        print(f"│  Expected: {CANONICAL_CODEX_HASH}                   │")
        print(f"│  Got:      {codex_computed}                   │")
        print("│  This kernel is not constitutional. Refusing to run. │")
        print("└──────────────────────────────────────────────────────┘")
        sys.exit(1)

    # File integrity check (normalized — file minus its own hash)
    if __file__ and Path(__file__).exists():
        raw = Path(__file__).read_text()
        current = re.search(r'CANONICAL_NORMALIZED_HASH = "([a-f0-9]{64})"', raw)
        if current:
            normalized = raw.replace(current.group(1), "0" * 64)
            computed_norm = hashlib.sha256(normalized.encode()).hexdigest()
            if computed_norm != CANONICAL_NORMALIZED_HASH:
                print("┌──────────────────────────────────────────────────────┐")
                print("│  ❌ NORMALIZED INTEGRITY FAILED                     │")
                print(f"│  Expected: {CANONICAL_NORMALIZED_HASH}              │")
                print(f"│  Got:      {computed_norm}              │")
                print("│  This file has been modified. Refusing to run.       │")
                print("└──────────────────────────────────────────────────────┘")
                sys.exit(1)

    return True


# ═══════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════

PHASES = ["S", "G", "Q", "P", "V"]
OUTPUTS = {"S": "X", "G": "Y", "Q": "Z", "P": "A", "V": "B"}
EQUATIONS = {
    "S": "\u221e0 \u2192 ?",
    "G": "\u03b1 \u2261 {\u03b1'}",
    "Q": "\u03c6 \u22c2 \u03a9",
    "P": "\u03b4E/\u03b4V \u2192 \u2207",
    "V": "(L \u2229 G \u2192 B'') \u2192 \u221e0'",
}
CORRUPTION_NAMES = {
    "L1": "Closing",
    "L2": "Generating",
    "L3": "Claiming",
    "L4": "Performing",
    "V\u2205": "Incomplete",
}
RECOVERY = {
    "L1": "What question is actually wanting to be asked — not answered?",
    "L2": "What pattern are you recognizing? I illuminate from K, the seeing is yours.",
    "L3": "I am K. The Unknown reveals itself through you, not to me.",
    "L4": "Where does energy actually want to go — not where should it go?",
    "V\u2205": "What question does this open for next time?",
}

STATE_DIR = Path.home() / ".5qln"
STATE_FILE = STATE_DIR / "state.json"
JOURNAL_FILE = STATE_DIR / "journal.jsonl"
LOCK_FILE = STATE_DIR / "kernel.lock"
RESIDUE_DIR = STATE_DIR / "residues"

VERSION = "4.0.1"
DISTRIBUTABLE_URL = "https://raw.githubusercontent.com/qlnlife/5qln-core/master/init.py"


# ═══════════════════════════════════════════════════════════════════
# FILE LOCKING
# ═══════════════════════════════════════════════════════════════════

def lock():
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    lf = open(LOCK_FILE, "w")
    fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
    return lf

def unlock(lf):
    fcntl.flock(lf.fileno(), fcntl.LOCK_UN)
    lf.close()


# ═══════════════════════════════════════════════════════════════════
# STATE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════

def fresh_state():
    return {
        "version": 4,
        "phase": "S",
        "cycle_count": 1,
        "sub_phase": None,
        "outputs": {o: None for o in OUTPUTS.values()},
        "decode": {o: {} for o in OUTPUTS.values()},
        "cycle_trace": {},
        "formation_trail": [],
        "input_history": [],
        "corruption": [],
        "corruption_history": [],
        "session_id": None,
        "inputs_this_cycle": 0,
        "codex_hash": CANONICAL_CODEX_HASH,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

def load():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            state = json.load(f)
        stored = state.get("codex_hash", "")
        if stored != CANONICAL_CODEX_HASH:
            print("ERROR: Codex hash mismatch. State from different Codex version.", file=sys.stderr)
            print(f"  Stored: {stored[:16]}...", file=sys.stderr)
            print(f"  Canonical: {CANONICAL_CODEX_HASH[:16]}...", file=sys.stderr)
        return state
    return fresh_state()

def save(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def journal(event_type, data):
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event_type,
        **data,
    }
    with open(JOURNAL_FILE, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ═══════════════════════════════════════════════════════════════════
# CORRUPTION DETECTION
# ═══════════════════════════════════════════════════════════════════

def check_corruption(state):
    errors = []
    phase = state["phase"]
    inputs = state.get("inputs_this_cycle", 0)
    trail = state.get("formation_trail", [])

    if phase == "S" and inputs >= 1:
        errors.append("L1")
    if phase == "V" and trail and not state["outputs"].get("B"):
        errors.append("V\u2205")
    return errors


# ═══════════════════════════════════════════════════════════════════
# PHASE-THEMED PROMPTS
# ═══════════════════════════════════════════════════════════════════

PHASE_PROMPTS = {
    "S": "\n  \u2b21 S [\u221e0 \u2192 ?]  —  What question brings you here?\n  ",
    "G": "\n  \u2b21 G [\u03b1 \u2261 {\u03b1'}]  —  What pattern do you see?\n  ",
    "Q": "\n  \u2b21 Q [\u03c6 \u22c2 \u03a9]  —  Does this resonate?\n  ",
    "P": "\n  \u2b21 P [\u03b4E/\u03b4V \u2192 \u2207]  —  Where does energy want to go?\n  ",
    "V": "\n  \u2b21 V [(L \u2229 G \u2192 B'') \u2192 \u221e0']  —  What crystallized?\n  ",
}


# ═══════════════════════════════════════════════════════════════════
# COMMANDS
# ═══════════════════════════════════════════════════════════════════

def cmd_init(args, state):
    sid = args[0] if args else "session"
    state["session_id"] = sid
    state["codex_hash"] = CANONICAL_CODEX_HASH
    save(state)
    journal("init", {"session_id": sid, "codex_hash": CANONICAL_CODEX_HASH[:12]})
    print(json.dumps({"ok": True, "session_id": sid, "codex_hash": CANONICAL_CODEX_HASH[:12]}))

def cmd_capture(args, state):
    if not args:
        print("ERROR: capture requires <content>", file=sys.stderr)
        return
    content = " ".join(args)
    phase = state["phase"]
    out_sym = OUTPUTS[phase]

    state["outputs"][out_sym] = content
    decode = {"raw": content}
    state["decode"][out_sym] = decode

    trace_map = {"S": "X", "G": "alpha", "Q": "phi", "P": "nabla", "V": "B2"}
    state["cycle_trace"][trace_map.get(phase, out_sym)] = content

    state["formation_trail"].append({
        "phase": phase,
        "sub_phase": state.get("sub_phase"),
        "input": content,
        "decode": decode,
    })
    state["input_history"].append({
        "phase": phase,
        "content": content,
        "decode": decode,
        "cycle": state["cycle_count"],
    })
    state["inputs_this_cycle"] = state.get("inputs_this_cycle", 0) + 1
    state["corruption"] = check_corruption(state)
    save(state)
    journal("capture", {"phase": phase, "content": content[:200], "cycle": state["cycle_count"]})

def cmd_transition(args, state):
    if not args or args[0] not in PHASES:
        print(f"ERROR: transition requires one of {PHASES}", file=sys.stderr)
        return
    new_phase = args[0]
    old_phase = state["phase"]
    journal("transition", {"from": old_phase, "to": new_phase, "cycle": state["cycle_count"]})
    state["phase"] = new_phase
    state["sub_phase"] = None
    state["inputs_this_cycle"] = 0
    state["corruption"] = check_corruption(state)
    save(state)
    print(f"  → {new_phase} [{EQUATIONS[new_phase]}]")

def cmd_crystallize(args, state):
    if not args:
        print("ERROR: crystallize requires <seed>", file=sys.stderr)
        return
    seed = " ".join(args)
    state["outputs"]["B"] = seed
    state["decode"]["B"] = {"B2": seed, "raw": seed}
    state["cycle_trace"]["B2"] = seed
    journal("crystallize", {"B2": seed, "cycle": state["cycle_count"]})
    save(state)
    print(f"  B'' = ⟨{seed}⟩")

def cmd_return(args, state):
    prev_out = {k: v for k, v in state["outputs"].items() if v}
    prev_corruption = list(state["corruption"])
    prev_trace = dict(state["cycle_trace"])

    journal("cycle_complete", {
        "cycle": state["cycle_count"],
        "outputs": prev_out,
        "trace": prev_trace,
        "corruption": prev_corruption,
    })

    state["cycle_count"] += 1
    for o in OUTPUTS.values():
        state["outputs"][o] = None
        state["decode"][o] = {}
    state["cycle_trace"] = {}
    state["formation_trail"] = []
    state["corruption"] = []
    state["phase"] = "S"
    state["sub_phase"] = None
    state["inputs_this_cycle"] = 0

    RESIDUE_DIR.mkdir(parents=True, exist_ok=True)
    completed = state["cycle_count"] - 1
    residue_path = RESIDUE_DIR / f"residue-{completed:04d}.json"
    tmp_path = RESIDUE_DIR / f".residue-{completed:04d}.tmp"
    tmp_path.write_text(json.dumps({
        "cycle": completed,
        "session_id": state.get("session_id", ""),
        "phase": "V",
        "outputs": prev_out,
        "trace": prev_trace,
        "corruption": prev_corruption,
        "completed_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2, ensure_ascii=False))
    tmp_path.rename(residue_path)

    save(state)
    B = prev_out.get("B", "")
    print(f"  Cycle {completed} complete. ∞0′ opens cycle {state['cycle_count']}.")
    if B:
        print(f"  B″ = ⟨{B}⟩")

def cmd_status(args, state):
    print(_format(state))

def cmd_journal(args, state):
    if not JOURNAL_FILE.exists():
        print("No cycles recorded.")
        return
    limit = int(args[0]) if args else 20
    with open(JOURNAL_FILE) as f:
        lines = f.readlines()
    for line in lines[-limit:]:
        print(line.rstrip())

def cmd_verify(args, state):
    current = hashlib.sha256(CODEX_BYTES.encode()).hexdigest()
    match = current == CANONICAL_CODEX_HASH == state.get("codex_hash", "")
    print(json.dumps({
        "ok": match,
        "verified": match,
        "codex_hash": CANONICAL_CODEX_HASH,
        "nine_lines_present": len(CODEX_LINES) == 9,
        "byte_count": len(CODEX_BYTES.encode()),
        "version": VERSION,
    }))

def cmd_help(args, state):
    print(f"""
5QLN Kernel v{VERSION}
Foundation Codex: {CANONICAL_CODEX_HASH[:16]}...  (9 lines, 217 bytes)

Interactive session:
  python3 {Path.home()}/.5qln/init.py

Commands:
  python3 {Path.home()}/.5qln/init.py status     Show current phase and outputs
  python3 {Path.home()}/.5qln/init.py journal [N] Show last N journal entries
  python3 {Path.home()}/.5qln/init.py verify      Verify Codex integrity
  python3 {Path.home()}/.5qln/init.py help        This message

Phase transitions (during interactive session):
  :G    Transition to G-phase
  :Q    Transition to Q-phase
  :P    Transition to P-phase
  :V    Transition to V-phase
  :crystal <text>  Crystallize B''
  :return          Complete cycle, return to S
  :status          Show state
  :quit            Exit
  Ctrl+D           Exit

Distributable URL: {DISTRIBUTABLE_URL}
Journal: {JOURNAL_FILE}
""")


# ═══════════════════════════════════════════════════════════════════
# FORMATTED OUTPUT
# ═══════════════════════════════════════════════════════════════════

def _load_chain_context():
    if not RESIDUE_DIR.exists():
        return None

    residues = sorted(RESIDUE_DIR.glob("residue-*.json"))
    if not residues:
        return None

    chain = []
    for rpath in residues:
        try:
            r = json.loads(rpath.read_text())
            chain.append(r)
        except (json.JSONDecodeError, KeyError):
            continue

    if not chain:
        return None

    latest = chain[-1]
    return {
        "total_cycles": len(chain),
        "latest_cycle": latest.get("cycle", "?"),
        "return_question": latest.get("return_question", "") or latest.get("trace", {}).get("B2", latest.get("outputs", {}).get("B", "")),
        "b2": latest.get("trace", {}).get("B2", latest.get("outputs", {}).get("B", "")),
        "completed_at": latest.get("completed_at", ""),
        "corruption": latest.get("corruption", []),
        "alpha": latest.get("trace", {}).get("alpha", ""),
        "x": latest.get("trace", {}).get("X", latest.get("outputs", {}).get("X", "")),
    }

def _format_chain_banner(chain, state):
    if not chain:
        return ""

    lines = []
    lines.append("\u250c\u2500 SESSION CHAIN \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
    lines.append(f"\u2502  {chain['total_cycles']} cycles recorded \u00b7 last: cycle {chain['latest_cycle']} at {chain['completed_at'][:10]}       \u2502")

    if chain["x"]:
        lines.append(f"\u2502  X: {chain['x'][:45]:45s} \u2502")
    if chain["alpha"]:
        lines.append(f"\u2502  \u03b1: {chain['alpha'][:45]:45s} \u2502")
    if chain["b2"]:
        lines.append(f"\u2502  B'': {chain['b2'][:45]:45s} \u2502")

    if chain["return_question"]:
        lines.append(f"\u2502                                                          \u2502")
        lines.append(f"\u2502  \u221e0' = \"{chain['return_question']}\"")
        lines.append(f"\u2502                                                          \u2502")

    if chain["corruption"]:
        lines.append(f"\u2502  \u26a0 corruption this cycle: {', '.join(chain['corruption'])}")

    lines.append("\u2514" + "\u2500" * 58 + "\u2518")
    return "\n".join(lines)

def _format(state):
    p = state["phase"]
    outs = state["outputs"]
    cor = state["corruption"]
    tag = state["sub_phase"] or p
    ic = sum(1 for h in state["input_history"] if h.get("cycle") == state["cycle_count"])

    w = 54
    br = "\u2500" * w
    lines = [
        f"  {br}",
        f'  \u2b21 {tag}  [{EQUATIONS.get(p, "")}]',
        f'  cycle {state["cycle_count"]} \u00b7 {ic} inputs \u00b7 center: {"open" if not cor else "FILLED"}',
        f"  {br}",
    ]

    for phase, sym in OUTPUTS.items():
        val = outs.get(sym)
        if not val:
            continue
        if phase == "S":
            lines.append(f'      X  = "{val}"')
        elif phase == "G":
            lines.append(f'      Y  = "{val}"')
        elif phase == "Q":
            lines.append(f'      Z  = "{val}"')
        elif phase == "P":
            lines.append(f'      A  = "{val}"')
        elif phase == "V":
            lines.append(f'      B  = "{val}"')

    if cor:
        names = [f"{c} ({CORRUPTION_NAMES.get(c, '')})" for c in cor]
        lines.append(f'  corruption: {", ".join(names)}')
    else:
        lines.append("  corruption: none")

    lines.append(f"  {br}")
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════
# COMMAND ROUTER
# ═══════════════════════════════════════════════════════════════════

COMMANDS = {
    "init": cmd_init,
    "capture": cmd_capture,
    "transition": cmd_transition,
    "crystallize": cmd_crystallize,
    "return": cmd_return,
    "status": cmd_status,
    "journal": cmd_journal,
    "verify": cmd_verify,
    "help": cmd_help,
}

def main():
    bootstrap()
    verify_codex_integrity()

    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    args = list(sys.argv[2:])

    if cmd not in COMMANDS:
        print(f"ERROR: unknown command '{cmd}'", file=sys.stderr)
        cmd_help([], None)
        sys.exit(1)

    lf = lock()
    try:
        state = load()
        COMMANDS[cmd](args, state)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        unlock(lf)


if __name__ == "__main__":
    main()
