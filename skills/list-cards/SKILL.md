---
name: list-cards
description: "Scan and list Hieroglyphs-compatible cards in `.ushabti/cards/` with optional filtering by status, priority, or type. Use when reviewing available work items or determining which cards to plan next."
user-invocable: false
---

# List Cards

Scan and list all Hieroglyphs-compatible cards in `.ushabti/cards/`, with optional filtering by status, priority, or type.

## Procedure

1. **Find all cards**: `find .ushabti/cards -name "card.md" -type f`
2. **Parse frontmatter** for each card (extract slug, title, status, priority, type)
3. **Apply filters** if requested (status, priority, or type)
4. **Display** in a clear, scannable format

## Output Format

```
Cards in .ushabti/cards/:

  improve-error-handling
    Title: Improve error handling
    Status: todo
    Priority: medium
    Type: feature

  fix-validation-bug
    Title: Fix validation bug
    Status: in-progress
    Priority: high
    Type: bug
```

## Common Filters

- **Open work**: status is `todo`, `backlog`, or `in-progress`
- **Closed work**: status is `done`
- **Actionable work**: status is `todo` or `in-progress`

## Example: Filter by Status

```bash
for card in .ushabti/cards/*/card.md; do
  status=$(awk '/^---$/{flag=!flag;next}flag && /^status:/{print $2}' "$card")
  if [ "$status" = "todo" ]; then
    slug=$(basename $(dirname "$card"))
    title=$(awk '/^---$/{flag=!flag;next}flag && /^title:/{sub(/^title: /, ""); print}' "$card")
    echo "$slug: $title"
  fi
done
```

## Example: Filter by Priority

```bash
for card in .ushabti/cards/*/card.md; do
  priority=$(sed -n '/^---$/,/^---$/p' "$card" | grep '^priority:' | sed 's/^priority: //')
  if [ "$priority" = "high" ]; then
    slug=$(basename $(dirname "$card"))
    title=$(sed -n '/^---$/,/^---$/p' "$card" | grep '^title:' | sed 's/^title: //')
    echo "$slug: $title (priority: high)"
  fi
done
```

## Empty Results

Handle gracefully when no cards exist:

```bash
cards=(.ushabti/cards/*/card.md)
if [ "${cards[0]}" = ".ushabti/cards/*/card.md" ]; then
  echo "No cards found in .ushabti/cards/"
fi
```

## Notes

- Cards with `status: done` are closed but not removed
- Always verify `.ushabti/cards/` directory exists before scanning
- Card slugs are unique identifiers — no two cards share the same slug
