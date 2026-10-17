> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/statement-auditor/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="statement-auditor--managed-agent-template"></a>
# Statement Auditor — 管理対象エージェント テンプレート

<a id="overview"></a>
## 概要

配布前に、作成済みのLP向け明細書を点検・照合します。[`statement-auditor`](../../plugins/agent-plugins/statement-auditor)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export NAV_MCP_URL=...
../../scripts/deploy-managed-agent.sh statement-auditor
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/statement-auditor/steering-examples.json) を参照してください。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

生成済みの明細書は、信頼されていない入力として扱います（生成元システムは対象範囲外）。三層に分離します。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`statement-reader`** | **はい** | `Read`、`Grep`のみ | なし |
| `reconciler` / オーケストレーター | いいえ | `Read`, `Grep`, `Glob`, `Agent` | nav（読取専用） |
| **`flagger`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`flagger` は `./out/signoff-<batch>.xlsx` を生成します。

**保証の対象外：** このエージェントは合格／保留を提案します。人による承認後にIR担当が配布します。
