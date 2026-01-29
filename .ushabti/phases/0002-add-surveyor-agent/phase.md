# Phase 0002: Add Surveyor Agent

## Intent

Ushabti currently assumes projects begin with Lawgiver and Artisan to establish laws and style. However, developers onboarding an existing codebase need a way to generate baseline documentation before planning Phases.

The Surveyor agent fills this gap. It creates structured documentation in `.ushabti/docs/` that other agents can reference when planning and building. It operates in four sequential parts:

1. **Setup** — Create directories and check for prior surveys
2. **Discovery and Planning** — Explore the codebase and plan documentation
3. **Writing Documentation** — Create docs stepwise from the plan
4. **Verification and Handoff** — Confirm completeness and suggest next agent

This Phase adds the Surveyor agent to the Ushabti plugin.

## Scope

### In scope

- Create `agents/surveyor.md` with complete agent prompt
- Register the agent in `.claude-plugin/plugin.json`
- Increment plugin version
- Validate the plugin after registration
- Update CLAUDE.md agent table to include Surveyor

### Out of scope

- Implementing any skills the Surveyor might use
- Creating the `.ushabti/docs/` directory structure (the agent does this at runtime)
- Modifying existing agents
- Changing laws or style

## Constraints

- **L02 (Agent Location):** Agent file must be in `agents/`
- **L03 (Agent File Format):** Must be markdown with YAML front matter
- **L06 (Plugin Manifest Completeness):** Must register in plugin.json agents array
- **L07 (Plugin Validation on Addition):** Must run `claude plugin validate .` successfully
- **L08 (Version Increment):** Must increment version in plugin.json
- **Style (Clarity):** Agent prompt must be explicit and unambiguous for LLM consumption
- **Style (Brevity):** No filler; say what needs saying
- **Style (Theme):** Restrained Egyptian references acceptable if they do not obscure meaning

## Acceptance Criteria

1. `agents/surveyor.md` exists with valid YAML front matter and complete agent prompt
2. The agent prompt defines all four parts (Setup, Discovery/Planning, Writing, Verification/Handoff) with clear instructions
3. `plugin.json` includes `./agents/surveyor.md` in the agents array
4. `plugin.json` version is incremented from current value
5. `claude plugin validate .` exits with code 0
6. CLAUDE.md agent table includes Surveyor with correct purpose and boundaries
7. Agent prompt includes hard role boundaries consistent with other agents
8. Agent prompt specifies the exact file formats for `index.md`, `surveyor.md`, and documentation files

## Risks / Notes

- The Surveyor creates files at runtime (`.ushabti/docs/`, `surveyor.md`). This Phase only defines the agent; it does not pre-create those directories.
- The Surveyor interacts with the user (asking confirmation if a prior survey exists). The prompt must handle this interaction clearly.
- The Surveyor commits changes (Part D). The prompt must specify commit message format.
- The handoff logic depends on checking for `laws.md` and `style.md`. The prompt must describe this conditional flow precisely.
- This is the first agent that creates substantial new files outside `.ushabti/phases/`. The pattern established here may influence future agents.
