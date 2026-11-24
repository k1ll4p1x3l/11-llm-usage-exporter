---
name: backup-restore-validation
description: Use for restore-tested backup and recovery planning with RPO, RTO, restore order, validation evidence, and last successful restore test tracking.
---

# Backup restore validation

## Trigger

- Use when reviewing backup health, designing recovery, or validating whether backups are actually restorable.
- Use when a service or dataset needs explicit recovery objectives and restore evidence.

## Inputs

- Services, datasets, and owners.
- Backup sources, destinations, and retention assumptions.
- Restore prerequisites and dependencies.
- Recovery objectives such as RPO and RTO.

## Workflow

1. Inventory what must be restorable: service, data, configuration, identity dependencies, and infrastructure dependencies.
2. Define RPO and RTO targets for each item.
3. Establish restore order and restore priority across dependencies.
4. Record the exact restore source, prerequisites, validation signal, and rollback or retry path.
5. Distinguish backup existence from restore-tested recovery.
6. Track the last successful restore test with date, scope, and evidence.
7. Highlight untested, partially tested, and stale recovery paths.

## Stop / Approval Rules

- Never treat "backup exists" as proof of recoverability.
- Never claim recovery readiness without at least one verifiable restore path.
- Never hide missing dependencies such as IAM, DNS, or keys behind a green backup label.
- Never overwrite primary data during validation unless explicitly approved and sandboxed.

## Recovery for a specific task

Before a consequential change, verify that the executor can reach and use
the needed recovery source, credentials and tooling. If the change can sever
network, DNS or identity access, verify an independent route. Prepare the
missing prerequisite within the current mandate. A tested rebuild can be
adequate for a resource explicitly designated disposable. Match backup and
restore-test depth to the data, downtime and actual change risk.

Keep regular retention and required recovery paths in place. For an additional
task backup, record its location, purpose, dependencies and removal condition
in the existing task state if it must outlive the change. When that purpose
ends, assess snapshot, clone and backup chains before removing the owned extra
copy within the existing mandate using the native procedure. Read back its
removal and, for substantial storage, check actual available capacity at the
affected store. Shared blocks and logical size do not measure reclaimed space.

## Checks

- RPO and RTO are explicit per critical item.
- Restore order reflects dependencies.
- Validation signal is independent of the backup job status.
- Last successful restore test is recorded or explicitly missing.

## Output

```text
## Recovery scope
...

## RPO / RTO
- ...

## Restore order
- ...

## Validation evidence
- ...

## Gaps
- ...
```
