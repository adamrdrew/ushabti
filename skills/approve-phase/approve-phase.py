#!/usr/bin/env python3
"""Approve a phase: set status to complete, mark all steps reviewed, update card if linked."""

import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def get_phase_status(text):
    """Extract current phase status."""
    m = re.search(r"^  status:\s+(\S+)", text, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r"^status:\s+(\S+)", text, re.MULTILINE)
    if m:
        return m.group(1)
    return None


def set_status_complete(text):
    """Set phase status to complete."""
    if re.search(r"^phase:", text, re.MULTILINE):
        return re.sub(
            r"^(  status:\s+)\S+", r"\g<1>complete", text, count=1, flags=re.MULTILINE
        )
    else:
        return re.sub(
            r"^(status:\s+)\S+", r"\g<1>complete", text, count=1, flags=re.MULTILINE
        )


def mark_all_reviewed(text):
    """Set reviewed: true for all steps."""
    return re.sub(
        r"^(\s+reviewed:\s+)\S+",
        r"\g<1>true",
        text,
        flags=re.MULTILINE,
    )


def find_card_slug(phase_md_text):
    """Extract card slug from phase.md."""
    m = re.search(r"^card:\s+(\S+)", phase_md_text, re.MULTILINE)
    return m.group(1) if m else None


def update_card(card_path, timestamp):
    """Update card status to done and set updated timestamp."""
    text = card_path.read_text()
    text = re.sub(r"^(status:\s+)\S+", r"\g<1>done", text, count=1, flags=re.MULTILINE)
    text = re.sub(
        r"^(updated:\s+).*$",
        rf"\g<1>'{timestamp}'",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    card_path.write_text(text)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <phase-dir>")
        sys.exit(1)

    phase_dir = Path(sys.argv[1])
    progress_path = phase_dir / "progress.yaml"
    phase_md_path = phase_dir / "phase.md"

    if not progress_path.exists():
        print(f"Error: {progress_path} not found")
        return 1

    # Check current status
    progress_text = progress_path.read_text()
    current_status = get_phase_status(progress_text)
    if current_status != "review":
        print(f"Warning: Phase status is '{current_status}', expected 'review'. Proceeding anyway.")

    # Update progress.yaml
    progress_text = set_status_complete(progress_text)
    progress_text = mark_all_reviewed(progress_text)
    progress_path.write_text(progress_text)
    print("Phase status: complete")
    print("All steps: reviewed")

    # Check for linked card
    if phase_md_path.exists():
        phase_md = phase_md_path.read_text()
        card_slug = find_card_slug(phase_md)
        if card_slug:
            # Look for card in .ushabti/cards/
            card_path = Path(".ushabti/cards") / card_slug / "card.md"
            if card_path.exists():
                timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                update_card(card_path, timestamp)
                print(f"Card '{card_slug}': marked done")
            else:
                print(f"Card '{card_slug}': not found at {card_path}, skipped")
        else:
            print("No linked card")
    else:
        print("No phase.md found, skipped card check")

    return 0


if __name__ == "__main__":
    sys.exit(main())
