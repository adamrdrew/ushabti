# Phase 0001: Update the README

## Intent

The README contains outdated information that no longer reflects how Ushabti is installed, structured, or developed. This Phase corrects the documentation to match the current state of the project.

Specifically:
- Ushabti is now a Claude Code plugin installed via the adamrdrew/marketplace
- Ushabti is developed using itself (dogfooding)
- The repository structure has changed (no root-level laws.md/style.md mirrors)

Accurate documentation is essential for users discovering the project and for the project's own agents, which read these files.

## Scope

### In scope

- Correcting installation instructions to use the marketplace
- Adding a section noting that Ushabti is developed with itself
- Fixing the repository structure diagram to match reality
- Removing duplicate or contradictory installation sections
- General cleanup for clarity and accuracy

### Out of scope

- Adding new features or agents
- Changing laws or style
- Modifying any plugin functionality
- Updating CLAUDE.md (separate concern)

## Constraints

- **L08 (Version Increment):** This Phase is documentation-only and does not affect plugin behavior. Version bump MAY be skipped per the exception clause.
- **Style (Documentation Accuracy):** Documentation must reflect current project state. Stale documentation is a defect.
- **Style (Brevity):** Say what needs saying. No more.
- **Style (Clarity):** Write for LLMs. Be explicit. Avoid ambiguity.

## Acceptance Criteria

1. The README contains exactly one installation section with correct marketplace instructions
2. The README mentions that Ushabti is developed using itself
3. The repository structure diagram matches the actual directory layout
4. No duplicate or contradictory information remains
5. All prose follows style guidelines (clear, brief, accurate)

## Risks / Notes

- The README currently has two installation sections (lines 7-12 and lines 180-215). Both must be reconciled into one correct section.
- The repository structure diagram shows `law.md` and `style.md` mirrors at `.ushabti/` level, but the actual structure places these files directly in `.ushabti/` without root-level mirrors.
- This is the first Phase planned for this project. It establishes the pattern for future Phases.
