# plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md)

### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:43

原文：

```text
IMPORTANT: Extract exact positions in inches
```

日本語：

重要: 正確な位置をインチ単位で抽出します


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:48

原文：

```text
, type=
```

日本語：

`, type=`

type=を含む出力文字列の断片。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:67

原文：

```text
Find the OBJECT placeholder to determine true content start
```

日本語：

OBJECT プレースホルダーを見つけて、実際のコンテンツの開始を判断します


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:71

原文：

```text
OBJECT type
```

日本語：

OBJECT型


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:73

原文：

```text
: OBJECT starts at y=
```

日本語：

: OBJECT は y= から始まります


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:73

原文：

```text
Layout [
```

日本語：

レイアウト [


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:74

原文：

```text
This y value is where your content should start!
```

日本語：

この y 値がコンテンツの開始位置です。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:91

原文：

```text
├── SKILL.md
```

日本語：

`├── SKILL.md`（スキル定義ファイル）


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:92

原文：

```text
└── assets/
```

日本語：

`└── assets/`（アセット用ディレクトリ）


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:93

原文：

```text
    └── template.pptx
```

日本語：

`    └── template.pptx`（テンプレートのPowerPointファイル）


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:102

原文：

```text
name: [company]-ppt-template
```

日本語：

`name: [company]-ppt-template`（スキル名の設定例。識別子はこの形式を保つ。）


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:103

原文：

```text
description: [Company] PowerPoint template for creating presentations. Use when creating [Company]-branded pitch decks, board materials, or client presentations.
```

日本語：

`description:`：[Company]のプレゼンテーションを作成するためのPowerPointテンプレート。[Company]ブランドの提案資料、取締役会資料、顧客向けプレゼンテーションの作成時に使う。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:106

原文：

```text
# [Company] PPT Template
```

日本語：

# [会社] PPT テンプレート


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:108

原文：

```text
Template: `assets/template.pptx` ([WIDTH]" x [HEIGHT]", [N] layouts)
```

日本語：

テンプレート: `assets/template.pptx` ([WIDTH]" x [HEIGHT]"、[N] レイアウト)


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:110

原文：

```text
## Creating Presentations
```

日本語：

## プレゼンテーションの作成


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:113

原文：

```text
from pptx import Presentation
```

日本語：

`from pptx import Presentation`

pptxからPresentationを読み込む。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:115

原文：

```text
prs = Presentation("path/to/skill/assets/template.pptx")
```

日本語：

`prs = Presentation("path/to/skill/assets/template.pptx")`

指定パスのテンプレートからPresentationを作成する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:117

原文：

```text
# DELETE all existing slides first
```

日本語：

# まず既存のスライドをすべて削除します


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:118

原文：

```text
while len(prs.slides) > 0:
```

日本語：

`while len(prs.slides) > 0:`

スライドが残っている間、削除処理を繰り返す。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:119

原文：

```text
    rId = prs.slides._sldIdLst[0].rId
```

日本語：

`rId = prs.slides._sldIdLst[0].rId`

先頭スライドのリレーションシップIDを取得する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:121

原文：

```text
    del prs.slides._sldIdLst[0]
```

日本語：

`del prs.slides._sldIdLst[0]`

先頭スライドのIDエントリを削除する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:123

原文：

```text
# Add slides from layouts
```

日本語：

# レイアウトからスライドを追加


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:124

原文：

```text
slide = prs.slides.add_slide(prs.slide_layouts[LAYOUT_IDX])
```

日本語：

`slide = prs.slides.add_slide(prs.slide_layouts[LAYOUT_IDX])`

LAYOUT_IDXで指定したレイアウトからスライドを追加する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:127

原文：

```text
## Key Layouts
```

日本語：

## 主なレイアウト


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:129

原文：

```text
| Index | Name | Use For |
```

日本語：

|インデックス |名前 |用途 |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:131

原文：

```text
| [0] | [Layout Name] | [Cover/title slide] |
```

日本語：

| [0] | [レイアウト名] | [表紙/タイトルスライド] |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:132

原文：

```text
| [N] | [Layout Name] | [Content with bullets] |
```

日本語：

| [N] | [レイアウト名] | [箇条書きの内容] |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:133

原文：

```text
| [N] | [Layout Name] | [Two-column layout] |
```

日本語：

| [N] | [レイアウト名] | [2カラムレイアウト] |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:135

原文：

```text
## Placeholder Mapping
```

日本語：

## プレースホルダーのマッピング


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:137

原文：

```text
**CRITICAL: Include exact positions (x, y coordinates) for each placeholder.**
```

日本語：

**重要: 各プレースホルダーの正確な位置 (x、y 座標) を含めてください。**


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:139

原文：

```text
### Layout [N]: [Name]
```

日本語：

### レイアウト [N]: [名前]


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:140

原文：

```text
| idx | Type | Position | Use |
```

日本語：

| idx | 種類 | 位置 | 用途 |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:142

原文：

```text
| [idx] | TITLE (1) | y=[Y]" | Slide title |
```

日本語：

| [idx] | TITLE (1) | y=[Y]" | スライドのタイトル |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:143

原文：

```text
| [idx] | BODY (2) | y=[Y]" | Subtitle/description |
```

日本語：

| [idx] | BODY (2) | y=[Y]" | サブタイトル/説明 |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:144

原文：

```text
| [idx] | BODY (2) | y=[Y]" | Footer |
```

日本語：

| [idx] | BODY (2) | y=[Y]" | フッター |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:145

原文：

```text
| [idx] | BODY (2) | y=[Y]" | Source/notes |
```

日本語：

| [idx] | BODY (2) | y=[Y]" | 出典/注記 |


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:147

原文：

```text
### Content Area Boundaries
```

日本語：

### コンテンツ領域の境界


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:149

原文：

```text
**Document the safe content area for custom shapes/tables/charts:**
```

日本語：

**カスタム図形/テーブル/グラフの安全なコンテンツ領域を文書化します:**


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:152

原文：

```text
Content Area (for Layout [N]):
```

日本語：

コンテンツエリア (レイアウト [N] の場合):


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:153

原文：

```text
- Left margin: [X]" (content starts here)
```

日本語：

- 左余白: [X]" (コンテンツはここから始まります)


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:154

原文：

```text
- Top: [Y]" (below subtitle placeholder)
```

日本語：

- 上端：[Y]"（サブタイトルのプレースホルダーより下）


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:155

原文：

```text
- Width: [W]"
```

日本語：

- 幅: [W]"


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:156

原文：

```text
- Height: [H]" (ends before footer)
```

日本語：

- 高さ: [H]" (フッターの前で終了)


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:158

原文：

```text
For 4-quadrant layouts:
```

日本語：

4 象限レイアウトの場合:


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:159

原文：

```text
- Left column: x=[X]", width=[W]"
```

日本語：

- 左列: x=[X]"、幅=[W]"


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:160

原文：

```text
- Right column: x=[X]", width=[W]"
```

日本語：

- 右列: x=[X]"、幅=[W]"


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:161

原文：

```text
- Top row: y=[Y]", height=[H]"
```

日本語：

- 一番上の行: y=[Y]"、高さ=[H]"


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:162

原文：

```text
- Bottom row: y=[Y]", height=[H]"
```

日本語：

- 最下段: y=[Y]"、高さ=[H]"


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:165

原文：

```text
**Why this matters:** Custom content (textboxes, tables, charts) must stay within these boundaries to avoid overlapping with template placeholders like titles, footers, and source lines.
```

日本語：

**これが重要な理由:** カスタム コンテンツ (テキストボックス、テーブル、グラフ) は、タイトル、フッター、ソース行などのテンプレート プレースホルダーとの重複を避けるために、これらの境界内に収める必要があります。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:167

原文：

```text
## Filling Content
```

日本語：

## コンテンツの入力


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:169

原文：

```text
**Do NOT add manual bullet characters** - slide master handles formatting.
```

日本語：

**手動で箇条書き文字を追加しないでください** - スライド マスターは書式設定を処理します。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:172

原文：

```text
# Fill title
```

日本語：

# タイトルを入力


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:173

原文：

```text
for shape in slide.shapes:
```

日本語：

`for shape in slide.shapes:`

slide.shapesに含まれる各shapeを順に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:174

原文：

```text
    if hasattr(shape, 'placeholder_format'):
```

日本語：

`if hasattr(shape, 'placeholder_format'):`

shapeがplaceholder_format属性を持つ場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:175

原文：

```text
        if shape.placeholder_format.type == 1:  # TITLE
```

日本語：

`if shape.placeholder_format.type == 1:  # TITLE`

プレースホルダーの種類が1（TITLE）の場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:176

原文：

```text
            shape.text = "Slide Title"
```

日本語：

`shape.text = "Slide Title"`

shape.textに「Slide Title」（スライドのタイトル）を設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:178

原文：

```text
# Fill content with hierarchy (level 0 = header, level 1 = bullet)
```

日本語：

# コンテンツを階層で埋める (レベル 0 = ヘッダー、レベル 1 = 箇条書き)


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:179

原文：

```text
for shape in slide.shapes:
```

日本語：

`for shape in slide.shapes:`

slide.shapesに含まれる各shapeを順に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:180

原文：

```text
    if hasattr(shape, 'placeholder_format'):
```

日本語：

`if hasattr(shape, 'placeholder_format'):`

shapeがplaceholder_format属性を持つ場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:181

原文：

```text
        idx = shape.placeholder_format.idx
```

日本語：

`idx = shape.placeholder_format.idx`

プレースホルダーのidxを取得する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:182

原文：

```text
        if idx == [CONTENT_IDX]:
```

日本語：

`if idx == [CONTENT_IDX]:`

idxが[CONTENT_IDX]と等しい場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:183

原文：

```text
            tf = shape.text_frame
```

日本語：

`tf = shape.text_frame`

shapeのテキストフレームをtfへ代入する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:184

原文：

```text
            for para in tf.paragraphs:
```

日本語：

`for para in tf.paragraphs:`

tf内の各段落paraを順に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:187

原文：

```text
            content = [
```

日本語：

`content = [`

contentのリスト定義を開始する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:188

原文：

```text
                ("Section Header", 0),
```

日本語：

`("Section Header", 0),`

「Section Header」（セクション見出し）を階層レベル0で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:189

原文：

```text
                ("First bullet point", 1),
```

日本語：

`("First bullet point", 1),`

「First bullet point」（最初の箇条書き項目）をレベル1で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:190

原文：

```text
                ("Second bullet point", 1),
```

日本語：

`("Second bullet point", 1),`

「Second bullet point」（2番目の箇条書き項目）をレベル1で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:193

原文：

```text
            tf.paragraphs[0].text = content[0][0]
```

日本語：

`tf.paragraphs[0].text = content[0][0]`

先頭段落のテキストをcontent[0][0]に設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:194

原文：

```text
            tf.paragraphs[0].level = content[0][1]
```

日本語：

`tf.paragraphs[0].level = content[0][1]`

先頭段落の階層レベルをcontent[0][1]に設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:195

原文：

```text
            for text, level in content[1:]:
```

日本語：

`for text, level in content[1:]:`

contentの2件目以降からtextとlevelを取り出して繰り返す。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:196

原文：

```text
                p = tf.add_paragraph()
```

日本語：

`p = tf.add_paragraph()`

新しい段落を追加し、pに代入する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:197

原文：

```text
                p.text = text
```

日本語：

`p.text = text`

pのテキストをtextに設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:198

原文：

```text
                p.level = level
```

日本語：

`p.level = level`

pの階層レベルをlevelに設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:201

原文：

```text
## Example: Cover Slide
```

日本語：

## 例: カバー スライド


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:204

原文：

```text
slide = prs.slides.add_slide(prs.slide_layouts[[COVER_IDX]])
```

日本語：

`slide = prs.slides.add_slide(prs.slide_layouts[[COVER_IDX]])`

[COVER_IDX]を使う表紙用レイアウトからスライドを追加するコード例。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:205

原文：

```text
for shape in slide.shapes:
```

日本語：

`for shape in slide.shapes:`

slide.shapesに含まれる各shapeを順に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:206

原文：

```text
    if hasattr(shape, 'placeholder_format'):
```

日本語：

`if hasattr(shape, 'placeholder_format'):`

shapeがplaceholder_format属性を持つ場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:207

原文：

```text
        idx = shape.placeholder_format.idx
```

日本語：

`idx = shape.placeholder_format.idx`

プレースホルダーのidxを取得する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:208

原文：

```text
        if idx == [TITLE_IDX]:
```

日本語：

`if idx == [TITLE_IDX]:`

idxが[TITLE_IDX]と等しい場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:209

原文：

```text
            shape.text = "Company Name"
```

日本語：

`shape.text = "Company Name"`

shape.textに「Company Name」（会社名）を設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:210

原文：

```text
        elif idx == [SUBTITLE_IDX]:
```

日本語：

`elif idx == [SUBTITLE_IDX]:`

それ以外でidxが[SUBTITLE_IDX]と等しい場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:211

原文：

```text
            shape.text = "Presentation Title | Date"
```

日本語：

`shape.text = "Presentation Title | Date"`

shape.textに「Presentation Title | Date」（発表タイトル | 日付）を設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:214

原文：

```text
## Example: Content Slide
```

日本語：

## 例: コンテンツ スライド


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:217

原文：

```text
slide = prs.slides.add_slide(prs.slide_layouts[[CONTENT_IDX]])
```

日本語：

`slide = prs.slides.add_slide(prs.slide_layouts[[CONTENT_IDX]])`

[CONTENT_IDX]を使うコンテンツ用レイアウトからスライドを追加するコード例。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:218

原文：

```text
for shape in slide.shapes:
```

日本語：

`for shape in slide.shapes:`

slide.shapesに含まれる各shapeを順に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:219

原文：

```text
    if hasattr(shape, 'placeholder_format'):
```

日本語：

`if hasattr(shape, 'placeholder_format'):`

shapeがplaceholder_format属性を持つ場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:220

原文：

```text
        ph_type = shape.placeholder_format.type
```

日本語：

`ph_type = shape.placeholder_format.type`

プレースホルダーの種類をph_typeへ代入する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:221

原文：

```text
        idx = shape.placeholder_format.idx
```

日本語：

`idx = shape.placeholder_format.idx`

プレースホルダーのidxを取得する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:222

原文：

```text
        if ph_type == 1:
```

日本語：

`if ph_type == 1:`

ph_typeが1の場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:223

原文：

```text
            shape.text = "Executive Summary"
```

日本語：

`shape.text = "Executive Summary"`

shape.textに「Executive Summary」（要旨）を設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:224

原文：

```text
        elif idx == [BODY_IDX]:
```

日本語：

`elif idx == [BODY_IDX]:`

それ以外でidxが[BODY_IDX]と等しい場合に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:225

原文：

```text
            tf = shape.text_frame
```

日本語：

`tf = shape.text_frame`

shapeのテキストフレームをtfへ代入する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:226

原文：

```text
            for para in tf.paragraphs:
```

日本語：

`for para in tf.paragraphs:`

tf内の各段落paraを順に処理する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:228

原文：

```text
            content = [
```

日本語：

`content = [`

contentのリスト定義を開始する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:229

原文：

```text
                ("Key Findings", 0),
```

日本語：

`("Key Findings", 0),`

「Key Findings」（主な調査結果）をレベル0で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:230

原文：

```text
                ("Revenue grew 40% YoY to $50M", 1),
```

日本語：

`("Revenue grew 40% YoY to $50M", 1),`

「売上高は前年同期比40%増の$50M」という文をレベル1で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:231

原文：

```text
                ("Expanded to 3 new markets", 1),
```

日本語：

`("Expanded to 3 new markets", 1),`

「3つの新市場へ進出」という文をレベル1で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:232

原文：

```text
                ("Recommendation", 0),
```

日本語：

`("Recommendation", 0),`

「Recommendation」（提案）をレベル0で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:233

原文：

```text
                ("Proceed with strategic initiative", 1),
```

日本語：

`("Proceed with strategic initiative", 1),`

「戦略的施策を進める」という文をレベル1で指定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:235

原文：

```text
            tf.paragraphs[0].text = content[0][0]
```

日本語：

`tf.paragraphs[0].text = content[0][0]`

先頭段落のテキストをcontent[0][0]に設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:236

原文：

```text
            tf.paragraphs[0].level = content[0][1]
```

日本語：

`tf.paragraphs[0].level = content[0][1]`

先頭段落の階層レベルをcontent[0][1]に設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:237

原文：

```text
            for text, level in content[1:]:
```

日本語：

`for text, level in content[1:]:`

contentの2件目以降からtextとlevelを取り出して繰り返す。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:238

原文：

```text
                p = tf.add_paragraph()
```

日本語：

`p = tf.add_paragraph()`

新しい段落を追加し、pに代入する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:239

原文：

```text
                p.text = text
```

日本語：

`p.text = text`

pのテキストをtextに設定する。


### plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md:240

原文：

```text
                p.level = level
```

日本語：

`p.level = level`

pの階層レベルをlevelに設定する。
