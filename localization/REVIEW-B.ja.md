# B担当：意味照合の記録

> 統合時追記：以下の分担終了時点で未着手だった決算分析4原文は[E担当](REVIEW-E.ja.md)、移管した9原文は[D担当](REVIEW-D.ja.md)で全文照合を完了しました。全担当分の重複コピーへの同期も完了しています。個別JSONは分担時点の履歴、最終状態は[source-manifest.json](source-manifest.json)を参照してください。

## 範囲と状態

`review-b.json` に対象別の状態と訳文SHA-256を記録した。B担当58原文のうち54原文を全文読んで意味照合・再翻訳した。未着手は `earnings-analysis` の SKILL.md、references/best-practices.md、references/report-structure.md、references/workflow.md の4原文。`initiating-coverage/` 配下9原文はD担当へ移管済みで、Bは変更していない。

校閲した範囲は、LSEG全18文書、PE全10スキルと10コマンド、Equityの7スキルと9コマンド（earnings.mdを含む）。原文英語のYAML、コードフェンス、API識別子、原文見出しのアンカーは保持した。重複するagent-plugin側へはBからコピーしておらず、親が同期する。

これはAIによる原文意味照合であり、金融実務の独立した専門家検証、実市場データの照合、コネクタ実行を行った記録ではない。

## 主な誤訳の修正

- LSEGの vol を「出来高・体積」から「ボラティリティ」、Greeks を「ギリシャ人」から「グリークス」へ修正。
- CTDを「最も安い配送先」から「最割安受渡適格銘柄」、delivery basketを「受渡適格銘柄群」、repoを「リポジトリ」でなく「レポ金利」として翻訳。
- 3M・6Mを300万・600万と誤読していた期間表記、FY-1を2019年度とした年度誤訳、25dを25日としたデルタ誤訳、2s10sを秒とした誤読、bpを血圧とした誤訳を修正。
- rich/cheapを「お金持ち・豊富／安価」でなく「割高／割安」、principalを「校長」でなく「元本」、Mod. Durationを「修正デュレーション」へ修正。
- PEのreturnsを投資リターン、marginを文脈に応じた利益率、customer referenceを顧客への評判確認、management rolloverを持分再出資、thesisを投資判断の根拠として訳した。
- 指標閾値、比率・符号、期間、否定、情報不足時の質問、メール送信前の明示的承認、前提の検証条件を原文どおり保持した。

## 原文のまま保持した疑問点

- LSEG `bond-futures-basis` は手順で3Mの日次履歴を取得する一方、出力表で6M平均も求める。6Mデータ取得を翻訳者判断で補ってはいない。
- LSEG `option-vol-analysis` は対応期間との比較と述べつつ、表で90dの実現値を6M ATMへ対応させる。日数の数え方・期間対応を独自に修正していない。
- LSEG `fixed-income-portfolio` の手順2は時価加重DV01を求めるが、対応コマンドはDV01合計を求める。DV01の正規化・単位の定義を補っておらず、原文の相違を残した。
- LSEG `bond-relative-value` の原則は「総スプレッドをリスクフリー＋信用＋残差」と述べる一方、表では国債に対する上乗せであるGスプレッドを全体とする。利回りとスプレッドの用語上の不整合は黙って修正していない。
- PE `ai-readiness` の手順1は「売却12か月前ではAI投資回収の重要性は下がる」と述べる一方、後半は短い残存保有期間でLTM EBITDAへの効果を求める。前者を勝手に「上がる」へ反転せず原文どおり訳した。
- PE `deal-screening` は「3部構成」と述べつつ4項目を列挙する。判定の Pass / Further Diligence / Hard Pass は Pass の用語定義がないため、Pass を保持し、Hard Pass のみ明確な見送りとして訳した。
- PE `dd-checklist` はデータプライバシー項目に GDPR、CCPA、SOC2 を並べる。各制度の分類を翻訳者判断で改めてはいない。

これらは原文の修正提案ではなく、翻訳中に意味を補間・変更しなかった箇所の記録である。
