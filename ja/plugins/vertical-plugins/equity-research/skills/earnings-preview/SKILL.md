---
name: earnings-preview
description: Build pre-earnings analysis with estimate models, scenario frameworks, and key metrics to watch. Use before a company reports quarterly earnings to prepare positioning notes, set up bull/bear scenarios, and identify what will move the stock. Triggers on "earnings preview", "what to watch for [company] earnings", "pre-earnings", "earnings setup", or "preview Q[X] for [company]".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/equity-research/skills/earnings-preview/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：予想モデル、シナリオ、注目指標で決算発表前分析を作る。四半期決算前のポジション検討、強気・弱気シナリオ、株価を動かす要因の特定に使う。適用表現は "earnings preview"、"what to watch for [company] earnings"、"pre-earnings"、"earnings setup"、"preview Q[X] for [company]"。

<a id="earnings-preview"></a>
# 決算発表前プレビュー

<a id="workflow"></a>
## ワークフロー

<a id="step-1-gather-context"></a>
### 手順1：背景を集める

- 企業と報告四半期を特定する。
- Web検索でコンセンサス予想（売上・EPS・主要セグメント指標）を取得する。
- 決算発表日時（市場開始前・終了後）を調べる。
- 前四半期の決算説明会から、会社予想・コメントを確認する。

<a id="step-2-key-metrics-framework"></a>
### 手順2：主要指標の枠組み

その企業固有の「注目点」を作る。

**財務指標：**
- 売上対コンセンサス（全体・セグメント別）。
- EPS対コンセンサス。
- 粗利益率・営業利益率・純利益率は拡大か縮小か。
- フリーキャッシュフロー。
- 将来の会社予想対コンセンサス。

**業務指標（セクター別）：**
- 技術・SaaS：ARR、純収益継続率、RPO、顧客数。
- 小売：既存店売上、客数、1回当たり購入額。
- 製造業等：受注残、受注売上比率、価格対数量。
- 金融：NIM、信用の質、貸出成長、手数料収入。
- 医療：処方件数、患者数、開発パイプライン更新。

<a id="step-3-scenario-analysis"></a>
### 手順3：シナリオ分析

株価への示唆を付け、3シナリオを作る。

| シナリオ | 売上 | EPS | 主要要因 | 株価反応 |
|----------|---------|-----|------------|----------------|
| 強気 | | | | |
| 基本 | | | | |
| 弱気 | | | | |

各シナリオについて：
- 業務上、何が起こる必要があるか。
- どの経営陣コメントが兆候になるか。
- 過去の類似決算で株価がどう動いたか。

<a id="step-4-catalyst-checklist"></a>
### 手順4：株価を動かす要因のチェックリスト

反応を決める3〜5事項を特定する。

1. [指標] 対 [コンセンサス・非公式な期待値]：重要な理由。
2. [会社予想項目]：運用側が聞きたいこと。
3. [見方の変化]：戦略変更、M&A、再編など。

<a id="step-5-output"></a>
### 手順5：出力

1ページに次を含める。
- 企業・四半期・発表日。
- コンセンサス表。
- 重要度順の注目指標。
- 強気・基本・弱気表。
- 株価変動要因のチェックリスト。
- 取引前提：直近株価実績、オプションが織り込む変動幅。

<a id="important-notes"></a>
## 重要事項

- コンセンサスは変わる。必ず情報源・予想日を記す。
- 運用側調査の非公式な期待値（whisper numbers）は、公表コンセンサス以上に重要なことが多い。
- 過去の反応で期待を調整する。"[company] earnings reaction history" を検索する。
- オプションの織り込み変動幅は市場期待を示す。自分のシナリオと比べる。
