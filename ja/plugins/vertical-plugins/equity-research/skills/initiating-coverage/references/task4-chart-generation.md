> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task4-chart-generation.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="task-4-chart-generation---detailed-workflow"></a>
# タスク 4: チャートの生成 - 詳細なワークフロー

このドキュメントでは、カバレッジ開始スキルのタスク 4 (チャートの生成) を実行するための段階的な手順を説明します。

<a id="task-overview"></a>
## タスクの概要

**目的**: レポート用に 25 ～ 35 の専門的な財務チャートを生成します。

**前提条件**: ⚠️ 開始する前に確認してください
- **必須**: タスク 1 の企業調査
  - 会社の歴史、マイルストーン（年表用）
  - 経営陣、組織構造（組織図用）
  - 製品ポートフォリオ（製品チャート用）
  - 顧客セグメンテーション（顧客グラフ用）
  - 競争環境（競争上のポジショニングチャート用）
  - TAM分析（市場規模チャート用）
- **必須**: タスク 2 の財務モデル
  - 製品/地域別売上高データ
  - 利益率の推移
  - シナリオ比較データ
- **必須**: タスク 3 のバリュエーション分析
  - DCF感度表
  - 比較対象会社データ
  - 評価範囲
- **必須**: 外部市場データ
  - 過去の株価データ（Yahoo Finance、Bloomberg）
  - 過去のバリュエーション倍率（チャート 34 のオプション）

**⚠️ 重要: タスク 1、2、および 3 が完了するまでは、このタスクを開始しないでください**

このタスクには、前の 3 つのタスクすべてからの出力が必要です。それらなしで開始すると、不完全なチャートが作成されます。

**タスク 1、2、または 3 のいずれかが完了していない場合**: すぐに停止し、どのタスクを最初に完了する必要があるかをユーザーに通知します。具体的な要件は次のとおりです。
- タスク 1: 企業調査ドキュメント (9 つのチャート用)
- タスク 2: 6 つのタブすべてを含む財務モデル (8 つのチャート用)
- タスク 3: モデルに追加された評価タブ (6 つのチャート用)
- 外部データアクセス (2 つのチャートの場合)

プレースホルダー グラフを作成したり、データが欠落しているためにグラフをスキップしたりしないでください。

**出力**: 25 ～ 35 のプロフェッショナル チャート ファイル (PNG/JPG、300 DPI)

---

<a id="input-verification"></a>
## 入力検証

**開始する前に - すべての前提条件を確認してください:**

<a id="task-1-verification-company-research"></a>
### 課題1 検証（企業調査）
- [ ] タスク 1 は完了しましたか? （企業調査文書が存在する）
- [ ] 会社の歴史とマイルストーンは文書化されていますか? (チャート05、06用)
- [ ] 経営チームと組織構造について説明されていますか? (チャート07の場合)
- [ ] 製品ポートフォリオの詳細は? (チャート08の場合)
- [ ] 顧客のセグメンテーションを分析しましたか? (チャート09の場合)
- [ ] 競争環境はマッピングされていますか? (チャート16、17、18の場合)
- [ ] TAM のサイジングは完了しましたか? (図表15の場合)

<a id="task-2-verification-financial-model"></a>
### タスク2の検証（財務モデル）
- [ ] タスク 2 は完了しましたか? （財務モデルExcelファイルあり）
- [ ] 製品別売上高の内訳はありますか? (チャート 03 ⭐)
- [ ] 地域別売上高の内訳はありますか? (チャート 04 ⭐)
- [ ] 過去の財務と予測の財務は完了しましたか? (チャート02、10、11、12用)
- [ ] シナリオ分析 (強気/ベース/弱気) は完了しましたか? (図表14の場合)
- [ ] 事業指標は利用可能ですか? (図13の場合)

<a id="task-3-verification-valuation"></a>
### タスク3 検証（評価）
- [ ] タスク 3 は完了しましたか? (評価タブがモデルに追加されました)
- [ ] DCF 感度マトリックスは存在しますか? (チャート 28 ⭐)
- [ ] DCF 計算の詳細は入手可能ですか? (図表29の場合)
- [ ] 比較対象企業のデータは収集されていますか? (チャート30、31の場合)
- [ ] 評価範囲は計算されていますか? (チャート 32 ⭐)

<a id="external-data-verification"></a>
### 外部データの検証
- [ ] 過去の株価データにアクセスできますか? (グラフ 01 については Yahoo Finance、Bloomberg)
- [ ] 過去の評価データにアクセスできますか? (オプション、チャート 34 の場合)

**検証が失敗した場合**:
- タスク 1 がありませんか? → タスク 1 (企業調査) を最初に完了してください
- タスク 2 がありませんか? → 最初にタスク 2 (財務モデリング) を完了します。
- タスク 3 がありませんか? → 最初にタスク 3 (バリュエーション分析) を完了します。
- 外部データが欠落していますか? → Yahoo Finance、Bloomberg、または同様の情報源から収集します。

---

<a id="chart-requirements-25-required--10-optional"></a>
## チャートの要件: 必須 25 + オプション 10

**重要**: タスク 5 (レポート アセンブリ) では、**作成されたすべてのグラフ**がレポート全体に埋め込まれます。レポートには緻密なビジュアル コンテンツ (200 ～ 300 ワードごとに 1 つのグラフ) が必要なので、包括的なグラフ カバレッジを作成します。

<a id="4-mandatory-charts-non-negotiable-"></a>
### 4 必須チャート (交渉不可) ⭐

これら 4 つのグラフは、必ず存在する必要がある重要な視覚化です。

1. **chart_03**: 製品/セグメント別売上高 - 積み上げ面グラフ ⭐
2. **chart_04**: 地域別売上高 - 積み上げ棒グラフ ⭐
3. **chart_28**: DCF 感度分析 - 2 方向ヒートマップ ⭐
4. **chart_32**: バリュエーション・フットボールフィールド - 横棒グラフ ⭐

<a id="25-required-charts-complete-set"></a>
### 25 必須チャート (完全なセット)

これらのグラフを 25 個すべて作成します。タスク 5 では、それぞれに特定の目的があります。

**投資概要セクション (1 つのグラフ):**
- chart_01: 株価パフォーマンス (12～24 か月)

**財務パフォーマンスセクション (6 つのグラフ):**
- chart_02: 売上高成長の推移
- chart_03: 製品別売上高 - 積み上げエリア ⭐ 必須
- chart_04: 地域別売上高 - 積み上げ棒 ⭐ 必須
- chart_10: 売上総利益率の推移
- chart_11: EBITDA利益率の推移
- chart_12: フリーキャッシュフローの傾向

**企業の基礎知識（Company 101） セクション (7 つのチャート):**
- chart_05: 会社概要/タイムライン
- chart_06: 主要なマイルストーンのタイムライン
- chart_07: 組織構造
- chart_08: 製品ポートフォリオの概要
- chart_09: 顧客のセグメンテーション
- chart_15: 市場規模の進化 (TAM)
- chart_16: 競争力のあるポジショニング マトリックス

**競争と市場セクション (2 つのグラフ):**
- chart_17: 市場シェアの内訳
- chart_18: 競合ベンチマーク

**シナリオ分析セクション (2 つのグラフ):**
- chart_13: 事業指標ダッシュボード
- chart_14: シナリオの比較 (強気/ベース/弱気)

**評価セクション (7 つのチャート):**
- chart_28: DCF 感度ヒートマップ ⭐ 必須
- chart_29: DCF 評価のウォーターフォール
- chart_30: 類似企業比較の散布図
- chart_31: 同業他社の評価倍率の比較
- chart_32: バリュエーション・フットボールフィールド ⭐ 必須
- chart_33: 目標株価シナリオ
- chart_34: 過去のバリュエーション倍率

**合計: 25 の必須チャート**

<a id="10-optional-charts-for-30-35-range"></a>
### 10 個のオプションのチャート (30 ～ 35 の範囲用)

視覚的な密度とストーリーテリングを高めるためにこれらを追加します (合計 26 ～ 35 に達します)。

- chart_19: 顧客獲得の傾向
- chart_20: ユニットエコノミクスの進化
- chart_21: 製品ロードマップのタイムライン
- chart_22: 地理的拡大マップ
- chart_23: 研究開発投資の動向
- chart_24: 販売およびマーケティングの効率
- chart_25: 運転資本の傾向
- chart_26: 債務満期スケジュール
- chart_27: 所有権構造
- chart_35: アナリストの目標株価分布

**合計範囲: 25 ～ 35 のチャート (25 は必須 + 0 ～ 10 はオプション)**

---

<a id="data-source-mapping-for-required-charts"></a>
## 必要なグラフのデータ ソース マッピング

各グラフのデータの出所を理解する:

<a id="from-task-1-company-research---9-charts"></a>
### タスク 1 (企業調査) から - 9 つのチャート
- chart_05: 会社概要 → タスク 1: 会社概要セクション
- chart_06: 主要なマイルストーン → タスク 1: 会社の歴史セクション
- chart_07: 組織構造 → タスク 1: 経営陣セクション
- chart_08: 製品ポートフォリオ → タスク 1: 製品とサービス セクション
- chart_09: 顧客のセグメンテーション → タスク 1: 顧客と市場開拓セクション
- chart_15: 市場規模の進化 → タスク 1: 市場機会 (TAM) セクション
- chart_16: 競争力のあるポジショニング → タスク 1: 競争環境セクション
- chart_17: 市場シェア → タスク 1: 競争環境セクション
- chart_18: 競争力のベンチマーク → タスク 1: 競争環境セクション

<a id="from-task-2-financial-model---8-charts"></a>
### タスク 2 (財務モデル) から - 8 つのチャート
- chart_02: 売上高成長 → 損益計算書タブ （売上高の行）
- chart_03: 製品別売上高 ⭐ → 売上高モデル タブ (製品の内訳)
- chart_04: 地域別売上高 ⭐ → 売上高モデル タブ (地域の内訳)
- chart_10: 売上総利益率 → 損益計算書タブ (売上総利益 / 売上高)
- chart_11: EBITDA利益率 → 損益計算書タブ (EBITDA / 売上高)
- chart_12: フリー キャッシュ フロー → キャッシュ フロー計算書タブ (CFO - CapEx)
- chart_13: 事業指標 → 複数のタブ (損益計算書、キャッシュ フロー)
- chart_14: シナリオ比較 → シナリオタブ (強気/ベース/弱気)

<a id="from-task-3-valuation---6-charts"></a>
### タスク 3 (評価) より - 6 つのチャート
- chart_28: DCF 感度 ⭐ → 感度分析タブ
- chart_29: DCF ウォーターフォール → DCF タブ (企業価値の構成要素)
- chart_30: 類似企業比較の散布図 → 比較可能な企業タブ
- chart_31: 同業他社の評価倍率 → 比較対象企業タブ
- chart_32: バリュエーション・フットボールフィールド ⭐ → 「評価概要」タブ
- chart_33: 目標株価シナリオ → 評価概要タブ (またはシナリオから計算)

<a id="from-external-sources---2-charts"></a>
### 外部ソースから - 2 つのチャート
- chart_01: 株価パフォーマンス → Yahoo Finance、Bloomberg、Alpha Vantage
- chart_34: 過去のバリュエーション倍率 → Yahoo Finance、Bloomberg (過去のPER、EV/EBITDA)

**重要**: 必要な 25 個のグラフすべてを作成するには、3 つのタスク (1、2、3) すべてに加えて外部データ アクセスを完了する必要があります。

---

<a id="step-by-step-chart-generation-workflow"></a>
## ステップバイステップのチャート生成ワークフロー

<a id="step-1-set-up-environment"></a>
### ステップ 1: 環境をセットアップする

**必要なライブラリをインストールします:**
```bash
pip install matplotlib seaborn pandas numpy plotly
```

**Python スクリプト ヘッダーを作成します:**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set global style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Global settings
DPI = 300
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6
TITLE_FONT_SIZE = 14
AXIS_FONT_SIZE = 12
LABEL_FONT_SIZE = 10
```

<a id="step-2-extract-data-from-model-and-valuation"></a>
### ステップ 2: モデルと評価からデータを抽出する

<a id="a-extract-revenue-data"></a>
#### A. 売上高データの抽出
```python
# Revenue by Product (from Task 2 model)
years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]

# Extract from Excel or define manually from model
product_a = [100, 120, 145, 175, 210, 252, 302, 363, 435, 522]
product_b = [80, 95, 115, 138, 165, 198, 238, 285, 342, 411]
product_c = [50, 62, 78, 98, 122, 153, 191, 239, 299, 374]
product_d = [30, 38, 48, 61, 77, 97, 122, 153, 191, 239]

# Revenue by Geography
north_america = [150, 180, 220, 265, 320, 384, 461, 553, 664, 797]
europe = [80, 95, 115, 140, 170, 204, 245, 294, 353, 423]
asia_pacific = [40, 50, 63, 80, 101, 127, 159, 199, 249, 311]
rest_of_world = [20, 25, 32, 40, 51, 64, 80, 100, 125, 156]
```

<a id="b-extract-margin-data"></a>
#### B. 利益率データの抽出
```python
# Margin evolution
gross_margin = [58.0, 59.2, 60.5, 61.8, 63.0, 64.5, 66.0, 67.0, 67.5, 68.0]
ebitda_margin = [12.0, 15.5, 18.8, 22.0, 25.0, 28.0, 30.5, 32.0, 33.0, 34.0]
fcf_margin = [8.0, 11.0, 14.5, 18.0, 21.0, 24.0, 26.5, 28.0, 29.0, 30.0]
```

<a id="c-extract-dcf-sensitivity-data"></a>
#### C. DCF 感度データの抽出
```python
# DCF Sensitivity (from Task 3 valuation)
wacc_values = [7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
terminal_growth = [1.5, 2.0, 2.5, 3.0, 3.5]

# Price per share matrix (rows = WACC, columns = terminal growth)
dcf_sensitivity = np.array([
    [66, 71, 76, 82, 89],
    [58, 62, 67, 72, 78],
    [52, 55, 59, 63, 68],
    [47, 50, 53, 56, 60],
    [42, 45, 48, 51, 54],
    [39, 41, 44, 46, 49]
])
```

<a id="d-extract-valuation-ranges"></a>
#### D. 評価範囲の抽出
```python
# Valuation Football Field (from Task 3)
valuation_methods = ['DCF Analysis', 'Trading Comps\n(NTM)', 'Precedent\nTransactions']
valuation_low = [48, 45, 52]
valuation_high = [62, 57, 66]
current_price = 50
target_price = 55
```

<a id="step-3-create-mandatory-charts"></a>
### ステップ 3: 必須のグラフを作成する

<a id="chart-1-revenue-by-product---stacked-area--mandatory"></a>
#### グラフ 1: 製品別売上高 - 積み上げ領域 ⭐ 必須

```python
def create_revenue_by_product_chart():
    """Create revenue by product stacked area chart"""

    fig, ax = plt.subplots(figsize=(10, 6))

    # Create stacked area chart
    ax.stackplot(years, product_a, product_b, product_c, product_d,
                 labels=['Product A', 'Product B', 'Product C', 'Product D'],
                 colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
                 alpha=0.8)

    # Formatting
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Revenue ($M)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 3 - Revenue by Product/Segment (2020-2029E)',
                 fontsize=14, fontweight='bold', pad=20)

    # Legend
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    # Grid
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add vertical line to separate historical from projected
    ax.axvline(x=2024, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(2024.2, ax.get_ylim()[1]*0.95, 'Projected →',
            fontsize=9, color='gray', ha='left')

    # Source line
    fig.text(0.12, 0.02, 'Source: Company data, [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # Save
    plt.tight_layout()
    plt.savefig('chart_03_revenue_by_product_stacked_area.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created: chart_03_revenue_by_product_stacked_area.png")

create_revenue_by_product_chart()
```

<a id="chart-2-revenue-by-geography---stacked-bar--mandatory"></a>
#### グラフ 2: 地域別売上高 - 積み上げ棒 ⭐ 必須

```python
def create_revenue_by_geography_chart():
    """Create revenue by geography stacked bar chart"""

    years_labels = ['2020', '2021', '2022', '2023', '2024',
                    '2025E', '2026E', '2027E', '2028E', '2029E']

    fig, ax = plt.subplots(figsize=(10, 6))

    # Create stacked bar chart
    width = 0.6
    x = np.arange(len(years_labels))

    p1 = ax.bar(x, north_america, width, label='North America', color='#1f77b4')
    p2 = ax.bar(x, europe, width, bottom=north_america,
                label='Europe', color='#ff7f0e')
    p3 = ax.bar(x, asia_pacific, width,
                bottom=np.array(north_america) + np.array(europe),
                label='Asia-Pacific', color='#2ca02c')
    p4 = ax.bar(x, rest_of_world, width,
                bottom=np.array(north_america) + np.array(europe) + np.array(asia_pacific),
                label='Rest of World', color='#d62728')

    # Formatting
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Revenue ($M)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 4 - Revenue by Geography (2020-2029E)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years_labels, rotation=45, ha='right')

    # Legend
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    # Grid
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Source line
    fig.text(0.12, 0.02, 'Source: Company data, [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # Save
    plt.tight_layout()
    plt.savefig('chart_04_revenue_by_geography_stacked_bar.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created: chart_04_revenue_by_geography_stacked_bar.png")

create_revenue_by_geography_chart()
```

<a id="chart-3-dcf-sensitivity---heatmap--mandatory"></a>
#### チャート 3: DCF 感度 - ヒートマップ ⭐ 必須

```python
def create_dcf_sensitivity_heatmap():
    """Create DCF sensitivity analysis heatmap"""

    # Create DataFrame
    df = pd.DataFrame(dcf_sensitivity,
                      index=[f'{w}%' for w in wacc_values],
                      columns=[f'{g}%' for g in terminal_growth])

    fig, ax = plt.subplots(figsize=(8, 6))

    # Create heatmap
    sns.heatmap(df, annot=True, fmt='d', cmap='RdYlGn',
                cbar_kws={'label': 'Price per Share ($)'},
                linewidths=0.5, linecolor='white',
                ax=ax, vmin=35, vmax=95)

    # Formatting
    ax.set_xlabel('Terminal Growth Rate', fontsize=12, fontweight='bold')
    ax.set_ylabel('WACC', fontsize=12, fontweight='bold')
    ax.set_title('Figure 28 - DCF Sensitivity Analysis ($/share)',
                 fontsize=14, fontweight='bold', pad=20)

    # Rotate y-axis labels
    plt.yticks(rotation=0)

    # Source line
    fig.text(0.12, 0.02, 'Source: [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # Save
    plt.tight_layout()
    plt.savefig('chart_28_dcf_sensitivity_heatmap.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created: chart_28_dcf_sensitivity_heatmap.png")

create_dcf_sensitivity_heatmap()
```

<a id="chart-4-valuation-football-field--mandatory"></a>
#### チャート 4: バリュエーション・フットボールフィールド ⭐ 必須

```python
def create_valuation_football_field():
    """Create valuation football field chart"""

    fig, ax = plt.subplots(figsize=(10, 5))

    # Create horizontal bars
    y_positions = np.arange(len(valuation_methods))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

    for i, (method, low, high, color) in enumerate(
            zip(valuation_methods, valuation_low, valuation_high, colors)):
        ax.barh(i, high - low, left=low, height=0.6,
                color=color, alpha=0.7, label=method)

        # Add value labels at ends
        ax.text(low - 1, i, f'${low}', va='center', ha='right', fontsize=10)
        ax.text(high + 1, i, f'${high}', va='center', ha='left', fontsize=10)

    # Add current price line
    ax.axvline(x=current_price, color='red', linestyle='--', linewidth=2,
               label=f'Current: ${current_price}', alpha=0.7)

    # Add target price line
    ax.axvline(x=target_price, color='black', linestyle='-', linewidth=2,
               label=f'Target: ${target_price}')

    # Formatting
    ax.set_yticks(y_positions)
    ax.set_yticklabels(valuation_methods, fontsize=11)
    ax.set_xlabel('Price Per Share ($)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 32 - Valuation Football Field',
                 fontsize=14, fontweight='bold', pad=20)

    # Set x-axis limits
    ax.set_xlim(40, 70)

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Grid
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # Legend
    ax.legend(loc='upper right', frameon=False, fontsize=9)

    # Source line
    fig.text(0.12, 0.02, 'Source: [Firm] estimates',
             fontsize=9, style='italic', color='gray')

    # Save
    plt.tight_layout()
    plt.savefig('chart_32_valuation_football_field.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created: chart_32_valuation_football_field.png")

create_valuation_football_field()
```

<a id="step-4-create-remaining-required-charts-charts-1-34"></a>
### ステップ 4: 残りの必要なチャート (チャート 1 ～ 34) を作成する

**必須リストから残りのすべてのグラフを作成して、25 個の必須グラフ**を完成させます。タスク 5 では、各チャートに特定の目的があります。

<a id="investment-summary-1-chart"></a>
#### 投資概要 (1 つのグラフ)
```python
# chart_01: Stock Price Performance (12-24 months)
# - Line chart showing stock price over time vs. market index
# - Used on Page 1 of final report
```

<a id="financial-performance-5-additional-charts-beyond-chart_03-and-chart_04"></a>
#### 財務パフォーマンス (chart_03 と chart_04 を超える 5 つの追加チャート)
```python
# chart_02: Revenue Growth Trajectory
# chart_10: Gross Margin Evolution
# chart_11: EBITDA Margin Progression
# chart_12: Free Cash Flow Trend
# chart_14: Scenario Comparison (Bull/Base/Bear)
```

<a id="company-101-section-7-charts"></a>
#### 企業の基礎知識（Company 101） セクション (7 つのチャート)
```python
# chart_05: Company Overview/Timeline
# chart_06: Key Milestones Timeline
# chart_07: Organizational Structure
# chart_08: Product Portfolio Overview
# chart_09: Customer Segmentation
# chart_15: Market Size Evolution (TAM)
# chart_16: Competitive Positioning Matrix
```

<a id="competitive--market-2-charts"></a>
#### 競争と市場 (2 つのグラフ)
```python
# chart_17: Market Share Breakdown
# chart_18: Competitive Benchmarking
```

<a id="scenario-analysis-1-chart"></a>
#### シナリオ分析 (1 つのチャート)
```python
# chart_13: Operating Metrics Dashboard
```

<a id="valuation-section-6-additional-charts-beyond-chart_28-and-chart_32"></a>
#### 評価セクション (chart_28 と chart_32 を超える 6 つの追加チャート)
```python
# chart_29: DCF Valuation Waterfall
# chart_30: Trading Comps Scatter Plot
# chart_31: Peer Multiples Comparison
# chart_33: Price Target Scenarios
# chart_34: Historical Valuation Multiples
```

**すべてのグラフで一貫した書式設定を使用します:**
- 300 DPI 解像度
- プロフェッショナルな配色
- 明確なラベル・凡例・タイトル
- 図番号 (例: 「図 5 - 会社のタイムライン」)
- 出典の引用は下部にあります

<a id="step-4b-create-optional-charts-for-26-35-total"></a>
### ステップ 4B: オプションのグラフを作成する (合計 26 ～ 35 個)

**オプション**: 視覚的な密度を高めるために、このリストから 1 ～ 10 個のグラフを追加します。

```python
# chart_19: Customer Acquisition Trends
# chart_20: Unit Economics Evolution
# chart_21: Product Roadmap Timeline
# chart_22: Geographic Expansion Map
# chart_23: R&D Investment Trends
# chart_24: Sales & Marketing Efficiency
# chart_25: Working Capital Trends
# chart_26: Debt Maturity Schedule
# chart_27: Ownership Structure
# chart_35: Analyst Price Target Distribution
```

これらのオプションのチャートは、追加の視覚的なストーリーテリングを提供し、タスク 5 の「200 ～ 300 ワードごとに 1 つのチャート」という密度目標の達成に役立ちます。

<a id="step-5-create-chart-index"></a>
### ステップ 5: チャートインデックスを作成する

すべてのチャートを文書化したテキスト ファイルを作成します。

```python
def create_chart_index():
    """Create index of all charts"""

    # 25 REQUIRED CHARTS
    required_charts = [
        "chart_01_stock_price_performance.png - Stock Price Performance (12-24M)",
        "chart_02_revenue_growth_trajectory.png - Revenue Growth Trajectory",
        "chart_03_revenue_by_product_stacked_area.png - Revenue by Product [MANDATORY]",
        "chart_04_revenue_by_geography_stacked_bar.png - Revenue by Geography [MANDATORY]",
        "chart_05_company_overview.png - Company Overview/Timeline",
        "chart_06_key_milestones_timeline.png - Key Milestones Timeline",
        "chart_07_organizational_structure.png - Organizational Structure",
        "chart_08_product_portfolio.png - Product Portfolio Overview",
        "chart_09_customer_segmentation.png - Customer Segmentation",
        "chart_10_gross_margin_evolution.png - Gross Margin Evolution",
        "chart_11_ebitda_margin_progression.png - EBITDA Margin Progression",
        "chart_12_free_cash_flow_trend.png - Free Cash Flow Trend",
        "chart_13_operating_metrics_dashboard.png - Operating Metrics Dashboard",
        "chart_14_scenario_comparison.png - Scenario Comparison (Bull/Base/Bear)",
        "chart_15_market_size_evolution.png - Market Size Evolution (TAM)",
        "chart_16_competitive_positioning.png - Competitive Positioning Matrix",
        "chart_17_market_share.png - Market Share Breakdown",
        "chart_18_competitive_benchmarking.png - Competitive Benchmarking",
        "chart_28_dcf_sensitivity_heatmap.png - DCF Sensitivity Heatmap [MANDATORY]",
        "chart_29_dcf_waterfall.png - DCF Valuation Waterfall",
        "chart_30_trading_comps_scatter.png - Trading Comps Scatter Plot",
        "chart_31_peer_multiples_comparison.png - Peer Multiples Comparison",
        "chart_32_valuation_football_field.png - Valuation Football Field [MANDATORY]",
        "chart_33_price_target_scenarios.png - Price Target Scenarios",
        "chart_34_historical_valuation_multiples.png - Historical Valuation Multiples",
    ]

    # 10 OPTIONAL CHARTS (for 26-35 range)
    optional_charts = [
        "chart_19_customer_acquisition_trends.png - Customer Acquisition Trends [OPTIONAL]",
        "chart_20_unit_economics_evolution.png - Unit Economics Evolution [OPTIONAL]",
        "chart_21_product_roadmap_timeline.png - Product Roadmap Timeline [OPTIONAL]",
        "chart_22_geographic_expansion_map.png - Geographic Expansion Map [OPTIONAL]",
        "chart_23_rd_investment_trends.png - R&D Investment Trends [OPTIONAL]",
        "chart_24_sales_marketing_efficiency.png - Sales & Marketing Efficiency [OPTIONAL]",
        "chart_25_working_capital_trends.png - Working Capital Trends [OPTIONAL]",
        "chart_26_debt_maturity_schedule.png - Debt Maturity Schedule [OPTIONAL]",
        "chart_27_ownership_structure.png - Ownership Structure [OPTIONAL]",
        "chart_35_analyst_price_targets.png - Analyst Price Target Distribution [OPTIONAL]",
    ]

    with open('chart_index.txt', 'w') as f:
        f.write("CHART INDEX FOR [COMPANY] EQUITY RESEARCH REPORT\n")
        f.write("=" * 60 + "\n\n")

        f.write("4 MANDATORY CHARTS (Must be present):\n")
        f.write("- chart_03: Revenue by Product (Stacked Area) ⭐\n")
        f.write("- chart_04: Revenue by Geography (Stacked Bar) ⭐\n")
        f.write("- chart_28: DCF Sensitivity (Heatmap) ⭐\n")
        f.write("- chart_32: Valuation Football Field ⭐\n\n")

        f.write("25 REQUIRED CHARTS:\n")
        for chart in required_charts:
            f.write(f"  {chart}\n")

        f.write("\n10 OPTIONAL CHARTS (for 26-35 total):\n")
        for chart in optional_charts:
            f.write(f"  {chart}\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("NOTE: Task 5 will embed ALL charts created (25-35) throughout\n")
        f.write("the report for visual density (1 chart every 200-300 words).\n")

    print("✓ Created: chart_index.txt")

create_chart_index()
```

<a id="step-6-quality-check"></a>
### ステップ 6: 品質チェック

**検証チェックを実行します:**

```python
import os

def verify_charts():
    """Verify all charts were created successfully"""

    mandatory_charts = [
        'chart_03_revenue_by_product_stacked_area.png',
        'chart_04_revenue_by_geography_stacked_bar.png',
        'chart_28_dcf_sensitivity_heatmap.png',
        'chart_32_valuation_football_field.png'
    ]

    print("\n" + "="*60)
    print("CHART GENERATION VERIFICATION")
    print("="*60)

    # Check mandatory charts
    print("\n1. MANDATORY CHARTS:")
    all_mandatory_present = True
    for chart in mandatory_charts:
        if os.path.exists(chart):
            size = os.path.getsize(chart) / 1024  # KB
            print(f"   ✓ {chart} ({size:.1f} KB)")
        else:
            print(f"   ✗ MISSING: {chart}")
            all_mandatory_present = False

    # Count total charts
    chart_files = [f for f in os.listdir('.') if f.startswith('chart_') and f.endswith('.png')]
    print(f"\n2. TOTAL CHARTS: {len(chart_files)}")
    print(f"   Target: 25-35 charts")
    print(f"   Status: {'✓ PASS' if 25 <= len(chart_files) <= 35 else '⚠ WARNING'}")

    # Check file sizes (should be > 50KB for 300 DPI)
    print("\n3. FILE SIZE CHECK:")
    small_files = []
    for chart in chart_files[:5]:  # Sample first 5
        size = os.path.getsize(chart) / 1024
        if size < 50:
            small_files.append(chart)
        print(f"   {chart}: {size:.1f} KB")

    if small_files:
        print(f"   ⚠ WARNING: {len(small_files)} files may be low resolution")
    else:
        print(f"   ✓ All sampled files have adequate size")

    # Final verdict
    print("\n" + "="*60)
    if all_mandatory_present and 25 <= len(chart_files) <= 35:
        print("✓ VERIFICATION PASSED - Ready for Task 5")
    else:
        print("✗ VERIFICATION FAILED - Review missing charts")
    print("="*60 + "\n")

verify_charts()
```

---

<a id="quality-standards"></a>
## 品質基準

<a id="visual-quality"></a>
### ビジュアル品質
- [ ] 高解像度 (最低 300 DPI)
- [ ] プロフェッショナルな配色 (すべてのチャートで一貫しています)
- [ ] 鮮明で読みやすいテキスト (9pt 未満のフォントは使用できません)
- [ ] 適切なアスペクト比（歪みがないこと）
- [ ] ピクセル化やアーティファクトがない

<a id="data-accuracy"></a>
### データの精度
- [ ] データはソースと一致します (財務モデルと評価)
- [ ] 適切な単位とラベル (百万ドル、パーセンテージなど)
- [ ] 適切なスケールと範囲
- [ ] チャート全体で一貫した期間
- [ ] 検証済みの計算

<a id="formatting-quality"></a>
### フォーマットの品質
- [ ] すべてのグラフにわたる一貫したスタイル
- [ ] 適切な図の番号付け (連番)
- [ ] タイトルとキャプションを明確にする
- [ ] すべてのグラフの出典引用
- [ ] プロフェッショナルな外観

<a id="completeness"></a>
### 完全性
- [ ] 4 つの必須チャートがすべて作成されました
- [ ] 合計 25 ～ 35 のチャート
- [ ] 適切なファイル名 (chart_01、chart_02 など)
- [ ] チャートインデックスが作成されました
- [ ] Word に埋め込む準備ができました

---

<a id="chart-types-reference"></a>
## グラフの種類のリファレンス

<a id="when-to-use-each-chart-type"></a>
### 各グラフの種類をいつ使用するか

**折れ線グラフ**: 時系列の推移（売上高、利益率、株価）

**スタックエリア**: 製品別売上高 ⭐、市場規模の構成

**積み上げバー**: 地域別売上高 ⭐、四半期内訳

**ヒートマップ**: DCF 感度 ⭐、相関行列

**横棒**: バリュエーション・フットボールフィールド ⭐、ピアランキング

**ウォーターフォール**: 売上高ブリッジ、利益率分析、DCF の構築

**散布図/バブルチャート**: 成長率とバリュエーション、競争上の位置付け

**2×2 マトリックス**: 競争力のあるポジショニング、製品ポートフォリオ

---

<a id="file-naming-convention"></a>
## ファイル命名規則

**常にこの形式を使用してください:**
```
chart_[NUMBER]_[DESCRIPTION].png

Examples:
chart_01_stock_price_performance.png
chart_03_revenue_by_product_stacked_area.png
chart_28_dcf_sensitivity_heatmap.png
```

**作成順序ではなく、レポート内の位置に基づいてチャートに連番を付けます**。

---

<a id="common-chart-generation-issues"></a>
## チャート生成に関する一般的な問題

<a id="issue-1-low-resolution"></a>
### 問題 1: 低解像度
**問題**: グラフがピクセル化して見える
**解決策**: `plt.savefig()` で `dpi=300` を確認してください

<a id="issue-2-text-cutoff"></a>
### 問題 2: テキストの切れ目
**問題**: ラベルまたはタイトルの端が切れている
**解決策**: `plt.savefig()` で `bbox_inches='tight'` を使用します。

<a id="issue-3-poor-colors"></a>
### 問題 3: 色が悪い
**問題**: 色がプロフェッショナルに見えない
**解決策**: Tableau10 などの確立されたパレットを使用するか、カスタムのコーポレートカラーを定義します

<a id="issue-4-overlapping-labels"></a>
### 問題 4: ラベルの重複
**問題**: 軸ラベルが重なっています
**解決策**: ラベルを回転するか (例: `rotation=45`)、フォント サイズを小さくします。

<a id="issue-5-white-space"></a>
### 問題 5: ホワイトスペース
**問題**: グラフの周囲に空白が多すぎる
**解決策**: 保存する前に `plt.tight_layout()` を使用してください

---

<a id="success-criteria"></a>
## 成功基準

チャート パッケージが成功するには、次のことが必要です。
1. **4 つの必須チャートをすべて含めます** (確認済み) ⭐
   - chart_03: 製品別売上高
   - chart_04: 地域別売上高
   - chart_28: DCF 感度
   - chart_32: バリュエーション・フットボールフィールド
2. **最低 25 個の必要なチャートを作成します** (確認済み)
3. **オプション: 1 ～ 10 の追加チャート** (合計 26 ～ 35)
4. すべてのチャートにわたって一貫したプロフェッショナルなスタイルを実現する
5. 印刷品質を高めるために高解像度 (300 DPI) であること
6. すべてのグラフに明確なラベル、凡例、タイトルを付ける
7. 適切な図番号と出典の引用を含める
8. Word にすぐに埋め込む準備を整える
9. すべての主要な財務指標と分析を網羅
10. 書面による分析を補完する視覚的なストーリーを伝える
11. ソースデータ（モデル/バリュエーション）に照らして正確で、追跡検証できること
12. すべてのチャートはチャート インデックス付きの zip ファイルにパッケージ化されています

**注意してください**: タスク 5 では、視覚的な密度を高めるために、作成されたすべてのグラフ (25 ～ 35) がレポート全体に埋め込まれます。

---

<a id="output-files"></a>
## 出力ファイル

タスク 4 を完了すると、次の成果物が得られます。

**25 個の必須チャート ファイル (最小):**
1. chart_01_stock_price_performance.png
2. chart_02_revenue_growth_trajectory.png
3. chart_03_revenue_by_product_stacked_area.png ⭐ 必須
4. chart_04_revenue_by_geography_stacked_bar.png ⭐ 必須
5. chart_05_company_overview.png
6. chart_06_key_milestones_timeline.png
7. chart_07_organizational_structure.png
8. chart_08_product_portfolio.png
9. chart_09_customer_segmentation.png
10. chart_10_gross_margin_evolution.png
11. chart_11_ebitda_margin_progression.png
12. chart_12_free_cash_flow_trend.png
13. chart_13_operating_metrics_dashboard.png
14. chart_14_scenario_comparison.png
15. chart_15_market_size_evolution.png
16. chart_16_competitive_positioning.png
17. chart_17_market_share.png
18. chart_18_competitive_benchmarking.png
19-27。 *作成された場合はオプションのチャート用に予約されます*
28. chart_28_dcf_sensitivity_heatmap.png ⭐ 必須
29. chart_29_dcf_waterfall.png
30. chart_30_trading_comps_scatter.png
31. chart_31_peer_multiples_comparison.png
32. chart_32_valuation_football_field.png ⭐ 必須
33. chart_33_price_target_scenarios.png
34. chart_34_historical_valuation_multiples.png
35. *作成された場合はオプションのチャート用に予約*

**10 個のオプションのチャート ファイル (合計 26 ～ 35 個):**
- chart_19 ～ chart_27、chart_35 (作成されている場合)

**チャート インデックス** (1 つのテキスト ファイル):
- chart_index.txt (説明とカテゴリを含むすべてのグラフのリスト)

**すべてのチャート ファイルは次のとおりである必要があります:**
- 300 DPI 解像度 (印刷品質)
- 幅 6 ～ 10 インチ (標準の Word 埋め込みサイズ)
- 白背景（プロフェッショナルな外観）
- PNG 形式 (ロスレス品質)
- Wordにすぐに埋め込める準備ができています

**最終ステップ: すべてのチャートをパッケージ化**

すべてのチャート ファイルとチャート インデックスを含む zip ファイルを作成します。

```
[Company]_Charts_[Date].zip
├── chart_01_stock_price_performance.png
├── chart_02_revenue_growth_trajectory.png
├── chart_03_revenue_by_product_stacked_area.png ⭐
├── chart_04_revenue_by_geography_stacked_bar.png ⭐
├── chart_05_company_overview.png
├── ... (all 25-35 chart files)
├── chart_28_dcf_sensitivity_heatmap.png ⭐
├── chart_32_valuation_football_field.png ⭐
├── chart_34_historical_valuation_multiples.png
└── chart_index.txt
```

**例**: `Tesla_Charts_2024-10-28.zip`

**これが重要な理由**: タスク 5 では、作成されたすべてのグラフ (25 ～ 35) がレポート全体に埋め込まれます。レポートには視覚的な密度 (200 ～ 300 ワードごとに 1 つのグラフ) が必要なので、すべてのグラフが特定の分析セクションまたは視覚的なストーリーテリングとページ密度のいずれかの目的を果たします。
- 25 ～ 35 のチャートがすべて存在することを確認します
- タスク 5 (レポートの組み立て) のグラフの抽出

---

<a id="next-steps"></a>
## 次のステップ

タスク 4 を完了すると、zip ファイルは次の目的で使用されます。
- **タスク 5 (レポートの組み立て)**: グラフを抽出し、すべてを最終的な DOCX レポートのドキュメント全体の適切な場所に埋め込みます。

4 つの必須チャートは、レポートの評価セクションと財務分析セクションで重要です。
