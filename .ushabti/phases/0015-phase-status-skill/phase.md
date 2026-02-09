# Phase: Phase Status Skill

card: phase-status-skill

## Intent

Create a new user-invocable skill `/phase-status` that external consumers (particularly Pharaoh) can call to query the status of a phase. This is a public API surface — the output format is a contract that consumers will parse.

Currently, the only way to check phase status is to read `.ushabti/phases/*/progress.yaml` directly, which couples consumers to Ushabti's internal directory structure and file format. This skill wraps that access behind a stable verb.

## Scope

**In scope:**
- New skill directory `skills/phase-status/` with `SKILL.md`
- User-invocable skill (frontmatter: `user-invocable: true`)
- Argument handling: phase slug, partial slug, `latest`, or empty (defaults to `latest`)
- Structured output format that is parseable and stable
- Error handling for phase not found
- Registration in plugin.json in alphabetical order within skills array
- Version bump from 1.7.0 to 1.8.0
- Plugin validation

**Out of scope:**
- Modifying existing `get-phase-status` or `find-current-phase` skills (they serve internal agent needs)
- Returning step-level detail beyond counts
- Changes to progress.yaml format
- SDK or frontend implementation

## Constraints

**Laws:**
- L04: Skill must reside in `skills/` directory at repository root
- L05: Skill directory must contain `SKILL.md` file
- L06: Skill must be registered in `.claude-plugin/plugin.json`
- L07: Plugin must be validated after adding the skill
- L08: Version must be incremented on phase completion

**Style:**
- YAML frontmatter must be syntactically valid with 2-space indentation
- Use ATX-style headers in markdown
- Clear, unambiguous prose for LLM parsing
- Keep lines under 120 characters where practical

## Acceptance Criteria

- [ ] `/phase-status latest` returns the status of the most recently modified phase
- [ ] `/phase-status 0002-welcome-banner` returns status of a specific phase by full slug
- [ ] `/phase-status welcome-banner` returns status using partial slug matching
- [ ] `/phase-status` with no argument behaves like `latest`
- [ ] Output follows exact structured format:
  ```
  PHASE_STATUS:
    slug: {phase directory name}
    status: {planned|building|review|complete}
    steps_implemented: {count}
    steps_total: {count}
  ```
- [ ] Phase not found produces error format without crashing:
  ```
  PHASE_STATUS:
    error: Phase not found
  ```
- [ ] Skill registered in plugin.json in alphabetical order within skills array
- [ ] Version bumped to 1.8.0 in plugin.json
- [ ] `claude plugin validate .` exits with success

## Risks / Notes

**Output format stability:** The structured output format is a public contract. External tools will parse this format. Any change to it is a breaking change and must be versioned appropriately.

**Partial matching behavior:** Partial slug matching (e.g., `welcome-banner` matching `0002-welcome-banner`) is a convenience feature. If multiple phases match a partial slug, the skill should return the first match (alphabetically by directory name). This is acceptable for MVP; future versions could surface ambiguity.

**Latest definition:** "Latest" is defined as the phase with the most recently modified `progress.yaml` file. This is a reasonable heuristic for the active phase.
