# Native extensions and action approvals

As of 2026-09-16. This is a limited English translation of material from
[08-llm-essentials, c616083aa52a9a98cb861f8b911230f9897b1826](https://github.com/k1ll4p1x3l/08-llm-essentials/blob/c616083aa52a9a98cb861f8b911230f9897b1826/templates/consumer/.agent-core/CONFIGURATION.md).

The following two sections and the preceding paragraph on precedence are
translated from the pinned source. Statements about the supplied project
baseline describe the current source definitions. This limited documentation
update installs no configuration, agent roles, or hooks. Check the consumer's
actual defaults separately. This is a translation, not a byte-identical export.

According to the [configuration documentation](https://learn.chatgpt.com/docs/config-file/config-basic),
CLI overrides take precedence over trusted project configuration, followed by
the selected user profile, user configuration, cloud/system defaults, and
built-ins. Native enforced policies are separate and remain effective.
A skill cannot correct a desktop model picker.

## User-wide extensions and action approvals

Already installed, connected, and supported plugins, apps, and skills are
managed through native user settings. These definitions require no additional
tool inventory or copied plugin registration for each new chat or worktree.
SSH, terminal, and app-server entry points should use the same `CODEX_HOME`
for the same user. Project rules and the configuration precedence described
above remain effective.

Installation and a visible tool catalog do not authorize actions. The supplied
project baseline retains `workspace-write`, `on-request`, reviewer `user`, and
app approval mode `writes`; destructive and open-world tools are initially
disabled. An explicitly approved host standard belongs in user configuration.
It must not silently become the general consumer default. The responsible
environment must check effective configuration to determine whether project
or tool rules override that standard.

The [native configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
distinguishes app activation, tool permission, and reviewer selection.
`destructive_enabled` and `open_world_enabled` can be enabled specifically for
explicitly approved apps. Retain reviewer `user` for required human action
approvals, and check app and tool overrides as well.

[MCP policies](https://learn.chatgpt.com/docs/extend/mcp) belong under
`mcp_servers.<server>` for custom servers and under
`plugins.<plugin>.mcp_servers.<server>` for plugin servers. Do not register
plugin transports twice. `default_tools_approval_mode = "writes"` prompts for
tools that are not marked read-only. Set `prompt` explicitly for unclear
classifications or especially sensitive actions. Preserve existing native
tool lists and project restrictions. Replace earlier supplementary inventories
only after mapping their rules; do not silently discard unclear restrictions.

When migrating, the responsible operating environment checks actual read
calls, rejection, and the absence of an approval channel using a harmless
write test. This also applies to direct calls and Code Mode, where used.
Source validation itself does not run an agent probe.
[Hooks](https://learn.chatgpt.com/docs/hooks) do not replace native approvals:
the current documentation does not support `PreToolUse` with
`permissionDecision = "ask"`; a hook error does not reliably stop the tool call.

## Headless operation and availability limits

For a headless host without a usable keyring,
`mcp_oauth_credentials_store = "file"` is an explicitly supported user option
([reference](https://learn.chatgpt.com/docs/config-file/config-reference)).
Restrict access to the credential store to the operating user. Credentials,
OAuth state, plugin installation, and caches do not belong in consumer file
synchronization; the operating environment manages them separately.

Start a new CLI session after [plugin installation](https://learn.chatgpt.com/docs/plugins).
An external connection may also be required. The IDE extension currently does
not support plugins; Codex CLI in an IDE terminal is a separate interface.
Platform-specific plugins and desktop functions are not guaranteed on Linux.
A revoked connection can require signing in again.

Identify the actual state: available, intentionally restricted, connection
required, unsupported on this platform, or provider failure. A loaded catalog
or successful diagnostic check alone proves neither usability nor effective
action approvals.
