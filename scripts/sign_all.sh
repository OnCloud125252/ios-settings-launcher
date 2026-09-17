#!/bin/bash
# Sign every unsigned shortcut in shortcuts/<language>/unsigned/.
# Apple signs shortcuts on a remote service. That service fails often, so retry.
# A failed attempt never destroys a shortcut that is already signed.
#
# Usage: sign_all.sh [tries] [seconds between tries]
set -u

cd "$(dirname "$0")/../shortcuts" || exit 1

tries="${1:-20}"
wait_seconds="${2:-120}"

attempt=1
while [ "$attempt" -le "$tries" ]; do
  pending=0
  for src in */unsigned/*.shortcut; do
    [ -f "$src" ] || continue
    language="${src%%/*}"
    name="$(basename "$src")"
    out="$language/$name"
    if [ -f "$out" ] && [ "$out" -nt "$src" ]; then
      continue
    fi
    tmp="$(mktemp -t shortcutsign)" || exit 1
    rm -f "$tmp"
    if shortcuts sign --mode anyone --input "$src" --output "$tmp" 2>/dev/null && [ -s "$tmp" ]; then
      mv -f "$tmp" "$out"
      echo "signed: $out ($(du -h "$out" | cut -f1))"
    else
      rm -f "$tmp"
      pending=1
    fi
  done

  if [ "$pending" -eq 0 ]; then
    echo "ALL SIGNED (attempt $attempt)"
    exit 0
  fi

  echo "attempt $attempt: signing service not ready, waiting ${wait_seconds}s"
  sleep "$wait_seconds"
  attempt=$((attempt + 1))
done

echo "STILL UNSIGNED after $tries attempts"
exit 1
