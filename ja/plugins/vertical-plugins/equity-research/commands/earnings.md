---
description: Analyze quarterly earnings and create an earnings update report
argument-hint: "[company name or ticker] [quarter, e.g. Q3 2024]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/equity-research/commands/earnings.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：四半期決算を分析し、決算更新レポートを作る。

<a id="earnings-analysis-command"></a>
# 決算分析コマンド

四半期実績を分析する、専門的な株式調査の決算更新レポートを作る。

<a id="workflow"></a>
## ワークフロー

<a id="step-1-gather-information"></a>
### 手順1：情報を集める

入力から読む。
- 企業名・ティッカー。
- 四半期（例Q3 2024、Q2 FY25）。

なければ尋ねる。
- 「どの企業の決算を分析しますか」。
- 「どの四半期ですか（例Q3 2024）」。

<a id="step-2-verify-timeliness"></a>
### 手順2：新しさを確認する

**必須：** 続ける前に最新データか確認する。
1. "[Company] latest earnings results [current year]" を検索する。
2. 発表が過去3か月以内か確認する。
3. 説明会記録の日付が発表日と一致するか確認する。

古ければユーザーへ伝え、最新情報を探す。

<a id="step-3-load-earnings-analysis-skill"></a>
### 手順3：決算分析スキルを読み込む

`skill: "earnings-analysis"` でレポートを作る。

1. **データ収集（最新を検索）：**
   - 決算発表資料。
   - SEC EDGARの10-Q。
   - 決算説明会記録。
   - 投資家向け説明・補足資料。
   - コンセンサス（Bloomberg・FactSet）。

2. **予想上振れ・下振れ分析：**
   - 売上対コンセンサス：Xドル・X%の上振れ／下振れ。
   - EPS対コンセンサス：Xドル・X%の上振れ／下振れ。
   - 主要セグメント実績対期待。
   - 異なった**理由**を説明。

3. **主要指標分析：**
   - セグメント・地域別売上。
   - 粗利益率・営業利益率・純利益率の推移。
   - 会社予想の引上げ・維持・引下げ。
   - 更新した将来予想。

4. **図の作成（8〜12点）：**
   - 四半期売上推移。
   - 四半期EPS推移。
   - 利益率推移。
   - セグメント別売上。
   - 予想上振れ・下振れの要約。
   - 予想修正。
   - 評価の図。

5. **レポート（8〜12ページ）：**
   - 1ページ目：格付け・目標株価を含む概要。
   - 2〜3ページ：詳細実績分析。
   - 4〜5ページ：主要指標・会社予想。
   - 6〜7ページ：更新した投資判断の根拠。
   - 8〜10ページ：評価・予想。
   - クリック可能なリンク付き出典節。

<a id="step-4-deliver-output"></a>
### 手順4：成果物を渡す

1. **DOCXレポート：** 8〜12ページの決算更新。
2. **要約：**
   - 主要指標の予想上振れ・下振れ。
   - 会社予想変更。
   - 投資判断の根拠への影響（プラス／マイナス／中立）。

<a id="report-structure-reference"></a>
## レポート構成の参照

```
PAGE 1: EARNINGS SUMMARY
┌─────────────────────────────────────────────────────────────────┐
│ [Company] Q3 2024 Earnings Update                               │
│ Rating: BUY | Price Target: $XXX (from $XXX)                    │
├─────────────────────────────────────────────────────────────────┤
│ KEY TAKEAWAYS                                                   │
│ • Revenue beat by X% on strong [segment] performance            │
│ • EPS beat by $X.XX driven by margin expansion                  │
│ • FY guidance raised to $X.XX-$X.XX (from $X.XX-$X.XX)         │
│ • Thesis intact; maintain BUY rating                            │
├─────────────────────────────────────────────────────────────────┤
│ RESULTS SNAPSHOT                                                │
│ ┌─────────────┬──────────┬──────────┬──────────┐               │
│ │ Metric      │ Actual   │ Consensus│ Beat/Miss│               │
│ │ Revenue     │ $X.XXB   │ $X.XXB   │ +X.X%    │               │
│ │ EPS         │ $X.XX    │ $X.XX    │ +$X.XX   │               │
│ │ Gross Margin│ XX.X%    │ XX.X%    │ +XXbps   │               │
│ └─────────────┴──────────┴──────────┴──────────┘               │
└─────────────────────────────────────────────────────────────────┘

PAGES 2-3: DETAILED RESULTS
- Segment-by-segment analysis
- Geographic breakdown
- Key drivers of beat/miss

PAGES 4-5: METRICS & GUIDANCE
- Margin analysis
- Full-year guidance comparison
- Updated quarterly estimates

PAGES 6-7: THESIS UPDATE
- What's changed
- Risks and catalysts
- Investment recommendation

PAGES 8-10: VALUATION
- Updated DCF/comps if material
- Price target justification
- Scenario analysis

SOURCES SECTION (with clickable hyperlinks):
- Earnings Release: [hyperlink]
- Form 10-Q: [EDGAR hyperlink]
- Earnings Call Transcript: [hyperlink]
- Consensus estimates: Bloomberg as of [date]
```

<a id="quality-checklist"></a>
## 品質チェックリスト

提出前に確認する。
- [ ] 最新四半期の決算データで、古くない。
- [ ] 上振れ・下振れを具体的な数字で定量化。
- [ ] 全図を埋め込み、計8〜12点。
- [ ] クリック可能リンク付き出典節。
- [ ] すべての図表に出典。
- [ ] 会社予想の変更を明確に記載。
- [ ] 格付け・目標株価を冒頭へ。
- [ ] 8〜12ページ、3,000〜5,000語。
