---
name: fsi-strip-profile
description: |
  Creates professional investment banking strip profiles (company profiles) for pitch books, deal materials, and client presentations. Generates 1-4 information-dense slides with quadrant layouts, charts, and tables.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/investment-banking/skills/strip-profile/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="workflow"></a>
## ワークフロー

<a id="1-clarify-requirements"></a>
### 1. 要件を明確にする
- **ユーザーに質問**: シングル スライドかマルチ スライド (3 ～ 4 スライド)?
- **ユーザーに質問します**: 強調すべき特定の重点分野やトピックはありますか?
- **ユーザーが確認した後のみ**、調査に進みます

<a id="2-research--planning"></a>
### 2.調査と企画
**データソース:**
- **主な**: 企業提出書類 (BamSEC、SEC EDGAR - 「項目 1. ビジネス」、MD&A)、投資家向けプレゼンテーション、企業 Web サイト
- **市場データ**: ブルームバーグ、ファクトセット、CapIQ（株価、株式数、時価総額、純負債、EV、所有権)
- **推定**: NTM 収益、EBITDA、EPS に関する FactSet/CapIQ コンセンサス
- **ニュース**: 過去 90 日間のプレスリリース、M&A 活動、ガイダンスの変更

**必要なメトリクス:**
- **財務**: ±3 年間の収益、EBITDA、利益率 (%)、EPS、FCF
- **評価**: 時価総額、EV、EV/収益、EV/EBITDA、PER倍数
- **成長率**: 前年比成長率 (%)
- **所有権**: 上位5株主と各保有比率
- **セグメント**: 製品構成および/または地理的構成 (% 内訳)

**正規化:**
- すべての金額を一貫した通貨に変換する
- 一貫してスケールする (全体で 百万ドルまたは十億ドル、混在しない)

**構築前:**
- 項目ごとに 4 ～ 5 個の箇条書きを含むアウトラインをチャットに表示します (実際の数字、プレースホルダーなし)
- スタイルの選択を表示する: 各データセットのフォント、色 (16 進コード)、グラフの種類
- ユーザーと方針を確認する: 「この概要とビジュアル戦略はあなたのビジョンと一致していますか?」

<a id="3-slide-by-slide-creation"></a>
### 3. スライドごとの作成
**重要: 次のスライドに進む前に、一度に 1 つのスライドを作成し、ユーザーの承認を得る必要があります。**

**各スライドについて:**
1. PptxGenJS を使用してこの 1 つのスライドのみを作成します
2. **必須: レビューのために画像に変換** - スライドを視覚的に確認できるように、スライドを画像に変換する必要があります。
   ```bash
   soffice --headless --convert-to pdf presentation.pptx
   pdftoppm -jpeg -r 150 -f 1 -l 1 presentation.pdf slide
   ```
3. **必須の視覚的レビュー**: 続行する前に、レンダリングされたスライド イメージを慎重に検査する必要があります。
   - **テキストの重複チェック**: すべてのテキスト要素をスキャンします - ラベル、箇条書き、またはタイトルが互いに衝突していませんか?
   - **テキストの切り取りチェック**: 境界でテキストが切り詰められていませんか?すべての単語が完全に表示されていますか?
   - **チャート境界チェック**: チャートはコンテナ内に収まっていますか?すべての軸ラベルが完全に表示されていますか?
   - **象限の整合性**: 1 つの象限のコンテンツが隣接する象限に流れ込んでいますか?
4. **オーバーラップまたはカットオフが検出された場合**: 次の戦略を順番に使用して直ちに修正します。
   - **最初**: フォント サイズを小さくします (1 ～ 2 ポイント下げます)。
   - **2 番目**: テキストを短くします (短縮し、重要度の低い情報を削除します)。
   - **3 番目**: 要素の位置またはコンテナのサイズを調整する
   - **再レンダリングして再度確認します** - すべてのテキストがきれいに収まるまで続行しないでください
5. ダウンロード リンクを含むスライド画像をユーザーに表示する
6. **次のスライドを作成する前に、停止して明示的なユーザーの承認を待ちます**。ユーザーが確認するまで続行しないでください。

**すべてのページで次の特定の問題を確認する必要があります:**
- 表の行がその下のテキストと衝突する
- グラフの X 軸のラベルが下部で切り取られている
- 長い箇条書きが隣接するコンテンツに折り返される
- 象限のコンテンツが隣接する象限に滲み出る
- タイトルテキストが以下の内容と重なっています
- グラフ要素と重なる凡例テキスト
- フッター/ソース テキストがメイン コンテンツと衝突する

---

<a id="slide-format-requirements"></a>
## スライドのフォーマット要件

<a id="information-density-is-critical"></a>
### 情報密度は重要です

**最大の目標は、情報密度を最大化することです。** 多忙な経営幹部は、会社のストーリー全体を 30 秒で理解する必要があります。すべての象限を容量まで満たします。

**象限ごとの目標:**
- **会社概要**: 最低 6 ～ 8 個の箇条書き (本社、設立、従業員、CEO/CFO、時価総額、ティッカー、業界、主要な統計)
- **ビジネスとポジショニング**: 6 ～ 8 項目 (収益要因、製品、市場シェア %、競争堀、顧客数、地理的構成)
- **主要な財務内容**: 8 ～ 10 行の表 OR グラフ + 4 ～ 5 つの主要な指標 (収益、EBITDA、利益率、EPS、FCF、成長率、評価倍率)
- **第 4 象限**: 5 ～ 7 の箇条書き (所有権 %、最近のM&A、事業動向、株価や業績を動かす材料)

**情報パッキング手法:**
- 関連する事実を結合します: 「本社: テキサス州オースティン、設立: 2003 年、従業員数 14 万人」
- 必ず数字を含めてください: 「多額の収益」ではなく「500 億ドルの収益」
- コンテキストを追加: 「EBITDA マージン: 25% (業界平均 18% に対して)」
- 前年比の変化を含める: 「収益: 1 億 2,500 万ドル (前年比 +28%)」
- パーセンテージを使用: 「エンタープライズ: 収益の 62%」

**象限がまばらに見える場合は、さらに追加します:**
- セグメントの内訳 (%)
- 地域別の収益分割
- 顧客集中度 (上位 10 = X%)
- 最近獲得した契約と、その金額
- ガイダンスとコンセンサス
- インサイダー所有権の割合

**行間隔 - セクションごとに 1 つのテキストボックスを使用します:**
```python
def add_section(slide, x, y, w, header_text, bullets, header_size=10, bullet_size=8):
    """Header + bullets in single textbox with natural spacing"""
    tb = slide.shapes.add_textbox(x, y, w, Inches(len(bullets) * 0.18 + 0.3))
    tf = tb.text_frame
    tf.word_wrap = True

    # Header paragraph
    p = tf.paragraphs[0]
    p.text = header_text
    p.font.bold = True
    p.font.size = Pt(header_size)
    p.font.color.rgb = RGBColor(0, 51, 102)
    p.space_after = Pt(6)  # Small gap after header

    # Bullet paragraphs
    for bullet in bullets:
        p = tf.add_paragraph()
        p.text = bullet
        p.font.size = Pt(bullet_size)
        p.space_after = Pt(3)
    return tb
```

**重要な間隔の原則:**
- ヘッダーと箇条書きを同じテキストボックスに配置します (別個のヘッダー テキストボックスはありません)
- ヘッダーの後に `space_after = Pt(6)` を使用し、箇条書きの間に `Pt(3)` を使用します。
- ギャップをハードコーディングしないでください - 段落間隔によって自然に処理されます
- コンテンツがオーバーフローする場合は、コンテンツを削除するのではなく、フォントを 1pt 減らします。

---

- **3 ～ 4 枚の密度の高いスライド** - 四分円、列、表、グラフを使用します
- **すべての本文テキストに箇条書き** - 段落は使用しないでください。 **セクションごとにすべての箇条書きを含む 1 つのテキストボックスを使用します** - 箇条書きごとに個別のテキストボックスを作成しないでください。 PptxGenJS の箇条書き形式を使用します。
  ```javascript
  // CORRECT: Single textbox with bullet list - each array item becomes a bullet
  // Position in top-left quadrant (Company Overview) - after header with accent bar
  slide.addText(
    [
      { text: 'Headquarters: Austin, Texas; Founded 2003', options: { bullet: { indent: 10 }, breakLine: true } },
      { text: 'Employees: 140,000+ globally across 6 continents', options: { bullet: { indent: 10 }, breakLine: true } },
      { text: 'CEO: Elon Musk; CFO: Vaibhav Taneja', options: { bullet: { indent: 10 }, breakLine: true } },
      { text: 'Market Cap: $850B (#6 globally by market cap)', options: { bullet: { indent: 10 }, breakLine: true } },
      { text: 'Segments: Automotive (85%), Energy (10%), Services (5%)', options: { bullet: { indent: 10 } } }
    ],
    { x: 0.45, y: 0.95, w: 4.5, h: 2.6, fontSize: 11, fontFace: 'Arial', valign: 'top', paraSpaceAfter: 6 }
  );

  // WRONG: Multiple separate textboxes for each bullet - causes alignment issues
  // slide.addText('Headquarters: Austin', { x: 0.5, y: 1.0, bullet: true });
  ```

  **箇条書きの書式設定のヒント:**
  - `bullet: { indent: 10 }` - 箇条書きのインデントを制御します (小さく = きつく)
  - `paraSpaceAfter: 6` - 各段落後のスペース (ポイント単位)
  - 複数の関連する事実を各箇条書きに詰め込みます (例: 「本社: オースティン、設立: 2003」)
  - 情報密度の具体的な数値とパーセンテージを含める
- **タイトルケース**（英語の主要語の頭文字を大文字にし、全文を大文字にはしない）、左揃え
- **表を含むあらゆる場所で一貫したフォント**
- **会社のブランドの色** - スライドを作成する前に、Web 検索で実際のブランドの色を調査する必要があります。色を推測したり仮定したりしないでください。
- **ブランドガイドラインが提供されている場合は、それに従う**

<a id="visual-reference"></a>
### ビジュアルリファレンス
レイアウトのインスピレーションについては、`examples/Nike_Strip_Profile_Example.pptx` を参照してください。各社のブランドに合わせたカラーを採用。

---

<a id="first-page-layout"></a>
## 最初のページのレイアウト

多忙なエグゼクティブのための「30秒理解テスト」に合格しなければなりません。

<a id="slide-setup-critical"></a>
### スライドのセットアップ (重要)
**4:3 アスペクト比を使用** (標準 IB ピッチブック形式):
```javascript
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_4x3';  // 10" wide × 7.5" tall - MUST USE THIS
```

<a id="slide-coordinate-system"></a>
### スライド座標系
PptxGenJS はインチを使用します。 4:3 スライド = **幅 10 インチ × 高さ 7.5 インチ**。
- **x**: 左端からの水平位置 (0 = 左、10 = 右)
- **y**: 上端からの垂直位置 (0 = 上、7.5 = 下)
- **コンテンツは境界内に収まる必要があります** - すべての辺に 0.3 インチの余白を残します

<a id="first-page-positioning-in-inches"></a>
### 最初のページの位置 (インチ単位)
```
┌─────────────────────────────────────────────────────────────────┐
│ y=0.2  Title: Company Name (Ticker)                             │
├────────────────────────────┬────────────────────────────────────┤
│ y=0.6  Company Overview    │ y=0.6  Business & Positioning      │
│ x=0.3, w=4.7               │ x=5.0, w=4.7                       │
│ h=3.0                      │ h=3.0                              │
├────────────────────────────┼────────────────────────────────────┤
│ y=3.7  Key Financials      │ y=3.7  Stock/Recent Developments   │
│ x=0.3, w=4.7               │ x=5.0, w=4.7                       │
│ h=3.5                      │ h=3.5                              │
└────────────────────────────┴────────────────────────────────────┘
                                                            y=7.5
```

<a id="title-section-y02"></a>
### タイトルセクション (y=0.2)
**会社名 (ティッカー)** - 例: `Tesla, Inc. (TSLA)`
```javascript
slide.addText('Tesla, Inc. (TSLA)', { x: 0.3, y: 0.2, w: 9.4, h: 0.35, fontSize: 18, bold: true });
```

<a id="4-quadrant-layout-y06-to-y72"></a>
### 4 象限レイアウト (y=0.6 ～ y=7.2)

| 象限 | ポジション | 内容 |
|----------|----------|---------|
| **1** | x=0.3, y=0.6, w=4.7, h=3.0 | **会社概要**: 本社、設立、主要統計、事業概要 (4 ～ 5 個の箇条書き) |
| **2** | x=5.0, y=0.6, w=4.7, h=3.0 | **ビジネスとポジショニング**: 収益の推進力、製品/サービス、競争上の地位、成長の推進力 (4 ～ 5 つの箇条書き) |
| **3** | x=0.3, y=3.7, w=4.7, h=3.5 | **主要な財務内容**: 収益、EBITDA、利益率、EPS、FCF + 評価額 (Mkt Cap、EV、マルチプル) — **表またはグラフ、両方ではありません** |
| **4** | x=5.0, y=3.7, w=4.7, h=3.5 | **上場企業向け**: 1 年間の株価チャート + 上位株主。 **非上場企業向け**: 最近の動向または所有権/M&A の歴史 |

<a id="font-sizes---use-these-exact-values"></a>
### フォント サイズ - これらの正確な値を使用してください
| 要素 | サイズ | 注意事項 |
|---------|------|-------|
| スライドのタイトル | 24pt | 太字、対象企業のブランドカラー |
| 象限ヘッダー | 14pt | 太字、アクセントバー付き |
| 本文/箇条書きテキスト | 11pt | 通常の太さ |
| 表のテキスト | 10pt | 密なテーブルには 9pt を使用します |
| グラフのラベル | 9pt | ラベルは短くする |
| ソース/フッター | 8pt | スライドの下部 |

**重要: テキストがオーバーフローする場合は、フォント サイズを 1 ポイント減らして再レンダリングしてください。**

<a id="visual-accents-required"></a>
### 視覚的なアクセント (必須)
各象限ヘッダーの左側に色付きのアクセント バーがなければなりません。
```javascript
// Add accent bar for quadrant header
slide.addShape(pptx.shapes.RECTANGLE, {
  x: 0.3, y: 0.6, w: 0.08, h: 0.25,
  fill: { color: 'E31937' }  // Use company brand color
});
slide.addText('Company Overview', {
  x: 0.45, y: 0.6, w: 4.5, h: 0.3, fontSize: 14, bold: true, fontFace: 'Arial'
});
```

**含める視覚的要素:**
- すべてのセクションヘッダーの横にあるアクセントバー (ブランドカラー)
- 上象限と下象限の間の細い水平分割線
- 可能な場合は右上隅に会社のロゴ
- 表の微妙なグリッド線 (ライトグレー #CCCCCC)

<a id="first-page-formatting"></a>
### 最初のページの書式設定
- **フォント: Arial** (またはユーザー/ブランドのガイドラインで指定されているもの)
- **象限タイトル**: タイトルの大文字と小文字 (すべて大文字ではありません)、例："COMPANY OVERVIEW"ではなく"Company Overview"
- **箇条書き**: 冒頭に太字の重要な用語、例: 「**市場での地位:** 世界をリードするメーカー...」
- 白の背景のみ - ボックス、塗りつぶし、シェーディングなし
- セクションヘッダー: 太字のテキスト。スタイルについてはブランドのガイドラインに従ってください。
- すべての象限が同じサイズで整列されている

---

<a id="subsequent-pages-free-form-layouts"></a>
## 後続のページ: 自由形式のレイアウト

- 2 列 (40/60 または 50/50)、フルスライド グラフ、またはサイドバー レイアウト
- 各ページで最初のページのコンテンツについて詳しく説明します
- 一貫したタイポグラフィーと配色を維持する
- 推奨フロー: 製品/市場 → 財務分析 → リーダーシップ

---

<a id="charts-multi-slide-profiles"></a>
## チャート (マルチスライド プロファイル)

**マルチスライド プロファイルの場合**: 2 ～ 3 個の実際の PptxGenJS チャートを含めます。プレースホルダー div や静的画像は決して使用しないでください。

**単一スライド プロファイルの場合**: 財務には表を使用します (スペース効率が向上します)。グラフを追加するのは、テーブルに追加するのではなく、テーブルを置き換える場合にのみ追加してください。

| データ型 | グラフの種類 |
|-----------|------------|
| 収益の推移 | 折れ線または縦棒（複数年） |
| 地理的内訳 | 横棒 |
| 製品構成 | パーセンテージ付きの円グラフ |
| 財務比較 | 縦棒 |
| 株価（1年間の日次） | 折れ線 |

<a id="chart-code-examples"></a>
### チャートのコード例

**水平バー (4:3 スライドの右下の象限に適合):**
```javascript
slide.addChart(pptx.charts.BAR, [{
  name: 'FY2024 Revenue by Region',
  labels: ['North America', 'EMEA', 'China', 'APLA'],
  values: [21.4, 13.6, 7.6, 6.7]
}], {
  x: 5.0, y: 4.1, w: 4.5, h: 3.0,  // Fits in bottom-right quadrant (4:3)
  barDir: 'bar', chartColors: ['FF6B35'], showValue: true,
  dataLabelFontSize: 10, catAxisLabelFontSize: 10, valAxisLabelFontSize: 10,
  dataLabelFormatCode: '$#,##0.0B',
  title: 'Revenue by Geography', titleFontSize: 12, titleBold: true
});
```

**円グラフ (4:3 スライドの右下の象限に収まります):**
```javascript
slide.addChart(pptx.charts.PIE, [{
  name: 'Product Mix',
  labels: ['Footwear', 'Apparel', 'Equipment'],
  values: [68, 29, 3]
}], {
  x: 5.0, y: 4.1, w: 4.5, h: 3.0,  // Fits in bottom-right quadrant (4:3)
  showPercent: true, showLegend: true, legendPos: 'r',
  dataLabelFontSize: 10, legendFontSize: 10,
  chartColors: ['FF6B35', '2C2C2C', '4A4A4A'],
  title: 'Revenue Mix FY24', titleFontSize: 12, titleBold: true
});
```

**折れ線グラフ (後続のスライドでは全幅):**
```javascript
slide.addChart(pptx.charts.LINE, [{
  name: 'Revenue ($B)',
  labels: ['FY21', 'FY22', 'FY23', 'FY24', 'FY25E'],
  values: [44.5, 46.7, 48.5, 51.4, 54.2]
}], {
  x: 0.3, y: 1.2, w: 9.4, h: 5.5,  // Full width for 4:3 slide
  chartColors: ['FF6B35'], showValue: true, lineSmooth: true,
  dataLabelFontSize: 11, catAxisLabelFontSize: 11, valAxisLabelFontSize: 11,
  title: 'Revenue Trend & Forecast', titleFontSize: 14, titleBold: true
});
```

---

<a id="financial-data-formatting"></a>
## 財務データのフォーマット

**常にネイティブの PptxGenJS テーブルまたはチャートを使用してください。プレーン テキストの散文テーブルや HTML テーブルは決して使用しないでください。**

財務データには `slide.addTable()` を使用します (4:3 スライドの左下の象限に収まります)。
```javascript
// Add header with accent bar first
slide.addShape(pptx.shapes.RECTANGLE, {
  x: 0.3, y: 3.7, w: 0.08, h: 0.25, fill: { color: 'E31937' }
});
slide.addText('Key Financials & Valuation', {
  x: 0.45, y: 3.7, w: 4.5, h: 0.3, fontSize: 14, bold: true, fontFace: 'Arial'
});

// Financial data table
slide.addTable([
  [{ text: 'Metric', options: { bold: true, fill: '003366', color: 'FFFFFF' } },
   { text: 'FY24', options: { bold: true, fill: '003366', color: 'FFFFFF' } },
   { text: 'FY25E', options: { bold: true, fill: '003366', color: 'FFFFFF' } }],
  ['Revenue', '$51.4B', '$54.2B'],
  ['YoY Growth', '+6.0%', '+5.5%'],
  ['EBITDA', '$8.9B', '$9.5B'],
  ['EBITDA Margin', '17.3%', '17.5%'],
  ['EPS', '$3.42', '$3.75'],
  ['Market Cap', '$185B', '—'],
  ['EV/EBITDA', '12.5x', '11.7x']
], {
  x: 0.45, y: 4.1, w: 4.3, h: 3.0,  // Below header in bottom-left quadrant
  fontFace: 'Arial', fontSize: 10,
  border: { pt: 0.5, color: 'CCCCCC' },
  valign: 'middle',
  colW: [1.8, 1.25, 1.25]  // Column widths
});
```

❌ **不正解:** `Note: FY2024 revenue growth +1.0%, Net Income $5.1B...` のようなプレーン テキスト
❌ **不正解:** HTML 表が PowerPoint に正しく変換されない

予測の場合は、構造化テーブルでベア/ベース/ブル ケースのシナリオを使用します。

---

<a id="quality-checklist"></a>
## 品質チェックリスト

<a id="first-page"></a>
### 最初のページ
- [ ] 会社名、ティッカー、業界を含むタイトルセクション
- [ ] タイトルの下にちょうど 4 等分
- [ ] すべての箇条書き、段落なし、それぞれ最大 1 行
- [ ] 表またはグラフの財務情報 (両方ではない)

<a id="all-slides"></a>
### すべてのスライド
- [ ] テキストのオーバーフローや切れはありません
- [ ] 全体的に一貫したフォントと色
- [ ] グラフが正しく表示される
- [ ] プレースホルダーテキストなし - すべて実際のデータ
- [ ] 一貫したスケーリング ($mm または $bn、混合なし)
- [ ] 引用された情報源
- [ ] 投資銀行品質（GS/MS/JPM基準）

**注:** PowerPoint ファイルの作成については、**PPTX スキル**を参照してください。
