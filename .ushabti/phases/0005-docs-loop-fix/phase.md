# Phase 0005 — Docs Loop Fix

## Intent

Fix the docs loop initialization gap so that the documentation system works correctly regardless of how an Ushabti project is started — whether onboarding an existing project, bootstrapping from an empty directory, or any hybrid scenario.

Currently, when bootstrapping a new project via the Lawgiver → Artisan flow, the `.ushabti/docs/` directory never gets created. Artisan recommends Surveyor if docs are missing, and Scribe refuses to plan without docs, but for empty directories there's nothing meaningful to survey. This creates a chicken-and-egg problem where the docs loop cannot activate.

## Scope

### In Scope

- Modify Lawgiver to create the `.ushabti/` base directory and a minimal docs scaffold when bootstrapping a new project
- Update the bootstrap flow documentation to reflect the new behavior
- Ensure Surveyor remains the agent for comprehensive project documentation
- Update the check-ushabti-prerequisites skill to reflect the new flow
- Update project documentation in `.ushabti/docs/`

### Out of Scope

- Changing Surveyor's core functionality (it remains the comprehensive documentation agent)
- Modifying Scribe, Builder, or Overseer agents
- Changing the Artisan handoff logic (it correctly recommends Surveyor for comprehensive docs)

## Constraints

- **L01 — Claude Code Plugin Compliance**: Plugin must validate after changes
- **L06 — Plugin Manifest Completeness**: Any new skills must be registered
- **L07 — Plugin Validation on Addition**: Run `claude plugin validate .` after changes
- **L08 — Version Increment on Phase Completion**: Bump version in plugin.json
- **Style — Documentation Accuracy**: Docs must reflect current project state

## Acceptance Criteria

1. When Lawgiver creates `.ushabti/laws.md` for a new project (no existing `.ushabti/` directory), it also creates `.ushabti/docs/index.md` with a minimal scaffold
2. The minimal docs scaffold contains placeholder content that allows the docs loop to function while signaling that comprehensive documentation is needed
3. Artisan continues to recommend Surveyor when comprehensive docs are missing (not just when the directory is missing)
4. The check-ushabti-prerequisites skill accurately reflects the new bootstrap flow
5. The `.ushabti/docs/agents.md` file is updated to document the new Lawgiver behavior
6. Plugin validation passes: `claude plugin validate .` exits with success
7. Version is incremented in `.claude-plugin/plugin.json`

## Risks / Notes

- **Design decision**: Lawgiver creates a minimal scaffold, not comprehensive docs. The scaffold enables the docs loop while signaling that Surveyor should be run for full documentation. This keeps role boundaries clear: Lawgiver inscribes laws (and minimal infrastructure), Surveyor documents systems.
- **Scaffold vs. empty**: The scaffold includes an index.md with a note indicating docs are minimal and Surveyor should be run. This is better than an empty directory because it provides enough structure for the docs loop to function.
- **Artisan handoff**: Artisan's current logic checks if "docs don't exist" — this should be refined to check if docs are "comprehensive" vs. "scaffold only". However, this may be deferred if the current behavior (recommending Surveyor when docs are minimal) is acceptable.
