# Phase 0004: Bug Fix and Documentation

## Intent

This Phase addresses two concrete issues:

1. **Bug**: The `find-current-phase` skill fails in zsh environments because it uses `status` as a variable name, which is a read-only built-in variable in zsh.

2. **Documentation gap**: Users cannot invoke skills without configuring Claude Code permissions, but the README does not document this requirement.

Both issues affect user experience. The bug prevents a core utility skill from functioning. The missing documentation causes confusion during setup.

## Scope

### In scope

- Fix the `find-current-phase` skill by renaming the `status` variable to avoid zsh conflict
- Update the README to document required Claude Code permissions configuration
- Increment plugin version (L08)
- Validate plugin after changes (L07)

### Out of scope

- Other skill modifications
- Agent modifications
- Adding new skills or agents
- Structural changes to the plugin

## Constraints

- **L04 (Skill Location):** Skill modifications must remain in `skills/`
- **L05 (Skill Directory Structure):** Skill must maintain `SKILL.md` file
- **L07 (Plugin Validation on Addition):** Must validate plugin after changes
- **L08 (Version Increment):** Must increment version in plugin.json
- **Style (Documentation Accuracy):** README must reflect current project state
- **Style (Clarity):** Documentation must be explicit and unambiguous

## Acceptance Criteria

1. `skills/find-current-phase/SKILL.md` does not use `status` as a variable name in its bash command
2. The skill executes successfully in zsh environments without the "read-only variable: status" error
3. `README.md` documents the required permissions configuration for `.claude/settings.json` or `.claude/settings.local.json`
4. The documented permissions include the `Bash(*)` allow rule
5. `plugin.json` version is incremented
6. `claude plugin validate .` exits with code 0

## Risks / Notes

- The variable rename is a simple find-and-replace within the skill's bash command. Common alternatives: `phase_status`, `pstatus`, `st`.
- The permissions documentation should be placed in the Installation section, as it is a setup requirement.
- This Phase does not require docs updates in `.ushabti/docs/` because the skill behavior is unchanged (only implementation) and README is not part of the docs system.
