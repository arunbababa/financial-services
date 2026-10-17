---
description: Analyze the bond futures basis with CTD identification, implied repo rate, and basis trade assessment
argument-hint: "<bond future RIC e.g. FGBLc1>"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/analyze-bond-basis.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：CTDの特定、インプライド・レポレート、ベーシス取引の評価により債券先物ベーシスを分析する。

<a id="analyze-bond-futures-basis"></a>
# 債券先物ベーシスの分析

> LSEGの債券先物評価、債券評価、利回りカーブ、過去データのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

先物価格の評価、最割安受渡適格銘柄（CTD）の特定、グロス・ネットベーシスの計算、ベーシス取引機会の評価を行う。

仕組みと取引戦略の専門知識は **bond-futures-basis** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-input"></a>
### 1. 入力を集める

ユーザーへ次を尋ねる。
- 債券先物RIC（必須）：例 FGBLc1（Euro Bund）、TYc1（米10年国債）、FFIc1（英Gilt）
- 市場データ日（任意、既定は本日）

<a id="2-price-the-bond-future"></a>
### 2. 債券先物を評価する

先物RICを指定して `bond_future_price` を呼ぶ。

理論価格、CTD銘柄識別子、交換比率付きの受渡適格銘柄群、契約DV01、受渡日を抽出する。

<a id="3-price-the-ctd-bond"></a>
### 3. CTD債券を評価する

手順2のCTD識別子で `bond_price` を呼ぶ。

クリーン・ダーティ価格、利回り、デュレーション、DV01、経過利息、クーポンを抽出する。

グロスベーシス、受渡代金、キャリー、ネットベーシスを計算する。

<a id="4-compute-implied-repo-rate"></a>
### 4. インプライド・レポレートを計算する

先物の通貨の `interest_rate_curve` を一覧取得後に計算する。短期金利をレポ金利の代替指標に使う。

インプライド・レポレートを計算し、市場のレポ金利と比べる。

<a id="5-track-historical-basis"></a>
### 5. ベーシスの履歴を追う

先物とCTD債券の両方に、`tenor: "3M"`、`interval: "P1D"` で `tscc_historical_pricing_summaries` を呼ぶ。

ベーシスのトレンド、ボラティリティ、過去の範囲を評価する。

<a id="6-sovereign-credit-context"></a>
### 6. ソブリン信用の状況

該当国（例：Bundは "DE"、米国債は "US"）の `credit_curve` を呼ぶ。

<a id="7-synthesize-the-report"></a>
### 7. レポートをまとめる

先物概要表、CTD債券分析、ベーシス計算表（グロス・ネットベーシス、インプライド対市場レポ金利）、過去の状況、取引提言（ロングベーシス／ショートベーシス／中立）を示す。

<a id="output-format"></a>
## 出力形式

ベーシス取引の評価（ロング／ショート／中立）とインプライド・レポ比較を先に示し、詳細な分析表を続ける。
