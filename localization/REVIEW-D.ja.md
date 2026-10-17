# 原文照合レビュー D

原文コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`

対象は公開されている参考テンプレートの翻訳です。原文との意味の照合を行いました。実データ、現行法令、投資判断に関する専門検証や、原文コードの実行検証は行っていません。以下は原文内の不整合や確認が必要な点です。訳文で黙って修正していません。

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md

- タスク4の前提条件にタスク1を含む箇所とタスク2・3のみの箇所が混在
- 単一タスク制約とタスク1・2の並行実行可が併記
- タスク3分析の拡張子.mdと推奨フォルダ構成の.pdfが不一致
- 機関投資家向け品質・公開可能との原文表現は基準の記述であり成果物の実地検証ではない

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/assets/quality-checklist.md

- チェックリストの15以上のモデルタブとSKILL.mdの6必須タブに差異
- Calibri/Arial等の指定とSKILL.mdのTimes New Roman指定が不一致
- DOCXとXLS両方納品という記述とタスク5のDOCXのみ納品が不一致

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/assets/report-template.md

- 1ページ目のInvestment Update/Company Update指定は他文書のINITIATING COVERAGE指定と不一致
- 本文見出しのページ範囲が重複し、末尾チャート一覧の対応ページとも異なる
- 図キャプションを下に配置する指定は他文書の上配置指定と異なる
- 20-30+チャート指定に対し列挙は38件、一部節のチャート数表示と列挙数も異なる
- DOC/DOCXのスキル名表記が混在

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task1-company-research.md

- 8-12リスクという総数に対し4カテゴリの指定内訳合計は11-16件
- 経営幹部3-4名に対しCEO/CFOに2名追加という記述が併存
- 各節語数の上限合計と全体6,000-8,000語の目安に差異

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task2-financial-modeling.md

- 前提を各タブ内に記載する指定と別のAssumptionsタブへのリンク指定が混在
- Step1末尾に対応する見出しのない箇条書きと3/4番号が残存
- 6必須タブに加え履歴抽出用5タブの別ファイルを作る記述と単一成果物指定の関係が不明瞭
- 損益計算書ひな型ではD&AとEBITDA/EBITの配置に計算上の解釈余地あり。数式を補正していない

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task3-valuation.md

- 複数の数値例は相互に統一されていない（DCF感度表の基本値、comps価格等）
- シナリオ例の確率加重期待値$59は表示値の20/60/20%と42/59/82からの単純計算$60.2と異なる
- 類似取引例の企業価値から株式価値への変換と後段株価表の関係が不明瞭
- 原文のWACC/ターミナル比率等の一般的目安は専門検証済のルールではない

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task4-chart-generation.md

- chart34は必須一覧に含まれる一方、そのデータは任意とされる
- 必須4図のうち2図以外の追加バリュエーション図は5件だが見出しは6とする
- ファイルサイズ50KBによる300DPI推定は例示上の簡易確認で解像度の独立検証にはならない
- 図の番号を掲載順にする指定と固定chart番号との関係に解釈余地あり

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/task5-report-assembly.md

- 成果物末尾はDOCX+XLSX同梱だがSKILL.mdではDOCXのみ納品
- Historical_Financials.xlsxをタスク1出力とする箇所がタスク2手順と不一致
- 挿入例の複数chartファイル名・番号がタスク4の一覧と異なる
- 各節/フェーズの指定語数合計、全体10,000-15,000語、1ページ1図以上と25-35図などの数量条件が整合しない場合あり
- フォント指定がSKILL.mdのTimes New Romanと不一致
- 原文の公開可能/投資判断に十分との記述は品質目標であり独立検証済の保証ではない

## plugins/vertical-plugins/equity-research/skills/initiating-coverage/references/valuation-methodologies.md

- 翌年見通しとNTM（今後12か月）の表現が同一視されている
- 基本ケース$42-$46の中点と説明される目標株価$45は算術的中点$44と異なる
- WACC/成長率/プレミアム/倍率選択等の一般論は原文の目安として訳し、投資判断向けの専門検証はしていない

## 保持と安全性

- 担当9文書の原文を全件読み、対応する日本語文書と照合しました。
- 原文コード、frontmatterの機械値、URL、既存アンカーは保持しました。コード例・コマンドは実行していません。
- 新たな外部接続、インストール、コミット、pushは行っていません。
- 訳文に実在の資格情報を追加していません。機密情報・資格情報の検査は担当文書の静的確認です。
