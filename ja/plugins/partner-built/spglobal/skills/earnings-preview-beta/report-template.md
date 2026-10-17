> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/partner-built/spglobal/skills/earnings-preview-beta/report-template.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="html-report-template-reference"></a>
# HTML レポート テンプレートのリファレンス

このテンプレートは、単一企業の決算プレビュー HTML レポートの基礎として使用します。フェーズ 1 ～ 5 で収集した調査に基づいて、データ、グラフ、説明コンテンツをカスタマイズします。

<a id="html-structure"></a>
## HTMLの構造

レポートは、以下を含む単一の自己完結型 HTML ファイルです。
- 埋め込み CSS (外部スタイルシートなし)
- インタラクティブなグラフ用に CDN からロードされた Chart.js
- `@media print` による印刷に適したスタイル
- 画面上でも印刷物でも機能するレスポンシブ レイアウト
- 対象: 印刷ページ 4 ～ 5 ページ

<a id="complete-template"></a>
## 完全なテンプレート

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Earnings Preview — [COMPANY] ([TICKER]) — [DATE]</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js" integrity="sha384-vsrfeLOOY6KuIYKDlmVH5UiBmgIdB1oEf7p01YgWHuqmOHfZr374+odEv96n9tNC" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3.1.0/dist/chartjs-plugin-annotation.min.js" integrity="sha384-3N9GHhCtN3CQef6tNfqgZlv7sQLYIkcChN+uaTZ7xVdzKYp/SjBNPxa92+hM7EAY" crossorigin="anonymous"></script>
  <style>
    /* ── Reset & Base ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: 15px; }
    body {
      font-family: 'Arial Narrow', Arial, sans-serif;
      color: #1a1a2e;
      background: #fff;
      line-height: 1.6;
    }

    /* ── Layout ── */
    .page {
      max-width: 1100px;
      margin: 0 auto;
      padding: 40px 48px;
    }
    .page-break {
      page-break-before: always;
      border-top: 2px solid #1a1a4e;
      margin-top: 48px;
      padding-top: 32px;
    }

    /* ── Header / Cover ── */
    .cover-header {
      border-bottom: 3px solid #1a1a4e;
      padding-bottom: 16px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .cover-header .brand {
      font-size: 24px;
      font-weight: bold;
      color: #1a1a4e;
      letter-spacing: 2px;
      text-transform: uppercase;
    }
    .cover-header .sector {
      font-size: 13px;
      color: #555;
    }
    .cover-header .date {
      font-size: 14px;
      color: #333;
      text-align: right;
    }
    .report-title {
      font-size: 26px;
      font-weight: bold;
      color: #1a1a2e;
      margin: 20px 0 16px 0;
      line-height: 1.3;
    }

    /* ── Executive Thesis ── */
    .executive-summary {
      font-size: 14px;
      line-height: 1.65;
      color: #222;
      margin-bottom: 16px;
    }
    .executive-summary p {
      margin-bottom: 10px;
      text-align: justify;
    }
    .executive-summary ul {
      margin: 8px 0 10px 20px;
      font-size: 13.5px;
    }
    .executive-summary ul li {
      margin-bottom: 5px;
      line-height: 1.5;
    }
    blockquote {
      border-left: 3px solid #b0b8c8;
      padding: 6px 14px;
      margin: 8px 0 8px 12px;
      font-style: italic;
      color: #444;
      background: #f9fafb;
      font-size: 12.5px;
      line-height: 1.5;
    }

    /* ── Section Headings ── */
    h2.section-title {
      font-size: 18px;
      font-weight: 700;
      color: #1a1a4e;
      border-bottom: 2px solid #1a1a4e;
      padding-bottom: 5px;
      margin: 28px 0 14px 0;
    }
    h3.subsection-title {
      font-size: 14px;
      font-weight: 600;
      color: #1a1a4e;
      margin: 16px 0 8px 0;
    }
    h4.figure-title {
      font-size: 12px;
      font-weight: 600;
      color: #444;
      margin: 14px 0 6px 0;
    }

    /* ── Tables ── */
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      margin: 10px 0 16px 0;
    }
    thead th {
      background: #1a1a4e;
      color: #fff;
      padding: 7px 10px;
      text-align: left;
      font-weight: 600;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    tbody td {
      padding: 6px 10px;
      border-bottom: 1px solid #e0e0e0;
    }
    tbody tr:nth-child(even) {
      background: #f9fafb;
    }
    tbody tr:hover {
      background: #eef0f5;
    }
    .num { text-align: right; font-variant-numeric: tabular-nums; }
    .pos { color: #0d7a3e; font-weight: 600; }
    .neg { color: #c0392b; font-weight: 600; }
    .neutral { color: #555; }
    .highlight-row { background: #e8eaf6 !important; font-weight: 600; }

    /* ── Chart Containers ── */
    .chart-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 12px 0 20px 0;
    }
    .chart-container {
      position: relative;
      background: #fafbfc;
      border: 1px solid #e8e8e8;
      border-radius: 4px;
      padding: 14px;
    }
    .chart-container canvas {
      max-height: 260px;
    }
    .chart-full {
      grid-column: 1 / -1;
    }

    /* ── Compact Lists ── */
    .key-metrics ul, .themes ul, .news-list ul {
      margin: 6px 0 6px 18px;
      font-size: 13px;
      line-height: 1.55;
    }
    .key-metrics li, .themes li, .news-list li {
      margin-bottom: 5px;
    }

    /* ── Data Reference Links ── */
    a.data-ref {
      color: #1a1a4e;
      text-decoration: none;
      border-bottom: 1px dotted transparent;
      transition: border-color 0.15s;
    }
    a.data-ref:hover {
      border-bottom-color: #1a1a4e;
    }

    /* ── Appendix ── */
    .appendix table {
      font-size: 10.5px;
    }
    .appendix thead th {
      font-size: 10px;
      padding: 5px 8px;
    }
    .appendix tbody td {
      padding: 4px 8px;
      font-size: 10.5px;
      vertical-align: top;
      line-height: 1.45;
    }
    .appendix .ref-id {
      font-weight: 600;
      color: #1a1a4e;
      white-space: nowrap;
    }
    .appendix .source-detail {
      font-size: 10px;
      color: #444;
    }
    .appendix .source-detail .formula {
      font-family: 'Courier New', monospace;
      font-size: 9.5px;
      color: #555;
    }
    .appendix .source-detail .excerpt {
      font-style: italic;
      color: #555;
    }
    .appendix .source-detail .src-label {
      font-weight: 600;
      color: #1a1a4e;
      font-size: 9.5px;
    }
    .appendix .source-detail a.data-ref {
      font-weight: 600;
    }
    .appendix a.src-url {
      color: #3366cc;
      text-decoration: underline;
      font-size: 10px;
      word-break: break-all;
    }
    .appendix a.src-url:hover {
      color: #1a1a4e;
    }
    .appendix .transcript-ref {
      font-weight: 600;
      color: #1a1a4e;
      font-size: 10px;
    }
    .appendix-group {
      font-size: 11px;
      font-weight: 700;
      color: #1a1a4e;
      background: #f0f1f5;
      padding: 4px 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* ── Source / Footer ── */
    .source {
      font-size: 10px;
      color: #999;
      margin-top: 3px;
      font-style: italic;
    }
    .ai-disclaimer {
      background-color: #fff3cd;
      border: 1px solid #ffc107;
      border-radius: 4px;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      color: #664d03;
      text-align: center;
      margin-bottom: 12px;
    }
    .page-footer {
      border-top: 2px solid #1a1a4e;
      padding-top: 10px;
      margin-top: 32px;
      text-align: center;
    }
    .page-footer .footer-disclaimer {
      font-size: 11px;
      font-weight: 600;
      color: #664d03;
      background-color: #fff3cd;
      border: 1px solid #ffc107;
      border-radius: 4px;
      padding: 4px 10px;
      display: inline-block;
      margin-bottom: 4px;
    }
    .page-footer .footer-meta {
      font-size: 10px;
      color: #888;
    }

    /* ── Print Styles ── */
    @media print {
      body { font-size: 11px; }
      .page { padding: 16px; max-width: none; }
      .chart-container { break-inside: avoid; }
      table { break-inside: avoid; }
      .page-break { margin-top: 0; }
      .no-print { display: none; }
    }
  </style>
</head>
<body>
<div class="page">

  <!-- ════════════════════════════════════════════ -->
  <!-- PAGE 1: COVER & THESIS                       -->
  <!-- ════════════════════════════════════════════ -->
  <div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>
  <div class="cover-header">
    <div>
      <div class="brand">Earnings Preview</div>
      <div class="sector">[Industry] | [TICKER]</div>
    </div>
    <div class="date">[Full Date]</div>
  </div>

  <h1 class="report-title">[Company Name] ([TICKER]) [Q# FY####] Earnings Preview: [Thematic Subtitle]</h1>

  <div class="executive-summary">
    <!-- Executive thesis: 2-3 short paragraphs + bullet points.
         What we expect, our EPS estimate vs consensus, guidance expectations,
         key metrics to watch, what would move the stock, key debates.
         Weave in 3-4 management quotes as blockquotes where they support the thesis.
         Do NOT create a separate "Key Management Quotes" section. -->

    <p>[Opening 1-2 sentences: what we expect from this print.]</p>

    <ul>
      <li><strong>EPS:</strong> We estimate <a href="#ref-1" class="data-ref">$X.XX</a> vs consensus <a href="#ref-2" class="data-ref">$X.XX</a>, [rationale]</li>
      <li><strong>Revenue:</strong> We estimate <a href="#ref-3" class="data-ref">$XX.XB</a> vs consensus <a href="#ref-4" class="data-ref">$XX.XB</a>, [rationale]</li>
      <li><strong>Guidance:</strong> [What to expect on forward guidance]</li>
      <li><strong>Key metric:</strong> [Most important sub-headline metric to watch]</li>
      <li><strong>Stock catalyst:</strong> [What would move the stock up/down post-print]</li>
      <li><strong>Key debate:</strong> [What bulls and bears disagree on]</li>
    </ul>

    <blockquote>"[Key management quote supporting a thesis point]" — [Speaker], [Q# FY####] Earnings Call</blockquote>

    <p>[1-2 sentences tying it together — your overall read on the setup.]</p>

    <blockquote>"[Another supporting quote]" — [Speaker], [Q# FY####] Earnings Call</blockquote>
  </div>

  <!-- ════════════════════════════════════════════ -->
  <!-- PAGE 2: ESTIMATES, THEMES & NEWS             -->
  <!-- ════════════════════════════════════════════ -->
  <div class="page-break">

    <!-- Consensus Estimates Table (Figure label inline) -->
    <h2 class="section-title">Consensus Estimates — [Q# FY####]</h2>
    <h4 class="figure-title">[Q# FY####] Consensus Estimates</h4>
    <table>
      <thead>
        <tr>
          <th>Metric</th>
          <th class="num">Consensus</th>
          <th class="num">Our Estimate</th>
          <th class="num">y/y Change</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Revenue</td><td class="num"><a href="#ref-N" class="data-ref">$[XX.X]B</a></td><td class="num"><a href="#ref-N" class="data-ref">$[XX.X]B</a></td><td class="num [pos|neg]"><a href="#ref-N" class="data-ref">[+/-X.X%]</a></td></tr>
        <tr><td>Diluted EPS</td><td class="num"><a href="#ref-N" class="data-ref">$[X.XX]</a></td><td class="num"><a href="#ref-N" class="data-ref">$[X.XX]</a></td><td class="num [pos|neg]"><a href="#ref-N" class="data-ref">[+/-X.X%]</a></td></tr>
        <tr><td>Gross Margin</td><td class="num"><a href="#ref-N" class="data-ref">[XX.X%]</a></td><td class="num"><a href="#ref-N" class="data-ref">[XX.X%]</a></td><td class="num [pos|neg]"><a href="#ref-N" class="data-ref">[+/-XXbps]</a></td></tr>
        <tr><td>Operating Income</td><td class="num"><a href="#ref-N" class="data-ref">$[X.X]B</a></td><td class="num"><a href="#ref-N" class="data-ref">$[X.X]B</a></td><td class="num [pos|neg]"><a href="#ref-N" class="data-ref">[+/-X.X%]</a></td></tr>
        <!-- Add 2-3 company-specific KPIs below (e.g., comp sales, eComm growth, membership revenue) -->
        <tr><td>[Company KPI 1]</td><td class="num">[Value]</td><td class="num">[Value]</td><td class="num [pos|neg]">[Change]</td></tr>
        <tr><td>[Company KPI 2]</td><td class="num">[Value]</td><td class="num">[Value]</td><td class="num [pos|neg]">[Change]</td></tr>
      </tbody>
    </table>
    <div class="source">Source: Kensho, S&P Capital IQ</div>

    <!-- Key Metrics Beyond Headline EPS -->
    <h3 class="subsection-title">Key Metrics Beyond Headline EPS</h3>
    <div class="key-metrics">
      <ul>
        <li><strong>[Metric 1]:</strong> [What consensus/management expects, why it matters. Be specific with numbers.]</li>
        <li><strong>[Metric 2]:</strong> [Details]</li>
        <li><strong>[Metric 3]:</strong> [Details]</li>
        <!-- 3-5 items -->
      </ul>
    </div>

    <!-- Themes to Watch -->
    <h3 class="subsection-title">Themes to Watch</h3>
    <div class="themes">
      <ul>
        <li><strong>[Theme 1]:</strong> [1-2 sentences max. Forward-looking, specific.]</li>
        <li><strong>[Theme 2]:</strong> [Details]</li>
        <li><strong>[Theme 3]:</strong> [Details]</li>
        <!-- 3-5 themes -->
      </ul>
    </div>

    <!-- Recent News & Developments -->
    <h3 class="subsection-title">Recent News & Developments</h3>
    <div class="news-list">
      <ul>
        <li><strong>[Date]:</strong> [Headline] — [Brief impact assessment, one line]</li>
        <li><strong>[Date]:</strong> [Headline] — [Impact]</li>
        <li><strong>[Date]:</strong> [Headline] — [Impact]</li>
        <!-- 3-5 material items from last 60 days -->
      </ul>
    </div>
    <div class="source">Source: Kensho</div>

  </div>

  <!-- ════════════════════════════════════════════ -->
  <!-- PAGES 3-5: FIGURES                           -->
  <!-- All charts and tables, numbered sequentially -->
  <!-- ════════════════════════════════════════════ -->
  <div class="page-break">
    <h2 class="section-title">Financial & Competitive Analysis</h2>

    <!-- Figure 1: Quarterly Revenue & Diluted EPS -->
    <div class="chart-row">
      <div class="chart-container">
        <h4 class="figure-title">Figure 1: Quarterly Revenue & Diluted EPS</h4>
        <canvas id="chart-rev-eps"></canvas>
        <div class="source">Source: S&P Capital IQ</div>
      </div>

      <!-- Figure 2: Margin Trends -->
      <div class="chart-container">
        <h4 class="figure-title">Figure 2: Margin Trends (Gross & Operating %)</h4>
        <canvas id="chart-margins"></canvas>
        <div class="source">Source: S&P Capital IQ</div>
      </div>
    </div>

    <!-- Figure 3: Revenue Growth y/y % -->
    <div class="chart-row">
      <div class="chart-container chart-full">
        <h4 class="figure-title">Figure 3: Revenue Growth y/y (%)</h4>
        <canvas id="chart-rev-growth" style="max-height: 200px;"></canvas>
        <div class="source">Source: S&P Capital IQ</div>
      </div>
    </div>

    <!-- Figure 4: Business Segment Revenue -->
    <h4 class="figure-title">Figure 4: Business Segment Revenue</h4>
    <table>
      <thead>
        <tr>
          <th>Segment</th>
          <th class="num">Latest Q Rev ($M)</th>
          <th class="num">% of Total</th>
          <th class="num">y/y Change</th>
        </tr>
      </thead>
      <tbody>
        <!-- Populate from segment data. Color-code y/y change with pos/neg classes. -->
      </tbody>
    </table>
    <div class="source">Source: S&P Capital IQ</div>
  </div>

  <!-- Page break for stock & competitor charts -->
  <div class="page-break">

    <!-- Figure 5: 1-Year Stock Price with Earnings Dates -->
    <div class="chart-row">
      <div class="chart-container chart-full">
        <h4 class="figure-title">Figure 5: 1-Year Stock Price with Earnings Dates</h4>
        <canvas id="chart-price-annotated" style="max-height: 300px;"></canvas>
        <div class="source">Source: S&P Capital IQ</div>
      </div>
    </div>

    <!-- Figure 6: Stock Performance vs. Competitors (Indexed to 100) -->
    <div class="chart-row">
      <div class="chart-container chart-full">
        <h4 class="figure-title">Figure 6: Stock Performance vs. Competitors — 1 Year (Indexed to 100)</h4>
        <canvas id="chart-comp-perf" style="max-height: 300px;"></canvas>
        <div class="source">Source: S&P Capital IQ</div>
      </div>
    </div>
  </div>

  <div class="page-break">

    <!-- Figure 7: LTM P/E vs. Competitors -->
    <div class="chart-row">
      <div class="chart-container chart-full">
        <h4 class="figure-title">Figure 7: LTM P/E vs. Competitors</h4>
        <canvas id="chart-pe-comp" style="max-height: 280px;"></canvas>
        <div class="source">Source: S&P Capital IQ</div>
      </div>
    </div>

    <!-- Figure 8: Competitor Comparison Table -->
    <h4 class="figure-title">Figure 8: Competitor Comparison</h4>
    <table>
      <thead>
        <tr>
          <th>Ticker</th>
          <th>Company</th>
          <th class="num">Mkt Cap ($B)</th>
          <th class="num">LTM P/E</th>
          <th class="num">NTM P/E</th>
          <th class="num">YTD %</th>
          <th class="num">1-Yr %</th>
        </tr>
      </thead>
      <tbody>
        <!-- Highlight the subject company row with class="highlight-row" -->
      </tbody>
    </table>
    <div class="source">Source: S&P Capital IQ</div>
  </div>

  <!-- ════════════════════════════════════════════ -->
  <!-- APPENDIX: DATA SOURCES & CALCULATIONS        -->
  <!-- ════════════════════════════════════════════ -->
  <div class="page-break appendix" id="appendix">
    <div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>
    <h2 class="section-title">Appendix: Data Sources & Calculations</h2>
    <p style="font-size: 11px; color: #666; margin-bottom: 12px;">
      Every claim in this report is hyperlinked to its entry below. Click any highlighted text to jump here.
    </p>
    <table>
      <thead>
        <tr>
          <th style="width: 40px;">Ref</th>
          <th style="width: 170px;">Fact</th>
          <th style="width: 75px;">Value</th>
          <th>Source & Derivation</th>
        </tr>
      </thead>
      <tbody>
        <!-- Group: Quarterly Financials -->
        <tr><td colspan="4" class="appendix-group">Quarterly Financials</td></tr>
        <tr id="ref-1">
          <td class="ref-id">1</td>
          <td>[Q# FY#### Revenue]</td>
          <td class="num">$[XX.X]B</td>
          <td class="source-detail">
            <span class="src-label">S&P Capital IQ</span> — get_financial_line_item_from_identifiers(identifier='[TICKER]', line_item='revenue', period_type='quarterly', period='[Q# FY####]')
          </td>
        </tr>
        <tr id="ref-2">
          <td class="ref-id">2</td>
          <td>[Q# FY#### Diluted EPS]</td>
          <td class="num">$[X.XX]</td>
          <td class="source-detail">
            <span class="src-label">S&P Capital IQ</span> — get_financial_line_item_from_identifiers(identifier='[TICKER]', line_item='diluted_eps', period_type='quarterly', period='[Q# FY####]')
          </td>
        </tr>
        <tr id="ref-3">
          <td class="ref-id">3</td>
          <td>[Q# FY#### Gross Profit]</td>
          <td class="num">$[XX.X]B</td>
          <td class="source-detail">
            <span class="src-label">S&P Capital IQ</span> — get_financial_line_item_from_identifiers(identifier='[TICKER]', line_item='gross_profit', period_type='quarterly', period='[Q# FY####]')
          </td>
        </tr>
        <tr id="ref-4">
          <td class="ref-id">4</td>
          <td>[Q# FY#### Gross Margin]</td>
          <td class="num">[XX.X%]</td>
          <td class="source-detail">
            <span class="formula"><a href="#ref-3" class="data-ref">Gross Profit $XX.XB</a> / <a href="#ref-1" class="data-ref">Revenue $XX.XB</a> = XX.X%</span><br>
            <span class="src-label">S&P Capital IQ</span> (calculated)
          </td>
        </tr>
        <tr id="ref-5">
          <td class="ref-id">5</td>
          <td>[Q# FY#### Revenue y/y Growth]</td>
          <td class="num">[+/-X.X%]</td>
          <td class="source-detail">
            <span class="formula">(<a href="#ref-1" class="data-ref">[Q# FY## Rev $XX.XB]</a> - <a href="#ref-N" class="data-ref">[Q# FY## Rev $XX.XB]</a>) / <a href="#ref-N" class="data-ref">[Q# FY## Rev $XX.XB]</a> = X.X%</span><br>
            <span class="src-label">S&P Capital IQ</span> (calculated)
          </td>
        </tr>
        <!-- Continue for all financial data points... -->

        <!-- Group: Valuation -->
        <tr><td colspan="4" class="appendix-group">Valuation</td></tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>Current Stock Price — [TICKER]</td>
          <td class="num">$[XXX.XX]</td>
          <td class="source-detail">
            <span class="src-label">S&P Capital IQ</span> — get_prices_from_identifiers(identifier='[TICKER]', periodicity='day')
          </td>
        </tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>Market Cap — [TICKER]</td>
          <td class="num">$[XXX.X]B</td>
          <td class="source-detail">
            <span class="src-label">S&P Capital IQ</span> — get_capitalization_from_identifiers(identifier='[TICKER]', capitalization='market_cap')
          </td>
        </tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>LTM P/E — [TICKER]</td>
          <td class="num">[XX.X]x</td>
          <td class="source-detail">
            <span class="formula"><a href="#ref-20" class="data-ref">Price $XXX.XX</a> / (<a href="#ref-8" class="data-ref">Q1 EPS $X.XX</a> + <a href="#ref-9" class="data-ref">Q2 EPS $X.XX</a> + <a href="#ref-10" class="data-ref">Q3 EPS $X.XX</a> + <a href="#ref-11" class="data-ref">Q4 EPS $X.XX</a>) = XX.Xx</span><br>
            <span class="src-label">S&P Capital IQ</span> (calculated)
          </td>
        </tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>NTM P/E — [TICKER]</td>
          <td class="num">[XX.X]x</td>
          <td class="source-detail">
            <span class="formula"><a href="#ref-20" class="data-ref">Price $XXX.XX</a> / (<a href="#ref-N" class="data-ref">Q4'25E $X.XX</a> + <a href="#ref-N" class="data-ref">Q1'26E $X.XX</a> + <a href="#ref-N" class="data-ref">Q2'26E $X.XX</a> + <a href="#ref-N" class="data-ref">Q3'26E $X.XX</a>) = XX.Xx</span><br>
            <span class="src-label">S&P Capital IQ</span> — get_consensus_estimates_from_identifiers(identifier='[TICKER]', period_type='quarterly', num_periods_forward=4). NTM EPS = sum of next 4 quarterly consensus mean EPS estimates.
          </td>
        </tr>

        <!-- Group: Transcript Claims -->
        <tr><td colspan="4" class="appendix-group">Transcript Claims</td></tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>[Fact, e.g., "Management guided comp sales +3-4%"]</td>
          <td class="num">N/A</td>
          <td class="source-detail">
            <span class="excerpt">"We expect comp sales growth of 3-4% in Q4, driven by continued strength in grocery and health &amp; wellness."</span><br>
            <span class="src-label">Source:</span> <span class="transcript-ref">[Q# FY#### Earnings Call Transcript]</span> (key_dev_id: [ID]) — [Speaker Name], [Title]
          </td>
        </tr>

        <!-- Group: Estimates & Consensus -->
        <tr><td colspan="4" class="appendix-group">Estimates & Consensus</td></tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>Consensus EPS — [Q# FY####]</td>
          <td class="num">$[X.XX]</td>
          <td class="source-detail">
            <span class="excerpt">"Consensus EPS estimate of $X.XX, revised up from $X.XX over the past 90 days."</span><br>
            <a href="https://[source-url-from-kensho-search]" target="_blank" class="src-url">[Source Title / Publication Name]</a><br>
            <span class="src-label">Query:</span> search("[TICKER] earnings estimates consensus EPS revenue upcoming quarter")
          </td>
        </tr>

        <!-- Group: News & Analyst Commentary -->
        <tr><td colspan="4" class="appendix-group">News & Analyst Commentary</td></tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>[e.g., "Barclays upgraded to Overweight"]</td>
          <td class="num">N/A</td>
          <td class="source-detail">
            <span class="excerpt">"Barclays upgraded WMT to Overweight with a $210 price target, citing accelerating eCommerce momentum."</span><br>
            <a href="https://[source-url-from-kensho-search]" target="_blank" class="src-url">[Source Title / Publication, Date]</a><br>
            <span class="src-label">Query:</span> search("[TICKER] analyst ratings price target upgrades downgrades")
          </td>
        </tr>

        <!-- Group: Stock Performance -->
        <tr><td colspan="4" class="appendix-group">Stock Performance</td></tr>
        <tr id="ref-N">
          <td class="ref-id">[N]</td>
          <td>YTD Return — [TICKER]</td>
          <td class="num">[+/-X.X%]</td>
          <td class="source-detail">
            <span class="formula">(<a href="#ref-N" class="data-ref">Current $XXX.XX</a> - <a href="#ref-N" class="data-ref">Dec 31 Close $XXX.XX</a>) / <a href="#ref-N" class="data-ref">Dec 31 Close $XXX.XX</a> = X.X%</span><br>
            <span class="src-label">S&P Capital IQ</span> (calculated from daily prices)
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ════════════════════════════════════════════ -->
  <!-- FOOTER                                       -->
  <!-- ════════════════════════════════════════════ -->
  <div class="page-footer">
    <div class="footer-disclaimer">Analysis is AI-generated — please confirm all outputs</div>
    <div class="footer-meta">Data: S&P Capital IQ, Kensho | [Month Day, Year]</div>
  </div>

</div>

<!-- ════════════════════════════════════════════════ -->
<!-- CHART.JS SCRIPTS                                 -->
<!-- ════════════════════════════════════════════════ -->
<script>
// ── Register Annotation Plugin ──
// The CDN-loaded annotation plugin must be explicitly registered.
// It is available as a global after the script tag loads.
if (window['chartjs-plugin-annotation']) {
  Chart.register(window['chartjs-plugin-annotation']);
}

// ── Chart Defaults ──
Chart.defaults.font.family = "'Arial Narrow', Arial, sans-serif";
Chart.defaults.font.size = 11;
Chart.defaults.color = '#555';
Chart.defaults.plugins.legend.position = 'bottom';
Chart.defaults.plugins.legend.labels.boxWidth = 12;

// ── Color Palette ──
const COLORS = {
  navy:     '#1a1a4e',
  blue:     '#3366cc',
  teal:     '#0d9488',
  orange:   '#e67e22',
  red:      '#c0392b',
  green:    '#27ae60',
  purple:   '#8e44ad',
  gray:     '#7f8c8d',
  lightBlue:'#85c1e9',
  gold:     '#f0b429',
};
const COMP_COLORS = [
  COLORS.navy, COLORS.blue, COLORS.teal,
  COLORS.orange, COLORS.red, COLORS.green,
  COLORS.purple, COLORS.gold
];

// ── Helper: Revenue & EPS Combo Chart ──
function createRevEpsChart(canvasId, labels, revenueData, epsData, revLabel) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: revLabel || 'Revenue ($B)',
          data: revenueData,
          backgroundColor: COLORS.navy + 'cc',
          borderColor: COLORS.navy,
          borderWidth: 1,
          yAxisID: 'y',
          order: 2
        },
        {
          label: 'Diluted EPS',
          data: epsData,
          type: 'line',
          borderColor: COLORS.orange,
          backgroundColor: COLORS.orange,
          borderWidth: 2.5,
          pointRadius: 4,
          pointBackgroundColor: COLORS.orange,
          tension: 0.3,
          yAxisID: 'y1',
          order: 1
        }
      ]
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      scales: {
        y: {
          position: 'left',
          title: { display: true, text: revLabel || 'Revenue ($B)', font: { size: 11 } },
          grid: { color: '#eee' }
        },
        y1: {
          position: 'right',
          title: { display: true, text: 'EPS ($)', font: { size: 11 } },
          grid: { drawOnChartArea: false }
        }
      }
    }
  });
}

// ── Helper: Margin Trend Chart ──
function createMarginChart(canvasId, labels, grossMargins, opMargins) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Gross Margin %',
          data: grossMargins,
          borderColor: COLORS.blue,
          backgroundColor: COLORS.blue + '20',
          borderWidth: 2.5,
          pointRadius: 4,
          fill: false,
          tension: 0.3
        },
        {
          label: 'Operating Margin %',
          data: opMargins,
          borderColor: COLORS.teal,
          backgroundColor: COLORS.teal + '20',
          borderWidth: 2.5,
          pointRadius: 4,
          fill: false,
          tension: 0.3
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          title: { display: true, text: 'Margin (%)', font: { size: 11 } },
          grid: { color: '#eee' },
          ticks: { callback: v => v.toFixed(1) + '%' }
        }
      }
    }
  });
}

// ── Helper: Revenue Growth Bar Chart ──
function createRevGrowthChart(canvasId, labels, growthData) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Revenue Growth y/y %',
        data: growthData,
        backgroundColor: growthData.map(v => v >= 0 ? COLORS.green + 'cc' : COLORS.red + 'cc'),
        borderColor: growthData.map(v => v >= 0 ? COLORS.green : COLORS.red),
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          title: { display: true, text: 'Growth (%)', font: { size: 11 } },
          grid: { color: '#eee' },
          ticks: { callback: v => v.toFixed(1) + '%' }
        }
      },
      plugins: { legend: { display: false } }
    }
  });
}

// ── Helper: Earnings-Annotated Stock Price Chart ──
function createAnnotatedPriceChart(canvasId, labels, prices, earningsDates, ticker) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  const annotations = {};
  earningsDates.forEach((ed, i) => {
    let xValue = ed.date;
    const isNeg = ed.move.startsWith('-');
    annotations['earnings' + i] = {
      type: 'line',
      xMin: xValue,
      xMax: xValue,
      borderColor: isNeg ? '#c0392b' : '#0d7a3e',
      borderWidth: 2,
      borderDash: [6, 4],
      label: {
        display: true,
        content: ed.label + ' (' + ed.move + ')',
        position: i % 2 === 0 ? 'start' : 'end',
        backgroundColor: isNeg ? '#c0392b' : '#0d7a3e',
        color: '#fff',
        font: { size: 10, weight: 'bold' },
        padding: { top: 3, bottom: 3, left: 6, right: 6 },
        borderRadius: 3
      }
    };
  });
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: ticker + ' Close',
        data: prices,
        borderColor: COLORS.navy,
        backgroundColor: COLORS.navy + '15',
        borderWidth: 1.5,
        pointRadius: 0,
        pointHitRadius: 4,
        fill: true,
        tension: 0.1
      }]
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      scales: {
        x: { type: 'category', ticks: { maxTicksLimit: 12, font: { size: 10 } }, grid: { display: false } },
        y: { title: { display: true, text: 'Price ($)', font: { size: 11 } }, grid: { color: '#eee' } }
      },
      plugins: {
        annotation: { annotations: annotations },
        tooltip: { callbacks: { label: ctx => ticker + ': $' + ctx.raw.toFixed(2) } }
      }
    }
  });
}

// ── Helper: Competitor Indexed Performance Chart ──
// datasets: [{ label: 'TICKER', data: [price1, price2, ...], color: '#xxx', isSubject: true/false }, ...]
function createCompPerfChart(canvasId, labels, datasets) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  const chartDatasets = datasets.map((ds, i) => {
    const base = ds.data[0] || 1;
    return {
      label: ds.label,
      data: ds.data.map(v => (v / base) * 100),
      borderColor: ds.color || COMP_COLORS[i % COMP_COLORS.length],
      backgroundColor: 'transparent',
      borderWidth: ds.isSubject ? 3 : 1.5,
      borderDash: ds.isSubject ? [] : [4, 2],
      pointRadius: 0,
      tension: 0.2
    };
  });
  new Chart(ctx, {
    type: 'line',
    data: { labels: labels, datasets: chartDatasets },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      scales: {
        y: { title: { display: true, text: 'Indexed (100 = Start)', font: { size: 11 } }, grid: { color: '#eee' } },
        x: { ticks: { maxTicksLimit: 12 } }
      },
      plugins: {
        tooltip: { callbacks: { label: ctx => ctx.dataset.label + ': ' + ctx.raw.toFixed(1) } }
      }
    }
  });
}

// ── Helper: LTM P/E Horizontal Bar Chart ──
// companies: [{ label: 'TICKER', pe: 25.3, isSubject: true/false }, ...]
function createPEChart(canvasId, companies) {
  const ctx = document.getElementById(canvasId);
  if (!ctx) return;
  companies.sort((a, b) => b.pe - a.pe);
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: companies.map(c => c.label),
      datasets: [{
        label: 'LTM P/E',
        data: companies.map(c => c.pe),
        backgroundColor: companies.map(c => c.isSubject ? COLORS.navy : COLORS.lightBlue),
        borderColor: companies.map(c => c.isSubject ? COLORS.navy : COLORS.blue),
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      scales: {
        x: {
          title: { display: true, text: 'LTM P/E', font: { size: 11 } },
          grid: { color: '#eee' }
        },
        y: {
          ticks: { font: { size: 12, weight: 'bold' } }
        }
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: { label: ctx => 'P/E: ' + ctx.raw.toFixed(1) + 'x' }
        }
      }
    }
  });
}

// ═══════════════════════════════════════════════
// HELPER FUNCTIONS DEFINED ABOVE — DO NOT REWRITE THEM.
// Use ONLY these functions to create charts.
// DO NOT write custom inline Chart.js code.
// ═══════════════════════════════════════════════

</script>

<!-- ═══════════════════════════════════════════════════════════ -->
<!-- CHART DATA — EACH CHART IN ITS OWN SCRIPT + TRY-CATCH     -->
<!-- A syntax error in one chart must NOT break the others.     -->
<!-- MANDATORY: Use the helper functions above. No custom code. -->
<!-- ═══════════════════════════════════════════════════════════ -->

<!-- Figure 1: Revenue & EPS -->
<script>
try {
  createRevEpsChart('chart-rev-eps',
    ['Q1 FY24','Q2 FY24','Q3 FY24','Q4 FY24','Q1 FY25','Q2 FY25','Q3 FY25','Q4 FY25'],
    [152.3, 161.6, 160.8, 173.4, 161.5, 169.3, 165.8, 178.0],  // revenue in $B
    [1.47, 1.84, 1.53, 1.80, 1.56, 1.92, 1.60, 1.90],          // diluted EPS
    'Revenue ($B)'
  );
} catch(e) { console.error('Figure 1 error:', e); }
</script>

<!-- Figure 2: Margin Trends -->
<script>
try {
  createMarginChart('chart-margins',
    ['Q1 FY24','Q2 FY24','Q3 FY24','Q4 FY24','Q1 FY25','Q2 FY25','Q3 FY25','Q4 FY25'],
    [24.0, 24.4, 24.2, 23.8, 24.5, 24.8, 24.6, 24.1],  // gross margin %
    [4.2, 5.1, 4.5, 4.8, 4.6, 5.3, 4.7, 5.0]            // operating margin %
  );
} catch(e) { console.error('Figure 2 error:', e); }
</script>

<!-- Figure 3: Revenue Growth y/y — ONLY quarters where y/y can be computed (most recent 4) -->
<script>
try {
  createRevGrowthChart('chart-rev-growth',
    ['Q1 FY25','Q2 FY25','Q3 FY25','Q4 FY25'],  // Only 4 labels — quarters with y/y data
    [6.0, 4.8, 3.1, 2.7]                          // y/y revenue growth % for those 4 quarters
  );
} catch(e) { console.error('Figure 3 error:', e); }
</script>

<!-- Figure 5: Annotated Stock Price -->
<script>
try {
  createAnnotatedPriceChart('chart-price-annotated',
    ['2025-02-18','2025-02-19'],  // ... daily date labels for 1 year
    [170.5, 171.2],               // ... daily closing prices
    [
      { date: '2025-05-15', label: 'Q1 FY26', move: '+3.2%' },
      { date: '2025-08-15', label: 'Q2 FY26', move: '-1.8%' }
    ],
    'WMT'
  );
} catch(e) { console.error('Figure 5 error:', e); }
</script>

<!-- Figure 6: Competitor Indexed Performance -->
<script>
try {
  createCompPerfChart('chart-comp-perf',
    ['2025-02-18','2025-03-18'],  // ... date labels
    [
      { label: 'WMT', data: [170.5, 172.3], isSubject: true },
      { label: 'COST', data: [580.2, 595.1], isSubject: false },
      { label: 'TGT', data: [142.0, 138.5], isSubject: false }
    ]
  );
} catch(e) { console.error('Figure 6 error:', e); }
</script>

<!-- Figure 7: LTM P/E Comparison -->
<script>
try {
  createPEChart('chart-pe-comp', [
    { label: 'COST', pe: 52.3, isSubject: false },
    { label: 'WMT', pe: 28.1, isSubject: true },
    { label: 'TGT', pe: 15.6, isSubject: false },
    { label: 'BJ', pe: 22.4, isSubject: false }
  ]);
} catch(e) { console.error('Figure 7 error:', e); }
</script>

</body>
</html>
```

<a id="chartjs-implementation-notes"></a>
## Chart.js 実装メモ

<a id="figure-2-revenue--eps-chart"></a>
### 図 2: 収益と EPS グラフ
- **タイプ**: コンボバー + ライン
- **棒**: 左の Y 軸は四半期ごとの収益
- **線**: 右 y 軸の希薄化 EPS
- **ラベル**: 四半期識別子 (例: 「2024 年度第 1 四半期」)
- 8四半期分のデータを使います。

<a id="figure-3-margin-trend-chart"></a>
### 図3：利益率の推移
- **タイプ**: 二重折れ線グラフ
- **線**: 売上総利益率 % と営業利益率 %
- **Y 軸**: 小数点第 1 位のパーセンテージ

<a id="figure-3-revenue-growth-chart"></a>
### 図 3: 収益増加グラフ
- **タイプ**: 条件付き色付き棒グラフ
- **緑色のバー**: プラス成長の四半期
- **赤いバー**: マイナス成長の四半期
- **重要**: 前年比成長率を計算できる四半期 (つまり、現在の四半期と前年の四半期の両方が `financials.csv` に存在する四半期) のみを含めます。生データが 8 四半期ある場合、通常は 8 ではなく 4 つのバーが生成されます。y/y データのない四半期にはラベルを渡さないでください。
- 凡例は必要ありません (一目瞭然)

<a id="figure-4-business-segment-revenue"></a>
### 図 4: 事業セグメントの収益
- HTML テーブルを使用します (グラフではありません)
- 列：セグメント | 直近四半期売上高（$M） | 全体比率 | 前年同期比
- pos/neg クラスを使用してセルを y/y で色分けする

<a id="figure-5-earnings-annotated-stock-price-chart"></a>
### 図5：決算発表日の注記付き株価チャート
- **タイプ**: 注釈プラグインの垂直線を含む折れ線グラフ
- **データ**: 1 年間の毎日の終値
- **注釈**: 各決算日の垂直破線
- **ラベル：** 四半期名＋決算発表後1日の株価変動
- **色：** 株価のプラス反応は緑、マイナス反応は赤
- **1 日の動きの計算**: 決算日の終値と次の取引日の終値を比較します。
- **重要**: 注釈プラグインはチャートを作成する前に登録する必要があります: `Chart.register(window['chartjs-plugin-annotation'])` — これはすでにテンプレート スクリプト ブロック内にあります

<a id="figure-7-competitor-indexed-performance-chart"></a>
### 図 7: 競合他社の指数化されたパフォーマンス チャート
- **タイプ**: 複数折れ線グラフ、100 にリベース
- **対象会社**：太実線（borderWidth: 3）
- **競合他社**: より細い破線 (borderWidth: 1.5、borderDash)
- この視覚的な階層により、対象企業をすぐに識別できるようになります。

<a id="figure-8-ltm-pe-comparison-chart"></a>
### 図 8: LTM PER 比較チャート
- **タイプ**: 横棒グラフ
- **対象会社**: 紺色で強調表示 (#1a1a4e)
- **競合企業：** 薄い青（#85c1e9）
- **並べ替え**: PER による降順
- 自社が同業他社に対してプレミアムまたはディスカウントで取引しているかどうかが一目でわかります

<a id="figure-8-competitor-comparison-table"></a>
### 図 8: 競合他社の比較表
- 対象会社のハイライト行を含む HTML テーブル
- 列：ティッカー | 企業名 | 時価総額（$B） | LTM P/E | NTM P/E | 年初来% | 1年間%
- リターンをpos/negクラスで色分けします。

<a id="formatting-conventions"></a>
## フォーマット規則

<a id="numbers"></a>
### 数字
- 収益: $B の場合は小数点以下 1 桁 (例: "$152.3B")、$M の場合は小数点以下なし (例: "$4,521M")
- EPS: 小数点以下 2 桁 (例: "$1.47")
- マージン: 小数点以下 1 桁 (% 記号付き) (例: 「24.5%」)
- 成長率: 小数点以下 1 桁 +/- 記号 (例: "+5.2%"、"-3.1%")
- 時価総額: $B の小数点第 1 位 (例: "$562.1B")
- 株価：小数点第2位（例：「$172.35」）
- PER: 小数点第 1 位に「x」を付けます (例: 「25.3x」)

<a id="color-coding"></a>
### カラーコーディング
- 正の値: `class="pos"` -- 緑 (#0d7a3e)
- 負の値: `class="neg"` -- 赤 (#c0392b)
- ニュートラル/フラット: `class="neutral"` -- グレー (#555)
- 対象会社行: `class="highlight-row"` -- 水色の背景

<a id="figure-labels"></a>
### 図のラベル
- すべての図に順番に番号を付けます (「図 1:」、「図 2:」など)。
- 図 1 ～ 8 は 3 ～ 5 ページにあります (2 ページのコンセンサス推定の表には番号が付いていません)。
- すべての図表の下に出典の帰属を含めます:「出典: S&P Capital IQ」

<a id="hyperlinked-claims"></a>
### ハイパーリンクされたクレーム
- レポート本文内のすべての事実主張 (数値および定性的記述) は、`<a href="#ref-N" class="data-ref">CLAIM TEXT</a>` で囲む必要があります。
- `ref-N` ID は、付録テーブルの行と一致する必要があります
- これは、説明文、箇条書き、表のセル、ブロック引用符など、事実が現れるあらゆる場所に適用されます。
- グラフの軸ラベルとツールヒントにはハイパーリンクは必要ありません (レポート本文テキストのみ)
- レポートを作成するときに、参照 ID を順番に割り当てます (`ref-1`、`ref-2`、...)。
- 同じ基礎となるクレームへの複数の参照は、同じ参照 ID を共有する必要があります
- 定性的な主張の場合は、キーワード `<a href="#ref-25" class="data-ref">management flagged tariff headwinds</a>` をラップします。

<a id="appendix"></a>
### 付録
- **必ず次で始める必要があります**: `<div class="ai-disclaimer">Analysis is AI-generated — please confirm all outputs</div>`
- 付録は、すべての図表の後に置くレポートの最終セクションです。
- **4 列**: 参照番号 | 事実 | 値 | ソースと派生
- レポート内で参照される一意のクレームごとに 1 行 (数値および非数値)
- **レポート本文のすべての数値は、付録行へのクリック可能な `<a href="#ref-N">` リンクである必要があります。例外はありません。**
- 分類ごとに行をまとめます：四半期財務、評価、決算説明会の発言に基づく主張、業績予想とコンセンサス、ニュースとアナリストの見方、株価パフォーマンス
- 小見出し行 (`appendix-group` クラス) を使用してグループを区切ります
- **ソースと派生列**には、すべての行の具体的で詳細なソースを含める必要があります。
  - 生の S&P データ (収益、EPS、価格、時価総額など) の場合: `<span class="src-label">S&P Capital IQ</span>` の後にパラメーターを指定した特定の MCP 関数呼び出しが続きます (例: `get_financial_line_item_from_identifiers(identifier='WMT', line_item='revenue', period_type='quarterly', period='Q3 FY2026')`)。 **詳細を書かずに「S&P Capital IQ」だけを書かないでください。**
  - 計算値 (利益率、成長率、PER、リターン) の場合: `<a class="data-ref">` ハイパーリンクを含む完全な式は各コンポーネント行にリンクされます (`formula` CSS クラスを使用)。 **式内のすべての数値は、独自の付録行へのクリック可能なリンクである必要があります。**
  - トランスクリプトのクレームの場合: イタリック体の逐語的抜粋文 (`excerpt` CSS クラス) + `transcript-ref` クラスのトランスクリプト名 + `key_dev_id`
  - Kensho の結果の場合: 主要な結果 (`excerpt` クラス) + **クリック可能なソース URL** (`<a href="[URL]" target="_blank" class="src-url">[Source Title]</a>`) + 使用された検索クエリ。 **Kensho が提供するすべての申し立てには、元のソースへのクリック可能な URL が必要です。**
- ソース ラベルは `src-label` CSS クラスを使用します (太字のネイビー)
- 外部ソース URL は、`src-url` CSS クラスを使用します (青色、下線付き、クリック可能)

<a id="style-rules"></a>
### スタイルルール
- **絵文字はレポートのどこにも含まれていません**。見出し、表、グラフのラベル、本文には絵文字を使用しないでください。これは専門的な研究文書です。
- フォントは本文、見出し、表、グラフのすべてでArial Narrowを使います。
- 経営陣の発言は、投資仮説の要旨の説明文の中に`<blockquote>`として組み込みます。独立した見出しにはしません。
- すべてのテキストは簡潔にしてください。印刷ページ数は合計 4 ～ 5 ページを目標とします (付録は追加です)。
