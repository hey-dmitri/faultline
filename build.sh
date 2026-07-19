#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
output_path="${1:-$repo_dir/faultline.skill}"

python3 "$repo_dir/scripts/package_skill.py" "$repo_dir" "$output_path"

echo "Built $output_path"
