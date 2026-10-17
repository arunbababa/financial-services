> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/market-researcher/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="market-researcher--managed-agent-template"></a>
# 市場調査員 — 管理エージェント テンプレート

<a id="overview"></a>
## 概要

業種・テーマ → 業界概要 → 競争環境 → 同業他社比較 → アイデア候補リスト → 調査ノート。[`market-researcher`](../../plugins/agent-plugins/market-researcher)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export CAPIQ_MCP_URL=... FACTSET_MCP_URL=...
../../scripts/deploy-managed-agent.sh market-researcher
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/market-researcher/steering-examples.json)を参照してください。調査キューのイベントから開始するか、調査担当銘柄のマップ全体へ処理を展開します。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

第三者のレポートと発行体資料は、信頼されていない入力として扱います。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`sector-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| `comps-spreader` / オーケストレーター | いいえ | `Read`, `Grep`, `Glob`, `Agent` | CapIQ、FactSet (読み取り専用) |
| **`note-writer`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`sector-reader` は、長さに制限があり、スキーマ検証された JSON を返します。 `note-writer` は `./out/primer-<sector>.docx` (スライドが要求された場合は `.pptx`) を生成します。

**引継ぎ：** アイデア候補リストに挙がった一銘柄のモデルを作るには、`model-builder`向けの`handoff_request`を出力します。`scripts/orchestrate.py`が新しい指示イベントとして振り分けます。
