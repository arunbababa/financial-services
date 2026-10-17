> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/valuation-methodologies.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="valuation-methodologies-for-equity-research"></a>
# 株式調査のためのバリュエーション手法論

この参考資料は、株式調査で使用される 3 つの主要なバリュエーション手法論、つまり割引キャッシュ フロー (DCF)、類似企業比較、および類似取引事例に関する包括的なガイダンスを提供します。

<a id="table-of-contents"></a>
## 目次

1. [割引キャッシュ フロー (DCF) 分析](#discounted-cash-flow-dcf-analysis)
2. [類似企業比較分析](#trading-comparables-analysis)
3. [類似取引事例分析](#precedent-transactions-analysis)
4. [バリュエーション結果の整合](#valuation-reconciliation)

---

<a id="discounted-cash-flow-dcf-analysis"></a>
## 割引キャッシュフロー (DCF) 分析

<a id="overview"></a>
### 概要

DCF 分析では、予測される将来キャッシュ フローの現在価値に基づいて企業を評価します。これは基本的な価値創造に基づいているため、理論的に最も健全なバリュエーション手法と考えられています。

<a id="step-by-step-dcf-process"></a>
### 段階的な DCF プロセス

<a id="1-historical-financial-analysis"></a>
#### 1. 過去の財務分析
- 3 ～ 5 年分の過去の財務データを収集する
- 過去のFCFを計算：FCF = EBIT(1-Tax Rate) + D&A - CapEx - Change in NWC
- 過去の成長率と利益率を分析する
- トレンドと循環性を特定する

<a id="2-build-revenue-projections-5-10-years"></a>
#### 2. 売上高予測を立てる (5 ～ 10 年)
**アプローチ:**
- **トップダウン**: 市場規模 (TAM) → 市場シェア → 売上高から始める
- **ボトムアップ**: 販売個数 × ユニットあたりの価格
- **ハイブリッド**: 複数のドライバーを組み合わせる

**重要な考慮事項:**
- 経営陣の業績見通しと過去の成長
- 業界の成長率と市場動向
- 競争力学と市場シェアの進化
- 製品パイプラインと新たな市場機会
- マクロ経済的要因

<a id="3-project-operating-expenses"></a>
#### 3. 営業費用を予測する
- **COGS**: 売上高に対する割合 (過去の利益率を分析)
- **SG&A**: 多くの場合、半固定です。スケール効果を伴う売上高比率としてモデル化
- **研究開発**: テクノロジー/製薬にとって重要。売上高比率としてのモデル
- **D&A**: 設備投資の想定に基づく

**EBITの計算** = Revenue - COGS - Operating Expenses

<a id="4-calculate-unlevered-free-cash-flow"></a>
#### 4. アンレバード・フリーキャッシュフローを計算する
```
EBIT
× (1 - Tax Rate)
= NOPAT (Net Operating Profit After Tax)
+ Depreciation & Amortization
- Capital Expenditures
- Increase in Net Working Capital
= Unlevered Free Cash Flow (UFCF)
```

**設備投資の仮定:**
- メンテナンス設備投資: 現在の運営を維持するために必要です (通常、売上高の2～4%)
- 成長設備投資: 拡張に必要
- 業界のベンチマークと企業のガイダンスを考慮する

**純運転資本:**
- NWC = (Accounts Receivable + Inventory) - Accounts Payable
- 売上高比率または日数でモデル化 (DSO、DIO、DPO)
- NWCの増加は現金の使用です

<a id="5-determine-terminal-value"></a>
#### 5. ターミナルバリューを算定する

**方法A：永久成長法**
```
Terminal Value = FCF(final year) × (1 + g) / (WACC - g)
```
- g = 永久成長率 (通常は 2 ～ 3%、GDP 成長を超えない)
- 会社が安定した成熟成長に達した場合に使用

**方法B：エグジット・マルチプル法**
```
Terminal Value = EBITDA(final year) × Exit Multiple
```
- 現在の類似企業比較の倍率に基づきエグジット倍率を設定する
- 景気循環型事業により適している

<a id="6-calculate-weighted-average-cost-of-capital-wacc"></a>
#### 6. 加重平均資本コスト (WACC) を計算します。

```
WACC = (E/V × Cost of Equity) + (D/V × Cost of Debt × (1 - Tax Rate))
```

**株主資本コスト（CAPMを使用）:**
```
Cost of Equity = Risk-Free Rate + Beta × Equity Risk Premium
```
- リスクフリーレート: 米国10年国債利回り
- ベータ: 個別株のリターンと市場リターンの回帰分析（または類似企業のベータを使用）
- 株式リスクプレミアム: 過去の平均 ~5-6%

**負債のコスト:**
```
Cost of Debt = Risk-Free Rate + Credit Spread
```
- 会社の現在の借入金利を使用するか、債券価格から算出される借入金利を使用します
- 発行残高のある債券がない場合は信用格付けに応じて調整する

**資本構成:**
- E/V = Market value of equity / Total value
- D/V = Market value of debt / Total value
- 現在のものではなく、目標とする資本構成を使用します（大幅に異なる場合）

<a id="7-discount-cash-flows-to-present-value"></a>
#### 7. キャッシュフローを現在価値に割り引く

```
PV = Σ [FCFt / (1 + WACC)^t] + [Terminal Value / (1 + WACC)^n]
```

<a id="8-calculate-enterprise-value-and-equity-value"></a>
#### 8. 企業価値と株式価値の計算

```
Enterprise Value = PV of Projected FCF + PV of Terminal Value
Less: Net Debt (Total Debt - Cash)
Plus: Non-operating Assets
Less: Minority Interest
Less: Preferred Stock
= Equity Value

Price Per Share = Equity Value / Diluted Shares Outstanding
```

<a id="dcf-sensitivity-analysis"></a>
### DCF感度解析

主要な変数に対して常に感度分析を実行します。

1. **二元感度表**: WACC 対ターミナル成長率
2. **売上高成長シナリオ**: ベース / 強気 / 弱気のケース
3. **利益率の前提**: 営業レバレッジのシナリオ
4. **ターミナル倍率の感度**: エグジット・マルチプル法を使用する場合

**感度テーブルの例:**
```
           Terminal Growth Rate
WACC      2.0%    2.5%    3.0%
8.0%      $45     $48     $52
9.0%      $40     $43     $46
10.0%     $36     $39     $41
```

<a id="common-dcf-pitfalls-to-avoid"></a>
### 避けるべき一般的な DCF の落とし穴

1. **成長の二重計算**: 対応する投資 (設備投資、NWC) がなければ、高い成長を予測しないでください。
2. **非現実的なターミナル成長率**: 長期的な GDP 成長率を超えるべきではない
3. **景気循環を無視**: 景気循環型事業の利益を平準化する
4. **間違ったキャッシュ フローの定義**: 純利益ではなく、アンレバードFCF を使用します。
5. **一貫性のない仮定**: 割引率をキャッシュ フローに一致させる (アンレバードFCF → WACC)

---

<a id="trading-comparables-analysis"></a>
## 類似企業比較分析

<a id="overview-1"></a>
### 概要

Trading Comps は、類似企業が公開市場でどのように評価されているかに基づいて企業を評価します。これは現在の市場センチメントと相対的な評価を反映しています。

<a id="step-by-step-comps-process"></a>
### 類似企業比較の手順

<a id="1-select-comparable-companies"></a>
#### 1. 比較対象企業の選定

**選択基準:**
- 同じ業界/セクター（第一基準）
- 同様のビジネスモデルと収益源
- 同等の規模（時価総額、売上高）
- 同様の成長プロファイルと利益率
- 同様の最終市場と地域

**一般的な分析対象群:**
- 8～15社からスタート
- 特殊な事情のある企業を排除する
- 最終的な 5 ～ 10 社のセット

<a id="2-gather-financial-information"></a>
#### 2. 財務情報の収集

**必須データ:**
- 現在の株価と発行済株式数
- 直近会計年度の財務諸表
- コンセンサスに基づく翌年（NTM）の予測
- 過去の成長率

**市場指標の計算:**
- Market Cap = Share Price × Shares Outstanding
- Enterprise Value = Market Cap + Debt + Minority Interest + Preferred - Cash
- Net Debt = Total Debt - Cash & Equivalents

<a id="3-calculate-valuation-multiples"></a>
#### 3. バリュエーション倍率の計算

**企業価値に基づく評価倍率:**
- **EV/Revenue**: 初期段階/高成長企業に適しています
- **EV/EBITDA**: 最も一般的です。資本集約的なビジネスに適しています
- **EV/EBIT**: D&A が大幅に変動する場合に役立ちます

**株式価値の倍率:**
- **P/E (価格/利益)**: 最も広く使用されています
- **P/B（株価純資産倍率）**: 金融機関にとって有利
- **P/S（価格/売上）**: 不採算企業向け

**計算対象:**
- 過去 12 か月 (LTM) - 履歴
- 次の 12 か月 (NTM) - 将来の見通し (推奨)

<a id="4-analyze-and-select-multiples"></a>
#### 4. 評価倍率を分析・選定する

**比較対象会社テーブルの作成:**

| 会社名 | 時価総額 | EV/Revenue | EV/EBITDA | EV/EBIT | 株価収益率 (NTM) | 売上高成長 | EBITDA利益率 |
|---------|-----------|------------|-----------|---------|-----------|----------------|---------------|
| コンプA  | $10B      | 3.5x       | 12.0x     | 18.0x   | 22.0x     | 15%            | 28%           |
| コンプB  | $8B       | 3.0x       | 10.5x     | 16.0x   | 19.0x     | 12%            | 27%           |
| ...     | ...       | ...        | ...       | ...     | ...       | ...            | ...           |
| 中央値  | -         | **3.2x**   | **11.0x** | **17.0x** | **20.5x** | 13%            | 27.5%         |

**調整:**
- 外れ値を削除します (通常は平均から2標準偏差を超えて乖離する)
- 平均値の代わりに中央値を使用することを検討してください (外れ値の影響が少ない)
- 類似性の高い比較対象がある場合は評価倍率に重みを付ける
- 成長、利益、リスクの違いを調整する

<a id="5-apply-multiples-to-target-company"></a>
#### 5. 対象会社への評価倍率の適用

**計算例:**
```
Target Company NTM EBITDA = $500M
Selected EV/EBITDA Multiple = 11.0x
Implied Enterprise Value = $500M × 11.0x = $5,500M

Less: Net Debt = $1,000M
Equity Value = $4,500M

Shares Outstanding = 100M
Implied Price Per Share = $45.00
```

<a id="6-select-appropriate-multiple"></a>
#### 6. 適切な評価倍率を選択する

**以下に基づいて選択してください:**
- **EV/Revenue**: 高成長だが採算が取れていない企業 (テクノロジー、バイオテクノロジーで利益を得る前)
- **EV/EBITDA**: 最も一般的です。資本集約型産業 (製造業、通信業)
- **PER**: 安定した資本構成を備えた収益性の高い企業 (消費者、小売)
- **セクター別**: 銀行の場合は P/B、石油およびガスの場合は EV/生産、メディアの場合は EV/加入者

<a id="premiumdiscount-analysis"></a>
### プレミアム/割引の分析

以下に基づいてプレミアムまたは割引を適用します。
- **成長プレミアム**: より高い成長 → より高い倍率
- **収益性**: 利益率の向上 → 倍率の向上
- **規模**: 通常、大企業はプレミアム (流動性) で取引されます。
- **市場での地位**: 市場リーダー → プレミアム
- **地域**: 先進国対新興市場

---

<a id="precedent-transactions-analysis"></a>
## 類似取引事例分析

<a id="overview-2"></a>
### 概要

類似取引事例では、M&A取引において類似企業に対して支払われた価格に基づいて企業を評価します。これは、支配権プレミアムと戦略的価値を反映しています。

<a id="step-by-step-process"></a>
### 段階的なプロセス

<a id="1-identify-relevant-transactions"></a>
#### 1. 関連する取引を特定する

**選択基準:**
- 同じまたは類似の業界
- 同様のサイズ (ターゲットのサイズの 0.5 倍から 2 倍以内)
- 同様のビジネス特性
- 最近の取引 (過去 3 ～ 5 年が好ましい)
- 発表済み・完了済みの取引 (取り消された取引を避ける)

**一般的な分析対象群:**
- 最低 5 ～ 10 のトランザクション
- 最近の取引に焦点を当てる (最近の取引ほど重みが高くなります)

<a id="2-gather-transaction-details"></a>
#### 2. トランザクションの詳細を収集する

**必須情報:**
- 取引日（発表と完了）
- 買収価格と構造（現金、株式、混合）
- 取引時のターゲットの財務状況
- 戦略的根拠と相乗効果
- 支払われた支配権プレミアム

**出典:**
- SEC 提出書類 (S-4、8-K、委任状)
- プレスリリースと投資家向けプレゼンテーション
- M&A データベース (CapIQ、FactSet、Bloomberg)

<a id="3-calculate-transaction-multiples"></a>
#### 3. トランザクションのマルチプルを計算する

**類似企業比較と同じ評価倍率ですが、取引額に基づきます:**

```
Transaction Value = Equity Purchase Price + Assumed Debt - Cash Acquired

EV/Revenue (LTM) = Transaction Value / Target's LTM Revenue
EV/EBITDA (LTM) = Transaction Value / Target's LTM EBITDA
EV/EBIT (LTM) = Transaction Value / Target's LTM EBIT
```

**支配権プレミアムの計算:**
```
Control Premium = (Offer Price - Unaffected Price) / Unaffected Price
```
- 買収発表の影響を受けていない株価 = 発表の 1 ～ 2 日前のターゲットの株価
- 通常の範囲: 20 ～ 40%

<a id="4-analyze-precedent-transactions"></a>
#### 4. 類似取引事例の分析

**類似取引事例 テーブルの作成:**

| 日付 | ターゲット | 取得者 | 取引額 | EV/Revenue | EV/EBITDA | プレミアム | 理論的根拠 |
|------|--------|----------|------------|------------|-----------|---------|-----------|
| Q1'24 | コンプX | 購入者A | $5.0B | 4.0x | 14.0x | 35% | 市場の統合 |
| Q3'23 | CompY | 購入者B | $3.5B | 3.5x | 12.5x | 28% | 戦略的適合 |
| 中央値 | - | - | - | **3.8x** | **13.0x** | **31%** | - |

<a id="5-apply-to-target-company"></a>
#### 5. 対象会社への適用

**重要な考慮事項:**
- 通常、類似取引事例の評価倍率は類似企業比較よりも高い（支配権プレミアムを含む）
- 取引根拠の違いを調整する
- 取引時の市場状況と現在の市場状況を考慮する
- 最近のトランザクションをより重視する

**計算例:**
```
Target Company LTM EBITDA = $450M
Selected EV/EBITDA Multiple = 13.0x (precedent)
vs Trading Comps Multiple = 11.0x

Implied EV (Precedent) = $450M × 13.0x = $5,850M
Implied EV (Trading) = $450M × 11.0x = $4,950M

Implied Control Premium = $5,850M / $4,950M - 1 = 18%
```

<a id="adjustments-to-transaction-multiples"></a>
### 取引倍率の調整

**次の調整を検討してください:**
- **市場状況**: 強気市場対弱気市場 (M&A 活動レベル)
- **取引構造**: 戦略的買い手と財務的買い手
- **シナジー**: 高いシナジーを伴う取引にはプレミアムがかかります
- **競争力学**: 単一の入札者と複数の入札者
- **時間値**: 古いトランザクションは関連性が低い

---

<a id="valuation-reconciliation"></a>
## バリュエーション結果の整合

<a id="creating-a-valuation-bridge"></a>
### 評価ブリッジの作成

3 つのメソッドすべてを単一のフレームワークで提示します。

**評価概要の例:**

| 方法 | 企業価値 | 株式価値 | 1株当たり価格 | 重み | 加重価値 |
|--------|------------------|--------------|-------------|--------|---------------|
| DCF解析 | $5,200M | $4,200M | $42.00 | 50% | $21.00 |
| 類似企業比較 | $5,500M | $4,500M | $45.00 | 30% | $13.50 |
| 類似取引事例 | $5,850M | $4,850M | $48.50 | 20% | $9.70 |
| **加重平均** | - | - | **$44.20** | - | **$44.20** |

<a id="weighting-the-methods"></a>
### メソッドの重み付け

**一般的な重み付け:**
- **DCF**: 40-60% (ファンダメンタルズに基づく価値だが、予測の精度を前提としています)
- **類似企業比較**: 25-40% (現在の市場センチメントを反映)
- **類似取引事例**: 15-25% (M&A の可能性がない限り関連性は低い)

**以下に基づいて重みを調整します:**
- **予測の信頼性**: 信頼性が高い → DCF 重みが高い
- **市場状況**: 強気/弱気市場はコンプの信頼性に影響を与えます
- **M&A の可能性**: 企業が買収対象となっている場合、または業界が統合されている場合はより高くなります。
- **企業の成熟度**: 成熟した企業 → 類似企業比較の比重が高くなります。成長 → DCF ウェイトの増加

<a id="valuation-range"></a>
### 評価範囲

点推定値ではなく、常に評価範囲を提示します。

**アプローチ:**
- **基本ケース**: 最も可能性の高いシナリオ
- **強気の場合**: 楽観的な仮定 (売上高成長、利益率)
- **ベアケース**: 保守的な仮定

**例:**
```
Bear Case: $38 - $40
Base Case: $42 - $46
Bull Case: $48 - $52

Recommendation: BUY with target price of $45 (midpoint of base case)
```

<a id="sanity-checks"></a>
### 妥当性チェック

**評価を以下と照合します:**
1. **歴史的な倍率**: 現在の評価額は歴史と一致していますか?
2. **同業他社との比較**: 同業他社と比較して、根拠のあるプレミアム/ディスカウントはありますか?
3. **織り込み成長率**: 市場はどのような成長を織り込んでいますか?
4. **想定リターン**: 現在株価から目標株価までの IRR
5. **時価総額分析**: 時価総額の合計は意味がありますか?

---

<a id="conclusion"></a>
## 結論

3 つのバリュエーション手法をすべて使用すると、公正価値を決定するための堅牢なフレームワークが提供されます。

- **DCF** はファンダメンタルズに基づく本源的価値を提供します
- **類似企業比較**は現在の市場評価を反映しています
- **類似取引事例**はM&A価値と支配権プレミアムを示します

重要なのは、各手法の前提条件を理解し、複数のシナリオと手法を考慮した合理的な評価範囲を提示することです。
