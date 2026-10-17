---
description: Build a DCF valuation model with comps-informed terminal multiples
argument-hint: "[company name or ticker]"
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../plugins/vertical-plugins/financial-analysis/commands/dcf.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：comps に基づいたターミナルマルチプルを使用して DCF 評価モデルを構築する

<a id="dcf-valuation-command"></a>
# DCF評価コマンド

比較可能な企業分析を使用して評価レンジの根拠を得る機関品質の DCF モデルを構築します。

<a id="workflow"></a>
## ワークフロー

<a id="step-1-gather-company-information"></a>
### ステップ 1: 会社情報を収集する

会社名またはティッカーが提供されている場合は、それを使用します。それ以外の場合は次のように尋ねてください。
- 「どの企業の価値を評価したいですか？」

<a id="step-2-run-comparable-company-analysis"></a>
### ステップ 2: 比較対象企業分析を実行する

**まず、コンプ分析スキル**をロードして、トレーディングコンプを構築します。

`skill: "comps-analysis"` を使用して次のことを行います。
1. 比較可能な上場企業を 4 ～ 6 社特定する
2. 事業指標を取得する（売上高、EBITDA、利益率、成長率）
3. プル評価倍率 (EV/収益、EV/EBITDA、PER)
4. 統計的概要の計算 (中央値、25/75 パーセンタイル)

**コンプからキャプチャする主な出力:**
- 中央値EV/EBITDAマルチプル → 継続価値のエグジット倍率の判断材料とする
- EV/収益倍率の中央値 → DCF 出力の健全性チェック
- 同業他社の成長率 → 収益予測のベンチマーク
- ピアマージン → マージン仮定のベンチマーク

<a id="step-3-build-dcf-model"></a>
### ステップ 3: DCF モデルの構築

**dcf-model スキル**をロードして評価を構築します。

`skill: "dcf-model"` を使用して次のことを行います。
1. 過去の財務データと市場データを収集する
2. 収益予測の構築 (ベア/ベース/ブルのケース)
3. モデル運営費とFCF
4. CAPM を使用して WACC を計算する
5. キャッシュフローを割り引いて継続価値を計算する
6. 株式価値と暗黙の株価への橋渡し

**類似企業比較をDCFの前提の判断材料にします:**

| コンプ出力 | DCF入力 |
|--------------|-----------|
| 同業他社のEV/EBITDA中央値 | 継続価値のエグジット倍率の範囲 |
| 同業他社の 25〜75パーセンタイルの EV/EBITDA | 感度分析範囲 |
| 同業他社の成長率中央値 | 収益想定のベンチマーク |
| 同業他社のEBITDAマージン中央値 | 最終年度の目標マージン |
| 同業他社のPER中央値 | DCF からの暗黙の PER をクロスチェックする |

<a id="step-4-cross-check-valuation"></a>
### ステップ 4: 評価のクロスチェック

DCF が完了したら、以下を検証します。
1. **DCF と競合他社の中央値からの **暗黙の EV/EBITDA**
   - DCF が 25 倍を示唆しているのに、同業他社が 12 倍で取引している場合は、その理由を調査してください
2. DCF とピア中央値からの **暗黙の P/E**
3. **EV の % としての継続価値** (50 ～ 70% である必要があります)
4. **評価に組み込まれた成長の暗示**と同業他社の成長率の比較

<a id="step-5-deliver-output"></a>
### ステップ 5: 出力を提供する

以下を提供します:
1. **Comps 分析スプレッドシート** (.xlsx) (ピア取引マルチプル付き)
2. **DCF モデル** (.xlsx) の内容:
   - ベア/ベース/ブルのシナリオ
   - 感度表 (WACC vs 永久成長率など)
   - 暗示的な上値/下値を含むバリュエーションの概要
3. **概要** の説明:
   - 主要な評価要因
   - 類似企業比較が分析にどのように影響したか
   - 注意すべきリスクと感応度

<a id="example-output-summary"></a>
## 出力例の概要

```
VALUATION SUMMARY: [Company] ([Ticker])

Comparable Companies Analysis:
- Peer Group: [List of 4-6 comps]
- Median EV/EBITDA: 12.5x (range: 10.2x - 15.8x)
- Median EV/Revenue: 3.2x (range: 2.1x - 4.5x)

DCF Valuation (Base Case):
- Implied Share Price: $XX.XX
- Current Price: $YY.YY
- Implied Upside: +XX%

Valuation Cross-Check:
- DCF Implied EV/EBITDA: 13.2x (vs peer median 12.5x)
- DCF Implied P/E: 22.4x (vs peer median 20.1x)
- Terminal Value: 62% of EV (within normal range)

Key Assumptions:
- Revenue CAGR: X% (vs peer median X%)
- Terminal EBITDA Margin: X% (vs peer median X%)
- WACC: X.X%
- Terminal Growth: X.X%
```
