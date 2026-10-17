> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/investment-banking/skills/pitch-deck/reference/xml-reference.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="powerpoint-xml-reference"></a>
# PowerPoint XML リファレンス

このファイルには、プログラムによる PowerPoint 編集用の XML パターンが含まれています。 OOXML 形式を直接操作する場合は、これらのパターンを使用します。

**注:** 例の色の値 (`E67E22`、`D35400` など) はプレースホルダーです。テンプレートのブランドカラーに置き換えます。

---

<a id="-when-to-use-this-reference"></a>
## ⚠️ このリファレンスを使用する場合

**Python-pptx は次の目的で使用します。**
- 新しいテーブルの作成 (セルの構造と関係を自動的に処理します)
- テキストボックスの追加
- 画像の挿入
- ほとんどの形状作成
- python-pptx が API を提供するすべての操作

**XML の直接編集は次の場合にのみ使用してください。**
- python-pptx が公開しない既存の要素のプロパティを変更する
- python-pptx によるテーブル作成後のセルの書式設定の微調整
- 特定の形状プロパティの調整は python-pptx API では利用できません

**次の場合には直接 XML を決して使用しないでください**
- テーブルを最初から作成する (リレーションシップ管理はエラーが発生しやすく、ファイルが破損する可能性があります)
- 初期シェイプの作成 (シェイプ ID の衝突リスク)
- python-pptx 経由で達成できることはすべて

このファイルの XML パターンは、**参照および対象を絞った変更** 用であり、大規模な要素構築のためのものではありません。

---

<a id="xml-editing-risks"></a>
## XML編集のリスク

XML の直接編集は、慎重に行わないと PowerPoint ファイルを破損する可能性があります。
- PowerPoint XML には相互依存関係があります (リレーションシップ ファイル、コンテンツ タイプ)
- 無効な XML またはリレーションシップが欠落していると、ファイル全体が破損する可能性があります
- 図形IDは各スライド内で一意である必要があります

**常にバックアップ コピーを使用して作業します**。元のファイルを直接編集しないでください。

---

<a id="contents"></a>
## 内容
- [テーブルの実装](#table-implementation)
- [矢印の形状](#arrow-shapes)
- [テキストボックス](#text-boxes)
- [塗りつぶしのあるシェイプ](#shapes-with-fill)
- [画像の挿入](#image-insertion)
- [コネクタライン](#connector-lines)
- [単位変換](#unit-conversions)

---

<a id="table-implementation"></a>
## テーブルの実装

<a id="critical-verify-tables-are-actual-table-objects"></a>
### 重要: テーブルが実際のテーブル オブジェクトであることを確認してください

テーブルを作成した後、それが区切り文字付きのテキストではなく、実際のテーブル オブジェクトであることを確認する必要があります。

**プログラムによる検証 (python-pptx):**
```python
for shape in slide.shapes:
    if shape.has_table:
        print(f"✓ Found table: {len(shape.table.rows)} rows, {len(shape.table.columns)} columns")
```

**視覚的な検証 (エクスポートされた画像):**
- コンテンツの長さに関係なく、列が完全に整列します
- セルの境界線が一貫している
- テーブルを選択すると、すべてのセルが単位として選択されます

**失敗インジケーター - テーブルではなくテキストを作成しました:**
- `|` 文字が値の間に表示されます
- コンテンツの長さが異なると列の位置がずれる
- スペースに使用されるタブ文字 (`\t`)
- 表のように配置された複数のテキスト ボックス

テキストベースの「表」は受信者が編集できず、フォントが変更されると位置がずれてしまい、素人の仕事であることがわかります。ピッチデッキでは、パイプ/タブで区切られた表形式データの許容可能な使用例はありません。

---

<a id="basic-table-structure"></a>
### 基本的なテーブル構造

```xml
<a:tbl>
  <a:tblPr firstRow="1" bandRow="1">
    <a:tableStyleId>{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}</a:tableStyleId>
  </a:tblPr>
  <a:tblGrid>
    <a:gridCol w="2000000"/>  <!-- Source column - width in EMUs -->
    <a:gridCol w="1200000"/>  <!-- 2024 Size column -->
    <a:gridCol w="1200000"/>  <!-- CAGR column -->
    <a:gridCol w="1200000"/>  <!-- 2030 Projection column -->
  </a:tblGrid>
  <!-- Row definitions follow -->
</a:tbl>
```

<a id="table-row-with-cells"></a>
### セルを含む表の行

```xml
<a:tr h="370840">  <!-- Row height in EMUs -->
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="l"/>  <!-- Left alignment for text columns -->
        <a:r>
          <a:rPr lang="en-US" sz="1000" b="0"/>
          <a:t>Grand View Research</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr/>
  </a:tc>
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="ctr"/>  <!-- Center alignment for numeric columns -->
        <a:r>
          <a:rPr lang="en-US" sz="1000"/>
          <a:t>22.1</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr/>
  </a:tc>
  <!-- Additional cells... -->
</a:tr>
```

<a id="header-row-styling"></a>
### ヘッダー行のスタイル設定

```xml
<a:tr h="370840">
  <a:tc>
    <a:txBody>
      <a:bodyPr/>
      <a:lstStyle/>
      <a:p>
        <a:pPr algn="l"/>
        <a:r>
          <a:rPr lang="en-US" sz="1000" b="1">  <!-- Bold for headers -->
            <a:solidFill>
              <a:srgbClr val="FFFFFF"/>  <!-- White text -->
            </a:solidFill>
          </a:rPr>
          <a:t>Source</a:t>
        </a:r>
      </a:p>
    </a:txBody>
    <a:tcPr>
      <a:solidFill>
        <a:srgbClr val="E67E22"/>  <!-- Orange background -->
      </a:solidFill>
    </a:tcPr>
  </a:tc>
  <!-- Additional header cells... -->
</a:tr>
```

---

<a id="arrow-shapes"></a>
## 矢印の形

<a id="right-arrow-shape"></a>
### 右矢印の形状

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="10" name="Arrow Right"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="3000000" y="2500000"/>  <!-- Position in EMUs -->
      <a:ext cx="500000" cy="300000"/>   <!-- Size in EMUs -->
    </a:xfrm>
    <a:prstGeom prst="rightArrow">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>  <!-- Arrow fill color -->
    </a:solidFill>
    <a:ln>
      <a:noFill/>  <!-- No outline -->
    </a:ln>
  </p:spPr>
</p:sp>
```

<a id="down-arrow-shape"></a>
### 下矢印の形

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="11" name="Arrow Down"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="2500000" y="3000000"/>
      <a:ext cx="300000" cy="500000"/>
    </a:xfrm>
    <a:prstGeom prst="downArrow">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>
    </a:solidFill>
  </p:spPr>
</p:sp>
```

<a id="chevron-shape"></a>
### シェブロン形状

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="12" name="Chevron"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="3000000" y="2500000"/>
      <a:ext cx="400000" cy="600000"/>
    </a:xfrm>
    <a:prstGeom prst="chevron">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>
    </a:solidFill>
  </p:spPr>
</p:sp>
```

---

<a id="text-boxes"></a>
## テキストボックス

<a id="basic-text-box"></a>
### 基本テキストボックス

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="5" name="TextBox 4"/>
    <p:cNvSpPr txBox="1"/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="500000" y="1500000"/>
      <a:ext cx="4000000" cy="500000"/>
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
    <a:noFill/>
  </p:spPr>
  <p:txBody>
    <a:bodyPr wrap="square" rtlCol="0">
      <a:spAutoFit/>
    </a:bodyPr>
    <a:lstStyle/>
    <a:p>
      <a:r>
        <a:rPr lang="en-US" sz="1400" dirty="0"/>
        <a:t>Text content here</a:t>
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

<a id="text-box-with-bullet-points"></a>
### 箇条書きのテキスト ボックス

```xml
<p:txBody>
  <a:bodyPr wrap="square">
    <a:spAutoFit/>
  </a:bodyPr>
  <a:lstStyle/>
  <a:p>
    <a:pPr marL="342900" indent="-342900">
      <a:buFont typeface="Wingdings" panose="05000000000000000000" pitchFamily="2" charset="2"/>
      <a:buChar char="&#252;"/>  <!-- Checkmark character -->
    </a:pPr>
    <a:r>
      <a:rPr lang="en-US" sz="1400" dirty="0"/>
      <a:t>First bullet point</a:t>
    </a:r>
  </a:p>
  <a:p>
    <a:pPr marL="342900" indent="-342900">
      <a:buFont typeface="Wingdings" panose="05000000000000000000" pitchFamily="2" charset="2"/>
      <a:buChar char="&#252;"/>
    </a:pPr>
    <a:r>
      <a:rPr lang="en-US" sz="1400" dirty="0"/>
      <a:t>Second bullet point</a:t>
    </a:r>
  </a:p>
</p:txBody>
```

<a id="text-with-white-color-for-dark-backgrounds"></a>
### 白色のテキスト (暗い背景用)

```xml
<a:r>
  <a:rPr lang="en-US" sz="1000" b="1" i="1" dirty="0">
    <a:solidFill>
      <a:srgbClr val="FFFFFF"/>  <!-- White text -->
    </a:solidFill>
  </a:rPr>
  <a:t>White text on colored background</a:t>
</a:r>
```

---

<a id="shapes-with-fill"></a>
## 塗りつぶしのある形状

<a id="rectangle-with-solid-fill"></a>
### 塗りつぶされた長方形

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="20" name="Rectangle 19"/>
    <p:cNvSpPr/>
    <p:nvPr/>
  </p:nvSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="500000" y="2500000"/>
      <a:ext cx="1000000" cy="2000000"/>
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
    <a:solidFill>
      <a:srgbClr val="E67E22"/>  <!-- Orange fill -->
    </a:solidFill>
    <a:ln w="12700">  <!-- Border width -->
      <a:solidFill>
        <a:srgbClr val="D35400"/>  <!-- Darker border -->
      </a:solidFill>
    </a:ln>
  </p:spPr>
  <p:txBody>
    <a:bodyPr rtlCol="0" anchor="ctr"/>  <!-- Vertically centered text -->
    <a:lstStyle/>
    <a:p>
      <a:pPr algn="ctr"/>  <!-- Horizontally centered -->
      <a:r>
        <a:rPr lang="en-US" sz="1600" b="1">
          <a:solidFill>
            <a:srgbClr val="FFFFFF"/>
          </a:solidFill>
        </a:rPr>
        <a:t>Label Text</a:t>
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

---

<a id="image-insertion"></a>
## 画像の挿入

<a id="adding-image-to-slide"></a>
### スライドに画像を追加する

```xml
<p:pic>
  <p:nvPicPr>
    <p:cNvPr id="99" name="Company Logo"/>
    <p:cNvPicPr>
      <a:picLocks noChangeAspect="1"/>
    </p:cNvPicPr>
    <p:nvPr/>
  </p:nvPicPr>
  <p:blipFill>
    <a:blip r:embed="rIdLogo"/>  <!-- Reference to relationship ID -->
    <a:stretch>
      <a:fillRect/>
    </a:stretch>
  </p:blipFill>
  <p:spPr>
    <a:xfrm>
      <a:off x="10800000" y="200000"/>  <!-- Top-right position -->
      <a:ext cx="800000" cy="600000"/>   <!-- Logo dimensions -->
    </a:xfrm>
    <a:prstGeom prst="rect">
      <a:avLst/>
    </a:prstGeom>
  </p:spPr>
</p:pic>
```

<a id="adding-image-relationship"></a>
### 画像の関係を追加する

`ppt/slides/_rels/slideN.xml.rels`:

```xml
<Relationship Id="rIdLogo" 
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" 
  Target="../media/logo.png"/>
```

---

<a id="connector-lines"></a>
## コネクタライン

<a id="straight-connector"></a>
### ストレートコネクタ

```xml
<p:cxnSp>
  <p:nvCxnSpPr>
    <p:cNvPr id="15" name="Straight Connector 14"/>
    <p:cNvCxnSpPr>
      <a:cxnSpLocks/>
    </p:cNvCxnSpPr>
    <p:nvPr/>
  </p:nvCxnSpPr>
  <p:spPr>
    <a:xfrm>
      <a:off x="500000" y="2500000"/>
      <a:ext cx="5000000" cy="0"/>  <!-- Horizontal line -->
    </a:xfrm>
    <a:prstGeom prst="line">
      <a:avLst/>
    </a:prstGeom>
    <a:ln w="12700">
      <a:solidFill>
        <a:srgbClr val="E67E22"/>
      </a:solidFill>
    </a:ln>
  </p:spPr>
</p:cxnSp>
```

<a id="dashed-line"></a>
### 破線

```xml
<p:spPr>
  <a:xfrm>
    <a:off x="500000" y="4500000"/>
    <a:ext cx="5000000" cy="0"/>
  </a:xfrm>
  <a:prstGeom prst="line">
    <a:avLst/>
  </a:prstGeom>
  <a:ln w="12700">
    <a:solidFill>
      <a:srgbClr val="E67E22"/>
    </a:solidFill>
    <a:prstDash val="dash"/>  <!-- Dashed style -->
  </a:ln>
</p:spPr>
```

---

<a id="unit-conversions"></a>
## 単位の変換

| ユニット | ユニットあたりの EMU |
|------|---------------|
| 1インチ | 914400 |
| 1cm | 360000 |
| 1ポイント | 12700 |
| 1ピクセル（96DPI） | 9525 |

<a id="common-slide-dimensions-169"></a>
### 共通スライド寸法（16:9）

- 幅: 12192000 EMU (13.333 インチ)
- 高さ: 6858000 EMU (7.5 インチ)

<a id="typical-element-positions"></a>
### 一般的な要素の位置

| 要素 | X 位置 | Y 位置 |
|---------|------------|------------|
| ロゴ（右上） | 10800000 | 200000 |
| タイトル | 342583 | 286603 |
| サブタイトル | 402591 | 1767390 |
| フッター | 342583 | 6435334 |
