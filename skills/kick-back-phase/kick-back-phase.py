#!/usr/bin/env python3
"""Kick a phase back to building: set status, add new step entries to progress.yaml."""

import re
import sys
from pathlib import Path


def find_highest_step_num(text):
    """Find the highest numeric step ID in progress.yaml."""
    # Match IDs like S001, S002 or bare 1, 2, etc.
    ids = re.findall(r"^\s+-\s*id:\s+['\"]?S?(\d+)", text, re.MULTILINE)
    if ids:
        return max(int(x) for x in ids)
    return 0


def detect_id_format(text):
    """Detect whether step IDs use S-prefix (S001) or bare numbers (1)."""
    if re.search(r"^\s+-\s*id:\s+S\d+", text, re.MULTILINE):
        return "s-prefix"
    return "bare"


def detect_indent_and_fields(text):
    """Detect indentation level and field names used in step entries."""
    # Check if 'touched' or 'files' is used
    if re.search(r"^\s+touched:", text, re.MULTILINE):
        file_field = "touched"
    elif re.search(r"^\s+files:", text, re.MULTILINE):
        file_field = "files"
    else:
        file_field = "touched"

    # Detect indentation of step fields (e.g., '    implemented:')
    m = re.search(r"^(\s+)implemented:", text, re.MULTILINE)
    field_indent = m.group(1) if m else "    "

    # Detect indentation of step list item (e.g., '  - id:')
    m = re.search(r"^(\s+)-\s*id:", text, re.MULTILINE)
    item_indent = m.group(1) if m else "  "

    return item_indent, field_indent, file_field


def main():
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <phase-dir> <title-1> [<title-2> ...]")
        print("Each title becomes a new step entry with implemented: false, reviewed: false.")
        sys.exit(1)

    phase_dir = Path(sys.argv[1])
    new_titles = sys.argv[2:]

    progress_path = phase_dir / "progress.yaml"
    if not progress_path.exists():
        print(f"Error: {progress_path} not found")
        return 1

    text = progress_path.read_text()

    # Set status to building
    if re.search(r"^phase:", text, re.MULTILINE):
        text = re.sub(
            r"^(  status:\s+)\S+", r"\g<1>building", text, count=1, flags=re.MULTILINE
        )
    elif re.search(r"^status:", text, re.MULTILINE):
        text = re.sub(
            r"^(status:\s+)\S+", r"\g<1>building", text, count=1, flags=re.MULTILINE
        )

    # Detect format
    highest = find_highest_step_num(text)
    id_fmt = detect_id_format(text)
    item_indent, field_indent, file_field = detect_indent_and_fields(text)

    # Generate new step entries
    new_entries = []
    new_ids = []
    for i, title in enumerate(new_titles, start=highest + 1):
        if id_fmt == "s-prefix":
            step_id = f"S{i:03d}"
        else:
            step_id = str(i)
        new_ids.append(step_id)

        entry = (
            f"{item_indent}- id: {step_id}\n"
            f"{field_indent}title: {title}\n"
            f"{field_indent}implemented: false\n"
            f"{field_indent}reviewed: false\n"
            f'{field_indent}notes: ""\n'
            f"{field_indent}{file_field}: []"
        )
        new_entries.append(entry)

    # Append new entries to the end of the file
    if not text.endswith("\n"):
        text += "\n"
    text += "\n".join(new_entries) + "\n"

    progress_path.write_text(text)

    print(f"Phase status: building")
    print(f"Added {len(new_ids)} follow-up steps:")
    for sid, title in zip(new_ids, new_titles):
        print(f"  {sid}: {title}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
