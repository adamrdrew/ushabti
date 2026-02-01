# Implementation Steps

## S001: Create Vizier agent definition

**Intent**: Define the Vizier agent with proper front matter and complete specification.

**Work**:
- Create `agents/vizier.md`
- Define YAML front matter (name, description, model, color, skills, tools)
- Write agent prompt covering:
  - Purpose and role (advisory only)
  - Hard invariants (cannot modify code, laws, style, or anything except vizier.md)
  - Memory system at `.ushabti/vizier.md`
  - Startup behavior (check for memory, create/seed if missing, operate in loop)
  - Character traits (humble, honest, prioritizes truth)
  - Knowledge requirements (docs, code, phases, risks, high-impact work)

**Done when**:
- File `agents/vizier.md` exists
- YAML front matter is valid and complete
- Agent prompt clearly defines role, constraints, memory system, and behavior

## S002: Register Vizier in plugin manifest

**Intent**: Make Vizier discoverable by Claude Code.

**Work**:
- Add `"./agents/vizier.md"` to the `agents` array in `.claude-plugin/plugin.json`
- Place after overseer to maintain alphabetical/logical ordering

**Done when**:
- `.claude-plugin/plugin.json` includes Vizier in agents array
- JSON is valid

## S003: Update existing agents to ignore vizier.md

**Intent**: Ensure agent isolation by preventing all other agents from reading or interacting with Vizier's memory.

**Work**:
- Edit all six existing agent files (lawgiver.md, artisan.md, surveyor.md, scribe.md, builder.md, overseer.md)
- Add explicit instruction to ignore `.ushabti/vizier.md` in each agent's constraints or procedure section

**Done when**:
- All six agent files contain explicit instruction to ignore `.ushabti/vizier.md`
- Instructions are clear and unambiguous

## S004: Update CLAUDE.md agent table

**Intent**: Reflect Vizier in the primary repository guidance file.

**Work**:
- Add Vizier row to the agent table in CLAUDE.md
- Include purpose and "Does NOT" constraints
- Update agent count from "Six" to "Seven"

**Done when**:
- CLAUDE.md agent table includes Vizier
- Agent count updated
- Table formatting consistent with existing entries

## S005: Document Vizier in agents.md

**Intent**: Provide comprehensive Vizier documentation in the project docs.

**Work**:
- Update `.ushabti/docs/agents.md`
- Add Vizier to the agent summary table
- Add full Vizier section covering:
  - File location
  - Purpose
  - Tools
  - Inputs
  - Outputs (vizier.md memory)
  - Startup behavior
  - Handoff (N/A - advisory only)
  - Isolation requirements

**Done when**:
- `.ushabti/docs/agents.md` includes Vizier in summary table
- Full Vizier section exists and matches format of other agent sections
- Documentation accurately reflects Vizier's unique role

## S006: Update README.md with Vizier documentation

**Intent**: Add Vizier to the repository README in the Agents section, matching the format used for other agents.

**Work**:
- Update README.md Agents section
- Add Vizier subsection with:
  - Purpose (advisory only - helps understand code, evaluate options, identify risks)
  - Capabilities (answers questions, provides analysis, maintains memory)
  - Constraints (does not plan, build, review, or modify code)
- Update agent count from "six" to "seven"
- Ensure formatting and tone match existing agent descriptions

**Done when**:
- README.md includes Vizier in the Agents section
- Agent count updated from six to seven
- Description accurately reflects Vizier's advisory role and constraints
- Formatting matches existing agent entries

## S007: Validate plugin

**Intent**: Verify plugin structure and manifest correctness.

**Work**:
- Run `claude plugin validate .` from repository root
- Verify command exits with success (exit code 0)
- If validation fails, fix issues and re-validate

**Done when**:
- Command `claude plugin validate .` exits successfully
- No validation errors reported

## S008: Increment plugin version

**Intent**: Signal that the plugin has been updated per L08.

**Work**:
- Update `version` field in `.claude-plugin/plugin.json` from `1.4.0` to `1.5.0`

**Done when**:
- Plugin version is `1.5.0` in `.claude-plugin/plugin.json`
- JSON is valid
