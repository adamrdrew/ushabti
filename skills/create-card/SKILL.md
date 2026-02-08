# Create Card

Create a new Hieroglyphs-compatible card to track work items, bugs, or features. Cards use the Hieroglyphs format with YAML frontmatter and markdown body, stored in `.ushabti/cards/{slug}/card.md` directories.

## When to Use

Create a card when:
- Discovering technical debt that should be tracked
- Identifying a bug or issue that should be addressed later
- Capturing a feature request or improvement idea
- Recording any work item that should be tracked separately from the current Phase

## Card Schema

Cards MUST have these frontmatter fields in **alphabetical order**:

- `created`: ISO 8601 timestamp (e.g., `2026-02-08T14:30:00Z`)
- `id`: UUID v4 (generated via `uuidgen` command)
- `priority`: One of `low`, `medium`, `high`
- `slug`: Lowercase kebab-case identifier matching directory name
- `status`: One of `todo`, `backlog`, `in-progress`, `done`
- `tags`: Array of strings (may be empty: `[]`)
- `title`: Human-readable card title
- `type`: One of `bug`, `feature`
- `updated`: ISO 8601 timestamp (same as `created` when first created)

## Slug Derivation

The slug is derived from the title:
1. Convert to lowercase
2. Replace spaces with hyphens
3. Remove all punctuation except hyphens
4. Collapse multiple consecutive hyphens to single hyphen
5. Strip leading and trailing hyphens

Examples:
- "Fix error handling" → `fix-error-handling`
- "Add user guide agent!" → `add-user-guide-agent`
- "Bug: broken validation" → `bug-broken-validation`

## Directory Structure

Cards are stored in directories named after their slug:

```
.ushabti/cards/{slug}/card.md
```

Before creating a card, verify the directory doesn't already exist to prevent slug collisions.

## File Format

Card files use YAML frontmatter delimited by `---`, followed by markdown content:

```markdown
---
created: 2026-02-08T14:30:00Z
id: 550e8400-e29b-41d4-a716-446655440000
priority: medium
slug: improve-error-handling
status: todo
tags: []
title: Improve error handling
type: feature
updated: 2026-02-08T14:30:00Z
---

# Overview

Current error handling is inconsistent across agents. Some failures
are silent, making debugging difficult.

# Requirements

- Define standard error response format
- Update all agents to use consistent error handling
- Add error recovery examples to documentation
```

## Procedure

1. **Validate inputs**: Ensure title, priority, and type are provided
2. **Derive slug**: Apply slug derivation rules to title
3. **Check for collisions**: Verify `.ushabti/cards/{slug}/` doesn't exist
4. **Generate UUID**: Run `uuidgen` command (lowercase the output)
5. **Get timestamp**: Generate current UTC time in ISO 8601 format: `date -u +"%Y-%m-%dT%H:%M:%SZ"`
6. **Create directory**: `mkdir -p .ushabti/cards/{slug}/`
7. **Write card.md**: Create file with frontmatter and markdown body
8. **Verify**: Ensure all frontmatter fields are present and alphabetically ordered

## Validation Checklist

Before completing card creation, verify:
- [ ] All nine required frontmatter fields are present
- [ ] Frontmatter fields are in alphabetical order
- [ ] `id` is a valid UUID (lowercase)
- [ ] `created` and `updated` are ISO 8601 timestamps
- [ ] `status` is `todo` (default for new cards)
- [ ] `priority` is one of `low`, `medium`, `high`
- [ ] `type` is one of `bug`, `feature`
- [ ] `slug` matches directory name exactly
- [ ] Markdown body has Overview and Requirements sections
- [ ] Directory `.ushabti/cards/{slug}/` exists and contains `card.md`

## Example

Creating a card with title "Add user guide agent", priority "low", type "feature":

```bash
# Derive slug
slug="add-user-guide-agent"

# Generate UUID and timestamp
id=$(uuidgen | tr '[:upper:]' '[:lower:]')
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Create directory
mkdir -p ".ushabti/cards/${slug}/"

# Write card.md
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

## Notes

- New cards always start with `status: todo`
- The `tags` field is reserved for future use; use empty array for now
- Cards with `status: done` are considered closed (use `complete-card` skill to update status)
- Unknown frontmatter fields MUST be preserved when updating cards (Hieroglyphs may add fields agents don't know about)
