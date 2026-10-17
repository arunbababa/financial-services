---
description: Create a one-page company strip profile using branded PPT template
argument-hint: "[company name or ticker]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/investment-banking/commands/one-pager.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：ブランドの PPT テンプレートを使用して 1 ページの会社概要プロフィールを作成する

<a id="one-pager-strip-profile-command"></a>
# 概要資料ストリップ プロファイル コマンド

ピッチブックや取引資料用に、プロフェッショナルな 1 ページの会社概要を作成します。

<a id="workflow"></a>
## ワークフロー

<a id="step-1-gather-company-information"></a>
### ステップ 1: 会社情報を収集する

会社名またはティッカーが提供されている場合は、それを使用します。それ以外の場合は次のように尋ねてください。
- 「どの企業について紹介したいですか?」

<a id="step-2-check-for-available-ppt-template-skills"></a>
### ステップ 2: 利用可能な PPT テンプレート スキルを確認する

**最初に、スキル ディレクトリにある既存の ppt テンプレート スキル**を確認します。

```bash
ls skills/ | grep -E "ppt-template|brand-guidelines"
```

テンプレート スキルが存在する場合 (例: `techcorp-ppt-template`、`gs-brand-guidelines`):
1. 利用可能なテンプレートをユーザーにリスト表示します
2. どのテンプレートを使用するか、またはきれいなプロフェッショナルなフォーマットが必要かどうかを尋ねます
3. 選択したテンプレート スキルを `skill: "[template-name]"` でロードします

テンプレート スキルが存在しない場合は、次のように尋ねます。
- 「使用するブランドの PowerPoint テンプレート ファイルはありますか? ある場合は、パスを指定してください。そうでない場合は、クリーンなプロフェッショナル フォーマットを使用します。」

テンプレート ファイルが提供されている場合:
1. テンプレートの構造を分析してレイアウトを理解する
2. 概要資料コンテンツに適切なレイアウトを使用する

<a id="step-3-load-strip-profile-skill"></a>
### ステップ 3: ストリップ プロファイル スキルのロード

`skill: "strip-profile"` を使用してプロファイルの作成を実行します。

1. **要件を明確にする**:
   - 1 枚のスライド形式 (概要資料) を確認する
   - 具体的な重点分野について質問する

2. **会社のデータを調査する**:
   - 会社概要（本社、設立、従業員、リーダーシップ）
   - 事業内容と位置付け
   - 主要な財務（収益、EBITDA、利益率、成長）
   - 評価指標 (時価総額、EV、マルチプル)
   - 最近の動向とニュース
   - 大株主（上場企業の場合）

3. **ストリッププロファイルを作成します**:
   - アスペクト比 4:3 を使用します (10 インチ x 7.5 インチ)。
   - 4象限レイアウト:
     - 左上: 会社概要 (箇条書き)
     - 右上: ビジネスとポジショニング (箇条書き)
     - 左下: 主要財務（表）
     - 右下: 株価チャート + 株主 OR 最近のニュース
   - 企業のブランドカラーを適用する
   - セクションヘッダーにアクセントバーを含める

<a id="step-4-visual-review"></a>
### ステップ 4: 視覚的なレビュー

スライドを作成した後:
1. レビュー用に画像に変換する
2. テキストの重なり/切れの問題をチェックする
3. すべてのデータが入力されていることを確認します (プレースホルダーがない)
4. 承認のためにユーザーにプレビューを表示する

<a id="step-5-deliver-output"></a>
### ステップ 5: 出力を提供する

以下を提供します:
1. **PowerPoint ファイル** (.pptx) - 概要資料
2. **画像プレビュー** - 簡単なレビュー用
3. 主要なデータポイントの**概要**が含まれています

<a id="one-pager-layout-reference"></a>
## 概要資料のレイアウト リファレンス

```
┌─────────────────────────────────────────────────────────────────┐
│ Company Name (TICKER)                                    [Logo] │
├────────────────────────────┬────────────────────────────────────┤
│ COMPANY OVERVIEW           │ BUSINESS & POSITIONING             │
│ • HQ, Founded, Employees   │ • Core business description        │
│ • CEO, CFO                 │ • Key products/services            │
│ • Market cap, industry     │ • Competitive positioning          │
│ • Key stats                │ • Growth drivers                   │
├────────────────────────────┼────────────────────────────────────┤
│ KEY FINANCIALS             │ STOCK PERFORMANCE / OWNERSHIP      │
│ ┌──────────────────────┐   │ [1Y Stock Chart]                   │
│ │ Metric │ FY24 │ FY25E│   │                                    │
│ │ Rev    │ $XXB │ $XXB │   │ Top Shareholders:                  │
│ │ EBITDA │ $XXB │ $XXB │   │ • Vanguard: X.X%                   │
│ │ Margin │ XX%  │ XX%  │   │ • BlackRock: X.X%                  │
│ │ EV/EBITDA │ XXx │ XXx │   │ • State Street: X.X%              │
│ └──────────────────────┘   │                                    │
└────────────────────────────┴────────────────────────────────────┘
Source: Company filings, FactSet
```

<a id="quality-checklist"></a>
## 品質チェックリスト

納品前：
- [ ] 4 つの象限すべてに実際のデータが入力される
- [ ] プレースホルダーテキストは残りません
- [ ] 対象企業のブランドカラーを適用
- [ ] すべてのセクションヘッダーのアクセントバー
- [ ] 財務表が適切にフォーマットされている
- [ ] 出典は下部に記載
- [ ] テキストのオーバーフローや切れはありません
- [ ] 投資銀行品質（GS/MS/JPM基準）
