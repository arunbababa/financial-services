---
name: tear-sheet
description: "Generate professional company tear sheets using S&P Capital IQ data via the Kensho LLM-ready API MCP server. Use this skill whenever the user asks for a tear sheet, company one-pager, company profile, fact sheet, company snapshot, or company overview document — especially when they mention a specific company name or ticker. Also trigger when users ask for equity research summaries, M&A company profiles, corporate development target profiles, sales/BD meeting prep documents, or any concise single-company financial summary. This skill supports four audience types: equity research, investment banking/M&A, corporate development, and sales/business development. If the user doesn't specify an audience, ask. Works for both public and private companies."
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：Kensho LLM-ready API MCP サーバーを介して S&P Capital IQ のデータを使用し、プロフェッショナルな企業要点資料（tear sheet）を作成します。ユーザーが企業要点資料、1 ページの企業資料、企業プロフィール、ファクトシート、企業スナップショット、企業概要文書を求めた場合、特に具体的な企業名やティッカーを挙げた場合に、このスキルを使用します。株式リサーチの要約、M&A 対象企業のプロフィール、経営企画・M&A 担当向けの買収候補企業プロフィール、営業・事業開発の商談準備資料、単一企業の簡潔な財務要約を求めた場合にも使用します。対象読者は、株式リサーチ、投資銀行・M&A、経営企画・M&A 担当、営業・事業開発の 4 種類です。ユーザーが対象読者を指定しない場合は確認してください。上場企業と非上場企業の両方に対応します。

<a id="financial-tear-sheet-generator"></a>
# 企業の財務要点資料ジェネレーター

S&P Global MCP ツールを介して S&P Capital IQ からライブ データを取得し、その結果をプロフェッショナルな Word ドキュメントとしてフォーマットすることで、対象ユーザーに特化した企業の企業要点資料を生成します。

<a id="style-configuration"></a>
## スタイル構成

これらは賢明なデフォルトです。会社のブランドに合わせてカスタマイズするには、このセクションを変更します。一般的な変更には、カラー パレットの交換、フォントの変更 (Calibri は多くの銀行で標準です)、免責事項のテキストの更新が含まれます。

**色:**
- プライマリ (ヘッダー バナーの背景、セクション ヘッダーのテキスト): #1F3864
- アクセント（特徴的な主要セクションの強調）：#2E75B6
- テーブルヘッダー行の塗りつぶし: #D6E4F0
- テーブルの交互の行の塗りつぶし: #F2F2F2
- テーブルの境界線: #CCCCCC
- ヘッダー バナー テキスト: #FFFFFF

**タイポグラフィ (docx-js のハーフポイントのサイズ):**
- フォントファミリー: Arial
- 社名：18pt太字（サイズ：36）
- セクションヘッダー: 11pt 太字 (サイズ: 22)、原色
- 本文：9pt（サイズ：18）
- 表テキスト：8.5pt（サイズ：17）
- フッター/免責事項: 7pt 斜体 (サイズ: 14)
- テンプレートごとのオーバーライドは、各参照ファイルのフォーマットに関する注意事項で指定されます。

**会社ヘッダー バナー:**
- ヘッダーは、ページ幅全体に広がるネイビー (#1F3864) のバナーで、白で会社名が表示されます。
- **バナー下のキーと値は、ページ幅いっぱいの二列・枠線なしの表で表示します。** 左列は企業情報（ティッカー、本社、設立、従業員、業種）、右列は財務情報（時価総額、EV、株価、発行済株式数）です。各セルでは太字ラベルと通常の太さの値を同じ行に置きます（例：「**Market Cap** $124.7B」）。全項目を一列に左寄せすると横幅を浪費し、専門的な資料に見えません。二列へ展開することが、既定の文書と専門的な企業要点資料を見分ける最も重要な視覚的特徴です。
  - **実装:** すべてのセルに `borders: none` および `shading: none` を含む 2 列のテーブルを作成します。列幅をそれぞれ 50% に設定します。左側の列フィールド (ティッカー、本社、設立、従業員) を左側のセルに別の段落として配置します。右列フィールド (時価総額、EV、株価、発行済株式数) を右セルに配置します。各フィールドは 1 つの段落です。ラベルは太字で表示され、値は通常で表示されます。
  - 各列の特定のフィールドは対象者によって異なります。参照ファイルのヘッダー仕様を参照してください。原則は常に、左側に固まらずにページ全体に広がることです。
- **ヘッダーのキーと値のブロックには枠付きテーブルを使用しないでください。** 枠付きテーブルは財務データのみに予約されています。
- ヘッダー内の主要な指標 (時価総額、EV、株価) は、枠線付きの別のテーブルではなく、インラインの Key-Value ペアとして表示する必要があります。

**セクションヘッダー:**
- 各セクションのヘッダーの直下に水平罫線 (細線、#CCCCCC、0.5pt) が付けられ、セクション間を視覚的に明確に分離します。
- **ヘッダー段落自体の下枠としてルールをレンダリングします** — ルールに別の段落要素を挿入しないでください。別の段落では前後に独自のスペースが追加され、セクション タイトルの下に過剰な空白が生じます。
- **実装:** docx-js で、`paragraph.borders.bottom = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" }` を介してセクション ヘッダー段落に下枠を適用します。 `doc.addParagraph()` を別の水平ルール要素とともに使用しないでください。 `thematicBreak` は使用しないでください。境界線は見出し段落自体に配置し、その後のスペースは 0pt である必要があるため、ルールはヘッダー テキストに対してしっかりと配置されます。
- 間隔: ヘッダー段落の前に 12 ポイント、ヘッダー段落の後に 0 ポイント、次のコンテンツ要素の前に 4 ポイント。

**箇条書きの書式設定:**
- すべての企業要点資料 タイプのすべての箇条書きコンテンツには、単一の箇条書き文字 (•) を使用します。 •、-、▸、または番号付きリストを企業要点資料内または企業要点資料間で混在させないでください。
- **統合・分析の箇条書き**（決算の要点、戦略的適合、統合の検討事項、会話のきっかけ）：左インデント360 DXA（0.25インチ）、箇条書き記号をぶら下げるブロック形式にします。解釈を含む内容であるため、通常本文、データ表、説明段落と見た目を区別します。
- 関係セクション内の **情報箇条書き**: 標準本文インデント (180 DXA)、ぶら下がりインデントなし。
- **箇条書きの左枠をアクセントにしてはいけません。** docx-jsでは描画が不安定で視覚的な乱れを生みます。特徴的な主要セクションは、字下げと文字サイズの違いで区別します。

**表 (財務データのみ):**
- ヘッダー行: 表ヘッダーの塗りつぶし (#D6E4F0) を太字の濃いテキストで表示
- 本文行: 白交互/表交互塗り (#F2F2F2)
- 境界線: 表の境界線の色 (#CCCCCC)、細線 (BorderStyle.SINGLE、サイズ 1)
- セルのパディング: 上/下 40 DXA、左/右 80 DXA
- すべての数値列を右揃えにする
- 常に ShadingType.CLEAR を使用します (SOLID は使用しないでください。SOLID では背景が黒くなります)。

**レイアウト:**
- US Letter ポートレート、余白 0.75 インチ (1080 DXA 全面)

**数値の書式設定:**
- 通貨はUSD。原則は百万ドル（$M）単位ですが、企業の売上高が$50B（500億ドル）を超えるなら十億ドル（$B）単位・小数第一位にします。単位は個別セルでなく列見出し（例："Revenue ($M)"）へ記します。
- **表のセル: カンマ付きの単純な数値。ドル記号はありません。** 例: 収益セルには、「$4,916」ではなく「4,916」が表示されます。列ヘッダーには単位が含まれます。
- 会計年度: 実際の年 (FY2022、FY2023、FY2024)、相対ラベル (FY-2、FY-1) はありません。
- 負の数は括弧で示します。例：(2.3%)
- パーセンテージ: 小数点第 1 位
- 大きな数値: 千の区切り文字としてカンマ

**フッター (ドキュメント フッター、インラインではない):**
出典の帰属と免責事項は、下部のインライン本文テキストとしてではなく、実際のドキュメントのフッターに配置します (各ページで繰り返されます)。フッターは、各ページの中央に配置されたちょうど 2 行です。
- 1 行目: 「データ: Kensho 経由の S&P Capital IQ」 | 分析: AI による生成 | [年月日]」
- 2行目: 「情報提供のみを目的としています。投資アドバイスではありません。」
- スタイル: 7pt 斜体、中央揃え、#666666 テキストの色
- このフッター テキストは、同じ会社のすべての企業要点資料 タイプで同一である必要があります。聴衆によって表現を変えないでください。
- **このフッターは、すべての企業要点資料、すべての対象ユーザー タイプ、すべてのページに必要です。** 省略しないでください。

<a id="component-functions"></a>
## コンポーネントの機能

**ドキュメント要素を作成するには、これらの関数を正確に使用する必要があります。カスタム docx-js スタイル コードを作成しないでください。** これらの関数を生成された Node スクリプトにコピーして呼び出してください。上記のスタイル設定の文章はドキュメントとして残ります。これらの機能は強制メカニズムです。

```javascript
const docx = require("docx");
const {
  Document, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType,
  Header, Footer, PageNumber, HeadingLevel, TableLayoutType,
  convertInchesToTwip
} = docx;

// ── Color constants ──
const COLORS = {
  PRIMARY: "1F3864",
  ACCENT: "2E75B6",
  TABLE_HEADER_FILL: "D6E4F0",
  TABLE_ALT_ROW: "F2F2F2",
  TABLE_BORDER: "CCCCCC",
  HEADER_TEXT: "FFFFFF",
  FOOTER_TEXT: "666666",
};

const FONT = "Arial";

// ── 1. createHeaderBanner ──
// Returns an array of docx elements: [banner paragraph, key-value table]
function createHeaderBanner(companyName, leftFields, rightFields) {
  // leftFields / rightFields: arrays of { label: string, value: string }
  const banner = new Paragraph({
    children: [
      new TextRun({
        text: companyName,
        bold: true,
        size: 36, // 18pt
        color: COLORS.HEADER_TEXT,
        font: FONT,
      }),
    ],
    shading: { type: ShadingType.CLEAR, color: "auto", fill: COLORS.PRIMARY },
    spacing: { after: 0 },
    alignment: AlignmentType.LEFT,
  });

  function buildCellParagraphs(fields) {
    return fields.map(
      (f) =>
        new Paragraph({
          children: [
            new TextRun({ text: f.label + "  ", bold: true, size: 18, font: FONT }),
            new TextRun({ text: f.value, size: 18, font: FONT }),
          ],
          spacing: { after: 40 },
        })
    );
  }

  const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };
  const noShading = { type: ShadingType.CLEAR, color: "auto", fill: "FFFFFF" };

  const kvTable = new Table({
    rows: [
      new TableRow({
        children: [
          new TableCell({
            children: buildCellParagraphs(leftFields),
            width: { size: 50, type: WidthType.PERCENTAGE },
            borders: noBorders,
            shading: noShading,
          }),
          new TableCell({
            children: buildCellParagraphs(rightFields),
            width: { size: 50, type: WidthType.PERCENTAGE },
            borders: noBorders,
            shading: noShading,
          }),
        ],
      }),
    ],
    width: { size: 100, type: WidthType.PERCENTAGE },
  });

  return [banner, kvTable];
}

// ── 2. createSectionHeader ──
// Returns a single Paragraph with bottom border rule
function createSectionHeader(text) {
  return new Paragraph({
    children: [
      new TextRun({
        text: text,
        bold: true,
        size: 22, // 11pt
        color: COLORS.PRIMARY,
        font: FONT,
      }),
    ],
    spacing: { before: 240, after: 0 }, // 12pt before, 0pt after
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    },
  });
}

// ── 3. createTable ──
// headers: string[], rows: string[][], options: { accentHeader?, fontSize? }
function createTable(headers, rows, options = {}) {
  const fontSize = options.fontSize || 17; // 8.5pt default
  const headerFill = options.accentHeader ? COLORS.ACCENT : COLORS.TABLE_HEADER_FILL;
  const headerTextColor = options.accentHeader ? COLORS.HEADER_TEXT : "000000";

  const cellBorders = {
    top: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    bottom: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    left: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
    right: { style: BorderStyle.SINGLE, size: 1, color: COLORS.TABLE_BORDER },
  };

  const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };

  function isNumeric(val) {
    if (typeof val !== "string") return false;
    const cleaned = val.replace(/[,$%()]/g, "").trim();
    return cleaned !== "" && !isNaN(cleaned);
  }

  // Header row
  const headerRow = new TableRow({
    children: headers.map(
      (h) =>
        new TableCell({
          children: [
            new Paragraph({
              children: [
                new TextRun({
                  text: h,
                  bold: true,
                  size: fontSize,
                  color: headerTextColor,
                  font: FONT,
                }),
              ],
            }),
          ],
          shading: { type: ShadingType.CLEAR, color: "auto", fill: headerFill },
          borders: cellBorders,
          margins: cellMargins,
        })
    ),
  });

  // Data rows with alternating shading
  const dataRows = rows.map((row, rowIdx) => {
    const fill = rowIdx % 2 === 1 ? COLORS.TABLE_ALT_ROW : "FFFFFF";
    return new TableRow({
      children: row.map((cell, colIdx) => {
        const align = colIdx > 0 && isNumeric(cell)
          ? AlignmentType.RIGHT
          : AlignmentType.LEFT;
        return new TableCell({
          children: [
            new Paragraph({
              children: [
                new TextRun({ text: cell, size: fontSize, font: FONT }),
              ],
              alignment: align,
            }),
          ],
          shading: { type: ShadingType.CLEAR, color: "auto", fill: fill },
          borders: cellBorders,
          margins: cellMargins,
        });
      }),
    });
  });

  return new Table({
    rows: [headerRow, ...dataRows],
    width: { size: 100, type: WidthType.PERCENTAGE },
  });
}

// ── 4. createBulletList ──
// items: string[], style: "synthesis" | "informational"
function createBulletList(items, style = "synthesis") {
  const indent =
    style === "synthesis"
      ? { left: 360, hanging: 180 }   // 360 DXA left, hanging indent for bullet
      : { left: 180 };                 // 180 DXA, no hanging

  return items.map(
    (item) =>
      new Paragraph({
        children: [
          new TextRun({ text: "•  ", font: FONT, size: 18 }),
          new TextRun({ text: item, font: FONT, size: 18 }),
        ],
        indent: indent,
        spacing: { after: 60 },
      })
  );
}

// ── 5. createFooter ──
// date: string (e.g., "February 23, 2026")
function createFooter(date) {
  return new Footer({
    children: [
      new Paragraph({
        children: [
          new TextRun({
            text: `Data: S&P Capital IQ via Kensho | Analysis: AI-generated | ${date}`,
            italics: true,
            size: 14, // 7pt
            color: COLORS.FOOTER_TEXT,
            font: FONT,
          }),
        ],
        alignment: AlignmentType.CENTER,
      }),
      new Paragraph({
        children: [
          new TextRun({
            text: "For informational purposes only. Not investment advice.",
            italics: true,
            size: 14,
            color: COLORS.FOOTER_TEXT,
            font: FONT,
          }),
        ],
        alignment: AlignmentType.CENTER,
      }),
    ],
  });
}
```

**生成されたスクリプトでの使用:**
1. 上記のすべての関数と定数を、生成された Node.js スクリプトにコピーします。
2. バナーの段落と表を手動で作成する代わりに、`createHeaderBanner(...)` を呼び出します。
3. すべてのセクション タイトルに対して `createSectionHeader(...)` を呼び出します。段落の境界線を手動で設定しないでください。
4. 財務概要、上場類似企業比較、M&A、取引関係、資金調達履歴等、**すべて**の表形式データに`createTable(...)`を使います。IB/M&AのM&A表には`{ accentHeader: true }`を渡します。関係や持分構成等の非数値の表にも使え、数値セルだけを右寄せします。
5. 決算ハイライト、戦略的適合、統合の検討事項、会話のきっかけには`createBulletList(items, "synthesis")`を呼び出します。
6. 関係エントリについては、`createBulletList(items, "informational")` を呼び出します。
7. `createFooter(date)` を Document コンストラクターの `footers.default` プロパティに渡します。

**これらの機能により排除されるもの:**
- 黒の背景テーブル (どこでも `ShadingType.CLEAR` を強制)
- セクション見出しの下に独立した水平罫線の段落ができる問題（段落自体への`border.bottom`を強制して防ぐ）
- ヘッダー内の境界線付きキー/値テーブル (`borders: none` を強制)
- 一貫性のない箇条書きスタイル (`•` 文字のみを適用)
- フッターがありません (正確なフッター構造を提供します)

<a id="workflow"></a>
## ワークフロー

<a id="step-1-identify-inputs"></a>
### ステップ 1: 入力を特定する

次に進む前に、最大 4 つのものを集めてください。

1. **会社** — 名前またはティッカー。ティッカーのみの場合は、最初のクエリで完全な会社名を解決します (たとえば、会社情報ツールを使用します)。
2. **対象者** — 4 つのタイプのいずれか:
   - **株式調査** — 投資を評価するバイサイド/セルサイドのアナリスト向け
   - **IB / M&A** — 取引の観点から企業のプロファイリングを行う銀行家向け
   - **経営企画・M&A担当** — 買収目標を評価する社内戦略チーム向け
   - **営業 / BD** — 顧客とのミーティングの準備をしている商業チーム向け
3. **比較可能な企業** (オプション) — ユーザーが特定のコンプを念頭に置いている場合は、それらをメモします。それ以外の場合、スキルは S&P Global データからピアを識別します。これは株式調査、IB/M&A、経営企画・M&A担当の企業要点資料にとって重要です。
4. **ページの長さの設定** (オプション) — デフォルトは対象読者によって異なります (下記を参照) が、ユーザーは上書きできます。

ユーザーが対象者を指定していない場合は、尋ねてください。

<a id="step-2-read-the-audience-specific-reference"></a>
### ステップ 2: 対象読者向けのリファレンスを読む

このスキルのディレクトリから対応する参照ファイルを読み取ります。

- 株式リサーチ → `references/equity-research.md`
- IB / M&A → `references/ib-ma.md`
- 経営企画・M&A担当 → `references/corp-dev.md`
- 販売 / BD → `references/sales-bd.md`

各参照では、セクション、クエリ プラン、書式設定のガイダンス、およびページの長さのデフォルトが定義されています。

<a id="step-3-pull-data-via-sp-global-mcp"></a>
### ステップ 3: S&P Global MCP 経由でデータを取得する

**最初に:** 中間ファイル ディレクトリを作成します。
```bash
mkdir -p /tmp/tear-sheet/
```

**S&P Global** MCP ツール (Kensho LLM 対応 API とも呼ばれます) を使用します。クロードは、財務データ、企業情報、市場データ、コンセンサス推定、決算説明会の書き起こし、M&A 取引、ビジネス関係のための構造化ツールにアクセスできるようになります。各参照ファイル内のクエリ プランは、各セクションでどのようなデータを取得するかを記述し、会話で利用可能な適切な S&P Global ツールにマッピングします。

**各クエリ ステップの後、取得したデータを参照ファイルのクエリ プランで指定された中間ファイルにすぐに書き込みます。** 書き込みを延期しないでください。ディスクに書き込まれるデータは、長い会話によるコンテキストの劣化から保護されます。

**クエリ戦略:**
各参照ファイルには、4 ～ 6 のデータ取得ステップを含むクエリ プランが含まれています。これらは出発点であり、厳格な制約ではありません。呼び出しを最小限に抑えるよりもデータの完全性を優先します。

- **3 年分しか表示されていない場合でも、必ず 4 会計年度分の財務データを取得してください**。最初に表示される年の前年比収益増加を計算するには、4 番目 (最も早い) 年が必要です。これがないと、最初の年の成長率は「N/A」と表示されます。これはデータが欠落しているように見え、設計上の選択ではありません。
- 必要なデータに一致する S&P Global ツールを使用して、書かれたとおりにクエリ プランを実行します。
- ツール呼び出しで不完全な結果が返された場合は、代替ツールまたはより範囲の狭いクエリを試してください。たとえば、会社概要にセグメントの詳細が含まれていない場合は、セグメント ツールを直接試してください。
- ターゲットを絞った再試行後にデータ ポイントが返されない場合は、「N/A」または「非公開」というラベルを付けて次に進みます。
- データの捏造は絶対に行わないでください。ツールが数値を返さない場合は、トレーニングの知識から推定しないでください。

**ユーザー指定の企業:** ユーザーが比較可能な企業を指定した場合は、各企業の財務と倍率を明示的にクエリします。カンプが提供されていない場合は、ツールが返すピア データを使用するか、競合他社ツールを使用して会社のセクターのピアを特定します。

**ユーザーからのオプションのコンテキスト:** ユーザーが自然に提供する追加のコンテキストを聞きます。買収者が誰であるか (「当社のプラットフォーム向けにこれを検討している」)、何を販売しているか (「当社はデータ分析を銀行に販売している」)、または可能性のある買い手が誰であるか (「これは Salesforce または Microsoft にとって興味深いでしょう」) について言及した場合は、そのコンテキストを関連する統合セクション (戦略的適合、会話のスターター、取引の角度) に組み込みます。この情報の入力を求めるプロンプトを表示しないでください。提供された場合にのみ使用してください。

**非上場企業の扱い：**
CIQ には非上場企業のデータが含まれるため、同じ方法でクエリを実行します。ただし、結果はまばらになることが予想されます。非上場企業のために生成する場合:
- スキップ: 株価、52 週間のレンジ、ベータ、株価パフォーマンス、コンセンサス推定、トレーディングコンプ
- ビジネスの概要、取引関係、所有権構造、利用可能な財務情報などを調べます。
- ヘッダーに「Private Company」と目立つように記載してください

<a id="step-3b-calculate-derived-metrics"></a>
### ステップ 3b: 派生メトリクスを計算する

すべてのデータ収集が完了し、中間ファイルが書き込まれた後、単一の専用パスですべての派生メトリックを計算します。これは計算のみのステップであり、新しい MCP クエリはありません。

**すべての中間ファイルをコンテキストに読み戻して**、次を計算します。

- **利益率:** 売上総利益率 %、EBITDA 利益率 %、FCF 利益率 %、営業利益率 %
- **成長率:** 前年比売上成長率、前年比セグメント売上成長率、前年比 EPS 成長率
- **効率指標：** FCF転換率（FCF/EBITDA）、売上高比の研究開発費、売上高比の設備投資
- **資本構成：** 純有利子負債（有利子負債合計 − 現金及び現金同等物）、純有利子負債 / EBITDA
- **セグメント構成:** 連結総収益に占める各セグメントの収益の割合 (データ整合性ルール 8 に従い、連結収益を分母として使用)

**検証 (算術検証から移動):** この計算パス中に、すべての算術チェックを強制します。

- **利益率：** EBITDA Margin = EBITDA / Revenue、Gross Margin = Gross Profit / Revenue等を確認します。計算した利益率が生の数値と整合しなければ、生の構成要素からの計算を使います。
- **成長率:** 前年比成長率 = (現在 − 以前) / 以前を確認します。基礎となる値がある場合は、事前に計算された成長率に依存しないでください。
- **セグメント合計:** セグメントごとに収益を表示する場合は、セグメントの合計が総収益であることを確認します (四捨五入許容範囲内)。そうでない場合は、一貫性のない計算を公開するのではなく、合計行を省略してください。
- **パーセンテージ列:** 「合計に対する %」列の合計が ~100% であることを確認します。
- **評価のクロスチェック:** EV と EV/収益の両方を表示する場合は、EV / 収益 ≈ 記載された倍数であることを確認してください。

検証が失敗した場合: 生データから再計算を試みます。それでも一貫性がない場合は、間違った数値を公開するのではなく、メトリックに「N/A」のフラグを立てます。企業要点資料にある静かな数学的エラーは信頼性を破壊します。

**結果を書き込み**、次の列を含む `/tmp/tear-sheet/calculations.csv` に書き込みます: `metric,value,formula,components`

行の例:
```
metric,value,formula,components
gross_margin_fy2024,72.4%,gross_profit/revenue,"9524/13159"
revenue_growth_fy2024,12.3%,(current-prior)/prior,"13159/11716"
net_debt_fy2024,2150,total_debt-cash,"4200-2050"
```

<a id="step-3c-verify-data-files"></a>
### ステップ 3c: データ ファイルを検証する

ドキュメントを生成する前に、すべての中間ファイルが存在し、データが設定されていることを確認してください。

**各中間ファイル**を個別の読み取り操作で読み取り、検証の概要を出力します。

```
=== Tear Sheet Data Verification ===
company-profile.txt: ✓ (12 fields)
financials.csv:      ✓ (36 rows)
segments.csv:        ✓ (8 rows)
valuation.csv:       ✓ (5 rows)
calculations.csv:    ✓ (18 rows)
earnings.txt:        ✓ (populated)
relationships.txt:   ⚠ MISSING
peer-comps.csv:      ✓ (12 rows)
================================
```

**ソフト ゲート:** 現在の対象ユーザー タイプに必要なファイルが見つからないか空の場合は、警告を出力しますが続行します。企業要点資料は、「N/A」とセクションのスキップを使用して欠落データを適切に処理します。ただし、警告により、どのデータが失われたのかが確実にわかります。

**重要なルール: 以前の会話の記憶ではなく、ファイルが文書内のすべての数値の信頼できる唯一の情報源です。** ステップ 4 で DOCX を生成するときは、中間ファイルから値を読み取ります。財務データについては会話のコンテキストに依存しないでください。

<a id="step-4-format-as-docx"></a>
### ステップ 4: DOCX としてフォーマットする

docx 作成の仕組み (ノード経由の docx-js) については、`/mnt/skills/public/docx/SKILL.md` をお読みください。上記のスタイル設定に加えて、参照ファイル内のセクション固有の書式設定を適用します。

**ページの長さのデフォルト (ユーザーは上書き可能):**
- 株式調査: 1 ページ (密度は慣例です)
- IB / M&A: 1-2 ページ
- 経営企画・M&A担当: 1 ～ 2 ページ
- 販売/BD：1～2ページ

コンテンツが目標を超える場合、各参照ファイルは最初にカットするセクションを指定します。

**出力ファイル名:** `[CompanyName]_TearSheet_[Audience]_[YYYYMMDD].docx`
例: `Nvidia_TearSheet_CorpDev_20260220.docx`

`/mnt/user-data/outputs/` に保存し、ユーザーに提示します。

<a id="data-integrity-rules"></a>
## データ整合性ルール

これらは他のすべてをオーバーライドします。
1. **S&P Global ツールは財務データの唯一の情報源です。** トレーニングに関する知識でギャップを埋めないでください。知識が古かったり、間違っていたりする可能性があります。
2. **見つからないものにはラベルを付けます。** 行を黙って省略するのではなく、「N/A」または「非公開」を使用します。
3. **日付を明示します。** 会計年度末・報告期間を記載し、暦年＝会計年度と仮定してはいけません。株価や時価総額には、そのデータの基準日（as of）を付けます。
4. **報告期間を混合しないでください。** 2023 会計年度の収益と LTM EBITDA がある場合は、それらを区別してラベル付けしてください。
5. **手動計算よりも MCP から返されるフィールドを優先します。** S&P Global ツールが事前に計算されたフィールド (純負債、EBITDA、FCF など) を返す場合は、コンポーネントから計算するのではなく、その値を直接使用します。ツールがフィールドを返さない場合にのみ、派生メトリクスを手動で計算します。これにより、不一致が減少します。
6. **企業要点資料のタイプ全体で一貫性を確保します。** 同じ会社に対して複数の企業要点資料を生成する場合 (例: 同じセッション内の株式調査と IB/M&A)、同じ基礎となるデータ ポイントがすべての出力にわたって同一の値を生成する必要があります。純負債、収益、EBITDA、利益率、成長率は正確に一致する必要があります。レポートごとに個別に再クエリまたは再計算を行わず、同じ取得値を再利用します。
7. **既知の取引値をダウングレードしないでください。** M&A ツールが取引の取引値を返す場合、その値が出力に表示される必要があります。既知の取引額を「非公開」に置き換えないでください。 「非公開」は、ツールが実際にトランザクションの値を返さない場合にのみ使用してください。
8. **セグメントのパーセンテージの分母として連結収益を使用してください。** セグメント表の「合計に対する割合」を計算する場合、各セグメントの収益をセグメント収益の合計ではなく、連結総収益 (損益計算書で報告されている) で割ってください。セグメント間の消去により、セグメントの合計は連結収益を超えることがよくあります。連結収益を使用すると、パーセンテージがドキュメント内の他の場所に示されている総収益の数値と確実に一致します。
9. **利用可能なら将来予想（NTM）倍率を必ず含めます。** ツールが実績・将来予想の両倍率を返すなら、両方を示します。将来予想倍率は株式調査、IB/M&A、経営企画・M&A担当の主要な評価基準です。予想データがあるのに実績倍率だけを示してはいけません。
10. **S&P Globalのツールから経営者・経営陣のデータは返りません。** 学習データから氏名、役職、略歴を補うと規則1に違反し、古い情報を生みます。テンプレートに経営陣の節があれば丸ごと省略してください。機関投資家持分、内部者比率、PEスポンサー等の持分構成は、ツールから取得できた場合だけ含めます。

<a id="intermediate-file-rule"></a>
## 中間ファイルのルール

MCP ツールから取得したすべてのデータは、ドキュメントを生成する前に構造化中間ファイルに保存する必要があります。これらのファイルは、会話のコンテキストではなく、文書内のすべての数値の信頼できる唯一の情報源です。

**セットアップ:** ステップ 3 の開始時に、作業ディレクトリを作成します。
```
mkdir -p /tmp/tear-sheet/
```

**クエリ後書き込みの義務:** 各 MCP クエリ ステップが完了したら、取得したデータを適切な中間ファイルに直ちに書き込みます。すべてのクエリが終了するまで待たないでください。各参照ファイルのクエリ プランでは、各ステップの後にどのファイルを書き込むかを指定します。

**ファイルスキーマ:**

| ファイル | 形式 | 列・構造 | 使用する読者区分 |
|---|---|---|---|
| `/tmp/tear-sheet/company-profile.txt` | キー・値のテキスト | name, ticker, exchange, HQ, sector, industry, founded, employees, market_cap, enterprise_value, stock_price, 52wk_high, 52wk_low, shares_outstanding, beta, ownership | 全区分 |
| `/tmp/tear-sheet/financials.csv` | CSV | `period,line_item,value,source` | すべて |
| `/tmp/tear-sheet/segments.csv` | CSV | `period,segment_name,revenue,source` | ER、IB、CD |
| `/tmp/tear-sheet/valuation.csv` | CSV | `metric,trailing,forward,source` | ER、IB、CD |
| `/tmp/tear-sheet/consensus.csv` | CSV | `metric,fy_year,value,source` | ER |
| `/tmp/tear-sheet/earnings.txt` | 構造化されたテキスト | 四半期、日付、主要な引用、ガイダンス、主要な要因 | ER、IB、セールス |
| `/tmp/tear-sheet/relationships.txt` | 構造化されたテキスト | 顧客、サプライヤー、パートナー、競合他社 - それぞれに記述子が付いています | IB、CD、セールス |
| `/tmp/tear-sheet/peer-comps.csv` | CSV | `ticker,metric,value,source` | ER、IB、CD |
| `/tmp/tear-sheet/ma-activity.csv` | CSV | `date,target,deal_value,type,rationale,source` | IB、CD |
| `/tmp/tear-sheet/calculations.csv` | CSV | `metric,value,formula,components` | すべて (ステップ 3b で記述) |

**略語:** ER = 株式リサーチ、IB = IB/M&A、CD = 経営企画・M&A担当、セールス = セールス/BD。

すべてのオーディエンス タイプがすべてのファイルを使用するわけではありません。参照ファイルはどのクエリ ステップが適用されるかを定義します。現在の視聴者タイプに関連しないファイルは作成する必要はありません。

**生の値のみ。** 中間ファイルには、ツールから返された生の値が保存されます。これらのファイルでマージン、成長率、またはその他の派生指標を事前計算しないでください。これはステップ 3b で行われます。

**ページ予算の適用:** 各参照ファイルは、デフォルトのページ長と番号付きのカットオーダーを指定します。レンダリングされたドキュメントが目標を超える場合は、指定された順序でカットを適用します。フォント サイズや余白をテンプレートの最小値よりも小さくしようとしないでください。カット順序は完全な優先スタックです。セクション 2 に触れる前にセクション 1 を完全にカットします。

<a id="content-quality-rules"></a>
## コンテンツ品質ルール

11. **読者ごとに説明文を書き直します。** CIQの企業概要は入力であり、完成品ではありません。株式調査には簡潔で投資仮説に沿った説明、IBには提案資料の文章、経営企画には製品中心の説明、営業・事業開発には平易な言葉が必要です。どの要点資料にもCIQの概要をそのまま貼ってはいけません。
12. **決算の要点も読者ごとに変えます。** 同じ説明会でも、株式調査はセグメント実績とコンセンサスの上振れ・下振れ、IBは利益率の推移と戦略的発言、営業・事業開発は会話につながる戦略テーマを必要とします。異なる種類の要点資料で同じ箇条書きを使い回してはいけません。
13. **総合セクションが差別化要因です。** 戦略的適合分析、統合に関する考慮事項、会話のきっかけ、およびビジネス概要の段落は、企業要点資料の価値が発揮される場所です。これらのセクションでは、データ ポイントを物語に結び付ける分析的推論が必要です。コンテキストなしで企業名を列挙することは合成ではありません。
14. **セグメント表で保留中の売却にフラグを立てる。** 企業がセグメントまたはビジネスユニットの保留中の売却を発表した場合は、保留中の取引を示す脚注または括弧をセグメント表に追加します (例: 「モビリティ* — *保留中の売却、2026 年半ばに予定」)。 Corp Dev および IB/M&A 企業要点資料の場合は、売却されたセグメントを除いた試算収益と収益構成を示すセグメント表の下に 1 行の注記を含めます。これは、読者が自分で計算をすることなく、「今後の」ビジネスを評価するのに役立ちます。

<a id="arithmetic-validation"></a>
### 算術検証

**→ ステップ 3b (派生メトリクスの計算) で算術検証が強制されるようになりました。** すべてのマージン計算、増加率、セグメント合計、パーセンテージ列、および評価のクロスチェックは、ドキュメント生成が開始される前に、専用の計算パス中に検証されます。完全な検証チェックリストについては、ステップ 3b を参照してください。
