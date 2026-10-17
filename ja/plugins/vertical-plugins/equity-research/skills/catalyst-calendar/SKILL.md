---
name: catalyst-calendar
description: Build and maintain a calendar of upcoming catalysts across a coverage universe — earnings dates, conferences, product launches, regulatory decisions, and macro events. Helps prioritize attention and position ahead of events. Triggers on "catalyst calendar", "upcoming events", "what's coming up", "earnings calendar", "event calendar", or "catalyst tracker".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/equity-research/skills/catalyst-calendar/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：調査対象全体の決算日、会議、製品投入、規制判断、マクロイベントをまとめたカレンダーを作成・維持する。注意を向ける優先度と事前のポジション調整に役立つ。適用表現は "catalyst calendar"、"upcoming events"、"what’s coming up"、"earnings calendar"、"event calendar"、"catalyst tracker"。

<a id="catalyst-calendar"></a>
# 株価変動イベントのカレンダー

<a id="workflow"></a>
## ワークフロー

<a id="step-1-define-coverage-universe"></a>
### 手順1：調査対象を定める

- 追う企業一覧（ティッカー・名称）。
- セクター・業界。
- マクロイベントを含むか（FRB会合、経済指標、規制期限）。
- 期間（今後2週間・1か月・四半期）。

<a id="step-2-gather-catalysts"></a>
### 手順2：イベントを集める

企業ごとに今後の予定を特定する。

**決算・財務イベント**
- 四半期決算日時（市場開始前・終了後）。
- 年次株主総会。
- 投資家・アナリスト説明会。
- 資本市場向け説明会。
- 債務満期・借換え日。

**企業イベント**
- 製品投入・発表。
- FDA承認・規制判断。
- 契約更新・終了。
- M&Aの節目（成立日、規制承認）。
- 経営陣の交代。
- 内部者取引が可能な期間（ロックアップ解除）。

**業界イベント**
- 主要会議（日付・登壇企業）。
- 見本市・展示会。
- 規制意見募集期間・決定。
- 月次売上・客数等の業界データ発表。

**マクロイベント**
- FRB会合（FOMC日程）。
- 雇用統計・CPI・GDP発表。
- ECB・日銀等の政策判断。
- 市場影響のある地政学的イベント。

<a id="step-3-calendar-view"></a>
### 手順3：カレンダー表示

| 日付 | イベント | 企業・セクター | 種類 | 影響（高・中・低） | 当社ポジション | 注記 |
|------|-------|---------------|------|-----------------|----------------|-------|
| | | | 決算／企業／業界／マクロ | | ロング／ショート／中立 | |

<a id="step-4-weekly-preview"></a>
### 手順4：週次プレビュー

毎週、先を見た要約を作る。

**今週の主要イベント：**
1. [曜日]：[企業]Q[X]決算。コンセンサス[$X EPS]、当社予想[$X]、重点[指標]。
2. [曜日]：[イベント]。[銘柄]に重要な理由。
3. [曜日]：[マクロ発表]。期待・ポジション。

**来週の見通し：**
- 今後の重要イベントを早期に知らせる。

**ポジションへの示唆：**
- 特定のポジションを動かし得るイベント。
- 推奨する事前のポジション調整。
- 結果が二分されるイベント前のリスク管理。

<a id="step-5-output"></a>
### 手順5：出力

- カレンダーと並べ替え可能な列を持つExcel。
- 週次プレビューのメール・メモ（Markdown）。
- 任意：Google Calendar連携。

<a id="important-notes"></a>
## 重要事項

- 決算日は変わる。直前に会社IR・Bloomberg・FactSetと照合する。
- 上方・下方の事前発表歴がある会社を追う。
- 会議の参加企業一覧は有用。誰が登壇し、誰が目立って不在か。
- 月次業界データ等の定例イベントは、ひな型を作り自動入力する。
- 赤＝高影響、黄＝中、緑＝通常で色分けする。
- 過去イベントを実際の結果とともに保存し、長期的なパターン認識を育てる。
