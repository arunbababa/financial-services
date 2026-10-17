---
name: returns-analysis
description: Build quick IRR/MOIC sensitivity tables for PE deal evaluation. Models returns across entry multiple, leverage, exit multiple, growth, and hold period scenarios. Use when sizing up a deal, stress-testing assumptions, or preparing IC returns exhibits. Triggers on "returns analysis", "IRR sensitivity", "MOIC table", "what's the return at", "model the returns", or "back of the envelope".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/private-equity/skills/returns-analysis/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：PE案件評価のためIRR・MOIC感度分析表を迅速に作る。取得倍率、レバレッジ、売却倍率、成長、保有期間を変えてリターンをモデル化する。案件評価、前提のストレステスト、ICのリターン資料に使う。適用表現は "returns analysis"、"IRR sensitivity"、"MOIC table"、"what’s the return at"、"model the returns"、"back of the envelope"。

<a id="returns-analysis"></a>
# 投資リターン分析

<a id="workflow"></a>
## ワークフロー

<a id="step-1-gather-deal-inputs"></a>
### 手順1：取引の入力を集める

ユーザーへ尋ねるか、先行分析から取得する。

**取得時：**
- 取得時EBITDA（LTM・NTM）
- 取得時倍率（EV / EBITDA）
- 企業価値
- クロージング時の純有利子負債
- エクイティ投資額
- 取引手数料・費用

**資金調達：**
- シニア債務（EBITDA倍率、金利、返済）
- 劣後債務・メザニン（あれば）
- 取得時の総レバレッジ（EBITDA倍率）
- エクイティ出資

**事業前提：**
- 年間売上成長率
- EBITDA利益率の推移
- 売上に対する設備投資比率
- 運転資本の変化
- 債務返済予定

**売却時：**
- 保有期間（年）
- 売却時倍率（EV / EBITDA）
- 売却時EBITDA（成長前提から計算）

<a id="step-2-base-case-returns"></a>
### 手順2：基本シナリオのリターン

次を計算する。

| 指標 | 値 |
|--------|-------|
| 取得時EV | |
| エクイティ投資額 | |
| 売却時EBITDA | |
| 売却時EV | |
| 売却時純有利子負債 | |
| 売却時エクイティ価値 | |
| **MOIC** | |
| **IRR** | |
| キャッシュ・オン・キャッシュ | |

リターンのウォーターフォールを示す。
- EBITDA成長の寄与
- 倍率上昇・低下の寄与
- 債務返済の寄与
- 手数料・費用による減少

<a id="step-3-sensitivity-tables"></a>
### 手順3：感度分析表

2変数の感度分析表を作る。

**取得時倍率 対 売却時倍率**
| | 売却6倍 | 売却7倍 | 売却8倍 | 売却9倍 | 売却10倍 |
|---|---------|---------|---------|---------|----------|
| 取得7倍 | | | | | |
| 取得8倍 | | | | | |
| 取得9倍 | | | | | |
| 取得10倍 | | | | | |

**EBITDA成長 対 売却時倍率**（取得時条件を固定）

**レバレッジ 対 売却時倍率**（取得時条件・成長を固定）

**保有期間 対 売却時倍率**

各セルにIRRとMOICの両方を、IRR / MOIC形式で示す。

<a id="step-4-scenario-analysis"></a>
### 手順4：シナリオ分析

3シナリオを作る。

| | 強気 | 基本 | 弱気 |
|---|------|------|------|
| 売上CAGR | | | |
| 売却時EBITDA利益率 | | | |
| 売却時倍率 | | | |
| 売却時EBITDA | | | |
| MOIC | | | |
| IRR | | | |

<a id="step-5-output"></a>
### 手順5：出力

- Excelワークブック：
  - 前提タブ
  - リターン計算
  - 条件付きの色付けを施した感度分析表
  - シナリオ概要
- ICスライドに使える1ページのリターン要約

<a id="key-formulas"></a>
## 主要数式

- **MOIC** = Exit Equity Value / Equity Invested（売却時エクイティ価値 / エクイティ投資額）
- **IRR** = solve for r: Equity Invested × (1 + r)^n = Exit Equity Value (adjust for interim cash flows)（途中キャッシュフローを調整し、左式のrを解く）
- **リターンの要因分解：**
  - Growth: (Exit EBITDA - Entry EBITDA) × Exit Multiple / Equity（成長寄与）
  - Multiple: (Exit Multiple - Entry Multiple) × Entry EBITDA / Equity（倍率寄与）
  - Leverage: Debt paydown over hold period / Equity（保有中の債務返済による寄与）

<a id="important-notes"></a>
## 重要事項

- 該当する場合、手数料・成功報酬控除前と控除後の両方を必ず示す。
- 経営陣の持分再出資・共同投資で必要エクイティが変わる。関連するか尋ねる。
- 配当目的の借換え・途中分配はIRRに大きく影響するため、予定があれば含める。
- 取引費用（通常EVの2〜4%）を忘れない。初日のエクイティ価値を減らす。
- 資産・株式取引の違い、338(h)(10)選択などの税務条件は、税引後リターンへ大きく影響し得る。
