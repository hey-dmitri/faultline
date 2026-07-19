#!/usr/bin/env python3
"""Build a deterministic Faultline skill archive."""

from __future__ import annotations

import stat
import sys
import zipfile
from pathlib import Path


FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: package_skill.py REPO_DIR OUTPUT", file=sys.stderr)
        return 2

    repo_dir = Path(sys.argv[1]).resolve()
    source = repo_dir / "SKILL.md"
    output = Path(sys.argv[2]).resolve()

    if not source.is_file():
        print(f"missing {source}", file=sys.stderr)
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    info = zipfile.ZipInfo("faultline/SKILL.md", FIXED_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | 0o644) << 16

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(info, source.read_bytes())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
