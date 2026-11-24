---
name: approved-change-execution
description: Use after real human action approval or a verified applicable human-approved area mandate to execute a bounded live change with preflight, preview, abort rules, readback, and rollback.
---

# Approved change execution

## Trigger

- Use only with real human approval. For an existing human-approved area
  mandate, verify that it covers the exact target, concrete effects and
  recovery path. It can then satisfy the approval requirement for this action.
- Use when planning is complete and the next step is controlled execution.
- Use for narrow live actions against exact approved targets, not broad maintenance.

## Inputs

- Human approval reference.
- Exact action, target, and scope boundary.
- Preflight assumptions and success criteria.
- Dry-run, check-mode, or diff-mode path if the tool supports it.
- Abort criteria, post-change readback, and reviewed rollback procedure.

## Workflow

1. Confirm the approved action, exact targets, and explicit non-goals.
2. Run preflight checks and compare them to the approved assumptions.
3. Use dry-run, check mode, diff mode, or equivalent preview when supported.
4. Limit execution to exact hosts, services, objects, or inventories. Use explicit limits, tags, selectors, or single-target addressing.
5. Stop the dependent application immediately if preflight or preview differs
   from what was approved. Continue authorized diagnosis, correction and
   applicable revalidation before reconsidering the blocked application.
6. Execute the minimum approved live action.
7. Perform independent post-change readback against the intended state.
8. If readback fails or signals are ambiguous, stop further application and
   apply the reviewed, authorized rollback when needed. Recheck it and diagnose
   the failure. Raise an uncovered recovery action or decision to the human.
9. Record what was executed, what was verified, and what remains unverified.

## Stop / Approval Rules

- Never treat a template, task note, or assistant summary as approval. Approval must come from a real human decision.
- Never treat a Git lifecycle approval as authorization for a live,
  production, Homelab, credential, permission, repository-setting, release,
  tag, workflow-dispatch, or destructive-data action. Verify human approval
  that independently covers the exact effects.
- Never widen scope from one target to many because the first step looked safe.
- Keep dependent application blocked after a failed preflight or preview,
  ambiguous validation or an unexpected side effect. Other authorized work
  can continue, including diagnosis, correction and reviewed recovery.
- Keep native denials and uncovered effects blocked. Changing tool, model,
  account or thread cannot lift a native denial.
- Never run live changes without a rollback path that matches the approved scope.
- Perform credential, permission, network-boundary or secret changes only
  when the human approval explicitly covers the concrete effect on the
  specific target. Preserve applicable native and service permissions.

## Checks

- The current human approval covers the target, concrete effects and recovery
  path. Record its source, exclusions and reserved decisions when relevant.
- Targets are exact, not inferred.
- Preflight and preview matched the approved assumptions.
- Post-change readback independently confirms the intended result.
- Rollback is ready before execution starts.

## Output

```text
## Approved action
...

## Targets and limits
- ...

## Preflight / preview
- ...

## Execution result
- ...

## Readback
- ...

## Rollback status
- ...
```
