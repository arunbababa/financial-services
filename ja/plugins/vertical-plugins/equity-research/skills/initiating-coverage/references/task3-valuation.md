> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task3-valuation.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="task-3-valuation-analysis---detailed-workflow"></a>
# タスク 3: バリュエーション分析 - 詳細なワークフロー

このドキュメントでは、カバレッジ開始スキルのタスク 3 (バリュエーション分析) を実行するための段階的な手順を説明します。

<a id="task-overview"></a>
## タスクの概要

**目的**: DCF、類似企業比較、類似取引事例を用いて包括的にバリュエーションを行います。

**前提条件**: ⚠️ 開始する前に確認してください
- **必須**: タスク 2 の財務モデル
  - 予想損益計算書
  - 予測キャッシュフロー
  - 売上高とEBITDAの予測
  - DCF 入力 (アンレバードFCF)

**⚠️ 重要: タスク 2 が完了するまではこのタスクを開始しないでください**

このタスクにはタスク 2 の財務モデルが必要です。これを使用せずに開始すると、作業が不完全になります。

**タスク 2 が完了していない場合**: 直ちに停止し、最初にタスク 2 (財務モデリング) を完了する必要があることをユーザーに通知します。続行したり、プレースホルダー評価を作成したりしないでください。

**出力**: バリュエーション分析 (4 ～ 6 ページ + Excel タブ)
- 感度テーブルを使用した DCF 解析
- 類似会社比較分析
- 類似取引事例 (該当する場合)
- バリュエーション・フットボールフィールド
- 目標株価と投資判断

---

<a id="input-verification"></a>
## 入力検証

**始める前に - チェックしてください:**
- [ ] タスク 2 は完了しましたか? (財務モデルは存在します)
- [ ] モデル ファイルのパス/場所はわかっていますか?
- [ ] モデルから予測財務情報にアクセスできますか?

**モデルから必須:**
- [ ] 予測FCF（5年）
- [ ] 売上高予測
- [ ] EBITDA予測
- [ ] 最終年度の指標
- [ ] 貸借対照表データ (負債、現金、株式)

**検証が失敗した場合**: 続行する前に、作業を停止し、先にタスク2（財務モデリング）を完了してください。

---

<a id="detailed-methodology-reference"></a>
## 詳細な方法論のリファレンス

バリュエーション手法、計算式、理論の詳細については、以下を参照してください。
**[バリュエーション手法.md](valuation-methodologies.md)**

このワークフロー ドキュメントは、実行ステップに焦点を当てています。以下については方法論ファイルを参照してください。
- DCFの理論と公式
- WACC計算の詳細
- ターミナルバリューの算定方法
- 類似会社比較理論
- 類似取引事例理論

---

<a id="step-by-step-valuation-workflow"></a>
## 段階的なバリュエーションのワークフロー

<a id="step-1-extract-data-from-financial-model"></a>
### ステップ 1: 財務モデルからデータを抽出する

**タスク2の財務モデルから以下を抽出:**

1. **財務予測 (5 年間)**
   - 年度別売上高 (2025E-2029E)
   - 年別EBITDA
   - 年別EBIT
   - 税率
   - 年別のD&A
   - 年別の設備投資
   - NWCの年次変化

2. **アンレバード・フリーキャッシュフロー**
   ```
   Extract from DCF Inputs tab in financial model:

                   2025E   2026E   2027E   2028E   2029E
   EBIT            $XXX    $XXX    $XXX    $XXX    $XXX
   × (1 - Tax Rate)
   = NOPAT         $XXX    $XXX    $XXX    $XXX    $XXX
   + D&A           $XXX    $XXX    $XXX    $XXX    $XXX
   - CapEx         ($XX)   ($XX)   ($XX)   ($XX)   ($XX)
   - Chg in NWC    ($XX)   ($XX)   ($XX)   ($XX)   ($XX)
   = Unlevered FCF $XXX    $XXX    $XXX    $XXX    $XXX
   ```

3. **貸借対照表データ (現在)**
   - 有利子負債総額
   - 現金及び現金同等物
   - 純有利子負債（有利子負債 - 現金）
   - 希薄化後の発行済株式数

4. **シナリオデータ**
   - 強気ケースの売上高CAGRと最終年度利益率
   - 基本ケースの売上高CAGRと最終年度利益率
   - 弱気ケースの売上高CAGRと最終年度利益率

<a id="step-2-build-dcf-analysis"></a>
### ステップ 2: DCF 解析を構築する

<a id="a-calculate-wacc"></a>
#### A. WACC を計算する

**1.リスクフリーレートの決定**
   - 米国10年国債利回りを使用します (現在の金利を確認してください)
   - 例: 2024 年末時点で 4.0 ～ 4.5%

**2.株主資本コスト（CAPM） の決定**
   ```
   Cost of Equity = Risk-Free Rate + Beta × Equity Risk Premium

   Inputs:
   - Risk-Free Rate: [Current 10-year Treasury, e.g., 4.2%]
   - Beta: [Company beta from Bloomberg/FactSet or peer average]
   - Equity Risk Premium: 5-6% (historical average)

   Example:
   Cost of Equity = 4.2% + 1.3 × 5.5% = 11.35%
   ```

**3.負債コストの決定**
   ```
   Cost of Debt = Current borrowing rate or implied yield on bonds

   For private companies:
   Cost of Debt = Risk-Free Rate + Credit Spread (based on rating)

   Example:
   Cost of Debt (pre-tax) = 6.5%
   Cost of Debt (after-tax) = 6.5% × (1 - 25% tax rate) = 4.875%
   ```

**4.資本構成の決定**
   ```
   Use market values (not book values):

   Market Value of Equity (E) = Share Price × Shares Outstanding
   Market Value of Debt (D) = Total Debt (use book value if bonds not traded)
   Total Value (V) = E + D

   Weight of Equity = E / V
   Weight of Debt = D / V

   Example:
   E = $5,000M (90.9%)
   D = $500M (9.1%)
   V = $5,500M (100%)
   ```

**5. WACCの計算**
   ```
   WACC = (E/V × Cost of Equity) + (D/V × Cost of Debt × (1 - Tax Rate))

   Example:
   WACC = (90.9% × 11.35%) + (9.1% × 6.5% × (1 - 25%))
   WACC = 10.32% + 0.44% = 10.76%

   Round to: 10.8% for base case
   ```

<a id="b-calculate-terminal-value"></a>
#### B. ターミナルバリューの計算

**方法1：永久成長法 (推奨)**
```
Terminal Value = FCF(2029) × (1 + g) / (WACC - g)

Where:
- FCF(2029) = Final year unlevered FCF from model
- g = Perpetual growth rate (typically 2.0-3.0%)
  - Should not exceed long-term GDP growth
  - Use 2.5% as base case

Example:
FCF(2029) = $500M
g = 2.5%
WACC = 10.8%

Terminal Value = $500M × (1.025) / (0.108 - 0.025)
Terminal Value = $512.5M / 0.083 = $6,175M
```

**方法2：エグジット・マルチプル法 (代替)**
```
Terminal Value = EBITDA(2029) × Exit Multiple

Where:
- Exit Multiple = Current peer trading median (e.g., 12-15x EBITDA)

Example:
EBITDA(2029) = $800M
Exit Multiple = 13x

Terminal Value = $800M × 13x = $10,400M
```

**いずれかの方法を選択するか、両方の平均を選択します。**

<a id="c-discount-cash-flows-to-present-value"></a>
#### C. キャッシュ フローを現在価値に割り引く

```
PV of Projected FCF = Σ [FCFt / (1 + WACC)^t] for t = 1 to 5

Example:
Year    FCF      Discount    PV of FCF
        ($M)     Factor      ($M)
2025    $250     1/(1.108)^1 = 0.9026    $226
2026    $320     1/(1.108)^2 = 0.8147    $261
2027    $390     1/(1.108)^3 = 0.7353    $287
2028    $450     1/(1.108)^4 = 0.6636    $299
2029    $500     1/(1.108)^5 = 0.5988    $299
                              Total PV:  $1,372M

PV of Terminal Value = Terminal Value / (1 + WACC)^5
PV of Terminal Value = $6,175M / (1.108)^5 = $6,175M × 0.5988 = $3,697M

Enterprise Value = $1,372M + $3,697M = $5,069M
```

<a id="d-calculate-equity-value-and-price-per-share"></a>
#### D. 株式価値と一株当たり価格の計算

```
Enterprise Value                 $5,069M
- Net Debt (Debt - Cash)         ($450M)
+ Non-operating Assets           $0M
- Minority Interest              $0M
- Preferred Stock                $0M
= Equity Value                   $4,619M

Diluted Shares Outstanding       100M

Price Per Share = $4,619M / 100M = $46.19

Current Stock Price: $42.00
Implied Upside: 10.0%
```

<a id="e-dcf-sensitivity-analysis-critical"></a>
#### E. DCF 感度分析 **重要**

**表 1: WACC 対ターミナル成長率**

双方向感度テーブルを作成します。
```
Price Per Share ($)     Terminal Growth Rate
WACC        1.5%    2.0%    2.5%    3.0%    3.5%
9.0%        $52     $55     $59     $63     $68
9.5%        $48     $51     $54     $58     $62
10.0%       $45     $48     $51     $54     $57
10.5%       $42     $45     $47     $50     $53
11.0%       $40     $42     $44     $47     $50
11.5%       $38     $40     $42     $44     $47
12.0%       $36     $38     $40     $42     $44

Base Case: WACC = 10.8%, g = 2.5% → $46
Format as heatmap: Green (high values) → Yellow → Red (low values)
```

**表 2: 売上高CAGR対最終年度EBITDA利益率**
```
Price Per Share ($)     Terminal EBITDA Margin (2029E)
Revenue CAGR    28%     30%     32%     34%     36%
15%             $38     $42     $46     $50     $54
20%             $42     $46     $51     $56     $61
25%             $46     $51     $56     $62     $68
30%             $51     $56     $62     $68     $75
35%             $56     $62     $68     $75     $83

Base Case: Rev CAGR = 25%, EBITDA Margin = 32% → $56
```

<a id="step-3-comparable-companies-analysis"></a>
### ステップ 3: 類似会社分析

<a id="a-select-comparable-companies"></a>
#### A. 比較対象企業の選択

**選択基準:**
- 同じ業界/セクター (主な要件)
- 同様のビジネスモデル
- 同等の規模（時価総額、売上高）
- 同様の成長プロファイル
- 類似した事業展開地域

**5 ～ 10 社の同業他社を特定します:**
1. [ピア 1] - 直接の競合他社
2. [ピア 2] - 直接の競合他社
3. [ピア 3] - 隣接するプレーヤー
4. [ピア 4] - 同様のビジネス モデル
5. [ピア 5] - 地域の競合他社
6. [さらに 3 ～ 5 個追加]

**選択した各ピアの根拠を文書化します。**

<a id="b-gather-peer-financial-data"></a>
#### B. 同業の財務データを収集する

**それぞれの比較対象について、以下を収集します。**
- 現在の株価
- 発行済株式数（希薄化後）
- 時価総額
- 有利子負債総額と現金残高（EV計算用）
- 企業価値
- LTM (過去 12 か月) の財務:
  - 売上高
  - EBITDA
  - EBIT
  - 当期純利益
- NTM (次の 12 か月) コンセンサス予測
- 売上高成長率
- EBITDA利益率

**データソース:**
- FactSet、CapitalIQ、Bloomberg (推奨)
- 会社の実績値の 10-Ks/10-Qs
- Yahoo Finance、Seeking Alpha からのコンセンサス推定 (プロツールが利用できない場合)

<a id="c-calculate-valuation-multiples"></a>
#### C. バリュエーション倍率の計算

**ピアごとに、以下を計算します。**
```
EV/Revenue (LTM) = Enterprise Value / LTM Revenue
EV/Revenue (NTM) = Enterprise Value / NTM Revenue (est.)
EV/EBITDA (LTM) = Enterprise Value / LTM EBITDA
EV/EBITDA (NTM) = Enterprise Value / NTM EBITDA (est.)
P/E (NTM) = Market Cap / NTM Net Income (est.)
```

<a id="d-create-comparable-companies-table-mandatory-format"></a>
#### D. 比較対象会社表の作成（必須形式）

```
COMPARABLE COMPANIES ANALYSIS

Company      Ticker  Mkt Cap  EV/Rev  EV/Rev  EV/EBITDA  EV/EBITDA  P/E   Rev     EBITDA
                     ($B)     LTM     NTM     LTM        NTM        NTM   Growth  Margin
Peer A       PRA     45.2     3.5x    3.2x    15.2x      13.8x      25x   18%     23%
Peer B       PRB     32.8     3.2x    2.9x    14.1x      12.5x      22x   15%     23%
Peer C       PRC     28.5     2.8x    2.6x    12.8x      11.2x      20x   12%     22%
Peer D       PRD     52.1     4.1x    3.7x    17.5x      15.2x      29x   22%     23%
Peer E       PRE     38.9     3.6x    3.3x    15.8x      14.1x      25x   17%     23%
Peer F       PRF     41.2     3.7x    3.4x    16.1x      13.9x      26x   19%     23%
Peer G       PRG     35.5     3.3x    3.0x    14.5x      12.8x      23x   16%     22%

[Target]     TRGT    38.0     3.4x    3.1x    14.8x      13.0x      24x   17%     23%

STATISTICAL SUMMARY
Maximum              52.1     4.1x    3.7x    17.5x      15.2x      29x   22%     23%
75th Percentile      45.2     3.7x    3.4x    16.1x      14.1x      26x   19%     23%
Median               38.9     3.5x    3.2x    15.2x      13.8x      25x   17%     23%
25th Percentile      32.8     3.2x    2.9x    14.1x      12.5x      22x   15%     22%
Minimum              28.5     2.8x    2.6x    12.8x      11.2x      20x   12%     22%

Note: Market data as of [Date]. LTM = Last Twelve Months. NTM = Next Twelve Months.
Source: FactSet, company filings, [Analyst] estimates.
```

**重要**: 統計概要 (最大値/第75百分位/中央値/第25百分位/最小値) は必須です。

<a id="e-apply-multiples-to-target-company"></a>
#### E. 対象会社に評価倍率を適用する

**主要倍率を選択してください (通常、成熟した企業の場合は EV/EBITDA):**

```
Target Company NTM EBITDA = $550M (from financial model)

Apply Median Peer Multiple:
Peer Median EV/EBITDA (NTM) = 13.8x
Implied EV = $550M × 13.8x = $7,590M

Apply 25th Percentile (Conservative):
25th Percentile EV/EBITDA (NTM) = 12.5x
Implied EV = $550M × 12.5x = $6,875M

Apply 75th Percentile (Optimistic):
75th Percentile EV/EBITDA (NTM) = 14.1x
Implied EV = $550M × 14.1x = $7,755M

Valuation Range (Comps): $6,875M - $7,755M
Midpoint: $7,315M

Convert to Equity Value:
Implied EV (Median)        $7,590M
- Net Debt                 ($450M)
= Implied Equity Value     $7,140M

Shares Outstanding         100M
Implied Price/Share        $71.40
```

**プレミアム/割引を正当化する:**
- 対象企業は17%成長、同業他社中央値は 17% → 同水準
- 対象企業のEBITDA利益率23%対同業他社中央値23% → 同水準
- 対象企業の市場での地位 → [プレミアム/割引を正当化する]
- **結論**: 中央値の評価倍率を適用する (調整なし)

<a id="step-4-precedent-transactions-optional"></a>
### ステップ 4: 類似取引事例 (オプション)

**注**: M&A がこのセクター/企業に関連する場合のみ。

<a id="a-identify-relevant-transactions"></a>
#### A. 関連する取引を特定する

**5 ～ 10 件の M&A 取引を検索:**
- 同じ業界、過去 3 ～ 5 年
- 同様のサイズ (ターゲットのサイズの 0.5 倍から 2 倍)
- 発表された取引と完了した取引

**例:**
```
PRECEDENT TRANSACTIONS ANALYSIS

Date     Target        Acquirer      Deal     EV/Rev  EV/EBITDA  Premium  Rationale
                                    Value($B)  LTM     LTM
Q1 2024  Comp A       Strategic      $5.2B    4.2x    16.5x      35%      Consolidation
Q3 2023  Comp B       PE Firm        $3.8B    3.8x    14.2x      28%      Platform
Q4 2023  Comp C       Strategic      $4.5B    4.0x    15.8x      32%      Geographic
Q2 2023  Comp D       Strategic      $6.1B    4.5x    17.2x      38%      Strategic fit
Q1 2023  Comp E       PE Firm        $3.2B    3.5x    13.5x      25%      Carve-out

Median                                        4.0x    15.8x      32%

Source: CapitalIQ, company filings, press releases.
```

<a id="b-apply-to-target-company"></a>
#### B. 対象会社への適用

```
Target Company LTM EBITDA = $500M
Precedent Median EV/EBITDA (LTM) = 15.8x

Implied EV (Precedent) = $500M × 15.8x = $7,900M

Note: Precedent multiples typically 10-20% higher than trading comps
due to control premium and synergies.
```

<a id="step-5-valuation-reconciliation"></a>
### ステップ 5: バリュエーション結果の整合

<a id="a-create-valuation-summary-table"></a>
#### A. 評価集計表の作成

```
VALUATION SUMMARY

Method                  Low     Base    High    Weight  Weighted Value
DCF Analysis            $42     $46     $51     50%     $23.00
Trading Comps (NTM)     $64     $71     $78     40%     $28.40
Precedent Trans.        $70     $79     $88     10%     $7.90
                                                        -------
Weighted Average Target                         100%    $59.30

Rounded Price Target: $59.00

Current Price (as of [Date]):    $42.00
Upside to Target:                40% ($59.00 / $42.00 - 1)
```

<a id="b-determine-weighting-rationale"></a>
#### B. 重み付けの根拠を決定する

**一般的な重み付け:**
- DCF: 40-60% (予測が信頼できる場合はさらに高くなります)
- 類似企業比較: 25-40% (市場センチメントを反映)
- 類似取引事例: 10-25% (M&A の可能性がない限りこれより低い)

**この例の場合:**
- DCF 50%: 予測に対する高い信頼性
- Comps 40%: 強力なピアセット
- 類似取引事例10%: 短期的には M&A の可能性は低い

<a id="c-create-valuation-football-field-chart"></a>
#### C. バリュエーション・フットボールフィールド・チャートの作成

```
VALUATION FOOTBALL FIELD

Method                  Low ◄────────── Range ──────────► High

DCF Analysis            $42 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ $51

Trading Comps (NTM)     $64 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ $78

Precedent Trans.        $70 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ $88
                                          ↑
                                    Current: $42
─────────────────────────────────────────────────────────
Valuation Range         $42                          $88
Price Target: $59 (weighted average)

Color code:
- DCF: Blue
- Trading Comps: Green
- Precedent Trans: Orange
- Vertical line at current price: Red dashed
- Vertical line at target: Black solid
```

<a id="d-scenario-based-valuations"></a>
#### D. シナリオに基づく評価

```
VALUATION BY SCENARIO

Scenario    Probability  Revenue  EBITDA    DCF      Comps    Weighted
                        CAGR     Margin    Value    Multiple  Avg
Bear Case   20%         18%      28%       $38      11.5x     $42
Base Case   60%         25%      32%       $46      13.8x     $59
Bull Case   20%         32%      36%       $58      16.0x     $82

Expected Value (probability-weighted): $59
```

<a id="step-6-final-price-target--recommendation"></a>
### ステップ 6: 最終的な目標株価と投資判断

```
═══════════════════════════════════════════════════════════
INVESTMENT RECOMMENDATION
═══════════════════════════════════════════════════════════

Current Price:          $42.00 (as of [Date])
Price Target:           $59.00 (12-month)
Upside/(Downside):      +40.5%

Rating:                 BUY / OUTPERFORM

Valuation Methodology:  Based on weighted average of DCF (50%),
                       trading comparables (40%), and precedent
                       transactions (10%).

Time Horizon:          12 months

───────────────────────────────────────────────────────────
KEY INVESTMENT CATALYSTS
───────────────────────────────────────────────────────────

1. New Product Launch (Q2 2025)
   - Expected to drive 15-20% revenue acceleration
   - Already seeing strong pre-orders

2. Margin Expansion (FY2025-2026)
   - Operating leverage from scale
   - Path to 35% EBITDA margin (from current 28%)

3. Market Share Gains (Ongoing)
   - Taking share from legacy competitors
   - Net Promoter Score improvement

4. International Expansion (H2 2025)
   - Entry into European markets
   - Potential $200M incremental revenue opportunity

5. Potential M&A Target (12-18 months)
   - Strategic fit for larger players
   - Precedent transactions suggest 30-40% premium

───────────────────────────────────────────────────────────
KEY RISKS TO PRICE TARGET
───────────────────────────────────────────────────────────

Downside Risks:
1. Competitive Pressure (High probability, -15% impact)
   - New entrant launched competing product
   - Could pressure pricing and market share

2. Execution Risk (Medium probability, -10% impact)
   - New product launch delays or underperformance
   - Management turnover

3. Macro Slowdown (Medium probability, -20% impact)
   - Economic recession would impact customer spending
   - Operating leverage would reverse

4. Regulatory Risk (Low probability, -25% impact)
   - Potential new regulations in key market
   - Would increase compliance costs

Upside Risks:
1. M&A Bid (Low probability, +35% impact)
   - Strategic acquirer pays control premium

2. Beat-and-Raise (Medium probability, +10% impact)
   - Consistent outperformance vs. estimates

═══════════════════════════════════════════════════════════
```

---

<a id="quality-standards"></a>
## 品質基準

<a id="dcf-quality-checks"></a>
### DCFの品質チェック
- [ ] WACC は文書化されたコンポーネントを使用して適切に計算されます
- [ ] 妥当なターミナルバリュー (企業価値総額の 70% 未満)
- [ ] 感度分析は現実的な範囲をカバーします (WACC の場合は ±200 ～ 300 bps、ターミナル成長率の場合は ±100 bps)
- [ ] EBITから適切に計算された非レバレッジFCF
- [ ] 企業価値と株式価値の橋渡しが正しい
- [ ] 株式数は基本株式数ではなく、希薄化株式数です

<a id="comparables-quality-checks"></a>
### 比較対象の品質チェック
- [ ] 5～10社の類似企業を選択
- [ ] 根拠を説明できる同業他社の選定 (各ピアが選ばれた理由を文書化)
- [ ] 統計概要が含まれます (最大値/第75百分位/中央値/第25百分位/最小値) - 必須
- [ ] 評価倍率の選択が適切 (成熟期の場合は EV/EBITDA、高成長期の場合は EV/売上高)
- [ ] 特定の要因によって正当化されるプレミアム/割引
- [ ] データは適切に入手され、日付が記載されている

<a id="overall-valuation-quality-checks"></a>
### 総合評価の品質チェック
- [ ] 少なくとも 2 つのバリュエーション手法を使用 （最低限、DCF + 類似企業比較）
- [ ] 重み付けの説明と適切性
- [ ] 単なるポイント推定ではなく、提供される評価範囲（低位/基本/高位）
- [ ] 分析されたシナリオ (強気/ベース/弱気)
- [ ] 実行された妥当性チェック (以下を参照)
- [ ] すべての仮定は根拠とともに文書化されています

---

<a id="sanity-checks"></a>
## 妥当性チェック

**次の検証チェックを常に実行してください:**

1. **過去の評価倍率との比較**
   - 算出される評価倍率は企業の過去の取引レンジと一致していますか?
   - そうでない場合は、その理由を説明してください

2. **ピア比較**
   - プレミアム/ディスカウントと他社との比較はファンダメンタルズに基づいて正当化されますか?
   - 確認項目：成長率、利益率、市場での地位

3. **織り込み成長率チェック**
   - 市場は現在の価格でどの程度の成長を織り込んでいますか?
   - 会社のこれまでの軌跡を考慮すると、それは合理的でしょうか?

4. **時価総額の妥当性**
   - 企業の規模や同業他社を考慮すると、時価総額の合計は意味があるのでしょうか?
   - 業界に比べて会社は大きすぎるのでしょうか、または小さすぎるのでしょうか?

5. **ターミナルバリューの確認**
   - ターミナルバリューは企業価値全体の 60 ～ 70% 未満ですか?
   - > 70% の場合、予測が十分な長さではない可能性があります

6. **WACC の合理性**
   - 一般的な企業の WACC は 8 ～ 14% の範囲ですか?
   - ハイテク/高成長: 10-14%
   - 成熟/安定: 7-10%

7. **想定リターンの確認**
   - 現在の価格から 12 か月にわたる目標までの IRR はどれくらいですか?
   - それは投資判断と一致していますか?

---

<a id="output-files"></a>
## 出力ファイル

次の成果物を作成します。

<a id="1-valuation-analysis-document"></a>
### 1. バリュエーション分析書
**ファイル**: `[Company]_Valuation_Analysis_[Date].md` (分析書面)

**目次** (4 ～ 6 ページ):
- 目標株価を含むエグゼクティブサマリー
- DCF解析（1ページ）感度表付き
- 比較企業分析（1ページ）と統計概要
- 類似取引事例 (0.5 ページ) (該当する場合)
- バリュエーション概要とフットボールフィールド (0.5 ページ)
- 投資に関する推奨事項 (1 ページ)
- 主要なカタリストとリスク (1 ページ)

<a id="2-excel-valuation-tabs"></a>
### 2. Excel の評価タブ
**タスク 2 の財務モデル ファイルに追加します:** `[Company]_Financial_Model_[Date].xlsx`

**重要**: 別の Excel ファイルを作成しないでください。これらのタブをタスク 2 の既存の財務モデルに追加します。これにより、すべての定量的データが 1 か所に保持されます。

**追加するタブ:**
- 完全な計算を含む DCF タブ
- 感度分析タブ
- ピアデータを含む「Comps」タブ
- [類似取引事例] タブ (該当する場合)
- 評価概要タブ

---

<a id="success-criteria"></a>
## 成功基準

バリュエーション分析を成功させるには、次のことが必要です。
1. 少なくとも 2 つの方法を使用します (DCF + Comps が最低)
2. 包括的な DCF 感度分析を含む (2 元テーブル)
3. 類似企業比較に統計的な概要を含めます (最大値/第75百分位/中央値/第25百分位/最小値)
4. ポイント推定ではなく、評価範囲 (低位/基本/高位) を提供します
5. すべての重要な前提を明確な根拠とともに文書化する
6. 妥当性チェックを実行する
7. 根拠を説明できる目標株価に到達
8. 明確な買い/保有/売りの投資判断を提供する
9. 3 ～ 5 つの主要なカタリストを特定する
10. 3 ～ 5 つの主要なリスクを特定する
11. 監査可能で透明性があること

---

<a id="next-steps"></a>
## 次のステップ

タスク 3 を完了すると、バリュエーション分析は次の目的で使用されます。
- **タスク 4 (チャート)**: DCF 感度ヒートマップ、バリュエーション・フットボールフィールド、シナリオ比較チャートを作成する
- **タスク 5 (レポート作成)**: バリュエーション分析を最終レポートに統合する

目標株価と投資判断は、株式調査レポートの最終的な投資推奨の基礎となります。
