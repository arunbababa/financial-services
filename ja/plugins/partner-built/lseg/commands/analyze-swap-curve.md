---
description: Analyze the swap curve with government and inflation overlays to identify curve trade opportunities
argument-hint: "<currency e.g. EUR> [index e.g. ESTR]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/analyze-swap-curve.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：国債とインフレの情報を重ねてスワップカーブを分析し、カーブ取引の機会を探す。

<a id="analyze-swap-curve"></a>
# スワップカーブの分析

> LSEGのスワップ評価、金利カーブ、インフレカーブのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

金利スワップカーブを構築・分析し、国債利回りとブレークイーブン・インフレ率を重ね、カーブ取引の機会を探す。

分析と取引構築の知識は **swap-curve-strategy** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-input"></a>
### 1. 入力を集める

ユーザーへ次を尋ねる。
- 通貨（必須）：例 EUR、USD、GBP、CHF、JPY
- 参照金利指数（任意）：例 ESTR、SOFR、SONIA、TONA
- 評価日（任意、既定は本日）

<a id="2-discover-swap-templates"></a>
### 2. スワップ・テンプレートを探す

通貨と任意の参照指数で、`ir_swap` を一覧モードで呼ぶ。

利用できるテンプレート参照、指数の詳細、市場慣行を抽出する。

<a id="3-build-the-swap-curve"></a>
### 3. スワップカーブを構築する

標準期間2Y、5Y、7Y、10Y、20Y、30Yについて、`ir_swap` を価格評価モードで呼ぶ。

期間ごとのパースワップレートとDV01を抽出する。

<a id="4-overlay-the-government-curve"></a>
### 4. 国債カーブを重ねる

同じ通貨の `interest_rate_curve` を一覧取得後に計算する。

期間別に、スワップスプレッド = スワップレート − 国債利回りを求める。

<a id="5-decompose-real-rates"></a>
### 5. 実質金利へ分解する

通貨の `inflation_curve` を検索後に計算する。

期間別に、実質スワップレート = 名目スワップレート − ブレークイーブン・インフレ率を求める。

<a id="6-synthesize-curve-strategy-views"></a>
### 6. カーブ戦略の見方をまとめる

2s10sの傾き、5s30sの傾き、2s5s10sバタフライを計算する。

現在水準と過去の通常水準を比べ、スティープナー、フラットナー、バタフライ、スワップスプレッド取引の機会を探す。

国債カーブを重ねたスワップカーブ表、カーブ指標、実質金利への分解、DV01中立の比率を付けた取引提言を示す。

<a id="output-format"></a>
## 出力形式

カーブ形状の概要と主要指標（2s10s、バタフライ）を先に示し、詳細表と取引案の節を続ける。
