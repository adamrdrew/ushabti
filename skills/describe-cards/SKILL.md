# Describe Cards

Comprehensive documentation of Ushabti's card system—the Hieroglyphs-compatible format for tracking work items, bugs, and features.

## Overview

Ushabti uses Hieroglyphs-compatible cards to track work outside the current Phase. Cards replace the previous ticket system, providing alignment with the Hieroglyphs task management tool.

Cards are stored as individual directories containing a `card.md` file with YAML frontmatter and markdown body. Unlike the old ticket system (flat YAML files with sequential IDs), cards use UUIDs and status fields to track lifecycle state.

## Card Schema

Each card has **nine required frontmatter fields**, listed in alphabetical order:

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `created` | string | ISO 8601 timestamp | When the card was created (immutable) |
| `id` | string | UUID v4 | Unique identifier (generated via `uuidgen`) |
| `priority` | string | `low`, `medium`, `high` | Urgency level |
| `slug` | string | kebab-case | Human-readable identifier matching directory name |
| `status` | string | `todo`, `backlog`, `in-progress`, `done` | Lifecycle state |
| `tags` | array | strings | Categorization tags (may be empty) |
| `title` | string | any | Human-readable card title |
| `type` | string | `bug`, `feature` | Work item type |
| `updated` | string | ISO 8601 timestamp | Last modification time |

### Field Details

**`created`**: ISO 8601 timestamp of card creation. Never changes after creation.
- Example: `2026-02-08T14:30:00Z`
- Format: `YYYY-MM-DDTHH:MM:SSZ` (UTC time with `Z` suffix)

**`id`**: UUID v4 identifier. Globally unique across all cards.
- Example: `550e8400-e29b-41d4-a716-446655440000`
- Generate: `uuidgen | tr '[:upper:]' '[:lower:]'`

**`priority`**: Urgency or importance level.
- `low`: Can be deferred; no immediate pressure
- `medium`: Should be addressed reasonably soon
- `high`: Urgent; should be prioritized

**`slug`**: Human-readable identifier derived from title. Must match directory name exactly.
- Example: `improve-error-handling`
- Rules: lowercase, kebab-case, no punctuation except hyphens

**`status`**: Current lifecycle state.
- `todo`: Ready to work on (default for new cards)
- `backlog`: Deprioritized; may be addressed later
- `in-progress`: Currently being implemented
- `done`: Completed and closed

**`tags`**: Array of categorization tags (reserved for future use).
- Example: `[]` (empty), `["documentation", "agent"]`

**`title`**: Human-readable card title.
- Example: `Improve error handling`

**`type`**: Nature of the work.
- `bug`: Fix incorrect behavior
- `feature`: Add new functionality

**`updated`**: ISO 8601 timestamp of last modification. Updated when status changes or other edits occur.
- Example: `2026-02-08T15:45:00Z`

## Directory Structure

Cards are stored in directories under `.ushabti/cards/`:

```
.ushabti/cards/
├── improve-error-handling/
│   └── card.md
├── add-user-guide-agent/
│   └── card.md
└── fix-validation-bug/
    └── card.md
```

Each card gets its own directory named after its slug. The directory contains a single `card.md` file.

## File Format

Card files use YAML frontmatter followed by markdown content:

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

### Frontmatter Section

- Delimited by `---` lines (YAML frontmatter markers)
- Contains all nine required fields in **alphabetical order**
- Must be valid YAML
- May contain additional fields (preserve them when updating)

### Markdown Body

- Begins after the closing `---` delimiter
- Contains at minimum:
  - `# Overview`: Context and motivation for the work
  - `# Requirements`: Specific acceptance criteria or implementation details
- Additional sections may be added as needed

## Card Lifecycle

Cards progress through states as work advances:

1. **Creation**: Card created with `status: todo`
2. **Planning**: Scribe reads card body to plan a Phase
3. **Implementation**: Card status may be updated to `in-progress` during Phase
4. **Completion**: Overseer marks card `status: done` after Phase review succeeds

Status flow:
```
todo → in-progress → done
  ↓
backlog
```

- **todo**: Default state; ready to work on
- **in-progress**: Active work happening
- **done**: Work completed and verified
- **backlog**: Deprioritized; may return to `todo` later

## Differences from Ticket System

The card system replaced Ushabti's original ticket system. Key differences:

| Aspect | Old Ticket System | New Card System |
|--------|-------------------|-----------------|
| ID format | Sequential (T0001, T0002) | UUID v4 |
| Storage | Flat YAML files | Directory + card.md |
| Status tracking | Archival directory (`.archived/`) | Status field (`done`) |
| Format | Single YAML file | YAML frontmatter + markdown body |
| Hierarchy | Flat list | Slug-based directories |
| Compatibility | Ushabti-specific | Hieroglyphs-compatible |

## Integration with Phases

Cards integrate with Ushabti's Phase workflow:

1. **Card created**: Agent discovers work needing attention (e.g., technical debt, bug)
2. **Scribe plans Phase**: When planning a Phase to address a card, Scribe:
   - Reads the card's body content (Overview, Requirements)
   - Adds `card: {slug}` metadata to phase.md immediately after title
3. **Phase executes**: Builder implements; Overseer reviews
4. **Card completed**: After successful review, Overseer:
   - Invokes `complete-card` skill to set `status: done`
   - Documents the action in review.md (e.g., "Marked card `improve-error-handling` as done")

## Hieroglyphs Compatibility

Cards use the canonical Hieroglyphs format, enabling future integration:
- YAML frontmatter with alphabetically ordered fields
- UUID identifiers (not sequential IDs)
- Status field for lifecycle tracking (not archival directories)
- Markdown body for human-readable content

This alignment means Hieroglyphs can eventually ingest cards created by Ushabti agents, providing unified work tracking across both tools.

## Example Cards

### Bug Card

```markdown
---
created: 2026-02-08T10:00:00Z
id: 7c9e6679-7425-40de-944b-e07fc1f90ae7
priority: high
slug: fix-validation-error
status: todo
tags: []
title: Fix validation error in plugin.json
type: bug
updated: 2026-02-08T10:00:00Z
---

# Overview

Plugin validation fails when agent files contain certain YAML structures.
The validator incorrectly rejects valid frontmatter.

# Requirements

- Identify root cause of validation failure
- Update validation logic to accept valid YAML
- Add test cases for edge cases
- Verify all existing agents pass validation
```

### Feature Card

```markdown
---
created: 2026-02-08T11:00:00Z
id: c7e89b45-3a2f-4f8b-9c1e-6d5a3b8f4e2a
priority: low
slug: add-card-search
status: backlog
tags: ["enhancement"]
title: Add card search capability
type: feature
updated: 2026-02-08T11:30:00Z
---

# Overview

Agents currently list all cards or filter by status. Add ability to
search card content for keywords.

# Requirements

- Search card titles and markdown body
- Support basic regex patterns
- Return matching cards with context (line numbers, snippets)
- Integrate with list-cards skill
```

## Related Skills

- **create-card**: Create new cards
- **list-cards**: Scan and filter cards
- **complete-card**: Mark cards as done

## Notes

- Cards are the single source of truth for work items tracked outside the current Phase
- Never delete cards—they serve as historical record
- Preserve unknown frontmatter fields when updating (Hieroglyphs may add fields)
- Slug collisions are prevented during creation (verify directory doesn't exist)
- Phase 0012 and 0013 document the historical ticket system
