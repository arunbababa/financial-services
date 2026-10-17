---
description: Review a fixed income portfolio with pricing, reference data, cashflows, and scenario analysis
argument-hint: "<ISIN1,ISIN2,...> [scenario e.g. +100bp]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/review-fi-portfolio.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：価格評価、属性データ、キャッシュフロー、シナリオ分析で債券ポートフォリオをレビューする。

<a id="review-fixed-income-portfolio"></a>
# 債券ポートフォリオのレビュー

> LSEGの債券評価、YieldBook分析、利回りカーブのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

全保有銘柄の価格評価、属性データの補完、キャッシュフロー予測、金利シナリオのストレステストで、債券ポートフォリオのリスク・リターンを統合したレポートを作る。

ポートフォリオ・シナリオ分析の知識は **fixed-income-portfolio** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-portfolio-holdings"></a>
### 1. 保有銘柄を集める

ユーザーへ次を尋ねる。
- 債券識別子（必須）：ISIN、CUSIP、RICのカンマ区切り
- ポジション量・ウェイト（任意。なければ均等ウェイト）
- 検証する特定のシナリオ（任意。例 "+100bp"。既定は標準グリッド）
- 評価日（任意、既定は本日）

<a id="2-price-all-bonds"></a>
### 2. 全債券を評価する

全識別子で `bond_price` を呼ぶ。

銘柄別にクリーン・ダーティ価格、利回り、デュレーション、コンベクシティ、DV01、通貨を抽出する。

ポートフォリオ全体の加重利回り、加重デュレーション、DV01合計、時価合計へ集計する。

<a id="3-enrich-with-reference-data"></a>
### 3. 属性データを補う

銘柄別に `yieldbook_bond_reference` を呼ぶ。

証券種別、セクター、格付け、クーポン種別、コール条項、発行体、国を抽出する。

セクター・格付け・満期区分・通貨別の構成内訳を作る。

<a id="4-project-cashflows"></a>
### 4. キャッシュフローを予測する

銘柄別に `yieldbook_cashflow` を呼ぶ。

四半期別のキャッシュフロー・ウォーターフォールへ集計し、満期が集中する期間を警告する。

<a id="5-run-scenario-analysis"></a>
### 5. シナリオ分析を行う

金利シフト -200bp、-100bp、-50bp、0bp、+50bp、+100bp、+200bp で `yieldbook_scenario` を呼ぶ。

上振れ・下振れリスクへの寄与が最も大きい銘柄を特定する。

<a id="6-curve-context"></a>
### 6. カーブの状況

ポートフォリオの主要通貨で `interest_rate_curve` を呼ぶ。

銘柄別のカーブに対するスプレッドを求め、カーブ環境を評価する。

<a id="7-synthesize-the-report"></a>
### 7. レポートをまとめる

ポートフォリオ概要指標、構成内訳、キャッシュフロー・ウォーターフォール、リスク寄与者付きシナリオ損益表、カーブへのエクスポージャーを示す。

<a id="output-format"></a>
## 出力形式

ポートフォリオ概要指標を先に示し、構成・キャッシュフロー・リスク分析を節別に詳述する。
