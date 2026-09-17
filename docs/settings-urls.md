# iOS 設定 URL Scheme 合併清單

這份清單合併 17 個來源，去除重複後共 **2589** 條。
其中 `prefs:` 1814 條，`bridge:`（Apple Watch）711 條，`settings-navigation://` 64 條。

資料基準是 iOS 16.2、18.7.1、26.2 的系統檔匯出，再加上各社群清單與文章。
其中 2147 條有系統檔佐證，2170 條有官方繁體中文名稱。
中文名稱來自 FifiTheBulldog 的 `zh_TW` 版本匯出，就是 iOS 設定 App 裡的實際文字。

---

## 1. 用法規則

1. `prefs:root=<頁面>` 開啟設定的一個主頁面。
2. `&path=<子頁面>` 再往下一層。多層用 `/` 接，例如 `&path=Keyboard/KEYBOARDS`。
3. `#<錨點>` 不換頁。它捲動到該頁的某一個項目，並且把它反白。
4. 值要做百分號編碼。空白寫成 `%20`，`&` 寫成 `%26`，`:` 寫成 `%3A`。
5. 第三方 App 的設定頁用它的 Bundle ID，例如 `prefs:root=com.adobe.lrmobilephone`。

### 前綴要用哪一個

| 前綴 | 用在哪裡 | 說明 |
| --- | --- | --- |
| `prefs:` | 捷徑 App、Widget | 現在最通用。本清單一律用這個前綴。 |
| `App-Prefs:` | 從自己的 App 呼叫 | iOS 10 之後的寫法。參數和 `prefs:` 相同。 |
| `app-settings:` | 很舊的 iOS | iOS 5.1 到 iOS 9 時期的寫法。現在多數無效。 |
| `bridge:` | iPhone 上的「Watch」App | 開 Apple Watch 的設定頁。 |
| `settings-navigation://` | iOS 18 之後 | Apple 新的內部跳轉協定，用 Bundle ID 當路徑。 |

### 三個重要提醒

1. 這些協定不是公開 API。App Store 審查可能因此退件。捷徑 App 內使用沒有這個問題。
2. Apple 每一版都可能改掉路徑。清單裡的 `舊版` 與 `已失效` 標記要注意。
3. 同一個頁面常有多條 URL。先試「系統檔驗證」欄有 26.2 或 18.7 的那一條。

### 「系統檔驗證」欄怎麼看

這一欄列出哪幾版 iOS 的系統檔裡有這條 URL。資料來自 FifiTheBulldog 的版本匯出。

| 值 | 意思 |
| --- | --- |
| `26.2` | iOS 26.2 的匯出有這一條。 |
| `18.7` | iOS 18.7.1 的匯出有這一條。這一版匯出最完整。 |
| `16.2` | iOS 16.2 的匯出有這一條。 |
| `—` | 只在社群清單或文章出現，沒有系統檔佐證。要自己測。 |

注意：26.2 的匯出並不完整。它沒有輔助使用（Accessibility）的項目。
所以 `18.7` 而沒有 `26.2`，不代表這條在 iOS 26 失效。

---

## 2. 來源代碼

| 代碼 | 來源 | 收錄條數 |
| --- | --- | ---: |
| `F26` | [FifiTheBulldog `versions/26.2/en/prefs.md`（iOS 26.2 系統檔匯出）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/26.2/en/prefs.md) | 488 |
| `F26W` | [FifiTheBulldog `versions/26.2/en/bridge.md`（Apple Watch）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/26.2/en/bridge.md) | 518 |
| `F18` | [FifiTheBulldog `versions/18.7.1/en/prefs.md`（iOS 18.7.1 系統檔匯出，內容最完整）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/18.7.1/en/prefs.md) | 1262 |
| `F18W` | [FifiTheBulldog `versions/18.7.1/en/bridge.md`（Apple Watch）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/18.7.1/en/bridge.md) | 425 |
| `F16` | [FifiTheBulldog `versions/16.2/en/prefs.md`（iOS 16.2 系統檔匯出）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/16.2/en/prefs.md) | 826 |
| `F16W` | [FifiTheBulldog `versions/16.2/en/bridge.md`（Apple Watch）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/versions/16.2/en/bridge.md) | 410 |
| `FIFI` | [FifiTheBulldog `settings-urls.md`（人工整理主清單）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/settings-urls.md) | 388 |
| `MAN` | [FifiTheBulldog PreferenceManifests 傾印 + `overrides/gaps.json`](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/preference-manifest-dump.txt) | 1239 |
| `DYLD` | [FifiTheBulldog dyld_shared_cache 傾印](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/dyld-shared-cache-dump.txt) | 160 |
| `DEP` | [FifiTheBulldog `archive/deprecated.md`（已失效）](https://github.com/FifiTheBulldog/ios-settings-urls/blob/master/archive/deprecated.md) | 4 |
| `MEHDI` | [1mehdifaraji/ios-settings-url-schemes](https://github.com/1mehdifaraji/ios-settings-url-schemes) | 586 |
| `WDG` | [Wesley de Groot：iOS Settings URLs（更新至 iOS 26.1）](https://wesleydegroot.nl/blog/iOS-settings-URLs) | 581 |
| `MS` | [MacStories：120+ Settings URLs（iOS 13.1）](https://www.macstories.net/ios/a-comprehensive-guide-to-all-120-settings-urls-supported-by-ios-and-ipados-13-1/) | 134 |
| `GH` | [Gadget Hacks：iOS 17.2 新增 URL Scheme](https://ios.gadgethacks.com/how-to/ios-17-2-includes-50-new-url-schemes-you-can-use-shortcuts-your-iphone-0385465/) | 62 |
| `DEAN` | [deanlyoung gist（iOS 10 時期，`prefs:` 對 `App-Prefs:`）](https://gist.github.com/deanlyoung/368e274945a6929e0ea77c4eca345560) | 54 |
| `TZ` | [tzmartin gist（與 ahmadtech199 gist 內容相同，`app-settings:`）](https://gist.github.com/tzmartin/b7019c22fc3152a0b2fe) | 41 |
| `MR` | [MacRumors 論壇討論串](https://forums.macrumors.com/threads/manually-creating-settings-launchers-in-app-launching-apps.2037291/) | 64 |

---

## 3. 目錄

- [(Settings root)](#settings-root)（2）
- [Accessibility](#accessibility)（1061）
- [Account Settings](#account-settings)（1）
- [Action Button](#action-button)（1）
- [Airplane Mode](#airplane-mode)（4）
- [App Store](#app-store)（6）
- [Apple Account](#apple-account)（71）
- [Apple Pencil](#apple-pencil)（3）
- [Battery](#battery)（4）
- [Bluetooth](#bluetooth)（1）
- [Books](#books)（25）
- [Calendar](#calendar)（13）
- [Camera](#camera)（10）
- [Carrier](#carrier)（1）
- [Cellular](#cellular)（12）
- [com.adobe.lrmobilephone](#comadobelrmobilephone)（1）
- [Compass](#compass)（2）
- [Contacts](#contacts)（10）
- [Control Center](#control-center)（3）
- [Developer](#developer)（44）
- [Display & Brightness](#display--brightness)（24）
- [Emergency SOS](#emergency-sos)（15）
- [Exposure Notifications](#exposure-notifications)（1）
- [Face ID & Passcode](#face-id--passcode)（13）
- [FACEBOOK](#facebook)（1）
- [FaceTime](#facetime)（2）
- [FLICKR](#flickr)（1）
- [Focus](#focus)（9）
- [FollowUpList_](#followuplist_)（1）
- [Freeform](#freeform)（1）
- [Game Center](#game-center)（3）
- [General](#general)（103）
- [Health Data](#health-data)（2）
- [HealthKit](#healthkit)（1）
- [Home](#home)（1）
- [Home Screen](#home-screen)（3）
- [Home Screen & App Library](#home-screen--app-library)（13）
- [ICLOUD_ID](#icloud_id)（1）
- [INTERNAL_SETTINGS](#internal_settings)（6）
- [Journal](#journal)（2）
- [Location Services](#location-services)（1）
- [Mail](#mail)（26）
- [Maps](#maps)（31）
- [Measure](#measure)（5）
- [Messages](#messages)（3）
- [Multitasking & Gestures](#multitasking--gestures)（15）
- [Music](#music)（21）
- [News](#news)（7）
- [Nike iPod](#nike-ipod)（1）
- [Notes](#notes)（12）
- [Notifications](#notifications)（6）
- [OnsiteProfileInstall](#onsiteprofileinstall)（1）
- [Passcode](#passcode)（1）
- [Passwords](#passwords)（2）
- [Passwords & Accounts](#passwords--accounts)（14）
- [Pearl](#pearl)（1）
- [Personal Hotspot](#personal-hotspot)（3）
- [Phone](#phone)（21）
- [Photos](#photos)（11）
- [Podcasts](#podcasts)（2）
- [Privacy & Security](#privacy--security)（29）
- [Reminders](#reminders)（6）
- [Safari](#safari)（21）
- [Screen Time](#screen-time)（14）
- [Shortcuts](#shortcuts)（4）
- [Siri](#siri)（13）
- [Sounds & Haptics](#sounds--haptics)（22）
- [StandBy](#standby)（1）
- [Stocks](#stocks)（3）
- [TOUCHID_PASSCODE](#touchid_passcode)（3）
- [Translate](#translate)（2）
- [TV](#tv)（8）
- [TV Provider](#tv-provider)（1）
- [Twitter](#twitter)（1）
- [Video](#video)（1）
- [VIMEO](#vimeo)（1）
- [Voice Memos](#voice-memos)（5）
- [VPN](#vpn)（2）
- [Wallet & Apple Pay](#wallet--apple-pay)（8）
- [Wallpaper](#wallpaper)（1）
- [Weather](#weather)（1）
- [WEIBO](#weibo)（1）
- [Wi-Fi](#wi-fi)（4）
- [settings-navigation:](#settings-navigation)（64）
- [watchOS bridge: (Settings root)](#watchos-bridge-settings-root)（1）
- [watchOS bridge: Accessibility](#watchos-bridge-accessibility)（110）
- [watchOS bridge: Action Button](#watchos-bridge-action-button)（10）
- [watchOS bridge: Activity](#watchos-bridge-activity)（13）
- [watchOS bridge: App Store](#watchos-bridge-app-store)（3）
- [watchOS bridge: App View](#watchos-bridge-app-view)（1）
- [watchOS bridge: Audiobooks](#watchos-bridge-audiobooks)（2）
- [watchOS bridge: Blood Oxygen](#watchos-bridge-blood-oxygen)（1）
- [watchOS bridge: Calendar](#watchos-bridge-calendar)（11）
- [watchOS bridge: Carrier Settings](#watchos-bridge-carrier-settings)（1）
- [watchOS bridge: Cellular](#watchos-bridge-cellular)（1）
- [watchOS bridge: Clock](#watchos-bridge-clock)（20）
- [watchOS bridge: com.apple.DeepBreathingSettings](#watchos-bridge-comappledeepbreathingsettings)（4）
- [watchOS bridge: com.nike.nikeplus-gps](#watchos-bridge-comnikenikeplus-gps)（2）
- [watchOS bridge: Complications](#watchos-bridge-complications)（1）
- [watchOS bridge: Contacts](#watchos-bridge-contacts)（18）
- [watchOS bridge: Control Center](#watchos-bridge-control-center)（2）
- [watchOS bridge: Depth](#watchos-bridge-depth)（1）
- [watchOS bridge: Display & Brightness](#watchos-bridge-display--brightness)（78）
- [watchOS bridge: Dock](#watchos-bridge-dock)（8）
- [watchOS bridge: Emergency SOS](#watchos-bridge-emergency-sos)（1）
- [watchOS bridge: Find My Apple Watch](#watchos-bridge-find-my-apple-watch)（2）
- [watchOS bridge: FollowUpList_](#watchos-bridge-followuplist_)（1）
- [watchOS bridge: General](#watchos-bridge-general)（98）
- [watchOS bridge: Gestures](#watchos-bridge-gestures)（14）
- [watchOS bridge: Handwashing](#watchos-bridge-handwashing)（6）
- [watchOS bridge: Health](#watchos-bridge-health)（1）
- [watchOS bridge: Heart](#watchos-bridge-heart)（26）
- [watchOS bridge: Mail](#watchos-bridge-mail)（17）
- [watchOS bridge: Mail & Calendar](#watchos-bridge-mail--calendar)（8）
- [watchOS bridge: Messages](#watchos-bridge-messages)（14）
- [watchOS bridge: Mindfulness](#watchos-bridge-mindfulness)（22）
- [watchOS bridge: Nike Run Club](#watchos-bridge-nike-run-club)（2）
- [watchOS bridge: Noise](#watchos-bridge-noise)（11）
- [watchOS bridge: NOTIFICATIONS_ID](#watchos-bridge-notifications_id)（1）
- [watchOS bridge: Phone](#watchos-bridge-phone)（5）
- [watchOS bridge: Photos](#watchos-bridge-photos)（15）
- [watchOS bridge: Podcasts](#watchos-bridge-podcasts)（1）
- [watchOS bridge: Privacy](#watchos-bridge-privacy)（15）
- [watchOS bridge: ROOT](#watchos-bridge-root)（2）
- [watchOS bridge: Schooltime](#watchos-bridge-schooltime)（2）
- [watchOS bridge: Screen Time](#watchos-bridge-screen-time)（1）
- [watchOS bridge: Selected Photo Album](#watchos-bridge-selected-photo-album)（1）
- [watchOS bridge: Siri](#watchos-bridge-siri)（25）
- [watchOS bridge: Sleep](#watchos-bridge-sleep)（2）
- [watchOS bridge: Smart Stack](#watchos-bridge-smart-stack)（1）
- [watchOS bridge: Sounds & Haptics](#watchos-bridge-sounds--haptics)（29）
- [watchOS bridge: Stocks](#watchos-bridge-stocks)（13）
- [watchOS bridge: Storage Limit](#watchos-bridge-storage-limit)（3）
- [watchOS bridge: Tips](#watchos-bridge-tips)（5）
- [watchOS bridge: Turn Alerts](#watchos-bridge-turn-alerts)（9）
- [watchOS bridge: Turn Passcode Off](#watchos-bridge-turn-passcode-off)（9）
- [watchOS bridge: Walkie-Talkie](#watchos-bridge-walkie-talkie)（6）
- [watchOS bridge: Wallet & Apple Pay](#watchos-bridge-wallet--apple-pay)（17）
- [watchOS bridge: Weather](#watchos-bridge-weather)（4）
- [watchOS bridge: Workout](#watchos-bridge-workout)（34）

---

## 4. 清單

### (Settings root)

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Settings | `prefs:` | — | MAN DYLD MEHDI DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | Settings | `prefs:root=` | — | MAN DYLD MEHDI |  |

### Accessibility

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 輔助使用 | Accessibility | `prefs:root=ACCESSIBILITY` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG MS |  |
| 輔助使用 → 語音捷徑 | Accessibility → Vocal Shortcuts | `prefs:root=ACCESSIBILITY&path=ADAPTIVE_VOICE_SHORTCUTS_TITLE` | 18.7 | F18 |  |
| 輔助使用 → AirPods | Accessibility → AirPods | `prefs:root=ACCESSIBILITY&path=AIRPODS` | 18.7 | F18 MAN |  |
| 輔助使用 → 個別App設定 | Accessibility → Per-App Settings | `prefs:root=ACCESSIBILITY&path=APP_AX_SETTINGS_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → Apple TV Remote | `prefs:root=ACCESSIBILITY&path=Apple%20TV%20Remote` | — | FIFI WDG |  |
| 輔助使用 → Apple TV遙控器 | Accessibility → Apple TV Remote | `prefs:root=ACCESSIBILITY&path=APPLE_TV_REMOTE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → Apple Watch鏡像輸出 | Accessibility → Apple Watch Mirroring | `prefs:root=ACCESSIBILITY&path=APPLE_WATCH_REMOTE_SCREEN` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 音訊與視覺 | Accessibility → Audio & Visual | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 相機控制 | Accessibility → Camera Control | `prefs:root=ACCESSIBILITY&path=CAMERA_CONTROL` | 18.7 | F18 MAN |  |
| 輔助使用 → 自訂輔助取用 | Accessibility → Assistive Access | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 語音控制 | Accessibility → Voice Control | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 輔助使用 → 控制附近裝置 | Accessibility → Control Nearby Devices | `prefs:root=ACCESSIBILITY&path=CONTROL_NEARBY_DEVICES` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 口述影像 | Accessibility → Audio Descriptions | `prefs:root=ACCESSIBILITY&path=DESCRIPTIVE_VIDEO` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 顯示與文字大小 | Accessibility → Display & Text Size | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 眼睛輸入 | Accessibility → Eye Input | `prefs:root=ACCESSIBILITY&path=DOMINANT_EYE` | 18.7 | F18 |  |
| — | Accessibility → Face ID & Attention | `prefs:root=ACCESSIBILITY&path=Face%20ID%20%26%20Attention` | — | DEP | 已失效 |
| 輔助使用 → Face ID與螢幕注視 | Accessibility → Face ID & Attention | `prefs:root=ACCESSIBILITY&path=FACE_ID` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 | Accessibility → Guided Access | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 輔助使用 → 音樂觸覺回饋 | Accessibility → Music Haptics | `prefs:root=ACCESSIBILITY&path=HAPTIC_MUSIC` | 18.7 | F18 |  |
| 輔助使用 → 助聽裝置 | Accessibility → Hearing Devices | `prefs:root=ACCESSIBILITY&path=HEARING_AID_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 聆聽控制中心 | Accessibility → Hearing Control Center | `prefs:root=ACCESSIBILITY&path=HEARING_CONTROL_CENTER` | 18.7 | F18 |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID | Accessibility → Side Button | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 懸浮文字 | Accessibility → Hover Text | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 鍵盤與輸入 | Accessibility → Keyboards & Typing | `prefs:root=ACCESSIBILITY&path=KEYBOARDS` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 即時語音 | Accessibility → Live Speech | `prefs:root=ACCESSIBILITY&path=LIVE_SPEECH_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 即時字幕 | Accessibility → Live Captions | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION` | 18.7 | F18 MAN |  |
| — | Accessibility → Magnifier | `prefs:root=ACCESSIBILITY&path=MAGNIFIER_TITLE` | — | FIFI MAN MEHDI WDG |  |
| 輔助使用 → 動態效果 | Accessibility → Motion | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 眼球追蹤 | Accessibility → Eye Tracking | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking` | 18.7 | F18 MAN |  |
| 輔助使用 → 個人聲音 | Accessibility → Personal Voice | `prefs:root=ACCESSIBILITY&path=PERSONAL_VOICE_TITLE` | 18.7 | F18 |  |
| 輔助使用 → RTT \| RTT/TTY \| TTY | Accessibility → RTT \| RTT/TTY \| TTY | `prefs:root=ACCESSIBILITY&path=RTT` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 切換控制 | Accessibility → Switch Control | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 輔助使用 → Siri | Accessibility → Siri | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 聲音辨識 | Accessibility → Sound Recognition | `prefs:root=ACCESSIBILITY&path=SOUND_RECOGNITION_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 輔助使用 → 語音內容 | Accessibility → Spoken Content | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 字幕與隱藏式字幕 | Accessibility → Subtitles & Captioning | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 互動 \| 觸控 | Accessibility → Interaction \| Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 輔助使用快速鍵 | Accessibility → Accessibility Shortcut | `prefs:root=ACCESSIBILITY&path=TRIPLE_CLICK_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 輔助使用 → 旁白 | Accessibility → VoiceOver | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 輔助使用 → 縮放 | Accessibility → Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 一般 | Accessibility → General | `prefs:root=ACCESSIBILITY#GENERAL_HEADING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 聽力 | Accessibility → Hearing | `prefs:root=ACCESSIBILITY#HEARING_HEADING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 身體動作 | Accessibility → Physical and Motor | `prefs:root=ACCESSIBILITY#MOBILITY_HEADING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 視覺 | Accessibility → Vision | `prefs:root=ACCESSIBILITY#VISION` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音捷徑 → 設定語音捷徑 | Accessibility → Vocal Shortcuts → Set Up Vocal Shortcuts | `prefs:root=ACCESSIBILITY&path=ADAPTIVE_VOICE_SHORTCUTS_TITLE#AVS_SET_UP_BUTTON_TITLE` | 18.7 | F18 |  |
| 輔助使用 → AirPods → 按住持續時間 | Accessibility → AirPods → Press and Hold Duration | `prefs:root=ACCESSIBILITY&path=AIRPODS#HoldGroup` | 18.7 | F18 |  |
| 輔助使用 → AirPods → iPhone音訊與視覺設定 | Accessibility → AirPods → iPhone Audio & Visual Settings | `prefs:root=ACCESSIBILITY&path=AIRPODS#PERSONAL_AUDIO_AIRPODS_BUTTON` | 18.7 | F18 |  |
| 輔助使用 → AirPods → 隨著iPhone移動 | Accessibility → AirPods → Follow iPhone | `prefs:root=ACCESSIBILITY&path=AIRPODS#SPATIAL_AUDIO_SWITCH` | 18.7 | F18 |  |
| 輔助使用 → AirPods → 按下速度 | Accessibility → AirPods → Press Speed | `prefs:root=ACCESSIBILITY&path=AIRPODS#TapGroup` | 18.7 | F18 |  |
| 輔助使用 → AirPods → 提示聲音量 | Accessibility → AirPods → Tone Volume | `prefs:root=ACCESSIBILITY&path=AIRPODS#TONE_VOLUME` | 18.7 | F18 |  |
| 輔助使用 → 個別App設定 → 加入App | Accessibility → Per-App Settings → Add App | `prefs:root=ACCESSIBILITY&path=APP_AX_SETTINGS_TITLE#AX_ADD_BUTTON_IDENTIFIER` | 18.7 | F18 |  |
| 輔助使用 → 個別App設定 → 顯示隱藏的App | Accessibility → Per-App Settings → Show Hidden Apps | `prefs:root=ACCESSIBILITY&path=APP_AX_SETTINGS_TITLE#PROTECTED_APPS_SHOW_HIDDEN_TITLE` | 18.7 | F18 |  |
| 輔助使用 → Apple TV遙控器 → 直播電視按鈕 | Accessibility → Apple TV Remote → Live TV Buttons | `prefs:root=ACCESSIBILITY&path=APPLE_TV_REMOTE#AppleTVLiveTVButtons` | 18.7 | F18 |  |
| 輔助使用 → Apple TV遙控器 → 方向按鈕 | Accessibility → Apple TV Remote → Directional Buttons | `prefs:root=ACCESSIBILITY&path=APPLE_TV_REMOTE#AppleTVSimpleGestures` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 | Accessibility → Audio & Visual → Background Sounds | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXCSEnableSpecID` | 16.2 | F16 |  |
| 輔助使用 → 音訊與視覺 → 耳機通知 | Accessibility → Audio & Visual → Headphone Notifications | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXHeadphoneNotificationsSpecID` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 永遠顯示音量控制 | Accessibility → Audio & Visual → Always Show Volume Control | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXPAAlwaysShowVolumeControlSpecID` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 音訊 | Accessibility → Audio & Visual → Audio | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXPAAudioGroupSpecID` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 平衡 | Accessibility → Audio & Visual → Balance | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXPABalanceSpecID` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 耳機調節 | Accessibility → Audio & Visual → Headphone Accommodations | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXPAEnableSpecID` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 單聲道音訊 | Accessibility → Audio & Visual → Mono Audio | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXPAMonoSpecID` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 電話降噪 | Accessibility → Audio & Visual → Phone Noise Cancellation | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#AXPANoiseSpecID` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 加入語音隔離 | Accessibility → Audio & Visual → Add Voice Isolation | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#ExtendedVoiceIsolationSpecID` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 收到提示時閃爍LED | Accessibility → Audio & Visual → LED Flash for Alerts | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#LED_FLASH` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 左右立體聲平衡 | Accessibility → Audio & Visual → Left-Right Stereo Balance | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#LeftRightBalance` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 音訊與視覺 → 音效 | Accessibility → Audio & Visual → Sound Effects | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#SOUND_EFFECTS_PREFERENCE` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 開機與關機聲音 | Accessibility → Audio & Visual → Power On & Off Sounds | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#StartupSound` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 音訊與視覺 → 視覺 | Accessibility → Audio & Visual → Visual | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE#VISUAL_HEADING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 | Accessibility → Audio & Visual → Background Sounds | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID` | 18.7 | F18 MAN |  |
| 輔助使用 → 音訊與視覺 → 耳機調節 | Accessibility → Audio & Visual → Headphone Accommodations | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXPAEnableSpecID` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 收到提示時閃爍LED | Accessibility → Audio & Visual → LED Flash for Alerts | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/LED_FLASH` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 在通話中加入音訊 | Accessibility → Audio & Visual → Add Audio in Calls | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/MIX_TO_UPLINK` | 18.7 | F18 |  |
| 輔助使用 → 相機控制 → 相機控制 | Accessibility → Camera Control → Camera Control | `prefs:root=ACCESSIBILITY&path=CAMERA_CONTROL#CAMERA_CONTROL_SWITCH` | 18.7 | F18 |  |
| 輔助使用 → 相機控制 → 輕按 | Accessibility → Camera Control → Light-Press | `prefs:root=ACCESSIBILITY&path=CAMERA_CONTROL#LIGHT_PRESS` | 18.7 | F18 |  |
| 輔助使用 → 相機控制 → 輕按力度 | Accessibility → Camera Control → Light-Press Force | `prefs:root=ACCESSIBILITY&path=CAMERA_CONTROL#LIGHT_PRESS_FORCE` | 18.7 | F18 |  |
| 輔助使用 → 相機控制 → 輕按兩下速度 | Accessibility → Camera Control → Double Light-Press Speed | `prefs:root=ACCESSIBILITY&path=CAMERA_CONTROL#SENSITIVITY` | 18.7 | F18 |  |
| 輔助使用 → 相機控制 → 滑動 | Accessibility → Camera Control → Swipe | `prefs:root=ACCESSIBILITY&path=CAMERA_CONTROL#SWIPE` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 允許Siri | Accessibility → Assistive Access → Allow Siri | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#AllowSiri` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 應用程式 | Accessibility → Assistive Access → Applications | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#Applications` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 開始自訂輔助取用 | Accessibility → Assistive Access → Start Assistive Access | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#ClarityUIStart` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 選項 | Accessibility → Assistive Access → Options | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#Options` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 設定自訂輔助取用 | Accessibility → Assistive Access → Set Up Assistive Access | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#SetUpClarityUISpecifier` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 在主畫面上顯示電池電量 | Accessibility → Assistive Access → Show Battery Level on Home Screen | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#ShowBattery` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 顯示通知標記 | Accessibility → Assistive Access → Show Notification Badges | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#ShowNotification` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 在鎖定畫面上顯示時間 | Accessibility → Assistive Access → Show Time on Lock Screen | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#ShowTime` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 允許音量按鈕 | Accessibility → Assistive Access → Allow Volume Buttons | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE#VolumeButtons` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 密碼設定 | Accessibility → Assistive Access → Passcode Settings | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE/PasscodeSettings` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 背景圖片 | Accessibility → Assistive Access → Wallpaper | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE/Wallpaper` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 覆疊 | Accessibility → Voice Control → Overlay | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#ALWAYS_SHOW_OVERLAY` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 連續覆疊 | Accessibility → Voice Control → Continuous Overlay | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#ALWAYS_SHOW_OVERLAY_GROUP_TITLE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 螢幕注視感知 | Accessibility → Voice Control → Attention Aware | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#ATTENTION_AWARE_ACTION` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 語言 | Accessibility → Voice Control → Language | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#COMMAND_AND_CONTROL_LANGUAGE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 打開語音控制教學指南 | Accessibility → Voice Control → Open Voice Control Tutorial | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#COMMAND_AND_CONTROL_LAUNCH_ONBOARDING` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 自訂指令 | Accessibility → Voice Control → Customize Commands | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#CUSTOMIZE_COMMANDS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 播放聲音 | Accessibility → Voice Control → Play Sound | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#PLAY_SOUND_RESPONSE_TITLE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 設定語音控制 | Accessibility → Voice Control → Set Up Voice Control | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#SETUP_COMMAND_AND_CONTROL` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 顯示確認 | Accessibility → Voice Control → Show Confirmation | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#SHOW_TEXT_RESPONSE_TITLE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 指令回饋 | Accessibility → Voice Control → Command Feedback | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#UPON_COMMAND_RECOGNITION_TITLE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 顯示提示 | Accessibility → Voice Control → Show Hints | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#USER_HINTS_SHOW_HINTS_TITLE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 詞彙 | Accessibility → Voice Control → Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle#VOCABULARY` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 覆疊 | Accessibility → Voice Control → Overlay | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/ALWAYS_SHOW_OVERLAY` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 語音控制 → 指令 | Accessibility → Voice Control → Commands | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 語言 | Accessibility → Voice Control → Language | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_LANGUAGE` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 詞彙 | Accessibility → Voice Control → Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY` | 18.7 | F18 MAN |  |
| — | Accessibility → Voice Control → Customize Commands | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/CUSTOMIZE_COMMANDS` | — | FIFI MAN DYLD WDG |  |
| — | Accessibility → Voice Control → Language | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/LANGUAGE` | — | FIFI WDG |  |
| — | Accessibility → Voice Control → Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/VOCABULARY` | — | FIFI MAN DYLD WDG |  |
| 輔助使用 → 控制附近裝置 → 控制附近裝置 | Accessibility → Control Nearby Devices → Control Nearby Devices | `prefs:root=ACCESSIBILITY&path=CONTROL_NEARBY_DEVICES#CONTROL_NEARBY_DEVICES` | 18.7 | F18 |  |
| 輔助使用 → 口述影像 → 口述影像 | Accessibility → Audio Descriptions → Audio Descriptions | `prefs:root=ACCESSIBILITY&path=DESCRIPTIVE_VIDEO#DESCRIPTIVE_VIDEO_SETTING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 自動調整亮度 | Accessibility → Display & Text Size → Auto-Brightness | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#AUTO_BRIGHTNESS` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 自動對齊螢幕 | Accessibility → Display & Text Size → Align Displays Automatically | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#AUTO_IPD_TEXT` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → 按鈕形狀 | Accessibility → Display & Text Size → Button Shapes | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#BUTTON_SHAPES` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 經典反相 | Accessibility → Display & Text Size → Classic Invert | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#CLASSIC_INVERT` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 不以顏色來區分 | Accessibility → Display & Text Size → Differentiate Without Color | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#DIFFERENTIATE_WITHOUT_COLOR` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 顏色濾鏡 | Accessibility → Display & Text Size → Display & Text Size → Color Filters | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#DISPLAY_FILTER_COLOR` | — | MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 粗體文字 | Accessibility → Display & Text Size → Bold Text | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#ENHANCE_TEXT_LEGIBILITY` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 增加注視狀態 | Accessibility → Display & Text Size → Increase Focus State | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#INCREASE_FOCUS_STATE_TEXT` | 18.7 | F18 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#INVERT_COLORS` | — | MAN DYLD |  |
| 輔助使用 → 顯示與文字大小 → 放大文字 | Accessibility → Display & Text Size → Larger Text | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#LARGER_TEXT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 開啟/關閉標籤 | Accessibility → Display & Text Size → On/Off Labels | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#OnOffLabels` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 橫書文字優先 | Accessibility → Display & Text Size → Prefer Horizontal Text | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#PREFER_HORIZONTAL_TEXT` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → 減少透明度 | Accessibility → Display & Text Size → Reduce Transparency | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#REDUCE_TRANSPARENCY` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 智慧型反相 | Accessibility → Display & Text Size → Smart Invert | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#SMART_INVERT` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 忽略眼球運動以穩定影像 | Accessibility → Display & Text Size → Ignore Eye Movements to Stabilize | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#STATIC_FOVEATION_TEXT` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → 增加對比 | Accessibility → Display & Text Size → Increase Contrast | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#TEXT_COLORS_DARKEN` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 降低白點值 | Accessibility → Display & Text Size → Reduce White Point | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT#WHITE_POINT` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | Accessibility → Display & Text Size → Color Filters | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/Color%20Filters` | — | DEP | 已失效 |
| 輔助使用 → 顯示與文字大小 → 顏色濾鏡 | Accessibility → Display & Text Size → Color Filters | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/DISPLAY_FILTER_COLOR` | 16.2 · 18.7 | F18 F16 FIFI WDG |  |
| — | Accessibility → Display & Text Size → Larger Text | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/Larger%20Text` | — | FIFI WDG |  |
| 輔助使用 → 顯示與文字大小 → 放大文字 | Accessibility → Display & Text Size → Larger Text | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/LARGER_TEXT` | 18.7 | F18 |  |
| 輔助使用 → Face ID與螢幕注視 → 螢幕注視感知功能 | Accessibility → Face ID & Attention → Attention Aware Features | `prefs:root=ACCESSIBILITY&path=FACE_ID#AttentionAware` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → Face ID與螢幕注視 → 成功認證時播放觸覺回饋 | Accessibility → Face ID & Attention → Haptic on Successful Authentication | `prefs:root=ACCESSIBILITY&path=FACE_ID#PearlSuccessHaptic` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → Face ID與螢幕注視 → 觸覺回饋 | Accessibility → Face ID & Attention → Haptics | `prefs:root=ACCESSIBILITY&path=FACE_ID#PearlSuccessHapticGroup` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → Face ID與螢幕注視 → 使用Face ID需要注視螢幕 | Accessibility → Face ID & Attention → Require Attention for Face ID | `prefs:root=ACCESSIBILITY&path=FACE_ID#PearlUnlockAttention` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 引導使用模式 | Accessibility → Guided Access → Guided Access | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE#EnableGuidedAccess` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 螢幕自動鎖定 | Accessibility → Guided Access → Display Auto-Lock | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE#GuidedAccessAutoLockTime` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 輔助使用快速鍵 | Accessibility → Guided Access → Accessibility Shortcut | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE#GuidedAccessEnableAXFeatures` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 密碼設定 | Accessibility → Guided Access → Passcode Settings | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE#GuidedAccessSecurityLinkList` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 時間限制 | Accessibility → Guided Access → Time Limits | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE#GuidedAccessTimeRestrictionsLinkList` | 16.2 | F16 MAN MEHDI |  |
| — | — | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/` | — | MAN DYLD | 結尾斜線來自系統檔 |
| 輔助使用 → 引導使用模式 → 螢幕自動鎖定 | Accessibility → Guided Access → Display Auto-Lock | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessAutoLockTime` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 引導使用模式 → 密碼設定 | Accessibility → Guided Access → Passcode Settings | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessSecurityLinkList` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 引導使用模式 → 時間限制 | Accessibility → Guided Access → Time Limits | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 助聽裝置 → MFi助聽裝置 | Accessibility → Hearing Devices → MFi Hearing Devices | `prefs:root=ACCESSIBILITY&path=HEARING_AID_TITLE#AvailableAidsHeading` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 助聽裝置 → 藍牙 | Accessibility → Hearing Devices → Bluetooth | `prefs:root=ACCESSIBILITY&path=HEARING_AID_TITLE#HEARING_AID_BLUETOOTH` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 助聽裝置 → 助聽器相容性 | Accessibility → Hearing Devices → Hearing Aid Compatibility | `prefs:root=ACCESSIBILITY&path=HEARING_AID_TITLE#HEARING_AID_COMPLIANCE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 聆聽控制中心 → 已包含控制項目 | Accessibility → Hearing Control Center → Included Controls | `prefs:root=ACCESSIBILITY&path=HEARING_CONTROL_CENTER#INCLUDED_MODULES_SECTION_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 聆聽控制中心 → 更多控制項目 | Accessibility → Hearing Control Center → More Controls | `prefs:root=ACCESSIBILITY&path=HEARING_CONTROL_CENTER#MORE_MODULES_SECTION_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID → 啟用透過輔助觸控確認 | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#APPLE_PAY_CONFIRM_WITH_AST` | 18.7 | F18 |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID → 啟用透過切換控制確認 | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#APPLE_PAY_CONFIRM_WITH_SC` | 18.7 | F18 |  |
| 輔助使用 → 側邊按鈕 → 預設值 | Accessibility → Side Button → Default | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HOME_CLICK_SPEED_DEFAULT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 側邊按鈕 → 慢 | Accessibility → Side Button → Slow | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HOME_CLICK_SPEED_SLOW` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 側邊按鈕 → 最慢 | Accessibility → Side Button → Slowest | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HOME_CLICK_SPEED_SLOWEST` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID → 按鍵速度 | Accessibility → Side Button → Click Speed | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HOME_SPEED_HEADER` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 側邊按鈕 → 關閉 | Accessibility → Side Button → Off | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HomeButtonAssistantOff` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 側邊按鈕 → Siri | Accessibility → Side Button → Siri | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HomeButtonAssistantSiri` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID → 按住來說話 | Accessibility → Side Button → Press and hold to speak | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HomeButtonAssistantTitle` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 側邊按鈕 → 傳統語音控制 | Accessibility → Side Button → Classic Voice Control | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE#HomeButtonAssistantVoiceControl` | 16.2 | F16 MAN MEHDI |  |
| — | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE/APPLE_PAY_CONFIRM_WITH_AST` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE/APPLE_PAY_CONFIRM_WITH_SC` | — | GH |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID → 主畫面按鈕 | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE/HomeButtonAssistantTitle` | 18.7 | F18 MAN |  |
| 輔助使用 → 懸浮文字 → 啟用鎖定 | Accessibility → Hover Text → Activation Lock | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE#HOVER_TEXT_ACTIVATION_LOCK` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 顏色 | Accessibility → Hover Text → Colors | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE#HOVER_TEXT_COLOR_OPTIONS` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 啟用變更鍵 | Accessibility → Hover Text → Activation Modifier | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextActivationModifier` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 顯示模式 | Accessibility → Hover Text → Display Mode | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextDisplayMode` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 捲動速度 | Accessibility → Hover Text → Scrolling Speed | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextScrollSpeed` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 大小 | Accessibility → Hover Text → Size | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextSize` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 字體 | Accessibility → Hover Text → Font | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextStyle` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤 → 全面鍵盤操控 | Accessibility → Keyboards → Full Keyboard Access | `prefs:root=ACCESSIBILITY&path=KEYBOARDS#FULL_KEYBOARD_ACCESS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤 → 按鍵重複 | Accessibility → Keyboards → Key Repeat | `prefs:root=ACCESSIBILITY&path=KEYBOARDS#KEY_REPEAT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 顯示小寫按鍵 | Accessibility → Keyboards & Typing → Show Lowercase Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS#LOWERCASE_KEYBOARD` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤 → 慢速按鍵 | Accessibility → Keyboards → Slow Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS#SLOW_KEYS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 軟體鍵盤 | Accessibility → Keyboards & Typing → Software Keyboards | `prefs:root=ACCESSIBILITY&path=KEYBOARDS#SOFTWARE_KEYBOARDS` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤 → 按鍵暫留 | Accessibility → Keyboards → Sticky Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS#STICKY_KEYS` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → Keyboards → Full Keyboard Access | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/Full%20Keyboard%20Access` | — | FIFI WDG |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 | Accessibility → Keyboards & Typing → Full Keyboard Access | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS` | 18.7 | F18 MAN |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 | Accessibility → Keyboards & Typing → Hover Typing | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵重複 | Accessibility → Keyboards & Typing → Key Repeat | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/KEY_REPEAT` | 18.7 | F18 FIFI MAN WDG |  |
| 輔助使用 → 鍵盤與輸入 → 慢速按鍵 | Accessibility → Keyboards & Typing → Slow Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/SLOW_KEYS` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵暫留 | Accessibility → Keyboards & Typing → Sticky Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/STICKY_KEYS` | 18.7 | F18 FIFI MAN WDG |  |
| 輔助使用 → 即時語音 → 聲音 | Accessibility → Live Speech → Voices | `prefs:root=ACCESSIBILITY&path=LIVE_SPEECH_TITLE#LIVE_SPEECH_VOICES` | 18.7 | F18 |  |
| 輔助使用 → 即時語音 → 詞句 | Accessibility → Live Speech → Phrases | `prefs:root=ACCESSIBILITY&path=LIVE_SPEECH_TITLE/LiveSpeechCategoryManagement` | 18.7 | F18 |  |
| 輔助使用 → 即時字幕 → FaceTime中顯示即時字幕 | Accessibility → Live Captions → Live Captions in FaceTime | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION#FACE_TIME_CAPTIONS` | 16.2 · 18.7 | F18 F16 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION#LIVE_TRANSCRIPTION_APPEARANCE` | — | GH |  |
| 輔助使用 → 即時字幕 → 即時字幕 | Accessibility → Live Captions → Live Captions | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION#LIVE_TRANSCRIPTION_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 即時字幕 → 外觀 | Accessibility → Live Captions → Appearance | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE` | 18.7 | F18 GH |  |
| — | Accessibility → Magnifier → Magnifier → Auto Brightness | `prefs:root=ACCESSIBILITY&path=MAGNIFIER_TITLE#AutoBrightness` | — | MAN MEHDI |  |
| — | Accessibility → Magnifier → Magnifier → Magnifier | `prefs:root=ACCESSIBILITY&path=MAGNIFIER_TITLE#MagnifierEnabled` | — | MAN MEHDI |  |
| 輔助使用 → 動態效果 → 顯示車輛動態提示 | Accessibility → Motion → Show Vehicle Motion Cues | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#MotionCues` | 18.7 | F18 |  |
| 輔助使用 → 動態效果 → 調暗閃爍燈光 | Accessibility → Motion → Dim Flashing Lights | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#PHOTOSENSITIVE_MITIGATION` | 18.7 | F18 |  |
| 輔助使用 → 動態效果 → 偏好不閃爍的游標 | Accessibility → Motion → Prefer Non-Blinking Cursor | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#PREFER_NONBLINKING_CURSOR` | 18.7 | F18 |  |
| 輔助使用 → 動態效果 → 減少動態效果 | Accessibility → Motion → Reduce Motion | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#REDUCE_MOTION` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 動態效果 → 自動播放動畫式影像 | Accessibility → Motion → Auto-Play Animated Images | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#REDUCE_MOTION_AUTOPLAY_ANIMATED_IMAGES` | 18.7 | F18 |  |
| 輔助使用 → 動態效果 → 自動播放影片預覽 | Accessibility → Motion → Auto-Play Video Previews | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#REDUCE_MOTION_AUTOPLAY_VIDEO_PREVIEWS` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → Motion → Motion → Reduce Motion | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#REDUCE_MOTION_ID` | — | MAN MEHDI |  |
| 輔助使用 → 動態效果 → 自動播放訊息效果 | Accessibility → Motion → Auto-Play Message Effects | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#ReduceMotionAutoplayMessagesEffects` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | Accessibility → Motion → Motion → Auto-Play Video Previews | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#ReduceMotionAutoplayVideoPreviews` | — | MAN MEHDI |  |
| 輔助使用 → 動態效果 → 限制影格率 | Accessibility → Motion → Limit Frame Rate | `prefs:root=ACCESSIBILITY&path=MOTION_TITLE#REFRESH_RATE` | 18.7 | F18 |  |
| 輔助使用 → 眼球追蹤 → 自動隱藏 | Accessibility → Eye Tracking → Auto-Hide | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking#AUTO_HIDE` | 18.7 | F18 |  |
| 輔助使用 → 眼球追蹤 → 停留控制 | Accessibility → Eye Tracking → Dwell Control | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking#DWELL_CONTROL` | 18.7 | F18 |  |
| 輔助使用 → 眼球追蹤 → 放大鍵盤按鍵 | Accessibility → Eye Tracking → Zoom on Keyboard Keys | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking#KEYBOARD_ZOOM` | 18.7 | F18 |  |
| 輔助使用 → 眼球追蹤 → 眼球追蹤 | Accessibility → Eye Tracking → Eye Tracking | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking#OnDeviceEyeTrackingEnabledSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 眼球追蹤 → 平滑 | Accessibility → Eye Tracking → Smoothing | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking#SMOOTHING` | 18.7 | F18 |  |
| 輔助使用 → 眼球追蹤 → 貼齊項目 | Accessibility → Eye Tracking → Snap to Item | `prefs:root=ACCESSIBILITY&path=OnDeviceEyeTracking#SNAP_TO_ITEM` | 18.7 | F18 |  |
| 輔助使用 → 個人聲音 → 允許App發出使用要求 | Accessibility → Personal Voice → Allow Apps to Request to Use | `prefs:root=ACCESSIBILITY&path=PERSONAL_VOICE_TITLE#VB_ALLOW_WITH_APPS` | 18.7 | F18 |  |
| 輔助使用 → 個人聲音 → 製作個人聲音 | Accessibility → Personal Voice → Create a Personal Voice | `prefs:root=ACCESSIBILITY&path=PERSONAL_VOICE_TITLE#VB_CREATE_PERSONAL_VOICE` | 18.7 | F18 |  |
| 輔助使用 → 個人聲音 → 在裝置之間共享 | Accessibility → Personal Voice → Share Across Devices | `prefs:root=ACCESSIBILITY&path=PERSONAL_VOICE_TITLE#VB_USE_ICLOUD_TITLE` | 18.7 | F18 |  |
| 輔助使用 → RTT \| RTT/TTY \| TTY → 硬體TTY | Accessibility → RTT \| RTT/TTY \| TTY → Hardware TTY | `prefs:root=ACCESSIBILITY&path=RTT#HW_TTY` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → RTT \| RTT/TTY \| TTY → 軟體RTT \| 軟體RTT/TTY \| 軟體TTY | Accessibility → RTT \| RTT/TTY \| TTY → Software RTT \| Software RTT/TTY \| Software TTY | `prefs:root=ACCESSIBILITY&path=RTT#SW_TTY` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 移動重複 | Accessibility → Switch Control → Move Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#ActionRepeatIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 總是點一下鍵盤按鍵 | Accessibility → Switch Control → Always Tap Keyboard Keys | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#AlwaysTapKeyboardIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 透過切換控制確認 | Accessibility → Switch Control → Confirm with Switch Control | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#APPLE_PAY_SWITCH` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 音訊 | Accessibility → Switch Control → Audio | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#AudioGroupIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 點掃描 | Accessibility → Switch Control → Point Scanning | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#AxisSelectionGroupIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 滑動游標 | Accessibility → Switch Control → Gliding Cursor | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#AxisSweepIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 頭部追蹤 | Accessibility → Switch Control → Head Tracking | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#CameraPointPickerSwitch` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 游標顏色 | Accessibility → Switch Control → Cursor Color | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#CursorColorIdentifier` | 16.2 | F16 |  |
| 輔助使用 → 切換控制 → 大型游標 | Accessibility → Switch Control → Large Cursor | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#CursorVisibilityIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 已儲存的手勢 | Accessibility → Switch Control → Saved Gestures | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#CustomGesturesIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 選單項目 | Accessibility → Switch Control → Menu Items | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#CustomizeMenuIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 於第一個項目暫停 | Accessibility → Switch Control → Pause on First Item | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#DelayAfterInputIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 切換控制 | Accessibility → Switch Control → Switch Control | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#EnablingCell` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 按住持續時間 | Accessibility → Switch Control → Hold Duration | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#HoldDurationIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 忽略重複 | Accessibility → Switch Control → Ignore Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#IgnoreRepeatIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 群組項目 | Accessibility → Switch Control → Group Items | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#ItemGroupingIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 長時間按下 | Accessibility → Switch Control → Long Press | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#LongPressIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 組合 | Accessibility → Switch Control → Recipes | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#RecipesIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 點下後掃描相同按鍵 | Accessibility → Switch Control → Scan Same Key After Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#RestartScanAtCurrentIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 點下後在焦點內的項目 | Accessibility → Switch Control → Focused Item After Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#ScanLocationIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 自動掃描時間 | Accessibility → Switch Control → Auto Scanning Time | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#ScanningSpeedIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 掃描樣式 | Accessibility → Switch Control → Scanning Style | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#ScanningStyleIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 音效 | Accessibility → Switch Control → Sound Effects | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#SoundIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 語音 | Accessibility → Switch Control → Speech | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#SpeechIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 切換 | Accessibility → Switch Control → Switches | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#SwitchesIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 鍵盤 | Accessibility → Switch Control → Keyboard | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#SwitchKeyboardIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 切換穩定效果 | Accessibility → Switch Control → Switch Stabilization | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#SwitchStabilityIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 點一下動作 | Accessibility → Switch Control → Tap Behavior | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#TapBehaviorIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 時間 | Accessibility → Switch Control → Timing | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#TimingIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 擴大預測字詞範圍 | Accessibility → Switch Control → Extended Predictions | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#UseExtendedKeyboardPredictionsIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 視覺 | Accessibility → Switch Control → Visual | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle#VisualGroupIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 移動重複項目 | Accessibility → Switch Control → Move Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ActionRepeatIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換控制模式 | Accessibility → Switch Control → Switch Control Mode | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSelectionGroupIdentifier` | 18.7 | F18 MAN |  |
| 輔助使用 → 切換控制 → 滑動游標 | Accessibility → Switch Control → Gliding Cursor | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 頭部追蹤 | Accessibility → Switch Control → Head Tracking | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CameraPointPickerSwitch` | 18.7 | F18 FIFI MAN WDG |  |
| 輔助使用 → 切換控制 → 游標顏色 | Accessibility → Switch Control → Cursor Color | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CursorColorIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 已儲存的手勢 | Accessibility → Switch Control → Saved Gestures | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomGesturesIdentifier` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 切換控制 → 選單項目 | Accessibility → Switch Control → Menu Items | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 切換控制 → 於第一個項目暫停 | Accessibility → Switch Control → Pause on First Item | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/DelayAfterInputIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換控制模式 | Accessibility → Switch Control → Switch Control Mode | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/FirstLaunchScanningModeIdentifier` | 18.7 | F18 |  |
| — | Accessibility → Switch Control → Focused Item After Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Focused%20Item%20After%20Tap` | — | FIFI WDG |  |
| — | Accessibility → Switch Control → Gliding Cursor | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Gliding%20Cursor` | — | FIFI WDG |  |
| — | Accessibility → Switch Control → Hold Duration | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Hold%20Duration` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 按住持續時間 | Accessibility → Switch Control → Hold Duration | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/HoldDurationIdentifier` | 18.7 | F18 |  |
| — | Accessibility → Switch Control → Ignore Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Ignore%20Repeat` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 忽略重複 | Accessibility → Switch Control → Ignore Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/IgnoreRepeatIdentifier` | 18.7 | F18 |  |
| — | Accessibility → Switch Control → Long Press | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Long%20Press` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 長時間按下 | Accessibility → Switch Control → Long Press | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/LongPressIdentifier` | 18.7 | F18 |  |
| — | Accessibility → Switch Control → Move Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Move%20Repeat` | — | FIFI WDG |  |
| — | Accessibility → Switch Control → Pause on First Item | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Pause%20on%20First%20Item` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 組合 | Accessibility → Switch Control → Recipes | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/RecipesIdentifier` | 18.7 | F18 FIFI |  |
| 輔助使用 → 切換控制 → 循環 | Accessibility → Switch Control → Loops | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanCyclesIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 點下後在焦點內的項目 | Accessibility → Switch Control → Focused Item After Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanLocationIdentifier` | 18.7 | F18 |  |
| — | Accessibility → Switch Control → Scanning Style | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Scanning%20Style` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 自動掃描時間 | Accessibility → Switch Control → Auto Scanning Time | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningSpeedIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 掃描樣式 | Accessibility → Switch Control → Scanning Style | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningStyleIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 語音 | Accessibility → Switch Control → Speech | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SpeechIdentifier` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 切換控制 → 切換 | Accessibility → Switch Control → Switches | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier` | 18.7 | F18 FIFI WDG |  |
| — | Accessibility → Switch Control → Tap Behavior | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/Tap%20Behavior` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 點一下動作 | Accessibility → Switch Control → Tap Behavior | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/TapBehaviorIdentifier` | 18.7 | F18 |  |
| 輔助使用 → Siri → 透過揚聲器播報通知 | Accessibility → Siri → Announce Notifications on Speaker | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#ANNOUNCE_NOTIFICATIONS_BUILT_IN_SPEAKER_ID` | 18.7 | F18 |  |
| 輔助使用 → Siri → Siri暫停時間 | Accessibility → Siri → Siri Pause Time | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#ENDPOINTER` | 18.7 | F18 |  |
| 輔助使用 → Siri → 聆聽非典型語音 | Accessibility → Siri → Listen for Atypical Speech | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SIRI_ATYPICAL_SPEECH` | 18.7 | F18 |  |
| 輔助使用 → Siri → 必須說「Siri」才能打斷 | Accessibility → Siri → Require “Siri” for Interruptions | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SIRI_BARGE` | 18.7 | F18 |  |
| 輔助使用 → Siri → 輸入來與Siri對話 | Accessibility → Siri → Type to Siri | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SIRI_SETTINGS_TYPE_TO_SIRI` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → Siri → 永遠聆聽「Siri」 | Accessibility → Siri → Always Listen for “Siri” | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SIRI_SETTINGS_VOICE_ACTIVATION_ALWAYS_ALLOW` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → Siri → 顯示Siri後方的App | Accessibility → Siri → Show Apps Behind Siri | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SIRL_SHOW_APPS` | 18.7 | F18 |  |
| 輔助使用 → Siri → Siri朗讀速度 | Accessibility → Siri → Siri Speaking Rate | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#SPEECH_RATE` | 18.7 | F18 |  |
| 輔助使用 → Siri → 語音回應 | Accessibility → Siri → Spoken Responses | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK` | 18.7 | F18 |  |
| — | Accessibility → Siri → Siri → Always Speak Responses | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK_ALWAYS_ID` | — | MAN MEHDI |  |
| 輔助使用 → Siri → 自動語音回應 | Accessibility → Siri → Automatic Spoken Responses | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK_AUTOMATIC_ID` | 16.2 | F16 |  |
| 輔助使用 → Siri → 語音回應 | Accessibility → Siri → Spoken Responses | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK_GROUP_ID` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → Siri → Siri → Only with "Hey Siri" | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK_HANDSFREE_ID` | — | MAN MEHDI |  |
| 輔助使用 → Siri → 偏好無聲回應 | Accessibility → Siri → Prefer Silent Responses | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK_NEVER_ID` | 16.2 | F16 |  |
| 輔助使用 → Siri → 「靜音模式」中不說話 | Accessibility → Siri → Don't Speak in Silent Mode | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE#VOICE_FEEDBACK_WITH_SWITCH_ID` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → Siri → 通話掛斷 | Accessibility → Siri → Call Hang Up | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE/SIRI_CALL_HANGUP_ID` | 18.7 | F18 |  |
| 輔助使用 → 聲音辨識 → 提示聲 | Accessibility → Sound Recognition → Sounds | `prefs:root=ACCESSIBILITY&path=SOUND_RECOGNITION_TITLE#Sounds` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 聲音辨識 → 音效 | Accessibility → Sound Recognition → Sounds | `prefs:root=ACCESSIBILITY&path=SOUND_RECOGNITION_TITLE/Sounds` | 18.7 | F18 FIFI MAN DYLD WDG |  |
| 輔助使用 → 語音內容 → 偵測語言 | Accessibility → Spoken Content → Detect Languages | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#LANGUAGE_DETECTION` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 語音內容 → 發音 | Accessibility → Spoken Content → Pronunciations | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#PRONUNCIATION_DICTIONARY` | 16.2 | F16 |  |
| 輔助使用 → 語音內容 → 朗讀所選範圍 | Accessibility → Spoken Content → Speak Selection | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#QUICK_SPEAK_TITLE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 聲音 | Accessibility → Spoken Content → Voices | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#QuickSpeakAccents` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 反白內容 | Accessibility → Spoken Content → Highlight Content | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#QuickSpeakHighlight` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 朗讀速度 | Accessibility → Spoken Content → Speaking Rate | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#QuickSpeakRate` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 朗讀速度 | Accessibility → Spoken Content → Speaking Rate | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#QuickSpeakRateGroup` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 空間化語音 | Accessibility → Spoken Content → Spatialize Speech | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#SPATIALIZE_SPEECH` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 朗讀螢幕 | Accessibility → Spoken Content → Speak Screen | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#SpeakThisEnabled` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 語音控制器 | Accessibility → Spoken Content → Spoken Content → Speech Controller | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#SpeechController` | — | MAN MEHDI |  |
| 輔助使用 → 語音內容 → 預設語言 | Accessibility → Spoken Content → Default Language | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#SpokenContentDefaultLanguage` | 16.2 | F16 |  |
| 輔助使用 → 語音內容 → 輸入回饋 | Accessibility → Spoken Content → Spoken Content → Typing Feedback | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE#TypingFeedback` | — | MAN MEHDI |  |
| 輔助使用 → 語音內容 → 聲音 | Accessibility → Spoken Content → Voices | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/QuickSpeakAccents` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 語音內容 → 反白內容 | Accessibility → Spoken Content → Highlight Content | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/QuickSpeakHighlight` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 語音內容 → 語音控制器 | Accessibility → Spoken Content → Speech Controller | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController` | 16.2 · 18.7 | F18 F16 FIFI WDG |  |
| 輔助使用 → 語音內容 → 預設語言 | Accessibility → Spoken Content → Default Language | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpokenContentDefaultLanguage` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 輸入回饋 | Accessibility → Spoken Content → Typing Feedback | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback` | 16.2 · 18.7 | F18 F16 FIFI WDG |  |
| 輔助使用 → 語音內容 → 發音 | Accessibility → Spoken Content → Pronunciations | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/VoiceOverSettings` | 18.7 | F18 |  |
| 輔助使用 → 字幕與隱藏式字幕 → 樣式 | Accessibility → Subtitles & Captioning → Style | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING#currentTheme` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 字幕與隱藏式字幕 → 隱藏式字幕 + SDH | Accessibility → Subtitles & Captioning → Closed Captions + SDH | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING#PREFER_SDH` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 字幕與隱藏式字幕 → 顯示音訊逐字稿 | Accessibility → Subtitles & Captioning → Show Audio Transcriptions | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING#SHOW_AUDIO_TRANSCRIPTIONS` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 字幕與隱藏式字幕 → 倒轉時顯示 | Accessibility → Subtitles & Captioning → Show on Skip Back | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING#SHOW_ON_SKIP_BACK` | 18.7 | F18 |  |
| 輔助使用 → 字幕與隱藏式字幕 → 靜音時顯示 | Accessibility → Subtitles & Captioning → Show when Muted | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING#SHOW_WHEN_MUTED` | 18.7 | F18 |  |
| 輔助使用 → 字幕與隱藏式字幕 → 樣式 | Accessibility → Subtitles & Captioning → Style | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING/currentTheme` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → 輔助觸控 | Accessibility → Touch → Touch → AssistiveTouch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#AIR_TOUCH_TITLE` | — | MAN MEHDI |  |
| 輔助使用 → 觸控 → 來電語音傳送 | Accessibility → Touch → Call Audio Routing | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#CALL_AUDIO_ROUTING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 偏好非頭部鎖定的控制項目 | Accessibility → Interaction \| Touch → Prefer Non-Headlocked Controls | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#CAMERA_ANCHOR_ALTERNATIVE_Preference` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → 3D與觸覺回饋觸控 | Accessibility → Touch → 3D & Haptic Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#ForceTouch` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 防止鎖定被用來結束通話 | Accessibility → Interaction \| Touch → Prevent Lock to End Call | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#LockButtonIgnore` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 互動 \| 觸控 → 螢幕上方觸控 | Accessibility → Interaction \| Touch → Reachability | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#REACHABILITY` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 晃動來還原 | Accessibility → Interaction \| Touch → Shake to Undo | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#SHAKE_TO_UNDO` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 點一下喚醒 | Accessibility → Interaction \| Touch → Tap to Wake | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#TAP_TO_WAKE_TITLE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 點一下或滑動來喚醒 | Accessibility → Interaction \| Touch → Tap or Swipe to Wake | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#TAP_TOUCH_TO_WAKE_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 觸控 → 觸控調節 | Accessibility → Touch → Touch Accommodations | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#TOUCH_ACCOMMODATIONS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 震動模式 | Accessibility → Interaction \| Touch → Vibration | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE#VIBRATION` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 | Accessibility → Interaction \| Touch → AssistiveTouch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD WDG |  |
| — | Accessibility → Touch → Back Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Back%20Tap` | — | FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 背面輕點 | Accessibility → Interaction \| Touch → Back Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/BackTap` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 來電語音傳送 | Accessibility → Interaction \| Touch → Call Audio Routing | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 | Accessibility → Interaction \| Touch → Dwell Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL` | 18.7 | F18 MAN |  |
| 輔助使用 → 互動 \| 觸控 → 3D與觸覺回饋觸控 | Accessibility → Interaction \| Touch → 3D & Haptic Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 | Accessibility → Interaction \| Touch → Pointer Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer` | 18.7 | F18 MAN |  |
| 輔助使用 → 互動 \| 觸控 → 聲音動作 | Accessibility → Interaction \| Touch → Sound Actions | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/SOUND_ACTIONS` | 18.7 | F18 |  |
| — | Accessibility → Touch → Touch Accommodations | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Touch%20Accommodations` | — | FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 觸控調節 | Accessibility → Interaction \| Touch → Touch Accommodations | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS` | 18.7 | F18 MAN |  |
| 輔助使用 → 互動 \| 觸控 → 向上看來顯示控制中心 | Accessibility → Interaction \| Touch → Look Upwards for Control Center | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/UPWARDS_HUD` | 18.7 | F18 MAN |  |
| 輔助使用 → 輔助使用快速鍵 → 放大鏡 | Accessibility → Accessibility Shortcut → Magnifier | `prefs:root=ACCESSIBILITY&path=TRIPLE_CLICK_TITLE#TripleClickMagnifier` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 活動 | Accessibility → VoiceOver → VoiceOver → Activities | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#Activities` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 音訊 | Accessibility → VoiceOver → VoiceOver → Audio | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#Audio` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 | Accessibility → VoiceOver → VoiceOver → Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#Braille` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 字幕面板 | Accessibility → VoiceOver → Caption Panel | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#CaptionPanel` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 大型游標 | Accessibility → VoiceOver → Large Cursor | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#CursorStyle` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 指令 | Accessibility → VoiceOver → Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#CUSTOMIZE_COMMANDS` | 16.2 | F16 MAN MEHDI |  |
| — | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#CustomizeCommands` | — | GH |  |
| 輔助使用 → 旁白 → 捏兩下逾時 | Accessibility → VoiceOver → Double-pinch Timeout | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#DOUBLE_TAP_INTERVAL` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點兩下逾時 | Accessibility → VoiceOver → VoiceOver → Double-tap Timeout | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#DOUBLE_TAP_INTERVAL_TITLE` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 導覽影像 | Accessibility → VoiceOver → Navigate Images | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#IncludeUnlabeledImages` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 導覽樣式 | Accessibility → VoiceOver → Navigation Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#NavigationStyle` | 16.2 | F16 |  |
| — | Accessibility → VoiceOver → VoiceOver → Rotor Actions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#ROTOR_ACTIONS` | — | MAN MEHDI |  |
| — | Accessibility → VoiceOver → VoiceOver → Always Speak Notifications | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#SPEAK_NOTIFICATIONS` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 朗讀速度 | Accessibility → VoiceOver → Speaking Rate | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#SpeakingRate` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 朗讀速度 | Accessibility → VoiceOver → Speaking Rate | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#SpeakingRateSlider` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 | Accessibility → VoiceOver → VoiceOver → Speech | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#Speech` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 輸入 | Accessibility → VoiceOver → VoiceOver → Typing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#TypingOptions` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 詳細程度 | Accessibility → VoiceOver → VoiceOver → Verbosity | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#Verbosity` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 所選範圍前的延遲時間 | Accessibility → VoiceOver → Delay before Selection | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#VoiceOverDelayUntilSpeak` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白 | Accessibility → VoiceOver → VoiceOver | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#VoiceOverTouchEnabled` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 旁白教學指南 | Accessibility → VoiceOver → VoiceOver Tutorial | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#VoiceOverTouchTutorialEnabled` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 轉輪 | Accessibility → VoiceOver → Rotor | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE#WebRotor` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → VoiceOver → Activities → (root) | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/ACTIVITIES` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 活動 | Accessibility → VoiceOver → Activities | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/activities` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Activities | Accessibility → VoiceOver → Activities | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Activities` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 音訊 | Accessibility → VoiceOver → Audio | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → VoiceOver → Audio | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/AUDIO_TITLE` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 點字 | Accessibility → VoiceOver → Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → VoiceOver → Braille → (root) | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CUSTOMIZE_COMMANDS` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 指令 | Accessibility → VoiceOver → Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 點兩下逾時 | Accessibility → VoiceOver → Double-tap Timeout | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/DOUBLE_TAP_INTERVAL_TITLE` | 16.2 · 18.7 | F18 F16 FIFI WDG |  |
| — | Accessibility → VoiceOver → Navigate Images | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/INCLUDE_UNLABELED_IMAGES_TITLE` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 導覽影像 | Accessibility → VoiceOver → Navigate Images | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/IncludeUnlabeledImages` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 導覽樣式 | Accessibility → VoiceOver → Navigation Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NavigationStyle` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 | Accessibility → VoiceOver → VoiceOver Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 快速設定 | Accessibility → VoiceOver → Quick Settings | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → VoiceOver → Rotor Actions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/ROTOR_ACTIONS` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 轉輪 | Accessibility → VoiceOver → Rotor | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → Speech | Accessibility → VoiceOver → Speech | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Speech` | 16.2 | F16 |  |
| — | Accessibility → VoiceOver → Speech | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/SPEECH_TITLE` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Typing → (root) | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TYPING_OPTIONS` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 輸入 | Accessibility → VoiceOver → Typing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → VoiceOver → Braille → Verbosity → (root) | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/VERBOSITY` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 詳細程度 | Accessibility → VoiceOver → Verbosity | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 語音 | Accessibility → VoiceOver → Speech | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices` | 18.7 | F18 |  |
| — | Accessibility → VoiceOver → Rotor | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/WEB_ROTOR` | — | FIFI WDG |  |
| 輔助使用 → 縮放 → 邊線顏色 | Accessibility → Zoom → Border Color | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#MagnifyingGlassBorderColor` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 智慧輸入 | Accessibility → Zoom → Smart Typing | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomAlwaysUseWindowZoomForTyping` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 將縮放設為預設的焦點 | Accessibility → Zoom → Set Zoom as Default Focus | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomAsDefaultDial` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 最大縮放層級 | Accessibility → Zoom → Maximum zoom level | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomFactorGroup` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 縮放濾鏡 | Accessibility → Zoom → Zoom Filter | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomFilter` | 16.2 | F16 |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 | Accessibility → Zoom → Zoom → Keybord Shortcuts | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomKeyboardShortcuts` | — | MAN MEHDI |  |
| 輔助使用 → 縮放 → 縮放區域 | Accessibility → Zoom → Zoom → Zoom Region | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomLensMode` | — | MAN MEHDI |  |
| 輔助使用 → 縮放 → 最大縮放層級 | Accessibility → Zoom → Maximum Zoom Level | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomPreferredMaxZoomLevel` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 隨焦點移動 | Accessibility → Zoom → Follow Focus | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomShouldFollowFocus` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鏡像輸出時顯示 | Accessibility → Zoom → Show while Mirroring | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomShowWhileMirroring` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 縮放 → 縮放控制器 | Accessibility → Zoom → Zoom Controller | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomSlug` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 使用數位旋鈕來縮放 | Accessibility → Zoom → Use Digital Crown to Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomStealsCrownTurns` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放 | Accessibility → Zoom → Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomTouchEnabled` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 使用觸控式軌跡板手勢來縮放 | Accessibility → Zoom → Use trackpad gesture to zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE#ZoomWithTrackpad` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放濾鏡 | Accessibility → Zoom → Zoom Filter | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomFilter` | 18.7 | F18 FIFI MEHDI WDG |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 | Accessibility → Zoom → Keyboard Shortcuts | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts` | 16.2 · 18.7 | F18 F16 FIFI MAN WDG |  |
| 輔助使用 → 縮放 → 縮放區域 | Accessibility → Zoom → Zoom Region | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomLensMode` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 縮放 → 縮放控制器 | Accessibility → Zoom → Zoom Controller | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 在媒體播放時使用 | Accessibility → Audio & Visual → Background Sounds → Use When Media Is Playing | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID#ComfortSoundsMixingName` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 播放媒體時的音量 | Accessibility → Audio & Visual → Background Sounds → Volume with Media | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID#ComfortSoundsMixingVolume` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 鎖定時停止聲音 | Accessibility → Audio & Visual → Background Sounds → Stop Sounds When Locked | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID#ComfortSoundsPlayWhenLockedName` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 背景聲音音量 | Accessibility → Audio & Visual → Background Sounds → Background Sounds Volume | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID#ComfortSoundsVolume` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 背景聲音 | Accessibility → Audio & Visual → Background Sounds → Background Sounds | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID#CSFeatureToggleSpecID` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 聲音 | Accessibility → Audio & Visual → Background Sounds → Sound | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID/ComfortSoundSoundLabel` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 耳機調節 → 耳機調節 | Accessibility → Audio & Visual → Headphone Accommodations → Headphone Accommodations | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXPAEnableSpecID#AXPAEnableSpecID` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 耳機調節 → 自訂音訊設定 | Accessibility → Audio & Visual → Headphone Accommodations → Custom Audio Setup | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXPAEnableSpecID#AXPAPersonalAudioSetupSpecID` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 音訊與視覺 → 收到提示時閃爍LED → 收到提示時閃爍LED | Accessibility → Audio & Visual → LED Flash for Alerts → LED Flash for Alerts | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/LED_FLASH#LED_FLASH` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 收到提示時閃爍LED → 解鎖期間閃爍 | Accessibility → Audio & Visual → LED Flash for Alerts → Flash While Unlocked | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/LED_FLASH#LED_FLASH_WHILE_UNLOCKED` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 音訊與視覺 → 收到提示時閃爍LED → 靜音模式中閃爍 | Accessibility → Audio & Visual → LED Flash for Alerts → Flash in Silent Mode | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/LED_FLASH#LED_RINGER_SWITCH_CONTROL` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 音訊與視覺 → 在通話中加入音訊 → 允許App在通話中加入音訊 | Accessibility → Audio & Visual → Add Audio in Calls → Allow Apps to Add Audio in Calls | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/MIX_TO_UPLINK#MIX_TO_UPLINK` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 密碼設定 → 密碼設定 | Accessibility → Assistive Access → Passcode Settings → Passcode Settings | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE/PasscodeSettings#PasscodeSettings` | 18.7 | F18 |  |
| 輔助使用 → 自訂輔助取用 → 背景圖片 → 背景圖片 | Accessibility → Assistive Access → Wallpaper → Wallpaper | `prefs:root=ACCESSIBILITY&path=CLARITY_UI_TITLE/Wallpaper#Wallpaper` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 覆疊 → 覆疊 | Accessibility → Voice Control → Overlay → Overlay | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/ALWAYS_SHOW_OVERLAY#ALWAYS_SHOW_OVERLAY` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → NEEDS_OVERRIDE_1379 → 編號格線 | Accessibility → Voice Control → NEEDS_OVERRIDE_257 → Numbered Grid | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/ALWAYS_SHOW_OVERLAY#OVERLAY_GRID` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → NEEDS_OVERRIDE_1379 → 項目名稱 | Accessibility → Voice Control → NEEDS_OVERRIDE_257 → Item Names | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/ALWAYS_SHOW_OVERLAY#OVERLAY_NAMES` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → NEEDS_OVERRIDE_1379 → 無 | Accessibility → Voice Control → NEEDS_OVERRIDE_257 → None | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/ALWAYS_SHOW_OVERLAY#OVERLAY_NONE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → NEEDS_OVERRIDE_1379 → 項目編號 | Accessibility → Voice Control → NEEDS_OVERRIDE_257 → Item Numbers | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/ALWAYS_SHOW_OVERLAY#OVERLAY_NUMBERS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音控制 → 指令 → 指令 | Accessibility → Voice Control → Commands → Commands | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS#COMMAND_AND_CONTROL_COMMANDS` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 輔助使用 | Accessibility → Voice Control → Commands → Accessibility | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Accessibility` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 文字刪除 | Accessibility → Voice Control → Commands → Text Deletion | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/AdvancedDeletion` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 新增指令 | Accessibility → Voice Control → Commands → Create New Command | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/CreateNewCommand` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 進階手勢 | Accessibility → Voice Control → Commands → Advanced Gestures | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/DragDropGestures` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 文字編輯 | Accessibility → Voice Control → Commands → Text Editing | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Editing` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 基本手勢 | Accessibility → Voice Control → Commands → Basic Gestures | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Gestures` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 裝置 | Accessibility → Voice Control → Commands → Device | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Hardware` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 輸入自訂指令 | Accessibility → Voice Control → Commands → Import Custom Commands | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/ImportCustomCommands` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 文字導覽 | Accessibility → Voice Control → Commands → Text Navigation | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Movement` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 覆疊 | Accessibility → Voice Control → Commands → Overlays | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Overlays` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 文字所選範圍 | Accessibility → Voice Control → Commands → Text Selection | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/Selection` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 基本導覽 | Accessibility → Voice Control → Commands → Basic Navigation | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/System` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 聽寫 | Accessibility → Voice Control → Commands → Dictation | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/TextDictation` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 語言 → 語言 | Accessibility → Voice Control → Language → Language | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_LANGUAGE#COMMAND_AND_CONTROL_LANGUAGE` | 18.7 | F18 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_LANGUAGE#English%20` | — | MAN |  |
| 輔助使用 → 語音控制 → NEEDS_OVERRIDE_1378 → 英文（美國） | Accessibility → Voice Control → NEEDS_OVERRIDE_256 → English (United States) | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_LANGUAGE#English%20(United%20States` | 16.2 | F16 MEHDI |  |
| 輔助使用 → 語音控制 → 詞彙 → 刪除所有詞彙 | Accessibility → Voice Control → Vocabulary → Delete All Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY#DELETE_ALL_VOCABULARY` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 詞彙 → 輸出詞彙 | Accessibility → Voice Control → Vocabulary → Export Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY#EXPORT_VOCABULARY` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 詞彙 → 輸入詞彙 | Accessibility → Voice Control → Vocabulary → Import Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY#IMPORT_VOCABULARY` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 詞彙 → 詞彙 | Accessibility → Voice Control → Vocabulary → Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY/VOCABULARY` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → 顏色濾鏡 → 顏色濾鏡 | Accessibility → Display & Text Size → Color Filters → Color Filters | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/DISPLAY_FILTER_COLOR#DISPLAY_FILTER_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → Color Filters → 顏色濾鏡 | Accessibility → Display & Text Size → Color Filters → Color Filters | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/DISPLAY_FILTER_COLOR#FILTER_COLOR_ENABLED` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 顯示與文字大小 → 顏色濾鏡 → 套用於影像透視 | Accessibility → Display & Text Size → Color Filters → Apply to Video Passthrough | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/DISPLAY_FILTER_COLOR#VIDEO_PASSTHROUGH` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → 放大文字 → 更大的輔助使用字體大小 | Accessibility → Display & Text Size → Larger Text → Larger Accessibility Sizes | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/LARGER_TEXT#LARGER_DYNAMIC_TYPE_SWITCH` | 18.7 | F18 |  |
| 輔助使用 → 顯示與文字大小 → 放大文字 → 放大文字 | Accessibility → Display & Text Size → Larger Text → Larger Text | `prefs:root=ACCESSIBILITY&path=DISPLAY_AND_TEXT/LARGER_TEXT#LARGER_TEXT` | 18.7 | F18 |  |
| 輔助使用 → 引導使用模式 → 螢幕自動鎖定 → 螢幕自動鎖定 | Accessibility → Guided Access → Display Auto-Lock → Display Auto-Lock | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessAutoLockTime#GuidedAccessAutoLockTime` | 18.7 | F18 |  |
| 輔助使用 → 引導使用模式 → 密碼設定 → 設定引導使用模式密碼 | Accessibility → Guided Access → Passcode Settings → Set Guided Access Passcode | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessSecurityLinkList#GAXPinButton` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 密碼設定 → Face ID \| Touch ID | Accessibility → Guided Access → Passcode Settings → Face ID \| Touch ID | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessSecurityLinkList#GAXSpecIDTouchIDSwitch` | 18.7 | F18 |  |
| 輔助使用 → 引導使用模式 → 密碼設定 → 密碼設定 | Accessibility → Guided Access → Passcode Settings → Passcode Settings | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessSecurityLinkList#GuidedAccessSecurityLinkList` | 18.7 | F18 |  |
| 輔助使用 → 引導使用模式 → NEEDS_OVERRIDE_1388 → 鬧鐘 | Accessibility → Guided Access → NEEDS_OVERRIDE_266 → Alarm | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList#GUIDED_ACCESS_TIME_RESTRICTIONS_HEADING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → NEEDS_OVERRIDE_1388 → 提示聲 | Accessibility → Guided Access → NEEDS_OVERRIDE_266 → Sound | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList#GUIDED_ACCESS_TIME_RESTRICTIONS_SOUND_TITLE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 時間限制 → 朗讀 | Accessibility → Guided Access → Time Limits → Speak | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList#GUIDED_ACCESS_TIME_RESTRICTIONS_SPEAK_TITLE` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 引導使用模式 → 時間限制 → 時間限制 | Accessibility → Guided Access → Time Limits → Time Limits | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList#GuidedAccessTimeRestrictionsLinkList` | 18.7 | F18 |  |
| 輔助使用 → 引導使用模式 → 時間限制 → 提示聲 | Accessibility → Guided Access → Time Limits → Sound | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList/GUIDED_ACCESS_TIME_RESTRICTIONS_SOUND_TITLE` | 18.7 | F18 FIFI WDG |  |
| — | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE/APPLE_PAY_CONFIRM_WITH_SC#APPLE_PAY_CONFIRM_WITH_SC` | — | GH |  |
| 輔助使用 → 主畫面按鈕 \| 側邊按鈕 \| 數位旋鈕 \| 頂端按鈕 \| 頂端按鈕/Touch ID → 主畫面按鈕 → 輕觸按鈕來打開 | — | `prefs:root=ACCESSIBILITY&path=HOME_CLICK_TITLE/HomeButtonAssistantTitle#RestingUnlockSetting` | 18.7 | F18 GH |  |
| 輔助使用 → 懸浮文字 → 啟用變更鍵 → 啟用變更鍵 | Accessibility → Hover Text → Activation Modifier → Activation Modifier | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextActivationModifier#HoverTextActivationModifier` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 顯示模式 → 顯示模式 | Accessibility → Hover Text → Display Mode → Display Mode | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextDisplayMode#HoverTextDisplayMode` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 捲動速度 → 捲動速度 | Accessibility → Hover Text → Scrolling Speed → Scrolling Speed | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextScrollSpeed#HoverTextScrollSpeed` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 大小 → 大小 | Accessibility → Hover Text → Size → Size | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextSize#HoverTextSize` | 18.7 | F18 |  |
| 輔助使用 → 懸浮文字 → 字體 → 字體 | Accessibility → Hover Text → Font → Font | `prefs:root=ACCESSIBILITY&path=HOVERTEXT_TITLE/HoverTextStyle#HoverTextStyle` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤 → NEEDS_OVERRIDE_1380 → 視覺效果 | Accessibility → Keyboards → NEEDS_OVERRIDE_258 → Visuals | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS#APPEARANCE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 全面鍵盤操控 | Accessibility → Keyboards & Typing → Full Keyboard Access → Full Keyboard Access | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS#FKAEnabledSwitch` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤 → NEEDS_OVERRIDE_1380 → 顏色 | Accessibility → Keyboards → NEEDS_OVERRIDE_258 → Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS#FKAFocusRingColor` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤 → NEEDS_OVERRIDE_1380 → 大焦點框 | Accessibility → Keyboards → NEEDS_OVERRIDE_258 → Large Focus Ring | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS#FKAFocusRingHighVisibilityEnabled` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤 → NEEDS_OVERRIDE_1380 → 自動隱藏 | Accessibility → Keyboards → NEEDS_OVERRIDE_258 → Auto-Hide | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS#FKAFocusRingTimeout` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 指令 | Accessibility → Keyboards & Typing → Full Keyboard Access → Commands | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKACommands` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 顏色 | Accessibility → Keyboards & Typing → Full Keyboard Access → Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKAFocusRingColor` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 高對比 | Accessibility → Keyboards & Typing → Full Keyboard Access → High Contrast | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKAFocusRingHighContrastEnabled` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 自動隱藏 | Accessibility → Keyboards & Typing → Full Keyboard Access → Auto-Hide | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKAFocusRingTimeout` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 增加大小 | Accessibility → Keyboards & Typing → Full Keyboard Access → Increase Size | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKALargeFocusRingEnabled` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 背景顏色 | Accessibility → Keyboards & Typing → Hover Typing → Background Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TEXT_BACKGROUND_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 邊線顏色 | Accessibility → Keyboards & Typing → Hover Typing → Border Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TEXT_BORDER_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 插入點顏色 | Accessibility → Keyboards & Typing → Hover Typing → Insertion Point Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TEXT_INSERTION_POINT_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 文字顏色 | Accessibility → Keyboards & Typing → Hover Typing → Text Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TEXT_TEXT_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 自動修正的字詞顏色 | Accessibility → Keyboards & Typing → Hover Typing → Autocorrected Word Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TYPING_AUTOCORRECTED_WORD_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 輸入顏色 | Accessibility → Keyboards & Typing → Hover Typing → Typing Colors | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TYPING_COLOR_OPTIONS` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 顯示顏色 | Accessibility → Keyboards & Typing → Hover Typing → Display Colors | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TYPING_DISPLAY_COLOR_OPTIONS` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 拼錯的字詞顏色 | Accessibility → Keyboards & Typing → Hover Typing → Misspelled Word Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TYPING_MISSPELLED_WORD` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 重置為預設值 | Accessibility → Keyboards & Typing → Hover Typing → Reset to Default | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING#HOVER_TYPING_RESET_BUTTON` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 大小 | Accessibility → Keyboards & Typing → Hover Typing → Size | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING/HoverTextSize` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 顯示模式 | Accessibility → Keyboards & Typing → Hover Typing → Display Mode | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING/HoverTextTypingDisplayMode` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 字體 | Accessibility → Keyboards & Typing → Hover Typing → Font | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING/HoverTypingStyle` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵重複 → 重複前暫延 | Accessibility → Keyboards & Typing → Key Repeat → Delay Until Repeat | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/KEY_REPEAT#KeyRepeatDelay` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵重複 → 按鍵重複 | Accessibility → Keyboards & Typing → Key Repeat → Key Repeat | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/KEY_REPEAT#KeyRepeatEnabled` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵重複 → 按鍵重複間隔 | Accessibility → Keyboards & Typing → Key Repeat → Key Repeat Interval | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/KEY_REPEAT#KeyRepeatInterval` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 慢速按鍵 → 慢速按鍵 | Accessibility → Keyboards & Typing → Slow Keys → Slow Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/SLOW_KEYS#NumericalPreferenceSwitcherIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵暫留 → 按鍵暫留 | Accessibility → Keyboards & Typing → Sticky Keys → Sticky Keys | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/STICKY_KEYS#StickyKeysEnabled` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵暫留 → 使用Shift鍵切換 | Accessibility → Keyboards & Typing → Sticky Keys → Toggle With Shift Key | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/STICKY_KEYS#StickyKeysShiftToggle` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 鍵盤與輸入 → 按鍵暫留 → 提示聲 | Accessibility → Keyboards & Typing → Sticky Keys → Sound | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/STICKY_KEYS#StickyKeysSound` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | — | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#ENHANCE_TEXT_LEGIBILITY` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LARGER_TEXT` | — | GH |  |
| 輔助使用 → 即時字幕 → 外觀 → 閒置不透明度 | Accessibility → Live Captions → Appearance → Idle Opacity | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LIVE_CAPTIONS_IDLE_OPACITY_TITLE` | 18.7 | F18 GH |  |
| 輔助使用 → 即時字幕 → 外觀 → 外觀 | Accessibility → Live Captions → Appearance → Appearance | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LIVE_TRANSCRIPTION_APPEARANCE` | 18.7 | F18 GH |  |
| 輔助使用 → 即時字幕 → 外觀 → 背景顏色 | Accessibility → Live Captions → Appearance → Background Color | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LIVE_TRANSCRIPTION_BACKGROUND_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 即時字幕 → 外觀 → 顏色選項 | Accessibility → Live Captions → Appearance → Color Options | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LIVE_TRANSCRIPTION_COLOR_OPTIONS` | 18.7 | F18 GH |  |
| 輔助使用 → 即時字幕 → 外觀 → 重置顏色 | Accessibility → Live Captions → Appearance → Reset Colors | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LIVE_TRANSCRIPTION_RESET_COLORS` | 18.7 | F18 |  |
| 輔助使用 → 即時字幕 → 外觀 → 文字顏色 | Accessibility → Live Captions → Appearance → Text Color | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE#LIVE_TRANSCRIPTION_TEXT_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 即時字幕 → 外觀 → 粗體文字 | Accessibility → Live Captions → Appearance → Bold Text | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE/ENHANCE_TEXT_LEGIBILITY` | 18.7 | F18 GH |  |
| 輔助使用 → 即時字幕 → 外觀 → 文字大小 | Accessibility → Live Captions → Appearance → Text Size | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE/LARGER_TEXT` | 18.7 | F18 GH |  |
| — | Accessibility → RTT/TTY → RTT/TTY → [Cell Line Name] → Hardware TTY | `prefs:root=ACCESSIBILITY&path=RTT/YourCellLineName#HW_TTY` | — | MEHDI |  |
| — | Accessibility → RTT/TTY → RTT/TTY → [Cell Line Name] → Software RTT | `prefs:root=ACCESSIBILITY&path=RTT/YourCellLineName#SW_TTY` | — | MEHDI |  |
| 輔助使用 → 切換控制 → 移動重複項目 → 移動重複項目 | Accessibility → Switch Control → Move Repeat → Move Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ActionRepeatIdentifier#NumericalPreferenceSwitcherIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 切換控制模式 → 滑動游標 | Accessibility → Switch Control → Switch Control Mode → Gliding Cursor | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSelectionGroupIdentifier#POINTER_PICKER_ENABLED` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 滑動游標 → 滑動游標 | Accessibility → Switch Control → Gliding Cursor → Gliding Cursor | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier#AxisSweepIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 滑動游標 → 滑動游標速度 | Accessibility → Switch Control → Gliding Cursor → Gliding Cursor Speed | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier#AxisSweepSpeed` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 滑動游標 → 選擇模式 | Accessibility → Switch Control → Gliding Cursor → Selection Mode | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier#SelectionStyleGroup` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1374 → 精確 | Accessibility → Switch Control → NEEDS_OVERRIDE_252 → Precise | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier#SelectionStylePrecise` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1374 → 精細 | Accessibility → Switch Control → NEEDS_OVERRIDE_252 → Refined | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier#SelectionStyleRefined` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1374 → 單一 | Accessibility → Switch Control → NEEDS_OVERRIDE_252 → Single | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/AxisSweepIdentifier#SelectionStyleSingle` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 頭部追蹤 → 頭部追蹤 | Accessibility → Switch Control → Head Tracking → Head Tracking | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CameraPointPickerSwitch#CameraPointPickerSwitcher` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 游標顏色 → 游標顏色 | Accessibility → Switch Control → Cursor Color → Cursor Color | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CursorColorIdentifier#CursorColorIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1377 → 新增手勢⋯ | Accessibility → Switch Control → NEEDS_OVERRIDE_255 → Create New Gesture… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomGesturesIdentifier#CreateCustomGesture` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 已儲存的手勢 → 已儲存的手勢 | Accessibility → Switch Control → Saved Gestures → Saved Gestures | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomGesturesIdentifier#CustomGesturesIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 已儲存的手勢 → 新增手勢⋯ | Accessibility → Switch Control → Saved Gestures → Create New Gesture… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomGesturesIdentifier/CreateCustomGesture` | 18.7 | F18 MAN DYLD |  |
| 輔助使用 → 切換控制 → 選單項目 → 選單項目 | Accessibility → Switch Control → Menu Items → Menu Items | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier#CustomizeMenuIdentifier` | 18.7 | F18 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier#Device` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier#Gestures` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier#MediaControls` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier#Settings` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier#TopLevel` | — | GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 裝置 | Accessibility → Switch Control → Menu Items → Device | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Device` | 18.7 | F18 FIFI WDG GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 手勢 | Accessibility → Switch Control → Menu Items → Gestures | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Gestures` | 18.7 | F18 FIFI WDG GH |  |
| — | Accessibility → Switch Control → Menu Items → Media Controls | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Media%20Controls` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 選單項目 → 媒體控制項目 | Accessibility → Switch Control → Menu Items → Media Controls | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/MediaControls` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 設定 | Accessibility → Switch Control → Menu Items → Settings | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Settings` | 18.7 | F18 FIFI WDG GH |  |
| — | Accessibility → Switch Control → Menu Items → Top Level | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Top%20Level` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → 選單項目 → 最上層 | Accessibility → Switch Control → Menu Items → Top Level | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/TopLevel` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 於第一個項目暫停 → 於第一個項目暫停 | Accessibility → Switch Control → Pause on First Item → Pause on First Item | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/DelayAfterInputIdentifier#NumericalPreferenceSwitcherIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 切換控制模式 → 切換控制模式 | Accessibility → Switch Control → Switch Control Mode → Switch Control Mode | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/FirstLaunchScanningModeIdentifier#FirstLaunchScanningModeIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 按住持續時間 → 按住持續時間 | Accessibility → Switch Control → Hold Duration → Hold Duration | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/HoldDurationIdentifier#NumericalPreferenceSwitcherIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 忽略重複 → 忽略重複 | Accessibility → Switch Control → Ignore Repeat → Ignore Repeat | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/IgnoreRepeatIdentifier#NumericalPreferenceSwitcherIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 長時間按下 → 長時間按下 | Accessibility → Switch Control → Long Press → Long Press | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/LongPressIdentifier#NumericalPreferenceSwitcherIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 組合 → 組合 | Accessibility → Switch Control → Recipes → Recipes | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/RecipesIdentifier#RecipesIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 組合 → 新增組合⋯ | Accessibility → Switch Control → Recipes → Create New Recipe… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/RecipesIdentifier/CreateNewRecipe` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 組合 → 啟動組合 | Accessibility → Switch Control → Recipes → Launch Recipe | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/RecipesIdentifier/LaunchRecipe` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 循環 → 循環 | Accessibility → Switch Control → Loops → Loops | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanCyclesIdentifier#ScanCyclesIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1371 → 目前的項目 | Accessibility → Switch Control → NEEDS_OVERRIDE_249 → Current Item | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanLocationIdentifier#ScanAfterTapCurrent` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1371 → 第一個項目 | Accessibility → Switch Control → NEEDS_OVERRIDE_249 → First Item | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanLocationIdentifier#ScanAfterTapFirst` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 點下後在焦點內的項目 → 點下後在焦點內的項目 | Accessibility → Switch Control → Focused Item After Tap → Focused Item After Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanLocationIdentifier#ScanLocationIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 自動掃描時間 → 自動掃描時間 | Accessibility → Switch Control → Auto Scanning Time → Auto Scanning Time | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningSpeedIdentifier#NumericalPreferencePickerGroupIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1365 → 自動掃描 | Accessibility → Switch Control → NEEDS_OVERRIDE_243 → Auto Scanning | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningStyleIdentifier#AUTO_SCANNING_LABEL` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1365 → 單一切換逐步掃描 | Accessibility → Switch Control → NEEDS_OVERRIDE_243 → Single Switch Step Scanning | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningStyleIdentifier#DWELL_SCANNING_LABEL` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1365 → 手動掃描 | Accessibility → Switch Control → NEEDS_OVERRIDE_243 → Manual Scanning | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningStyleIdentifier#MANUAL_SCANNING_LABEL` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 掃描樣式 → 掃描樣式 | Accessibility → Switch Control → Scanning Style → Scanning Style | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/ScanningStyleIdentifier#ScanningStyleIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 語音 → 朗讀時暫停 | Accessibility → Switch Control → Speech → Pause while Speaking | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SpeechIdentifier#SPEECH_PAUSES_SCANNING_LABEL` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 語音 → 朗讀項目屬性 | Accessibility → Switch Control → Speech → Speak Item Attributes | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SpeechIdentifier#SPEECH_SPEAKS_TRAITS_LABEL` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1376 → 朗讀速度 | Accessibility → Switch Control → NEEDS_OVERRIDE_254 → Speaking Rate | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SpeechIdentifier#SpeechRateIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 語音 → 聲音 | Accessibility → Switch Control → Speech → Voices | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SpeechIdentifier#VoicesIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | Accessibility → Switch Control → Speech → Voices | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SpeechIdentifier/VoicesIdentifier` | — | FIFI WDG |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1364 → 新增切換⋯ | Accessibility → Switch Control → NEEDS_OVERRIDE_242 → Add New Switch… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier#AddSwitchIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1364 → 藍牙裝置⋯ | Accessibility → Switch Control → NEEDS_OVERRIDE_242 → Bluetooth Devices… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier#BluetoothDevicesIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 切換 → 切換 | Accessibility → Switch Control → Switches → Switches | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier#SwitchesIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換 → 略過無效的切換設定 | Accessibility → Switch Control → Switches → Ignore Invalid Switch Setup | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier#UpwardsHUDToggleSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換 → 新增切換⋯ | Accessibility → Switch Control → Switches → Add New Switch… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier/AddSwitchIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換 → 藍牙裝置⋯ | Accessibility → Switch Control → Switches → Bluetooth Devices… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier/BluetoothDevicesIdentifier` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1370 → 總是點一下 | Accessibility → Switch Control → NEEDS_OVERRIDE_248 → Always Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/TapBehaviorIdentifier#AlwaysTap` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1370 → 自動點一下 | Accessibility → Switch Control → NEEDS_OVERRIDE_248 → Auto Tap | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/TapBehaviorIdentifier#TapBehaviorAuto` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → NEEDS_OVERRIDE_1370 → 預設值 | Accessibility → Switch Control → NEEDS_OVERRIDE_248 → Default | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/TapBehaviorIdentifier#TapBehaviorDefault` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 切換控制 → 點一下動作 → 點一下動作 | Accessibility → Switch Control → Tap Behavior → Tap Behavior | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/TapBehaviorIdentifier#TapBehaviorIdentifier` | 18.7 | F18 |  |
| 輔助使用 → Siri → 通話掛斷 → 通話掛斷 | Accessibility → Siri → Call Hang Up → Call Hang Up | `prefs:root=ACCESSIBILITY&path=SIRI_SETTINGS_TITLE/SIRI_CALL_HANGUP_ID#SIRI_CALL_HANGUP_ID` | 18.7 | F18 |  |
| 輔助使用 → 聲音辨識 → 音效 → 音效 | Accessibility → Sound Recognition → Sounds → Sounds | `prefs:root=ACCESSIBILITY&path=SOUND_RECOGNITION_TITLE/Sounds#Sounds` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 聲音 → 聲音 | Accessibility → Spoken Content → Voices → Voices | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/QuickSpeakAccents#QuickSpeakAccents` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 反白內容 → 反白顏色 | Accessibility → Spoken Content → Highlight Content → Highlight Colors | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/QuickSpeakHighlight#COLOR_CHOICE` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 反白內容 → 反白內容 | Accessibility → Spoken Content → Highlight Content → Highlight Content | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/QuickSpeakHighlight#QuickSpeakHighlight` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 反白內容 → 句子反白樣式 | Accessibility → Spoken Content → Highlight Content → Sentence Highlight Style | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/QuickSpeakHighlight#SENTENCE_HIGHLIGHT_STYLE` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 語音控制器 → 自訂滑鼠按鈕 | Accessibility → Spoken Content → Speech Controller → Customize Mouse Buttons | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController#CustomizeMouseButtons` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 語音控制器 → 語音控制器 | Accessibility → Spoken Content → Speech Controller → Speech Controller | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController#SpeechController` | 18.7 | F18 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController#SpeechControllerDoubleTapAction` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController#SpeechControllerIdleOpacity` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController#SpeechControllerLongPressAction` | — | GH |  |
| — | Accessibility → Spoken Content → Customize Mouse Buttons | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/CustomizeMouseButtons` | — | FIFI WDG |  |
| 輔助使用 → 語音內容 → 語音控制器 → 點兩下 | Accessibility → Spoken Content → Speech Controller → Double Tap | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/SpeechControllerDoubleTapAction` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 語音控制器 → 閒置不透明度 | Accessibility → Spoken Content → Speech Controller → Idle Opacity | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/SpeechControllerIdleOpacity` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 語音控制器 → 長時間按下 | Accessibility → Spoken Content → Speech Controller → Long Press | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/SpeechControllerLongPressAction` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 預設語言 → 預設語言 | Accessibility → Spoken Content → Default Language → Default Language | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpokenContentDefaultLanguage#SpokenContentDefaultLanguage` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 輸入回饋 → 字元 | Accessibility → Spoken Content → Typing Feedback → Characters | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#LETTER` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 輸入回饋 → 字元提示 | Accessibility → Spoken Content → Typing Feedback → Character Hints | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#PhoneticFeedback` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 輸入回饋 → 按住來朗讀預測字詞 | Accessibility → Spoken Content → Typing Feedback → Hold to Speak Predictions | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#QUICKTYPE_WORD_FEEDBACK` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 輸入回饋 → 朗讀自動文字 | Accessibility → Spoken Content → Typing Feedback → Speak Auto-text | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#SPEAK_AUTOCORRECTIONS` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → Typing Feedback → 字元回饋 | Accessibility → Spoken Content → Typing Feedback → Character Feedback | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#TYPING_FEEDBACK_HEADER` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 輸入回饋 → 輸入回饋 | Accessibility → Spoken Content → Typing Feedback → Typing Feedback | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#TypingFeedback` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 輸入回饋 → 朗讀字詞 | Accessibility → Spoken Content → Typing Feedback → Speak Words | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/TypingFeedback#WORD_FEEDBACK` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 語音內容 → 發音 → 發音 | Accessibility → Spoken Content → Pronunciations → Pronunciations | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/VoiceOverSettings#VoiceOverSettings` | 18.7 | F18 |  |
| 輔助使用 → 字幕與隱藏式字幕 → 樣式 → 樣式 | Accessibility → Subtitles & Captioning → Style → Style | `prefs:root=ACCESSIBILITY&path=SUBTITLES_CAPTIONING/currentTheme#currentTheme` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 | Accessibility → Interaction \| Touch → Dwell Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/#DwellEnabledSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 自訂動作 | Accessibility → Touch → AssistiveTouch → Custom Actions | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#ActionsGroupSpecifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 永遠顯示選單 | Accessibility → Interaction \| Touch → AssistiveTouch → Always Show Menu | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#AlwaysShowMenu` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 顯示螢幕鍵盤 | Accessibility → Interaction \| Touch → AssistiveTouch → Show Onscreen Keyboard | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#AlwaysShowSoftwareKeyboard` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 透過輔助觸控確認 | Accessibility → Interaction \| Touch → AssistiveTouch → Confirm with AssistiveTouch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#APPLE_PAY_SWITCH` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 自訂最上層選單 | Accessibility → Touch → Touch → AssistiveTouch → Customize Top Level Menu | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#AssistiveTouchCustomize` | — | MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 裝置 | Accessibility → Touch → Touch → AssistiveTouch → Devices | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#AssistiveTouchMouseDevices` | — | MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 模擬滑鼠 | Accessibility → Touch → AssistiveTouch → Mouse Keys | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#AssistiveTouchMouseKeys` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 新增手勢⋯ | Accessibility → Touch → AssistiveTouch → Create New Gesture… | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#CreateCustomGesture` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 自訂手勢 | Accessibility → Touch → AssistiveTouch → Custom Gestures | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#CustomGestureHeading` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 點兩下 | Accessibility → Touch → Touch → AssistiveTouch → Double-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DoubleTapSpecifier` | — | MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 後備動作 | Accessibility → Touch → AssistiveTouch → Fallback Action | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellAutorevertSpecifier` | 16.2 | F16 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 熱點 | Accessibility → Touch → AssistiveTouch → Hot Corners | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellCornersSpecifier` | 16.2 | F16 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 停留控制 | Accessibility → Interaction \| Touch → AssistiveTouch → Dwell Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellEnabledSpecifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 擴大預測字詞範圍 | Accessibility → Interaction \| Touch → AssistiveTouch → Extended Predictions | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellExtendedPredictionsSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 停留控制逾時 | Accessibility → Interaction \| Touch → AssistiveTouch → Dwell Control Timeout | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellTimeoutSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 動作誤差 | Accessibility → Touch → AssistiveTouch → Movement Tolerance | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#DwellToleranceSpecifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 使用遊戲控制器 | Accessibility → Interaction \| Touch → AssistiveTouch → Use Game Controller | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#EnableAssistiveTouchGameControllerSpecifier` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 輔助觸控 | Accessibility → Interaction \| Touch → AssistiveTouch → AssistiveTouch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#EnableAssistiveTouchSpecifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 3D觸控 | Accessibility → Interaction \| Touch → AssistiveTouch → 3D Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#ForceTouchSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 閒置不透明度 | Accessibility → Touch → AssistiveTouch → Idle Opacity | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#IdleOpacity` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 長時間按下 | Accessibility → Touch → Touch → AssistiveTouch → Long Press | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#LongPressSpecifier` | — | MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 執行觸控手勢 | Accessibility → Interaction \| Touch → AssistiveTouch → Perform Touch Gestures | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#MouseBehavesLikeFinger` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點按聲 | Accessibility → Interaction \| Touch → AssistiveTouch → Sound on Click | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#MouseClickSounds` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指向裝置 | Accessibility → Touch → AssistiveTouch → Pointer Devices | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#MouseDevicesHeaderTitle` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 聲音動作 | Accessibility → Interaction \| Touch → AssistiveTouch → Sound Actions | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#SOUND_ACTIONS` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 點一下 | Accessibility → Touch → AssistiveTouch → Single-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#TapSpecifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 軌跡敏感度 | Accessibility → Interaction \| Touch → AssistiveTouch → Tracking Sensitivity | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE#TouchSpeed` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 自訂最上層選單 | Accessibility → Interaction \| Touch → AssistiveTouch → Customize Top Level Menu | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchCustomize` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD WDG |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 裝置 | Accessibility → Interaction \| Touch → AssistiveTouch → Devices | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices` | 16.2 · 18.7 | F18 F16 FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 模擬滑鼠 | Accessibility → Interaction \| Touch → AssistiveTouch → Mouse Keys | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseKeys` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 | Accessibility → Touch → AssistiveTouch → Pointer Style | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization` | 16.2 | F16 FIFI MAN MEHDI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 新增手勢⋯ | Accessibility → Interaction \| Touch → AssistiveTouch → Create New Gesture… | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/CreateCustomGesture` | 18.7 | F18 MAN DYLD |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點兩下 | Accessibility → Interaction \| Touch → AssistiveTouch → Double-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DoubleTapSpecifier` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 後備動作 | Accessibility → Interaction \| Touch → AssistiveTouch → Fallback Action | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellAutorevertSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 熱點 | Accessibility → Interaction \| Touch → AssistiveTouch → Hot Corners | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellCornersSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 動作誤差 | Accessibility → Interaction \| Touch → AssistiveTouch → Movement Tolerance | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellToleranceSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 閒置不透明度 | Accessibility → Interaction \| Touch → AssistiveTouch → Idle Opacity | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/IdleOpacity` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 長時間按下 | Accessibility → Interaction \| Touch → AssistiveTouch → Long Press | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/LongPressSpecifier` | 16.2 · 18.7 | F18 F16 |  |
| — | Accessibility → Touch → AssistiveTouch → Movement Tolerance | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/Movement%20Tolerance` | — | FIFI WDG |  |
| — | Accessibility → Touch → AssistiveTouch → Single-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/Single-Tap` | — | FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 聲音動作 | Accessibility → Interaction \| Touch → AssistiveTouch → Sound Actions | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/SOUND_ACTIONS` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點一下 | Accessibility → Interaction \| Touch → AssistiveTouch → Single-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/TapSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 背面輕點 → 背面輕點 | Accessibility → Interaction \| Touch → Back Tap → Back Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/BackTap#BackTap` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 背面輕點 → 點兩下 | Accessibility → Interaction \| Touch → Back Tap → Double Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/BackTap/DoubleTap` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 背面輕點 → 點三下 | Accessibility → Interaction \| Touch → Back Tap → Triple Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/BackTap/TripleTap` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 來電語音傳送 → 來電語音傳送 | Accessibility → Interaction \| Touch → Call Audio Routing → Call Audio Routing | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING#CALL_AUDIO_ROUTING` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1363 → 自動 | Accessibility → Touch → NEEDS_OVERRIDE_241 → Automatic | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING#CALL_AUDIO_ROUTING_AUTOMATIC` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1363 → 藍牙耳機 | Accessibility → Touch → NEEDS_OVERRIDE_241 → Bluetooth Headset | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING#CALL_AUDIO_ROUTING_HEADSET` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1363 → 擴音 | Accessibility → Touch → NEEDS_OVERRIDE_241 → Speaker | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING#CALL_AUDIO_ROUTING_SPEAKER` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1363 → 自動接聽來電 | Accessibility → Touch → NEEDS_OVERRIDE_241 → Auto-Answer Calls | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING#callAudioRoutingAutoAnswer` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 來電語音傳送 → 自動接聽來電 | Accessibility → Interaction \| Touch → Call Audio Routing → Auto-Answer Calls | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING/callAudioRoutingAutoAnswer` | 18.7 | F18 FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 選單追蹤 | Accessibility → Interaction \| Touch → Dwell Control → Menu Follow | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL#AXDwellFollowSpecifierID` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 顯示捲動控制項目 | Accessibility → Interaction \| Touch → Dwell Control → Show Scroll Controls | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL#AXDwellQuickScrollSpecifierID` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 停留控制 | Accessibility → Interaction \| Touch → Dwell Control → Dwell Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL#DWELL_CONTROL_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 反白控制項目 | Accessibility → Interaction \| Touch → Dwell Control → Highlight Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL#DWELL_HIGHLIGHT_CONTROL_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 媒體播放期間暫停 | Accessibility → Interaction \| Touch → Dwell Control → Pause During Media Playback | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL#DWELL_PAUSE_FOR_MEDIA_PLAYBACK_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 目標 | Accessibility → Interaction \| Touch → Dwell Control → Target | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL/DWELL_CONTROL_TARGET` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 停留控制 → 動作誤差 | Accessibility → Interaction \| Touch → Dwell Control → Movement Tolerance | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/DWELL/DWELL_MOVEMENT_TOLERANCE` | 18.7 | F18 |  |
| — | Accessibility → Touch → Touch → Haptic Touch [or 3D & Haptic Touch] | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#FORCE_TOUCH` | — | MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 3D與觸覺回饋觸控 → 3D與觸覺回饋觸控 \| 觸覺回饋觸控 | Accessibility → Interaction \| Touch → 3D & Haptic Touch → 3D & Haptic Touch \| Haptic Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#ForceTouch` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 3D與觸覺回饋觸控 → 3D觸控 | Accessibility → Interaction \| Touch → 3D & Haptic Touch → 3D Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#ForceTouchAccessibilityMainSwitch` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1361 → 3D觸控 | Accessibility → Touch → NEEDS_OVERRIDE_239 → 3D Touch | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#ForceTouchAccessibilityMasterSwitch` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 3D與觸覺回饋觸控 → 3D觸控敏感度 | Accessibility → Interaction \| Touch → 3D & Haptic Touch → 3D Touch Sensitivity | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#FourceTouchSensitivityGroupIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 3D與觸覺回饋觸控 → 3D觸控敏感度與觸控持續時間測試 \| 觸控持續時間測試 | Accessibility → Touch → NEEDS_OVERRIDE_239 → 3D Touch Sensitivity and Touch Duration Test | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#FourceTouchSensitivityTestGroupIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1361 → 快 | Accessibility → Touch → NEEDS_OVERRIDE_239 → Fast | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#HapticTouchFastIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1361 → 慢 | Accessibility → Touch → NEEDS_OVERRIDE_239 → Slow | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#HapticTouchSlowIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 3D與觸覺回饋觸控 → 觸控持續時間 | Accessibility → Interaction \| Touch → 3D & Haptic Touch → Touch Duration | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/ForceTouch#timingGroup` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 捲動速度 | Accessibility → Interaction \| Touch → Pointer Control → Scrolling Speed | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#DeviceScrollSpeed` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 忽略觸控式軌跡板 | Accessibility → Interaction \| Touch → Pointer Control → Ignore Trackpad | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#IgnoreTrackpad` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 自動隱藏 \| 自動隱藏指標 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerAutoHideSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 顏色 | Accessibility → Interaction \| Touch → Pointer Control → Color | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerColorSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 指標控制 | Accessibility → Interaction \| Touch → Pointer Control → Pointer Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerControlEnablingCell` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 指標動畫 | Accessibility → Interaction \| Touch → Pointer Control → Pointer Animations | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerCustomShapes` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 增加對比 | Accessibility → Interaction \| Touch → Pointer Control → Increase Contrast | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerIncreaseContrastSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 觸控式軌跡板慣性 | Accessibility → Interaction \| Touch → Pointer Control → Trackpad Inertia | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerInertia` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 指標大小 | Accessibility → Interaction \| Touch → Pointer Control → Pointer Size | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer#PointerSizeSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 控制 | Accessibility → Interaction \| Touch → Pointer Control → Control | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer/POINTER_CONTROL_CONTROL` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 顏色 | Accessibility → Interaction \| Touch → Pointer Control → Color | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer/PointerColorSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1362 → 使用最終觸控位置 | Accessibility → Touch → NEEDS_OVERRIDE_240 → Use Final Touch Location | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#ACTIVATE_ON_RELEASE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1362 → 使用最初觸控位置 | Accessibility → Touch → NEEDS_OVERRIDE_240 → Use Initial Touch Location | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#ACTIVATE_ON_TOUCH` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 觸控調節 → 按住持續時間 | Accessibility → Interaction \| Touch → Touch Accommodations → Hold Duration | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#HoldDuration` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | Accessibility → Touch → Touch → Touch Accommodations → Hold Duration (jump to section) | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#HoldDurationGroup` | — | MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 觸控調節 → 忽略重複 | Accessibility → Interaction \| Touch → Touch Accommodations → Ignore Repeat | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#IgnoreRepeat` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | Accessibility → Touch → Touch → Touch Accommodations → Ignore Repeat (jump to section) | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#IgnoreRepeatGroup` | — | MAN MEHDI |  |
| 輔助使用 → 觸控 → NEEDS_OVERRIDE_1362 → 關閉 | Accessibility → Touch → NEEDS_OVERRIDE_240 → Off | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#OFF` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 觸控調節 → 輕點輔助 | Accessibility → Interaction \| Touch → Touch Accommodations → Tap Assistance | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#Tap%20Assistance` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 觸控調節 → 觸控調節 | Accessibility → Interaction \| Touch → Touch Accommodations → Touch Accommodations | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/TOUCH_ACCOMMODATIONS#TOUCH_ACCOMMODATIONS_SWITCHER` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 向上看來顯示控制中心 → 「控制中心」的垂直位置 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/UPWARDS_HUD#UpwardsHUDPositionSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 向上看來顯示控制中心 → 向上看來顯示控制中心 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/UPWARDS_HUD#UpwardsHUDToggleSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 活動 → 活動 | Accessibility → VoiceOver → Activities → Activities | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/activities#activities` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Activities → 加入活動⋯ | Accessibility → VoiceOver → Activities → Add Activity… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Activities#New` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Activities → 程式設計 | Accessibility → VoiceOver → Activities → Programming | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Activities#Programming` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → VoiceOver → Activities → Add Activity… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/ACTIVITIES/New` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 活動 → 加入活動⋯ | Accessibility → VoiceOver → Activities → Add Activity… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/activities/New` | 18.7 | F18 |  |
| — | Accessibility → VoiceOver → Activities → Programming | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/ACTIVITIES/Programming` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 活動 → 程式設計 | Accessibility → VoiceOver → Activities → Programming | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/activities/Programming` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 音訊 | Accessibility → VoiceOver → Audio → Audio | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio#Audio` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 音訊迴避 | Accessibility → VoiceOver → Audio → Audio Ducking | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio#AUDIO_DUCKING` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 音訊 → 傳到HDMI | Accessibility → VoiceOver → Audio → Send to HDMI | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio#ROUTE_TO_HDMI` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 音訊 → 通話期間自動選取擴音 | Accessibility → VoiceOver → Audio → Auto-select Speaker in Call | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio#ROUTE_TO_SPEAKER` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 方程式使用聶美茲數學點字 | Accessibility → VoiceOver → Braille → Equations use Nemeth Code | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#ALWAYS_USE_NEMETH` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 移動時翻頁 | Accessibility → VoiceOver → Braille → Turn Pages when Panning | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#AUTO_TURN_PAGES` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 點字 | Accessibility → VoiceOver → Braille → Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#Braille` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 文字格式 | Accessibility → VoiceOver → Braille → Text Formatting | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#BRAILLE_FORMATTING` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 符合輸入和輸出表 | Accessibility → VoiceOver → Braille → Match Input and Output Tables | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#BRAILLE_SYNC_TABLES` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → 輸入 | Accessibility → VoiceOver → VoiceOver → Braille → Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#BrailleDisplayInput` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 輸入和輸出 | Accessibility → VoiceOver → Braille → Input and Output | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#BrailleDisplayOutput` | 18.7 | F18 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → 點字螢幕輸入 | Accessibility → VoiceOver → VoiceOver → Braille → Braille Screen Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#BrailleGesturesInput` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 選擇點字顯示器 | Accessibility → VoiceOver → Braille → Choose a Braille Display | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#DEVICES` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 點字 → 自動轉譯 | Accessibility → VoiceOver → Braille → Automatic Translation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#GRADE2_AUTO_TRANSLATE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 顯示螢幕鍵盤 | Accessibility → VoiceOver → Braille → Show Onscreen Keyboard | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#SHOW_SW_KEYBOARD` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 聲音簾幕 | Accessibility → VoiceOver → Braille → Sound Curtain | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#SOUND_CURTAIN` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → 狀態輸入格 | Accessibility → VoiceOver → Braille → Status Cells | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#STATUS_CELL` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → 點字表 | Accessibility → VoiceOver → Braille → Braille Tables | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#tableIdentifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 啟動時啟用藍牙 | Accessibility → VoiceOver → Braille → Enable Bluetooth on Start | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#voiceOverAlwaysTurnOnBluetooth` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → 點字提示訊息 | Accessibility → VoiceOver → Braille → Braille Alert Messages | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#voiceOverBrailleAlertDisplayDuration` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Braille → 自動前進持續時間 | Accessibility → VoiceOver → Braille → Auto Advance Duration | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#voiceOverBrailleAutoAdvance` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Braille → 忽略組合持續時間 | Accessibility → VoiceOver → Braille → Ignore Chord Duration | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#voiceOverBrailleDebounceTimeout` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 點字 → 自動換行 | Accessibility → VoiceOver → Braille → Word Wrap | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille#WORD_WRAP` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 輸入 | Accessibility → VoiceOver → Braille → Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayInput` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 點字 → 輸出 | Accessibility → VoiceOver → Braille → Output | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayOutput` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 | Accessibility → VoiceOver → Braille → Braille Screen Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 點字 → 狀態輸入格 | Accessibility → VoiceOver → Braille → Status Cells | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 點字 → 點字表 | Accessibility → VoiceOver → Braille → Braille Tables | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/tableIdentifier` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 點字 → 點字提示訊息 | Accessibility → VoiceOver → Braille → Braille Alert Messages | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleAlertDisplayDuration` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 自動前進持續時間 | Accessibility → VoiceOver → Braille → Auto Advance Duration | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleAutoAdvance` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 忽略組合持續時間 | Accessibility → VoiceOver → Braille → Ignore Chord Duration | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleDebounceTimeout` | 18.7 | F18 |  |
| — | Accessibility → VoiceOver → Braille → Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE/BrailleDisplayInput` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Braille → Output | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE/BrailleDisplayOutput` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Braille → Braille Screen Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE/BrailleGesturesInput` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Braille → Status Cells | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE/STATUS_CELL` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Braille → Braille Tables → (root) | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE/tableIdentifier` | — | FIFI WDG |  |
| — | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#BrailleScreenInput` | — | GH |  |
| 輔助使用 → 旁白 → 指令 → 指令 | Accessibility → VoiceOver → Commands → Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#CustomizeCommands` | 18.7 | F18 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#Handwriting` | — | GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#KeyboardShortcuts` | — | GH |  |
| 輔助使用 → 旁白 → 指令 → 重置「旁白」指令 | Accessibility → VoiceOver → Commands → Reset VoiceOver Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#ResetVoiceOverCommands` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 指令 → 切換手勢慣用手 | Accessibility → VoiceOver → Commands → Switch Gesture Handedness | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#SWITCH_GESTURE_HANDEDNESS` | 18.7 | F18 |  |
| — | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands#TouchGestures` | — | GH |  |
| 輔助使用 → 旁白 → 指令 → 所有指令 | Accessibility → VoiceOver → Commands → All Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/AllCommands` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 指令 → 點字鍵盤輸入 | Accessibility → VoiceOver → Commands → Braille Keyboard Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/BrailleKeyboardInput` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 指令 → 點字螢幕輸入 | Accessibility → VoiceOver → Commands → Braille Screen Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/BrailleScreenInput` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 指令 → 手寫 | Accessibility → VoiceOver → Commands → Handwriting | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/Handwriting` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 指令 → 鍵盤快速鍵 | Accessibility → VoiceOver → Commands → Keyboard Shortcuts | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/KeyboardShortcuts` | 18.7 | F18 GH |  |
| — | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/ResetVoiceOverCommands` | — | GH |  |
| 輔助使用 → 旁白 → 指令 → 觸控手勢 | Accessibility → VoiceOver → Commands → Touch Gestures | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/TouchGestures` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 點兩下逾時 → 點兩下逾時 | Accessibility → VoiceOver → Double-tap Timeout → Double-tap Timeout | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/DOUBLE_TAP_INTERVAL_TITLE#NumericalPreferencePickerGroupIdentifier` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 導覽影像 → 導覽影像 | Accessibility → VoiceOver → Navigate Images → Navigate Images | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/IncludeUnlabeledImages#IncludeUnlabeledImages` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Include Unlabeled Images → 永遠 | Accessibility → VoiceOver → Include Unlabeled Images → Always | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/IncludeUnlabeledImages#NAV_IMG_ALWAYS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Include Unlabeled Images → 永不 | Accessibility → VoiceOver → Include Unlabeled Images → Never | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/IncludeUnlabeledImages#NAV_IMG_NEVER` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Include Unlabeled Images → 帶有描述 | Accessibility → VoiceOver → Include Unlabeled Images → With descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/IncludeUnlabeledImages#NAV_IMG_W_DESCRIPTIONS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 導覽樣式 → 導覽樣式 | Accessibility → VoiceOver → Navigation Style → Navigation Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NavigationStyle#NavigationStyle` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 旁白辨識 | Accessibility → VoiceOver → VoiceOver Recognition → VoiceOver Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver#NeuralVoiceOver` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → VoiceOver Recognition → 影像描述 | Accessibility → VoiceOver → VoiceOver Recognition → Image Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver#VO_IMAGE_DESCRIPTIONS` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 文字辨識 | Accessibility → VoiceOver → VoiceOver Recognition → Text Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver#VO_OCR` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → VoiceOver Recognition → 螢幕辨識 | Accessibility → VoiceOver → VoiceOver Recognition → Screen Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver#VO_SCREEN_RECOGNITION` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 回饋樣式 | Accessibility → VoiceOver → VoiceOver Recognition → Feedback Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 | Accessibility → VoiceOver → VoiceOver Recognition → Image Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 即時辨識 | Accessibility → VoiceOver → VoiceOver Recognition → Live Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_REAL_WORLD_DETECTION` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 螢幕辨識 | Accessibility → VoiceOver → VoiceOver Recognition → Screen Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_SCREEN_RECOGNITION` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Quick Settings → 活動 | Accessibility → VoiceOver → Quick Settings → Activities | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Activities` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 音訊迴避 | Accessibility → VoiceOver → Quick Settings → Audio Ducking | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#AudioDucking` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 點字提示訊息 | Accessibility → VoiceOver → Quick Settings → Braille Alert Messages | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#BrailleAlerts` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 點字自動前進 | Accessibility → VoiceOver → Quick Settings → Braille Auto Advance | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#BrailleAutoAdvanceDuration` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 點字輸入 | Accessibility → VoiceOver → Quick Settings → Braille Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#BrailleInput` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 點字輸出 | Accessibility → VoiceOver → Quick Settings → Braille Output | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#BrailleOutput` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 點字表 | Accessibility → VoiceOver → Quick Settings → Braille Tables | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#BrailleTables` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 字幕面板 | Accessibility → VoiceOver → Quick Settings → Caption Panel | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#CaptionPanel` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 直接觸控 | Accessibility → VoiceOver → Quick Settings → Direct Touch | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#DirectTouch` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 手勢方向 | Accessibility → VoiceOver → Quick Settings → Gesture Direction | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#GestureDirection` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 硬體輸入回饋 | Accessibility → VoiceOver → Quick Settings → Hardware Typing Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#HardwareTypingFeedback` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 提示 | Accessibility → VoiceOver → Quick Settings → Hints | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Hints` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 影像描述 | Accessibility → VoiceOver → Quick Settings → Image Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#ImageDescriptions` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 語言 | Accessibility → VoiceOver → Quick Settings → Language | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Language` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 大型游標 | Accessibility → VoiceOver → Quick Settings → Large Cursor | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#LargeCursor` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 媒體描述 | Accessibility → VoiceOver → Quick Settings → Media Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#MediaDescriptions` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 導覽影像 | Accessibility → VoiceOver → Quick Settings → Navigate Images | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#NavigateImages` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 導覽樣式 | Accessibility → VoiceOver → Quick Settings → Navigation Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#NavigationStyle` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 音標回饋 | Accessibility → VoiceOver → Quick Settings → Phonetic Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#PhoneticFeedback` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 音調變更 | Accessibility → VoiceOver → Quick Settings → Pitch Change | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Pitch` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 標點符號 | Accessibility → VoiceOver → Quick Settings → Punctuation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Punctuation` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 快速設定 → 快速設定 | Accessibility → VoiceOver → Quick Settings → Quick Settings | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#QuickSettings` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Quick Settings → 朗讀轉輪確認訊息 | Accessibility → VoiceOver → Quick Settings → Speak Rotor Confirmation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#RotorActionConfirmation` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 螢幕辨識 | Accessibility → VoiceOver → Quick Settings → Screen Recognition | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#ScreenRecognition` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 傳到HDMI | Accessibility → VoiceOver → Quick Settings → Send to HDMI | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#SendToHDMI` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 滑動輸入 | Accessibility → VoiceOver → Quick Settings → Slide to Type | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#SlideToType` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 軟體輸入回饋 | Accessibility → VoiceOver → Quick Settings → Software Typing Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#SoftwareTypingFeedback` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 聲音 | Accessibility → VoiceOver → Quick Settings → Sounds | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Sounds` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 朗讀速度 | Accessibility → VoiceOver → Quick Settings → Speaking Rate | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#SpeakingRate` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 永遠朗讀通知 | Accessibility → VoiceOver → Quick Settings → Always Speak Notifications | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#SpeakNotifications` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 輸入樣式 | Accessibility → VoiceOver → Quick Settings → Typing Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#TypingStyle` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → Quick Settings → 音量 | Accessibility → VoiceOver → Quick Settings → Volume | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/QuickSettings#Volume` | 16.2 | F16 |  |
| — | Accessibility → VoiceOver → VoiceOver → Rotor Actions → Edit Apps on Home Screen | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/ROTOR_ACTIONS#EDIT_APPS_ACTION` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → Rotor Actions → 直接觸控App | Accessibility → VoiceOver → Rotor Actions → Direct Touch Apps | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions#apps` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 轉輪 → 編輯主畫面上的App | Accessibility → VoiceOver → Rotor → Edit Apps on Home Screen | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions#editApps` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 轉輪 → 轉輪 | Accessibility → VoiceOver → Rotor → Rotor | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions#RotorActions` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 轉輪 → 以項目更改轉輪 | Accessibility → VoiceOver → Rotor → Change Rotor with Item | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions#STICKY_ROTOR_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 轉輪 → 直接觸控App | Accessibility → VoiceOver → Rotor → Direct Touch Apps | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions/apps` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 轉輪 → 轉輪項目 | Accessibility → VoiceOver → Rotor → Rotor Items | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions/WebRotor` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Speech → 聲音 | Accessibility → VoiceOver → Speech → Voice | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Speech#DialectCell` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → VoiceOver → Typing → Keyboard Interaction Time | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TYPING_OPTIONS/Keyboard%20Interaction%20Time` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Typing → Modifier Keys | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TYPING_OPTIONS/Modifier%20Keys` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Typing → Phonetic Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TYPING_OPTIONS/Phonetic%20Feedback` | — | FIFI WDG |  |
| — | Accessibility → VoiceOver → Typing → Typing Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TYPING_OPTIONS/Typing%20Style` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → Typing → 鍵盤互動時間 | Accessibility → VoiceOver → Typing → Keyboard Interaction Time | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions#KEYBOARD_TIMING_TIMEOUT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → 變更鍵 | Accessibility → VoiceOver → VoiceOver → Typing → Modifier Keys | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions#MODIFIER_KEYS` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → 音標回饋 | Accessibility → VoiceOver → VoiceOver → Typing → Phonetic Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions#PHONETICS_TITLE` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → 輸入回饋 | Accessibility → VoiceOver → Typing → Typing Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions#TYPING_FEEDBACK` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → 輸入樣式 | Accessibility → VoiceOver → VoiceOver → Typing → Typing Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions#TYPING_MODE_TITLE` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → 輸入 → 輸入 | Accessibility → VoiceOver → Typing → Typing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions#TypingOptions` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 輸入 → 鍵盤互動時間 | Accessibility → VoiceOver → Typing → Keyboard Interaction Time | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/KEYBOARD_TIMING_TIMEOUT` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 輸入 → 變更鍵 | Accessibility → VoiceOver → Typing → Modifier Keys | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/MODIFIER_KEYS` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 輸入 → 音標回饋 | Accessibility → VoiceOver → Typing → Phonetic Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/PHONETICS_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → Typing → Typing Style | Accessibility → VoiceOver → Typing → Typing Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/Typing%20Style` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 輸入 → 輸入回饋 | Accessibility → VoiceOver → Typing → Typing Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/TYPING_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 輸入 → 輸入樣式 | Accessibility → VoiceOver → Typing → Typing Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/TYPING_MODE_TITLE` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 詳細程度 → 朗讀確認訊息 | Accessibility → VoiceOver → Verbosity → Speak Confirmation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#ACTION_CONFIRMATION` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 表情符號後綴 | Accessibility → VoiceOver → Verbosity → Emoji Suffix | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#EMOJI_SUFFIX` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 朗讀提示 | Accessibility → VoiceOver → Verbosity → Speak Hints | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#HINTS_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 橫列與直欄編號 | Accessibility → VoiceOver → Verbosity → Row & Column Numbers | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#SPEAK_TABLE_ROW_COLUMN` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 表格標題 | Accessibility → VoiceOver → Verbosity → Table Headers | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#speakTableHeader` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 詳細程度 → 詳細程度 | Accessibility → VoiceOver → Verbosity → Verbosity | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#Verbosity` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → App懸浮回饋 | Accessibility → VoiceOver → Verbosity → App Hover Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#voiceOverAppHoverFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 輸入回饋 | Accessibility → VoiceOver → Verbosity → Input Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#voiceOverInputFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Verbosity → 媒體描述 | Accessibility → VoiceOver → VoiceOver → Verbosity → Media Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#voiceOverMediaDescriptions` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → Verbosity → 標點符號 | Accessibility → VoiceOver → Verbosity → Punctuation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity#voiceOverPunctuationGroup` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 詳細程度 → 預測字詞回饋 | Accessibility → VoiceOver → Verbosity → Predictive Text Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/PREDICTIVE_TEXT_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 系統通知 | Accessibility → VoiceOver → Verbosity → System Notifications | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/SystemNotifications` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 動作 | Accessibility → VoiceOver → Verbosity → Actions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverActionsFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 大寫字母 | Accessibility → VoiceOver → Verbosity → Capital Letters | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverCapitalLetterFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 容器描述 | Accessibility → VoiceOver → Verbosity → Container Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverContainerOutputFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 刪除文字 | Accessibility → VoiceOver → Verbosity → Deleting Text | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverDeletionFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 表情符號 | Accessibility → VoiceOver → Verbosity → Emoji | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverEmojiFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 手電筒通知 | Accessibility → VoiceOver → Verbosity → Flashlight Notifications | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverFlashlightNotificationsEnabled` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 連結 | Accessibility → VoiceOver → Verbosity → Links | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverLinkFeedback` | 18.7 | F18 |  |
| — | Accessibility → VoiceOver → Braille → Verbosity → Punctuation → Media Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/VERBOSITY/voiceOverMediaDescriptions` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 詳細程度 → 媒體描述 | Accessibility → VoiceOver → Verbosity → Media Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMediaDescriptions` | 16.2 · 18.7 | F18 F16 |  |
| 輔助使用 → 旁白 → 詳細程度 → 更多內容 | Accessibility → VoiceOver → Verbosity → More Content | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMoreContentOutputFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 數字 | Accessibility → VoiceOver → Verbosity → Numbers | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverNumberFeedback` | 18.7 | F18 |  |
| — | Accessibility → VoiceOver → Braille → Verbosity → Punctuation → (root) | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/VERBOSITY/voiceOverPunctuationGroup` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 | Accessibility → VoiceOver → Verbosity → Punctuation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 快速導覽宣告 | Accessibility → VoiceOver → Verbosity → QuickNav Announcements | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverQuickNavAnnouncementFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 網頁轉輪摘要 | Accessibility → VoiceOver → Verbosity → Web Rotor Summary | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverRotorSummaryFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 → 加入轉輪聲音⋯ | Accessibility → VoiceOver → Speech → Add Rotor Voice… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices#ADD_NEW_VOICE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 → 偵測語言 | Accessibility → VoiceOver → Speech → Detect Languages | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices#LANGUAGE_DETECTION` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 → 音高變更 | Accessibility → VoiceOver → Speech → Pitch Change | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices#PITCH_CHANGES_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 → 空間化語音 | Accessibility → VoiceOver → Speech → Spatialize Speech | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices#SPATIALIZE_SPEECH` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 → 發音 | Accessibility → VoiceOver → Speech → Pronunciations | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices/PRONUNCIATION_DICTIONARY` | 18.7 | F18 |  |
| — | Accessibility → Zoom → Zoom → Zoom Filter → Grayscale | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomFilter#Grayscale` | — | MEHDI |  |
| — | Accessibility → Zoom → Zoom → Zoom Filter → Inverted | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomFilter#Inverted` | — | MEHDI |  |
| — | Accessibility → Zoom → Zoom → Zoom Filter → None | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomFilter#None` | — | MEHDI |  |
| 輔助使用 → 縮放 → 縮放濾鏡 → 縮放濾鏡 | Accessibility → Zoom → Zoom Filter → Zoom Filter | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomFilter#ZoomFilter` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 鍵盤快速鍵 | Accessibility → Zoom → Keyboard Shortcuts → Keyboard Shortcuts | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomEnableKeyboardShortcuts` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 調整縮放層級 | Accessibility → Zoom → Keyboard Shortcuts → Adjust Zoom Level | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutAdjustZoomLevel` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 移動縮放視窗 | Accessibility → Zoom → Keyboard Shortcuts → Move Zoom Window | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutPanZoom` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 調整縮放視窗大小 | Accessibility → Zoom → Keyboard Shortcuts → Resize Zoom Window | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutResizeZoomWindow` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 透過滾輪縮放 | Accessibility → Zoom → Keyboard Shortcuts → Zoom with Scroll Wheel | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutScrollWheel` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 切換縮放區域 | Accessibility → Zoom → Keyboard Shortcuts → Switch Zoom Region | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutSwitchZoomMode` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 暫時切換縮放 | Accessibility → Zoom → Keyboard Shortcuts → Temporarily Toggle Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutTempToggleZoom` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 鍵盤快速鍵 → 切換縮放 | Accessibility → Zoom → Keyboard Shortcuts → Toggle Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomKeyboardShortcuts#ZoomKeyboardShortcutToggleZoom` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → Zoom Region → 全螢幕縮放 | Accessibility → Zoom → Zoom Region → Full Screen Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomLensMode#Fullscreen` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → Zoom Region → 視窗縮放 | Accessibility → Zoom → Zoom Region → Window Zoom | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomLensMode#Window` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 縮放 → 縮放區域 → 縮放區域 | Accessibility → Zoom → Zoom Region → Zoom Region | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomLensMode#ZoomLensMode` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 顯示控制器 | Accessibility → Zoom → Zoom Controller → Show Controller | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug#ZOOM_DETACH_CONTROLS` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 調整縮放層級 | Accessibility → Zoom → Zoom Controller → Adjust Zoom Level | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug#ZOOM_TAP_AND_SLIDE_TO_ADJUST_ZOOM_LEVEL` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 縮放控制器 | Accessibility → Zoom → Zoom Controller → Zoom Controller | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug#ZoomSlug` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 顏色 | Accessibility → Zoom → Zoom Controller → Color | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/CONTROLLER_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 點兩下 | Accessibility → Zoom → Zoom Controller → Double-Tap | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_CONTROLLER_ACTION_DOUBLE_TAP` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 點一下 | Accessibility → Zoom → Zoom Controller → Single-Tap | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_CONTROLLER_ACTION_SINGLE_TAP` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 點三下 | Accessibility → Zoom → Zoom Controller → Triple-Tap | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_CONTROLLER_ACTION_TRIPLE_TAP` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 閒置不透明度 | Accessibility → Zoom → Zoom Controller → Idle Opacity | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_IDLE_SLUG_OPACITY` | 18.7 | F18 |  |
| 輔助使用 → 音訊與視覺 → 背景聲音 → 聲音 → 聲音 | Accessibility → Audio & Visual → Background Sounds → Sound → Sound | `prefs:root=ACCESSIBILITY&path=AUDIO_VISUAL_TITLE/AXCSEnableSpecID/ComfortSoundSoundLabel#ComfortSoundSoundLabel` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 新增指令 → 新增指令 | Accessibility → Voice Control → Commands → Create New Command → Create New Command | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/CreateNewCommand#CreateNewCommand` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 指令 → 輸入自訂指令 → 輸入自訂指令 | Accessibility → Voice Control → Commands → Import Custom Commands → Import Custom Commands | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_COMMANDS/ImportCustomCommands#ImportCustomCommands` | 18.7 | F18 |  |
| 輔助使用 → 語音控制 → 詞彙 → 詞彙 → 詞彙 | Accessibility → Voice Control → Vocabulary → Vocabulary → Vocabulary | `prefs:root=ACCESSIBILITY&path=CommandAndControlTitle/COMMAND_AND_CONTROL_VOCABULARY/VOCABULARY#VOCABULARY` | 18.7 | F18 |  |
| 輔助使用 → 引導使用模式 → 時間限制 → 提示聲 → 提示聲 | Accessibility → Guided Access → Time Limits → Sound → Sound | `prefs:root=ACCESSIBILITY&path=GUIDED_ACCESS_TITLE/GuidedAccessTimeRestrictionsLinkList/GUIDED_ACCESS_TIME_RESTRICTIONS_SOUND_TITLE#GUIDED_ACCESS_TIME_RESTRICTIONS_SOUND_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 指令 → 指令 | Accessibility → Keyboards & Typing → Full Keyboard Access → Commands → Commands | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKACommands#FKACommands` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 顏色 → 顏色 | Accessibility → Keyboards & Typing → Full Keyboard Access → Color → Color | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKAFocusRingColor#FKAFocusRingColor` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 全面鍵盤操控 → 自動隱藏 → 自動隱藏 | Accessibility → Keyboards & Typing → Full Keyboard Access → Auto-Hide → Auto-Hide | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/FULL_KEYBOARD_ACCESS/FKAFocusRingTimeout#FKAFocusRingTimeout` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 大小 → 大小 | Accessibility → Keyboards & Typing → Hover Typing → Size → Size | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING/HoverTextSize#HoverTextSize` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 顯示模式 → 顯示模式 | Accessibility → Keyboards & Typing → Hover Typing → Display Mode → Display Mode | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING/HoverTextTypingDisplayMode#HoverTextTypingDisplayMode` | 18.7 | F18 |  |
| 輔助使用 → 鍵盤與輸入 → 懸浮輸入 → 字體 → 字體 | Accessibility → Keyboards & Typing → Hover Typing → Font → Font | `prefs:root=ACCESSIBILITY&path=KEYBOARDS/HOVER_TYPING/HoverTypingStyle#HoverTypingStyle` | 18.7 | F18 |  |
| 輔助使用 → 即時字幕 → 外觀 → 粗體文字 → 粗體文字 | Accessibility → Live Captions → Appearance → Bold Text → Bold Text | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE/ENHANCE_TEXT_LEGIBILITY#ENHANCE_TEXT_LEGIBILITY` | 18.7 | F18 GH |  |
| 輔助使用 → 即時字幕 → 外觀 → 文字大小 → 文字大小 | Accessibility → Live Captions → Appearance → Text Size → Text Size | `prefs:root=ACCESSIBILITY&path=LIVE_TRANSCRIPTION/LIVE_TRANSCRIPTION_APPEARANCE/LARGER_TEXT#LARGER_TEXT` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 已儲存的手勢 → 新增手勢⋯ → 新增手勢⋯ | — | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomGesturesIdentifier/CreateCustomGesture#CreateCustomGesture` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 選單項目 → 裝置 → 裝置 | Accessibility → Switch Control → Menu Items → Device → Device | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Device#Device` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 手勢 → 手勢 | Accessibility → Switch Control → Menu Items → Gestures → Gestures | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Gestures#Gestures` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 媒體控制項目 → 媒體控制項目 | Accessibility → Switch Control → Menu Items → Media Controls → Media Controls | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/MediaControls#MediaControls` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 設定 → 設定 | Accessibility → Switch Control → Menu Items → Settings → Settings | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/Settings#Settings` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 選單項目 → 最上層 → 最上層 | Accessibility → Switch Control → Menu Items → Top Level → Top Level | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/CustomizeMenuIdentifier/TopLevel#TopLevel` | 18.7 | F18 GH |  |
| 輔助使用 → 切換控制 → 組合 → 新增組合⋯ → 新增組合⋯ | Accessibility → Switch Control → Recipes → Create New Recipe… → Create New Recipe… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/RecipesIdentifier/CreateNewRecipe#CreateNewRecipe` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 組合 → 啟動組合 → 啟動組合 | Accessibility → Switch Control → Recipes → Launch Recipe → Launch Recipe | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/RecipesIdentifier/LaunchRecipe#LaunchRecipe` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換 → 新增切換⋯ → 新增切換⋯ | Accessibility → Switch Control → Switches → Add New Switch… → Add New Switch… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier/AddSwitchIdentifier#AddSwitchIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 切換控制 → 切換 → 藍牙裝置⋯ → 藍牙裝置⋯ | Accessibility → Switch Control → Switches → Bluetooth Devices… → Bluetooth Devices… | `prefs:root=ACCESSIBILITY&path=ScannerSwitchTitle/SwitchesIdentifier/BluetoothDevicesIdentifier/BluetoothDevicesIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 語音內容 → 語音控制器 → 點兩下 → 點兩下 | Accessibility → Spoken Content → Speech Controller → Double Tap → Double Tap | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/SpeechControllerDoubleTapAction#SpeechControllerDoubleTapAction` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 語音控制器 → 閒置不透明度 → 閒置不透明度 | Accessibility → Spoken Content → Speech Controller → Idle Opacity → Idle Opacity | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/SpeechControllerIdleOpacity#SpeechControllerIdleOpacity` | 18.7 | F18 GH |  |
| 輔助使用 → 語音內容 → 語音控制器 → 長時間按下 → 長時間按下 | Accessibility → Spoken Content → Speech Controller → Long Press → Long Press | `prefs:root=ACCESSIBILITY&path=SPEECH_TITLE/SpeechController/SpeechControllerLongPressAction#SpeechControllerLongPressAction` | 18.7 | F18 GH |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 自訂最上層選單 → 自訂最上層選單 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchCustomize#AssistiveTouchCustomize` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 自訂最上層選單 → 點一下圖像來更改： | Accessibility → Touch → AssistiveTouch → Customize Top Level Menu → Tap an icon to change: | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchCustomize#ASTStepperCell` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → Customize Top Level Menu → 重置⋯ | Accessibility → Touch → AssistiveTouch → Customize Top Level Menu → Reset… | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchCustomize#Reset` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 裝置 → 裝置 | Accessibility → Interaction \| Touch → AssistiveTouch → Devices → Devices | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices#AssistiveTouchMouseDevices` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → Devices → 藍牙裝置⋯ | Accessibility → Touch → AssistiveTouch → Devices → Bluetooth Devices… | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices#BluetoothDevicesScanning` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → Touch → AssistiveTouch → Devices → Bluetooth Devices… | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices/Bluetooth%20Devices%E2%80%A6` | — | FIFI WDG |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 裝置 → 藍牙裝置⋯ | Accessibility → Interaction \| Touch → AssistiveTouch → Devices → Bluetooth Devices… | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices/BluetoothDevicesScanning` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 模擬滑鼠 → 模擬滑鼠 | Accessibility → Interaction \| Touch → AssistiveTouch → Mouse Keys → Mouse Keys | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseKeys#AssistiveTouchMouseKeys` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 模擬滑鼠 → 開始前的延遲 | Accessibility → Interaction \| Touch → AssistiveTouch → Mouse Keys → Initial Delay | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseKeys#InitialDelay` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 模擬滑鼠 → 最快速度 | Accessibility → Interaction \| Touch → AssistiveTouch → Mouse Keys → Maximum Speed | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseKeys#MaximumSpeed` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 模擬滑鼠 → Option鍵切換 | Accessibility → Interaction \| Touch → AssistiveTouch → Mouse Keys → Option Key Toggle | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseKeys#OptionKeyToggle` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 模擬滑鼠 → 使用主要鍵盤 | Accessibility → Interaction \| Touch → AssistiveTouch → Mouse Keys → Use Primary Keyboard | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseKeys#UsePrimaryKeyboard` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → 顏色 | Accessibility → Touch → AssistiveTouch → Pointer Style → Color | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization#MOUSE_POINTER_COLOR` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → 大小 | Accessibility → Touch → AssistiveTouch → Pointer Style → Size | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization#MOUSE_POINTER_SIZE_TITLE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → 自動隱藏 | Accessibility → Touch → AssistiveTouch → Pointer Style → Auto-Hide | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization#MOUSE_POINTER_TIMEOUT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → 視覺 | Accessibility → Touch → AssistiveTouch → Pointer Style → Visual | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization#MOUSE_POINTER_VISUAL_APPEARANCE` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → Touch → AssistiveTouch → Pointer Style → Auto-Hide | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization/Auto-Hide` | — | FIFI WDG |  |
| — | Accessibility → Touch → AssistiveTouch → Pointer Style → Color → (root) | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization/Color` | — | FIFI WDG |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → SOMETHING IDK | Accessibility → Touch → AssistiveTouch → Pointer Style → SOMETHING IDK | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization/MOUSE_POINTER_COLOR` | 16.2 | F16 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 邊線 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Border | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID#BORDER` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 自然捲動 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID#NATURAL_SCROLLING` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 捲動速度 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Scroll Speed | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID#SCROLL_SPEED_SLIDER` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 軌跡速度 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Tracking Speed | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID#TRACKING_SPEED_SLIDER` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 觸控式軌跡板 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Trackpad | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID#TRACKPAD` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 邊線 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Border | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/BORDER` | 18.7 | F18 MAN |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 觸控式軌跡板 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Trackpad | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/TRACKPAD` | 18.7 | F18 MAN |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 新增手勢⋯ → 新增手勢⋯ | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/CreateCustomGesture#CreateCustomGesture` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → Double-Tap → 點兩下逾時 | Accessibility → Touch → AssistiveTouch → Double-Tap → Double-tap Timeout | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DoubleTapSpecifier#ASTDoubleTapTimeoutSpecifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點兩下 → 點兩下 | Accessibility → Interaction \| Touch → AssistiveTouch → Double-Tap → Double-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DoubleTapSpecifier#DoubleTapSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點兩下 → 點兩下逾時 | Accessibility → Interaction \| Touch → AssistiveTouch → Double-Tap → Double-tap Timeout | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DoubleTapSpecifier/ASTDoubleTapTimeoutSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 後備動作 → 後備動作 | Accessibility → Interaction \| Touch → AssistiveTouch → Fallback Action → Fallback Action | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellAutorevertSpecifier#DwellAutorevertSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 熱點 → 左下 | Accessibility → Interaction \| Touch → AssistiveTouch → Hot Corners → Bottom Left | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellCornersSpecifier#BottomLeft` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 熱點 → 右下 | Accessibility → Interaction \| Touch → AssistiveTouch → Hot Corners → Bottom Right | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellCornersSpecifier#BottomRight` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 熱點 → 熱點 | Accessibility → Interaction \| Touch → AssistiveTouch → Hot Corners → Hot Corners | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellCornersSpecifier#DwellCornersSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 熱點 → 左上 | Accessibility → Interaction \| Touch → AssistiveTouch → Hot Corners → Top Left | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellCornersSpecifier#TopLeft` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 熱點 → 右上 | Accessibility → Interaction \| Touch → AssistiveTouch → Hot Corners → Top Right | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellCornersSpecifier#TopRight` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 動作誤差 → 動作誤差 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DwellToleranceSpecifier#DwellToleranceSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 閒置不透明度 → 閒置不透明度 | Accessibility → Interaction \| Touch → AssistiveTouch → Idle Opacity → Idle Opacity | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/IdleOpacity#IdleOpacity` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → Long Press → 長時間按下持續時間 | Accessibility → Touch → AssistiveTouch → Long Press → Long Press Duration | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/LongPressSpecifier#ASTLongPressDurationSpecifier` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 長時間按下 → 長時間按下 | Accessibility → Interaction \| Touch → AssistiveTouch → Long Press → Long Press | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/LongPressSpecifier#LongPressSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 長時間按下 → 長時間按下持續時間 | Accessibility → Interaction \| Touch → AssistiveTouch → Long Press → Long Press Duration | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/LongPressSpecifier/ASTLongPressDurationSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點一下 → 點一下 | Accessibility → Interaction \| Touch → AssistiveTouch → Single-Tap → Single-Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/TapSpecifier#TapSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 背面輕點 → 點兩下 → 點兩下 | Accessibility → Interaction \| Touch → Back Tap → Double Tap → Double Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/BackTap/DoubleTap#DoubleTap` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 背面輕點 → 點三下 → 點三下 | Accessibility → Interaction \| Touch → Back Tap → Triple Tap → Triple Tap | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/BackTap/TripleTap#TripleTap` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 來電語音傳送 → 自動接聽來電 → 自動接聽來電 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/CALL_AUDIO_ROUTING/callAudioRoutingAutoAnswer#callAudioRoutingAutoAnswer` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 指標控制 → 顏色 → 邊線寬度 | Accessibility → Interaction \| Touch → Pointer Control → Color → Border Width | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/Pointer/PointerColorSpecifier#PointerStrokeWidth` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 活動 → 加入活動⋯ → 加入活動⋯ | Accessibility → VoiceOver → Activities → Add Activity… → Add Activity… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/activities/New#New` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 活動 → 程式設計 → 程式設計 | Accessibility → VoiceOver → Activities → Programming → Programming | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/activities/Programming#Programming` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 旁白音效 \| 旁白音效與觸覺回饋 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSounds` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → App回饋 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → App Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSOutputEventCategory.AppFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 點字 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSOutputEventCategory.Braille` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 互動 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → Interaction | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSOutputEventCategory.Interaction` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 系統 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → System | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSOutputEventCategory.System` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 文字編輯 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → Text Editing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSOutputEventCategory.TextEditing` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 旁白回饋 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → VoiceOver Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSOutputEventCategory.VoiceOverFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 音訊 → 旁白音效與觸覺回饋 → 音效 | Accessibility → VoiceOver → Audio → VoiceOver Sounds & Haptics → Sounds | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Audio/VOSounds#VOSSettingsItem.Sounds` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 輸入 → 輸入 | Accessibility → VoiceOver → Braille → Input → Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayInput#BrailleDisplayInput` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → Input → 收縮的點字法 | Accessibility → VoiceOver → Braille → Input → Contracted Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayInput#ContractedBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Input → 未收縮的8點點字法 | Accessibility → VoiceOver → Braille → Input → Uncontracted Eight-dot Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayInput#EightDotBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Input → 自動轉譯 | Accessibility → VoiceOver → Braille → Input → Automatic Translation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayInput#GRADE2_AUTO_TRANSLATE` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Input → 未收縮的6點點字法 | Accessibility → VoiceOver → Braille → Input → Uncontracted Six-dot Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayInput#SixDotBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 輸出 → 輸出 | Accessibility → VoiceOver → Braille → Output → Output | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayOutput#BrailleDisplayOutput` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → Output → 收縮的點字法 | Accessibility → VoiceOver → Braille → Output → Contracted Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayOutput#ContractedBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Output → 未收縮的8點點字法 | Accessibility → VoiceOver → Braille → Output → Uncontracted Eight-dot Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayOutput#EightDotBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Output → 未收縮的6點點字法 | Accessibility → VoiceOver → Braille → Output → Uncontracted Six-dot Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleDisplayOutput#SixDotBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 編輯文字時自動開始 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#AUTO_ACTIVATE_ON_TEXT_FIELDS` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 點字螢幕輸入 | Accessibility → VoiceOver → Braille → Braille Screen Input → Braille Screen Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#BrailleGesturesInput` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 選擇點字表 | Accessibility → VoiceOver → Braille → Braille Screen Input → Choose a Braille Table | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#BSI_TABLES` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → Braille Screen Input → 收縮的點字法 | Accessibility → VoiceOver → Braille → Braille Screen Input → Contracted Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#ContractedBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 保持啟用直到關閉 | Accessibility → VoiceOver → Braille → Braille Screen Input → Keep Active until Dismissed | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#CONTROL_DEVICE_USING_BRAILLE_GESTURE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 視覺文字回饋 | Accessibility → VoiceOver → Braille → Braille Screen Input → Visual Text Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#DISPLAY_ENTERED_TEXT` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → Braille Screen Input → 未收縮的8點點字法 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#EightDotBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 反向點位置 | Accessibility → VoiceOver → Braille → Braille Screen Input → Reverse Dot Positions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#SHOULD_REVERSE_DOTS` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Braille Screen Input → 未收縮的6點點字法 | Accessibility → VoiceOver → Braille → Braille Screen Input → Uncontracted Six-dot Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#SixDotBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 模式宣告 | Accessibility → VoiceOver → Braille → Braille Screen Input → Mode Announcements | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#SOUND_OPTION` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 輸入回饋 | Accessibility → VoiceOver → Braille → Braille Screen Input → Typing Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#TYPING_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 聲音 | Accessibility → VoiceOver → Braille → Braille Screen Input → Sound | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#USE_HAPTIC_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字螢幕輸入 → 聲音 | Accessibility → VoiceOver → Braille → Braille Screen Input → Sound | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/BrailleGesturesInput#USE_TYPING_SOUND_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 狀態輸入格 → 狀態輸入格 | Accessibility → VoiceOver → Braille → Status Cells → Status Cells | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL#STATUS_CELL` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Braille → Status Cell → 左 | Accessibility → VoiceOver → Braille → Status Cell → Left | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL#STATUS_CELL_LEFT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 狀態輸入格 → 狀態輸入格位置 | Accessibility → VoiceOver → Braille → Status Cells → Status Cells Position | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL#STATUS_CELL_POSITION` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Status Cell → 右 | Accessibility → VoiceOver → Braille → Status Cell → Right | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL#STATUS_CELL_RIGHT` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 狀態輸入格 → 顯示一般狀態 | Accessibility → VoiceOver → Braille → Status Cells → Show General Status | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL#StatusCellGeneral` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 點字 → 狀態輸入格 → 顯示文字狀態 | Accessibility → VoiceOver → Braille → Status Cells → Show Text Status | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/STATUS_CELL#StatusCellTextStyle` | 16.2 · 18.7 | F18 F16 MAN MEHDI |  |
| — | Accessibility → VoiceOver → VoiceOver → Braille → Braille Tables → Add Braille Table | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/tableIdentifier#ADD_NEW_BRAILLE_LANGUAGE` | — | MAN MEHDI |  |
| 輔助使用 → 旁白 → Braille → Tables → 加入點字表⋯ | Accessibility → VoiceOver → Braille → Tables → Add Braille Table… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/tableIdentifier#ADD_NEW_BRAILLE_LANGUAGE_TITLE` | 16.2 | F16 |  |
| 輔助使用 → 旁白 → 點字 → 點字表 → 點字表 | Accessibility → VoiceOver → Braille → Braille Tables → Braille Tables | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/tableIdentifier#tableIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字表 → 加入點字表⋯ | Accessibility → VoiceOver → Braille → Braille Tables → Add Braille Table… | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/tableIdentifier/ADD_NEW_BRAILLE_LANGUAGE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字提示訊息 → 顯示直到關閉 | Accessibility → VoiceOver → Braille → Braille Alert Messages → Show until Dismissed | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleAlertDisplayDuration#NumericalPreferenceInfiniteTimeDurationIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字提示訊息 → 點字提示訊息 | Accessibility → VoiceOver → Braille → Braille Alert Messages → Braille Alert Messages | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleAlertDisplayDuration#NumericalPreferenceSwitcherIdentifier` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字提示訊息 → 點字提示訊息 | Accessibility → VoiceOver → Braille → Braille Alert Messages → Braille Alert Messages | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleAlertDisplayDuration#voiceOverBrailleAlertDisplayDuration` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 自動前進持續時間 → 自動前進持續時間 | Accessibility → VoiceOver → Braille → Auto Advance Duration → Auto Advance Duration | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleAutoAdvance#voiceOverBrailleAutoAdvance` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 忽略組合持續時間 → 忽略組合持續時間 | Accessibility → VoiceOver → Braille → Ignore Chord Duration → Ignore Chord Duration | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/voiceOverBrailleDebounceTimeout/voiceOverBrailleDebounceTimeout` | 18.7 | F18 |  |
| — | Accessibility → VoiceOver → Braille → Braille Tables → Language | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/BRAILLE_TITLE/tableIdentifier/DefaultLanguage` | — | FIFI WDG |  |
| 輔助使用 → 旁白 → 指令 → 所有指令 → 所有指令 | Accessibility → VoiceOver → Commands → All Commands → All Commands | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/AllCommands#AllCommands` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 指令 → 點字鍵盤輸入 → 點字鍵盤輸入 | Accessibility → VoiceOver → Commands → Braille Keyboard Input → Braille Keyboard Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/BrailleKeyboardInput#BrailleKeyboardInput` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 指令 → 點字螢幕輸入 → 點字螢幕輸入 | Accessibility → VoiceOver → Commands → Braille Screen Input → Braille Screen Input | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/BrailleScreenInput#BrailleScreenInput` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 指令 → 手寫 → 手寫 | Accessibility → VoiceOver → Commands → Handwriting → Handwriting | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/Handwriting#Handwriting` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 指令 → 鍵盤快速鍵 → 鍵盤快速鍵 | Accessibility → VoiceOver → Commands → Keyboard Shortcuts → Keyboard Shortcuts | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/KeyboardShortcuts#KeyboardShortcuts` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 指令 → 觸控手勢 → 觸控手勢 | Accessibility → VoiceOver → Commands → Touch Gestures → Touch Gestures | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/CustomizeCommands/TouchGestures#TouchGestures` | 18.7 | F18 GH |  |
| 輔助使用 → 旁白 → 旁白辨識 → 回饋樣式 → 回饋樣式 | Accessibility → VoiceOver → VoiceOver Recognition → Feedback Style → Feedback Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_FEEDBACK#VO_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 → 敏感性內容輸出 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS#SensitiveContentGroup` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 → 影像描述 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS#VO_IMAGE_DESCRIPTIONS` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 → 其他語言 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS/AdditionalLanguages` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 → 套用到App | Accessibility → VoiceOver → VoiceOver Recognition → Image Descriptions → Apply to Apps | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS/apps` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 螢幕辨識 → 螢幕辨識 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_SCREEN_RECOGNITION#VO_SCREEN_RECOGNITION` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 螢幕辨識 → 套用到App | Accessibility → VoiceOver → VoiceOver Recognition → Screen Recognition → Apply to Apps | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_SCREEN_RECOGNITION/apps` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 轉輪 → 直接觸控App → 直接觸控App | Accessibility → VoiceOver → Rotor → Direct Touch Apps → Direct Touch Apps | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions/apps#apps` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 轉輪 → 轉輪項目 → 轉輪項目 | Accessibility → VoiceOver → Rotor → Rotor Items → Rotor Items | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/RotorActions/WebRotor#WebRotor` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 輸入 → 鍵盤互動時間 → 鍵盤互動時間 | Accessibility → VoiceOver → Typing → Keyboard Interaction Time → Keyboard Interaction Time | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/KEYBOARD_TIMING_TIMEOUT#KEYBOARD_TIMING_TIMEOUT` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 輸入 → 變更鍵 → 變更鍵 | Accessibility → VoiceOver → Typing → Modifier Keys → Modifier Keys | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/MODIFIER_KEYS#MODIFIER_KEYS` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Typing → Modifier Keys → Caps Lock | Accessibility → VoiceOver → Typing → Modifier Keys → Caps Lock | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/MODIFIER_KEYS#VO_MODIFIER_KEY_CAPS_LOCK` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → Modifier Keys → Control + Option | Accessibility → VoiceOver → Typing → Modifier Keys → Control + Option | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/MODIFIER_KEYS#VO_MODIFIER_KEY_CONTROL_OPTIONS` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → Phonetic Feedback → 關閉 | Accessibility → VoiceOver → Typing → Phonetic Feedback → Off | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/PHONETICS_TITLE#PHONETICS_OFF` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → Phonetic Feedback → 字元與音標 | Accessibility → VoiceOver → Typing → Phonetic Feedback → Character and Phonetics | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/PHONETICS_TITLE#PHONETICS_SPEAK_AFTER_DELAY` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → Phonetic Feedback → 只限音標 | Accessibility → VoiceOver → Typing → Phonetic Feedback → Phonetics Only | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/PHONETICS_TITLE#PHONETICS_SPEAK_EXCLUSIVELY` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 輸入 → 音標回饋 → 音標回饋 | Accessibility → VoiceOver → Typing → Phonetic Feedback → Phonetic Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/PHONETICS_TITLE#PHONETICS_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Typing → Typing Style → 直接觸控輸入 | Accessibility → VoiceOver → Typing → Typing Style → Direct Touch Typing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/Typing%20Style#TYPING_MODE_DIRECT_TOUCH` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Typing → Typing Style → 觸控輸入 | Accessibility → VoiceOver → Typing → Typing Style → Touch Typing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/Typing%20Style#TYPING_MODE_TOUCH_TYPING` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 輸入 → 輸入回饋 → 輸入回饋 | Accessibility → VoiceOver → Typing → Typing Feedback → Typing Feedback | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/TYPING_FEEDBACK#TYPING_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Typing → Typing Mode → 標準輸入 | Accessibility → VoiceOver → Typing → Typing Mode → Standard Typing | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/TYPING_MODE_TITLE#TYPING_MODE_STANDARD` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 輸入 → 輸入樣式 → 輸入樣式 | Accessibility → VoiceOver → Typing → Typing Style → Typing Style | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/TypingOptions/TYPING_MODE_TITLE#TYPING_MODE_TITLE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 預測字詞回饋 → 預測字詞回饋 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/PREDICTIVE_TEXT_FEEDBACK#PREDICTIVE_TEXT_FEEDBACK` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 預測字詞回饋 → 當預測字詞顯示時 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/PREDICTIVE_TEXT_FEEDBACK/InlineTextCompletionAppearanceFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 預測字詞回饋 → 當輸入預測字詞回饋時 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/PREDICTIVE_TEXT_FEEDBACK/InlineTextCompletionInsertionFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 系統通知 → 橫幅通知 | Accessibility → VoiceOver → Verbosity → System Notifications → Banner Notifications | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/SystemNotifications#BannerNotifications` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 系統通知 → 鎖定時通知 | Accessibility → VoiceOver → Verbosity → System Notifications → Notifications when Locked | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/SystemNotifications#LockScreenNotifications` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 系統通知 → 使用靜音模式 | Accessibility → VoiceOver → Verbosity → System Notifications → Use Silent Mode | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/SystemNotifications#NOTIFICATION_USE_RINGER_SWITCH` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 系統通知 → 系統通知 | Accessibility → VoiceOver → Verbosity → System Notifications → System Notifications | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/SystemNotifications#SystemNotifications` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 動作 → 動作 | Accessibility → VoiceOver → Verbosity → Actions → Actions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverActionsFeedback#voiceOverActionsFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 大寫字母 → 大寫字母 | Accessibility → VoiceOver → Verbosity → Capital Letters → Capital Letters | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverCapitalLetterFeedback#voiceOverCapitalLetterFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 容器描述 → 容器描述 | Accessibility → VoiceOver → Verbosity → Container Descriptions → Container Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverContainerOutputFeedback#voiceOverContainerOutputFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 刪除文字 → 刪除文字 | Accessibility → VoiceOver → Verbosity → Deleting Text → Deleting Text | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverDeletionFeedback#voiceOverDeletionFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 表情符號 → 表情符號 | Accessibility → VoiceOver → Verbosity → Emoji → Emoji | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverEmojiFeedback#voiceOverEmojiFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 手電筒通知 → 手電筒通知 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverFlashlightNotificationsEnabled#voiceOverFlashlightNotificationsEnabled` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 連結 → 連結 | Accessibility → VoiceOver → Verbosity → Links → Links | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverLinkFeedback#voiceOverLinkFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → Verbosity → Media Descriptions → 點字 | Accessibility → VoiceOver → Verbosity → Media Descriptions → Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMediaDescriptions#mdBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Verbosity → Media Descriptions → 關閉 | Accessibility → VoiceOver → Verbosity → Media Descriptions → Off | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMediaDescriptions#mdOff` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Verbosity → Media Descriptions → 語音 | Accessibility → VoiceOver → Verbosity → Media Descriptions → Speech | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMediaDescriptions#mdSpeech` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → Verbosity → Media Descriptions → 語音和點字 | Accessibility → VoiceOver → Verbosity → Media Descriptions → Speech and Braille | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMediaDescriptions#mdSpeechAndBraille` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 旁白 → 詳細程度 → 媒體描述 → 媒體描述 | Accessibility → VoiceOver → Verbosity → Media Descriptions → Media Descriptions | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMediaDescriptions#voiceOverMediaDescriptions` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 更多內容 → 更多內容 | Accessibility → VoiceOver → Verbosity → More Content → More Content | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverMoreContentOutputFeedback#voiceOverMoreContentOutputFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 數字 → 數字 | Accessibility → VoiceOver → Verbosity → Numbers → Numbers | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverNumberFeedback#voiceOverNumberFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 全部 | Accessibility → VoiceOver → Verbosity → Punctuation → All | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup#all` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 部分 | Accessibility → VoiceOver → Verbosity → Punctuation → Some | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup#AXSSVoiceOverPunctuationGroupSome` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 無 | Accessibility → VoiceOver → Verbosity → Punctuation → None | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup#PunctuationGroupNone` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 啟用的標點符號群組 | Accessibility → VoiceOver → Verbosity → Punctuation → Active Punctuation Group | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup#voiceOverActivePunctuationGroup` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 標點符號 | Accessibility → VoiceOver → Verbosity → Punctuation → Punctuation | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup#voiceOverPunctuationGroup` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 輸入 | Accessibility → VoiceOver → Verbosity → Punctuation → Import | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup/ImportPunctuation` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 加入標點符號群組 | Accessibility → VoiceOver → Verbosity → Punctuation → Add Punctuation Group | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup/NewPunctuation` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 快速導覽宣告 → 快速導覽宣告 | Accessibility → VoiceOver → Verbosity → QuickNav Announcements → QuickNav Announcements | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverQuickNavAnnouncementFeedback#voiceOverQuickNavAnnouncementFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 網頁轉輪摘要 → 網頁轉輪摘要 | Accessibility → VoiceOver → Verbosity → Web Rotor Summary → Web Rotor Summary | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverRotorSummaryFeedback#voiceOverRotorSummaryFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 語音 → 發音 → 發音 | Accessibility → VoiceOver → Speech → Pronunciations → Pronunciations | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Voices/PRONUNCIATION_DICTIONARY#PRONUNCIATION_DICTIONARY` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 顏色 → 顏色 | Accessibility → Zoom → Zoom Controller → Color → Color | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/CONTROLLER_COLOR#CONTROLLER_COLOR` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 點兩下 → 點兩下 | Accessibility → Zoom → Zoom Controller → Double-Tap → Double-Tap | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_CONTROLLER_ACTION_DOUBLE_TAP#ZOOM_CONTROLLER_ACTION_DOUBLE_TAP` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 點一下 → 點一下 | Accessibility → Zoom → Zoom Controller → Single-Tap → Single-Tap | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_CONTROLLER_ACTION_SINGLE_TAP#ZOOM_CONTROLLER_ACTION_SINGLE_TAP` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 點三下 → 點三下 | Accessibility → Zoom → Zoom Controller → Triple-Tap → Triple-Tap | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_CONTROLLER_ACTION_TRIPLE_TAP#ZOOM_CONTROLLER_ACTION_TRIPLE_TAP` | 18.7 | F18 |  |
| 輔助使用 → 縮放 → 縮放控制器 → 閒置不透明度 → 閒置不透明度 | Accessibility → Zoom → Zoom Controller → Idle Opacity → Idle Opacity | `prefs:root=ACCESSIBILITY&path=ZOOM_TITLE/ZoomSlug/ZOOM_IDLE_SLUG_OPACITY#ZOOM_IDLE_SLUG_OPACITY` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 裝置 → 藍牙裝置⋯ → 藍牙裝置⋯ | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/AssistiveTouchMouseDevices/BluetoothDevicesScanning#BluetoothDevicesScanning` | 18.7 | F18 |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → NEEDS_OVERRIDE_1360 → 自動隱藏 | Accessibility → Touch → AssistiveTouch → Pointer Style → NEEDS_OVERRIDE_238 → Auto-Hide | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization/AMOUSE_POINTER_TIMEOUT#Auto-Hide` | 16.2 | F16 MAN MEHDI |  |
| — | Accessibility → Touch → AssistiveTouch → Pointer Style → Color → Customize Mouse Buttons | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization/Color/CustomizeMouseButtons` | — | FIFI WDG |  |
| 輔助使用 → 觸控 → AssistiveTouch → 指標樣式 → SOMETHING IDK → 自訂滑鼠按鈕 | Accessibility → Touch → Touch → AssistiveTouch → Pointer Style → Color | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTMousePointerCustomization/MOUSE_POINTER_COLOR#CustomizeMouseButtons` | 16.2 | F16 MAN MEHDI |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 邊線 → 邊線寬度 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/BORDER#BORDER_WIDTH` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 邊線 → 顏色 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Border → Color | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/BORDER#COLOR` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 邊線 → 不透明度 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Border → Opacity | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/BORDER#OPACITY` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 觸控式軌跡板 → 顏色 | Accessibility → Interaction \| Touch → AssistiveTouch → Virtual Trackpad → Trackpad → Color | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/TRACKPAD#COLOR` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 虛擬觸控式軌跡板 → 觸控式軌跡板 → 不透明度 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/ASTVirtualTrackpadCellID/TRACKPAD#OPACITY` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 點兩下 → 點兩下逾時 → 點兩下逾時 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/DoubleTapSpecifier/ASTDoubleTapTimeoutSpecifier#ASTDoubleTapTimeoutSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 互動 \| 觸控 → 輔助觸控 → 長時間按下 → 長時間按下持續時間 → 長時間按下持續時間 | — | `prefs:root=ACCESSIBILITY&path=TOUCH_REACHABILITY_TITLE/AIR_TOUCH_TITLE/LongPressSpecifier/ASTLongPressDurationSpecifier#ASTLongPressDurationSpecifier` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 點字 → 點字表 → 加入點字表⋯ → 加入點字表⋯ | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Braille/tableIdentifier/ADD_NEW_BRAILLE_LANGUAGE#ADD_NEW_BRAILLE_LANGUAGE` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 → 其他語言 → 其他語言 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS/AdditionalLanguages#AdditionalLanguages` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 影像描述 → 套用到App → 套用到App | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_IMAGE_DESCRIPTIONS/apps#apps` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 旁白辨識 → 螢幕辨識 → 套用到App → 套用到App | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/NeuralVoiceOver/VO_SCREEN_RECOGNITION/apps#apps` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 預測字詞回饋 → 當預測字詞顯示時 → 當預測字詞顯示時 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/PREDICTIVE_TEXT_FEEDBACK/InlineTextCompletionAppearanceFeedback#InlineTextCompletionAppearanceFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 預測字詞回饋 → 當輸入預測字詞回饋時 → 當輸入預測字詞回饋時 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/PREDICTIVE_TEXT_FEEDBACK/InlineTextCompletionInsertionFeedback#InlineTextCompletionInsertionFeedback` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 輸入 → 輸入 | Accessibility → VoiceOver → Verbosity → Punctuation → Import → Import | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup/ImportPunctuation#ImportPunctuation` | 18.7 | F18 |  |
| 輔助使用 → 旁白 → 詳細程度 → 標點符號 → 加入標點符號群組 → 加入標點符號群組 | — | `prefs:root=ACCESSIBILITY&path=VOICEOVER_TITLE/Verbosity/voiceOverPunctuationGroup/NewPunctuation#NewPunctuation` | 18.7 | F18 |  |

### Account Settings

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Account Settings | `prefs:root=ACCOUNT_SETTINGS` | — | MAN DYLD DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |

### Action Button

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 動作按鈕 | Action Button | `prefs:root=ACTION_BUTTON` | 18.7 | F18 FIFI WDG |  |

### Airplane Mode

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Airplane Mode | `prefs:root=AIRPLANE_MODE` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=ROOT` | — | MAN DYLD |  |
| — | — | `prefs:root=ROOT%23` | — | MAN DYLD |  |
| 飛航模式 | Airplane Mode | `prefs:root=ROOT#AIRPLANE_MODE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN DYLD MEHDI WDG |  |

### App Store

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| App Store | App Store | `prefs:root=STORE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| App Store → App下載項目 | App Store → App Downloads | `prefs:root=STORE&path=App%20Downloads` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| App Store → 自動播放影片 | App Store → Video Autoplay | `prefs:root=STORE&path=Video%20Autoplay` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| App Store → App更新項目 | App Store → App Updates | `prefs:root=STORE#App%20Updates` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| App Store → 自動下載 | App Store → Automatic Downloads | `prefs:root=STORE#Automatic%20Downloads` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| App Store → App內評分與評論 | App Store → In-App Ratings & Reviews | `prefs:root=STORE#In-App%20Ratings%20&%20Reviews` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Apple Account

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Apple帳號 | Apple Account | `prefs:root=APPLE_ACCOUNT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| — | — | `prefs:root=APPLE_ACCOUNT&aaaction=setupFamily&clientAppContext=iCloudStorage` | — | MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&aaaction=upgradeSecurityLevel` | — | MAN DYLD |  |
| Apple帳號 → 姓名、電話號碼、電子郵件 | Apple Account → Name, Phone Numbers, Email | `prefs:root=APPLE_ACCOUNT&path=APPLE_ACCOUNT_CONTACT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG |  |
| Apple ID → 家人共享 | Apple ID → Family | `prefs:root=APPLE_ACCOUNT&path=FAMILY` | 16.2 | F16 FIFI MAN DYLD MEHDI WDG |  |
| Apple帳號 → 家人共享 | Apple Account → Family | `prefs:root=APPLE_ACCOUNT&path=Family` | 18.7 · 26.2 | F26 F18 |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=FAMILY&faservice=APPLE_CASH` | — | MAN DYLD |  |
| Apple帳號 → iCloud | Apple Account → iCloud | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE&path=PAYMENT_AND_SHIPPING` | — | MAN DYLD |  |
| Apple帳號 → 分享我的位置 | Apple Account → Share My Location | `prefs:root=APPLE_ACCOUNT&path=LOCATION_SHARING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG |  |
| Apple帳號 → 密碼與安全性 | Apple Account → Password & Security | `prefs:root=APPLE_ACCOUNT&path=PASSWORD_AND_SECURITY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG |  |
| Apple帳號 → 付款與寄送 | Apple Account → Payment & Shipping | `prefs:root=APPLE_ACCOUNT&path=PAYMENT_AND_SHIPPING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| Apple帳號 → 訂閱項目 | Apple Account → Subscriptions | `prefs:root=APPLE_ACCOUNT&path=SUBSCRIPTIONS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| Apple帳號 → 聯絡人密鑰驗證 | Apple Account → Contact Key Verification | `prefs:root=APPLE_ACCOUNT&path=TRANSPARENCY` | 18.7 · 26.2 | F26 F18 GH |  |
| Apple帳號 → iCloud | Apple Account → iCloud | `prefs:root=CASTLE` | 18.7 · 26.2 | F26 F18 FIFI MAN DYLD MEHDI MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=CASTLE&` | — | MAN DYLD |  |
| Apple帳號 → iCloud → 備份 | Apple Account → iCloud → Backup | `prefs:root=CASTLE&path=BACKUP` | 18.7 · 26.2 | F26 F18 FIFI MEHDI MS MR | 也見於 `App-Prefs:` |
| — | — | `prefs:root=CASTLE&path=CKDATABASESERVICE` | — | MAN DYLD |  |
| Apple帳號 → iCloud → Safari | Apple Account → iCloud → Safari | `prefs:root=CASTLE&path=com.apple.Dataclass.Bookmarks` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 行事曆 | Apple Account → iCloud → Calendar | `prefs:root=CASTLE&path=com.apple.Dataclass.Calendars` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 聯絡人 | Apple Account → iCloud → Contacts | `prefs:root=CASTLE&path=com.apple.Dataclass.Contacts` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 健康 | Apple Account → iCloud → Health | `prefs:root=CASTLE&path=com.apple.Dataclass.Health` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 密碼與鑰匙圈 | Apple Account → iCloud → Passwords and Keychain | `prefs:root=CASTLE&path=com.apple.Dataclass.KeychainSync` | 18.7 · 26.2 | F26 F18 FIFI |  |
| Apple帳號 → iCloud → 郵件 | Apple Account → iCloud → Mail | `prefs:root=CASTLE&path=com.apple.Dataclass.Mail` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 照片 | Apple Account → iCloud → Photos | `prefs:root=CASTLE&path=com.apple.Dataclass.MediaStream` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 新聞 | Apple Account → iCloud → News | `prefs:root=CASTLE&path=com.apple.Dataclass.News` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 備忘錄 | Apple Account → iCloud → Notes | `prefs:root=CASTLE&path=com.apple.Dataclass.Notes` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 提醒事項 | Apple Account → iCloud → Reminders | `prefs:root=CASTLE&path=com.apple.Dataclass.Reminders` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → iCloud雲碟 | Apple Account → iCloud → iCloud Drive | `prefs:root=CASTLE&path=com.apple.Dataclass.Ubiquity` | 18.7 · 26.2 | F26 F18 |  |
| — | — | `prefs:root=CASTLE&path=FAMILY` | — | MAN DYLD |  |
| Apple帳號 → iCloud → 隱藏電子郵件地址 | Apple Account → iCloud → Hide My Email | `prefs:root=CASTLE&path=PRIVATE_EMAIL_MANAGE` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → iCloud儲存空間 | Apple Account → iCloud → iCloud Storage | `prefs:root=CASTLE&path=STORAGE_AND_BACKUP` | 18.7 · 26.2 | F26 F18 DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=APPLE_ACCOUNT#TRANSPARENCY` | — | GH |  |
| — | Apple ID → Family Sharing → App Store Subscriptions | `prefs:root=APPLE_ACCOUNT&path=FAMILY#APP_STORE_SUBSCRIPTIONS` | — | MEHDI |  |
| — | Apple ID → Family Sharing → Apple Cash | `prefs:root=APPLE_ACCOUNT&path=FAMILY#APPLE_CASH` | — | MEHDI |  |
| — | Apple ID → Family Sharing → Apple Subscriptions | `prefs:root=APPLE_ACCOUNT&path=FAMILY#APPLE_SUBSCRIPTIONS` | — | MEHDI |  |
| — | Apple ID → Family Sharing → Ask to Buy | `prefs:root=APPLE_ACCOUNT&path=FAMILY#ASK_TO_BUY` | — | MEHDI |  |
| — | Apple ID → Family Sharing → iCloud Storage / iCloud+ | `prefs:root=APPLE_ACCOUNT&path=FAMILY#ICLOUD_STORAGE` | — | MEHDI |  |
| — | Apple ID → Family Sharing → Purchase Sharing | `prefs:root=APPLE_ACCOUNT&path=FAMILY#PURCHASE_SHARING` | — | MEHDI |  |
| — | Apple ID → Family Sharing → Screen Time | `prefs:root=APPLE_ACCOUNT&path=FAMILY#SCREEN_TIME` | — | MEHDI |  |
| Apple帳號 → iCloud → 備份 | Apple Account → iCloud → Backup | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/BACKUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/CKDATABASESERVICE` | — | MAN DYLD |  |
| Apple帳號 → iCloud → Safari | Apple Account → iCloud → Safari | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Bookmarks` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → 行事曆 | Apple Account → iCloud → Calendar | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Calendars` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → 聯絡人 | Apple Account → iCloud → Contacts | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Contacts` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → 健康 | Apple Account → iCloud → Health | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Health` | 16.2 · 18.7 · 26.2 | F26 F18 F16 |  |
| Apple帳號 → iCloud → 密碼與鑰匙圈 | Apple Account → iCloud → Passwords and Keychain | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.KeychainSync` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD |  |
| Apple帳號 → iCloud → 郵件 | Apple Account → iCloud → Mail | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN |  |
| Apple帳號 → iCloud → 照片 | Apple Account → iCloud → Photos | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.MediaStream` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → 新聞 | Apple Account → iCloud → News | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.News` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → 備忘錄 | Apple Account → iCloud → Notes | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Notes` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → 提醒事項 | Apple Account → iCloud → Reminders | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Reminders` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| Apple帳號 → iCloud → iCloud雲碟 | Apple Account → iCloud → iCloud Drive | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Ubiquity` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN DYLD |  |
| Apple ID → iCloud → 私密轉送 | Apple ID → iCloud → Private Relay | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/INTERNET_PRIVACY` | 16.2 | F16 |  |
| Apple帳號 → iCloud → 隱藏電子郵件地址 | Apple Account → iCloud → Hide My Email | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/PRIVATE_EMAIL_MANAGE` | 18.7 · 26.2 | F26 F18 FIFI WDG |  |
| Apple帳號 → iCloud → iCloud儲存空間 | Apple Account → iCloud → iCloud Storage | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/STORAGE_AND_BACKUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN DYLD |  |
| Apple帳號 → 分享我的位置 → 尋找 | Apple Account → Share My Location → Find My | `prefs:root=APPLE_ACCOUNT&path=LOCATION_SHARING/FindMyDevice-Settings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=PAYMENT_AND_SHIPPING/PRIMARY_PAYMENT` | — | MAN DYLD |  |
| Apple帳號 → iCloud → 郵件 → 自訂電子郵件網域 | Apple Account → iCloud → Mail → Custom Email Domain | `prefs:root=CASTLE&path=com.apple.Dataclass.Mail/BYOD_SETTING_SPECIFIER_ID` | 18.7 | F18 |  |
| — | iCloud → iCloud Mail → Auto-Reply | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/AUTO_REPLY` | — | FIFI |  |
| Apple帳號 → iCloud → 郵件 → 自訂電子郵件網域 | Apple Account → iCloud → Mail → Custom Email Domain | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/BYOD_SETTING_SPECIFIER_ID` | 18.7 | F18 |  |
| — | iCloud → iCloud Mail → Default Email | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/DEFAULT_EMAIL` | — | FIFI |  |
| — | iCloud → iCloud Mail → Import Messages | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/MAIL_IMPORT` | — | FIFI |  |
| — | iCloud → iCloud Mail → Mailbox Behaviors | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/MAILBOX_BEHAVIORS` | — | FIFI |  |
| — | iCloud → iCloud Mail → Signing and Encryption | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/S_MIME` | — | FIFI |  |
| — | iCloud → iCloud Mail → iCloud Mail Rules | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/SERVER_SIDE_RULES` | — | FIFI |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/STORAGE_AND_BACKUP/CHANGE_STORAGE_PLAN` | — | MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/STORAGE_AND_BACKUP/CURRENT_DEVICE_BACKUP` | — | MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/STORAGE_AND_BACKUP/MANAGE_STORAGE` | — | MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/STORAGE_AND_BACKUP/PHOTOS` | — | MAN DYLD |  |
| — | — | `prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/STORAGE_AND_BACKUP/STORAGE_UPGRADE` | — | MAN DYLD |  |

### Apple Pencil

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Apple Pencil | Apple Pencil | `prefs:root=Pencil` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| Apple Pencil → Apple Pencil | Apple Pencil → Apple Pencil | `prefs:root=Pencil#PencilTextInput` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| Apple Pencil → Apple Pencil | Apple Pencil → Apple Pencil | `prefs:root=Pencil#PrefersPencilDraws` | 18.7 · 26.2 | F26 F18 MAN MEHDI WDG |  |

### Battery

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 電池 | Battery | `prefs:root=BATTERY_USAGE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| — | Battery → Battery Health | `prefs:root=BATTERY_USAGE&path=BATTERY_HEALTH` | — | FIFI MAN DYLD MEHDI WDG MS |  |
| 電池 → 電池健康度 | Battery → Battery Health | `prefs:root=BATTERY_USAGE#BATTERY_HEALTH_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電池 → 低耗電模式 | Battery → Low Power Mode | `prefs:root=BATTERY_USAGE#BATTERY_SAVER_MODE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Bluetooth

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 藍牙 | Bluetooth | `prefs:root=Bluetooth` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |

### Books

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 書籍 | Books | `prefs:root=IBOOKS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 書籍 → 版權宣告 | Books → Acknowledgements | `prefs:root=IBOOKS&path=Acknowledgements` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 書籍 → 跳到上一段 | Books → Skip Back | `prefs:root=IBOOKS&path=BKAudioBookSkipBackward` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 書籍 → 跳到下一段 | Books → Skip Forward | `prefs:root=IBOOKS&path=BKAudioBookSkipForward` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | Books → Siri & Search | `prefs:root=IBOOKS&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| 書籍 → 有聲書 | Books → AUDIOBOOKS | `prefs:root=IBOOKS#AUDIOBOOKS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 重置識別碼 | Books → Reset Identifier | `prefs:root=IBOOKS#BAResetAnalyticsUserID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → iCloud雲碟 | Books → iCloud Drive | `prefs:root=IBOOKS#BCSyncICloudDrive` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 線上內容 | Books → Online Content | `prefs:root=IBOOKS#BKAllowOnlineContent` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 自動加入連字號 | Books → Auto-hyphenation | `prefs:root=IBOOKS#BKAutoHyphenation` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 書店 | Books → Book Store | `prefs:root=IBOOKS#BKExcludeBookStoreResultsInSearch` | 16.2 | F16 MAN |  |
| 書籍 → 左右齊行 | Books → Full Justification | `prefs:root=IBOOKS#BKFullJustification` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 書店 | Books → Book Store | `prefs:root=IBOOKS#BKIncludeBookStoreResultsInSearch` | 18.7 · 26.2 | F26 F18 WDG |  |
| 書籍 → 點一下左右頁邊來翻頁 | Books → Both Margins Advance | `prefs:root=IBOOKS#BKLeftTapTurnToNext` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 閱讀中 | Books → Reading Now | `prefs:root=IBOOKS#BKLibrary.ReadingNow` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 清除閱讀目標資料 | Books → Clear Reading Goals Data | `prefs:root=IBOOKS#BKReadingGoalsShouldClearDataKey` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 閱讀目標 | Books → Reading Goals | `prefs:root=IBOOKS#BKReadingGoalsUserDefaultsKey` | 16.2 | F16 MAN |  |
| 書籍 → 外部控制項目 | Books → EXTERNAL CONTROLS | `prefs:root=IBOOKS#BKRemoteSkipInsteadOfNextTrackDefaultKey` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 隱私權 | Books → PRIVACY | `prefs:root=IBOOKS#PRIVACY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 閱讀 | Books → READING | `prefs:root=IBOOKS#READING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 閱讀目標 | Books → Reading Goals | `prefs:root=IBOOKS#READING_GOALS` | 18.7 · 26.2 | F26 F18 WDG |  |
| 書籍 → 搜尋 | Books → SEARCHING | `prefs:root=IBOOKS#SEARCHING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 同步 | Books → SYNCING | `prefs:root=IBOOKS#SYNCING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 下一集/上一集 | Books → Next/Previous | `prefs:root=IBOOKS#Next/Previous` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 書籍 → 快轉/倒轉 | Books → Skip Forward/Back | `prefs:root=IBOOKS#Skip%20Forward/Back` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Calendar

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 行事曆 | Calendar | `prefs:root=CALENDAR` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 行事曆 → 其他曆法 | Calendar → Alternate Calendars | `prefs:root=CALENDAR&path=Alternate%20Calendars` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 行事曆 → 每週開始日 | Calendar → Start Week On | `prefs:root=CALENDAR&path=com.apple.mobilecal` | 16.2 | F16 FIFI MAN WDG |  |
| 行事曆 → 預設提示時間 | Calendar → Default Alert Times | `prefs:root=CALENDAR&path=Default%20Alert%20Times` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Calendar → Default Calendar | `prefs:root=CALENDAR&path=Default%20Calendar` | — | FIFI MEHDI WDG MS |  |
| — | — | `prefs:root=CALENDAR&path=DELEGATE_CALENDARS` | — | MAN DYLD |  |
| — | Calendar → Siri & Search | `prefs:root=CALENDAR&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| 行事曆 → 每週開始日 | Calendar → Start Week On | `prefs:root=CALENDAR&path=Start%20Week%20On` | 18.7 · 26.2 | F26 F18 WDG |  |
| 行事曆 → 同步 | Calendar → Sync | `prefs:root=CALENDAR&path=Sync` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 行事曆 → 時區覆蓋 | Calendar → Time Zone Override | `prefs:root=CALENDAR&path=TimeZoneCityArray` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 行事曆 → 地點建議 | Calendar → Location Suggestions | `prefs:root=CALENDAR#Location%20Suggestions` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 行事曆 → 顯示邀請對象的拒絕內容 | Calendar → Show Invitee Declines | `prefs:root=CALENDAR#Show%20Invitee%20Declines` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 行事曆 → 週數 | Calendar → Week Numbers | `prefs:root=CALENDAR#Week%20Numbers` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Camera

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 相機 | Camera | `prefs:root=CAMERA` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 相機 → 格式 | Camera → Formats | `prefs:root=CAMERA&path=CameraFormatsSettingsList` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 相機 → 保留設定 | Camera → Preserve Settings | `prefs:root=CAMERA&path=CameraPreserveSettingsSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| — | Camera → Record Slo-mo | `prefs:root=CAMERA&path=Record%20Slo-mo` | — | FIFI MEHDI WDG MS |  |
| 相機 → Record Video | Camera → Record Video | `prefs:root=CAMERA&path=Record%20Video` | 18.7 · 26.2 | F26 F18 FIFI MAN MEHDI WDG MS |  |
| 相機 → 格線 | Camera → Grid | `prefs:root=CAMERA#CameraGridSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 相機 → 掃描行動條碼 | Camera → Scan QR Codes | `prefs:root=CAMERA#CameraQRBannerSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 相機 → 格式 → Apple ProRaw | Camera → Formats → Apple ProRaw | `prefs:root=CAMERA&path=CameraFormatsSettingsList#CAMUserPreferenceEnableLinearDNGControl` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |
| 相機 → 保留設定 → 相機模式 | Camera → Preserve Settings → Camera Mode | `prefs:root=CAMERA&path=CameraPreserveSettingsSwitch#CAMUserPreferencePreserveCaptureMode` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 相機 → Record Video → HDR影片 | Camera → Record Video → HDR Video | `prefs:root=CAMERA&path=Record%20Video#HDR%20Video` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |

### Carrier

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=Carrier` | — | MAN DYLD |  |

### Cellular

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 行動服務 | Cellular | `prefs:root=MOBILE_DATA_SETTINGS_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| 行動服務 → 行動數據選項 | Cellular → Cellular Data Options | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=CELLULAR_DATA_OPTIONS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| — | Cellular → Personal Hotspot → (root) | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=INTERNET_TETHERING` | — | FIFI WDG |  |
| — | Cellular → Cellular Data (for devices with two SIMs) | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=MOBILE_DATA_SETTINGS` | — | FIFI MEHDI WDG |  |
| 行動服務 → 行動數據 | Cellular → Cellular Data | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=SHOW_ALL` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | Cellular → System Services | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=System%20Services` | — | FIFI WDG |  |
| — | — | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=WIRELESS_APP_DATA_USAGE_ID` | — | MAN DYLD |  |
| 行動服務 → 行動數據 | Cellular → Cellular Data | `prefs:root=MOBILE_DATA_SETTINGS_ID#APP_DATA_USAGE` | 16.2 | F16 MAN DYLD MEHDI |  |
| — | Cellular → Reset Statistics | `prefs:root=MOBILE_DATA_SETTINGS_ID#Reset%20Statistics` | — | FIFI WDG |  |
| 行動服務 → 行動數據選項 → 低數據模式 | Cellular → Cellular Data Options → Low Data Mode | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=CELLULAR_DATA_OPTIONS#Low%20Data%20Mode` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| — | Cellular → Personal Hotspot → Family Sharing → (root) | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=INTERNET_TETHERING/Family%20Sharing` | — | FIFI WDG |  |
| — | Cellular → Personal Hotspot → Wi-Fi Password | `prefs:root=MOBILE_DATA_SETTINGS_ID&path=INTERNET_TETHERING/Wi-Fi%20Password` | — | FIFI WDG |  |

### com.adobe.lrmobilephone

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=com.adobe.lrmobilephone` | — | MS |  |

### Compass

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 指南針 | Compass | `prefs:root=COMPASS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| 指南針 → 使用正北 | Compass → Use True North | `prefs:root=COMPASS#USE_TRUE_NORTH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Contacts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 聯絡人 | Contacts | `prefs:root=CONTACTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 聯絡人 → 排序 | Contacts → Sort Order | `prefs:root=CONTACTS&path=ContactsSortOrder` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 聯絡人 → 我的資訊 | Contacts → My Info | `prefs:root=CONTACTS&path=MeCard` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 聯絡人 → 顯示順序 | Contacts → Display Order | `prefs:root=CONTACTS&path=PersonNameOrder` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 聯絡人 → 簡稱 | Contacts → Short Name | `prefs:root=CONTACTS&path=PersonShortName` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 聯絡人 → Siri | Contacts → Siri | `prefs:root=CONTACTS&path=SIRI_AND_SEARCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 聯絡人 → 允許聯絡人取用 | Contacts → Allow Contacts To Access | `prefs:root=CONTACTS#Allow%20Contacts%20To%20Access` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 聯絡人 → 輸入SIM卡的聯絡人 | Contacts → Import SIM Contacts | `prefs:root=CONTACTS#SIMImport` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 聯絡人 → 簡稱 → 偏好暱稱 | Contacts → Short Name → Prefer Nicknames | `prefs:root=CONTACTS&path=PersonShortName#Prefer%20Nicknames` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 聯絡人 → 簡稱 → 簡稱 | Contacts → Short Name → Short Name | `prefs:root=CONTACTS&path=PersonShortName#Short%20Name` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Control Center

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 控制中心 | Control Center | `prefs:root=ControlCenter` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| 控制中心 → 自訂控制項目 | Control Center → Customize Controls | `prefs:root=ControlCenter&path=CUSTOMIZE_CONTROLS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 控制中心 → 在App中取用 | Control Center → Access Within Apps | `prefs:root=ControlCenter#ALLOWED_WITHIN_APPS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Developer

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 開發者 | Developer | `prefs:root=DEVELOPER_SETTINGS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | Developer → Ad Refresh Rate | `prefs:root=DEVELOPER_SETTINGS&path=AD_REFRESH_RATE` | — | FIFI MAN WDG |  |
| 開發者 → ClassKit API | Developer → ClassKit API | `prefs:root=DEVELOPER_SETTINGS&path=ClassKitSettings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → AirPlay建議 | Developer → AirPlay Suggestions | `prefs:root=DEVELOPER_SETTINGS&path=D2A_AIRPLAY_SUGGESTIONS` | 16.2 | F16 MAN |  |
| 開發者 → 記錄 | Developer → Logging | `prefs:root=DEVELOPER_SETTINGS&path=DTInstrumentsSettings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 開發者 → 填充率 | Developer → Fill Rate | `prefs:root=DEVELOPER_SETTINGS&path=FILL_RATE` | 16.2 | F16 FIFI MAN WDG |  |
| 開發者 → 多重路徑網路 | Developer → Multipath Networking | `prefs:root=DEVELOPER_SETTINGS&path=MULTI_PATH_AGG` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 開發者 → 網路連結調節器 | Developer → Network Link Conditioner | `prefs:root=DEVELOPER_SETTINGS&path=NLC` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 開發者 → 可播放內容API | Developer → Playable Content API | `prefs:root=DEVELOPER_SETTINGS&path=RoutineSettings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 電視業者 | Developer → TV Provider | `prefs:root=DEVELOPER_SETTINGS&path=VideoSubscriberAccountSettings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 開發者 → iAd開發者App測試 | Developer → iAd Developer App Testing | `prefs:root=DEVELOPER_SETTINGS#AD_DEVELOPER_GROUP` | 16.2 | F16 MAN |  |
| 開發者 → 其他記錄 | Developer → Additional Logging | `prefs:root=DEVELOPER_SETTINGS#ADDITIONAL_LOGGING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 允許HTTP服務 | Developer → Allow HTTP Services | `prefs:root=DEVELOPER_SETTINGS#ALLOW_HTTP_SERVICES` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 清除已信任的電腦 | Developer → Clear Trusted Computers | `prefs:root=DEVELOPER_SETTINGS#CLEAR_TRUSTED_COMPUTERS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → CoreSpotlight測試 | Developer → CoreSpotlight Testing | `prefs:root=DEVELOPER_SETTINGS#CORESPOTLIGHT_TESTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 停用速率限制 | Developer → Disable Rate Limiting | `prefs:root=DEVELOPER_SETTINGS#DISABLE_RATE_LIMITING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 在鎖定畫面上顯示捐贈 | Developer → Display Donations on Lock Screen | `prefs:root=DEVELOPER_SETTINGS#DISPLAY_DONATIONS_LOCKSCREEN` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 顯示最近提供的捷徑 | Developer → Display Recent Shortcuts | `prefs:root=DEVELOPER_SETTINGS#DISPLAY_DONATIONS_SPOTLIGHT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 顯示下一個媒體 | Developer → Display Upcoming Media | `prefs:root=DEVELOPER_SETTINGS#DISPLAY_UPCOMING_MEDIA` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → Instruments | Developer → Instruments | `prefs:root=DEVELOPER_SETTINGS#DTInstrumentsGroup` | 16.2 | F16 MAN |  |
| 開發者 → 配對的裝置 | Developer → Paired Devices | `prefs:root=DEVELOPER_SETTINGS#DTPairedDevicesGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | — | `prefs:root=DEVELOPER_SETTINGS#EU_VOLUME_LIMIT` | — | MAN |  |
| 開發者 → 當機偵測 | Developer → Hang Detection | `prefs:root=DEVELOPER_SETTINGS#HANGTRACER_EXTERNAL_CONFIGURE` | 18.7 · 26.2 | F26 F18 WDG |  |
| 開發者 → 反白遭裁切的橫幅 | Developer → Highlight Clipped Banners | `prefs:root=DEVELOPER_SETTINGS#HIGHLIGHT_CLIPPED_BANNERS` | 16.2 | F16 MAN |  |
| 開發者 → 媒體服務測試 | Developer → Media Services Testing | `prefs:root=DEVELOPER_SETTINGS#MEDIA_SERVICES_TESTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → MIDI-CI測試 | Developer → MIDI-CI Testing | `prefs:root=DEVELOPER_SETTINGS#MIDI_CI_API_BETA` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 啟用MIDI-CI | Developer → Enable MIDI-CI | `prefs:root=DEVELOPER_SETTINGS#MIDI_CI_API_BETA_ENABLE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 新聞測試 | Developer → News Testing | `prefs:root=DEVELOPER_SETTINGS#NEWS_TESTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → NFC票卡密鑰（可留空） | Developer → NFC Pass Key Optional | `prefs:root=DEVELOPER_SETTINGS#NFC_PASS_KEY_OPTIONAL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 網路 | Developer → Networking | `prefs:root=DEVELOPER_SETTINGS#NLCGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → PassKit測試 | Developer → PassKit Testing | `prefs:root=DEVELOPER_SETTINGS#PASSKIT_TESTING` | 16.2 | F16 MAN |  |
| 開發者 → 重新索引所有項目 | Developer → Reindex All Items | `prefs:root=DEVELOPER_SETTINGS#REINDEX_ALL_ITEMS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 重新索引所有包含識別碼的項目 | Developer → Reindex All Items with Identifiers | `prefs:root=DEVELOPER_SETTINGS#REINDEX_ALL_ITEMS_WITH_IDENTIFIERS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 下次啟動時重置本機資料 | Developer → Reset Local Data on Next Launch | `prefs:root=DEVELOPER_SETTINGS#RESET_LOCAL_DATA_ON_NEXT_LAUNCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 重置媒體服務 | Developer → Reset Media Services | `prefs:root=DEVELOPER_SETTINGS#RESET_MEDIA_SERVICES` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 媒體播放程式架構測試 | Developer → Media Player Framework Testing | `prefs:root=DEVELOPER_SETTINGS#RoutineSettingsGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 強制將捷徑同步到手錶 | Developer → Force Sync Shortcuts to Watch | `prefs:root=DEVELOPER_SETTINGS#SIRI_ACTIONS_SYNC_WATCHOS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 捷徑測試 | Developer → Shortcuts Testing | `prefs:root=DEVELOPER_SETTINGS#SIRI_ACTIONS_TESTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 介面自動化 \| 啟用介面自動化 | Developer → Enable UI Automation \| UI Automation | `prefs:root=DEVELOPER_SETTINGS#UIAGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 外觀 | Developer → Appearance | `prefs:root=DEVELOPER_SETTINGS#UIAppearanceGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 深色外觀 | Developer → Dark Appearance | `prefs:root=DEVELOPER_SETTINGS#UIAppearanceSettings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 開發者 → 不受限的廣告呈現 | Developer → Unlimited Ad Presentation | `prefs:root=DEVELOPER_SETTINGS#UNLIMITED_AD_PRESENTATION` | 16.2 | F16 MAN |  |
| 開發者 → 電視業者測試 | Developer → TV Provider Testing | `prefs:root=DEVELOPER_SETTINGS#VideoSubscriberAccountSettingsGroup` | 16.2 | F16 MAN |  |
| 開發者 → 多重路徑網路 → 多重路徑網路 | Developer → Multipath Networking → Multipath Networking | `prefs:root=DEVELOPER_SETTINGS&path=MULTI_PATH_AGG#Multipath%20Networking` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Display & Brightness

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Display & Brightness | `prefs:root=Brightness` | — | DEAN TZ | 舊版、也見於 `app-settings:` |
| 外觀 \| 螢幕顯示與亮度 | Appearance \| Display & Brightness | `prefs:root=DISPLAY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| 外觀 \| 螢幕顯示與亮度 → 永遠顯示 | Appearance \| Display & Brightness → Always On Display | `prefs:root=DISPLAY&path=ALWAYS_ON` | 18.7 · 26.2 | F26 F18 |  |
| 外觀 \| 螢幕顯示與亮度 → 外觀 | Appearance \| Display & Brightness → Appearance | `prefs:root=DISPLAY&path=APPEARANCE` | 18.7 · 26.2 | F26 F18 MAN |  |
| — | Display → Options | `prefs:root=DISPLAY&path=APPEARANCE_OPTIONS` | — | FIFI WDG |  |
| 外觀 \| 螢幕顯示與亮度 → 自動鎖定 | Appearance \| Display & Brightness → Auto-Lock | `prefs:root=DISPLAY&path=AUTOLOCK` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| 外觀 \| 螢幕顯示與亮度 → 夜覽 | Appearance \| Display & Brightness → Night Shift | `prefs:root=DISPLAY&path=BLUE_LIGHT_REDUCTION` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG |  |
| 外觀 \| 螢幕顯示與亮度 → 相容App | Appearance \| Display & Brightness → Compatible Apps | `prefs:root=DISPLAY&path=COMPATIBLE_APPEARANCE` | 18.7 · 26.2 | F26 F18 |  |
| 外觀 \| 螢幕顯示與亮度 → 顯示方式 | Appearance \| Display & Brightness → View | `prefs:root=DISPLAY&path=MAGNIFY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN DYLD |  |
| 外觀 \| 螢幕顯示與亮度 → 文字大小 | Appearance \| Display & Brightness → Text Size | `prefs:root=DISPLAY&path=TEXT_SIZE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS |  |
| 外觀 \| 螢幕顯示與亮度 → 粗體文字 | Appearance \| Display & Brightness → Bold Text | `prefs:root=DISPLAY#BOLD_TEXT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 亮度 | Appearance \| Display & Brightness → Brightness | `prefs:root=DISPLAY#BRIGHTNESS` | 18.7 · 26.2 | F26 F18 |  |
| 外觀 \| 螢幕顯示與亮度 → 外觀 | Appearance \| Display & Brightness → Appearance | `prefs:root=DISPLAY#DEVICE_APPEARANCE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 螢幕縮放 | Appearance \| Display & Brightness → Display Zoom | `prefs:root=DISPLAY#DISPLAY_ZOOM_GROUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 抬起喚醒 | Appearance \| Display & Brightness → Raise to Wake | `prefs:root=DISPLAY#RAISE_TO_WAKE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 鎖定/解鎖 | Appearance \| Display & Brightness → Lock / Unlock | `prefs:root=DISPLAY#SMART_CASE_LOCK_SPEC` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 原彩 | Appearance \| Display & Brightness → True Tone | `prefs:root=DISPLAY#WHITE_BALANCE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 永遠顯示 → 永遠顯示 | Appearance \| Display & Brightness → Always On Display → Always On Display | `prefs:root=DISPLAY&path=ALWAYS_ON#ALWAYS_ON` | 18.7 · 26.2 | F26 F18 |  |
| 外觀 \| 螢幕顯示與亮度 → 外觀 → 使用兩手視窗縮放 | Appearance \| Display & Brightness → Appearance → Two-Handed Window Zoom | `prefs:root=DISPLAY&path=APPEARANCE#TWO_HANDED_WINDOW_ZOOM` | 18.7 · 26.2 | F26 F18 |  |
| 外觀 \| 螢幕顯示與亮度 → 外觀 → 視窗縮放 | Appearance \| Display & Brightness → Appearance → Window Zoom | `prefs:root=DISPLAY&path=APPEARANCE#WINDOW_ZOOM` | 18.7 · 26.2 | F26 F18 |  |
| 外觀 \| 螢幕顯示與亮度 → 夜覽 → 色溫 | Appearance \| Display & Brightness → Night Shift → Color Temperature | `prefs:root=DISPLAY&path=BLUE_LIGHT_REDUCTION#COLOR_TEMPERATURE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 夜覽 → 手動啟用直到明天為止 | Appearance \| Display & Brightness → Night Shift → Manually Enable Until Tomorrow | `prefs:root=DISPLAY&path=BLUE_LIGHT_REDUCTION#MANUAL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 夜覽 → 已排程 | Appearance \| Display & Brightness → Night Shift → Scheduled | `prefs:root=DISPLAY&path=BLUE_LIGHT_REDUCTION#SCHEDULED` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 外觀 \| 螢幕顯示與亮度 → 相容App → 深色、淺色 | Appearance \| Display & Brightness → Compatible Apps → Dark, Light | `prefs:root=DISPLAY&path=COMPATIBLE_APPEARANCE#COMPATIBLE_APPEARANCE_CHOICES` | 18.7 · 26.2 | F26 F18 |  |

### Emergency SOS

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| SOS緊急服務 | Emergency SOS | `prefs:root=EMERGENCY_SOS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS |  |
| — | — | `prefs:root=EMERGENCY_SOS%23-64` | — | MAN DYLD |  |
| — | Emergency SOS → Countdown Sound | `prefs:root=EMERGENCY_SOS#ALARM_SOUND_GROUP` | — | MEHDI |  |
| SOS緊急服務 → 倒數聲 | Emergency SOS → Countdown Sound | `prefs:root=EMERGENCY_SOS#ALARM_SOUND_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| SOS緊急服務 → 自動通話 | Emergency SOS → Auto Call | `prefs:root=EMERGENCY_SOS#AUTO_CALL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | Emergency SOS → Call with Hold | `prefs:root=EMERGENCY_SOS#CALL_WITH_HOLD` | — | MEHDI |  |
| — | Emergency SOS → Call with Hold (jump to section) | `prefs:root=EMERGENCY_SOS#CALL_WITH_HOLD_GROUP` | — | MEHDI |  |
| — | Emergency SOS → Call with 5 Presses | `prefs:root=EMERGENCY_SOS#CALL_WITH_PRESSES` | — | MEHDI |  |
| — | Emergency SOS → Call with 5 Presses (jump to section) | `prefs:root=EMERGENCY_SOS#CALL_WITH_PRESSES_GROUP` | — | MEHDI |  |
| SOS緊急服務 → 透過側邊按鈕通話 | Emergency SOS → Call with Side Button | `prefs:root=EMERGENCY_SOS#CALL_WITH_SIDE_BUTTON` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| — | Emergency SOS → Call with Side Button (jump to section) | `prefs:root=EMERGENCY_SOS#CALL_WITH_SIDE_BUTTON_GROUP` | — | MEHDI |  |
| SOS緊急服務 → 緊急聯絡人 | Emergency SOS → Emergency Contacts | `prefs:root=EMERGENCY_SOS#EMERGENCY_CONTACTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| — | Emergency SOS → Set up Emergency Contacts in Health | `prefs:root=EMERGENCY_SOS#OPEN_HEALTH` | — | MEHDI |  |
| — | Emergency SOS → Animation Demo (highlight animation) | `prefs:root=EMERGENCY_SOS#TRIGGER_ANIMATION` | — | MEHDI |  |
| — | Emergency SOS → Animation Demo (jump to section) | `prefs:root=EMERGENCY_SOS#TRIGGER_ANIMATION_GROUP` | — | MEHDI |  |

### Exposure Notifications

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 暴露通知 | Exposure Notifications | `prefs:root=EXPOSURE_NOTIFICATION` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG |  |

### Face ID & Passcode

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 | Face ID & Passcode \| Passcode \| Touch ID & Passcode | `prefs:root=PASSCODE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 需要密碼 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Require Passcode | `prefs:root=PASSCODE&path=PASSCODE_REQ` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 鎖定時允許取用 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Allow Access When Locked | `prefs:root=PASSCODE#ALLOW_ACCESS_WHEN_LOCKED` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 透過Apple Watch解鎖 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Unlock with Apple Watch | `prefs:root=PASSCODE#AUTO_UNLOCK_DEVICES_GROUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 更改裝置密碼 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Change Passcode | `prefs:root=PASSCODE#CHANGE_PASSCODE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 遭竊裝置防護 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Stolen Device Protection | `prefs:root=PASSCODE#DTO_GROUP_ID` | 18.7 · 26.2 | F26 F18 WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 家庭控制 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Home Control | `prefs:root=PASSCODE#HOME_CONTROL_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 關閉密碼 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Turn Passcode Off | `prefs:root=PASSCODE#PASSCODE_OFF` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 用訊息回覆 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Reply with Message | `prefs:root=PASSCODE#REPLY_WITH_MESSAGE_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 回撥未接來電 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Return Missed Calls | `prefs:root=PASSCODE#RETURN_MISSED_CALLS_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 語音撥號 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Voice Dial | `prefs:root=PASSCODE#VOICE_DIAL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 錢包 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Wallet | `prefs:root=PASSCODE#WALLET_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| Face ID與密碼 \| Touch ID與密碼 \| 裝置密碼 → 清除資料 | Face ID & Passcode \| Passcode \| Touch ID & Passcode → Erase Data | `prefs:root=PASSCODE#WIPE_DEVICE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### FACEBOOK

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=FACEBOOK` | — | MR | 舊版、也見於 `App-Prefs:` |

### FaceTime

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| FaceTime | FaceTime | `prefs:root=FACETIME` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | FaceTime → Siri & Search | `prefs:root=FACETIME&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |

### FLICKR

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=FLICKR` | — | MR | 舊版、也見於 `App-Prefs:` |

### Focus

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 專注模式 | Focus | `prefs:root=DO_NOT_DISTURB` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| — | Focus (Do Not Disturb) → Allow Calls From | `prefs:root=DO_NOT_DISTURB&path=Allow%20Calls%20From` | — | FIFI MAN MEHDI WDG MS |  |
| — | Focus (Do Not Disturb) → Auto-Reply To | `prefs:root=DO_NOT_DISTURB&path=DRIVER_MODE_AUTOREPLY` | — | FIFI MAN WDG |  |
| — | Focus (Do Not Disturb) → Auto-Reply | `prefs:root=DO_NOT_DISTURB&path=DRIVER_MODE_AUTOREPLY_MESSAGE` | — | FIFI MAN WDG |  |
| 專注模式 → 專注模式狀態 | Focus → Focus Status | `prefs:root=DO_NOT_DISTURB&path=status` | 16.2 · 18.7 · 26.2 | F26 F18 F16 |  |
| — | — | `prefs:root=DO_NOT_DISTURB#DRIVER_MODE_TITLE` | — | MAN |  |
| — | — | `prefs:root=DO_NOT_DISTURB#Repeated%20Calls` | — | MAN |  |
| — | — | `prefs:root=DO_NOT_DISTURB#Scheduled` | — | MAN |  |
| — | — | `prefs:root=DO_NOT_DISTURB&path=DRIVER_MODE_TURN_ON#Activate%20With%20CarPlay` | — | MAN |  |

### FollowUpList_

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=FollowUpList_` | — | MAN DYLD |  |

### Freeform

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 無邊記 | Freeform | `prefs:root=FREEFORM` | 18.7 · 26.2 | F26 F18 |  |

### Game Center

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Game Center | Game Center | `prefs:root=GAMECENTER` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| — | Game Center → Add Friends | `prefs:root=GAMECENTER&path=Add%20Friends` | — | FIFI WDG |  |
| — | Game Center → Terms and Conditions | `prefs:root=GAMECENTER&path=Terms%20and%20Conditions` | — | FIFI WDG |  |

### General

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 一般 | General | `prefs:root=General` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → 關於本機 | General → About | `prefs:root=General&path=About` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | Accessibility | `prefs:root=General&path=ACCESSIBILITY` | — | DEAN TZ MR | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → AirDrop | General → AirDrop | `prefs:root=General&path=AIRDROP_LINK` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| — | Siri iOS < 10? | `prefs:root=General&path=Assistant` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → 背景App重新整理 | General → Background App Refresh | `prefs:root=General&path=AUTO_CONTENT_DOWNLOAD` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| 一般 → 自動填寫與密碼 | General → AutoFill & Passwords | `prefs:root=General&path=AUTOFILL` | 18.7 · 26.2 | F26 F18 |  |
| — | Auto-Lock iOS < 10 | `prefs:root=General&path=AUTOLOCK` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | Bluetooth iOS < 9 | `prefs:root=General&path=Bluetooth` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → CarPlay | General → CarPlay | `prefs:root=General&path=CARPLAY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 一般 → AirPlay與接續互通 | General → AirPlay & Continuity | `prefs:root=General&path=CONTINUITY_SPEC` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 一般 → 日期與時間 | General → Date & Time | `prefs:root=General&path=DATE_AND_TIME` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → 辭典 | General → Dictionary | `prefs:root=General&path=DICTIONARY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| — | Do Not Disturb | `prefs:root=General&path=DO_NOT_DISTURB` | — | DEAN | 舊版、也見於 `App-Prefs:` |
| 一般 → 主畫面按鈕 | General → Home Button | `prefs:root=General&path=HOME_BUTTON` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 語言與地區 | General → Language & Region | `prefs:root=General&path=INTERNATIONAL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → 鍵盤 | General → Keyboard | `prefs:root=General&path=Keyboard` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → 法律資訊與電信規範 | General → Legal & Regulatory | `prefs:root=General&path=LEGAL_AND_REGULATORY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 一般 → VPN與裝置管理 | General → VPN & Device Management | `prefs:root=General&path=ManagedConfigurationList` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | General → Multitasking (iPad-only) | `prefs:root=General&path=MULTITASKING` | — | DEP MEHDI MS MR | 也見於 `App-Prefs:` |
| — | Network iOS < 10? | `prefs:root=General&path=Network` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → NFC | General → NFC | `prefs:root=General&path=NFC_LINK` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN DYLD MEHDI WDG |  |
| 一般 → 子母畫面 | General → Picture in Picture | `prefs:root=General&path=PiP_SPEC` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 觸控式軌跡板 \| 觸控式軌跡板與滑鼠 | General → Trackpad \| Trackpad & Mouse | `prefs:root=General&path=POINTERS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 電信規範 | General → Regulatory | `prefs:root=General&path=REGULATORY` | 16.2 | F16 MAN MEHDI |  |
| 一般 → 重置 | General → Reset | `prefs:root=General&path=Reset` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=General&path=RESTRICTIONS` | — | MAN DYLD |  |
| — | — | `prefs:root=General&path=SIRI` | — | MAN DYLD |  |
| 一般 → 軟體更新 | General → Software Update | `prefs:root=General&path=SOFTWARE_UPDATE_LINK` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=General&path=STORAGE_ICLOUD_USAGE` | — | MR | 舊版、也見於 `App-Prefs:` |
| 一般 → 儲存空間 | General → Storage | `prefs:root=General&path=STORAGE_MGMT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG |  |
| 一般 → 電視輸出 | General → TV Out | `prefs:root=General&path=TV_OUT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| — | Usage | `prefs:root=General&path=USAGE` | — | MAN DYLD DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → VPN | General → VPN | `prefs:root=General&path=VPN` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| 一般 → 手勢 | General → Gestures | `prefs:root=General#Multitasking_Gesture_Switch` | 16.2 | F16 MAN MEHDI |  |
| 一般 → 側邊切換 | General → Side Switch | `prefs:root=General#Rotation_Switch_Action_Group` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 關機 | General → Shut Down | `prefs:root=General#SHUTDOWN_LABEL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 關於本機 → 機型型號 | General → About → Model Number | `prefs:root=General&path=About#ProductModel` | 18.7 · 26.2 | F26 F18 WDG |  |
| 一般 → 關於本機 → 機型名稱 | General → About → Model Name | `prefs:root=General&path=About#ProductModelName` | 18.7 · 26.2 | F26 F18 WDG |  |
| 一般 → 關於本機 → 序號 | General → About → Serial Number | `prefs:root=General&path=About#SerialNumber` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | — | `prefs:root=General&path=About/APPLICATIONS` | — | MAN DYLD |  |
| 一般 → 關於本機 → 信任的憑證 | General → About → Trusted Certificates | `prefs:root=General&path=About/CERT_TRUST_SETTINGS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| — | General → About → SEID | `prefs:root=General&path=About/SEID` | — | FIFI WDG |  |
| 一般 → 關於本機 → iOS版本 | General → About → iOS Version | `prefs:root=General&path=About/SW_VERSION_SPECIFIER` | 18.7 · 26.2 | F26 F18 WDG |  |
| 一般 → AirDrop → 將裝置互相靠近 | General → AirDrop → Bringing Devices Together | `prefs:root=General&path=AIRDROP_LINK#AIRDROP_NFC_ID` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | General → Background App Refresh → Background App Refresh | `prefs:root=General&path=AUTO_CONTENT_DOWNLOAD/AUTO_CONTENT_DOWNLOAD` | — | FIFI WDG |  |
| 一般 → 自動填寫與密碼 → 自動填寫密碼 | General → AutoFill & Passwords → AutoFill Passwords | `prefs:root=General&path=AUTOFILL#AUTOFILL` | 18.7 · 26.2 | F26 F18 |  |
| 一般 → 自動填寫與密碼 → 清除驗證碼 | General → AutoFill & Passwords → Clean up verification codes | `prefs:root=General&path=AUTOFILL#CLEAN_UP_VERIFICATION_CODES` | 18.7 · 26.2 | F26 F18 |  |
| 一般 → 自動填寫與密碼 → 設定驗證碼 | General → AutoFill & Passwords → Set up verification codes | `prefs:root=General&path=AUTOFILL#SET_UP_VERIFICATION_CODES` | 18.7 · 26.2 | F26 F18 |  |
| 一般 → AirPlay與接力 → 自動AirPlay到電視 | General → AirPlay & Handoff → Automatically AirPlay to TVs | `prefs:root=General&path=CONTINUITY_SPEC#AIRPLAY_TO_TV` | 16.2 | F16 MAN MEHDI |  |
| 一般 → AirPlay與接續互通 → 自動AirPlay | General → AirPlay & Continuity → Automatically AirPlay | `prefs:root=General&path=CONTINUITY_SPEC#AUTOMATICALLY_AIRPLAY` | 18.7 · 26.2 | F26 F18 WDG |  |
| 一般 → AirPlay與接續互通 → 接力 | General → AirPlay & Continuity → Handoff | `prefs:root=General&path=CONTINUITY_SPEC#CONTINUITY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → AirPlay與接續互通 → 傳送到HomePod | General → AirPlay & Continuity → Transfer to HomePod | `prefs:root=General&path=CONTINUITY_SPEC#TRANSFER_TO_HOMEPOD` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → AirPlay與接續互通 → 接續互通相機 | General → AirPlay & Continuity → Continuity Camera | `prefs:root=General&path=CONTINUITY_SPEC#WOMBAT_CAMERA` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |
| 一般 → AppleCare與保固 | General → AppleCare & Warranty | `prefs:root=General&path=COVERAGE/` | 18.7 · 26.2 | F26 F18 | 結尾斜線來自系統檔 |
| 一般 → 語言與地區 → 加入語言⋯ | General → Language & Region → Add Language… | `prefs:root=General&path=INTERNATIONAL#ADD_PREFERRED_LANGUAGE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 語言與地區 → 其他語言⋯ | General → Language & Region → Other Languages… | `prefs:root=General&path=INTERNATIONAL#NEW_PREFERRED_LANGUAGE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 語言與地區 → 偏好的語言順序 | General → Language & Region → Preferred Language Order | `prefs:root=General&path=INTERNATIONAL#PREFERRED_LANGUAGE_GROUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 語言與地區 → 行事曆 | General → Language & Region → Calendar | `prefs:root=General&path=INTERNATIONAL/CALENDAR` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | General → Language & Region → Device Language | `prefs:root=General&path=INTERNATIONAL/DEVICE_LANGUAGE` | — | FIFI WDG |  |
| 一般 → 語言與地區 → 地區 | General → Language & Region → Region | `prefs:root=General&path=INTERNATIONAL/LOCALE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 一般 → 語言與地區 → 數字 | General → Language & Region → Numbers | `prefs:root=General&path=INTERNATIONAL/NUMBERING_SYSTEM` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 一般 → 語言與地區 → 溫度單位 | General → Language & Region → Temperature Unit | `prefs:root=General&path=INTERNATIONAL/TEMPERATURE_UNIT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 一般 → 鍵盤 → 自動標點符號 | General → Keyboard → Auto-Punctuation | `prefs:root=General&path=Keyboard#AutoPunctuationSetting` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |
| 一般 → 鍵盤 → 啟用聽寫 | General → Keyboard → Enable Dictation | `prefs:root=General&path=Keyboard#Dictation` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 啟用按鍵滑動 | General → Keyboard → Enable Key Flicks | `prefs:root=General&path=Keyboard#GesturesEnabled` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 預覽字元 | General → Keyboard → Character Preview | `prefs:root=General&path=Keyboard#KeyboardAllowPaddle` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 快速鍵 | General → Keyboard → Shortcuts | `prefs:root=General&path=Keyboard#KeyboardAssistant` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 自動大寫 | General → Keyboard → Auto-Capitalization | `prefs:root=General&path=Keyboard#KeyboardAutocapitalization` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 自動修正 | General → Keyboard → Auto-Correction | `prefs:root=General&path=Keyboard#KeyboardAutocorrection` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 啟用大寫鎖定鍵 | General → Keyboard → Enable Caps Lock | `prefs:root=General&path=Keyboard#KeyboardCapsLock` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 檢查拼字 | General → Keyboard → Check Spelling | `prefs:root=General&path=Keyboard#KeyboardCheckSpelling` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 滑動輸入 | General → Keyboard → Slide to type | `prefs:root=General&path=Keyboard#KeyboardContinuousPathEnabled` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 句號快速鍵 | General → Keyboard → “.” Shortcut | `prefs:root=General&path=Keyboard#KeyboardPeriodShortcut` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 預測字詞 | General → Keyboard → Predictive | `prefs:root=General&path=Keyboard#KeyboardPrediction` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 分開式鍵盤 | General → Keyboard → Split Keyboard | `prefs:root=General&path=Keyboard#RivenKeyboard` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 一般 → 鍵盤 → 智慧型標點符號 | General → Keyboard → Smart Punctuation | `prefs:root=General&path=Keyboard#SmartTyping` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | — | `prefs:root=General&path=Keyboard/DictationSettings` | — | MAN DYLD |  |
| — | General → Keyboard → Hardware Keyboard | `prefs:root=General&path=Keyboard/Hardware%20Keyboard` | — | FIFI MAN DYLD WDG MS |  |
| 一般 → 鍵盤 → 鍵盤 | General → Keyboard → Keyboards | `prefs:root=General&path=Keyboard/KEYBOARDS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| — | General → Keyboard → One Handed Keyboard | `prefs:root=General&path=Keyboard/ReachableKeyboard` | — | FIFI MEHDI WDG MS |  |
| 一般 → 鍵盤 → 替代文字 | General → Keyboard → Text Replacement | `prefs:root=General&path=Keyboard/USER_DICTIONARY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 一般 → 法律資訊與電信規範 → 保固 | General → Legal & Regulatory → Warranty | `prefs:root=General&path=LEGAL_AND_REGULATORY#Warranty` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | — | `prefs:root=General&path=ManagedConfigurationList/InstallRequested` | — | MAN DYLD |  |
| — | — | `prefs:root=General&path=ManagedConfigurationList/ProfileError` | — | MAN DYLD |  |
| — | — | `prefs:root=General&path=ManagedConfigurationList/ProvisioningInstallRequested` | — | MAN DYLD |  |
| — | General → Profiles → Install Profile | `prefs:root=General&path=ManagedConfigurationList/PurgatoryInstallRequested` | — | FIFI MAN DYLD WDG |  |
| — | VPN iOS < 10? | `prefs:root=General&path=Network/VPN` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| 一般 → 重置 → 移除所有行動數據方案 | General → Reset → Remove All Cellular Data Plans | `prefs:root=General&path=Reset#cellularErase` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 清除所有內容和設定 | General → Reset → Erase All Content and Settings | `prefs:root=General&path=Reset#fullErase` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 重置主畫面佈局 | General → Reset → Reset Home Screen Layout | `prefs:root=General&path=Reset#RESET_ICONS_LABEL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 重置鍵盤辭典 | General → Reset → Reset Keyboard Dictionary | `prefs:root=General&path=Reset#RESET_KEYBOARD_DICTIONARY_LABEL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 重置網路設定 | General → Reset → Reset Network Settings | `prefs:root=General&path=Reset#RESET_NETWORK_LABEL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 重置定位服務與隱私權 | General → Reset → Reset Location & Privacy | `prefs:root=General&path=Reset#RESET_PRIVACY_LABEL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 重置所有設定 | General → Reset → Reset All Settings | `prefs:root=General&path=Reset#settingsErase` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 重置 → 訂戶服務 | General → Reset → Subscriber Services | `prefs:root=General&path=Reset#SUBSCRIBER_SERVICES_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 軟體更新 → 自動更新 | General → Software Update → Automatic Updates | `prefs:root=General&path=SOFTWARE_UPDATE_LINK/SUAutomaticUpdateButton` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | — | `prefs:root=General&path=STORAGE_ICLOUD_USAGE/DEVICE_STORAGE` | — | MR | 舊版、也見於 `App-Prefs:` |
| 一般 → 儲存空間 → 儲存空間 | General → Storage → Storage | `prefs:root=General&path=STORAGE_MGMT#MANAGE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 一般 → 儲存空間 → 卸載未使用的App | General → Storage → Offload Unused Apps | `prefs:root=General&path=STORAGE_MGMT#OFFLOAD` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| — | — | `prefs:root=General&path=USAGE/CELLULAR_USAGE` | — | TZ | 舊版、也見於 `app-settings:` |
| — | General → VPN → Add VPN Configuration… | `prefs:root=General&path=VPN/Add%20VPN%20Configuration%E2%80%A6` | — | FIFI WDG |  |
| — | General → VPN → DNS | `prefs:root=General&path=VPN/DNS` | — | FIFI WDG MS |  |

### Health Data

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 健康 \| 健康資料 | Health \| Health Data | `prefs:root=HEALTH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Health → Siri & Search | `prefs:root=HEALTH&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |

### HealthKit

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | HealthKit | `prefs:root=HealthKit` | — | DEAN | 舊版、也見於 `App-Prefs:` |

### Home

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Home | `prefs:root=HOMEKIT` | — | FIFI WDG |  |

### Home Screen

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 主畫面 | Home Screen | `prefs:root=HOME_SCREEN` | 16.2 · 18.7 | F18 F16 FIFI MAN WDG |  |
| 主畫面 → 新下載的App | Home Screen → Newly Downloaded Apps | `prefs:root=HOME_SCREEN&path=APP_DOWNLOADS_GO_TO` | 16.2 · 18.7 | F18 F16 MAN |  |
| 主畫面 → 通知標記 | Home Screen → Notification Badges | `prefs:root=HOME_SCREEN#BADGES_IN_APP_LIBRARY` | 16.2 · 18.7 | F18 F16 MAN |  |

### Home Screen & App Library

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 主畫面與App資料庫 | Home Screen & App Library | `prefs:root=HOME_SCREEN_DOCK` | 16.2 · 18.7 | F18 F16 FIFI MAN WDG |  |
| 主畫面與App資料庫 → 新下載的App | Home Screen & App Library → Newly Downloaded Apps | `prefs:root=HOME_SCREEN_DOCK&path=APP_DOWNLOADS_GO_TO` | 18.7 | F18 |  |
| 主畫面與App資料庫 → 幕前調度 | Home Screen & App Library → Stage Manager | `prefs:root=HOME_SCREEN_DOCK&path=CONTINUOUS-EXPOSE` | 18.7 | F18 |  |
| — | Home Screen & Dock (iPad) → Multitasking | `prefs:root=HOME_SCREEN_DOCK&path=MULTITASKING` | — | FIFI MAN WDG |  |
| 主畫面與App資料庫 → Dock | Home Screen & App Library → Dock | `prefs:root=HOME_SCREEN_DOCK&path=MULTITASKING_DOCK` | 18.7 | F18 MAN |  |
| 主畫面與App資料庫 → 在Dock中顯示建議的App和最近使用的App | Home Screen & App Library → Show Suggested and Recent Apps in Dock | `prefs:root=HOME_SCREEN_DOCK#ALLOW_RECENTS` | 16.2 · 18.7 | F18 F16 MAN |  |
| — | — | `prefs:root=HOME_SCREEN_DOCK#APP_ICON_SIZE_GROUP` | — | MAN |  |
| — | — | `prefs:root=HOME_SCREEN_DOCK#MULTITASKING_DOCK` | — | MAN |  |
| — | — | `prefs:root=HOME_SCREEN_DOCK#TODAY_VIEW_GROUP` | — | MAN |  |
| — | — | `prefs:root=HOME_SCREEN_DOCK#TODAY_VIEW_ON_HOME_SCREEN` | — | MAN |  |
| — | — | `prefs:root=HOME_SCREEN_DOCK&path=MULTITASKING#ALLOW_MULTIPLE_APPS` | — | MAN |  |
| — | — | `prefs:root=HOME_SCREEN_DOCK&path=MULTITASKING#Mutltitasking_Gesture_Switch` | — | MAN |  |
| 主畫面與App資料庫 → Dock → 在Dock中顯示App資料庫 | Home Screen & App Library → Dock → Show App Library in Dock | `prefs:root=HOME_SCREEN_DOCK&path=MULTITASKING_DOCK#SHOW_APP_LIBRARY` | 16.2 · 18.7 | F18 F16 |  |

### ICLOUD_ID

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=ICLOUD_ID` | — | MAN DYLD |  |

### INTERNAL_SETTINGS

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=INTERNAL_SETTINGS&path=Home` | — | MAN DYLD |  |
| — | — | `prefs:root=INTERNAL_SETTINGS&path=HomeKit` | — | MAN DYLD |  |
| — | — | `prefs:root=INTERNAL_SETTINGS&path=Prototyping` | — | MAN DYLD |  |
| — | — | `prefs:root=INTERNAL_SETTINGS&path=Siri` | — | MAN DYLD |  |
| — | — | `prefs:root=INTERNAL_SETTINGS&path=Siri%20Shortcuts` | — | MAN DYLD |  |
| — | — | `prefs:root=INTERNAL_SETTINGS&path=sysdiagnose` | — | MAN DYLD |  |

### Journal

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 日誌 | Journal | `prefs:root=JOURNAL` | 18.7 · 26.2 | F26 F18 FIFI GH |  |
| — | Journal → Journaling Schedule | `prefs:root=JOURNAL&path=journalingSchedule` | — | FIFI |  |

### Location Services

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Location Services | `prefs:root=LOCATION_SERVICES` | — | DEAN TZ MR | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |

### Mail

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 郵件 | Mail | `prefs:root=MAIL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 帳號 | Mail → Accounts | `prefs:root=MAIL&path=ACCOUNTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 封鎖名單 | Mail → Blocked | `prefs:root=MAIL&path=Blocked` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 已封鎖的寄件人選項 | Mail → Blocked Sender Options | `prefs:root=MAIL&path=Blocked%20Sender%20Options` | 18.7 · 26.2 | F26 F18 FIFI MEHDI WDG MS |  |
| — | Mail → Default Account | `prefs:root=MAIL&path=Default%20Account` | — | FIFI MEHDI WDG MS |  |
| 郵件 → 在回覆中加入附件 | Mail → Include Attachments with Replies | `prefs:root=MAIL&path=Include%20Attachments%20with%20Replies` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 增加引言層級 | Mail → Increase Quote Level | `prefs:root=MAIL&path=Increase%20Quote%20Level` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 標示地址 | Mail → Mark Addresses | `prefs:root=MAIL&path=Mark%20Addresses` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 已靜音的討論串動作 | Mail → Muted Thread Action | `prefs:root=MAIL&path=Muted%20Thread%20Action` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Mail → Notifications | `prefs:root=MAIL&path=NOTIFICATIONS` | — | FIFI MEHDI WDG MS |  |
| 郵件 → 預覽 | Mail → Preview | `prefs:root=MAIL&path=Preview` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 簽名 | Mail → Signature | `prefs:root=MAIL&path=Signature` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 滑動選項 | Mail → Swipe Options | `prefs:root=MAIL&path=Swipe%20Options` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 郵件 → 寄送密件副本給自己 | Mail → Always Bcc Myself | `prefs:root=MAIL#Always%20Bcc%20Myself` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 刪除前先詢問 | Mail → Ask Before Deleting | `prefs:root=MAIL#Ask%20Before%20Deleting` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 收合已讀郵件 | Mail → Collapse Read Messages | `prefs:root=MAIL#Collapse%20Read%20Messages` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 完整討論串 | Mail → Complete Threads | `prefs:root=MAIL#Complete%20Threads` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 忽略已封鎖的寄件人 | Mail → Ignore Blocked Senders | `prefs:root=MAIL#Ignore%20Blocked%20Senders` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 載入遠端影像 | Mail → Load Remote Images | `prefs:root=MAIL#Load%20Remote%20Images` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 最新的郵件置於最上方 | Mail → Most Recent Message on Top | `prefs:root=MAIL#Most%20Recent%20Message%20on%20Top` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 以討論串來分類 | Mail → Organize by Thread | `prefs:root=MAIL#Organize%20by%20Thread` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 帳號 → 加入帳號 | Mail → Accounts → Add Account | `prefs:root=MAIL&path=ACCOUNTS#ADD_ACCOUNT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 郵件 → 帳號 → 擷取新資料 | Mail → Accounts → Fetch New Data | `prefs:root=MAIL&path=ACCOUNTS#FETCH_NEW_DATA` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | Mail → Swipe Options → Swipe Left | `prefs:root=MAIL&path=Swipe%20Options/Swipe%20Left` | — | FIFI WDG |  |
| — | Mail → Swipe Options → Swipe Right | `prefs:root=MAIL&path=Swipe%20Options/Swipe%20Right` | — | FIFI WDG |  |
| 郵件 → 顯示收件人/副本標籤 | Mail → Show To/Cc Labels | `prefs:root=MAIL#Show%20To/Cc%20Labels` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Maps

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 地圖 | Maps | `prefs:root=MAPS` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| — | Maps → Cycling | `prefs:root=MAPS&path=Cycling` | — | FIFI WDG |  |
| 地圖 → 自行車 | Maps → Cycling | `prefs:root=MAPS&path=CyclingLinkPreferenceID` | 18.7 | F18 |  |
| — | Maps → Driving | `prefs:root=MAPS&path=Driving` | — | FIFI WDG |  |
| — | Maps → Driving & Navigation | `prefs:root=MAPS&path=Driving%20%26%20Navigation` | — | DEP MS |  |
| — | Maps → Driving & Navigation (open menu) * | `prefs:root=MAPS&path=Driving%20&%20Navigation` | — | MAN MEHDI |  |
| 地圖 → 開車 | Maps → Driving | `prefs:root=MAPS&path=DrivingLinkPreferenceID` | 18.7 | F18 |  |
| 地圖 → 語音導航 | Maps → Spoken Directions | `prefs:root=MAPS&path=NavigationGuidanceLinkPreferenceID` | 18.7 | F18 |  |
| — | Maps → Transit | `prefs:root=MAPS&path=Transit` | — | FIFI MAN MEHDI WDG MS |  |
| 地圖 → 大眾運輸 | Maps → Transit | `prefs:root=MAPS&path=TransitLinkPreferenceID` | 18.7 | F18 |  |
| — | Maps → Walking (iPhone) | `prefs:root=MAPS&path=Walking` | — | FIFI MAN MEHDI WDG |  |
| 地圖 → 步行 | Maps → Walking | `prefs:root=MAPS&path=WalkingLinkPreferenceID` | 18.7 | F18 |  |
| — | Maps → Climate \| Air Quality Index | `prefs:root=MAPS#Air%20Quality%20Index` | — | MAN MEHDI |  |
| 地圖 → 空氣品質指標 | Maps → Air Quality Index | `prefs:root=MAPS#AirQualityPreferenceID` | 18.7 | F18 |  |
| — | Maps → Map Labels \| Always in English | `prefs:root=MAPS#Always%20in%20English` | — | MAN MEHDI |  |
| — | Maps → Distances (jump to section) | `prefs:root=MAPS#Distances` | — | MAN MEHDI |  |
| 地圖 → 總是使用中文 | Maps → Always in English | `prefs:root=MAPS#LabelLanguageAlwaysUIPreferenceID` | 18.7 | F18 |  |
| 地圖 → 顯示停車位置 | Maps → Show Parked Location | `prefs:root=MAPS#ParkedCarPreferenceID` | 18.7 | F18 |  |
| — | Maps → Preferred Transportation Type (jump to section) | `prefs:root=MAPS#Preferred%20Transportation%20Type` | — | MAN MEHDI |  |
| 地圖 → 分享抵達時間 | Maps → Share ETA | `prefs:root=MAPS#ShareETAPreferenceID` | 18.7 | F18 |  |
| — | Maps → Your Car \| Show Parked Location | `prefs:root=MAPS#Show%20Parked%20Location` | — | MAN MEHDI |  |
| 地圖 → 偏好的交通類型 | Maps → Preferred Type of Travel | `prefs:root=MAPS#TransportTypePreferenceGroupID` | 18.7 | F18 |  |
| — | Maps → Climate \| Weather Conditions | `prefs:root=MAPS#Weather%20Conditions` | — | MAN MEHDI |  |
| 地圖 → 天氣狀況 | Maps → Weather Conditions | `prefs:root=MAPS#WeatherConditionsPreferenceID` | 18.7 | F18 |  |
| — | Maps → Driving & Navigation → Avoid (jump to section) * | `prefs:root=MAPS&path=Driving%20&%20Navigation#Avoid` | — | MAN MEHDI |  |
| — | Maps → Driving & Navigation → Show in Navigation \| Compass (jump to toggle) * | `prefs:root=MAPS&path=Driving%20&%20Navigation#Compass` | — | MAN MEHDI |  |
| — | Maps → Driving & Navigation → Navigation Voice Volume (jump to section) * | `prefs:root=MAPS&path=Driving%20&%20Navigation#Navigation%20Voice%20Volume` | — | MAN MEHDI |  |
| — | Maps → Driving & Navigation → Pause Spoken Audio (jump to toggle) * | `prefs:root=MAPS&path=Driving%20&%20Navigation#Pause%20Spoken%20Audio` | — | MAN MEHDI |  |
| — | Maps → Driving & Navigation → Show in Navigation (jump to section) * | `prefs:root=MAPS&path=Driving%20&%20Navigation#Show%20in%20Navigation` | — | MAN MEHDI |  |
| — | Maps → Driving & Navigation → Show in Navigation \| Speed Limit (jump to toggle) * | `prefs:root=MAPS&path=Driving%20&%20Navigation#Speed%20Limit` | — | MAN MEHDI |  |
| — | Maps → Walking → Optical Heading | `prefs:root=MAPS&path=Walking#Optical%20Heading` | — | MAN MEHDI |  |

### Measure

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 測距儀 | Measure | `prefs:root=MEASURE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Measure → Siri & Search | `prefs:root=MEASURE&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| 測距儀 → 英制 | Measure → Imperial | `prefs:root=MEASURE#Imperial` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 測距儀 → 測量單位 | Measure → Measure Units | `prefs:root=MEASURE#MEASURE_UNITS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 測距儀 → 公制 | Measure → Metric | `prefs:root=MEASURE#Metric` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Messages

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 訊息 | Messages | `prefs:root=MESSAGES` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| — | — | `prefs:root=MESSAGES&path=JUNK_CONVERSATIONS_BUTTON` | — | MAN DYLD |  |
| — | — | `prefs:root=MESSAGES&path=MMS_EMAIL` | — | MAN DYLD |  |

### Multitasking & Gestures

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Multitasking & Gestures | Multitasking & Gestures | `prefs:root=com.apple.MultitaskingAndGesturesSettings` | 18.7 | F18 MAN |  |
| Multitasking & Gestures → 角落手勢 | Multitasking & Gestures → Corner Gestures | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=CornerGestures` | 18.7 | F18 |  |
| Multitasking & Gestures → 四指與五指手勢 | Multitasking & Gestures → Four & Five Finger Gestures | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=FourAndFiveFingers` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 | Multitasking & Gestures → Multitasking | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking` | 18.7 | F18 |  |
| Multitasking & Gestures → 子母畫面 | Multitasking & Gestures → Picture in Picture | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=PictureInPicture` | 18.7 | F18 |  |
| Multitasking & Gestures → 高效率手勢 | Multitasking & Gestures → Productivity Gestures | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Productivity` | 18.7 | F18 MAN |  |
| Multitasking & Gestures → 晃動來還原 | Multitasking & Gestures → Shake to Undo | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=ShakeToUndo` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 → 允許多個App | Multitasking & Gestures → Multitasking → Allow Multiple Apps | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking#MultipleApps` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 → 螢幕鏡像輸出 | Multitasking & Gestures → Multitasking → Screen Mirroring | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking#ScreenMirroring` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 → 分割顯示與滑動置前 | Multitasking & Gestures → Multitasking → Split View & Slide Over | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking#SplitViewSlideOver` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 → 幕前調度 | Multitasking & Gestures → Multitasking → Stage Manager | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking#StageManager` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 → 在幕前調度中顯示Dock | Multitasking & Gestures → Multitasking → Show Dock in Stage Manager | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking#StageManagerDock` | 18.7 | F18 |  |
| Multitasking & Gestures → 多工處理 → 在幕前調度中顯示最近使用的App | Multitasking & Gestures → Multitasking → Show Recent Apps in Stage Manager | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Multitasking#StageManagerRecentApps` | 18.7 | F18 |  |
| Multitasking & Gestures → 高效率手勢 → 手勢 | Multitasking & Gestures → Productivity Gestures → Gestures | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Productivity#Gestures` | 18.7 | F18 |  |
| Multitasking & Gestures → 高效率手勢 → 高效率手勢 | Multitasking & Gestures → Productivity Gestures → Productivity Gestures | `prefs:root=com.apple.MultitaskingAndGesturesSettings&path=Productivity#ProductivityGestures` | 18.7 | F18 |  |

### Music

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 音樂 | Music | `prefs:root=MUSIC` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | Music → Dolby Atmos | `prefs:root=MUSIC&path=com.apple.Music%3AAtmos` | — | FIFI WDG |  |
| — | Music → Audio Quality | `prefs:root=MUSIC&path=com.apple.Music%3AAudioQuality` | — | FIFI WDG |  |
| 音樂 → 行動數據 | Music → Cellular Data | `prefs:root=MUSIC&path=com.apple.Music%3ACellularData` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 音樂 → 等化器 | Music → EQ | `prefs:root=MUSIC&path=com.apple.Music%3AEQ` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 音樂 → 已下載的音樂 | Music → Downloaded Music | `prefs:root=MUSIC&path=com.apple.Music%3AMusicUsageLink` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 最佳化儲存空間 | Music → Optimize Storage | `prefs:root=MUSIC&path=com.apple.Music%3AOptimizeStorage` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | Music → Volume Limit | `prefs:root=MUSIC&path=com.apple.Music%3AVolumeLimit` | — | FIFI WDG |  |
| — | Music → Cellular Data | `prefs:root=MUSIC&path=com.apple.Music:CellularData` | — | MEHDI MS |  |
| — | Music → EQ | `prefs:root=MUSIC&path=com.apple.Music:EQ` | — | MEHDI MS MR | 也見於 `App-Prefs:` |
| — | Music → Optimize Storage | `prefs:root=MUSIC&path=com.apple.Music:OptimizeStorage` | — | MEHDI MS |  |
| — | Music → Volume Limit | `prefs:root=MUSIC&path=com.apple.Music:VolumeLimit` | — | MEHDI MS MR | 也見於 `App-Prefs:` |
| — | iTunes Equalizer | `prefs:root=MUSIC&path=EQ` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | iTunes Volume | `prefs:root=MUSIC&path=VolumeLimit` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |
| 音樂 → 加入播放列表歌曲 | Music → Add Playlist Songs | `prefs:root=MUSIC#com.apple.Music%3AAddPlaylistSongsToMyMusicSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 顯示Apple Music | Music → Show Apple Music | `prefs:root=MUSIC#com.apple.Music%3AAppleMusicEnabled` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 同步資料庫 | Music → Sync Library | `prefs:root=MUSIC#com.apple.Music%3ACloudMusicLibraryEnabled` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 自動下載 | Music → Automatic Downloads | `prefs:root=MUSIC#com.apple.Music%3AMusicAutomaticDownload` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 使用聆聽記錄 | Music → Use Listening History | `prefs:root=MUSIC#com.apple.Music%3APrivateListening` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 顯示星星評分 | Music → Show Star Ratings | `prefs:root=MUSIC#com.apple.Music%3AShowStarRatings` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 音樂 → 音量平衡 | Music → Sound Check | `prefs:root=MUSIC#com.apple.Music%3ASoundCheck` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### News

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| News | News | `prefs:root=NEWS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS |  |
| News → 版權宣告 | News → Acknowledgements | `prefs:root=NEWS&path=Acknowledgements` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | — | `prefs:root=NEWS&path=NOTIFICATIONS` | — | MAN DYLD |  |
| News → 隱私權 | News → Privacy | `prefs:root=NEWS#Privacy` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| News → 重置識別碼 | News → Reset Identifier | `prefs:root=NEWS#reset_identifier` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| News → 顯示報導預覽 | News → Show Story Previews | `prefs:root=NEWS#show_excerpt_mode` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| News → 限制Today中的報導 | News → Restrict Stories in Today | `prefs:root=NEWS#showStoriesFromFavoritesSpecifierID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Nike iPod

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Nike iPod | `prefs:root=NIKE_PLUS_IPOD` | — | DEAN TZ | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |

### Notes

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 備忘錄 | Notes | `prefs:root=NOTES` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 備忘錄 → 從鎖定畫面取用備忘錄 | Notes → Access Notes from Lock Screen | `prefs:root=NOTES&path=Access%20Notes%20from%20Lock%20Screen` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 備忘錄 → 預設帳號 | Notes → Default Account | `prefs:root=NOTES&path=Default%20Account` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 備忘錄 → 橫線與格線 | Notes → Lines & Grids | `prefs:root=NOTES&path=Lines%20%26%20Grids` | 18.7 · 26.2 | F26 F18 FIFI MEHDI WDG MS |  |
| 備忘錄 → 橫線與格線 | Notes → Lines & Grids | `prefs:root=NOTES&path=Lines%20&%20Grids` | 16.2 | F16 MAN |  |
| 備忘錄 → 新備忘錄開頭格式 | Notes → New Notes Start With | `prefs:root=NOTES&path=New%20Notes%20Start%20With` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Notes → Note Backgrounds | `prefs:root=NOTES&path=Note%20Backgrounds` | — | FIFI WDG |  |
| 備忘錄 → 密碼 | Notes → Password | `prefs:root=NOTES&path=Password` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Notes → Siri & Search | `prefs:root=NOTES&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| 備忘錄 → 排序已勾選的項目 | Notes → Sort Checked Items | `prefs:root=NOTES&path=Sort%20Checked%20Items` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 備忘錄 → 備忘錄排序方式 | Notes → Sort Notes By | `prefs:root=NOTES&path=Sort%20Notes%20By` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 備忘錄 → 儲存到「照片」 | Notes → Save to Photos | `prefs:root=NOTES#Save%20to%20Photos` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Notifications

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 通知 | Notifications | `prefs:root=NOTIFICATIONS_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | Notifications → App Name | `prefs:root=NOTIFICATIONS_ID&path=App%20Bundle%20ID` | — | FIFI WDG |  |
| — | — | `prefs:root=NOTIFICATIONS_ID&path=com.apple.Home` | — | MAN DYLD |  |
| 通知 → 摘要排程 | Notifications → Scheduled Summary | `prefs:root=NOTIFICATIONS_ID&path=SCHEDULED_DELIVERY_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 |  |
| — | Notifications → Show Previews | `prefs:root=NOTIFICATIONS_ID&path=SHOW_PREVIEW_GROUP_ID` | — | FIFI |  |
| — | Notifications → Siri Suggestions | `prefs:root=NOTIFICATIONS_ID&path=Siri%20Suggestions` | — | FIFI MEHDI WDG MS |  |

### OnsiteProfileInstall

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=OnsiteProfileInstall&path=OnsiteProfileInstall` | — | MAN DYLD |  |

### Passcode

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=Passcode` | — | MAN DYLD |  |

### Passwords

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 密碼 | Passwords | `prefs:root=PASSWORDS` | 16.2 | F16 FIFI MAN WDG MS |  |
| 密碼 → 自動填寫密碼 | Passwords → AutoFill Passwords | `prefs:root=PASSWORDS#PASSWORD_AUTOFILL_SWITCH` | 16.2 | F16 MAN |  |

### Passwords & Accounts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Passwords & Accounts → (root) | `prefs:root=ACCOUNTS_AND_PASSWORDS` | — | FIFI MEHDI WDG |  |
| — | Mail → Accounts | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ACCOUNTS` | — | MS |  |
| — | Passwords & Accounts → Add Account → (root) | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT` | — | FIFI MAN DYLD MEHDI WDG MS |  |
| — | Passwords & Accounts → Fetch New Data | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=FETCH_NEW_DATA` | — | FIFI MEHDI WDG MS |  |
| — | Passwords & Accounts → Add Account → AOL | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/AOL` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Google | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/Gmail` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → iCloud | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/iCloud` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Other → (root) | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/OTHER` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Outlook | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/Outlook` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Other → Add CalDAV Account | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/OTHER/Add%20CalDAV%20Account` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Other → Add CardDAV Account | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/OTHER/Add%20CardDAV%20Account` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Other → Add LDAP Account | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/OTHER/Add%20LDAP%20Account` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Other → Add Mail Account | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/OTHER/Add%20Mail%20Account` | — | FIFI WDG |  |
| — | Passwords & Accounts → Add Account → Other → Add Subscribed Calendar | `prefs:root=ACCOUNTS_AND_PASSWORDS&path=ADD_ACCOUNT/OTHER/Add%20Subscribed%20Calendar` | — | FIFI WDG |  |

### Pearl

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=Pearl` | — | MAN DYLD |  |

### Personal Hotspot

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Personal Hotspot → (root) | `prefs:root=INTERNET_TETHERING` | — | FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | Personal Hotspot → Family Sharing → (root) | `prefs:root=INTERNET_TETHERING&path=Family%20Sharing` | — | FIFI MEHDI WDG MS |  |
| — | Personal Hotspot → Wi-Fi Password | `prefs:root=INTERNET_TETHERING&path=Wi-Fi%20Password` | — | FIFI MEHDI WDG MS |  |

### Phone

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 電話 | Phone | `prefs:root=Phone` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=PHONE` | — | MAN DYLD |  |
| 電話 → 播報來電者 | Phone → Announce Calls | `prefs:root=Phone&path=ANNOUNCE_CALLS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 來電轉接 | Phone → Call Forwarding | `prefs:root=Phone&path=Call%20Forwarding` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 來電等候 | Phone → Call Waiting | `prefs:root=Phone&path=Call%20Waiting` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | — | `prefs:root=Phone&path=CallerID` | — | MR | 舊版、也見於 `App-Prefs:` |
| 電話 → SMS/來電回報 | Phone → SMS/Call Reporting | `prefs:root=Phone&path=CLASSIFICATION_AND_REPORTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | — | `prefs:root=Phone&path=com.apple.settings.WiFiCallingSettingsBundle` | — | MAN DYLD |  |
| 電話 → 撥號輔助 | Phone → Dial Assist | `prefs:root=Phone&path=Dial%20Assist` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 撥入電話 | Phone → Incoming Calls | `prefs:root=Phone&path=INCOMING_CALL_STYLE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 本機號碼 | Phone → My Number | `prefs:root=Phone&path=My%20Number` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | — | `prefs:root=Phone&path=MY_NUMBER` | — | MAN DYLD |  |
| 電話 → 用訊息回覆 | Phone → Respond with Text | `prefs:root=Phone&path=Respond%20with%20Text` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 電話 → 顯示發話號碼 | Phone → Show My Caller ID | `prefs:root=Phone&path=Show%20My%20Caller%20ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| — | Phone → Silence Unknown Callers | `prefs:root=Phone&path=SILENCE_CALLS` | — | FIFI WDG |  |
| — | — | `prefs:root=Phone&path=SIM%20PIN` | — | MR | 舊版、也見於 `App-Prefs:` |
| 電話 → 封鎖的聯絡人 | Phone → Blocked Contacts | `prefs:root=Phone&path=SPECIFIER_IDENTIFIER_BLACKLIST` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 將未知的來電設為靜音 | Phone → Silence Unknown Callers | `prefs:root=Phone#SILENCE_CALLS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 來電轉接 → 來電轉接 | Phone → Call Forwarding → Call Forwarding | `prefs:root=Phone&path=Call%20Forwarding#idMasterOnOffSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 電話 → 顯示發話號碼 → 顯示發話號碼 | Phone → Show My Caller ID → Show My Caller ID | `prefs:root=Phone&path=Show%20My%20Caller%20ID/Primary` | 18.7 · 26.2 | F26 F18 MAN |  |
| 電話 → 顯示發話號碼 → 顯示發話號碼 → 顯示發話號碼 | Phone → Show My Caller ID → Show My Caller ID → Show My Caller ID | `prefs:root=Phone&path=Show%20My%20Caller%20ID/Primary#Show%20My%20Caller%20ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Photos

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 照片 | Photos | `prefs:root=Photos` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 照片 → 行動數據 | Photos → Cellular Data | `prefs:root=Photos&path=CellularDataLinkList` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 照片 → 下載並保留原始檔 | Photos → Download and Keep Originals | `prefs:root=Photos#iCloudKeepOriginalsOption` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → 最佳化儲存空間 | Photos → Optimize Storage | `prefs:root=Photos#iCloudOptimizeStorageOption` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → iCloud照片 | Photos → iCloud Photos | `prefs:root=Photos#iCloudPhotosSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → 檢視完整HDR | Photos → View Full HDR | `prefs:root=Photos#ImageModulationSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → 顯示節日 | Photos → Show Holiday Events | `prefs:root=Photos#MEMORIES_HOLIDAY_CALENDAR_EVENTS_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → 我的照片串流 | Photos → My Photo Stream | `prefs:root=Photos#PhotoStreamSwitch` | 16.2 | F16 MAN |  |
| 照片 → 共享的相簿 | Photos → Shared Albums | `prefs:root=Photos#SharedStreamsSwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → 傳到Mac或PC | Photos → Transfer to Mac or PC | `prefs:root=Photos#TransferGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 照片 → 自動播放影片 | Photos → Autoplay Videos | `prefs:root=Photos#VideoAutoplaySwitch` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Podcasts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Podcasts | `prefs:root=com.apple.podcasts` | — | FIFI WDG |  |
| Podcast | Podcasts | `prefs:root=PODCASTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |

### Privacy & Security

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 隱私權與安全性 | Privacy & Security | `prefs:root=Privacy` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| 隱私權與安全性 → 廣告 | Privacy & Security → Advertising | `prefs:root=Privacy&path=ADVERTISING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG MS |  |
| 隱私權與安全性 → 藍牙分享 | Privacy & Security → Bluetooth Sharing | `prefs:root=Privacy&path=BT_PERIPHERAL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 隱私權與安全性 → 行事曆 | Privacy & Security → Calendars | `prefs:root=Privacy&path=CALENDARS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 隱私權與安全性 → 相機 | Privacy & Security → Camera | `prefs:root=Privacy&path=CAMERA` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 隱私權與安全性 → 聯絡人 | Privacy & Security → Contacts | `prefs:root=Privacy&path=CONTACTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 隱私權與安全性 → 檔案和檔案夾 | Privacy & Security → Files and Folders | `prefs:root=Privacy&path=FILEACCESS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 隱私權與安全性 → 健康 | Privacy & Security → Health | `prefs:root=Privacy&path=HEALTH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 隱私權與安全性 → 健康資料 | Privacy & Security → Health Data | `prefs:root=Privacy&path=HEALTH_DATA` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | Privacy → Local Network | `prefs:root=Privacy&path=LOCAL_NETWORK` | — | FIFI WDG |  |
| 隱私權與安全性 → 定位服務 | Privacy & Security → Location | `prefs:root=Privacy&path=LOCATION` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| 隱私權與安全性 → 媒體與Apple Music | Privacy & Security → Media & Apple Music | `prefs:root=Privacy&path=MEDIALIBRARY` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 隱私權與安全性 → 麥克風 | Privacy & Security → Microphone | `prefs:root=Privacy&path=MICROPHONE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Privacy → Motion & Fitness | `prefs:root=Privacy&path=MOTION` | — | FIFI MEHDI WDG MS |  |
| 隱私權與安全性 → 照片 | Privacy & Security → Photos | `prefs:root=Privacy&path=PHOTOS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 隱私權與安全性 → App隱私權報告 | Privacy & Security → App Privacy Report | `prefs:root=Privacy&path=PRIVACY_REPORT` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI WDG |  |
| 隱私權與安全性 → 分析 | Privacy & Security → Analytics | `prefs:root=Privacy&path=PROBLEM_REPORTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD WDG MS |  |
| 隱私權與安全性 → 提醒事項 | Privacy & Security → Reminders | `prefs:root=Privacy&path=REMINDERS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 隱私權與安全性 → 安全檢查 | Privacy & Security → Safety Check | `prefs:root=Privacy&path=SAFETY_CHECK` | 16.2 | F16 |  |
| 隱私權與安全性 → 語音辨識 | Privacy & Security → Speech Recognition | `prefs:root=Privacy&path=SPEECH_RECOGNITION` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 隱私權與安全性 → 追蹤 | Privacy & Security → Tracking | `prefs:root=Privacy&path=USER_TRACKING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 隱私權與安全性 → HomeKit | Privacy & Security → HomeKit | `prefs:root=Privacy&path=WILLOW` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 隱私權與安全性 → 封閉模式 | Privacy & Security → Lockdown Mode | `prefs:root=Privacy#LOCKDOWN_MODE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 WDG |  |
| 隱私權與安全性 → 敏感性內容 | Privacy & Security → Sensitive Content | `prefs:root=Privacy#NUDITY_DETECTION` | 18.7 · 26.2 | F26 F18 WDG |  |
| — | — | `prefs:root=Privacy&path=HEALTH/HEADPHONE_AUDIO_LEVELS` | — | MAN DYLD |  |
| — | — | `prefs:root=Privacy&path=LOCATION/com.apple.Health` | — | MAN DYLD |  |
| 隱私權與安全性 → 定位服務 → 分享我的位置 | Privacy & Security → Location → Share My Location | `prefs:root=Privacy&path=LOCATION/LOCATION_SHARING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | Privacy → Location Services → System Services | `prefs:root=Privacy&path=LOCATION/SYSTEM_SERVICES` | — | FIFI MAN DYLD WDG |  |
| — | — | `prefs:root=Privacy&path=PROBLEM_REPORTING/SHARE_HEALTH_RECORDS_DATA` | — | MAN DYLD |  |

### Reminders

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 提醒事項 | Reminders | `prefs:root=REMINDERS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS MR | 也見於 `App-Prefs:` |
| 提醒事項 → 預設列表 | Reminders → Default List | `prefs:root=REMINDERS&path=DEFAULT_LIST` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| — | Reminders → Siri & Search | `prefs:root=REMINDERS&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| 提醒事項 → 顯示為已過期 | Reminders → Show as Overdue | `prefs:root=REMINDERS#showRemindersAsOverdue` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 提醒事項 → 今天通知 | Reminders → Today Notification | `prefs:root=REMINDERS#todayNotificationFireTime` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |
| 提醒事項 → 預設列表 → 提醒事項 | Reminders → Default List → Reminders | `prefs:root=REMINDERS&path=DEFAULT_LIST#preferredDefaultListID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### Safari

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Safari | Safari | `prefs:root=SAFARI` | 16.2 | F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| — | — | `prefs:root=Safari` | — | TZ | 舊版、也見於 `app-settings:` |
| — | Safari → Advanced | `prefs:root=SAFARI&path=ADVANCED` | — | FIFI WDG MS |  |
| Safari → 自動填寫 | Safari → AutoFill | `prefs:root=SAFARI&path=AUTO_FILL` | 16.2 | F16 FIFI MAN WDG |  |
| — | Safari → Camera | `prefs:root=SAFARI&path=Camera` | — | FIFI MEHDI WDG MS |  |
| — | Safari → Clear History and Website Data | `prefs:root=SAFARI&path=CLEAR_HISTORY_AND_DATA` | — | FIFI WDG MS |  |
| — | Safari → Close Tabs | `prefs:root=SAFARI&path=Close%20Tabs` | — | FIFI MEHDI WDG MS |  |
| — | Safari → Content Blockers | `prefs:root=SAFARI&path=Content%20Blockers` | — | MEHDI MS |  |
| — | Safari → Content Blockers | `prefs:root=SAFARI&path=CONTENT_BLOCKERS` | — | FIFI WDG |  |
| Safari → 下載項目 | Safari → Downloads | `prefs:root=SAFARI&path=DOWNLOADS` | 16.2 | F16 FIFI MAN MEHDI WDG MS |  |
| — | Safari → Hide IP Address | `prefs:root=SAFARI&path=Hide%20IP%20Address` | — | FIFI WDG |  |
| — | Safari → Location | `prefs:root=SAFARI&path=Location` | — | FIFI MEHDI WDG MS |  |
| — | Safari → Microphone | `prefs:root=SAFARI&path=Microphone` | — | FIFI MEHDI WDG MS |  |
| — | Safari → Page Zoom | `prefs:root=SAFARI&path=Page%20Zoom` | — | FIFI MEHDI WDG MS |  |
| — | Passwords | `prefs:root=SAFARI&path=Passwords` | — | DEAN | 舊版、也見於 `App-Prefs:` |
| — | Safari → Reader | `prefs:root=SAFARI&path=Reader` | — | FIFI MEHDI WDG MS |  |
| — | Safari → Request Desktop Website | `prefs:root=SAFARI&path=Request%20Desktop%20Website` | — | FIFI MEHDI WDG MS |  |
| Safari → 內容阻擋器 | Safari → Content Blocker | `prefs:root=SAFARI&path=WEB_EXTENSIONS` | 16.2 | F16 |  |
| Safari → 阻擋彈出式視窗 | Safari → Block Pop-ups | `prefs:root=SAFARI#BLOCK_POPUPS` | 16.2 | F16 |  |
| Safari → 防止跨網站追蹤 | Safari → Prevent Cross-Site Tracking | `prefs:root=SAFARI#TRACKER_PROTECTION` | 16.2 | F16 MAN |  |
| — | Safari → AutoFill → Saved Credit Cards | `prefs:root=SAFARI&path=AUTO_FILL/CreditCardList` | — | FIFI |  |

### Screen Time

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 螢幕使用時間 | Screen Time | `prefs:root=SCREEN_TIME` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS |  |
| 螢幕使用時間 → 永遠允許 | Screen Time → Always Allowed | `prefs:root=SCREEN_TIME&path=ALWAYS_ALLOWED` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG MS |  |
| 螢幕使用時間 → App限制 | Screen Time → App Limits | `prefs:root=SCREEN_TIME&path=APP_LIMITS` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG MS |  |
| 螢幕使用時間 → 通訊限制 | Screen Time → Communication Limits | `prefs:root=SCREEN_TIME&path=COMMUNICATION_LIMITS` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| 螢幕使用時間 → 通訊安全 | Screen Time → Communication Safety | `prefs:root=SCREEN_TIME&path=COMMUNICATION_SAFETY` | 16.2 · 18.7 | F18 F16 |  |
| 螢幕使用時間 → 內容與隱私權限制 | Screen Time → Content & Privacy Restrictions | `prefs:root=SCREEN_TIME&path=CONTENT_PRIVACY` | 16.2 · 18.7 | F18 F16 FIFI MAN DYLD MEHDI WDG |  |
| — | — | `prefs:root=SCREEN_TIME&path=ContentAndPrivacy` | — | MAN DYLD |  |
| 螢幕使用時間 → 停用時間 | Screen Time → Downtime | `prefs:root=SCREEN_TIME&path=DOWNTIME` | 16.2 · 18.7 | F18 F16 FIFI MAN MEHDI WDG MS |  |
| 螢幕使用時間 → 螢幕距離 | Screen Time → Screen Distance | `prefs:root=SCREEN_TIME&path=EYE_DISTANCE` | 18.7 | F18 FIFI |  |
| 螢幕使用時間 → See All App & Website Activity | Screen Time → See All App & Website Activity | `prefs:root=SCREEN_TIME&path=SCREEN_TIME_SUMMARY` | 16.2 · 18.7 | F18 F16 FIFI MAN WDG |  |
| — | Screen Time → Turn On Screen Time | `prefs:root=SCREEN_TIME&path=Turn%20On%20Screen%20Time` | — | FIFI WDG |  |
| 螢幕使用時間 → 分級保護控制 | Screen Time → Parental Controls | `prefs:root=SCREEN_TIME#FAMILY` | 16.2 · 18.7 | F18 F16 MAN |  |
| 螢幕使用時間 → See All App & Website Activity → 今天 | Screen Time → See All App & Website Activity → Today | `prefs:root=SCREEN_TIME&path=SCREEN_TIME_SUMMARY#DAY` | 16.2 · 18.7 | F18 F16 MAN |  |
| 螢幕使用時間 → See All App & Website Activity → 週 | Screen Time → See All App & Website Activity → Week | `prefs:root=SCREEN_TIME&path=SCREEN_TIME_SUMMARY#WEEK` | 16.2 · 18.7 | F18 F16 MAN |  |

### Shortcuts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 捷徑 | Shortcuts | `prefs:root=SHORTCUTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS |  |
| 捷徑 → 法律聲明 | Shortcuts → Legal Notices | `prefs:root=SHORTCUTS&path=Legal%20Notices` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 捷徑 → iCloud同步 | Shortcuts → iCloud Sync | `prefs:root=SHORTCUTS#WFCloudKitSyncEnabled` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 捷徑 → 同步捷徑順序 | Shortcuts → Sync Shortcut Order | `prefs:root=SHORTCUTS#WFCloudKitSyncOrderEnabled` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |

### Siri

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Siri | Siri | `prefs:root=SIRI` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| — | Siri → Siri & Dictation History | `prefs:root=SIRI&path=HISTORY` | — | FIFI WDG |  |
| Siri → 語言 | Siri → Language | `prefs:root=SIRI&path=LANGUAGE_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| Siri → 我的資訊 | Siri → My Information | `prefs:root=SIRI&path=MY_INFO` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| Siri → 語音回饋 | Siri → Voice Feedback | `prefs:root=SIRI&path=VOICE_FEEDBACK_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| Siri → Siri聲音 | Siri → Siri Voice | `prefs:root=SIRI&path=VOICE_ID` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| Siri → 鎖定時允許Siri | Siri → Allow Siri When Locked | `prefs:root=SIRI#ASSISTANT_LOCK_SCREEN_ACCESS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| Siri與搜尋 → 查詢字詞時建議 | Siri & Search → Suggestions in Look Up | `prefs:root=SIRI#Suggestions%20in%20Look%20Up` | 16.2 | F16 MAN MEHDI |  |
| Siri與搜尋 → 搜尋時建議 | Siri & Search → Suggestions in Search | `prefs:root=SIRI#Suggestions%20in%20Search` | 16.2 | F16 MAN MEHDI |  |
| — | Siri & Search → Suggestions on Home Screen | `prefs:root=SIRI#Suggestions%20on%20Home%20Screen` | — | MEHDI |  |
| Siri與搜尋 → 鎖定畫面上建議 | Siri & Search → Suggestions on Lock Screen | `prefs:root=SIRI#Suggestions%20on%20Lock%20Screen` | 16.2 | F16 MAN MEHDI |  |
| — | Siri & Search → Suggestions when Sharing | `prefs:root=SIRI#Suggestions%20when%20Sharing` | — | MEHDI |  |
| — | Siri & Search → Suggestions while Searching | `prefs:root=SIRI#Suggestions%20while%20Searching` | — | MEHDI |  |

### Sounds & Haptics

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 聲音 \| 音效與觸覺回饋 | Sounds \| Sounds & Haptics | `prefs:root=Sounds` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 聲音 → AirDrop | Sounds → AirDrop | `prefs:root=Sounds&path=AIRDROP` | 16.2 | F16 FIFI MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 行事曆提示 | Sounds \| Sounds & Haptics → Calendar Alerts | `prefs:root=Sounds&path=Calendar%20Alarm` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| — | Sounds → Haptics | `prefs:root=Sounds&path=HAPTICS` | — | FIFI |  |
| 聲音 \| 音效與觸覺回饋 → 耳機安全性 | Sounds \| Sounds & Haptics → Headphone Safety | `prefs:root=Sounds&path=HEADPHONE_LEVEL_LIMIT_SETTING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN DYLD MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 新增郵件 | Sounds \| Sounds & Haptics → New Mail | `prefs:root=Sounds&path=NEW_MAIL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 個人化空間音訊 | Sounds \| Sounds & Haptics → Personalized Spatial Audio | `prefs:root=Sounds&path=Personalized%20Spatial%20Audio` | 18.7 · 26.2 | F26 F18 |  |
| 聲音 \| 音效與觸覺回饋 → 提醒事項提示 | Sounds \| Sounds & Haptics → Reminder Alerts | `prefs:root=Sounds&path=Reminder%20Alerts` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| — | iOS Settings URL's → Personalized Spatial Audio | `prefs:root=Sounds&path=Reminder&path=Personalized%20Spatial%20Audio` | — | WDG |  |
| 聲音 \| 音效與觸覺回饋 → 鈴聲 | Sounds \| Sounds & Haptics → Ringtone | `prefs:root=Sounds&path=Ringtone` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| 聲音 \| 音效與觸覺回饋 → 已傳送郵件 | Sounds \| Sounds & Haptics → Sent Mail | `prefs:root=Sounds&path=SENT_MAIL` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 音效 | Sounds \| Sounds & Haptics → Sound Effects | `prefs:root=Sounds&path=SOUND_EFFECTS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 訊息聲 | Sounds \| Sounds & Haptics → Text Tone | `prefs:root=Sounds&path=Text_Messages` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 收到新留言 | Sounds \| Sounds & Haptics → New Voicemail | `prefs:root=Sounds&path=Voicemail` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 使用按鈕更改音量 | Sounds \| Sounds & Haptics → Change with Buttons | `prefs:root=Sounds#CHANGE_WITH_BUTTONS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 按鍵聲 | Sounds \| Sounds & Haptics → Keyboard Clicks | `prefs:root=Sounds#KEYBOARD_SOUND_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 鎖定聲 | Sounds \| Sounds & Haptics → Lock Sound | `prefs:root=Sounds#LOCK_SOUND_SWITCH` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 鈴聲和提示聲 | Sounds \| Sounds & Haptics → Ringer and Alerts | `prefs:root=Sounds#RINGER_AND_ALERT_GROUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 聲音和震動模式 | Sounds \| Sounds & Haptics → Sounds and Vibration Patterns | `prefs:root=Sounds#SOUNDS_ALERT_GROUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 耳機安全性 → 降低高音量 | Sounds \| Sounds & Haptics → Headphone Safety → Reduce Loud Audio | `prefs:root=Sounds&path=HEADPHONE_LEVEL_LIMIT_SETTING#SHSHeadphoneLevelLimitSwitchKey` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 耳機安全性 → 耳機通知 | Sounds \| Sounds & Haptics → Headphone Safety → Headphone Notifications | `prefs:root=Sounds&path=HEADPHONE_LEVEL_LIMIT_SETTING#SHSHeadphoneWeeklyNotificationsKey` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 聲音 \| 音效與觸覺回饋 → 耳機安全性 → Lightning轉接器 | Sounds \| Sounds & Haptics → Headphone Safety → Lightning Adapters | `prefs:root=Sounds&path=HEADPHONE_LEVEL_LIMIT_SETTING/HEADPHONE_LIGHTNING_ADAPTERS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |

### StandBy

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 待機模式 | StandBy | `prefs:root=AMBIENT` | 18.7 | F18 FIFI |  |

### Stocks

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 股市 | Stocks | `prefs:root=STOCKS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 股市 → 隱私權 | Stocks → Privacy | `prefs:root=STOCKS#Privacy` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| 股市 → 重置識別碼 | Stocks → Reset Identifier | `prefs:root=STOCKS#reset_identifier` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |

### TOUCHID_PASSCODE

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=TOUCHID_PASSCODE` | — | MR | 舊版、也見於 `App-Prefs:` |
| — | — | `prefs:root=TOUCHID_PASSCODE&path=TOUCHID_PASSCODE` | — | MAN DYLD |  |
| — | — | `prefs:root=TOUCHID_PASSCODE&path=TOUCHID_PASSCODE#HOME_CONTROL_SWITCH` | — | MAN DYLD |  |

### Translate

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 翻譯 | Translate | `prefs:root=TRANSLATE` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 翻譯 → 裝置端模式 | Translate → On-Device Mode | `prefs:root=TRANSLATE#OnDeviceOnly` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### TV

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| TV \| 影片 | TV \| Videos | `prefs:root=TVAPP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| TV \| 影片 → 購買和租借項目 | TV \| Videos → Purchases and Rentals | `prefs:root=TVAPP&path=com.apple.videos%3APreferredPurchaseResolution` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG |  |
| — | TV → Cellular | `prefs:root=TVAPP&path=com.apple.videos%3AVideosPlaybackQualityCellularSetting` | — | FIFI WDG |  |
| — | TV → Wi-Fi | `prefs:root=TVAPP&path=com.apple.videos%3AVideosPlaybackQualitySetting` | — | FIFI WDG |  |
| — | TV → Siri & Search | `prefs:root=TVAPP&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| TV \| 影片 → 家庭共享 | TV \| Videos → Home Sharing | `prefs:root=TVAPP#com.apple.videos%3AHomeSharingFooter` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| TV \| 影片 → 播放品質 | TV \| Videos → Playback Quality | `prefs:root=TVAPP#com.apple.videos%3APlaybackQualityGroup` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |
| TV \| 影片 → 使用行動數據來播放 | TV \| Videos → Use Cellular Data for Playback | `prefs:root=TVAPP#com.apple.videos%3AVideosUseCellularDataEnabledSetting` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN MEHDI WDG |  |

### TV Provider

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 電視業者 | TV Provider | `prefs:root=VIDEO_SUBSCRIBER` | 16.2 | F16 FIFI MAN MEHDI WDG |  |

### Twitter

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Twitter | `prefs:root=TWITTER` | — | DEAN TZ MR | 舊版、也見於 `app-settings:`、也見於 `App-Prefs:` |

### Video

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | Video | `prefs:root=VIDEO` | — | MAN DYLD DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |

### VIMEO

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=VIMEO` | — | MR | 舊版、也見於 `App-Prefs:` |

### Voice Memos

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 語音備忘錄 | Voice Memos | `prefs:root=VOICE_MEMOS` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS |  |
| 語音備忘錄 → 音訊品質 | Voice Memos → Audio Quality | `prefs:root=VOICE_MEMOS&path=RCVoiceMemosAudioQualityKey` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| 語音備忘錄 → 清除已刪除的項目 | Voice Memos → Clear Deleted | `prefs:root=VOICE_MEMOS&path=RCVoiceMemosRecentlyDeletedWindowKey` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN WDG |  |
| — | Voice Memos → Siri & Search | `prefs:root=VOICE_MEMOS&path=SIRI_AND_SEARCH` | — | FIFI WDG |  |
| 語音備忘錄 → 基於位置命名 | Voice Memos → Location-based Naming | `prefs:root=VOICE_MEMOS#RCVoiceMemosUseLocationBasedNaming` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN WDG |  |

### VPN

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | VPN → (root) | `prefs:root=VPN` | — | FIFI WDG DEAN | 也見於 `App-Prefs:` |
| — | VPN → Add VPN Configuration… | `prefs:root=VPN&path=Add%20VPN%20Configuration%E2%80%A6` | — | FIFI WDG |  |

### Wallet & Apple Pay

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 錢包與Apple Pay | Wallet & Apple Pay | `prefs:root=PASSBOOK` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN MR | 也見於 `App-Prefs:` |
| — | — | `prefs:root=PASSBOOK&path=` | — | MAN DYLD |  |
| — | Wallet → Add Card | `prefs:root=PASSBOOK&path=Add%20Card` | — | FIFI WDG |  |
| 錢包與Apple Pay → 加入卡片 | Wallet & Apple Pay → Add Card | `prefs:root=PASSBOOK#Add%20Card` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 錢包與Apple Pay → Apple Cash | Wallet & Apple Pay → Apple Cash | `prefs:root=PASSBOOK#Apple%C2%A0Cash` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 錢包與Apple Pay → 按兩下側邊按鈕 | Wallet & Apple Pay → Double-Click Side Button | `prefs:root=PASSBOOK#Double-Click%20Side%20Button` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |
| 錢包與Apple Pay → 訂單追蹤 | Wallet & Apple Pay → Order Tracking | `prefs:root=PASSBOOK#ORDER_TRACKING` | 16.2 · 18.7 · 26.2 | F26 F18 F16 |  |
| 錢包與Apple Pay → 付款卡 | Wallet & Apple Pay → Payment Cards | `prefs:root=PASSBOOK#SETTINGS_PAYMENT_CARDS_GROUP` | 16.2 · 18.7 · 26.2 | F26 F18 F16 MAN |  |

### Wallpaper

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 背景圖片 | Wallpaper | `prefs:root=Wallpaper` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |

### Weather

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 天氣 | Weather | `prefs:root=WEATHER` | 16.2 · 18.7 · 26.2 | F26 F18 F16 |  |

### WEIBO

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `prefs:root=WEIBO` | — | MR | 舊版、也見於 `App-Prefs:` |

### Wi-Fi

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| WLAN \| Wi-Fi | WLAN \| Wi-Fi | `prefs:root=WIFI` | 16.2 · 18.7 · 26.2 | F26 F18 F16 FIFI MAN DYLD MEHDI WDG MS DEAN TZ MR | 也見於 `app-settings:`、也見於 `App-Prefs:` |
| — | — | `prefs:root=WIFI&path=` | — | MAN DYLD |  |
| — | — | `prefs:root=WIFI&path=Credentials` | — | MAN DYLD |  |
| — | — | `prefs:root=WIFI&path=WIRELESS_APP_DATA_USAGE_ID` | — | MAN DYLD |  |

### settings-navigation:

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Apple帳號 | Apple Account | `settings-navigation://com.apple.Settings.AppleAccount` | 18.7 · 26.2 | F26 F18 |  |
| — | Apps | `settings-navigation://com.apple.Settings.Apps` | — | MAN |  |
| — | iOS Settings URL's → Home | `settings-navigation://com.apple.Settings.HomeKit` | — | WDG |  |
| 隱私權與安全性 | Privacy & Security | `settings-navigation://com.apple.Settings.PrivacyAndSecurity` | 18.7 · 26.2 | F26 F18 |  |
| — | iOS Settings URL's → SEARCH | `settings-navigation://com.apple.Settings.Search` | — | WDG |  |
| — | iOS Settings URL's → TV Provider | `settings-navigation://com.apple.Settings.TVProvider` | — | WDG |  |
| Apple帳號 → 姓名、電話號碼、電子郵件 | Apple Account → Name, Phone Numbers, Email | `settings-navigation://com.apple.Settings.AppleAccount/APPLE_ACCOUNT_CONTACT` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 家人共享 | Apple Account → Family | `settings-navigation://com.apple.Settings.AppleAccount/Family` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud | Apple Account → iCloud | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 分享我的位置 | Apple Account → Share My Location | `settings-navigation://com.apple.Settings.AppleAccount/LOCATION_SHARING` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 密碼與安全性 | Apple Account → Password & Security | `settings-navigation://com.apple.Settings.AppleAccount/PASSWORD_AND_SECURITY` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 付款與寄送 | Apple Account → Payment & Shipping | `settings-navigation://com.apple.Settings.AppleAccount/PAYMENT_AND_SHIPPING` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 訂閱項目 | Apple Account → Subscriptions | `settings-navigation://com.apple.Settings.AppleAccount/SUBSCRIPTIONS` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 聯絡人密鑰驗證 | Apple Account → Contact Key Verification | `settings-navigation://com.apple.Settings.AppleAccount/TRANSPARENCY` | 18.7 · 26.2 | F26 F18 |  |
| 測距儀 | Measure | `settings-navigation://com.apple.Settings.Apps/com.apple.measure` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 | Notes | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 廣告 | Privacy & Security → Advertising | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/ADVERTISING` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 藍牙分享 | Privacy & Security → Bluetooth Sharing | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/BT_PERIPHERAL` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 行事曆 | Privacy & Security → Calendars | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/CALENDARS` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 相機 | Privacy & Security → Camera | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/CAMERA` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 聯絡人 | Privacy & Security → Contacts | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/CONTACTS` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 檔案和檔案夾 | Privacy & Security → Files and Folders | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/FILEACCESS` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 健康 | Privacy & Security → Health | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/HEALTH` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 健康資料 | Privacy & Security → Health Data | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/HEALTH_DATA` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 定位服務 | Privacy & Security → Location | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/LOCATION` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 媒體與Apple Music | Privacy & Security → Media & Apple Music | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/MEDIALIBRARY` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 麥克風 | Privacy & Security → Microphone | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/MICROPHONE` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 照片 | Privacy & Security → Photos | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/PHOTOS` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → App隱私權報告 | Privacy & Security → App Privacy Report | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/PRIVACY_REPORT` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 分析 | Privacy & Security → Analytics | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/PROBLEM_REPORTING` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 提醒事項 | Privacy & Security → Reminders | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/REMINDERS` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 語音辨識 | Privacy & Security → Speech Recognition | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/SPEECH_RECOGNITION` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 追蹤 | Privacy & Security → Tracking | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/USER_TRACKING` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → HomeKit | Privacy & Security → HomeKit | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/WILLOW` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 備份 | Apple Account → iCloud → Backup | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/BACKUP` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → Safari | Apple Account → iCloud → Safari | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Bookmarks` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 行事曆 | Apple Account → iCloud → Calendar | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Calendars` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 聯絡人 | Apple Account → iCloud → Contacts | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Contacts` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 健康 | Apple Account → iCloud → Health | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Health` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 密碼與鑰匙圈 | Apple Account → iCloud → Passwords and Keychain | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.KeychainSync` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 郵件 | Apple Account → iCloud → Mail | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Mail` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 照片 | Apple Account → iCloud → Photos | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.MediaStream` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 新聞 | Apple Account → iCloud → News | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.News` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 備忘錄 | Apple Account → iCloud → Notes | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Notes` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 提醒事項 | Apple Account → iCloud → Reminders | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Reminders` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → iCloud雲碟 | Apple Account → iCloud → iCloud Drive | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Ubiquity` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 隱藏電子郵件地址 | Apple Account → iCloud → Hide My Email | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/PRIVATE_EMAIL_MANAGE` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → iCloud儲存空間 | Apple Account → iCloud → iCloud Storage | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/STORAGE_AND_BACKUP` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → 分享我的位置 → 尋找 | Apple Account → Share My Location → Find My | `settings-navigation://com.apple.Settings.AppleAccount/LOCATION_SHARING/FindMyDevice-Settings` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 從鎖定畫面取用備忘錄 | Notes → Access Notes from Lock Screen | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/Access%20Notes%20from%20Lock%20Screen` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 預設帳號 | Notes → Default Account | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/Default%20Account` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 橫線與格線 | Notes → Lines & Grids | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/Lines%20%26%20Grids` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 新備忘錄開頭格式 | Notes → New Notes Start With | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/New%20Notes%20Start%20With` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 密碼 | Notes → Password | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/Password` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 排序已勾選的項目 | Notes → Sort Checked Items | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/Sort%20Checked%20Items` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 備忘錄排序方式 | Notes → Sort Notes By | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes/Sort%20Notes%20By` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 封閉模式 | Privacy & Security → Lockdown Mode | `settings-navigation://com.apple.Settings.PrivacyAndSecurity#LOCKDOWN_MODE#LOCKDOWN_MODE` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 敏感性內容 | Privacy & Security → Sensitive Content | `settings-navigation://com.apple.Settings.PrivacyAndSecurity#NUDITY_DETECTION#NUDITY_DETECTION` | 18.7 · 26.2 | F26 F18 |  |
| 隱私權與安全性 → 定位服務 → 分享我的位置 | Privacy & Security → Location → Share My Location | `settings-navigation://com.apple.Settings.PrivacyAndSecurity/LOCATION/LOCATION_SHARING` | 18.7 · 26.2 | F26 F18 |  |
| Apple帳號 → iCloud → 郵件 → 自訂電子郵件網域 | Apple Account → iCloud → Mail → Custom Email Domain | `settings-navigation://com.apple.Settings.AppleAccount/ICLOUD_SERVICE/com.apple.Dataclass.Mail/BYOD_SETTING_SPECIFIER_ID` | 18.7 | F18 |  |
| 測距儀 → 英制 | Measure → Imperial | `settings-navigation://com.apple.Settings.Apps/com.apple.measure#Imperial#Imperial` | 18.7 · 26.2 | F26 F18 |  |
| 測距儀 → 測量單位 | Measure → Measure Units | `settings-navigation://com.apple.Settings.Apps/com.apple.measure#MEASURE_UNITS#MEASURE_UNITS` | 18.7 · 26.2 | F26 F18 |  |
| 測距儀 → 公制 | Measure → Metric | `settings-navigation://com.apple.Settings.Apps/com.apple.measure#Metric#Metric` | 18.7 · 26.2 | F26 F18 |  |
| 備忘錄 → 儲存到「照片」 | Notes → Save to Photos | `settings-navigation://com.apple.Settings.Apps/com.apple.mobilenotes#Save%20to%20Photos#Save%20to%20Photos` | 18.7 · 26.2 | F26 F18 |  |

### watchOS bridge: (Settings root)

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `bridge:` | — | MAN DYLD |  |

### watchOS bridge: Accessibility

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 輔助使用 | Accessibility | `bridge:root=ACCESSIBILITY` | 16.2 · 18.7 | F18W F16W |  |
| 輔助使用 → 輔助使用快速鍵 | Accessibility → Accessibility Shortcut | `bridge:root=ACCESSIBILITY&path=AX_SHORTCUT` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 複雜功能 | Accessibility → Complication | `bridge:root=ACCESSIBILITY&path=HearingDevicesComplicationRowID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 減少動態效果 | Accessibility → Reduce Motion | `bridge:root=ACCESSIBILITY&path=ReduceMotion` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → RTT | Accessibility → RTT | `bridge:root=ACCESSIBILITY&path=RTT` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 側邊按鈕按鍵速度 | Accessibility → Side Button Click Speed | `bridge:root=ACCESSIBILITY&path=SideButton` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 | Accessibility → Chimes | `bridge:root=ACCESSIBILITY&path=TapticChimesCell` | 16.2 · 18.7 | F18W F16W |  |
| 輔助使用 → 觸控調節 | Accessibility → Touch Accommodations | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 旁白 | Accessibility → VoiceOver | `bridge:root=ACCESSIBILITY&path=VOICEOVER_TITLE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 縮放 | Accessibility → Zoom | `bridge:root=ACCESSIBILITY&path=ZOOM_TITLE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 | Accessibility | `bridge:root=ACCESSIBILITY_ID` | 26.2 | F26W |  |
| 輔助使用 → 輔助使用快速鍵 | Accessibility → Accessibility Shortcut | `bridge:root=ACCESSIBILITY_ID&path=AX_SHORTCUT_ID` | 26.2 | F26W |  |
| 輔助使用 → 複雜功能 | Accessibility → Complication | `bridge:root=ACCESSIBILITY_ID&path=HearingDevicesComplicationRowID` | 26.2 | F26W |  |
| 輔助使用 → 減少動態效果 | Accessibility → Reduce Motion | `bridge:root=ACCESSIBILITY_ID&path=ReduceMotion` | 26.2 | F26W |  |
| 輔助使用 → RTT | Accessibility → RTT | `bridge:root=ACCESSIBILITY_ID&path=RTT_ID` | 26.2 | F26W |  |
| 輔助使用 → 側邊按鈕按鍵速度 | Accessibility → Side Button Click Speed | `bridge:root=ACCESSIBILITY_ID&path=SideButton` | 26.2 | F26W |  |
| 輔助使用 → Siri | Accessibility → Siri | `bridge:root=ACCESSIBILITY_ID&path=SIRI_CELL_ID` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 | Accessibility → Chimes | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell` | 26.2 | F26W MAN |  |
| 輔助使用 → 觸控調節 | Accessibility → Touch Accommodations | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell` | 26.2 | F26W |  |
| 輔助使用 → 旁白 | Accessibility → VoiceOver | `bridge:root=ACCESSIBILITY_ID&path=VOICEOVER_ID` | 26.2 | F26W |  |
| 輔助使用 → 縮放 | Accessibility → Zoom | `bridge:root=ACCESSIBILITY_ID&path=ZOOM_ID` | 26.2 | F26W |  |
| 輔助使用 → 粗體文字 | Accessibility → Bold Text | `bridge:root=ACCESSIBILITY#BoldTextEnabled` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 灰階 | Accessibility → Grayscale | `bridge:root=ACCESSIBILITY#GrayscaleDisplay` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 耳機通知 | Accessibility → Headphone Notifications | `bridge:root=ACCESSIBILITY#HeadphoneNotificationsID` | 16.2 · 18.7 | F18W F16W |  |
| 輔助使用 → 聽力 | Accessibility → Hearing | `bridge:root=ACCESSIBILITY#HEARING` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 助聽裝置 | Accessibility → Hearing Devices | `bridge:root=ACCESSIBILITY#HearingDevicesComplicationGroupID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 左右立體聲平衡 | Accessibility → Left-Right Stereo Balance | `bridge:root=ACCESSIBILITY#LEFT_RIGHT_BALANCE_SPOKEN` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 輪椅活動 | Accessibility → WHEELCHAIR ACTIVITY | `bridge:root=ACCESSIBILITY#MOBILITY` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 單聲道音訊 | Accessibility → Mono Audio | `bridge:root=ACCESSIBILITY#MonoAudioEnabled` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 動作 | Accessibility → Motor | `bridge:root=ACCESSIBILITY#MotorGroupCell` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 開啟/關閉標籤 | Accessibility → On/Off Labels | `bridge:root=ACCESSIBILITY#OnOffLabelsEnabled` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 減少透明度 | Accessibility → Reduce Transparency | `bridge:root=ACCESSIBILITY#REDUCE_TRANSPARENCY` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸覺回饋時間速度 | Accessibility → Taptic Time Speed | `bridge:root=ACCESSIBILITY#TapticTimeSpeedAdjustmentGroup` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 視覺 | Accessibility → Vision | `bridge:root=ACCESSIBILITY#VISION` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 點一下來說話 | Accessibility → Tap to Talk | `bridge:root=ACCESSIBILITY#WalkieTalkieTapToTalk` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 對講機 | Accessibility → Walkie-Talkie | `bridge:root=ACCESSIBILITY#WalkieTalkieTapToTalkGroup` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 複雜功能 → 麥克風音量 | Accessibility → Complication → Mic Volume | `bridge:root=ACCESSIBILITY&path=HearingDevicesComplicationRowID#Mic%20Volume` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 複雜功能 → 程式 | Accessibility → Complication → Program | `bridge:root=ACCESSIBILITY&path=HearingDevicesComplicationRowID#Program` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → RTT → RTT | Accessibility → RTT → RTT | `bridge:root=ACCESSIBILITY&path=RTT#RTT_TITLE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → RTT → 立即傳送 | Accessibility → RTT → Send Immediately | `bridge:root=ACCESSIBILITY&path=RTT#TTY_REALTIME_LABEL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → RTT → 預設回覆 | Accessibility → RTT → Default Replies | `bridge:root=ACCESSIBILITY&path=RTT/RTT_CANNED_TEXT_TITLE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → RTT → 轉送號碼 | Accessibility → RTT → Relay Number | `bridge:root=ACCESSIBILITY&path=RTT/TTY_RELAY_LABEL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 預設值 | Accessibility → Side Button Click Speed → Default | `bridge:root=ACCESSIBILITY&path=SideButton#SIDE_CLICK_SPEED_DEFAULT` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 慢速 | Accessibility → Side Button Click Speed → Slow | `bridge:root=ACCESSIBILITY&path=SideButton#SIDE_CLICK_SPEED_SLOW` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 最慢 | Accessibility → Side Button Click Speed → Slowest | `bridge:root=ACCESSIBILITY&path=SideButton#SIDE_CLICK_SPEED_SLOWEST` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 按鍵速度 | Accessibility → Side Button Click Speed → Click Speed | `bridge:root=ACCESSIBILITY&path=SideButton#SIDE_SPEED_HEADER` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 響鈴 | Accessibility → Chimes → Chimes | `bridge:root=ACCESSIBILITY&path=TapticChimesCell#Chimes` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 排程 | Accessibility → Chimes → Schedule | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Schedule` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 聲音 | Accessibility → Chimes → Sounds | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Sounds` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸控調節 → 使用最終觸控位置 | Accessibility → Touch Accommodations → Use Final Touch Location | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#ACTIVATE_ON_RELEASE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸控調節 → 使用最初觸控位置 | Accessibility → Touch Accommodations → Use Initial Touch Location | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#ACTIVATE_ON_TOUCH` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸控調節 → 按住持續時間 | Accessibility → Touch Accommodations → Hold Duration | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#HoldDuration` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸控調節 → 按住持續時間 | Accessibility → Touch Accommodations → Hold Duration | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#HoldDurationGroup` | 18.7 | F18W MAN |  |
| 輔助使用 → 觸控調節 → 忽略重複 | Accessibility → Touch Accommodations → Ignore Repeat | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#IgnoreRepeat` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸控調節 → 忽略重複 | Accessibility → Touch Accommodations → Ignore Repeat | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#IgnoreRepeatGroup` | 18.7 | F18W MAN |  |
| 輔助使用 → 觸控調節 → 關閉 | Accessibility → Touch Accommodations → Off | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#OFF` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 觸控調節 → 輕點輔助 | Accessibility → Touch Accommodations → Tap Assistance | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#Tap%20Assistance` | 16.2 · 18.7 | F18W F16W MAN |  |
| — | — | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#TOUCH_ACCOMMODATIONS` | — | MAN |  |
| 輔助使用 → 觸控調節 → 觸控調節 | Accessibility → Touch Accommodations → Touch Accommodations | `bridge:root=ACCESSIBILITY&path=TouchAccommodationsCell#TOUCH_ACCOMMODATIONS_SWITCHER` | 16.2 · 18.7 | F18W F16W |  |
| 輔助使用 → 自動選取焦點內的App | Accessibility → Auto-Select Focused App | `bridge:root=ACCESSIBILITY_ID#AppSwitcherAutoSelect` | 26.2 | F26W |  |
| 輔助使用 → App切換器 | Accessibility → App Switcher | `bridge:root=ACCESSIBILITY_ID#AppSwitcherAutoSelectGroup` | 26.2 | F26W |  |
| 輔助使用 → 粗體文字 | Accessibility → Bold Text | `bridge:root=ACCESSIBILITY_ID#BoldTextEnabled` | 26.2 | F26W |  |
| 輔助使用 → 灰階 | Accessibility → Grayscale | `bridge:root=ACCESSIBILITY_ID#GrayscaleDisplay` | 26.2 | F26W |  |
| 輔助使用 → 耳機通知 | Accessibility → Headphone Notifications | `bridge:root=ACCESSIBILITY_ID#HeadphoneNotificationsID` | 26.2 | F26W |  |
| 輔助使用 → 聽力 | Accessibility → Hearing | `bridge:root=ACCESSIBILITY_ID#HEARING` | 26.2 | F26W |  |
| 輔助使用 → 助聽裝置 | Accessibility → Hearing Devices | `bridge:root=ACCESSIBILITY_ID#HearingDevicesComplicationGroupID` | 26.2 | F26W |  |
| 輔助使用 → 增加對比 | Accessibility → Increase Contrast | `bridge:root=ACCESSIBILITY_ID#INCREASE_CONTRAST` | 26.2 | F26W |  |
| 輔助使用 → 左右立體聲平衡 | Accessibility → Left-Right Stereo Balance | `bridge:root=ACCESSIBILITY_ID#LEFT_RIGHT_BALANCE_SPOKEN` | 26.2 | F26W |  |
| 輔助使用 → 輪椅活動 | Accessibility → Wheelchair Activity | `bridge:root=ACCESSIBILITY_ID#MOBILITY` | 26.2 | F26W |  |
| 輔助使用 → 單聲道音訊 | Accessibility → Mono Audio | `bridge:root=ACCESSIBILITY_ID#MonoAudioEnabled` | 26.2 | F26W |  |
| 輔助使用 → 動作 | Accessibility → Motor | `bridge:root=ACCESSIBILITY_ID#MotorGroupCell` | 26.2 | F26W |  |
| 輔助使用 → 開啟/關閉標籤 | Accessibility → On/Off Labels | `bridge:root=ACCESSIBILITY_ID#OnOffLabelsEnabled` | 26.2 | F26W |  |
| 輔助使用 → 減少透明度 | Accessibility → Reduce Transparency | `bridge:root=ACCESSIBILITY_ID#REDUCE_TRANSPARENCY` | 26.2 | F26W |  |
| 輔助使用 → 觸覺回饋時間速度 | Accessibility → Taptic Time Speed | `bridge:root=ACCESSIBILITY_ID#TapticTimeSpeedAdjustmentGroup` | 26.2 | F26W |  |
| 輔助使用 → 文字大小 | Accessibility → Text Size | `bridge:root=ACCESSIBILITY_ID#TEXT_SIZE` | 26.2 | F26W |  |
| 輔助使用 → 視覺 | Accessibility → Vision | `bridge:root=ACCESSIBILITY_ID#VISION_GROUP` | 26.2 | F26W |  |
| 輔助使用 → 點一下來說話 | Accessibility → Tap to Talk | `bridge:root=ACCESSIBILITY_ID#WalkieTalkieTapToTalk` | 26.2 | F26W |  |
| 輔助使用 → 對講機 | Accessibility → Walkie-Talkie | `bridge:root=ACCESSIBILITY_ID#WalkieTalkieTapToTalkGroup` | 26.2 | F26W |  |
| 輔助使用 → 複雜功能 → 麥克風音量 | Accessibility → Complication → Mic Volume | `bridge:root=ACCESSIBILITY_ID&path=HearingDevicesComplicationRowID#Mic%20Volume` | 26.2 | F26W |  |
| 輔助使用 → 複雜功能 → 程式 | Accessibility → Complication → Program | `bridge:root=ACCESSIBILITY_ID&path=HearingDevicesComplicationRowID#Program` | 26.2 | F26W |  |
| 輔助使用 → RTT → RTT | Accessibility → RTT → RTT | `bridge:root=ACCESSIBILITY_ID&path=RTT_ID#RTT_ROW_ID` | 26.2 | F26W |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 按鍵速度 | Accessibility → Side Button Click Speed → Click Speed | `bridge:root=ACCESSIBILITY_ID&path=SideButton#CLICK_SPEED_GROUP_CELL` | 26.2 | F26W |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 預設值 | Accessibility → Side Button Click Speed → Default | `bridge:root=ACCESSIBILITY_ID&path=SideButton#SIDE_CLICK_SPEED_DEFAULT` | 26.2 | F26W |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 慢速 | Accessibility → Side Button Click Speed → Slow | `bridge:root=ACCESSIBILITY_ID&path=SideButton#SIDE_CLICK_SPEED_SLOW` | 26.2 | F26W |  |
| 輔助使用 → 側邊按鈕按鍵速度 → 最慢 | Accessibility → Side Button Click Speed → Slowest | `bridge:root=ACCESSIBILITY_ID&path=SideButton#SIDE_CLICK_SPEED_SLOWEST` | 26.2 | F26W |  |
| 輔助使用 → Siri → 輸入來與Siri對話 | Accessibility → Siri → Type to Siri | `bridge:root=ACCESSIBILITY_ID&path=SIRI_CELL_ID#Type%20to%20Siri` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 響鈴 | Accessibility → Chimes → Chimes | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell#Chimes` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 排程 | Accessibility → Chimes → Schedule | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SCHEDULE_ID` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 聲音 | Accessibility → Chimes → Sounds | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SOUNDS_ID` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 使用最終觸控位置 | Accessibility → Touch Accommodations → Use Final Touch Location | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#ACTIVATE_ON_RELEASE` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 使用最初觸控位置 | Accessibility → Touch Accommodations → Use Initial Touch Location | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#ACTIVATE_ON_TOUCH` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 按住持續時間 | Accessibility → Touch Accommodations → Hold Duration | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#HoldDuration` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 按住持續時間 | Accessibility → Touch Accommodations → Hold Duration | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#HoldDurationGroup` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 忽略重複 | Accessibility → Touch Accommodations → Ignore Repeat | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#IgnoreRepeat` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 忽略重複 | Accessibility → Touch Accommodations → Ignore Repeat | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#IgnoreRepeatGroup` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 關閉 | Accessibility → Touch Accommodations → Off | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#OFF` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 輕點輔助 | Accessibility → Touch Accommodations → Tap Assistance | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#Tap%20Assistance` | 26.2 | F26W |  |
| 輔助使用 → 觸控調節 → 觸控調節 | Accessibility → Touch Accommodations → Touch Accommodations | `bridge:root=ACCESSIBILITY_ID&path=TouchAccommodationsCell#TOUCH_ACCOMMODATIONS_SWITCHER` | 26.2 | F26W |  |
| 輔助使用 → RTT → 預設回覆 → 加入回覆⋯ | Accessibility → RTT → Default Replies → Add reply… | `bridge:root=ACCESSIBILITY&path=RTT/RTT_CANNED_TEXT_TITLE#Add%20reply%E2%80%A6` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → RTT → 預設回覆 → 預設回覆 | Accessibility → RTT → Default Replies → Default Replies | `bridge:root=ACCESSIBILITY&path=RTT/RTT_CANNED_TEXT_TITLE#Default%20Replies` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 排程 → 15分鐘 | Accessibility → Chimes → Schedule → 15 minutes | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Schedule#15%20minutes` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 排程 → 30分鐘 | Accessibility → Chimes → Schedule → 30 minutes | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Schedule#30%20minutes` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 排程 → 每小時 | Accessibility → Chimes → Schedule → Hourly | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Schedule#Hourly` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 聲音 → 鈴聲 | Accessibility → Chimes → Sounds → Bells | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Sounds#Bells` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 聲音 → 鳥 | Accessibility → Chimes → Sounds → Birds | `bridge:root=ACCESSIBILITY&path=TapticChimesCell/Sounds#Birds` | 16.2 · 18.7 | F18W F16W MAN |  |
| 輔助使用 → 響鈴 → 排程 → 15分鐘 | Accessibility → Chimes → Schedule → 15 minutes | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SCHEDULE_ID#15%20minutes` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 排程 → 30分鐘 | Accessibility → Chimes → Schedule → 30 minutes | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SCHEDULE_ID#30%20minutes` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 排程 → 每小時 | Accessibility → Chimes → Schedule → Hourly | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SCHEDULE_ID#Hourly` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 聲音 → 鈴聲 | Accessibility → Chimes → Sounds → Bells | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SOUNDS_ID#Bells` | 26.2 | F26W |  |
| 輔助使用 → 響鈴 → 聲音 → 鳥 | Accessibility → Chimes → Sounds → Birds | `bridge:root=ACCESSIBILITY_ID&path=TapticChimesCell/CHIMES_SOUNDS_ID#Birds` | 26.2 | F26W |  |

### watchOS bridge: Action Button

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 動作按鈕 | Action Button | `bridge:root=ACTION_BUTTON_ID` | 26.2 | F26W |  |
| 動作按鈕 → 快速切換 | Action Button → Quick Switch | `bridge:root=ACTION_BUTTON_ID&path=ShowQuickSwitch` | 26.2 | F26W |  |
| 動作按鈕 → 體能訓練 | Action Button → Workout | `bridge:root=ACTION_BUTTON_ID&path=StingSystemSettingsActionTypeItem` | 26.2 | F26W |  |
| 動作按鈕 | Action Button | `bridge:root=STING_TITLE` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 動作按鈕 → 動作 \| 手勢 | Action Button → Action \| Gestures | `bridge:root=ACTION_BUTTON_ID#StingSystemSettingsActionTypeGroupID` | 26.2 | F26W |  |
| 動作按鈕 → 第一次按下 | Action Button → First Press | `bridge:root=ACTION_BUTTON_ID#StingSystemSettingsWorkoutGroupID` | 26.2 | F26W |  |
| 動作按鈕 → 快速切換 → 快速切換 | Action Button → Quick Switch → Quick Switch | `bridge:root=ACTION_BUTTON_ID&path=ShowQuickSwitch#Quick%20Switch` | 26.2 | F26W |  |
| 動作按鈕 → 快速切換 → 包含的App | Action Button → Quick Switch → Included Apps | `bridge:root=ACTION_BUTTON_ID&path=ShowQuickSwitch#StingQuickSwitchAppGroup` | 26.2 | F26W |  |
| 動作按鈕 → 快速切換 → 快速切換 | Action Button → Quick Switch → Quick Switch | `bridge:root=ACTION_BUTTON_ID&path=ShowQuickSwitch#StingQuickSwitchToggleGroup` | 26.2 | F26W |  |
| 動作按鈕 → 體能訓練 → 無 | Action Button → Workout → None | `bridge:root=ACTION_BUTTON_ID&path=StingSystemSettingsActionTypeItem#StingSystemSettingsSelectedActionTypeItem` | 26.2 | F26W |  |

### watchOS bridge: Activity

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 活動記錄 | Activity | `bridge:root=com.apple.HealthAppsSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 進度更新 | Activity → Progress Updates | `bridge:root=com.apple.HealthAppsSettings&path=PROGRESS_UPDATES_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 成就 | Activity → Achievements | `bridge:root=com.apple.HealthAppsSettings#ACHIEVEMENTS_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 活動記錄分享通知 | Activity → Activity Sharing Notifications | `bridge:root=com.apple.HealthAppsSettings#ACTIVITY_SHARING_NOTIFICATIONS_ENABLED` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 每日指導 | Activity → Daily Coaching | `bridge:root=com.apple.HealthAppsSettings#DAILY_PROGRESS_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 目標完成 | Activity → Goal Completions | `bridge:root=com.apple.HealthAppsSettings#GOAL_COMPLETIONS_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 特殊挑戰 | Activity → Special Challenges | `bridge:root=com.apple.HealthAppsSettings#REMOTE_ACHIEVEMENTS_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 每週摘要 | Activity → Weekly Summary | `bridge:root=com.apple.HealthAppsSettings#WEEKLY_SUMMARY_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 進度更新 → 每8小時 | Activity → Progress Updates → Every 8 hours | `bridge:root=com.apple.HealthAppsSettings&path=PROGRESS_UPDATES_ENABLED_LABEL#EIGHT_HOURS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 進度更新 → 每4小時 | Activity → Progress Updates → Every 4 hours | `bridge:root=com.apple.HealthAppsSettings&path=PROGRESS_UPDATES_ENABLED_LABEL#FOUR_HOURS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 進度更新 → 每6小時 | Activity → Progress Updates → Every 6 hours | `bridge:root=com.apple.HealthAppsSettings&path=PROGRESS_UPDATES_ENABLED_LABEL#SIX_HOURS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 進度更新 → 每2小時 | Activity → Progress Updates → Every 2 hours | `bridge:root=com.apple.HealthAppsSettings&path=PROGRESS_UPDATES_ENABLED_LABEL#TWO_HOURS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 活動記錄 → 進度更新 → 無 | Activity → Progress Updates → None | `bridge:root=com.apple.HealthAppsSettings&path=PROGRESS_UPDATES_ENABLED_LABEL#ZERO_HOURS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: App Store

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| App Store | App Store | `bridge:root=com.apple.BridgeAppStoreDaemonSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| App Store → 自動更新 | App Store → Automatic Updates | `bridge:root=com.apple.BridgeAppStoreDaemonSettings#Automatic%20Updates` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| App Store → 自動下載 | App Store → Automatic Downloads | `bridge:root=com.apple.BridgeAppStoreDaemonSettings#automaticDownloadSpecifier` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: App View

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| App顯示方式 | App View | `bridge:root=APP_VIEW_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Audiobooks

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 有聲書 | Audiobooks | `bridge:root=com.apple.NanoBooks.BridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 有聲書 → 登入 | Audiobooks → Sign In | `bridge:root=com.apple.NanoBooks.BridgeSettings#Sign%20In` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Blood Oxygen

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 血氧濃度 | Blood Oxygen | `bridge:root=com.apple.OxygenSaturationSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Calendar

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 行事曆 | Calendar | `bridge:root=com.apple.NanoCalendarBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 行事曆 → 自訂⋯ | Calendar → Custom… | `bridge:root=com.apple.NanoCalendarBridgeSettings&path=CALENDARS_CUSTOM_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 行事曆 → 邀請 | Calendar → Invitations | `bridge:root=com.apple.NanoCalendarBridgeSettings&path=Invitations` | 18.7 · 26.2 | F26W F18W MAN |  |
| 行事曆 → 邀請對象回覆 | Calendar → Invitee Responses | `bridge:root=com.apple.NanoCalendarBridgeSettings&path=Invitee%20Responses` | 18.7 · 26.2 | F26W F18W MAN |  |
| 行事曆 → 共享的行事曆更動 | Calendar → Shared Calendar Changes | `bridge:root=com.apple.NanoCalendarBridgeSettings&path=Shared%20Calendar%20Alerts` | 18.7 · 26.2 | F26W F18W MAN |  |
| 行事曆 → 即將到來的行程 | Calendar → Upcoming Events | `bridge:root=com.apple.NanoCalendarBridgeSettings&path=Upcoming%20Events` | 18.7 · 26.2 | F26W F18W MAN |  |
| 行事曆 → 使用iPhone設定 | Calendar → Mirror my iPhone | `bridge:root=com.apple.NanoCalendarBridgeSettings#CALENDARS_MIRROR_MY_COMPANION_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 行事曆 → 行事曆 | Calendar → CALENDARS | `bridge:root=com.apple.NanoCalendarBridgeSettings#CALENDARS_MIRROR_RADIO_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 行事曆 → 自訂⋯ | Calendar → Custom… | `bridge:root=com.apple.NanoCalendarBridgeSettings#CUSTOM_ID` | 18.7 · 26.2 | F26W F18W MAN |  |
| 行事曆 → 使用iPhone設定 | Calendar → Mirror my iPhone | `bridge:root=com.apple.NanoCalendarBridgeSettings#MIRROR_MY_COMPANION_ID` | 18.7 · 26.2 | F26W F18W MAN |  |
| 行事曆 → 通知 | Calendar → NOTIFICATIONS | `bridge:root=com.apple.NanoCalendarBridgeSettings#MIRROR_RADIO_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Carrier Settings

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 電信業者設定 | Carrier Settings | `bridge:root=CARRIER_SETTINGS` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Cellular

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 行動服務 | Cellular | `bridge:root=CELLULAR_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Clock

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 時鐘 | Clock | `bridge:root=com.apple.NanoClockBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → 城市簡稱 | Clock → City Abbreviations | `bridge:root=com.apple.NanoClockBridgeSettings&path=City%20Abbreviations` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → 姓名簡稱 | Clock → Monogram | `bridge:root=com.apple.NanoClockBridgeSettings&path=MONOGRAM_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → Siri錶面資料來源 | Clock → Siri Face Data Sources | `bridge:root=com.apple.NanoClockBridgeSettings&path=Siri%20Face%20Data%20Sources` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → 聲音 | Clock → Sounds | `bridge:root=com.apple.NanoClockBridgeSettings&path=Sounds` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 觸覺回饋時間 | Clock → Taptic Time | `bridge:root=com.apple.NanoClockBridgeSettings&path=Taptic%20Time` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 24小時制 | Clock → 24-Hour Time | `bridge:root=com.apple.NanoClockBridgeSettings#24-Hour%20Time` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → 永遠報時 | Clock → Always Speak | `bridge:root=com.apple.NanoClockBridgeSettings#Always%20Speak` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 鐘聲 | Clock → Chimes | `bridge:root=com.apple.NanoClockBridgeSettings#Chimes` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 以「靜音模式」控制 | Clock → Control With Silent Mode | `bridge:root=com.apple.NanoClockBridgeSettings#Control%20With%20Silent%20Mode` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 通知指示符號 | Clock → Notifications Indicator | `bridge:root=com.apple.NanoClockBridgeSettings#Notifications%20Indicator` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → 推播iPhone上的提示 | Clock → Push Alerts from iPhone | `bridge:root=com.apple.NanoClockBridgeSettings#Push%20Alerts%20from%20iPhone` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 時鐘 → 報時 | Clock → Speak Time | `bridge:root=com.apple.NanoClockBridgeSettings#Speak%20Time` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 錶面通知 | Clock → Watch Face Notifications | `bridge:root=com.apple.NanoClockBridgeSettings#Watch%20Face%20Notifications` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 聲音 → 鈴聲 | Clock → Sounds → Bells | `bridge:root=com.apple.NanoClockBridgeSettings&path=Sounds#Bells` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 聲音 → 鳥 | Clock → Sounds → Birds | `bridge:root=com.apple.NanoClockBridgeSettings&path=Sounds#Birds` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 觸覺回饋時間 → 數字 | Clock → Taptic Time → Digits | `bridge:root=com.apple.NanoClockBridgeSettings&path=Taptic%20Time#Digits` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 觸覺回饋時間 → 摩斯密碼 | Clock → Taptic Time → Morse Code | `bridge:root=com.apple.NanoClockBridgeSettings&path=Taptic%20Time#Morse%20Code` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 觸覺回饋時間 → 觸覺回饋時間 | Clock → Taptic Time → Taptic Time | `bridge:root=com.apple.NanoClockBridgeSettings&path=Taptic%20Time#Taptic%20Time` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 時鐘 → 觸覺回饋時間 → 簡易 | Clock → Taptic Time → Terse | `bridge:root=com.apple.NanoClockBridgeSettings&path=Taptic%20Time#Terse` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: com.apple.DeepBreathingSettings

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `bridge:root=com.apple.DeepBreathingSettings` | — | MAN |  |
| — | — | `bridge:root=com.apple.DeepBreathingSettings&path=DEEP_BREATHING_FREQUENCY_ID` | — | MAN |  |
| — | — | `bridge:root=com.apple.DeepBreathingSettings#DEEP_BREATHING_MUTE_FOR_TODAY_ID` | — | MAN |  |
| — | — | `bridge:root=com.apple.DeepBreathingSettings#DEEP_BREATHING_WEEKLY_SUMMARY_ID` | — | MAN |  |

### watchOS bridge: com.nike.nikeplus-gps

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `bridge:root=com.nike.nikeplus-gps&thirdPartyBundleID=com.nike.nikeplus-gps` | — | MAN |  |
| — | — | `bridge:root=com.nike.nikeplus-gps#SHOWS_ON_GIZMO` | — | MAN |  |

### watchOS bridge: Complications

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 複雜功能 | Complications | `bridge:root=COMPLICATIONS` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Contacts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 聯絡人 | Contacts | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 排序 | Contacts → Sort Order | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=contactsSortOrder` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 顯示順序 | Contacts → Display Order | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=NSPersonNameDefaultDisplayNameOrder` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 簡稱 | Contacts → Short Name | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 排序 → 名字在前，姓氏在後 | Contacts → Sort Order → First, Last | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=contactsSortOrder#0` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 聯絡人 → 排序 → 姓氏在前，名字在後 | Contacts → Sort Order → Last, First | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=contactsSortOrder#1` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=contactsSortOrder#First` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=contactsSortOrder#Last` | — | MAN |  |
| 聯絡人 → 顯示順序 → 名字在前，姓氏在後 | Contacts → Display Order → First, Last | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=NSPersonNameDefaultDisplayNameOrder#1` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 聯絡人 → 顯示順序 → 姓氏在前，名字在後 | Contacts → Display Order → Last, First | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=NSPersonNameDefaultDisplayNameOrder#2` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=NSPersonNameDefaultDisplayNameOrder#First` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=NSPersonNameDefaultDisplayNameOrder#Last` | — | MAN |  |
| 聯絡人 → 簡稱 → 名字起始字母和姓氏 | Contacts → Short Name → First Initial & Last Name | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName#First%20Initial%20&%20Last%20Name` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 簡稱 → 名字和姓氏起始字母 | Contacts → Short Name → First Name & Last Initial | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName#First%20Name%20&%20Last%20Initial` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 簡稱 → 只有名字 | Contacts → Short Name → First Name Only | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName#First%20Name%20Only` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 簡稱 → 只有姓氏 | Contacts → Short Name → Last Name Only | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName#Last%20Name%20Only` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 簡稱 → 偏好暱稱 | Contacts → Short Name → Prefer Nicknames | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName#Prefer%20Nicknames` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 聯絡人 → 簡稱 → 簡稱 | Contacts → Short Name → Short Name | `bridge:root=com.apple.NanoContactsBridgeSettingsPaired&path=PersonShortName#Short%20Name` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Control Center

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 控制中心 | Control Center | `bridge:root=CONTROL_CENTER_ID` | 26.2 | F26W |  |
| 控制中心 → 重置「控制中心」佈局 | Control Center → Reset Control Center Layout | `bridge:root=CONTROL_CENTER_ID#CONTROL_CENTER_RESET_ID` | 26.2 | F26W |  |

### watchOS bridge: Depth

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 水深 | Depth | `bridge:root=com.apple.DepthCompanionSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Display & Brightness

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 螢幕顯示與亮度 | Display & Brightness | `bridge:root=DISPLAY_AND_BRIGHTNESS` | 16.2 · 18.7 | F18W F16W MAN |  |
| 螢幕顯示與亮度 → 永遠開啟 | Display & Brightness → Always On | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 螢幕顯示與亮度 → 喚醒持續時間 | Display & Brightness → Wake Duration | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=Wake%20Duration` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 | Display & Brightness | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 | Display & Brightness → Always On | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 | Display & Brightness → Wake Duration | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=WAKE_DURATION_SELECTION_KEY` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 粗體文字 | Display & Brightness → Bold Text | `bridge:root=DISPLAY_AND_BRIGHTNESS#BOLD_TEXT` | 16.2 · 18.7 | F18W F16W MAN |  |
| 螢幕顯示與亮度 → 亮度 | Display & Brightness → Brightness | `bridge:root=DISPLAY_AND_BRIGHTNESS#BRIGHTNESS_LABEL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 螢幕顯示與亮度 → 文字大小 | Display & Brightness → Text Size | `bridge:root=DISPLAY_AND_BRIGHTNESS#TEXT_SIZE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 螢幕顯示與亮度 → 喚醒 | Display & Brightness → WAKE | `bridge:root=DISPLAY_AND_BRIGHTNESS#WAKE` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 轉動錶冠時喚醒 | Display & Brightness → Wake on Crown Rotation | `bridge:root=DISPLAY_AND_BRIGHTNESS#WAKE_SCREEN_ON_CROWN_UP_SWITCH_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 抬起手腕時喚醒 | Display & Brightness → Wake on Wrist Raise | `bridge:root=DISPLAY_AND_BRIGHTNESS#WAKE_SCREEN_ON_WRIST_RAISE_SWITCH_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 永遠開啟 → 永遠開啟 | Display & Brightness → Always On → Always On | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID#TRITIUM_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 螢幕顯示與亮度 → 永遠開啟 → 放下手腕 | Display & Brightness → Always On → WRIST DOWN | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID#TRITIUM_PRIVACY_GROUP_ID` | 16.2 · 18.7 | F18W F16W |  |
| — | — | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID#TRITIUM_PRIVACY_ID` | — | MAN |  |
| 螢幕顯示與亮度 → 永遠開啟 → 顯示App | Display & Brightness → Always On → Show Apps | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID/Show%20Apps` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 永遠開啟 → 顯示通知 | Display & Brightness → Always On → Show Notifications | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID/Show%20Notifications` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 → 發亮70秒 | Display & Brightness → Wake Duration → Wake for 70 Seconds | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=Wake%20Duration#LONG_WAKE_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 → 點一下時 | Display & Brightness → Wake Duration → ON TAP | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=Wake%20Duration#ON_TAP_GROUP_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 → 發亮15秒 | Display & Brightness → Wake Duration → Wake for 15 Seconds | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=Wake%20Duration#SHORT_WAKE_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 粗體文字 | Display & Brightness → Bold Text | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID#BOLD_TEXT` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 亮度 | Display & Brightness → Brightness | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID#BRIGHTNESS_LABEL` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 文字大小 | Display & Brightness → Text Size | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID#TEXT_SIZE` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 喚醒 | Display & Brightness → Wake | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID#Wake` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 轉動錶冠時喚醒 | Display & Brightness → Wake on Crown Rotation | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID#WAKE_SCREEN_ON_CROWN_UP_SWITCH_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 抬起手腕時喚醒 | Display & Brightness → Wake on Wrist Raise | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID#WAKE_SCREEN_ON_WRIST_RAISE_SWITCH_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 永遠顯示 | Display & Brightness → Always On → Always On | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID#TRITIUM_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 放下手腕 | Display & Brightness → Always On → WRIST DOWN | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID#TRITIUM_PRIVACY_GROUP_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App | Display & Brightness → Always On → Show Apps | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示複雜功能資料 | Display & Brightness → Always On → Show Complications Data | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_COMPLICATIONS_DATA_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示即時動態 | Display & Brightness → Always On → Show Live Activities | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_LIVE_ACTIVITIES_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 | Display & Brightness → Always On → Show Notifications | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 → 發亮70秒 | Display & Brightness → Wake Duration → Wake for 70 Seconds | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=WAKE_DURATION_SELECTION_KEY#LONG_WAKE_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 → 點一下時 | Display & Brightness → Wake Duration → ON TAP | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=WAKE_DURATION_SELECTION_KEY#ON_TAP_GROUP_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 喚醒持續時間 → 發亮15秒 | Display & Brightness → Wake Duration → Wake for 15 Seconds | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=WAKE_DURATION_SELECTION_KEY#SHORT_WAKE_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠開啟 → 顯示App → 顯示App | Display & Brightness → Always On → Show Apps → Show Apps | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID/Show%20Apps#APP_BACKLIGHT_PRIVACY_GLOBAL_APP` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 永遠開啟 → 顯示App → APP | Display & Brightness → Always On → Show Apps → APPS | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID/Show%20Apps#APP_GROUP_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 永遠開啟 → 顯示通知 → 顯示通知 | Display & Brightness → Always On → Show Notifications → Show Notifications | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID/Show%20Notifications#APP_BACKLIGHT_PRIVACY_GLOBAL_APP` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 永遠開啟 → 顯示通知 → APPLE WATCH APP | Display & Brightness → Always On → Show Notifications → APPLE WATCH APPS | `bridge:root=DISPLAY_AND_BRIGHTNESS&path=TRITIUM_ID/Show%20Notifications#APP_GROUP_ID` | 16.2 · 18.7 | F18W F16W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → 顯示App | Display & Brightness → Always On → Show Apps → Show Apps | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#APP_BACKLIGHT_PRIVACY_GLOBAL_APP` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → APP | Display & Brightness → Always On → Show Apps → APPS | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#APP_GROUP_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → App Store | Display & Brightness → Always On → Show Apps → App Store | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#com.apple.AppStore` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → 電話 | Display & Brightness → Always On → Show Apps → Phone | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#com.apple.NanoPhone` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → 照片 | Display & Brightness → Always On → Show Apps → Photos | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#com.apple.NanoPhotos` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → 設定 | Display & Brightness → Always On → Show Apps → Settings | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#com.apple.NanoSettings` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → Tap-to-Radar | Display & Brightness → Always On → Show Apps → Tap-to-Radar | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#com.apple.NanoTapToRadar` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示App → Nike Run Club | Display & Brightness → Always On → Show Apps → Nike Run Club | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_APPS_ID#com.nike.nikeplus-gps.watchkitapp` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示複雜功能資料 → App | Display & Brightness → Always On → Show Complications Data → Apps | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_COMPLICATIONS_DATA_ID#Apps` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示複雜功能資料 → 載入中⋯ | Display & Brightness → Always On → Show Complications Data → Loading… | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_COMPLICATIONS_DATA_ID#Loading%E2%80%A6` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示複雜功能資料 → 顯示複雜功能資料 | Display & Brightness → Always On → Show Complications Data → Show Complication Data | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_COMPLICATIONS_DATA_ID#Show%20Complication%20Data` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示複雜功能資料 → Siri | Display & Brightness → Always On → Show Complications Data → Siri | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_COMPLICATIONS_DATA_ID#Siri` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示複雜功能資料 → Siri卡片 | Display & Brightness → Always On → Show Complications Data → Siri Cards | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_COMPLICATIONS_DATA_ID#Siri%20Cards` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示即時動態 → 顯示即時動態 | Display & Brightness → Always On → Show Live Activities → Show Live Activities | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_LIVE_ACTIVITIES_ID#APP_BACKLIGHT_PRIVACY_GLOBAL_APP` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 顯示通知 | Display & Brightness → Always On → Show Notifications → Show Notifications | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#APP_BACKLIGHT_PRIVACY_GLOBAL_APP` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → APPLE WATCH APP \| IPHONE APP | Display & Brightness → Always On → Show Notifications → APPLE WATCH APPS \| IPHONE APPS | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#APP_GROUP_ID` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 輔助使用設定 | Display & Brightness → Always On → Show Notifications → Accessibility Settings | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.accessibility.TeachableMomentsNotifications` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → App Store | Display & Brightness → Always On → Show Notifications → App Store | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.AppStore` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 相機 | Display & Brightness → Always On → Show Notifications → Camera | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.camera` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 診斷回報程式 | Display & Brightness → Always On → Show Notifications → Diagnostics Reporter | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.DiagnosticsReporter` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Feedback Internal | Display & Brightness → Always On → Show Notifications → Feedback Internal | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.FeedbackInternal` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 追蹤通知 | Display & Brightness → Always On → Show Notifications → Tracking Notifications | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.FindMySafetyAlertsNotifications` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 健身 | Display & Brightness → Always On → Show Notifications → Fitness | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.Fitness` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Game Center | Display & Brightness → Always On → Show Notifications → Game Center | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.gamecenter` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 健康 | Display & Brightness → Always On → Show Notifications → Health | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.Health` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 書籍 | Display & Brightness → Always On → Show Notifications → Books | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.iBooks` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Connect | Display & Brightness → Always On → Show Notifications → Connect | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.ist.AppleConnect` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Caffè Macs | Display & Brightness → Always On → Show Notifications → Caffè Macs | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.ist.CaffeMacsApp` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Livability | Display & Brightness → Always On → Show Notifications → Livability | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.Livability` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 行事曆 | Display & Brightness → Always On → Show Notifications → Calendar | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.mobilecal` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 郵件 | Display & Brightness → Always On → Show Notifications → Mail | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.mobilemail` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 訊息 | Display & Brightness → Always On → Show Notifications → Messages | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.MobileSMS` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 電話 | Display & Brightness → Always On → Show Notifications → Phone | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.NanoPhone` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 照片 | Display & Brightness → Always On → Show Notifications → Photos | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.NanoPhotos` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 設定 | Display & Brightness → Always On → Show Notifications → Settings | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.NanoSettings` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Tap-to-Radar | Display & Brightness → Always On → Show Notifications → Tap-to-Radar | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.NanoTapToRadar` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → 天氣 | Display & Brightness → Always On → Show Notifications → Weather | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.apple.weather` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Self Service | Display & Brightness → Always On → Show Notifications → Self Service | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.jamfsoftware.selfservice` | 26.2 | F26W |  |
| 螢幕顯示與亮度 → 永遠顯示 → 顯示通知 → Nike Run Club | Display & Brightness → Always On → Show Notifications → Nike Run Club | `bridge:root=DISPLAY_AND_BRIGHTNESS_ID&path=TRITIUM_ID/SHOW_NOTIFICATIONS_ID#com.nike.nikeplus-gps.watchkitapp` | 26.2 | F26W |  |

### watchOS bridge: Dock

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Dock | Dock | `bridge:root=DOCK` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Dock | Dock | `bridge:root=DOCK.0` | 18.7 · 26.2 | F26W F18W MAN |  |
| Dock → 喜好項目 | Dock → Favorites | `bridge:root=DOCK#Favorites` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Dock → Dock排列 | Dock → Dock Ordering | `bridge:root=DOCK#OrderingOptionGroup` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Dock → 最近項目 | Dock → Recents | `bridge:root=DOCK#Recents` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Dock → 喜好項目 | Dock → Favorites | `bridge:root=DOCK.0#Favorites` | 18.7 · 26.2 | F26W F18W MAN |  |
| Dock → Dock排列 | Dock → Dock Ordering | `bridge:root=DOCK.0#OrderingOptionGroup` | 18.7 · 26.2 | F26W F18W MAN |  |
| Dock → 最近項目 | Dock → Recents | `bridge:root=DOCK.0#Recents` | 18.7 · 26.2 | F26W F18W MAN |  |

### watchOS bridge: Emergency SOS

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| SOS緊急服務 | Emergency SOS | `bridge:root=SOS_MODE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Find My Apple Watch

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 尋找我的Apple Watch | Find My Apple Watch | `bridge:root=ActiveWatch` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 尋找我的Apple Watch → 配對新的Apple Watch | Find My Apple Watch → Pair New Watch | `bridge:root=ActiveWatch&path=Pair%20New%20Watch` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: FollowUpList_

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `bridge:root=FollowUpList_` | — | MAN DYLD |  |

### watchOS bridge: General

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 一般 | General | `bridge:root=GENERAL_LINK` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 | General → About | `bridge:root=GENERAL_LINK&path=ABOUT` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 飛航模式 | General → Airplane Mode | `bridge:root=GENERAL_LINK&path=AIRPLANE_MODE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 浸入水中時自動啟動 | General → Auto-launch when Submerged | `bridge:root=GENERAL_LINK&path=AUTO_LAUNCH` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 一般 → 自動啟動 | General → Auto-Launch | `bridge:root=GENERAL_LINK&path=AUTO_LAUNCH_ID` | 26.2 | F26W |  |
| 一般 → 背景App重新整理 | General → Background App Refresh | `bridge:root=GENERAL_LINK&path=BAR_ROW_ID` | 26.2 | F26W MAN |  |
| 一般 → 診斷記錄 | General → Diagnostic Logs | `bridge:root=GENERAL_LINK&path=DIAGNOSTIC_LOG_BROWSER` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=DO_NOT_DISTURB_ID` | — | MAN |  |
| 一般 → 專注模式 | General → Focus | `bridge:root=GENERAL_LINK&path=FOCUS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 一般 → 手錶方向 | General → Watch Orientation | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 手錶方向 | General → Watch Orientation | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION_ID` | 26.2 | F26W |  |
| 一般 → 語言與地區 | General → Language & Region | `bridge:root=GENERAL_LINK&path=LANGUAGE_AND_REGION` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 語言與地區 | General → Language & Region | `bridge:root=GENERAL_LINK&path=LANGUAGE_AND_REGION_ID` | 26.2 | F26W |  |
| 一般 → Apple帳號 | General → Apple Account | `bridge:root=GENERAL_LINK&path=LINK_WITH_ICLOUD_LINK` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| 一般 → 個人檔案 | General → Profile | `bridge:root=GENERAL_LINK&path=ManagedConfigurationList` | 26.2 | F26W MAN |  |
| 一般 → 重置 | General → Reset | `bridge:root=GENERAL_LINK&path=RESET` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 重置 | General → Reset | `bridge:root=GENERAL_LINK&path=RESET_ID` | 26.2 | F26W |  |
| 一般 → 返回錶面 | General → RETURN TO CLOCK | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 返回錶面 | General → RETURN TO CLOCK | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK_ID` | 26.2 | F26W |  |
| 一般 → 軟體更新 | General → Software Update | `bridge:root=GENERAL_LINK&path=SOFTWARE_UPDATE_LINK` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| 一般 → 上次充飽電後的使用時間 \| 儲存空間 \| 已待機 \| 省電模式 | General → Power Reserve \| Standby \| Storage \| Time Since Last Full Charge | `bridge:root=GENERAL_LINK&path=USAGE_LINK` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → Wake Screen | General → Wake Screen | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:tab=SETTINGS&root=GENERAL_LINK&path=LINK_WITH_ICLOUD_LINK` | — | MAN DYLD |  |
| 一般 → 自動App安裝 | General → Automatic App Install | `bridge:root=GENERAL_LINK#AUTO_APP_INSTALL_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 啟用截圖 | General → Enable Screenshots | `bridge:root=GENERAL_LINK#BUTTON_CHORD_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 啟用接力 | General → Enable Handoff | `bridge:root=GENERAL_LINK#CONTINUITY` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 啟用接力 | General → Enable Handoff | `bridge:root=GENERAL_LINK#CONTINUITY_ID` | 26.2 | F26W |  |
| 一般 → 自動標點符號 | General → Auto-Punctuation | `bridge:root=GENERAL_LINK#DICTATION_AUTO_PUNCTUATION_CELL_ID` | 26.2 | F26W |  |
| 一般 → 啟用聽寫 | General → Enable Dictation | `bridge:root=GENERAL_LINK#DICTATION_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 拷貝Apple Watch分析 | General → Copy Watch Analytics | `bridge:root=GENERAL_LINK#LOGS_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 夜鐘模式 | General → Nightstand Mode | `bridge:root=GENERAL_LINK#NIGHTSTAND_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=GENERAL_LINK#POWER_SAVING_MODE` | — | MAN |  |
| 一般 → 關於本機 → 應用程式 | General → About → Applications | `bridge:root=GENERAL_LINK&path=ABOUT#APPLICATIONS_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 電信業者 | General → About → Carrier | `bridge:root=GENERAL_LINK&path=ABOUT#CARRIER_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 藍牙 | General → About → Bluetooth | `bridge:root=GENERAL_LINK&path=ABOUT#DEVICE_BLUETOOTH_ADDRESS_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 機型詳細資訊 | General → About → Model Detail | `bridge:root=GENERAL_LINK&path=ABOUT#DEVICE_DETAIL_CELL_ID` | 26.2 | F26W |  |
| 一般 → 關於本機 → 機型名稱 | General → About → Model Name | `bridge:root=GENERAL_LINK&path=ABOUT#DEVICE_MARKETING_NAME_CELL_ID` | 26.2 | F26W |  |
| 一般 → 關於本機 → 機型型號 | General → About → Model Number | `bridge:root=GENERAL_LINK&path=ABOUT#DEVICE_MODEL_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 序號 | General → About → Serial Number | `bridge:root=GENERAL_LINK&path=ABOUT#DEVICE_SERIAL_NUMBER_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → Wi-Fi位址 | General → About → Wi-Fi Address | `bridge:root=GENERAL_LINK&path=ABOUT#DEVICE_WIFI_ADDRESS_CELL_ID` | 16.2 | F16W MAN |  |
| 一般 → 關於本機 → ICCID | General → About → ICCID | `bridge:root=GENERAL_LINK&path=ABOUT#ICCID_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → IMEI | General → About → IMEI | `bridge:root=GENERAL_LINK&path=ABOUT#IMEI_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 檢視Apple Watch使用手冊 | General → About → View the Apple Watch User Guide | `bridge:root=GENERAL_LINK&path=ABOUT#MANUAL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 關於本機 → watchOS版本 | General → About → watchOS Version | `bridge:root=GENERAL_LINK&path=ABOUT#OS_VERSION_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 照片 | General → About → Photos | `bridge:root=GENERAL_LINK&path=ABOUT#PHOTOS_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 檢視Apple Watch使用手冊 | General → About → View the Apple Watch User Guide | `bridge:root=GENERAL_LINK&path=ABOUT#SHOW_MANUAL_CELL_ID` | 26.2 | F26W |  |
| 一般 → 關於本機 → 歌曲 | General → About → Songs | `bridge:root=GENERAL_LINK&path=ABOUT#SONGS_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 可用空間 | General → About → Available | `bridge:root=GENERAL_LINK&path=ABOUT#STORAGE_AVAILABLE_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 容量 | General → About → Capacity | `bridge:root=GENERAL_LINK&path=ABOUT#STORAGE_CAPACITY_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → SEID | General → About → SEID | `bridge:root=GENERAL_LINK&path=ABOUT/DEVICE_SEID_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → EID | General → About → EID | `bridge:root=GENERAL_LINK&path=ABOUT/EID_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 關於本機 → 法律資訊 | General → About → Legal | `bridge:root=GENERAL_LINK&path=ABOUT/LEGAL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 關於本機 → 法律資訊 | General → About → Legal | `bridge:root=GENERAL_LINK&path=ABOUT/LEGAL_CELL_ID` | 26.2 | F26W |  |
| 一般 → 關於本機 → 名稱 | General → About → Name | `bridge:root=GENERAL_LINK&path=ABOUT/NAME_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 一般 → 浸入水中時自動啟動 → 自動啟動音訊App | General → Auto-launch when Submerged → Auto-launch Audio Apps | `bridge:root=GENERAL_LINK&path=AUTO_LAUNCH#AUTO_LAUNCH_MEDIA` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 背景App重新整理 → 背景App重新整理 | General → Background App Refresh → Background App Refresh | `bridge:root=GENERAL_LINK&path=BAR_ROW_ID#BACKGROUND_APP_UPDATING_CELL_ID` | 26.2 | F26W |  |
| 一般 → 診斷記錄 → 載入中⋯ | General → Diagnostic Logs → Loading… | `bridge:root=GENERAL_LINK&path=DIAGNOSTIC_LOG_BROWSER#Loading%E2%80%A6` | 26.2 | F26W |  |
| 一般 → 專注模式 → 使用iPhone設定 | General → Focus → Mirror my iPhone | `bridge:root=GENERAL_LINK&path=FOCUS_ID#Mirror%20my%20iPhone` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 一般 → 手錶方向 → 左手 | General → Watch Orientation → Left Wrist | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION#LEFT_HAND_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 手錶方向 → 數位錶冠在左側 | General → Watch Orientation → Digital Crown on Left Side | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION#LISA_ON_LEFT_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 手錶方向 → 數位錶冠在右側 | General → Watch Orientation → Digital Crown on Right Side | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION#LISA_ON_RIGHT_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 手錶方向 → 右手 | General → Watch Orientation → Right Wrist | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION#RIGHT_HAND_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 手錶方向 → 將Apple Watch戴在 | General → Watch Orientation → Wear Apple Watch on | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION#WRIST_CHOICE_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 手錶方向 → 左手 | General → Watch Orientation → Left Wrist | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION_ID#LEFT_HAND_ID` | 26.2 | F26W |  |
| 一般 → 手錶方向 → 數位錶冠在左側 | General → Watch Orientation → Digital Crown on Left Side | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION_ID#LISA_ON_LEFT_ID` | 26.2 | F26W |  |
| 一般 → 手錶方向 → 數位錶冠在右側 | General → Watch Orientation → Digital Crown on Right Side | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION_ID#LISA_ON_RIGHT_ID` | 26.2 | F26W |  |
| 一般 → 手錶方向 → 右手 | General → Watch Orientation → Right Wrist | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION_ID#RIGHT_HAND_ID` | 26.2 | F26W |  |
| 一般 → 手錶方向 → 將Apple Watch戴在 | General → Watch Orientation → Wear Apple Watch on | `bridge:root=GENERAL_LINK&path=GIZMO_ORIENTATION_ID#WRIST_CHOICE_ID` | 26.2 | F26W |  |
| 一般 → 語言與地區 → 自訂 | General → Language & Region → Custom | `bridge:root=GENERAL_LINK&path=LANGUAGE_AND_REGION#CUSTOM_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 語言與地區 → 使用iPhone設定 | General → Language & Region → Mirror my iPhone | `bridge:root=GENERAL_LINK&path=LANGUAGE_AND_REGION#MIRROR_MY_COMPANION_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 一般 → 語言與地區 → 自訂 | General → Language & Region → Custom | `bridge:root=GENERAL_LINK&path=LANGUAGE_AND_REGION_ID#CUSTOM_ID` | 26.2 | F26W |  |
| 一般 → 語言與地區 → 使用iPhone設定 | General → Language & Region → Mirror my iPhone | `bridge:root=GENERAL_LINK&path=LANGUAGE_AND_REGION_ID#MIRROR_MY_COMPANION_ID` | 26.2 | F26W |  |
| 一般 → 返回錶面 → APP | General → RETURN TO CLOCK → APPS | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK#APP_GROUP_ID` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 返回錶面 → 返回錶面 | General → RETURN TO CLOCK → RETURN TO CLOCK | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK#CSLPRFReturnToClockGroupID` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 返回錶面 → 1小時後 | General → RETURN TO CLOCK → After 1 hour | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK#RETURN_TO_CLOCK_AFTER_1_HOUR` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 返回錶面 → 2分鐘後 | General → RETURN TO CLOCK → After 2 minutes | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK#RETURN_TO_CLOCK_AFTER_2_MINUTES` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 返回錶面 → 永遠 | General → RETURN TO CLOCK → Always | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK#RETURN_TO_CLOCK_ALWAYS` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 返回錶面 → APP | General → RETURN TO CLOCK → APPS | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK_ID#APP_GROUP_ID` | 26.2 | F26W |  |
| 一般 → 返回錶面 → 返回錶面 | General → RETURN TO CLOCK → RETURN TO CLOCK | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK_ID#CSLPRFReturnToClockGroupID` | 26.2 | F26W |  |
| 一般 → 返回錶面 → 1小時後 | General → RETURN TO CLOCK → After 1 hour | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK_ID#RETURN_TO_CLOCK_AFTER_1_HOUR` | 26.2 | F26W |  |
| 一般 → 返回錶面 → 2分鐘後 | General → RETURN TO CLOCK → After 2 minutes | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK_ID#RETURN_TO_CLOCK_AFTER_2_MINUTES` | 26.2 | F26W |  |
| 一般 → 返回錶面 → 永遠 | General → RETURN TO CLOCK → Always | `bridge:root=GENERAL_LINK&path=RETURN_TO_CLOCK_ID#RETURN_TO_CLOCK_ALWAYS` | 26.2 | F26W |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#ALWAYS_SHOW_WATCH_FACE_NO_STICKINESS_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#APP_STICKINESS_GROUP_ID` | — | MAN |  |
| 一般 → Wake Screen → 播放中 | General → Wake Screen → Now Playing | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#AUTO_LAUNCH_MEDIA` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#LONG_WAKE_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#ON_TAP_GROUP_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#ONE_HOUR_WINDOW_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#SHORT_WAKE_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#TINY_WINDOW_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#TWO_MINUTE_WINDOW_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#WAKE_SCREEN_ON_CROWN_UP_SWITCH_ID` | — | MAN |  |
| — | — | `bridge:root=GENERAL_LINK&path=WAKE_SCREEN#WAKE_SCREEN_ON_WRIST_RAISE_SWITCH_ID` | — | MAN |  |
| — | — | `bridge:tab=SETTINGS&root=GENERAL_LINK&path=ManagedConfigurationList/InstallRequested` | — | MAN DYLD |  |
| 一般 → 關於本機 → 有限保固 → 聊天與電話支援 | General → About → Limited Warranty → Chat & Phone Support | `bridge:root=GENERAL_LINK&path=ABOUT/WARRANTY_DESCRIPTION#Chat%20&%20Phone%20Support` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 關於本機 → 有限保固 → 保固範圍詳細資訊 | General → About → Limited Warranty → COVERAGE DETAILS | `bridge:root=GENERAL_LINK&path=ABOUT/WARRANTY_DESCRIPTION#COVERAGE%20DETAILS` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 關於本機 → 有限保固 → 硬體保固範圍 | General → About → Limited Warranty → Hardware Coverage | `bridge:root=GENERAL_LINK&path=ABOUT/WARRANTY_DESCRIPTION#Hardware%20Coverage` | 16.2 · 18.7 | F18W F16W |  |
| 一般 → 關於本機 → 有限保固 → 有限保固 | General → About → Limited Warranty → Limited Warranty | `bridge:root=GENERAL_LINK&path=ABOUT/WARRANTY_DESCRIPTION#Limited%20Warranty` | 16.2 · 18.7 | F18W F16W |  |

### watchOS bridge: Gestures

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 手勢 | Gestures | `bridge:root=ELTON_SETTINGS_ID` | 26.2 | F26W |  |
| 手勢 → 點兩下 | Gestures → Double Tap | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID` | 26.2 | F26W |  |
| 手勢 → 蓋住螢幕靜音 | Gestures → Cover to Mute | `bridge:root=ELTON_SETTINGS_ID#Cover%20to%20Mute` | 26.2 | F26W |  |
| 手勢 → 手勢 | Gestures → Gestures | `bridge:root=ELTON_SETTINGS_ID#Gestures` | 26.2 | F26W |  |
| 手勢 → 翻轉手腕 | Gestures → Wrist Flick | `bridge:root=ELTON_SETTINGS_ID#Wrist%20Flick` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 點兩下 | Gestures → Double Tap → Double Tap | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#Double%20Tap` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 忽略「互點兩下」 | Gestures → Double Tap → Ignore Double Tap | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#ignoreDoubleTap` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 使用Apple Vision Pro時 | Gestures → Double Tap → When using Apple Vision Pro | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#ignoreWhileVisionProDonned` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 播放 | Gestures → Double Tap → Playback | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#playbackSettingsGroup` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 播放/暫停 | Gestures → Double Tap → Play / Pause | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#playbackSettingsPlayPause` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 略過 | Gestures → Double Tap → Skip | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#playbackSettingsSkip` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 智慧型堆疊 | Gestures → Double Tap → Smart Stack | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#smartStackGroup` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 前進 | Gestures → Double Tap → Advance | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#smartStackSettingsAdvance` | 26.2 | F26W |  |
| 手勢 → 點兩下 → 選取 | Gestures → Double Tap → Select | `bridge:root=ELTON_SETTINGS_ID&path=ELTON_DOUBLE_TAP_ID#smartStackSettingsSelect` | 26.2 | F26W |  |

### watchOS bridge: Handwashing

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 洗手 | Handwashing | `bridge:root=com.apple.BrookBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 洗手 → 通知分類 | Handwashing → Notification Grouping | `bridge:root=com.apple.BrookBridgeSettings&path=NOTIFICATION_COALESCING_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 洗手 → 允許通知 | Handwashing → Allow Notifications | `bridge:root=com.apple.BrookBridgeSettings#ALLOW_NOTIFICATIONS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 洗手 → 洗手計時器 | Handwashing → Handwashing Timer | `bridge:root=com.apple.BrookBridgeSettings#HANDWASHING_TIMER_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 洗手 → 關閉通知 | Handwashing → Notifications Off | `bridge:root=com.apple.BrookBridgeSettings#NOTIFICATIONS_OFF_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 洗手 → 傳送到通知中心 | Handwashing → Send to Notification Center | `bridge:root=com.apple.BrookBridgeSettings#SEND_TO_NOTIFICATION_CENTER_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Health

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 健康 | Health | `bridge:root=com.apple.BridgeHealthSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Heart

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 心臟 | Heart | `bridge:root=com.apple.HeartRateSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_BRADYCARDIA_ID` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=NOTIFICATION_COALESCING_ID` | — | MAN |  |
| 心臟 → 心臟 | Heart → Heart | `bridge:root=com.apple.HeartRateSettings#1` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 心臟 → 心率通知 | Heart → Heart Rate Notifications | `bridge:root=com.apple.HeartRateSettings#2` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 心臟 → 高心率 | Heart → High Heart Rate | `bridge:root=com.apple.HeartRateSettings#3` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 心臟 → 低心率 | Heart → Low Heart Rate | `bridge:root=com.apple.HeartRateSettings#4` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 心臟 → 心律不整 | Heart → Irregular Rhythm | `bridge:root=com.apple.HeartRateSettings#5` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 心臟 → 在「健康」中檢視記錄的心電圖 | Heart → View Recorded ECGs in Health | `bridge:root=com.apple.HeartRateSettings#6` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 心臟 → 心電圖 | Heart → ECG | `bridge:root=com.apple.HeartRateSettings#7` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.HeartRateSettings#ATRIAL_FIBRILLATION_GROUP_ID` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings#ATRIAL_FIBRILLATION_HEALTH_ROOM_BUTTON` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings#ELECTROCARDIOGRAM_GROUP_ID` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings#ELECTROCARDIOGRAM_HEALTH_ROOM_BUTTON` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_BRADYCARDIA_ID#ID_BPM_40` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_BRADYCARDIA_ID#ID_BPM_45` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_BRADYCARDIA_ID#ID_BPM_50` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_BRADYCARDIA_ID#OFF` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#ID_BPM_100` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#ID_BPM_110` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#ID_BPM_120` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#ID_BPM_130` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#ID_BPM_140` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#ID_BPM_150` | — | MAN |  |
| — | — | `bridge:root=com.apple.HeartRateSettings&path=HEART_NOTIFICATION_TACHYCARDIA_ID#OFF` | — | MAN |  |

### watchOS bridge: Mail

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 郵件 | Mail | `bridge:root=com.apple.NanoMailBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 帳號 | Mail → Accounts | `bridge:root=com.apple.NanoMailBridgeSettings&path=Accounts` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 預設回覆 | Mail → Default Replies | `bridge:root=com.apple.NanoMailBridgeSettings&path=Default%20Replies` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 包含郵件 | Mail → Include Mail | `bridge:root=com.apple.NanoMailBridgeSettings&path=Include%20Mail` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 預覽郵件 | Mail → Message Preview | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 簽名檔 | Mail → Signature | `bridge:root=com.apple.NanoMailBridgeSettings&path=Signature` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 自訂 | Mail → Custom | `bridge:root=com.apple.NanoMailBridgeSettings#CUSTOM_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 郵件設定 | Mail → Mail Settings | `bridge:root=com.apple.NanoMailBridgeSettings#Mail%20Settings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 使用iPhone設定 | Mail → Mirror my iPhone | `bridge:root=com.apple.NanoMailBridgeSettings#MIRROR_MY_COMPANION_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 預設回覆 → 加入回覆⋯ | Mail → Default Replies → Add reply… | `bridge:root=com.apple.NanoMailBridgeSettings&path=Default%20Replies#Add%20reply%E2%80%A6` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 預設回覆 → 預設回覆 | Mail → Default Replies → Default Replies | `bridge:root=com.apple.NanoMailBridgeSettings&path=Default%20Replies#Default%20Replies` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 郵件 → 預覽郵件 → 無 | Mail → Message Preview → None | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview#0` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件 → 預覽郵件 → 1行 | Mail → Message Preview → 1 Line | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview#1` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview#1%20Line` | — | MAN |  |
| 郵件 → 預覽郵件 → 2行 | Mail → Message Preview → 2 Lines | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview#2` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview#2%20Lines` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoMailBridgeSettings&path=Message%20Preview#None` | — | MAN |  |

### watchOS bridge: Mail & Calendar

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 郵件與行事曆 | Mail & Calendar | `bridge:root=com.apple.BridgeRemoteAccounts` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 擷取 | Mail & Calendar → Fetch | `bridge:root=com.apple.BridgeRemoteAccounts&path=Fetch` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 帳號 | Mail & Calendar → Accounts | `bridge:root=com.apple.BridgeRemoteAccounts#Accounts` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 加入Google帳號⋯ | Mail & Calendar → Add Google Account... | `bridge:root=com.apple.BridgeRemoteAccounts#ADD_GOOGLE_ACCOUNT` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 擷取 → 15分鐘 | Mail & Calendar → Fetch → 15 min | `bridge:root=com.apple.BridgeRemoteAccounts&path=Fetch#15%20min` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 擷取 → 30分鐘 | Mail & Calendar → Fetch → 30 min | `bridge:root=com.apple.BridgeRemoteAccounts&path=Fetch#30%20min` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 擷取 → 每小時 | Mail & Calendar → Fetch → Hourly | `bridge:root=com.apple.BridgeRemoteAccounts&path=Fetch#Hourly` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 郵件與行事曆 → 擷取 → 關閉 | Mail & Calendar → Fetch → Off | `bridge:root=com.apple.BridgeRemoteAccounts&path=Fetch#Off` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Messages

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 訊息 | Messages | `bridge:root=com.apple.MessagesBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 傳送讀取回條 | Send Read Receipts | `bridge:root=com.apple.MessagesBridgeSettings%23READ_RECEIPTS` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 語音訊息 | Messages → Audio Messages | `bridge:root=com.apple.MessagesBridgeSettings&path=AudioMessagesMode` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 預設回覆 | Messages → Default Replies | `bridge:root=com.apple.MessagesBridgeSettings&path=DEFAULT_REPLIES` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=com.apple.MessagesBridgeSettings&path=DictatedMessagesMode` | — | MAN |  |
| 訊息 → 重複提示 | Messages → Repeat Alerts | `bridge:root=com.apple.MessagesBridgeSettings&path=PLAY_ALERT_TONE` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 自訂 | Messages → Custom | `bridge:root=com.apple.MessagesBridgeSettings#CUSTOM_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 使用iPhone設定 | Messages → Mirror my iPhone | `bridge:root=com.apple.MessagesBridgeSettings#MIRROR_MY_COMPANION_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 預設回覆 → 加入回覆⋯ | Messages → Default Replies → Add reply… | `bridge:root=com.apple.MessagesBridgeSettings&path=DEFAULT_REPLIES#Add%20reply%E2%80%A6` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 預設回覆 → 預設回覆 | Messages → Default Replies → Default Replies | `bridge:root=com.apple.MessagesBridgeSettings&path=DEFAULT_REPLIES#Default%20Replies` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 訊息 → 預設回覆 → 智慧型回覆 | Messages → Default Replies → Smart Replies | `bridge:root=com.apple.MessagesBridgeSettings&path=DEFAULT_REPLIES#Smart%20Replies` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=com.apple.MessagesBridgeSettings&path=DictatedMessagesMode#Audio` | — | MAN |  |
| — | — | `bridge:root=com.apple.MessagesBridgeSettings&path=DictatedMessagesMode#Transcript` | — | MAN |  |
| — | — | `bridge:root=com.apple.MessagesBridgeSettings&path=DictatedMessagesMode#Transcript%20or%20Audio` | — | MAN |  |

### watchOS bridge: Mindfulness

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 正念 | Mindfulness | `bridge:root=com.apple.MindSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 | Mindfulness → Breath Rate | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 觸覺回饋 | Mindfulness → Haptics | `bridge:root=com.apple.MindSettings&path=MIND_HAPTICS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 加入提醒事項⋯ | Mindfulness → Add Reminder… | `bridge:root=com.apple.MindSettings#Add%20Reminder%E2%80%A6` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 允許通知 | Mindfulness → Allow Notifications | `bridge:root=com.apple.MindSettings#ALLOW_NOTIFICATIONS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 當天結束 | Mindfulness → End of Day | `bridge:root=com.apple.MindSettings#MIND_END_OF_DAY_REMINDER` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 正念提醒 | Mindfulness → Mindfulness Reminders | `bridge:root=com.apple.MindSettings#MIND_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 今天不再提醒 | Mindfulness → Mute for today | `bridge:root=com.apple.MindSettings#MIND_MUTE_FOR_TODAY_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 一天開始 | Mindfulness → Start of Day | `bridge:root=com.apple.MindSettings#MIND_START_OF_DAY_REMINDER` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 每週摘要 | Mindfulness → Weekly Summary | `bridge:root=com.apple.MindSettings#MIND_WEEKLY_SUMMARY_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 關閉通知 | Mindfulness → Notifications Off | `bridge:root=com.apple.MindSettings#NOTIFICATIONS_OFF_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 傳送到通知中心 | Mindfulness → Send to Notification Center | `bridge:root=com.apple.MindSettings#SEND_TO_NOTIFICATION_CENTER_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸10次 | Mindfulness → Breath Rate → 10 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_10` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸4次 | Mindfulness → Breath Rate → 4 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_4` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸5次 | Mindfulness → Breath Rate → 5 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_5` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸6次 | Mindfulness → Breath Rate → 6 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_6` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸7次 | Mindfulness → Breath Rate → 7 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_7` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸8次 | Mindfulness → Breath Rate → 8 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_8` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 呼吸速率 → 每分鐘呼吸9次 | Mindfulness → Breath Rate → 9 breaths per minute | `bridge:root=com.apple.MindSettings&path=MIND_BREATHE_RATE_ID#ID_BPM_9` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 觸覺回饋 → 弱 | Mindfulness → Haptics → Minimal | `bridge:root=com.apple.MindSettings&path=MIND_HAPTICS_ID#MINIMAL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 觸覺回饋 → 無 | Mindfulness → Haptics → None | `bridge:root=com.apple.MindSettings&path=MIND_HAPTICS_ID#NONE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 正念 → 觸覺回饋 → 強 | Mindfulness → Haptics → Prominent | `bridge:root=com.apple.MindSettings&path=MIND_HAPTICS_ID#PROMINENT_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Nike Run Club

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Nike Run Club | Nike Run Club | `bridge:root=VICTORY_ROW_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| Nike Run Club → 在Apple Watch上顯示App | Nike Run Club → Show App on Apple Watch | `bridge:root=VICTORY_ROW_ID#SHOWS_ON_GIZMO` | 26.2 | F26W |  |

### watchOS bridge: Noise

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 噪音 | Noise | `bridge:root=com.apple.Noise.settings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| 噪音 → 噪音臨界值 | Noise → Noise Threshold | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 通知分類 | Noise → Notification Grouping | `bridge:root=com.apple.Noise.settings&path=NOTIFICATION_COALESCING_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 環境聲音測量 | Noise → Environmental Sound Measurements | `bridge:root=com.apple.Noise.settings#ENABLE_MEASUREMENTS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音通知 | Noise → Noise Notifications | `bridge:root=com.apple.Noise.settings#LOUD_NOTIFICATION_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音臨界值 → 100分貝 | Noise → Noise Threshold → 100 decibels | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID#ID_BPM_100` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音臨界值 → 80分貝 | Noise → Noise Threshold → 80 decibels | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID#ID_BPM_80` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音臨界值 → 85分貝 | Noise → Noise Threshold → 85 decibels | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID#ID_BPM_85` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音臨界值 → 90分貝 | Noise → Noise Threshold → 90 decibels | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID#ID_BPM_90` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音臨界值 → 95分貝 | Noise → Noise Threshold → 95 decibels | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID#ID_BPM_95` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 噪音 → 噪音臨界值 → 關閉 | Noise → Noise Threshold → Off | `bridge:root=com.apple.Noise.settings&path=LOUD_NOTIFICATION_ID#OFF` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: NOTIFICATIONS_ID

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `bridge:root=NOTIFICATIONS_ID&path=com.apple.HeartRateSettings` | — | MAN DYLD |  |

### watchOS bridge: Phone

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 電話 | Phone | `bridge:root=com.apple.PhoneBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 電話 → 通話 | Phone → Calls | `bridge:root=com.apple.PhoneBridgeSettings#carrier_direct_calling_group_id` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 電話 → 觸覺回饋 | Phone → Haptic | `bridge:root=com.apple.PhoneBridgeSettings#INCOMING_CALL_HAPTIC` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 電話 → 聲音 | Phone → Sound | `bridge:root=com.apple.PhoneBridgeSettings#INCOMING_CALL_SOUND` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 電話 → 鈴聲 | Phone → Ringtone | `bridge:root=com.apple.PhoneBridgeSettings#RINGTONE` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Photos

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 照片 | Photos | `bridge:root=com.apple.NanoPhotosBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 照片 → 照片上限 | Photos → Photos Limit | `bridge:root=com.apple.NanoPhotosBridgeSettings&path=Photos%20Limit` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 照片 → 同步相簿 | Photos → Sync Album | `bridge:root=com.apple.NanoPhotosBridgeSettings&path=Sync%20Album` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.NanoPhotosBridgeSettings&path=Synced%20Album` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPhotosBridgeSettings#2` | — | MAN |  |
| 照片 → 相簿 | Photos → Album | `bridge:root=com.apple.NanoPhotosBridgeSettings#Album` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.NanoPhotosBridgeSettings#App%20Settings` | — | MAN |  |
| 照片 → 自訂 | Photos → Custom | `bridge:root=com.apple.NanoPhotosBridgeSettings#CUSTOM_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 照片 → 精選照片 | Photos → Featured Photos | `bridge:root=com.apple.NanoPhotosBridgeSettings#Featured%20Photos` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 照片 → 回憶 | Photos → Memories | `bridge:root=com.apple.NanoPhotosBridgeSettings#Memories` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 照片 → 使用iPhone設定 | Photos → Mirror my iPhone | `bridge:root=com.apple.NanoPhotosBridgeSettings#MIRROR_MY_COMPANION_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 照片 → 通知設定 | Photos → Notification Settings | `bridge:root=com.apple.NanoPhotosBridgeSettings#MIRROR_RADIO_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 照片 → 照片同步 | Photos → Photo Syncing | `bridge:root=com.apple.NanoPhotosBridgeSettings#Photo%20Syncing` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 照片 → 同步精選照片 | Photos → Sync Featured Photos | `bridge:root=com.apple.NanoPhotosBridgeSettings#Sync%20Featured%20Photos` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 照片 → 同步回憶 | Photos → Sync Memories | `bridge:root=com.apple.NanoPhotosBridgeSettings#Sync%20Memories` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Podcasts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Podcast | Podcasts | `bridge:root=com.apple.private.PodcastsBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Privacy

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 隱私權 | Privacy | `bridge:root=PRIVACY_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| 隱私權 → 耳機音效測量 | Privacy → Headphone Audio Measurements | `bridge:root=PRIVACY_ID&path=HeadphoneAudio` | 16.2 · 18.7 | F18W F16W MAN DYLD |  |
| 隱私權 → 環境聲音測量 | Privacy → Environmental Sound Measurements | `bridge:root=PRIVACY_ID#ENVIRONMENTAL_AUDIO_ENABLED_SWITCH_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| 隱私權 → 體能追蹤 | Privacy → Fitness Tracking | `bridge:root=PRIVACY_ID#FITNESS_TRACKING_ENABLED_LABEL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 隱私權 → 心率 | Privacy → Heart Rate | `bridge:root=PRIVACY_ID#HEART_RATE_ENABLED_LABEL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 隱私權 → 血氧濃度測量 | Privacy → Blood Oxygen Measurements | `bridge:root=PRIVACY_ID#OXYGEN_SATURATION_ENABLED_SWITCH_ID` | 16.2 · 18.7 | F18W F16W |  |
| — | — | `bridge:root=PRIVACY_ID#Privacy%20Settings` | — | MAN |  |
| 隱私權 → 重置健身校正資料 | Privacy → Reset Fitness Calibration Data | `bridge:root=PRIVACY_ID#RESET_MOTION_CALIBRATION_LABEL` | 16.2 · 18.7 | F18W F16W MAN |  |
| 隱私權 → 呼吸速率 | Privacy → Respiratory Rate | `bridge:root=PRIVACY_ID#RESPIRATORY_RATE_LABEL` | 16.2 · 18.7 | F18W F16W |  |
| 隱私權 → 手腕溫度 | Privacy → Wrist Temperature | `bridge:root=PRIVACY_ID#WRIST_TEMPERATURE_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 隱私權 → 耳機音效測量 → 保留8天 | Privacy → Headphone Audio Measurements → For 8-Days | `bridge:root=PRIVACY_ID&path=HeadphoneAudio#FOR_EIGHT_DAYS_CELL` | 16.2 · 18.7 | F18W F16W |  |
| — | — | `bridge:root=PRIVACY_ID&path=HeadphoneAudio#MEASURE_LEVELS_SWITCH` | — | MAN |  |
| — | — | `bridge:root=PRIVACY_ID&path=HeadphoneAudio#OTHER_HEADPHONES_SWITCH` | — | MAN |  |
| 隱私權 → 耳機音效測量 → 在「健康」中儲存 | Privacy → Headphone Audio Measurements → Save In Health | `bridge:root=PRIVACY_ID&path=HeadphoneAudio#SAVE_IN_HEALTH_GROUP` | 16.2 · 18.7 | F18W F16W |  |
| 隱私權 → 耳機音效測量 → 保留直到刪除為止 | Privacy → Headphone Audio Measurements → Until I Delete | `bridge:root=PRIVACY_ID&path=HeadphoneAudio#UNTIL_I_DELETE_CELL` | 16.2 · 18.7 | F18W F16W |  |

### watchOS bridge: ROOT

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| — | — | `bridge:root=ROOT#Available%20Apps` | — | MAN |  |
| — | — | `bridge:root=ROOT#Installed%20On%20Apple%20Watch` | — | MAN |  |

### watchOS bridge: Schooltime

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 上課時間 | Schooltime | `bridge:root=SCHOOLTIME` | 26.2 | F26W |  |
| 上課時間 → 上課時間 | Schooltime → Schooltime | `bridge:root=SCHOOLTIME#SCHEDULE_FEATURE_ACTIVE_TITLE` | 26.2 | F26W |  |

### watchOS bridge: Screen Time

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 螢幕使用時間 | Screen Time | `bridge:root=SCREEN_TIME_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Selected Photo Album

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 所選的相簿 \| 照片上限 | Photos Limit \| Selected Photo Album | `bridge:root=com.apple.mobileslideshow` | 18.7 · 26.2 | F26W F18W MAN |  |

### watchOS bridge: Siri

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Siri | Siri | `bridge:root=SIRI_WATCH_SETTINGS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → Siri回應 | Siri → Siri Responses | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID` | 26.2 | F26W |  |
| Siri → 語音回饋 | Siri → Voice Feedback | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_FEEDBACK_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → 聆聽 | Siri → Listen for | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_TRIGGER_ID` | 26.2 | F26W |  |
| Siri → 跟Siri對話 | Siri → Ask Siri | `bridge:root=SIRI_WATCH_SETTINGS_ID#ASK_SIRI_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| Siri → Siri建議 | Siri → Siri Suggestions | `bridge:root=SIRI_WATCH_SETTINGS_ID#ASSISTANT_SUGGESTIONS_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| Siri → 自動傳送訊息 | Siri → Automatically Send Messages | `bridge:root=SIRI_WATCH_SETTINGS_ID#AUTOMATICALLY_SEND_MESSAGES_SWITCH_ID` | 26.2 | F26W |  |
| Siri → 按下數位錶冠 | Siri → Press Digital Crown | `bridge:root=SIRI_WATCH_SETTINGS_ID#DIGITAL_CROWN_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → Siri | Siri → Siri | `bridge:root=SIRI_WATCH_SETTINGS_ID#HEY_SIRI_SWITCH_ID` | 16.2 · 18.7 | F18W F16W MAN |  |
| Siri → 抬起說話 | Siri → Raise to Speak | `bridge:root=SIRI_WATCH_SETTINGS_ID#RAISE_TO_SPEAK_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → 音量 | Siri → Voice Volume | `bridge:root=SIRI_WATCH_SETTINGS_ID#VOICE_VOLUME_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → Siri回應 → 永遠顯示Siri字幕 | Siri → Siri Responses → Always Show Siri Captions | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID#ALWAYS_SHOW_SIRI_CAPTIONS_SWITCH_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 永遠顯示語音 | Siri → Siri Responses → Always Show Speech | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID#ALWAYS_SHOW_SPEECH_SWITCH_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 音量 | Siri → Siri Responses → Voice Volume | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID#CONSIDERATE_VOLUME_GROUP_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 自動調整音量 | Siri → Siri Responses → Automatically Adjust Volume | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID#CONSIDERATE_VOLUME_SWITCH_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 音量 | Siri → Siri Responses → Level | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID/CONSIDERATE_VOLUME_PROFILE_ID` | 26.2 | F26W |  |
| Siri → 語音回饋 → 永遠開啟 | Siri → Voice Feedback → Always On | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_FEEDBACK_ID#VOICE_FEEDBACK_ALWAYS_ON_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → 語音回饋 → 以「靜音模式」控制 | Siri → Voice Feedback → Control With Silent Mode | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_FEEDBACK_ID#VOICE_FEEDBACK_CONTROL_WITH_SILENT_MODE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → 語音回饋 → 只限耳機 | Siri → Voice Feedback → Headphones Only | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_FEEDBACK_ID#VOICE_FEEDBACK_HEADPHONES_ONLY_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri → 聆聽 → 「嘿Siri」 | Siri → Listen for → “Hey Siri” | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_TRIGGER_ID#HEY_SIRI_ID` | 26.2 | F26W |  |
| Siri → 聆聽 → 「Siri」或「嘿Siri」 | Siri → Listen for → “Siri” or “Hey Siri” | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_TRIGGER_ID#HS_JS_ID` | 26.2 | F26W |  |
| Siri → 聆聽 → 關閉 | Siri → Listen for → Off | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=VOICE_TRIGGER_ID#VOICE_TRIGGER_DISABLED_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 音量 → 預設值 | Siri → Siri Responses → Level → Default | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID/CONSIDERATE_VOLUME_PROFILE_ID#CONSIDERATE_VOLUME_PROFILE_DEFAULT_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 音量 → 音量較大 | Siri → Siri Responses → Level → Louder | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID/CONSIDERATE_VOLUME_PROFILE_ID#CONSIDERATE_VOLUME_PROFILE_LOUDER_ID` | 26.2 | F26W |  |
| Siri → Siri回應 → 音量 → 音量較小 | Siri → Siri Responses → Level → Quieter | `bridge:root=SIRI_WATCH_SETTINGS_ID&path=SIRI_RESPONSES_ID/CONSIDERATE_VOLUME_PROFILE_ID#CONSIDERATE_VOLUME_PROFILE_QUIETER_ID` | 26.2 | F26W |  |

### watchOS bridge: Sleep

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 睡眠 | Sleep | `bridge:root=com.apple.NanoBedtimeBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| 睡眠 → 在「健康」App中設定「睡眠」 | Sleep → Set Up Sleep in Health App | `bridge:root=com.apple.NanoBedtimeBridgeSettings#SET_UP_SLEEP_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Smart Stack

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 智慧型堆疊 | Smart Stack | `bridge:root=SMARTSTACK_LINK` | 18.7 · 26.2 | F26W F18W |  |

### watchOS bridge: Sounds & Haptics

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 音效與觸覺回饋 | Sounds & Haptics | `bridge:root=SOUNDS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 音量 | Sounds & Haptics → Level | `bridge:root=SOUNDS_ID&path=contextual_volume_profile` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 觸覺回饋 | Sounds & Haptics → Haptics | `bridge:root=SOUNDS_ID&path=HAPTICS_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 耳機安全性 | Sounds & Haptics → Headphone Safety | `bridge:root=SOUNDS_ID&path=HEADPHONE_LEVEL_LIMIT_SETTING` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 行事曆提示 | Sounds & Haptics → Calendar Alerts | `bridge:root=SOUNDS_ID&path=SOUND_AND_HAPTIC_PATTERNS_CALENDARALERTS_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 預設提示 | Sounds & Haptics → Default Alerts | `bridge:root=SOUNDS_ID&path=SOUND_AND_HAPTIC_PATTERNS_DEFAULTALERTS_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 收到新郵件 | Sounds & Haptics → New Mail | `bridge:root=SOUNDS_ID&path=SOUND_AND_HAPTIC_PATTERNS_NEWMAIL_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 提醒事項提示 | Sounds & Haptics → Reminder Alerts | `bridge:root=SOUNDS_ID&path=SOUND_AND_HAPTIC_PATTERNS_REMINDERALERTS_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 鈴聲 | Sounds & Haptics → Ringtone | `bridge:root=SOUNDS_ID&path=SOUND_AND_HAPTIC_PATTERNS_RINGTONE_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 訊息聲 | Sounds & Haptics → Text Tone | `bridge:root=SOUNDS_ID&path=SOUND_AND_HAPTIC_PATTERNS_TEXTTONE_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 靜音模式 | Sounds & Haptics → Silent Mode | `bridge:root=SOUNDS_ID#audio_mute_switch` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 提示聲音量 | Sounds & Haptics → Alert Volume | `bridge:root=SOUNDS_ID#AUDIO_SLIDER` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 自動調整音量 | Sounds & Haptics → Automatically Adjust Volume | `bridge:root=SOUNDS_ID#contextual_volume_switch` | 26.2 | F26W |  |
| 聲音與觸覺回饋 → 蓋住螢幕靜音 | Sounds & Haptics → Cover to Mute | `bridge:root=SOUNDS_ID#COVER_TO_MUTE` | 16.2 · 18.7 | F18W F16W MAN |  |
| 聲音與觸覺回饋 → 觸覺回饋提示 | Sounds & Haptics → Haptic Alerts | `bridge:root=SOUNDS_ID#Haptic%20Alerts` | 16.2 · 18.7 | F18W F16W MAN |  |
| 聲音與觸覺回饋 → 觸覺回饋 | Sounds & Haptics → Haptics | `bridge:root=SOUNDS_ID#Haptics` | 16.2 · 18.7 | F18W F16W MAN |  |
| 音效與觸覺回饋 → 耳機音訊 | Sounds & Haptics → Headphone Audio | `bridge:root=SOUNDS_ID#HEADPHONE_AUDIO_GROUP` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 系統聲音與觸覺回饋 | Sounds & Haptics → System Sounds & Haptics | `bridge:root=SOUNDS_ID#JACKRABBIT_GROUP_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 錶冠觸覺回饋 | Sounds & Haptics → Crown Haptics | `bridge:root=SOUNDS_ID#JACKRABBIT_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 鈴聲和提示聲 | Sounds & Haptics → Ringtone and Alerts | `bridge:root=SOUNDS_ID#RINGTONE_AND_ALERTS_SECTION_TITLE` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 系統觸覺回饋 | Sounds & Haptics → System Haptics | `bridge:root=SOUNDS_ID#SYSTEM_HAPTICS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 音效與觸覺回饋 → 音量 → 預設值 | Sounds & Haptics → Level → Default | `bridge:root=SOUNDS_ID&path=contextual_volume_profile#CONTEXTUAL_VOLUME_PROFILE_DEFAULT_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 音量 → 音量較大 | Sounds & Haptics → Level → Louder | `bridge:root=SOUNDS_ID&path=contextual_volume_profile#CONTEXTUAL_VOLUME_PROFILE_LOUDER_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 音量 → 音量較小 | Sounds & Haptics → Level → Quieter | `bridge:root=SOUNDS_ID&path=contextual_volume_profile#CONTEXTUAL_VOLUME_PROFILE_QUIETER_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 觸覺回饋 → 預設值 | Sounds & Haptics → Haptics → Default | `bridge:root=SOUNDS_ID&path=HAPTICS_ID#DEFAULT_ITEM_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 觸覺回饋 → 關閉 | Sounds & Haptics → Haptics → Off | `bridge:root=SOUNDS_ID&path=HAPTICS_ID#OFF_ITEM_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 觸覺回饋 → 強 | Sounds & Haptics → Haptics → Prominent | `bridge:root=SOUNDS_ID&path=HAPTICS_ID#PROMINENT_ITEM_ID` | 26.2 | F26W |  |
| 音效與觸覺回饋 → 耳機安全性 → 降低高音量 | Sounds & Haptics → Headphone Safety → Reduce Loud Sounds | `bridge:root=SOUNDS_ID&path=HEADPHONE_LEVEL_LIMIT_SETTING#COSHeadphoneLevelLimitSwitchKey` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 音效與觸覺回饋 → 耳機安全性 → 耳機通知 | Sounds & Haptics → Headphone Safety → Headphone Notifications | `bridge:root=SOUNDS_ID&path=HEADPHONE_LEVEL_LIMIT_SETTING#COSHeadphoneNotificationsSwitchKey` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Stocks

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 | Stocks | `bridge:root=com.apple.StocksBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=com.apple.StocksBridgeSettings&path=Default%20Stock` | — | MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 所選的股票 | Stocks → Selected Stock | `bridge:root=com.apple.StocksBridgeSettings&path=Selected%20Stock` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 錶面複雜功能顯示 | Stocks → Clock Face Complication Shows | `bridge:root=com.apple.StocksBridgeSettings#Clock%20Face%20Complication%20Shows` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.StocksBridgeSettings#CLOCK%20FACE%20COMPLICATION%20SHOWS%3A` | — | MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 目前價格 | Stocks → Current Price | `bridge:root=com.apple.StocksBridgeSettings#Current%20Price` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 市值 | Stocks → Market Cap | `bridge:root=com.apple.StocksBridgeSettings#Market%20Cap` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 漲跌幅 | Stocks → Percentage Change | `bridge:root=com.apple.StocksBridgeSettings#Percentage%20Change` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 漲跌 | Stocks → Points Change | `bridge:root=com.apple.StocksBridgeSettings#Points%20Change` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → Siri錶面顯示的股票報價 | Stocks → Siri Face Shows Quote For | `bridge:root=com.apple.StocksBridgeSettings#Siri%20Face%20Shows%20Quote%20For` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.StocksBridgeSettings&path=Default%20Stock#Default%20Stock` | — | MAN |  |
| — | — | `bridge:root=com.apple.StocksBridgeSettings&path=Default%20Stock#Last%20Viewed` | — | MAN |  |
| Siri卡片所選的股票 \| 市值 \| 漲跌 \| 漲跌幅 \| 目前價格 \| 股市 → 所選的股票 → 所選的股票 | Stocks → Selected Stock → Selected Stock | `bridge:root=com.apple.StocksBridgeSettings&path=Selected%20Stock#Selected%20Stock` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Storage Limit

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 儲存空間上限 \| 同步的音樂 \| 音樂 | Music \| Storage Limit \| Synced Music | `bridge:root=com.apple.NanoMusicBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 儲存空間上限 \| 同步的音樂 \| 音樂 → 加入音樂⋯ | Music \| Storage Limit \| Synced Music → Add Music… | `bridge:root=com.apple.NanoMusicBridgeSettings#Add%20Music%E2%80%A6` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 儲存空間上限 \| 同步的音樂 \| 音樂 → 播放列表與專輯 | Music \| Storage Limit \| Synced Music → PLAYLISTS & ALBUMS | `bridge:root=com.apple.NanoMusicBridgeSettings#PLAYLISTS%20&%20ALBUMS` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Tips

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 提示 | Tips | `bridge:root=com.apple.NanoTipsBridgeSettings` | 26.2 | F26W |  |
| 提示 → 通知分類 | Tips → Notification Grouping | `bridge:root=com.apple.NanoTipsBridgeSettings&path=NOTIFICATION_COALESCING_ID` | 26.2 | F26W |  |
| 提示 → 允許通知 | Tips → Allow Notifications | `bridge:root=com.apple.NanoTipsBridgeSettings#ALLOW_NOTIFICATIONS_ID` | 26.2 | F26W |  |
| 提示 → 關閉通知 | Tips → Notifications Off | `bridge:root=com.apple.NanoTipsBridgeSettings#NOTIFICATIONS_OFF_ID` | 26.2 | F26W |  |
| 提示 → 傳送到通知中心 | Tips → Send to Notification Center | `bridge:root=com.apple.NanoTipsBridgeSettings#SEND_TO_NOTIFICATION_CENTER_ID` | 26.2 | F26W |  |

### watchOS bridge: Turn Alerts

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 地圖 \| 轉彎提示 | Maps \| Turn Alerts | `bridge:root=com.apple.NanoMapsBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 版號資訊 | Maps \| Turn Alerts → Build Info | `bridge:root=com.apple.NanoMapsBridgeSettings#Build%20Info%3A` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 自行車 | Maps \| Turn Alerts → Cycling | `bridge:root=com.apple.NanoMapsBridgeSettings#Cycling` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 地圖 \| 轉彎提示 → 開車 | Maps \| Turn Alerts → Driving | `bridge:root=com.apple.NanoMapsBridgeSettings#Driving` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 開車時啟用CarPlay | Maps \| Turn Alerts → Driving with CarPlay | `bridge:root=com.apple.NanoMapsBridgeSettings#Driving%20with%20CarPlay` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 顯示導航 | Maps \| Turn Alerts → Show Navigation | `bridge:root=com.apple.NanoMapsBridgeSettings#Show%20Navigation` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 大眾運輸 | Maps \| Turn Alerts → Transit | `bridge:root=com.apple.NanoMapsBridgeSettings#Transit` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 轉彎提示 | Maps \| Turn Alerts → Turn Alerts | `bridge:root=com.apple.NanoMapsBridgeSettings#Turn%20Alerts` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 地圖 \| 轉彎提示 → 步行 | Maps \| Turn Alerts → Walking | `bridge:root=com.apple.NanoMapsBridgeSettings#Walking` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Turn Passcode Off

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 | Turn Passcode Off | `bridge:root=PASSCODE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 透過iPhone解鎖 | Turn Passcode Off → Unlock with iPhone | `bridge:root=PASSCODE_ID#AUTO_UNLOCK_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 更改密碼 | Turn Passcode Off → Change Passcode | `bridge:root=PASSCODE_ID#CHANGE_PASSCODE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 清除資料 | Turn Passcode Off → Erase Data | `bridge:root=PASSCODE_ID#ERASE_DATA_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 複雜功能 | — | `bridge:root=PASSCODE_ID#SHOW_COMPLICATION_DATA_WHEN_LOCKED_GROUP_ID` | 26.2 | F26W |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 鎖定時顯示資料 | — | `bridge:root=PASSCODE_ID#SHOW_COMPLICATION_DATA_WHEN_LOCKED_SWITCH_ID` | 26.2 | F26W |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 簡易密碼 | Turn Passcode Off → Simple Passcode | `bridge:root=PASSCODE_ID#SIMPLE_PASSCODE_SWITCH_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 開啟密碼 | Turn Passcode Off → Turn Passcode On | `bridge:root=PASSCODE_ID#TOGGLE_PASSCODE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 密碼 \| 手腕偵測 \| 更改密碼 \| 清除資料 \| 簡易密碼 \| 透過iPhone解鎖 \| 開啟密碼 \| 關閉密碼 → 手腕偵測 | Turn Passcode Off → Wrist Detection | `bridge:root=PASSCODE_ID#WRIST_DETECTION_CELL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN DYLD |  |

### watchOS bridge: Walkie-Talkie

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 對講機 | Walkie-Talkie | `bridge:root=com.apple.tincan.settings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 對講機 → 通知分類 | Walkie-Talkie → Notification Grouping | `bridge:root=com.apple.tincan.settings&path=NOTIFICATION_COALESCING_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 對講機 → 允許通知 | Walkie-Talkie → Allow Notifications | `bridge:root=com.apple.tincan.settings#ALLOW_NOTIFICATIONS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 對講機 → 朋友 | Walkie-Talkie → Friends | `bridge:root=com.apple.tincan.settings#Friends` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 對講機 → 關閉通知 | Walkie-Talkie → Notifications Off | `bridge:root=com.apple.tincan.settings#NOTIFICATIONS_OFF_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 對講機 → 傳送到通知中心 | Walkie-Talkie → Send to Notification Center | `bridge:root=com.apple.tincan.settings#SEND_TO_NOTIFICATION_CENTER_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

### watchOS bridge: Wallet & Apple Pay

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 錢包與Apple Pay | Wallet & Apple Pay | `bridge:root=com.apple.NanoPassbookBridgeSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings&path=ADD_CARD` | — | MAN DYLD |  |
| 錢包與Apple Pay → 加入卡片 | Wallet & Apple Pay → Add Card | `bridge:root=com.apple.NanoPassbookBridgeSettings#Add%20Card` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 錢包與Apple Pay → Apple Cash | Wallet & Apple Pay → Apple Cash | `bridge:root=com.apple.NanoPassbookBridgeSettings#Apple%C2%A0Cash` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 錢包與Apple Pay → 自訂 | Wallet & Apple Pay → Custom | `bridge:root=com.apple.NanoPassbookBridgeSettings#CUSTOM_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 錢包與Apple Pay → 使用iPhone設定 | Wallet & Apple Pay → Mirror my iPhone | `bridge:root=com.apple.NanoPassbookBridgeSettings#MIRROR_MY_COMPANION_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 錢包與Apple Pay → 通知 | Wallet & Apple Pay → Notifications | `bridge:root=com.apple.NanoPassbookBridgeSettings#MIRROR_RADIO_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#PAYMENTS%20ON%20MAC` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#PKHandoffPaymentsDisabled` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#SETTINGS_DEFAULT_EXPRESS_TRANSIT_CELL_TITLE` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#SETTINGS_PAYMENT_CARDS_GROUP_PLURAL_WATCH` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#SETTINGS_TRANSACTION_DEFAULTS_EMAIL` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#SETTINGS_TRANSACTION_DEFAULTS_PAYMENT_CARD` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#SETTINGS_TRANSACTION_DEFAULTS_PHONE` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#SETTINGS_TRANSACTION_DEFAULTS_SHIPPING_ADDRESS` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#TRANSACTION%20DEFAULTS` | — | MAN |  |
| — | — | `bridge:root=com.apple.NanoPassbookBridgeSettings#TRANSIT%20CARDS` | — | MAN |  |

### watchOS bridge: Weather

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 天氣 | Weather | `bridge:root=com.apple.weatherbridgesettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 天氣 → 預設城市 | Weather → Default City | `bridge:root=com.apple.weatherbridgesettings&path=Default%20City` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 天氣 → 預設城市 → 目前位置 | Weather → Default City → Current Location | `bridge:root=com.apple.weatherbridgesettings&path=Default%20City#Current%20Location` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 天氣 → 預設城市 → 預設城市 | Weather → Default City → Default City | `bridge:root=com.apple.weatherbridgesettings&path=Default%20City#Default%20City` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |

### watchOS bridge: Workout

| 中文名稱 | English | URL | 系統檔驗證 | 來源 | 備註 |
| --- | --- | --- | --- | --- | --- |
| 體能訓練 | Workout | `bridge:root=com.apple.SessionTrackerAppSettings` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 自動暫停 | Workout → Auto-Pause | `bridge:root=com.apple.SessionTrackerAppSettings&path=AUTO_PAUSE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 體能訓練顯示畫面 | Workout → Workout View | `bridge:root=com.apple.SessionTrackerAppSettings&path=METRIC_VIEW_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.SessionTrackerAppSettings&path=METRIC_VIEW_LABEL` | — | MAN |  |
| 體能訓練 → 體能訓練播放列表 | Workout → Workout Playlist | `bridge:root=com.apple.SessionTrackerAppSettings&path=MUSIC_AUTOSTART_TITLE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 配速/速度顯示畫面 | Workout → Pace/Speed View | `bridge:root=com.apple.SessionTrackerAppSettings&path=PACE_VIEW_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 度量單位 | Workout → Units of Measure | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| — | — | `bridge:root=com.apple.SessionTrackerAppSettings#AUTO_PAUSE_ENABLED_LABEL` | — | MAN |  |
| 體能訓練 → 開始體能訓練提醒 | Workout → Start Workout Reminder | `bridge:root=com.apple.SessionTrackerAppSettings#AUTO_START_WORKOUT_NOTIFICATIONS_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 按下來暫停 | Workout → Press to Pause | `bridge:root=com.apple.SessionTrackerAppSettings#CHORD_PRESS_PAUSE_WORKOUT_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 結束體能訓練提醒 | Workout → End Workout Reminder | `bridge:root=com.apple.SessionTrackerAppSettings#END_REMINDERS_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 健走趣 | Workout → Time to Walk | `bridge:root=com.apple.SessionTrackerAppSettings#GUIDED_WORKOUT_PREFETCH_FOOTER_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 將新的體能訓練加入Apple Watch | Workout → Add New Workouts to Watch | `bridge:root=com.apple.SessionTrackerAppSettings#GUIDED_WORKOUT_PREFETCH_LABEL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 低耗電模式 | Workout → Low Power Mode | `bridge:root=com.apple.SessionTrackerAppSettings#LOW_POWER_MODE` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 偵測健身器材 | Workout → Detect Gym Equipment | `bridge:root=com.apple.SessionTrackerAppSettings#NFC_ENABLED_LABEL_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| — | — | `bridge:root=com.apple.SessionTrackerAppSettings#POWER_SAVING_MODE_ENABLED_LABEL` | — | MAN |  |
| 體能訓練 → 顯示目標測量指標 | Workout → Show Goal Metric | `bridge:root=com.apple.SessionTrackerAppSettings#PRO_SETTING_ENABLED_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 從頭播放 | Workout → Play from beginning | `bridge:root=com.apple.SessionTrackerAppSettings#WORKOUT_MUSIC_PLAY_FROM_BEGINNING_SETTING_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 隨機顯示 | Workout → Shuffle | `bridge:root=com.apple.SessionTrackerAppSettings#WORKOUT_MUSIC_SHUFFLE_SETTING_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 語音回饋 | Workout → Voice Feedback | `bridge:root=com.apple.SessionTrackerAppSettings#WORKOUT_VOICE_FEEDBACK_LABEL` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 自動暫停 → 自動暫停 | Workout → Auto-Pause → Auto-Pause | `bridge:root=com.apple.SessionTrackerAppSettings&path=AUTO_PAUSE_ID#WorkoutAutoPauseSwitch` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 體能訓練播放列表 → 播放列表 | Workout → Workout Playlist → Playlists | `bridge:root=com.apple.SessionTrackerAppSettings&path=MUSIC_AUTOSTART_TITLE_ID#MUSIC_PLAYLIST_GROUP_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 體能訓練播放列表 → 無 | Workout → Workout Playlist → None | `bridge:root=com.apple.SessionTrackerAppSettings&path=MUSIC_AUTOSTART_TITLE_ID#NONE_AUTOSTART_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 配速/速度顯示畫面 → 平均 | Workout → Pace/Speed View → Average | `bridge:root=com.apple.SessionTrackerAppSettings&path=PACE_VIEW_LABEL#AVERAGE_PACE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 配速/速度顯示畫面 → 目前 | Workout → Pace/Speed View → Current | `bridge:root=com.apple.SessionTrackerAppSettings&path=PACE_VIEW_LABEL#CURRENT_PACE_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W MAN |  |
| 體能訓練 → 度量單位 → 公里 | Workout → Units of Measure → Kilometers | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#CYCLING_WORKOUTS_KILOMETERS_ID` | 18.7 · 26.2 | F26W F18W |  |
| 體能訓練 → 度量單位 → 英里 | Workout → Units of Measure → Miles | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#CYCLING_WORKOUTS_MILES_ID` | 18.7 · 26.2 | F26W F18W |  |
| 體能訓練 → 度量單位 → 大卡 | Workout → Units of Measure → Calories | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#ENERGY_UNITS_CALORIES_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 度量單位 → 千卡 | Workout → Units of Measure → Kilocalories | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#ENERGY_UNITS_KILOCALORIES_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 度量單位 → 千焦耳 | Workout → Units of Measure → Kilojoules | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#ENERGY_UNITS_KILOJOULES_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 度量單位 → 公尺 | Workout → Units of Measure → Meters | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#POOL_LENGTH_METERS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 度量單位 → 碼 | Workout → Units of Measure → Yards | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#POOL_LENGTH_YARDS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 度量單位 → 公里 | Workout → Units of Measure → Kilometers | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#WALKING_AND_RUNNING_WORKOUTS_KILOMETERS_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |
| 體能訓練 → 度量單位 → 英里 | Workout → Units of Measure → Miles | `bridge:root=com.apple.SessionTrackerAppSettings&path=UNITS_OF_MEASURE_ID#WALKING_AND_RUNNING_WORKOUTS_MILES_ID` | 16.2 · 18.7 · 26.2 | F26W F18W F16W |  |

---

## 5. 附錄 A：第三方 App 的 URL Scheme

來源：[Tanaschita/ios-known-url-schemes-and-universal-links](https://github.com/Tanaschita/ios-known-url-schemes-and-universal-links)。
這些是「開啟 App」的協定，不是設定頁面。全部有官方文件。

| App | URL | 用途 |
| --- | --- | --- |
| App Store | `https://itunes.apple.com/us/app/apple-store/id375380948?mt=8` | 開啟指定 App 的商店頁 |
| FaceTime | `facetime://user@example.com` | 視訊通話 |
| FaceTime | `facetime-audio://user@example.com` | 語音通話 |
| Google Chrome | `googlechrome://github.com` | 用 Chrome 開 http 網址 |
| Google Chrome | `googlechromes://github.com` | 用 Chrome 開 https 網址 |
| Google Maps | `comgooglemaps://?center=40.765819,-73.975866&zoom=14` | 開啟指定座標與縮放 |
| Instagram | `instagram://app` | 開啟 Instagram |
| Instagram | `instagram://camera` | 開啟相機 |
| Instagram | `instagram://user?username=USERNAME` | 開啟指定使用者 |
| Mail | `mailto://foo@example.com?subject=test&body=test` | 新增郵件，帶主旨與內文 |
| Apple Maps | `http://maps.apple.com/?q=vegan+restaurant` | 搜尋地點 |
| Apple Maps | `http://maps.apple.com/?ll=30.269686,-97.759912` | 開啟指定座標 |
| Phone | `tel://phonenumber` | 撥號 |
| Spotify | `spotify://` | 開啟 Spotify |
| YouTube | `http://www.youtube.com/v/VIDEO_IDENTIFIER` | 開啟指定影片 |
| WhatsApp | `whatsapp://send?text=Hello` | 新對話，帶預填文字 |

---

## 6. 附錄 B：沒有納入的來源

| 來源 | 狀態 | 處理方式 |
| --- | --- | --- |
| [0xyza/ios-settings-urls](https://github.com/0xyza/ios-settings-urls) | 倉庫已不存在，GitHub 回傳 404 | 它本來就是 FifiTheBulldog 的分支。原始資料已全部收錄。 |
| [Reddit r/shortcuts: An updated list of Settings URLs](https://www.reddit.com/r/shortcuts/comments/i9rjbh/an_updated_list_of_settings_urls/) | Reddit 擋自動抓取 | 這篇就是 FifiTheBulldog 清單的發布貼。內容已由 GitHub 倉庫收錄。 |
| [Reddit r/shortcuts: iOS settings app URL schemes](https://www.reddit.com/r/shortcuts/comments/1qechhq/ios_settings_app_url_schemes/) | Reddit 擋自動抓取 | 未收錄。要看留言請自己開網頁。 |
