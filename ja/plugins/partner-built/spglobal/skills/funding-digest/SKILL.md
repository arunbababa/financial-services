---
name: funding-digest
description: "Generate a polished one-page PowerPoint slide summarizing key takeaways from recent funding rounds and notable capital markets activity across a user's watched sectors or companies. Use this skill when the user asks for a deal flow summary, weekly recap, funding digest, transaction roundup, or capital markets briefing. Triggers on: 'deal flow digest', 'weekly funding recap', 'deal roundup', 'transaction summary this week', 'what happened in [sector] this week', 'capital markets update', or any request to compile recent funding activity into a briefing slide. Produces a professional single-slide PPTX with key takeaways, valuation data, and Capital IQ deal links."
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/partner-built/spglobal/skills/funding-digest/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：最近の資金調達ラウンドからの重要なポイントや、ユーザーが注目しているセクターや企業全体にわたる注目すべき資本市場の活動をまとめた、洗練された 1 ページの PowerPoint スライドを生成します。このスキルは、ユーザーが取引フローの概要、週次の要約、資金調達ダイジェスト、取引のまとめ、または資本市場の説明を要求するときに使用します。トリガー：「取引フローダイジェスト」、「毎週の資金調達概要」、「取引まとめ」、「今週の取引概要」、「今週[セクター]で起こったこと」、「資本市場最新情報」、または最近の資金調達活動を説明スライドにまとめるリクエスト。重要なポイント、評価データ、Capital IQ 取引リンクを含む、プロフェッショナルなシングルスライド PPTX を作成します。

**AI の免責条項 (必須):**
パワーポイントのフッターには次の免責事項テキストを含める必要があります。これはオプションではありません。これがないとレポートは不完全になります。

> **「分析は AI によって生成されます - すべての出力を確認してください。」**

**フッター** — 生成されたスライドの下部に、目立つ黄色のバナーとして「分析は AI によって生成されています — すべての出力を確認してください」が表示されます。

---

<a id="weekly-deal-flow-digest"></a>
# 毎週の取引フローのダイジェスト

S&P Global Capital IQ データを使用して、注目のセクターまたは企業にわたる最近の資金調達ラウンドからの重要なポイントを要約したアナリスト品質の **シングル スライドのパワーポイント**を生成します。各取引はCapital IQプロファイルにリンクされており、素早いドリルダウンが可能です。

<a id="when-to-use"></a>
## いつ使用するか

次のいずれかのパターンでトリガーされます。
- 「今週の取引フローのダイジェストを教えてください」
- 「[セクター] の毎週の資金調達の概要」
- 「[セクター/企業] で最近成立した取引は何ですか?」
- 「取引まとめ」または「取引まとめ」
- 「調査担当企業群の資本市場動向を更新して」
- 「最近の資金調達活動の概要」
- 取引、資金調達、ラウンドに関する定期的な説明資料の依頼

<a id="nested-skills"></a>
## ネストされたスキル

このスキルにより、1 スライドの PPTX ブリーフィングが作成されます。
- PowerPointを生成する前に、**`/mnt/skills/public/pptx/SKILL.md`を読みます**。最初から作成する場合は、補助リファレンスの`pptxgenjs.md`も読みます。

<a id="entity-resolution--tool-robustness"></a>
## エンティティの解決とツールの堅牢性

S&P Global の識別システムは、会社名を法人に解決します。これはほとんどの企業でうまく機能しますが、空の結果を引き起こす既知の障害モードがあります。 **これらのルールをワークフロー全体に適用して、サイレントなデータ損失を回避します。**

<a id="rule-0-pre-validate-all-identifiers-before-querying-funding"></a>
### ルール 0: 資金をクエリする前にすべての識別子を事前検証する

**資金調達ツールを呼び出す前に**、`get_info_from_identifiers` を通じてすべての識別子を実行してください。これは、問題を早期に発見するための最も安価で信頼性の高い方法です。応答で 2 つのことを確認してください。

1. **識別子を解決できたか。** 空またはエラーが返れば、その名前はS&P Globalにありません。`references/sector-seeds.md`の別名、正式法人名、または`company_id`を直接試します。
2. **`status`フィールドの値は何か。**
   - `"Operating"` → 資金調達ラウンドのクエリを安全に実行できます。
   - `"Operating Subsidiary"` → 企業は存在しますが、親会社の傘下です。**資金調達ラウンドは0件**と返ります。「[親会社]による買収済み」等の背景情報として記し、資金調達の照会は行いません。
   - その他のステータス (例: 閉鎖、非アクティブ) → 会社はもう運営されていません。履歴データは存在する可能性がありますが、新しいアクティビティはありません。

**この 1 つの事前検証手順により、結果が空になる問題の大部分は回避されます。** すべての候補を 1 つの `get_info_from_identifiers` 呼び出しにまとめて (大規模なバッチを適切に処理します)、続行する前に優先順位を付けます。

<a id="rule-1-never-trust-empty-results-without-a-fallback"></a>
### ルール 1: フォールバックなしの空の結果を決して信頼しない

データがあると予想される会社に対して `get_rounds_of_funding_from_identifiers` が空を返した場合:
1. **法人名または company_id を試してください。** 通常はブランド名が機能しますが、一部のブランド名は機能しません。既知の不一致については、`references/sector-seeds.md` の別名テーブルを参照してください。よくあるパターン：「[ブランド] AI」→「[法人名], Inc.」 (例: Together AI → 「Together Computer, Inc.」、Character.ai → 「Character Technologies, Inc.」、Runway ML → 「Runway AI, Inc.」)。
2. **会社が S&P に存在することを確認してください。** ルール 0 をスキップした場合は、今すぐ `get_info_from_identifiers(identifiers=["Company"])` を呼び出してください。これも空を返す場合は、会社が初期段階すぎるか、まだインデックスに登録されていない可能性があります。

<a id="rule-2-subsidiaries-have-no-funding-rounds"></a>
### ルール 2: 子会社には資金調達ラウンドがない

大企業の部門・完全子会社（Alphabet傘下のDeepMind、Microsoft傘下のGitHub、Voodoo傘下のBeReal等）では、**資金調達ラウンドは0件**と返ります。資本取引の動きは親会社のレベルで追跡されます。

**検出方法：** `get_info_from_identifiers`の`status`が`"Operating Subsidiary"`となります。`references/sector-seeds.md`でも既知の子会社に⚠️を付けています。資金調達の照会からは除外します。

<a id="rule-3-use-get_rounds_of_funding_from_identifiers-as-the-primary-tool-not-get_funding_summary_from_identifiers"></a>
### ルール 3: `get_funding_summary_from_identifiers` ではなく、`get_rounds_of_funding_from_identifiers` をプライマリ ツールとして使用する

概要ツールは高速ですが、信頼性が低くなります。詳細なラウンドが存在する場合でも、エラーや不完全なデータが返される可能性があります。常に詳細ラウンド ツールをプライマリ データ ソースとして使用してください。概要ツールは、簡単な集計チェック (合計調達額、ラウンド数) の場合にのみ使用でき、結果が低いと思われる場合は、ラウンド ツールに対して検証する必要があります。

<a id="rule-4-batch-carefully-and-validate"></a>
### ルール 4: 慎重にバッチ処理して検証する

大規模な企業ユニバース (50 社以上) を処理する場合は、15 ～ 20 のグループに分けてバッチ処理します。各バッチの後、空の結果を返した企業を確認し、次に進む前にルール 1 のフォールバック ステップを実行します。

<a id="rule-5-the-role-parameter-is-critical"></a>
### ルール 5: `role` パラメータは重要です

- `company_raising_funds` → 「X社はどのラウンドで資金を調達したか」（調達企業の視点）
- `company_investing_in_round_of_funding` → 「投資家Yは何に投資しましたか?」 （投資家の視点）

間違ったロールを使用すると、何も表示されずに空の結果が返されます。取引フロー ダイジェストの場合、ほとんどの場合、`company_raising_funds` が必要になります。投資家のポートフォリオ活動を具体的に分析する場合にのみ、投資家ロールを使用してください。

<a id="rule-6-identifier-resolution-is-case-insensitive-but-spelling-sensitive"></a>
### ルール 6: 識別子の解決では大文字と小文字は区別されませんが、スペルは区別されます

S&P Global は大文字と小文字の違い (「openai」 = 「OpenAI」) を処理しますが、スペルと句読点には厳格です。 「Character.ai」は成功しても「Character AI」は失敗する可能性があります。疑わしい場合は、解決が保証されている `company_id` (例: `C_1829047235`) を使用してください。

<a id="workflow"></a>
## ワークフロー

<a id="step-1-establish-coverage--period"></a>
### ステップ1：対象範囲と期間を定める

ダイジェストで何をカバーするかを決定します。次の 2 つのセットアップがあります。

**リピーター ユーザー (ウォッチリストあり):**
ユーザーが追跡するセクターまたは企業を以前に定義している場合は、そのリストを使用します。以前のウォッチリストの会話履歴を確認してください。

**新規ユーザー:**
尋ねる:

| パラメータ | デフォルト | 注意事項 |
|-----------|---------|-------|
| **セクター** | *(少なくとも 1 つ)* | 例: 「AI、フィンテック、バイオテクノロジー」 |
| **特定の企業** | オプション | セクターレベルのカバレッジを補足する |
| **期間** | 過去 7 日間 | 「今週」、「過去 2 週間」、「今月」 |

期間から正確な `start_date` および `end_date` を計算します。

<a id="step-2-build-the-company-universe"></a>
### ステップ2：対象企業群を作る

指定したセクターごとに、検証済みのブートストラップ アプローチを使用して企業ユニバースを構築します。

1. ドメイン知識からの **シード企業** (`references/sector-seeds.md` を参照)
   - シード ファイル内の ⚠️ 警告とエイリアスのメモに注意してください。一部の有名な企業は子会社であるか、買収されているか、解決するために特定の法人名が必要です。
   - シード ファイルには、既知のエイリアス不一致に対する `company_id` 値が含まれています。ブランド名が失敗した場合は、これらを直接使用してください。

2. **すべてのシードを直ちに事前検証します** (ルール 0):
   ```
   get_info_from_identifiers(identifiers=[all_seeds_for_this_sector])
   ```
   結果を二つの分類に分けます。
   - ✅ **識別でき、事業活動中**（`status` = "Operating"）→ 競合企業を用いた拡張へ進む
   - ❌ **識別できない、または子会社** → 起点企業ファイルの別名・正式法人名で再試行。子会社である点は背景情報として記し、資金調達の照会からは除外する

3. **競合他社経由で拡張** (✅ 解決されたシードのみを使用):
   ```
   get_competitors_from_identifiers(identifiers=[resolved_seeds], competitor_source="all")
   ```

4. **拡張されたユニバースを検証します:**
   ```
   get_info_from_identifiers(identifiers=[new_competitors])
   ```
   同じトリアージを適用します。ターゲットセクターに一致する `simple_industry` でフィルターします。未解決の名前または子会社を削除します。

ユーザーが特定の企業を指定した場合は、それらを直接追加しますが、事前検証トリアージを実行します。検証をスキップしないでください。有名なブランド名であっても、黙って失敗する可能性があります。

ユニバースを管理しやすい状態に保つ — セクターあたり 15 ～ 40 社の**解決済みで事業を行っている**企業を目指します。マルチセクターのダイジェストの場合、合計 50 ～ 100 社以上の企業が含まれる可能性があります。

<a id="step-3-pull-funding-rounds"></a>
### ステップ 3: 資金調達ラウンドをプルする

対象企業群のすべての企業について、次を行います。

```
get_rounds_of_funding_from_identifiers(
    identifiers=[batch],
    role="company_raising_funds",
    start_date="YYYY-MM-DD",
    end_date="YYYY-MM-DD"
)
```

ユニバースが大きい場合は、15 ～ 20 のバッチで処理します。

**各バッチの後、結果が空の企業を特定します。** アクティビティがあると予想される企業の場合:
1. 法人名または代替識別子を使用して再試行してください (上記のエンティティ解決ルールを参照)。
2. フォールバックを徹底的に行った後でのみ、会社を「データなし」としてログに記録します。

成功した結果からすべての `transaction_id` 値を収集し、詳細なラウンド情報を追加します。

```
get_rounds_of_funding_info_from_transaction_ids(
    transaction_ids=[all_funding_ids]
)
```

すべてのトランザクション ID をトランザクションごとに 1 つではなく 1 回の呼び出し (または少数の呼び出し) で渡します。ツールはバッチを効率的に処理します。

**各ラウンドから以下を抜粋します (スライドにとって重要):**
- `transaction_id` — Capital IQ 取引リンクに必要
- **発表日** — ラウンドが公表された日
- **終了日** — ラウンドが正式に終了した日
- 調達金額
- **資金調達前の評価** (開示されている場合)
- **資金調達後の企業評価額（ポストマネー）**（開示されていれば）
- 主要投資家
- ラウンドの種別（Series A、B、C等）
- 発行する証券の条件
- アドバイザー
- 価格傾向（上昇ラウンド/下降ラウンド/横ばい）

> **日付は必須です。** 発表日と完了日は、最終スライドの取引表に常に表示される必要があります。使用可能な日付が 1 つだけの場合は、それを表示し、もう 1 つを「—」としてマークします。

<a id="step-4-pull-company-context-for-notable-deals"></a>
### ステップ 4: 注目すべき取引について会社のコンテキストを取得する

重要な取引 (大規模なラウンド、注目すべき評価の変化) に関与している企業については、簡単な説明を取得してください。

```
get_company_summary_from_identifiers(identifiers=[notable_companies])
```

これにより、物語にコンテキストが追加されます (例: 「2021 年に設立された AI インフラストラクチャのスタートアップ企業である同社は、... に拡大しています。」)。

<a id="step-5-identify-highlights--trends"></a>
### ステップ 5: ハイライトとトレンドを特定する

スライドをデザインする前に、データを分析してストーリーを明らかにします。

**「注目」としてフラグを立てる:**
- ラウンド ≥ 1 億ドル
- ダウンラウンド（前回より低い評価額での資金調達。pricing trend = down）
- 新しいユニコーン (ポストマネー評価額が 10 億ドルを超える)
- 評価額の大幅な上昇 (ポストマネーが最後に知られている評価額の 2 倍以上)
- 同じ企業が6か月以内に再び資金調達するケース
- 異常に大規模な投資家シンジケート

**トレンドの特定:**
- この期間に導入された総資本と通常の資本の比較 (履歴データが利用可能な場合)
- どのサブセクターが最も注目されているか (最も多くのラウンド、最も資本が多い)
- ラウンドステージの分布 (初期ステージまたは後期ステージが優勢ですか?)
- ダイジェスト全体で最もアクティブな投資家
- 地理的集中
- 評価の傾向 (マネー前の評価は圧縮されているのか、それとも拡大しているのか?)

**重要なポイントを選択してください (3 ～ 5):**
最も重要なシグナルを 3 ～ 5 つの簡潔な箇条書き形式の要点に抽出します。これらはスライドの中心部分です。それぞれの要点は 1 文で、パンチがあり、データに裏付けられたものである必要があります。

例:
- 「AIセクターは8ラウンドで24億ドルを調達しました。これは、120億ドルのポストマネー評価で[会社]からの8億ドルのメガラウンドを筆頭に、前週の3倍です。」
- 「（同社は）2億ドルのシリーズDを35億ドルのプレマネーでクローズし、シリーズCの18億ドルから増加しました。これはAI開発者ツールに対する強い需要を示しています。」
- 「ダウンラウンドの動きが活発化した。後期ステージラウンド6件中2件の価格が以前のバリュエーションを下回った。」

<a id="step-6-generate-company-logos"></a>
### ステップ 6: 会社ロゴを生成する

重要なポイントや注目すべき取引で紹介されている企業ごとに、2 層のローカル パイプラインを使用してロゴを生成します。 **Clearbit は使用しないでください** (`logo.clearbit.com`) — これは非推奨であり、常に失敗します。外部ロゴ CDN (Brandfetch、logo.dev、Google Favicon) には API キーが必要であるか、ネットワーク制限によってブロックされています。代わりに、次のアプローチを使用してください。

<a id="tier-1-simple-icons-npm-package-3300-brand-svgs-no-network-required"></a>
#### Tier 1: `simple-icons` npm パッケージ (3,300 以上のブランド SVG、ネットワーク不要)

`simple-icons` パッケージには、数千の有名ブランドの高品質 SVG アイコンがバンドルされています。 API キーやネットワーク呼び出しはなく、完全にオフラインで動作します。 SVG → PNG 変換のために `sharp` と一緒にインストールします。

```bash
npm install simple-icons sharp
```

**検索戦略:**

```javascript
const si = require('simple-icons');
const sharp = require('sharp');

// Find an icon by exact title match (case-insensitive)
function findSimpleIcon(companyName) {
    // Try exact match first
    for (const [key, val] of Object.entries(si)) {
        if (!key.startsWith('si') || !val || !val.title) continue;
        if (val.title.toLowerCase() === companyName.toLowerCase()) return val;
    }
    // Try without common suffixes (AI, Inc., Corp.)
    const stripped = companyName.replace(/\s*(AI|Inc\.?|Corp\.?|Ltd\.?)$/i, '').trim();
    if (stripped !== companyName) {
        for (const [key, val] of Object.entries(si)) {
            if (!key.startsWith('si') || !val || !val.title) continue;
            if (val.title.toLowerCase() === stripped.toLowerCase()) return val;
        }
    }
    return null;
}

// Convert SVG to PNG with the brand's official color
async function simpleIconToPng(icon, outputPath) {
    const coloredSvg = icon.svg.replace('<svg', `<svg fill="#${icon.hex}"`);
    await sharp(Buffer.from(coloredSvg))
        .resize(128, 128, { fit: 'contain', background: { r: 255, g: 255, b: 255, alpha: 0 } })
        .png()
        .toFile(outputPath);
}
```

**対応範囲：** 典型的な対象企業のおよそ43%。Stripe、Anthropic、Databricks、Snowflake、Discord、Shopify、SpaceX、Mistral AI、Hugging Face等の大手技術ブランドに強く、ニッチなフィンテック、バイオ、初期企業には弱い傾向です。

<a id="tier-2-initial-based-fallback-via-sharp-100-coverage"></a>
#### 第2段階：`sharp`で頭文字ベースの代替画像を作る（100%対応）

`simple-icons` に見つからない企業の場合は、クリーンなイニシャルベースのロゴを PNG として生成します。

```javascript
async function generateInitialLogo(companyName, outputPath) {
    const initial = companyName.charAt(0).toUpperCase();
    const svg = `
    <svg width="128" height="128" xmlns="http://www.w3.org/2000/svg">
        <circle cx="64" cy="64" r="64" fill="#BDBDBD"/>
        <text x="64" y="64" font-family="Arial, Helvetica, sans-serif"
              font-size="56" font-weight="bold" fill="#FFFFFF"
              text-anchor="middle" dominant-baseline="central">${initial}</text>
    </svg>`;
    await sharp(Buffer.from(svg)).png().toFile(outputPath);
}
```

<a id="complete-pipeline"></a>
#### 完全なパイプライン

```javascript
async function fetchLogo(companyName, outputDir) {
    const fileName = companyName.toLowerCase().replace(/[\s.]+/g, '-') + '.png';
    const outPath = path.join(outputDir, fileName);

    // Tier 1: Try simple-icons
    const icon = findSimpleIcon(companyName);
    if (icon) {
        await simpleIconToPng(icon, outPath);
        return { path: outPath, source: 'simple-icons' };
    }

    // Tier 2: Generate initial-based fallback
    await generateInitialLogo(companyName, outPath);
    return { path: outPath, source: 'initial-fallback' };
}
```

**ロゴのガイドライン:**
- すべてのロゴを `/home/claude/logos/[company-name].png` に保存します
- すべてのロゴは背景が透明の 128×128 PNG です
- スライド上では、ロゴを高さ 0.35 ～ 0.5 インチで表示します。ロゴはアクセントであり、焦点ではありません。
- 初期フォールバック円は、白のテキストで灰色 (`BDBDBD`) の塗りつぶしを使用します - モノクロ パレットと一致します
- ロゴ スタイルを無作為に混合しないでください。ほとんどの企業がブランド アイコンを選択する場合、いくつかの代替案は自然に溶け込むはずです。

<a id="step-7-generate-the-one-page-pptx"></a>
### ステップ 7: 1 ページ PPTX を生成する

スライドを作成する前に、`/mnt/skills/public/pptx/SKILL.md` と `/mnt/skills/public/pptx/pptxgenjs.md` をお読みください。

`pptxgenjs` を使用して **シングル スライド** PowerPoint を作成します。スライドは情報が豊富であると同時に視覚的にすっきりしている必要があります。「テキストの壁」ではなく「エグゼクティブ ダッシュボード」と考えてください。

<a id="slide-layout"></a>
#### スライドのレイアウト

```
┌─────────────────────────────────────────────────────────────┐
│  DEAL FLOW DIGEST                                           │
│  [Period] · [Sectors]                           [Date]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │  $X.XB  │  │  N      │  │  $X.XB  │  │  $X.XB  │       │
│  │ Raised  │  │ Rounds  │  │ Avg Pre │  │ Largest │       │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │
│                                                             │
│  KEY TAKEAWAYS                                              │
│  ─────────────────────────────────────────────────          │
│  [Logo] Takeaway 1 text goes here...                        │
│  [Logo] Takeaway 2 text goes here...                        │
│  [Logo] Takeaway 3 text goes here...                        │
│  [Logo] Takeaway 4 text goes here...                        │
│                                                             │
│  TOP DEALS                                                  │
│  ┌──────────────────────────────────────────────────────────┐│
│  │Company│Type │Announced│Closed│Amount│Pre-$│Post-$│Lead│🔗││
│  │───────│─────│─────────│──────│──────│─────│──────│────│──││
│  │ ...   │ ... │  ...    │ ...  │ ...  │ ... │ ...  │... │🔗││
│  └──────────────────────────────────────────────────────────┘│
│                                                             │
│  [Footer: Deal Flow Digest · Sources: S&P Global Capital IQ]│
│  [Footer: AI Disclaimer]                                    │
└─────────────────────────────────────────────────────────────┘
```

<a id="design-specifications"></a>
#### 設計仕様

**色の哲学: ミニマル、モノクロファースト。** スライドは高級な財務報告書のように感じられるようにする必要があります。黒、白、グレーが大半を占めます。色は、意味を伝える場合 (例: 下降ラウンドの場合は赤のインジケーター、目立ったメトリクスの場合は緑のインジケーター)、または読者が自然にそれを期待する場合 (会社のロゴ) にのみ使用されます。背景の塗りつぶし、アクセントバー、グラデーション効果など、純粋に装飾的な目的で色を使用しないでください。

**カラー パレット — モノクロ エグゼクティブ:**
- プライマリ背景: `FFFFFF` (白) — クリーンでオープンなスライドの背景
- ヘッダー バー: `1A1A1A` (黒に近い) — タイトル領域の強いコントラスト
- 主要テキスト: `1A1A1A` (黒に近い) — すべての本文テキスト、統計数値、要点
- 二次テキスト: `6B6B6B` (ミディアムグレー) — ラベル、キャプション、フッター、日付スタンプ
- 枠線と仕切り: `D0D0D0` (ライトグレー) — 微妙な構造線、カードの輪郭、テーブルの枠線
- カードの背景: `F5F5F5` (オフホワイト / 非常に明るいグレー) - 統計カードの塗りつぶし、交互のテーブル行
- リンクテキスト: `2B5797` (落ち着いた青) — 表内の Capital IQ 取引リンク (スライド上の唯一の青)
- **セマンティックカラー (控えめに):**
  - ダウンラウンドや否定的なシグナル：`C0392B`（落ち着いた赤）。小さい点、タグ、単語一つの強調に限り、塗りつぶしや背景には使わない
  - 際立ったポジティブな指標 (新しいユニコーン、特大ラウンド): `2E7D32` (落ち着いた緑色) — 同じ最小限の使用法: ドット、小さなタグ、または 1 つの強調表示された数字
  - 色インジケーターを保証するデータ ポイントがない場合は、**色をまったく使用しない**。完全にモノクロのスライドは完全に正しいです。

**タイポグラフィ:**
- タイトル: 28 ～ 32 ポイント、太字、黒に近いヘッダー バーに白
- 統計数値: 36 ～ 44 ポイント、太字、ほぼ黒
- 統計ラベル: 10 ～ 12 ポイント、ミディアム グレー (`6B6B6B`)
- 重要なテキスト: 12 ～ 14 ポイント、黒に近い、左揃え
- 表の本文：9〜11pt。基本は黒に近い色、補助的な列は灰色（`6B6B6B`）
- リンクテキスト: 9 ～ 10 ポイント、ミュートブルー (`2B5797`)
- フッター: 8pt、ミディアムグレー

**統計カード (一番上の行):**
- 大規模なコールアウトとしての 4 つの主要な指標: 総調達額、ラウンド数、平均プレマネー評価、最大ラウンド
- 各カードの塗りは`F5F5F5`、枠線は細い`D0D0D0`とし、影や有彩色の塗りは使いません。
- 統計が驚くべきものまたは極端な場合 (例: 通常の 3 倍のボリューム、記録的な取引)、その 1 つの数字の横に小さな色付きの点または下線が配置される場合があります。それ以外の場合は完全にモノクロのままにしてください。
- 資金調達前の評価額がほとんど公開されていない場合は、別の指標で代用します (例: ラウンド サイズの中央値、新規ユニコーンの数)。

**重要なポイント (中央セクション):**
- 3 ～ 5 つの 1 行要点。それぞれに関連する会社のロゴが接頭辞として付けられます (小、高さ約 0.35 インチ)。
- 利用可能なロゴがない場合は、色付きの丸ではなく、会社のイニシャルが白の **灰色の丸** を使用してください。
- 左揃えにし、窮屈にならない余白を確保します。
- ダウンラウンドまたはネガティブなテイクアウェイには、小さな赤い点の接頭辞が使用される場合があります。それ以外の場合は色がありません
- 可能な場合は評価のコンテキストを含めます (例: 「50 億ドルのポストマネー評価で」)

**上位取引表 (下部セクション):**
- 特に注目すべき案件4〜6件を示すコンパクトな表
- 列: 会社、タイプ (シリーズ X)、発表済み (日付)、完了済み (日付)、金額 ($M)、プレマネー ($M)、ポストマネー ($M)、リード投資家、取引リンク
- **Announced**と**Closed**の列には、`MMM DD`形式（例："Jan 15"）で日付を示します。両列は必須で、省略しません。日付が不明なら「—」と表示します。
- **Deal Link** 列には、Capital IQ にリンクするクリック可能な「View →」テキストが含まれています。
  ```
  https://www.capitaliq.spglobal.com/web/client?#offering/capitalOfferingProfile?id=<transaction_id>
  ```
  ここで、`<transaction_id>` は、`get_rounds_of_funding_from_identifiers` の `transaction_id` です。
- 調達前・調達後の企業評価額が非開示なら、そのセルは「—」にします。
- ほぼ黒 (`1A1A1A`) の塗りつぶしと白のテキストを持つヘッダー行。 `F5F5F5` と `FFFFFF` の交互の行
- **テーブルをスライドの水平方向の中央に配置します**。テーブルの合計幅を計算し、スライド幅の中央に配置されるように `x` を設定します: `x = (slideWidth - tableWidth) / 2`。 16:9 レイアウト (幅 13.33 インチ) の場合、テーブルの幅が 12 インチの場合は、`x = 0.67` を使用します。テーブルをスライドの端に合わせて左揃えにしないでください。
- コンパクトにまとめます。この表は参照用であり、スライドの主役ではありません。
- 表のセルに色付きの塗りつぶしはありません。取引がダウンラウンドの場合、金額の横に小さな赤いテキストタグ「(↓ダウン)」が表示されることがあります。これが表で唯一許可されている色です。

**ディールリンクの実装 (pptxgenjs):**
pptxgenjs では、セル オブジェクトの `options.hyperlink` プロパティを使用して、ハイパーリンクが表のセルに追加されます。
```javascript
// Table cell with Capital IQ deal link
{
  text: "View →",
  options: {
    hyperlink: {
      url: `https://www.capitaliq.spglobal.com/web/client?#offering/capitalOfferingProfile?id=${transactionId}`
    },
    color: "2B5797",
    fontSize: 9,
    fontFace: "Arial"
  }
}
```

**テーブルのセンタリング (pptxgenjs):**
取引テーブルは常にスライドの中央に配置してください。 x 位置を動的に計算します。
```javascript
const SLIDE_W = 13.33; // 16:9 slide width
const TABLE_W = 12.5;  // total table width (sum of all column widths)
const TABLE_X = (SLIDE_W - TABLE_W) / 2; // ≈ 0.42"

slide.addTable(tableRows, {
  x: TABLE_X,
  y: tableY,
  w: TABLE_W,
  colW: [1.8, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.6, 0.7], // Company, Type, Announced, Closed, Amount, Pre-$, Post-$, Lead, Link
  // ... other options
});
```
必要に応じて `colW` 値を調整しますが、テーブルを中央に配置するために、常に `(SLIDE_W - sum(colW)) / 2` から `TABLE_X` を再計算してください。

**フッター:**
- 中程度のグレーの小さなテキスト: 「取引フロー ダイジェスト · [期間] · 出典: S&P グローバル キャピタル IQ · 生成 [日付]」

**一般的な色のルール (厳密に適用):**
- 会社のロゴは、スライド上の唯一の「フルカラー」要素であり、ソースからそのまま表示されます。
- 取引リンクでは、ミュートされた青 (`2B5797`) が使用されます。これは、セマンティックな赤/緑以外の唯一の非モノクロ テキスト色です。
- ロゴとリンクを除けば、スライドは白黒プリンターで正しく印刷される必要があります。
- 背景、アクセントバー、装飾的な図形、またはセクションの区切りには決して色を適用しないでください。
- 疑わしい場合は、灰色のままにしておきます。

<a id="code-structure"></a>
#### コード構造

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Deal Flow Digest";

const slide = pres.addSlide();
const SLIDE_W = 13.33; // 16:9 slide width in inches

// 1. Dark header bar with title and period
// 2. Stat cards row (4 cards: Total Raised, # Rounds, Avg Pre-Money, Largest Round)
// 3. Key takeaways section with logos (include valuation context)
// 4. Top deals table with Announced, Closed, Pre-Money, Post-Money columns and Capital IQ deal links
//    - Center the table: x = (SLIDE_W - tableWidth) / 2
// 5. Footer

pres.writeFile({ fileName: "/home/claude/deal-flow-digest.pptx" });
```

pptxgenjs の落とし穴ガイダンスに従って、シャドウと繰り返しスタイルにはファクトリ関数 (共有オブジェクトではない) を使用してください。

<a id="step-8-qa-the-slide"></a>
### ステップ 8: スライドの QA

PPTX スキルの QA プロセスに従います。

1. **コンテンツ QA:** `python -m markitdown deal-flow-digest.pptx` — すべてのテキスト、数字、会社名、評価額、取引リンクが正しいことを確認してください。
2. **ビジュアル QA:** 画像に変換して検査:
   ```bash
   python /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf deal-flow-digest.pptx
   pdftoppm -jpeg -r 200 deal-flow-digest.pdf slide
   ```
   要素の重なり、テキストのオーバーフロー、配置の問題、低コントラストのテキスト、ロゴのサイズ変更の問題、および取引リンク テキストが表示されていることを確認します。
3. **リンク QA:** 表内の Capital IQ URL が正しいトランザクション ID で正しくフォーマットされていることを確認します。
4. **修正と再検証** — 完了を宣言する前に、少なくとも 1 回の修正と検証のサイクル。

<a id="step-9-present-results"></a>
### ステップ 9: 結果を提示する

1. 最後の `.pptx` を `/mnt/user-data/outputs/` にコピーします
2. `present_files` を使用してスライドを共有します
3. 2 ～ 3 文の口頭での要約を提供します。
   - 「あなたのダイジェストには、[セクター] 全体で調達された合計 Y ドルの X ラウンドが含まれています。」
   - 最も注目すべき 1 つの取引とその評価を取り上げる
   - ダウンラウンド、評価額の縮小等、懸念する傾向を指摘します。

<a id="error-handling"></a>
## エラー処理

<a id="entity-resolution-failures"></a>
### エンティティ解決の失敗
- **既知の会社の空の結果:** まず `get_info_from_identifiers` を確認します。これが失敗した場合は、`references/sector-seeds.md` のエイリアスまたは `company_id` を直接試してください。一般的なブランド→法的不一致: Together AI → 「Together Computer, Inc.」、Character.ai → 「Character Technologies, Inc.」、Runway ML → 「Runway AI, Inc.」。
- **子会社：** DeepMind、GitHub、Instagram、WhatsApp、YouTube、BeReal等は子会社で、独立した資金調達ラウンドはありません。背景として「買収済み／子会社」と記し、「活動なし」と報告してはいけません。
- **事業停止企業：** Convoy（2023年10月に事業停止）等はS&P Globalで識別できても、新しい活動は生じません。`references/sector-seeds.md`に印があるので、対象へ含める前に確認します。
- **`get_funding_summary_from_identifiers` エラーが発生するか、ゼロが返されます:** `get_rounds_of_funding_from_identifiers` にフォールバックします。要約ツールの信頼性は低くなります。集計ツールを唯一のデータ ソースとして依存しないでください。
- **間違った `role` パラメータ:** 投資家視点のクエリが空を返す場合は、`company_raising_funds` ではなく `company_investing_in_round_of_funding` を使用していることを確認してください (逆も同様)。

<a id="data-quality-issues"></a>
### データ品質の問題
- **期間内にアクティビティはありません:** セクターの資金調達ラウンドがゼロの場合は、そのことをスライドに明示的に記載します (「期間中に [セクター] でトランザクションは記録されませんでした」)。アクティビティがないこと自体が有益です。
- **企業評価額の情報が少ない場合：** 多くの取引でプレマネー・ポストマネー評価額が非開示なら、そのデータ制約をフッター注記に記し、表では「—」を使います。統計カードも平均プレマネー評価額に代えて、調達額の中央値等の別指標を表示します。
- **ロゴ取得の失敗：** `simple-icons` npmパッケージは典型的な対象企業のおよそ43%をカバーします。残りは`sharp`で作る頭文字画像で補います。無作為な方式を混ぜず、統一したアイコン様式にします。`simple-icons`または`sharp`の導入に失敗したら、外部依存のないpptxgenjsの図形（灰色の楕円＋白い頭文字）へ切り替えます。
- **1 つのスライドに取引が多すぎます:** 注目すべき取引が 6 件を超えている場合は、表に上位 6 件を表示し、「+N 個の追加取引は表示されていません」という脚注を追加します。取引規模に応じて優先順位を付けます。
- **大規模なユニバース:** 100 社以上のマルチセクター ダイジェストの場合は、すべての API 呼び出しを 15 ～ 20 のグループにまとめます。マイナーな取引の完全性よりも、注目すべき取引の深さを優先します。
- **起点企業が適切でない場合：** 競合他社で対象を広げても結果が極端に少なければ、起点企業がニッチすぎる可能性があります。有名な企業をさらに2～3社追加し、再び対象企業群を広げます。
- **リンクのトランザクション ID が無効です:** 資金調達ツールの `transaction_id` が有効な Capital IQ URL を生成しない場合は、壊れたリンクを含めるのではなく、その行のリンク セルを省略してください。

<a id="example-prompts"></a>
## プロンプトの例

- 「AI とフィンテックに関する毎週の取引フローのダイジェストを教えてください」
- 「今週のバイオテクノロジー分野の資金調達の概要」
- 「過去 2 週間のサイバーセキュリティ、クラウド インフラストラクチャ、開発ツールに関する私の取材対象の取引まとめ」
- 「今週、私がフォローしているすべてのセクターのベンチャー業界で何が起こったでしょうか?」
- 「今月の気候変動テクノロジーに関する簡単な取引フローのスライド」
