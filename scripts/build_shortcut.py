#!/usr/bin/env python3
"""Build an importable .shortcut file that opens any iOS Settings URL.

Flow inside the shortcut:
  Text (whole list) -> Ask for Input (keyword) -> Replace Text (make the keyword
  regex-safe) -> Match Text (keep matching lines) -> Choose from List ->
  Split Text -> Get Item from List -> URL -> Open URLs
"""

import json
import os
import plistlib
import re
import sys
import uuid as uuidlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = json.load(open(os.path.join(ROOT, "data", "settings-urls.json"), encoding="utf-8"))

LANGUAGES = {
    "zh-TW": {
        "labels": "chinese",
        "choose": "\u9078\u64c7\u8981\u958b\u555f\u7684\u8a2d\u5b9a\u9801\u9762",
        "names": {
            "phone": "iOS \u8a2d\u5b9a\u6377\u5f91",
            "phone_all": "iOS \u8a2d\u5b9a\u6377\u5f91 \u5b8c\u6574\u7248",
            "watch": "Apple Watch \u8a2d\u5b9a\u6377\u5f91",
        },
        "prompts": {
            "phone": "\u8f38\u5165\u95dc\u9375\u5b57\uff08\u4e2d\u82f1\u6587\u7686\u53ef\uff0c\u7559\u7a7a\uff1d\u5168\u90e8 {count} \u7b46\uff09",
            "phone_all": "\u8f38\u5165\u95dc\u9375\u5b57\uff08\u542b\u672a\u6e2c\u8a66\u9805\u76ee\uff0c\u5171 {count} \u7b46\uff09",
            "watch": "\u8f38\u5165\u95dc\u9375\u5b57\uff08Apple Watch \u8a2d\u5b9a\uff0c\u5171 {count} \u7b46\uff09",
        },
    },
    "en": {
        "labels": "english",
        "choose": "Choose a Settings page",
        "names": {
            "phone": "iOS Settings Launcher",
            "phone_all": "iOS Settings Launcher (Full)",
            "watch": "Apple Watch Settings Launcher",
        },
        "prompts": {
            "phone": "Keyword (leave empty for all {count} pages)",
            "phone_all": "Keyword (includes untested pages, {count} total)",
            "watch": "Keyword (Apple Watch settings, {count} total)",
        },
    },
}

SEPARATOR = " \u21e2 "          # between the label and the URL
LANG_SEPARATOR = " \uff5c "     # between the Chinese label and the English label
OBJ = "\ufffc"                  # object replacement character used by Shortcuts

GLYPH = 59666
COLOR = 1440408063


# Fixed namespace, so two builds of the same data give the same file.
UUID_NAMESPACE = uuidlib.UUID("6f9f1f4e-4a1a-5f6a-9c9d-6a5f0b6c2f10")


def stable_uuid(seed):
    return str(uuidlib.uuid5(UUID_NAMESPACE, seed)).upper()


def attachment(out_uuid, name):
    return {
        "Value": {"OutputUUID": out_uuid, "OutputName": name, "Type": "ActionOutput"},
        "WFSerializationType": "WFTextTokenAttachment",
    }


def token_string(parts):
    """parts: list of plain strings and (uuid, name) tuples."""
    text = ""
    attachments = {}
    for part in parts:
        if isinstance(part, str):
            text += part
        else:
            attachments["{%d, 1}" % len(text)] = {
                "OutputUUID": part[0],
                "OutputName": part[1],
                "Type": "ActionOutput",
            }
            text += OBJ
    return {
        "Value": {"string": text, "attachmentsByRange": attachments},
        "WFSerializationType": "WFTextTokenString",
    }


def action(identifier, params):
    return {"WFWorkflowActionIdentifier": identifier, "WFWorkflowActionParameters": params}


def clean(text):
    return text.replace(SEPARATOR.strip(), "-").replace(LANG_SEPARATOR.strip(), "-").replace("\n", " ").strip()


# A few pages exist only in community lists, so Apple has no Chinese label for them.
SEGMENT_ZH = {
    "Passwords & Accounts": "密碼與帳號",
    "Accounts": "帳號",
    "Account Settings": "帳號設定",
    "Add Account": "加入帳號",
    "Fetch New Data": "取得新資料",
    "Other": "其他",
    "Add CalDAV Account": "加入CalDAV帳號",
    "Add CardDAV Account": "加入CardDAV帳號",
    "Add LDAP Account": "加入LDAP帳號",
    "Add Mail Account": "加入郵件帳號",
    "Add Subscribed Calendar": "加入訂閱的行事曆",
    "Personal Hotspot": "個人熱點",
    "Family Sharing": "家人共享",
    "Wi-Fi Password": "Wi-Fi密碼",
    "Add VPN Configuration\u2026": "加入VPN設定⋯",
    "Podcasts": "Podcast",
    "Video": "影片",
    "Home": "家庭",
    "Mail": "郵件",
    "Settings": "設定",
    "Usage": "使用情況",
}


def segments_of(label):
    return [s.strip() for s in label.split("\u2192") if s.strip() and s.strip() != "(root)"]


def chinese_from_english(label):
    """Build a Chinese label when Apple never shipped one. Empty if nothing is known."""
    parts = segments_of(label)
    translated = [SEGMENT_ZH.get(p, p) for p in parts]
    if translated == parts:
        return ""
    return " \u2192 ".join(translated)


def alias_label(label):
    """A label segment can hold several manifest names joined by ' | '. Keep one."""
    segments = []
    for segment in segments_of(label):
        parts = [p.strip() for p in segment.split(" | ") if p.strip()]
        if parts:
            segments.append(max(parts, key=lambda p: len(re.split(r"[\s\-]+", p))))
    return " \u2192 ".join(segments)


def depth(row):
    label = row["label_zh"] or row["label"]
    return label.count("\u2192") if label else 9


def build_lines(rows, mode):
    """mode 'chinese' shows Chinese plus the English leaf. mode 'english' shows English."""
    # Top level pages first, so a search shows the main page before deep sub items.
    rows = sorted(rows, key=lambda r: (depth(r), r["section"].lower(), r["url"].lower()))
    lines = []
    for row in rows:
        en = alias_label(clean(row["label"]))
        zh = alias_label(clean(row["label_zh"])) or chinese_from_english(en)
        fallback = alias_label(clean(row["section"]))
        if mode == "english":
            label = en or zh or fallback
        else:
            leaf = en.split("\u2192")[-1].strip()
            if zh and leaf and zh != leaf and not zh.endswith(leaf):
                label = zh + LANG_SEPARATOR + leaf
            else:
                label = zh or en or fallback
        lines.append(label + SEPARATOR + row["url"])
    return lines


def build_workflow(lines, prompt, choose_prompt, seed):
    text_uuid = stable_uuid(seed + ":text")
    ask_uuid = stable_uuid(seed + ":ask")
    safe_uuid = stable_uuid(seed + ":safe")
    match_uuid = stable_uuid(seed + ":match")
    choose_uuid = stable_uuid(seed + ":choose")
    split_uuid = stable_uuid(seed + ":split")
    item_uuid = stable_uuid(seed + ":item")
    url_uuid = stable_uuid(seed + ":url")

    actions = [
        action("is.workflow.actions.gettext", {
            "UUID": text_uuid,
            "CustomOutputName": "Settings URL List",
            "WFTextActionText": "\n".join(lines),
        }),
        action("is.workflow.actions.ask", {
            "UUID": ask_uuid,
            "WFInputType": "Text",
            "CustomOutputName": "Keyword",
            "WFAskActionPrompt": prompt,
        }),
        # Turn every regex metacharacter into "." so any typed text stays a valid pattern.
        action("is.workflow.actions.text.replace", {
            "UUID": safe_uuid,
            "CustomOutputName": "Safe Keyword",
            "WFReplaceTextRegularExpression": True,
            "WFReplaceTextFind": "[^\\p{L}\\p{N}\\s_]",
            "WFReplaceTextReplace": ".",
            "WFInput": token_string([(ask_uuid, "Provided Input")]),
        }),
        action("is.workflow.actions.text.match", {
            "UUID": match_uuid,
            "CustomOutputName": "Matching Lines",
            "WFMatchTextCaseSensitive": False,
            "WFMatchTextPattern": token_string(["(?im)^.*", (safe_uuid, "Updated Text"), ".*$"]),
            "text": token_string([(text_uuid, "Settings URL List")]),
        }),
        action("is.workflow.actions.choosefromlist", {
            "UUID": choose_uuid,
            "CustomOutputName": "Chosen Line",
            "WFChooseFromListActionPrompt": choose_prompt,
            "WFInput": attachment(match_uuid, "Matching Lines"),
        }),
        action("is.workflow.actions.text.split", {
            "UUID": split_uuid,
            "CustomOutputName": "Line Parts",
            "WFTextSeparator": "Custom",
            "WFTextCustomSeparator": SEPARATOR,
            "text": attachment(choose_uuid, "Chosen Line"),
        }),
        action("is.workflow.actions.getitemfromlist", {
            "UUID": item_uuid,
            "CustomOutputName": "Settings URL",
            "WFItemSpecifier": "Last Item",
            "WFInput": attachment(split_uuid, "Line Parts"),
        }),
        action("is.workflow.actions.url", {
            "UUID": url_uuid,
            "WFURLActionURL": attachment(item_uuid, "Settings URL"),
        }),
        action("is.workflow.actions.openurl", {
            "UUID": stable_uuid(seed + ":open"),
            "WFInput": attachment(url_uuid, "URL"),
        }),
    ]

    return {
        "WFQuickActionSurfaces": [],
        "WFWorkflowActions": actions,
        "WFWorkflowClientVersion": "2605.0.5",
        "WFWorkflowHasOutputFallback": False,
        "WFWorkflowHasShortcutInputVariables": False,
        "WFWorkflowIcon": {
            "WFWorkflowIconGlyphNumber": GLYPH,
            "WFWorkflowIconStartColor": COLOR,
        },
        "WFWorkflowImportQuestions": [],
        "WFWorkflowInputContentItemClasses": [
            "WFAppStoreAppContentItem", "WFArticleContentItem", "WFContactContentItem",
            "WFDateContentItem", "WFEmailAddressContentItem", "WFFolderContentItem",
            "WFGenericFileContentItem", "WFImageContentItem", "WFiTunesProductContentItem",
            "WFLocationContentItem", "WFDCMapsLinkContentItem", "WFAVAssetContentItem",
            "WFPDFContentItem", "WFPhoneNumberContentItem", "WFRichTextContentItem",
            "WFSafariWebPageContentItem", "WFStringContentItem", "WFURLContentItem",
        ],
        "WFWorkflowMinimumClientVersion": 900,
        "WFWorkflowMinimumClientVersionString": "900",
        "WFWorkflowOutputContentItemClasses": [],
        "WFWorkflowTypes": [],
    }


def write_unsigned(workflow, name, out_dir):
    """Write the plist. Signing happens later, in sign_all.sh."""
    unsigned_dir = os.path.join(out_dir, "unsigned")
    os.makedirs(unsigned_dir, exist_ok=True)
    path = os.path.join(unsigned_dir, name + ".shortcut")
    data = plistlib.dumps(workflow)
    # Keep the old file when nothing changed, so sign_all.sh does not sign again.
    if os.path.exists(path) and open(path, "rb").read() == data:
        return path, False
    with open(path, "wb") as handle:
        handle.write(data)
    return path, True


def row_sets():
    # Phone list: no watch pages, no dead URLs, and a real name for every row.
    phone = [
        r for r in ROWS
        if r["family"] in ("prefs", "settings-navigation")
        and not r["status"]
        and (r["label_zh"] or r["label"])
    ]
    # Apple signs shortcuts on a remote service that rejects very large files.
    # So the data ships as three smaller shortcuts instead of one big one.
    phone_all = [r for r in ROWS if r["family"] in ("prefs", "settings-navigation")]
    watch = [r for r in ROWS if r["family"] == "bridge"]
    return {"phone": phone, "phone_all": phone_all, "watch": watch}


def main():
    wanted = sys.argv[1:] or list(LANGUAGES)
    sets = row_sets()

    for language in wanted:
        if language not in LANGUAGES:
            print(f"unknown language: {language}. known: {', '.join(LANGUAGES)}")
            sys.exit(1)
        config = LANGUAGES[language]
        out_dir = os.path.join(ROOT, "shortcuts", language)
        os.makedirs(out_dir, exist_ok=True)
        for key, rows in sets.items():
            lines = build_lines(rows, config["labels"])
            prompt = config["prompts"][key].format(count=len(rows))
            name = config["names"][key]
            workflow = build_workflow(lines, prompt, config["choose"], f"{language}:{key}")
            path, changed = write_unsigned(workflow, name, out_dir)
            print(f"{language:6s} {name:32s} {len(lines):5d} entries  "
                  f"{os.path.getsize(path) / 1024:5.0f} KB  {'written' if changed else 'unchanged'}")

    print("\nNow run scripts/sign_all.sh to sign every file.")


if __name__ == "__main__":
    main()
