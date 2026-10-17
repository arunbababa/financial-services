# 個人設定サンプルの日本語対訳

原本：[plugins/vertical-plugins/investment-banking/.claude/investment-banking.local.md.example](../../../../../plugins/vertical-plugins/investment-banking/.claude/investment-banking.local.md.example)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。以下のコードブロックは原本L1–83と1行ずつ対応する読解用の全訳です。原本や実行用設定は変更していません。氏名・会社名等は例示のプレースホルダーで、ユーザー本人の情報ではありません。日付・金額・識別子・数式は原表記を保持しています。

## L1–83（全体）

```text
---
# 投資銀行プラグインの設定
# このファイルを.claude/investment-banking.local.mdへコピーしてカスタマイズする

# 自分の情報
name: "自分の氏名"
title: "バイスプレジデント"
group: "テクノロジー分野のM&A"
firm: "自社名"
email_signature: |
  よろしくお願いいたします。
  [自分の氏名]
  [役職] | [所属グループ]
  [会社名]
  [電話番号]

# 調査・担当対象の重点領域
sectors:
  - "企業向けソフトウェア"
  - "フィンテック"
  - "サイバーセキュリティ"
verticals:
  - "B2B SaaS"
  - "インフラストラクチャ"
  - "AI/ML"

# 案件の条件
typical_deal_size_range: "$50M - $500M"
transaction_types:
  - "売り手側のM&A"
  - "買い手側のM&A"
  - "資金調達"
  - "戦略的アドバイザリー"

# 進行中の案件（セッションでのリマインダー用）
active_mandates:
  - name: "Project Alpine"
    type: "売り手側のM&A"
    stage: "買い手候補への案内・打診"
    next_milestone: "経営陣による説明会"
    date: "2024-01-20"
  - name: "Project Summit"
    type: "買い手側"
    stage: "デューデリジェンス"
    next_milestone: "修正版のLOI（意向表明書）の提出"
    date: "2024-01-18"

# 対象企業の追跡
priority_targets:
  - company: "Target Corp"
    rationale: "顧客Xにとっての戦略的な適合性"
    status: "初期のアプローチ"
  - company: "Growth Co"
    rationale: "事業基盤となるプラットフォーム企業の買収候補"
    status: "関係構築中"

# 評価の既定値
default_valuation_methodologies:
  - "類似企業比較"
  - "類似取引事例比較"
  - "DCF"
comps_multiples:
  - "EV/Revenue"
  - "EV/EBITDA"
  - "EV/ARR"
---

# メモ

案件固有のメモ、市場情報、関係者との関係の背景をここへ追加する。

## 市場のテーマ
- [テーマ1]: [案件への影響]
- [テーマ2]: [案件への影響]

## 重要な関係者
- [担当者名] @ [会社名]: [背景・文脈]
- [担当者名] @ [会社名]: [背景・文脈]

## 最近の類似取引事例
| 対象企業 | 買収企業 | 取引価値 | 倍率 | 日付 |
|--------|----------|-------|----------|------|
| [会社名] | [買い手] | [$XXM] | [X.Xx] | [日付] |
```

原文のVice Presidentは投資銀行の職位として「バイスプレジデント」と訳しています。企業一般の副社長と断定していません。Marketingは案件の買い手候補への案内・打診段階、platform acquisitionは投資・買収の事業基盤となる企業の取得という文脈です。LOIはLetter of Intent（意向表明書）です。
