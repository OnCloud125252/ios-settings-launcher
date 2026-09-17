#!/usr/bin/env python3
"""Turn the merged JSON into one Markdown list."""

import json
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = json.load(open(os.path.join(ROOT, "data", "settings-urls.json"), encoding="utf-8"))

TAGS = {
    "fifi26": "F26",
    "fifi26b": "F26W",
    "fifi18": "F18",
    "fifi18b": "F18W",
    "fifi16": "F16",
    "fifi16b": "F16W",
    "fifi": "FIFI",
    "fifiman": "MAN",
    "fifidyld": "DYLD",
    "fifidep": "DEP",
    "mehdi": "MEHDI",
    "wesley": "WDG",
    "macstories": "MS",
    "gadgethacks": "GH",
    "dean": "DEAN",
    "tzmartin": "TZ",
    "macrumors": "MR",
}

SOURCE_TABLE = [
    ("F26", "FifiTheBulldog `versions/26.2/en/prefs.md`（iOS 26.2 系統檔匯出）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/26.2/en/prefs.md"),
    ("F26W", "FifiTheBulldog `versions/26.2/en/bridge.md`（Apple Watch）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/26.2/en/bridge.md"),
    ("F18", "FifiTheBulldog `versions/18.7.1/en/prefs.md`（iOS 18.7.1 系統檔匯出，內容最完整）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/18.7.1/en/prefs.md"),
    ("F18W", "FifiTheBulldog `versions/18.7.1/en/bridge.md`（Apple Watch）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/18.7.1/en/bridge.md"),
    ("F16", "FifiTheBulldog `versions/16.2/en/prefs.md`（iOS 16.2 系統檔匯出）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/16.2/en/prefs.md"),
    ("F16W", "FifiTheBulldog `versions/16.2/en/bridge.md`（Apple Watch）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/16.2/en/bridge.md"),
    ("FIFI", "FifiTheBulldog `settings-urls.md`（人工整理主清單）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/settings-urls.md"),
    ("MAN", "FifiTheBulldog PreferenceManifests 傾印 + `overrides/gaps.json`", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/preference-manifest-dump.txt"),
    ("DYLD", "FifiTheBulldog dyld_shared_cache 傾印", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/dyld-shared-cache-dump.txt"),
    ("DEP", "FifiTheBulldog `archive/deprecated.md`（已失效）", "https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/deprecated.md"),
    ("MEHDI", "1mehdifaraji/ios-settings-url-schemes", "https://github.com/1mehdifaraji/ios-settings-url-schemes"),
    ("WDG", "Wesley de Groot：iOS Settings URLs（更新至 iOS 26.1）", "https://wesleydegroot.nl/blog/iOS-settings-URLs"),
    ("MS", "MacStories：120+ Settings URLs（iOS 13.1）", "https://www.macstories.net/ios/a-comprehensive-guide-to-all-120-settings-urls-supported-by-ios-and-ipados-13-1/"),
    ("GH", "Gadget Hacks：iOS 17.2 新增 URL Scheme", "https://ios.gadgethacks.com/how-to/ios-17-2-includes-50-new-url-schemes-you-can-use-shortcuts-your-iphone-0385465/"),
    ("DEAN", "deanlyoung gist（iOS 10 時期，`prefs:` 對 `App-Prefs:`）", "https://gist.github.com/deanlyoung/368e274945a6929e0ea77c4eca345560"),
    ("TZ", "tzmartin gist（與 ahmadtech199 gist 內容相同，`app-settings:`）", "https://gist.github.com/tzmartin/b7019c22fc3152a0b2fe"),
    ("MR", "MacRumors 論壇討論串", "https://forums.macrumors.com/threads/manually-creating-settings-launchers-in-app-launching-apps.2037291/"),
]


def esc(text):
    return text.replace("|", "\\|")


def tag_list(sources):
    order = [t for t in TAGS.values()]
    tags = sorted({TAGS.get(s, s) for s in sources}, key=order.index)
    return " ".join(tags)


def note(row):
    notes = []
    if row["status"] == "deprecated":
        notes.append("已失效")
    elif row["status"] == "legacy":
        notes.append("舊版")
    extra = [s for s in row["schemes"] if s not in ("prefs", "bridge", "settings-navigation")]
    if "app-settings" in extra:
        notes.append("也見於 `app-settings:`")
    if "app-prefs" in extra:
        notes.append("也見於 `App-Prefs:`")
    if row["url"].endswith("/"):
        notes.append("結尾斜線來自系統檔")
    return "、".join(notes)


def section_key(name):
    if name == "(Settings root)":
        return (0, "")
    if name == "settings-navigation:":
        return (2, "")
    if name.startswith("watchOS bridge: "):
        return (3, name[len("watchOS bridge: "):].lower())
    return (1, name.lower())


groups = defaultdict(list)
for row in ROWS:
    groups[row["section"]].append(row)

sections = sorted(groups, key=section_key)
counts = Counter(s for row in ROWS for s in row["sources"])

lines = []
add = lines.append

total = len(ROWS)
prefs_total = sum(1 for r in ROWS if r["family"] == "prefs")
bridge_total = sum(1 for r in ROWS if r["family"] == "bridge")
nav_total = sum(1 for r in ROWS if r["family"] == "settings-navigation")

add("# iOS 設定 URL Scheme 合併清單")
add("")
add(f"這份清單合併 {len(SOURCE_TABLE)} 個來源，去除重複後共 **{total}** 條。")
add(f"其中 `prefs:` {prefs_total} 條，`bridge:`（Apple Watch）{bridge_total} 條，`settings-navigation://` {nav_total} 條。")
add("")
add("資料基準是 iOS 16.2、18.7.1、26.2 的系統檔匯出，再加上各社群清單與文章。")
add(f"其中 {sum(1 for r in ROWS if r['versions'])} 條有系統檔佐證，{sum(1 for r in ROWS if r['label_zh'])} 條有官方繁體中文名稱。")
add("中文名稱來自 FifiTheBulldog 的 `zh_TW` 版本匯出，就是 iOS 設定 App 裡的實際文字。")
add("")
add("---")
add("")
add("## 1. 用法規則")
add("")
add("1. `prefs:root=<頁面>` 開啟設定的一個主頁面。")
add("2. `&path=<子頁面>` 再往下一層。多層用 `/` 接，例如 `&path=Keyboard/KEYBOARDS`。")
add("3. `#<錨點>` 不換頁。它捲動到該頁的某一個項目，並且把它反白。")
add("4. 值要做百分號編碼。空白寫成 `%20`，`&` 寫成 `%26`，`:` 寫成 `%3A`。")
add("5. 第三方 App 的設定頁用它的 Bundle ID，例如 `prefs:root=com.adobe.lrmobilephone`。")
add("")
add("### 前綴要用哪一個")
add("")
add("| 前綴 | 用在哪裡 | 說明 |")
add("| --- | --- | --- |")
add("| `prefs:` | 捷徑 App、Widget | 現在最通用。本清單一律用這個前綴。 |")
add("| `App-Prefs:` | 從自己的 App 呼叫 | iOS 10 之後的寫法。參數和 `prefs:` 相同。 |")
add("| `app-settings:` | 很舊的 iOS | iOS 5.1 到 iOS 9 時期的寫法。現在多數無效。 |")
add("| `bridge:` | iPhone 上的「Watch」App | 開 Apple Watch 的設定頁。 |")
add("| `settings-navigation://` | iOS 18 之後 | Apple 新的內部跳轉協定，用 Bundle ID 當路徑。 |")
add("")
add("### 三個重要提醒")
add("")
add("1. 這些協定不是公開 API。App Store 審查可能因此退件。捷徑 App 內使用沒有這個問題。")
add("2. Apple 每一版都可能改掉路徑。清單裡的 `舊版` 與 `已失效` 標記要注意。")
add("3. 同一個頁面常有多條 URL。先試「系統檔驗證」欄有 26.2 或 18.7 的那一條。")
add("")
add("### 「系統檔驗證」欄怎麼看")
add("")
add("這一欄列出哪幾版 iOS 的系統檔裡有這條 URL。資料來自 FifiTheBulldog 的版本匯出。")
add("")
add("| 值 | 意思 |")
add("| --- | --- |")
add("| `26.2` | iOS 26.2 的匯出有這一條。 |")
add("| `18.7` | iOS 18.7.1 的匯出有這一條。這一版匯出最完整。 |")
add("| `16.2` | iOS 16.2 的匯出有這一條。 |")
add("| `—` | 只在社群清單或文章出現，沒有系統檔佐證。要自己測。 |")
add("")
add("注意：26.2 的匯出並不完整。它沒有輔助使用（Accessibility）的項目。")
add("所以 `18.7` 而沒有 `26.2`，不代表這條在 iOS 26 失效。")
add("")
add("---")
add("")
add("## 2. 來源代碼")
add("")
add("| 代碼 | 來源 | 收錄條數 |")
add("| --- | --- | ---: |")
for tag, name, url in SOURCE_TABLE:
    key = [k for k, v in TAGS.items() if v == tag][0]
    add(f"| `{tag}` | [{name}]({url}) | {counts.get(key, 0)} |")
add("")
add("---")
add("")
add("## 3. 目錄")
add("")
for name in sections:
    anchor = re.sub(r"[^\w\u4e00-\u9fff -]", "", name).strip().lower().replace(" ", "-")
    add(f"- [{name}](#{anchor})（{len(groups[name])}）")
add("")
add("---")
add("")
add("## 4. 清單")
add("")

for name in sections:
    rows = sorted(groups[name], key=lambda r: (r["url"].count("/") + r["url"].count("#"), r["url"].lower()))
    add(f"### {name}")
    add("")
    add("| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |")
    add("| --- | --- | --- | --- | --- | --- |")
    for row in rows:
        label = esc(row["label"]) if row["label"] else "—"
        label_zh = esc(row["label_zh"]) if row["label_zh"] else "—"
        versions = " · ".join(row["versions"]) if row["versions"] else "—"
        add(f"| {label_zh} | {label} | `{esc(row['url'])}` | {versions} | {tag_list(row['sources'])} | {note(row)} |")
    add("")

add("---")
add("")
add("## 5. 附錄 A：第三方 App 的 URL Scheme")
add("")
add("來源：[Tanaschita/ios-known-url-schemes-and-universal-links](https://github.com/Tanaschita/ios-known-url-schemes-and-universal-links)。")
add("這些是「開啟 App」的協定，不是設定頁面。全部有官方文件。")
add("")
add("| App | URL | 用途 |")
add("| --- | --- | --- |")
for app, url, usage in [
    ("App Store", "https://itunes.apple.com/us/app/apple-store/id375380948?mt=8", "開啟指定 App 的商店頁"),
    ("FaceTime", "facetime://user@example.com", "視訊通話"),
    ("FaceTime", "facetime-audio://user@example.com", "語音通話"),
    ("Google Chrome", "googlechrome://github.com", "用 Chrome 開 http 網址"),
    ("Google Chrome", "googlechromes://github.com", "用 Chrome 開 https 網址"),
    ("Google Maps", "comgooglemaps://?center=40.765819,-73.975866&zoom=14", "開啟指定座標與縮放"),
    ("Instagram", "instagram://app", "開啟 Instagram"),
    ("Instagram", "instagram://camera", "開啟相機"),
    ("Instagram", "instagram://user?username=USERNAME", "開啟指定使用者"),
    ("Mail", "mailto://foo@example.com?subject=test&body=test", "新增郵件，帶主旨與內文"),
    ("Apple Maps", "http://maps.apple.com/?q=vegan+restaurant", "搜尋地點"),
    ("Apple Maps", "http://maps.apple.com/?ll=30.269686,-97.759912", "開啟指定座標"),
    ("Phone", "tel://phonenumber", "撥號"),
    ("Spotify", "spotify://", "開啟 Spotify"),
    ("YouTube", "http://www.youtube.com/v/VIDEO_IDENTIFIER", "開啟指定影片"),
    ("WhatsApp", "whatsapp://send?text=Hello", "新對話，帶預填文字"),
]:
    add(f"| {app} | `{esc(url)}` | {usage} |")
add("")
add("---")
add("")
add("## 6. 附錄 B：沒有納入的來源")
add("")
add("| 來源 | 狀態 | 處理方式 |")
add("| --- | --- | --- |")
add("| [0xyza/ios-settings-urls](https://github.com/0xyza/ios-settings-urls) | 倉庫已不存在，GitHub 回傳 404 | 它本來就是 FifiTheBulldog 的分支。原始資料已全部收錄。 |")
add("| [Reddit r/shortcuts: An updated list of Settings URLs](https://www.reddit.com/r/shortcuts/comments/i9rjbh/an_updated_list_of_settings_urls/) | Reddit 擋自動抓取 | 這篇就是 FifiTheBulldog 清單的發布貼。內容已由 GitHub 倉庫收錄。 |")
add("| [Reddit r/shortcuts: iOS settings app URL schemes](https://www.reddit.com/r/shortcuts/comments/1qechhq/ios_settings_app_url_schemes/) | Reddit 擋自動抓取 | 未收錄。要看留言請自己開網頁。 |")
add("")

os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
out = os.path.join(ROOT, "docs", "settings-urls.md")
with open(out, "w", encoding="utf-8") as handle:
    handle.write("\n".join(lines))
print("wrote", out, len(lines), "lines")
