---
name: ppt-template-creator
description: Creates self-contained PPT template SKILLS (not presentations) from user-provided PowerPoint templates. Use ONLY when a user wants to create a reusable skill from their template. For creating actual presentations, use the pptx skill instead.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：ユーザーが提供した PowerPoint テンプレートから、自己完結型の PPT テンプレート スキル (プレゼンテーションではない) を作成します。ユーザーがテンプレートから再利用可能なスキルを作成したい場合にのみ使用してください。実際のプレゼンテーションを作成するには、代わりに pptx スキルを使用してください。

<a id="ppt-template-creator"></a>
# PPTテンプレート作成者

**このスキルはプレゼンテーションではなくスキルを作成します。** ユーザーが PowerPoint テンプレートを後でプレゼンテーションを生成できる再利用可能なスキルに変換したい場合にこれを使用します。ユーザーがプレゼンテーションを作成したいだけの場合は、代わりに `pptx` スキルを使用してください。

生成されるスキルには次のものが含まれます。
- `assets/template.pptx` - テンプレート ファイル
- `SKILL.md` - 完全な手順 (このメタ スキルへの参照は必要ありません)

**一般的なスキル構築のベスト プラクティス**については、`skill-creator` スキルを参照してください。このスキルは、PPT 固有のパターンに焦点を当てています。

<a id="workflow"></a>
## ワークフロー

1. **ユーザーがテンプレートを提供** (.pptx または .potx)
2. **テンプレートを分析** - レイアウト、プレースホルダー、寸法を抽出します
3. **スキルの初期化** - `skill-creator` スキルを使用してスキル構造を設定します
4. **テンプレートを追加** - .pptx を `assets/template.pptx` にコピーします
5. **SKILL.md を作成します** - PPT 固有の詳細を含む以下のテンプレートに従います
6. **サンプルの作成** - 検証するサンプル プレゼンテーションを生成します。
7. **パッケージ** - `skill-creator` スキルを使用して .skill ファイルにパッケージ化します

<a id="step-2-analyze-template"></a>
## ステップ 2: テンプレートを分析する

**重要: 正確なプレースホルダーの位置を抽出します** - これにより、コンテンツ領域の境界が決まります。

```python
from pptx import Presentation

prs = Presentation(template_path)
print(f"Dimensions: {prs.slide_width/914400:.2f}\" x {prs.slide_height/914400:.2f}\"")
print(f"Layouts: {len(prs.slide_layouts)}")

for idx, layout in enumerate(prs.slide_layouts):
    print(f"\n[{idx}] {layout.name}:")
    for ph in layout.placeholders:
        try:
            ph_idx = ph.placeholder_format.idx
            ph_type = ph.placeholder_format.type
            # IMPORTANT: Extract exact positions in inches
            left = ph.left / 914400
            top = ph.top / 914400
            width = ph.width / 914400
            height = ph.height / 914400
            print(f"    idx={ph_idx}, type={ph_type}")
            print(f"        x={left:.2f}\", y={top:.2f}\", w={width:.2f}\", h={height:.2f}\"")
        except:
            pass
```

**文書化すべき主な測定値:**
- **タイトルの位置**: タイトルのプレースホルダーはどこに配置されますか?
- **サブタイトル/説明**: サブタイトル行はどこですか?
- **フッター プレースホルダー**: フッター/ソースはどこに表示されますか?
- **コンテンツエリア**: サブタイトルとフッターの間のスペースがコンテンツエリアです。

<a id="finding-the-true-content-start-position"></a>
### 真のコンテンツの開始位置を見つける

**重要:** コンテンツ領域は、必ずしもサブタイトルプレースホルダーの直後から始まるとは限りません。多くのテンプレートには、サブタイトルとコンテンツ領域の間に視覚的な境界線、線、または予約されたスペースがあります。

**最良のアプローチ:** OBJECT プレースホルダーを含むレイアウト 2 または同様の「コンテンツ」レイアウトを確認します。このプレースホルダーの `y` 位置は、コンテンツが実際に開始される場所を示します。

```python
# Find the OBJECT placeholder to determine true content start
for idx, layout in enumerate(prs.slide_layouts):
    for ph in layout.placeholders:
        try:
            if ph.placeholder_format.type == 7:  # OBJECT type
                top = ph.top / 914400
                print(f"Layout [{idx}] {layout.name}: OBJECT starts at y={top:.2f}\"")
                # This y value is where your content should start!
        except:
            pass
```

**例:** テンプレートには次のものが含まれる場合があります。
- サブタイトルは y=1.38" で終わります
- ただし、y=1.90" から始まる OBJECT プレースホルダー
- ギャップ (0.52 インチ) は境界線/線用に予約されています - **そこにコンテンツを配置しないでください**

サブタイトルの終了位置ではなく、OBJECT プレースホルダーの `y` 位置をコンテンツの開始位置として使用します。

<a id="step-5-write-skillmd"></a>
## ステップ5: SKILL.mdを書き込む

生成されたスキルは次の構造になっている必要があります。
```
[company]-ppt-template/
├── SKILL.md
└── assets/
    └── template.pptx
```

<a id="generated-skillmd-template"></a>
### 生成されたSKILL.mdテンプレート

生成された SKILL.md は、すべての命令が埋め込まれた **自己完結型** である必要があります。このテンプレートを使用して、分析から得られた括弧内の値を入力します。

````markdown
---
name: [company]-ppt-template
description: [Company] PowerPoint template for creating presentations. Use when creating [Company]-branded pitch decks, board materials, or client presentations.
---

# [Company] PPT Template

Template: `assets/template.pptx` ([WIDTH]" x [HEIGHT]", [N] layouts)

## Creating Presentations

```python
from pptx import Presentation

prs = Presentation("path/to/skill/assets/template.pptx")

# DELETE all existing slides first
while len(prs.slides) > 0:
    rId = prs.slides._sldIdLst[0].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[0]

# Add slides from layouts
slide = prs.slides.add_slide(prs.slide_layouts[LAYOUT_IDX])
```

## Key Layouts

| Index | Name | Use For |
|-------|------|---------|
| [0] | [Layout Name] | [Cover/title slide] |
| [N] | [Layout Name] | [Content with bullets] |
| [N] | [Layout Name] | [Two-column layout] |

## Placeholder Mapping

**CRITICAL: Include exact positions (x, y coordinates) for each placeholder.**

### Layout [N]: [Name]
| idx | Type | Position | Use |
|-----|------|----------|-----|
| [idx] | TITLE (1) | y=[Y]" | Slide title |
| [idx] | BODY (2) | y=[Y]" | Subtitle/description |
| [idx] | BODY (2) | y=[Y]" | Footer |
| [idx] | BODY (2) | y=[Y]" | Source/notes |

### Content Area Boundaries

**Document the safe content area for custom shapes/tables/charts:**

```
Content Area (for Layout [N]):
- Left margin: [X]" (content starts here)
- Top: [Y]" (below subtitle placeholder)
- Width: [W]"
- Height: [H]" (ends before footer)

For 4-quadrant layouts:
- Left column: x=[X]", width=[W]"
- Right column: x=[X]", width=[W]"
- Top row: y=[Y]", height=[H]"
- Bottom row: y=[Y]", height=[H]"
```

**Why this matters:** Custom content (textboxes, tables, charts) must stay within these boundaries to avoid overlapping with template placeholders like titles, footers, and source lines.

## Filling Content

**Do NOT add manual bullet characters** - slide master handles formatting.

```python
# Fill title
for shape in slide.shapes:
    if hasattr(shape, 'placeholder_format'):
        if shape.placeholder_format.type == 1:  # TITLE
            shape.text = "Slide Title"

# Fill content with hierarchy (level 0 = header, level 1 = bullet)
for shape in slide.shapes:
    if hasattr(shape, 'placeholder_format'):
        idx = shape.placeholder_format.idx
        if idx == [CONTENT_IDX]:
            tf = shape.text_frame
            for para in tf.paragraphs:
                para.clear()

            content = [
                ("Section Header", 0),
                ("First bullet point", 1),
                ("Second bullet point", 1),
            ]

            tf.paragraphs[0].text = content[0][0]
            tf.paragraphs[0].level = content[0][1]
            for text, level in content[1:]:
                p = tf.add_paragraph()
                p.text = text
                p.level = level
```

## Example: Cover Slide

```python
slide = prs.slides.add_slide(prs.slide_layouts[[COVER_IDX]])
for shape in slide.shapes:
    if hasattr(shape, 'placeholder_format'):
        idx = shape.placeholder_format.idx
        if idx == [TITLE_IDX]:
            shape.text = "Company Name"
        elif idx == [SUBTITLE_IDX]:
            shape.text = "Presentation Title | Date"
```

## Example: Content Slide

```python
slide = prs.slides.add_slide(prs.slide_layouts[[CONTENT_IDX]])
for shape in slide.shapes:
    if hasattr(shape, 'placeholder_format'):
        ph_type = shape.placeholder_format.type
        idx = shape.placeholder_format.idx
        if ph_type == 1:
            shape.text = "Executive Summary"
        elif idx == [BODY_IDX]:
            tf = shape.text_frame
            for para in tf.paragraphs:
                para.clear()
            content = [
                ("Key Findings", 0),
                ("Revenue grew 40% YoY to $50M", 1),
                ("Expanded to 3 new markets", 1),
                ("Recommendation", 0),
                ("Proceed with strategic initiative", 1),
            ]
            tf.paragraphs[0].text = content[0][0]
            tf.paragraphs[0].level = content[0][1]
            for text, level in content[1:]:
                p = tf.add_paragraph()
                p.text = text
                p.level = level
```
````

<a id="step-6-create-example-output"></a>
## ステップ 6: 出力例を作成する

サンプル プレゼンテーションを生成して、スキルの動作を検証します。参照用にスキルと一緒に保存してください。

<a id="ppt-specific-rules-for-generated-skills"></a>
## 生成されるスキルに対する PPT 固有のルール

1. **assets/** 内のテンプレート - 常に .pptx ファイルをバンドルします
2. **自己完結型 SKILL.md** - すべての命令が埋め込まれており、外部参照はありません
3. **手動の箇条書きはありません** - 階層には `paragraph.level` を使用してください
4. **最初にスライドを削除してください** - 新しいスライドを追加する前に、必ず既存のスライドをクリアしてください
5. **プレースホルダーをidxで記録する** - プレースホルダーの idx 値はテンプレート固有です
