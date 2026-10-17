---
name: initiating-coverage
description: Create institutional-quality equity research initiation reports through a 5-task workflow. Tasks must be executed individually with verified prerequisites - (1) company research, (2) financial modeling, (3) valuation analysis, (4) chart generation, (5) final report assembly. Each task produces specific deliverables (markdown docs, Excel models, charts, or DOCX reports). Tasks 3-5 have dependencies on earlier tasks.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：5 つのタスクのワークフローを通じて、機関投資家向けの高品質な株式調査カバレッジ開始レポートを作成します。タスクは、(1) 企業調査、(2) 財務モデリング、(3) バリュエーション分析、(4) チャートの生成、(5) 最終レポートの作成など、検証された前提条件に従って個別に実行する必要があります。各タスクは特定の成果物 (マークダウン ドキュメント、Excel モデル、グラフ、または DOCX レポート) を作成します。タスク 3 ～ 5 には、以前のタスクとの依存関係があります。

<a id="initiating-coverage"></a>
# カバレッジ開始

構造化された 5 つのタスクのワークフローを通じて、機関投資家向けの高品質な株式調査カバレッジ開始レポートを作成します。各タスクは、検証された入力を使用して個別に実行する必要があります。

<a id="overview"></a>
## 概要

このスキルは、機関投資家向けの基準（JPモルガン、ゴールドマン・サックス、モルガン・スタンレー形式）に従って包括的な初回カバレッジレポートを作成します。タスクは個別に実行され、続行する前にそれぞれの前提条件が確認されます。

**デフォルト フォント**: すべてのドキュメント全体で Times New Roman (ユーザーが別途指定しない限り)。

---

<a id="-critical-one-task-at-a-time"></a>
## ⚠️ クリティカル: 一度に 1 つのタスク

**このスキルはシングルタスク モードでのみ動作します。**

<a id="if-user-requests-full-pipeline"></a>
### ユーザーが完全なパイプラインをリクエストした場合

ユーザーがリクエストした場合:
- 「[会社] のカバレッジ開始レポートを作成してください」
- 「[会社] のカバレッジ開始レポートを書いてください」
- 「[会社] の株式調査プロセス全体を行う」
- 「[会社] の 5 つのタスクをすべて完了してください」
- 複数のタスクまたはワークフロー全体の実行を意味するリクエスト

**必須の回答:**

1. **どの特定のタスクを実行するかを尋ねます:**
   ```
   I can help you create an equity research initiation report for [Company].
   This involves 5 separate tasks that need to be completed individually:

   1. Company Research - Research business, management, industry
   2. Financial Modeling - Build projection model
   3. Valuation Analysis - DCF and comparable companies
   4. Chart Generation - Create 25-35 charts
   5. Report Assembly - Compile final report

   Which task would you like to start with?
   ```

2. **ユーザーがすべてのタスクをまとめて明示的に要求する場合:**
   ```
   I understand you'd like to complete the entire initiation report pipeline.
   Currently, this skill supports executing one task at a time, which allows
   for better quality control and review at each stage.

   We're working on a seamless end-to-end workflow that will make this process
   more automated, but for now, we'll need to complete each task separately.

   Would you like to start with Task 1 (Company Research)?
   ```

3. **どのタスクを開始するかを自動的に想定しないでください** - 常にユーザーに確認を求めます。

4. **複数のタスクを連続して実行しないでください** - 1 つのタスクを完了し、出力を提供してから、次のユーザー要求を待ちます。

<a id="task-execution-rules"></a>
### タスク実行ルール

- ✅ ユーザーリクエストごとにタスクを 1 つだけ実行します
- ✅ タスクを開始する前に必ず前提条件を確認してください
- ✅ タスクの出力を提供し、完了を確認する
- ✅ ユーザーが次のタスクを明示的に要求するまで待ちます
- ❌ 複数のタスクを自動的に連鎖させないでください。
- ❌ ユーザーが次のタスクに進みたいと考えないでください
- ❌ 必要な入力が存在することを確認せずにタスク 3 ～ 5 を実行しないでください。

<a id="-deliverables-policy-no-shortcuts"></a>
### ⚠️ 成果物ポリシー: 近道はありません

**指定された出力のみを配信します。余分なドキュメントを作成しないでください。**

各タスクは正確な成果物を指定します。以下のものを作成しないでください。
- ❌「完了概要」
- ❌ 「エグゼクティブサマリー」
- ❌「クイックリファレンスガイド」
- ❌「次のステップのドキュメント」
- ❌「タスク完了レポート」
- ❌ 明示的に指定されていないその他の「役立つ」ドキュメント

**理由**: これらの追加文書はコンテキストを無駄にしており、プロフェッショナルなワークフローの一部ではありません。

**提供するもの**:
- ✅ タスク 1: 調査文書 (.md) — **他には何もありません**
- ✅ タスク 2: 財務モデル (.xlsx) — **他には何もありません**
- ✅ タスク 3: バリュエーション分析 (.md) + Excel タブをタスク 2 ファイルに追加 — **他には何もありません**
- ✅ タスク 4: チャート zip ファイル (.zip) — **他には何もありません**
- ✅ タスク 5: 最終レポート (.docx) — **他には何もありません**

**成果物が上記にリストされていない場合は、作成しないでください。**

---

<a id="task-selection"></a>
## タスクの選択

実行するタスクを選択します:

| タスク | 名前 | 前提条件 | 出力 |
|------|------|--------------|--------|
| **1** | 企業調査 | 会社名/ティッカー | 6,000～8,000語の文書 |
| **2** | 財務モデリング | 10-K または財務情報へのアクセス | Excelモデル（6タブ） |
| **3** | バリュエーション分析 | 財務モデル (タスク 2) | バリュエーション + 目標株価 |
| **4** | チャートの生成 | タスク1、2、3 + 外部データ | 25-35 PNG/JPG チャート |
| **5** | レポートの組み立て | 以前のすべてのタスク (1 ～ 4) | 30～50ページのDOCXレポート |

---

<a id="how-to-use-this-skill"></a>
## このスキルの使い方

<a id="user-request-patterns-and-responses"></a>
### ユーザーの要求パターンと応答

**パターン 1: ユーザーが特定のタスクを指定する**
```
User: "Use initiating-coverage, Task 1 for Tesla"
Response: ✅ Execute Task 1 immediately
```

**パターン 2: ユーザーは「カバレッジ開始レポート」または「完全なパイプライン」を要求します**
```
User: "Create a coverage initiation report for Tesla"
Response: ❌ DO NOT start any task automatically
         ✅ Ask which task to start with (see template above)
```

**パターン 3: ユーザーは「すべてのタスク」または「ワークフロー全体」を実行したい**
```
User: "I want to complete all 5 tasks for Tesla"
Response: ❌ DO NOT chain tasks together
         ✅ Explain one-at-a-time limitation (see template above)
         ✅ Ask if they want to start with Task 1
```

<a id="correct-usage-examples"></a>
### 正しい使用例

**単一タスクの実行:**
```
"Use initiating-coverage skill, Task 1 for Tesla"
"Do Task 2 of initiating-coverage for Tesla"
"Run Task 3 for Tesla using the initiating-coverage skill"
```

**完全なレポートを完了するには (5 回の個別のリクエストが必要です):**
```
Request 1: "Do Task 1 for Tesla" → Complete → Deliver outputs
Request 2: "Do Task 2 for Tesla" → Complete → Deliver outputs
Request 3: "Do Task 3 for Tesla" → Complete → Deliver outputs
Request 4: "Do Task 4 for Tesla" → Complete → Deliver outputs
Request 5: "Do Task 5 for Tesla" → Complete → Deliver outputs
```

<a id="task-execution-order"></a>
### タスクの実行順序

完全なカバレッジ開始レポートを作成するには、次の順序に従って個別のユーザー リクエストでタスクを実行する必要があります。

```
Request 1: Task 1 - Company Research (independent)
           ↓ [User reviews outputs and requests next task]
Request 2: Task 2 - Financial Modeling (independent)
           ↓ [User reviews outputs and requests next task]
Request 3: Task 3 - Valuation Analysis (requires Task 2 output)
           ↓ [User reviews outputs and requests next task]
Request 4: Task 4 - Chart Generation (requires Tasks 2 & 3 outputs)
           ↓ [User reviews outputs and requests next task]
Request 5: Task 5 - Report Assembly (requires ALL previous task outputs)
```

**注意**: タスク 1 と 2 は任意の順序で実行できます。タスク 3 ～ 5 には厳密な依存関係があるため、続行する前に入力を検証する必要があります。

---

<a id="task-1-company-research"></a>
## タスク 1: 企業調査

**目的**: 企業の事業、経営、競争上の地位、業界、リスクを調査します。

**前提条件**: ✅ なし (完全に独立)
- 会社名またはティッカーシンボル

**プロセス**:
1. 提供された会社名/ティッカーを確認してください
2. 詳細な手順をreferences/task1-company-research.mdからロードします。
3. 定性調査ワークフローの実行
4. 調査文書の納品

**出力**: 企業調査ドキュメント (6,000 ～ 8,000 ワード)
- 会社概要・沿革
- 経営経歴（300～400ワード × 3～4人の役員）
- 製品とサービスの分析
- 業界概要
- 競合分析 (5 ～ 10 社の競合他社)
- TAM サイジング
- リスク評価 (8 ～ 12 のリスク)

**ファイル名**: `[Company]_Research_Document_[Date].md`

**⚠️ この 1 ファイルのみを配信します。完了概要や追加の書類はありません。**

**⚠️ ショートカットを使用しないでください:**
- ✅ 6,000～8,000 ワード完全に書きます (要約ではありません)
- ✅ 3～4人の幹部全員の300～400ワードの経歴を完成させる
- ✅ 5 ～ 10 社の競合他社をすべて徹底的に分析する
- ✅ 4 つのカテゴリにわたる 8 ～ 12 のリスクをすべてカバー
- ❌ 時間を節約するためにセクションを省略しないでください
- ❌ 必須セクションをスキップしないでください

**続行する前の確認**: このタスクには必要ありません。

---

<a id="task-2-financial-modeling"></a>
## タスク 2: 財務モデリング

**目的**: 過去の財務を抽出し、予測とシナリオを備えた包括的な Excel 財務モデルを構築します。

**前提条件**: ⚠️ 開始する前に確認してください
- **必須**: 会社の財務データへのアクセス
  - 上場企業向け: SEC EDGAR の最新 10-K
  - 非上場企業の場合: 財務諸表または入手可能な推計値
  - または: ユーザーが提供した事前に抽出された過去の財務データ
- **オプション**: ビジネスコンテキストに関する企業調査 (タスク 1)

**入力検証**:
```
BEFORE STARTING - Select approach:

Option A: Extract financials (most common)
- [ ] Have access to 10-K or financial statements?
- [ ] Ready to extract 3-5 years of data?

Option B: User provided pre-extracted financials
- [ ] Historical financials file received?
- [ ] Contains income statement, cash flow, balance sheet (3-5 years)?

Optional:
- [ ] Company research (Task 1) complete for context?
```

**プロセス**:
1. 財務データへのアクセスを確認する
2. 詳細な手順をreferences/task2-financial-modeling.mdからロードします。
3. **ステップ 1**: 過去の財務データを抽出する (必要な場合)
4. **ステップ 2+**: 6 つの必須タブを使用して予測モデルを構築する
5. Excelモデルの納品

**出力**: Excel 財務モデル (.xlsx)
- 6 つの必須タブ:
  1. **売上高モデル** - 製品の内訳 (20 ～ 30 行) + 地域の内訳 (15 ～ 20 行)
  2. **損益計算書** - 40 ～ 50 項目の完全な損益計算書、過去 (3 ～ 5 年) + 予測 (5 年)
  3. **キャッシュ フロー計算書** - 営業/投資/財務活動、過去 + 予測
  4. **貸借対照表** - 資産/負債/資本、過去 + 予測
  5. **シナリオ** - ブル/ベース/ベアの比較表
  6. **DCF 入力** - タスク 3 の評価の準備

**ファイル名**: `[Company]_Financial_Model_[Date].xlsx`

**⚠️ この 1 ファイルのみを配信します。完了概要や追加の書類はありません。**

**⚠️ ショートカットを使用しないでください:**
- ✅ 財務を抽出する場合: 3 つの財務諸表からすべての明細を抽出します (3 ～ 5 年)
- ✅ 6 つの予測タブすべてを完全な詳細で完全に構築します
- ✅ 20 ～ 30 の製品行と 15 ～ 20 の地理行を含む詳細な売上高モデルを作成します
- ✅ 40～50 項目（省略不可）を含む完全な損益計算書を作成する
- ✅ すべての明細項目を含む完全なキャッシュフロー計算書と貸借対照表を含めます
- ✅ 異なるパラメータを使用して 3 つのシナリオ (強気/基本/弱気) をすべて完了します
- ❌ 簡略化/短縮版を作成しないでください
- ❌ 6 つの必須タブはいずれもスキップしないでください
- ❌ 必要な場合に過去の財務データの抽出をスキップしないでください

**タスク 3 に進む前の確認**:
- [ ] 過去の財務情報（必要な場合）の抽出または提供
- [ ] Excelファイルが作成され、開くことができます
- [ ] モデルには 6 つの必須タブ (売上高モデル、損益計算書、キャッシュ フロー、貸借対照表、シナリオ、DCF 入力) がすべてあります。
- [ ] 履歴データ (3 ～ 5 年) を組み込み
- [ ] 予測完了（今後5年間）
- [ ] シナリオ完了 (ブル/ベース/ベア)

---

<a id="task-3-valuation-analysis"></a>
## タスク 3: バリュエーション分析

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

**入力検証**:
```
BEFORE STARTING:
- [ ] Task 2 complete? (Financial model exists)
- [ ] Model file path/location known?
- [ ] Can access projected financials from model?

Required from model:
- [ ] Projected FCF (5 years)
- [ ] Revenue projections
- [ ] EBITDA projections
- [ ] Terminal year metrics
```

**プロセス**:
1. 財務モデルがアクセス可能であることを確認する
2. 詳細な手順をreferences/task3-valuation.mdからロードします。
3. バリュエーションのワークフローの実行
4. バリュエーション分析の提供

**出力**: バリュエーション分析 (4 ～ 6 ページ + Excel タブ)
- 感度テーブルを使用した DCF 解析
- 比較対象企業 (5 ～ 10 社の同業他社と統計的概要)
- 類似取引事例 (該当する場合)
- バリュエーション・フットボールフィールド
- **目標株価**: $XX.XX
- **投資判断**: BUY/HOLD/SELL（買い/保有/売り）
- **上昇余地**: XX%
- 主要なカタリスト (3-5)

**ファイル**:
- `[Company]_Valuation_Analysis_[Date].md` (分析文書)
- Excel タブが `[Company]_Financial_Model_[Date].xlsx` に追加されました (タスク 2 から)
  - 計算を含む DCF タブ
  - 感度分析タブ
  - 「比較対象企業」タブ
  - 評価概要タブ

**⚠️ 配信のみ: 1 つのマークダウン ファイル + 4 つのタブが既存の Excel に追加されます。完了概要や追加の書類はありません。**

**⚠️ ショートカットを使用しないでください:**
- ✅ 感度マトリックスを使用した完全な DCF 解析 (簡略化されていない)
- ✅ 完全なデータを使用して 5 ～ 10 社すべての比較可能な企業を分析します
- ✅ 類似企業比較表に統計的な概要を含めます (最大値/第75百分位/中央値/第25百分位/最小値)
- ✅ 複数の WACC およびターミナル成長率シナリオを含む完全な感度分析タブを作成
- ✅ 4 ～ 6 ページにわたるバリュエーション分析をすべて書きます (省略不可)
- ✅ 具体的な手法に基づき目標株価を調査し、根拠を示す
- ❌ 比較対象企業分析を省略しないでください
- ❌ 感度分析のない簡易 DCF を作成しないでください

**タスク 4 に進む前の確認**:
- [ ] 目標株価を決定
- [ ] バリュエーションには複数の手法を使用する（最低限、DCF + 類似企業比較）
- [ ] DCF 感度テーブルが完成しました
- [ ] 類似会社比較表には統計概要が含まれています

---

<a id="task-4-chart-generation"></a>
## タスク 4: チャートの生成

**目的**: レポート用に 25 ～ 35 の専門的な財務チャートを生成します。

**前提条件**: ⚠️ 開始する前に確認してください
- **必須**: タスク 1 の企業調査
  - 会社の歴史とマイルストーン（年表用）
  - 経営陣と組織構造（組織図用）
  - 製品ポートフォリオ（製品チャート用）
  - 顧客セグメンテーション（顧客グラフ用）
  - 競合状況 (競合チャート用)
  - TAM分析（市場規模チャート用）
- **必須**: タスク 2 の財務モデル (タスク 3 の評価タブを追加)
  - 製品/地域別売上高データ (タスク 2 タブ)
  - 利益率の傾向 (タスク 2 タブ)
  - シナリオ比較データ (タスク 2 タブ)
  - DCF 感度テーブル (同じ Excel ファイルのタスク 3 タブ)
  - 比較対象企業データ (同じ Excel ファイルのタスク 3 タブ)
  - 評価範囲 (同じ Excel ファイルの [タスク 3] タブ)
- **必須**: 外部市場データ
  - 過去の株価データ（Yahoo Finance、Bloombergなど）
  - 過去のバリュエーション倍率（過去の傾向チャートの場合）

**⚠️ 重要: タスク 1、2、および 3 が完了するまでは、このタスクを開始しないでください**

このタスクには、前の 3 つのタスクすべてからの出力が必要です。それらなしで開始すると、不完全なチャートが作成されます。

**タスク 1、2、または 3 のいずれかが完了していない場合**: すぐに停止し、どのタスクを最初に完了する必要があるかをユーザーに通知します。具体的な要件は次のとおりです。
- タスク 1: 企業調査ドキュメント (9 つのチャート用)
- タスク 2: 6 つのタブすべてを含む財務モデル (8 つのチャート用)
- タスク 3: モデルに追加された評価タブ (6 つのチャート用)
- 外部データアクセス (2 つのチャートの場合)

プレースホルダー グラフを作成したり、データが欠落しているためにグラフをスキップしたりしないでください。

**入力検証**:
```
BEFORE STARTING:
- [ ] Task 1 complete? (Company research exists)
- [ ] Task 2 complete? (Financial model exists)
- [ ] Task 3 complete? (Valuation analysis exists)
- [ ] Can access external market data sources?

Required from Task 1:
- [ ] Company history and milestones (for charts 05, 06)
- [ ] Management team structure (for chart 07)
- [ ] Product portfolio details (for chart 08)
- [ ] Customer segmentation data (for chart 09)
- [ ] Competitive landscape analysis (for charts 16, 17, 18)
- [ ] TAM sizing and market data (for chart 15)

Required from Task 2:
- [ ] Revenue by product (historical + projected) - for chart 03 ⭐
- [ ] Revenue by geography (historical + projected) - for chart 04 ⭐
- [ ] Income statement with margins (for charts 02, 10, 11)
- [ ] Cash flow statement (for chart 12)
- [ ] Scenario comparison data (for chart 14)

Required from Task 3:
- [ ] DCF sensitivity matrix - for chart 28 ⭐
- [ ] DCF components (for chart 29)
- [ ] Comparable companies data (for charts 30, 31)
- [ ] Valuation ranges - for chart 32 ⭐

Required from External Sources:
- [ ] Historical stock price data (for chart 01)
- [ ] Historical valuation multiples (for chart 34)
```

**プロセス**:
1. モデルと評価の出力にアクセスできることを確認する
2. 詳細な手順をreferences/task4-chart-generation.mdからロードします。
3. チャート生成ワークフローの実行
4. すべてのチャートを zip ファイルにパッケージ化する
5. zipファイルを納品する

**出力**: zip にパッケージ化された 25 ～ 35 のプロフェッショナル チャート ファイル (PNG/JPG、300 DPI)

**4 つの必須チャート** (必須) ⭐:
- chart_03: 製品別売上高 (積み上げ領域)
- chart_04: 地域別売上高 (積み上げ棒)
- chart_28: DCF 感度 (2 ウェイ ヒートマップ)
- chart_32: バリュエーション・フットボールフィールド (横棒)

**25 の必須チャート** (特定のリスト):
- 投資の概要: chart_01
- 財務実績: チャート 02、03⭐、04⭐、10、11、12、14
- 企業の基礎知識（Company 101）: チャート 05、06、07、08、09、15、16
- 競争/市場: チャート 17、18
- シナリオ分析: 図 13
- バリュエーション: チャート 28⭐、29、30、31、32⭐、33、34

**10 個のオプションのチャート** (26 ～ 35 の範囲用):
- チャート 19 ～ 27、35 (顧客獲得、ユニットエコノミクス、製品ロードマップなど)

**重要**: タスク 5 では、視覚的な密度を高めるために作成されたすべてのグラフ (25 ～ 35) が埋め込まれます (200 ～ 300 ワードごとに 1 つのグラフ)。

**ファイル名**: `chart_01_description.png`、`chart_02_description.png` など。

**納品物**: 25 ～ 35 個のチャート ファイルすべてと chart_index.txt を含む `[Company]_Charts_[Date].zip`

**⚠️ この ZIP ファイルは 1 つだけ配信します。完成概要、個別のチャートリスト、追加の文書はありません。**

**⚠️ ショートカットを使用しないでください:**
- ✅ 必要なチャートを少なくとも 25 個すべて作成します (具体的なリストは task4-chart-generation.md で提供されます)。
- ✅ 4 つの必須チャートをすべて含めます:
  - chart_03: 製品別売上高 (積み上げ領域) ⭐
  - chart_04: 地域別売上高 (積み上げ棒) ⭐
  - chart_28: DCF 感度 (ヒートマップ) ⭐
  - chart_32: バリュエーション・フットボールフィールド ⭐
- ✅ オプション: グラフを 1 ～ 10 個追加して合計 26 ～ 35 個にし、視覚的な密度を高めます。
- ✅ 300 DPI でプロ品質のチャートを生成します (低解像度のプレースホルダーではありません)
- ✅ ビジュアライゼーションごとに、適切にフォーマットされた独自のグラフを作成します
- ✅ すべてのチャートをチャートインデックス付きの zip ファイルにパッケージ化します
- ❌ 10 ～ 15 個のグラフのみを作成しないでください (最小数は 25)
- ❌ 4 つの必須チャートをスキップしないでください
- ❌ 低品質の画像やプレースホルダ画像を使用しないでください

**タスク 5 に進む前の確認**:
- [ ] 最低 25 個のチャート ファイルを作成する (必須)
- [ ] 4 つの必須チャートがすべて存在します。
  - [ ] chart_03: 製品別売上高 ⭐
  - [ ] chart_04: 地域別売上高 ⭐
  - [ ] chart_28: DCF感度 ⭐
  - [ ] chart_32: バリュエーション・フットボールフィールド ⭐
- [ ] すべてのチャートが開き、正しく表示されます
- [ ] 300 DPI (印刷品質) で保存されたチャート
- [ ] カテゴリ付きのすべてのファイルをリストするチャート インデックスが作成されました
- [ ] すべてのチャートは zip ファイルにパッケージ化されています
- [ ] ファイルの命名規則は次のとおりです: chart_##_description.png

---

<a id="task-5-report-assembly"></a>
## タスク 5: レポートの組み立て

**目的**: 包括的な最終 DOCX レポートを作成してまとめます。

**前提条件**: ⚠️ 開始する前に確認してください
- **必須**: タスク 1 の企業調査
  - コンテンツのすべての 6,000 ～ 8,000 語
  - 経営経歴
  - 競合分析
  - リスク評価
- **必須**: タスク 2 の財務モデル
  - Excelワークブック
  - すべての予測とシナリオ
- **必須**: タスク 3 のバリュエーション分析
  - 目標株価と投資判断
  - DCF、類似企業比較、類似取引事例
  - すべての評価データ
- **必須**: タスク 4 のチャート ファイル
  - 25 ～ 35 個の PNG/JPG ファイルすべてを含む ZIP ファイル
  - チャートインデックスはzipに含まれています

**⚠️ 重要: タスク 1 ～ 4 がすべて完了するまでは、このタスクを開始しないでください**

これが最後の組み立て作業です。これまでのすべての成果物がなければ完了できません。

**タスク 1、2、3、または 4 のいずれかが完了していない場合**: すぐに停止し、どのタスクを最初に完了する必要があるかをユーザーに通知します。具体的な要件は次のとおりです。
- タスク 1: 企業調査ドキュメント (6,000 ～ 8,000 語)
- タスク 2: 6 つのタブすべてを含む財務モデル
- タスク 3: 目標株価と投資判断を含むバリュエーション分析
- タスク 4: 25 ～ 35 個のチャートを含むチャート zip ファイル

プレースホルダー コンテンツを作成したり、欠落しているセクションを置き換えたり、不完全なレポートを組み立てたりしないでください。レポートでは、すべての入力が公開準備完了である必要があります。

**入力検証**:
```
BEFORE STARTING - ALL TASKS MUST BE COMPLETE:

Task 1 Verification:
- [ ] Company research document exists? (6-8K words)
- [ ] Management bios complete? (300-400 words × 3-4 execs)
- [ ] Competitive analysis complete? (5-10 competitors)
- [ ] Risk assessment complete? (8-12 risks)

Task 2 Verification:
- [ ] Financial model exists and can be opened?
- [ ] Model has projections (5 years)?
- [ ] Scenarios exist (Bull/Base/Bear)?

Task 3 Verification:
- [ ] Valuation analysis complete?
- [ ] Price target determined?
- [ ] Recommendation set? (BUY/HOLD/SELL)
- [ ] DCF and comps complete?

Task 4 Verification:
- [ ] Chart zip file exists?
- [ ] Can extract/access all 25-35 chart files from zip?
- [ ] All 4 mandatory charts present?
  - [ ] Revenue by product (stacked area)
  - [ ] Revenue by geography (stacked bar)
  - [ ] DCF sensitivity (heatmap)
  - [ ] Valuation football field
- [ ] Chart files accessible and can be opened?

IF ANY VERIFICATION FAILS: Stop and complete missing task first.
```

**プロセス**:
1. **重要**: 開始する前にすべての前提条件を確認してください
2. 詳細な手順をreferences/task5-report-assembly.mdからロードします。
3. Claude の組み込みスキルを使用してレポート アセンブリ ワークフローを実行します。
   - **DOCX スキルを使用**して Word 文書を作成および操作します
   - **XLSX スキルを使用**してタスク 2/3 から Excel データを読み取ります
   - **読み取りツールを使用**して、タスク 1 およびタスク 3 マークダウン ファイルを読み取ります
   - タスク 1 の .md ファイルを読み取る → Word 書式に変換する → グラフをインラインで挿入する
   - タスク 2 .xlsx ファイルの読み取り → テーブルの抽出 → 定量分析の書き込み
   - タスク 3 の .md ファイル + Excel タブの読み取り → バリュエーション分析のコピー/適応
   - DOCX スキルを使用して、タスク 4 の .png チャート ファイルを全体に挿入します。
   - 200 ～ 300 ワードごとにグラフが散りばめられたテキスト密度の高いレポートを作成します
4. 最終的な DOCX レポートを保存して配信する

**重要な原則**:
- Claude の DOCX および XLSX スキルを使用します (Python ライブラリではありません)。
- 実際のファイル操作を使用する (.md/.xlsx/.png ファイルの読み取り、.docx ファイルの書き込み)
- 優れた株式調査レポートは、テキストが多く、図解画像が多く含まれています (ページ使用率 60 ～ 80%、ページごとに 1 つ以上のチャート)

**🔥 重要: このタスクに全力を尽くしてください**

**これが最終成果物です。近道をしないでください。**

- ✅ **トークン予算をフルに使用** - これはこれまでのすべての作業の集大成です
- ✅ **すべてのセクションを完全に記述してください** - 要約したり省略したりしないでください
- ✅ **すべての最小要件を満たす** - 30 ページ以上、10,000 以上の単語、25 以上のグラフ、12 以上の表
- ✅ **予測の仮定を徹底的に行う** - 製品ごとの詳細を含む 2,000 ～ 3,000 ワード
- ✅ **シナリオについて包括的である** - 特定のブル/ベース/ベアパラメータを含む 1,500 ～ 2,000 語
- ✅ **タスク 4 からすべてのグラフを挿入** - いくつかだけではなく、全体の 25 ～ 35 のすべてのグラフ
- ✅ **タスク 2/3 からすべてのテーブルを作成** - すべての財務テーブルを抽出します。スキップしないでください。
- ✅ **タスク 1 の内容をそのまま使用** - Company 101 セクション全体 (6,000 ～ 8,000 語) をコピー/ペーストします。
- ✅ **プロフェッショナル品質のみ** - これは JPモルガン/ゴールドマンサックスの調査と区別できない必要があります

**決してしないでください:**
- ❌ 「このセクションには...が含まれます。」 - 実際のセクションを書きます
- ❌ 「ここにチャートが挿入されます...」 - 実際のチャートを挿入
- ❌ 「詳細については財務モデルを参照してください...」 - 詳細を抽出して含めます
- ❌ 長さのためセクションをスキップ - すべてのセクションを完了する必要があります
- ❌ トークン節約のための省略 - 必要なだけトークンを使用します

**これは公開可能な機関投資家向けリサーチです。努力、トークン、詳細を惜しみません。**

**出力**: 包括的な株式調査レポート (.docx)

**仕様**:
- **長さ**: 30 ～ 50 ページ (最低 30)
- **単語数**: 10,000 ～ 15,000 単語 (最低 10,000)
- **チャート**: 25 ～ 35 個の埋め込み画像
- **テーブル**: 12 ～ 20 の包括的なテーブル
- **形式**: クリック可能なハイパーリンクを備えたプロフェッショナル DOCX

**構造**:
- ページ 1: 投資概要 (INITIATING COVERAGE 形式)
- ページ 2 ～ 5: 投資判断の根拠とリスク
- 6～17ページ：企業の基礎知識（Company 101）
- ページ 18 ～ 30: 財務分析と予測
- ページ 31 ～ 40: バリュエーション分析
- ページ 41 ～ 50: 付録

**ファイル名**: `[Company]_Initiation_Report_[Date].docx`

**⚠️ この 1 つの DOCX ファイルのみを配信します。エグゼクティブサマリー、「ハイライト」文書、追加ファイルはありません。**

**最終確認**:
- [ ] 報告書は30～50ページです
- [ ] ワード数は10,000～15,000です
- [ ] 25～35 個のチャートが埋め込まれています
- [ ] 12～20のテーブルが含まれます
- [ ] すべての引用はクリック可能なハイパーリンクです
- [ ] 数値は財務モデルと完全に一致しています

---

<a id="input-verification-protocol"></a>
## 入力検証プロトコル

<a id="why-input-verification-matters"></a>
### 入力検証が重要な理由

各タスクには厳密な前提条件があります。必要な入力を行わずにタスクを実行すると、次のことが行われます。
- 未完了の作業で時間を無駄にする
- 低品質の出力を生成する
- やり直しが必要

**タスクを開始する前に、必ず入力を確認してください。**

<a id="verification-checklist-by-task"></a>
### タスク別の検証チェックリスト

**タスク 1**: ✅ 検証は必要ありません (独立)

**タスク 2**: 利用可能な過去の財務状況を確認する

**タスク 3**: 財務モデルが存在し、アクセス可能であることを確認する

**タスク 4**: モデル (タスク 2) と評価 (タスク 3) の両方が存在することを確認します。

**タスク 5**: 前のタスクがすべて完了していることを確認します (1、2、3、4)

<a id="what-to-do-if-verification-fails"></a>
### 検証が失敗した場合の対処方法

```
IF prerequisites are missing:
1. Stop the current task
2. Identify which prerequisite task(s) need to be completed
3. Execute the missing task(s) first
4. Return to current task once prerequisites are met
```

<a id="example-verification-dialogue"></a>
### 検証ダイアログの例

```
User: "Use initiating-coverage, Task 5 for Tesla"

Claude: "Starting Task 5: Report Assembly for Tesla

VERIFICATION - Checking prerequisites:
- Task 1 (Company research)... ❌ NOT FOUND
- Task 2 (Financial model)... ❌ NOT FOUND
- Task 3 (Valuation)... ❌ NOT FOUND
- Task 4 (Charts)... ❌ NOT FOUND

⚠️ VERIFICATION FAILED

Task 5 requires ALL previous tasks to be complete.

To proceed:
1. Complete Task 1: Company Research
2. Complete Task 2: Financial Modeling
3. Complete Task 3: Valuation Analysis
4. Complete Task 4: Chart Generation
5. Then return to Task 5

Would you like to start with Task 1 first?"
```

---

<a id="task-reference-files"></a>
## タスク参照ファイル

このスキルを無駄なく保つために、各タスクの詳細な手順は別の参照ファイルに記載されています。

- **references/task1-company-research.md** - 企業調査ワークフロー
- **references/task2-financial-modeling.md** - 財務モデリングのワークフロー
- **references/task3-valuation.md** - バリュエーション手法
  - DCF/comps の詳細については、references/valuation-methodologies.md も参照してください。
- **references/task4-chart-generation.md** - チャート生成ワークフロー
- **references/task5-report-assembly.md** - レポート作成ワークフロー
  - レポートの構造については、assets/report-template.md も参照してください。
  - 品質チェックについては、assets/quality-checklist.md も参照してください。

**参照ファイルをロードする場合**: 実行中の特定のタスクに関連付けられた参照ファイルのみをロードします。これらのファイルは非常に大きいため、複数の参照ファイルを一度にロードしないでください。詳細な手順については、タスクの開始時に適切なタスク参照ファイルを参照してください。

---

<a id="quality-standards"></a>
## 品質基準

すべての成果物は、大手投資銀行 (JPモルガン、ゴールドマン・サックス、モルガン・スタンレー) の機関投資家向けの基準を満たしています。

- **包括的**: 最小要件をすべて満たしています
- **詳細**: 一般的な記述ではなく、特定のデータと例
- **定量化**: 数値と指標でリードする
- **引用**: クリック可能なハイパーリンクのある適切なソース
- **プロフェッショナル**: 機関投資家向け品質の書式設定
- **正確**: すべての数値が検証およびクロスチェックされています

---

<a id="important-notes"></a>
## 重要な注意事項

<a id="task-independence"></a>
### タスクの独立性

- **タスク 1** はいつでも実行できます (依存関係なし)
- **タスク 2** はいつでも実行できます (履歴データのみが必要です)
- **タスク 1 と 2** は並行して実行できます
- **タスク 3** にはタスク 2 が必要です
- **タスク 4** にはタスク 2 と 3 が必要です
- **タスク 5** にはタスク 1、2、3、および 4 が必要です

<a id="session-management"></a>
### セッション管理

**同じセッション**: 出力は後続のタスクで自動的に利用可能になります

**異なるセッション**: 前のタスクの出力を明示的に参照します
```
"Use Task 3 with the model from yesterday at [path]"
"Use Task 5 with the research document at [path]"
```

<a id="file-organization"></a>
### ファイル構成

ワークフロー中に推奨される構造:
```
ProjectFolder/
├── Task1_Research/
│   └── [Company]_Research_Document.md
├── Task2_Model/
│   └── [Company]_Financial_Model.xlsx
├── Task3_Valuation/
│   └── [Company]_Valuation_Analysis.pdf
├── Task4_Charts/
│   ├── chart_01.png
│   └── ... (25-35 files)
└── Task5_Report/
    └── [Company]_Initiation_Report.docx
```

<a id="no-end-to-end-execution"></a>
### エンドツーエンドの実行なし

このスキルは、すべてのタスクを順番に自動実行することを**サポートしません**。各タスクは明示的に要求して検証する必要があります。

**理由**: これにより、次のことが保証されます。
- 各段階での品質管理
- 続行する前に出力を確認する機能
- ワークフローを一時停止/再開する柔軟性
- 前提条件の明確な検証

---

<a id="success-criteria"></a>
## 成功基準

カバレッジ開始レポートのワークフローが成功するには、次のことが必要です。
1. 5 つのタスクをすべて順番に完了します
2. すべての入力検証に合格する
3. すべての品質基準を満たしています
4. 必要な成果物をすべて作成する
5. 出力間の数値のクロスチェック
6. 最終レポートは出版準備完了です

**アウトプットの品質**: 機関投資家向け（JPモルガン/ゴールドマン/モルガン・スタンレーレベル）
**用途**: 企業の初回の包括的なカバレッジ
