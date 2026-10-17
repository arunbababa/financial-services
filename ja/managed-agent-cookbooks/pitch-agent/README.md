> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/pitch-agent/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="pitch-agent--managed-agent-template"></a>
# 提案エージェント — 管理対象エージェント テンプレート

<a id="overview"></a>
## 概要

類似企業比較、類似取引事例、LBOから、ブランド様式に沿った提案スライドまで一貫して作成します。[`pitch-agent`](../../plugins/agent-plugins/pitch-agent)のCoworkプラグインと同じ原本を使用します。このディレクトリは`POST /v1/agents`用のManaged Agentの設定・利用例です。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export CAPIQ_MCP_URL=... DALOOPA_MCP_URL=...
../../scripts/deploy-managed-agent.sh pitch-agent
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/pitch-agent/steering-examples.json) を参照してください。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

作業の分解に基づく役割分担です。データはCapIQ/DaloopaのMCPから取得するため、信頼されていない入力への対処よりも、並列処理と成果物の分離を主眼とします。`Write`を持つ作業担当は一つだけです。

| 末端の作業担当 | ツール | コネクタ |
|---|---|---|
| `researcher` | `Read`, `Grep` | CapIQ、Daloopa (読み取り専用) |
| `modeler` | `Read`、`Bash` (サンドボックス) | CapIQ、Daloopa (読み取り専用) |
| **`deck-writer`** (書き込みホルダー) | `Read`, `Write`, `Edit` | なし |

アーティファクトは、`pptx-author` / `xlsx-author` を介して、`./out/pitch-<target>.pptx` および `./out/model.xlsx` に配置されます。

**引継ぎ：** 投資仮説の変更後にモデルを作り直す場合、統括担当は`model-builder`向けの`handoff_request`を出力します。`scripts/orchestrate.py`（または自社のワークフローエンジン）が新しい指示イベントとして振り分けます。許可リストとペイロード検証の方式はスクリプトを参照してください。
