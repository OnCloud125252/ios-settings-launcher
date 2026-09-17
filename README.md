# iOS Settings Launcher

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: iOS 16+](https://img.shields.io/badge/Platform-iOS%2016%2B-black.svg)](https://www.apple.com/ios/)
[![Data: 2589 URLs](https://img.shields.io/badge/Data-2589%20URLs-green.svg)](data/settings-urls.json)

*Open any page of the iOS Settings app from a Shortcut. Search 2589 Settings URLs by keyword.*

## Overview

iOS can open one page of the Settings app with a URL, for example `prefs:root=WIFI`.
Apple does not document these URLs.
Many people have collected them, but every list is partial and most lists are old.

This project does two things.

1. It merges 17 public sources into one deduplicated list, with a note for each URL that says which iOS system files contain it.
2. It builds a Shortcut that holds the whole list, so you can search by keyword and open any Settings page.

## Install the Shortcut

Pick a file, AirDrop it to your iPhone, then tap "Add Shortcut".
You can also open the file on a Mac. iCloud then syncs the shortcut to your iPhone.

| File | Entries | Use it for |
| --- | ---: | --- |
| [`shortcuts/en/iOS Settings Launcher.shortcut`](shortcuts/en) | 1758 | Daily use on iPhone and iPad. |
| [`shortcuts/en/iOS Settings Launcher (Full).shortcut`](shortcuts/en) | 1878 | Adds pages with no name, and old pages. |
| [`shortcuts/en/Apple Watch Settings Launcher.shortcut`](shortcuts/en) | 711 | `bridge:` pages, opened from the Watch app. |

A Traditional Chinese build is in [`shortcuts/zh-TW/`](shortcuts/zh-TW).
It shows the official Apple Chinese name and the English name on every row, so you can search in either language.

The `unsigned/` folder holds the same shortcuts without an Apple signature.
Use those only if the signed file fails to import.
First turn on Settings → Shortcuts → Allow Untrusted Shortcuts.

## Use the Shortcut

1. Run the shortcut.
2. Type a keyword, for example `bluetooth`, `wifi`, or `screen time`.
3. Leave the field empty to list every page.
4. Pick a row. The Settings app opens that page.

The search reads the label and the URL.
So `root=CAMERA` works as a keyword too.
Top level pages sort first, so a search for `bluetooth` shows the main Bluetooth page first.

## How the Shortcut works

The Shortcuts app has no searchable picker.
"Choose from Menu" never had a search field.
"Choose from List" had one in iOS 13, and Apple removed it in iOS 14.
So this shortcut builds its own search from nine actions.

| # | Action | Job |
| --- | --- | --- |
| 1 | Text | Hold the whole list. One line per page: `label ⇢ url`. |
| 2 | Ask for Input | Read the keyword. |
| 3 | Replace Text | Turn every regex metacharacter into `.`, so any typed text stays a valid pattern. |
| 4 | Match Text | Keep the lines that match `(?im)^.*<keyword>.*$`. |
| 5 | Choose from List | Show the matching lines. |
| 6 | Split Text | Split the chosen line on ` ⇢ `. |
| 7 | Get Item from List | Take the last part, which is the URL. |
| 8 | URL | Cast the text to a URL. |
| 9 | Open URLs | Open the Settings page. |

Step 3 also helps the user. A keyword of `Wi-Fi` becomes `Wi.Fi`, which still matches `Wi-Fi`.

## The data

`data/settings-urls.json` is the source of truth. Each row has these fields.

| Field | Meaning |
| --- | --- |
| `url` | The URL, always written with the `prefs:`, `bridge:`, or `settings-navigation://` prefix. |
| `label` | English name, with the page path, for example `General → Keyboard → Keyboards`. |
| `label_zh` | Official Traditional Chinese name from Apple. Empty when Apple never shipped one. |
| `section` | Top level Settings section. |
| `family` | `prefs`, `bridge`, or `settings-navigation`. |
| `versions` | iOS versions whose system files contain this URL: `16.2`, `18.7`, `26.2`. |
| `sources` | Which upstream sources list this URL. |
| `status` | Empty, `legacy`, or `deprecated`. |

Totals: 2589 URLs. 1814 use `prefs:`, 711 use `bridge:`, and 64 use `settings-navigation://`.
2147 URLs appear in an Apple system file. 2170 URLs have an official Chinese name.

`docs/settings-urls.md` is the same data as a human readable list, in Traditional Chinese.

### A note on the version column

The iOS 26.2 export is not complete. It has no Accessibility pages.
So a URL marked `18.7` but not `26.2` is not dead. It only means the newer export does not cover it.

## URL syntax

1. `prefs:root=<page>` opens a main page.
2. `&path=<subpage>` goes one level deeper. Join more levels with `/`, for example `&path=Keyboard/KEYBOARDS`.
3. `#<anchor>` stays on the same page. It scrolls to one item and highlights it.
4. Percent encode the values. A space becomes `%20`, and `&` becomes `%26`.
5. For a third party app, use its bundle identifier, for example `prefs:root=com.adobe.lrmobilephone`.

| Prefix | Where it works |
| --- | --- |
| `prefs:` | Shortcuts and widgets. This project writes every URL this way. |
| `App-Prefs:` | Calls from inside your own app. Same parameters. |
| `app-settings:` | iOS 5.1 to iOS 9. Mostly dead now. |
| `bridge:` | The Watch app on iPhone. It opens Apple Watch settings. |
| `settings-navigation://` | iOS 18 and later. It uses a bundle identifier as the path. |

These URL schemes are not public API.
App Review can reject an app that uses them.
Use inside the Shortcuts app has no such problem.

## Repository layout

```
data/settings-urls.json      merged data, the source of truth
docs/settings-urls.md        the same list for humans (zh-TW)
docs/shortcut-guide.zh-TW.md shortcut guide in Traditional Chinese
scripts/fetch_sources.py     download every upstream source into raw/
scripts/merge.py             raw/ -> data/settings-urls.json
scripts/generate.py          data -> docs/settings-urls.md
scripts/build_shortcut.py    data -> unsigned .shortcut files
scripts/sign_all.sh          sign every .shortcut with the Apple service
scripts/verify_shortcut.py   check action wiring and simulate a search
shortcuts/<language>/        signed shortcuts, plus unsigned copies
```

## Build it yourself

You need macOS with the `shortcuts` command, and Python 3.9 or later.

```sh
make fetch      # download the upstream sources into raw/
make merge      # build data/settings-urls.json
make docs       # build docs/settings-urls.md
make shortcuts  # build unsigned .shortcut files for every language
make sign       # sign them
make verify     # check the result
```

`make all` runs everything except signing.

Signing calls an Apple service. That service fails often and returns HTTP 5xx.
`scripts/sign_all.sh` retries, and it never deletes a shortcut that is already signed.
A large file fails more often, and this is why the data ships as three shortcuts instead of one.

## Sources

The data is a merge of these public sources. Thanks to every author.

| Source | What it gives |
| --- | --- |
| [FifiTheBulldog/ios-settings-urls](https://github.com/FifiTheBulldog/ios-settings-urls) | The curated list, per version exports of Apple system files for many languages, and two raw dumps. This is the largest source. |
| [1mehdifaraji/ios-settings-url-schemes](https://github.com/1mehdifaraji/ios-settings-url-schemes) | A large hand made list with page names. |
| [Wesley de Groot: iOS Settings URLs](https://wesleydegroot.nl/blog/iOS-settings-URLs) | A list kept up to date, plus a method to extract new values. |
| [MacStories: A Comprehensive Guide to All 120+ Settings URLs](https://www.macstories.net/ios/a-comprehensive-guide-to-all-120-settings-urls-supported-by-ios-and-ipados-13-1/) | The iOS 13 research that started most later lists. |
| [Gadget Hacks: iOS 17.2 URL schemes](https://ios.gadgethacks.com/how-to/ios-17-2-includes-50-new-url-schemes-you-can-use-shortcuts-your-iphone-0385465/) | URLs added in iOS 17.2. |
| [deanlyoung gist](https://gist.github.com/deanlyoung/368e274945a6929e0ea77c4eca345560) | The iOS 10 era list. It shows `prefs:` against `App-Prefs:`. |
| [tzmartin gist](https://gist.github.com/tzmartin/b7019c22fc3152a0b2fe) | The old `app-settings:` list. |
| [MacRumors forum thread](https://forums.macrumors.com/threads/manually-creating-settings-launchers-in-app-launching-apps.2037291/) | Community tests of old URLs. |
| [Tanaschita/ios-known-url-schemes-and-universal-links](https://github.com/Tanaschita/ios-known-url-schemes-and-universal-links) | Third party app URL schemes, used in the appendix. |

Two listed sources are not included.
The `0xyza/ios-settings-urls` repository is gone.
Reddit blocks automated reading, so the two `r/shortcuts` threads were not read. One of them is the post that announces the FifiTheBulldog list, and that data is included through GitHub.

## License

The code in this repository uses the MIT License. See [LICENSE](LICENSE).

The data is a compilation of facts from the public sources above.
None of those sources states a license.
The raw pages are not stored here. `scripts/fetch_sources.py` downloads them when you build.
If you are an author of a source and you want a change, open an issue.
