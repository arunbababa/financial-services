> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/equity-research/skills/initiating-coverage/assets/report-template.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="equity-research-initiation-report-template"></a>
# 株式調査カバレッジ開始レポートのテンプレート

このテンプレートは、包括的な株式調査カバレッジ開始レポートを作成するための構造を提供します。最終レポート文書を作成する際のガイドとしてこれを使用してください。

**注意:** 実際のレポートは、DOCX スキルを使用して作成する必要があります。マークダウンコンテンツを生成しないでください。

**重要な要件:**
1. **Word ドキュメントを作成する前に、Python (matplotlib/plotly) を使用して 20 ～ 30 以上のグラフ画像を生成します**
2. **DOCX スキルを使用**: 適切なスタイル、ヘッダー/フッター、書式設定を備えた本格的なレポートを作成します
3. **実際のチャート画像を埋め込む**: 生成された PNG/JPG チャート ファイルを Word ドキュメントの適切な場所に挿入します。
4. **マークダウンなし**: マークダウン コンテンツを生成しません。 DOCX スキルを使用して .docx ファイルを作成します。

**重要なフォーマットに関するガイダンス:**
- **最大密度**: すべてのページに情報を詰め込む必要があります。全体にテキスト、グラフ、表を散りばめます。
- **孤立したセクションは禁止**: 単独のセクション ヘッダーや単独のページに単一のグラフを含めないでください。
- **20 ～ 30 以上の実際のチャート画像**: チャートを画像ファイルとして生成し、DOCX スキルを使用してテキスト セクションに埋め込みます。

---

<a id="page-1-investment-update-most-important-page"></a>
## ページ 1: 投資最新情報 (最も重要なページ)

**重要**: 1 ページ目は従来のエグゼクティブサマリーではありません。これは、専門の株式調査会社が使用する機関投資家向けの特定の書式を備えた **投資最新情報** です。

**重要な構造上の注意事項:**
- これは「投資最新情報」または「会社最新情報」ページであり、「エグゼクティブサマリー」ではありません。
- 左上隅の投資判断ボックスを使用します
- 株価パフォーマンスチャート（図1）を目立つように表示
- ■ 文字付きの詳細な箇条書きが 3 ～ 4 つ含まれています
- 各箇条書きには **太字のトピック ヘッダー**があり、その後に 3 ～ 5 文の説明が続きます
- 下部セクションには財務指標とバリュエーション指標の表があります
- すべてのチャートには、ソース行とともに図番号 (図 1、図 2 など) が必要です。

<a id="layout-structure"></a>
### レイアウト構造

**左上 - 投資判断ボックス:**
```
Rating:             [OUTPERFORM / NEUTRAL / UNDERWEIGHT / etc.]
Price ([Date]):     $[XX.XX]
Target Price:       $[XX.XX]
52-Week Range:      $[XX.XX] - $[XX.XX]
Market Cap:         $[XX.X]B
Enterprise Value:   $[XX.X]B
```

**左上 - リサーチアナリスト:**
```
[Name], [Credentials (Ph.D., CFA, M.D., etc.)]
[Email] | [Phone]

[Name 2], [Credentials]
[Email] | [Phone]
```

**右上 - 株価パフォーマンス:**
```
Figure 1 - [Company Name] Stock Price Performance
[Line chart showing stock price over 12-24 months with benchmark comparison]
Source: Company data, [Firm Name] estimates.
```

**メインコンテンツ - 灰色のヘッダーバー:**
```
[OUTPERFORM / NEUTRAL / etc.] RECOMMENDATION / COMPANY UPDATE
```

**メインコンテンツ - 詳細な箇条書き (3 ～ 4 つの箇条書き):**

箇条書きには ■ 文字を使用します。各箇条書きは次の形式に従います。
```
■ **[Bold Topic Header capturing main point].** Regular text explanation providing 3-5 sentences of detail with specific numbers, comparisons, and analysis. Lead with numbers and quantification where possible. Use "vs." not "versus". Be specific and concrete.

■ **[Second Topic Header].** [3-5 sentences of detailed explanation...]

■ **[Third Topic Header].** [3-5 sentences of detailed explanation...]

■ **[Fourth Topic Header - Optional].** [3-5 sentences of detailed explanation...]
```

**箇条書き形式の例:**
```
■ **Vertical SaaS leadership and regulatory moat should enable $50bn+ TAM by 2030.**
Deep domain expertise in healthcare IT, strong customer retention (95%+ net revenue retention),
and cross-sell capabilities have driven Acme Health's market expansion. With the healthcare IT
market expected to reach $50bn+ by 2030, Acme Health is well-positioned to capture share given
its regulatory moat and high switching costs. Management has indicated that 70% of current
revenue comes from enterprise hospital systems, suggesting strong product-market fit.
```

**下のセクション - 財務およびバリュエーション指標の表:**
```
                            [Year-3]A   [Year-2]A   [Year-1]A   [Year]E    [Year+1]E
Revenue ($M)                [X]         [X]         [X]         [X]        [X]
Revenue Growth (%)          X.X%        X.X%        X.X%        X.X%       X.X%
Gross Margin (%)           X.X%        X.X%        X.X%        X.X%       X.X%
EBITDA ($M)                [X]         [X]         [X]         [X]        [X]
EBITDA Margin (%)          X.X%        X.X%        X.X%        X.X%       X.X%
EPS ($)                    X.XX        X.XX        X.XX        X.XX       X.XX
P/E (x)                    XX.Xx       XX.Xx       XX.Xx       XX.Xx      XX.Xx
EV/Revenue (x)             X.Xx        X.Xx        X.Xx        X.Xx       X.Xx
EV/EBITDA (x)              XX.Xx       XX.Xx       XX.Xx       XX.Xx      XX.Xx

Note: Use "A" suffix for actual/historical years, "E" suffix for estimated/projected years
Source: Company data, [Firm Name] estimates.
```

---

<a id="figure-numbering-and-formatting-standards"></a>
## 図の番号付けとフォーマットの標準

**重要**: すべてのチャート、グラフ、表は、専門的な株式調査で使用される厳密な図番号の規則に従う必要があります。

<a id="figure-numbering-format"></a>
### 図の番号付け形式

**すべてのグラフ/表には次のものが必要です:**
1. **連続番号**: 図 1、図 2、図 3 など (レポート全体を通じて連続して続きます)
2. **説明的なタイトル**: 「図 X - [会社] [特定の指標] [グラフ/分析の種類]」
3. **ソース行** (常に一番下): 「出典: 会社データ、[調査会社名] の推計。」

**例:**
- 図1 - [企業]株価パフォーマンス
- 図 2 - [企業] 製品別の過去および予測の売上高構成
- 図 3 - [企業] 地域別売上高
- 図 4 - [製品名] 患者あたりの年間売上高と価格
- 図 5 - [企業] 売上総利益率の推移
- 図 6 - DCF 感度分析 ($/株)
- 図 7 - バリュエーション・フットボールフィールド

<a id="caption-format"></a>
### キャプションの形式

```
Figure X - [Descriptive Title]
[Chart/Table/Graph content]
Source: Company data, [Firm Name] estimates.
```

複数のデータ ソースを持つテーブルの場合:
```
Figure X - [Descriptive Title]
[Table content]
Source: Company filings, FactSet, [Firm Name] estimates.
```

<a id="placement-guidelines"></a>
### 配置ガイドライン

- 図にはレポート内での出現順に番号を付ける必要があります
- 最初の図 (図 1) は通常、1 ページ目の株価チャートまたは売上高成長の軌跡です。
- 各図には、ビジュアルのすぐ下にキャプションが必要です
- ソース行は、図の一番下に、より小さなフォントで斜体で表示する必要があります。

---

<a id="page-2-table-of-contents"></a>
## ページ 2: 目次

```
Executive Summary....................................................1
Investment Thesis & Risks..........................................3
Company Overview.......................................................6
  Business Description & History................................6
  Management & Ownership..........................................8
  Products & Technology...........................................9
  Customers & Go-to-Market......................................11
Growth Outlook & Drivers...........................................13
Financial Analysis & Performance.................................16
  Historical Performance........................................16
  Financial Projections.........................................19
Industry Overview & Competitive Landscape.....................21
  Market Size & TAM..............................................21
  Competitive Analysis..........................................23
  Industry Trends................................................25
Valuation Analysis..................................................27
Appendices & Disclosures...........................................31
```

---

<a id="pages-3-5-investment-thesis--risks"></a>
## ページ 3 ～ 5: 投資判断の根拠とリスク

**レイアウトの原則**: このセクションでは、テキストと 2 ～ 3 つのグラフを散在させます。各ページにはテキストとグラフィックの両方を含める必要があります。テキストのみやグラフのみのページは決して設けないでください。

<a id="investment-thesis"></a>
### 投資判断の根拠

**[投資判断を支える柱 1]: [タイトル - 例: 「大規模かつ成長する TAM」]**

[重要な統計を含む冒頭文]

[段落 1: 市場機会の定量化]
- 現在の市場規模
- 成長の原動力
- 会社のポジショニング

[段落 2: 企業がシェアを獲得する理由]
- 競争上の優位性
- 市場開拓戦略
- 初期の事業進捗/裏付けとなる実績

[段落 3: 財務上の影響]
- 売上高の獲得機会
- 利益率の特性
- タイムライン

**[埋め込みグラフ: TAM 成長グラフ]** - 市場規模の進化と企業の機会を示す積み上げ面グラフ

**[投資判断を支える柱 2]: [タイトル - 例: 「差別化された技術/製品」]**

[同様の構成 - 機会、競争上の地位、財務上の影響をカバーする 3 つの段落]

**[埋め込みチャート: 競合他社のポジショニング マトリックス]** - 主要な側面における企業と競合他社を示す 2×2 チャート

**[投資判断を支える柱 3]: [タイトル - 例: 「強力な実行と管理」]**

【同様の構造】

**[必要に応じてさらに 2 ～ 3 つの柱を追加します]**

**[埋め込みグラフ: 利益率拡大への道筋]** - 利益率改善への道筋を示すウォーターフォールまたは折れ線グラフ

<a id="investment-risks"></a>
### 投資リスク

**企業固有のリスク**

**[リスク 1]: [タイトル - 例: 「顧客集中」]**
[リスクの説明、可能であれば定量化、緩和要因。 2～3文。]

**[リスク 2]: [タイトル - 例: 「製品ロードマップの実行リスク」]**
【説明。 2～3文。]

**[リスク 3-5]: [追加の企業固有のリスク]**
[企業全体のリスクを 3 ～ 5 つ続けます]

**業界/市場のリスク**

**[リスク 1]: [タイトル - 例: 「規制上の不確実性」]**
【説明。 2～3文。]

**[リスク 2]: [タイトル - 例: 「激しい競争」]**
【説明。 2～3文。]

**[リスク 3-4]: [追加の業界/市場リスク]**
[業界全体の 2 ～ 4 のリスクを続ける]

---

<a id="pages-8-19-company-101"></a>
## ページ 8 ～ 19: 企業の基礎知識（Company 101）

<a id="company-description-1-page"></a>
### 会社概要（1ページ）

**概要**
[3 ～ 4 段落で以下を説明:
- 会社が何をしているのか（わかりやすい英語で）
- どうやってお金が儲かるのか
- 顧客は誰なのか
- 事業展開地域
- 規模を示す指標]

**ビジネスモデル図/ビジュアル**
[会社がどのように価値を生み出しているかを示すビジュアルを挿入]

<a id="company-history-2-3-pages"></a>
### 会社沿革（2～3ページ）

**初期の頃: [創業物語のタイトル]**

【設立に関する段落：誰が、いつ、なぜ、最初のビジョン】

**主要なマイルストーンのタイムライン**

```
[Year]: [Founding event, initial funding]
[Year]: [Product launch, key milestone]
[Year]: [Major partnership, funding round]
[Year]: [Geographic expansion, new product]
[Year]: [Recent achievement]
```

**[大きな転換点またはピボット]**
[該当する場合は、主要な戦略的変化について説明してください]

**[会社名] 今日: [現在の状況を示すタイトル]**
[現在の立場、最近の展開、現在の戦略を説明する段落]

<a id="management--ownership-2-pages"></a>
### 経営陣と所有構造 (2 ページ)

**主要幹部**

各幹部向け:
```
[Name] - [Title]
[Bio paragraph including:
- Current role and responsibilities
- Prior experience and track record
- Key accomplishments at company
- Education/credentials]
```

**企業構造とガバナンス**
- 法人形態 (C-Corp、PBC など)
- 取締役会の構成
- 特別なガバナンス機能
- [該当する場合はガバナンス図を含める]

**所有構造** [開示されている場合]
- 大株主及び持株比率
- 戦略的投資家
- 従業員の持株
- 内部者の持株の傾向

<a id="core-technologyproducts-2-3-pages"></a>
### コア技術・製品（2～3ページ）

**テクノロジーの概要**
【コア技術・プラットフォームの説明】

**製品ポートフォリオ**

各主要製品について:
```
[Product Name]

Description:
[What it does, key features]

Target Customers:
[Who uses it, use cases]

Pricing Model:
[How it's priced, typical contract values]

Competitive Positioning:
[How it compares to alternatives]

Traction:
[Customers, revenue, growth metrics]
```

**製品ロードマップ**
【今後開発中の製品・機能】

<a id="customers--distribution-2-3-pages"></a>
### 顧客と流通 (2～3 ページ)

**顧客ベース**
- 総顧客数: [数]
- 顧客セグメント (エンタープライズ、中堅企業、SMB)
- 地理的内訳
- お客様の事例/お客様の声

**市場開拓戦略**
- 販売チャネル（直販、パートナー等）
- 販売サイクルとCAC
- 流通における主要なパートナーシップ
- マーケティング戦略

**顧客単位の採算性**
- LTV/CAC比率
- ネットリテンション率
- チャーンレート
- 既存顧客取引の拡大率

---

<a id="pages-20-22-growth-outlook"></a>
## ページ 20 ～ 22: 成長見通し

<a id="growth-framework-overview"></a>
### 成長フレームワークの概要

**短期的な成長ドライバー (1 ～ 2 年)**
1. 【ドライバー1】
2. 【ドライバー2】
3. 【ドライバー3】

**中期的な成長ドライバー（3～5年）**
1. 【ドライバー1】
2. 【ドライバー2】

<a id="detailed-growth-driver-analysis"></a>
### 詳細な成長ドライバー分析

**[成長ドライバー 1]: [タイトル]**

*現在の状態:*
[ベースライン指標、現在のパフォーマンス]

*機会:*
【市場規模、企業の位置付け、成長性】

*タイムラインとマイルストーン:*
- 短期 (1 ～ 2 年): [予想される進歩]
- 中期（3～5年）：【期待される進捗状況】

*リスクと課題:*
【この機会の実現を妨げるもの】

**[主要な成長要因ごとに繰り返します]**

<a id="financial-projections"></a>
### 財務予測

**売上高の積み上げ**
[売上高が現在から予測までどのように増加するかを示すビジュアル]

**シナリオ分析**
[ベア/ベース/ブルケースの予測を示す表またはチャート]

---

<a id="pages-21-24-financial-analysis--performance"></a>
## ページ 21 ～ 24: 財務分析とパフォーマンス

**レイアウトの原則**: このセクションは、財務表が点在する 5 ～ 7 個のグラフで非常に密集している必要があります。各ページには複数の要素 (表 + 1 ～ 2 つのグラフ) が必要です。

<a id="historical-financial-analysis"></a>
### 過去の財務分析

**損益計算書のハイライト (3～5 年の歴史)**
```
                    2021    2022    2023    2024    LTM
Revenue ($M)        [X]     [X]     [X]     [X]     [X]
  Growth %          -       X%      X%      X%      X%
Gross Profit ($M)   [X]     [X]     [X]     [X]     [X]
  Margin %          X%      X%      X%      X%      X%
EBITDA ($M)         [X]     [X]     [X]     [X]     [X]
  Margin %          X%      X%      X%      X%      X%
Net Income ($M)     [X]     [X]     [X]     [X]     [X]
  Margin %          X%      X%      X%      X%      X%
FCF ($M)            [X]     [X]     [X]     [X]     [X]
```

**[チャート 1: 売上高成長の軌跡]**
過去の売上高と主要なマイルストーンの注釈を示す折れ線グラフ。グラフに成長率ラベルを含めます。

**[図 2: 製品/セグメント別売上高]** ⭐ クリティカル
製品ラインまたは事業セグメントごとの売上高構成を時系列で示す積み上げ面グラフ。これは、ミックスシフトと、どの製品が成長を牽引しているかを示します。
```
Example segments:
- Product A Revenue
- Product B Revenue
- Product C Revenue
- Services Revenue
```

**[図 3: 地域別売上高]** ⭐ クリティカル
経時的な地域別売上高の内訳を示す積み上げ棒グラフ。
```
Example regions:
- North America
- Europe
- Asia-Pacific
- Rest of World
```

<a id="financial-performance-analysis"></a>
### 財務業績分析

**[チャート 4: 売上総利益率の推移]**
利益率の変動要因（規模、価格設定、構成など）を説明する注釈付きの折れ線グラフ

**[チャート 5: 営業利益率の推移]**
売上総利益率から営業利益率までの経路を示すウォーターフォール グラフ、または EBITDA 利益率の傾向を示す折れ線グラフ

**[チャート 6: フリー キャッシュ フローの生成]**
棒 + 折れ線コンボ チャート: 棒 = FCF、折れ線 = FCF利益率 %

**[図 7: 主要な事業指標ダッシュボード]**
3 ～ 4 つの主要な指標を示すマルチパネル グラフ:
- 顧客数またはユーザーの増加
- ARPU (ユーザーあたりの平均売上高) または ACV (年間契約額)
- 顧客コホート維持率または売上高維持率（NRR）
- LTV/CAC、マジックナンバー、またはその他のユニットエコノミクス指標

<a id="forward-projections-3-5-years"></a>
### 将来予測（3～5年）

**予測される財務モデル**
```
                    2025E   2026E   2027E   2028E   2029E
Revenue ($M)        [X]     [X]     [X]     [X]     [X]
  Growth %          X%      X%      X%      X%      X%
Gross Profit ($M)   [X]     [X]     [X]     [X]     [X]
  Margin %          X%      X%      X%      X%      X%
EBITDA ($M)         [X]     [X]     [X]     [X]     [X]
  Margin %          X%      X%      X%      X%      X%
FCF ($M)            [X]     [X]     [X]     [X]     [X]
  FCF Margin %      X%      X%      X%      X%      X%
```

**重要な前提条件**
- 売上高成長の推進要因と前提条件
- 利益率推移の前提
- 売上高に対する設備投資の割合（%）
- 運転資本の仮定

**チャート:**
- 成長の原動力を示す売上高ブリッジ
- 黒字化/利益率拡大への道筋を示す利益率のウォーターフォール
- フリーキャッシュフローの軌跡

<a id="fundraising--valuation-for-private-companies"></a>
### 資金調達とバリュエーション【非上場企業向け】

**資金調達の履歴**
```
Round    Date      Amount    Valuation    Lead Investor(s)
Seed     [Date]    $XM       $XM          [Investor]
Series A [Date]    $XM       $XM          [Investor]
Series B [Date]    $XM       $XM          [Investor]
[etc.]
```

**バリュエーション推移グラフ**
【時間の経過に伴うバリュエーションの推移を示すビジュアル】

**現在のバリュエーション指標**
- 最新の評価額: $XXbn（XX×10億ドル）
- 暗黙のバリュエーション倍率: XX.Xx
- 上場同業他社との比較

---

<a id="pages-26-31-industry-overview"></a>
## ページ 26 ～ 31: 業界の概要

<a id="industry-definition--market-size"></a>
### 業界の定義と市場規模

**業界の概要**
[2-3 段落:
- 業界の定義と範囲
- 現在の市場規模
- 過去の成長率
- 主要な傾向と推進力]

**市場規模チャート**
[過去から予測までの市場の成長を示すビジュアル]

<a id="competitive-landscape"></a>
### 競争環境

**競合上の位置付けマトリックス**
[主要な側面における企業と競合他社を示す 2x2 グラフ]

**競合他社比較表**
```
Metric              [Company]  Comp A   Comp B   Comp C   Comp D
Revenue ($B)        [X]        [X]      [X]      [X]      [X]
Growth %            X%         X%       X%       X%       X%
Market Share        X%         X%       X%       X%       X%
Gross Margin        X%         X%       X%       X%       X%
Key Differentiator  [X]        [X]      [X]      [X]      [X]
```

**競合分析の説明**
[2 ～ 3 段落の分析:
- 競争上の強みと弱み
- 市場でのポジショニング
- 市場シェアの獲得/喪失
- 競争優位の堀（参入障壁）]

<a id="total-addressable-market"></a>
### 獲得可能な最大市場規模（TAM）

**TAM の計算**
```
Current TAM (2025):              $XXbn
Projected TAM (2030):            $XXbn
CAGR:                            XX%

Segmentation:
- [Segment A]:                   $XXbn
- [Segment B]:                   $XXbn
- [Segment C]:                   $XXbn
```

**TAM 成長チャート**
[TAM の長期的な拡大をセグメントごとに示すビジュアル]

**企業の市場機会**
```
Total TAM (2030):                $XXbn
Serviceable TAM:                 $XXbn
Company's Realistic Share:       XX%
Implied Revenue Potential:       $XXbn
```

<a id="industry-dynamics"></a>
### 業界の動向

**ポーターのファイブフォース分析**
- 新規参入者の脅威：[高/中/低] - [説明]
- サプライヤーの交渉力：[高/中/低] - [説明]
- 買い手の交渉力：[高/中/低] - [説明]
- 代替品の脅威：[高/中/低] - [説明]
- 業界ライバル関係：[高/中/低] - [説明]

**主要な業界動向**
1. 【トレンド1】：【説明と影響】
2. 【トレンド2】：【説明と影響】
3. 【トレンド3】：【説明と影響】

---

<a id="pages-32-34-valuation-analysis"></a>
## ページ 32 ～ 34: バリュエーション分析

<a id="valuation-methodology-summary"></a>
### バリュエーション手法の概要

```
Valuation Method            Weight    Implied Value    Weighted Value
DCF Analysis                50%       $XX - $YY        $ZZ
Trading Comparables         30%       $XX - $YY        $ZZ
Precedent Transactions      20%       $XX - $YY        $ZZ
                           ────       ─────────────    ─────────
Weighted Average Price Target         $AA - $BB        $CC
```

<a id="dcf-analysis"></a>
### DCF解析

**重要な前提条件**
```
Revenue Growth (2025-2029):         XX% CAGR
Terminal Growth Rate:               X.X%
WACC:                               X.X%
Terminal Year EBITDA Margin:        XX%
```

**図 X - DCF 感度分析 ($/株)**

重要な形式: DCF 感度は、色分けされた 2 方向ヒート マップ テーブルとして表示される必要があります。

```
                        Terminal Growth Rate
WACC        2.0%      2.5%      3.0%      3.5%      4.0%
8.0%        $52       $55       $58       $62       $66
9.0%        $48       $51       $54       $57       $61
10.0%       $45       $47       $50       $53       $56
11.0%       $42       $44       $47       $49       $52
12.0%       $39       $41       $44       $46       $49

Color coding: Green (higher values) → Yellow (mid) → Red (lower values)
Source: [Firm Name] estimates.
```

**シナリオ分析**
```
Scenario      Enterprise Value    Equity Value    Price/Share
Bear Case     $XXbn              $XXbn           $XX
Base Case     $XXbn              $XXbn           $XX
Bull Case     $XXbn              $XXbn           $XX
```

<a id="trading-comparables"></a>
### 類似企業比較（Trading Comparables）

**図 X - 比較対象企業の分析**

クリティカルフォーマット: 比較表は、統計概要を含む 2 つの部分からなる構造でなければなりません。

**パート 1: 個別の企業データ**
```
Company         Ticker   Market   EV/Rev   EV/Rev   EV/EBITDA  EV/EBITDA  Rev     EBITDA
                         Cap($B)  2024E    2025E    2024E      2025E      Growth  Margin
Peer A          PERA     XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
Peer B          PERB     XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
Peer C          PERC     XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
Peer D          PERD     XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
[Company]       COMP     XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
```

**パート 2: 統計の概要**
```
Max                      XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
75th Percentile          XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
Median                   XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
25th Percentile          XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%
Min                      XX.X     X.Xx     X.Xx     XX.X       XX.X       XX%     XX%

Source: FactSet, company filings, [Firm Name] estimates.
```

**算出されるバリュエーション**
[同業他社の倍率を企業指標に適用した計算]

<a id="precedent-transactions-if-applicable"></a>
### 類似取引事例 [該当する場合]

**図 X - 類似取引事例分析**
```
Date        Target       Acquirer      Deal      EV/Rev   EV/EBITDA  Premium
                                      Value($B)
[MM/YYYY]   [Company A]  [Buyer A]    X.X       X.Xx     XX.X       XX%
[MM/YYYY]   [Company B]  [Buyer B]    X.X       X.Xx     XX.X       XX%
[MM/YYYY]   [Company C]  [Buyer C]    X.X       X.Xx     XX.X       XX%
────────────────────────────────────────────────────────────────────
Median                                          X.Xx     XX.X       XX%

Source: Capital IQ, company filings, [Firm Name] estimates.
```

**コントロールプレミアム分析**
【業界の一般的な支配権プレミアムについての考察】

<a id="valuation-summary"></a>
### 評価概要

**図 X - バリュエーション・フットボールフィールド**

クリティカルフォーマット: フットボールフィールドは、すべてのバリュエーション手法を示す水平棒グラフである必要があります。

```
Valuation Method                Low End ────── Range ────── High End

DCF Analysis                    $42 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ $58

Trading Comps (NTM)             $45 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ $55

Precedent Trans.                $48 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ $60
                                                      ↑
                                            Current Price: $50
────────────────────────────────────────────────────────────────
Valuation Range:                $42                        $60

Color coding: Each method should have distinct color bar
Add vertical line showing current stock price
Source: [Firm Name] estimates.
```

**目標株価と投資判断**
```
Current Price:              $XX.XX ([Date])
Price Target:               $YY.YY
Upside/Downside:            ZZ%

Recommendation:             BUY / HOLD / SELL
Time Horizon:               12 months

Catalysts:
• [Near-term catalyst with timeframe]
• [Medium-term catalyst with timeframe]
• [Long-term catalyst with timeframe]
```

---

<a id="pages-35-appendices--disclosures"></a>
## 35 ページ以上: 付録と開示事項

<a id="appendix-a-detailed-financial-model"></a>
### 付録 A: 詳細な財務モデル
【Excelモデル参照】

<a id="appendix-b-management-bios"></a>
### 付録 B: 経営陣の経歴
[本文に含まれていない場合は詳細な略歴]

<a id="appendix-c-product-detail"></a>
### 付録 C: 製品の詳細
[必要に応じて追加の製品情報]

<a id="appendix-d-industry-data-sources"></a>
### 付録 D: 業界のデータソース
【業界分析に使用したソースのリスト】

<a id="required-disclosures"></a>
### 必要な開示
- アナリスト認定
- 重要な開示
- 企業固有の開示
- 法人に関する開示
- その他の規制上の開示

---

<a id="graphics--charts-to-include"></a>
## 含めるグラフィックとチャート

**ターゲット: レポート全体で 20 ～ 30 以上のグラフ**

**重要な原則**: グラフは、別のページにグループ化するのではなく、テキスト セクション内に埋め込む必要があります。すべてのページ (目次を除く) には、少なくとも 1 つのグラフまたは表が必要です。

<a id="page-1---executive-summary-3-charts"></a>
### ページ 1 - エグゼクティブ サマリー (3 つのグラフ)
1. 売上高/ARR 成長軌跡 (折れ線グラフ、過去 + 予測)
2. 主要指標ダッシュボード (マルチパネル グラフ)
3. 市場でのポジショニングまたは利益率の推移

<a id="pages-3-5---investment-thesis--risks-3-charts"></a>
### ページ 3 ～ 5 - 投資判断の根拠とリスク (3 つのグラフ)
4. TAM の成長と機会 (積み上げ面グラフ)
5. 競合ポジショニングマトリックス (2×2 バブルあり)
6. 利益率拡大への道筋（ウォーターフォールまたはライン）

<a id="pages-6-17---company-101-6-8-charts"></a>
### ページ 6 ～ 17 - 企業の基礎知識（Company 101） (6 ～ 8 のグラフ)
7. ビジネスモデル図（フローチャート）
8. 会社のタイムライン（横方向のタイムライン）
9. 資金調達履歴（評価線付き棒グラフ）
10. 組織図
11. 製品ポートフォリオマトリックス
12. 顧客のセグメンテーション (円またはツリー マップ)
13. 売上高の地域別内訳
14. 顧客コホートの維持

<a id="pages-18-20---growth-outlook-4-charts"></a>
### ページ 18 ～ 20 - 成長見通し (4 つのグラフ)
15. ドライバーを示す売上高ブリッジ (ウォーターフォール)
16. 市場シェアの推移（折れ線グラフ）
17. 製品ロードマップ (タイムライン)
18. 地理的拡大 (タイムライン付きの地図)

<a id="pages-21-24---financials-7-charts--critical-section"></a>
### ページ 21 ～ 24 - 財務 (7 つのチャート) ⭐ クリティカルセクション
19. 売上高成長の軌跡 (注釈付きの線)
20. **製品/セグメント別売上高** (積み上げ領域) ⭐必須
21. **地域別売上高** (積み上げバー) ⭐必須
22. 売上総利益率の推移（折れ線グラフ）
23. 営業利益率の推移（ウォーターフォールまたはライン）
24. フリー キャッシュ フローの軌跡 (バー + ラインのコンボ)
25. 主要な事業指標ダッシュボード (マルチパネル)
26. シナリオの比較 (グループ化されたバー: ベア/ベース/ブル)

<a id="pages-25-30---industry-overview-6-charts"></a>
### ページ 25 ～ 30 - 業界の概要 (6 つのグラフ)
27. 市場規模の推移（CAGRを含む面グラフ）
28. 競争環境マップ（2×2）
29. 市場シェアの円グラフ
30. 時間の経過に伴う市場シェアの推移（折れ線グラフ）
31. TAM セグメンテーション
32. 業界動向グラフ

<a id="pages-31-34---valuation-5-charts"></a>
### ページ 31 ～ 34 - バリュエーション (5 つのチャート)
33. DCF感度解析（ヒートマップ）
34. DCFウォーターフォール（キャッシュフローのPV→株式価値）
35. 類似企業比較の散布図（成長率対評価倍率）
36. ピアバリュエーション倍率（グループ化されたバー）
37. バリュエーション・フットボールフィールド（範囲表）
38. 目標株価シナリオ (上昇余地/下落余地のあるバー)

**チャートスタイルのガイドライン:**
- **一貫した配色** (ブランドカラーを 3 ～ 5 つ選択)
- **プロフェッショナル フォント** (Arial、Calibri など)
- すべてのグラフの **明確なラベルと凡例**
- **各図の下部にある出典引用**
- **高い情報密度** - チャートスペースを効率的に使用します
- **視覚的に興味深いグラフ タイプの組み合わせ**
- 重要な洞察を強調する **注釈**
- **テキストに埋め込まれています** - スタンドアロン ページではありません
- **表内のスパークライン** (該当する場合)

---

<a id="notes-on-using-this-template"></a>
## このテンプレートの使用上の注意

1. **1 ページ目は重要です:** 1 ページ目のエグゼクティブ サマリーには、主要な情報 (概要、財務スナップショット、3 つのグラフ、評価概要、投資判断の根拠、リスク) がすべて含まれている必要があります。これは最も重要なページです。

2. **最大密度:** 専門的な株式調査は非常に情報密度が高いです。すべてのページには、散りばめられたテキスト、グラフ、表が詰め込まれている必要があります。余白を最小限に抑え、ページ使用率が 60 ～ 80% になるようにします。

3. **孤立したセクションはありません:** セクション ヘッダーだけを使用したり、単独のページに単一のグラフ/表を使用したりしないでください。常に要素を組み合わせてください。例: 「財務スナップショット」を6ページ目に単独で配置しないでください。周囲のコンテンツと統合してください。

4. **20 ～ 30 以上のグラフ:** 以下に特に重点を置いた広範なグラフィックを全体に含めます。
   - **製品/セグメント別売上高** (積み上げ面グラフ)
   - **地域別売上高** (積み上げ棒グラフ)
   - **財務パフォーマンスの傾向** (複数のグラフ)
   - グラフは個別にグループ化するのではなく、テキスト内に埋め込む必要があります。

5. **DOC スキルを使用する:** このアウトラインは、適切な書式設定、スタイル、ヘッダー/フッター、ページ番号を備えた DOC スキルを使用して、プロフェッショナルな Word 文書に変換する必要があります。

6. **インタースプライス コンテンツ:** テキストの段落には、インラインで埋め込まれたグラフが必要です。各ページには 2 ～ 4 つの異なる要素 (表、グラフ、テキスト ブロック) が必要です。

7. **一貫した書式設定:** ヘッダー、本文、表、グラフ全体に一貫したスタイルを使用します。カラースキームを選択し、それを忠実に守ります。

8. **参考文献:** すべてのデータ ポイントの引用と出典を含めます

9. **校正:** 正確さ、特に財務データと計算を常に校正します。

10. **エグゼクティブサマリーの最後:** このセクションは 1 ページ目に表示されますが、完全な分析が完了した後に最後に記述してください。

11. **バランス:** ポジティブな側面とネガティブな側面の両方を客観的に提示する

12. **具体的な記述 > 一般論:** 一般的なステートメントではなく、特定のデータと例を使用します
