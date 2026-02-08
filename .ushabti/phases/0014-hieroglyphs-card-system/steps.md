# Steps

## S001: Create `create-card` skill

**Intent:** Enable agents to create new Hieroglyphs-compatible cards with proper schema, UUID generation, and slug derivation.

**Work:**
- Create `skills/create-card/SKILL.md`
- Document card schema: all frontmatter fields in alphabetical order (created, id, priority, slug, status, tags, title, type, updated)
- Document field constraints: status (todo/backlog/in-progress/done), type (bug/feature), priority (low/medium/high)
- Document slug derivation: lowercase, kebab-case, strip punctuation, match directory name
- Document UUID generation via `uuidgen` command
- Document ISO 8601 timestamp format: `YYYY-MM-DDTHH:MM:SSZ`
- Document directory creation: `mkdir -p .ushabti/cards/{slug}/`
- Document card.md format: YAML frontmatter delimited by `---`, followed by markdown body with Overview and Requirements sections
- Include validation checklist: all required fields present, frontmatter alphabetically ordered, slug matches directory name

**Done when:** `skills/create-card/SKILL.md` exists with complete instructions for creating Hieroglyphs-compatible cards, including schema, constraints, and examples.

---

## S002: Create `list-cards` skill

**Intent:** Enable agents to discover and filter existing cards by status and other criteria.

**Work:**
- Create `skills/list-cards/SKILL.md`
- Document scanning: find all `.ushabti/cards/*/card.md` files
- Document frontmatter parsing: extract title, status, priority, type, slug from YAML
- Document listing format: include slug, title, status, priority for each card
- Document status filtering: ability to list only cards matching specific status (e.g., only `todo` cards, exclude `done`)
- Include command examples for scanning and parsing YAML frontmatter

**Done when:** `skills/list-cards/SKILL.md` exists with instructions for scanning, parsing, and filtering cards.

---

## S003: Create `complete-card` skill

**Intent:** Enable agents to mark cards as done by updating status field, replacing the archival directory pattern.

**Work:**
- Create `skills/complete-card/SKILL.md`
- Document status update: change `status` field from current value to `done`
- Document timestamp update: set `updated` field to current UTC time in ISO 8601 format
- Document frontmatter preservation: when updating, preserve all existing frontmatter fields (including unknown fields Hieroglyphs may add)
- Document procedure: read existing card.md, parse frontmatter, modify status and updated, write back
- Include validation: verify card exists before attempting update

**Done when:** `skills/complete-card/SKILL.md` exists with instructions for updating card status while preserving all other frontmatter fields.

---

## S004: Create `describe-cards` skill

**Intent:** Provide comprehensive documentation of the card system for agents to reference.

**Work:**
- Create `skills/describe-cards/SKILL.md`
- Document canonical card schema: all fields, types, constraints, defaults
- Document directory structure: `.ushabti/cards/{slug}/card.md`
- Document card lifecycle: todo → in-progress → done (backlog is optional)
- Document relationship to Hieroglyphs: cards use Hieroglyphs format as single source of truth
- Document differences from ticket system: UUID vs sequential ID, status field vs archival directory, frontmatter + markdown vs flat YAML
- Include example cards showing both bug and feature types

**Done when:** `skills/describe-cards/SKILL.md` exists with comprehensive card system documentation.

---

## S005: Remove ticket skills

**Intent:** Delete obsolete ticket skills to prevent confusion and ensure agents use the new card system.

**Work:**
- Delete `skills/create-ticket/` directory
- Delete `skills/list-tickets/` directory
- Delete `skills/archive-ticket/` directory
- Delete `skills/describe-tickets/` directory
- Delete `skills/find-next-ticket-number/` directory

**Done when:** All five ticket skill directories removed from `skills/`.

---

## S006: Update `scribe.md` agent

**Intent:** Replace ticket reading and metadata with card reading and metadata in the Scribe agent.

**Work:**
- Read `agents/scribe.md`
- Replace ticket reading instructions: change "read the ticket YAML from `.ushabti/tickets/`" to "read `.ushabti/cards/{slug}/card.md`"
- Replace ticket field references: change "ticket's `context` and `proposed_work` fields" to "card's body content (Overview, Requirements sections)"
- Replace phase metadata: change "add `ticket: TNNNN` metadata" to "add `card: {slug}` metadata"
- Update metadata placement: keep instruction to add metadata immediately after phase title, before Intent section
- Verify no other ticket references remain

**Done when:** `agents/scribe.md` references cards instead of tickets, with `card: {slug}` metadata format documented.

---

## S007: Update `overseer.md` agent

**Intent:** Replace ticket archival with card status update in the Overseer agent.

**Work:**
- Read `agents/overseer.md`
- Replace archival instructions in "Declaring a Phase green" section:
  - Change "Check phase.md for a `ticket` metadata field" to "Check phase.md for a `card` metadata field"
  - Change "If ticket field exists (e.g., `ticket: T0042`)" to "If card field exists (e.g., `card: improve-error-handling`)"
  - Change "Invoke the archive-ticket skill" to "Invoke the complete-card skill"
  - Change "Move the ticket file from `.ushabti/tickets/` to `.ushabti/tickets/.archived/`" to "Update the card's status to done"
  - Change "Document the archival action in review.md (e.g., 'Archived ticket T0042')" to "Document the status update in review.md (e.g., 'Marked card `improve-error-handling` as done')"
- Verify no other ticket references remain

**Done when:** `agents/overseer.md` references cards and `complete-card` skill instead of tickets and `archive-ticket` skill.

---

## S008: Update `vizier.md` agent

**Intent:** Replace ticket reading and creation with card reading and creation in the Vizier agent.

**Work:**
- Read `agents/vizier.md`
- Replace ticket references with card references throughout
- Change ticket reading instructions: `.ushabti/tickets/*.yaml` to `.ushabti/cards/*/card.md`
- Change ticket creation: reference `create-card` skill instead of `create-ticket` skill
- Update status awareness: change "active vs archived" to "status field (todo/backlog/in-progress/done)"
- Add instruction: never read or modify cards with status `done` (they're closed)
- Verify no other ticket references remain

**Done when:** `agents/vizier.md` references cards and card skills instead of tickets and ticket skills.

---

## S009: Update `lawgiver.md` agent

**Intent:** Bootstrap card infrastructure instead of ticket infrastructure in the Lawgiver agent.

**Work:**
- Read `agents/lawgiver.md`
- Find bootstrap infrastructure instructions (directory creation)
- Replace `.ushabti/tickets/` with `.ushabti/cards/`
- Remove `.ushabti/tickets/.archived/` directory creation (not needed with status field)
- Verify no other ticket references remain

**Done when:** `agents/lawgiver.md` bootstraps `.ushabti/cards/` directory instead of `.ushabti/tickets/`.

---

## S010: Update `surveyor.md` agent

**Intent:** Bootstrap card infrastructure instead of ticket infrastructure in the Surveyor agent.

**Work:**
- Read `agents/surveyor.md`
- Find bootstrap infrastructure instructions (directory creation)
- Replace `.ushabti/tickets/` with `.ushabti/cards/`
- Remove `.ushabti/tickets/.archived/` directory creation (not needed with status field)
- Verify no other ticket references remain

**Done when:** `agents/surveyor.md` bootstraps `.ushabti/cards/` directory instead of `.ushabti/tickets/`.

---

## S011: Verify `builder.md` agent

**Intent:** Confirm Builder agent has no direct ticket references requiring updates.

**Work:**
- Read `agents/builder.md` in full
- Search for any references to "ticket", "T0001", ".ushabti/tickets", or ticket-related workflows
- If references found: update to card equivalents following same patterns as other agents
- If no references found: document in step notes that no changes were needed

**Done when:** `agents/builder.md` verified to have no ticket references, or updated to use cards if references found.

---

## S012: Update `plugin.json`

**Intent:** Register new card skills, unregister ticket skills, and increment version.

**Work:**
- Read `.claude-plugin/plugin.json`
- Remove from skills array:
  - `./skills/archive-ticket/`
  - `./skills/create-ticket/`
  - `./skills/describe-tickets/`
  - `./skills/find-next-ticket-number/`
  - `./skills/list-tickets/`
- Add to skills array:
  - `./skills/complete-card/`
  - `./skills/create-card/`
  - `./skills/describe-cards/`
  - `./skills/list-cards/`
- Increment version from `1.6.8` to `1.6.9`
- Verify JSON remains valid after changes

**Done when:** `plugin.json` has ticket skills removed, card skills added, version incremented to 1.6.9, and is valid JSON.

---

## S013: Validate plugin

**Intent:** Ensure plugin passes Claude Code validation after skill changes.

**Work:**
- Run `claude plugin validate .` from repository root
- Verify command exits with code 0 (success)
- If validation fails: diagnose error, fix manifest or file paths, re-run until passing

**Done when:** `claude plugin validate .` exits successfully.

---

## S014: Update README.md

**Intent:** Replace ticket system documentation with card system documentation in the main README.

**Work:**
- Read `README.md`
- Locate "Ticketing System" section (around line 217)
- Replace entire section with "Cards" section describing:
  - Hieroglyphs-compatible card format
  - When to create cards (same triggers as tickets)
  - Card workflow: create → phase → complete
  - Directory structure: `.ushabti/cards/{slug}/card.md`
  - Reference to getting-started.md for detailed workflow
- Update directory structure diagram: replace `tickets/` and `.archived/` with `cards/`
- Search for any other ticket references in README and update to cards

**Done when:** README.md documents card system instead of ticket system, with no stale ticket references.

---

## S015: Update docs/getting-started.md

**Intent:** Replace ticket workflow with card workflow in the getting started guide.

**Work:**
- Read `docs/getting-started.md`
- Locate ticket workflow section
- Replace with card workflow:
  - Creating cards with `create-card` skill
  - Listing cards with `list-cards` skill
  - Planning phases from cards (Scribe reads card body)
  - Completing cards when phase finishes (Overseer invokes `complete-card`)
- Update examples: change ticket IDs (T0001) to card slugs (improve-error-handling)
- Update file paths: `.ushabti/tickets/` to `.ushabti/cards/{slug}/card.md`
- Search for any other ticket references and update

**Done when:** `docs/getting-started.md` documents card workflow instead of ticket workflow.

---

## S016: Update docs/brownfield.md

**Intent:** Update technical debt capture instructions to use cards instead of tickets.

**Work:**
- Read `docs/brownfield.md`
- Locate "Capture Technical Debt with Tickets" section
- Rename section to "Capture Technical Debt with Cards"
- Update instructions: replace `create-ticket` skill with `create-card` skill
- Update examples: show card format (frontmatter + markdown body) instead of flat YAML
- Update file references: `.ushabti/tickets/` to `.ushabti/cards/`
- Search for any other ticket references and update

**Done when:** `docs/brownfield.md` documents capturing technical debt with cards instead of tickets.

---

## S017: Migrate T0001 to card format

**Intent:** Convert the existing ticket to Hieroglyphs card format as a concrete data migration example.

**Work:**
- Read `.ushabti/tickets/T0001-ushabti-user-guide-agent.yaml`
- Create directory `.ushabti/cards/ushabti-user-guide-agent/`
- Generate new UUID via `uuidgen`
- Create `.ushabti/cards/ushabti-user-guide-agent/card.md` with:
  - Frontmatter fields in alphabetical order: created, id, priority, slug, status, tags, title, type, updated
  - created: `2026-02-01T00:00:00Z` (convert ticket's `2026-02-01`)
  - id: generated UUID
  - priority: `low` (from ticket)
  - slug: `ushabti-user-guide-agent`
  - status: `todo`
  - tags: `[]`
  - title: `Ushabti user guide agent` (from ticket)
  - type: `feature`
  - updated: current UTC timestamp in ISO 8601
  - Markdown body:
    - "# Overview" section with ticket's `context` field content
    - "# Requirements" section with ticket's `proposed_work` field content
- Verify card is valid YAML and follows Hieroglyphs schema

**Done when:** `.ushabti/cards/ushabti-user-guide-agent/card.md` exists with all required fields and properly migrated content.

---

## S018: Remove `.ushabti/tickets/` directory

**Intent:** Delete obsolete ticket storage to complete migration.

**Work:**
- Verify card migration completed successfully in S017
- Delete `.ushabti/tickets/` directory and all contents (including `.archived/` subdirectory)
- Verify directory no longer exists

**Done when:** `.ushabti/tickets/` directory removed entirely.

---

## S019: Verify ticket reference cleanup

**Intent:** Ensure no stale ticket references remain in the repository outside historical phases.

**Work:**
- Run `grep -ri ticket .` from repository root
- Exclude `.git/` directory from search
- Verify results include only:
  - `.ushabti/phases/0012-ticketing-system/` files (historical)
  - `.ushabti/phases/0013-ticketing-system-fixes/` files (historical)
  - `.ushabti/phases/0014-hieroglyphs-card-system/` files (this phase)
- If other references found: investigate and update or justify

**Done when:** `grep -ri ticket` shows only historical Phase 0012, 0013, and current Phase 0014 references.

---

## S020: Test card creation

**Intent:** Verify the new `create-card` skill produces valid, parseable Hieroglyphs cards.

**Work:**
- Create a test card using the `create-card` skill instructions
- Title: "Test card creation workflow"
- Priority: medium
- Type: feature
- Verify resulting card file:
  - Exists at `.ushabti/cards/{slug}/card.md`
  - Has valid YAML frontmatter
  - Has all required fields in alphabetical order
  - Has UUID in `id` field
  - Has ISO 8601 timestamps
  - Has markdown body with expected sections
- Delete test card after verification (or keep if useful)

**Done when:** Test card created successfully, verified to match Hieroglyphs schema, demonstrating the `create-card` skill produces valid output.

---

## S021: Update `using-skills` skill

**Intent:** Remove obsolete ticket skill references from the using-skills skill documentation and add the new card skills.

**Work:**
- Read `skills/using-skills/SKILL.md`
- Remove five ticket skill entries:
  - `archive-ticket` (lines 17-20)
  - `create-ticket` (lines 27-29)
  - `describe-tickets` (lines 97-99)
  - `find-next-ticket-number` (lines 122-124)
  - `list-tickets` (lines 132-134)
- Add four card skill entries in alphabetical order:
  - `complete-card`: Mark cards as done by updating status field
  - `create-card`: Create new Hieroglyphs-compatible cards
  - `describe-cards`: Documentation of card system schema and workflows
  - `list-cards`: Scan and filter cards by status and other criteria
- Verify the skill list is in alphabetical order
- Verify no ticket references remain

**Done when:** `skills/using-skills/SKILL.md` lists only card skills (not ticket skills) and all entries are in alphabetical order.
