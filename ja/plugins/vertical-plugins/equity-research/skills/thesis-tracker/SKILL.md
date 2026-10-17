---
name: thesis-tracker
description: Maintain and update investment theses for portfolio positions and watchlist names. Track key data points, catalysts, and thesis milestones over time. Use when updating a thesis with new information, reviewing position rationale, or checking if a thesis is still intact. Triggers on "update thesis for [company]", "is my thesis still intact", "thesis check", "add data point to [company]", or "review my positions".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/equity-research/skills/thesis-tracker/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：保有ポジション・監視銘柄の投資判断の根拠を維持・更新し、主要情報、きっかけ、仮説の節目を追跡する。新情報の反映、ポジションの理由の見直し、根拠が維持されるかの確認に使う。適用表現は "update thesis for [company]"、"is my thesis still intact"、"thesis check"、"add data point to [company]"、"review my positions"。

<a id="thesis-tracker"></a>
# 投資判断の根拠の追跡

<a id="workflow"></a>
## ワークフロー

<a id="step-1-define-or-load-thesis"></a>
### 手順1：根拠を定義・読み込む

新規作成では：
- **企業：** 名称・ティッカー。
- **ポジション：** ロング・ショート。
- **主張：** 中核の根拠を1〜2文（例「ACMEをロング。ソフトウェアへの構成変化に伴う価格決定力と営業レバレッジで利益率が拡大」）。
- **柱：** 3〜5の支持論拠。
- **リスク：** 根拠を無効にする3〜5のリスク。
- **きっかけ：** 裏付け・反証になる決算、製品投入、規制判断等。
- **目標株価・評価：** 主張が実現した場合の価値。
- **損切り条件：** 撤退する理由。

既存の更新なら、新情報・動向をユーザーへ尋ねる。

<a id="step-2-update-log"></a>
### 手順2：更新記録

各新情報・動向について：

- **日付：** 発生時。
- **情報：** 変化（決算上振れ、経営陣退職、競合行動等）。
- **根拠への影響：** 特定の柱を強める・弱める・中立化するか。
- **行動：** 変更なし／増加／縮小／撤退。
- **更新後確信度：** 高／中／低。

<a id="step-3-thesis-scorecard"></a>
### 手順3：評価表

継続的に維持する。

| 柱 | 当初の期待 | 現状 | 傾向 |
|--------|---------------------|----------------|-------|
| 売上成長 >20% | 順調 | Q3は22% | 安定 |
| 利益率拡大 | 遅れ | 前年比横ばい | 懸念 |
| 新製品投入 | 未了 | Q2へ遅延 | 注視 |

<a id="step-4-catalyst-calendar"></a>
### 手順4：イベントカレンダー

今後の株価変動要因を追う。

| 日付 | イベント | 予想影響 | 注記 |
|------|-------|-----------------|-------|
| | | | |

<a id="step-5-output"></a>
### 手順5：出力

次に使える根拠の要約：
- 朝の会議。
- ポートフォリオレビュー。
- リスク委員会への説明。

簡潔なMarkdown・Wordで、評価表、最近の更新、現在の確信度を含める。

<a id="important-notes"></a>
## 重要事項

- 反証可能でなければならない。何をもっても反証できないなら仮説ではない。
- 支持する証拠と同じ厳密さで、否定する証拠を追う。
- 大きな出来事がなくても、最低四半期ごとに見直す。
- 複数ポジションを運用するなら、全体の根拠レビューを提案する。
- セッションをまたいで参照できる構造化形式でデータを保存する。
