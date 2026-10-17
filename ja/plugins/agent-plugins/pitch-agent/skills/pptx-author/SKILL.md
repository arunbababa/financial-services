---
name: pptx-author
description: Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sessions with no open Office app.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/pitch-agent/skills/pptx-author/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：Office アプリが開いていない管理エージェント セッションの場合、ライブ PowerPoint ドキュメントを駆動する代わりに、ディスク上に .pptx ファイル (ヘッドレス) を生成します。

<a id="pptx-author"></a>
# pptx-author

このスキルは、**ヘッドレス** (管理対象エージェント/CMA モード) を実行し、`mcp__office__powerpoint_*` を介してライブ ドキュメントを編集するのではなく、**ファイル アーティファクト**として PowerPoint デッキを配信する必要がある場合に使用します。

<a id="output-contract"></a>
## 出力契約

- `./out/<name>.pptx` に書き込みます。 `./out/` が存在しない場合は作成します。
- オーケストレーション層がそれを収集できるように、最終メッセージで相対パスを返します。

<a id="how-to-build-the-deck"></a>
## デッキの組み方

短い Python スクリプトを作成し、Bash で実行します。 `python-pptx` を使用します。

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation("./templates/firm-template.pptx")  # if a template is provided
# or: prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[5])    # title-only
slide.shapes.title.text = "Valuation Summary"
# ... add tables / charts / text boxes ...

prs.save("./out/pitch-<target>.pptx")
```

<a id="conventions-mirror-the-live-office-pitch-deck-skill"></a>
## 規約 (ライブ Office `pitch-deck` スキルを反映)

- **各スライドにつき 1 つのアイデア。** タイトルには要点が記載されています。本文でそれを裏付けます。
- **すべての数値はモデルをトレースします。** 数値が `./out/model.xlsx` からのものである場合は、シートとセルに脚注を付けます。
- **会社テンプレートが `./templates/` にマウントされている場合は、会社テンプレートを使用します。それ以外の場合はデフォルトのレイアウト。
- **チャート**: 忠実度が重要な場合は、ネイティブの pptx チャートよりもモデルからレンダリングされた PNG を埋め込むことを好みます。
- **外部送信はありません。** このスキルはファイルを書き込みます。電子メールを送信したりアップロードしたりすることはありません。

<a id="when-not-to-use"></a>
## 使用しない場合

`mcp__office__powerpoint_*` ツールが利用可能な場合 (Cowork プラグイン モード)、代わりにそれらを使用してください。これらのツールは、レビュー チェックポイントを使用してユーザーのライブ ドキュメントを駆動します。このスキルは、ヘッドレス実行のファイル生成フォールバックです。
