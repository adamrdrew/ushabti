# Implementation Steps

## S001: Update Vizier memory structure specification

**Intent**: Define the Reference Library section in the Vizier's memory structure.

**Work**:
- Edit `agents/vizier.md` Memory system section
- Specify that vizier.md includes a "Reference Library" section
- Document what the Reference Library contains: links to official documentation for major technologies
- Specify structure: organized by category (Languages, Frameworks, Libraries, Tools)

**Done when**:
- Memory system section in `agents/vizier.md` describes Reference Library section
- Structure is clearly defined
- Purpose is explicit

## S002: Add technology identification instructions

**Intent**: Instruct Vizier to identify and track major technologies used in the project.

**Work**:
- Add "Technology Identification" subsection to Capabilities section in `agents/vizier.md`
- Instruct Vizier to identify languages, frameworks, libraries, and tools the project depends on
- Explain this happens during initial memory creation and as the project evolves

**Done when**:
- Instructions for identifying major technologies are clear and complete
- Scope includes languages, frameworks, libraries, and tools
- Timing is specified (initial creation and ongoing updates)

## S003: Add documentation curation instructions

**Intent**: Define how Vizier should search for and curate official documentation links.

**Work**:
- Add "Documentation Curation" subsection to Capabilities section in `agents/vizier.md`
- Instruct Vizier to search for authoritative sources
- Explicitly list allowed sources: official language docs, framework docs, library docs
- Explicitly list forbidden sources: blogs, Medium, Stack Overflow, Substack, Reddit, or similar third-party sources
- Specify first-party/official sources only

**Done when**:
- Instructions specify what sources are allowed (official/first-party only)
- Instructions explicitly forbid third-party sources with examples
- Curation process is clear

## S004: Add library consultation instructions

**Intent**: Define when and how Vizier should consult the documentation library.

**Work**:
- Add "Library Consultation" subsection to Capabilities section in `agents/vizier.md`
- Instruct to consult judiciously, not aggressively
- Specify priority: answer with project knowledge, product knowledge, or built-in knowledge first
- Specify to consult library when uncertain or when deeper technical details are needed
- Give example: security risk analysis should combine code review with documentation consultation

**Done when**:
- Instructions specify judicious (not aggressive) consultation
- Priority ordering is clear (project/product/built-in knowledge first, library when needed)
- Example use case is provided
- Balance between using library and existing knowledge is explicit

## S005: Add library pre-population instructions

**Intent**: Ensure Vizier pre-populates the library when creating vizier.md for the first time.

**Work**:
- Update Startup behavior section in `agents/vizier.md`
- Modify step 2 (when vizier.md is missing) to include pre-populating Reference Library
- Specify seeding with select relevant links for core technologies
- Maintain existing seeding for other sections (Observations, Risks, High-Impact Work, Notes)

**Done when**:
- Startup behavior step 2 includes pre-populating Reference Library
- Instruction specifies seeding with core technology documentation
- Other memory sections (Observations, Risks, etc.) remain specified

## S006: Add library maintenance instructions

**Intent**: Instruct Vizier to keep the library updated as the project changes.

**Work**:
- Add "Library Maintenance" subsection to Capabilities section in `agents/vizier.md`
- Instruct to add new technologies as they're introduced
- Instruct to update links if sources change
- Instruct to remove entries for deprecated or removed technologies

**Done when**:
- Instructions cover adding new technologies
- Instructions cover updating existing links
- Instructions cover removing obsolete entries
- Maintenance is framed as ongoing responsibility

## S007: Add developer reference instructions

**Intent**: Enable Vizier to refer developers to relevant documentation.

**Work**:
- Add to "Library Consultation" or Capabilities section in `agents/vizier.md`
- Instruct Vizier to include relevant documentation links when answering questions
- Specify this helps developers dive deeper into topics
- Maintain conversational, helpful tone

**Done when**:
- Instructions specify including relevant links in responses
- Purpose (helping developers dive deeper) is stated
- Tone guidance (helpful, not preachy) is clear

## S008: Update agents.md documentation

**Intent**: Document the Reference Library capability in the project documentation.

**Work**:
- Edit `.ushabti/docs/agents.md` Vizier section
- Add Reference Library to the Capabilities or Outputs subsection
- Describe what it contains and how it's used
- Maintain consistency with existing documentation format

**Done when**:
- `.ushabti/docs/agents.md` Vizier section mentions Reference Library
- Description is accurate and concise
- Formatting matches existing content

## S009: Update README.md

**Intent**: Reflect the Reference Library capability in the repository README.

**Work**:
- Edit README.md Vizier section
- Add Reference Library to capabilities or description
- Keep description brief and clear
- Maintain existing tone and format

**Done when**:
- README.md Vizier section mentions Reference Library capability
- Description is concise and accurate
- Formatting matches existing agent descriptions

## S010: Validate plugin

**Intent**: Verify plugin structure and manifest correctness after modifications.

**Work**:
- Run `claude plugin validate .` from repository root
- Verify command exits with success (exit code 0)
- If validation fails, fix issues and re-validate

**Done when**:
- Command `claude plugin validate .` exits successfully
- No validation errors reported

## S011: Increment plugin version

**Intent**: Signal that the plugin has been updated per L08.

**Work**:
- Update `version` field in `.claude-plugin/plugin.json` from `1.5.0` to `1.6.0`

**Done when**:
- Plugin version is `1.6.0` in `.claude-plugin/plugin.json`
- JSON is valid
