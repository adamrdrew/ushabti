#!/usr/bin/env python3
"""Dump everything Builder needs to start work."""

import os
import re
from pathlib import Path

phases_dir = Path(".ushabti/phases")

if not phases_dir.is_dir():
    print("No .ushabti/phases/ directory found.")
    exit(0)


def get_status(progress_text):
    """Extract phase-level status from progress.yaml."""
    m = re.search(r"^status:\s+(\S+)", progress_text, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r"^  status:\s+(\S+)", progress_text, re.MULTILINE)
    if m:
        return m.group(1)
    return None


def find_next_step(progress_text):
    """Find first step with implemented: false."""
    current_id = None
    for line in progress_text.splitlines():
        id_match = re.match(r"^\s{2}- id:\s+(.+)", line)
        if id_match:
            current_id = id_match.group(1).strip().strip('"')
        impl_match = re.match(r"^\s{4}implemented:\s+(.+)", line)
        if impl_match and current_id:
            if impl_match.group(1).strip().lower() == "false":
                return current_id
    return None


def count_steps(progress_text):
    impl = len(re.findall(r"^\s+implemented:\s+true", progress_text, re.MULTILINE))
    total = len(re.findall(r"^\s+implemented:\s+", progress_text, re.MULTILINE))
    return impl, total


# Find the active phase (building or planned, highest number first — most recently created)
current = None
for d in sorted(phases_dir.iterdir(), reverse=True):
    if not d.is_dir():
        continue
    progress_path = d / "progress.yaml"
    if not progress_path.exists():
        continue
    progress = progress_path.read_text()
    status = get_status(progress)
    if status in ("building", "planned"):
        current = (d, progress, status)
        break

if not current:
    print("No active phase (no phase with status: building or planned).")
    exit(0)

phase_dir, progress, status = current
impl, total = count_steps(progress)
next_step = find_next_step(progress)

print(f"=== PHASE CONTEXT ===")
print(f"Phase: {phase_dir.name}")
print(f"Path: {phase_dir.resolve()}")
print(f"Status: {status}")
print(f"Steps: {impl}/{total} implemented")
if next_step:
    print(f"Next step: {next_step}")
else:
    print("All steps implemented — ready for review")

for filename in ("phase.md", "steps.md", "progress.yaml"):
    filepath = phase_dir / filename
    if filepath.exists():
        print(f"\n--- {filename} ---")
        print(filepath.read_text())
    else:
        print(f"\n--- {filename} --- (not found)")
