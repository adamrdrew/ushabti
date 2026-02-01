# Phase 0004: Steps

## S001: Fix zsh variable conflict in find-current-phase skill

### Intent

The `status` variable name conflicts with zsh's read-only built-in. Renaming eliminates the conflict while preserving functionality.

### Work

In `skills/find-current-phase/SKILL.md`, modify the bash command to use a different variable name instead of `status`. The command currently reads:

```bash
status=$(grep "^  status:" "$dir/progress.yaml" 2>/dev/null | awk '{print $2}')
```

Change `status` to `phase_status` (or similar non-conflicting name) in both the assignment and the echo statement.

### Done when

The bash command in `skills/find-current-phase/SKILL.md` no longer uses `status` as a variable name.

---

## S002: Test the skill fix

### Intent

Verify the fix resolves the zsh conflict without breaking functionality.

### Work

Invoke the skill via Claude Code (or manually run the bash command in zsh) and confirm:
- No "read-only variable" error occurs
- The skill outputs phase names and statuses correctly

### Done when

The skill executes in zsh without error and produces correct output.

---

## S003: Document permissions requirement in README

### Intent

Users need to configure Claude Code permissions for skills to function. Without documentation, users encounter failures without understanding why.

### Work

Add a section to `README.md` in or near the Installation section documenting:

1. Users must add permissions configuration to `.claude/settings.json` or `.claude/settings.local.json`
2. The required configuration:

```json
"permissions": {
  "allow": [
    "Bash(*)"
  ]
}
```

3. Brief explanation that this allows skills to execute bash commands

### Done when

`README.md` contains clear documentation of the permissions requirement with the exact configuration needed.

---

## S004: Increment plugin version

### Intent

L08 requires version increment when any development Phase completes.

### Work

Increment the `version` field in `.claude-plugin/plugin.json`.

### Done when

`plugin.json` version field is incremented from its current value.

---

## S005: Validate plugin

### Intent

L07 requires plugin validation after changes.

### Work

Run `claude plugin validate .` from the repository root.

### Done when

`claude plugin validate .` exits with code 0.

---

## S006: Verify all acceptance criteria

### Intent

Final verification that all acceptance criteria are met before handoff to Overseer.

### Work

Review each acceptance criterion from `phase.md` and verify:

1. `find-current-phase` skill does not use `status` as a variable name
2. The skill executes in zsh without the read-only variable error
3. README documents the permissions configuration
4. The documented permissions include `Bash(*)` allow rule
5. Plugin version is incremented
6. Plugin validates successfully

### Done when

All six acceptance criteria are verified as satisfied.
