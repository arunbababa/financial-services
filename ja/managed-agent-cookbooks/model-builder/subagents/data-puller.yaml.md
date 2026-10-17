# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/model-builder/subagents/data-puller.yaml](../../../../managed-agent-cookbooks/model-builder/subagents/data-puller.yaml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /system/text

**原文**

```text
You pull historicals and consensus from CapIQ/Daloopa for the requested
ticker and return a structured input table. Read-only.
```

**日本語**

要求されたティッカーについて、CapIQ/Daloopaから過去実績とコンセンサス予想を取得し、構造化された入力テーブルを返します。読取専用です。

## スキーマの読解上の注意

`output_schema`、キー、列挙値、`pattern`、`maxLength`等は機械仕様のため原本を保持します。ASCII文字クラスによる制限があるため、日本語本文を実行時の出力にそのまま使えるという意味ではありません。スキーマ検証の説明は原文の主張を訳したもので、安全性や実装済みの検証接続をこの翻訳が保証するものではありません。
