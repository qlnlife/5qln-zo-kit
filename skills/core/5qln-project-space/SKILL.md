---
name: 5qln-project-space
description: 5QLN-native project space for Zo Computer — SparkWell-aligned phase structure with DuckDB data integration
compatibility: Created for Zo Computer
metadata:
  author: amihai.zo.computer
  category: 5qln
---
## What This Is

A **5QLN-native project space** on Zo Computer. Each project lives in `/Projects/<name>/` and follows the phase-gated structure:

```
/Projects/<name>/
├── META.yaml              ← project identity + current phase
├── S/                     ← RECEIVE: raw inputs, threat model
│   ├── validated_X.md     ← what ∞0 revealed
│   └── sources.md         ← linked datasets
├── G/                     ← ILLUMINATE: pattern recognition
│   └── pattern_map.md     ← α + {α'} echoes
├── Q/                     ← RESONATE: click moments
│   └── resonant_keys.md   ← φ ∩ Ω
├── P/                     ← FLOW: where energy goes
│   └── flow_gradient.md   ← δE/δV → ∇
└── V/                     ← CRYSTALLIZE: artifact + return
    ├── artifact.md        ← B + B''
    └── infinity_prime.md  ← ∞0'
```

**SparkWell alignment:** The 12-month curriculum maps to S→G→Q→P→V. Each project declares its **threat model** at S (external ∞0 anchor). The return question (∞0') at V seeds the next cycle.

## Tools

```bash
# Initialize a project
python3 /home/workspace/.zo-tools/init_project.py <name> [--domain commercialize|research|selfimprove|skillgen]

# Show current phase + what inputs/outputs are expected
python3 /home/workspace/.zo-tools/route_phase.py <name>

# Advance to next phase
python3 /home/workspace/.zo-tools/route_phase.py <name> --advance

# Save anything to project long-term memory
python3 /home/workspace/.zo-tools/save_memory.py <name> "<text>"

# List all projects
python3 /home/workspace/.zo-tools/list_projects.py
```

## Linked Datasets

- `sparkwell-antientropy` — SparkWell homepage + enrollment (DuckDB)
- `sparkwell-resource-portal` — 14 articles, 9,314 words, full 12-month curriculum (DuckDB)

Query with: `duckdb /home/workspace/Datasets/<name>/data.duckdb -c "SQL"`

## Zo Space Dashboard

- **Homepage:** https://amihai.zo.space/ — project list
- **Project detail:** https://amihai.zo.space/p/:name (private, owner-only)
- **APIs:**
  - `GET /api/projects` — all projects
  - `GET /api/projects-detail?name=X` — single project + files
  - `POST /api/projects-advance?name=X` — advance phase
  - `GET|POST /api/projects-todos?name=X` — todos

## Phase Behavior

**S** — Receive. Collect raw data. Declare threat model (what catastrophic risk does this project address?). Link datasets.

**G** — Illuminate. Name the core pattern. Show fractal echoes. What is the irreducible essence?

**Q** — Resonate. What clicks. What doesn't. Test candidates. Watch for natural intersection.

**P** — Flow. Where does energy want to go. Map friction. Reveal the gradient.

**V** — Crystallize. Artifact + return question. ∞0' must carry a question. No V without ∞0'.

## Corruption Watch

- L1: Closing with answers before ∞0 reveals
- L2: Generating the spark (AI creates X instead of receiving it)
- L3: Claiming access to ∞0 (AI says "the Unknown shows me")
- L4: Performing wisdom ("here's what you should do")
- V∅: Ending without ∞0'
