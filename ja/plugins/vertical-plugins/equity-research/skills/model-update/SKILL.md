---
name: model-update
description: Update financial models with new data — quarterly earnings, management guidance, macro changes, or revised assumptions. Adjusts estimates, recalculates valuation, and flags material changes. Use after earnings, guidance updates, or when assumptions need refreshing. Triggers on "update model", "plug earnings", "refresh estimates", "update numbers for [company]", "new guidance", or "revise estimates".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/equity-research/skills/model-update/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：四半期決算、会社予想、マクロ変化、前提修正で財務モデルを更新し、予想調整・評価再計算・重要変更の警告を行う。決算後、会社予想更新後、前提見直し時に使う。適用表現は "update model"、"plug earnings"、"refresh estimates"、"update numbers for [company]"、"new guidance"、"revise estimates"。

<a id="model-update"></a>
# 財務モデルの更新

<a id="workflow"></a>
## ワークフロー

<a id="step-1-identify-what-changed"></a>
### 手順1：変更点を特定する

更新のきっかけを定める。
- **決算発表：** 入力すべき新四半期実績。
- **会社予想変更：** 将来見通しの更新。
- **予想修正：** 新データによるアナリストの前提変更。
- **マクロ更新：** 金利・為替・商品価格の変化。
- **イベント：** M&A、再編、新製品、経営陣変更。

<a id="step-2-plug-new-data"></a>
### 手順2：新データを入れる

<a id="after-earnings"></a>
#### 決算後

公表実績を反映する。

| 項目 | 旧予想 | 実績 | 差分 | 注記 |
|-----------|---------------|--------|-------|-------|
| 売上 | | | | |
| 粗利益率 | | | | |
| 営業費用 | | | | |
| EBITDA | | | | |
| EPS | | | | |
| [主要指標1] | | | | |
| [主要指標2] | | | | |

**セグメント詳細（該当時）：**
- 各セグメントの売上・利益率を更新する。
- 構成変化を記す。

**貸借対照表・キャッシュフロー：**
- 現金・債務残高。
- 株数（自社株買い・希薄化）。
- 設備投資の実績対予想。
- 運転資本の変化。

<a id="step-3-revise-forward-estimates"></a>
### 手順3：将来予想を修正する

新データに基づき調整する。

| | 旧当期予想 | 新当期予想 | 変化 | 旧翌期予想 | 新翌期予想 | 変化 |
|---|-----------|-----------|--------|------------|------------|--------|
| 売上 | | | | | | |
| EBITDA | | | | | | |
| EPS | | | | | | |

**主要前提の変更：**
- 何を、なぜ変えるか。
- 売上成長率：旧 → 新（理由）。
- 利益率：旧 → 新（理由）。
- 新項目（再編費用、一時利益等）。

<a id="step-4-valuation-impact"></a>
### 手順4：評価額への影響

更新予想で再計算する。

| 評価方法 | 旧 | 更新後 | 変化 |
|-----------------|-------|---------|--------|
| DCF適正価値 | | | |
| PER（NTM EPS × 目標倍率） | | | |
| EV/EBITDA（NTM EBITDA × 目標倍率） | | | |
| **目標株価** | | | |

<a id="step-5-summary--action"></a>
### 手順5：要約と対応

**予想変更の要約：**
- 変更内容・理由・株価への意味を1段落。
- 投資判断の根拠が変わる出来事か、雑音か。

**格付け・目標株価：**
- 維持か変更か。
- 変更するなら、新目標と方法。
- 現在株価からの上昇・下落余地。

<a id="step-6-output"></a>
### 手順6：出力

- 既存モデルが提供されれば、更新したExcel。
- 予想変更要約（Markdown・Word）。
- 更新した目標株価の算定根拠。

<a id="important-notes"></a>
## 重要事項

- 将来予測前に必ず自分の予想を会社の公表値と照合する。
- 非反復項目と、GAAP・調整後のどちらの予想かを明記する。
- 分析の変遷が分かるよう予想修正履歴を追う。
- 一時的な要因が多い四半期なら、修正時に兆候と雑音を分ける。
- 更新後にコンセンサスと比べる。市場の予想との差はどうか。
- 株数は重要。株式報酬・転換証券・自社株買いによる変化はEPSに大きく影響し得る。
