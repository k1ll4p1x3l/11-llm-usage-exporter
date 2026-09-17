#!/usr/bin/env python3
"""Read one explicitly chosen small lesson file; never execute or write lessons."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import stat
import sys

FIELDS = {"id", "title", "component", "versions", "environment", "triggers", "observed_problem",
          "verified_solution", "next_action", "source_refs", "status"}
STATES = {"observed", "verified", "adopted", "obsolete", "refuted"}
MARKERS = re.compile(r"(?i)(?:/users/|/home/|[a-z]:\\users\\|authorization\s*:|"
                     r"bearer\s+|cookie\s*:|-----BEGIN .*PRIVATE KEY|(?:sk-|ghp_)[A-Za-z0-9_-]{12,})")


def read_lessons(path: Path) -> list[dict]:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate lesson key")
            result[key] = value
        return result

    def reject_constant(unused):
        raise ValueError("non-finite JSON is not lesson data")

    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    with os.fdopen(os.open(path, flags), "rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise ValueError("lesson input must be a regular file")
        raw = stream.read(65537)
    if len(raw) > 65536:
        raise ValueError("lesson file exceeds 64 KiB")
    value = json.loads(raw, object_pairs_hook=pairs, parse_constant=reject_constant)
    if (not isinstance(value, dict) or set(value) != {"schema_version", "lessons"}
            or type(value["schema_version"]) is not int or value["schema_version"] != 1
            or not isinstance(value["lessons"], list) or len(value["lessons"]) > 32):
        raise ValueError("invalid bounded lesson document")
    ids = set()
    for entry in value["lessons"]:
        if not isinstance(entry, dict) or set(entry) != FIELDS:
            raise ValueError("lesson fields mismatch")
        for key in FIELDS - {"versions", "triggers", "source_refs"}:
            if not isinstance(entry[key], str) or not entry[key].strip() or len(entry[key]) > 1500:
                raise ValueError("invalid lesson text")
        for key in ("versions", "triggers", "source_refs"):
            values = entry[key]
            if (not isinstance(values, list) or not 1 <= len(values) <= 16
                    or any(not isinstance(item, str) or not item.strip() or len(item) > 200 for item in values)
                    or len(values) != len(set(values))):
                raise ValueError("invalid lesson selectors/references")
        if entry["id"] in ids or entry["status"] not in STATES:
            raise ValueError("duplicate ID or invalid lesson status")
        ids.add(entry["id"])
        if any(path.anchor or ".." in path.parts
               for ref in entry["source_refs"]
               for path in (PurePosixPath(ref), PureWindowsPath(ref))):
            raise ValueError("lesson references must be repository-relative")
        if any(MARKERS.search(text) for text in _texts(entry)):
            raise ValueError("lesson contains a forbidden sensitive marker; no values printed")
    return value["lessons"]


def _texts(entry: dict) -> list[str]:
    return [text for value in entry.values() for text in (value if isinstance(value, list) else [value])]


def select(lessons: list[dict], component: str, version: str, trigger: str) -> list[dict]:
    return [entry for entry in lessons if entry["status"] == "adopted" and entry["component"] == component
            and version in entry["versions"] and trigger in entry["triggers"]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    for name in ("component", "version", "trigger"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    try:
        result = select(read_lessons(args.file), args.component, args.version, args.trigger)
    except (ValueError, OSError, UnicodeError):
        print("Invalid lesson file; no lesson contents emitted.", file=sys.stderr)
        return 2
    print(json.dumps({"selected": result, "authority": "none"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
