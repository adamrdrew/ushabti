# Phase Files Reference

## Overview

Each Phase is a bounded unit of work stored in its own directory under `.ushabti/phases/`. This document details the structure and format of all Phase files.

## Directory Structure

```
.ushabti/phases/NNNN-short-slug/
├── phase.md        # Intent, scope, acceptance criteria
├── steps.md        # Ordered implementation steps
├── progress.yaml   # Machine-tracked state
└── review.md       # Review findings
```

### Naming Convention

- **Phase ID**: Zero-padded, sequential (0001, 0002, 0003, ...)
- **Slug**: Short, lowercase, hyphenated, descriptive
- **Example**: `0003-http-client-retry`

## phase.md

Defines what the Phase accomplishes and how success is measured.

### Required Sections

```markdown
# Phase NNNN: Title

## Intent

What this Phase accomplishes and why it exists now.

## Scope

### In scope

- Item 1
- Item 2

### Out of scope

- Item 1
- Item 2

## Constraints

References to relevant laws and style sections that affect this Phase.

## Acceptance Criteria

1. Concrete, verifiable condition
2. Another verifiable condition
3. ...

## Risks / Notes

Known tradeoffs or intentionally deferred work.
```

### Guidelines

- Intent should explain both what and why
- Scope boundaries must be explicit
- Acceptance criteria must be verifiable by Overseer
- List constraints by law/style ID when applicable

## steps.md

Lists ordered steps for implementation.

### Step Format

```markdown
## S001 — Short Title

**Intent**: Why this step exists.

**Work**: What needs to be done.

**Done when**: Observable condition that proves completion.
```

### Rules

- Prefer 5-15 steps per Phase
- Steps must be ordered (dependencies reflected in order)
- Tests are first-class steps, not implied
- Each step should be independently verifiable

### Example

```markdown
## S001 — Add retry configuration struct

**Intent**: Define the data structure for retry settings.

**Work**: Create a `RetryConfig` struct with fields for max attempts, backoff duration, and retry conditions.

**Done when**: The struct exists and compiles.

---

## S002 — Implement retry logic

**Intent**: Add the actual retry behavior.

**Work**: Wrap HTTP calls with retry logic using the config from S001.

**Done when**: HTTP calls are retried according to configuration.

---

## S003 — Add retry tests

**Intent**: Verify retry behavior works correctly.

**Work**: Write unit tests covering success, retry on failure, and max attempts exceeded.

**Done when**: Tests exist and pass.
```

## progress.yaml

Machine-readable state of the Phase.

### Schema

```yaml
phase:
  id: "NNNN"
  slug: short-slug
  title: Phase Title
  status: planned|building|review|complete

steps:
  - id: S001
    title: Short title
    implemented: false
    reviewed: false
    notes: ""
    touched: []

  - id: S002
    title: Another step
    implemented: false
    reviewed: false
    notes: ""
    touched: []
```

### Phase Status Values

| Status | Meaning |
|--------|---------|
| `planned` | Phase created by Scribe, not yet started |
| `building` | Builder is implementing steps |
| `review` | All steps implemented, awaiting Overseer review |
| `complete` | Overseer approved, Phase is green |

### Status Transitions

```
planned --> building --> review --> complete
                ^          |
                |          v
                +-- (needs work)
```

### Field Ownership

| Field | Set By | Notes |
|-------|--------|-------|
| `implemented` | Builder | Set to `true` when step is done |
| `reviewed` | Overseer | Set to `true` when step passes review |
| `notes` | Builder/Overseer | Concise explanation of work done or issues |
| `touched` | Builder | List of files meaningfully modified |

### Example (in progress)

```yaml
phase:
  id: "0003"
  slug: http-client-retry
  title: Add HTTP Client Retry Logic
  status: building

steps:
  - id: S001
    title: Add retry configuration struct
    implemented: true
    reviewed: false
    notes: "Created RetryConfig in pkg/http/retry.go"
    touched:
      - pkg/http/retry.go

  - id: S002
    title: Implement retry logic
    implemented: false
    reviewed: false
    notes: ""
    touched: []

  - id: S003
    title: Add retry tests
    implemented: false
    reviewed: false
    notes: ""
    touched: []
```

## review.md

Created by Scribe as a scaffold, filled by Overseer during review.

### Format

```markdown
# Review: Phase NNNN

## Summary

Overall assessment of the Phase.

## Verified

- What was confirmed as complete and correct

## Issues

- Problems found during review

## Required Follow-ups

- Additional steps needed (if any)

## Decision

[COMPLETE | NEEDS WORK]

Explanation of decision.
```

### Example (approved)

```markdown
# Review: Phase 0003

## Summary

HTTP client retry logic implemented as planned. All acceptance criteria met.

## Verified

- RetryConfig struct exists with correct fields
- Retry logic wraps HTTP calls correctly
- Backoff behavior matches specification
- All tests pass

## Issues

None.

## Required Follow-ups

None.

## Decision

COMPLETE

The work has been verified against acceptance criteria and passes review.
```

### Example (needs work)

```markdown
# Review: Phase 0003

## Summary

Implementation mostly complete but missing error type handling.

## Verified

- RetryConfig struct exists
- Basic retry logic works
- Tests exist

## Issues

- S002: Retry logic does not distinguish between retryable and non-retryable errors
- S003: No test for non-retryable error handling

## Required Follow-ups

- S004: Add retryable error classification
- S005: Add test for non-retryable errors

## Decision

NEEDS WORK

Two follow-up steps have been added to steps.md and progress.yaml.
```
