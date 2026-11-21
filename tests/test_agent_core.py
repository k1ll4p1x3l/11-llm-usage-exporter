from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).resolve().parents[1] / "scripts/verify_agent_core.py"


class AgentCoreLockTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.managed: dict[str, dict[str, str]] = {}
        self.add_file("AGENTS.md", b"public agent rules\n", "0644")
        self.add_file(".agents/skills/example/check.py", b"# example check\n", "0755")
        self.payload = {
            "format": "essentials-files-v1", "profile": "public",
            "managed_files": self.managed,
        }

    def add_file(self, relative: str, data: bytes, mode: str = "0644") -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        path.chmod(int(mode, 8))
        self.managed[relative] = {"mode": mode, "sha256": hashlib.sha256(data).hexdigest()}

    def run_check(self, *, raw_lock: str | None = None) -> subprocess.CompletedProcess[str]:
        (self.root / ".agent-core.lock.json").write_text(
            raw_lock if raw_lock is not None else json.dumps(self.payload), encoding="utf-8"
        )
        return subprocess.run(
            [sys.executable, str(CHECKER), "--root", str(self.root)],
            capture_output=True, text=True, check=False, timeout=10,
        )

    def test_current_public_lock_and_unmanaged_file_pass(self) -> None:
        (self.root / "README.md").write_text("consumer-owned content\n")
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("2 managed hashes and modes verified", result.stdout)

    def test_changed_and_missing_managed_file_fail(self) -> None:
        path = self.root / "AGENTS.md"
        path.write_text("changed rules\n")
        self.assertNotEqual(self.run_check().returncode, 0)
        path.unlink()
        self.assertNotEqual(self.run_check().returncode, 0)

    def test_required_agents_entry_cannot_be_omitted(self) -> None:
        del self.managed["AGENTS.md"]
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires AGENTS.md", result.stderr)

    def test_undeclared_private_area_fails_closed(self) -> None:
        for directory in ("private", "Private"):
            with self.subTest(directory=directory):
                private = self.root / ".agent-core" / directory / "README.md"
                private.parent.mkdir(parents=True)
                private.write_text("not part of the public profile\n")
                result = self.run_check()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("private Agent Core content", result.stderr)
                private.unlink()
                private.parent.rmdir()

    @unittest.skipIf(os.name == "nt", "executable mode changes require POSIX")
    def test_git_executable_mode_change_fails(self) -> None:
        (self.root / "AGENTS.md").chmod(0o755)
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mode mismatch", result.stderr)

    def test_unknown_format_private_profile_and_empty_map_fail(self) -> None:
        for field, value in (("format", "unknown-v2"), ("profile", "private"), ("managed_files", {})):
            with self.subTest(field=field):
                original = self.payload[field]
                self.payload[field] = value
                self.assertNotEqual(self.run_check().returncode, 0)
                self.payload[field] = original

    def test_unmanaged_private_and_escaping_lock_entries_fail(self) -> None:
        for relative in ("README.md", ".agent-core/private/README.md", "../outside", ".codex/agents/../config.toml"):
            with self.subTest(relative=relative):
                self.managed[relative] = dict(self.managed["AGENTS.md"])
                self.assertNotEqual(self.run_check().returncode, 0)
                del self.managed[relative]

    def test_invalid_hash_and_mode_records_fail(self) -> None:
        for field, value in (("sha256", "not-a-hash"), ("mode", "0777"), ("mode", 644)):
            with self.subTest(field=field, value=value):
                original = self.managed["AGENTS.md"][field]
                self.managed["AGENTS.md"][field] = value
                self.assertNotEqual(self.run_check().returncode, 0)
                self.managed["AGENTS.md"][field] = original

    def test_duplicate_keys_and_case_collisions_fail(self) -> None:
        raw = json.dumps(self.payload).replace('"format":', '"format": "essentials-files-v1", "format":', 1)
        self.assertNotEqual(self.run_check(raw_lock=raw).returncode, 0)
        self.add_file(".codex/agents/Sample.toml", b"role\n")
        self.add_file(".codex/agents/sample.toml", b"role\n")
        self.assertNotEqual(self.run_check().returncode, 0)

    @unittest.skipIf(os.name == "nt", "symlink creation requires platform privileges")
    def test_symlinked_managed_file_fails(self) -> None:
        path = self.root / "AGENTS.md"
        path.rename(self.root / "unmanaged-target.md")
        path.symlink_to("unmanaged-target.md")
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symbolic link", result.stderr)


if __name__ == "__main__":
    unittest.main()
