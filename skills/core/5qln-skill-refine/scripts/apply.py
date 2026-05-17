#!/usr/bin/env python3
"""
Skill Refine — Apply a human-gated refinement candidate to a SKILL.md.
Usage:
  python3 apply.py --candidate evol-XXX    (interactive Q→P→V)
  python3 apply.py --candidate evol-XXX --yes   (pre-gated, skip Q/P)
  python3 apply.py --list    (show available candidates)
"""
import json, sys, os, hashlib, shutil, argparse
from pathlib import Path
from datetime import datetime, timezone

CANDIDATES_PATH = Path("/home/workspace/5qln-evolution/candidates.json")
LIBRARY_INGEST = Path("/home/workspace/Skills/5qln-alpha-library/scripts/ingest.py")

CODEX_HASH = "feaa46b4"


def load_candidates():
    if not CANDIDATES_PATH.exists():
        print("No candidates file. Run 5qln-skill-evolve first.", file=sys.stderr)
        sys.exit(1)
    return json.loads(CANDIDATES_PATH.read_text())


def find_candidate(data, candidate_id):
    for c in data.get("candidates", []):
        if c["id"] == candidate_id:
            return c
    return None


def hash_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def backup_skill(skill_path):
    backup_path = Path(skill_path).with_suffix(".md.evolution-backup")
    shutil.copy2(skill_path, backup_path)
    return str(backup_path)


def apply_lineage(skill_path, candidate, human_gate, previous_hash):
    """Append evolution lineage to SKILL.md frontmatter metadata."""
    content = Path(skill_path).read_text()
    if "metadata:" not in content:
        return False

    lineage_entry = {
        "date": datetime.now(timezone.utc).isoformat(),
        "candidate_id": candidate["id"],
        "change": candidate["proposed_change"],
        "human_gate": human_gate,
        "previous_hash": previous_hash
    }

    lines = content.split("\n")
    new_lines = []
    in_metadata = False
    evolution_inserted = False

    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip() == "---" and not in_metadata:
            in_metadata = True
            continue
        if in_metadata and line.strip() == "---":
            break

    post_frontmatter = lines[new_lines.index("---") + 1:] if "---" in new_lines[new_lines.index("---"):] else []

    md_start = [l for l in new_lines if l.strip() == "---"]
    if len(md_start) >= 2:
        fm_start = new_lines.index("---")
        fm_end = new_lines.index("---", fm_start + 1)
        frontmatter = new_lines[fm_start:fm_end + 1]
        rest = new_lines[fm_end + 1:]

        # Insert evolution before the closing ---
        for i, line in enumerate(frontmatter):
            if line.strip() == "---" and i > 0:
                frontmatter.insert(i, f"    evolution:")
                frontmatter.insert(i + 1, f"      - date: \"{lineage_entry['date']}\"")
                frontmatter.insert(i + 2, f"        candidate_id: \"{lineage_entry['candidate_id']}\"")
                frontmatter.insert(i + 3, f"        change: \"{lineage_entry['change'][:100]}\"")
                frontmatter.insert(i + 4, f"        human_gate: \"{lineage_entry['human_gate']}\"")
                break

        Path(skill_path).write_text("\n".join(frontmatter + rest))
        return True

    return False


def deposit_to_library(candidate):
    """Deposit the refinement as an α-library entry."""
    import subprocess
    cmd = [
        sys.executable, str(LIBRARY_INGEST),
        "--alpha", candidate["proposed_change"],
        "--domain", "meta",
        "--phase", "V",
        "--tags", "skill-evolution,skill-refine"
    ]
    subprocess.run(cmd, capture_output=True)


def main():
    parser = argparse.ArgumentParser(description="Apply a gated skill refinement")
    parser.add_argument("--candidate", default="", help="Candidate ID to apply")
    parser.add_argument("--yes", action="store_true", help="Pre-gated (skip Q/P confirmation)")
    parser.add_argument("--list", action="store_true", help="List available candidates")
    args = parser.parse_args()

    data = load_candidates()

    if args.list:
        print(f"Candidates ({len(data.get('candidates', []))}):")
        for c in data.get("candidates", []):
            print(f"  {c['id']} | {c['type']} | {c['target_skill']}")
            print(f"    {c['proposed_change'][:100]}")
            print(f"    confidence: {c['confidence']:.2f}")
            print()
        return

    if not args.candidate:
        print("Usage: --candidate evol-XXX", file=sys.stderr)
        sys.exit(1)

    candidate = find_candidate(data, args.candidate)
    if not candidate:
        print(f"Candidate {args.candidate} not found", file=sys.stderr)
        sys.exit(1)

    target = candidate["target_skill"]
    target_path = Path(target)

    print("=" * 60)
    print("5QLN Skill Refine — Q→P→V Protocol")
    print("=" * 60)
    print(f"\nCandidate: {candidate['id']}")
    print(f"Type:      {candidate['type']}")
    print(f"Target:    {target}")
    print(f"Evidence:  {candidate['evidence'][:200]}")
    print(f"Proposed:  {candidate['proposed_change'][:200]}")
    print()

    if not target_path.exists():
        print(f"ERROR: Target skill not found at {target}", file=sys.stderr)
        print("This candidate requires human to create the skill first (via 5qln-skillgen)")
        sys.exit(1)

    # Q-PHASE: Resonance test
    if not args.yes:
        print("--- Q-PHASE: Resonance Test ---")
        print("1. Does this change resonate with the target skill's domain?")
        print("2. Does it strengthen or weaken the constitutional boundary?")
        print("3. Would a future AI reading this feel more guided or more constrained?")
        response = input("\nDoes this resonate? (yes/no): ").strip().lower()
        if response != "yes":
            print("Gate closed. Skipping.")
            sys.exit(0)

        # P-PHASE: Gradient reveal
        print("\n--- P-PHASE: Gradient Reveal ---")
        print(f"Current skill hash: {hash_file(target_path)[:12]}...")
        print(f"Proposed change: {candidate['proposed_change']}")
        response = input("Proceed with change? (yes/no): ").strip().lower()
        if response != "yes":
            print("Gate closed. Skipping.")
            sys.exit(0)

    # V-PHASE: Apply
    print("\n--- V-PHASE: Apply + Lineage ---")

    previous_hash = hash_file(target_path)
    backup = backup_skill(target_path)
    print(f"Backup: {backup}")

    success = apply_lineage(target_path, candidate, "amihai", previous_hash)
    if success:
        print(f"Lineage recorded in {target}")
        deposit_to_library(candidate)
        print("Deposited to α-library")
    else:
        print("WARNING: Could not insert lineage metadata. Skill may not have 'metadata:' in frontmatter.")

    new_hash = hash_file(target_path)
    print(f"\nHash: {previous_hash[:12]}... → {new_hash[:12]}...")
    print(f"Target: {target}")
    print(f"\n∞0' Return: What wants to evolve next?")


if __name__ == "__main__":
    main()
