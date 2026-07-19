#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
temp_dir="$(mktemp -d)"
trap 'rm -rf "$temp_dir"' EXIT

python3 "$repo_dir/scripts/package_skill.py" \
  "$repo_dir" \
  "$temp_dir/faultline.skill"

cmp "$repo_dir/faultline.skill" "$temp_dir/faultline.skill"
unzip -t "$repo_dir/faultline.skill"

echo "Package matches SKILL.md."
