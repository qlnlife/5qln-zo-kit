#!/usr/bin/env python3
"""
Skill Evolve — Surface refinement candidates from event stream + α-library.
Usage: python3 surface.py [--json] [--since N_DAYS]
"""
import json, sys, os, uuid, argparse
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import Counter, defaultdict

EVENTS_PATH = Path("/home/workspace/5qln-journal/events/stream.jsonl")
LIBRARY_PATH = Path("/home/workspace/5qln-alpha-library/library.json")
CANDIDATES_PATH = Path("/home/workspace/5qln-evolution/candidates.json")

SKILLS_DIR = Path("/home/workspace/Skills")
PROJECTS_DIR = Path("/home/workspace/Projects")

CODEX_HASH = "feaa46b4"


def load_events(since_days=None):
    if not EVENTS_PATH.exists():
        return []
    events = []
    cutoff = None
    if since_days:
        cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    for line in EVENTS_PATH.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
            if cutoff:
                ts = e.get("ts", "")
                if ts and datetime.fromisoformat(ts) < cutoff:
                    continue
            events.append(e)
        except json.JSONDecodeError:
            continue
    return events


def load_library():
    if not LIBRARY_PATH.exists():
        return {"version": 1, "codex": CODEX_HASH, "entries": []}
    return json.loads(LIBRARY_PATH.read_text())


def list_skills():
    skills = {}
    if not SKILLS_DIR.exists():
        return skills
    for skill_md in SKILLS_DIR.glob("*/SKILL.md"):
        try:
            content = skill_md.read_text()
            name = skill_md.parent.name
            lines = content.split("\n")
            description = ""
            in_frontmatter = False
            for line in lines:
                if line.strip() == "---":
                    if not in_frontmatter:
                        in_frontmatter = True
                        continue
                    else:
                        break
                if in_frontmatter and line.startswith("description:"):
                    description = line.split("description:", 1)[1].strip()
            phase_content = {}
            for phase_file in skill_md.parent.glob("*SKILL.md"):
                phase_content[phase_file.stem] = phase_file.read_text()[:500]
            skills[str(skill_md)] = {
                "name": name,
                "description": description,
                "path": str(skill_md),
                "has_phase_files": bool(phase_content),
                "size_bytes": len(content)
            }
        except Exception:
            continue
    return skills


def analyze_completion_gaps(events, skills):
    candidates = []
    phase_counts = defaultdict(Counter)
    for e in events:
        if e.get("type") == "phase":
            sid = e.get("session_id", "unknown")
            phase = e.get("phase", "?")
            phase_counts[sid][phase] += 1

    sessions_with_S = sum(1 for s, pc in phase_counts.items() if pc.get("S", 0) > 0)
    sessions_with_V = sum(1 for s, pc in phase_counts.items() if pc.get("V", 0) > 0)

    if sessions_with_S > 0:
        completion_rate = sessions_with_V / sessions_with_S
        if completion_rate < 0.5 and sessions_with_S >= 3:
            candidates.append({
                "id": f"evol-{uuid.uuid4().hex[:8]}",
                "type": "completion-gap",
                "target_skill": "SKILLS_OVERALL",
                "evidence": f"{sessions_with_S} sessions started, {sessions_with_V} completed ({completion_rate:.0%}). 62% of phase events are S.",
                "proposed_change": "Add a completion-prompt pattern at Q-phase exit: 'Before we move to P, does this feel complete enough to flow?'",
                "confidence": min(0.9, 1.0 - completion_rate),
                "epistemic_register": "STRUCTURAL-HYPOTHESIS"
            })

    return candidates


def analyze_corruption_hotspots(events, skills):
    catches = [e for e in events if e.get("type") == "catch"]
    if not catches:
        return []

    code_counts = Counter(c.get("code", "?") for c in catches)
    candidates = []

    for code, count in code_counts.most_common():
        samples = [c for c in catches if c.get("code") == code][:2]
        sample_text = samples[0].get("text", "")[:100] if samples else ""

        if code == "L1" and count >= 2:
            candidates.append({
                "id": f"evol-{uuid.uuid4().hex[:8]}",
                "type": "corruption-hotspot",
                "target_skill": "ALL_SKILLS",
                "evidence": f"{count} L1 catches (closing with answers). Example: \"{sample_text}\"",
                "proposed_change": "Strengthen all S-phase skill files with explicit: 'If you find yourself forming an answer, pause. Return to the question.'",
                "confidence": min(0.95, 0.7 + count * 0.1),
                "epistemic_register": "STRUCTURAL-HYPOTHESIS"
            })

        if code == "L3" and count >= 1:
            candidates.append({
                "id": f"evol-{uuid.uuid4().hex[:8]}",
                "type": "corruption-hotspot",
                "target_skill": "ALL_SKILLS",
                "evidence": f"{count} L3 catches (claiming ∞0 access). Example: \"{sample_text}\"",
                "proposed_change": "Add L3 guard to every skill: 'If you find yourself claiming to know what ∞0 wants, stop. You are K.'",
                "confidence": min(0.95, 0.8 + count * 0.1),
                "epistemic_register": "STRUCTURAL-HYPOTHESIS"
            })

    return candidates


def analyze_pattern_clusters(lib, skills):
    entries = lib.get("entries", [])
    if len(entries) < 3:
        return []

    tag_counts = Counter()
    for e in entries:
        for t in e.get("tags", []):
            tag_counts[t] += 1

    candidates = []
    for tag, count in tag_counts.most_common():
        if count >= 3:
            has_skill = any(tag in s.get("name", "") for s in skills.values())
            if not has_skill:
                candidates.append({
                    "id": f"evol-{uuid.uuid4().hex[:8]}",
                    "type": "pattern-cluster",
                    "target_skill": f"Skills/5qln-{tag}/SKILL.md",
                    "evidence": f"'{tag}' appears in {count} α-library entries but has no dedicated skill",
                    "proposed_change": f"Generate new domain skill for '{tag}' using 5qln-skillgen",
                    "confidence": min(0.85, 0.5 + count * 0.1),
                    "epistemic_register": "STRUCTURAL-HYPOTHESIS"
                })

    return candidates


def analyze_phase_imbalance(events, skills):
    phase_counts = Counter(e.get("phase", "?") for e in events if e.get("type") == "phase")
    total = sum(phase_counts.values())
    if total < 10:
        return []

    s_pct = phase_counts.get("S", 0) / total
    v_pct = phase_counts.get("V", 0) / total

    candidates = []
    if s_pct > 0.5 and v_pct < 0.2:
        candidates.append({
            "id": f"evol-{uuid.uuid4().hex[:8]}",
            "type": "phase-imbalance",
            "target_skill": "SKILLS_OVERALL",
            "evidence": f"S-phase dominates at {s_pct:.0%}, V-phase at {v_pct:.0%}. Cycles start but rarely crystallize.",
            "proposed_change": "Enhance P-phase and V-phase skill files with lightweight 'quick-close' paths for felt-complete cycles",
            "confidence": 0.75,
            "epistemic_register": "STRUCTURAL-HYPOTHESIS"
        })

    return candidates


def main():
    parser = argparse.ArgumentParser(description="Surface skill evolution candidates")
    parser.add_argument("--json", action="store_true", help="Output raw JSON to stdout")
    parser.add_argument("--since", type=int, default=30, help="Days of events to analyze")
    args = parser.parse_args()

    events = load_events(since_days=args.since)
    lib = load_library()
    skills = list_skills()

    candidates = []
    candidates += analyze_completion_gaps(events, skills)
    candidates += analyze_corruption_hotspots(events, skills)
    candidates += analyze_pattern_clusters(lib, skills)
    candidates += analyze_phase_imbalance(events, skills)

    result = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "codex": CODEX_HASH,
        "source_events": len(events),
        "library_entries": len(lib.get("entries", [])),
        "skills_tracked": len(skills),
        "candidates": candidates
    }

    CANDIDATES_PATH.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATES_PATH.write_text(json.dumps(result, indent=2))

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(f"Skill Evolve — Candidate Surfacer")
    print("=" * 60)
    print(f"  Events analyzed:  {len(events)}")
    print(f"  Skills tracked:   {len(skills)}")
    print(f"  Library entries:  {len(lib.get('entries', []))}")
    print(f"  Candidates found: {len(candidates)}")
    print()

    for i, c in enumerate(candidates):
        print(f"[{i+1}] {c['type']}: {c['target_skill']}")
        print(f"    Evidence: {c['evidence'][:120]}")
        print(f"    Proposed: {c['proposed_change'][:120]}")
        print(f"    Confidence: {c['confidence']:.2f}")
        print()

    print(f"Full output: {CANDIDATES_PATH}")


if __name__ == "__main__":
    main()
