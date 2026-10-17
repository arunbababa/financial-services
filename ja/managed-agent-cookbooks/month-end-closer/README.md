> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/month-end-closer/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="month-end-closer--managed-agent-template"></a>
# 月末締め — 管理対象エージェント テンプレート

<a id="overview"></a>
## 概要

発生計上、期首から期末までの増減整理、差異要因の説明を行います。[`month-end-closer`](../../plugins/agent-plugins/month-end-closer)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export GL_MCP_URL=...
../../scripts/deploy-managed-agent.sh month-end-closer
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/month-end-closer/steering-examples.json) を参照してください。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

裏付け資料である請求書や仕入先の明細書は、信頼されていない入力として扱います。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`ledger-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| `rollforward` / オーケストレーター | いいえ | `Read`, `Grep`, `Glob`, `Agent` | internal-gl（読取専用） |
| **`poster`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`poster`は`./out/close-package-<entity>-<period>.xlsx`を生成します。仕訳案を承認前の状態で用意し、GLへは記帳しません。

**引継ぎ：** `gl-reconciler`から検証済みの照合差異を含む`handoff_request`イベントを受け取り、決算の説明文へ反映します。
