#!/usr/bin/env python3
"""Merge every collected iOS Settings URL source into one list."""

import html
import json
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")

SOURCES = {
    "fifi": ("FifiTheBulldog/ios-settings-urls (settings-urls.md)", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/settings-urls.md"),
    "fifi26": ("FifiTheBulldog versions/26.2/en/prefs.md", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/26.2/en/prefs.md"),
    "fifi26b": ("FifiTheBulldog versions/26.2/en/bridge.md (watchOS)", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/26.2/en/bridge.md"),
    "fifi18": ("FifiTheBulldog versions/18.7.1/en/prefs.md", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/18.7.1/en/prefs.md"),
    "fifi18b": ("FifiTheBulldog versions/18.7.1/en/bridge.md (watchOS)", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/18.7.1/en/bridge.md"),
    "fifi16": ("FifiTheBulldog versions/16.2/en/prefs.md", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/16.2/en/prefs.md"),
    "fifi16b": ("FifiTheBulldog versions/16.2/en/bridge.md (watchOS)", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/16.2/en/bridge.md"),
    "fifidep": ("FifiTheBulldog archive/deprecated.md", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/deprecated.md"),
    "fifiman": ("FifiTheBulldog PreferenceManifests dump", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/preference-manifest-dump.txt"),
    "fifidyld": ("FifiTheBulldog dyld_shared_cache dump", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/dyld-shared-cache-dump.txt"),
    "mehdi": ("1mehdifaraji/ios-settings-url-schemes", "https://github.com/1mehdifaraji/ios-settings-url-schemes"),
    "wesley": ("Wesley de Groot: iOS Settings URLs", "https://wesleydegroot.nl/blog/iOS-settings-URLs"),
    "macstories": ("MacStories: 120+ Settings URLs (iOS 13.1)", "https://www.macstories.net/ios/a-comprehensive-guide-to-all-120-settings-urls-supported-by-ios-and-ipados-13-1/"),
    "gadgethacks": ("Gadget Hacks: iOS 17.2 new URL schemes", "https://ios.gadgethacks.com/how-to/ios-17-2-includes-50-new-url-schemes-you-can-use-shortcuts-your-iphone-0385465/"),
    "dean": ("deanlyoung gist (URL Schemes, updated)", "https://gist.github.com/deanlyoung/368e274945a6929e0ea77c4eca345560"),
    "tzmartin": ("tzmartin / ahmadtech199 gist", "https://gist.github.com/tzmartin/b7019c22fc3152a0b2fe"),
    "macrumors": ("MacRumors forum thread", "https://forums.macrumors.com/threads/manually-creating-settings-launchers-in-app-launching-apps.2037291/"),
}

LABEL_PRIORITY = ["fifi26", "fifi26b", "fifi18", "fifi18b", "fifi16", "fifi16b", "fifi", "wesley", "macstories", "mehdi", "fifidep", "dean", "tzmartin"]
VERSION_SOURCES = {"fifi16": "16.2", "fifi16b": "16.2", "fifi18": "18.7", "fifi18b": "18.7", "fifi26": "26.2", "fifi26b": "26.2"}
LEGACY_ONLY = {"dean", "tzmartin", "fifidep", "macrumors"}

SCHEME_RE = re.compile(r"^(app-prefs|prefs|app-settings|settings|bridge|settings-navigation)\s*:\s*/{0,2}", re.I)
URL_RE = re.compile(r"(?:App-[Pp]refs|app-prefs|APP-PREFS|[Pp]refs|PREFS|app-settings|bridge|settings-navigation)\s*:\s*/{0,2}[^\s\"'`<>()\[\]|,;]*")

records = []  # (family, body, label, source, extra_scheme)


def read(name):
    path = os.path.join(RAW, name)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="ignore") as handle:
        return handle.read()


JUNK_TAIL = re.compile(r"(?:\\+[nrt]|\n|\r|\t|\u21b3|&nbsp;).*$", re.S)


def normalize(raw):
    """Return (family, body, original_scheme) or None."""
    raw = html.unescape(raw.strip()).strip("`.,;)")
    raw = raw.replace("&amp;", "&")
    raw = JUNK_TAIL.sub("", raw)
    match = SCHEME_RE.match(raw)
    if not match:
        return None
    scheme = match.group(1).lower()
    body = raw[match.end():]
    body = JUNK_TAIL.sub("", body).strip().rstrip("`.,;)")
    if "%@" in body or "\\" in body:
        return None
    if re.search(r"_(DESCRIPTION|KEYWORDS)$", body):
        return None
    if scheme == "bridge":
        family = "bridge"
    elif scheme == "settings-navigation":
        family = "settings-navigation"
    else:
        family = "prefs"
    if family == "prefs":
        if body and not body.lower().startswith("root"):
            return None
        if body.lower() == "root":
            body = ""
    if " " in body or "<" in body or "%20%20" in body:
        return None
    if len(body) > 300:
        return None
    return family, body, scheme


def clean_label(label):
    label = re.sub(r"\s+", " ", (label or "").strip())
    if len(label) > 90 or "http" in label or re.search(r"[.?!] [a-z]", label):
        return ""
    return label


def add(raw_url, label, source):
    norm = normalize(raw_url)
    if not norm:
        return
    family, body, scheme = norm
    records.append((family, body, clean_label(label), source, scheme))


def parse_md_pairs(text, source):
    """Lines like: - Label: `url` or `url2`"""
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        match = re.match(r"^-\s+(.*?):\s*(`.*)$", line)
        if not match:
            continue
        label = match.group(1).replace("\u21fe", "\u2192").replace("\u2192", " \u2192 ")
        label = re.sub(r"\s*\u2192\s*", " \u2192 ", label)
        for url in re.findall(r"`([^`]+)`", match.group(2)):
            add(url, label, source)


def parse_mehdi(text):
    section = ""
    label = ""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or set(stripped) <= {"-", "="}:
            continue
        if stripped.startswith(">"):
            url = stripped[1:].strip()
            full = label or section
            if section and label and not label.startswith(section):
                full = section + " \u2192 " + label
            add(url, full, "mehdi")
            continue
        if stripped.startswith("#"):
            continue
        cleaned = stripped.replace("\u21fe", "\u2192")
        cleaned = re.sub(r"\s*\u2192\s*", " \u2192 ", cleaned)
        cleaned = re.sub(r"\s*\((?:open menu|highlight menu item|jump to toggle|jump to menu item)[^)]*\)\s*$", "", cleaned, flags=re.I)
        if cleaned.lower().startswith("settings \u2192"):
            section = cleaned.split("\u2192", 1)[1].strip()
            label = ""
        else:
            label = cleaned


def parse_wesley(text):
    section = ""
    for match in re.finditer(r"<h1[^>]*>(.*?)</h1>|<h3[^>]*>(.*?)</h3>|<a href='([^']+)'", text):
        h1, h3, href = match.groups()
        if h1:
            section = html.unescape(re.sub(r"<[^>]+>", "", h1)).strip()
            label_part = ""
        elif h3:
            label_part = html.unescape(re.sub(r"<[^>]+>", "", h3)).strip()
            parse_wesley.current = label_part
        elif href:
            label_part = getattr(parse_wesley, "current", "")
            if label_part.lower() in ("root", ""):
                full = section
            else:
                full = (section + " \u2192 " + label_part) if section else label_part
            add(href, full, "wesley")


def parse_macstories(text):
    text = html.unescape(text)
    section = ""
    for match in re.finditer(r"<h4[^>]*>(.*?)</h4>|<li>(.*?)</li>", text, re.S):
        head, item = match.groups()
        if head:
            section = re.sub(r"<[^>]+>", "", head).strip()
            continue
        if not item or "prefs:" not in item.lower():
            continue
        plain = re.sub(r"<[^>]+>", "\n", item)
        parts = [p.strip() for p in plain.split("\n") if p.strip()]
        label = ""
        for part in parts:
            if "prefs:" in part.lower():
                continue
            label = part.rstrip(":").strip()
            break
        label = label.replace("\u21fe", "\u2192")
        label = re.sub(r"\s*\u2192\s*", " \u2192 ", label)
        if not label:
            label = section
        for url in re.findall(r"prefs:[^\s<\"']+", item, re.I):
            add(url, label, "macstories")


def parse_plain_urls(text, source):
    text = html.unescape(html.unescape(text))
    for url in URL_RE.findall(text):
        add(url, "", source)


def parse_dean(text):
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        label = re.sub(r"[*~`]", "", cells[0]).strip()
        if not label or label.lower().startswith("settings section") or set(label) <= {"-", ":"}:
            continue
        for cell in cells[1:]:
            for url in re.findall(r"`([^`]+)`", cell):
                add(url, label, "dean")


parse_md_pairs(read("fifi.md"), "fifi")
# Traditional Chinese labels, so the list can be searched in Chinese too.
ZH_FILES = [("zh162_prefs.md", "16.2"), ("zh162_bridge.md", "16.2"),
            ("zh1871_prefs.md", "18.7"), ("zh1871_bridge.md", "18.7"),
            ("zh262_prefs.md", "26.2"), ("zh262_bridge.md", "26.2")]
ZH_PRIORITY = ["26.2", "18.7", "16.2"]
zh_labels = defaultdict(dict)


def parse_zh(text, version):
    for line in text.splitlines():
        match = re.match(r"^-\s+(.*?):\s*(`.*)$", line.strip())
        if not match:
            continue
        label = clean_label(re.sub(r"\s*\u2192\s*", " \u2192 ", match.group(1)))
        if not label:
            continue
        for url in re.findall(r"`([^`]+)`", match.group(2)):
            norm = normalize(url)
            if norm:
                zh_labels[(norm[0], norm[1])][version] = label


for name, version in ZH_FILES:
    parse_zh(read(name), version)

parse_md_pairs(read("v26_prefs.md"), "fifi26")
parse_md_pairs(read("v26_bridge.md"), "fifi26b")
parse_md_pairs(read("v1871_prefs.md"), "fifi18")
parse_md_pairs(read("v1871_bridge.md"), "fifi18b")
parse_md_pairs(read("v162_prefs.md"), "fifi16")
parse_md_pairs(read("v162_bridge.md"), "fifi16b")
parse_md_pairs(read("fifi_deprecated.md"), "fifidep")
parse_mehdi(read("mehdi.md"))
parse_wesley(read("art_wesley.html"))
parse_macstories(read("art_macstories.html"))
parse_dean(read("gist_dean.txt"))
parse_plain_urls(read("gist_tzmartin.txt"), "tzmartin")
parse_plain_urls(read("dump_manifest.txt"), "fifiman")
parse_plain_urls(read("dump_dyld.txt"), "fifidyld")
parse_plain_urls(read("art_gadgethacks.html"), "gadgethacks")
parse_plain_urls(read("forum_macrumors.html"), "macrumors")

# gaps.json holds URLs that Fifi pulled from manifests but had not merged yet
try:
    for item in json.loads(read("fifi_gaps.json") or "[]"):
        label = ""
        if isinstance(item.get("label"), dict):
            label = item["label"].get("en", "")
        add(item.get("url", ""), label, "fifiman")
except Exception:
    pass

entries = {}
for family, body, label, source, scheme in records:
    key = (family, body)
    entry = entries.setdefault(key, {
        "family": family,
        "body": body,
        "labels": defaultdict(list),
        "sources": set(),
        "schemes": set(),
    })
    entry["sources"].add(source)
    entry["schemes"].add(scheme)
    if label:
        entry["labels"][source].append(label)


def best_label(entry):
    for source in LABEL_PRIORITY:
        for label in entry["labels"].get(source, []):
            if label:
                return label, source
    for source, labels in entry["labels"].items():
        for label in labels:
            if label:
                return label, source
    return "", ""


ROOT_RE = re.compile(r"root=([^&#/]*)", re.I)


def root_token(body):
    match = ROOT_RE.search(body)
    if not match:
        return ""
    return re.split(r"%23", match.group(1), flags=re.I)[0]


def pick_alias(head):
    """Fifi joins several manifest labels with ' | '. Keep the most descriptive one."""
    parts = [p.strip() for p in head.split(" | ") if p.strip()]
    if not parts:
        return ""
    return max(parts, key=lambda p: len(re.split(r"[\s\-]+", p)))


# Vote for a section name per root token, and trust the best source first.
section_votes = defaultdict(lambda: defaultdict(Counter))
for entry in entries.values():
    token = root_token(entry["body"])
    for source, labels in entry["labels"].items():
        for label in labels:
            head = pick_alias(label.split("\u2192")[0].strip())
            if head:
                section_votes[(entry["family"], token)][source][head] += 1


def section_name(family, token):
    votes = section_votes.get((family, token))
    if not votes:
        return ""
    for source in LABEL_PRIORITY:
        if votes.get(source):
            return votes[source].most_common(1)[0][0]
    return max(votes.values(), key=lambda c: sum(c.values())).most_common(1)[0][0]

rows = []
for (family, body), entry in entries.items():
    label, label_source = best_label(entry)
    token = root_token(body)
    section = section_name(family, token) or token or "(Settings root)"
    if not token:
        section = "(Settings root)"
    if family == "bridge":
        section = "watchOS bridge: " + section
    if family == "settings-navigation":
        section = "settings-navigation:"
    scheme_prefix = {"prefs": "prefs:", "bridge": "bridge:", "settings-navigation": "settings-navigation://"}[family]
    url = scheme_prefix + body
    live_sources = entry["sources"] - LEGACY_ONLY
    status = "" if live_sources else "legacy"
    if "fifidep" in entry["sources"] and not live_sources:
        status = "deprecated"
    zh = zh_labels.get((family, body), {})
    label_zh = next((zh[v] for v in ZH_PRIORITY if v in zh), "")
    rows.append({
        "section": section,
        "label": label,
        "label_zh": label_zh,
        "url": url,
        "family": family,
        "root": token,
        "sources": sorted(entry["sources"]),
        "schemes": sorted(entry["schemes"]),
        "versions": sorted({VERSION_SOURCES[s] for s in entry["sources"] if s in VERSION_SOURCES}),
        "status": status,
        "label_source": label_source,
    })

# One spelling per section: keep the most common capitalization.
spelling = defaultdict(Counter)
for row in rows:
    spelling[row["section"].casefold()][row["section"]] += 1
for row in rows:
    row["section"] = spelling[row["section"].casefold()].most_common(1)[0][0]

rows.sort(key=lambda r: (r["section"].lower(), r["url"].count("/") + r["url"].count("#"), r["url"].lower()))

os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
with open(os.path.join(ROOT, "data", "settings-urls.json"), "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=1)

print("entries:", len(rows))
print("prefs:", sum(1 for r in rows if r["family"] == "prefs"))
print("bridge:", sum(1 for r in rows if r["family"] == "bridge"))
print("nav:", sum(1 for r in rows if r["family"] == "settings-navigation"))
print("legacy/deprecated:", sum(1 for r in rows if r["status"]))
print("version confirmed:", sum(1 for r in rows if r["versions"]))
print("zh labelled:", sum(1 for r in rows if r["label_zh"]))
print("labelled:", sum(1 for r in rows if r["label"]))
print("sections:", len({r["section"] for r in rows}))
counts = Counter(s for r in rows for s in r["sources"])
for source, count in counts.most_common():
    print("  ", source, count)
