#!/usr/bin/env python3
"""Verify the current public Agent Core ownership lock and every declared file."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import sys
from pathlib import Path, PurePosixPath

from public_repo_sanity_check import canonical_root, stable_read


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
LOCK_NAME = ".agent-core.lock.json"
PUBLIC_FILES = {
    "AGENTS.md", ".codex/config.toml", ".agent-core/LICENSE",
    ".agent-core/CONFIGURATION.md", ".agent-core/ROLES.md",
    ".agent-core/VARIANTS.md",
}
PUBLIC_PREFIXES = (
    ".agents/skills/", ".codex/agents/", ".agent-core/templates/",
    ".agent-core/profiles/",
)
MAX_FILE_SIZE = 2 * 1024 * 1024
MAX_MANAGED_FILES = 2000


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key in Agent Core lock")
        result[key] = value
    return result


def regular_file(root: Path, relative: str) -> tuple[Path, object]:
    path = root / relative
    for candidate in (path, *path.parents):
        if candidate == root:
            break
        if candidate.is_symlink():
            raise ValueError(f"symbolic link in managed path: {relative}")
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_FILE_SIZE:
        raise ValueError(f"managed path is not a bounded regular file: {relative}")
    return path, info


def verify(root: Path) -> int:
    core_path = root / ".agent-core"
    if core_path.is_symlink():
        raise ValueError("symbolic link in Agent Core directory")
    if core_path.is_dir() and any(path.name.casefold() == "private" for path in core_path.iterdir()):
        raise ValueError("private Agent Core content is forbidden in the public profile")
    lock_path, lock_info = regular_file(root, LOCK_NAME)
    payload = json.loads(
        stable_read(lock_path, lock_info, LOCK_NAME), object_pairs_hook=unique_object
    )
    if not isinstance(payload, dict) or set(payload) != {"format", "profile", "managed_files"}:
        raise ValueError("unsupported Agent Core lock shape")
    if payload["format"] != "essentials-files-v1":
        raise ValueError("unsupported Agent Core lock format")
    if payload["profile"] != "public":
        raise ValueError("public repository requires the public Agent Core profile")
    managed = payload["managed_files"]
    if not isinstance(managed, dict) or not 1 <= len(managed) <= MAX_MANAGED_FILES:
        raise ValueError("invalid Agent Core ownership map")
    if "AGENTS.md" not in managed:
        raise ValueError("public Agent Core lock requires AGENTS.md")
    folded: set[str] = set()
    for relative, recorded in managed.items():
        parsed = PurePosixPath(relative)
        if (not re.fullmatch(r"[A-Za-z0-9_./-]+", relative)
                or parsed.is_absolute() or relative != parsed.as_posix()
                or any(part in {"..", ".git"} for part in parsed.parts)
                or not (relative in PUBLIC_FILES or relative.startswith(PUBLIC_PREFIXES))):
            raise ValueError("unsafe or non-public managed path")
        if relative.casefold() in folded:
            raise ValueError("case-colliding managed paths")
        folded.add(relative.casefold())
        if (not isinstance(recorded, dict) or set(recorded) != {"sha256", "mode"}
                or recorded["mode"] not in {"0644", "0755"}
                or not isinstance(recorded["sha256"], str)
                or not re.fullmatch(r"[0-9a-f]{64}", recorded["sha256"])):
            raise ValueError(f"invalid ownership metadata: {relative}")
        path, info = regular_file(root, relative)
        actual_mode = "0755" if info.st_mode & 0o111 else "0644"
        if actual_mode != recorded["mode"]:
            raise ValueError(f"managed file mode mismatch: {relative}")
        if hashlib.sha256(stable_read(path, info, relative)).hexdigest() != recorded["sha256"]:
            raise ValueError(f"managed file hash mismatch: {relative}")
    return len(managed)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    args = parser.parse_args()
    try:
        count = verify(canonical_root(args.root))
    except (OSError, ValueError, TypeError) as exc:
        print(f"Agent Core verification failed closed: {exc}", file=sys.stderr)
        return 1
    print(f"Agent Core essentials-files-v1 (public): {count} managed hashes and modes verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
