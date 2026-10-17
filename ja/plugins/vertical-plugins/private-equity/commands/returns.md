---
description: Build IRR/MOIC sensitivity tables
argument-hint: "[company or deal parameters]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/private-equity/commands/returns.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：IRR・MOICの感度分析表を作る。

`returns-analysis` スキルを読み込み、取得時倍率、レバレッジ、売却時倍率、成長シナリオを変えたPE投資リターンをモデル化する。

取引条件があれば使用し、なければ取得時EBITDA、評価額、資金調達の前提を尋ねる。
