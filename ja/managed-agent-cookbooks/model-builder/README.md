> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/model-builder/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="model-builder--managed-agent-template"></a>
# モデル ビルダー — 管理対象エージェント テンプレート

<a id="overview"></a>
## 概要

DCF、LBO、財務三表、類似企業比較を成果物ファイルとして作成します。[`model-builder`](../../plugins/agent-plugins/model-builder)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export CAPIQ_MCP_URL=... DALOOPA_MCP_URL=...
../../scripts/deploy-managed-agent.sh model-builder
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/model-builder/steering-examples.json) を参照してください。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

タスク分解の分割 - 入力は信頼できる MCP から取得されるため、分割はアーティファクトの分離と再検証に関するものです。ちょうど 1 つのワーカーが `Write` を保持します。

| 末端の作業担当 | ツール | コネクタ |
|---|---|---|
| `data-puller` | `Read`, `Grep` | CapIQ、Daloopa (読み取り専用) |
| **`builder`** (書き込みホルダー) | `Read`、`Write`、`Edit`、`Bash` (サンドボックス) | なし |
| `auditor` | `Read`, `Grep` | なし |

`builder`が`./out/model.xlsx`を書き込んだ後、`auditor`が数値の突合と貸借等の一致を再確認します。

**ハンドオフ:** `earnings-reviewer` または `pitch-agent` から呼び出された場合、呼び出し側エージェントの `handoff_request` は、`scripts/orchestrate.py` によってここにルーティングされます。
