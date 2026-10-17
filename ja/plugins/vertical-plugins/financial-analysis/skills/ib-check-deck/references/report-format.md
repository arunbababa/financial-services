> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/vertical-plugins/financial-analysis/skills/ib-check-deck/references/report-format.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="deck-check-report-format"></a>
# デッキチェックレポートフォーマット

<a id="report-template"></a>
## レポートテンプレート

```markdown
# Deck Check Report: [Presentation Name]

## Summary
- Total issues: X
- Critical: X (number mismatches, factual errors)
- Important: X (narrative-data alignment, language)
- Minor: X (formatting)

## Critical Issues

### Number Consistency
1. **[Issue name]** (Slides X, Y)
   - Slide X: [value]
   - Slide Y: [value]
   - Action: [recommendation]

### Data-Narrative Alignment
1. **[Issue name]** (Slides X, Y)
   - Claim: "[quoted text]"
   - Data shows: [contradiction]
   - Action: [recommendation]

## Important Issues

### Language Polish
1. **[Issue type]** (Slide X)
   - Current: "[quoted text]"
   - Suggested: "[replacement]"

## Minor Issues

### Formatting
1. **[Issue type]** (Slide X)
   - [Description and fix]

## Final Checklist
- [ ] Numbers reconciled
- [ ] Narrative matches data
- [ ] Language meets IB standards
- [ ] Charts sourced
- [ ] Formatting consistent
```

<a id="issue-severity-classification"></a>
## 問題の重大度の分類

**重要** (クライアントに配信する前に修正する必要があります):
- スライド間の番号の不一致
- 計算ミス
- 事実の不正確さ (名前、役職、日付)
- 物語と矛盾するデータ

**重要** (修正する必要があります):
- カジュアル/カジュアルな言葉遣い
- 具体性のない曖昧な主張
- 用語の不一致
- チャートのソースがありません

**マイナー** (研磨アイテム):
- フォント/色の不一致
- 日付形式のバリエーション
- 間隔/配置の問題
- 孤立したテキスト
