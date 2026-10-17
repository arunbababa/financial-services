---
name: earnings-preview-single
description: Generate a concise 4-5 page equity research earnings preview for a single company. Analyzes the most recent earnings transcript, competitor landscape, valuation, and recent news to produce a professional HTML report.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/partner-built/spglobal/skills/earnings-preview-beta/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：単一企業について、4～5 ページの簡潔な株式リサーチ用の決算プレビューを作成します。直近の決算説明会の書き起こし、競合環境、バリュエーション、最近のニュースを分析し、プロフェッショナルな HTML レポートにまとめます。

<a id="single-company-earnings-preview"></a>
# 単一企業の決算プレビュー

単一企業について、簡潔で専門的な株式調査の決算プレビューを生成します。成果物は印刷時4〜5ページを目安とする自己完結型HTMLファイルです。数値とデータを密に配置し、説明は要点へ直接進む簡潔な文章にします。

**データ ソース (例外なし):** 許可されるデータ ソースは、**Kensho Grounding MCP** (`search`) および **S&P Global MCP** (`kfinance`) のみです。他のツール、データ ソース、またはいかなる種類の Web アクセスも絶対に禁止します。具体的には:
- Kensho が遅い場合、結果が返されない場合、または一時的に利用できない場合でも、`WebSearch`、`WebFetch`、`web_search`、`brave_search`、`google_search`、またはその他の汎用 Web/インターネット検索ツールは使用しないでください。
- ブラウザ、URL フェッチ、または Web スクレイピング ツールは使用しないでください。
- Kensho Grounding がクエリに対して結果を返さない場合は、クエリを言い換えるか、レポートに「データが利用できません」と記載してください。 **代替手段として Web 検索に決して頼らないでください。**
- レポート内のすべての情報は、`kfinance` MCP 関数呼び出しまたは Kensho `search` 呼び出しのいずれかに追跡できる必要があります。これら 2 つのいずれかに情報源を提供できない場合は、レポートに記載してはなりません。

**重要なルール:** レポートの一部を作成する前に、すべての調査とデータ収集 (フェーズ 1 ～ 5) を完了する必要があります。

**中間ファイル ルール:** MCP ツール呼び出しからのすべての生データは、**各ツール呼び出しが返された直後**、つまり次の呼び出しに進む前に、`/tmp/earnings-preview/` 内のファイルに書き込まれる必要があります。これにより、コンテキスト ウィンドウの圧縮からデータが保護されます。データをメモリ内にのみ保持しないでください。フェーズ 1 の開始時に、`mkdir -p /tmp/earnings-preview` を実行してディレクトリを作成します。 **HTML レポート (フェーズ 7) を生成する前に、`cat` コマンドを使用してすべての中間ファイルをコンテキストに読み戻す必要があります。ファイルは、以前の会話の記憶ではなく、レポート内のすべての数値、引用、ソース URL に関する唯一の信頼できる情報源です。ファイルの読み取りをスキップすると、レポートにエラーが含まれます。**

**会計四半期の規則：** 暦上の発表日から会計四半期を推測してはいけません。企業の会計年度は一様ではありません。例えばWalmartの年度末は1月31日なので、2026年2月の発表はQ4 2025やQ1 2026ではなく、Q4 FY2026を対象とします。`get_next_earnings_from_identifiers`または`get_earnings_from_identifiers`が返す決算説明会名に記載された会計四半期・年度を厳密に使ってください。例えば「Walmart Q4 FY2026 Earnings Call」の四半期はQ4 FY2026です。タイトル、見出し、表、すべての参照にこの表記をそのまま使います。説明会名が曖昧なら`get_financial_line_item_from_identifiers`の期間ラベルと突合してください。

**長さのルール:** レポートは簡潔でなければなりません。印刷時の目標は 4 ～ 5 ページです。複数の段落にまたがる長い物語を書かないでください。タイトでパンチのある箇条書きを使用します。すべての文がその場所を獲得しなければなりません。もっと少ない言葉で言えるならそうしてください。

**逐語引用の規則：** `<blockquote>`で経営陣を引用する場合、つなぎ言葉や不完全文も含め、書き起こしから一語一句**正確に**コピーします。言い換え、並べ替え、別箇所の文の結合、読みやすくする改変は禁止です。完全に一致する表現を見つけられないなら直接引用にせず、blockquoteを使わない自分の説明文として要約します（例：「経営陣はデータセンター需要が依然大きいと述べた」）。すべてのblockquoteは原文と照合できる逐語的な抜粋でなければなりません。

**計算の整合性：** 年間見通しから逆算する四半期値、LTM P/E、前年比成長率、セグメントの前年比変化等、複数段階の計算は各手順を明記し、次の計算へ進む前に中間結果を検証します。A + B + C = Xと示すなら、後続式でXを使う前に算術的に正しいか確認します。付録の合計が記載した内訳と一致しなければ、そのレポートは誤りです。迷ったら既存の中間結果を再利用せず、生データから再計算します。

**比率命名規則:** すべての評価比率は、**LTM** (過去 12 か月) または **NTM** (次の 12 か月) として明示的にラベル付けする必要があります。 「トレーリング」または「フォワード」は決して使用しないでください。常に LTM または NTM を使用してください。 LTM 比率は、報告された直近 4 四半期の合計を使用します。 NTM 比率は、単一の年間数値ではなく、`get_consensus_estimates_from_identifiers` からの **次の 4 四半期のコンセンサス平均 EPS 推定値の合計**を使用します。 LTM と NTM の両方の P/E を計算し、競合他社比較表に表示する必要があります。

**ハイパーリンクのルール（厳守）：** レポート内の主張は、数値か定性情報かを問わず、付録の対応項目を指す`<a href="#ref-N" class="data-ref">`ハイパーリンクで必ず囲みます。**任意ではありません。レポートのすべての数値をクリック可能にします。** 対象は、売上高、EPS、利益率、成長率、時価総額、PER、株価リターン、目標株価、セグメント売上高、その他あらゆる財務指標です。決算説明会の書き起こしやKensho検索から得た定性的な主張も含み、事実として述べるなら出典へリンクします。異なる主張ごとに連番の参照ID（`ref-1`、`ref-2`等）を割り当てます。リンクは控えめに、ネイビー、下線なしとし、ホバー時に点線の下線を表示します。**レポート本文には、`<a>`タグで囲まない数値を書いてはいけません。** 例：`<a href="#ref-1" class="data-ref">$152.3B</a>`と書き、`$152.3B`をプレーンテキストで書かないでください。

---

<a id="phase-1-company-profile--setup"></a>
## フェーズ1：企業概要と準備

1. `$ARGUMENTS` から単一の会社ティッカーを解析します (空白を削除)。
2. `mkdir -p /tmp/earnings-preview` を実行して作業ディレクトリを作成します。
3. `get_latest()` を呼び出して、現在のレポート期間のコンテキストを確立します。
4. `get_info_from_identifiers`を呼び出し、時価総額と業種を記録します。
5. `get_company_summary_from_identifiers`を呼び出し、事業の説明を記録します。
6. `get_next_earnings_from_identifiers`を呼び出し、次の決算発表日と会計四半期名を記録します。

**すぐに書き込みます** `/tmp/earnings-preview/company-info.txt`:
```
TICKER: [ticker]
COMPANY: [full name]
INDUSTRY: [industry]
MARKET_CAP: [value] (as of [date])
NEXT_EARNINGS_DATE: [date]
NEXT_EARNINGS_QUARTER: [Q# FY#### exactly as returned by API]
BUSINESS_DESCRIPTION: [2-3 sentence summary]
```

---

<a id="phase-2-earnings-transcript-analysis-mandatory--complete-before-writing"></a>
## フェーズ2：決算説明会の書き起こし分析（必須・執筆前に完了）

1. `get_latest_earnings_from_identifiers`を呼び出し、直近で終了した決算説明会の`key_dev_id`を取得します。
2. その書き起こしを取得するため、`get_transcript_from_key_dev_id`を呼び出します。
3. **すぐに** `/tmp/earnings-preview/transcript-extracts.txt` と次のセクションを記述します。コンテキスト内のトランスクリプトがまだ残っている間に、このファイルを書き込みます。待たずに次のようにします。

```
TRANSCRIPT_SOURCE: [Call Name, e.g., "Q3 2025 Earnings Call"]
KEY_DEV_ID: [key_dev_id]
CALL_DATE: [date]
FISCAL_QUARTER: [Q# FY####]

=== VERBATIM QUOTES (copy-paste exactly — do NOT paraphrase) ===
QUOTE_1: "[exact text from transcript]"
SPEAKER_1: [Name], [Title]
CONTEXT_1: [1 sentence on where this appeared — prepared remarks or Q&A]

QUOTE_2: "[exact text from transcript]"
SPEAKER_2: [Name], [Title]
CONTEXT_2: [context]

QUOTE_3: "[exact text from transcript]"
SPEAKER_3: [Name], [Title]
CONTEXT_3: [context]

QUOTE_4: "[exact text from transcript]"
SPEAKER_4: [Name], [Title]
CONTEXT_4: [context]

=== GUIDANCE (quantitative only) ===
- [metric]: [range or point estimate as stated by management]
- [metric]: [range or point estimate]

=== KEY DRIVERS ===
- [driver 1 with supporting data point]
- [driver 2 with supporting data point]
- [driver 3 with supporting data point]

=== HEADWINDS & RISKS ===
- [risk 1 with quantification if available]
- [risk 2]

=== ANALYST Q&A THEMES ===
- [theme 1: what analysts pushed on]
- [theme 2]
- [theme 3]

=== SYNTHESIS: THEMES TO WATCH NEXT QUARTER ===
- [theme 1]
- [theme 2]
- [theme 3]
```

---

<a id="phase-3-competitor-analysis"></a>
## フェーズ 3: 競合他社の分析

1. `get_competitors_from_identifiers` を `competitor_source="all"` で呼び出します。
2. **関連性が最も高い上場競合企業を5〜7社**選びます。
3. 会社と選択したすべての競合他社について、以下を収集します。
   - `get_prices_from_identifiers` と `periodicity="day"`、過去 12 か月
   - `get_financial_line_item_from_identifiers`、`diluted_eps`、`period_type="quarterly"`、`num_periods=8`
   - `get_capitalization_from_identifiers` と `capitalization="market_cap"` (最新)
   - `get_consensus_estimates_from_identifiers` と `period_type="quarterly"`、`num_periods_forward=4` — これは、NTM EPS を計算するために合計される、次の 4 四半期のコンセンサス平均 EPS 推定値を返します。

**各ツール呼び出しが戻ったら、すぐに生データを適切な中間ファイルに追加します。**

**書き込み** `/tmp/earnings-preview/prices.csv` — (ティッカー、日付、終値) ごとに 1 行。正確な MCP 関数呼び出しを含む `source` 列を含めます。最初に対象企業の価格を記述し、次に取得時に各競合他社の価格を記述します。
```
ticker,date,close,source
D,2025-02-19,55.67,get_prices_from_identifiers(identifier='D',periodicity='day')
D,2025-02-20,55.82,get_prices_from_identifiers(identifier='D',periodicity='day')
...
DUK,2025-02-19,111.79,get_prices_from_identifiers(identifier='DUK',periodicity='day')
...
```
注: `source` 値は、1 回の呼び出しで得られるすべての行で同じです。常に使用できるように、すべての行にこの値を書き込みます。

**書き込み** `/tmp/earnings-preview/peer-eps.csv` — (ティッカー、ピリオド、eps) ごとに 1 行。各 `diluted_eps` 呼び出しの直後に次のように書き込みます。
```
ticker,period,diluted_eps,source
D,Q4 2024,1.09,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
D,Q1 2025,-0.11,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
...
DUK,Q4 2024,1.52,get_financial_line_item_from_identifiers(identifier='DUK',line_item='diluted_eps',period_type='quarterly')
...
```

**書き込み** `/tmp/earnings-preview/peer-market-caps.csv` — ティッカーごとに 1 行。各 `market_cap` 呼び出しの直後に次のように書き込みます。
```
ticker,market_cap,retrieval_date,source
D,55900000000,2026-02-19,get_capitalization_from_identifiers(identifier='D',capitalization='market_cap')
DUK,98300000000,2026-02-19,get_capitalization_from_identifiers(identifier='DUK',capitalization='market_cap')
...
```

**書き込み** `/tmp/earnings-preview/consensus-eps.csv` — (ティッカー、ピリオド、コンセンサス平均 EPS) ごとに 1 行。各 `get_consensus_estimates_from_identifiers` 呼び出しの直後に次のように書き込みます。
```
ticker,period,consensus_mean_eps,num_estimates,source
D,Q4 2025,0.88,12,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q1 2026,0.72,10,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q2 2026,0.91,9,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
D,Q3 2026,1.05,8,get_consensus_estimates_from_identifiers(identifier='D',period_type='quarterly',num_periods_forward=4)
DUK,Q4 2025,1.48,14,get_consensus_estimates_from_identifiers(identifier='DUK',period_type='quarterly',num_periods_forward=4)
...
```

4. **PER やリターンはまだ計算しないでください。** 生データは現在ディスク上にあります。計算はフェーズ 6 (検証) で行われ、これらのファイルから読み取ります。

**日付の整合性ルール（株価リターン）：** 年初来%、1年%、30日%、90日%等を比較する際は、すべての銘柄で**開始日と終了日を完全に揃えます**。価格データをすべて`prices.csv`に保存したら、全銘柄のデータに共通する最初の取引日を探し、共通の基準日にします。対象企業は2月19日、同業他社は2月28日など、銘柄ごとに基準日を変えてはいけません。ある銘柄のデータが遅い日から始まるなら、全銘柄で最初に重なる日をすべての計算に使用します。各リターン計算について、共通の基準日を付録に記載します。

**P/Eの実績鮮度の規則（LTM P/E）：** 各企業の`peer-eps.csv`から、その企業の**公表済みの直近4四半期**を使います。全社に共通の暦期間を固定してはいけません。対象企業がQ3 2025までしか発表していなくても、同業他社がQ4 2025を発表済みなら、その企業のLTM EPSにはQ4 2025を含めます。各企業の最新公表期を確認し、直近4期を使い、各P/Eの計算に使った四半期を付録に記載します。

**時価総額の日付スタンプ:** 時価総額を報告する場合は、`peer-market-caps.csv` から `retrieval_date` を使用します。レポートの日付と異なる場合は、付録にその旨を記載してください。

---

<a id="phase-4-news-estimates--sector-intelligence-via-kensho-grounding"></a>
## フェーズ4：ニュース、予想、業種情報（Kensho Grounding経由）

以下の **各** カテゴリに対して `search` クエリを実行します。スキップしないでください。

**重要 — ソース URL のキャプチャ:** Kensho `search` のすべての結果には、基礎となる記事、レポート、またはデータ ページの **ソース URL** が含まれます。各結果の横に URL を記録する必要があります。

**各検索呼び出し後、次の形式を使用して結果をすぐに** `/tmp/earnings-preview/kensho-findings.txt` に追加します。すべての検索が完了するまで待たずに、各検索の後に次のように記述します。

```
=== SEARCH: "[query used]" ===
DATE_RUN: [today's date]
CATEGORY: [estimates|analyst_ratings|risks|news|sector]

FINDING_1: [key finding or excerpt]
URL_1: [source URL from search result]
SOURCE_1: [publication name, date if available]

FINDING_2: [key finding or excerpt]
URL_2: [source URL]
SOURCE_2: [publication name, date]

[...continue for all relevant results from this search...]
```

**収益予想とアナリストのセンチメント:**
1. `search`、「[TICKER] 次期四半期の収益予測コンセンサス EPS 収益」
   - 記録: 過去 90 日間のコンセンサス EPS、コンセンサス収益、予想修正方向。
   - **直ちに kensho-findings.txt に追加してください。**
2. `search`、「[TICKER] アナリスト格付け、目標株価の格上げ、格下げ」
   - 直近の格上げ・格下げ、目標株価レンジ、強気・弱気の投資仮説の要点を記録します。
   - **直ちに kensho-findings.txt に追加してください。**
3. `search`で「[TICKER] risks bear case concerns investors」（リスク、弱気シナリオ、投資家の懸念）を検索します。
   - 主要な論点、弱気派の主張、次の決算発表の結果を左右する要因を記録します。
   - **直ちに kensho-findings.txt に追加してください。**

**最近のニュース (必須 - 飛ばさないでください):**
4. `search` 「[TICKER] [会社名] の最近のニュース展開」
   - 記録: 過去 60 日間の重要なニュース - M&A、製品の発売、役員の交代、規制措置、パートナーシップ、法的発展、関税、または今後の業績報告書やフォワードガイダンスに影響を与える可能性のあるあらゆるイベント。
   - 各項目について、日付、見出し、潜在的な収益への影響に注目してください。
   - **直ちに kensho-findings.txt に追加してください。**

**セクターの背景:**
5. `search` 「[企業の業界/セクター] セクター見通しの傾向」
   - 記録: セクターレベルの追い風/逆風、マクロデータ、競争力学。
   - **直ちに kensho-findings.txt に追加してください。**

---

<a id="phase-5-financial-data-collection"></a>
## フェーズ 5: 財務データの収集

**四半期財務 (過去 8 四半期):**
`get_financial_line_item_from_identifiers` と `period_type="quarterly"`、`num_periods=8`:
`revenue`, `gross_profit`, `operating_income`, `ebitda`, `net_income`, `diluted_eps`

**各行項目の呼び出しが戻ったら、すぐに ** `/tmp/earnings-preview/financials.csv` に追加します。返されたままの生の値を正確に書き込みます。まだ丸めたり変換したりしないでください。正確な MCP 関数呼び出しとパラメーターを含む `source` 列を含めます。
```
ticker,period,line_item,value,source
D,Q4 2024,revenue,3941000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q1 2025,revenue,3400000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q2 2025,revenue,4076000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q3 2025,revenue,3810000000,get_financial_line_item_from_identifiers(identifier='D',line_item='revenue',period_type='quarterly')
D,Q4 2024,diluted_eps,1.09,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
D,Q1 2025,diluted_eps,-0.11,get_financial_line_item_from_identifiers(identifier='D',line_item='diluted_eps',period_type='quarterly')
...
```

**マージンや成長率はまだ計算しないでください。** 生データのみを書き込みます。計算はフェーズ 6 で行われます。

**セグメントデータ:**
- `get_segments_from_identifiers` と `segment_type="business"`、`period_type="quarterly"`、`num_periods=8`
- 前年同期を比較するには前年四半期が必要となるため、4 四半期ではなく 8 四半期が必要です。 2025 年第 3 四半期の前年比を計算するには、2024 年第 3 四半期、つまり第 5 四半期まで遡る必要があります。 **前年四半期のセグメント データが API 応答で利用できない場合は、それを推定したり捏造したりしないでください。レポートに「y/y は利用できません」と記載します。**

**すぐに書き込みます** `/tmp/earnings-preview/segments.csv`:
```
ticker,period,segment_name,revenue,source
D,Q3 2024,Dominion Energy Virginia,2762000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2024,Dominion Energy South Carolina,848000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2024,Contracted Energy,260000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2025,Dominion Energy Virginia,3311000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2025,Dominion Energy South Carolina,945000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
D,Q3 2025,Contracted Energy,297000000,get_segments_from_identifiers(identifier='D',segment_type='business',period_type='quarterly')
...
```

**決算発表の履歴（株価チャートの注記用）：**
- `get_earnings_from_identifiers`で、対象の12か月の株価期間内の過去の決算発表日を集めます。
- **すぐに書き込みます** `/tmp/earnings-preview/earnings-dates.csv`:
```
ticker,earnings_date,call_name,source
D,2025-05-02,Q1 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
D,2025-08-01,Q2 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
D,2025-10-31,Q3 2025 Earnings Call,get_earnings_from_identifiers(identifier='D')
...
```

---

<a id="phase-6-verification--calculations-mandatory--do-not-skip"></a>
## フェーズ 6: 検証と計算 (必須 — スキップしないでください)

レポートを生成する前に、すべての中間ファイルを読み込み、クリーンなデータから計算を実行します。このフェーズでは、圧縮された会話コンテキストではなくファイルから作業することで、データの整合性を確保します。

1. **bash `cat` コマンドを使用して、すべての中間ファイルを読み取ります**。
   - `cat /tmp/earnings-preview/company-info.txt`
   - `cat /tmp/earnings-preview/transcript-extracts.txt`
   - `cat /tmp/earnings-preview/financials.csv`
   - `cat /tmp/earnings-preview/segments.csv`
   - `cat /tmp/earnings-preview/prices.csv`
   - `cat /tmp/earnings-preview/peer-eps.csv`
   - `cat /tmp/earnings-preview/peer-market-caps.csv`
   - `cat /tmp/earnings-preview/consensus-eps.csv`
   - `cat /tmp/earnings-preview/kensho-findings.txt`
   - `cat /tmp/earnings-preview/earnings-dates.csv`

2. **コンテキスト内の生データから派生メトリクスを計算**:
   - 粗利益率 % = 売上総利益 / 収益 (四半期あたり)
   - 営業利益率 % = 営業利益 / 収益 (四半期あたり)
   - 売上前年比成長率 % = (現在の Q 売上 - 前年 Q 売上) / 前年 Q 売上
   - EPS 前年比成長率 % = 同じロジック。 「n.m.」を使用します。基数が負の場合
   - セグメントの前年比成長率 % = セグメント名を前年比 Q と一致させます。見つからない場合は、「y/y が利用できません」と記入してください
   - 企業ごとの LTM P/E = 最新価格 / 直近 4 四半期の EPS の合計 (`peer-eps.csv` を使用して、ティッカーごとにどの 4 四半期が利用可能であるかを確認します)
   - 各社のNTM P/E＝直近株価÷NTM EPS。**NTM EPSは`consensus-eps.csv`にある今後4四半期のコンセンサス平均EPS予想の合計**です。各銘柄の4期分のconsensus_mean_epsを加算します。同業他社について将来の四半期予想が4期分揃わない場合、NTM P/Eは「n/a」とします。どの4四半期を合計したか付録に記載します。
   - 株式リターン (YTD、1 年、30 日、90 日) = `prices.csv` で **すべてのティッカーに共通する最初の日** を見つけ、その日付からのリターンを計算します

3. **クロスチェック**:
   - すべてのセグメント y/y に、`segments.csv` の実際の前年度の行があることを確認します。そうでない場合は、「y/y は利用できません」とマークしてください。
   - すべての銘柄で、株価リターンの基準日が同じであることを確認します。
   - 構成要素を再合計して、複数ステップの計算を検証します (たとえば、LTM EPS 合計が 4 つの四半期値と一致します)。
   - `transcript-extracts.txt` 内のすべての逐語的な引用が正確なコピーアンドペースト (言い換えではない) であることを確認します。

4. **すべての派生値を含む** `/tmp/earnings-preview/calculations.csv` を書き込みます。
```
ticker,metric,value,formula,components
D,gross_margin_Q3_2025,32.5%,gross_profit/revenue,"gross_profit=1238100000,revenue=3810000000"
D,revenue_yoy_Q3_2025,+9.3%,(Q3_2025-Q3_2024)/Q3_2024,"Q3_2025=3810000000,Q3_2024=3486000000"
D,ltm_pe,24.2x,price/ltm_eps,"price=65.46,ltm_eps=2.70,quarters=Q4_2024+Q1_2025+Q2_2025+Q3_2025"
D,ntm_pe,18.5x,price/ntm_eps,"price=65.46,ntm_eps=3.56,quarters=Q4_2025(0.88)+Q1_2026(0.72)+Q2_2026(0.91)+Q3_2026(1.05),source=get_consensus_estimates_from_identifiers"
D,yoy_return,+17.6%,(end-start)/start,"end=65.46,start=55.67,base_date=2025-02-19"
DUK,yoy_return,+13.0%,(end-start)/start,"end=126.32,start=111.79,base_date=2025-02-19"
...
```

このファイルは、レポート内のすべての数値の信頼できる唯一の情報源になります。

---

<a id="phase-7-generate-the-html-report"></a>
## フェーズ 7: HTML レポートの生成

**停止 — HTML を記述する前に、すべての中間ファイルを読む必要があります。これはブロックの前提条件です。**

これはオプションではありません。以下の各 `cat` コマンドを **別個の bash ツール呼び出し** (1 つに結合しない) として実行する必要があります。これにより、各ファイルの内容が個別に読み込まれ、会話に表示されるようになります。これらを 1 つのコマンドに結合しないでください。ファイルをスキップしないでください。

これらのコマンドを **一度に 1 つずつ、それぞれ独自の bash 呼び出しとして実行**します。

1. `cat /tmp/earnings-preview/company-info.txt`
2. `cat /tmp/earnings-preview/transcript-extracts.txt`
3. `cat /tmp/earnings-preview/financials.csv`
4. `cat /tmp/earnings-preview/segments.csv`
5. `cat /tmp/earnings-preview/prices.csv`
6. `cat /tmp/earnings-preview/peer-eps.csv`
7. `cat /tmp/earnings-preview/peer-market-caps.csv`
8. `cat /tmp/earnings-preview/consensus-eps.csv`
9. `cat /tmp/earnings-preview/kensho-findings.txt`
10. `cat /tmp/earnings-preview/earnings-dates.csv`
11. `cat /tmp/earnings-preview/calculations.csv`

**すべてのファイルを読み取った後、すべてのファイルとそのステータスをリストした概要メッセージをユーザーに出力する必要があります**。まさに次の形式を使用してください。

```
--- DATA FILE VERIFICATION ---
1. company-info.txt        ✓ loaded ([N] lines)
2. transcript-extracts.txt ✓ loaded ([N] lines)
3. financials.csv          ✓ loaded ([N] rows)
4. segments.csv            ✓ loaded ([N] rows)
5. prices.csv              ✓ loaded ([N] rows)
6. peer-eps.csv            ✓ loaded ([N] rows)
7. peer-market-caps.csv    ✓ loaded ([N] rows)
8. consensus-eps.csv       ✓ loaded ([N] rows)
9. kensho-findings.txt     ✓ loaded ([N] lines)
10. earnings-dates.csv     ✓ loaded ([N] rows)
11. calculations.csv       ✓ loaded ([N] rows)

All intermediate data files loaded successfully.
Generating report using file data as the single source of truth.
---
```

ファイルが見つからないか空の場合は、停止して、どのファイルが失敗したかをユーザーに伝えます。データが欠落している状態でレポートの生成を続行しないでください。

**HTML レポート内のすべての数値、引用符、ソース URL、および MCP 関数呼び出しの参照は、以前の会話の記憶からではなく、これらのファイルから取得する必要があります。** ファイルは信頼できる唯一の情報源です。以前の会話コンテキストは圧縮または要約されている可能性があり、依存するとエラーが含まれます。データ ポイントがファイルに存在しない場合、そのデータ ポイントはレポートに表示されません。

完全な HTML テンプレート、CSS、Chart.js の設定については、[report-template.md](report-template.md) を参照してください。

**必須 — グラフにはテンプレート ヘルパー関数を使用します:**
report-template.md は、事前に構築され、デバッグされた Chart.js ヘルパー関数を提供します。グラフを作成するには、これらの関数を正確に使用する必要があります。カスタムのインライン Chart.js コードを記述しないでください。ヘルパーは次のとおりです。
- `createRevEpsChart(canvasId, labels, revenueData, epsData, revLabel)` — 図 1 の場合
- `createMarginChart(canvasId, labels, grossMargins, opMargins)` — 図 2 の場合
- `createRevGrowthChart(canvasId, labels, growthData)` — 図 3 の場合
- `createAnnotatedPriceChart(canvasId, labels, prices, earningsDates, ticker)` — 図 5 の場合
- `createCompPerfChart(canvasId, labels, datasets)` — 図 6 の場合
- `createPEChart(canvasId, companies)` — 図 7 の場合

各チャート呼び出しは、try-catch ブロックでラップされた独自の `<script>` タグ内になければなりません。これにより、1 つのグラフのバグによって他のグラフのレンダリングが妨げられることがなくなります。例:
```html
<script>
try {
  createRevEpsChart('chart-rev-eps', [...], [...], [...], 'Revenue ($B)');
} catch(e) { console.error('Figure 1 error:', e); }
</script>
<script>
try {
  createMarginChart('chart-margins', [...], [...], [...]);
} catch(e) { console.error('Figure 2 error:', e); }
</script>
```

<a id="report-structure-4-5-pages-total"></a>
### レポート構成 (合計 4 ～ 5 ページ)

このレポートは、**説明** (1 ～ 2 ページ) と **図** (3 ～ 5 ページ) の 2 つの部分に分かれています。これらをしっかりと統合してください。

---

**AI 免責事項 (必須 — 3 か所に表示する必要があります):**
レポート HTML には次の免責事項テキストを含める必要があります。これはオプションではありません。これがないとレポートは不完全になります。

> **「分析は AI によって生成されます - すべての出力を確認してください。」**

正確に次の 3 つの場所に表示される必要があります。
1. **ヘッダー バナー** — 表紙ヘッダーの直前、中央に配置された黄色のバナー: `<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`
2. **フッター** — ページ フッター div 内で、目立つ黄色のバナーとして表示されます: `<div class="footer-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`
3. **付録** — 表の前の付録セクションの最初の行: `<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`

---

**ページ1：表紙と投資仮説**

- **AI 免責条項バナー** (黄色、中央 - 上記の AI 免責条項を参照)
- **ヘッダー**: 会社名 (TICKER) | 産業 | 報告日
- **タイトル：** 当該四半期に即したテーマ性のあるものにします。例：「Walmart Inc. (WMT) Q4 FY2026決算プレビュー：Holiday Harvest — Furnerの初回決算は$1T（1兆ドル）の投資仮説を裏付けるか？」
- **投資仮説の要旨**（箇条書きを交え、短い段落を最大2〜3段落）：
  - 今回の決算に何を期待するかを1〜2文で示します。
  - 4 ～ 6 個の箇条書き: 当社の EPS 予想とコンセンサス、ガイダンスの期待、注目すべき重要な指標、株価を動かすもの、主要な議論
  - 率直かつ意見を述べてください — あらゆることをヘッジせずに、見解を持ちましょう
- 最新の決算説明会における**経営陣の重要な発言**を、関連する箇所の説明へ織り込みます。独立した見出しは作りません。投資仮説を裏付ける証拠として自然に統合し、字下げしたblockquoteで示します。

---

**ページ2：業績予想、テーマ、ニュース**

- **コンセンサス推定表** (単一の表、図としてラベル付け):
  - 列: メトリック | コンセンサス | 私たちの見積もり | 前年比変化
  - 行：売上高、EPS、売上総利益率、営業利益と、その企業について市場アナリストが重視する固有KPIを2〜3件（既存店売上高、EC成長率、会費収入等）。
  - **色分けは厳密に機械的です:** y/y 変更値が負の場合は、`class="neg"` (赤) を使用します。正の場合は、`class="pos"` (緑) を使用します。ゼロまたは N/A の場合は、`class="neutral"` を使用します。数値の符号によってクラスが決まります。解釈に基づいてオーバーライドしないでください。たとえ下落が小さくても、-1.1% は常に赤です。
  - これは唯一のガイダンス/見積もりセクションです。推定データを他の場所で繰り返さないでください。

- **見出し EPS 以外の主要な指標** (箇条書き、3 ～ 5 項目):
  - EPS 数値を超えて、今四半期が良い四半期であるか悪い四半期であるかを判断する具体的な指標
  - 各項目について、指標の内容、コンセンサス・経営陣の予想、重要な理由を示します。
  - 具体的に: 「ウォルマート コネクトの広告収入の伸び (コンセンサスは前年比 ~30%、第 3 四半期は 33%)」

- **注目のテーマ** (3 ～ 5 個の箇条書き):
  - 今後のレポートの将来の見通しに関する事項
  - 経営陣が達成すべきこと、驚くべきこと、弱気派が焦点を当てていること
  - 各テーマ：最大1～2文

- **最近のニュースと開発** (3 ～ 5 個の箇条書き):
  - 過去 60 日間の重要なニュースを 1 行ずつ表示
  - 日付 + 見出し + 簡単な影響評価
  - 次の決算発表または会社側の見通しに影響し得る項目だけを含めます。

---

**ページ 3 ～ 5: 図 (すべてのグラフと表)**

すべての図には連続した番号が付けられています。すべての図にはタイトルとソース行があります。

- **図 1: 四半期収益と希薄化後 EPS** — バー/ラインのコンボ、8 四半期
- **図2：利益率の推移（売上総利益率・営業利益率、%）** — 二本の折れ線、8四半期
- **図 3: 収益成長率 y/y %** — 緑/赤の条件付き色付きの棒グラフ。 **現在データと前年データの両方が存在する四半期のみを含めます** (通常は、取得された 8 四半期のうちの最新の 4 四半期)。 y/y を計算できない四半期は含めないでください。グラフには 8 本ではなく 4 本の棒が必要です。
- **図4：事業セグメント別売上高** — 表：セグメント | 直近四半期売上高（$M） | 全体比率 | 前年同期比
- **図 5: 決算日を含む 1 年間の株価** — 四半期および決算後の 1 日の動きをラベル付けした、決算日の垂直注釈付きの価格線
- **図 6: 株価パフォーマンスと競合他社 (100 にインデックス付け)** — 複数折れ線グラフ、対象企業は太い実線、競合他社は細い破線
- **図 7: LTM PER 対競合他社** — 横棒グラフ、対象企業は紺色で強調表示されています
- **図8：競合企業の比較表** — ティッカー | 企業名 | 時価総額 | LTM P/E | NTM P/E | 年初来% | 1年間%

---

**付録: データ ソースと計算 (必須 — スキップしたり省略したりしないでください)**

付録は AI 免責事項バナーで始まらなければなりません: `<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`

報告書の最終ページには、報告書で引用された**すべての主張** (数値および非数値) を文書化した付録表を含めなければなりません。 **レポート本文に表示されるすべての数値には、この付録に対応する行が必要です。また、レポート本文内のそのようなすべての数値は、付録行までスクロールするクリック可能な `<a href="#ref-N">` ハイパーリンクである必要があります。** 付録へのハイパーリンクなしでレポートに数値が表示される場合、レポートは不完全です。

- **表の列**: 参照番号 | 事実 | 値 | ソースと派生
- **参照 #**: レポート本文のハイパーリンク アンカーに一致する連続 ID (`ref-1`、`ref-2` など)。各行には `id="ref-N"` 属性があるため、ハイパーリンクはその属性にスクロールします。
- **事実**: 人間が読めるラベル (例: 「2026 年度第 3 四半期収益」、「LTM P/E — WMT」、「経営陣が関税逆風を指摘」、「バークレイズがオーバーウェイトに格上げ」)
- **値**: レポートに表示される正確な数値 (例: "$152.3B"、"24.5%"、"28.1x")。数値以外の事実については、空白のままにするか、「N/A」と記入します。
- **出典と派生**: これは重要な列です。 **すべての行には、単なるラベルではなく、特定の詳細なソースが必要です。** 次のルールに厳密に従ってください。

  **S&P Capital IQ の生の財務データ (収益、EPS、粗利益、営業利益、純利益、EBITDA、価格、時価総額など):**
  - 使用した MCP 関数とその主要なパラメータを記述します。形式: `S&P Capital IQ — [function_name](identifier='[TICKER]', line_item='[item]', period_type='[type]', period='[Q# FY####]')`
  - 例:
    - `S&P Capital IQ — get_financial_line_item_from_identifiers(identifier='WMT', line_item='revenue', period_type='quarterly', period='Q3 FY2026')`
    - `S&P Capital IQ — get_financial_line_item_from_identifiers(identifier='WMT', line_item='diluted_eps', period_type='quarterly', period='Q3 FY2026')`
    - `S&P Capital IQ — get_prices_from_identifiers(identifier='WMT', periodicity='day')`
    - `S&P Capital IQ — get_capitalization_from_identifiers(identifier='WMT', capitalization='market_cap')`
  - **詳細を記載せずに「S&P Capital IQ」とだけ書かないでください。** 読者は、どのツール呼び出しからどのデータ ポイントがこの数値を生成したかを正確に把握する必要があります。

  **計算値 (利益率、成長率、PER、リターン、前年比変化):**
  - **ハイパーリンクされたコンポーネント**を使用して完全な式を表示します。各コンポーネントは、その生データ ポイントの付録行に戻る `<a href="#ref-N">` リンクである必要があります。これは重要です。リーダーは、計算された値からその各入力までクリックスルーできなければなりません。
  - 例: `Gross Margin = <a href='#ref-5'>Gross Profit $37.2B</a> / <a href='#ref-1'>Revenue $152.3B</a> = 24.4%. Source: S&P Capital IQ (calculated)`
  - 例: `LTM P/E = <a href='#ref-20'>Price $172.35</a> / (<a href='#ref-8'>Q1 EPS $1.47</a> + <a href='#ref-9'>Q2 EPS $1.84</a> + <a href='#ref-10'>Q3 EPS $1.53</a> + <a href='#ref-11'>Q4 EPS $1.80</a>) = $172.35 / $6.64 = 25.9x`
  - 例: `Revenue y/y growth = (<a href='#ref-12'>Q3 FY26 Rev $165.8B</a> - <a href='#ref-3'>Q3 FY25 Rev $160.8B</a>) / <a href='#ref-3'>Q3 FY25 Rev $160.8B</a> = +3.1%`
  - **すべての数式コンポーネントはクリック可能なハイパーリンクである必要があります。** プレーンテキストの数値を使用して数式を作成しないでください。

  **トランスクリプトをソースとする主張の場合 (引用、経営陣のコメント、ガイダンス):**
  - トランスクリプトから**逐語的な抜粋文**を書きます。
  - トランスクリプトを完全名と、それを取得するために使用される `key_dev_id` で参照します。
  - 形式: `"[verbatim quote]" — [Speaker], [Title]. Source: [Q# FY#### Earnings Call Transcript] (key_dev_id: [ID])`
  - 例: `"We expect comp sales growth of 3-4% in Q4" — CEO John Furner. Source: Q3 FY2026 Earnings Call Transcript (key_dev_id: 12345678)`

  **Kensho Grounding の検索結果 (ニュース、アナリスト評価、コンセンサス推定):**
  - 主要な結果、または検索結果からの抜粋を書き込みます。
  - **必須: Kensho `search` ツールによって返されたソース URL** を、クリック可能な `<a href="[URL]" target="_blank">` ハイパーリンクとして含めます。これが最も重要な部分です。読者はクリックして元のソースにアクセスできる必要があります。
  - 形式: `"[finding/excerpt]" — <a href="[URL]" target="_blank">[Source Title or Publication]</a>. Query: search("[query used]")`
  - 例: `"Barclays upgraded WMT to Overweight with $210 price target on Jan 15, 2026." — <a href="https://www.investing.com/news/barclays-upgrades-wmt" target="_blank">Investing.com, Jan 15 2026</a>. Query: search("WMT analyst ratings price target upgrades downgrades")`
  - 特定の結果に対して URL が返されなかった場合は、「ソース URL が利用できません」と書き込み、検索クエリを含めます。

**完全性チェック:** レポートを完成させる前に、レポート本文のすべての番号に目を通します。 `<a href="#ref-N" class="data-ref">` でラップされていない数値がある場合は、修正してください。付録の行に「S&P Capital IQ」のような単なるラベルで関数呼び出しの詳細がない Source & Derivation がある場合は、それを修正します。計算された値の式にハイパーリンクされたコンポーネントがない場合は、それを修正します。 Kensho が提供する主張にソース URL が欠けている場合は、修正してください。

付録の行をセクション (財務、評価、見積りとコンセンサス、トランスクリプトの主張、ニュースとアナリストのコメント、株価パフォーマンス) ごとに小見出しを付けてグループ化します。小さいフォント サイズ (10 ～ 11 ピクセル) を使用します。

---

<a id="phase-8-output"></a>
## フェーズ 8: 出力

1. 完全な HTML ファイルを現在の作業ディレクトリの `earnings-preview-[TICKER]-YYYY-MM-DD.html` に書き込みます。
2. ブラウザで開きます: `open earnings-preview-[TICKER]-YYYY-MM-DD.html`
3. ファイルが作成されたことをユーザーに伝え、主な結果を要約します。

---

<a id="writing-guidelines"></a>
## 執筆ガイドライン

- **絵文字は使用しない**: レポート内のどこにも絵文字を使用しないでください。これは専門的な研究文書です。
- **簡潔**: 印刷ページ数は 4 ～ 5 ページです。すべての文には重みがなければなりません。可能な限り、段落ではなく箇条書きを使用してください。セクションが長いと感じたら、カットしてください。
- **数値を具体的に示す：**「売上高が大きく成長」ではなく、「売上高$52.4B（524億ドル）、前年比5.2%増」と書きます。
- **見解を示す：** これは決算プレビューであり単なる要約ではありません。予想、重要な点、その理由を述べます。独自の見方を示し、データで裏付けます。
- **ヘッダーのない経営陣の引用**: 最新の通話からの 3 ～ 4 つの重要な経営陣の引用を、ブロック引用として物語に直接織り込みます。 「重要な管理の引用」セクション見出しを作成しないでください。裏付けとなる証拠として自然に流れるようにしてください。
- **プロフェッショナルな口調**: セルサイドの株式調査スタイル - 分析的、直接的、データ主導型。
- **チャートは実際のデータを使用する必要があります**: すべてのチャートには実際の MCP データが入力されます。決して捏造しないでください。
- **競合他社のコンテキスト**: 競合他社と比較したフレーム評価。同業者が20倍や35倍で取引していることを知らなければ、PERが25倍であっても意味がありません。
- **ハイパーリンクされた主張**: すべての事実に関する主張 (数値または定性) は、付録のエントリにリンクする `<a class="data-ref">` タグである必要があります。番号: `<a href="#ref-1" class="data-ref">$152.3B</a>`。定性的: `<a href="#ref-25" class="data-ref">management flagged tariff headwinds as the primary margin risk</a>`。付録に追跡可能な情報源がなければ、いかなる事実も記載すべきではありません。
