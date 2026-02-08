# Phase 0014: Hieroglyphs Card System

## Intent

Replace Ushabti's ticket system with Hieroglyphs-compatible cards to align the two systems. Agents will create, read, and manage cards using the Hieroglyphs card format (YAML frontmatter + markdown body in `{slug}/card.md` directories) instead of flat YAML ticket files. This enables Hieroglyphs to eventually ingest cards created by agents during development, providing a unified work tracking system across both tools.

## Scope

**In scope:**
- Replace five ticket skills (create-ticket, list-tickets, archive-ticket, describe-tickets, find-next-ticket-number) with four card skills (create-card, list-cards, complete-card, describe-cards)
- Update six agent definitions (scribe, overseer, vizier, lawgiver, surveyor, builder) to reference cards instead of tickets
- Update plugin.json with new skill registrations and incremented version
- Update documentation: README.md, docs/getting-started.md, docs/brownfield.md
- Migrate existing ticket T0001 to Hieroglyphs card format
- Remove `.ushabti/tickets/` directory (both active and .archived)

**Out of scope:**
- Modifying historical Phase 0012 and 0013 files (they document the ticket system's creation and remain as historical records)
- Implementing Hieroglyphs ingestion capabilities (separate project concern)
- Adding new card features beyond the baseline Hieroglyphs schema

## Constraints

- **L06 — Plugin Manifest Completeness**: All new card skills must be registered in plugin.json; all ticket skills must be unregistered
- **L07 — Plugin Validation on Addition**: Must run `claude plugin validate .` successfully after skill changes
- **L08 — Version Increment on Phase Completion**: Version in plugin.json must be incremented from 1.6.8 to 1.6.9
- **Style — Documentation Accuracy**: All documentation must reflect the new card system; stale ticket references are defects
- **Style — Clarity**: Card skill instructions must be explicit and unambiguous for LLM agents
- **Hieroglyphs Schema Compliance**: Cards must use the canonical Hieroglyphs format (frontmatter fields alphabetically ordered, ISO 8601 timestamps, UUID IDs, status field instead of archival directory)

## Acceptance Criteria

1. Four new card skills exist in `skills/` directory, each with SKILL.md:
   - `create-card`: Generate UUID, derive slug, write card.md with Hieroglyphs frontmatter
   - `list-cards`: Scan and parse cards, filter by status
   - `complete-card`: Update card status to "done" and updated timestamp
   - `describe-cards`: Document card schema and workflows

2. Five ticket skills removed from `skills/` directory:
   - `create-ticket`, `list-tickets`, `archive-ticket`, `describe-tickets`, `find-next-ticket-number`

3. Six agent definitions updated to reference cards:
   - `scribe.md`: Read cards instead of tickets, use `card: {slug}` metadata instead of `ticket: TNNNN`
   - `overseer.md`: Invoke `complete-card` instead of `archive-ticket`, check for `card` metadata field
   - `vizier.md`: Read and create cards instead of tickets
   - `lawgiver.md`: Bootstrap `.ushabti/cards/` directory instead of `.ushabti/tickets/`
   - `surveyor.md`: Bootstrap `.ushabti/cards/` directory instead of `.ushabti/tickets/`
   - `builder.md`: Verified to have no direct ticket references (no changes needed if true)

4. plugin.json updated:
   - Version incremented to 1.6.9
   - Four card skills registered in skills array
   - Five ticket skills removed from skills array
   - Plugin validates successfully: `claude plugin validate .` exits with code 0

5. Documentation updated:
   - README.md: "Ticketing System" section replaced with "Cards" section describing Hieroglyphs-compatible cards
   - docs/getting-started.md: Ticket workflow replaced with card workflow
   - docs/brownfield.md: "Capture Technical Debt with Tickets" section updated to use cards

6. Data migration completed:
   - `.ushabti/cards/ushabti-user-guide-agent/card.md` exists with:
     - UUID id field (generated fresh)
     - slug: ushabti-user-guide-agent
     - title: Ushabti user guide agent
     - priority: low
     - status: todo
     - type: feature
     - tags: []
     - created: 2026-02-01T00:00:00Z (converted from ticket's 2026-02-01)
     - updated: timestamp of migration
     - Overview section (from ticket's context)
     - Requirements section (from ticket's proposed_work)
   - `.ushabti/tickets/` directory removed entirely

7. Verification:
   - `grep -ri ticket .` across repo returns only:
     - Phase 0012 and 0013 historical files
     - Phase 0014 files (this phase)
     - No other references to ticket system
   - Cards created by `create-card` skill are parseable by Hieroglyphs (valid YAML frontmatter, all required fields present)

## Risks / Notes

- **Breaking change**: Any external tooling or workflows expecting `.ushabti/tickets/` will break. This is acceptable as Ushabti is early-stage and the migration provides long-term alignment with Hieroglyphs.
- **Unknown frontmatter fields**: Card skills must preserve unknown frontmatter fields when updating cards, as Hieroglyphs may add fields agents don't know about. This requires careful YAML parsing and round-tripping.
- **Historical phases**: Phase 0012 and 0013 document the ticket system. These files are intentionally preserved as historical records and must not be modified.
- **Slug collisions**: If multiple cards have the same slug, the directory-based structure will fail. Card creation must validate that the slug directory doesn't already exist.
