---
name: morning-note
description: Draft concise morning meeting notes summarizing overnight developments, trade ideas, and key events for coverage stocks. Designed for the 7am morning meeting format — tight, opinionated, actionable. Triggers on "morning note", "morning meeting", "what happened overnight", "trade idea", "morning call prep", or "daily note".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/equity-research/skills/morning-note/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：対象銘柄の夜間動向、取引案、主要イベントをまとめた簡潔な朝の会議メモを作る。午前7時の会議向けに短く、見解と行動を明確にする。適用表現は "morning note"、"morning meeting"、"what happened overnight"、"trade idea"、"morning call prep"、"daily note"。

<a id="morning-note"></a>
# 朝の会議用メモ

<a id="workflow"></a>
## ワークフロー

<a id="step-1-overnight-developments"></a>
### 手順1：夜間の動向

調査対象銘柄全体の関連イベントを調べる。

**決算・会社予想**
- 夜間・市場開始前に発表した対象企業。
- 売上・EPS・主要指標の予想上振れ・下振れ。
- 会社予想の引上げ・引下げ・維持。

**ニュース・イベント**
- M&A発表・観測。
- 経営陣変更。
- 製品投入・規制判断。
- 他社アナリストの格上げ・格下げ。
- セクターへ影響するマクロデータ・政策変更。

**市場背景**
- 夜間先物・市場開始前の動き。
- セクターETFの実績。
- 関連する商品・為替の動き。
- 本日の重要経済指標発表。

<a id="step-2-morning-note-format"></a>
### 手順2：メモの形式

2分で読めるよう簡潔にする。

---

**[日付] 朝のメモ — [アナリスト名]**
**[担当セクター]**

**最重要の見解：[見出し — PMが聞くべき1つのこと]**
- 重要な動向と理由、2〜3文。
- 株価影響：目標株価、格付け維持・変更。

**夜間・市場開始前の動向**
- [企業A]：決算・ニュースの1行要約＋当社の見方。
- [企業B]：1行要約＋当社の見方。
- [セクター・マクロ]：関連するセクター全体の動向。

**本日の主要イベント**
- [時刻]：[企業]決算説明会。
- [時刻]：経済指標発表（期待対当社見解）。
- [時刻]：会議・投資家向け説明会。

**取引案**（あれば）
- [ロング／ショート] [企業]：1〜2文の根拠＋きっかけ。
- リスク：何があれば見方が誤りとなるか。

---

<a id="step-3-quick-takes-on-earnings"></a>
### 手順3：決算の速報見解

対象企業が発表した場合：

| 指標 | コンセンサス | 実績 | 上振れ・下振れ |
|--------|-----------|--------|-----------|
| 売上 | | | |
| EPS | | | |
| [主要指標] | | | |
| 会社予想 | | | |

**当社の見方：** 株価によいか悪いか、投資判断の根拠が変わるかを2〜3文。

**行動：** 格付け維持・格上げ・格下げか。目標株価を変えるか。

<a id="step-4-output"></a>
### 手順4：出力

- メール・Slack配布用Markdown。
- 正式な配布ならWord。
- 最大1ページ。PM・トレーダーはそれ以上読まない。

<a id="important-notes"></a>
## 重要事項

- 見解を示す。ニュースの要約だけでは役に立たない。
- 最重要事項を先に示し、見出しを埋もれさせない。
- 「ニュースなし」も有効。「夜間に重要事項なし、ポジション維持」と述べる。
- 行動に関わる決算・M&Aと、軽微なアナリストメモ等の雑音を分ける。
- 見解に時刻を付ける。午前6時執筆なら、開始までに市場開始前状況が変わると記す。
- 誤ったら翌朝のメモで認める。毎回正しいことより信頼が重要。
