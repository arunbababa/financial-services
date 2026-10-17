---
description: Analyze option volatility with vol surface, Greeks, and implied vs realized vol comparison
argument-hint: "<underlying e.g. .SPX or EURUSD> [strike] [expiry]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/analyze-option-vol.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：ボラティリティ曲面、グリークス、インプライド対実現ボラティリティの比較で、オプションのボラティリティを分析する。

<a id="analyze-option-volatility"></a>
# オプションのボラティリティ分析

> LSEGのボラティリティ曲面、オプション評価、過去データのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

曲面の生成、全グリークス付きのオプション評価、インプライド対実現ボラティリティの比較で、原資産のボラティリティ環境を分析する。

曲面の解釈とグリークス分析の知識は **option-vol-analysis** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-input"></a>
### 1. 入力を集める

ユーザーへ次を尋ねる。
- 原資産（必須）：
  - 株式・指数：RIC形式（例 "VOD.L@RIC"、".SPX@RIC"）
  - 先物：RICROOT形式（例 "ES@RICROOT"、"CL@RICROOT"）
  - 為替：ISOペア（例 "EURUSD"、"USDJPY"）
- 権利行使価格（任意、既定はATM）
- 満期日または期間（任意、既定は3M）
- コール／プット（任意、既定は両方）

株式・指数か為替かを判別して、正しい曲面ツールを選ぶ。

<a id="2-generate-the-volatility-surface"></a>
### 2. ボラティリティ曲面を生成する

**株式・指数・先物：** `equity_vol_surface` を呼ぶ。

**為替：** `fx_vol_surface` を呼ぶ。

各期間のATMボラティリティ、25デルタ・リスクリバーサル、25デルタ・バタフライを抽出する。

<a id="3-discover-option-templates"></a>
### 3. オプション・テンプレートを探す

原資産に対して `option_template_list` を呼ぶ。利用できる種類・満期・権利行使価格を確認する。

<a id="4-price-the-option"></a>
### 4. オプションを評価する

原資産・権利行使価格・満期で `option_value` を呼ぶ。

プレミアム、デルタ、ガンマ、ベガ、シータ、インプライド・ボラティリティを抽出する。

<a id="5-compute-realized-volatility"></a>
### 5. 実現ボラティリティを計算する

`interval: "P1D"`、`tenor: "1Y"` で `tscc_historical_pricing_summaries` を呼ぶ。

終値から次の終値への変化に基づく実現ボラティリティを、20日・60日・90日の窓で求める。対応する期間のインプライド・ボラティリティと比べる。

<a id="6-synthesize-the-report"></a>
### 6. レポートをまとめる

曲面概要表、グリークス表、インプライド対実現の比較、ボラティリティ局面の評価、戦略提言を示す。

<a id="output-format"></a>
## 出力形式

主な発見（実現値に対してインプライドが割高か割安か）を先に示し、曲面概要、オプション評価、詳細比較を続ける。
