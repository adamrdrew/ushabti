# Complete Card

Mark a card as done by updating its status field to `done` and setting the updated timestamp. This replaces the old ticket archival system where tickets were moved to an `.archived/` directory.

## When to Use

Mark a card complete when:
- A Phase addressing the card's work has been completed and reviewed
- The work item has been fully implemented and verified
- The Overseer determines the card's requirements are satisfied

## Status Update

Cards track their lifecycle state in the `status` frontmatter field:
- `todo`: Not yet started (default for new cards)
- `backlog`: Deprioritized or deferred
- `in-progress`: Currently being worked on
- `done`: Completed and closed

Completing a card means setting `status: done`.

## Timestamp Update

When marking a card complete, also update the `updated` field to the current UTC time in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`

Example: `2026-02-08T14:30:00Z`

Generate timestamp:
```bash
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

## Frontmatter Preservation

**CRITICAL**: When updating a card, you MUST preserve all existing frontmatter fields, including fields you don't recognize. Hieroglyphs may add additional fields that agents don't know about. Dropping unknown fields will corrupt the card.

Strategy:
1. Read the entire card file
2. Parse the frontmatter section
3. Update only the `status` and `updated` fields
4. Write back the complete frontmatter with all original fields intact
5. Preserve the markdown body unchanged

## Procedure

1. **Verify card exists**: Check that `.ushabti/cards/{slug}/card.md` exists
2. **Read card**: Load entire file contents
3. **Parse frontmatter**: Extract YAML frontmatter section (between `---` delimiters)
4. **Update status**: Change `status` field to `done`
5. **Update timestamp**: Set `updated` field to current UTC time
6. **Preserve alphabetical order**: Keep frontmatter fields sorted alphabetically
7. **Write back**: Replace card.md with updated content
8. **Verify**: Confirm status and updated fields changed

## Example Implementation

```bash
slug="improve-error-handling"
card_path=".ushabti/cards/${slug}/card.md"

# Verify card exists
if [ ! -f "$card_path" ]; then
  echo "Error: Card not found: $card_path"
  exit 1
fi

# Generate new timestamp
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Read current card
current_content=$(cat "$card_path")

# Update status and timestamp using sed
# This example assumes frontmatter is well-formed
updated_content=$(echo "$current_content" | sed "s/^status: .*/status: done/" | sed "s/^updated: .*/updated: ${timestamp}/")

# Write back
echo "$updated_content" > "$card_path"

echo "Card ${slug} marked as done"
```

## Safe Update with awk

For more robust parsing that preserves unknown fields:

```bash
slug="example-card"
card_path=".ushabti/cards/${slug}/card.md"
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Create temporary file
temp_file=$(mktemp)

# Update frontmatter while preserving structure
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

# Replace original
mv "$temp_file" "$card_path"
```

## Verification

After updating, verify the changes:

```bash
# Check status field
grep '^status:' "$card_path"
# Expected: status: done

# Check updated timestamp
grep '^updated:' "$card_path"
# Expected: updated: <current timestamp>

# Verify frontmatter is still valid YAML
sed -n '/^---$/,/^---$/p' "$card_path" | sed '1d;$d'
```

## Common Issues

**Issue**: Frontmatter order changes during update
**Solution**: Manually restore alphabetical order or use YAML-aware tools

**Issue**: Unknown fields dropped during update
**Solution**: Parse more carefully, preserving all fields not explicitly updated

**Issue**: Markdown body corrupted
**Solution**: Only modify the frontmatter section; everything after the closing `---` should remain unchanged

## Notes

- Completed cards remain in `.ushabti/cards/` (they are NOT moved to a separate directory)
- Cards with `status: done` should be excluded from "open work" listings
- The `updated` timestamp tracks the last modification time (creation, status change, or any other update)
- Never delete cards—they serve as historical record of work items
