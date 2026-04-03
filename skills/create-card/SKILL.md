---
name: create-card
description: "Create a new Hieroglyphs-compatible card in `.ushabti/cards/{slug}/card.md` with UUID, YAML frontmatter, and markdown body. Use when capturing work items, bugs, or features outside the current Phase."
user-invocable: false
---

# Create Card

Create a new Hieroglyphs-compatible card to track work items, bugs, or features. Cards are stored in `.ushabti/cards/{slug}/card.md` with YAML frontmatter and markdown body.

## Procedure

1. **Validate inputs**: Ensure title, priority, and type are provided
2. **Derive slug**: Lowercase the title, replace spaces with hyphens, remove punctuation, collapse consecutive hyphens
3. **Check for collisions**: Verify `.ushabti/cards/{slug}/` doesn't exist
4. **Generate UUID**: Run `uuidgen | tr '[:upper:]' '[:lower:]'`
5. **Get timestamp**: `date -u +"%Y-%m-%dT%H:%M:%SZ"`
6. **Create directory**: `mkdir -p .ushabti/cards/{slug}/`
7. **Write card.md**: Create file with all nine frontmatter fields in alphabetical order plus markdown body
8. **Verify**: Ensure all fields present, alphabetically ordered, slug matches directory name

## Required Frontmatter Fields (alphabetical order)

| Field | Type | Values |
|-------|------|--------|
| `created` | string | ISO 8601 timestamp |
| `id` | string | UUID v4 (lowercase) |
| `priority` | string | `low`, `medium`, `high` |
| `slug` | string | kebab-case, matches directory name |
| `status` | string | `todo` (always for new cards) |
| `tags` | array | strings (empty `[]` for now) |
| `title` | string | human-readable title |
| `type` | string | `bug`, `feature` |
| `updated` | string | ISO 8601 timestamp (same as `created` initially) |

## Example

```bash
slug="add-user-guide-agent"
id=$(uuidgen | tr '[:upper:]' '[:lower:]')
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

mkdir -p ".ushabti/cards/${slug}/"

cat > ".ushabti/cards/${slug}/card.md" <<EOF
---
created: ${timestamp}
id: ${id}
priority: low
slug: ${slug}
status: todo
tags: []
title: Add user guide agent
type: feature
updated: ${timestamp}
---

# Overview

[Describe the context and motivation for this work item]

# Requirements

[List specific requirements or acceptance criteria]
EOF
```

## Validation Checklist

- All nine required frontmatter fields present and alphabetically ordered
- `id` is a valid lowercase UUID
- `created` and `updated` are ISO 8601 timestamps
- `status` is `todo`
- `slug` matches directory name exactly
- Markdown body has Overview and Requirements sections

## Notes

- New cards always start with `status: todo`
- Cards with `status: done` are considered closed (use `complete-card` skill)
- Unknown frontmatter fields MUST be preserved when updating cards (Hieroglyphs may add fields)
