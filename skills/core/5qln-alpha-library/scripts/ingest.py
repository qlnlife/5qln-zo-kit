#!/usr/bin/env python3
"""
α-Library Ingest — Deposit a completed cycle's outputs.
Usage:
  python3 ingest.py --file <memory.yaml or cycle-output.json>
  python3 ingest.py --project <project-name>
  python3 ingest.py --stdin  (reads JSON from stdin)
"""
import json, sys, os, uuid, argparse
from datetime import datetime, timezone
from pathlib import Path

LIBRARY_PATH = Path(__file__).parent.parent.parent.parent / "5qln-alpha-library" / "library.json"

def load():
    if not LIBRARY_PATH.exists():
        LIBRARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        return {"version": 1, "codex": "feaa46b4", "entries": []}
    return json.loads(LIBRARY_PATH.read_text())

def save(lib):
    LIBRARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    LIBRARY_PATH.write_text(json.dumps(lib, indent=2))

def ingest_entry(lib, entry_data):
    entry = {
        "id": str(uuid.uuid4()),
        "source_cycle": entry_data.get("source_cycle", "unknown"),
        "phase": entry_data.get("phase", "?"),
        "domain": entry_data.get("domain", "unknown"),
        "skill_reference": entry_data.get("skill_reference", ""),
        "content": {
            "alpha_pattern": entry_data.get("alpha_pattern", ""),
            "alpha_expressions": entry_data.get("alpha_expressions", []),
            "resonance": entry_data.get("resonance", ""),
            "gradient": entry_data.get("gradient", ""),
            "artifact": entry_data.get("artifact", "")
        },
        "human_author": entry_data.get("human_author", "amihai"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tags": entry_data.get("tags", []),
        "epistemic_register": entry_data.get("epistemic_register", "STRUCTURAL-HYPOTHESIS"),
        "sealed": entry_data.get("sealed", False)
    }
    lib["entries"].append(entry)
    return entry

def main():
    parser = argparse.ArgumentParser(description="Ingest into 5QLN α-Library")
    parser.add_argument("--file", default="", help="Path to cycle output JSON")
    parser.add_argument("--project", default="", help="Project name to scan for memory.yaml")
    parser.add_argument("--stdin", action="store_true", help="Read JSON from stdin")
    parser.add_argument("--alpha", default="", help="Alpha pattern text (quick ingest)")
    parser.add_argument("--resonance", default="", help="Resonance text (quick ingest)")
    parser.add_argument("--domain", default="unknown", help="Domain name")
    parser.add_argument("--phase", default="G", help="Phase: G, Q, P, V")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    args = parser.parse_args()

    lib = load()

    if args.stdin:
        data = json.loads(sys.stdin.read())
        if isinstance(data, list):
            for d in data:
                ingest_entry(lib, d)
        else:
            ingest_entry(lib, data)
        save(lib)
        print(f"Ingested. Library now: {len(lib['entries'])} entries")
        return

    if args.file:
        data = json.loads(Path(args.file).read_text())
        if isinstance(data, list):
            for d in data:
                ingest_entry(lib, d)
        else:
            ingest_entry(lib, data)
        save(lib)
        print(f"Ingested from {args.file}. Library now: {len(lib['entries'])} entries")
        return

    if args.alpha:
        entry = ingest_entry(lib, {
            "source_cycle": "quick-ingest",
            "phase": args.phase,
            "domain": args.domain,
            "alpha_pattern": args.alpha,
            "resonance": args.resonance,
            "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
            "sealed": False
        })
        save(lib)
        print(f"Ingested quick entry: {entry['id'][:8]}...")
        return

    print("No input source specified. Use --stdin, --file, or --alpha", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
