---
description: Debug and audit a financial model for errors
argument-hint: "[path to .xlsx model file]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/financial-analysis/commands/debug-model.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：財務モデルのデバッグとエラーの監査

スコープ **model** で `audit-xls` スキルをロードし、完全なモデル整合性チェック (BSの貸借一致、現金残高の照合、ロールフォワード、モデル タイプ固有のバグ) を含む、指定された財務モデルの壊れた式、貸借対照表の不均衡、ハードコードされたオーバーライド、循環参照、およびロジック エラーを監査します。

ファイル パスが指定されている場合は、それを使用します。それ以外の場合は、レビューするモデルをユーザーに依頼します。
