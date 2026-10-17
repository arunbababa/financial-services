---
name: portfolio-monitoring
description: Track and analyze portfolio company performance against plan. Ingests monthly/quarterly financial packages (Excel, PDF), extracts KPIs, flags variances to budget, and produces summary dashboards. Use when reviewing portfolio company financials, preparing board materials, or monitoring covenant compliance. Triggers on "review portfolio company", "monthly financials", "how is [company] performing", "covenant check", or "portfolio update".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/valuation-reviewer/skills/portfolio-monitoring/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：月次・四半期財務資料（Excel・PDF）からKPIを抽出し、予算差異を警告し、計画に対する投資先実績を追跡・分析して概要ダッシュボードを作る。財務レビュー、取締役会資料、財務制限条項の監視に使う。適用表現は "review portfolio company"、"monthly financials"、"how is [company] performing"、"covenant check"、"portfolio update"。

<a id="portfolio-monitoring"></a>
# 投資先企業のモニタリング

<a id="workflow"></a>
## ワークフロー

<a id="step-1-ingest-financial-package"></a>
### 手順1：財務資料を取り込む

- ユーザーの投資先企業の財務資料（Excel、PDF、CSV）を受け取る。
- 売上、EBITDA、現金残高、借入残高、設備投資、運転資本を抽出する。
- 報告期間を特定し、前期および予算・計画と比べる。

<a id="step-2-kpi-extraction--variance-analysis"></a>
### 手順2：KPI抽出・差異分析

主要指標はセクターに合わせる。

**財務KPI：**
- 売上の予算比（金額・%）
- EBITDA・EBITDA利益率の予算比
- 現金残高・純有利子負債
- レバレッジ比率（純有利子負債 / LTM EBITDA）
- インタレスト・カバレッジ比率
- 設備投資の予算比
- フリーキャッシュフロー

**業務KPI**（ユーザーへ尋ねるか、データから推定）：
- 顧客数・顧客当たり売上
- 従業員数・従業員当たり売上
- 受注残・商談パイプライン
- 解約率・継続率

<a id="step-3-flag--summarize"></a>
### 手順3：警告と要約

- **緑：** 計画との差が5%以内。
- **黄：** 計画を5〜15%下回る。議論対象として示す。
- **赤：** 計画を15%超下回る、または財務制限条項への抵触リスク。即時対応。

簡潔に出力する。
1. 1段落の概要（「X社は計画を上回る／下回る／計画どおりに進んでいる……」）
2. 実績・予算・前期を並べたKPI表
3. 背景を付けた赤・黄の警告
4. 財務制限条項の順守状況（該当する場合）
5. 経営陣への質問

<a id="step-4-trend-analysis"></a>
### 手順4：トレンド分析

複数期間がある場合：
- 売上・EBITDA・現金等の推移を図示する。
- 加速・減速・安定の傾向を特定する。
- 投資審査時の事業計画と比べる。

<a id="important-notes"></a>
## 重要事項

- 比較する予算・計画がなければ必ず求める。
- セクター固有KPIを決めつけず、その会社で重要なものを尋ねる。
- 財務制限条項の水準が不明なら、融資契約条件をユーザーへ尋ねる。
- 取締役会に提出できる、簡潔・事実中心で余分な文のない出力にする。
