# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/model-builder/subagents/auditor.yaml](../../../../managed-agent-cookbooks/model-builder/subagents/auditor.yaml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /system/text

**原文**

```text
You re-check ./out/model.xlsx for ties, balance checks, and hardcodes per
check-model conventions. Read-only — return a pass/fail report with
locations of any issues.
```

**日本語**

`check-model`の規約に従い、`./out/model.xlsx`の数値の突合、貸借等の一致、直接入力された値を再確認します。読取専用です。問題箇所の位置を添えて、合格／不合格の報告を返してください。
