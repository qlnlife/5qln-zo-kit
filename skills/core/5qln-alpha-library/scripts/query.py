#!/usr/bin/env python3
"""
α-Library Query — Search the cross-cycle pattern store.
Usage: python3 query.py [--domain D] [--phase P] [--tag T] [--similar TEXT] [--limit N] [--json]
"""
import json, sys, os, argparse
from pathlib import Path

LIBRARY_PATH = Path(__file__).parent.parent.parent.parent / "5qln-alpha-library" / "library.json"

def load():
    if not LIBRARY_PATH.exists():
        return {"version": 1, "codex": "feaa46b4", "entries": []}
    return json.loads(LIBRARY_PATH.read_text())

def match_tag(entry, tag):
    return tag.lower() in [t.lower() for t in entry.get("tags", [])]

def match_domain(entry, domain):
    return entry.get("domain", "").lower() == domain.lower()

def match_phase(entry, phase):
    return entry.get("phase", "").upper() == phase.upper()

def word_overlap(text_a, text_b):
    words_a = set(text_a.lower().split())
    words_b = set(text_b.lower().split())
    if not words_b:
        return 0
    return len(words_a & words_b) / max(len(words_a), 1)

def match_similar(entry, text):
    content = entry.get("content", {})
    searchable = " ".join([
        content.get("alpha_pattern", ""),
        content.get("resonance", ""),
        " ".join(content.get("alpha_expressions", []))
    ])
    return word_overlap(searchable, text)

def main():
    parser = argparse.ArgumentParser(description="Query the 5QLN α-Library")
    parser.add_argument("--domain", default="", help="Filter by domain")
    parser.add_argument("--phase", default="", help="Filter by phase (G,Q,P,V)")
    parser.add_argument("--tag", default="", help="Filter by tag")
    parser.add_argument("--similar", default="", help="Find entries similar to text")
    parser.add_argument("--limit", type=int, default=20, help="Max results")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    lib = load()
    entries = lib.get("entries", [])
    results = []

    for e in entries:
        if args.domain and not match_domain(e, args.domain):
            continue
        if args.phase and not match_phase(e, args.phase):
            continue
        if args.tag and not match_tag(e, args.tag):
            continue
        if args.similar:
            score = match_similar(e, args.similar)
            if score > 0:
                e["_similarity"] = round(score, 3)
                results.append(e)
        else:
            results.append(e)

    if args.similar:
        results.sort(key=lambda e: e.get("_similarity", 0), reverse=True)

    results = results[:args.limit]

    if args.json:
        print(json.dumps(results, indent=2))
        return

    print(f"α-Library ({len(results)} of {len(entries)} entries)")
    print("=" * 60)
    for i, e in enumerate(results):
        print(f"\n[{i+1}] {e.get('id','?')[:8]}... | {e.get('domain','?')} | {e.get('phase','?')}")
        c = e.get("content", {})
        if c.get("alpha_pattern"):
            print(f"  α: {c['alpha_pattern'][:120]}")
        if c.get("resonance"):
            print(f"  φ∩Ω: {c['resonance'][:120]}")
        if e.get("_similarity"):
            print(f"  similarity: {e['_similarity']}")
        print(f"  tags: {', '.join(e.get('tags',[]))}")
        print(f"  by: {e.get('human_author','?')} | {e.get('timestamp','?')[:10]}")

if __name__ == "__main__":
    main()
