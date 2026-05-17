# 5QLN Boot — Architecture Reference

> Fratal Init: A 5QLN workspace bootstrap that IS a 5QLN cycle.

## Layer Architecture

```
╔══════════════════════════════════════════════╗
║ L0: CODEX (immutable, fetched, verified)     ║
║     ~/.5qln/codex.txt                        ║
║     SHA-256: feaa46b4...                     ║
║     9 lines, 217 bytes                       ║
║     Authoritative source: foundation repo    ║
║     Never self-modifies. Ground of truth.    ║
╠══════════════════════════════════════════════╣
║ L1: KERNEL (self-verifying, frozen)          ║
║     ~/.5qln/init.py v4.0.1                   ║
║     Dual-hash: codex + normalized (self)     ║
║     Five phases, state machine, events       ║
║     State: ~/.5qln_kernel_state.json         ║
║     Replaceable only by explicit re-init     ║
╠══════════════════════════════════════════════╣
║ L2: ACTIVATION (persona + rule)              ║
║     Persona: "5qln" — Codex alignment        ║
║     Rule: session_start → init.py status      ║
║     Fires every session, no user action      ║
║     Zo-managed (not filesystem)              ║
╠══════════════════════════════════════════════╣
║ L3: INITIATION (workspace defaults)          ║
║     AGENTS.md, SOUL.md                       ║
║     Template → personalized by setup cycle   ║
║     AGENTS.md IS the V-phase B''             ║
║     Can evolve through user edits            ║
╠══════════════════════════════════════════════╣
║ L4: CORE SKILLS (bundled, evolvable)          ║
║     5qln-orchestrate, 5qln-project-*         ║
║     5qln-corruption-codex                    ║
║     5qln-constitutional-block-validator      ║
║     + evolution pipeline (full mode)         ║
╠══════════════════════════════════════════════╣
║ L5: RUNTIME (accumulating, feeding back)     ║
║     5qln-journal/events/stream.jsonl         ║
║     5qln-alpha-library/library.json          ║
║     5qln-evolution/candidates.json           ║
║     Grows every session, feeds evolution     ║
╚══════════════════════════════════════════════╝
```

## Fratal Property

The setup IS a cycle. What it produces can run cycles. Those cycles
can improve the setup. This is the self-reference:

```
SETUP CYCLE (S→V) → workspace with core skills → user cycles →
skill-evolve surfaces candidates → human gates → skill-refine applies →
skills improve → enough drift → re-init cycle → SETUP CYCLE (again)
```

The only hard boundary is L0 (Codex). It never changes.
L1 can be re-initialized. L2-L5 evolve continuously.

## Setup Flow (S→G→Q→P→V)

### S: RECEIVE
- Human names themselves (H)
- Human names founding question (X)
- AI DOES NOT suggest the question (L2 protection)

### G: ILLUMINATE
- AI presents three setup modes: minimal, standard, full
- AI lists relevant core skills for each mode
- AI shows AGENTS.md/SOUL.md templates
- AI DOES NOT recommend (L1 protection)

### Q: RESONATE
- AI asks: "Does a particular mode feel right?"
- Human feels resonance. AI does not claim it (L3 protection).
- Silence is data. Don't fill it (L4 protection).

### P: FLOW
- Execute bootstrap.sh for filesystem components
- Create persona and rule via Zo tools
- Copy core skills to workspace
- Each file written = δE/δV → ∇

### V: CRYSTALLIZE
- Run verify-all.sh
- Confirm AGENTS.md is personalized correctly
- Open ∞0': "What question does this open for you?"
- "Nothing" is valid ∞0' — record it
- No V without ∞0' (V∅ protection)

## Setup Modes

| Mode | L0 | L1 | L2 | L3 | L4 | L5 |
|------|----|----|----|----|----|-----|
| minimal | ✓ | ✓ | ✓ |   |   |   |
| standard | ✓ | ✓ | ✓ | ✓ | ✓ (core) |   |
| full | ✓ | ✓ | ✓ | ✓ | ✓ (all) | ✓ |

## Integrity Verification

Every layer has its own verification:

| Layer | Verification |
|-------|-------------|
| L0 | SHA-256 against `feaa46b4...`. Line count (9). Byte count (217). U+22C2 check. |
| L1 | `init.py verify` — dual hash against Codex and normalized self. |
| L2 | Persona prompt contains `feaa46b4`. Rule fires on session_start. |
| L3 | AGENTS.md contains Codex hash. SOUL.md exists. |
| L4 | Core skill directories exist with SKILL.md files. |
| L5 | Directories exist and are writable. |

`verify-all.sh` runs all checks. Exits 0 only if all pass.

## Evolution Pipeline

```
stream.jsonl → skill-evolve:surface → candidates.json → HUMAN GATE →
skill-refine:apply → updated SKILL.md → α-library:ingest → library.json
```

Evolution candidates carry:
- `epistemic_register`: STRUCTURAL-HYPOTHESIS, LEGAL-PROSPECTIVE, or PHENOMENOLOGICAL-ASSERTION
- `confidence`: 0.0 to 1.0
- `proposed_change`: human-readable description
- `reasoning`: why the data supports this change

## Re-init Triggers

A re-init cycle should be considered when:
1. Kernel version is N+2 behind foundation repo
2. Enough skills have evolved that AGENTS.md routing is stale
3. Accumulated α-library entries suggest a different setup mode
4. Human explicitly requests re-init

Re-init does NOT touch L0. It always verifies the same Codex.

## File Map

```
Skills/5qln-boot/
├── SKILL.md                          ← Master instruction
├── scripts/
│   ├── bootstrap.sh                  ← Filesystem installer
│   └── verify-all.sh                 ← Integrity check
├── assets/
│   ├── codex.txt                     ← Foundation Codex (bundled)
│   ├── init.py                       ← Kernel v4.0.1 (bundled)
│   ├── persona-prompt.md             ← For create_persona
│   ├── AGENTS.md.template            ← Workspace default
│   └── SOUL.md.template              ← Soul default
└── references/
    └── ARCHITECTURE.md               ← This file
```

## Runtime (post-boot)

```
/home/workspace/
├── AGENTS.md                         ← V-phase B'' of setup cycle
├── SOUL.md                           ← Soul (personalized)
├── Skills/
│   ├── 5qln-boot/                    ← This skill (reference)
│   ├── 5qln-orchestrate/             ← Session routing
│   ├── 5qln-open-template-stack/     ← Template stack
│   ├── 5qln-project-space/           ← Project space
│   ├── 5qln-corruption-codex/        ← Corruption reference
│   ├── 5qln-constitutional-block-validator/ ← Block validation
│   ├── 5qln-alpha-library/           ← Pattern store
│   ├── 5qln-skill-evolve/            ← Evolution surfacer
│   └── 5qln-skill-refine/            ← Evolution applier
├── 5qln-journal/
│   └── events/
│       └── stream.jsonl              ← Events accumulate here
├── 5qln-evolution/
│   └── candidates.json              ← Surfaced candidates
└── 5qln-alpha-library/
    └── library.json                  ← Cross-cycle patterns

~/.5qln/
├── codex.txt                         ← Foundation Codex (immutable)
└── init.py                           ← Kernel (self-verifying)
```

---

*5QLN Boot — The setup IS a 5QLN cycle.*
