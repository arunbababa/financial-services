> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task2-financial-modeling.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="task-2-financial-modeling---detailed-workflow"></a>
# タスク 2: 財務モデリング - 詳細なワークフロー

このドキュメントでは、カバレッジ開始スキルのタスク 2 (財務モデリング) を実行するための段階的な手順を説明します。

<a id="task-overview"></a>
## タスクの概要

**目的**: 過去の財務を抽出し、予測とシナリオを備えた包括的な Excel 財務モデルを構築します。

**前提条件**: ⚠️ 開始する前に確認してください
- **必須**: 会社の財務データへのアクセス
  - 上場企業向け: SEC EDGAR の最新 10-K および最近の 10-Q
  - 非上場企業の場合: 入手可能な情報源からの財務諸表または推計値
  - または: ユーザーが提供した事前に抽出された過去の財務データ
- **オプション**: ビジネスコンテキストに関する企業調査 (タスク 1)

**出力**: 6 つの必須タブを含む Excel 財務モデル (.xlsx):
1. 売上高モデル
2. 損益計算書
3. キャッシュフロー計算書
4. 貸借対照表
5. シナリオ
6. DCF入力

---

<a id="input-verification"></a>
## 入力検証

**始める前に - チェックしてください:**

**オプション A: 財務情報を直接抽出する (最も一般的)**
- [ ] 10-K の提出書類 (上場企業) にアクセスできますか?
- [ ] それとも財務諸表にアクセスできますか (非上場企業)?
- [ ] 履歴抽出用の Excel ファイルを作成する準備はできましたか?

**オプション B: ユーザーは事前に抽出された財務情報を持っています**
- [ ] 過去の財務ファイルは提供されていますか? (.xlsx またはその他の形式)
- [ ] 3 ～ 5 年分の損益計算書、キャッシュ フロー、貸借対照表が含まれていますか?
- [ ] データはクリーンですぐに使用できますか?

**オプションのコンテキスト:**
- [ ] ビジネスを理解するための企業調査 (タスク 1) は完了しましたか?

**検証が失敗した場合**: 続行する前に、停止して財務諸表 (10-K または同等のもの) にアクセスしてください。

---

<a id="model-structure-and-formatting"></a>
## モデルの構造とフォーマット

<a id="color-coding-industry-standard"></a>
### カラーコーディング (業界標準)
- **青色のテキスト**: ハードコードされた入力 (ユーザーは変更可能)
- **黒文字**: 数式と計算
- **緑色のテキスト**: 他のシートへのリンク
- **赤色のテキスト**: エラーまたはフラグ (解決する必要があります)

<a id="formatting-standards"></a>
### 書式設定の標準
- プロフェッショナルなボーダーとシェーディング
- 明確なセクション見出し
- 折りたたみ可能にするためのグループ化された行
- キー入力/出力の名前付き範囲
- 数式にハードコードされた数値は使用できません (12 か月などの定数を除く)
- 明確な単位 (千ドル、百万ドルなど)

<a id="formula-best-practices"></a>
### 数式のベストプラクティス
- すべての数字は仮定から導き出される必要があります
- 仮定を変更 → モデル全体を更新
- 循環参照はありません
- キーセルに名前付き範囲を使用する
- 数式をシンプルかつ監査可能に保つ
- 複雑な計算のコメントを追加する

---

<a id="step-by-step-modeling-workflow"></a>
## 段階的なモデリングのワークフロー

<a id="step-1-extract-historical-financials"></a>
### ステップ 1: 過去の財務データを抽出する

**過去の財務データが既に抽出されている場合は、ステップ 2 に進みます。**

**上場企業の場合:**

1. **10-K ファイリングをダウンロード**
   - SEC エドガー (https://www.sec.gov/edgar/searchedgar/companysearch.html) に移動します。
   - 会社名またはティッカーを検索する
   - 最新の10-K（アニュアルレポート）をダウンロード
   - 項目 8: 財務諸表および補足データに移動します。

2. **過去の財務 Excel ファイルを作成**
   - ファイル名: `[Company]_Historical_Financials_[Date].xlsx`
   - このファイルはモデルの基礎となります

3. **損益計算書の抽出 (3 ～ 5 年)**
   - シート 1:「過去の損益計算書」を作成します。
   - 3 ～ 5 年間のすべてのラインアイテムを抽出します。
     - 売上高（合計、および開示されている場合はセグメント別）
     - 売上原価 / COGS
     - 売上総利益
     - 営業費用（研究開発、販売およびマーケティング、一般管理費の内訳）
     - EBITDA (非開示の場合は計算: EBIT + D&A)
     - EBIT/営業利益
     - 支払利息/受取利息
     - その他の収入・支出
     - 税引前利益
     - 法人所得税と税率
     - 当期純利益
     - EPS（基本および希薄化後）
     - 発行済株式数（基本および希薄化後）

4. **キャッシュ フロー計算書の抽出 (3 ～ 5 年)**
   - シート 2:「過去のキャッシュ フロー」を作成する
   - すべての行項目を抽出します。
     - 営業活動（純利益ベース）
     - 減価償却費と償却費
     - 株式報酬
     - 運転資本（売掛金、在庫、買掛金）の推移
     - 営業活動によるキャッシュフロー
     - 投資活動 (CapEx、買収)
     - 財務活動（借入金の発行・返済、資本、配当）
     - 現金の純変動
     - 期首および期末の現金残高

5. **貸借対照表の抽出 (3 ～ 5 年)**
   - シート 3:「過去の貸借対照表」を作成します。
   - すべての行項目を抽出します。
     - 流動資産（現金、債権、在庫、その他）
     - 非流動資産（PP&E、無形資産、のれん）
     - 総資産
     - 流動負債（買掛金、未払費用、短期有利子負債）
     - 固定負債（長期借入金、繰延税金）
     - 負債総額
     - 株主資本（普通株式、利益剰余金）
     - 負債合計+資本合計

6. **過去の財務指標の計算**
   - シート 4:「過去の財務指標」を作成します。
   - 財務諸表から計算します。
     - 売上高成長率 (前年比)
     - 粗利率 %
     - EBITDA利益率%
     - 営業利益率%
     - 純利益率 %
     - フリー キャッシュ フロー (CFO - CapEx)
     - FCF利益率%
     - ROIC（概算値：NOPAT / 投下資本）
     - 負債/自己資本比率
     - 流動比率（流動資産／流動負債）

7. **ドキュメントのソースとメモ**
   - シート5「メモ」を作成します。
   - 文書:
     - 10-Kの提出日と会計年度末
     - 1 回限りの項目または調整が記載されている場合
     - 非 GAAP と GAAP の違い
     - セグメントの内訳 (売上高を製品/地域ごとに分割した場合)
     - データ品質に関する注意事項と制限事項

**非上場企業の場合:**

1. **利用可能なデータを収集**
   - 財務諸表（入手可能な場合）
   - 売上高の数値を記載したプレスリリース
   - 資金調達のお知らせ
   - 業界の推定値または比較可能な企業データ

2. **簡易履歴ファイルの作成**
   - 推定売上高 (入手可能な場合)
   - 推定利益率（必要に応じて比較対象から）
   - 主要な比率と指標
   - すべての仮定と情報源を文書化する

**検証:**
- [ ] 3 つの財務諸表すべてを抽出 (3 ～ 5 年)
- [ ] 数値は各財務諸表間で整合している（純利益が一致）
- [ ] 主要な指標が正しく計算される
- [ ] Excel ファイルが保存され、開くことができます
- [ ] データソースの文書化 (10-K の日付、ページ番号)

**予測モデルの基礎が完成しました。ステップ 2 に進みます。**
   - 設備投資
   - 運転資本項目
   - 借入金および支払利息
   - 株式数（基本および希薄化後）

3. **入力用の履歴データを整理する**
   - 3～5年分の実績を準備する
   - 損益計算書、キャッシュフロー計算書、貸借対照表のタブに直接入力されます。
   - 過去の年度を列に配置し、その右に予測年度を配置する

4. **過去の傾向を計算**
   - 売上高のCAGR
   - 利益率の推移
   - 売上高に対する営業費用比率の低下効果
   - 運転資本のパターン
   - 売上高に対する設備投資の割合（%）
   - これらの傾向は予測の仮定に影響を与えます

**注意**: 前提条件は、別のタブではなく、各タブに青色のテキスト入力として直接文書化されます。

<a id="step-2-model-revenue"></a>
### ステップ 2: 売上高のモデル化

**重要: これはモデルの最も重要かつ詳細な部分です。**

<a id="a-revenue-by-productcategory-20-30-rows"></a>
#### A. 製品/カテゴリ別売上高 (20 ～ 30 行)

詳細なテーブルを作成します。
```
                        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
Product Category A
  Sub-product A1        XX      XX      XX      XX      XX      XX      XX      XX      XX
  Sub-product A2        XX      XX      XX      XX      XX      XX      XX      XX      XX
  Sub-product A3        XX      XX      XX      XX      XX      XX      XX      XX      XX
  Category A Total      XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Total Rev        X%      X%      X%      X%      X%      X%      X%      X%      X%
  YoY Growth %          -       X%      X%      X%      X%      X%      X%      X%      X%

Product Category B
  [Similar structure]

[Continue for all product categories]

Services Revenue        XX      XX      XX      XX      XX      XX      XX      XX      XX
Other Revenue           XX      XX      XX      XX      XX      XX      XX      XX      XX

TOTAL REVENUE           XX      XX      XX      XX      XX      XX      XX      XX      XX
Total Revenue Growth %  -       X%      X%      X%      X%      X%      X%      X%      X%
```

**主な要件:**
- カテゴリごとの売上高の絶対額（百万ドル） を表示します
- カテゴリごとに売上高全体に占める割合を計算します
- カテゴリごとに前年比成長率を表示します
- 詳細なサブカテゴリが必要です (3 ～ 5 つのトップレベル カテゴリだけではありません)
- 時間の経過に伴うミックスシフトを表示
- すべての予測を「仮定」タブにリンクする

<a id="b-revenue-by-geography-15-20-rows"></a>
#### B. 地域別売上高 (15 ～ 20 行)

詳細なテーブルを作成します。
```
                        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
North America
  United States         XX      XX      XX      XX      XX      XX      XX      XX      XX
  Canada                XX      XX      XX      XX      XX      XX      XX      XX      XX
  Mexico                XX      XX      XX      XX      XX      XX      XX      XX      XX
  NA Total              XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Total            X%      X%      X%      X%      X%      X%      X%      X%      X%
  YoY Growth %          -       X%      X%      X%      X%      X%      X%      X%      X%

Europe
  UK                    XX      XX      XX      XX      XX      XX      XX      XX      XX
  Germany               XX      XX      XX      XX      XX      XX      XX      XX      XX
  France                XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other Europe          XX      XX      XX      XX      XX      XX      XX      XX      XX
  Europe Total          XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Total            X%      X%      X%      X%      X%      X%      X%      X%      X%
  YoY Growth %          -       X%      X%      X%      X%      X%      X%      X%      X%

Asia-Pacific
  [Similar structure]

Rest of World
  [Similar structure]

TOTAL REVENUE           XX      XX      XX      XX      XX      XX      XX      XX      XX
```

**検証:**
- 製品別売上高の合計 = 地域別売上高の合計 = 売上高合計
- すべてのパーセンテージの合計は 100% になります
- 成長率は正しく計算されました

<a id="c-revenue-by-channel-if-applicable"></a>
#### C. チャネル別売上高 (該当する場合)

```
                        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
Direct Sales            XX      XX      XX      XX      XX      XX      XX      XX      XX
E-commerce/Online       XX      XX      XX      XX      XX      XX      XX      XX      XX
Wholesale/Partner       XX      XX      XX      XX      XX      XX      XX      XX      XX
Retail Stores
  Company-owned stores  XX      XX      XX      XX      XX      XX      XX      XX      XX
  Store count           XX      XX      XX      XX      XX      XX      XX      XX      XX
  Sales per store       XX      XX      XX      XX      XX      XX      XX      XX      XX
Other Channels          XX      XX      XX      XX      XX      XX      XX      XX      XX

TOTAL REVENUE           XX      XX      XX      XX      XX      XX      XX      XX      XX
```

<a id="step-3-model-operating-expenses"></a>
### ステップ 3: 営業経費のモデル化

<a id="a-cost-of-revenue"></a>
#### A. 売上原価
1. **COGS コンポーネントの内訳**
   - 製品原価（材料費、製造費）
   - 配送と物流
   - サービス提供コスト
   - その他の直接費用

2. **売上高に連動させる**
   - COGSを売上高比率として計算します
   - 年度別の売上総利益率をモデル化
   - 「仮定」タブへのリンク

<a id="b-rd-expenses"></a>
#### B. 研究開発費
```
Research & Development  2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
R&D Headcount           XX      XX      XX      XX      XX      XX      XX      XX      XX
R&D Comp per head       XX      XX      XX      XX      XX      XX      XX      XX      XX
R&D Personnel Costs     XX      XX      XX      XX      XX      XX      XX      XX      XX
R&D Other Costs         XX      XX      XX      XX      XX      XX      XX      XX      XX
Total R&D               XX      XX      XX      XX      XX      XX      XX      XX      XX
% of Revenue            X%      X%      X%      X%      X%      X%      X%      X%      X%
```

<a id="c-sales--marketing-expenses"></a>
#### C. 販売およびマーケティング費用
```
Sales & Marketing       2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
S&M Headcount           XX      XX      XX      XX      XX      XX      XX      XX      XX
S&M Comp per head       XX      XX      XX      XX      XX      XX      XX      XX      XX
S&M Personnel Costs     XX      XX      XX      XX      XX      XX      XX      XX      XX
Marketing Spend         XX      XX      XX      XX      XX      XX      XX      XX      XX
S&M Other Costs         XX      XX      XX      XX      XX      XX      XX      XX      XX
Total S&M               XX      XX      XX      XX      XX      XX      XX      XX      XX
% of Revenue            X%      X%      X%      X%      X%      X%      X%      X%      X%
```

<a id="d-general--administrative"></a>
#### D. 一般管理費
```
G&A                     2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E
G&A Headcount           XX      XX      XX      XX      XX      XX      XX      XX      XX
G&A Comp per head       XX      XX      XX      XX      XX      XX      XX      XX      XX
G&A Personnel Costs     XX      XX      XX      XX      XX      XX      XX      XX      XX
G&A Other Costs         XX      XX      XX      XX      XX      XX      XX      XX      XX
Total G&A               XX      XX      XX      XX      XX      XX      XX      XX      XX
% of Revenue            X%      X%      X%      X%      X%      X%      X%      X%      X%
```

<a id="e-depreciation--amortization"></a>
#### E. 減価償却費と償却費
- CapEx スケジュールへのリンク
- 仮定に基づいて減価償却率を適用する
- 年間 D&A を計算する

<a id="step-4-build-income-statement"></a>
### ステップ 4: 損益計算書の作成

**40 ～ 50 個の明細項目を含む完全な損益計算書を作成します:**

```
INCOME STATEMENT        2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E

REVENUE
[Link to Revenue Model tab]
Total Revenue           XX      XX      XX      XX      XX      XX      XX      XX      XX
  YoY Growth %          -       X%      X%      X%      X%      X%      X%      X%      X%

COST OF REVENUE
[Link to COGS breakdown]
Total COGS              XX      XX      XX      XX      XX      XX      XX      XX      XX

GROSS PROFIT            XX      XX      XX      XX      XX      XX      XX      XX      XX
  Gross Margin %        X%      X%      X%      X%      X%      X%      X%      X%      X%

OPERATING EXPENSES
Total R&D               XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Revenue          X%      X%      X%      X%      X%      X%      X%      X%      X%
Total S&M               XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Revenue          X%      X%      X%      X%      X%      X%      X%      X%      X%
Total G&A               XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Revenue          X%      X%      X%      X%      X%      X%      X%      X%      X%
Depreciation & Amort.   XX      XX      XX      XX      XX      XX      XX      XX      XX

Total Operating Exp.    XX      XX      XX      XX      XX      XX      XX      XX      XX
  % of Revenue          X%      X%      X%      X%      X%      X%      X%      X%      X%

EBITDA                  XX      XX      XX      XX      XX      XX      XX      XX      XX
  EBITDA Margin %       X%      X%      X%      X%      X%      X%      X%      X%      X%

EBIT                    XX      XX      XX      XX      XX      XX      XX      XX      XX
  EBIT Margin %         X%      X%      X%      X%      X%      X%      X%      X%      X%

Interest expense        (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
Interest income         XX      XX      XX      XX      XX      XX      XX      XX      XX
Other income/(expense)  XX      XX      XX      XX      XX      XX      XX      XX      XX

Pre-tax income          XX      XX      XX      XX      XX      XX      XX      XX      XX

Income tax              (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  Tax rate %            X%      X%      X%      X%      X%      X%      X%      X%      X%

NET INCOME              XX      XX      XX      XX      XX      XX      XX      XX      XX
  Net Margin %          X%      X%      X%      X%      X%      X%      X%      X%      X%

SHARES OUTSTANDING
Basic shares (M)        XX      XX      XX      XX      XX      XX      XX      XX      XX
Diluted shares (M)      XX      XX      XX      XX      XX      XX      XX      XX      XX

EARNINGS PER SHARE
Basic EPS               $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX
Diluted EPS             $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX   $X.XX
```

<a id="step-5-build-cash-flow-statement"></a>
### ステップ 5: キャッシュ フロー計算書の作成

```
CASH FLOW STATEMENT     2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E

OPERATING ACTIVITIES
Net Income              XX      XX      XX      XX      XX      XX      XX      XX      XX
Adjustments:
  Depreciation & Amort. XX      XX      XX      XX      XX      XX      XX      XX      XX
  Stock-based comp      XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other non-cash        XX      XX      XX      XX      XX      XX      XX      XX      XX

Changes in WC:
  Accounts Receivable   (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  Inventory             (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  Accounts Payable      XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other working capital (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)

Cash from Operations    XX      XX      XX      XX      XX      XX      XX      XX      XX

INVESTING ACTIVITIES
Capital Expenditures    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
Acquisitions            (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
Other investing         XX      XX      XX      XX      XX      XX      XX      XX      XX

Cash from Investing     (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)

FREE CASH FLOW          XX      XX      XX      XX      XX      XX      XX      XX      XX
  FCF Margin %          X%      X%      X%      X%      X%      X%      X%      X%      X%

FINANCING ACTIVITIES
Debt issuance           XX      XX      XX      XX      XX      XX      XX      XX      XX
Debt repayment          (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
Equity issuance         XX      XX      XX      XX      XX      XX      XX      XX      XX
Dividends paid          (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
Other financing         XX      XX      XX      XX      XX      XX      XX      XX      XX

Cash from Financing     XX      XX      XX      XX      XX      XX      XX      XX      XX

NET CHANGE IN CASH      XX      XX      XX      XX      XX      XX      XX      XX      XX

Beginning Cash          XX      XX      XX      XX      XX      XX      XX      XX      XX
Ending Cash             XX      XX      XX      XX      XX      XX      XX      XX      XX
```

<a id="step-6-build-balance-sheet"></a>
### ステップ 6: 貸借対照表を作成する

35 ～ 45 項目の完全な貸借対照表を作成します。

```
BALANCE SHEET           2021A   2022A   2023A   2024A   2025E   2026E   2027E   2028E   2029E

ASSETS
Current Assets:
  Cash & Equivalents    XX      XX      XX      XX      XX      XX      XX      XX      XX
  Accounts Receivable   XX      XX      XX      XX      XX      XX      XX      XX      XX
  Inventory             XX      XX      XX      XX      XX      XX      XX      XX      XX
  Prepaid expenses      XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other current assets  XX      XX      XX      XX      XX      XX      XX      XX      XX
Total Current Assets    XX      XX      XX      XX      XX      XX      XX      XX      XX

Non-Current Assets:
  PP&E, gross           XX      XX      XX      XX      XX      XX      XX      XX      XX
  Accumulated Depr.     (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  PP&E, net             XX      XX      XX      XX      XX      XX      XX      XX      XX
  Intangible assets     XX      XX      XX      XX      XX      XX      XX      XX      XX
  Goodwill              XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other non-current     XX      XX      XX      XX      XX      XX      XX      XX      XX
Total Non-Current       XX      XX      XX      XX      XX      XX      XX      XX      XX

TOTAL ASSETS            XX      XX      XX      XX      XX      XX      XX      XX      XX

LIABILITIES
Current Liabilities:
  Accounts Payable      XX      XX      XX      XX      XX      XX      XX      XX      XX
  Accrued expenses      XX      XX      XX      XX      XX      XX      XX      XX      XX
  Deferred revenue      XX      XX      XX      XX      XX      XX      XX      XX      XX
  Current debt          XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other current liab.   XX      XX      XX      XX      XX      XX      XX      XX      XX
Total Current Liab.     XX      XX      XX      XX      XX      XX      XX      XX      XX

Non-Current Liabilities:
  Long-term debt        XX      XX      XX      XX      XX      XX      XX      XX      XX
  Deferred taxes        XX      XX      XX      XX      XX      XX      XX      XX      XX
  Other non-current     XX      XX      XX      XX      XX      XX      XX      XX      XX
Total Non-Current Liab. XX      XX      XX      XX      XX      XX      XX      XX      XX

TOTAL LIABILITIES       XX      XX      XX      XX      XX      XX      XX      XX      XX

EQUITY
  Common stock          XX      XX      XX      XX      XX      XX      XX      XX      XX
  Additional paid-in    XX      XX      XX      XX      XX      XX      XX      XX      XX
  Retained earnings     XX      XX      XX      XX      XX      XX      XX      XX      XX
  Treasury stock        (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)    (XX)
  Other equity          XX      XX      XX      XX      XX      XX      XX      XX      XX
TOTAL EQUITY            XX      XX      XX      XX      XX      XX      XX      XX      XX

TOTAL LIAB + EQUITY     XX      XX      XX      XX      XX      XX      XX      XX      XX

BALANCE CHECK           OK      OK      OK      OK      OK      OK      OK      OK      OK
```

**バランスチェック式:**
- 各年の総資産は総負債 + 資本と等しくなければなりません
- 不均衡がある場合は赤でフラグを立てます

<a id="step-7-build-dcf-inputs-tab"></a>
### ステップ 7: DCF 入力タブの構築

評価用の入力を準備します (タスク 3):

```
DCF INPUTS              2025E   2026E   2027E   2028E   2029E

EBIT                    XX      XX      XX      XX      XX
Tax Rate                X%      X%      X%      X%      X%
NOPAT                   XX      XX      XX      XX      XX

Add: D&A                XX      XX      XX      XX      XX
Less: CapEx             (XX)    (XX)    (XX)    (XX)    (XX)
Less: Chg in NWC        (XX)    (XX)    (XX)    (XX)    (XX)

UNLEVERED FCF           XX      XX      XX      XX      XX

Terminal Year Metrics:
  2029E Revenue         $X,XXX
  2029E EBITDA          $XXX
  2029E EBIT            $XXX
  2029E Unlevered FCF   $XXX
```

<a id="step-8-build-scenarios-tab"></a>
### ステップ 8: [シナリオの構築] タブ

異なる前提条件で 3 つのシナリオを作成します。

<a id="scenario-assumptions-table"></a>
#### シナリオの前提条件表
```
Assumption                      Bull        Base        Bear
Revenue CAGR (2025-2029)        XX%         XX%         XX%
Gross Margin 2029E              XX%         XX%         XX%
EBITDA Margin 2029E             XX%         XX%         XX%
CapEx as % of Revenue           X%          X%          X%
[Add other key assumptions]
```

<a id="scenario-output-table"></a>
#### シナリオ出力テーブル
```
Metric                          Bull        Base        Bear
2029E Revenue ($M)              $X,XXX      $X,XXX      $X,XXX
2029E EBITDA ($M)               $XXX        $XXX        $XXX
2029E EBITDA Margin             XX%         XX%         XX%
2029E Net Income ($M)           $XXX        $XXX        $XXX
2029E EPS                       $X.XX       $X.XX       $X.XX
2029E FCF ($M)                  $XXX        $XXX        $XXX
2029E FCF Margin                XX%         XX%         XX%

Cumulative FCF 2025-2029 ($M)   $XXX        $XXX        $XXX
```

**シナリオの根拠を文書化します:**
- 強気ケース: [楽観的だが達成可能な仮定を説明する]
- 基本ケース: [最も可能性の高いシナリオを説明する]
- 弱気ケース: [下落リスクとトリガーについて説明]

<a id="step-9-quality-check"></a>
### ステップ9: 品質チェック

**モデルの整合性を確認します:**
1. [ ] すべての式をテストする (スポットチェック計算)
2. [ ] 仮定を変更 → モデルが正しく更新されたことを確認する
3. [ ] シナリオ切り替えをテストする
4. [ ] 色分けを確認してください (青/黒/緑)
5. [ ] 全年度で貸借対照表の貸借が一致することを確認する
6. [ ] 循環参照がないことを確認します (Excel でフラグが付けられます)。
7. [ ] 予測内のハードコードされた数値をチェックする
8. [ ] すべてのシート間リンクが機能することを確認する
9. [ ] 売上高合計がすべてのタブで一致していることをテストする
10. [ ] 書式とプレゼンテーションを確認する

---

<a id="quality-standards"></a>
## 品質基準

<a id="model-integrity"></a>
### モデルの完全性
- すべての数式がシート間で適切にリンクされる
- 予測にハードコードされた数値はありません (「仮定」タブを除く)
- 循環参照はありません
- 全年度で貸借対照表の貸借が一致
- シナリオ切り替えは正常に動作します

<a id="completeness"></a>
### 完全性
- 6 つの必須タブすべて: 売上高モデル、損益計算書、キャッシュ フロー計算書、貸借対照表、シナリオ、DCF 入力
- 損益計算書の項目数 40 ～ 50
- 売上高モデル (製品の内訳) の 20 ～ 30 行
- 売上高モデルの 15 ～ 20 行 (地域内訳)
- すべての項目を含む完全なキャッシュ フローと貸借対照表
- ブル/ベース/ベアのシナリオが完了しました

<a id="professional-formatting"></a>
### プロフェッショナルなフォーマット
- 一貫した色分け (青/黒/緑)
- 明確な見出しとラベル
- 適切な境界線とシェーディング
- キーセルの名前付き範囲
- 折りたたみ可能にするためのグループ化された行
- 単位を明確にラベル付け (千ドル対数百万ドル)

<a id="documentation"></a>
### ドキュメント
- 根拠とともに文書化された仮定 (コメントのある青いテキストのセル)
- セルのコメントまたはタブ内のメモセクションに記載されたデータソース
- 複雑な計算をコメント付きで解説
- 方法論の説明

---

<a id="file-naming-convention"></a>
## ファイル命名規則

財務モデルを次のように保存します。
`[Company]_Financial_Model_[Date].xlsx`

例: `Tesla_Financial_Model_2024-10-27.xlsx`

---

<a id="success-criteria"></a>
## 成功基準

成功する財務モデルには次のことが必要です。
1. 6 つの必須タブ (売上高モデル、損益計算書、キャッシュ フロー計算書、貸借対照表、シナリオ、DCF 入力) をすべて備えている
2. 完全に動的であること（仮定の変更→モデルの更新）
3. 予測にハードコードされた数値がない
4. 売上高の詳細な内訳を含めます (製品ごとに 20 ～ 30 行、地域ごとに 15 ～ 20 行)
5. 損益計算書に 40 ～ 50 の明細が含まれる
6. ブル/ベース/ベアのシナリオを含める
7. カラーコーディングを使用して専門的に書式設定する
8. 適切なバランス（貸借対照表、キャッシュフロー）
9. 監査可能でフォローしやすいこと
10. 適切なFCF計算によるバリュエーション分析をサポート

---

<a id="common-model-types---special-considerations"></a>
## 一般的なモデル タイプ - 特別な考慮事項

<a id="high-growth-techsaas"></a>
### 高成長テクノロジー/SaaS
- ARRの成長とネットリテンション率に焦点を当てる
- 製品ラインおよび地域別のモデル
- 研究開発とS&Mに多額の費用がかかる
- 黒字化までの道筋と時期
- ユニットエコノミクス (LTV/CAC)

<a id="e-commerceretail"></a>
### 電子商取引/小売
- 製品カテゴリおよびチャネル別売上高
- 店舗数と既存店売上高成長（該当する場合）
- 在庫回転数と運転資本
- 受注処理・配送コスト（フルフィルメント費用）
- 顧客の獲得

<a id="manufacturingindustrial"></a>
### 製造業・産業用
- 生産能力の稼働率
- 原材料費と価格設定
- 売上総利益率ブリッジ (数量/価格/構成/コスト)
- 設備投資負担の大きいモデル
- 運転資本サイクル

---

<a id="next-steps"></a>
## 次のステップ

タスク 2 を完了すると、財務モデルは次の目的で使用されます。
- **タスク 3 (評価)**: DCF インプット、予測財務データ
- **タスク 4 (グラフ)**: 売上高の推移、利益率のグラフ、シナリオ比較のデータ
- **タスク 5 (レポートの組み立て)**: レポートの表と分析のための財務データ
