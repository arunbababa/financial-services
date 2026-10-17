# plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md)

### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:91

原文：

```text
── Color constants ──
```

日本語：

── 色定数 ──


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:104

原文：

```text
── 1. createHeaderBanner ──
```

日本語：

── 1. createHeaderBanner（ヘッダーバナーを作成）──


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:105

原文：

```text
Returns an array of docx elements: [banner paragraph, key-value table]
```

日本語：

docx 要素の配列を返します: [バナー段落、キーと値のテーブル]


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:107

原文：

```text
leftFields / rightFields: arrays of { label: string, value: string }
```

日本語：

`leftFields` / `rightFields`: `{ label: string, value: string }` を要素とする配列


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:138

原文：

```text
, fill: 
```

日本語：

`, fill: `


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:165

原文：

```text
── 2. createSectionHeader ──
```

日本語：

── 2.createSectionHeader ──


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:166

原文：

```text
Returns a single Paragraph with bottom border rule
```

日本語：

下線となる下罫線を持つ Paragraph を 1 つ返す


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:185

原文：

```text
── 3. createTable ──
```

日本語：

── 3. createTable（表を作成）──


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:186

原文：

```text
headers: string[], rows: string[][], options: { accentHeader?, fontSize? }
```

日本語：

`headers: string[]` は見出し、`rows: string[][]` は行データ、`options: { accentHeader?, fontSize? }` は任意の設定


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:207

原文：

```text
Header row
```

日本語：

ヘッダー行


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:232

原文：

```text
Data rows with alternating shading
```

日本語：

交互にシェーディングされたデータ行


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:263

原文：

```text
── 4. createBulletList ──
```

日本語：

── 4. createBulletList（箇条書きリストを作成）──


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:264

原文：

```text
items: string[], style: "synthesis" | "informational"
```

日本語：

`items: string[]` は項目、`style: "synthesis" | "informational"` はスタイルの指定


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:284

原文：

```text
── 5. createFooter ──
```

日本語：

── 5.createFooter ──


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:285

原文：

```text
February 23, 2026
```

日本語：

2026 年 2 月 23 日


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:285

原文：

```text
date: string (e.g., "February 23, 2026")
```

日本語：

日付: 文字列 (例: "2026 年 2 月 23 日")


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:304

原文：

```text
For informational purposes only. Not investment advice.
```

日本語：

情報提供のみを目的としています。投資アドバイスではありません。


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:431

原文：

```text
=== Tear Sheet Data Verification ===
```

日本語：

=== 企業概要シートのデータ検証 ===


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:432

原文：

```text
company-profile.txt: ✓ (12 fields)
```

日本語：

company-profile.txt: ✓ (12 フィールド)


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:433

原文：

```text
financials.csv:      ✓ (36 rows)
```

日本語：

financials.csv:      ✓（36 行）


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:434

原文：

```text
segments.csv:        ✓ (8 rows)
```

日本語：

segments.csv:        ✓（8 行）


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:435

原文：

```text
valuation.csv:       ✓ (5 rows)
```

日本語：

valuation.csv:       ✓（5 行）


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:436

原文：

```text
calculations.csv:    ✓ (18 rows)
```

日本語：

calculations.csv:    ✓（18 行）


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:437

原文：

```text
earnings.txt:        ✓ (populated)
```

日本語：

earnings.txt:        ✓（入力済み）


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:438

原文：

```text
relationships.txt:   ⚠ MISSING
```

日本語：

relationships.txt:   ⚠ 未取得


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:439

原文：

```text
peer-comps.csv:      ✓ (12 rows)
```

日本語：

peer-comps.csv:      ✓（12 行）


### plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md:484

原文：

```text
mkdir -p /tmp/tear-sheet/
```

日本語：

`mkdir -p /tmp/tear-sheet/`


