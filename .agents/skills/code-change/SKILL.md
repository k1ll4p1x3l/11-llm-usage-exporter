---
name: code-change
description: Use for bounded code or config changes that should stay minimal, reviewable, tested, and free of unauthorized side effects.
---

# Code change

## Trigger

- Use for bugfixes, small features, refactors, config changes, or tests in a known repository.
- Use when a task should end in a minimal diff plus validation.

## Inputs

- Goal, scope, and acceptance criteria.
- Relevant files, tests, and conventions.
- Allowed write surface and forbidden side effects.

## Workflow

1. Map the smallest relevant code path before editing and bind the change to a must-criterion or necessary prerequisite. Agree whether the requested endpoint is implementation, verification, integration or installation.
2. Change only what is required to meet the goal.
3. Preserve existing style, patterns, and ownership boundaries.
4. Update tests or docs when behavior or operator guidance changes.
5. Run the narrowest meaningful checks first, then broader checks if warranted. Existing suitable tests and known mappings may be reused; don't repeat full checks or reviews without a relevant change, failure or unresolved concern.
6. Summarize behavior changes, validation, and residual risks.

## Stop / Approval Rules

- Stop before new dependencies, schema/data migrations, auth changes, secret handling, or live deployments unless explicitly approved.
- Stop if the fix grows beyond the promised scope or crosses another owner's area.
- Do not "clean up" unrelated code opportunistically.
- Repair an ordinary in-scope defect autonomously under existing actual approval; do not treat it as a new authority boundary. Track its stable problem reference, cumulative attempts and expected learning within per-problem and total limits. A failed check remains negative until its relevant verification passes.
- Classify a known environment limit narrowly; it must not hide a new product defect. Record optional review ideas separately and finish once the must-criteria and requested handoff are satisfied.
- Reuse only relevant adopted lessons through `learning-reuse`; version drift requires validation. A larger prevention project remains a recommendation, not extra implementation scope.

## Checks

- Diff is minimal and attributable to the goal.
- Behavior change is explicit.
- Relevant tests, lint, or syntax checks ran or a concrete reason is given.
- Rollback path is obvious from the diff.

## Output

```text
## Goal
...

## Changed files
- ...

## Behavior changed
- ...

## Checks
- command: result

## Risks / follow-up
- ...
```
