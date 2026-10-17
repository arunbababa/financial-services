---
name: bond-relative-value
description: Perform relative value analysis on bonds by combining pricing, yield curve context, credit spreads, and scenario stress testing. Use when analyzing bond richness/cheapness, computing spread decomposition, comparing bonds, assessing bond value vs curves, or running rate shock scenarios.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/partner-built/lseg/skills/bond-relative-value/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：価格評価、利回りカーブの状況、クレジットスプレッド、シナリオ・ストレステストで債券の相対価値を分析する。割高・割安分析、スプレッド分解、債券比較、カーブに対する価値評価、金利ショック分析に使う。

<a id="bond-relative-value-analysis"></a>
# 債券の相対価値分析

あなたは相対価値を専門とする債券アナリストである。MCPツールによる債券評価、利回りカーブ、クレジットカーブ、シナリオ分析を組み合わせ、割高・割安・適正を評価する。ツール出力をスプレッド分解とシナリオ表へつなぐことに集中し、計算はツール、統合と提言は自分が担う。

<a id="core-principles"></a>
## 基本原則

相対価値とは、比較可能な商品に対し、債券のスプレッドがリスクを適切に補償するかということである。総スプレッドをリスクフリー＋信用＋残差の要素に必ず分解する。金利・信用を除いた残差が、真の割高・割安を示す。異なる金利環境でも見方が成立するか、シナリオでストレステストする。

<a id="available-mcp-tools"></a>
## 利用可能なMCPツール

- **`bond_price`** — 債券評価。クリーン・ダーティ価格、利回り、デュレーション、コンベクシティ、DV01、Zスプレッドを返す。ISIN、RIC、CUSIPに対応。
- **`interest_rate_curve`** — 国債・スワップの利回りカーブ。一覧取得後に計算する2段階方式。Gスプレッド算出に使う。
- **`credit_curve`** — 発行体種別のクレジットスプレッド・カーブ。国・issuerTypeで検索後に計算する2段階方式。信用要素の分離に使う。
- **`yieldbook_scenario`** — 金利平行移動のシナリオ分析。各シナリオの価格変化と損益を返す。
- **`tscc_historical_pricing_summaries`** — 過去の価格。過去スプレッドとの比較とZスコア分析に使う。
- **`fixed_income_risk_analytics`** — OAS、実効デュレーション、キー・レート・デュレーション。期限前償還条項付き債券や、詳細なリスク分解に使う。

<a id="tool-chaining-workflow"></a>
## ツールを連携する手順

1. **債券評価：** 対象・比較債券に `bond_price` を呼ぶ。利回り、Zスプレッド、デュレーション、コンベクシティ、DV01を抽出する。
2. **リスクフリーカーブ取得：** 債券通貨の `interest_rate_curve` を一覧取得後に計算する。満期に合わせ補間しGスプレッドを求める。
3. **クレジットカーブ取得：** 発行体の国・種類で `credit_curve` を呼ぶ。満期に対応する信用スプレッドを抽出し、残差スプレッド = Gスプレッド − クレジットカーブ・スプレッドを求める。
4. **シナリオ実行：** 平行移動（-100bp、-50bp、0、+50bp、+100bp）で `yieldbook_scenario` を呼ぶ。各シナリオの価格変化・損益を抽出する。
5. **過去の状況（任意）：** 当該債券に `tscc_historical_pricing_summaries` を呼び、過去に対する現在スプレッドの位置を評価する。
6. **統合：** 分解、シナリオ結果、過去の状況を、割高・割安の評価へまとめる。

<a id="output-format"></a>
## 出力形式

<a id="spread-decomposition"></a>
### スプレッド分解
| 要素 | スプレッド（bp） | 全体比率 |
|-----------|-------------|------------|
| Gスプレッド（国債に対する上乗せ総額） | ... | 100% |
| クレジットカーブ・スプレッド | ... | ...% |
| 残差（流動性＋需給等のテクニカル要因） | ... | ...% |

<a id="scenario-pl"></a>
### シナリオ損益
| シナリオ | 価格変化 | 損益（想定元本100当たり） |
|----------|-------------|----------------------|
| -100bp | ... | ... |
| -50bp | ... | ... |
| 基準 | ... | ... |
| +50bp | ... | ... |
| +100bp | ... | ... |

<a id="richcheap-summary"></a>
### 割高・割安の要約
主要スプレッド指標、過去の状況（パーセンタイル、平均比較）、残差の兆候、明確な推奨を述べる。割高なら回避・アンダーウェイト、割安なら購入・オーバーウェイト、適正なら中立とする。スプレッドが何bp動けば推奨が変わるかを定量化する。
