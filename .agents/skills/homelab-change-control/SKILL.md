---
name: homelab-change-control
description: Use for infrastructure, homelab, and operations work that must separate diagnosis, planning, offline patching, and approved live execution.
---

# Homelab change control

## Trigger

- Use for Docker, Compose, DNS, reverse proxy, VPN, firewall, IAM, backup, storage, monitoring, or host-level operations work.
- Use when a wrong change could cause outage, lockout, or data loss.

## Inputs

- Current topology, affected hosts/services, and available evidence.
- Risk class of the proposed work.
- Backup, rollback, and validation expectations.

## Workflow

1. Start with inventory and evidence, not mutation.
2. Classify the actual consequences. Check the affected data and dependent
   services, access paths, tolerable downtime and recoverability. Size the
   technical controls to these findings. For example, assess whether a DNS
   change affects a disposable test host or a shared resolver.
3. Route incident work through `incident-response` when live impact, evidence capture, or containment are central.
4. Route backup and recovery readiness through `backup-restore-validation` when restore-tested evidence is needed.
5. Route monitoring, alerts, and operator guidance through `observability-and-runbooks`.
6. For critical change work, require a plan before any patching.
7. Prepare validation and a recovery path the executor can actually reach.
   If the change affects its only access route, verify independent access
   before applying it, or identify the specific assistance required.
8. Use `approved-change-execution` for live actions. Verify that a human
   decision covers the exact target, effect and recovery path. An applicable
   human-approved area mandate can already cover all three. Identify the
   executor and retain required reviews, native approvals, preflight,
   preview, abort conditions and independent readback.
9. Keep secrets redacted and private topology out of public-safe outputs.

## Stop / Approval Rules

- No live changes without explicit user approval.
- Stop before restarts, deploys, firewall edits, DNS changes, storage actions, credential changes, or backup mutations unless already approved.
- Never treat a plan, patch, or template as human approval for live execution.
- Block the dependent action if recovery is missing, a check fails or
  evidence is insufficient. Continue authorized diagnosis, preparation
  and correction, then repeat the affected check. An uncovered effect or
  native denial remains blocked.

## Checks

- Risk class is explicit.
- Impact, rollback, and validation exist before execution.
- Live and offline steps are clearly separated.
- Incident, recovery, and observability work are routed to the dedicated contracts when relevant.

## Output

```text
## Impact
...

## Plan
...

## Rollback
...

## Validation
...

## Approval points
- ...

## Recommended follow-on skill
- incident-response / backup-restore-validation / observability-and-runbooks / approved-change-execution
```
