# Implementation Steps

## S001: Update vizier.md with evergreen structure

**Intent**: Establish the balanced memory structure with all required evergreen sections.

**Work**:
- Read current `.ushabti/vizier.md` to preserve existing Reference Library content
- Add Project Context section (3-5 line summary of Ushabti core purpose and stack)
- Add User Preferences section (include user's name: Adam)
- Add Architectural Principles section (state "Ushabti is for experienced developers who know what they want" as fact)
- Add Persistent Risks section (include R002: no automated validation, R003: missing user onboarding examples - without phase number references)
- Ensure Reference Library section remains intact
- Verify total file length is 40-60 lines

**Done when**:
- `.ushabti/vizier.md` contains all five sections
- Total line count is between 40-60 lines
- No narrative or temporal markers present
- File is syntactically valid Markdown

## S002: Add evergreen examples to agent definition

**Intent**: Prevent future over-correction by explicitly defining what belongs in memory with concrete examples.

**Work**:
- Read `agents/vizier.md` memory boundaries section
- Add explicit examples of evergreen content:
  - "Project Context: 'Ushabti is a file-backed agent system for Claude Code using TypeScript and React'"
  - "User Preferences: 'User prefers TypeScript over JavaScript'"
  - "Architectural Principles: 'Ushabti targets experienced developers who know what they want'"
  - "Persistent Risks: 'R002: No automated validation of phase files exists'"
- Add explicit examples of ephemeral content to avoid:
  - "Conversation logs: 'User mentioned preferring TypeScript in our discussion about stack choices'"
  - "State tracking: 'Phase 0008 is currently in review'"
  - "Temporal markers: 'As of last week, we decided...'"
  - "Discovery narrative: 'During analysis, I discovered that...'"

**Done when**:
- `agents/vizier.md` contains both evergreen and ephemeral examples in the memory boundaries section
- Examples are concrete and unambiguous
- Section clearly distinguishes what to store vs what to avoid

## S003: Document the evergreen test

**Intent**: Provide a clear principle for future memory decisions.

**Work**:
- Add "The Evergreen Test" subsection to the memory boundaries section in `agents/vizier.md`
- Include the test question: "Will this be useful in 6 months without knowing what phase we're on or what was recently discussed?"
- Specify the decision rule: "If yes, consider storing. If no, don't store."
- Add clarification: "Evergreen content remains valuable across phases and conversations. Ephemeral content is tied to specific moments in time."

**Done when**:
- The evergreen test is documented with the exact question, decision rule, and clarification
- Placement is logical within the memory boundaries section
- Language is clear and actionable

## S004: Increment plugin version

**Intent**: Satisfy L08 requirement for version increment on Phase completion.

**Work**:
- Read `.claude-plugin/plugin.json`
- Increment the `version` field according to semantic versioning
- Ensure JSON remains valid

**Done when**:
- `version` field in `.claude-plugin/plugin.json` is incremented
- JSON file is syntactically valid
- No other fields are modified

## S005: Validate all changes

**Intent**: Ensure all modifications maintain file validity and meet acceptance criteria.

**Work**:
- Verify `.ushabti/vizier.md` is valid Markdown
- Verify `.ushabti/vizier.md` line count is 40-60
- Verify `agents/vizier.md` is valid Markdown with valid YAML front matter
- Verify `.claude-plugin/plugin.json` is valid JSON
- Check that all acceptance criteria from phase.md are met

**Done when**:
- All files are syntactically valid
- Line count requirement is met
- All acceptance criteria pass verification
