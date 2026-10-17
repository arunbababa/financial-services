> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/earnings-reviewer/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="earnings-reviewer--managed-agent-template"></a>
# Earnings Reviewer — 決算レビューのManaged Agent雛形

<a id="overview"></a>
## 概要

決算説明会＋提出書類 → モデル更新 → ノートの下書き。[`earnings-reviewer`](../../plugins/agent-plugins/earnings-reviewer)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export FACTSET_MCP_URL=... DALOOPA_MCP_URL=...
../../scripts/deploy-managed-agent.sh earnings-reviewer
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/earnings-reviewer/steering-examples.json) を参照してください。オーケストレーション レイヤーからカバレッジ リスト全体にファンアウトします (ティッカーごとに 1 つのセッション)。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

決算説明会の書き起こしとプレスリリースは、信頼されていない入力として扱います。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`transcript-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| `model-updater` / オーケストレーター | いいえ | `Read`, `Grep`, `Glob`, `Agent` | ファクトセット、Daloopa (読み取り専用) |
| **`note-writer`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`transcript-reader` は、長さに制限があり、スキーマ検証された JSON を返します。 `note-writer` は `./out/note-<ticker>.docx` と `./out/model-<ticker>.xlsx` の更新されたモデルを生成します。

**引継ぎ：** 決算を受けて投資仮説が変わりDCFを再作成する場合は、`model-builder`向けの`handoff_request`を出力します。`scripts/orchestrate.py`が新しい指示イベントとして振り分けます。
