#!/bin/bash
# Publish a GitHub release with the signed shortcuts and the data files.
#
# Usage: scripts/release.sh v1.0.0 [--draft]
#
# The script checks everything first, then tags, then uploads.
# GitHub turns a space in an asset name into a period, so single files get
# hyphens instead of spaces. Each ZIP keeps the original file names.
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
gh auth status >/dev/null 2>&1 || fail "gh is not logged in"

branch="$(git rev-parse --abbrev-ref HEAD)"
[ "$branch" = "main" ] || fail "you are on branch $branch, not main"

git diff --quiet || fail "the working tree has changes"
git diff --cached --quiet || fail "the index has changes"
[ -z "$(git status --porcelain)" ] || fail "the working tree is not clean"

if git rev-parse -q --verify "refs/tags/$version" >/dev/null; then
  fail "tag $version already exists"
fi

git fetch --quiet origin "$branch"
[ "$(git rev-parse HEAD)" = "$(git rev-parse "origin/$branch")" ] ||
  fail "HEAD and origin/$branch differ. Push first."

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

for language_dir in shortcuts/*/; do
  language="$(basename "$language_dir")"
  for signed in "$language_dir"*.shortcut; do
    [ -f "$signed" ] || continue
    flat="$(basename "$signed" | tr ' ' '-')"
    cp "$signed" "$stage/$flat"
    assets+=("$stage/$flat")
  done
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
import os
import sys

notes_path, version = sys.argv[1], sys.argv[2]
root = os.getcwd()
rows = json.load(open(os.path.join(root, "data", "settings-urls.json"), encoding="utf-8"))

total = len(rows)
families = {}
for row in rows:
    families[row["family"]] = families.get(row["family"], 0) + 1
verified = sum(1 for row in rows if row["versions"])
chinese = sum(1 for row in rows if row["label_zh"])
sources = len({source for row in rows for source in row["sources"]})

phone = sum(1 for row in rows
            if row["family"] in ("prefs", "settings-navigation")
            and not row["status"] and (row["label_zh"] or row["label"]))
phone_all = sum(1 for row in rows if row["family"] in ("prefs", "settings-navigation"))
watch = families.get("bridge", 0)

text = f"""## Install

Download a `.shortcut` file, AirDrop it to your iPhone, then tap "Add Shortcut".
You can also open the file on a Mac, and iCloud syncs the shortcut to your iPhone.

| File | Entries | Use it for |
| --- | ---: | --- |
| `iOS-Settings-Launcher.shortcut` | {phone} | Daily use on iPhone and iPad. |
| `iOS-Settings-Launcher-(Full).shortcut` | {phone_all} | Adds pages with no name, and old pages. |
| `Apple-Watch-Settings-Launcher.shortcut` | {watch} | Apple Watch pages, opened from the Watch app. |

The `iOS-設定捷徑*.shortcut` files are the Traditional Chinese build.
They show the official Apple Chinese name and the English name on every row.

Each ZIP holds the same shortcuts with their original file names, including spaces.

## Use it

1. Run the shortcut.
2. Type a keyword, for example `bluetooth`, `wifi`, or `screen time`.
3. Leave the field empty to list every page.
4. Pick a row. The Settings app opens that page.

## Data in this release

- {total} URLs from {sources} public sources
- {families.get("prefs", 0)} `prefs:`, {families.get("bridge", 0)} `bridge:`, {families.get("settings-navigation", 0)} `settings-navigation://`
- {verified} URLs appear in an Apple system file export (iOS 16.2, 18.7.1, 26.2)
- {chinese} URLs carry the official Traditional Chinese name

`settings-urls.json` is the machine readable list. `settings-urls.md` is the same data for humans.

## Notes

These URL schemes are not public API. App Review can reject an app that uses them.
Use inside the Shortcuts app has no such problem.
"""

with open(notes_path, "w", encoding="utf-8") as handle:
    handle.write(text)
print(f"  notes: {total} URLs, {phone}/{phone_all}/{watch} per shortcut")
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
  --jq '"\(.url)\n" + ([.assets[] | "  \(.name) (\(.size) bytes)"] | join("\n"))'
