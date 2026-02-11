#!/usr/bin/env python3
"""Dump everything Overseer needs to start a review."""

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


def count_steps(progress_text):
    impl = len(re.findall(r"^\s+implemented:\s+true", progress_text, re.MULTILINE))
    total = len(re.findall(r"^\s+implemented:\s+", progress_text, re.MULTILINE))
    return impl, total


def find_card_slug(phase_md_text):
    """Extract card slug from phase.md if present."""
    m = re.search(r"^card:\s+(\S+)", phase_md_text, re.MULTILINE)
    return m.group(1) if m else None


# Find the phase in review (highest number first — most recently moved to review)
current = None
for d in sorted(phases_dir.iterdir(), reverse=True):
    if not d.is_dir():
        continue
    progress_path = d / "progress.yaml"
    if not progress_path.exists():
        continue
    progress = progress_path.read_text()
    status = get_status(progress)
    if status == "review":
        current = (d, progress, status)
        break

if not current:
    print("No phase in review (no phase with status: review).")
    exit(0)

phase_dir, progress, status = current
impl, total = count_steps(progress)

phase_md = ""
phase_md_path = phase_dir / "phase.md"
if phase_md_path.exists():
    phase_md = phase_md_path.read_text()

card_slug = find_card_slug(phase_md)

print(f"=== PHASE CONTEXT ===")
print(f"Phase: {phase_dir.name}")
print(f"Path: {phase_dir.resolve()}")
print(f"Status: {status}")
print(f"Steps: {impl}/{total} implemented")
if card_slug:
    print(f"Card: {card_slug}")

for filename in ("phase.md", "steps.md", "progress.yaml", "review.md"):
    filepath = phase_dir / filename
    if filepath.exists():
        print(f"\n--- {filename} ---")
        print(filepath.read_text())
    else:
        print(f"\n--- {filename} --- (not found)")
