# Consumer-owned Codex compatibility

Status: consumer-owned
Managed-by-source: no

## Native integrations and preserved safeguards

Installed and connected integrations use native Codex permissions without a
mandatory `.agent-state/tool-inventory.json` in every chat or worktree. An
explicit project inventory remains an additional restriction: malformed files,
symlinks, disabled integrations and unlisted tools fail closed. This adapter
never grants native approval. Unknown MCP mutations still pass through the
existing overlay, run-contract and action-envelope guards.

The existing Git adapter accepts quoted search expressions, simple sequences
of independently read-only commands and `git check-ignore`. Unknown programs,
shell expansion, unquoted parentheses (including process substitution),
pipelines, redirections and write-capable command options
remain unclassified. File compilation also stays blocked when short options
are combined; `find -fprintf` and `-fls` cannot pass as reads. Branch listing
checks every option so mixed deletion, rename or copy flags remain mutations.
Protected-branch, detached-HEAD, force-push and direct-main
push restrictions remain active. Existing hook registrations are preserved.

Automatically generated historical inventories are retired only by separate
host maintenance after exact provenance and hash checks. This repository does
not create inventories, provision worktrees or embed host-specific exceptions.

## Historical ownership migration

This section records the earlier migration only. Its 58-file count and hashes
are historical, not current state. The adoption below supersedes that state;
the orchestration policy now follows variant 2. of 2026-09-16

The definitions source excluded the former runtime and its templates. Their
removal would lose repository safeguards. The following
25 existing paths therefore remain in the repository under consumer ownership;
they are no longer deletion candidates in the central ownership map. Only the
two compatibility adapters changed content. At that migration, the 58 remaining
centrally managed entries retained their prior metadata exactly. No file was removed.

Definition boundary: [04-llm-essentials at c616083](https://github.com/k1ll4p1x3l/04-llm-essentials/blob/c616083aa52a9a98cb861f8b911230f9897b1826/distribution/README.md).
Baseline before this compatibility migration: `e864b5dd65b4a1bfcff58c95ec833c695bf6cc6e`.
Hashes below describe the retained files after this migration, not a complete
release or installation attestation.

| Consumer-owned path | SHA-256 | Git mode |
|---|---|---|
| `.agent-core/templates/ACTION_ENVELOPE.json` | `ec54c0db3853ffb05a4ceb7446e3ac95750085ce3a55bff5311b7c38f1de51f5` | `100644` |
| `.agent-core/templates/CHECKPOINT.json` | `43b2b396d096345975c406c74f14ab2a699e6d1bfe10e180155c8480070af8e0` | `100644` |
| `.agent-core/templates/DELEGATION_LEDGER.json` | `448511283bb167a8978cbc6fd540a7de717f1bc78440e5e7ac6d66358bb2aef9` | `100644` |
| `.agent-core/templates/EVIDENCE.json` | `90ad8cb899fa7e130c2419c1697bcb4724076ff8f33d4b7238336ac66ef03fc1` | `100644` |
| `.agent-core/templates/GIT_LIFECYCLE_APPROVAL_ENVELOPE.json` | `f9b52fcaeb2e71b425158ab63341fd78517a4c340f9a18178ae0aa29d2b1b22f` | `100644` |
| `.agent-core/templates/REPOSITORY_AGENT_OVERLAY.md` | `5990cfce40620eb9fc8f4441b3ffccf65531ee49409449b135725b5ce1ec074a` | `100644` |
| `.agent-core/templates/REPOSITORY_AGENT_OVERLAY.schema.json` | `f9b529409be26ae671aa8866f43c0311c7e7a51a9d32d24cc5e6a9a978d231ed` | `100644` |
| `.agent-core/templates/REPOSITORY_AGENT_OVERLAY_MANIFEST.json` | `6ff62c39677c7b54735700fbfafbd14587d89a1c0f9380135a0175344ac159e8` | `100644` |
| `.agent-core/templates/RUN_CONTRACT.json` | `7e9fcf29c5d96a2f20fdba55dfa4bad460002a8765ea8319e633937f08d148af` | `100644` |
| `.agent-core/templates/SCOPE_ASSUMPTION_LEDGER.json` | `00fd7a47c725b0ef36aefe8069137b7ee70db42a857be05e05337606e1ce3fe5` | `100644` |
| `.agent-core/templates/TASK_LOG.md` | `14074779df5226438ffa887b04d3974a050b6e5907405e73d1d84ddcde3d75d7` | `100644` |
| `.agent-core/templates/TOOL_INTEGRATION_INVENTORY.json` | `bc1b6220edcf1ce5ebb95b1d65774b281b7b6a35b55ca58b74541cf531c2c5eb` | `100644` |
| `.codex/hooks.json` | `75f7df4bae4c8eb3440570d42cf673f1e870311cec1df020a16fc5c577e02fec` | `100644` |
| `.codex/hooks/git_guard.py` | `87f9aed200854911dfaac158f501c2d45bda076e2253f94e69d930c8658f0d1a` | `100644` |
| `.codex/hooks/policy_guard.py` | `b8c0737449a102f2796408be5014d19657d8f128556afd386b8dca4b36d417e6` | `100644` |
| `.codex/hooks/repository_context.py` | `cf8f1a9b5f8a84df54d8ef351ecddfb48d1f31cb94b6f23cd3599bcb2e813492` | `100644` |
| `.codex/hooks/repository_overlay.py` | `a4b3eb910e0a29d3306937d6104a37cf1f58b750af8cc4dca1ac20d96824936e` | `100644` |
| `.codex/hooks/run_guard.py` | `c0199a4c3b23a41d95d5004c4c0750fa5e9f1f03fd60b27b9170fe8115741c3a` | `100644` |
| `.codex/hooks/worktree_guard.py` | `2cc1087b91af741c15692cecc23f8ee5f5e0d16df392f2d8c20fd0d5b0fdd8d2` | `100644` |
| `.codex/policies/capability_profiles.json` | `c1f26c8271f4db6d42c924299a2509808cd99bc922542c4185c539d250813ec3` | `100644` |
| `.codex/policies/git_lifecycle.json` | `45c9593a49d143789c3fc93239206865da5659bf8bc76aa0b80dba8529495a31` | `100644` |
| `.codex/policies/integration_registry.schema.json` | `84915889261809eadb95b9d76462f53f6ff9dddebf862101b60d0fef96a7248b` | `100644` |
| `.codex/policies/orchestration_limits.json` | `ddfc5632cfcf8389f27cf529e06b6bca12a412fbb713303434d8932129595850` | `100644` |
| `.codex/policies/tool_zones.json` | `64cd0bdd370430a0f940d1f9aa82ffe5373226a2cf523b0543813cb96cc8d3a4` | `100644` |
| `.codex/policies/trust_boundaries.json` | `371f8017c74c51af63cc4346bc701d45f24f3a9f6fedaa92608ff40fd448c358` | `100644` |

## Current definition adoption — variant 2 (2026-09-23)

The user explicitly selected variant 2 for all eight consumers. The earlier
adoption used [04-llm-essentials at 927131f](https://github.com/k1ll4p1x3l/04-llm-essentials/tree/927131f2c6d0e32072942073dc5d315a1e2c0e85).
The current definitions are pinned to
[04-llm-essentials at 937e047](https://github.com/k1ll4p1x3l/04-llm-essentials/tree/937e047057217a1dc9a7bf18304a3df35562f54b).
The public profile contains 297 managed files. Current contents, hashes and
modes are recorded in `.agent-core.lock.json`; the source adds GPT-6 Sol and
Luna options and removes Spark entries without changing the 28 base roles.
No model availability or live behavior is claimed.

All 28 base roles explicitly pin model and effort. The native project ceiling
is `max_concurrent_threads_per_session = 8`; the consumer-owned
`.codex/policies/orchestration_limits.json` also sets
`max_parallel_subagents = 8`. The former inheritance/four-agent configuration
is superseded. Role alternatives remain available; the parent has no global
model pin. Eight is a ceiling, not a capacity promise or delegation target.
Narrower platform limits and task budgets remain binding.

URI schemes, control characters and surrounding whitespace are also rejected.
The learning selector rejects absolute, drive-qualified, UNC and traversal
references under POSIX and Windows semantics, independently of the host.
Retained hooks, templates, permission adapters and overlays remain consumer-owned.
Their safeguards are preserved; only the explicit concurrency policy value changes.
File adoption does not prove live agent or integration behavior.

The reviewed selector also rejects SCP/colon references and Unicode control/format characters, uses ASCII-safe JSON, rejects over-nested input generically, and detects known GitHub PAT/AWS key markers. Detection is heuristic; content review remains required.

The current official [schema](https://learn.chatgpt.com/docs/config-schema.json) and [reference](https://learn.chatgpt.com/docs/config-file/config-reference), checked 2026-09-17, define the scalar settings under `agents`. Old 0.137/0.144 parser examples are historical and incompatible; use a current compatible CLI. No tested minimum version or live agent execution is claimed.

## Future definition updates

Compare updates with the adopted source and the current ownership lock.
Do not restore the superseded inheritance/four-agent baseline. Keep retained
hooks and templates consumer-owned; do not re-adopt or remove them because they
are absent from the central source. Review subsequent model or limit changes.

## Validation and rollback

Maintenance tests exercise the real adapters with isolated synthetic fixtures:
missing/explicit/disabled/malformed inventories, invalid overlays and run
contracts, missing envelopes, read-only shell classification and Git mutation
denials. Native approval and actual integration calls require a separate live
Codex readback; adapter tests alone do not prove them. Test fixtures and host
maintenance tooling are not distributed by this repository.

Rollback of this definition adoption requires reviewed reverts of the relevant
consumer PRs, preserving the earlier compatibility adapters and safeguards.
The historical ownership migration is a separate change; reverting it would
restore the old inventory requirement. Neither action deletes user sessions or
worktree data. Inheritance and limit 4 are historical rollback states, not an
alternative active configuration.
