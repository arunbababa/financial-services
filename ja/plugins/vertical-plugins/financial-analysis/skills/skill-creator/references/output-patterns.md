> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/financial-analysis/skills/skill-creator/references/output-patterns.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="output-patterns"></a>
# 出力パターン

スキルが一貫した高品質の出力を生成する必要がある場合は、これらのパターンを使用します。

<a id="template-pattern"></a>
## テンプレートパターン

出力形式のテンプレートを提供します。ニーズに合わせて厳密さのレベルを調整してください。

**厳密な要件の場合 (API 応答やデータ形式など):**

```markdown
## Report structure

ALWAYS use this exact template structure:

# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data
- Finding 3 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```

**柔軟なガイダンス用 (適応が役立つ場合):**

```markdown
## Report structure

Here is a sensible default format, but use your best judgment:

# [Analysis Title]

## Executive summary
[Overview]

## Key findings
[Adapt sections based on what you discover]

## Recommendations
[Tailor to the specific context]

Adjust sections as needed for the specific analysis type.
```

<a id="examples-pattern"></a>
## 例 パターン

出力の品質が例を見ることに依存するスキルの場合は、入力/出力のペアを提供します。

```markdown
## Commit message format

Generate commit messages following these examples:

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): JWT ベースの認証を実装します。

ログインエンドポイントとトークン検証ミドルウェアを追加する
```

**Example 2:**
Input: Fixed bug where dates displayed incorrectly in reports
Output:
```
fix(reports): タイムゾーン変換での日付書式を修正する

レポート生成全体にわたって一貫して UTC タイムスタンプを使用する
```

Follow this style: type(scope): brief description, then detailed explanation.
```

例は、クロードが説明だけよりも目的のスタイルと詳細レベルをより明確に理解するのに役立ちます。
