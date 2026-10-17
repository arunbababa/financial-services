# scripts/validate.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/validate.py)

### scripts/validate.py:2

原文：

```text
Harness-side schema validation for managed-agent worker output.

Usage: validate.py <output.json> <schema.json|schema.yaml>
Exits 0 on valid, 1 on invalid (message to stderr).

The CMA API does not enforce structured output today, so the deploy harness
runs this between a reader subagent and the orchestrator. Schemas live in each
subagent yaml under `output_schema:` — the deploy script extracts them.

```

日本語：

マネージドエージェントのワーカー出力を、実行基盤（ハーネス）側でスキーマ検証する。

使用法：`validate.py <output.json> <schema.json|schema.yaml>`
妥当なら終了コード0、不正なら1で終了し、メッセージを標準エラー出力へ出す。

原文の説明では、CMA APIは構造化出力を強制しないため、デプロイ用ハーネスが読み取り担当サブエージェントとオーケストレーターの間でこの検証を実行する。スキーマは各サブエージェントのYAML内の`output_schema:`に置かれ、デプロイスクリプトが抽出する。
