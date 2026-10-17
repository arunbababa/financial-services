---
description: Generate a comprehensive equity research snapshot with consensus estimates, fundamentals, and price performance
argument-hint: "<ticker e.g. AAPL> [period e.g. FY2024-FY2026]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/partner-built/lseg/commands/research-equity.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：コンセンサス予想、ファンダメンタルズ、価格パフォーマンスをまとめた総合的な株式調査の概要を作る。

<a id="research-equity"></a>
# 株式調査

> LSEGの定量分析、過去の価格、マクロ経済データのツールを使う。利用可能なツールは [CONNECTORS.md](../CONNECTORS.md) を参照。

アナリスト・コンセンサス予想、過去の財務、価格パフォーマンス、マクロ経済の状況を組み合わせ、総合的な株式調査の概要を作る。

ファンダメンタルズ分析と予想の解釈は **equity-research** スキルを参照。

<a id="workflow"></a>
## ワークフロー

<a id="1-gather-input"></a>
### 1. 入力を集める

ユーザーへ次を尋ねる。
- ティッカー（必須）：IBES形式（例 AAPL、MSFT、VOD）
- 関心のある将来期間（任意、既定は今後2会計年度）
- 特に見る領域（例 利益、売上高、配当）

<a id="2-gather-consensus-estimates"></a>
### 2. コンセンサス予想を集める

ティッカーを指定して `qa_ibes_consensus` でFY1・FY2予想を取得する。
- 指標：EPS、Revenue、EBITDA、DPS
- 期間種別："A"（年次）

予想の中央値・平均値、アナリスト数、最高・最低範囲、ばらつきを抽出する。

<a id="3-pull-historical-fundamentals"></a>
### 3. 過去のファンダメンタルズを取得する

直近3〜5会計年度について `qa_company_fundamentals` を呼ぶ。

売上成長率、利益率推移、レバレッジ、利益の軌跡を抽出する。

<a id="4-assess-price-performance"></a>
### 4. 株価パフォーマンスを評価する

1Yの履歴で `qa_historical_equity_price` を呼ぶ。

年初来リターン、1年リターン、52週の範囲、ベータを計算する。

<a id="5-recent-price-action-detail"></a>
### 5. 最近の値動きの詳細

`interval: "P1D"`、`tenor: "3M"` で `tscc_historical_pricing_summaries` を呼ぶ。

日次OHLCV、出来高の傾向、直近のモメンタムを抽出する。

<a id="6-macro-context"></a>
### 6. マクロの状況

企業の主市場のGDP、CPI、政策金利について `qa_macroeconomic` を呼ぶ。

経済環境が当該セクターの追い風か向かい風かをまとめる。

<a id="7-synthesize-the-report"></a>
### 7. レポートをまとめる

コンセンサス予想表、過去財務の概要、評価指標（予想PER = 株価 / コンセンサスEPS）、価格パフォーマンス、マクロ背景、投資判断の根拠の要約を示す。

<a id="output-format"></a>
## 出力形式

構造化した調査メモとする。1〜2文の投資判断の根拠の要約を先に示し、根拠となる各節の詳細を表付きで続ける。
