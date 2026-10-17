> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../managed-agent-cookbooks/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="managed-agent-templates-for-financial-services"></a>
# 金融サービス用のマネージド エージェント テンプレート

このリポジトリの各エージェントは**二つの形**で提供されます。アナリストがインストールするCoworkプラグイン（リポジトリ直下の業務別ディレクトリを参照）と、プラットフォーム担当が自社のワークフローエンジンの背後に配備するClaude Managed Agentの雛形です。**同じエージェント、同じスキルで、実行環境を選べます。** 以下の各ディレクトリは配備マニフェストを持ち、対応プラグインの正本であるシステムプロンプトとスキルを参照するため、正本は一つです。

`../scripts/deploy-managed-agent.sh <slug>` を実行してスキルをアップロードし、リーフ ワーカーを作成し、解決された構成を使用して `POST /v1/agents` を実行します。各テンプレートには、[`steering-examples.json`](../../managed-agent-cookbooks/pitch-agent/steering-examples.json) と、セキュリティ層とハンドオフをカバーするエージェントごとの README が付属しています。

| エージェント | 業務別プラグイン | Coworkのタイル | CMAの指示イベント | 末端の作業担当 |
|---|---|---|---|---|
| [`pitch-agent`](pitch-agent) | investment-banking | 類似企業比較・類似取引事例・LBO → ブランド様式に沿った提案スライド | `Build pitch book: <target> / <acquirer>, thesis: <text>` | researcher · modeler · **deck-writer** |
| [`market-researcher`](market-researcher) | equity-research | 業種・テーマ → 概要、競争環境、同業他社比較、アイデア候補リスト | `Primer: <sector or theme>, angle: <text>` | sector-reader · comps-spreader · **note-writer** |
| [`earnings-reviewer`](earnings-reviewer) | equity-research | 決算説明会＋提出書類 → モデル更新 → ノートの下書き | `Process earnings: <ticker> <period>` | transcript-reader · model-updater · **note-writer** |
| [`meeting-prep-agent`](meeting-prep-agent) | wealth-management | 毎回の顧客面談前の説明資料一式 | `Briefing pack for <client-id>, meeting <event-id>` | profiler · news-reader · **pack-writer** |
| [`model-builder`](model-builder) | financial-analysis | DCF、LBO、財務三表、類似企業比較をファイルとして作成 | `Build <dcf\|lbo\|3-stmt> for <ticker>, assumptions: {...}` | data-puller · **builder** · auditor |
| [`gl-reconciler`](gl-reconciler) | financial-analysis | 照合差異の検出、根本原因の追跡、承認への回付 | `Reconcile GL vs subledger, trade date <D>, classes: <list>` | reader · critic · **resolver** |
| [`kyc-screener`](kyc-screener) | financial-analysis | 顧客受入れ審査文書の解析、ルール判定、不足の指摘 | `Screen onboarding packet <id>` | doc-reader · rules-engine · **escalator** |
| [`valuation-reviewer`](valuation-reviewer) | private-equity | GP資料の取込み、評価の実行、LP報告の承認前準備 | `Review portco valuations for fund <X> as of <date>` | package-reader · valuation-runner · **publisher** |
| [`month-end-closer`](month-end-closer) | financial-analysis | 発生計上、期首から期末までの増減整理、差異要因の説明 | `Close <entity> for period <YYYY-MM>` | ledger-reader · rollforward · **poster** |
| [`statement-auditor`](statement-auditor) | private-equity | 配布前のLP向け明細書の点検・照合 | `Tie out statement batch <id> against <fund> NAV pack` | statement-reader · reconciler · **flagger** |

**太字**の末端担当だけが`Write`を持ちます。

<a id="manifest-vs-api"></a>
## マニフェストと API

`agent.yaml`は実際の`POST /v1/agents`のフィールド名を使い、配備スクリプトが解決する便利な記法をいくつか加えています。

| マニフェストの記法 | 解決後の内容 |
|---|---|
| `system: {file: ../../plugins/agent-plugins/<slug>/agents/<slug>.md, append: "..."}` | `system: "<inlined contents + append>"` |
| `system: {text: "..."}` | `system: "<text>"` |
| `skills: [{from_plugin: ../../plugins/agent-plugins/<slug>}]` | そのディレクトリ内のすべての `skills/*` をアップロードします → `[{type: custom, skill_id: ...}, ...]` |
| `skills: [{path: ../../...}]` | `skills: [{type: custom, skill_id: <uploaded-id>}]` |
| `callable_agents: [{manifest: ./subagents/x.yaml}]` | `callable_agents: [{type: agent, id: <created-id>, version: latest}]` |

> **調査プレビュー:** `callable_agents` (マルチエージェント委任) は **1 つの委任レベル**をサポートします。オーケストレーターはワーカーを呼び出すことができます。ワーカーはそれ以上のサブエージェントを呼び出すことはできません。

<a id="cross-agent-handoffs"></a>
## エージェント間のハンドオフ

名称付きエージェント同士は直接呼び出しません。別エージェントが必要な場合は出力に`handoff_request`を含め、[`../scripts/orchestrate.py`](../../scripts/orchestrate.py)（またはTemporal/Airflow/Guidewireのイベントバス）が対象セッションへの新しい指示イベントとして振り分けます。参考スクリプトは固定の許可リストで対象を制限し、ペイロードをスキーマで検証します。脅威モデルは冒頭のコメントを参照してください。
