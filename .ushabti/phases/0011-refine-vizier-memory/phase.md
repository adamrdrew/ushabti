# Phase 0011: Refine Vizier Memory System

## Intent

Restore balanced evergreen context to `.ushabti/vizier.md` after Phase 0010 over-corrected by removing too much valuable context. The file currently contains only 14 lines with reference docs, losing project summary, user preferences, and architectural principles. This Phase establishes a lean memory (~40-60 lines) that captures evergreen information without ephemeral bloat.

## Scope

**In scope:**
- Update `.ushabti/vizier.md` with evergreen context sections (project summary, user preferences, architectural principles, persistent risks)
- Clarify Vizier agent definition (`agents/vizier.md`) with explicit examples of evergreen vs ephemeral content
- Document the "evergreen test" principle in the agent definition

**Out of scope:**
- Changes to other agent definitions
- Changes to skills or plugin structure
- Documentation beyond vizier.md and agents/vizier.md

## Constraints

**Laws:**
- L08: Version increment required on completion

**Style:**
- Clarity: Explicit, unambiguous content
- Brevity: Lean memory, no redundancy
- Documentation accuracy: Must reflect current state

**Content constraints:**
- Memory must stay under 60 lines
- No narrative or conversation references
- No state tracking or temporal markers
- No duplication of content from `.ushabti/docs/`

## Acceptance Criteria

1. `.ushabti/vizier.md` contains all evergreen sections:
   - Project Context (3-5 lines)
   - User Preferences (Adam's name, working style if known)
   - Architectural Principles (experienced developer audience insight)
   - Persistent Risks (R002, R003 without phase numbers)
   - Reference Library (already present)

2. `.ushabti/vizier.md` total length is between 40-60 lines

3. `agents/vizier.md` includes explicit examples of evergreen vs ephemeral content in the memory boundaries section

4. The "evergreen test" principle is documented in `agents/vizier.md`: "Will this be useful in 6 months without knowing what phase we're on or what was recently discussed?"

5. `.claude-plugin/plugin.json` version field is incremented

6. All YAML and JSON files remain valid

## Risks / Notes

**Intentional tradeoffs:**
- This Phase focuses on defining the structure, not populating all possible evergreen content. Future phases may add to user preferences or principles as they're discovered.

**Related work:**
- Phase 0010 reduced Vizier memory to eliminate ephemeral bloat; this Phase restores the balance
