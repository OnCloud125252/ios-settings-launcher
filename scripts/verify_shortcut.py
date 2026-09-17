#!/usr/bin/env python3
"""Check the unsigned shortcut plists: action wiring, and a runtime simulation."""

import glob
import os
import plistlib
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OBJ = "\ufffc"
SEPARATOR = " \u21e2 "


def collect_attachments(value, found):
    if isinstance(value, dict):
        if "OutputUUID" in value and value.get("Type") == "ActionOutput":
            found.append(value["OutputUUID"])
        for item in value.values():
            collect_attachments(item, found)
    elif isinstance(value, list):
        for item in value:
            collect_attachments(item, found)


def simulate(text, keyword):
    safe = re.sub(r"[^\w\s]", ".", keyword, flags=re.UNICODE)
    matches = re.findall(r"(?im)^.*" + safe + r".*$", text)
    return matches


def check(path):
    print("=" * 70)
    print(os.path.basename(path))
    with open(path, "rb") as handle:
        workflow = plistlib.load(handle)
    actions = workflow["WFWorkflowActions"]
    known = set()
    problems = []
    for index, act in enumerate(actions):
        params = act["WFWorkflowActionParameters"]
        refs = []
        collect_attachments(params, refs)
        for ref in refs:
            if ref not in known:
                problems.append(f"action {index} ({act['WFWorkflowActionIdentifier']}) uses unknown output {ref}")
        if "UUID" in params:
            known.add(params["UUID"])
        print(f" {index + 1}. {act['WFWorkflowActionIdentifier']:45s} refs={len(refs)}")

    text = actions[0]["WFWorkflowActionParameters"]["WFTextActionText"]
    lines = text.split("\n")
    print(f" lines={len(lines)}  chars={len(text)}")

    # Every line must split into exactly one label and one URL.
    bad = [line for line in lines if line.count(SEPARATOR) != 1]
    if bad:
        problems.append(f"{len(bad)} lines do not have exactly one separator, e.g. {bad[0][:80]}")
    bad_url = [line for line in lines if not re.match(r"^(prefs|bridge|settings-navigation):", line.split(SEPARATOR)[-1])]
    if bad_url:
        problems.append(f"{len(bad_url)} lines end with something that is not a URL, e.g. {bad_url[0][:80]}")

    # The pattern in the Match Text action must be the one we expect.
    pattern = actions[3]["WFWorkflowActionParameters"]["WFMatchTextPattern"]["Value"]["string"]
    if pattern != "(?im)^.*" + OBJ + ".*$":
        problems.append("unexpected match pattern: " + repr(pattern))
    ranges = actions[3]["WFWorkflowActionParameters"]["WFMatchTextPattern"]["Value"]["attachmentsByRange"]
    if list(ranges) != ["{8, 1}"]:
        problems.append("keyword placeholder is at the wrong offset: " + str(list(ranges)))

    for keyword in ["wifi", "藍牙", "鍵盤", "Wi-Fi", "keyboard", "電池", "VPN",
                    "螢幕使用時間", "專注模式", "個人熱點", "root=CAMERA", ""]:
        matches = simulate(text, keyword)
        sample = matches[0].split(SEPARATOR)[-1] if matches else "-"
        # A keyword with no hit is normal for a list that does not cover that page.
        print(f"   search {keyword!r:16s} -> {len(matches):5d} hits   first: {sample}")

    chosen = simulate(text, "藍牙")[0] if simulate(text, "藍牙") else lines[0]
    print("   picked line:", chosen)
    print("   parsed URL: ", chosen.split(SEPARATOR)[-1])

    if problems:
        print(" PROBLEMS:")
        for problem in problems:
            print("  -", problem)
    else:
        print(" OK: every action is wired, and every line parses into a URL.")
    return not problems


ok = True
for path in sorted(glob.glob(os.path.join(ROOT, "shortcuts", "*", "unsigned", "*.shortcut"))):
    ok = check(path) and ok
print("=" * 70)
print("ALL OK" if ok else "HAS PROBLEMS")
