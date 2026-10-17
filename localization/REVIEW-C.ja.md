# 原文照合記録 C

基準原文：`574ed3624aebd0418c7e96cd101262f30210ab26`。この記録は、ルート文書、Microsoft 365 導入支援、Managed Agent の README、S&P Global パートナー文書の計35件を対象にしています。対象一覧と照合結果は [review-c.json](review-c.json) にあります。

## 確認した範囲

35件すべてについて、英語本文と日本語本文を順に照合し、欠落、誤訳、否定・必須条件、権限と送信の境界、金融用語、数値・日付の意味を確認して修正しました。英語の frontmatter は保持し、日本語の説明を別行で補っています。S&P の企業名・正式法人名、API名、識別子、数式を照合しています。

これは LLM による原文照合です。金融・会計・税務・法務・規制の専門家による校閲や、実データによる計算・実行検証を完了したという意味ではありません。外部 API、プラグイン、Office 設定、クラウド配備、上流スクリプトは実行していません。

原文と完全一致するコードブロック126件、frontmatter、見出し数、原文見出しのアンカー数を検査しました。インラインコードも改行・空白の正規化を除いて、原文の項目がすべて残ることを確認しています。原本のハッシュは変更されていません。コード内の英語コメント・図・例文の日本語補足は、別の [コード・図・コメントの補訳](CODE-AND-FENCE-NOTES.ja.md) で扱います。

JSON/YAML等82ファイルと個人設定サンプル1ファイルについても、付録と原本ハッシュを検査しました。自然言語203項目の日本語が対応する付録に存在し、サンプルは原文83行と行数が一致します。機械値だけの設定は自然言語の翻訳対象がない旨を明記しています。全件索引は [CONFIG-INDEX.ja.md](CONFIG-INDEX.ja.md) です。

## 主な修正

| 領域 | 修正した内容の例 |
|---|---|
| Office の権限 | allow/deny、既定の許可・拒否、実行環境、パス照合、大小文字を無視する正規化の意味を復元 |
| Office の操作 | ドライランと適用、ローカルのマニフェスト削除と全キャッシュ消去、チャット履歴保存、管理者同意、トークンの発行元を区別 |
| コードの保持 | インデントしたフェンスも原文と照合。verify の4ブロック、debug の7ブロックを含め、コード原本を復元・保持 |
| 決算プレビュー | 会計年度と暦年、直近4・8四半期、前年比に必要な前年期間、LTM/NTM、株価リターン、$1T＝1兆ドルを修正 |
| 企業要点資料 | tear sheet を「企業要点資料」、thesis を「投資仮説」、Corp Dev を「経営企画・M&A担当」、public/private を上場/非上場の文脈へ修正 |
| 企業比較・取引 | EVと株式価値、security の取引条件、削る順序、売上構成、取引関係、プレマネー・ポストマネーの意味を確認 |
| 資金調達 | raise を資金調達、seed companies を対象企業群の起点、entity resolution を企業の識別、subsidiary を子会社として復元 |
| 固有名詞 | Plaid、Adept AI、Convoy、正式法人名、Vertex/Bedrock/Foundry 等を原表記へ修正 |
| 未訳 | IB/M&A・営業資料に残っていた段落単位の英文を日本語化 |

修正過程は [review-c-changes.json](review-c-changes.json) に変更イベントの順で記録しています。同じ箇所を複数回直した中間状態も含むため、最終本文は `ja/` のファイルを参照してください。

## 原文にある不整合・解釈上の注意

原文の不整合は、翻訳で黙って仕様を変更せず、原文の記載と本注記を分けています。

- [Corp Dev テンプレート](../plugins/partner-built/spglobal/skills/tear-sheet/references/corp-dev.md) のヘッダー表は、`Enterprise Value` の説明に「上場企業は時価総額、非上場企業は直近の企業評価額」と書いています。EVと株式時価総額は通常異なる指標です。訳文にも元の対応を残し、評価額の実務上の定義を確定したものとはしていません。
- [決算プレビューのテンプレート](../plugins/partner-built/spglobal/skills/earnings-preview-beta/report-template.md) は `self-contained HTML` と説明する一方、Chart.js を CDN から読み込みます。単一ファイルとして配布できることと、完全オフラインで動くことを同一視できません。
- 同テンプレートの「Chart.js Implementation Notes」の図番号は、HTML 本体や [SKILL.md](../plugins/partner-built/spglobal/skills/earnings-preview-beta/SKILL.md) の図番号と一部一致しません。原文の見出し番号を保持しています。
- [企業要点資料のスキル](../plugins/partner-built/spglobal/skills/tear-sheet/SKILL.md) は、原データからの再計算による検証と、APIが返す計算済み指標を優先する方針を併記しています。また、セグメント構成比の合計検査と、内部取引消去等で合計が100%を超え得る扱いもあります。数値の定義・分母・検証手順は案件ごとの確認が必要です。
- [S&P Global の README](../plugins/partner-built/spglobal/README.md) のドキュメントリンクは URL のスキームを欠き、通常の Markdown では相対リンクとして扱われます。原文由来のリンク不備として残しています。
- [Managed Agent の一覧](../managed-agent-cookbooks/README.md) は `meeting-prep-agent` の分類を `wealth-management` と書きますが、この基準コミットの業務別プラグイン一覧に同名ディレクトリはありません。文書内の分類名と配布済み構成を同一視できません。
- Managed Agent のスキーマ検証や安全性に関する説明は、実行時の保証とは扱っていません。`deploy-managed-agent.sh` は `output_schema` を送信前に削除し、利用者側で検証処理の接続を確認する必要があります。詳細は [入口 README](../README.ja.md) の静的確認結果を参照してください。
- Office のドキュメントは、M365 の反映時間、OS・Office版ごとの挙動、特定の認証構成を前提にしています。これらは基準コミット時点の記載として翻訳し、現行サービスでの動作を検証していません。`scripts/check.py` には Git フック設定の副作用があります。
- S&P 文書には `/mnt/skills/public/`、`/home/claude`、`/mnt/user-data/outputs/`、`present_files` 等、Claude の実行環境を前提とする値があります。Codex 向けに移植した実行用プラグインではなく、読解用ミラーです。

不正な MCP JSON、接続先数の不一致、存在しないリンクなど、他の静的確認結果は [README.ja.md](../README.ja.md) と [翻訳方針](../TRANSLATION-NOTES.ja.md) にまとめています。
