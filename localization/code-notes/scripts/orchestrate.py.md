# scripts/orchestrate.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/orchestrate.py)

### scripts/orchestrate.py:2

原文：

```text
Reference event loop for cross-agent handoffs between managed agents.

REFERENCE ONLY — replace with your firm's workflow engine (Temporal, Airflow,
Guidewire event bus). This script shows the shape of the loop, not a
production implementation.

Security note: handoff requests are surfaced in the orchestrator's text output,
which is downstream of untrusted-document readers. An attacker who controls a
processed document could embed a literal handoff_request blob that, if echoed,
would be parsed here. This script mitigates by (a) hard-allowlisting
target_agent against the deployed slugs and (b) schema-validating the payload
before steering. In production, prefer emitting handoffs via a dedicated tool
call or a typed SSE event the model cannot produce by quoting document text.

```

日本語：

マネージドエージェント間で処理を引き継ぐための、イベントループの参考例。

参考用のみ。利用組織のワークフローエンジン（Temporal、Airflow、Guidewireのイベントバスなど）へ置き換える。このスクリプトはループの構成例を示しており、本番向けの実装ではない。

セキュリティ上の注意：引き継ぎ要求はオーケストレーターのテキスト出力に現れる。その上流には信頼できない文書を読むエージェントがある。攻撃者が処理対象の文書を制御できると、handoff_requestのデータをそのまま埋め込み、出力で復唱された際に、ここで要求として解析させるおそれがある。このスクリプトは、(a) target_agentをデプロイ済みslugの厳格な許可リストに限定し、(b) 追加指示を送る前にペイロードをスキーマ検証することで対処する。本番では専用のツール呼び出し、または型の定まったSSEイベントを通じて引き継ぎを発行する方がよい。文書のテキストを引用しただけでは、モデルがそのような要求を生成できない経路を選ぶ。


### scripts/orchestrate.py:65

原文：

```text
agent_ids maps slug -> deployed CMA agent_id.
```

日本語：

agent_idsは、slugからデプロイ済みCMAのagent_idへの対応を保持する。


### scripts/orchestrate.py:67

原文：

```text
/v1/agents is a preview endpoint; SDK type stubs don't cover it yet.
```

日本語：

/v1/agents はプレビュー エンドポイントです。 SDK タイプのスタブではまだカバーされていません。


### scripts/orchestrate.py:68

原文：

```text
type: ignore[attr-defined]
```

日本語：

`type: ignore[attr-defined]`

型検査のattr-definedエラーを抑制する指定。


### scripts/orchestrate.py:79

原文：

```text
type: ignore[attr-defined]
```

日本語：

`type: ignore[attr-defined]`

型検査のattr-definedエラーを抑制する指定。
