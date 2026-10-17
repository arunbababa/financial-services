---
name: ic-memo
description: Draft a structured investment committee memo for PE deal approval. Synthesizes due diligence findings, financial analysis, and deal terms into a professional IC-ready document. Use when preparing for investment committee, writing up a deal, or creating a formal recommendation. Triggers on "write IC memo", "investment committee memo", "deal write-up", "prepare IC materials", or "recommendation memo".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/private-equity/skills/ic-memo/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：PE案件の承認向けに、デューデリジェンスの発見・財務分析・取引条件を統合した、投資委員会用の構造化メモを作る。委員会準備、案件の文書化、正式な提言に使う。適用表現は "write IC memo"、"investment committee memo"、"deal write-up"、"prepare IC materials"、"recommendation memo"。

<a id="investment-committee-memo"></a>
# 投資委員会メモ

<a id="workflow"></a>
## ワークフロー

<a id="step-1-gather-inputs"></a>
### 手順1：入力を集める

ユーザー、またはセッション内の先行分析から集める。

- 企業概要・事業説明
- 業界・市場の状況
- 過去3〜5年の財務
- 経営陣の評価
- 取引条件（価格・構造・資金調達）
- デューデリジェンスの発見（事業・財務・法務・業務）
- 価値創造計画・100日計画
- リターン分析（基本・上振れ・下振れ）

<a id="step-2-draft-memo-structure"></a>
### 手順2：メモの構成を作る

標準的なICメモの形式：

**I. エグゼクティブサマリー**（1ページ）
- 企業説明、取引の根拠、主要条件
- 提言と主要なリターン
- 上位3リスクと軽減策

**II. 企業概要**（1〜2ページ）
- 事業・製品・サービス
- 顧客基盤と市場開拓の方法
- 競争上の位置
- 経営陣

**III. 業界・市場**（1ページ）
- 規模と成長
- 競争環境
- 長期的トレンド・追い風
- 規制環境

**IV. 財務分析**（2〜3ページ）
- 過去実績（売上・EBITDA・利益率・キャッシュフロー）
- 利益の質に関する調整
- 運転資本分析
- 必要設備投資

**V. 投資判断の根拠**（1ページ）
- 魅力的な理由（3〜5本柱）
- 価値創造の手段（自力成長、利益率拡大、M&A、評価倍率上昇）
- 最初の100日の優先事項

**VI. 取引条件・構造**（1ページ）
- 企業価値と、それが意味する倍率
- 資金調達・使途（Sources & Uses）
- 資本構成・レバレッジ
- 主要な法的条件

**VII. リターン分析**（1ページ）
- 基本・上振れ・下振れシナリオ
- シナリオ別のIRR・MOIC
- リターンを左右する主要前提
- 感度分析

**VIII. リスク要因**（1ページ）
- 深刻さ・発生可能性順の主要リスク
- 各軽減策
- 取引を中止すべきリスク（あれば）

**IX. 提言**
- 明確な提言：実行／見送り／条件付き実行
- 主要条件・次の行動

<a id="step-3-output-format"></a>
### 手順3：出力形式

- 既定：整った体裁のWord文書（.docx）
- 代替：迅速な確認用のMarkdown
- 財務・リターンは文章だけでなく表を含める

<a id="important-notes"></a>
## 重要事項

- 事実に基づき均衡を保ち、強気・弱気の両方を誠実に示す。
- リスクを小さく見せない。委員は結局発見するため、信頼性が重要である。
- 提供された場合は、会社の標準メモひな型を使う。
- 財務表を整合させる。EBITDAブリッジ、S&Uの収支、リターン計算を照合する。
- 取引条件・リターンを推測せず、不足する入力を尋ねる。
