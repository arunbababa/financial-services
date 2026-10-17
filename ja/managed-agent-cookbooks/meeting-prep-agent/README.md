> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/meeting-prep-agent/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="meeting-prep-agent--managed-agent-template"></a>
# 会議準備エージェント — 管理対象エージェント テンプレート

<a id="overview"></a>
## 概要

すべてのクライアントとのミーティングの前にブリーフィングパックを提供します。 [`meeting-prep-agent`](../../plugins/agent-plugins/meeting-prep-agent) Cowork プラグインと同じソース — このディレクトリは、`POST /v1/agents` の管理対象エージェント クックブックです。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export CRM_MCP_URL=... CAPIQ_MCP_URL=...
../../scripts/deploy-managed-agent.sh meeting-prep-agent
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/meeting-prep-agent/steering-examples.json)を参照してください。通常はワークフローエンジンがカレンダーの予定から起動します。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

顧客が提供した文書と受信メールは、信頼されていない入力として扱います。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| `profiler` | いいえ | `Read`, `Grep` | CRM、CapIQ (読み取り専用) |
| **`news-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| **`pack-writer`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`pack-writer` は `./out/briefing-<client>.pptx` を生成します。クライアントが提供するコンテンツを直接開くことはありません。

**保証の対象外：** この資料一式は顧客ではなくアドバイザー向けです。顧客への送信は行いません。
