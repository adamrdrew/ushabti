# Vizier Memory

## Project Context

Ushabti is a file-backed, agent-driven development system implemented as a Claude Code plugin. Development happens in bounded Phases that are planned (Scribe), implemented (Builder), reviewed (Overseer), and completed. All state lives in files under `.ushabti/`, not chat history.

The project uses no traditional programming languages. All implementation consists of markup files: Markdown (agent definitions, documentation), JSON (plugin manifest), and YAML (phase progress tracking).

## User Preferences

User goes by Adam.

## Architectural Principles

Ushabti targets experienced developers who know what they want. Agents have strictly enforced boundaries. No agent can plan, build, and review.

The Phase loop (Plan → Build → Review) is the core workflow. No Phase is complete without Overseer approval.

## Persistent Risks

R001: Card directory structure is not automatically created during bootstrap. If users attempt to create cards before running Lawgiver (which does bootstrap `.ushabti/` and `.ushabti/docs/`), card operations will fail because `.ushabti/cards/` doesn't exist. Card skills lack just-in-time directory creation logic.

## Reference Library

### Languages
- [Markdown Guide](https://www.markdownguide.org/) - Markdown syntax and best practices
- [YAML Specification](https://yaml.org/spec/) - Official YAML specification
- [JSON](https://json.org/) - JSON format specification

### Tools
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code) - Official Claude Code documentation
- [Git Documentation](https://git-scm.com/doc) - Official Git documentation
