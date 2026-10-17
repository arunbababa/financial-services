---
description: Analyze a bond's relative value vs yield curves and credit spreads with scenario stress testing
argument-hint: "<ISIN, RIC, or CUSIP> [vs benchmark]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/analyze-bond-rv.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：シナリオ・ストレステストを伴い、利回りカーブ・クレジットスプレッドに対する債券の相対価値を分析する。

<a id="analyze-bond-relative-value"></a>
# 債券の相対価値分析

> LSEGの債券評価、利回りカーブ、クレジットカーブ、シナリオ分析ツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

価格分析、利回りカーブの状況、クレジットスプレッド分解、金利ショックのシナリオを組み合わせ、1つ以上の債券の相対価値を分析する。

スプレッドの枠組みと割高・割安評価の知識は **bond-relative-value** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-bond-identifiers"></a>
### 1. 債券識別子を集める

ユーザーへ次を尋ねる。
- 債券識別子：ISIN、RIC、CUSIP（必須）
- 比較対象のベンチマーク債券（任意）
- 評価日（任意、既定は本日）

<a id="2-price-the-bonds"></a>
### 2. 債券を評価する

識別子で `bond_price` を呼ぶ。

クリーン・ダーティ価格、利回り、デュレーション、コンベクシティ、DV01、通貨を抽出する。

ベンチマークがあれば、それも評価する。

<a id="3-get-the-risk-free-yield-curve"></a>
### 3. リスクフリー利回りカーブを取得する

債券の通貨の `interest_rate_curve` を一覧取得後に計算する。

債券の満期に合わせて補間し、Gスプレッドを求める。

<a id="4-get-the-credit-spread-curve"></a>
### 4. クレジットスプレッド・カーブを取得する

`credit_curve` を国・issuerTypeで検索した後、計算する。

残差スプレッド = 債券のGスプレッド − 同じ満期のクレジットカーブ・スプレッド。正なら割安、負なら割高。

<a id="5-run-scenario-analysis"></a>
### 5. シナリオ分析を行う

金利の平行移動 -100bp、-50bp、0bp、+50bp、+100bp で `yieldbook_scenario` を呼ぶ。

各シナリオの価格変化と損益を抽出する。

<a id="6-synthesize-the-report"></a>
### 6. レポートをまとめる

債券概要表、スプレッド分解（Gスプレッド・クレジットスプレッド・残差）、シナリオ損益表、割高・割安評価を示す。

ベンチマークがあれば並べた比較を含める。

<a id="output-format"></a>
## 出力形式

割高・割安の評価と根拠を先に示し、スプレッド分解とシナリオ表を続ける。
