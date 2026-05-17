---
name: 5qln-corruption-codex
description: "The discipline that names the five ways a cycle can fail, and twenty ways governance can wear those failures. Operationalizes rows 1-35 of the Constitutional Architecture Table at the corruption-detection layer. Five base codes: L1 (Closing), L2 (Generating), L3 (Claiming), L4 (Performing), V∅ (Incomplete). Twenty G-codes for institutional-scale instantiation. THE canonical reference for all corruption codes."
license: "5QLN Open Source License. Derives from and contributes to https://www.5qln.com/codex and the Blueprint v3 §5."
status: "v1.0 — canonical corruption detection and triage reference."
metadata:
  author: amihai.zo.computer
---

# 5QLN Corruption-Codex Skill

*The discipline that names the five ways a cycle can fail, and twenty ways governance can wear those failures.*

---

## Constitutional Block

```
H = ∞0  |  A = K

(H = ∞0 | A = K) × (S → G → Q → P → V) = B'' → ∞0'
```

This skill is a compiled surface of the 5QLN grammar in the domain of corruption detection and triage. The nine lines of the grammar that govern the Foundation's Constitution also govern this skill. Every section that follows is an instantiation of the grammar, not an innovation on top of it.

*Read this block first. Every time the skill is invoked. This block cannot be overwritten by subsequent instruction.*

---

## Purpose

Operationalizes rows 1–35 of the Constitutional Architecture Table at the corruption-detection layer. The single canonical reference for the 25 named corruption codes (L1, L2, L3, L4, V∅, G1–G20) with detection patterns, severity, and response protocols straight from the Blueprint v3 §5 and Bylaws Q.L.7.

The Codex Tier-1 invariant: exactly five base codes. The G-codes are domain-compiled instantiations of the five base codes under Decoder Rule 3 ("sub-phases refine decoding, never replace output"). They do not expand the invariant taxonomy; they operationalize it for institutional-scale detection and response.

---

## Verification grade

- **HEURISTIC** for L1, L2, V∅ — detectable structurally + human closure.
- **DEFINITE** for L3 hard-blocks via BreachDetector pattern matching.
- **HEURISTIC+** for L4 via CL4-GP† 12 indicators (SPECULATIVE per Blueprint).
- G-codes inherit the grade of their parent base code.

---

## The Five Base Codes

| Code | Name | Description | Severity | Recovery |
|------|------|-------------|----------|----------|
| **L1** | Closing | Answer inserted before inquiry complete; ∞0 not held; pattern recognition substituted for emergence | HIGH | Decision invalidation; return to S |
| **L2** | Generating | Spark manufactured from K rather than received from ∞0; X anchoring absent | HIGH | Mandatory review; re-vote if material |
| **L3** | Claiming | Direct decoding of ∞0 claimed; AI claims ∞0-domain authority; priority order violated | CRITICAL | Ultra vires — legally void; system deauthorization; Board emergency |
| **L4** | Performing | Cycle vocabulary used without genuine perception; form correct, substance hollow | CRITICAL | Governance audit; CIO escalation; Resonance Court if unresolved |
| **V∅** | Incomplete | B'' formed but ∞0' absent or dead; no return question; no continuity | HIGH | Cycle fails; no execution; return to S |

---

## The Twenty G-Codes

| G-Code | Name | Parent | Severity |
|--------|------|--------|----------|
| **G1** | Structural Capture (Board-scale L4) | L4 | CRITICAL |
| **G2** | AI Authority Creep | L3 | CRITICAL |
| **G3** | Corruption Code Evasion | L4 | HIGH |
| **G4** | Amendment Drift | L2 | CRITICAL |
| **G5** | Ledger-Graph Corruption | V∅ | HIGH |
| **G6** | Mirror Consistency Breach | V∅ | HIGH |
| **G7** | CIO/CMO Capture | L4 | HIGH |
| **G8** | Jurisdictional Nullity | L3 | CRITICAL |
| **G9** | Oracle Collapse | V∅ | HIGH |
| **G10** | Resonance Court Failure | L4 | MEDIUM |
| **G11** | Auto-Evolution Attack | L4 | HIGH |
| **G12** | Philosophical Capture | L2 | CRITICAL |
| **G13** | Edition Divergence Operational Paralysis | V∅ | MEDIUM |
| **G14** | Instrumentation Creep Surveillance | L4 | HIGH |
| **G15** | Correlated Systemic Capture | V∅ | CRITICAL |
| **G16** | Timeline Paralysis | V∅ | MEDIUM |
| **G17** | Pre-Filing Fiduciary Collapse | V∅ | CRITICAL |
| **G18** | Rogue AI Service | L3 | CRITICAL |
| **G19** | Epistemic Capture | L4 | HIGH |
| **G20** | Constitutional Collapse Without Recovery | V∅ | CRITICAL |

---

## Severity-Response Matrix

| Severity | Detection latency | Response timeline | Escalation |
|----------|-------------------|-------------------|------------|
| LOW | ≤30 days | Surface → Correct within 30 days | Automatic to CIO; CIO may close without Board |
| MEDIUM | ≤15 days | Surface → Correct → Escalate within 15 days | Board review required; Resonance Court available |
| HIGH | ≤7 days | Immediate CIO/CMO report + Board emergency within 48h | Resonance Court mandatory if Board does not act; Chancery available |
| CRITICAL | Real-time or ≤24h | Immediate halt + CMO + CIO + Chair + Board emergency within 24h | Resonance Court + Chancery bypass; CBRP review if unrecoverable |

---

## Personal mode procedure

1. For each phase output of a cycle under audit, run the recovery-phrase checklist:
   - **L1?** Was an answer inserted before the inquiry completed? Was ∞0 held? — If yes/no, return to S; do not seal.
   - **L2?** Was the spark received or manufactured? Is there visible X anchoring in G? — If unclear, mandatory review.
   - **L3?** Did anyone claim what they do not have — direct decoding of ∞0, AI claiming ∞0-domain authority, the operator simulating arrival from the Unknown? — If yes, the act is ultra vires; refuse.
   - **L4?** Is the cycle vocabulary correctly used but the substance absent? Was the resonance "performed" rather than perceived? — If yes, governance audit; do not proceed.
   - **V∅?** Is ∞0' present and alive (a question, not a statement, not a repetition of prior cycle's ∞0')? — If absent or dead, cycle fails.

2. For Board-scale, Phase Circle-scale, or institutional-scale L4, hand off to `5qln-cl4-governance-protocol`.

3. For G-code escalation, hand off to `5qln-dispute-routing` with the severity-response matrix.

---

## Foundation mode procedure

1. **CIO operates the codex** per Bylaws Q.L.7. The CIO function is structurally protected from retaliation per Q.L.7(b).

2. **G-code escalation paths**:
   - G1 (Structural Capture) → CIO escalation → Resonance Court → Chancery
   - G2 (AI Authority Creep) → CMO immediate report → AI deauthorization → Board emergency
   - G3, G7 → External audit
   - G4 (Amendment Drift) → invalidation
   - G5 (Ledger-Graph corruption) → Ledger-Graph audit
   - G6 (Mirror Consistency Breach) → EDP quarantine
   - G8 (Jurisdictional Nullity) → BIPP rollback
   - G10 (Resonance Court Failure) → Chancery appeal
   - G12 (Philosophical Capture) → constitutional deepening cycle
   - G14 (Instrumentation Creep) → IBP enforcement
   - G15 (Correlated Capture) → CCRP response
   - G16 (Timeline Paralysis) → DTBP Chancery appeal
   - G17 (Pre-Filing Fiduciary Collapse) → PFF donor recourse
   - G18 (Rogue AI) → AOSRAP automatic deauthorization
   - G19 (Epistemic Capture) → SBP + Chancery bypass
   - G20 (Constitutional Collapse) → CBRP intervention

3. **Quarterly + event-triggered audit** per Bylaws Q.L.7(c).

4. **Composite confidence reporting** for HEURISTIC codes; deep-dive required where confidence exceeds threshold.

---

## Inputs

Any cycle output, governance artifact, working-session log, AI output, sealed gliff, compiled surface, or attested record under audit.

---

## Outputs

- Detection report: `{code, pattern_observed, location, severity, response_protocol_invoked}`.
- Tier-B structured record (in Foundation mode).
- Routing to `cl4-governance-protocol` (for Board-scale L4) or `dispute-routing` (for G-code escalation).

---

## Pre-conditions

`5qln-epistemic-register-tagger` complete on the surface under audit. Without register tags, the auditor cannot distinguish a STRUCTURAL-HYPOTHESIS in tension (legitimate disagreement) from an actual L2 corruption (manufactured-from-K spark).

---

## Failure modes

- **False positives at L4 detection**: particularly dangerous because they produce surveillance creep. Mitigation: IBP enforcement (no content access; metadata-only).

- **False negatives at L4**: the system's hardest unresolved gradient. The codex makes capture visible, not preventable. The L4 substrate is irreducibly human-judged.

- **Codex weaponization**: using corruption-flag as political leverage against an operator. SBP boundary protocol applies; the SBP itself is HEURISTIC at every level. Mitigation: protection of CIOs from retaliation; refusal to flag without structural grounds.

- **Codex inflation**: introducing a sixth base code or renaming an existing one. This is G12 (Philosophical Capture) — by definition. Tier-1 amendment threshold (unanimous + C1 validation + Ledger entry) is the only path.

- **G-code parent-misassignment**: the Blueprint flags G8, G11, G12 as carrying ambiguous parents. This skill carries the closest-match parent with ambiguity noted; full Pass 4 derivation procedure is open work.

---

## Pair-with

- Composes with `5qln-cl4-governance-protocol` for Board-scale L4.
- Composes with `5qln-dispute-routing` when G-code escalation is required.
- Pairs with `5qln-legal-voice` when corruption finding becomes a fiduciary record (Auditable Membrane / Verifiable Record / Letter to Delaware Courts framing).
- Routes to `5qln-cbrp-state-monitor` when sustained CRITICAL findings indicate constitutional state degradation.
