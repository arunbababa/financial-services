# claude-for-msft-365-install/commands/export-data.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/commands/export-data.md)

### claude-for-msft-365-install/commands/export-data.md:41

原文：

```text
  manifest.xml                       the WebView                storage bucket
```

日本語：

`manifest.xml                       the WebView                storage bucket`

manifest.xml、WebView、保存領域の対応を示す図の見出し。


### claude-for-msft-365-install/commands/export-data.md:43

原文：

```text
  │ <Id>  3499c065-…     │──ignored─╳│               │          │             │
```

日本語：

`│ <Id>  3499c065-…     │──ignored─╳│               │          │             │`

Idはストレージの識別に使われない。


### claude-for-msft-365-install/commands/export-data.md:44

原文：

```text
  │ <Version> 1.0.0.11   │──ignored─╳│  loads  URL   │──origin─▶│ IndexedDB   │
```

日本語：

`│ <Version> 1.0.0.11   │──ignored─╳│  loads  URL   │──origin─▶│ IndexedDB   │`

Versionもストレージの識別に使われない。WebViewが読み込むURLのオリジンに対応するIndexedDBが使われる。


### claude-for-msft-365-install/commands/export-data.md:45

原文：

```text
  │ <SourceLocation>     │──────────▶│               │          │  for that   │
```

日本語：

`│ <SourceLocation>     │──────────▶│               │          │  for that   │`

SourceLocationが読み込むURLを指定する。


### claude-for-msft-365-install/commands/export-data.md:46

原文：

```text
  │   https://host/…     │           └───────────────┘          │   origin    │
```

日本語：

`│   https://host/…     │           └───────────────┘          │   origin    │`

URLのオリジンに対応するストレージがある。


### claude-for-msft-365-install/commands/export-data.md:49

原文：

```text
         │ replaced / deleted / re-ID'd / version-bumped               │
```

日本語：

`│ replaced / deleted / re-ID'd / version-bumped               │`

マニフェストの置換、削除、ID変更、バージョン更新。


### claude-for-msft-365-install/commands/export-data.md:50

原文：

```text
         └──── none of this reaches ───────────────────────────────────┘
```

日本語：

`└──── none of this reaches ───────────────────────────────────┘`

これらの変更はストレージには及ばない。


### claude-for-msft-365-install/commands/export-data.md:96

原文：

```text
└── Excel/                            macOS groups by app — each Office app has
```

日本語：

`└── Excel/                            macOS groups by app — each Office app has`

macOSではアプリごとにグループ分けされ、各Officeアプリが


### claude-for-msft-365-install/commands/export-data.md:97

原文：

```text
    ├── pivot.claude.ai/              its own sandbox, so each keeps separate history
```

日本語：

`├── pivot.claude.ai/              its own sandbox, so each keeps separate history`

個別のサンドボックスを持つため、履歴もアプリ別に保持する。


### claude-for-msft-365-install/commands/export-data.md:98

原文：

```text
    │   ├── claude-chat-history/
```

日本語：

`│   ├── claude-chat-history/`

claude-chat-history/はチャット履歴。


### claude-for-msft-365-install/commands/export-data.md:99

原文：

```text
    │   ├── claude-local-skills/
```

日本語：

`│   ├── claude-local-skills/`

claude-local-skills/はローカルのスキル。


### claude-for-msft-365-install/commands/export-data.md:100

原文：

```text
    │   ├── claude-mcp-gateways/
```

日本語：

`│   ├── claude-mcp-gateways/`

claude-mcp-gateways/はMCPゲートウェイ。


### claude-for-msft-365-install/commands/export-data.md:101

原文：

```text
    │   ├── claude-memory/
```

日本語：

`│   ├── claude-memory/`

claude-memory/はメモリ。


### claude-for-msft-365-install/commands/export-data.md:102

原文：

```text
    │   └── local-storage/            settings, inference config, onboarding + terms
```

日本語：

`│   └── local-storage/            settings, inference config, onboarding + terms`

local-storage/は設定、推論設定、オンボーディングと利用規約のフラグ。


### claude-for-msft-365-install/commands/export-data.md:103

原文：

```text
    └── addins.contoso.com_8443/      a non-default port is kept in the name:
```

日本語：

`└── addins.contoso.com_8443/      a non-default port is kept in the name:`

既定以外のポート番号は名前に残す。


### claude-for-msft-365-install/commands/export-data.md:104

原文：

```text
        └── …                         :8443 is a different origin, so a different store
```

日本語：

`└── …                         :8443 is a different origin, so a different store`

:8443は別のオリジンであり、ストアも別になる。


### claude-for-msft-365-install/commands/export-data.md:113

原文：

```text
└── <guid>_ADAL__2\                    the Office account (see "Putting data back")
```

日本語：

`└── <guid>_ADAL__2\                    the Office account (see "Putting data back")`

Officeのアカウント（「Putting data back」を参照）。


### claude-for-msft-365-install/commands/export-data.md:114

原文：

```text
    ├── pivot.claude.ai\
```

日本語：

`├── pivot.claude.ai\`

pivot.claude.aiの保存先。


### claude-for-msft-365-install/commands/export-data.md:115

原文：

```text
    │   └── https_pivot.claude.ai_0.indexeddb.leveldb\
```

日本語：

`│   └── https_pivot.claude.ai_0.indexeddb.leveldb\`

IndexedDBのLevelDBストアのディレクトリ。


### claude-for-msft-365-install/commands/export-data.md:116

原文：

```text
    ├── addins.contoso.com_8443\
```

日本語：

`├── addins.contoso.com_8443\`

既定以外のポート番号8443を含む保存先。


### claude-for-msft-365-install/commands/export-data.md:117

原文：

```text
    └── Local Storage\                 ⚠ whole profile store — ALL origins, not
```

日本語：

`└── Local Storage\                 ⚠ whole profile store — ALL origins, not`

Local Storageはプロファイル全体のストア。すべてのオリジンを含み、


### claude-for-msft-365-install/commands/export-data.md:118

原文：

```text
        └── leveldb\                     just Claude's. Chromium cannot split it.
```

日本語：

`└── leveldb\                     just Claude's. Chromium cannot split it.`

Claudeだけのものではない。Chromiumでは分割できない。


### claude-for-msft-365-install/commands/export-data.md:145

原文：

```text
SELECT sum(length(value)) FROM Records;
```

日本語：

`SELECT sum(length(value)) FROM Records;`

Records内のvalueの長さの合計を取得するSQL。
