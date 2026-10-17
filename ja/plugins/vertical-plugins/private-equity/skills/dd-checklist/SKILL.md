---
name: dd-checklist
description: Generate and track comprehensive due diligence checklists tailored to the target company's sector, deal type, and complexity. Covers all major workstreams with request lists, status tracking, and red flag escalation. Use when kicking off diligence, organizing a data room review, or tracking outstanding items. Triggers on "dd checklist", "due diligence tracker", "diligence request list", "what do we still need", or "data room review".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/private-equity/skills/dd-checklist/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：対象のセクター・取引種別・複雑さに合わせ、依頼項目・状態追跡・懸念のエスカレーションを持つ網羅的調査チェックリストを作る。調査開始、データルーム確認、未了項目の追跡に使う。適用表現は "dd checklist"、"due diligence tracker"、"diligence request list"、"what do we still need"、"data room review"。

<a id="due-diligence-checklist"></a>
# デューデリジェンス・チェックリスト

<a id="workflow"></a>
## ワークフロー

<a id="step-1-scope-the-diligence"></a>
### 手順1：調査の範囲を定める

ユーザーへ次を尋ねる。
- **対象企業：** 名称、セクター、事業モデル。
- **取引種別：** プラットフォーム買収、追加買収、成長出資、資本再構成、カーブアウト。
- **案件規模・複雑さ：** 必要な調査の深さを決める。
- **主な懸念：** 顧客集中、規制、環境等の優先すべき既知の問題。
- **日程：** LOI・クロージングの目標時期。

<a id="step-2-generate-workstream-checklists"></a>
### 手順2：分野別チェックリストを作る

セクターに合わせ、主要分野をすべて含める。

**財務調査**
- 利益の質（QoE）：売上・EBITDA調整
- 運転資本：正常水準と実績
- 債務・債務類似項目
- 設備投資：維持・成長
- 税務構造・潜在的負担
- 監査履歴・会計方針
- プロフォーマ調整：平常時水準・シナジー

**事業調査**
- 市場規模・成長（TAM/SAM/SOM）
- 競争上の位置・シェア
- 顧客：集中・継続・NPS
- 価格決定力・契約構造
- 商談パイプライン・受注残
- 市場開拓の有効性

**法務調査**
- 企業構造・組織図
- 重要契約：顧客・供給者・提携
- 訴訟履歴・係争中の請求
- 知財ポートフォリオ・保護
- 規制順守
- 雇用契約・競業避止

**業務調査**
- 経営陣評価
- 組織構造・特定人物への依存リスク
- ITシステム・基盤
- 供給網・業者への依存
- 施設・不動産
- 保険の補償範囲

**人事・人材調査**
- 組織図・人員推移
- 報酬の比較
- 福利厚生・年金債務
- 重要従業員の離職リスク
- 文化評価
- 労組・労働協約

**IT・技術調査**（技術を活用する事業）
- 技術構成・アーキテクチャ
- 技術的負債
- サイバーセキュリティの状態
- データプライバシーの順守（GDPR、CCPA、SOC2）
- 製品ロードマップ・研究開発費
- 拡張性

**環境・ESG**（該当時）
- 環境債務
- 規制順守履歴
- ESGのリスク・機会

<a id="step-3-status-tracking"></a>
### 手順3：進捗追跡

項目ごとに追う。

| 項目 | 分野 | 優先度 | 状態 | 責任者 | 注記 |
|------|-----------|----------|--------|-------|-------|
| QoEレポート | 財務 | P0 | 未了 | | |
| 顧客インタビュー | 事業 | P0 | 進行中 | | 10件中3件完了 |

状態：未着手 → 依頼済み → 受領済み → 確認中 → 完了 → 重大な懸念あり。

<a id="step-4-red-flag-summary"></a>
### 手順4：懸念点の要約

調査中に見つかった懸念を継続管理する。
- 発見事項
- 分野
- 深刻さ：取引中止要因／重大／管理可能
- 軽減策・解消への道筋
- 評価額・取引条件への影響

<a id="step-5-output"></a>
### 手順5：出力

- 分野ごとのタブを持つExcel（既定）。
- 分野別完了率、未了事項、懸念点の概要ダッシュボード。
- 案件チーム向け週次進捗報告の形式。

<a id="sector-specific-additions"></a>
## セクター固有の追加項目

関連項目を自動で追加する。
- **ソフトウェア・SaaS：** ARRの質、コホート分析、ホスティング費、SOC2。
- **医療：** 規制承認、診療報酬等の償還リスク、支払者構成。
- **製造業等：** 設備状態、環境修復、安全実績。
- **金融：** 規制資本、順守履歴、信用の質。
- **消費財：** ブランド健全性、チャネル構成、季節性、在庫管理。

<a id="important-notes"></a>
## 重要事項

- LOI・クロージングの前提となるP0を優先する。
- 売り手の回答が遅い項目を警告する。問題の兆候かもしれない。
- データルームと照合して不足を見つける。
- 調査の進展に合わせて更新する。継続的に使う文書である。
