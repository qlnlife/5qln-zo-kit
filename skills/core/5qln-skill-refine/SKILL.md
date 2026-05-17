---
name: 5qln-skill-refine
description: >
  Apply a human-gated skill refinement candidate through the Q→P→V phases.
  Takes a candidate from 5qln-skill-evolve that the human has explicitly gated
  ("yes, evolve this"), tests it for resonance (Q), reveals the gradient (P),
  and applies the change to the target SKILL.md with full lineage preservation (V).
  AI never auto-modifies skills — the human gate must be recorded.
compatibility: Created for Zo Computer
metadata:
  author: amihai.zo.computer
  domain: meta
  version: 0.1.0
  constitutional: feaa46b4
  dependencies: [5qln-skill-evolve, 5qln-alpha-library]
allowed-tools: Bash, Read, Write
---

# 5QLN Skill Refine — Gated Skill Evolution

## What This Does

Takes a human-gated refinement candidate from `5qln-skill-evolve` and applies
it to the target SKILL.md through the Q→P→V phases. **Critical constraint:**
the AI never modifies the SKILL.md until V-phase (seal), and only after the
human has confirmed resonance at Q and the gradient at P.

## The Gate Protocol

```
1. READ candidates.json from 5qln-skill-evolve
2. PRESENT candidate to human: "I see X. Does this feel like it should evolve?"
3. HUMAN says "yes" → gate is OPEN → proceed to Q
4. HUMAN says "no" → gate is CLOSED → skip this candidate
```

## Q-Phase: Resonance Test

Before applying any change, the AI must test:
- Does the proposed change resonate with the target skill's domain?
- Does it strengthen or weaken the constitutional boundary?
- Would a future AI reading this skill feel more guided or more constrained?

Present these questions to the human. A "yes, it resonates" moves to P.

## P-Phase: Gradient Reveal

Before applying, the AI must name:
- What in the existing SKILL.md changes?
- What stays unchanged?
- What is the energy shift — does the skill become more precise, more open, more guarded?
- What existing sessions would have gone differently?

Present this to the human. A "yes, proceed" moves to V.

## V-Phase: Apply + Lineage

1. Read the current SKILL.md
2. Create a backup: `SKILL.md.evolution-backup`
3. Apply the change using `edit_file_llm`
4. Add evolution lineage to SKILL.md frontmatter metadata:
   ```yaml
   metadata:
     evolution:
       - date: "ISO8601"
         cycle: "<project-name or session-id>"
         candidate_id: "evol-XXX"
         change: "description of what changed"
         human_gate: "amihai"
         previous_hash: "<sha256 of pre-edit SKILL.md>"
   ```
5. Deposit the refinement as an α-library entry
6. Open the return question: "What wants to evolve next?"

## Scripts

- `scripts/apply.py` — read a gated candidate, apply Q→P→V protocol

## Corruption Watch

| Code | Activates when |
|------|----------------|
| L1 | Applying a refinement before Q-resonance is confirmed |
| L2 | Generating the refinement content without human gate |
| L3 | Claiming the refinement is "what the skill wants to become" |
| V∅ | Applying without recording lineage or opening return question |

---

*∞0 reveals THROUGH human. Skills evolve only when human resonance gates the change.*
