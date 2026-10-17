# plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../../plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py)

### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:2

原文：

```text

DCF Model Validation Script
Validates Excel DCF models for formula errors and common DCF mistakes

```

日本語：


DCF モデル検証スクリプト
Excel DCF モデルの数式エラーや一般的な DCF 間違いを検証します。


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:14

原文：

```text
Validates DCF models for errors and quality issues
```

日本語：

DCF モデルにエラーや品質の問題がないか検証します


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:20

原文：

```text
openpyxl not installed. Run: pip install openpyxl
```

日本語：

openpyxlがインストールされていません。実行: pip install openpyxl


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:26

原文：

```text
File not found: 
```

日本語：

ファイルが見つかりません:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:35

原文：

```text

        Run all validation checks

        Returns:
            Dict with validation results
        
```

日本語：


すべての検証チェックを実行する

戻り値:
検証結果を含む辞書


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:61

原文：

```text
Verify required sheets exist
```

日本語：

必要なシートが存在することを確認してください


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:67

原文：

```text
Recommended sheet missing: 
```

日本語：

推奨シートが欠落しています:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:69

原文：

```text
Found sheet: 
```

日本語：

見つかったシート: 


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:72

原文：

```text
Check for Excel formula errors in all sheets
```

日本語：

すべてのシートで Excel の数式エラーをチェックする


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:86

原文：

```text
Count formulas
```

日本語：

数式を数える


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:90

原文：

```text
Check for errors
```

日本語：

エラーを確認


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:100

原文：

```text
Add summary info
```

日本語：

概要情報を追加する


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:101

原文：

```text
Total formulas: 
```

日本語：

合計の式:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:103

原文：

```text
✓ No formula errors found
```

日本語：

✓ 数式エラーは見つかりませんでした


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:105

原文：

```text
Total formula errors: 
```

日本語：

合計数式エラー:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:110

原文：

```text
Validate DCF-specific logic and calculations
```

日本語：

DCF 固有のロジックと計算を検証する


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:116

原文：

```text
Critical check: Terminal growth must be less than WACC
```

日本語：

重要なチェック: 永久成長率は WACC 未満でなければなりません


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:123

原文：

```text
Search for terminal growth and WACC values
```

日本語：

永久成長率と WACC 値の検索


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:129

原文：

```text
Look for value in adjacent cells
```

日本語：

隣接するセルの値を探す


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:145

原文：

```text
) >= WACC (
```

日本語：

) >= WACC (


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:145

原文：

```text
). This creates infinite value and is mathematically invalid.
```

日本語：

）。これは無限の値を作成し、数学的に無効です。


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:145

原文：

```text
CRITICAL: Terminal growth (
```

日本語：

重大: 永久成長率 (


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:150

原文：

```text
) < WACC (
```

日本語：

) < WACC (


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:150

原文：

```text
✓ Terminal growth (
```

日本語：

✓ 永久成長率（


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:153

原文：

```text
Could not locate terminal growth and WACC values
```

日本語：

永久成長率と WACC の値が見つかりませんでした


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:156

原文：

```text
DCF sheet not found
```

日本語：

DCF シートが見つからない


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:158

原文：

```text
Could not validate terminal growth vs WACC: 
```

日本語：

永久成長率と WACC を検証できませんでした:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:161

原文：

```text
Check if WACC is in reasonable range
```

日本語：

WACC が妥当な範囲内にあるかどうかを確認する


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:179

原文：

```text
) is outside typical range (5%-20%). Verify calculation.
```

日本語：

) は通常の範囲（5%-20%）外です。計算を確認してください。


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:179

原文：

```text
WACC (
```

日本語：

WACC (


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:182

原文：

```text
) in reasonable range
```

日本語：

) は妥当な範囲内


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:182

原文：

```text
✓ WACC (
```

日本語：

✓ WACC (


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:184

原文：

```text
Could not locate WACC value
```

日本語：

WACC 値が見つかりませんでした


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:187

原文：

```text
Could not validate WACC range: 
```

日本語：

WACC 範囲を検証できませんでした:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:190

原文：

```text
Check if terminal value is reasonable proportion of enterprise value
```

日本語：

継続価値が企業価値の妥当な割合であるかどうかを確認する


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:218

原文：

```text
 of EV (typically should be 50-70%). Model may be over-reliant on terminal assumptions.
```

日本語：

EV の割合 (通常は 50 ～ 70% である必要があります)。モデルは継続価値算定の前提条件に過度に依存している可能性があります。


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:218

原文：

```text
Terminal value is 
```

日本語：

継続価値は 


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:223

原文：

```text
 of EV (typically should be 50-70%). Check if terminal assumptions are too conservative.
```

日本語：

EV の割合 (通常は 50 ～ 70% である必要があります)。継続価値算定の前提条件が保守的すぎるかどうかを確認します。


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:223

原文：

```text
Terminal value is 
```

日本語：

継続価値は 


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:227

原文：

```text
✓ Terminal value is 
```

日本語：

✓ 継続価値は 


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:229

原文：

```text
Could not locate terminal value and enterprise value
```

日本語：

継続価値と企業価値を見つけることができませんでした


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:232

原文：

```text
Could not validate terminal value proportion: 
```

日本語：

継続価値の比率を検証できませんでした:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:237

原文：

```text

    Validate a DCF model Excel file

    Args:
        excel_path: Path to Excel DCF model

    Returns:
        Dict with validation results
    
```

日本語：

DCF モデルの Excel ファイルを検証する。

引数:
- `excel_path`: Excel DCF モデルのパス

戻り値: 検証結果を含む辞書。


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:251

原文：

```text
Command-line interface
```

日本語：

コマンドラインインターフェース


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:253

原文：

```text
Usage: python validate_dcf.py <excel_file> [output.json]
```

日本語：

使用法: python validate_dcf.py <excel_file> [output.json]


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:254

原文：

```text

Validates DCF model for:
```

日本語：

DCF モデルの次の項目を検証する:


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:255

原文：

```text
  - Formula errors (#REF!, #DIV/0!, etc.)
```

日本語：

- 数式エラー (#REF!、#DIV/0! など)


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:256

原文：

```text
  - Terminal growth < WACC (critical)
```

日本語：

- 永久成長率 < WACC (重大)


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:257

原文：

```text
  - WACC in reasonable range (5-20%)
```

日本語：

- 妥当な範囲の WACC (5 ～ 20%)


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:258

原文：

```text
  - Terminal value proportion of EV (40-80%)
```

日本語：

  - EV に占める継続価値の割合（40-80%）


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:259

原文：

```text

Returns JSON with errors, warnings, and info
```

日本語：


エラー、警告、情報を含む JSON を返します


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:260

原文：

```text

Example: python validate_dcf.py model.xlsx
```

日本語：


例: python validate_dcf.py model.xlsx


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:261

原文：

```text
Example: python validate_dcf.py model.xlsx results.json
```

日本語：

例: python validate_dcf.py model.xlsx results.json


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:270

原文：

```text
Print results
```

日本語：

結果を表示


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:273

原文：

```text
Save to file if requested
```

日本語：

要求された場合はファイルに保存します


### plugins/agent-plugins/pitch-agent/skills/dcf-model/scripts/validate_dcf.py:278

原文：

```text
Exit with error code if validation failed
```

日本語：

検証が失敗した場合はエラー コードで終了します


