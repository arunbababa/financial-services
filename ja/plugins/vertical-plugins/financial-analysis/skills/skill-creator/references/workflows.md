> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/financial-analysis/skills/skill-creator/references/workflows.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="workflow-patterns"></a>
# ワークフローパターン

<a id="sequential-workflows"></a>
## 順次ワークフロー

複雑なタスクの場合は、操作を明確な連続したステップに分割します。クロードに SKILL.mdの冒頭近くでプロセス全体の概要を示すすると役立つことがよくあります。

```markdown
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

<a id="conditional-workflows"></a>
## 条件付きワークフロー

分岐ロジックを含むタスクの場合は、クロードに意思決定ポイントを案内します。

```markdown
1. Determine the modification type:
   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```