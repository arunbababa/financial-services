---
name: xlsx-author
description: Produce a .xlsx file on disk (headless) instead of driving a live Excel workbook — for managed-agent sessions with no open Office app.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/month-end-closer/skills/xlsx-author/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：Office アプリを開いていない管理エージェント セッションの場合は、ライブ Excel ワークブックを駆動する代わりに、ディスク上に .xlsx ファイル (ヘッドレス) を生成します。

<a id="xlsx-author"></a>
# xlsx-author

このスキルは、**ヘッドレス** (管理対象エージェント/CMA モード) を実行し、`mcp__office__excel_*` を介してライブ ワークブックを編集するのではなく、**ファイル アーティファクト**として Excel ワークブックを配信する必要がある場合に使用します。

<a id="output-contract"></a>
## 出力契約

- `./out/<name>.xlsx` に書き込みます。 `./out/` が存在しない場合は作成します。
- オーケストレーション層がそれを収集できるように、最終メッセージで相対パスを返します。

<a id="how-to-build-the-workbook"></a>
## ワークブックの作成方法

短い Python スクリプトを作成し、Bash で実行します。 `openpyxl` を使用します。

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active; ws.title = "Inputs"
ws["B2"] = "Revenue"; ws["C2"] = 1_250_000_000
ws["C2"].font = Font(color="0000FF")           # blue = hardcoded input
calc = wb.create_sheet("DCF")
calc["C5"] = "=Inputs!C2*(1+Inputs!C3)"        # black = formula
wb.save("./out/model.xlsx")
```

<a id="conventions-mirror-audit-xls"></a>
## 規則（以下に準拠： `audit-xls`)

- **青 / 黒 / 緑。** 青 = ハードコードされた入力、黒 = 数式、緑 = 別のシート/ファイルへのリンク。
- **計算セルへ数値を直接固定入力しない。** すべての計算セルは数式です。すべての入力はInputsタブに置きます。
- デックまたはメモから参照される任意の値の **名前付き範囲**。
- **残高チェック。** BSの貸借一致、CFと現金残高の一致などを照合し、TRUE/FALSEを示すChecksタブを含めます。
- **ファイルごとに 1 つのモデル。** 明示的に要求されない限り、既存のワークブックに追加しないでください。

<a id="when-not-to-use"></a>
## 使用しない場合

`mcp__office__excel_*` ツールが利用可能な場合 (Cowork プラグイン モード)、代わりにそれらを使用してください。これらのツールは、レビュー チェックポイントを使用してユーザーのライブ ワークブックを駆動します。このスキルは、ヘッドレス実行のファイル生成フォールバックです。
