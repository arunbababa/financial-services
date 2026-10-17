---
name: unit-economics
description: Analyze unit economics for PE targets — ARR cohorts, LTV/CAC, net retention, payback periods, revenue quality, and margin waterfall. Essential for software/SaaS, recurring revenue, and subscription businesses. Use when evaluating revenue quality, building a cohort analysis, or assessing customer economics. Triggers on "unit economics", "cohort analysis", "ARR analysis", "LTV CAC", "net retention", "revenue quality", or "customer economics".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/private-equity/skills/unit-economics/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：PE対象企業のARRコホート、LTV/CAC、純収益継続率、回収期間、売上の質、利益のウォーターフォールを分析する。ソフトウェア・SaaS・継続課金で重要。売上品質、コホート、顧客採算を評価するときに使う。適用表現は "unit economics"、"cohort analysis"、"ARR analysis"、"LTV CAC"、"net retention"、"revenue quality"、"customer economics"。

<a id="unit-economics-analysis"></a>
# ユニットエコノミクス分析

<a id="workflow"></a>
## ワークフロー

<a id="step-1-identify-business-model"></a>
### 手順1：事業モデルを特定する

売上モデルに合わせて分析する。
- **SaaS・サブスクリプション：** ARR、純収益継続率、コホート。
- **継続サービス：** 契約価値、更新率、アップセル。
- **取引・従量課金：** 取引当たり売上、数量推移、手数料率。
- **混合型：** 売上源別に分解。

<a id="step-2-core-metrics"></a>
### 手順2：主要指標

<a id="arr--revenue-quality"></a>
#### ARR・売上の質
- **ARRブリッジ：** 期首ARR → 新規 → 拡大 → 縮小 → 解約 → 期末ARR。
- **コホート別ARR：** 獲得年別の集団がどう継続・成長するか。
- **売上集中：** 上位10・20・50顧客の全体比。
- **売上種別：** 継続・非継続・専門サービス。
- **契約構造：** ACV分布、複数年契約比率、自動更新比率。

<a id="customer-economics"></a>
#### 顧客単位の採算
- **CAC（顧客獲得費用）：** Total S&M spend / new customers acquired（営業・マーケティング総費用 / 新規顧客数）。
- **LTV（生涯価値）：** (ARPU × Gross Margin) / Churn Rate（ARPU × 粗利益率 / 解約率）。
- **LTV:CAC：** 健全な事業の目標は3倍超。
- **CAC回収期間：** 獲得費用の回収月数。
- **混合値と区分別：** 大企業・中小・中堅の顧客セグメントへ分解する。

<a id="retention--expansion"></a>
#### 継続・拡大
- **グロス継続率：** 拡大を除いた、期首ARRの維持比率。
- **純収益継続率（NDR）：** 拡大を含む期首ARRの維持比率。
- **顧客数解約率：** 失った顧客の比率。
- **売上解約率：** 失った売上の比率。顧客数解約率とは異なることが多い。
- **拡大率：** アップセル＋クロスセルの期首ARR比。

<a id="cohort-analysis"></a>
#### コホート分析

次の表を作る。

| コホート | 0年目 | 1年目 | 2年目 | 3年目 | 4年目 |
|--------|--------|--------|--------|--------|--------|
| 2020 | $1.0M | $1.1M | $1.2M | $1.1M | |
| 2021 | $1.5M | $1.7M | $1.8M | | |
| 2022 | $2.0M | $2.3M | | | |
| 2023 | $3.0M | | | | |

ドル絶対額と、0年目=100%の指数の両方を示す。

<a id="margin-waterfall"></a>
#### 利益のウォーターフォール
- 売上 → 粗利益 → 限界利益 → EBITDA。
- 総費用込みの単位採算：顧客の獲得・提供・維持にいくらかかるか。
- 売上源別の粗利益率（サブスクリプション・サービス・その他）。

<a id="step-3-benchmarking"></a>
### 手順3：ベンチマーク比較

関連する基準と比べる。
- **SaaSの40%ルール：** 成長率＋EBITDA利益率 > 40%。
- **SaaS Magic Number：** Net new ARR / prior period S&M spend > 0.75x（純増ARR / 前期営業・マーケティング費 > 0.75倍）。
- **NDR：** 最高水準 >120%、良好 >110%、懸念 <100%。
- **LTV:CAC：** 最高水準 >5倍、良好 >3倍、懸念 <2倍。
- **グロス継続率：** 最高水準 >95%、良好 >90%、懸念 <85%。
- **CAC回収：** 最高水準 <12か月、良好 <18か月、懸念 >24か月。

<a id="step-4-revenue-quality-score"></a>
### 手順4：売上の質の採点

評価を統合する。

| 要素 | 点数（1〜5） | 注記 |
|--------|-------------|-------|
| 継続売上比率 | | |
| 純収益継続率 | | |
| 顧客集中 | | |
| コホートの安定性 | | |
| 成長の持続性 | | |
| 利益率の特性 | | |
| **総合** | | |

<a id="step-5-output"></a>
### 手順5：出力

- ARRブリッジ、コホート表、単位採算ダッシュボードを含むExcel。
- 主要指標・基準を示す概要スライド。
- 懸念と追加調査領域。

<a id="important-notes"></a>
## 重要事項

- あれば必ず生の顧客別データを求める。集計指標は問題を隠し得る。
- 拡大が強ければ、NDR100%超でも高いグロス解約を隠し得る。両方を必ず示す。
- コホート分析は売上の質で最重要。データ提供を求める。
- 契約上のARRと実際の認識売上を分ける。
- 従量課金では従来型ARR指標より消費量推移・拡大パターンを重視する。
- 専門サービス売上は別に評価する。継続的でなく、通常は利益率も低い。
