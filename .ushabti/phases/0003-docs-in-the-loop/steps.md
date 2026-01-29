# Phase 0003: Steps

## S001: Update Lawgiver with docs law requirements

### Intent

Lawgiver must inscribe docs-related laws into every project's `laws.md`. This step adds instructions to Lawgiver's prompt specifying what docs laws it must always include.

### Work

Add a new section to `agents/lawgiver.md` titled "Mandatory docs laws" (or similar) that instructs Lawgiver to always include the following laws when writing `laws.md`:

- Scribe MUST consult `.ushabti/docs` to inform Phase planning
- Builder MUST consult docs during implementation and update docs when code changes affect documented systems
- Overseer MUST verify docs are reconciled with code changes before declaring a Phase complete
- A Phase cannot be marked GREEN/complete until docs are reconciled with the code work

This section should be placed after "What qualifies as a law" and before the document structure section.

### Done when

`agents/lawgiver.md` contains explicit instructions requiring Lawgiver to inscribe docs-related laws, specifying the four mandatory laws above.

---

## S002: Update Artisan with docs existence check

### Intent

Artisan should guide users toward creating docs if they do not exist. This completes the onboarding flow.

### Work

Add to `agents/artisan.md` in the "Completion and handoff" section:

- After completing style work, check if `.ushabti/docs/index.md` exists
- If docs do not exist, recommend running Surveyor to create project documentation before proceeding to Scribe
- This is a suggestion, not a blocker

### Done when

`agents/artisan.md` completion section includes a docs existence check and Surveyor handoff recommendation.

---

## S003: Update Scribe with docs prerequisite check

### Intent

Scribe should not plan Phases without docs. Missing docs means missing context that could lead to poor plans.

### Work

Add to `agents/scribe.md`:

1. In "Inputs you must read first" section, add `.ushabti/docs/index.md` and relevant docs files to the required reading list

2. Add a new section "Docs prerequisite" (after "Inputs you must read first") that specifies:
   - Before planning, check if `.ushabti/docs/index.md` exists
   - If docs do not exist, stop planning and instruct the user to run Surveyor first
   - If docs exist, consult them to understand the codebase when planning

3. Update the "Procedure" section to include consulting docs in the "Understand" step

### Done when

`agents/scribe.md` contains:
- Docs in the required inputs list
- A docs prerequisite check that bails if docs are missing
- Procedure updated to consult docs during planning

---

## S004: Update Builder with docs usage and maintenance requirements

### Intent

Builder must both use docs as a resource and keep them current as code changes.

### Work

Add to `agents/builder.md`:

1. In "Canonical inputs" section, add `.ushabti/docs/index.md` and relevant docs files to the required reading list

2. Add a new section "Docs maintenance" (after "Tests and correctness") that specifies:
   - Consult `.ushabti/docs` to understand existing systems before implementing
   - When implementation changes documented systems, update the relevant docs
   - Docs updates are part of step completion, not separate work
   - If docs are missing, note this in `progress.yaml` but proceed with implementation

3. Update "Definition of implemented" to include: relevant docs are updated if code changes affect documented systems

### Done when

`agents/builder.md` contains:
- Docs in the required inputs list
- A docs maintenance section with clear requirements
- Updated definition of "implemented" including docs updates

---

## S005: Update Overseer with docs reconciliation checkpoint

### Intent

Overseer must verify docs are current before declaring a Phase complete.

### Work

Add to `agents/overseer.md`:

1. In "Canonical inputs" section, add `.ushabti/docs/` files to the required reading list

2. Add a new section "Docs reconciliation" (after "Review rules") that specifies:
   - Verify that code changes affecting documented systems have corresponding docs updates
   - If Builder touched systems documented in `.ushabti/docs/`, verify docs were updated
   - Missing docs updates are defects that must be fixed before Phase is green
   - If docs do not exist for the project, note this as a recommendation but do not block

3. Update "Declaring a Phase green" conditions to include: docs are reconciled with code changes

### Done when

`agents/overseer.md` contains:
- Docs in the required inputs list
- A docs reconciliation section with verification requirements
- Updated green declaration conditions including docs reconciliation

---

## S006: Increment plugin version

### Intent

L08 requires version increment when any development Phase completes.

### Work

Increment the `version` field in `.claude-plugin/plugin.json`.

### Done when

`plugin.json` version field is incremented from its current value.

---

## S007: Validate plugin

### Intent

L07 requires plugin validation after changes.

### Work

Run `claude plugin validate .` from the repository root.

### Done when

`claude plugin validate .` exits with code 0.

---

## S008: Verify all acceptance criteria

### Intent

Final verification that all acceptance criteria are met before handoff to Overseer.

### Work

Review each acceptance criterion from `phase.md` and verify:

1. Lawgiver has mandatory docs law instructions
2. Artisan has docs existence check in completion
3. Scribe has docs prerequisite and consultation
4. Builder has docs usage and maintenance requirements
5. Overseer has docs reconciliation checkpoint
6. Plugin version is incremented
7. Plugin validates successfully

### Done when

All seven acceptance criteria are verified as satisfied.
