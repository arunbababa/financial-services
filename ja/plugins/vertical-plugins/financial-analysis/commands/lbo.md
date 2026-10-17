---
description: Build an LBO model for a PE acquisition
argument-hint: "[company name or deal details]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/financial-analysis/commands/lbo.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：PE買収のためのLBOモデルを構築する

`lbo-model` スキルをロードし、指定された会社または取引のレバレッジ バイアウト モデルを構築します。

引数として会社名が指定されている場合は、それを使用します。それ以外の場合は、ターゲット企業と取引パラメータをユーザーに尋ねます。
