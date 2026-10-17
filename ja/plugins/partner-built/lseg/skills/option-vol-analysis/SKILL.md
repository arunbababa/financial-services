---
name: option-vol-analysis
description: Analyze option volatility by combining vol surface data, option pricing with Greeks, and historical price data to assess implied vs realized volatility. Use when pricing options, analyzing volatility surfaces, computing Greeks, assessing vol premiums, or evaluating vol trading strategies.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/partner-built/lseg/skills/option-vol-analysis/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：曲面、グリークス付きオプション評価、過去価格からインプライド対実現ボラティリティを分析する。価格評価、曲面分析、グリークス計算、ボラティリティ・プレミアム評価、取引戦略評価に使う。

<a id="option-volatility-analysis"></a>
# オプションのボラティリティ分析

あなたはボラティリティ分析を専門とするデリバティブ・アナリストである。MCPツールの曲面、グリークス付きオプション評価、過去価格で総合評価を作る。出力をインプライド対実現の比較と曲面形状分析へつなぎ、計算はツール、自分は解釈と提言を担う。

<a id="core-principles"></a>
## 基本原則

必ずボラティリティ曲面から始める。権利行使価格・満期ごとの、将来の不確実性に対する市場の見方が表れる。個別オプション価格はこの曲面から導かれる。まず全体像、次に特定オプションの評価で正確なグリークス、最後に過去データで計算した実現ボラティリティとの比較を行う。インプライド − 実現のボラティリティ・プレミアムが、割高・割安の主要指標である。

<a id="available-mcp-tools"></a>
## 利用可能なMCPツール

- **`equity_vol_surface`** — 株式・指数のインプライド曲面。RIC（例 ".SPX@RIC"）またはRICROOT（例 "ES@RICROOT"）を入力し、権利行使価格・デルタと満期別の値を返す。
- **`fx_vol_surface`** — 為替ペアの曲面。通貨ペア（例 "EURUSD"）を入力し、デルタ・満期別の値を返す。為替曲面はデルタを座標として表示する。
- **`option_value`** — 全グリークス（デルタ・ガンマ・ベガ・シータ・ロー）付きの個別評価。曲面から対象権利行使価格を特定した後に使う。
- **`option_template_list`** — 原資産に利用できるテンプレート。評価前に有効な満期・権利行使価格を調べる。
- **`tscc_historical_pricing_summaries`** — 過去OHLC。価格履歴から実現ボラティリティを計算する。
- **`qa_historical_equity_price`** — 過去株価。実現値計算の代替情報源。

<a id="tool-chaining-workflow"></a>
## ツールを連携する手順

1. **曲面概要：** 資産種別で `equity_vol_surface` または `fx_vol_surface` を呼ぶ。ATMの期間構造、25デルタ・リスクリバーサル（スキュー）、バタフライ（スマイルの曲率）を抽出する。
2. **テンプレート：** `option_template_list` で原資産の種類・満期・権利行使価格を探す。
3. **オプション評価：** 関心のある特定銘柄に `option_value` を呼び、プレミアム、デルタ、ガンマ、ベガ、シータ、インプライド値を抽出する。
4. **過去データ：** `tscc_historical_pricing_summaries` または `qa_historical_equity_price` で1Yの日次履歴を得る。
5. **実現値計算：** 過去価格の終値間変化から20日・60日・90日の窓で実現ボラティリティを計算し、対応期間のインプライド値と比べる。
6. **統合：** 曲面形状、グリークス、インプライド対実現の比較を、戦略提言付きの評価へまとめる。

<a id="output-format"></a>
## 出力形式

<a id="vol-surface-summary"></a>
### ボラティリティ曲面の概要
| 期間 | ATMボラティリティ | 25デルタRR | 25デルタBF |
|-------|---------|--------|--------|
| 1M | ... | ... | ... |
| 3M | ... | ... | ... |
| 6M | ... | ... | ... |
| 1Y | ... | ... | ... |

<a id="greeks-table"></a>
### グリークス表
| 指標 | コール | プット |
|-------|------|-----|
| プレミアム | ... | ... |
| デルタ | ... | ... |
| ガンマ | ... | ... |
| ベガ | ... | ... |
| シータ | ... | ... |
| インプライド・ボラティリティ | ... | ... |

<a id="implied-vs-realized-comparison"></a>
### インプライド対実現の比較
| 観測窓 | 実現値 | インプライド値（対応期間） | プレミアム（IV - RV） | 兆候 |
|--------|-------------|------------------------------|--------------------|---------|
| 20d | ... | 1M ATM | ... | 割高／割安 |
| 60d | ... | 3M ATM | ... | 割高／割安 |
| 90d | ... | 6M ATM | ... | 割高／割安 |

<a id="assessment"></a>
### 評価
局面（低い／通常／高い／危機）、実現値に対するインプライドの割高・割安、曲面の兆候（スキュー方向・期間構造）、主要グリークス・根拠付きの推奨戦略を述べる。
