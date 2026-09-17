#!/usr/bin/env python3
"""Download every upstream source into raw/.

The raw files are not stored in this repository. They belong to their authors.
Run this script once before merge.py.
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")

FIFI = "https://raw.githubusercontent.com/FifiTheBulldog/ios-settings-urls/master"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# name in raw/, url
SOURCES = [
    ("fifi.md", FIFI + "/settings-urls.md"),
    ("fifi_deprecated.md", FIFI + "/archive/deprecated.md"),
    ("fifi_gaps.json", FIFI + "/overrides/gaps.json"),
    ("dump_manifest.txt", FIFI + "/archive/preference-manifest-dump.txt"),
    ("dump_dyld.txt", FIFI + "/archive/dyld-shared-cache-dump.txt"),

    ("v162_prefs.md", FIFI + "/versions/16.2/en/prefs.md"),
    ("v162_bridge.md", FIFI + "/versions/16.2/en/bridge.md"),
    ("v1871_prefs.md", FIFI + "/versions/18.7.1/en/prefs.md"),
    ("v1871_bridge.md", FIFI + "/versions/18.7.1/en/bridge.md"),
    ("v26_prefs.md", FIFI + "/versions/26.2/en/prefs.md"),
    ("v26_bridge.md", FIFI + "/versions/26.2/en/bridge.md"),

    ("zh162_prefs.md", FIFI + "/versions/16.2/zh_TW/prefs.md"),
    ("zh162_bridge.md", FIFI + "/versions/16.2/zh_TW/bridge.md"),
    ("zh1871_prefs.md", FIFI + "/versions/18.7.1/zh_TW/prefs.md"),
    ("zh1871_bridge.md", FIFI + "/versions/18.7.1/zh_TW/bridge.md"),
    ("zh262_prefs.md", FIFI + "/versions/26.2/zh_TW/prefs.md"),
    ("zh262_bridge.md", FIFI + "/versions/26.2/zh_TW/bridge.md"),

    ("mehdi.md", "https://raw.githubusercontent.com/1mehdifaraji/ios-settings-url-schemes/main/README.md"),
    ("tanaschita.md", "https://raw.githubusercontent.com/Tanaschita/ios-known-url-schemes-and-universal-links/master/README.md"),
    ("gist_dean.txt", "https://gist.githubusercontent.com/deanlyoung/368e274945a6929e0ea77c4eca345560/raw"),
    ("gist_tzmartin.txt", "https://gist.githubusercontent.com/tzmartin/b7019c22fc3152a0b2fe/raw"),

    ("art_macstories.html", "https://www.macstories.net/ios/a-comprehensive-guide-to-all-120-settings-urls-supported-by-ios-and-ipados-13-1/"),
    ("art_gadgethacks.html", "https://ios.gadgethacks.com/how-to/ios-17-2-includes-50-new-url-schemes-you-can-use-shortcuts-your-iphone-0385465/"),
    ("art_wesley.html", "https://wesleydegroot.nl/blog/iOS-settings-URLs"),
    ("forum_macrumors.html", "https://forums.macrumors.com/threads/manually-creating-settings-launchers-in-app-launching-apps.2037291/"),
]

MINIMUM_BYTES = 500


def resolve_with_public_dns(host):
    """Some networks fail to resolve a host. Ask a public resolver instead."""
    result = subprocess.run(["dig", "+short", host, "@1.1.1.1"], capture_output=True, text=True)
    addresses = [line for line in result.stdout.split() if line.count(".") == 3]
    return addresses[-1] if addresses else ""


def download(name, url):
    target = os.path.join(RAW, name)
    base = ["curl", "-fsSL", "--compressed", "-A", USER_AGENT]
    result = subprocess.run(base + ["-o", target, url], capture_output=True, text=True)
    if result.returncode != 0 and "Could not resolve host" in result.stderr:
        # Some networks fail on one host. Resolve it with a public resolver.
        host = url.split("/")[2]
        address = resolve_with_public_dns(host)
        if address:
            result = subprocess.run(
                base + ["--resolve", f"{host}:443:{address}", "-o", target, url],
                capture_output=True, text=True,
            )
    size = os.path.getsize(target) if os.path.exists(target) else 0
    ok = result.returncode == 0 and size >= MINIMUM_BYTES
    print(f"  {'ok  ' if ok else 'FAIL'} {name:26s} {size / 1024:8.1f} KB  {url}")
    return ok


def main():
    os.makedirs(RAW, exist_ok=True)
    failed = [name for name, url in SOURCES if not download(name, url)]
    print()
    if failed:
        print("failed:", ", ".join(failed))
        print("Some sites block automated downloads. Save those pages by hand into raw/.")
        sys.exit(1)
    print(f"all {len(SOURCES)} sources are in {RAW}")


if __name__ == "__main__":
    main()
