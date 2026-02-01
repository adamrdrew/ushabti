# Phase 0007: Vizier Documentation Library

## Intent

Enhance the Vizier agent with a reference documentation library capability. The Vizier should maintain a curated collection of links to official documentation for the major technologies used in the project, consult this library when answering questions, and keep it updated as the project evolves.

This makes the Vizier more studious and better equipped to provide informed, accurate guidance by grounding its analysis in authoritative technical documentation.

##Scope

**In scope**:
- Modify Vizier agent definition to add documentation library responsibilities
- Update Vizier's memory structure specification to include Reference Library section
- Add instructions for identifying major technologies
- Add instructions for searching and curating official documentation links
- Add instructions for consulting the library judiciously
- Add instructions for pre-populating the library during initial vizier.md creation
- Update `.ushabti/docs/agents.md` to document the library capability
- Update README.md to reflect the library capability
- Validate plugin after changes
- Increment plugin version

**Out of scope**:
- Creating or modifying any actual vizier.md file (Vizier creates this on first run)
- Modifying any other agents
- Creating new skills or tools
- Implementing web search capabilities (Vizier uses existing tools)

## Constraints

### Laws
- **L03**: Agent file must remain markdown with YAML front matter
- **L06**: Agent must remain registered in plugin manifest
- **L07**: Plugin must be validated after changes
- **L08**: Version must be incremented (1.5.0 → 1.6.0)

### Style
- Clarity and brevity in all prose
- Documentation must reflect current project state
- No forced Egyptian references that obscure meaning

## Acceptance Criteria

1. File `agents/vizier.md` includes comprehensive documentation library instructions
2. Vizier agent prompt specifies memory structure with "Reference Library" section
3. Instructions clearly state only official/first-party sources allowed (no blogs, Medium, Stack Overflow, Reddit, Substack)
4. Instructions specify when and how to consult the library (judiciously, not aggressively)
5. Instructions specify pre-populating the library when creating vizier.md for the first time
6. Instructions specify keeping the library updated as the project grows
7. `.ushabti/docs/agents.md` Vizier section documents the library capability
8. README.md Vizier section mentions the library capability
9. Command `claude plugin validate .` exits with success (exit code 0)
10. Plugin version incremented from 1.5.0 to 1.6.0 in `.claude-plugin/plugin.json`

## Risks / Notes

- The library must remain focused on official sources to ensure accuracy and authority
- The Vizier should consult the library to enhance answers, not replace its own reasoning
- Pre-population of the library during onboarding ensures immediate value
- The library adds value by grounding the Vizier's analysis in authoritative technical knowledge
