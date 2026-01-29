# Project Style Guide

## Purpose

This guide defines how we write and maintain Ushabti. Since this repository contains no traditional code—only markup (JSON, YAML, Markdown)—these conventions govern **prose** and **structured data**.

Agents and reviewers use this guide to ensure consistency across all project files.

---

## Prose Conventions

### Clarity

- Write for Large Language Models. Be explicit. Avoid ambiguity.
- State things once, correctly. No contradictions.
- Use precise terms. Define them if non-obvious.
- Avoid pronouns when the referent could be unclear.

### Brevity

Brevity is the soul of wit.

- Say what needs saying. No more.
- Cut filler words: "basically," "actually," "in order to," "the fact that."
- Prefer short sentences. One idea per sentence.
- Avoid repetition unless emphasis is intentional.

### Logic

- No contradictions. If two statements conflict, one must be removed or reconciled.
- No circular definitions. No undefined terms used as though defined.
- Conditionals must be complete: if A then B—what happens when not A?

---

## Markup Conventions

### YAML

- Must be syntactically valid.
- Use 2-space indentation.
- Quote strings containing special characters.
- Prefer explicit `true`/`false` over `yes`/`no`.

### JSON

- Must be syntactically valid.
- Use 2-space indentation for readability.
- No trailing commas.
- No comments (JSON does not support them).

### Markdown

- Use ATX-style headers (`#`, `##`, etc.).
- One blank line before headers.
- Use fenced code blocks with language specifiers.
- Lists: use `-` for unordered, `1.` for ordered.
- Keep lines under 120 characters where practical.

---

## Documentation Accuracy

- Documentation must reflect the current state of the project.
- When the project changes, update affected documentation in the same Phase.
- Stale documentation is a defect.

---

## Project Structure

Refer to `.ushabti/laws.md` for mandatory structure. Style preferences:

- Keep agent files focused. One agent, one file, one clear purpose.
- Keep skill files self-contained. A skill directory should be understandable in isolation.
- Prefer flat structures over deep nesting.

---

## Theme 🏛️

Ushabti is a serious development tool. It is also ancient Egypt–themed, because life is short.

**Acceptable:**
- Brief Egyptian references that fit naturally (e.g., "inscribe," "decree," "chamber of phases")
- Occasional thematic emoji (🏛️ 𓂀 📜) in headers or summaries
- Agent names drawn from Egyptian roles

**Not acceptable:**
- Forced references that obscure meaning
- Emoji overload
- Theme at the expense of clarity or accuracy

When in doubt, choose clarity.

---

## Review Checklist

Before declaring work complete, verify:

- [ ] All prose is clear and unambiguous
- [ ] No contradictions or logic errors
- [ ] All YAML files are valid
- [ ] All JSON files are valid
- [ ] Documentation reflects current project state
- [ ] No laws are violated (see `.ushabti/laws.md`)
- [ ] Theme usage is restrained and appropriate

---

## Revision History

| Date       | Change                           |
|------------|----------------------------------|
| 2026-01-28 | Initial style guide established  |
