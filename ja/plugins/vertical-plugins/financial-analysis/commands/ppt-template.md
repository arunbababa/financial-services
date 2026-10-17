---
description: Create a reusable PPT template skill from a PowerPoint template file
argument-hint: "[path to .pptx or .potx file]"
allowed-tools: ["Read", "Write", "Bash", "Glob"]
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/financial-analysis/commands/ppt-template.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：PowerPoint テンプレート ファイルから再利用可能な PPT テンプレート スキルを作成する

<a id="ppt-template-creator-command"></a>
# PPT テンプレート作成コマンド

ユーザーが提供した PowerPoint テンプレートから自己完結型の PPT テンプレート スキルを作成します。

<a id="instructions"></a>
## 指示

1. **テンプレート ファイルが提供されていない場合は、テンプレート ファイルを要求します**:
   - 「PowerPoint テンプレート ファイル (.pptx または .potx) へのパスを入力してください。」
   - テンプレートには、使用するスライド レイアウトとブランドを含める必要があります

2. **ppt-template-creator スキルをロードします**:
   - `skill: "ppt-template-creator"` ツールを使用して完全なスキル手順をロードします
   - スキルのワークフローに従ってテンプレートを分析し、新しいスキルを生成します

3. **追加情報を収集**:
   - 会社名/テンプレート名（スキルの名前付け用）
   - 主な使用例 (提案資料、役員資料、クライアントのプレゼンテーションなど)

4. **スキル ワークフローを実行します**:
   - テンプレートの構造 (レイアウト、プレースホルダー、寸法) を分析します。
   - スキルディレクトリをassets/とSKILL.mdで生成
   - 検証するプレゼンテーションの例を作成する
   - スキルをパッケージ化する

5. **パッケージ化されたスキルをユーザーに提供**
