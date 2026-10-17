> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../CLAUDE.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="financial-services-plugins"></a>
# 金融サービスプラグイン

金融サービス向けのCoworkプラグインとClaude Managed Agentの雛形です。各名称付きエージェントは、一つの原本から二つの形で提供されます。

<a id="repository-structure"></a>
## リポジトリ構造

```
├── plugins/
│   ├── agent-plugins/               #   named agents — one self-contained plugin each
│   │   └── <slug>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── agents/<slug>.md     #   ← canonical system prompt (one source, two wrappers)
│   │       └── skills/              #   ← bundled copies, synced from vertical-plugins/
│   ├── vertical-plugins/            #   FSI verticals — skill sources, commands, MCPs
│   │   └── <vertical>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── commands/
│   │       ├── skills/
│   │       └── .mcp.json
│   └── partner-built/               #   partner plugins (LSEG, S&P Global)
├── managed-agent-cookbooks/         # CMA cookbooks (one dir per named agent)
│   └── <slug>/
│       ├── agent.yaml               #   system + skills → ../../plugins/agent-plugins/<slug>/...
│       ├── subagents/*.yaml         #   depth-1 leaf workers
│       ├── steering-examples.json
│       └── README.md                #   security tier + handoff notes
├── claude-for-msft-365-install/     # admin tooling for the Microsoft 365 add-in (separate from FSI plugins)
└── scripts/                         # deploy-managed-agent.sh, check.py, validate.py, orchestrate.py, sync-agent-skills.py
```

コミット前に`python3 scripts/check.py`を実行します。すべてのマニフェストを検査し、`system.file`、`skills.path`、`callable_agents.manifest`の参照先が解決できることを確認します。`agent-plugins/<slug>/skills/`のコピーが`vertical-plugins/`の原本と異なる場合、およびUTF-8 BOMのない`.ps1`に非ASCIIバイトが含まれる場合は、検査を失敗させます。

**`.ps1`ファイルはASCIIのみで記述してください。** 管理されたWindows環境で依然として既定のシェルであるWindows PowerShell 5.1は、BOMのない`.ps1`をUTF-8ではなく端末のANSIコードページで読み込みます。emダッシュや曲線の引用符は文字化けし、文字列を終端するリテラルの`"`を生じさせ、スクリプト全体の*構文解析*を失敗させる場合があります。`—`ではなく`--`を記述してください。この問題はmacOSでは見えず、Windowsでは致命的です。`check.py`が検査します。**スキルは`vertical-plugins/`で編集**し、`python3 scripts/sync-agent-skills.py`でエージェントの束ねコピーへ反映してください。

`check.py`は`pre-commit`フックも自動設定します（`git config core.hooksPath .githooks`。Husky/Nodeは不要）。フックは各プラグインの`.claude-plugin/plugin.json`の`version`を更新し、ブランチのバージョンを`main`よりちょうど一つ先のパッチバージョンにします（コミットごとではなく、ブランチで一度だけ更新。`version`がインストール済みユーザーへの更新配信を制御します）。`version-bump` GitHub Actionも補完策としてPRに同じ規則を適用します。単一コミットでフックを回避するには`git commit --no-verify`を使用します。更新処理は`scripts/version_bump.py`にあります。

<a id="key-files"></a>
## キーファイル

- `marketplace.json`: マーケットプレイス マニフェスト - すべてのプラグインをソース パスに登録します
- `plugin.json`: プラグインのメタデータ - 名前、説明、バージョン、コンポーネント検出設定
- `commands/*.md`: `/plugin:command-name` として呼び出されるスラッシュ コマンド
- `skills/*/SKILL.md`: 特定のタスクに関する詳細な知識とワークフロー
- `*.local.md`: ユーザー固有の構成 (gitignored)
- `mcp-categories.json`: プラグイン間で共有される正規 MCP カテゴリ定義

<a id="development-workflow"></a>
## 開発ワークフロー

1. マークダウン ファイルを直接編集 - 変更はすぐに有効になります
2. `/plugin:command-name`の構文でコマンドをテストします
3. 発動条件が一致すると自動でスキルが発動します
