> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/kyc-screener/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="kyc-screener--managed-agent-template"></a>
# KYC スクリーナー — 管理対象エージェントのテンプレート

<a id="overview"></a>
## 概要

顧客受入れ審査の文書を解析し、ルールエンジンを実行し、制裁対象者・PEPの照合を行い、不足を指摘します。[`kyc-screener`](../../plugins/agent-plugins/kyc-screener)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export SCREENING_MCP_URL=...
../../scripts/deploy-managed-agent.sh kyc-screener
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/kyc-screener/steering-examples.json) を参照してください。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

顧客受入れ審査の文書は、信頼されていない入力として扱います。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`doc-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| `rules-engine` / オーケストレーター | いいえ | `Read`, `Grep`, `Glob`, `Agent` | スクリーニング（読み取り専用） |
| **`escalator`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`doc-reader` は、長さに制限があり、スキーマ検証された JSON を返します。 `escalator` は `./out/escalation-<packet>.xlsx` を生成します。

**保証の対象外：** このエージェントはリスク格付けを提案します。判断するのはコンプライアンス責任者です。
