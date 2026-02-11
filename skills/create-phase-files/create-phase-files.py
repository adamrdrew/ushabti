#!/usr/bin/env python3
"""Create a phase directory with all required files from stdin."""

import sys
from pathlib import Path

DELIMITERS = {
    "===PHASE===": "phase.md",
    "===STEPS===": "steps.md",
    "===PROGRESS===": "progress.yaml",
    "===REVIEW===": "review.md",
}

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <phase-dir>")
    print()
    print("Reads file contents from stdin, separated by delimiters:")
    print("  ===PHASE===      -> phase.md")
    print("  ===STEPS===      -> steps.md")
    print("  ===PROGRESS===   -> progress.yaml")
    print("  ===REVIEW===     -> review.md (optional)")
    sys.exit(1)

phase_dir = Path(sys.argv[1])

# Read all stdin
content = sys.stdin.read()

# Parse sections
sections = {}
current_file = None
current_lines = []

for line in content.splitlines():
    stripped = line.strip()
    if stripped in DELIMITERS:
        if current_file:
            sections[current_file] = "\n".join(current_lines).strip() + "\n"
        current_file = DELIMITERS[stripped]
        current_lines = []
    else:
        current_lines.append(line)

# Don't forget the last section
if current_file:
    sections[current_file] = "\n".join(current_lines).strip() + "\n"

if not sections:
    print("Error: No file sections found in stdin. Use ===PHASE===, ===STEPS===, etc. as delimiters.")
    sys.exit(1)

# Require at least phase.md, steps.md, and progress.yaml
required = {"phase.md", "steps.md", "progress.yaml"}
missing = required - set(sections.keys())
if missing:
    print(f"Error: Missing required sections: {', '.join(sorted(missing))}")
    sys.exit(1)

# Create directory
phase_dir.mkdir(parents=True, exist_ok=True)

# Write all files
for filename, file_content in sections.items():
    filepath = phase_dir / filename
    filepath.write_text(file_content)
    print(f"  created: {filepath}")

print(f"Phase directory ready: {phase_dir}")
