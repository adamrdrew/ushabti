# Phase 0009: User Documentation

## Intent

Create comprehensive, user-facing documentation to help new users understand and effectively use Ushabti. Currently, the README provides a high-level overview and `.ushabti/docs` contains internal documentation for agents. New users need clearer onboarding materials that explain the development loop, agent roles, workflow differences between greenfield and brownfield projects, and non-obvious patterns for effective use.

This Phase adds a top-level `docs/` directory with four focused guides and refactors the README to be leaner while prominently linking to these resources.

## Scope

### In Scope

- Create `docs/` directory at repository root
- Write `docs/getting-started.md` covering prerequisites, installation, agent overview, and development loop
- Write `docs/greenfield.md` explaining how to start a new project with Ushabti
- Write `docs/brownfield.md` explaining how to onboard Ushabti onto an existing project
- Write `docs/tips-and-tricks.md` with advanced but useful patterns and non-obvious usage guidance
- Update README to:
  - Link prominently to new documentation early in the file
  - Remove redundant content covered in greater detail in the docs
  - Maintain high-level overview while referring readers to docs for depth

### Out of Scope

- Changes to `.ushabti/docs/` (internal agent documentation)
- Changes to agent prompts or behavior
- Changes to plugin functionality
- Tutorial videos or interactive content

## Constraints

### Relevant Laws

- **L08 (Version Increment)**: This is a documentation-only Phase that does not affect plugin behavior. Version bump is explicitly skipped per the law's exception clause.

### Relevant Style

- **Documentation Accuracy**: New docs must reflect current project state
- **Clarity**: Write explicitly for both humans and LLMs; avoid ambiguity
- **Brevity**: Say what needs saying, no more
- **Markdown**: ATX-style headers, fenced code blocks with language specifiers, lines under 120 characters where practical
- **Theme**: Restrained Egyptian references only where they add value without obscuring meaning

## Acceptance Criteria

1. **Directory Structure**
   - `docs/` directory exists at repository root
   - Contains exactly four markdown files: `getting-started.md`, `greenfield.md`, `brownfield.md`, `tips-and-tricks.md`

2. **Getting Started Guide**
   - Covers prerequisites (Claude Code, plugin installation)
   - Explains installation via marketplace
   - Introduces all seven agents with clear role descriptions
   - Explains the Plan → Build → Review loop
   - Provides guidance on when to use each agent

3. **Greenfield Guide**
   - Clear step-by-step workflow for starting a new project
   - Explains bootstrapping with Lawgiver and Artisan
   - Covers initial Phase creation and execution
   - Provides concrete examples or patterns

4. **Brownfield Guide**
   - Clear step-by-step workflow for onboarding existing projects
   - Emphasizes Surveyor-first approach
   - Explains how docs integrate with subsequent Phase work
   - Addresses common concerns when introducing Ushabti to existing codebases

5. **Tips and Tricks Guide**
   - Includes at least five non-obvious but valuable patterns
   - Covers Vizier usage and memory
   - Explains docs system integration with Phase loop
   - Documents available skills and user-invokable capabilities
   - Provides patterns discovered through framework use

6. **README Updates**
   - Links to new documentation appear prominently in first few sections
   - Redundant content has been removed where covered in detail elsewhere
   - High-level overview remains intact
   - All links to new docs are valid and correctly formatted

7. **Quality Standards**
   - All markdown files are syntactically valid
   - No broken internal links
   - Consistent tone and style across all docs
   - No contradictions between different documentation files
   - Content is accurate relative to current Ushabti implementation

## Risks / Notes

- **Content Duplication Risk**: Must be careful to avoid duplicating content between README and new docs. README should provide overview and links; docs should provide depth.
- **Documentation Drift**: These docs must be maintained as Ushabti evolves. Future Phases that change workflow or add agents must update these docs.
- **No Version Bump**: This Phase explicitly skips version increment per L08 exception for documentation-only changes that don't affect plugin behavior.
