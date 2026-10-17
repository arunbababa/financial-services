---
description: Build an accretion/dilution merger model
argument-hint: "[acquirer] acquiring [target]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/investment-banking/commands/merger-model.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：EPSの増加・希薄化を分析する合併モデルの構築

`merger-model` スキルをロードし、合併の影響分析を構築します。

買収者とターゲットが提供されている場合は、それらを使用します。それ以外の場合は、ユーザーに取引の詳細を尋ねます。
