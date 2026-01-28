# Phase Files

Each Phase is a bounded, reviewable unit of work stored in its own directory under `.ushabti/phases/`.

## Phase Directory Structure

```
.ushabti/phases/NNNN-short-slug/
├── phase.md        # Intent, scope, acceptance criteria
├── steps.md        # Ordered implementation steps
├── progress.yaml   # Machine-tracked state
└── review.md       # Review findings
```

**Naming**: Phase IDs are zero-padded and sequential (0001, 0002, ...). Slugs are short, lowercase, hyphenated, and descriptive.

Example: `0003-http-client-retry`

## phase.md

Defines what the Phase accomplishes and how success is measured.

Required sections:
- **Intent**: What this Phase accomplishes and why it exists now
- **Scope**: In scope / Out of scope
- **Constraints**: References to relevant laws and style sections
- **Acceptance criteria**: Concrete, verifiable conditions for completion
- **Risks / notes**: Known tradeoffs or intentionally deferred work

Acceptance criteria must be verifiable by the Overseer.

## steps.md

Lists ordered steps for implementation. Each step must include:
- **Title**: Short description
- **Intent**: Why the step exists
- **Work**: What needs to be done
- **Done when**: Observable condition that proves completion

Rules:
- Prefer 5-15 steps
- Steps must be ordered (dependencies reflected in ordering)
- Tests are first-class steps, not implied

## progress.yaml

Machine-readable state of the Phase. Structure:

```yaml
phase:
  id: NNNN
  slug: short-slug
  title: Title
  status: planned|building|review|complete

steps:
  - id: S001
    title: Short title
    implemented: false
    reviewed: false
    notes: ""
    touched: []
```

**Status transitions**:
- `planned` → `building` (when Builder starts)
- `building` → `review` (when all steps implemented)
- `review` → `building` (if Overseer requests fixes)
- `review` → `complete` (when Overseer approves)

**Field ownership**:
- `implemented`: Set by Builder when step is done
- `reviewed`: Set only by Overseer
- `notes`: Updated by whoever completes the step
- `touched`: List of files meaningfully modified

## review.md

Created by Scribe as a scaffold, filled by Overseer during review.

Sections:
- **Summary**: Overall assessment
- **Verified**: What was confirmed
- **Issues**: Problems found
- **Required follow-ups**: Additional steps needed (if any)
- **Decision**: Complete or needs work

## What Makes a Good Phase

A Phase is:
- Small enough to complete in one tight iteration loop
- Large enough to produce visible, testable progress
- Reviewable against explicit acceptance criteria
- Internally coherent, with one primary intent

A Phase is NOT:
- An open-ended milestone
- A roadmap
- A grab-bag of unrelated tasks
- A substitute for architecture decisions

If a requested Phase is too large, split it into multiple sequential Phases.
