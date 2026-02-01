# Phase 0008: Minimal Bash Permissions

## Intent

Replace the overly permissive `Bash(*)` permission in `.claude/settings.json` with explicit, minimal permissions for only the read-only bash commands that skills actually use.

## Scope

**In scope:**
- Replace `Bash(*)` with explicit command permissions in `.claude/settings.json`
- Update README to explain the permissions granted and why
- Update `.ushabti/docs/configuration.md` to document the change
- Increment version in `.claude-plugin/plugin.json`

**Out of scope:**
- Modifying skill implementations
- Changing how skills invoke bash commands
- Adding new skills or commands
- Changing Claude Code's permission system

## Constraints

**Laws:**
- L08: Version must be incremented when Phase completes

**Style:**
- Clarity: Be explicit about what permissions are granted and why
- JSON: Must be syntactically valid with 2-space indentation
- Documentation Accuracy: Docs must reflect actual state

## Acceptance Criteria

- [ ] `.claude/settings.json` contains explicit permissions for: `[ -f *`, `[ -d *`, `ls *`, `grep *`, `awk *`, `basename *`, `echo *`, `sed *`, `sort *`, `tail *`, `printf *`
- [ ] `.claude/settings.json` no longer contains `Bash(*)`
- [ ] README explains what permissions are granted out of the box
- [ ] README explains why these permissions are needed (skills use read-only bash)
- [ ] README states this follows principle of least privilege
- [ ] README notes that new skills requiring additional commands need settings.json updated
- [ ] `.ushabti/docs/configuration.md` reflects the new permissions approach
- [ ] Version incremented in `.claude-plugin/plugin.json`
- [ ] All modified JSON files are syntactically valid

## Risks / Notes

This is a security hardening change. Skills will continue to function because we are granting exactly the permissions they need. No functional changes to skills are required.

If future skills need additional bash commands, `.claude/settings.json` must be updated to add those specific commands.
