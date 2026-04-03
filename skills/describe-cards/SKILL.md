---
name: describe-cards
description: "Reference documentation for Ushabti's Hieroglyphs-compatible card system — schema, lifecycle, directory structure, and Phase integration. Use when agents need to understand card format or work with `.ushabti/cards/`."
user-invocable: false
---

# Describe Cards

Ushabti uses Hieroglyphs-compatible cards to track work outside the current Phase. Cards are stored as directories containing a `card.md` file with YAML frontmatter and markdown body in `.ushabti/cards/{slug}/`.

## Card Schema

Nine required frontmatter fields in **alphabetical order**:

| Field | Type | Values |
|-------|------|--------|
| `created` | string | ISO 8601 timestamp (immutable after creation) |
| `id` | string | UUID v4 (lowercase, via `uuidgen`) |
| `priority` | string | `low`, `medium`, `high` |
| `slug` | string | kebab-case, matches directory name |
| `status` | string | `todo`, `backlog`, `in-progress`, `done` |
| `tags` | array | strings (may be empty `[]`) |
| `title` | string | human-readable card title |
| `type` | string | `bug`, `feature` |
| `updated` | string | ISO 8601 timestamp (set on every modification) |

## Directory Structure

```
.ushabti/cards/
├── improve-error-handling/
│   └── card.md
├── add-user-guide-agent/
│   └── card.md
└── fix-validation-bug/
    └── card.md
```

## File Format

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

[Context and motivation]

# Requirements

[Acceptance criteria]
```

The frontmatter must be valid YAML with all fields in alphabetical order. The markdown body requires at minimum `# Overview` and `# Requirements` sections.

## Card Lifecycle

```
todo → in-progress → done
  ↓
backlog
```

1. **Creation**: Card created with `status: todo` via `create-card` skill
2. **Planning**: Scribe reads card body to plan a Phase, adds `card: {slug}` to phase.md
3. **Implementation**: Status updated to `in-progress` during Phase execution
4. **Completion**: Overseer marks `status: done` via `complete-card` skill after Phase review

## Integration with Phases

When a Phase addresses a card:
- Scribe adds `card: {slug}` metadata to phase.md immediately after the title
- Builder implements the work described in the card's Requirements
- Overseer invokes `complete-card` to set `status: done` and documents it in review.md

## Frontmatter Preservation (CRITICAL)

When updating cards, preserve ALL existing frontmatter fields — including unknown fields that Hieroglyphs may have added. Dropping fields corrupts the card.

## Related Skills

- **create-card**: Create new cards
- **list-cards**: Scan and filter cards
- **complete-card**: Mark cards as done

## Notes

- Cards are never deleted — they serve as historical record
- Slug collisions are prevented during creation (verify directory doesn't exist)
- Cards use Hieroglyphs format for future integration with unified work tracking
