# Steps

## S001: Update .claude/settings.json with explicit permissions

**Intent**: Replace `Bash(*)` with the minimal set of bash commands that skills actually use.

**Work**:
- Replace the permissions array in `.claude/settings.json`
- Use explicit permissions for: `[ -f *`, `[ -d *`, `ls *`, `grep *`, `awk *`, `basename *`, `echo *`, `sed *`, `sort *`, `tail *`, `printf *`
- Maintain proper JSON formatting (2-space indentation, no trailing commas)

**Done when**:
- `.claude/settings.json` contains the explicit permissions list
- `Bash(*)` is no longer present
- JSON is syntactically valid

---

## S002: Update README permissions section

**Intent**: Replace the `Bash(*)` guidance with explanation of explicit permissions.

**Work**:
- Remove the current "Permissions Configuration" section that shows `Bash(*)`
- Replace with new section explaining:
  - What permissions are granted out of the box
  - Why these permissions are needed (skills use specific read-only bash commands)
  - That this follows principle of least privilege
  - That new skills requiring additional commands will need settings.json updated

**Done when**:
- README no longer mentions `Bash(*)`
- README clearly documents the explicit permissions approach
- Guidance is actionable and complete

---

## S003: Update configuration documentation

**Intent**: Reflect the new permissions approach in the configuration reference docs.

**Work**:
- Update `.ushabti/docs/configuration.md` in the Claude Settings section
- Replace the generic example with the actual explicit permissions list
- Add explanation of why these specific permissions are granted
- Note that this is the minimal set for current skills

**Done when**:
- Configuration docs show the explicit permissions
- Docs explain the security rationale
- Docs are consistent with README

---

## S004: Increment plugin version

**Intent**: Satisfy L08 by bumping the version number.

**Work**:
- Increment the `version` field in `.claude-plugin/plugin.json`
- Follow semantic versioning (patch bump for security hardening)

**Done when**:
- Version field incremented
- JSON remains valid

---

## S005: Validate JSON syntax

**Intent**: Ensure all modified JSON files are syntactically valid.

**Work**:
- Verify `.claude/settings.json` is valid JSON
- Verify `.claude-plugin/plugin.json` is valid JSON
- Use a JSON validator or parser to confirm

**Done when**:
- All modified JSON files parse successfully
- No syntax errors present
