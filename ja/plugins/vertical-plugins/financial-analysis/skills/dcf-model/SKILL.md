---
name: dcf-model
description: Real DCF (Discounted Cash Flow) model creation for equity valuation. Retrieves financial data from SEC filings and analyst reports, builds comprehensive cash flow projections with proper WACC calculations, performs sensitivity analysis, and outputs professional Excel models with executive summaries. Use when users need to value a company using DCF methodology, request intrinsic value analysis, or ask for detailed financial modeling with growth projections and terminal value calculations.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/financial-analysis/skills/dcf-model/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：株式評価のための実質 DCF (割引キャッシュ フロー) モデルの作成。 SEC 提出書類やアナリストレポートから財務データを取得し、適切な WACC 計算を使用して包括的なキャッシュ フロー予測を構築し、感度分析を実行して、エグゼクティブ サマリーを含むプロフェッショナルな Excel モデルを出力します。ユーザーが DCF 手法を使用して企業を評価する必要がある場合、本質的価値分析を要求する場合、または成長予測と継続価値の計算を含む詳細な財務モデリングを要求する必要がある場合に使用します。

<a id="dcf-model-builder"></a>
# DCFモデルビルダー

<a id="overview"></a>
## 概要

このスキルは、投資銀行標準に従って株式評価のための機関品質の DCF モデルを作成します。各分析により、詳細な Excel モデルが生成されます (DCF シートの下部に感度分析が含まれています)。

<a id="tools"></a>
## ツール

- デフォルトでは、データ ソースに使用できるユーザーおよび MCP サーバーによって提供されるすべての情報が使用されます。

<a id="critical-constraints---read-these-first"></a>
## 重要な制約 - 最初にお読みください

これらの制約は、すべての DCF モデル構築全体に適用されます。始める前に確認してください:

**環境: Office JS と Python/openpyxl:**
- **Excel 内で実行している場合 (Office アドイン / Office JS 環境):** Office JS を直接使用します。Python/openpyxl は使用しないでください。 `range.formulas = [["=D19*(1+$B$8)"]]` 経由で数式を記述します。別の再計算ステップは必要ありません。 Excel はネイティブに計算します。スタイリングには `range.format.*` を使用してください。ハードコードよりも数式を優先するという同じルールが適用されます。派生セルには `.formulas` を設定し、決して `.values` を設定しません。
- **スタンドアロン .xlsx ファイルを生成する場合 (ライブ Excel セッションなし):** 以下の説明に従って Python/openpyxl を使用し、配信前に `recalc.py` を実行します。
- このスキルの残りの部分では、openpyxl の例を使用します。その環境では Office JS API 呼び出しに変換されますが、すべての原則 (数式文字列、セル コメント、セクション チェックポイント、感度分析表 ループ) は同様に適用されます。

**⚠️ Office JS マージ セルの落とし穴:** マージされたセルを使用してセクション ヘッダーを作成する場合は、`.merge()` を呼び出してからマージされた範囲に `.values` を設定しないでください。Office JS は引き続き範囲の元のサイズを報告し、`InvalidArgument: The number of rows or columns in the input array doesn't match the size or dimensions of the range` をスローします。代わりに、左上のセルのみに値を書き込み、全範囲を結合して書式設定します。

```js
// WRONG — throws InvalidArgument:
const hdr = ws.getRange("A7:H7");
hdr.merge();
hdr.values = [["MARKET DATA & KEY INPUTS"]];  // 1×1 array vs 1×8 range → fails

// CORRECT — value first on single cell, then merge + format the range:
ws.getRange("A7").values = [["MARKET DATA & KEY INPUTS"]];
const hdr = ws.getRange("A7:H7");
hdr.merge();
hdr.format.fill.color = "#1F4E79";
hdr.format.font.bold = true;
hdr.format.font.color = "#FFFFFF";
```

これは、DCF 内のすべてのマージされたセクション ヘッダー (市場データ、シナリオ ブロック、キャッシュ フロー予測、継続価値、評価概要、感応度テーブル) に適用されます。

**ハードコードよりも数式を使用する (交渉不可):**
- すべての予測、マージン、割引係数、PV、および感度セルは、ライブ Excel 式でなければなりません。決して Python で計算され数値として書き込まれた値ではありません。
- openpyxl を使用する場合: `ws["D20"] = "=D19*(1+$B$8)"` は正しいです。 `ws["D20"] = calculated_revenue` は間違っています
- 許可されるハードコードされた数値のみ: (1) 生の過去の入力値、(2) 仮定の要因 (成長率、WACC 入力値、ターミナル g)、(3) 現在の市場データ (株価、債務残高)
- Python で何かを計算して結果を書いていることに気づいたら、やめてください。ユーザーが仮定を変更するときは、モデルを柔軟にする必要があります。

**ユーザーと一緒に段階的に確認してください (エンドツーエンドで構築しないでください):**
- データ取得後 → 生の入力ブロック (売上高、利益率、株式数、純有利子負債) をユーザーに表示し、予測前に確認します。
- 収益予測後 → 予測されるトップラインと成長率を表示し、利益率を構築する前に確認します
- FCF ビルド後 → 完全な FCF スケジュールを表示し、WACC を計算する前にロジックを確認します
- WACC後→計算と入力を表示、割引前に確認
- 継続価値+PV後→株式ブリッジ(EV→株式価値→1株当たり)を表示、感応度テーブル前に確認
- 各段階でエラーをキャッチ - 感度テーブルの構築後に間違ったマージン仮定が発見されると、下流ですべてを再構築する必要があります

**感度テーブル:**
- **奇数の行と列を使用します** (標準: 5×5、場合によっては 7×7) - これにより真の中央セルが保証されます
- **中央のセル = 基本ケース。** 中央の行ヘッダーと中央列のヘッダーがモデルの実際の仮定と正確に等しくなるように軸の値を構築します (たとえば、ベース WACC = 9.0% の場合、中央の行は 9.0%、永久成長率g = 3.0% の場合、中央の列は 3.0%)。したがって、中央のセルの出力は、モデルの実際のモデルが示唆する株価と等しくなる必要があります。これは、テーブルが正しく構築されているかどうかの健全性チェックです。
- **中央のセルを中程度の青色の塗りつぶし (`#BDD7EE`) + 太字フォントで強調表示します**。これにより、どのセルが基本ケースであるかがすぐにわかります。
- すべてのセル (通常、3 テーブル × 25 セル = 75) に完全な DCF 再計算式を入力します。
- openpyxl ループ (または Office JS ループ) を使用してプログラムで数式を記述する
- プレースホルダー、線形近似は禁止し、ユーザーの手作業を必要としてはいけません。
- 各セルは、その仮定の組み合わせに対して完全な DCF を再計算する必要があります。

**セルのコメント:**
- ハードコードされた値が作成されるたびにセル コメントを追加します。
- 形式: 「ソース: [システム/ドキュメント]、[日付]、[参照]、[該当する場合は URL]」
- 次のセクションに進む前に、すべての青色の入力にコメントが必要です
- 最後に先送りしたり、「TODO: ソースを追加」と書き込んだりしないでください。

**モデルのレイアウト計画:**
- 数式を記述する前に、すべてのセクションの行位置を定義してください
- すべてのヘッダーとラベルを最初に書き込みます
- すべてのセクション区切りと空白行を 2 番目に書き込みます
- 次に、ロックされた行位置を使用して数式を作成します
- 作成直後に数式をテストする

**式の再計算:**
- 配信前に `python recalc.py model.xlsx 30` を実行する
- ステータスが「成功」になるまですべてのエラーを修正します
- 式エラーがゼロである必要があります (#REF!、#DIV/0!、#VALUE! など)

**シナリオ ブロック:**
- Bear/Base/Bull の場合に個別のブロックを作成する
- 各ブロック内の予測年にわたって仮定を水平方向に表示します
- IF 式を使用します: `=IF($B$6=1,[Bear cell],IF($B$6=2,[Base cell],[Bull cell]))`
- 数式が正しいシナリオ ブロック セルを参照していることを確認する

<a id="dcf-process-workflow"></a>
## DCF プロセスのワークフロー

<a id="step-1-data-retrieval-and-validation"></a>
### ステップ 1: データの取得と検証

MCP サーバー、ユーザー提供データ、Web からデータを取得します。

**データ ソースの優先順位:**
1. **MCP サーバー** (構成されている場合) - Daloopa などのプロバイダーからの構造化財務データ
2. **ユーザー提供データ** - 研究による過去の財務状況
3. **Web 検索/フェッチ** - 現在の株価、ベータ、負債、必要な場合の現金

**検証チェックリスト:**
- 純負債と純現金を検証する (評価に重要)
- 希薄化後の発行済株式数を確認（最近の買い戻し/発行を確認）
- 過去のマージンがビジネスモデルと一致していることを検証する
- 収益成長率を業界ベンチマークと照合する
- 税率が妥当であることを確認します (通常は 21 ～ 28%)

<a id="step-2-historical-analysis-3-5-years"></a>
### ステップ 2: 履歴分析 (3 ～ 5 年)

分析して文書化します。
- **収益成長傾向**: CAGR を計算し、推進要因を特定する
- **利益率の推移**：売上総利益率、EBIT マージン、FCF マージンを追跡します
- **資本強度**: 収益に占める D&A と設備投資の割合 (%)
- **運転資本効率**: 売上増加額に対するNWC増減額の割合
- **収益指標**: ROIC、ROE の傾向

以下を示す要約テーブルを作成します。
```
Historical Metrics (LTM):
Revenue: $X million
Revenue growth: X% CAGR
Gross margin: X%
EBIT margin: X%
D&A % of revenue: X%
CapEx % of revenue: X%
FCF margin: X%
```

<a id="step-3-build-revenue-projections"></a>
### ステップ 3: 収益予測を立てる

**方法論:**
1. 最新の実際の収益 (LTM または最新の会計年度) から開始します。
2. 各予測年の成長率を適用する
3. 金額と計算された成長率の両方を表示します

**成長率のフレームワーク:**
- 1 ～ 2 年目: 短期的な見通しを反映したより高い成長
- 3 ～ 4 年目: 業界平均に向けて徐々に緩和
- 5 年目以降: 永久成長率に近づく

**式の構造:**
- 収益(N年) = 収益(N-1年) × (1 + 成長率)
- 成長率 %(N 年) = 収益 (N 年) / 収益 (N-1 年) - 1

**3 つのシナリオによるアプローチ:**
```
Bear Case: Conservative growth (e.g., 8-12%)
Base Case: Most likely scenario (e.g., 12-16%)
Bull Case: Optimistic growth (e.g., 16-20%)
```

<a id="step-4-operating-expense-modeling"></a>
### ステップ 4: 営業費用のモデリング

**固定費/変動費分析:**

営業費用は、現実的な営業レバレッジをモデル化する必要があります。
- **販売およびマーケティング**: ビジネス モデルに応じて、通常は収益の 15 ～ 40%
- **研究開発**: テクノロジー企業の場合、通常 10 ～ 30%
- **一般および管理**: 通常、売上高の8〜15%。企業規模の拡大に伴い売上高比率が低下します。

**重要な原則:**
- すべてのパーセンテージは、売上総利益ではなく収益に基づいています
- モデルの営業レバレッジ: 収益が拡大するにつれて、% は低下するはずです
- S&M、R&D、G&A ごとに個別の項目を維持する
- EBIT = 総利益 - 合計 OpEx を計算します。

**マージン拡大フレームワーク:**
```
Current State → Target State (Year 5)
Gross Margin: X% → Y% (justify based on scale, efficiency)
EBIT Margin: X% → Y% (result of revenue growth + opex leverage)
```

<a id="step-5-free-cash-flow-calculation"></a>
### ステップ 5: フリー キャッシュ フローの計算

**適切な順序で FCF を構築します:**

```
EBIT
(-) Taxes (EBIT × Tax Rate)
= NOPAT (Net Operating Profit After Tax)
(+) D&A (non-cash expense, % of revenue)
(-) CapEx (% of revenue, typically 4-8%)
(-) Δ NWC (change in working capital)
= Unlevered Free Cash Flow
```

**運転資本モデリング:**
- 収益変化の % (デルタ収益) として計算します。
- 一般的な範囲: 収益変化の -2% ～ +2%
- 負の数 = 現金の源泉 (運転資本の放出)
- 正の数 = 現金の使用 (運転資本の構築)

**メンテナンスと成長の設備投資:**
- メンテナンス設備投資: 現在の運営を維持します (売上高の約2〜3%)
- 成長設備投資: 拡大をサポート (売上高に対して追加で2〜5%)
- 総設備投資は企業の成長戦略と一致する必要があります

<a id="step-6-cost-of-capital-wacc-research"></a>
### ステップ 6: 資本コスト (WACC) 調査

**株主資本コストに関するCAPM手法:**

```
Cost of Equity = Risk-Free Rate + Beta × Equity Risk Premium

Where:
- Risk-Free Rate = Current 10-Year Treasury Yield
- Beta = 5-year monthly stock beta vs market index
- Equity Risk Premium = 5.0-6.0% (market standard)
```

**負債のコストの計算:**

```
After-Tax Cost of Debt = Pre-Tax Cost of Debt × (1 - Tax Rate)

Determine Pre-Tax Cost of Debt from:
- Credit rating (if available)
- Current yield on company bonds
- Interest expense / Total Debt from financials
```

**資本構造の重み:**

```
Market Value Equity = Current Stock Price × Shares Outstanding
Net Debt = Total Debt - Cash & Equivalents
Enterprise Value = Market Cap + Net Debt

Equity Weight = Market Cap / Enterprise Value
Debt Weight = Net Debt / Enterprise Value

WACC = (Cost of Equity × Equity Weight) + (After-Tax Cost of Debt × Debt Weight)
```

**特殊な場合:**
- **純現金ポジション**: 現金 > 負債の場合、純負債はマイナスです。
  - 負債の重みがマイナスになる可能性があります
  - WACC計算はそれに応じて調整します
- **負債なし**: WACC = 株主資本コスト

**一般的な WACC 範囲:**
- 大型株、安定: 7-9%
- 成長企業: 9-12%
- 高成長/リスク: 12-15%

<a id="step-7-discount-rate-application-5-10-year-forecast"></a>
### ステップ 7: 割引率の適用 (5 ～ 10 年予測)

**年央割引の慣行:**
- キャッシュフローは年度途中に発生すると想定
- 割引期間：0.5、1.5、2.5、3.5、4.5など
- 割引係数 = 1 / (1 + WACC)^期間

**現在価値の計算:**
```
For each projection year:
PV of FCF = Unlevered FCF × Discount Factor

Example (Year 1):
FCF = $1,000
WACC = 10%
Period = 0.5
Discount Factor = 1 / (1.10)^0.5 = 0.9535
PV = $1,000 × 0.9535 = $954
```

**予測期間の選択:**
- **5 年**: ほとんどの分析の標準
- **7 ～ 10 年**: ランウェイが長い高成長企業
- **3 年**: 成熟した安定したビジネス

<a id="step-8-terminal-value-calculation"></a>
### ステップ 8: 継続価値の計算

**永久成長法 (推奨):**

```
Terminal FCF = Final Year FCF × (1 + Terminal Growth Rate)
Terminal Value = Terminal FCF / (WACC - Terminal Growth Rate)

Critical Constraint: Terminal Growth < WACC (otherwise infinite value)
```

**ターミナル成長率の選択:**
- 保守派: 2.0-2.5% (GDP成長率)
- 中程度: 2.5-3.5%
- 積極的: 3.5-5.0% (市場リーダーのみ)

**超過しない**: リスクフリー金利または長期 GDP 成長率

**エグジット倍率法 (代替):**
```
Terminal Value = Final Year EBITDA × Exit Multiple

Where Exit Multiple comes from:
- Industry comparable trading multiples
- Precedent transaction multiples
- Typical range: 8-15x EBITDA
```

**継続価値の現在価値:**
```
PV of Terminal Value = Terminal Value / (1 + WACC)^Final Period

Where Final Period accounts for timing:
5-year model with mid-year convention: Period = 4.5
```

**継続価値の健全性チェック:**
- 企業価値の 50 ～ 70% を占める必要がある
- >75% の場合、モデルは継続価値の前提に過度に依存している可能性があります
- 40% 未満の場合は、継続価値の前提が保守的すぎるかどうかを確認します

<a id="step-9-enterprise-to-equity-value-bridge"></a>
### ステップ 9: 企業と株式価値の橋渡し

**評価概要の構成:**

```
(+) Sum of PV of Projected FCFs = $X million
(+) PV of Terminal Value = $Y million
= Enterprise Value = $Z million

(-) Net Debt [or + Net Cash if negative] = $A million
= Equity Value = $B million

÷ Diluted Shares Outstanding = C million shares
= Implied Price per Share = $XX.XX

Current Stock Price = $YY.YY
Implied Return = (Implied Price / Current Price) - 1 = XX%
```

**重要な調整:**
- **純負債 = 負債合計 - 現金および同等物**
  - プラスの場合：EVから減算（株式価値を減少）
  - マイナスの場合（ネットキャッシュ）：EVに加算（株式価値の増加）
- **希薄化株式の使用**: オプション、RSU、転換社債が含まれます
- **その他の調整** (該当する場合):
  - 非支配株主持分
  - 年金債務
  - オペレーティングリース債務

**評価出力形式:**
```csv
Valuation Component,Amount ($M)
PV Explicit FCFs,X.X
PV Terminal Value,Y.Y
Enterprise Value,Z.Z
(-) Net Debt,A.A
Equity Value,B.B
,,
Shares Outstanding (M),C.C
Implied Price per Share,$XX.XX
Current Share Price,$YY.YY
Implied Upside/(Downside),+XX%
```

<a id="step-10-sensitivity-analysis"></a>
### ステップ 10: 感度分析

DCF シートの下部に **3 つの感応度テーブル**を作成し、さまざまな仮定で評価がどのように変化するかを示します。

1. **WACC と永久成長率** - 割引率と永久成長に対する企業価値の感応度を示します。
2. **売上成長率 vs EBIT マージン** - 売上高の成長と営業レバレッジの影響を示します。
3. **ベータ対リスクフリーレート** - 株主資本コストの構成要素に対する感応度を示します。

**実装**: これらは、各セルに数式が入った単純な 2D グリッド (Excel の「データ テーブル」機能ではありません) です。各セルには、その特定の仮定の組み合わせに対する完全な DCF 再計算が含まれている必要があります。 openpyxl を使用してプログラムで 75 個のセルすべてを設定するための詳細な要件については、「重要な制約」セクションを参照してください。

<correct_patterns>

このセクションには、DCF モデルを構築する際に従うべき正しいパターンがすべて含まれています。

<a id="scenario-block-selection-pattern---follow-this-approach"></a>
### シナリオ ブロックの選択パターン - このアプローチに従ってください

**仮定は、シナリオごとに個別のブロックにまとめられています。**

**重要な構造 - セクション ヘッダーごとに 3 行:**

```csv
BEAR CASE ASSUMPTIONS (section header, merge cells across)
Assumption,FY1,FY2,FY3,FY4,FY5
Revenue Growth (%),12%,10%,9%,8%,7%
EBIT Margin (%),45%,44%,43%,42%,41%

BASE CASE ASSUMPTIONS (section header, merge cells across)
Assumption,FY1,FY2,FY3,FY4,FY5
Revenue Growth (%),16%,14%,12%,10%,9%
EBIT Margin (%),48%,49%,50%,51%,52%

BULL CASE ASSUMPTIONS (section header, merge cells across)
Assumption,FY1,FY2,FY3,FY4,FY5
Revenue Growth (%),20%,18%,15%,13%,11%
EBIT Margin (%),50%,51%,52%,53%,54%
```

**各シナリオ ブロックには、セクション タイトルのすぐ下に予測年 (2025 年度、2026 年度など) を示す列ヘッダー行がなければなりません**。これがないと、ユーザーはどの仮定値がどの年に対応するかを知ることができません。

**仮定を参照する方法 - 統合列を作成します:**
1. シナリオ選択セル (B6 など) には、1=Bear、2=Base、または 3=Bull が含まれます。
2. INDEX または OFFSET 式を使用して統合列を作成し、正しいシナリオ ブロックから取得します。
3. 予測式は統合列を参照します (クリーンセル参照)
4. 各シナリオ ブロックには、予測年にわたる DCF 仮定の完全なセットが含まれています

**推奨される統合列パターン (INDEX を使用):**
`=INDEX(B10:D10, 1, $B$6)`

**これではありません - 全体に散在する IF ステートメント:**
`=IF($B$6=1,[Bear block cell],IF($B$6=2,[Base block cell],[Bull block cell]))`

統合列アプローチによりロジックが集中化され、モデルの監査が容易になります。

<a id="correct-revenue-projection-pattern"></a>
### 正しい収益予測パターン

**INDEX 式を使用して集計列を作成し、それを予測で参照します。**

**ステップ 1 - 1 会計年度の成長の統合列:**
`=INDEX([Bear FY1 growth]:[Bull FY1 growth], 1, $B$6)`

**ステップ 2 - 収益予測は統合列を参照します:**
`Revenue Year 1: =D29*(1+$E$10)`

場所:
- D29 = 前年度の収益
- $E$10 = FY1 成長の統合列セル (INDEX 式を含む)
- $B$6 = ケースセレクター (1=ベア、2=ベース、3=ブル)

**このアプローチは、すべての予測式に IF ステートメントを埋め込むよりもクリーンです**。また、どのシナリオの仮定が使用されているかを監査するのがはるかに簡単になります。

<a id="correct-fcf-formula-pattern"></a>
### 正しい FCF 式パターン

**INDEX 式で統合列を使用し、FCF 計算で参照します。**

**統合列アプローチ:**
```csv
Item,Formula,Reference
D&A,=E29*$E$21,$E$21 = consolidation column for D&A %
CapEx,=E29*$E$22,$E$22 = consolidation column for CapEx %
Δ NWC,=(E29-D29)*$E$23,$E$23 = consolidation column for NWC %
Unlevered FCF,=E57+E58-E60-E62,E57=NOPAT E58=D&A E60=CapEx E62=Δ NWC
```

**各統合列セルには、ケース セレクターに基づいて適切なシナリオ ブロックから取得する INDEX 式**が含まれています。これにより、予測式がクリーンで監査可能に保たれます。

数式を記述する前に、シナリオブロックの行位置を確認し、統合列を設定します。

<a id="correct-cell-comment-format"></a>
### 正しいセルのコメント形式

**すべてのハードコードされた値には次の形式が必要です:**

「出典: [システム/ドキュメント]、[日付]、[参照]、[該当する場合は URL]」

**例:**
```csv
Item,Source Comment
Stock price,Source: Market data script 2025-10-12 Close price
Shares outstanding,Source: 10-K FY2024 Page 45 Note 12
Historical revenue,Source: 10-K FY2024 Page 32 Consolidated Statements
Beta,Source: Market data script 2025-10-12 5-year monthly beta
Consensus estimates,Source: Management guidance Q3 2024 earnings call
```

<a id="correct-assumption-table-structure"></a>
### 正しい仮定テーブルの構造

**重要: 各シナリオ ブロックには 3 つの構造要素が必要です。**

1. **セクションヘッダー行** (結合されたセル): 例: 「BEAR CASE ASSUMPTIONS」
2. **列ヘッダー行** 年を表示 - これは必須です。スキップしないでください
3. **仮定値を含む**データ行**

**構造:**
```csv
BEAR CASE ASSUMPTIONS (section header - merge across columns A:G)
Assumption,FY1,FY2,FY3,FY4,FY5
Revenue Growth (%),X%,X%,X%,X%,X%
EBIT Margin (%),X%,X%,X%,X%,X%
Terminal Growth,X%,,,,
WACC,X%,,,,

BASE CASE ASSUMPTIONS (section header - merge across columns A:G)
Assumption,FY1,FY2,FY3,FY4,FY5
Revenue Growth (%),X%,X%,X%,X%,X%
EBIT Margin (%),X%,X%,X%,X%,X%
Terminal Growth,X%,,,,
WACC,X%,,,,

BULL CASE ASSUMPTIONS (section header - merge across columns A:G)
Assumption,FY1,FY2,FY3,FY4,FY5
Revenue Growth (%),X%,X%,X%,X%,X%
EBIT Margin (%),X%,X%,X%,X%,X%
Terminal Growth,X%,,,,
WACC,X%,,,,
```

**予測年 (FY2025E、FY2026E など) を示す列ヘッダー行がないと、ユーザーはどの仮定値がどの年に対応するかを判断できません。この行は必須です。**

**次に、INDEX 式を使用してケース セレクターに基づいて選択されたシナリオ ブロックから取得する統合列** (通常は右隣の列) を作成します。この統合列は、予測式が参照するものです。

<a id="correct-row-planning-process"></a>
### 正しい行計画プロセス

**1.すべてのヘッダーとラベルを最初に書き込みます:**
```csv
Row,Content
1,[Company Name] DCF Model
2,Ticker | Date | Year End
4,Case Selector
7,KEY ASSUMPTIONS
26,Assumption headers
27-31,Growth assumptions
...,...
```

**2.すべてのセクション区切り線と空白行を書き込みます**

**3.次に、ロックされた行位置を使用して数式を作成します**

**4.作成直後に数式をテストします**

**建設のようなものだと考えてください:**
- 良い: 基礎を注入してから壁を構築します (安定した構造)
- 悪い例: 壁を建ててから基礎を流し込む (壁が崩壊する)

**Excel のバージョン:**
- 良い例: ヘッダーを追加してから数式を記述します (数式は安定しています)
- 悪い例: 数式を書いてからヘッダーを追加する (数式が壊れる)

<a id="correct-sensitivity-table-implementation"></a>
### 正しい感度テーブルの実装

**重要**: これらは Excel の「データ テーブル」機能ではありません。これらは、openpyxl を使用して通常の数式を記述する単純なグリッドです。はい、これは合計約 75 個の数式 (3 つのテーブル × それぞれ 25 セル) を意味しますが、これは簡単であり、必須です。

**数式を使用したプログラムによる入力:**

各感応度テーブルには、仮定の組み合わせごとにモデルが示唆する株価を再計算する式を完全に入力する必要があります。 **Excel のデータ テーブル機能は使用しないでください** (手動介入が必要で、openpyxl で自動化することはできません)。

**実装アプローチ - 具体例:**

**テーブル構造 - 5×5 グリッド (ODD 寸法、ベースケースを中心に配置):**

モデルの基本 WACC = 9.0% および基本ケースの永久成長 = 3.0% の場合、これらの値を中心に対称に軸を構築します。

```csv
WACC vs Terminal Growth,  2.0%,  2.5%,  3.0%,  3.5%,  4.0%
              8.0%,       [fml], [fml], [fml], [fml], [fml]
              8.5%,       [fml], [fml], [fml], [fml], [fml]
              9.0%,       [fml], [fml], [★  ], [fml], [fml]   ← middle row = base WACC
              9.5%,       [fml], [fml], [fml], [fml], [fml]
             10.0%,       [fml], [fml], [fml], [fml], [fml]
                                   ↑
                          middle col = base terminal g
```

**★ = 中央のセル。** その式の出力は、(評価概要からの) モデルの実際のモデルが示唆する株価と等しくなければなりません。このセルに中程度の青の塗りつぶし (`#BDD7EE`) と太字のフォントを適用して、基本ケースが視覚的に固定されるようにします。

**軸の値のルール:** `axis_values = [base - 2*step, base - step, base, base + step, base + 2*step]` — ベースの周りで対称、奇数の数は中心を保証します。

**式パターン - セル B88 (WACC=8.0%、永久成長 = 2.0%):**

B88 の式は、以下を使用してモデルが示唆する株価を再計算する必要があります。
- 行ヘッダーからの WACC: `$A88` (8.0%)
- 列ヘッダーからの永久成長率: `B$87` (2.0%)

**推奨されるアプローチ:** メインの DCF 計算を参照しますが、これらの値を置き換えます。

**式の構造の例:**
`=([SUM of PV FCFs using $A88 as discount rate] + [Terminal Value using B$87 as growth rate and $A88 as WACC] - [Net Debt]) / [Shares]`

**重要 - 5x5 グリッド内のすべてのセルに数式を作成します (テーブルごとに 25 セル、合計 75 セル)。** これらの数式をループ内でプログラム的に作成するには、openpyxl を使用します。この手順をスキップしたり、プレースホルダー テキストを残さないでください。

**Python 実装パターン:**
```python
# Pseudocode for populating sensitivity table
for row_idx, wacc_value in enumerate(wacc_range):
    for col_idx, term_growth_value in enumerate(term_growth_range):
        # Build formula that uses wacc_value and term_growth_value
        formula = f"=<DCF recalc using {wacc_value} and {term_growth_value}>"
        ws.cell(row=start_row+row_idx, column=start_col+col_idx).value = formula
```

**感度テーブルは、ユーザーが手動で行う必要がなく、モデルを開いたときにすぐに機能する必要があります。**

</correct_patterns>

<common_mistakes>

このセクションには、DCF モデルを構築する際に避けるべき間違ったパターンがすべて含まれています。

<a id="wrong-simplified-sensitivity-table-approximations-or-placeholder-text"></a>
### 誤: 簡略化された感度テーブルの近似値またはプレースホルダー テキスト

**線形近似は使用しないでください:**

```
// WRONG - Linear approximation
B97: =B88*(1+(0.096-0.116))    // Assumes linear relationship

// WRONG - Division shortcut
B105: =B88/(1+(E48-0.07))      // Doesn't recalculate full DCF
```

**プレースホルダーテキストを残さないでください:**
```
// WRONG - Placeholder note
"Note: Use Excel Data Table feature (Data → What-If Analysis → Data Table) to populate sensitivity tables."

// WRONG - Empty cells
[leaving cells blank because "this is complex"]
```

**用語を混同しないでください:**
- ❌ 「感度テーブルには Excel のデータ テーブル機能が必要です」 (いいえ、これは使用できない特定の Excel ツールです)
- ✅ 「感度テーブルは、各セルに数式が入った単純なグリッドです」 (はい - これが私たちが構築するものです)

**これらのショートカットが間違っている理由:**
- 線形近似式は実際には DCF を再計算しません。単純な数学的調整を適用するだけです。
- 関係は線形ではないため、結果は不正確になります
- プレースホルダー テキストにはユーザーの手動介入が必要です
- モデルは納品されてもすぐには使用できません
- プロフェッショナルまたはクライアント対応ではない
- 空のセル = 不完全な成果物

**退けるべき、よくある自己正当化:**
「75 以上の数式を書くのは複雑に感じるので、ユーザーが手動で入力できるようにメモを残しておきます。」

**現実:** openpyxl を使用して Python のループを使用すると、75 の数式を書くのは簡単です。各式は同じパターンに従います。行/列の値を置き換えるだけです。これは成果物の必須部分です。

**代わりに:** すべての感度セルに、特定の仮定の組み合わせに対する完全な DCF を再計算する式を入力します。

<a id="wrong-missing-cell-comments"></a>
### 間違い: セルのコメントがありません

**これは行わないでください:**
- コメントなしですべてのハードコーディングされた入力を作成します
- 「後で追加しよう」と考えてください
- 「TODO: ソースを追加」と書きます。
- 青色の入力を文書化せずにそのままにする

**間違っている理由:**
- データの出所を確認できない
- xlsx スキル要件に失敗します
- 監査の準備ができていない
- 後で修正するのは時間を無駄にする

**代わりに:** ハードコードされた値が作成されるたびにセル コメントを追加します

<a id="wrong-formula-row-references-off"></a>
### 間違っています: 数式行の参照がオフになっています

**症状:**
FCF セクションは、間違った仮定行を参照しています。
`D&A:  =E29*$E$34    // Should be $E$21, but referencing wrong row`
`CapEx: =E29*$E$41   // Should be $E$22, but row shifted`

**これが起こる理由:**
1. 最初に書かれた数式
2. 次にヘッダーを挿入します
3. すべての行参照がシフトされました
4. 数式が間違ったセルを指している → #REF!エラー

**代わりに:** 最初に行レイアウトをロックしてから、数式を記述します

<a id="wrong-single-row-for-each-assumption-across-scenarios"></a>
### 誤り: シナリオ全体の仮定ごとに 1 行

**次のような仮定を組み立てないでください:**
```csv
Assumption,Bear,Base,Bull
Revenue Growth FY1,10%,13%,16%
Revenue Growth FY2,9%,12%,15%
```
この縦方向のレイアウトでは、各シナリオ内での数年にわたる進捗を確認することが困難になります。

**間違っている理由:**
- 各シナリオ内で数年にわたって変化する仮定を確認することが困難になる
- 予測期間全体にわたってシナリオの仮定を比較するのが困難
- シナリオロジックのレビューが直感的ではない

**代わりに:**
- シナリオごとに個別のブロックを作成します (ベア、ベース、ブル)
- 各ブロック内で、予測年全体にわたって水平方向に仮定を表示します。
- これにより、各シナリオの仮定をまとまったセットとしてレビューしやすくなります。

<a id="wrong-no-borders"></a>
### 間違い: 罫線がない

**境界線のないモデルを提供しないでください:**
- セクションの描写なし
- すべてのセルが区切りなく混ざって見える
- 読みにくく、専門的ではない

**間違っている理由:**
- クライアント対応ではありません
- ナビゲートが難しい
- 素人っぽい

**代わりに:** すべての主要セクションの周囲に境界線を追加します

<a id="wrong-wrong-font-colors-or-no-font-color-distinction"></a>
### 間違っています: フォントの色が間違っているか、フォントの色の区別がありません

**これは行わないでください:**
- 文字はすべて黒です
- 塗りつぶしの色のみを使用します (フォントの色の変更はありません)。
- どのセルが青か黒かを混同する

**間違っている理由:**
- 入力と数式を区別できない
- 監査が不可能になる
- xlsx スキル要件に違反します

**代わりに:** すべてのハードコードされた入力には青色のテキスト、すべての数式には黒色のテキスト、シート リンクには緑色のテキストが表示されます。

<a id="wrong-operating-expenses-based-on-gross-profit"></a>
### 間違い: 売上総利益に基づく営業費用

**これは行わないでください:**
`S&M: =E33*0.15    // E33 = Gross Profit (WRONG)`

**間違っている理由:**
- 営業費用は、売上総利益ではなく、収益に比例します
- 非現実的なマージンの進行を生成する
- ビジネスが実際にどのように運営されるかではない

**代わりに:**
`S&M: =E29*0.15    // E29 = Revenue (CORRECT)`

<a id="top-5-errors-summary"></a>
### 上位 5 つのエラーの概要

1. **数式の行参照がオフ** → 数式を記述する前にすべての行の位置を定義してください
2. **セルのコメントがありません** → コメントを追加 を最後ではなくセル作成時に行う
3. **簡略化された感度テーブル** → すべてのセルに近似ではなく完全な DCF 再計算式を入力します。
4. **シナリオ ブロックの参照が間違っている** → IF 式が正しい Bear/Base/Bull ブロックから取得されていることを確認してください
5. **枠線なし** → クライアントに適した外観を実現するために、プロフェッショナルなセクションの枠線を追加します

さらに、次のエラーにも注意してください。

<a id="wacc-calculation-errors"></a>
### WACC 計算エラー
- 資本構成における簿価と市場価値の混合
- 資産/レバレッジなしベータの代わりに株式ベータを誤って使用する
- 負債コストに対する誤った税率の適用
- 不正なリスクフリーレート (現在の 10 年国債を使用する必要があります)
- 純負債と純キャッシュポジションの調整ができていない

<a id="growth-assumption-flaws"></a>
### 成長の仮定の欠陥
- 最終的な成長 > WACC (無限の価値を生み出す)
- 予測成長率が過去の実績と一致しない
- 業界の成長制約を無視する
- 収益の伸びがユニットエコノミクスと一致しない
- 運用上の正当性のないマージン拡大

<a id="terminal-value-mistakes"></a>
### 継続価値の間違い
- 間違った成長方法の使用 (永久成長法とエグジット倍率法)
- 継続価値が企業価値の80%超 (過度の依存を示唆)
- 定常状態の仮定と一貫性のないターミナルマージン
- ターミナルバリューの割引期間が間違っています

<a id="cash-flow-projection-errors"></a>
### キャッシュフロー予測の誤差
- 収益ではなく売上総利益に基づく営業費用
- ビジネスモデルと乖離したD&A/CapExの割合
- 運転資本の変化が適切に計算されていない
- 年間の税率の不一致
- NOPAT 計算エラー

**これらのエラーは最も一般的です。 DCF ビルドを開始する前に、このセクションをもう一度読んでください。**

</common_mistakes>

<a id="excel-file-creation"></a>
## Excelファイルの作成

**このスキルは、すべてのスプレッドシート操作に `xlsx` スキルを使用します。** xlsx スキルは以下を提供します。
- 標準化された式構築ルール
- 数値の書式設定規則
- `recalc.py` スクリプトによる自動式再計算
- 包括的なエラーチェックと検証

このスキルで作成されたすべての Excel ファイルは、ゼロ数式エラーや適切な再計算など、xlsx スキル要件に従う必要があります。

<a id="quality-rubric"></a>
## 高品質のルーブリック

すべての DCF モデルは以下を最大化する必要があります。
1. **過去の実績に基づく現実的な収益と利益率の仮定**
2. **適切な CAPM 手法による適切な資本コストの計算**
3. **包括的な感応度分析**による評価範囲の表示
4. **明確な継続価値の計算**と裏付けとなる理論的根拠
5. **シナリオ分析を可能にするプロフェッショナルなモデル構造**
6. すべての重要な前提条件の **透明性のある文書**

<a id="input-requirements"></a>
## 入力要件

<a id="minimum-required-inputs"></a>
### 最小限必要な入力
1. **会社識別子**: ティッカーシンボルまたは会社名
2. **成長の仮定**: 予測期間の収益成長率 (または「コンセンサスを使用」)
3. **オプションのパラメータ**:
   - 予測期間（デフォルト：5年）
   - シナリオケース（弱気/ベース/強気の成長率と利益率の前提）
   - 永久成長率 (デフォルト: 2.5-3.0%)
   - CAPM を使用しない場合の特定の WACC 入力

<a id="excel-model-structure"></a>
## Excel モデルの構造

<a id="sheet-architecture"></a>
### シートアーキテクチャ

**2 つのシート**を作成します:

1. **DCF** - 下部に感応度分析を含む主要な評価モデル
2. **WACC** - 資本コストの計算

**重要**: 感度テーブルは DCF シートの下部にあります (別のシートではありません)。これにより、すべての評価出力がまとめられます。

<a id="formula-recalculation-mandatory"></a>
### 式の再計算 (必須)

Excel モデルを作成または変更した後、xlsx スキルの recalc.py スクリプトを使用して **すべての数式を再計算**します。

```bash
python recalc.py [path_to_excel_file] [timeout_seconds]
```

例:
```bash
python recalc.py AAPL_DCF_Model_2025-10-12.xlsx 30
```

スクリプトは次のことを行います。
- LibreOfficeを使用してすべてのシートのすべての数式を再計算する
- Excel エラー (#REF!、#DIV/0!、#VALUE!、#NAME?、#NULL!、#NUM!、#N/A) のすべてのセルをスキャンします。
- エラーの場所と数を含む詳細な JSON を返します

**予想される出力形式:**
```json
{
  "status": "success",           // or "errors_found"
  "total_errors": 0,              // Total error count
  "total_formulas": 42,           // Number of formulas in file
  "error_summary": {}             // Only present if errors found
}
```

**エラーが見つかった場合**、出力には詳細が含まれます。
```json
{
  "status": "errors_found",
  "total_errors": 2,
  "total_formulas": 42,
  "error_summary": {
    "#REF!": {
      "count": 2,
      "locations": ["DCF!B25", "DCF!C25"]
    }
  }
}
```

**すべてのエラーを修正**し、ステータスが「成功」になるまで recalc.py を再実行してから、モデルを配信します。

<a id="formatting-standards"></a>
### 書式設定の標準

**重要**: 数式の構築ルールと数値の書式設定規則については、xlsx スキルに従ってください。 DCF スキルは、特定のビジュアル プレゼンテーション標準を追加します。

**配色 - 2 つのレイヤー**:

**レイヤー 1: フォントの色 (xlsx スキルから必須)**
- **青色のテキスト (RGB: 0,0,255)**: すべてのハードコードされた入力 (株価、株式、過去のデータ、仮定)
- **黒色のテキスト (RGB: 0,0,0)**: すべての式と計算
- **緑色のテキスト (RGB: 0,128,0)**: 他のシートへのリンク (WACC シート参照)

**レイヤー 2: 塗りつぶしの色 — プロフェッショナル ブルー/グレー パレット (ユーザーが別途指定しない限りデフォルト)**
- **最小限に抑えてください** — 塗りつぶしには青とグレーのみを使用します。緑、黄色、オレンジ、または複数のアクセントカラーを導入しないでください。色が多すぎるモデルは素人っぽく見えます。
- **デフォルトの塗りつぶしパレット:**
  - **セクション ヘッダー**: ダークブルー (RGB: 31,78,121 / `#1F4E79`) の背景に白の太字テキスト
  - **サブヘッダー/列ヘッダー**: 水色 (RGB: 217,225,242 / `#D9E1F2`) の背景に黒の太字テキスト
  - **入力セル**: ライトグレー (RGB: 242,242,242 / `#F2F2F2`) の背景に青のフォント — または、最大限のミニマリズムが必要な場合は、白に青のフォント
  - **計算セル**: 白の背景に黒のフォント
  - **出力/サマリー行** (一株当たりの価値、EV など): 中青色 (RGB: 189,215,238 / `#BDD7EE`) の背景に黒の太字フォント
- **それだけです — ブルー 3 色 + グレー 1 色 + ホワイト。** さらに追加したい衝動を抑えてください。
- ユーザーが提供したテンプレートまたは明示的な色の設定は、常にこれらのデフォルトをオーバーライドします。

**レイヤーがどのように連携するか:**
- 入力セル: 青色のフォント + ライトグレーの塗りつぶし = 「ハードコードされた入力」
- 数式セル：黒文字＋白背景＝「計算値」
- シートリンク：緑色の文字＋背景白＝「別シートからの参照」
- キー出力: 黒の太字フォント + 中程度の青の塗りつぶし = 「これが答えです」

**フォントの色は、それが何であるかを示します (入力/式/リンク)。塗りつぶしの色で、どこにいるか (ヘッダー/データ/出力) がわかります。**

<a id="border-standards-required-for-professional-appearance"></a>
### 境界基準 (プロフェッショナルな外観に必須)

主要セクションの周囲の **太い境界線** (1.5 ポイント):
- キー入力セクション
- 予測の仮定セクション
- 5 年間のキャッシュ フロー予測セクション
- 継続価値セクション
- 評価概要セクション
- 各感度分析テーブル

サブセクション間の **中枠** (1pt):
- 会社概要と過去の業績
- 成長率の仮定 vs EBITマージン vs FCFパラメータ

データ テーブルの周囲の **細い境界線** (0.5 ポイント):
- シナリオ想定表（ベア） | ベース | 強気 | 選択済み)
- 過去の財務マトリックスと予測された財務マトリックス

**枠線なし:** 表内の個々のセル (クリーンな状態を保ち、スキャン可能にします)

**境界線は必須です** - 専門的な境界線のないモデルはクライアントに対応できません。

**数値形式** (xlsx スキル標準に準拠):
- **年**: テキスト文字列としてフォーマットします (例: 「2,024」ではなく「2024」)
- **パーセンテージ**: `0.0%` (小数点第 1 位)
- **通貨**: 百万ドルの場合は `$#,##0`。 `$#,##0.00` (1 株当たり) - 常にヘッダーで単位を指定します (「収益 ($mm)」)
- **ゼロ**: 数値書式設定を使用してすべてのゼロを「-」にします (例: `$#,##0;($#,##0);-`)
- **大きな数値**: `#,##0` (桁区切り文字付き)
- **負の数**: 括弧内は `(#,##0)` (マイナス記号ではありません)

**セルのコメント (すべてのハードコードされた入力に必須)**:

xlsx スキルごとに、すべてのハードコードされた値には、ソースを文書化するセル コメントが必要です。形式: 「ソース: [システム/ドキュメント]、[日付]、[参照]、[該当する場合は URL]」

**重要**: セルの作成時にコメントを追加します。最後まで先送りしないでください。

<a id="dcf-sheet-detailed-structure"></a>
### DCFシートの詳細構造

**セクション 1: ヘッダー**
```csv
Row,Content
1,[Company Name] DCF Model
2,Ticker: [XXX] | Date: [Date] | Year End: [FYE]
3,Blank
4,Case Selector Cell (1=Bear 2=Base 3=Bull)
5,Case Name Display (formula: =IF([Selector]=1"Bear"IF([Selector]=2"Base""Bull")))
```

**セクション 2: 市場データ (ケースに依存しない)**
```csv
Item,Value
Current Stock Price,$XX.XX
Shares Outstanding (M),XX.X
Market Cap ($M),[Formula]
Net Debt ($M),XXX [or Net Cash if negative]
```

**セクション 3: DCF シナリオの仮定**

DCF 固有の仮定 (収益成長率 %、EBIT マージン %、税率 %、収益の D&A %、収益の設備投資 %、ΔRev の NWC 変化率、永久成長率、WACC) を使用して、各シナリオ (ベア、ベース、ブル) に対して個別の仮定ブロックを作成し、予測年にわたって水平に配置します。各ブロックには、セクション ヘッダー、予測年 (FY1、FY2 など) を示す列ヘッダー行、およびデータ行が含まれている必要があります。正確なレイアウトについては、`<correct_patterns>` セクション「正しい仮定テーブルの構造」を参照してください。

**セクション 4: 過去および将来の財務状況**

**すべての予測行に散在する IF 式ではなく、シナリオ ブロックから取得する統合列 (例: 「選択されたケース」) を参照します**。

```csv
Income Statement ($M),2020A,2021A,2022A,2023A,2024E,2025E,2026E
Revenue,XXX,XXX,XXX,XXX,[=E29*(1+$E$10)],[=F29*(1+$E$11)],[=G29*(1+$E$12)]
  % growth,XX%,XX%,XX%,XX%,[=E29/D29-1],[=F29/E29-1],[=G29/F29-1]
,,,,,,
Gross Profit,XXX,XXX,XXX,XXX,[=E29*E33],[=F29*F33],[=G29*G33]
  % margin,XX%,XX%,XX%,XX%,[=E33/E29],[=F33/F29],[=G33/G29]
,,,,,,
Operating Expenses:,,,,,,,
  S&M,XXX,XXX,XXX,XXX,[=E29*0.15],[=F29*0.14],[=G29*0.13]
  R&D,XXX,XXX,XXX,XXX,[=E29*0.12],[=F29*0.11],[=G29*0.10]
  G&A,XXX,XXX,XXX,XXX,[=E29*0.08],[=F29*0.07],[=G29*0.07]
  Total OpEx,XXX,XXX,XXX,XXX,[=E36+E37+E38],[=F36+F37+F38],[=G36+G37+G38]
,,,,,,
EBIT,XXX,XXX,XXX,XXX,[=E33-E39],[=F33-F39],[=G33-G39]
  % margin,XX%,XX%,XX%,XX%,[=E41/E29],[=F41/F29],[=G41/G29]
,,,,,,
Taxes,(XX),(XX),(XX),(XX),[=E41*$E$24],[=F41*$E$24],[=G41*$E$24]
  Tax rate,XX%,XX%,XX%,XX%,[=E43/E41],[=F43/F41],[=G43/G41]
,,,,,,
NOPAT,XXX,XXX,XXX,XXX,[=E41-E43],[=F41-F43],[=G41-G43]
```

**主要な数式パターン**:
- 収益の増加: `=E29*(1+$E$10)` ($E$10 は 1 年目の成長の統合列)
- ではありません: `=E29*(1+IF($B$6=1,$B$10,IF($B$6=2,$C$10,$D$10)))`

このアプローチは、よりクリーンで監査が容易で、シナリオ ロジックを一元化することで式のエラーを防ぎます。

**セクション 5: フリー キャッシュ フローの構築**

**重要**: 行参照が正しい仮定行を指していることを確認してください。作成直後に数式をテストします。

```csv
Cash Flow ($M),2020A,2021A,2022A,2023A,2024E,2025E,2026E
NOPAT,XXX,XXX,XXX,XXX,[=E45],[=F45],[=G45]
(+) D&A,XXX,XXX,XXX,XXX,[=E29*$E$21],[=F29*$E$21],[=G29*$E$21]
    % of Rev,XX%,XX%,XX%,XX%,[=E58/E29],[=F58/F29],[=G58/G29]
(-) CapEx,(XX),(XX),(XX),(XX),[=E29*$E$22],[=F29*$E$22],[=G29*$E$22]
    % of Rev,XX%,XX%,XX%,XX%,[=E60/E29],[=F60/F29],[=G60/G29]
(-) Δ NWC,(XX),(XX),(XX),(XX),[=(E29-D29)*$E$23],[=(F29-E29)*$E$23],[=(G29-F29)*$E$23]
    % of Δ Rev,XX%,XX%,XX%,XX%,[=E62/(E29-D29)],[=F62/(F29-E29)],[=G62/(G29-F29)]
,,,,,,
Unlevered FCF,XXX,XXX,XXX,XXX,[=E57+E58-E60-E62],[=F57+F58-F60-F62],[=G57+G58-G60-G62]
```

**行の参照例** (レイアウト計画に基づく):
- $E$21 = D&A % 仮定 (統合列、行 21)
- $E$22 = CapEx % の仮定 (統合列、行 22)
- $E$23 = NWC % 仮定 (統合列、行 23)
- E29 = 年間収益 (行 29)
- E45 = 年の NOPAT (行 45)

**数式を記述する前に**: これらの行番号が実際のレイアウトと一致していることを確認してください。 1 つの列をテストしてから、全体にコピーします。

**セクション 6: 割引と評価**
```csv
DCF Valuation,2024E,2025E,2026E,2027E,2028E,Terminal
Unlevered FCF ($M),XXX,XXX,XXX,XXX,XXX,
Period,0.5,1.5,2.5,3.5,4.5,
Discount Factor,0.XX,0.XX,0.XX,0.XX,0.XX,
PV of FCF ($M),XXX,XXX,XXX,XXX,XXX,
,,,,,,
Terminal FCF ($M),,,,,,,XXX
Terminal Value ($M),,,,,,,XXX
PV Terminal Value ($M),,,,,,,XXX
,,,,,,
Valuation Summary ($M),,,,,,
Sum of PV FCFs,XXX,,,,,
PV Terminal Value,XXX,,,,,
Enterprise Value,XXX,,,,,
(-) Net Debt,(XX),,,,,
Equity Value,XXX,,,,,
,,,,,,
Shares Outstanding (M),XX.X,,,,,
IMPLIED PRICE PER SHARE,$XX.XX,,,,,
Current Stock Price,$XX.XX,,,,,
Implied Upside/(Downside),XX%,,,,,
```

<a id="wacc-sheet-structure"></a>
### WACCシートの構造

```csv
COST OF EQUITY CALCULATION,,
Risk-Free Rate (10Y Treasury),X.XX%,[Yellow input]
Beta (5Y monthly),X.XX,[Yellow input]
Equity Risk Premium,X.XX%,[Yellow input]
Cost of Equity,X.XX%,[Calculated blue]
,,
COST OF DEBT CALCULATION,,
Credit Rating,AA-,[Yellow input]
Pre-Tax Cost of Debt,X.XX%,[Yellow input]
Tax Rate,XX.X%,[Link to DCF sheet]
After-Tax Cost of Debt,X.XX%,[Calculated blue]
,,
CAPITAL STRUCTURE,,
Current Stock Price,$XX.XX,[Link to DCF]
Shares Outstanding (M),XX.X,[Link to DCF]
Market Capitalization ($M),"X,XXX",[Calculated]
,,
Total Debt ($M),XXX,[Yellow input]
Cash & Equivalents ($M),XXX,[Yellow input]
Net Debt ($M),XXX,[Calculated]
,,
Enterprise Value ($M),"X,XXX",[Calculated]
,,
WACC CALCULATION,Weight,Cost,Contribution
Equity,XX.X%,X.X%,X.XX%
Debt,XX.X%,X.X%,X.XX%
,,
WEIGHTED AVERAGE COST OF CAPITAL,X.XX%,[Green output]
```

**主要な WACC 式:**
```
Market Cap = Price × Shares
Net Debt = Total Debt - Cash
Enterprise Value = Market Cap + Net Debt
Equity Weight = Market Cap / EV
Debt Weight = Net Debt / EV
WACC = (Cost of Equity × Equity Weight) + (After-tax Cost of Debt × Debt Weight)
```

<a id="sensitivity-analysis-bottom-of-dcf-sheet"></a>
### 感度解析（DCFシート下部）

**用語の注意**: 「感度テーブル」 = 各データ セルに行ヘッダー、列ヘッダー、および数式を含む単純な 2D グリッド。 Excel の「データ テーブル」機能 (データ → What-If 分析 → データ テーブル) ではありません。 openpyxl を使用して、通常の Excel 数式を各セルに書き込みます。

**場所**: DCF シートの 87 行目以降 (別のシートではありません)

**3 つの感度テーブル、垂直に積み上げられています:**

1. **WACC と永久成長** (行 87 ～ 100) - 5x5 グリッド = 数式を含む 25 セル
2. **収益成長率と EBIT マージン** (行 102 ～ 115) - 5x5 グリッド = 数式を含む 25 個のセル
3. **ベータ vs リスクフリーレート** (行 117 ～ 130) - 5x5 グリッド = 数式を含む 25 セル

**作成する式の合計: 75** (これは必須であり、オプションではありません)

**重要**: openpyxl を使用して、すべての感度テーブルのセルにプログラムで数式を入力する必要があります。線形近似のショートカットは使用しないでください。手動手順に関するプレースホルダー テキストやメモを残さないでください。 「複雑だから」という理由でセルを空のままにすることを正当化しないでください。Python ループを使用して数式を生成します。

**テーブルセットアップ:**
1. 行/列ヘッダー (テストする仮定値) を含むテーブル構造を作成します。
2. すべてのデータ セルに次の式を入力します。
   - 行ヘッダー値を使用します (例: WACC = 9.0%)
   - 列ヘッダーの値を使用します (例: Terminal Growth = 3.0%)
   - これらの特定の仮定を使用して完全な DCF を再計算します。
   - そのシナリオのモデルが示唆する株価を返します
3. 納品時にはすべてのセルに有効な数式が含まれている必要があります
4. 条件付き書式設定を使用してセルを書式設定します。値が大きい場合は緑のスケール、値が小さい場合は赤のスケール
5. 基本ケースのセルを太字にする
6. 表の間には 1 ～ 2 行の空白行を残します

**手動介入は必要ありません** - ユーザーがファイルを開いたときに感度テーブルが完全に機能している必要があります。

<a id="case-selector-implementation"></a>
## ケースセレクターの実装

**3 つのケースのフレームワーク:**

<a id="bear-case"></a>
### ベアケース
- 保守的な収益増加（過去の範囲の下限）
- マージンの圧縮または拡張なし
- WACCの上昇（リスクプレミアムの増加）
- 永久成長率が低い
- より高い設備投資の想定

<a id="base-case"></a>
### 基本ケース
- コンセンサスまたは経営陣のガイダンスによる収益の増加
- 営業レバレッジに基づいた適度な利益拡大
- 現在の市場が示唆する WACC
- GDPと連動したターミナル成長率（2.5～3.0%）
- 標準的な設備投資の想定

<a id="bull-case"></a>
### ブルケース
- 楽観的な収益成長 (予測の上限)
- 大幅な利益拡大
- WACCの低下（リスクプレミアムの低下）
- より高いターミナル成長率 (3.5-5.0%)
- 売上高に対する設備投資比率の低下

**式の実装:**

**全体に散在するネストされた IF 式は使用しないでください。** 代わりに、INDEX 式または OFFSET 式を使用して適切なシナリオ ブロックから取得する統合列を作成します。

**推奨パターン (INDEX を使用):**
`=INDEX(B10:D10, 1, $B$6)` ここで、`B10:D10` = ベア/ベース/ブル値、`1` = 行オフセット、`$B$6` = ケース セレクター セル (1、2、または 3)

**次に、すべての予測で統合列**を参照します。
`Revenue Year 1: =D29*(1+$E$10)` ここで、$E$10 は、1 年目の成長の統合列の値です。

このアプローチにより、シナリオ ロジックが集中化され、モデルの監査と保守が容易になります。

<a id="deliverables-structure"></a>
## 成果物の構造

**ファイル名**: `[Ticker]_DCF_Model_[Date].xlsx`

**シート 2 枚**:
1. **DCF** - ベア/ベース/ブルのケースを含む完全なモデル + 下部の 3 つの感応度表 (WACC 対ターミナル成長、収益成長対 EBIT マージン、ベータ対リスクフリーレート)
2. **WACC** - 資本コストの計算

**主な機能**: シナリオ選択セル (1/2/3)、INDEX/OFFSET 式を備えた統合列、色分けされたセル、すべての入力のセル コメント、プロフェッショナル ボーダー

<a id="best-practices"></a>
## ベストプラクティス

<a id="model-construction"></a>
### モデルの構築
1. **段階的に構築**: 次のセクションに進む前に、各セクションを完了してください。
2. **構築としてテスト**: サンプル番号を入力して式を検証します
3. **一貫した構造を使用**: 同様の計算は同様のパターンに従います
4. **複雑な数式にコメントする**: 珍しい計算についてメモを追加します
5. **ビルトインチェック**: 該当する場合、合計チェックと残高チェック

<a id="documentation"></a>
### ドキュメント
1. **すべての仮定を文書化**: 主要な入力の背後にある推論を説明する
2. **データ ソースを引用する**: 各データ ポイントの出所に注意してください。
3. **方法論の説明**: 非標準的なアプローチについて説明します
4. **不確実性をフラグ**: 視界が制限されている領域を強調表示します。

<a id="quality-control"></a>
### 品質管理
1. **計算のクロスチェック**: 複数の方法で数学を検証します。
2. **ストレス テストの仮定**: モデルが堅牢であることを確認するための実行感度
3. **ピアレビュー**: 他の人に数式をチェックしてもらいます
4. **バージョン管理**: 作業の進行に応じてバージョンを保存します。

<a id="common-variations"></a>
## 一般的なバリエーション

<a id="high-growth-technology-companies"></a>
### 高成長テクノロジー企業
- 長期の予測期間（7～10年）
- より高い初期成長率 (20 ～ 30%)
- 時間の経過とともにマージンが大幅に拡大
- より高い WACC (12-15%)
- モデルのユニットエコノミクス (ユーザー、ARPU など)

<a id="maturestable-companies"></a>
### 成熟/安定した企業
- 予測期間の短縮（3～5年）
- 緩やかな成長率 (GDP +1-3%)
- 安定したマージン
- WACC の低下 (7-9%)
- 現金の創出と資本配分に重点を置く

<a id="cyclical-companies"></a>
### 循環型企業
- 経済サイクルをモデル化
- サイクルの半ばでマージンを正規化する
- 谷とピークのシナリオを考慮する
- 循環性を考慮してベータを調整する

<a id="multi-segment-companies"></a>
### マルチセグメント企業
- ビジネスユニットごとに個別の DCF
- セグメントごとに異なる成長率と利益率
- 事業別価値合算法（SOTP）による評価
- 相乗効果を考慮する

<a id="troubleshooting"></a>
## トラブルシューティング

**エラーや不当な結果が発生した場合は、詳細なデバッグ ガイダンスについて [TROUBLESHOOTING.md](TROUBLESHOOTING.md) をお読みください。**

<a id="workflow-integration"></a>
## ワークフローの統合

<a id="at-start-of-dcf-build"></a>
### DCF ビルドの開始時

1. **市場データを収集**:
   - 現在の市場データに利用可能な MCP サーバーを確認する
   - Web 検索/フェッチを使用して株価、ベータ、その他の市場指標を取得する
   - 特定のデータが必要ならユーザーに依頼する

2. **過去の財務情報を収集**:
   - 利用可能な MCP サーバー (Daloopa など) を確認します。
   - MCPで取得できなければユーザーに依頼する
   - 必要に応じて 10-K から手動で抽出

3. **このスキルで詳しく説明されている DCF 手法を使用してモデルの構築を開始します**

<a id="during-model-construction"></a>
### モデル構築中

1. **openpyxl と数式 (ハードコードされた値ではない) を使用して Excel モデルを構築**
2. **数式の構築と書式設定については、xlsx スキルの規則に従ってください**
3. **ユーザーが要求した場合、または特定のブランドのガイドラインが提供されている場合にのみ、塗りつぶしの色を適用します**

<a id="before-delivering-model-mandatory"></a>
### モデル納品前（必須）

1. **構造を確認してください**:
   - 予測年にわたる仮定を含むベア/ベース/ブルのシナリオ ブロック
   - 正しいシナリオブロックを参照する数式を使用して機能するケースセレクター
   - DCFシートの下部にある感度表（別紙ではありません）
   - フォントの色: 青の入力、黒の数式、緑のシートのリンク
   - すべてのハードコードされた入力に対するセルのコメント
   - 主要セクションの周囲に専門的な境界線

2. **式を再計算**: `python recalc.py model.xlsx 30` を実行します。

3. **出力を確認してください**:
   - `status`が`"success"`の場合 → 手順4へ
   - `status` が `"errors_found"` の場合 → `error_summary` を確認し、デバッグ ガイダンスについて [TROUBLESHOOTING.md](TROUBLESHOOTING.md) を読んでください。

4. **エラーを修正し、ステータスが「成功」になるまで recalc.py を再実行します**

5. **スポットチェック式**:
   - 1 つの FCF 式をテストします - それは正しい仮定行を参照していますか?
   - シナリオ選択セルを変更します - 統合列は適切に更新されますか?
   - 収益式が統合列を参照していることを確認します (ネストされた IF 式ではない)

6. **納品モデル**

<a id="available-data-sources"></a>
### 利用可能なデータソース

- **MCP サーバー**: 構成されている場合 (過去の財務データ用の Daloopa)
- **Web 検索/取得**: 現在の株価、ベータ、市場データの場合
- **ユーザー提供データ**: 過去の財務状況、コンセンサス推定
- **手動抽出**: フォールバックとしての SEC EDGAR 申告

<a id="final-output-checklist"></a>
## 最終出力チェックリスト

DCF モデルを提供する前に:

**必須:**
- ステータスが「成功」になるまで (数式エラーがゼロになるまで) `python recalc.py model.xlsx 30` を実行します。
- 2枚：DCF（下部感度あり）、WACC
- フォントの色: 青 = 入力、黒 = 数式、緑 = シート リンク
- すべてのハードコードされた入力に対するセルのコメント
- 数式が完全に入力された感度テーブル
- 主要セクションの周囲に専門的な境界線

**検証:**
- OpExは売上高に基づく（売上総利益に基づかない）
- 継続価値 EV の 50 ～ 70%
- 永久成長 < WACC
- 税率 21～28%
- ファイル名: `[Ticker]_DCF_Model_[Date].xlsx`