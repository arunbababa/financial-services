# plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../../plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py)

### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:2

原文：

```text

Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location

```

日本語：

スキル初期化ツール - テンプレートから新しいスキルを作成

使用法:
    init_skill.py <skill-name> --path <path>

例:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:18

原文：

```text
---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

**1. Workflow-Based** (best for sequential processes)
- Works well when there are clear step-by-step procedures
- Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...

**3. Reference/Guidelines** (best for standards or specifications)
- Works well for brand guidelines, coding standards, or requirements
- Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...

**4. Capabilities-Based** (best for integrated systems)
- Works well when the skill provides multiple interrelated features
- Example: Product Management with "Core Capabilities" → numbered capability list
- Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...

Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex operations).

Delete this entire "Structuring This Skill" section when done - it's just guidance.]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. See examples in existing skills:
- Code samples for technical skills
- Decision trees for complex workflows
- Concrete examples with realistic user requests
- References to scripts/templates/references as needed]

## Resources

This skill includes example resource directories that demonstrate how to organize different types of bundled resources:

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.

```

日本語：

---
name: {skill_name}
description: [TODO: スキルが何を行うのか、いつ使用するのかについての完全かつ有益な説明。このスキルを使用するタイミング (特定のシナリオ、ファイル タイプ、またはスキルをトリガーするタスク) を含めます。]
---

# {skill_title}

## 概要

[TODO: このスキルで何が可能になるかを説明する 1 ～ 2 文]

## このスキルの構造化

[TODO: このスキルの目的に最も適した構造を選択してください。よくあるパターン:

**1.ワークフローベース** (順次プロセスに最適)
- 明確な段階的な手順がある場合にうまく機能します
- 例：「ワークフローデシジョンツリー」→「閲覧」→「作成」→「編集」のDOCXスキル
- 構造: ## 概要 → ## ワークフロー デシジョン ツリー → ## ステップ 1 → ## ステップ 2...

**2.タスクベース** (ツールコレクションに最適)
- スキルがさまざまな操作/機能を提供する場合にうまく機能します
- 例：「クイックスタート」→「PDFの結合」→「PDFの分割」→「テキストの抽出」によるPDFスキル
- 構造: ## 概要 → ## クイック スタート → ## タスク カテゴリ 1 → ## タスク カテゴリ 2...

**3.参考/ガイドライン** (標準または仕様に最適)
- ブランドのガイドライン、コーディング標準、または要件に適しています。
- 例：「ブランドガイドライン」→「カラー」→「タイポグラフィ」→「特徴」によるブランドスタイリング
- 構成: ## 概要 → ## ガイドライン → ## 仕様 → ## 使用法...

**4.機能ベース** (統合システムに最適)
- スキルが相互に関連する複数の機能を提供する場合にうまく機能します
- 例: 「コア機能」による製品管理 → 番号付き機能リスト
- 構造: ## 概要 → ## コア機能 → ### 1. 機能 → ### 2. 機能...

必要に応じてパターンを組み合わせたり、組み合わせたりすることができます。ほとんどのスキルはパターンを組み合わせています (例: タスクベースから始めて、複雑な操作のワークフローを追加します)。

完了したら、この「このスキルの構造化」セクション全体を削除してください。これは単なるガイダンスです。]

## [TODO: 選択した構造に基づいて最初のメイン セクションに置き換えます]

[TODO: ここにコンテンツを追加します。既存のスキルの例を参照してください。
- 技術スキルのためのコードサンプル
- 複雑なワークフローのためのデシジョン ツリー
- 現実的なユーザーの要望を反映した具体例
- 必要に応じて、スクリプト/テンプレート/リファレンスへの参照]

## リソース

このスキルには、さまざまな種類のバンドルされたリソースを整理する方法を示すサンプル リソース ディレクトリが含まれています。

### scripts/
特定の操作を実行するために直接実行できる実行可能コード (Python/Bash など)。

**他のスキルの例:**
- PDF スキル: `fill_fillable_fields.py`、`extract_form_field_info.py` - PDF 操作用ユーティリティ
- DOCX スキル: `document.py`、`utilities.py` - ドキュメント処理用の Python モジュール

**次の用途に適しています:** Python スクリプト、シェル スクリプト、または自動化、データ処理、または特定の操作を実行する実行可能コード。

**注意:** スクリプトはコンテキストにロードせずに実行できますが、パッチ適用や環境調整のためにクロードが読み取ることはできます。

### references/
クロードのプロセスと思考を知らせるためにコンテキストにロードされることを目的とした文書と参考資料。

**他のスキルの例:**
- 製品管理: `communication.md`、`context_building.md` - 詳細なワークフロー ガイド
- BigQuery: API リファレンス ドキュメントとクエリの例
- 財務: スキーマ文書、会社ポリシー

**以下に適しています:** 詳細なドキュメント、API リファレンス、データベース スキーマ、包括的なガイド、またはクロードが作業中に参照する必要がある詳細情報。

### assets/
ファイルはコンテキストにロードされることを意図したものではなく、クロードが生成する出力内で使用されます。

**他のスキルの例:**
- ブランド スタイリング: PowerPoint テンプレート ファイル (.pptx)、ロゴ ファイル
- フロントエンド ビルダー: HTML/React ボイラープレート プロジェクト ディレクトリ
- タイポグラフィ: フォント ファイル (.ttf、.woff2)

**次の用途に適しています:** テンプレート、定型コード、ドキュメント テンプレート、画像、アイコン、フォント、または最終出力でコピーまたは使用されるファイル。

---

**不要なディレクトリは削除できます。** すべてのスキルが 3 種類のリソースすべてを必要とするわけではありません。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:105

原文：

```text
#!/usr/bin/env python3
"""
Example helper script for {skill_name}

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.

Example real scripts from other skills:
- pdf/scripts/fill_fillable_fields.py - Fills PDF form fields
- pdf/scripts/convert_pdf_to_images.py - Converts PDF pages to images
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here
    # This could be data processing, file conversion, API calls, etc.

if __name__ == "__main__":
    main()

```

日本語：

`{skill_name}` 用のサンプルヘルパースクリプト。直接実行できるひな形です。実際の実装に置き換えるか、不要なら削除します。

他のスキルの実例:
- `pdf/scripts/fill_fillable_fields.py`: PDF フォームのフィールドに入力
- `pdf/scripts/convert_pdf_to_images.py`: PDF のページを画像に変換

コード構造は原文どおり `def main()`、`print("This is an example script for {skill_name}")`、`if __name__ == "__main__": main()` です。`print` は「これは {skill_name} のサンプルスクリプトです」と表示します。TODO コメントは、ここへ実際の処理（データ処理、ファイル変換、API 呼び出しなど）を追加することを示します。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:126

原文：

```text
# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Replace with actual reference content or delete if not needed.

Example real reference docs from other skills:
- product-management/references/communication.md - Comprehensive guide for status updates
- product-management/references/context_building.md - Deep-dive on gathering context
- bigquery/references/ - API references and query examples

## When Reference Docs Are Useful

Reference docs are ideal for:
- Comprehensive API documentation
- Detailed workflow guides
- Complex multi-step processes
- Information too lengthy for main SKILL.md
- Content that's only needed for specific use cases

## Structure Suggestions

### API Reference Example
- Overview
- Authentication
- Endpoints with examples
- Error codes
- Rate limits

### Workflow Guide Example
- Prerequisites
- Step-by-step instructions
- Common patterns
- Troubleshooting
- Best practices

```

日本語：

# {skill_title} のリファレンス ドキュメント

これは、詳細なリファレンス ドキュメントのプレースホルダーです。
実際の参照内容に置き換えるか、不要な場合は削除してください。

他のスキルからの実際の参照ドキュメントの例:
- product-management/references/communication.md - ステータス更新のための包括的なガイド
- product-management/references/context_building.md - コンテキストの収集に関する詳細
- bigquery/references/ - API リファレンスとクエリの例

## リファレンス ドキュメントが役立つ場合

リファレンス ドキュメントは次の場合に最適です。
- 包括的な API ドキュメント
- 詳細なワークフローガイド
- 複雑な複数ステップのプロセス
- メインの SKILL.md に収めるには長すぎる情報
- 特定の使用例にのみ必要なコンテンツ

## 構造に関する提案

### API リファレンスの例
- 概要
- 認証
- エンドポイントと例
- エラーコード
- レート制限

### ワークフロー ガイドの例
- 前提条件
- 段階的な説明
- よくあるパターン
- トラブルシューティング
- ベストプラクティス


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:162

原文：

```text
# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, images, fonts, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output Claude produces.

Example asset files from other skills:
- Brand guidelines: logo.png, slides_template.pptx
- Frontend builder: hello-world/ directory with HTML/React boilerplate
- Typography: custom-font.ttf, font-family.woff2
- Data: sample_data.csv, test_dataset.json

## Common Asset Types

- Templates: .pptx, .docx, boilerplate directories
- Images: .png, .jpg, .svg, .gif
- Fonts: .ttf, .otf, .woff, .woff2
- Boilerplate code: Project directories, starter files
- Icons: .ico, .svg
- Data files: .csv, .json, .xml, .yaml

Note: This is a text placeholder. Actual assets can be any file type.

```

日本語：

# アセット ファイルの例

このプレースホルダーは、アセット ファイルが保存される場所を表します。
実際のアセット ファイル (テンプレート、画像、フォントなど) に置き換えるか、不要な場合は削除します。

アセットファイルはコンテキストへの読み込み用ではなく、Claude が生成する出力に組み込んで使用するためのものです。

他のスキルのアセット ファイルの例:
- ブランドガイドライン: logo.png、slides_template.pptx
- フロントエンド ビルダー: HTML/React ボイラープレートを含む hello-world/ ディレクトリ
- タイポグラフィ:custom-font.ttf、font-family.woff2
- データ：sample_data.csv、test_dataset.json

## 一般的な資産タイプ

- テンプレート: .pptx、.docx、定型ディレクトリ
- 画像: .png、.jpg、.svg、.gif
- フォント: .ttf、.otf、.woff、.woff2
- 定型コード: プロジェクト ディレクトリ、スターター ファイル
- アイコン: .ico、.svg
- データ ファイル: .csv、.json、.xml、.yaml

注: これはテキストのプレースホルダーです。実際のアセットは任意のファイル タイプにすることができます。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:190

原文：

```text
Convert hyphenated skill name to Title Case for display.
```

日本語：

ハイフン区切りのスキル名を、表示用に各単語の先頭を大文字にした形式へ変換する。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:195

原文：

```text

    Initialize a new skill directory with template SKILL.md.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    
```

日本語：

テンプレート SKILL.md を使って新しいスキルディレクトリを初期化する。

引数:
- `skill_name`: スキル名
- `path`: スキルディレクトリを作成する場所

戻り値: 作成したスキルディレクトリのパス。エラーの場合は `None`。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:205

原文：

```text
Determine skill directory path
```

日本語：

スキルディレクトリのパスを決定する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:208

原文：

```text
Check if directory already exists
```

日本語：

ディレクトリがすでに存在するかどうかを確認する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:210

原文：

```text
❌ Error: Skill directory already exists: 
```

日本語：

❌ エラー: スキル ディレクトリはすでに存在します:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:213

原文：

```text
Create skill directory
```

日本語：

スキルディレクトリの作成


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:216

原文：

```text
✅ Created skill directory: 
```

日本語：

✅ 作成されたスキルディレクトリ:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:218

原文：

```text
❌ Error creating directory: 
```

日本語：

❌ ディレクトリ作成エラー:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:221

原文：

```text
Create SKILL.md from template
```

日本語：

テンプレートからSKILL.mdを作成


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:231

原文：

```text
✅ Created SKILL.md
```

日本語：

✅ SKILL.mdを作成しました


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:233

原文：

```text
❌ Error creating SKILL.md: 
```

日本語：

❌ SKILL.md の作成中にエラーが発生しました:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:236

原文：

```text
Create resource directories with example files
```

日本語：

サンプルファイルを含むリソースディレクトリを作成する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:238

原文：

```text
Create scripts/ directory with example script
```

日本語：

サンプルスクリプトを含む scripts/ ディレクトリを作成します


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:244

原文：

```text
✅ Created scripts/example.py
```

日本語：

✅ 作成されたscripts/example.py


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:246

原文：

```text
Create references/ directory with example reference doc
```

日本語：

サンプルリファレンスドキュメントを含むreferences/ディレクトリを作成します。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:251

原文：

```text
✅ Created references/api_reference.md
```

日本語：

✅ references/api_reference.md を作成しました


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:253

原文：

```text
Create assets/ directory with example asset placeholder
```

日本語：

サンプルのアセット用プレースホルダーを含む assets/ ディレクトリを作成


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:258

原文：

```text
✅ Created assets/example_asset.txt
```

日本語：

✅ assets/example_asset.txt を作成しました


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:260

原文：

```text
❌ Error creating resource directories: 
```

日本語：

❌ リソース ディレクトリの作成中にエラーが発生しました:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:263

原文：

```text
Print next steps
```

日本語：

次の手順を表示


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:264

原文：

```text

✅ Skill '
```

日本語：


✅ スキル '


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:264

原文：

```text
' initialized successfully at 
```

日本語：

' を次の場所で正常に初期化しました: 


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:265

原文：

```text

Next steps:
```

日本語：


次のステップ:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:266

原文：

```text
1. Edit SKILL.md to complete the TODO items and update the description
```

日本語：

1. SKILL.md を編集して TODO 項目を完成させ、説明を更新します


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:267

原文：

```text
2. Customize or delete the example files in scripts/, references/, and assets/
```

日本語：

2. scripts/、references/、assets/ 内のサンプル ファイルをカスタマイズまたは削除します。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:268

原文：

```text
3. Run the validator when ready to check the skill structure
```

日本語：

3. スキル構造を確認する準備ができたら、バリデーターを実行します。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:275

原文：

```text
Usage: init_skill.py <skill-name> --path <path>
```

日本語：

使用法: init_skill.py <skill-name> --path <path>


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:276

原文：

```text

Skill name requirements:
```

日本語：


スキル名の要件:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:277

原文：

```text
  - Hyphen-case identifier (e.g., 'data-analyzer')
```

日本語：

  - ハイフン区切りの識別子（例: 'data-analyzer'）


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:278

原文：

```text
  - Lowercase letters, digits, and hyphens only
```

日本語：

- 小文字、数字、ハイフンのみ


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:279

原文：

```text
  - Max 40 characters
```

日本語：

- 最大40文字


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:280

原文：

```text
  - Must match directory name exactly
```

日本語：

- ディレクトリ名は正確に一致する必要があります


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:282

原文：

```text
  init_skill.py my-new-skill --path skills/public
```

日本語：

  init_skill.py my-new-skill --path skills/public


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:283

原文：

```text
  init_skill.py my-api-helper --path skills/private
```

日本語：

  init_skill.py my-api-helper --path skills/private


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:284

原文：

```text
  init_skill.py custom-skill --path /custom/location
```

日本語：

  init_skill.py custom-skill --path /custom/location


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/init_skill.py:290

原文：

```text
🚀 Initializing skill: 
```

日本語：

🚀 スキルの初期化:


