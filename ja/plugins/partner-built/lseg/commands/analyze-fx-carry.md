---
description: Evaluate FX carry trade opportunities with spot, forwards, vol surface, and historical context
argument-hint: "<currency pair e.g. USDJPY> [tenor e.g. 3M]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/analyze-fx-carry.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：スポット、フォワード、ボラティリティ曲面、過去の状況から為替キャリートレード機会を評価する。

<a id="analyze-fx-carry-trade"></a>
# 為替キャリートレードの分析

> LSEGの為替評価、フォワードカーブ、ボラティリティ曲面、過去データのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

スポットレート、フォワードポイント、キャリーの期間構造、ボラティリティリスク、過去の価格の状況を組み合わせ、通貨ペアのキャリー取引機会を評価する。

枠組みとリスク指標の知識は **fx-carry-trade** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-input"></a>
### 1. 入力を集める

ユーザーへ次を尋ねる。
- 通貨ペア（必須）：例 USDJPY、EURUSD、AUDUSD
- 対象期間（任意、既定は3M）
- 評価日（任意、既定は本日）

<a id="2-get-the-spot-rate"></a>
### 2. スポットレートを取得する

通貨ペアで `fx_spot_price` を呼ぶ。

仲値・買値・売値、売買スプレッドを抽出する。

<a id="3-price-the-forward-at-target-tenor"></a>
### 3. 対象期間のフォワードを評価する

通貨ペア・対象期間で `fx_forward_price` を呼ぶ。

フォワードレート・フォワードポイントを抽出し、年率換算キャリーを計算する。

<a id="4-map-the-full-carry-curve"></a>
### 4. キャリーカーブ全体を描く

通貨ペアの `fx_forward_curve` を一覧取得後に計算する。

ONから1Yの各期間のフォワードポイント、年率換算キャリー、累積キャリーを示す。最も条件のよい期間を特定する。

<a id="5-assess-volatility-risk"></a>
### 5. ボラティリティリスクを評価する

通貨ペアの `fx_vol_surface` を呼ぶ。

対象期間のATMボラティリティ、25デルタ・リスクリバーサル、25デルタ・バタフライを抽出する。

キャリー対ボラティリティ比率 = 年率換算キャリー / ATMインプライド・ボラティリティを計算する。

<a id="6-historical-spot-context"></a>
### 6. 過去のスポットの状況

通貨ペアのRICに、`interval: "P1D"`、`tenor: "1Y"` で `tscc_historical_pricing_summaries` を呼ぶ。

52週の範囲、現在値の範囲内の位置、トレンド方向を評価する。

<a id="7-synthesize-the-report"></a>
### 7. レポートをまとめる

キャリー対ボラティリティ比率と総合評価、スポット・フォワード価格、キャリー期間構造表、ボラティリティ曲面の概要、過去の状況を示す。

<a id="output-format"></a>
## 出力形式

キャリー対ボラティリティ比率と総合評価（魅力的／中程度／魅力に乏しい）を先に示し、詳細な根拠データの表を続ける。
