#!/bin/bash
# Publish a GitHub release with the signed shortcuts and the data files.
#
# Usage: scripts/release.sh v1.0.0 [--draft]
#
# The script checks everything first, then tags, then uploads.
# GitHub deletes every non ASCII character from an asset name, and turns a
# space into a period. So each single file uses the plain name from
# shortcuts/manifest.json. Each ZIP keeps the real file names.
set -eu

root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"

version="${1:-}"
draft="${2:-}"

if ! printf '%s' "$version" | grep -Eq '^v[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "usage: scripts/release.sh v<major>.<minor>.<patch> [--draft]" >&2
  exit 1
fi

fail() {
  echo "  FAIL $1" >&2
  exit 1
}

echo "==> Checking the repository"

command -v gh >/dev/null || fail "the gh command is not installed"
command -v zip >/dev/null || fail "the zip command is not installed"
gh auth status >/dev/null 2>&1 || fail "gh is not logged in"

branch="$(git rev-parse --abbrev-ref HEAD)"
[ "$branch" = "main" ] || fail "you are on branch $branch, not main"

[ -z "$(git status --porcelain)" ] || fail "the working tree is not clean"

if git rev-parse -q --verify "refs/tags/$version" >/dev/null; then
  fail "tag $version already exists"
fi

git fetch --quiet origin "$branch"
[ "$(git rev-parse HEAD)" = "$(git rev-parse "origin/$branch")" ] ||
  fail "HEAD and origin/$branch differ. Push first."

[ -f shortcuts/manifest.json ] || fail "shortcuts/manifest.json is missing. Run make shortcuts."

echo "==> Checking that every shortcut is signed and current"

for src in shortcuts/*/unsigned/*.shortcut; do
  relative="${src#shortcuts/}"
  language="${relative%%/*}"
  signed="shortcuts/$language/$(basename "$src")"
  [ -f "$signed" ] || fail "$signed is missing. Run scripts/sign_all.sh."
  [ "$signed" -nt "$src" ] || fail "$signed is older than its source. Run scripts/sign_all.sh."
  head -c 4 "$signed" | grep -q 'AEA1' || fail "$signed is not a signed shortcut"
done

echo "==> Verifying the shortcut logic"

python3 scripts/verify_shortcut.py | tail -1 | grep -q '^ALL OK$' ||
  fail "scripts/verify_shortcut.py did not print ALL OK"

echo "==> Building the assets"

stage="$(mktemp -d -t shortcutrelease)"
trap 'rm -rf "$stage"' EXIT

assets=()

# One line per build: signed file, then the plain asset name.
while IFS=$'\t' read -r file asset; do
  [ -f "$file" ] || fail "$file is in the manifest but not on disk"
  cp "$file" "$stage/$asset"
  assets+=("$stage/$asset")
done < <(python3 -c '
import json
for row in json.load(open("shortcuts/manifest.json", encoding="utf-8")):
    print(row["file"], row["asset"], sep="\t")
')

for language_dir in shortcuts/*/; do
  language="$(basename "$language_dir")"
  bundle="$stage/shortcuts-$language-$version.zip"
  # -j drops the folder path, so the ZIP holds the files with their real names.
  (cd "$language_dir" && zip -q -j "$bundle" ./*.shortcut)
  assets+=("$bundle")
done

cp data/settings-urls.json "$stage/settings-urls.json"
cp docs/settings-urls.md "$stage/settings-urls.md"
assets+=("$stage/settings-urls.json" "$stage/settings-urls.md")

echo "==> Writing the release notes"

notes="$stage/notes.md"
python3 - "$notes" "$version" <<'PYTHON'
import json
import sys

notes_path, version = sys.argv[1], sys.argv[2]
rows = json.load(open("data/settings-urls.json", encoding="utf-8"))
builds = json.load(open("shortcuts/manifest.json", encoding="utf-8"))

families = {}
for row in rows:
    families[row["family"]] = families.get(row["family"], 0) + 1
verified = sum(1 for row in rows if row["versions"])
chinese = sum(1 for row in rows if row["label_zh"])
sources = len({source for row in rows for source in row["sources"]})

USE = {
    "phone": "Daily use on iPhone and iPad.",
    "phone_all": "Adds pages with no name, and old pages.",
    "watch": "Apple Watch pages, opened from the Watch app.",
}
LANGUAGE_NAME = {"en": "English", "zh-TW": "Traditional Chinese"}

table = ["| Download | Language | Entries | Use it for |", "| --- | --- | ---: | --- |"]
for build in builds:
    table.append(
        f"| `{build['asset']}` | {LANGUAGE_NAME.get(build['language'], build['language'])} "
        f"| {build['entries']} | {USE.get(build['key'], '')} |"
    )

text = f"""## Install

Download one `.shortcut` file, AirDrop it to your iPhone, then tap "Add Shortcut".
On a Mac you can open the file directly, and iCloud syncs the shortcut to your iPhone.

{chr(10).join(table)}

The Traditional Chinese build shows the official Apple Chinese name and the English
name on every row, so you can search in either language.

A release asset name must be plain ASCII, so the names above use hyphens.
Each `shortcuts-<language>-{version}.zip` holds the same files with their real
names, for example `iOS 設定捷徑.shortcut`. Rename the shortcut after import if
you want a different name.

## Use it

1. Run the shortcut.
2. Type a keyword, for example `bluetooth`, `wifi`, or `screen time`.
3. Leave the field empty to list every page.
4. Pick a row. The Settings app opens that page.

## Data in this release

- {len(rows)} URLs from {sources} public sources
- {families.get("prefs", 0)} `prefs:`, {families.get("bridge", 0)} `bridge:`, \
{families.get("settings-navigation", 0)} `settings-navigation://`
- {verified} URLs appear in an Apple system file export (iOS 16.2, 18.7.1, 26.2)
- {chinese} URLs carry the official Traditional Chinese name

`settings-urls.json` is the machine readable list. `settings-urls.md` is the same
data for humans.

## Notes

These URL schemes are not public API. App Review can reject an app that uses them.
Use inside the Shortcuts app has no such problem.
"""

with open(notes_path, "w", encoding="utf-8") as handle:
    handle.write(text)
print(f"  notes: {len(rows)} URLs, {len(builds)} shortcuts")
PYTHON

echo "==> Tagging $version"

git tag -a "$version" -m "Release $version"
git push --quiet origin "$version"

echo "==> Creating the release"

create_args=("$version" "--title" "$version" "--notes-file" "$notes")
if [ "$draft" = "--draft" ]; then
  create_args+=("--draft")
fi

gh release create "${create_args[@]}" "${assets[@]}"

echo "==> Done"
gh release view "$version" --json url,assets \
  --jq '.url, (.assets[] | "  \(.name) (\(.size) bytes)")'
