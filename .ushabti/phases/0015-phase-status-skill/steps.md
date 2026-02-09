# Implementation Steps

## S001 — Create skill directory

**Intent:** Establish the directory structure for the new skill according to plugin conventions.

**Work:** Create the directory `skills/phase-status/` at the repository root.

**Done when:** Directory exists at `/Users/adam/Development/ushabti/skills/phase-status/`

---

## S002 — Write SKILL.md

**Intent:** Define the skill specification with frontmatter, description, input handling, and output format instructions.

**Work:**
- Create `skills/phase-status/SKILL.md`
- Add YAML frontmatter with:
  - `name: phase-status`
  - `description: Query the status of a phase. Returns structured status information for external consumers.`
  - `user-invocable: true`
- Document argument handling:
  - `$ARGUMENTS` can be: phase slug (full or partial), `latest`, or empty (defaults to `latest`)
- Provide bash command to find phases:
  - If `latest` or empty: find phase with most recently modified `progress.yaml`
  - If slug: match against directory names (exact or partial match)
- Document the exact output format:
  ```
  PHASE_STATUS:
    slug: {phase directory name}
    status: {planned|building|review|complete}
    steps_implemented: {count}
    steps_total: {count}
  ```
- Document error format for phase not found:
  ```
  PHASE_STATUS:
    error: Phase not found
  ```
- Include guidance for parsing progress.yaml to extract status and step counts

**Done when:**
- File exists at `/Users/adam/Development/ushabti/skills/phase-status/SKILL.md`
- Frontmatter is syntactically valid YAML
- Output format instructions are clear and match the specification exactly
- Bash commands are provided for both `latest` and slug-based lookups

---

## S003 — Register skill in plugin.json

**Intent:** Make the skill discoverable by registering it in the plugin manifest.

**Work:**
- Open `.claude-plugin/plugin.json`
- Add `"./skills/phase-status/"` to the `skills` array
- Maintain alphabetical order within the skills array
- Verify JSON syntax remains valid

**Done when:**
- `./skills/phase-status/` appears in the skills array
- Entry is in alphabetical order
- JSON is syntactically valid

---

## S004 — Bump version to 1.8.0

**Intent:** Signal the plugin update with a version increment as required by L08.

**Work:**
- Open `.claude-plugin/plugin.json`
- Change `"version": "1.7.0"` to `"version": "1.8.0"`

**Done when:**
- Version field in plugin.json reads `"1.8.0"`
- No other fields modified

---

## S005 — Validate plugin

**Intent:** Ensure the plugin manifest is valid and the new skill is properly registered.

**Work:**
- Run `claude plugin validate .` from repository root
- Verify exit code is 0 (success)
- If validation fails, fix the issues and re-run

**Done when:**
- `claude plugin validate .` exits with success
- No validation errors or warnings

---

## S006 — Test skill invocation formats

**Intent:** Verify the skill works with all supported argument formats.

**Work:**
- Invoke `/phase-status` (no argument, should behave like `latest`)
- Invoke `/phase-status latest`
- Invoke a specific phase using full slug (e.g., `/phase-status 0014-something`)
- Invoke a specific phase using partial slug (e.g., `/phase-status something`)
- Invoke a non-existent phase to verify error handling
- Verify output format matches specification exactly in all cases

**Done when:**
- All invocation formats work correctly
- Output format is consistent and parseable
- Error case handled gracefully

---

## S007 — Document skill in README if applicable

**Intent:** Ensure discoverability of the new skill for users reading project documentation.

**Work:**
- Check if `README.md` or similar documentation lists available skills
- If so, add `/phase-status` to the list with a brief description
- If not, skip this step

**Done when:**
- Skill is documented in README if a skills list exists, or
- No README update needed (no skills list exists)

---

## S008 — Update skill count in README

**Intent:** Correct stale documentation to reflect current state.

**Work:**
- Open README.md
- Change line 268 from `├── skills/               # Skill definitions (20 skills)`
- To: `├── skills/               # Skill definitions (26 skills)`

**Done when:**
- README.md accurately reflects the current number of skills
- No other references to "20 skills" exist in README.md
