> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../plugins/vertical-plugins/investment-banking/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="investment-banking-plugin"></a>
# 投資銀行プラグイン

株式調査、評価、プレゼンテーション、取引資料用の投資銀行業務生産性ツール。

<a id="features"></a>
## 特長

- **取引資料** - CIM、ティーザー、プロセスレター、購入者リスト
- **プレゼンテーション** - ブランドのテンプレートを使用したストリッププロファイル、ピッチデッキ
- **トランザクション サポート** - 合併モデル、取引追跡、データ パック

<a id="installation"></a>
## インストール

```bash
claude --plugin-dir /path/to/investment-banking
```

または、プロジェクトの `.claude-plugin/` ディレクトリにコピーします。

<a id="commands"></a>
## コマンド

| コマンド | 説明 |
|---------|-------------|
| `/one-pager [company]` | ピッチブック用の 1 ページのストリップ プロファイル |
| `/cim [company]` | 機密情報覚書草案 |
| `/teaser [company]` | 匿名の 1 ページの会社紹介 |
| `/buyer-list [company]` | 戦略的かつ財務的なバイヤーユニバース |
| `/merger-model [deal]` | EPSの増加・希薄化を測るM&A分析 |
| `/process-letter [deal]` | 入札説明書及び手続き上の対応 |
| `/deal-tracker` | 現在の取引、マイルストーン、アクションアイテムを追跡します |

<a id="skills"></a>
## スキル

<a id="deal-materials"></a>
### 取引資料
| スキル | 説明 |
|-------|-------------|
| **cim-builder** | 機密情報覚書草案 |
| **teaser** | 匿名の 1 ページの会社紹介 |
| **process-letter** | 入札説明書及び手続き上の対応 |
| **buyer-list** | 戦略的かつ財務的なバイヤーユニバース |
| **datapack-builder** | CIM とファイリングからデータ パックを構築する |

<a id="presentations"></a>
### プレゼンテーション
| スキル | 説明 |
|-------|-------------|
| **strip-profile** | ピッチブック用の情報密度の高い企業プロフィール |
| **pitch-deck** | 提案資料テンプレートにデータを入力する |

<a id="transaction-support"></a>
### トランザクションサポート
| スキル | 説明 |
|-------|-------------|
| **merger-model** | EPSの増加・希薄化を測るM&A分析 |
| **deal-tracker** | 現在の取引、マイルストーン、アクションアイテムを追跡します |

<a id="example-workflows"></a>
## ワークフローの例

<a id="one-page-strip-profile"></a>
### 1 ページのストリップ プロファイル
```
/one-pager Target

# Generates:
# - Single-slide company profile using PPT template
# - 4 quadrants: Overview, Business, Financials, Ownership
# - Respects template margins and branding
```

<a id="cim-drafting"></a>
### CIM草案作成
```
/cim Target

# Generates:
# - Full CIM document with executive summary, business overview,
#   financial analysis, and market positioning
```

<a id="merger-model"></a>
### 合併モデル
```
/merger-model Acquirer acquiring Target

# Generates:
# - Accretion/dilution analysis
# - Sources and uses, pro forma financials
# - Sensitivity on purchase price and synergies
```
