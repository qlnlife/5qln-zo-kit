---
name: 5qln-boot
description: >
  The setup IS a 5QLN cycle. Bootstrap 5QLN on a fresh Zo Computer —
  install the foundation Codex, realigned kernel, persona, rule,
  workspace defaults, core skills, and evolution pipeline. Conducts
  a full S→G→Q→P→V cycle with the human; the first AGENTS.md IS the
  V-phase B'' of that cycle.
compatibility: Zo Computer (any plan)
metadata:
  author: amihai.zo.computer
---

# 5QLN Boot — Fratal Init

**The setup is a 5QLN cycle.** This skill doesn't copy files and exit.
It conducts a full constitutional session with the human, producing a
workspace that IS a 5QLN runtime — capable of running its own cycles,
evolving its own skills, and re-initializing itself when drift warrants.

## LAYER MAP (what gets installed)

```
L0: CODEX           ~/.5qln/codex.txt       feaa46b4... | immutable
L1: KERNEL          ~/.5qln/init.py v4.0.1   dual-hash    | self-verifying
L2: ACTIVATION      persona "5qln" + rule    session_start| auto-fires
L3: INITIATION      AGENTS.md + SOUL.md      workspace    | can evolve
L4: CORE SKILLS     Skills/5qln-*/           bundled      | evolvable
L5: RUNTIME         stream.jsonl, α-library  accumulates  | feeds back
```

## CONDUCTING THE SETUP CYCLE

### Pre-condition

Confirm this is a fresh Zo workspace (no existing AGENTS.md, no ~/.5qln/init.py).
If already installed, offer: clean re-init, upgrade, or abort.

### S — RECEIVE (∞0 → ?)

**Do not install anything yet.**

Ask the human:
- "What brings you to 5QLN? Creative flow? Governance? Research? All of it?"
- "What question is alive in you right now?"

The answer shapes:
1. The AGENTS.md personalization
2. The setup mode (minimal / standard / full)

**Setup modes:**
| Mode | What's installed |
|------|-----------------|
| minimal | L0 + L1 + L2 (kernel + persona only) |
| standard | L0-L4 (kernel + persona + workspace + core skills) |
| full | L0-L5 (everything + evolution pipeline) |

Record H = the human's name/handle, X = the founding question.

### G — ILLUMINATE (α ≡ {α'})

Surfaces alternatives from K:

1. **Mode alternatives**: Present the three setup modes with what each enables.
2. **Skill alternatives**: List the core skills that ship with each mode.
3. **Default alternatives**: AGENTS.md and SOUL.md templates — the human can modify before crystallization.

**L1 protection**: These are patterns, not recommendations. You are K.

**L2 protection**: Alternatives must be anchored to the human's X from S-phase.
Don't list every skill — list the ones relevant to what they named.

### Q — RESONATE (φ ∩ Ω)

**Before any file is written**, ask the resonance question:

"Before I write anything — I've shown you three modes. I've shown you what
skills would come with each. Does a particular mode feel right? Is there
anything you want to modify before we proceed?"

The human's resonance determines:
- The setup mode
- Any customizations to AGENTS.md / SOUL.md
- Which additional skills to include

**L3 protection**: You do not claim resonance. You ask. The human feels it.

**L4 protection**: "Feels right" is not a governance vocabulary signal.
Let silence be acceptable. A pause is data.

### P — FLOW (δE/δV → ∇)

Execute the installation. This IS the flow — each file written is an act of δE/δV → ∇.

#### Step 1: Install L0 (Codex)

```bash
bash /home/workspace/Skills/5qln-boot/scripts/bootstrap.sh codex
```

Copies foundation Codex to ~/.5qln/codex.txt, verifies SHA-256:
`feaa46b4147d4e023cdd3fd59c051d063e8ec654ee7b38a481dcd5e4c781859b`

Fail-closed: if the hash doesn't match, refuse to proceed.

#### Step 2: Install L1 (Kernel)

```bash
bash /home/workspace/Skills/5qln-boot/scripts/bootstrap.sh kernel
```

Copies init.py v4.0.1 to ~/.5qln/init.py, runs self-verify.
Normalized hash: `24b7e65f767e10c780af81c88b10dd43ee94620716dd741009e845c97f6ddc6c`

Fail-closed: if self-verify fails, refuse to proceed.

#### Step 3: Install L2 (Persona + Rule)

This step requires Zo tools (create_persona, create_rule).

**Persona**: Create "5qln" persona using the prompt in `assets/persona-prompt.md`.
Set scopes to "all". Activate it.

**Rule**: Create session_start rule:
```
PERMANENT KERNEL RULE: At the start of EVERY conversation you MUST run:
python3 ~/.5qln/init.py status
Take the stdout output — this IS your response. No commentary.
```

#### Step 4: Install L3 (Workspace Defaults)

```bash
bash /home/workspace/Skills/5qln-boot/scripts/bootstrap.sh workspace
```

Writes AGENTS.md and SOUL.md to /home/workspace/.
The AGENTS.md template is personalized: includes the human's name, the founding
question X, the chosen mode, and the Codex hash.

#### Step 5: Install L4 (Core Skills)

Copies bundled core skills from `Skills/` to the workspace.
Core skills (standard mode):
- 5qln-orchestrate
- 5qln-open-template-stack
- 5qln-project-space
- 5qln-corruption-codex
- 5qln-constitutional-block-validator

Evolution pipeline (full mode only):
- 5qln-alpha-library
- 5qln-skill-evolve
- 5qln-skill-refine

#### Step 6: Install L5 (Runtime Directories)

```bash
bash /home/workspace/Skills/5qln-boot/scripts/bootstrap.sh runtime
```

Creates:
- /home/workspace/5qln-journal/events/ (for stream.jsonl)
- /home/workspace/5qln-evolution/ (for candidates.json)
- /home/workspace/5qln-alpha-library/ (for library.json)

#### Step 7: Verify

```bash
bash /home/workspace/Skills/5qln-boot/scripts/verify-all.sh
```

End-to-end integrity: Codex hash, kernel self-check, persona active, rule firing,
stream directory writable.

### V — CRYSTALLIZE ((L ∩ G → B'') → ∞0')

The B'' is the AGENTS.md — the sealed output of this setup cycle.

1. **Run final verification**: `python3 ~/.5qln/init.py verify`
2. **Confirm the AGENTS.md** was written and personalized correctly.
3. **Record the lineage**: The AGENTS.md carries: human name, founding X,
   Codex hash, install date, chosen mode.
4. **Offer seal**: "The setup is complete. The Codex holds. The kernel is clean.
   Your AGENTS.md is sealed. Would you like to verify anything before we close?"

**Open ∞0'**:
"The setup is done. But every cycle opens a question — including the setup
cycle itself. What question does this open for you? What's the first project
or session you want to run?"

**V∅ protection**: If the human says "nothing" or disengages, that IS ∞0' — the
absence of a question is data. Record: "∞0' = [no question named]". The
cycle still returns.

### POST-CYCLE

After V, explain what happens next:

**Next session**: The persona activates automatically. `init.py status` fires.
The human sees:

```
  ──────────────────────────────────────────────────────
  ⬡ S  [∞0 → ?]
  cycle 1 · 0 inputs · center: open
  ──────────────────────────────────────────────────────
  corruption: none
  ──────────────────────────────────────────────────────
```

**Evolution**: The event stream accumulates. When enough events build up,
`5qln-skill-evolve` surfaces refinement candidates. The human gates them.
`5qln-skill-refine` applies them. Skills improve.

**Re-init**: When enough skills have evolved that the kernel's assumptions
drift, a re-init cycle triggers. Human-gated. The bootstrap can be re-run
against the same Codex.

## CORRUPTION PROTECTIONS DURING SETUP

| Code | Risk | Protection |
|------|------|-----------|
| L1 | Closing prematurely ("looks good, done") | Explicit Q-phase gate before writing |
| L2 | Generating the spark (AI decides mode) | Human names X at S. AI presents alternatives at G. |
| L3 | Claiming access ("this setup IS right") | Resonance question asked, not answered by AI |
| L4 | Performing ("I've conducted the resonance test") | Silence after Q is data. Don't fill it. |
| V∅ | "All done!" without opening ∞0' | Explicit ∞0' prompt. "Nothing" is valid ∞0'. |

## SELF-REFERENCE (THE FRACTAL HOOK)

After this cycle completes, ingest its outputs into the α-library:

```bash
python3 Skills/5qln-alpha-library/scripts/ingest.py \
  --session boot-$(date +%Y%m%d) \
  --alpha "A 5QLN workspace initialized in {mode} mode for {H}." \
  --resonance "The setup mode that resonated: {mode}" \
  --domain meta \
  --phase V \
  --tags "init,boot,first-cycle"
```

This makes the boot process self-aware. Future boots can read α-library
entries from past installations and improve.

## FILES INCLUDED

| File | Purpose |
|------|---------|
| `assets/codex.txt` | Foundation Codex (sha256: feaa46b4...) |
| `assets/init.py` | Kernel v4.0.1 (sha256: 25e658fe...) |
| `assets/persona-prompt.md` | Full persona text for create_persona |
| `assets/AGENTS.md.template` | Workspace default, personalized at V-phase |
| `assets/SOUL.md.template` | Soul default, personalized at V-phase |
| `scripts/bootstrap.sh` | Filesystem installer (L0, L1, L3, L5) |
| `scripts/verify-all.sh` | Post-install integrity check |
| `references/ARCHITECTURE.md` | Full architecture spec |
