---
name: deal-screening
description: Quickly screen inbound deal flow — CIMs, teasers, and broker materials — against the fund's investment criteria. Extracts key deal metrics, runs a pass/fail framework, and outputs a one-page screening memo. Use when reviewing new deal flow, triaging inbound materials, or deciding whether to take a first call. Triggers on "screen this deal", "review this CIM", "should we look at this", "triage this teaser", or "deal screening".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/private-equity/skills/deal-screening/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：持ち込まれたCIM・ティーザー・仲介資料をファンド基準で迅速に選別する。主要指標を抽出し適否を評価して1ページのメモを作る。新案件確認、資料の振り分け、初回通話可否に使う。適用表現は "screen this deal"、"review this CIM"、"should we look at this"、"triage this teaser"、"deal screening"。

<a id="deal-screening"></a>
# 案件のスクリーニング

<a id="workflow"></a>
## ワークフロー

<a id="step-1-extract-deal-facts"></a>
### 手順1：案件の事実を抽出する

提供されたCIM、ティーザー、説明から抽出する。

- **企業：** 名称、所在地、セクター・下位分類。
- **説明：** 何をする企業か、1〜2文。
- **財務：** 売上、EBITDA、利益率、成長率。
- **取引種別：** プラットフォーム、追加買収、資本再構成、少数持分、カーブアウト。
- **希望価格・評価額：** 記載があれば倍率・企業価値。
- **売り手の動機：** 今売る理由。
- **経営陣：** 持分再出資で残るか、退出するか。
- **主要顧客：** 集中リスク。
- **主要リスク：** 明らかな懸念。

<a id="step-2-screen-against-criteria"></a>
### 手順2：基準に照らす

ファンドの投資基準を適用する。不明ならユーザーへ尋ねる。

| 基準 | 目標 | 実際 | 適合・不適合 |
|-----------|--------|--------|-----------|
| 売上範囲 | | | |
| EBITDA範囲 | | | |
| EBITDA利益率 | | | |
| 成長特性 | | | |
| セクター適合 | | | |
| 地域 | | | |
| 案件規模・EV | | | |
| 評価額（EBITDA倍率） | | | |
| 顧客集中 | | | |
| 経営継続性 | | | |

<a id="step-3-quick-assessment"></a>
### 手順3：迅速な評価

3部構成の評価を示す。

1. **判定：** Pass / Further Diligence（追加調査） / Hard Pass（明確な見送り）。
2. **強気の見方**（2〜3箇条）：よい案件になり得る理由。
3. **弱気の見方**（2〜3箇条）：主要リスク・懸念。
4. **主要な問い：** 初回通話で答えが必要なこと。

<a id="step-4-output"></a>
### 手順4：出力

パートナーへの共有やICの初期選別に使う、1ページのスクリーニングメモ。

<a id="important-notes"></a>
## 重要事項

- 速度が大切。数時間でなく数分で行う。
- 懸念は率直に述べ、埋もれさせない。
- 財務が不整合・不完全に見えたら明示する。
- 初回の選別なら、ファンドの基準を最初に尋ねる。
- 基準が確認されたら、今後の案件のため記憶へ保存する。
