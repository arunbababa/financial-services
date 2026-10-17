---
name: deal-sourcing
description: PE deal sourcing workflow — discover target companies, check CRM for existing relationships, and draft personalized founder outreach emails. Use when sourcing new deals, prospecting companies in a sector, or reaching out to founders. Triggers on "find companies", "source deals", "draft founder email", "check if we've seen this company", or "outreach to founder".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/private-equity/skills/deal-sourcing/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：PEの案件発掘として対象企業の発見、CRMでの既存関係確認、創業者向けに個別化した連絡メール案を作る。新案件探し、セクター内企業の探索、創業者への連絡に使う。適用表現は "find companies"、"source deals"、"draft founder email"、"check if we’ve seen this company"、"outreach to founder"。

<a id="deal-sourcing"></a>
# 案件の発掘

<a id="workflow"></a>
## ワークフロー

3段階の発掘手順を使う。

<a id="step-1-discover-companies"></a>
### 手順1：企業を探す

ユーザーの基準に合う候補企業を調査・特定する。

- **セクター・業界：** 探す分野を尋ねる（例「医療分野のB2B SaaS」「米南東部の産業サービス」）。
- **案件条件：** 売上・EBITDA範囲、成長特性、地域、所有形態（創業者所有、PE出資、企業カーブアウト）。
- **情報源：** Web検索で基準に合う企業を探す。業界レポート、会議参加者一覧、専門誌、競争環境を見る。
- **出力：** 名称、説明、推定売上・規模、所在地、創業者・CEO名、Webサイト、投資仮説に合う理由を持つ候補一覧。

<a id="step-2-crm-check"></a>
### 手順2：CRM確認

連絡前に、企業・創業者が会社のCRMへ既に登録されているか調べる。

- ユーザーのGmailで過去のやり取りを検索する。
- Slackで社内言及・過去の議論を検索する。
- 「あなたやチームは[Company]と以前に接触しましたか」と尋ねる。
- 既存関係、過去の見送り、既知の背景を示す。
- **出力：** 各社に「新規」（接触なし）、「既存」（やり取りあり。要約する）、「過去に見送り」（証拠がある場合）を付ける。

<a id="step-3-draft-founder-outreach"></a>
### 手順3：創業者への連絡文案

創業者・CEOごとに、面識のない相手へ送るメール案を作る。

- **口調：** 丁寧で温かく、堅すぎない。創業者には誠実で簡潔な連絡が響きやすい。
- **構成：**
  1. 自分と所属会社の短い紹介。不明なら会社紹介を尋ねる。
  2. 注目した理由。製品、市場での位置、成長など具体事項を挙げる。
  3. 求めるもの。単なる取引でなく提携。
  4. 控えめな依頼。「短くお話しする機会をいただけますか」。
- **個別化：** 製品・最近のニュース・市場の位置を参照する。汎用ひな型を使わない。
- **長さ：** 最大4〜6文。創業者は忙しい。
- **文体：** 過去の連絡メールがあれば学んで合わせる。Gmailの送信済みで "reaching out"、"introduction"、"partnership" 等を検索して例を探す。

<a id="email-draft-guidelines"></a>
### メール案の指針

- 件名は短く具体的に。「投資機会」でなく会社・セクターを示す。
- 初回は添付しない。
- 明確だが押し付けない行動依頼を入れる。
- Gmailが使えれば下書きを作り、なければコピーできる本文を出す。

<a id="example-interaction"></a>
## やり取りの例

**ユーザー：**「テキサスで売上1,000万〜5,000万ドル、創業者所有の産業サービス企業を探して」

**アシスタント：**
1. 条件に合うテキサスの企業をWeb検索する。
2. 主要情報付きで5〜8社の候補を示す。
3. Gmail・Slackで各社の過去接触を確認する。
4. 「新規」の企業向けに個別化した連絡文案を作る。
5. 送信前にユーザーへ下書きを示す。

<a id="important-notes"></a>
## 重要事項

- メール案を作る前に、必ず候補一覧をユーザーへ見せる。
- ユーザーの明示的承認なしにメールを送らない。
- 所属会社の紹介・投資基準が不明なら、起案前に尋ねる。
- 数より質。よく調べた5社は一般的な20社に勝る。
