#!/usr/bin/env python3
"""
α-Library Stats — Summary statistics on accumulated patterns.
Usage: python3 stats.py [--json]
"""
import json, sys
from pathlib import Path
from collections import Counter

LIBRARY_PATH = Path(__file__).parent.parent.parent.parent / "5qln-alpha-library" / "library.json"

def main():
    if not LIBRARY_PATH.exists():
        print("α-Library: empty (no library.json found)")
        return

    lib = json.loads(LIBRARY_PATH.read_text())
    entries = lib.get("entries", [])

    if not entries:
        print("α-Library: empty (0 entries)")
        return

    domains = Counter(e.get("domain","?") for e in entries)
    phases = Counter(e.get("phase","?") for e in entries)
    tags = Counter()
    for e in entries:
        for t in e.get("tags", []):
            tags[t] += 1
    sealed = sum(1 for e in entries if e.get("sealed"))
    registers = Counter(e.get("epistemic_register","?") for e in entries)

    print(f"α-Library Stats")
    print("=" * 60)
    print(f"  Total entries:   {len(entries)}")
    print(f"  Sealed:          {sealed}")
    print(f"  Unsealed:        {len(entries) - sealed}")
    print(f"\n  By domain:")
    for d,c in domains.most_common():
        print(f"    {d}: {c}")
    print(f"\n  By phase:")
    for p,c in sorted(phases.items()):
        print(f"    {p}: {c}")
    print(f"\n  By register:")
    for r,c in sorted(registers.items()):
        print(f"    {r}: {c}")
    if tags:
        print(f"\n  Top tags:")
        for t,c in tags.most_common(10):
            print(f"    {t}: {c}")

    if "--json" in sys.argv:
        print(json.dumps({
            "total": len(entries), "sealed": sealed,
            "domains": dict(domains), "phases": dict(phases),
            "tags": dict(tags), "registers": dict(registers)
        }, indent=2))

if __name__ == "__main__":
    main()
