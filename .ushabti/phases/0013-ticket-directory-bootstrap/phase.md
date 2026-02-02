# Phase 0013: Ticket Directory Bootstrap

## Intent

Ensure ticket directories exist in all scenarios by adding bootstrap logic to Lawgiver and Surveyor, adding defensive directory creation to ticket skills, and documenting the ticket system for users.

Currently, new projects and onboarded projects fail when using tickets because the required directories (`.ushabti/tickets/` and `.ushabti/tickets/.archived/`) are not created during bootstrap or onboarding. Additionally, users cannot discover the ticket system exists because it is undocumented in user-facing documentation.

This Phase completes the ticket system implementation by ensuring directories exist in all scenarios and making the feature discoverable.

## Scope

### In Scope

- Modify Lawgiver agent to create ticket directories during bootstrap
- Modify Surveyor agent to create ticket directories during onboarding
- Add defensive `mkdir -p` to create-ticket, find-next-ticket-number, and archive-ticket skills
- Document ticket system in README.md
- Add ticket workflow to getting-started.md
- Update greenfield.md to mention tickets in bootstrap flow
- Update brownfield.md to mention tickets in onboarding flow

### Out of Scope

- Changes to ticket schema or validation
- New ticket features or capabilities
- Ticket skill enhancements beyond directory creation
- Integration with external ticketing systems

## Constraints

### Laws

- L02: All agent modifications must remain in `agents/` directory
- L03: Agent files must maintain markdown with YAML front matter format
- L04: All skill modifications must remain in `skills/` directory
- L05: Skills must maintain directory structure with `SKILL.md` file
- L08: Version in `.claude-plugin/plugin.json` must be incremented on completion

### Style

- Maintain clarity and explicitness in all prose
- Ensure all YAML remains syntactically valid
- Keep documentation current with implementation changes
- Preserve existing agent and skill structures

## Acceptance Criteria

1. Lawgiver creates `.ushabti/tickets/` and `.ushabti/tickets/.archived/` during bootstrap
2. Surveyor creates `.ushabti/tickets/` and `.ushabti/tickets/.archived/` during Part A setup
3. create-ticket skill includes defensive `mkdir -p` before writing ticket files
4. find-next-ticket-number skill includes defensive directory check or creation
5. archive-ticket skill includes defensive `mkdir -p` for `.archived/` directory
6. README.md documents the ticket system's existence and purpose
7. getting-started.md includes ticket system overview and basic workflow
8. greenfield.md mentions tickets in bootstrap section
9. brownfield.md mentions tickets in onboarding section
10. All modified files maintain syntactic validity (YAML, markdown)
11. Version incremented in `.claude-plugin/plugin.json`

## Risks / Notes

- Defensive directory creation in skills provides fallback but bootstrap should still create directories to avoid repeated mkdir operations
- Documentation additions should integrate naturally without disrupting existing content flow
- This Phase touches many files but changes are localized and low-risk
