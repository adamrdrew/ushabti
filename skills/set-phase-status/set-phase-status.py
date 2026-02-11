#!/usr/bin/env python3
"""Set the status field in a phase's progress.yaml."""

import re
import sys
from pathlib import Path

VALID_STATUSES = ("planned", "building", "review", "complete")

if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} <phase-dir> <status>")
    print(f"Valid statuses: {', '.join(VALID_STATUSES)}")
    sys.exit(1)

phase_dir = Path(sys.argv[1])
new_status = sys.argv[2].lower()

if new_status not in VALID_STATUSES:
    print(f"Error: Invalid status '{new_status}'. Must be one of: {', '.join(VALID_STATUSES)}")
    sys.exit(1)

progress_path = phase_dir / "progress.yaml"
if not progress_path.exists():
    print(f"Error: {progress_path} not found")
    sys.exit(1)

text = progress_path.read_text()

# Handle nested format: "  status: X" under "phase:"
if re.search(r"^phase:", text, re.MULTILINE):
    text = re.sub(
        r"^(  status:\s+)\S+",
        rf"\g<1>{new_status}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
# Handle flat format: "status: X" at root level
elif re.search(r"^status:", text, re.MULTILINE):
    text = re.sub(
        r"^(status:\s+)\S+",
        rf"\g<1>{new_status}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
else:
    print("Error: No status field found in progress.yaml")
    sys.exit(1)

progress_path.write_text(text)
print(f"Phase status set to: {new_status}")
