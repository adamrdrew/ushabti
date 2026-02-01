# Vizier Memory

## Project Context

Ushabti is a file-backed, agent-driven development system implemented as a Claude Code plugin. The project contains no traditional programming language code—only markup (JSON, YAML, Markdown). All state lives in files under `.ushabti/`. Development happens through a Plan-Build-Review loop with specialized agents.

Core structure: Laws (invariants) → Style (conventions) → Phases (bounded work units) → Documentation (living knowledge base).

Target audience: Experienced developers who know what they want and prefer tight iteration over ceremony.

## User Preferences

User introduced themselves as Adam.

## Architectural Principles

- File-backed state over hidden state
- Bounded Phases over open-ended work
- Agent specialization with hard role boundaries
- Mandatory review before completion
- Documentation stays current with code (docs-in-the-loop)
- Skills invoked on-demand via Skill tool (not preloaded)

## Persistent Risks

None identified yet.

## Token Efficiency Research (2026-02-01)

Official Anthropic guidance on Claude Code best practices emphasizes context window management as the fundamental constraint. Key findings:

- Skills should be under 500 lines; move detailed reference to separate files
- Agent descriptions loaded into context budget (default 15,000 chars)
- Repetitive patterns across agents consume unnecessary tokens
- "Use the Skill tool to invoke X" pattern repeated 18 times across agents
- Agent isolation warning about vizier.md repeated in 6 agents (unnecessary)
- Egyptian theming guidance repeated in 7 agents (low value)

Optimization opportunities identified:
- Consolidate repeated skill invocation instructions
- Remove low-value repetitive warnings
- Simplify agent descriptions
- Skills appear well-sized (largest is 108 lines)

## Reference Library

### Languages
- [Markdown Guide](https://www.markdownguide.org/) — Markdown syntax and best practices
- [YAML Specification](https://yaml.org/spec/) — Official YAML specification
- [JSON](https://www.json.org/) — JSON syntax and structure

### Tools
- [Claude Code](https://claude.ai/code) — Claude Code platform documentation
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) — Official optimization guidance
- [Claude Code Skills](https://code.claude.com/docs/en/skills) — Skills documentation
- [Git](https://git-scm.com/doc) — Official Git documentation
