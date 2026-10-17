# 決算分析4文書：原文対照レビュー記録

原文コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。2026-10-17に以下4原文と日本語訳を全文照合した。翻訳上の意味、数値の表し方、比較方向、否定、条件を確認したものであり、金融専門家による実データ・投資判断・法令の検証ではない。

- `plugins/vertical-plugins/equity-research/skills/earnings-analysis/SKILL.md`
- `plugins/vertical-plugins/equity-research/skills/earnings-analysis/references/best-practices.md`
- `plugins/vertical-plugins/equity-research/skills/earnings-analysis/references/report-structure.md`
- `plugins/vertical-plugins/equity-research/skills/earnings-analysis/references/workflow.md`

原文のコードフェンス（インデント付きも含む）、URL、インラインコード、frontmatter機械値を保持した。英文テンプレートの日本語説明はコード外に補訳した。原文ファイルは上記コミットとバイト一致。4文書で計23個の原文コードフェンスが日本語版と完全一致し、見出し用アンカーを保持している。詳細は `review-e.json` を参照。

## 原文側に残した不整合・注意点

- `workflow.md` の「Step 1c」が、最新データの必須検証と名称・表記の違いへの対応で重複している。番号を変更せず保持した。同じ段落群に現れる単独の「3. Alternative search methods」も原文どおり保持した。
- 決算発表日の新しさについて、「直近3か月以内」と「90日超は停止」が併記される。暦上の3か月と90日は常に同一ではない。翻訳では各箇所の条件を保持し、同一の基準へ統一していない。
- 書き起こしの日付について、`SKILL.md` と `workflow.md` の一部は「決算発表日と一致」を要求する一方、`workflow.md` の日付検証表では「±1日」を認めている。どちらも原文どおり訳した。
- `workflow.md` の最新検索例に「Tesla Q3 2024 earnings」があり、存在確認には使えても現在の最新四半期を保証する検索語ではない。2024年の日付や会計年度例も原文の例として保持し、現時点の事実に更新していない。
- レポート全体では表1～3点という指定があるが、`report-structure.md` にはそれを超える数の表テンプレート例が示される。どの例を採用するかの優先順位は補っていない。
- `workflow.md` の目標株価変更の目安は「5%超」と「5%未満」であり、ちょうど5%の場合の扱いは明記されない。原文の不等号を保持した。

公開資料は翻訳対象のデータとして扱い、資料内の実行指示、外部接続、スキル導入、上流スクリプト・MCPの実行は行っていない。担当訳4ファイルに対する既知の資格情報形式の文字列走査では該当なし。これは限定的な文字列検査であり、コード実行や本番環境のセキュリティ監査ではない。
