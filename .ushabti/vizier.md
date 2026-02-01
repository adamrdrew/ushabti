# Vizier Memory

## Project Context

Ushabti is a file-backed, agent-driven development system distributed as a Claude Code plugin. Development happens in bounded Phases (planned, implemented, reviewed) tracked in `.ushabti/phases/`. Seven specialized agents handle distinct responsibilities: Lawgiver (laws), Artisan (style), Surveyor (onboarding), Scribe (planning), Builder (implementation), Overseer (review), and Vizier (advisory). The system is built with TypeScript for the VS Code extension and uses React for any UI components.

## User Preferences

- User's name: Adam
- Prefers structured, disciplined development workflows
- Values explicit boundaries and role clarity

## Architectural Principles

Ushabti targets experienced developers who know what they want. The system assumes competence and provides structure without hand-holding. Agents enforce boundaries strictly — no agent steps outside its defined role. Phase completion requires Overseer approval; no work is "done" until reviewed and approved.

## Persistent Risks

**R002: No automated validation of phase files**
Phase files (phase.md, steps.md, progress.yaml) are hand-edited. Structural errors or invalid YAML can break workflows. Manual review is the only current safeguard.

**R003: Missing user onboarding examples**
New users lack concrete examples of complete Phase cycles. Documentation describes the system but doesn't show realistic end-to-end workflows.

## Reference Library

### Languages
- [TypeScript Documentation](https://www.typescriptlang.org/docs/) — Official TypeScript language documentation
- [JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) — MDN JavaScript reference
- [Markdown Guide](https://www.markdownguide.org/) — Markdown syntax reference
- [YAML Specification](https://yaml.org/spec/) — YAML format specification
- [JSON Specification](https://www.json.org/) — JSON format specification
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/) — GNU Bash documentation

### Frameworks
- [React Documentation](https://react.dev/) — Official React documentation
- [Node.js Documentation](https://nodejs.org/docs/latest/api/) — Official Node.js API documentation

### Tools
- [Claude Code Documentation](https://docs.anthropic.com/claude/docs/claude-code) — Official Claude Code documentation
- [Git Documentation](https://git-scm.com/doc) — Official Git documentation
- [VS Code Extension API](https://code.visualstudio.com/api) — Visual Studio Code extension development
