# Phase 0006: Add Vizier Agent

## Intent

Add Vizier, a conversational advisory agent that helps the human developer understand code, evaluate options, identify risks, and suggest high-impact work. Vizier is fundamentally different from other Ushabti agents: it does not plan, build, review, or modify code. It only answers questions, provides analysis, and maintains its own memory.

This Phase introduces the agent definition, establishes its isolation from other agents, and updates all relevant documentation.

## Scope

**In scope**:
- Create Vizier agent definition file
- Register Vizier in plugin manifest
- Update all existing agent definitions to ignore `.ushabti/vizier.md`
- Update CLAUDE.md to include Vizier in agent table
- Update `.ushabti/docs/agents.md` to document Vizier
- Update README.md to include Vizier in Agents section
- Validate plugin after changes
- Increment plugin version

**Out of scope**:
- Creating initial `.ushabti/vizier.md` memory file (Vizier creates this on first run)
- Any actual invocation or testing of Vizier
- Changes to existing agent behavior beyond ignoring vizier.md

## Constraints

### Laws
- **L02**: Vizier agent must reside in `agents/` directory
- **L03**: Agent file must be markdown with YAML front matter
- **L06**: Vizier must be registered in `.claude-plugin/plugin.json`
- **L07**: Plugin must be validated after addition
- **L08**: Version must be incremented

### Style
- Clarity and brevity in all prose
- YAML with 2-space indentation, explicit true/false
- Documentation must reflect current project state

## Acceptance Criteria

1. File `agents/vizier.md` exists with valid YAML front matter and complete agent specification
2. Vizier is registered in `.claude-plugin/plugin.json` agents array
3. All six existing agent files (lawgiver, artisan, surveyor, scribe, builder, overseer) explicitly state they must ignore `.ushabti/vizier.md`
4. CLAUDE.md agent table includes Vizier with correct purpose and constraints
5. `.ushabti/docs/agents.md` includes Vizier documentation matching the format of other agents
6. README.md includes Vizier in the Agents section with purpose, capabilities, and constraints matching the format of other agents
7. Agent count updated from "six" to "seven" in both README.md and CLAUDE.md
8. Command `claude plugin validate .` exits with success (exit code 0)
9. Plugin version incremented from 1.4.0 to 1.5.0 in `.claude-plugin/plugin.json`

## Risks / Notes

- Vizier's role is advisory only. The hard constraint against modifying anything (except its own memory) must be crystal clear in the agent definition
- All existing agents must be explicitly told to ignore vizier.md to prevent cross-contamination
- Vizier's startup behavior (creating and seeding memory on first run) is documented but not implemented in this Phase
