> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../plugins/partner-built/lseg/CONNECTORS.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="connectors"></a>
# コネクタ

このプラグインは、LSEG（London Stock Exchange Group：ロンドン証券取引所グループ）の金融分析ツールを提供する **LFA MCP Server** へ接続する。全ツールは1つの MCP サーバーから提供され、追加のコネクタは不要である。

<a id="how-commands-reference-tools"></a>
## コマンドによるツールの参照方法

各コマンドは MCP ツールの正確な名前（`bond_price`、`interest_rate_curve` など）を使う。分かりやすくするため、次のカテゴリーに整理している。

<a id="tool-categories"></a>
## ツールのカテゴリー

| カテゴリー | プレースホルダー | ツール | 説明 |
|----------|-------------|-------|-------------|
| 債券価格評価 | `~~bond-pricing` | `bond_price`, `bond_future_price` | 詳細な分析を伴う債券・債券先物の価格評価 |
| FX価格評価 | `~~fx-pricing` | `fx_spot_price`, `fx_forward_price` | 為替スポット・フォワードレートの評価 |
| 金利カーブ | `~~ir-curves` | `interest_rate_curve`, `inflation_curve` | 国債利回りカーブとブレークイーブン・インフレ率 |
| クレジットカーブ | `~~credit-curves` | `credit_curve` | 発行体種別のクレジットスプレッド・カーブ |
| FXカーブ | `~~fx-curves` | `fx_forward_curve` | 為替フォワードポイント・カーブ |
| オプション | `~~options` | `option_value`, `option_template_list` | グリークスを伴うオプション評価 |
| スワップ | `~~swaps` | `ir_swap` | 金利スワップの価格評価 |
| ボラティリティ・サーフェス | `~~volatility` | `fx_vol_surface`, `equity_vol_surface` | 為替・株式のインプライド・ボラティリティ曲面 |
| 定量分析 | `~~qa` | `qa_ibes_consensus`, `qa_company_fundamentals`, `qa_historical_equity_price`, `qa_macroeconomic` | アナリスト予想、ファンダメンタルズ、価格、マクロデータ |
| 時系列 | `~~time-series` | `tscc_historical_pricing_summaries` | 過去の価格要約（日をまたぐ間隔／日中の間隔） |
| 債券分析 | `~~yieldbook` | `yieldbook_bond_reference`, `yieldbook_cashflow`, `yieldbook_scenario`, `fixed_income_risk_analytics` | 債券属性、キャッシュフロー、シナリオ、OAS・デュレーション |

<a id="complete-tool-reference"></a>
## 全ツールの参照情報

<a id="bond-domain"></a>
### 債券分野
- **`bond_price`** — 債券の価格・価値・分析指標を計算する。ISIN、RIC、CUSIP、AssetId を受け付ける。利回り、デュレーション、コンベクシティ、DV01、経過利息を返す。価格・利回りの上書きによる仮定シナリオに対応する。
- **`bond_future_price`** — 債券先物の価格と分析指標を計算する。理論価格、最割安受渡適格銘柄（CTD）の特定、受渡適格銘柄群、交換比率、先物契約の DV01 を返す。

<a id="fx-domain"></a>
### FX分野
- **`fx_spot_price`** — ISO通貨ペアの為替スポットレートを評価する。仲値・買値・売値を返す。
- **`fx_forward_price`** — 指定した期間・日付の為替フォワードレートを評価する。フォワードポイント、アウトライトレート、キャリーを返す。

<a id="curves-domain"></a>
### カーブ分野
- **`interest_rate_curve`** — 国債利回りカーブ。利用可能なカーブの一覧取得後、各点を計算する2段階方式。パーレート・ゼロレート、割引係数、フォワードレートを返す。
- **`credit_curve`** — クレジットスプレッド・カーブ。国と発行体種別（企業、国、政府機関など）で検索し、スプレッドの期間構造を計算する。
- **`inflation_curve`** — ブレークイーブン・インフレ率のカーブ。国・通貨で検索し、ブレークイーブン・インフレ率と実質利回りを計算する。
- **`fx_forward_curve`** — 為替フォワードポイント・カーブ。カーブを一覧取得後、すべての標準期間のフォワードポイントを計算する。

<a id="swaps-domain"></a>
### スワップ分野
- **`ir_swap`** — 金利スワップの価格評価。通貨・参照金利指数でテンプレートを一覧取得し、指定期間のスワップを評価する2段階方式。パーレート、DV01、NPV を返す。

<a id="options-domain"></a>
### オプション分野
- **`option_value`** — バニラ、バリア、バイナリー、アジアン・オプションに対応する評価。プレミアム、全グリークス（デルタ、ガンマ、ベガ、シータ、ロー）、リスク指標を返す。
- **`option_template_list`** — 価格評価に利用できるオプション・テンプレートの一覧。

<a id="volatility-domain"></a>
### ボラティリティ分野
- **`fx_vol_surface`** — SABRモデルによる為替ボラティリティ曲面生成。期間とデルタ別の権利行使価格にわたる曲面を返す。
- **`equity_vol_surface`** — 株式のインプライド・ボラティリティ曲面。株式・指数は RIC、先物は RICROOT に対応する。

<a id="quantitative-analytics-domain"></a>
### 定量分析分野
- **`qa_ibes_consensus`** — IBESアナリスト・コンセンサス予想（EPS、売上高、EBITDA、DPS）。将来予想に、アナリスト数、ばらつき、最高・最低予想の範囲を付ける。
- **`qa_company_fundamentals`** — 公表済み企業財務（損益計算書、貸借対照表の指標）。過去の会計年度データ。
- **`qa_historical_equity_price`** — OHLCV、トータルリターン、ベータを含む過去の株価。
- **`qa_macroeconomic`** — マクロ経済指標データベース。ニーモニックまたは説明で検索し、最新値・時系列を取得する。

<a id="time-series-domain"></a>
### 時系列分野
- **`tscc_historical_pricing_summaries`** — 任意の RIC の過去の価格要約。日をまたぐ間隔（日次・週次・月次）と、日中の間隔（1分〜1時間）に対応する。

<a id="fixed-income-analytics-yieldbook-domain"></a>
### 債券分析（YieldBook）分野
- **`yieldbook_bond_reference`** — 債券属性：証券種別、セクター、格付け、クーポン、満期、発行体。
- **`yieldbook_cashflow`** — 債券キャッシュフロー予測：将来の利払い・元本返済の予定。
- **`yieldbook_scenario`** — 債券シナリオ分析：金利の平行移動時の価格・利回り。
- **`fixed_income_risk_analytics`** — 債券リスク分析：OAS、実効デュレーション、キー・レート・デュレーション、コンベクシティ。
