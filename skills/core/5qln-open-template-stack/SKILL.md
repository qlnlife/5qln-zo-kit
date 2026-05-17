---
name: 5qln-open-template-stack
description: "The complete 5QLN Open Template Stack — constitutional grammar + project space for Zo Computer. Contains: L1 (language), D1 (decoder), C1 (compiler), BP (deployment best practices), four compiled skill sets (Commercialize, Self-Improve, SkillGen, Research), and the 5QLN Project Space system. Use when starting, running, or advancing any 5QLN project through S→G→Q→P→V cycles."
compatibility: Created for Zo Computer
metadata:
  author: amihai.zo.computer
  source: 5qln.com + custom
  version: 1
---
# 5QLN Open Template Stack

## Quick Commands

```bash
# Project Management
python3 /home/workspace/.zo-tools/init_project.py <name> --domain <commercialize|research|selfimprove|skillgen>
python3 /home/workspace/.zo-tools/route_phase.py <project>
python3 /home/workspace/.zo-tools/route_phase.py <project> --advance
python3 /home/workspace/.zo-tools/list_projects.py
python3 /home/workspace/.zo-tools/bridge.py <dataset> <project>

# Memory
python3 /home/workspace/.zo-tools/save_memory.py <project> --phase V --alpha "..." --z "..." --artifact "..."
python3 /home/workspace/.zo-tools/cycle_advance.py <project>

# Skills Registry
ls /home/workspace/5qln-open-template-stack/skills/
ls /home/workspace/5qln-open-template-stack/core/
```

## What's Inside

| Component | Path | Purpose |
|---|---|---|
| Language | `core/L1_The_Language.md` | Vocabulary & symbols |
| Decoder | `core/D1_The_Decoder.md` | Decoding grammar |
| Compiler | `core/C1_The_Compiler.md` | Output enforcement |
| Best Practices | `core/BP_Deployment_Best_Practices.md` | Deployment guidance |
| Commercialize Skills | `skills/commercialize/` | SKILL_S → V for commercialization |
| Self-Improve Skills | `skills/selfimprove/` | SKILL_S → V for personal growth |
| SkillGen Skills | `skills/skillgen/` | SKILL_S → V for generating new skills |
| Research Skills | `skills/research/` | SKILL_S → V for deep inquiry |
| Project Space | `/home/workspace/Projects/` | Living project directories |

## Project Space Architecture

```
Projects/
└── <project-name>/
    ├── META.yaml
    ├── README.md
    ├── .5qln/
    │   ├── S/raw/ & S/validated/
    │   ├── G/alpha/ & G/echoes/
    │   ├── Q/candidates/ & Q/resonant/
    │   ├── P/gradient/ & P/energy/
    │   ├── V/artifact/ & V/benefit/ & V/return/
    │   └── memory.yaml
    └── out/
```

## The 5QLN Cycle

```
∞0 → ? → X (S)
X → α ≡ {α'} → Y (G)
Y → φ ∩ Ω → Z (Q)
Z → δE/δV → ∇ → A (P)
∇ + A → (L ∩ G → B'') → ∞0' (V)
∞0' → Seeds next S
```
