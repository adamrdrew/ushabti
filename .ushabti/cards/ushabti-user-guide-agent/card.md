---
created: 2026-02-01T00:00:00Z
id: 4261b35b-6a2a-4b71-94bf-f7ae85d67384
priority: low
slug: ushabti-user-guide-agent
status: todo
tags: []
title: Ushabti user guide agent
type: feature
updated: 2026-02-08T21:24:43Z
---

# Overview

When Ushabti is used in other projects, the project-specific Vizier knows
about that project's architecture, patterns, and domain - but nothing about
Ushabti itself. Users may have questions about how to use Ushabti (phase
structure, agent roles, workflows, etc.) that their project Vizier cannot
answer because it lacks Ushabti framework knowledge.

Currently this is mitigated by documentation (getting-started.md,
tips-and-tricks.md) and the skills system (25 describe-* skills), but a
conversational agent may provide a lower-friction experience for exploratory
questions.

An additional benefit: a dedicated user guide agent could answer Ushabti
questions while another agent (like Builder) is active, avoiding context
disruption mid-Phase.

# Requirements

- Create a dedicated "Ushabti Guide" agent (functional naming, not Egyptian)
- Make it read-only with no memory system (pure Q&A consultation)
- Preload all describe-* skills for immediate framework knowledge access
- Have it quote and reference canonical docs rather than replace them
- Keep scope narrow: only answer Ushabti framework questions

Before building, track actual user pain points to validate the need. If users
frequently struggle with docs or need help mid-Phase, that justifies the
effort. If docs prove sufficient, defer indefinitely.
