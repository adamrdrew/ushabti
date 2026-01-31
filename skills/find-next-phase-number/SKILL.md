---
name: find-next-phase-number
description: Determine the next sequential phase ID for creating a new phase. Use when planning a new phase.
---

# Find Next Phase Number

Determine the next sequential phase ID when creating a new phase.

## Phase Numbering Convention

- Phase IDs are 4-digit, zero-padded integers: `0001`, `0002`, `0003`, ...
- Combined with a slug: `0001-initial-setup`, `0002-add-auth`, ...

## Commands

**Get the highest existing phase number:**
```bash
ls -1 .ushabti/phases/ 2>/dev/null | sed 's/-.*//' | sort -n | tail -1
```

**Calculate next phase number:**
```bash
current=$(ls -1 .ushabti/phases/ 2>/dev/null | sed 's/-.*//' | sort -n | tail -1)
if [ -z "$current" ]; then
  echo "0001"
else
  printf "%04d\n" $((10#$current + 1))
fi
```

## If No Phases Exist

If `.ushabti/phases/` is empty or doesn't exist, start with `0001`.

## Creating the Directory

Once you have the next number and a slug:
```bash
mkdir -p .ushabti/phases/0003-your-slug
```

Replace `0003` with the calculated number and `your-slug` with a short, lowercase, hyphenated description.
