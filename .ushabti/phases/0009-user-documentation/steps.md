# Implementation Steps

## S001: Create docs directory structure

**Intent**: Establish the top-level documentation directory that will house all user-facing guides.

**Work**:
- Create `docs/` directory at repository root
- Verify directory is created at correct location (not inside `.ushabti/`)

**Done when**:
- Directory `/docs/` exists at repository root
- Directory is empty and ready to receive documentation files

---

## S002: Write getting-started.md

**Intent**: Provide new users with essential onboarding information covering prerequisites, installation, and core concepts.

**Work**:
- Create `docs/getting-started.md`
- Document prerequisites (Claude Code installation)
- Document plugin installation via marketplace
- Explain permissions configuration
- Introduce all seven agents (Lawgiver, Artisan, Surveyor, Scribe, Builder, Overseer, Vizier)
- Explain the Plan → Build → Review development loop
- Provide guidance on when to use each agent
- Include clear examples where helpful

**Done when**:
- File exists and is syntactically valid markdown
- All seven agents are described with their purposes
- Development loop is clearly explained with visual representation if helpful
- Prerequisites and installation steps are accurate and complete
- Content is clear, concise, and actionable for new users

---

## S003: Write greenfield.md

**Intent**: Provide a clear workflow for users starting a new project from scratch with Ushabti.

**Work**:
- Create `docs/greenfield.md`
- Document step-by-step workflow for new projects
- Explain bootstrapping process (Lawgiver → Artisan → Surveyor)
- Cover initial Phase planning with Scribe
- Show complete flow through first Phase (Plan → Build → Review)
- Explain how to continue with subsequent Phases
- Include practical examples or patterns where helpful

**Done when**:
- File exists and is syntactically valid markdown
- Workflow is presented in clear, ordered steps
- All critical bootstrapping agents are covered
- Examples or patterns help clarify the process
- Content enables a new user to successfully start a greenfield project

---

## S004: Write brownfield.md

**Intent**: Provide a clear workflow for users onboarding Ushabti onto an existing codebase.

**Work**:
- Create `docs/brownfield.md`
- Document step-by-step workflow for existing projects
- Emphasize Surveyor-first approach and why it matters
- Explain how Surveyor documentation integrates with subsequent work
- Cover establishing laws and style after documentation
- Address common concerns (impact on existing code, gradual adoption, etc.)
- Show how to begin Phase loop with existing codebase context

**Done when**:
- File exists and is syntactically valid markdown
- Surveyor-first workflow is clearly explained
- Distinction from greenfield approach is clear
- Common concerns are addressed
- Content enables a new user to successfully onboard an existing project

---

## S005: Write tips-and-tricks.md

**Intent**: Document advanced patterns, non-obvious features, and effective usage strategies discovered through framework use.

**Work**:
- Create `docs/tips-and-tricks.md`
- Document Vizier usage patterns (asking questions, requesting memory)
- Explain how docs system integrates with Phase loop
- Document available skills and how users can invoke them
- Include patterns like:
  - Using Vizier to evaluate options before planning
  - Asking Vizier to remember project-specific context
  - How and when to split Phases
  - Effective acceptance criteria writing
  - Leveraging progress.yaml for tracking
- Add at least 5-7 distinct tips that are valuable but not obvious from basic usage

**Done when**:
- File exists and is syntactically valid markdown
- Contains at least five non-obvious but valuable patterns
- Vizier usage is well-documented
- Skills system is explained with examples
- Docs loop integration is clear
- Content provides genuine value beyond basic documentation

---

## S006: Update README with documentation links

**Intent**: Make new documentation prominent and easily discoverable while maintaining README's role as high-level overview.

**Work**:
- Add "Documentation" or "Getting Started" section early in README (after Installation, before Core Idea)
- Link to all four new documentation files with brief descriptions
- Ensure links are prominent and impossible to miss for new users
- Verify all links work correctly

**Done when**:
- Documentation section exists in README
- Section appears early (within first few major sections)
- All four docs files are linked with helpful descriptions
- Links are valid and correctly formatted
- Section is visually prominent

---

## S007: Remove redundant content from README

**Intent**: Streamline README by removing content that's covered in greater depth in the new documentation, while preserving high-level overview.

**Work**:
- Review README for content that duplicates new docs
- Remove or significantly shorten sections that are covered in detail elsewhere
- Maintain high-level overview of all features
- Replace detailed explanations with brief summaries and links to docs
- Preserve README's role as entry point and overview
- Keep essential quick-reference information
- Ensure README remains coherent after edits

**Done when**:
- Redundant detailed content is removed or condensed
- README maintains high-level overview character
- All removed content is available in linked documentation
- README remains coherent and useful as entry point
- No information is lost, only relocated

---

## S008: Cross-reference validation

**Intent**: Ensure all documentation is internally consistent, accurate, and free of broken links.

**Work**:
- Verify all internal links between documentation files work
- Check that README links to docs directory are valid
- Verify no contradictions exist between different documentation files
- Confirm all agent names, counts, and descriptions are consistent
- Validate workflow steps are consistent across all docs
- Check that all technical details (file paths, commands, etc.) are accurate

**Done when**:
- All links are validated as working
- No contradictions exist between docs
- Agent information is consistent across all files
- Technical details are verified as accurate
- Documentation forms a coherent, consistent whole

---

## S009: Quality review

**Intent**: Ensure all documentation meets style guidelines and quality standards.

**Work**:
- Verify all markdown is syntactically valid
- Check adherence to style guide (ATX headers, fenced code blocks, line length)
- Verify clarity and conciseness throughout
- Check for ambiguous language or unclear instructions
- Ensure appropriate restraint with theme references
- Verify no emoji overload or forced Egyptian references
- Confirm documentation reflects current project state

**Done when**:
- All markdown files are syntactically valid
- Style guide conventions are followed consistently
- Language is clear, concise, and unambiguous
- Theme usage is appropriate and restrained
- Documentation accurately reflects Ushabti as implemented
- All quality standards from acceptance criteria are met
