---
description: Build a macro and rates dashboard with economic indicators, yield curves, inflation, and swap spreads
argument-hint: "<country e.g. US> [timeframe e.g. 5Y]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/macro-rates.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：経済指標、利回りカーブ、インフレ、スワップスプレッドを使い、マクロ・金利ダッシュボードを作る。

<a id="macro--rates-dashboard"></a>
# マクロ・金利ダッシュボード

> LSEGのマクロ経済データ、利回りカーブ、インフレカーブ、スワップ評価、過去データのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

主要経済指標、傾き分析付き利回りカーブ、実質金利への分解、スワップスプレッドの状況を示す、総合的なマクロ経済・金利ダッシュボードを作る。

分析の専門知識は **macro-rates-monitor** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-input"></a>
### 1. 入力を集める

ユーザーへ次を尋ねる。
- 国（必須）：例 US、DE、GB、JP、CH
- 過去系列の期間（任意、既定は3Y）
- 特に関心のある指標（任意）

国を通貨へ対応付ける：US→USD、DE→EUR、GB→GBP、JP→JPY。

<a id="2-pull-macro-indicators"></a>
### 2. マクロ指標を取得する

主要指標について `qa_macroeconomic` を呼ぶ。
- GDP成長率（四半期系列）
- CPI・インフレ率（月次系列）
- 失業率（月次系列）
- 政策金利・中央銀行金利

ニーモニックのワイルドカード・パターン（例 "US\*GDP\*"、"US\*CPI\*"）で利用可能な系列を探す。

<a id="3-get-the-yield-curve"></a>
### 3. 利回りカーブを取得する

対象国の国債カーブについて、`interest_rate_curve` を一覧取得後に計算する。

標準期間の利回りを抽出し、2s10s、3M-10Y、5s30sの傾きを計算する。カーブ形状を分類する。

<a id="4-decompose-real-rates"></a>
### 4. 実質金利へ分解する

通貨の `inflation_curve` を検索後に計算する。

主要期間で実質金利 = 名目金利 − ブレークイーブン・インフレ率を求め、実質金利が緩和的か引き締め的か評価する。

<a id="5-swap-spread-analysis"></a>
### 5. スワップスプレッド分析

2Y、5Y、10Yで `ir_swap` を一覧取得後に価格評価する。

期間別にスワップスプレッド = スワップレート − 国債利回りを求め、金融環境を評価する。

<a id="6-historical-yield-context"></a>
### 6. 過去の利回りの状況

ベンチマーク利回りのRICに、ユーザーが指定した期間で `tscc_historical_pricing_summaries` を呼ぶ。

現在の利回りが過去の範囲のどこにあるかと、トレンド方向を評価する。

<a id="7-synthesize-the-dashboard"></a>
### 7. ダッシュボードをまとめる

マクロ概要表、傾き指標付き利回りカーブ、実質金利への分解、スワップスプレッド表、過去の状況、2〜3文のマクロ・金利総合評価を示す。

<a id="output-format"></a>
## 出力形式

明確な節名を付けたダッシュボードとする。マクロの総合評価を先に示し、各構成要素の詳細を続ける。
