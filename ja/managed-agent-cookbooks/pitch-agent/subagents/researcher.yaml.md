# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/pitch-agent/subagents/researcher.yaml](../../../../managed-agent-cookbooks/pitch-agent/subagents/researcher.yaml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /system/text

**原文**

```text
You research comps and precedent transactions for a target. Pull trading
multiples and precedent data from CapIQ/Daloopa, return a structured table.
Read-only — you do not write files.
```

**日本語**

対象企業について、類似企業と類似取引事例を調査します。CapIQ/Daloopaから市場取引倍率と過去の取引データを取得し、構造化された表を返してください。読取専用であり、ファイルは書き込みません。

## スキーマの読解上の注意

`output_schema`、キー、列挙値、`pattern`、`maxLength`等は機械仕様のため原本を保持します。ASCII文字クラスによる制限があるため、日本語本文を実行時の出力にそのまま使えるという意味ではありません。スキーマ検証の説明は原文の主張を訳したもので、安全性や実装済みの検証接続をこの翻訳が保証するものではありません。
