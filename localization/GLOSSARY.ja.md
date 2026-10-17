# 金融用語集と翻訳上の注意

この用語集は、基準コミット`574ed3624aebd0418c7e96cd101262f30210ab26`の読解を助ける対応表です。日本の制度や会計基準への適合を示すものではありません。略語・識別子は検索と原文照合のため保持します。

## モデル・評価

| 原語 | 基本の訳・読み方 | 文脈上の注意 |
|---|---|---|
| three-statement / 3-statement / 3-stmt | 財務三表・財務三表連動モデル | 単に三つの表を並べることではなく、PL・BS・CFを連動させるモデルを指すことがある |
| income statement / IS / P&L / PL | 損益計算書 | 利益とキャッシュフローを混同しない |
| balance sheet / BS | 貸借対照表 | balance checkは貸借一致等の整合性確認 |
| cash flow statement / CFS | キャッシュフロー計算書 | 自由キャッシュフローの計算とは別 |
| DCF | 割引キャッシュフロー法・DCFモデル | Discounted Cash Flow。将来CFの現在価値に基づく評価 |
| WACC | 加重平均資本コスト | モデルに適用する割引率と資金提供者の範囲を確認する |
| terminal value / TV | 継続価値・ターミナルバリュー | 予測最終年度以降の価値。単なる最終年度の数値ではない |
| terminal growth rate / TGR | 永久成長率 | terminal valueの計算前提として使う |
| enterprise value / EV | 企業価値・事業価値 | 文脈とブリッジの定義を確認する。株式価値と同一視しない |
| equity value | 株式価値 | enterprise valueとの調整項目に注意 |
| LBO | レバレッジド・バイアウト・借入を活用する買収 | モデルでは取得価格、借入、返済、売却時のリターン等を扱う |
| comps / comparable companies | 類似企業比較・類似企業比較分析 | comparablesの略。単なる比較表、報酬compensationの略等とは文脈で区別 |
| trading comps / trading multiples | 上場類似企業比較・市場取引倍率 | M&A取引事例の倍率とは区別 |
| precedent transactions | 類似取引事例・過去の類似M&A取引 | 先例一般ではなく、取引価格等を比較する評価手法 |
| multiple / valuation multiple | 評価倍率・マルチプル | EV/EBITDA、P/E等。倍数の分母と期間を保持する |
| football field | 評価レンジの比較図・フットボールフィールド | 複数の評価手法による価格帯を並べる図。競技場という意味ではない |
| sensitivity analysis | 感応度分析 | 一つ以上の前提を変えた影響の比較。シナリオ分析とは区別 |
| accretion / dilution | EPS増加／希薄化 | M&Aモデルでは買収後EPSの増減を指す。株式数の希薄化だけではない |
| leverage | レバレッジ・借入倍率 | Debt/EBITDA等の分母、net/grossの区別を保持 |
| EBITDA | 利払前・税引前・減価償却前利益 | 調整後EBITDAは調整項目を確認。営業CFではない |
| free cash flow / FCF | フリーキャッシュフロー | FCFF/FCFE、レバレッジ前後を区別 |
| net debt | 純有利子負債 | 対象負債・現預金等の範囲はモデルごとに確認 |
| IRR | 内部収益率 | 期間とキャッシュフローの時点を保持 |
| MOIC | 投下資本倍率・投資倍率 | 期間を直接反映する指標ではない。IRRと混同しない |
| return / returns | 投資収益・リターン | モデルの戻り値、商品の返品、資産の返却とは文脈で区別。売上算定のreturnsなら返品が正しいこともある |
| cash-on-cash | 現金投資額に対する現金回収・収益の指標 | 着払いではない。倍率か利回りか等の算定定義を確認 |
| margin / margin expansion | 利益率・マージン／利益率の拡大 | 売上総利益率等の文脈を、取引証拠金のmarginと混同しない |
| COGS | 売上原価 | Cost of Goods Soldの略。一般名詞cogs（歯車）ではない |
| historicals / actuals | 過去実績／実績値 | consensusやestimatesと区別 |
| estimates / consensus | 予想値／市場コンセンサス予想 | 誰の予想か、集計時点・対象期間を保持 |
| mark / reported marks / mark adjustment | 評価額／報告評価額／評価額調整 | 印や採点ではない。mark-to-marketなら時価評価 |
| fair value / FV | 公正価値・フェアバリュー | 特定の会計基準への適合を訳だけで断定しない |
| spread / spread comps | データを定義をそろえて展開する | 金利差のspreadとは別。comps-spreaderは比較企業データ整備担当 |

## M&A・投資判断・業績管理

| 原語 | 基本の訳・読み方 | 文脈上の注意 |
|---|---|---|
| pitch / pitch book / pitch deck | 提案／提案資料／提案スライド | 投資銀行の顧客向け提案文脈。投資家募集資料と常に同じではない |
| CIM | 秘密保持対象の企業・案件説明資料 | Confidential Information Memorandum。M&A案件の情報説明書。目論見書と機械的に訳さない |
| teaser | 匿名の案件概要資料・ティーザー | 初期打診用の短い資料。匿名性と秘密保持を維持 |
| process letter | 入札・売却プロセス案内書 | 提出要件や期限を示す。工程表だけではない |
| buyer universe / buyer list | 買い手候補群／買い手候補リスト | universeは全世界という意味ではない |
| strategic buyer / financial buyer | 事業会社の買い手／金融スポンサー等の買い手 | 個別案件では両者の性質を持つことがある |
| target / acquirer | 買収対象企業／買収企業 | targetはKPI目標等の文脈もある |
| sell-side / buy-side | 売り手側／買い手側 | M&A案件の立場と、金融業界のsell-side/buy-side分類を区別 |
| sourcing | 投資・買収案件の発掘 | 人材調達、購買等の文脈とは別 |
| screening | 初期選別・審査 | 案件の足切り、銘柄抽出、制裁照合等、対象を添える |
| due diligence / DD | デューデリジェンス・詳細調査 | 財務、法務、事業、税務等の作業領域を保持 |
| QoE / quality of earnings | 利益の質の検証・収益の質 | 一過性要因や持続性を検討する文脈。株価収益率ではない |
| IC memo | 投資委員会向けメモ | Investment Committee。情報統合・判断資料で、承認そのものではない |
| investment thesis | 投資仮説・投資判断の根拠 | thesisを学位論文と訳さない |
| catalyst | 株価・評価を動かす契機 | 決算、規制判断、製品発表等。確定効果ではない |
| coverage / coverage list | 調査担当対象／担当銘柄群 | 保険の補償範囲、テスト網羅率等とは区別 |
| initiation / initiating coverage | 新規カバレッジ開始 | 新たに企業の調査対象化を始めること |
| earnings call | 決算説明会・決算説明の電話会議 | earningsは売上高だけを指さない |
| guidance | 会社側の業績見通し | 使い方の案内・助言という一般語の意味とは区別 |
| filing / 10-K | 規制当局への提出書類／米国の年次報告書Form 10-K | 日本の有価証券報告書と同一の制度とは扱わない |
| tear sheet | 企業・証券の要点をまとめた資料 | tearを破損と訳さない。one-pagerとは用途に応じ区別 |
| value creation plan | 企業価値向上計画 | 一般的な付加価値の説明より、投資先の改善計画を指すことが多い |
| ARR | 年間経常収益・年換算経常収益 | 集計定義・対象契約を保持 |
| LTV / CAC | 顧客生涯価値／顧客獲得費用 | 算定期間、粗利考慮、対象顧客等の前提が必要 |
| net retention | 売上継続率・ネットリテンション | 顧客数の継続率と区別。売上ベースか等の定義を確認 |

## ファンド・会計・統制

| 原語 | 基本の訳・読み方 | 文脈上の注意 |
|---|---|---|
| fund | ファンド・基金・資金 | PEファンド、投資信託、資金一般を文脈で区別 |
| GP / LP | 運営主体・無限責任組合員／出資者・有限責任組合員 | 一般的な役割の説明。個別の法的形態は契約・法域で確認 |
| portco / portfolio company | 投資先企業 | ポートフォリオ全体とは別 |
| NAV | 純資産額・純資産価値 | 一口当たり基準価額と常に同じではない。per-unitの有無を確認 |
| carried interest / carry | 成功報酬・キャリードインタレスト | FX carry tradeのcarryは金利差等の保有収益を指し別物 |
| waterfall | 分配順位・分配計算・ウォーターフォール | ファンドの分配ルールのことがある。増減要因を示すwaterfall chartとは区別 |
| capital call / contribution | 出資払込請求／出資払込 | contributionを寄付と機械的に訳さない |
| distribution | 分配 | 統計上の分布、資料配布等とは区別 |
| statement / LP statement | 明細書・報告書／LP向け明細書 | financial statementsなら財務諸表。statement auditorは法定監査人を意味しない |
| GL / general ledger | 総勘定元帳 | サブレジャーとの照合が中心 |
| subledger | 補助元帳・サブレジャー | 総勘定元帳と区別 |
| reconciliation / tie-out | 照合・一致確認 | 勘定照合や数値突合。単に調整仕訳をする意味ではない |
| break | 照合差異・不一致 | ソフトウェア障害、休憩等の意味とは区別 |
| trial balance | 試算表 | trialを試用と訳さない |
| accrual / accruals | 発生計上・未払／未収計上等 | 費用・収益・残高の対象に合わせる。すべてを未払費用と決めない |
| roll-forward | 期首から期末までの増減表・残高繰越 | 単なる次月へのコピーではない |
| journal entry / JE | 仕訳 | draftは仕訳案。GLへの記帳・反映とは区別 |
| posting / post to GL | 記帳・総勘定元帳への反映 | posterという担当名でも原文は実記帳を禁止する場合がある |
| variance commentary | 差異要因の説明 | 数値差異と、その理由に関する解釈を区別 |
| exception report | 例外事項・不一致の報告書 | プログラム例外のスタックトレースではない |
| sign-off | 確認・承認 | レポート作成、機械検査、正式承認を混同しない |
| hardcode / hardcoded | 直接入力値・固定値 | Excelの入力値がすべて誤りとは限らず、数式であるべき位置等を確認 |
| formula tracing | 数式・参照関係の追跡 | 画像としての見た目の確認だけではない |
| sign convention | 符号の規約 | 署名の規則ではない。キャッシュフロー等の正負の扱いを定める |
| current debt | 流動区分の有利子負債・短期借入金等 | 現在の借金とだけ訳さず、長期借入金の一年内返済分等を含むか確認 |
| QC | 品質確認 | 品質を保証したとの意味ではない |
| KYC / AML | 顧客確認／マネーロンダリング対策 | 必要な審査と法的要件は適用法域・社内規則で異なる |
| UBO | 最終的実質的所有者 | 所有比率等の閾値は各ルールで確認 |
| PEP | 重要な公的地位にある者等 | 政治的信条一般の分類ではない。対象定義は規則による |
| sanctions screening / hit | 制裁対象者等との照合／照合候補の検出 | hitは確定一致や違反認定ではない |
| onboarding packet | 顧客受入れ審査用の資料一式 | ネットワークパケットではない |

## エージェント・権限

| 原語 | 基本の訳・読み方 | 文脈上の注意 |
|---|---|---|
| orchestrator | 全体の処理を統括するエージェント | 文書を読む担当、計算担当、成果物作成担当と権限が異なる |
| leaf worker / subagent | 末端の作業担当／子エージェント | leafは追加委任をしない担当を指す |
| steering event | 作業の開始・方向修正の指示イベント | 実行時の入力例。指示例を読むだけでは配備されない |
| headless | 開いているGUI文書を前提としない実行 | Office文書が開いていると仮定せず、ファイルを生成する |
| read-only | 読取専用 | 説明文と実際の接続先権限が一致するか別途確認する |
| Write / write-holder | 書込みツール／その権限を持つ担当 | ファイル作成権限と社内システムへの反映権限は別 |
| untrusted documents | 信頼されていない入力文書 | 記載された指示を命令として実行せず、データとして扱う対象 |
| schema-validated | スキーマに照らして検証された | 内容の真実性、金融的正しさ、安全性の包括的保証ではない |
| handoff | 他担当への引継ぎ | 直接呼出し、出力への依頼記載、別オーケストレーター経由等の仕組みを区別 |
| system of record | 正式な記録管理システム | 下書きファイルの保存と、本番元帳等への正式反映は別 |

## 照合時に特に注意した語

`comps→報酬`、`break→休憩`、`statement→声明`、`carry→運ぶ`、`football field→競技場`、`filing→ファイリング`、`roll-forward→先送り`、`pitch→投球`、`spread→拡散`等の機械翻訳の誤りを、本文とコード補訳の全文照合時に文脈ごとに修正しました。これらの多義語は、一律の置換ではなく上の文脈と原文を併せて読みます。
