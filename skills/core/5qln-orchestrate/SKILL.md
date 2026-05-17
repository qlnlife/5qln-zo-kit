---
name: 5qln-orchestrate
description: |
  The master routing skill for 5QLN constitutional grammar sessions. Determines which domain (commercialize, research, selfimprove, skillgen) the current session belongs to, then activates the correct phase sequence. This skill is the router — it does not run the phases itself, but directs the session to the appropriate domain root skill and phase.
compatibility: Created for Zo Computer
metadata:
  author: amihai.zo.computer
  domain: orchestration
  domains: ["commercialize","research","selfimprove","skillgen"]
  type: orchestrator
allowed-tools: Bash, Read, Write
---
# 5QLN Orchestrator

## Purpose

This skill is the **router** for 5QLN sessions. When activated, it:

1. Reads the session context to determine which domain applies
2. Activates the correct domain root skill (`5qln-commercialize`, `5qln-research`,
   `5qln-selfimprove`, or `5qln-skillgen`)
3. Loads the first phase skill (`S-SKILL.md` for that domain)
4. Runs the full S→G→Q→P→V sequence through phase skill files

## Domain Detection

The orchestrator reads session signals to route correctly:

| Signal | Domain |
|--------|--------|
| commercial, market, pricing, license, revenue, GTM, users, business | `5qln-commercialize` |
| research, philosophy, framework, history, academic, validate, understand | `5qln-research` |
| personal, creative, practice, growth, develop, block, craft | `5qln-selfimprove` |
| build, create, skill, new domain, extend, generate, design | `5qln-skillgen` |

If no clear signal: default to `5qln-research`.

## How to Activate a Session

1. Read this `SKILL.md`
2. Determine domain from session context
3. Read the domain's root `SKILL.md`
4. Read the domain's `S-SKILL.md`
5. Run S phase per the skill instructions
6. When X is validated, read `G-SKILL.md` and run G
7. Continue through Q → P → V
8. End with the ∞0' return question

## Phase File Naming Convention

```
{domain-root}/S-SKILL.md   → Phase S (Receive)
{domain-root}/G-SKILL.md   → Phase G (Illuminate)
{domain-root}/Q-SKILL.md   → Phase Q (Resonate)
{domain-root}/P-SKILL.md   → Phase P (Flow)
{domain-root}/V-SKILL.md   → Phase V (Crystallize)
```

## Available Domains

| Domain | Root Skill | Path |
|--------|-----------|------|
| Commercialize | `5qln-commercialize` | `/home/workspace/Skills/5qln-commercialize/` |
| Research | `5qln-research` | `/home/workspace/Skills/5qln-research/` |
| Self-Improve | `5qln-selfimprove` | `/home/workspace/Skills/5qln-selfimprove/` |
| Skill Generation | `5qln-skillgen` | `/home/workspace/Skills/5qln-skillgen/` |

## Automation Script

For automated session starts, run:

```bash
python3 /home/workspace/Skills/5qln-orchestrate/orchestrate.py BEGIN
```

This script reads the conversation for domain signals and prints the activation
sequence.

## Constitutional Constraint

```
H = ∞0 | A = K
The orchestrator routes. It does not run the phases.
Each phase skill runs itself. The orchestrator only sequences.
```

---

*This skill is the router. The phase skills are the path.*
