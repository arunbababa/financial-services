> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="claude-for-financial-services"></a>
# Claude for Financial Services（金融サービス向けClaude）

投資銀行業務、株式調査、プライベート エクイティ、ウェルス マネジメントなど、私たちが最も目にする金融サービス ワークフローのリファレンス エージェント、スキル、データ コネクタ。

ここにあるものはすべて **1 つのソースから 2 つの方法**で利用できます。[Claude Cowork](https://claude.com/product/cowork) プラグインとしてインストールするか、独自のワークフロー エンジンの背後で [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) を通じてデプロイします。同じシステム プロンプト、同じスキル - 実行場所を選択できます。

> [!IMPORTANT]
> このリポジトリは投資・法務・税務・会計に関する助言を構成しません。エージェントは、適格な専門家によるレビューに向けて、モデル、メモ、調査ノート、照合結果等のアナリスト成果物を下書きします。投資推奨、取引実行、リスクの引受け、元帳への記帳、顧客受入れの承認は行いません。すべての出力は人の確認・承認を待つ段階に置かれます。出力の検証と自社に適用される法令・規則の遵守は、利用者の責任です。

リポジトリの内容:

- **[エージェント](#agents)** — 一連のワークフローを担う名称付きエージェント（Pitch Agent、Market Researcher、GL Reconciler等）。Coworkプラグイン**と**、`/v1/agents`で配備する[Claude Managed Agentの雛形](managed-agent-cookbooks)の両方で提供します。
- **[業務別プラグイン](#vertical-plugins)** — 金融サービスの業務領域ごとに基礎となるスキル、スラッシュコマンド、データコネクタをまとめたものです。エージェント全体を使わず`/comps`、`/dcf`、`/earnings`とコネクタだけが必要なら、これらを単独で導入します。

<a id="agents"></a>
## エージェント

各エージェントには、実行するワークフローに応じた名前が付けられます。これらは出発点です。自分の業務に適合するものをインストールし、プロンプト、スキル、コネクタを会社のやり方に合わせて調整します。

各エージェント プラグインは**自己完結型**であり、使用するスキルがバンドルされているため、必要なのはエージェントをインストールすることだけです。

| 機能 | エージェント | 何をするのか |
|---|---|---|
| **顧客担当・助言業務** | **[Pitch Agent](plugins/agent-plugins/pitch-agent)** | 類似企業比較・類似取引事例・LBO → ブランド様式に沿った提案スライドまで一貫して作成 |
| | **[Meeting Prep Agent](plugins/agent-plugins/meeting-prep-agent)** | 毎回の顧客面談前の説明資料一式 |
| **調査・モデリング** | **[Market Researcher](plugins/agent-plugins/market-researcher)** | 業種・テーマ → 業界概要、競争環境、同業他社比較、アイデア候補リスト |
| | **[Earnings Reviewer](plugins/agent-plugins/earnings-reviewer)** | 決算説明会＋提出書類 → モデル更新 → ノートの下書き |
| | **[Model Builder](plugins/agent-plugins/model-builder)** | DCF、LBO、財務三表、類似企業比較を、開いているExcelで作成 |
| **ファンド事務管理・財務運営** | **[Valuation Reviewer](plugins/agent-plugins/valuation-reviewer)** | GP資料の取込み、評価テンプレートの実行、LP報告の承認前準備 |
| | **[GL Reconciler](plugins/agent-plugins/gl-reconciler)** | 照合差異の検出、根本原因の追跡、承認への回付 |
| | **[Month-End Closer](plugins/agent-plugins/month-end-closer)** | 発生計上、期首から期末までの増減整理、差異要因の説明 |
| | **[Statement Auditor](plugins/agent-plugins/statement-auditor)** | 配布前のLP向け明細書の点検・照合 |
| **オペレーション・顧客受入れ** | **[KYC Screener](plugins/agent-plugins/kyc-screener)** | 顧客受入れ審査文書の解析、ルール判定、不足の指摘 |

管理対象エージェントの展開 (`agent.yaml`、リーフワーカー サブエージェント、ステアリング イベントの例、およびエージェントごとのセキュリティに関する注意事項) については、**[managed-agent-cookbooks/](managed-agent-cookbooks)** を参照してください。

<a id="repository-layout"></a>
## リポジトリのレイアウト

```
plugins/
  agent-plugins/               # Named agents — one self-contained plugin each
  vertical-plugins/            # Skill + command bundles by FSI vertical, plus MCP connectors
  partner-built/               # Partner-authored plugins (LSEG, S&P Global)
managed-agent-cookbooks/       # Claude Managed Agent cookbooks — one dir per agent
claude-for-msft-365-install/   # Admin tooling to provision the Claude Microsoft 365 add-in
scripts/                       # deploy-managed-agent.sh · check.py · validate.py · orchestrate.py · sync-agent-skills.py
```

<a id="getting-started"></a>
## はじめに

<a id="cowork"></a>
### コワーク

Cowork で、**設定 → プラグイン → プラグインの追加** を開き、次のいずれかを行います。

- **このリポジトリ URL** (`https://github.com/anthropics/financial-services`) を貼り付けて、マーケットプレイスのリストから必要なエージェントと業種を選択します。または
- **zip をアップロード** — `plugins/` の下の任意のディレクトリ (例: `plugins/agent-plugins/pitch-agent/`) を zip 形式で圧縮し、ドロップインします。

<a id="claude-code"></a>
### Claude Code

```bash
# Add the marketplace
claude plugin marketplace add anthropics/financial-services

# Core skills + connectors (install first)
claude plugin install financial-analysis@claude-for-financial-services

# Named agents — pick the ones you want
claude plugin install pitch-agent@claude-for-financial-services
claude plugin install gl-reconciler@claude-for-financial-services
claude plugin install market-researcher@claude-for-financial-services

# Vertical skill bundles
claude plugin install investment-banking@claude-for-financial-services
claude plugin install equity-research@claude-for-financial-services
```

インストールすると、エージェントが Cowork ディスパッチに表示され、関連するスキルが自動的に起動され、セッションでスラッシュ コマンド (`/comps`、`/dcf`、`/earnings`、`/ic-memo` など) が使用可能になります。

<a id="claude-managed-agents"></a>
### Claude Managed Agents

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh gl-reconciler
```

[`managed-agent-cookbooks/`](managed-agent-cookbooks) の各テンプレートは、対応するプラグインと同じシステム プロンプトとスキルを参照します。デプロイ スクリプトは、ファイル参照を解決し、スキルをアップロードし、リーフワーカー サブエージェントを作成し、オーケストレーターを `/v1/agents` に POST します。独自のオーケストレーション層を介してエージェント間で `handoff_request` イベントをルーティングするリファレンス イベント ループについては、[`scripts/orchestrate.py`](../scripts/orchestrate.py) を参照してください。

> **リサーチ プレビュー:** サブエージェント委任 (`callable_agents`) はプレビュー機能です。セキュリティとハンドオフのガイダンスについては、エージェントごとの README を参照してください。

<a id="how-it-fits-together"></a>
## 構成要素の関係

| | 内容 | 保存先 |
|---|---|---|
| **エージェント** | ワークフローをエンドツーエンドで所有する自己完結型プラグイン (システム プロンプトとそれが使用するスキル)。 Cowork と管理対象エージェント ラッパーは両方とも同じディレクトリを参照します。 | `plugins/agent-plugins/<slug>/` |
| **スキル** | Claudeが関連する作業で自動的に参照する分野の専門知識、規約、段階的な手順です。業務別プラグインに一度だけ記述し、各エージェントには必要なものの同期コピーを同梱します。 | `plugins/vertical-plugins/<vertical>/skills/`（原本）· `plugins/agent-plugins/<slug>/skills/`（同梱コピー） |
| **コマンド** | 明示的にトリガーするスラッシュ アクション (`/comps`、`/earnings`、`/ic-memo`)。 | `plugins/vertical-plugins/<vertical>/commands/` |
| **コネクタ** | [MCP サーバー](https://modelcontextprotocol.io/) クロードをデータ (端末、研究プラットフォーム、ドキュメント ストア) に接続します。 | `plugins/vertical-plugins/financial-analysis/.mcp.json` |
| **管理対象エージェント ラッパー** | `agent.yaml` + 深さ 1 のサブエージェント + ヘッドレス デプロイメントのステアリングの例。 | `managed-agent-cookbooks/<slug>/` |

すべてがファイルベースであり、マークダウンと JSON であり、ビルドステップはありません。

<a id="vertical-plugins"></a>
## 業務別プラグイン

**financial-analysis**から始めます。共通のモデリングスキルとすべてのデータコネクタを含みます。必要なワークフローに応じて業務別プラグインを追加してください。

| プラグイン | 追加されるもの |
|---|---|
| **[financial-analysis](plugins/vertical-plugins/financial-analysis)** *（中核）* | 類似企業比較、DCF、LBO、財務三表、スライド品質確認、Excel監査。全11データコネクタ。 |
| **[investment-banking](plugins/vertical-plugins/investment-banking)** | CIM、匿名案件概要資料、プロセス案内書、買い手候補リスト、M&Aモデル、案件追跡。 |
| **[equity-research](plugins/vertical-plugins/equity-research)** | 決算ノート、新規カバレッジ開始、モデル更新、投資仮説と株価を動かす契機の追跡。 |
| **[private-equity](plugins/vertical-plugins/private-equity)** | 案件発掘、初期選別、デューデリジェンスのチェックリスト、投資委員会メモ、投資先のモニタリング。 |
| **[fund-admin](plugins/vertical-plugins/fund-admin)** | GL照合、照合差異の追跡、発生計上、期首から期末までの増減整理、差異要因の説明、NAV突合。 |
| **[オペレーション](plugins/vertical-plugins/operations)** | KYC 文書の解析とルールグリッドの評価。 |
| **[claude-for-financial-advisors](../claude-for-financial-advisors)** | アドバイザー向けワークフロー：面談準備・フォロー、コンプライアンス事前確認、見込み顧客の受入れ、リバランス確認、オルタナティブ投資・相続等の概要資料。アドバイザーのCRM、ポートフォリオ、プランニング、相続・資産承継プラットフォームのライブデータに基づきます。 |
| **[lseg](plugins/partner-built/lseg)** *（パートナー）* | LSEGデータによる債券の相対価値、スワップカーブ、FXキャリー、オプションのボラティリティ、マクロ・金利の監視。 |
| **[sp-global](plugins/partner-built/spglobal)** *（パートナー）* | S&P Capital IQによる企業要点資料、決算プレビュー、資金調達ダイジェスト。 |

<a id="mcp-integrations"></a>
## MCP の統合

すべてのコネクタは中核の**financial-analysis**プラグインに集約され、他のプラグインから共有されます。

| プロバイダー | URL |
|---|---|
| [ダルーパ](https://www.daloopa.com/) | `https://mcp.daloopa.com/server/mcp` |
| [モーニングスター](https://www.morningstar.com/) | `https://mcp.morningstar.com/mcp` |
| [S&P グローバル](https://www.spglobal.com/) | `https://kfinance.kensho.com/integrations/mcp` |
| [ファクトセット](https://www.factset.com/) | `https://mcp.factset.com/mcp` |
| [ムーディーズ](https://www.moodys.com/) | `https://api.moodys.com/genai-ready-data/m1/mcp` |
| [MTニュースワイヤー](https://www.mtnewswires.com/) | `https://vast-mcp.blueskyapi.com/mtnewswires` |
| [アイエラ](https://www.aiera.com/) | `https://mcp-pub.aiera.com` |
| [LSEG](https://www.lseg.com/) | `https://api.analytics.lseg.com/lfa/mcp` |
| [ピッチブック](https://pitchbook.com/) | `https://premium.mcp.pitchbook.com/mcp` |
| [クロノグラフ](https://www.chronograph.pe/) | `https://ai.chronograph.pe/mcp` |
| [エグナイト](https://www.egnyte.com/) | `https://mcp-server.egnyte.com/mcp` |
| [ボックス](https://www.box.com/home) | `https://mcp.box.com` |

> MCP アクセスには、プロバイダーからのサブスクリプションまたは API キーが必要な場合があります。

<a id="claude-for-microsoft-365--install-tooling"></a>
## Claude for Microsoft 365 — 導入支援ツール

会社が Microsoft 365 アドインを介して Excel、PowerPoint、Word、Outlook 内で Claude を実行している場合、[`claude-for-msft-365-install/`](claude-for-msft-365-install) は、Anthropic の API ではなく **独自のクラウド** (Vertex AI、Bedrock、または内部 LLM ゲートウェイ) に対してクロードをプロビジョニングするための管理ツールです。

これは、カスタマイズされたアドイン マニフェストの生成、Azure 管理者の同意の付与、Microsoft Graph を介したユーザーごとのルーティング構成の書き込みを IT 管理者に指示する Claude Code プラグイン (Cowork プラグインではありません) です。以下を使用してインストールします。

```bash
claude plugin install claude-for-msft-365-install@claude-for-financial-services
/claude-for-msft-365-install:setup
```

これは、上記のエージェントや垂直プラグインとは別のものです。これは、アドインをテナントに展開するオンランプであり、その後、ここでのエージェントとスキルがその中で実行されるものになります。

<a id="making-it-yours"></a>
## 自分のものにする

これらは参照テンプレートです。会社の仕組みに合わせて調整すると、さらに良くなります。

- **コネクタを交換** — `.mcp.json` をデータ プロバイダーと内部システムに向けます。
- **自社の文脈を追加** — 用語、業務プロセス、書式の基準をスキルファイルに追加します。
- **テンプレートを持参してください** — `/ppt-template` がブランドの PowerPoint レイアウトをクロードに教えます。
- **エージェントのスコープを調整** — チームが実際にワークフローを実行する方法に合わせて `agents/<slug>.md` を編集します。
- **独自の追加** — ここで説明していないワークフローの構造をコピーします。

<a id="skill--command-reference"></a>
## スキル＆コマンドリファレンス

<details>
<summary><b>financial-analysis</b> — 中核モデリング、Excel、スライドの品質確認</summary>

| スキル | コマンド | 説明 |
|---|---|---|
| comps-analysis | `/comps` | 市場取引倍率を使う類似企業比較分析 |
| dcf-model | `/dcf` | WACCと感応度分析を含むDCF評価 |
| lbo-model | `/lbo` | レバレッジド・バイアウト・モデル |
| 3-statement-model | `/3-statement-model` | 財務三表モデルのテンプレートへ入力 |
| audit-xls | `/debug-model` | Excelモデルの監査：数式追跡、直接入力値の検出、貸借等の一致確認 |
| clean-data-xls | — | Excel の表形式データを正規化してクリーンアップする |
| deck-refresh | — | デッキ全体に埋め込まれたグラフ/表を再リンクして更新します |
| competitive-analysis | `/competitive-analysis` | 競争環境と市場での位置付け |
| ib-check-deck | — | プレゼンテーションの誤りと整合性の品質確認 |
| pptx-author | — | `.pptx` ファイルをヘッドレスで生成します (管理エージェント モード) |
| xlsx-author | — | `.xlsx` ファイルをヘッドレスで生成します (管理エージェント モード) |
| ppt-template-creator | `/ppt-template` | 再利用可能な PPT テンプレート スキルを作成する |
| skill-creator | — | 新しいスキルを作成するためのガイド |

</details>

<details>
<summary><b>investment-banking</b> — 案件資料と取引実行</summary>

| スキル | コマンド | 説明 |
|---|---|---|
| strip-profile | `/one-pager` | 提案資料向けの1ページ企業概要 |
| pitch-deck | — | 提案資料テンプレートにデータを入力する |
| datapack-builder | — | CIMと提出書類からデータ一式を作成 |
| cim-builder | `/cim` | 秘密保持対象の企業・案件説明資料（CIM）を起草 |
| teaser | `/teaser` | 匿名の 1 ページの会社紹介 |
| buyer-list | `/buyer-list` | 事業会社・金融スポンサー等の買い手候補群 |
| merger-model | `/merger-model` | M&AによるEPS増加／希薄化の分析 |
| process-letter | `/process-letter` | 入札説明書及び手続き上の対応 |
| deal-tracker | `/deal-tracker` | 現在の取引、マイルストーン、アクションアイテムを追跡します |

</details>

<details>
<summary><b>equity-research</b> — 調査担当業務とレポート発行</summary>

| スキル | コマンド | 説明 |
|---|---|---|
| earnings-analysis | `/earnings` | 決算後の四半期更新レポート |
| earnings-preview | `/earnings-preview` | 決算前のシナリオ分析と主要指標 |
| initiating-coverage | `/initiate` | 機関投資家向け水準の新規カバレッジ開始レポート |
| model-update | `/model-update` | 新しいデータで財務モデルを更新する |
| morning-note | `/morning-note` | 朝礼のメモとトレードのアイデア |
| sector-overview | `/sector` | 業界の状況とテーマ別レポート |
| thesis-tracker | `/thesis` | 投資仮説の維持・更新 |
| catalyst-calendar | `/catalysts` | 調査担当銘柄群について今後の株価変動の契機を追跡 |
| idea-generation | `/screen` | 銘柄スクリーニングと投資アイデアの発掘 |

</details>

<details>
<summary><b>private-equity</b> — 案件発掘から投資先の運営まで</summary>

| スキル | コマンド | 説明 |
|---|---|---|
| deal-sourcing | `/source` | 企業を発見し、CRMをチェックし、創業者へのアウトリーチの草案を作成する |
| deal-screening | `/screen-deal` | インバウンド CIM およびティーザーのクイック合格/不合格 |
| dd-checklist | `/dd-checklist` | 作業領域別のデューデリジェンスのチェックリスト |
| dd-meeting-prep | `/dd-prep` | 経営陣のプレゼンテーションと専門家との通話の準備をする |
| unit-economics | `/unit-economics` | ARRコホート、LTV/CAC、ネットリテンション、収益の質 |
| returns-analysis | `/returns` | IRR/MOICの感応度表 |
| ic-memo | `/ic-memo` | 投資委員会メモ草案 |
| portfolio-monitoring | `/portfolio` | 投資先企業のKPIと差異を追跡 |
| value-creation-plan | `/value-creation` | 買収完了後の100日計画とEBITDA増減要因の整理 |
| ai-readiness | `/ai-readiness` | 投資先企業のAI導入準備状況を評価 |

</details>

<a id="contributing"></a>
## 貢献する

ここにあるものはすべてマークダウンと YAML です。フォーク、編集、PR。新しいコンテンツの場合:

- 新しいスキル → `plugins/vertical-plugins/<vertical>/skills/` の下に追加し、`python3 scripts/sync-agent-skills.py` を実行して、それをバンドルするエージェントに伝播します。
- 新しいエージェント → `plugins/agent-plugins/<slug>/` (`agents/<slug>.md` + `skills/`) および一致する `managed-agent-cookbooks/<slug>/`。
- push前に`python3 scripts/check.py`を実行します。すべてのマニフェストとファイル間参照を検査し、同梱スキルが業務別の原本と異なれば失敗させます。

<a id="license"></a>
## ライセンス

[Apache ライセンス 2.0](../LICENSE)
