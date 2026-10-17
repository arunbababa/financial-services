> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/agent-plugins/earnings-reviewer/skills/earnings-analysis/references/report-structure.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="report-structure-and-templates"></a>
# レポートの構造とテンプレート

このドキュメントには、決算更新DOCXレポートの完全なページごとのテンプレートとフォーマット要件が記載されています。

<a id="complete-report-structure"></a>
## 完全なレポート構造

**レポートの構造:**

---

<a id="page-1-earnings-summary"></a>
## ページ1：決算概要

**トップセクション - ヘッダー:**
```
[COMPANY NAME] ([TICKER])
[QUARTER] [YEAR] EARNINGS UPDATE

[Current Date]

Rating: [MAINTAIN/RAISE/LOWER] [RATING]
Price (as of [date]): $XX.XX
Price Target: [OLD → NEW if changed, or MAINTAIN $XXX]
```

日本語補訳：企業名（ティッカー）、四半期・年度、「決算更新」、作成日を記載する。投資評価は維持／引き上げ／引き下げを示し、基準日付き株価、変更した場合は従来→新目標株価、変更しない場合は「目標株価XXXドルを維持」と記載する。

**上部セクション - クイック サマリー ボックス:**
```
EARNINGS SUMMARY
─────────────────────────────────────────────────
Q[X] [YEAR] RESULTS: [BEAT / INLINE / MISS]

                Reported    Est      Variance
Revenue         $X,XXX      $X,XXX   +$XXX (+X%)
EPS (Adj)       $X.XX       $X.XX    +$X.XX (+X%)

Key Takeaways:
■ [Takeaway 1 - one sentence]
■ [Takeaway 2 - one sentence]
■ [Takeaway 3 - one sentence]
```

日本語補訳：「決算概要」に対象四半期・年度と「予想超過／予想並み／予想未達」を示す。表は公表実績・予想・差異の列、売上高と調整後EPSの行で構成し、差異を金額と率で示す。主要なポイントを各1文、3項目で記す。

**主な内容 - 投資への影響 (3 ～ 4 つの箇条書き):**

■記号を使い、**太字の見出し**と1段落程度の説明を付ける。

```
■ **Results beat on strong [segment/geography/product], maintaining positive momentum**

Q[X] revenue of $X.XB exceeded our $X.XB estimate by X% and consensus by X%,
driven primarily by [specific driver]. [Segment] revenue grew X% YoY (vs. our
X% estimate), while [segment] grew X% (vs. X% estimate). Management highlighted
[specific products/initiatives] as key growth drivers and maintained confident
tone on outlook. The beat demonstrates [thesis point], reinforcing our positive
view.

■ **Margins expanded XXbps YoY despite [headwind], showcasing operational leverage**

[Detailed margin analysis paragraph...]

■ **Guidance raised / maintained / lowered - implies [interpretation]**

[Detailed guidance analysis paragraph...]

■ **Maintaining [RATING] with [raised/unchanged] $XXX price target**

[Investment conclusion paragraph...]
```

日本語補訳：

- **好調な[セグメント／地域／製品]により実績は予想を上回り、良好な勢いが継続。** 第[X]四半期売上高[X.X]十億ドルは、主に[具体的要因]により、当社予想[X.X]十億ドルを[X]%上回り、コンセンサス予想も[X]%上回った。[セグメント]売上高は前年同期比[X]%増（当社予想[X]%）、別の[セグメント]は[X]%増（予想[X]%）だった。経営陣は[特定の製品／施策]を主要な成長要因として挙げ、先行きにも自信を保った。予想超過は[投資判断の論点]を裏付け、当社の強気見解を補強する。
- **[逆風]にもかかわらず利益率は前年同期比XXbps改善し、営業レバレッジが表れた。** 続けて詳細な利益率分析を記載する。
- **会社業績見通しを引き上げ／維持／引き下げ — [解釈]を示唆。** 続けて詳細な見通し分析を記載する。
- **目標株価を[引き上げ／据え置き]のXXXドルとし、投資評価[RATING]を維持。** 続けて投資判断の結論を記載する。

**下のセクション - 更新した業績予想表:**

```
UPDATED FINANCIAL ESTIMATES
─────────────────────────────────────────────────────────────────
                     FY2024E (OLD)  FY2024E (NEW)  Change  FY2025E (NEW)
Revenue ($M)         XX,XXX         XX,XXX         +X%     XX,XXX
Revenue Growth (%)   X.X%           X.X%           +XXbps  X.X%
Gross Margin (%)     XX.X%          XX.X%          +XXbps  XX.X%
EBITDA ($M)          X,XXX          X,XXX          +X%     X,XXX
EBITDA Margin (%)    XX.X%          XX.X%          +XXbps  XX.X%
EPS (Adjusted) ($)   X.XX           X.XX           +X%     X.XX
P/E (x)              XX.Xx          XX.Xx          -X%     XX.Xx

Note: "E" = Estimate. Old estimates from [prior report date].
Source: Company data, [Firm Name] estimates.
```

日本語補訳：「更新した財務予想」は2024年度予想の従来・新・増減、2025年度の新予想を比較する。行は売上高（百万ドル）、売上成長率、売上総利益率、EBITDA（百万ドル）、EBITDAマージン、調整後EPS（ドル）、PER（倍）。金額・EPSは増減率、利益率の差はbpsで示す。Eは予想を意味し、従来予想のレポート日を注記する。出典は企業データと[調査会社名]の予想。

---

<a id="pages-2-3-detailed-results-analysis"></a>
## ページ 2 ～ 3: 詳細な結果分析

決算を次の項目に分けて分析する。

<a id="revenue-analysis-1-page"></a>
### 売上高分析（1ページ）
- 売上高全体が予想を上回った・下回った理由の説明
- セグメント/地域/製品の内訳
- 前年同期比と前四半期比の推移
- ガイダンスとの比較 (提供されている場合)

**表: 四半期売上高の推移**
```
                        Q[X-3]  Q[X-2]  Q[X-1]  Q[X]    YoY Chg  QoQ Chg
Total Revenue ($M)      X,XXX   X,XXX   X,XXX   X,XXX   +X%      +X%
  [Segment A] ($M)      XXX     XXX     XXX     XXX     +X%      +X%
  [Segment B] ($M)      XXX     XXX     XXX     XXX     +X%      +X%
  [Segment C] ($M)      XXX     XXX     XXX     XXX     +X%      +X%

Note: Q[X] = [Quarter] [Year]
Source: Company reports, [Firm Name] analysis
```

日本語補訳：直近4四半期の総売上高とセグメントA・B・Cの売上高を百万ドル単位で並べ、前年同期比と前四半期比の増減率を示す。第[X]四半期がどの年度・四半期かを注記する。出典は企業の公表資料と[調査会社名]の分析。

<a id="profitability-analysis-1-page"></a>
### 収益性分析 (1 ページ)
- 売上総利益率の分析（変動要因、推移）
- 営業利益率分析
- 営業利益より下の損益項目（利息、税金など）
- EPSの調整表（調整後EPSとGAAPベースのEPSの照合）

**表：利益率分析**
```
                        Q[X-3]  Q[X-2]  Q[X-1]  Q[X]    YoY Chg
Gross Margin (%)        XX.X%   XX.X%   XX.X%   XX.X%   +XXbps
Operating Margin (%)    XX.X%   XX.X%   XX.X%   XX.X%   +XXbps
Net Margin (%)          XX.X%   XX.X%   XX.X%   XX.X%   +XXbps

Key Drivers:
+ [Positive driver 1]
+ [Positive driver 2]
- [Negative driver 1]
- [Negative driver 2]
```

日本語補訳：直近4四半期の売上総利益率、営業利益率、純利益率と、前年同期比の変化（bps）を示す。主要な変動要因としてプラス要因2点、マイナス要因2点を記載する。

**これらのページに 2 ～ 3 つのグラフを埋め込みます:**
- グラフ 1: 四半期売上高の推移
- グラフ 2: 四半期ごとの EPS の推移
- チャート 3: 利益率の推移

---

<a id="pages-4-5-key-metrics--guidance"></a>
## ページ 4 ～ 5: 主要な指標とガイダンス

<a id="business-metrics-1-page"></a>
### 事業指標（1ページ）
- 顧客数、ARPU、販売数量、店舗数など
- 企業が重視するあらゆる指標
- 予想との比較
- 傾向と展望

**表: 主要な事業指標**
```
                        Q[X-3]  Q[X-2]  Q[X-1]  Q[X]    YoY Chg  Our Est  Var
[Metric 1]              XXX     XXX     XXX     XXX     +X%      XXX      +X%
[Metric 2]              XXX     XXX     XXX     XXX     +X%      XXX      +X%
[Metric 3]              XXX     XXX     XXX     XXX     +X%      XXX      +X%

Source: Company reports
```

日本語補訳：指標1～3について直近4四半期の実績、前年同期比、当社予想、予想との差異を並べる。出典は企業の公表資料。

<a id="guidance--outlook-1-page"></a>
### ガイダンスと展望 (1 ページ)
- 会社業績見通し（ガイダンス）の内容（示されている場合）
- 以前のガイダンスとの比較
- 市場予想との比較
- レポート作成者による達成可能性の評価
- 主な前提条件

**ガイダンスが提供される場合:**
```
MANAGEMENT GUIDANCE vs. ESTIMATES
─────────────────────────────────────────────────────────────────
                     New Guidance    Old Guidance    Change    Street
FY2024E Revenue      $XX-XXB         $XX-XXB         Raised    $XX.XB
FY2024E EPS          $X.XX-X.XX      $X.XX-X.XX      Raised    $X.XX

Our Take: [Brief assessment of guidance]
```

日本語補訳：「会社業績見通しと予想の比較」として2024年度の売上高（十億ドル）・EPSについて、新ガイダンス、従来ガイダンス、変更内容、市場予想を並べる。例ではいずれも引き上げ。最後に会社業績見通しに対する当社の簡潔な評価を記す。

**2 ～ 3 個のグラフを埋め込む:**
- グラフ 4: 主要な指標の傾向
- グラフ 5: 会社業績見通しと市場予想の比較
- 図 6: セグメント別・地域別売上高

---

<a id="pages-6-7-updated-investment-thesis"></a>
## ページ6～7：投資判断の根拠の更新

<a id="thesis-impact-assessment-1-2-pages"></a>
### 投資判断の根拠への影響評価（1～2ページ）

投資判断を支える主要な柱のそれぞれについて、決算の影響を評価する。

```
■ **Thesis Pillar 1: [Original thesis statement]**

Status: [STRENGTHENED / UNCHANGED / WEAKENED]

Q[X] results [supported / challenged] this thesis pillar because [specific
evidence from results]. [Detailed analysis of 150-200 words explaining how
results impact this specific thesis element.]

■ **Thesis Pillar 2: [Original thesis statement]**

[Similar analysis]

■ **Thesis Pillar 3: [Original thesis statement]**

[Similar analysis]
```

日本語補訳：柱1に従来の投資判断の根拠を記載し、状態を「強化／変わらず／弱まった」で示す。第[X]四半期決算がこの柱を支持したか、疑問を投げかけたかを、決算から得られる具体的証拠で説明する。個々の根拠に及ぼす影響を英語150～200語相当で詳述する。柱2・柱3にも同様の分析を行う。

<a id="risks-update-05-pages"></a>
### リスクの最新情報 (0.5 ページ)
- 新たなリスクが特定されましたか?
- 既存のリスクは軽減されましたか、それとも悪化しましたか?
- 簡単な評価

**1 ～ 2 個のグラフを埋め込む:**
- 図 7: 現在と過去のバリュエーションの比較
- 図表 8: 業績予想修正の比較

---

<a id="pages-8-10-valuation--estimates"></a>
## ページ8～10：バリュエーションと業績予想

<a id="updated-valuation-1-2-pages"></a>
### バリュエーションの更新（1～2ページ）

**DCF アップデート:**
```
Updated DCF inputs based on Q[X] results:
- Revenue growth FY24E: X.X% → X.X% (raised/lowered)
- EBIT margin FY24E: XX.X% → XX.X%
- Terminal growth: X.X% (unchanged)
- WACC: X.X% (unchanged)

Updated DCF fair value: $XXX (prior: $XXX)
```

日本語補訳：第[X]四半期決算に基づき、2024年度の売上成長率とEBITマージンの従来→新前提を示す。売上成長率は引き上げ／引き下げを明記し、永久成長率とWACCは据え置きの例。更新後のDCF理論価値XXXドルを、従来のXXXドルと比較する。

**比較対象企業:**
```
[Company] trades at XX.Xx NTM P/E vs. peer median of XX.Xx (-X% discount).
Given [rationale], we believe [premium/discount/inline] valuation is warranted.
```

日本語補訳：[企業]の今後12か月（NTM）のPERはXX.X倍で、同業他社中央値XX.X倍に対しX%のディスカウント。[根拠]を踏まえ、プレミアム／ディスカウント／同水準のバリュエーションが妥当と判断する。

**目標株価の手法:**
```
Our $XXX price target (prior: $XXX) is based on:
- XX% DCF
- XX% NTM P/E of XX.Xx (vs. peers at XX.Xx)
- XX% EV/EBITDA

Implied upside: +XX% from current price of $XXX
```

日本語補訳：目標株価XXXドル（従来XXXドル）は、DCFにXX%、NTM PER XX.X倍（同業他社XX.X倍）にXX%、EV/EBITDAにXX%の重みを置いて算定する。現在株価XXXドルに対する上昇余地は+XX%。

<a id="updated-estimates-detail"></a>
### 更新した業績予想の詳細

少なくとも当期と翌期について、更新した業績予想を示す。

```
DETAILED ESTIMATE UPDATES
─────────────────────────────────────────────────────────────────
                            FY2024E                 FY2025E
                     Old      New      Change    New Estimate
Revenue ($B)         XX.X     XX.X     +X.X%     XX.X
  [Segment A]        XX.X     XX.X     +X.X%     XX.X
  [Segment B]        XX.X     XX.X     +X.X%     XX.X

Gross Profit ($B)    XX.X     XX.X     +X.X%     XX.X
Gross Margin (%)     XX.X%    XX.X%    +XXbps    XX.X%

EBITDA ($B)          X.X      X.X      +X.X%     X.X
EBITDA Margin (%)    XX.X%    XX.X%    +XXbps    XX.X%

Operating Income     X.X      X.X      +X.X%     X.X
Op Margin (%)        XX.X%    XX.X%    +XXbps    XX.X%

Net Income ($B)      X.X      X.X      +X.X%     X.X
EPS - Adjusted ($)   X.XX     X.XX     +X.X%     X.XX
EPS - GAAP ($)       X.XX     X.XX     +X.X%     X.XX

P/E (x)              XX.Xx    XX.Xx              XX.Xx
EV/EBITDA (x)        XX.Xx    XX.Xx              XX.Xx

Source: [Firm Name] estimates
```

日本語補訳：「業績予想更新の詳細」は、2024年度の従来予想・新予想・増減と、2025年度の新予想を並べる。項目は売上高とセグメントA・B内訳、売上総利益と売上総利益率、EBITDAとEBITDAマージン、営業利益と営業利益率、純利益、調整後EPS、GAAPベースEPS、PER、EV/EBITDA。Bは十億ドル、EPSはドル、倍率は倍、利益率の差はbpsを示す。出典は[調査会社名]の予想。

**1 ～ 2 個のグラフを埋め込む:**
- 図表 9: P/E または EV/EBITDA バンド
- 図表 10: 目標株価の変更要因の内訳（従来→新）

---

<a id="pages-11-12-appendix-optional"></a>
## ページ 11 ～ 12: 付録 (オプション)

<a id="detailed-quarterly-models-if-space-allows"></a>
### 詳細な四半期モデル (スペースが許せば)
- 損益計算書の詳細
- キャッシュフローのハイライト
- 貸借対照表のハイライト

<a id="call-transcript-highlights-optional"></a>
### 決算説明会の書き起こしの要点（任意）
- 主なQ&Aの抜粋
- 注目すべき経営陣の発言

<a id="peer-comparison-if-peers-have-reported"></a>
### 同業他社との比較（同業他社が決算発表済みの場合）
- 競合他社との結果の比較
- 市場シェアへの影響

**最終チャートを埋め込む:**
- 図 11: 同業他社比較
- 図 12: 追加の裏付けグラフ

---

<a id="formatting-requirements"></a>
## フォーマット要件

<a id="1-page-1-requirements"></a>
### 1. ページ 1 要件
- 明確な評価（アウトパフォームの維持、買いに引き上げるなど）
- 更新された目標株価を目立つように表示
- 従来予想と新予想の概要表
- ■記号を用いた、各1段落程度の箇条書き3～4項目

<a id="2-all-tables-requirements"></a>
### 2. すべてのテーブルの要件
- 表の下部に出典行を置く
- 明確な列見出しを付ける
- ヘッダー行の網掛け

<a id="3-all-charts-requirements"></a>
### 3. すべてのチャートの要件
- グラフの上に「Figure X - [Title]」のキャプションを置く
- グラフの下に「Source: [Source]」の行を置く
- プロフェッショナルな体裁にする

<a id="4-year-notation"></a>
### 4. 年表記
- 実績値にはAを使用 (Q3'24A)
- 予想値にはEを使用 (Q4'24E)

<a id="5-writing-style"></a>
### 5. 文体
- 数値から書く（「売上高が大幅成長」ではなく「売上高は15%増の12億ドル」）
- 英語では「versus」ではなく「vs.」を使う
- 直接的かつ簡潔であること
- 新しい情報に焦点を当てる

<a id="6-hyperlink-requirements-"></a>
### 6. ハイパーリンクの要件 ⭐⭐⭐
- すべての URL は Word でクリック可能なハイパーリンクである必要があります
- Ctrl+クリックで開く青色の下線付きテキスト
- 意味のあるテキストを表示します (生の URL ではありません)
- すべての情報源の引用には、該当する場合にはクリック可能なリンクが必要です
- プレーンテキストの URL は使用できません - 常にハイパーリンクとしてフォーマットされます

<a id="citation-examples-for-specific-content"></a>
## 特定の内容の引用例

<a id="for-beatmiss-analysis"></a>
### 予想の上振れ・下振れ分析の場合:
```
Revenue of $2.45B beat consensus of $2.39B by $60M (2.5%)¹

¹ Bloomberg consensus as of market close November 6, 2024; Company earnings release November 7, 2024
  [Hyperlink "earnings release" to: https://investor.company.com/news/q3-2024-earnings]
```

日本語補訳：売上高24億5,000万ドルはコンセンサス予想23億9,000万ドルを6,000万ドル（2.5%）上回った。脚注1の出典は2024年11月6日の市場引け時点のBloombergコンセンサスと、11月7日の企業決算発表資料。「earnings release」を例示URLにリンクする。

<a id="for-guidance"></a>
### ガイダンスについて:
```
Management raised FY2024 revenue guidance to $9.8-10.0B from prior $9.5-9.7B²

² Q3 2024 Earnings Call, November 7, 2024, CFO prepared remarks
  [Hyperlink "Earnings Call" to: https://seekingalpha.com/article/...]
  Prior guidance from Q2 earnings call August 8, 2024
  [Hyperlink "Q2 earnings call" to August transcript]
```

日本語補訳：経営陣は2024年度売上高見通しを従来の95～97億ドルから98～100億ドルへ引き上げた。脚注2は2024年11月7日の第3四半期決算説明会でのCFOの事前準備発言を出典とする。「Earnings Call」をリンクし、従来見通しは8月8日の第2四半期決算説明会を出典として、その書き起こしにもリンクする。

<a id="for-key-metrics"></a>
### 主要な指標の場合:
```
Enterprise customers grew 23% YoY to 845, with net revenue retention at 128%³

³ Q3 2024 10-Q, page 23
  [Hyperlink "10-Q" to: https://www.sec.gov/cgi-bin/viewer?accession=...]
  Q3 2024 Investor Presentation slide 8
  [Hyperlink "Investor Presentation" to PDF]
```

日本語補訳：法人顧客数は前年同期比23%増の845社となり、売上高のネットリテンション率は128%。脚注3は2024年第3四半期Form 10-Qの23ページと、同四半期の投資家向けプレゼンテーションのスライド8を出典とし、それぞれにハイパーリンクを付す。
