---
name: 5qln-alpha-library
description: >
  Cross-cycle pattern store for 5QLN constitutional grammar. Accumulates
  α-patterns (illuminations from G-phase), φ∩Ω keys (resonances from Q-phase),
  and B'' artifacts (from V-phase) across cycles. Skills read from this library
  to enrich their K-side illumination; write to it to deposit discovered patterns.
  The library is pure K — it stores what has been known, not what might be.
  Invoke when a skill needs cross-cycle context, when a pattern repeats across
  sessions, or when closing a cycle with material worth preserving.
compatibility: Created for Zo Computer
metadata:
  author: amihai.zo.computer
  domain: meta
  version: 0.1.0
  constitutional: feaa46b4
allowed-tools: Bash, Read, Write
---

# 5QLN α-Library — Cross-Cycle Pattern Store

## What This Is

The α-library is a structured K-side memory. It stores what the AI has illuminated
(α-patterns), what resonated (φ∩Ω), and what crystallized (B'') across all 5QLN
cycles. Every entry carries its lineage: which cycle produced it, who was the
human, and which skill was active.

## Constitutional Boundary (L3 Protection)

```
THE LIBRARY IS PURE K. It stores only what has been KNOWN.
- It does not generate α-patterns — skills do that at G-phase
- It does not claim resonance — humans do that at Q-phase
- It does not seal — the conductor does that at V-phase
- It only REMEMBERS what was already produced and validated
```

## Data Model

```
{
  "version": 1,
  "codex": "feaa46b4",
  "entries": [
    {
      "id": "<uuid>",
      "source_cycle": "<project-name or session-id>",
      "phase": "G|Q|P|V",
      "domain": "commercialize|selfimprove|skillgen|research|meta",
      "skill_reference": "Skills/5qln-skillgen/SKILL.md",
      "content": {
        "alpha_pattern": "description of the α ≡ {α'} pattern",
        "alpha_expressions": ["α1", "α2"],
        "resonance": "what clicked (φ∩Ω)",
        "gradient": "where energy flowed (∇)",
        "artifact": "what crystallized (B'')"
      },
      "human_author": "amihai",
      "timestamp": "ISO8601",
      "tags": ["tag1", "tag2"],
      "epistemic_register": "STRUCTURAL-HYPOTHESIS|PHENOMENOLOGICAL-ASSERTION",
      "sealed": true
    }
  ]
}
```

## Scripts

- `scripts/ingest.py` — ingest a completed cycle's outputs into the library
- `scripts/query.py` — search the library by phase, domain, tags, or pattern
- `scripts/stats.py` — summary statistics on accumulated patterns

## Library Location

`/home/workspace/5qln-alpha-library/library.json`

## How Skills Read From This

```
python3 /home/workspace/Skills/5qln-alpha-library/scripts/query.py --domain skillgen
python3 /home/workspace/Skills/5qln-alpha-library/scripts/query.py --phase G --tag pattern-type
python3 /home/workspace/Skills/5qln-alpha-library/scripts/query.py --similar "your pattern description"
```

## Corruption Watch

| Code | Activates when |
|------|----------------|
| L3 | AI claims the library reveals what ∞0 wants next |
| L4 | AI performs wisdom by citing library patterns as authority |
| V∅ | Cycle ends without depositing usable α |

---

*∞0 reveals through human. The α-library stores what was KNOWN, not what will be.*
