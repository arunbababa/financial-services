> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/valuation-reviewer/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="valuation-reviewer--managed-agent-template"></a>
# 評価レビュー担当者 — 管理対象エージェントのテンプレート

<a id="overview"></a>
## 概要

GPの資料一式を取り込み、評価テンプレートを実行し、LP向け報告を承認前の段階まで準備します。[`valuation-reviewer`](../../plugins/agent-plugins/valuation-reviewer)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export PORTFOLIO_MCP_URL=...
../../scripts/deploy-managed-agent.sh valuation-reviewer
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/valuation-reviewer/steering-examples.json) を参照してください。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

GPが提供する評価資料一式は、信頼されていない入力として扱います。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`package-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| `valuation-runner` / オーケストレーター | いいえ | `Read`, `Grep`, `Glob`, `Agent` | ポートフォリオ (読み取り専用) |
| **`publisher`**（書込み権限を持つ担当） | いいえ | `Read`, `Write`, `Edit` | なし |

`package-reader` は、長さに制限があり、スキーマ検証された JSON を返します。 `publisher` は `./out/lp-pack-<fund>.xlsx` を生成します。

**引継ぎ：** 指摘対象の投資先企業をGL Reconcilerへ渡すには、`gl-reconciler`向けの`handoff_request`を出力します。`scripts/orchestrate.py`が振り分けます。

**保証の対象外：** LP向け報告には、このエージェントの外でIR担当とCCOによる確認・承認が必要です。
