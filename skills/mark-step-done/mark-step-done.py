#!/usr/bin/env python3
"""Mark a step as implemented in a phase's progress.yaml."""

import argparse
import re
import sys
from pathlib import Path


def find_step_range(lines, step_id):
    """Find the line range for a step entry by its ID."""
    start = None
    # Match step ID as string or number, quoted or unquoted
    id_pattern = re.compile(
        r"^\s+-\s*id:\s+['\"]?" + re.escape(str(step_id)) + r"['\"]?\s*$"
    )
    step_pattern = re.compile(r"^\s+-\s*id:")

    for i, line in enumerate(lines):
        if id_pattern.match(line):
            start = i
        elif start is not None and step_pattern.match(line):
            return start, i
    if start is not None:
        return start, len(lines)
    return None, None


def update_field(lines, start, end, field, value):
    """Update a field value within a line range."""
    field_pattern = re.compile(rf"^(\s+){field}:\s+.*$")
    for i in range(start, end):
        m = field_pattern.match(lines[i])
        if m:
            indent = m.group(1)
            lines[i] = f"{indent}{field}: {value}"
            return True
    return False


def update_list_field(lines, start, end, field, values):
    """Update a list field (touched/files) within a line range."""
    field_pattern = re.compile(rf"^(\s+)({field}):\s*(.*)$")
    for i in range(start, end):
        m = field_pattern.match(lines[i])
        if m:
            indent = m.group(1)
            fname = m.group(2)
            rest = m.group(3).strip()

            # Remove any existing list items following this field
            j = i + 1
            item_pattern = re.compile(rf"^{indent}\s+-\s+")
            while j < end and item_pattern.match(lines[j]):
                j += 1
            # Delete old list items
            del lines[i + 1 : j]
            end -= j - (i + 1)

            if not values:
                lines[i] = f"{indent}{fname}: []"
            else:
                lines[i] = f"{indent}{fname}:"
                for idx, v in enumerate(reversed(values)):
                    lines.insert(i + 1, f"{indent}  - {v}")
            return True, end
    return False, end


def main():
    parser = argparse.ArgumentParser(description="Mark a step as implemented")
    parser.add_argument("phase_dir", help="Path to the phase directory")
    parser.add_argument("step_id", help="Step ID (e.g., S001 or 1)")
    parser.add_argument("--notes", help="Notes about the completed step", default=None)
    parser.add_argument(
        "--files", nargs="*", help="Files touched by this step", default=None
    )
    args = parser.parse_args()

    progress_path = Path(args.phase_dir) / "progress.yaml"
    if not progress_path.exists():
        print(f"Error: {progress_path} not found")
        return 1

    lines = progress_path.read_text().splitlines()
    start, end = find_step_range(lines, args.step_id)

    if start is None:
        print(f"Error: Step '{args.step_id}' not found in progress.yaml")
        return 1

    update_field(lines, start, end, "implemented", "true")

    if args.notes is not None:
        # Quote notes if they contain special YAML characters
        note_val = f'"{args.notes}"' if any(c in args.notes for c in ":{}[]#&*!|>',") else args.notes
        update_field(lines, start, end, "notes", note_val)

    if args.files is not None:
        # Try 'touched' first, then 'files'
        updated, end = update_list_field(lines, start, end, "touched", args.files)
        if not updated:
            update_list_field(lines, start, end, "files", args.files)

    progress_path.write_text("\n".join(lines) + "\n")
    print(f"Step {args.step_id}: marked implemented")
    if args.notes:
        print(f"  notes: {args.notes}")
    if args.files:
        print(f"  files: {', '.join(args.files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
