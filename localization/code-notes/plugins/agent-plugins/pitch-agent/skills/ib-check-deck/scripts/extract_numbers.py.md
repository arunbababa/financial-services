# plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../../plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py)

### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:2

原文：

```text

Extract numerical values from presentation content for consistency checking.

Usage:
    python extract_numbers.py presentation-content.md
    python extract_numbers.py presentation-content.md --output numbers.json

This script parses markdown-formatted presentation content (from markitdown)
and extracts all numerical values with their context and slide references.

```

日本語：

プレゼンテーションの内容から、整合性を確認するための数値を抽出する。

使用例：

```sh
python extract_numbers.py presentation-content.md
python extract_numbers.py presentation-content.md --output numbers.json
```

markitdownが出力したMarkdown形式のプレゼンテーションを解析し、すべての数値を周辺の文脈とスライド参照付きで抽出する。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:25

原文：

```text
A numerical value found in the presentation.
```

日本語：

プレゼンテーションで見つかった数値。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:26

原文：

```text
Original string representation
```

日本語：

元の文字列表現


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:27

原文：

```text
Normalized numeric value
```

日本語：

正規化された数値


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:28

原文：

```text
Detected unit (M, B, K, %, bps, x, etc.)
```

日本語：

検出単位（M、B、K、%、bps、xなど）


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:29

原文：

```text
Slide number (0 if unknown)
```

日本語：

スライド番号 (不明の場合は 0)


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:30

原文：

```text
Surrounding text for context
```

日本語：

コンテキストを示す周囲のテキスト


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:31

原文：

```text
Line number in source file
```

日本語：

ソースファイルの行番号


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:32

原文：

```text
Detected category (revenue, margin, multiple, etc.)
```

日本語：

検出した分類（revenue=売上高、margin=利益率、multiple=評価倍率など）


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:36

原文：

```text
Convert a number string with unit to a normalized float value.
```

日本語：

単位付きの数値文字列を正規化された浮動小数点値に変換します。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:37

原文：

```text
Remove commas and spaces
```

日本語：

カンマとスペースを削除する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:45

原文：

```text
Apply unit multipliers
```

日本語：

単位乗数を適用する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:68

原文：

```text
Detect the category of a number based on context and unit.
```

日本語：

コンテキストと単位に基づいて数値のカテゴリを検出します。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:72

原文：

```text
top line
```

日本語：

top line（売上高を意味する表現）


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:89

原文：

```text
Valuation multiples
```

日本語：

評価倍率


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:93

原文：

```text
Enterprise value / market cap
```

日本語：

企業価値・時価総額


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:94

原文：

```text
enterprise value
```

日本語：

企業価値


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:94

原文：

```text
market cap
```

日本語：

時価総額


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:97

原文：

```text
Percentage (generic)
```

日本語：

パーセンテージ (一般)


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:101

原文：

```text
Multiple indicator
```

日本語：

倍率を示す指標


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:109

原文：

```text
Extract all numbers from presentation content.
```

日本語：

プレゼンテーションのコンテンツからすべての数値を抽出します。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:113

原文：

```text
Pattern for slide markers (from markitdown format)
```

日本語：

スライド マーカーのパターン (markitdown 形式から)


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:114

原文：

```text
^#+\s*Slide\s*(\d+)|^<!-- Slide (\d+)
```

日本語：

`^#+\s*Slide\s*(\d+)|^<!-- Slide (\d+)`

Slideの見出しまたはHTMLコメントからスライド番号を抽出する正規表現。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:116

原文：

```text
Pattern for numbers with various formats
```

日本語：

さまざまな形式の数字のパターン


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:117

原文：

```text
Matches: $500M, 500M, $500 million, 25%, 25.5%, 2.5x, 150bps, $1,234.56, etc.
```

日本語：

一致例：$500M, 500M, $500 million, 25%, 25.5%, 2.5x, 150bps, $1,234.56 など。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:119

原文：

```text
Optional currency symbol
```

日本語：

オプションの通貨記号


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:120

原文：

```text
The number itself
```

日本語：

数値そのもの


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:122

原文：

```text
Common units
```

日本語：

一般的な単位


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:123

原文：

```text
Full words
```

日本語：

省略せず単語で書いた単位


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:125

原文：

```text
Negative lookahead to avoid partial matches
```

日本語：

部分一致を避けるための否定先読み


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:131

原文：

```text
Check for slide marker
```

日本語：

スライドマーカーを確認する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:137

原文：

```text
Find all numbers in the line
```

日本語：

行内のすべての数字を検索します


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:143

原文：

```text
Skip very short numbers without context (likely not financial)
```

日本語：

文脈のない非常に短い数字をスキップします (財務に関するものではない可能性があります)


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:147

原文：

```text
Skip year-like numbers (1900-2099) unless they have units
```

日本語：

単位がない場合、年のような数字 (1900 ～ 2099) をスキップします。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:155

原文：

```text
Build full value string
```

日本語：

完全な値の文字列を構築する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:158

原文：

```text
Get context (surrounding words)
```

日本語：

コンテキスト (周囲の単語) を取得する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:163

原文：

```text
Normalize unit
```

日本語：

単位を正規化する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:166

原文：

```text
Assume USD for $ without unit
```

日本語：

単位の付かない$表記はUSDと仮定する。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:187

原文：

```text
Find potential inconsistencies in extracted numbers.
```

日本語：

抽出された数値内の潜在的な不一致を見つけます。


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:190

原文：

```text
Group numbers by category
```

日本語：

数値を分類ごとにグループ化する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:196

原文：

```text
Check each category for mismatches
```

日本語：

各カテゴリの不一致をチェックする


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:201

原文：

```text
Group by approximate value (within 5% tolerance)
```

日本語：

概算値でグループ化する（許容差5%以内）


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:209

原文：

```text
5% tolerance
```

日本語：

5%許容範囲


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:216

原文：

```text
If we have multiple groups, there might be inconsistencies
```

日本語：

複数のグループがある場合、不一致が発生する可能性があります


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:218

原文：

```text
Sort groups by size (largest first)
```

日本語：

グループをサイズ順に並べ替えます (大きい順)


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:221

原文：

```text
The largest group is likely "correct", others are potential issues
```

日本語：

最大のグループはおそらく「正しい」ですが、その他は潜在的な問題です


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:244

原文：

```text
Extract numbers from presentation content for consistency checking
```

日本語：

プレゼンテーションのコンテンツから数値を抽出して一貫性をチェックする


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:246

原文：

```text
Markdown file with presentation content
```

日本語：

プレゼンテーション コンテンツを含むマークダウン ファイル


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:247

原文：

```text
Output JSON file (default: stdout)
```

日本語：

出力JSONファイル（デフォルト：stdout）


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:249

原文：

```text
Check for inconsistencies and report
```

日本語：

矛盾がないか確認して報告する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:253

原文：

```text
Read input
```

日本語：

入力の読み取り


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:256

原文：

```text
Error: File not found: 
```

日本語：

エラー: ファイルが見つかりません:


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:261

原文：

```text
Extract numbers
```

日本語：

数値を抽出する


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:264

原文：

```text
Prepare output
```

日本語：

出力の準備


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:280

原文：

```text
Check for inconsistencies if requested
```

日本語：

要求に応じて矛盾がないかチェックします


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:286

原文：

```text

=== POTENTIAL INCONSISTENCIES DETECTED ===

```

日本語：


=== 潜在的な矛盾が検出されました ===


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:289

原文：

```text
, Count: 
```

日本語：

、カウント:


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:290

原文：

```text
, Count: 
```

日本語：

、カウント:


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:294

原文：

```text
Output results
```

日本語：

出力結果


### plugins/agent-plugins/pitch-agent/skills/ib-check-deck/scripts/extract_numbers.py:299

原文：

```text
Output written to 
```

日本語：

出力の書き込み先
