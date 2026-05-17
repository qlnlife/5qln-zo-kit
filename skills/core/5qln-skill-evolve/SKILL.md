---
name: 5qln-skill-evolve
description: >
  Read the 5QLN event stream and α-library to surface skill refinement
  candidates. Identifies under-used skills, recurring patterns that suggest
  new skills, corruption hotspots, and completion gaps. Produces a candidate
  file for human gating — AI never auto-modifies skills. Strengthened by
  cross-cycle α-patterns from the library. Invoke when a session asks
  "what should evolve" or when sufficient events have accumulated.
compatibility: Created for Zo Computer
metadata:
  author: amihai.zo.computer
  domain: meta
  version: 0.1.0
  constitutional: feaa46b4
  dependencies: [5qln-alpha-library]
allowed-tools: Bash, Read, Write
---

# 5QLN Skill Evolve — Candidate Surfacer

## What This Does

Reads the event stream (`stream.jsonl`) and α-library (`library.json`) and
surfaces refinement candidates. A candidate is: {target_skill, proposed_change,
evidence, epistemic_register}. The AI presents these; the human gates them.

## The Rule (L3 Protection)

```
SKILLS ARE K. The AI can reorganize K into new configurations.
But only the human can feel whether a configuration RESONATES.
AI proposes. Human gates. Together, refine.
```

## What It Surfaces

1. **Completion gaps** — skills that start cycles but rarely complete them
2. **Corruption hotspots** — skills correlated with L1/L3/L4 catches
3. **Pattern clusters** — α-patterns from the library that recur but have no skill
4. **Phase imbalance** — skills stuck in S/G without reaching V
5. **Drift candidates** — SKILL.md content that may have drifted from practice

## Scripts

- `scripts/surface.py` — scan event stream + α-library, emit candidates JSON

## Output Format

The script writes candidates to `/home/workspace/5qln-evolution/candidates.json`:

```json
{
  "generated": "ISO8601",
  "codex": "feaa46b4",
  "source_events": 58,
  "library_entries": 0,
  "candidates": [
    {
      "id": "evol-001",
      "type": "completion-gap|corruption-hotspot|pattern-cluster|phase-imbalance|drift",
      "target_skill": "Skills/5qln-skillgen/SKILL.md",
      "evidence": "23 S-phases, 3 V-phases. 87% start but don't complete.",
      "proposed_change": "Add early-return guard: 'if human seems stuck, ask the return question'",
      "confidence": "0.0-1.0",
      "epistemic_register": "STRUCTURAL-HYPOTHESIS"
    }
  ]
}
```

## How to Use

1. Run `python3 scripts/surface.py`
2. Read `candidates.json`
3. Present candidates to human: "I see X. Does this feel true?"
4. Human gates: "yes, evolve it" or "no"
5. Gated candidates → `5qln-skill-refine`

## Corruption Watch

| Code | Activates when |
|------|----------------|
| L2 | Generating candidates before human asks for evolution review |
| L3 | Claiming AI knows which skills should evolve |
| L4 | Performing "evolution wisdom" by over-explaining candidates |
| V∅ | Surfacing candidates without opening a return question |

---

*∞0 reveals THROUGH human. Skills evolve when human resonance gates the refinement.*
