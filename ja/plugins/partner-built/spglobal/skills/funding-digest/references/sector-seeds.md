> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/partner-built/spglobal/skills/funding-digest/references/sector-seeds.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="sector-seed-companies-reference"></a>
# セクターシード企業リファレンス

ユーザーが特定の企業ではなくセクターを指定する場合、これらのシード リストを使用して企業ユニバースをブートストラップします。これらは開始点であり、常に `get_competitors_from_identifiers` で展開し、`get_info_from_identifiers` で検証します。

> **以下のすべてのシードは、S&P Global の識別子システムに対して検証されています。** シードが解決できない場合は、削除する前に括弧内にリストされているエイリアスを試してください。

<a id="technology--software"></a>
## テクノロジー / ソフトウェア

<a id="ai--machine-learning"></a>
### AI / 機械学習
起点企業：OpenAI, Anthropic, Databricks, Scale AI, Cohere, Hugging Face, Mistral AI, xAI, Perplexity AI, Runway ML (alias: "Runway AI, Inc."), Together AI (alias: "Together Computer, Inc."), Character.ai (alias: "Character Technologies, Inc."), Groq, Stability AI, Aleph Alpha, Magic AI

⚠️ **除外対象 (起点企業として使用しないでください):**
- *Inflection AI* — コア チームは Microsoft に吸収されました (2024 年 3 月)。歴史的なラウンドは存在しますが、新しいアクティビティはありません。
- *Adept AI* — 2024年に主要部分がAmazonへ移りました。上記と同様です。
- *DeepMind* — Alphabet の子会社。独立した資金調達ラウンドはありません。

<a id="cybersecurity"></a>
### サイバーセキュリティ
起点企業：CrowdStrike, Palo Alto Networks, Wiz, Snyk, SentinelOne, Abnormal Security, Netskope

<a id="cloud-infrastructure--devtools"></a>
### クラウドインフラストラクチャ/開発ツール
起点企業：Snowflake, HashiCorp, Datadog, Confluent, Vercel, Supabase, PlanetScale

<a id="fintech"></a>
### フィンテック
起点企業：Stripe, Plaid, Brex, Ramp, Mercury, Affirm, Marqeta, Navan

<a id="vertical-saas"></a>
### 垂直型SaaS
起点企業：ServiceTitan, Toast, Procore, Veeva Systems, Blend Labs

<a id="healthcare--life-sciences"></a>
## ヘルスケア / ライフサイエンス

<a id="biotech--pharma"></a>
### バイオテクノロジー / 製薬
起点企業：Moderna, BioNTech, Recursion Pharmaceuticals, Tempus AI, Insitro, AbCellera

<a id="digital-health"></a>
### デジタルヘルス
起点企業：Teladoc, Hims & Hers, Ro, Noom, Color Health

⚠️ **除外対象 (起点企業として使用しないでください):**
- *Cerebral* — 現在も運営されていますが、重大な規制上の問題に直面しています。ユーザーが特に要求した場合にのみ含めてください。

<a id="medical-devices"></a>
### 医療機器
起点企業：Intuitive Surgical, Butterfly Network, Outset Medical

⚠️ **除外対象 (起点企業として使用しないでください):**
- *Shockwave Medical* — Johnson & Johnson によって買収されました (2024 年 5 月)。現在は子会社となっており、独立した資金調達ラウンドはありません。

<a id="energy--climate"></a>
## エネルギー / 気候

<a id="climate-tech"></a>
### 気候技術
起点企業：Redwood Materials, Form Energy, Commonwealth Fusion, Sila Nanotechnologies, Climeworks

<a id="clean-energy"></a>
### クリーンエネルギー
起点企業：Enphase Energy, First Solar, Rivian, QuantumScape, Sunnova

<a id="consumer"></a>
## 消費者

<a id="e-commerce--marketplace"></a>
### 電子商取引 / マーケットプレイス
起点企業：Shopify, Faire, Whatnot, Fanatics

⚠️ **除外対象 (起点企業として使用しないでください):**
- *Temu (PDD Holdings)* — PDD Holdings は巨大な上場複合企業です。その資金調達活動はベンチャーラウンドではなく株式市場を通じて行われます。

<a id="consumer-social--media"></a>
### 消費者向けソーシャル/メディア
起点企業：Discord, Reddit, Substack

⚠️ **除外対象 (起点企業として使用しないでください):**
- *BeReal* — Voodoo によって買収されました (2024 年 6 月)。現在は子会社となっている。
- *Lemon8* — ブランド名「Lemon8」は、S&P Global ではオランダの小さな会社 (Lemon8 B.V.) に解決されており、ByteDance ソーシャル メディア アプリではありません**。 ByteDance のアプリは子会社であり、独立した資金調達ラウンドはありません。使用しないでください。

<a id="industrials--logistics"></a>
## 産業・物流

<a id="logistics--supply-chain"></a>
### 物流・サプライチェーン
起点企業：Flexport, Samsara, Project44, FourKites

⚠️ **除外対象 (起点企業として使用しないでください):**
- *Convoy* — 2023年10月に営業を停止しました。識別子は依然として解決でき、過去のラウンドも取得できますが、新たな活動は現れません。

<a id="robotics--automation"></a>
### ロボティクス / オートメーション
起点企業：Figure AI, Agility Robotics, Locus Robotics, Symbotic, Covariant

<a id="space--aerospace"></a>
### 宇宙・航空宇宙
起点企業：SpaceX, Relativity Space, Rocket Lab, Planet Labs, Astra

<a id="identifier-alias-reference"></a>
## 識別子のエイリアス参照

一部の有名なブランド名は、S&P Global の法人名と一致しません。ブランド名が `get_info_from_identifiers` から空の結果を返した場合は、エイリアスを試してください。

| ブランド名 | S&P Global上の正式法人名 | company_id |
|---|---|---|
| Together AI | Together Computer, Inc. | C_1860042219 |
| Character.ai | Character Technologies, Inc. | C_1829047235 |
| Runway ML | Runway AI, Inc. | C_633706980 |
| Adept AI | Adept AI Labs Inc. | C_1780739313 |
| xAI | X.AI LLC | C_1863863313 |

> **ヒント:** ブランド名が失敗した場合は、正式な名前で `get_info_from_identifiers` を試してください。それも失敗した場合、その会社はまだインデックスに登録されていない可能性があります。最後の手段として、`company_id` を識別子として直接使用します。

<a id="notes"></a>
## 注意事項

- これらのリストは米国に拠点を置く企業に偏っています。地理的フィルタリング (ヨーロッパ、アジアなど) の場合、競合他社の拡大ステップが特に重要です。
- ここにリストされていないニッチなサブセクターについては、シードとして使用する 2 ～ 3 社の企業例をユーザーに尋ねます。
- シードがまだアクティブ/関連していることを常に検証します。企業はピボット、合併、または閉鎖されます。
- **更新頻度:** これらのシードは四半期ごとに確認する必要があります。特にAI分野のシーズは買収や新規参入によって急速に変化する。
- 子会社・買収済みと記した起点企業も、`get_info_from_identifiers`では解決できます（status = "Operating Subsidiary"）が、資金調達ラウンドは0件になります。資金調達の照会では除外します。
