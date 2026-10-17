# CLAUDE.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../CLAUDE.md)

### CLAUDE.md:8

原文：

```text
├── plugins/
```

日本語：

`├── plugins/`

plugins/ディレクトリ。


### CLAUDE.md:9

原文：

```text
│   ├── agent-plugins/               #   named agents — one self-contained plugin each
```

日本語：

`│   ├── agent-plugins/               #   named agents — one self-contained plugin each`

agent-plugins/：名前付きエージェントごとに、自己完結したプラグインを1つ置く。


### CLAUDE.md:10

原文：

```text
│   │   └── <slug>/
```

日本語：

`│   │   └── <slug>/`

エージェントのslugごとのディレクトリ。


### CLAUDE.md:11

原文：

```text
│   │       ├── .claude-plugin/plugin.json
```

日本語：

`│   │       ├── .claude-plugin/plugin.json`

プラグインのメタデータファイル。


### CLAUDE.md:12

原文：

```text
│   │       ├── agents/<slug>.md     #   ← canonical system prompt (one source, two wrappers)
```

日本語：

`│   │       ├── agents/<slug>.md     #   ← canonical system prompt (one source, two wrappers)`

agents/<slug>.md：正規のシステムプロンプト。1つの原文を2つのラッパーで使う。


### CLAUDE.md:13

原文：

```text
│   │       └── skills/              #   ← bundled copies, synced from vertical-plugins/
```

日本語：

`│   │       └── skills/              #   ← bundled copies, synced from vertical-plugins/`

skills/：vertical-plugins/から同期した同梱コピー。


### CLAUDE.md:14

原文：

```text
│   ├── vertical-plugins/            #   FSI verticals — skill sources, commands, MCPs
```

日本語：

`│   ├── vertical-plugins/            #   FSI verticals — skill sources, commands, MCPs`

vertical-plugins/：金融サービス分野別のスキル原本、コマンド、MCP。


### CLAUDE.md:15

原文：

```text
│   │   └── <vertical>/
```

日本語：

`│   │   └── <vertical>/`

各分野のディレクトリ。


### CLAUDE.md:16

原文：

```text
│   │       ├── .claude-plugin/plugin.json
```

日本語：

`│   │       ├── .claude-plugin/plugin.json`

プラグインのメタデータファイル。


### CLAUDE.md:17

原文：

```text
│   │       ├── commands/
```

日本語：

`│   │       ├── commands/`

commands/ディレクトリ。


### CLAUDE.md:18

原文：

```text
│   │       ├── skills/
```

日本語：

`│   │       ├── skills/`

skills/ディレクトリ。


### CLAUDE.md:19

原文：

```text
│   │       └── .mcp.json
```

日本語：

`│   │       └── .mcp.json`

.mcp.jsonファイル。


### CLAUDE.md:20

原文：

```text
│   └── partner-built/               #   partner plugins (LSEG, S&P Global)
```

日本語：

`│   └── partner-built/               #   partner plugins (LSEG, S&P Global)`

partner-built/：LSEG、S&P Globalなどのパートナー製プラグイン。


### CLAUDE.md:21

原文：

```text
├── managed-agent-cookbooks/         # CMA cookbooks (one dir per named agent)
```

日本語：

`├── managed-agent-cookbooks/         # CMA cookbooks (one dir per named agent)`

managed-agent-cookbooks/：名前付きエージェントごとに1ディレクトリを置くCMAの実装例。


### CLAUDE.md:22

原文：

```text
│   └── <slug>/
```

日本語：

`│   └── <slug>/`

エージェントのslugごとのディレクトリ。


### CLAUDE.md:23

原文：

```text
│       ├── agent.yaml               #   system + skills → ../../plugins/agent-plugins/<slug>/...
```

日本語：

`│       ├── agent.yaml               #   system + skills → ../../plugins/agent-plugins/<slug>/...`

agent.yaml：システムとスキルを../../plugins/agent-plugins/<slug>/...へ対応付ける。


### CLAUDE.md:24

原文：

```text
│       ├── subagents/*.yaml         #   depth-1 leaf workers
```

日本語：

`│       ├── subagents/*.yaml         #   depth-1 leaf workers`

subagents/*.yaml：深さ1の末端ワーカー。


### CLAUDE.md:25

原文：

```text
│       ├── steering-examples.json
```

日本語：

`│       ├── steering-examples.json`

steering-examples.json：追加指示の例。


### CLAUDE.md:26

原文：

```text
│       └── README.md                #   security tier + handoff notes
```

日本語：

`│       └── README.md                #   security tier + handoff notes`

README.md：セキュリティ区分と引き継ぎの注意事項。


### CLAUDE.md:27

原文：

```text
├── claude-for-msft-365-install/     # admin tooling for the Microsoft 365 add-in (separate from FSI plugins)
```

日本語：

`├── claude-for-msft-365-install/     # admin tooling for the Microsoft 365 add-in (separate from FSI plugins)`

Microsoft 365アドインの管理ツール。FSIプラグインとは別。


### CLAUDE.md:28

原文：

```text
└── scripts/                         # deploy-managed-agent.sh, check.py, validate.py, orchestrate.py, sync-agent-skills.py
```

日本語：

`└── scripts/                         # deploy-managed-agent.sh, check.py, validate.py, orchestrate.py, sync-agent-skills.py`

scripts/：一覧にある各スクリプトを格納する。
