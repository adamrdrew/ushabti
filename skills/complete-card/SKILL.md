---
name: complete-card
description: "Mark a Hieroglyphs-compatible card as done by updating its status and timestamp in `.ushabti/cards/{slug}/card.md`. Use when a Phase addressing the card has been completed and reviewed by the Overseer."
user-invocable: false
---

# Complete Card

Mark a card as done by updating its `status` field to `done` and setting the `updated` timestamp. Completed cards remain in `.ushabti/cards/` as historical record — they are not moved or deleted.

## Procedure

1. **Verify card exists**: Check that `.ushabti/cards/{slug}/card.md` exists
2. **Read card**: Load entire file contents
3. **Parse frontmatter**: Extract YAML frontmatter section (between `---` delimiters)
4. **Update status**: Change `status` field to `done`
5. **Update timestamp**: Set `updated` field to current UTC time in ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`)
6. **Preserve all fields**: Keep all existing frontmatter fields in alphabetical order, including unknown fields added by Hieroglyphs
7. **Write back**: Replace card.md with updated content, preserving the markdown body unchanged
8. **Verify**: Confirm status and updated fields changed

## Frontmatter Preservation (CRITICAL)

When updating a card, you MUST preserve all existing frontmatter fields, including fields you don't recognize. Hieroglyphs may add additional fields that agents don't know about. Dropping unknown fields will corrupt the card.

## Example

```bash
slug="improve-error-handling"
card_path=".ushabti/cards/${slug}/card.md"
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Create temporary file
temp_file=$(mktemp)

# Update frontmatter while preserving all fields and structure
awk -v ts="$timestamp" '
  BEGIN { in_frontmatter=0; first_delimiter=0 }
  /^---$/ {
    if (!first_delimiter) { first_delimiter=1; in_frontmatter=1 }
    else if (in_frontmatter) { in_frontmatter=0 }
    print; next
  }
  in_frontmatter && /^status:/ { print "status: done"; next }
  in_frontmatter && /^updated:/ { print "updated: " ts; next }
  { print }
' "$card_path" > "$temp_file"

mv "$temp_file" "$card_path"
echo "Card ${slug} marked as done"
```

## Verification

```bash
grep '^status:' "$card_path"
# Expected: status: done

grep '^updated:' "$card_path"
# Expected: updated: <current timestamp>
```

## Notes

- Cards with `status: done` should be excluded from "open work" listings
- The `updated` timestamp tracks the last modification time
- Never delete cards — they serve as historical record of work items
