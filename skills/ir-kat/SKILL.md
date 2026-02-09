---
name: ir-kat
description: Execute a full Scribe → Builder → Overseer phase cycle. Use when you have a PHASE_PROMPT and want to plan, build, and review a phase end-to-end.
user-invocable: true
---

# Ir-Kat — Do The Work

Execute a complete phase cycle: plan with Scribe, build with Builder, review with Overseer. If the Overseer kicks back, the Builder fixes and the Overseer re-reviews, up to 3 attempts.

The PHASE_PROMPT is provided via $ARGUMENTS. It can be either:
- Inline prompt text
- A file path to a PHASE_PROMPT.md

## Step 1: Create task list

Create tasks for the phase loop:

1. "Validate PHASE_PROMPT" — Validating PHASE_PROMPT
2. "Plan phase with Scribe" — Planning phase with Scribe
3. "Build phase with Builder" — Building phase with Builder
4. "Review phase with Overseer" — Reviewing phase with Overseer
5. "Report result" — Reporting result

## Step 2: Validate PHASE_PROMPT

Mark task 1 as in_progress.

If $ARGUMENTS looks like a file path (ends in `.md` or contains `/`), read the file.
Otherwise, treat $ARGUMENTS as the prompt text directly.

Verify the prompt is non-empty and contains meaningful content.

If invalid, mark task 1 as completed, report the error, and stop.

Mark task 1 as completed.

## Step 3: Plan phase with Scribe

Mark task 2 as in_progress.

Use the Task tool to invoke `@ushabti:scribe` with the following prompt:

> Plan a phase from the following PHASE_PROMPT. Follow your standard procedure — read laws, style, docs, and existing phases, then create the phase directory with phase.md, steps.md, and progress.yaml.
>
> PHASE_PROMPT:
> {the prompt content from Step 2}

Wait for the Scribe to complete. Verify that the phase directory was created by invoking the `find-current-phase` skill. The newest phase with status `planned` is the one just created.

If the Scribe failed, report the error and stop.

Mark task 2 as completed.

## Step 4: Build phase with Builder

Mark task 3 as in_progress.

Use the Task tool to invoke `@ushabti:builder` with the following prompt:

> Implement the current phase. Follow your standard procedure — read laws, style, docs, find the current phase, and implement all steps. Update progress.yaml as you go. When all steps are complete, set the phase status to `review`.

Wait for the Builder to complete. Verify the phase status is now `review` by invoking the `get-phase-status` skill.

If the Builder failed, report the error and stop.

Mark task 3 as completed.

## Step 5: Review phase with Overseer

Mark task 4 as in_progress.

Set a retry counter to 0.

Use the Task tool to invoke `@ushabti:overseer` with the following prompt:

> Review the current phase. Follow your standard procedure — read laws, style, the phase files, and the code changes. Verify acceptance criteria are met. Either declare the phase green (status: complete) or kick it back (status: building) with specific feedback.

Wait for the Overseer to complete.

Check the phase status by invoking the `get-phase-status` skill:

**If status is `complete`**: The phase is green. Mark task 4 as completed. Proceed to Step 6.

**If status is `building`** (kicked back): Increment retry counter.

- If retry counter < 3:
  - Read the review file (`.ushabti/phases/{phase}/review.md`) to understand what the Overseer found.
  - Use the Task tool to invoke `@ushabti:builder` with the following prompt:
    > The Overseer reviewed the current phase and kicked it back. Read the review at `.ushabti/phases/{phase}/review.md` for details. Fix the issues identified, then set the phase status back to `review`.
  - When the Builder completes, invoke `@ushabti:overseer` again with the same prompt as above.
  - Repeat this check.

- If retry counter >= 3:
  - The phase is blocked. Mark task 4 as completed. Proceed to Step 6 with outcome "blocked".

## Step 6: Report result

Mark task 5 as in_progress.

Report the outcome:

**If green:**
> Phase loop complete. The phase has been planned, built, and reviewed successfully.
> - Phase: {phase directory name}
> - Status: GREEN
> - Review cycles: {retry counter + 1}

**If blocked:**
> Phase loop blocked after 3 review cycles. Manual intervention required.
> - Phase: {phase directory name}
> - Status: BLOCKED
> - Last review: see `.ushabti/phases/{phase}/review.md`

Mark task 5 as completed.
