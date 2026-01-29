# Phase 0003: Docs in The Loop

## Intent

The Surveyor agent (Phase 0002) creates structured documentation in `.ushabti/docs/`. However, this documentation currently exists in isolation. Agents do not consult it, update it, or verify its accuracy.

This Phase integrates `.ushabti/docs/` into the core Plan/Build/Review loop. The docs become:
- a planning resource for Scribe
- an implementation guide and maintenance responsibility for Builder
- a review checkpoint for Overseer
- a mandatory requirement enforced by laws

When complete, docs will be a living, reliable source of truth that agents both consume and maintain.

## Scope

### In scope

- **Lawgiver:** Add mandatory laws requiring docs integration across the workflow
- **Artisan:** Add completion check suggesting Surveyor handoff if docs are missing
- **Scribe:** Add pre-planning check for docs existence; use docs to inform Phase plans
- **Builder:** Add requirement to consult docs during implementation and update them as code changes
- **Overseer:** Add review checkpoint verifying docs are reconciled with code changes
- **Surveyor:** No changes (already creates docs)
- Increment plugin version
- Validate plugin after changes

### Out of scope

- Changing the structure or format of `.ushabti/docs/` files
- Modifying Surveyor agent behavior
- Adding new agents or skills
- Changing the Phase workflow itself

## Constraints

- **L02 (Agent Location):** All agent modifications must remain in `agents/`
- **L03 (Agent File Format):** Agent files must maintain YAML front matter format
- **L06 (Plugin Manifest Completeness):** No new agents, so manifest changes not required beyond version
- **L07 (Plugin Validation on Addition):** Must validate plugin after changes
- **L08 (Version Increment):** Must increment version in plugin.json
- **Style (Clarity):** Agent prompts must be explicit and unambiguous
- **Style (Documentation Accuracy):** Documentation must reflect current project state

## Acceptance Criteria

1. `agents/lawgiver.md` includes mandatory laws that Lawgiver must inscribe regarding docs integration:
   - Scribe MUST consult `.ushabti/docs` when planning
   - Builder MUST use docs for information and keep them updated
   - Overseer MUST verify docs are reconciled with code changes
   - A Phase cannot be marked complete until docs are reconciled

2. `agents/artisan.md` includes a completion check that suggests Surveyor handoff if `.ushabti/docs` does not exist

3. `agents/scribe.md` includes:
   - A pre-planning check for `.ushabti/docs` existence
   - Instruction to bail and recommend Surveyor if docs are missing
   - Instruction to consult docs when planning Phases

4. `agents/builder.md` includes:
   - Requirement to consult `.ushabti/docs` during implementation
   - Requirement to update docs when code changes affect documented systems

5. `agents/overseer.md` includes:
   - Review checkpoint verifying docs have been updated to reflect code changes
   - Requirement that docs reconciliation is mandatory for Phase completion

6. `plugin.json` version is incremented

7. `claude plugin validate .` exits with code 0

## Risks / Notes

- The Lawgiver changes are meta: they define what Lawgiver must include in *future* laws.md files, not changes to the current Ushabti laws.md.
- This Phase modifies all agents except Surveyor. Changes must be carefully coordinated.
- The "docs reconciliation" requirement for Overseer needs clear definition: it means any code changes that affect documented systems must have corresponding docs updates.
- Agents should check for docs existence gracefully and provide clear guidance when docs are missing.
