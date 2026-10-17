> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../managed-agent-cookbooks/gl-reconciler/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="gl-reconciler--managed-agent-template"></a>
# GL Reconciler — 管理対象エージェント テンプレート

<a id="overview"></a>
## 概要

指定された約定日と資産クラス群について、総勘定元帳と補助元帳の照合差異を見つけ、根本原因を追跡し、経理管理責任者の確認・承認用に例外報告書を作成します。

[`gl-reconciler`](../../plugins/agent-plugins/gl-reconciler) Cowork プラグインと同じソース — このディレクトリは、`POST /v1/agents` の管理対象エージェント クックブックです。

<a id="deploy"></a>
## デプロイ

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export GL_MCP_URL=...           # read-only GL MCP
export SUBLEDGER_MCP_URL=...    # read-only subledger MCP
../../scripts/deploy-managed-agent.sh gl-reconciler
```

<a id="steering-events"></a>
## ステアリングイベント

[`steering-examples.json`](../../../managed-agent-cookbooks/gl-reconciler/steering-examples.json)を参照してください。約定日と資産クラスの一覧でセッションを開始し、追加イベントで単一の照合差異を再追跡できます。

<a id="security--handoffs"></a>
## セキュリティとハンドオフ

このエージェントは取引相手・カストディアンの明細書を読みます。これらは外部者が作成する文書で、敵対的な指示を含む可能性があります。テンプレートは、これらの文書内のペイロードがシェル、書込みツール、社内システムへ到達しないよう構成されています。

| 階層 | 信頼できないドキュメントに触れますか? | ツール | コネクタ |
|---|---|---|---|
| **`reader`** | **はい** | `Read`、`Grep`のみ | なし |
| **オーケストレーター** | いいえ | `Read`, `Grep`, `Glob`, `Agent` | 読み取り専用のGL + 補助元帳MCP |
| **`resolver`** (書き込みホルダー) | いいえ | `Read`, `Write`, `Edit` | なし |

`reader`は、長さの上限を設け、スキーマ検証したJSONだけを返します（`scripts/validate.py`による検証）。`critic`が信頼できる情報源に照らして各照合差異を独立に再確認してから、統括担当が一式を`resolver`へ渡します。`resolver`は例外報告書を`./out/`へ書き込み、外部者のファイルは開きません。

**引継ぎ：** 検証済みの照合差異をMonth-End Closerへ渡すため、統括担当は最終出力に`month-end-closer`向けの`handoff_request`を含めます。`scripts/orchestrate.py`（またはTemporal/Airflowのワーカー）が新しい指示イベントとして振り分けます。許可リストとペイロード検証の方式はスクリプトを参照してください。

**保証の対象外：** ここでの処理は正式な記録管理システムへは書き込みません。元帳の調整には、エージェント外で人による承認が必要です。
