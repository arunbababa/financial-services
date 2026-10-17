> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../../plugins/agent-plugins/pitch-agent/skills/pitch-deck/reference/calculation-standards.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="calculation-verification-reference"></a>
# 計算検証リファレンス

このファイルには、テンプレートを設定する前にソース データ内の事前計算された値を検証するための式とガイドラインが提供されます。ソース データにはすでに計算された数値が含まれている必要があります。これらの式を使用して精度を確認してください。

<a id="contents"></a>
## 内容

- [鍵検証式](#key-verification-formulas)
- [コンセンサス方法論](#consensus-methodology)
- [丸めガイドライン](#rounding-guidelines)
- [検証チェックリスト](#verification-checklist)
- [調査すべき危険信号](#red-flags-to-investigate)

---

<a id="key-verification-formulas"></a>
## 主要な検証式

<a id="cagr-projection"></a>
### CAGR 予測

**式:**
```
Future Value = Present Value × (1 + CAGR)^n
```

**変数:**
- 現在価値: 現在/基準年の市場規模
- CAGR: 年間複合成長率 (小数として、例: 16.4% = 0.164)
- n: 基準年と目標年の間の年数

**検証例:**
```
Source claims: $22.1bn (2024) at 16.4% CAGR = $55.0bn (2030)

Verify: 22.1 × (1.164)^6 = 22.1 × 2.488 = 55.0 ✓
```

**n (年) の計算:** 基準年と目標年の間の年数をカウントします。例: 2024→2030 = 6 年、2025→2030 = 5 年。

<a id="valuation-multiples"></a>
### 評価倍率

**EV/収益:**
```
EV/Revenue Multiple = Enterprise Value ÷ Revenue
Implied EV = Revenue × Multiple
```

**EV/EBITDA:**
```
EV/EBITDA Multiple = Enterprise Value ÷ EBITDA
Implied EV = EBITDA × Multiple
```

**検証例:**
```
Source claims: $436m deal at 9.7x revenue multiple on $45m revenue

Verify: 436 ÷ 45 = 9.69 ≈ 9.7x ✓
```

<a id="market-share"></a>
### 市場シェア

**式:**
```
Market Share = (Segment Size ÷ Total Market Size) × 100
```

**検証例:**
```
Source claims: Online segment ($18bn) is 28% of total market ($65bn)

Verify: 18 ÷ 65 = 0.277 = 27.7% ≈ 28% ✓
```

<a id="growth-rate"></a>
### 成長率

**前年比:**
```
YoY Growth = (Current Year - Prior Year) ÷ Prior Year × 100
```

**エンドポイントからの CAGR:**
```
CAGR = (End Value ÷ Start Value)^(1/n) - 1
```

---

<a id="consensus-methodology"></a>
## コンセンサス方法論

ソース データに複数の推定値が含まれている場合は、コンセンサス計算を検証します。

<a id="size-consensus-range"></a>
### サイズのコンセンサス (範囲)

**方法:** すべてのソースにわたる完全な最小値と最大値の範囲

**例:**
```
Sources: $14.9bn, $18.3bn, $21.1bn, $21.2bn, $22.1bn
Consensus: $15-22bn (rounded to nearest $1bn)
```

<a id="cagr-consensus-central-cluster"></a>
### CAGR コンセンサス (中央クラスター)

**方法:** 外れ値 (最高値と最低値) を除外し、中央クラスター範囲を使用します。

**例:**
```
Sources: 10.6%, 16.4%, 17.2%, 19.0%, 22.7%
Exclude outliers: 10.6% (low), 22.7% (high)
Central cluster: 16.4%, 17.2%, 19.0%
Consensus: 16-19% or 16-17% (conservative)
```

<a id="projection-consensus"></a>
### 予測のコンセンサス

**方法:** コンセンサス CAGR をサイズ範囲の中間点に適用します

**例:**
```
Size range: $15-22bn → Midpoint: $18.5bn
CAGR consensus: 16-17%
At 16%: 18.5 × (1.16)^6 = $45.1bn
At 17%: 18.5 × (1.17)^6 = $47.5bn
Consensus projection: $45-48bn
```

---

<a id="rounding-guidelines"></a>
## 丸めのガイドライン

これらは **一般的な規則** であり、値の大きさとテンプレート スタイルに基づいて調整します。

| 値のタイプ | 一般的な丸め | 例 |
|------------|------------------|---------|
| 大きな市場規模（100億ドル以上） | 最も近い10億ドル単位 | 18.47 → 180億ドル |
| 市場規模が小さい（100億ドル未満） | 最も近い5億ドルまたは1億ドル単位 | 23億→25億ドル |
| サイズ範囲 | ソースの一致精度 | 14.9-22.1 → 150-220億ドル |
| CAGR | 整数の% または 0.5% | 16.4% → 16% または 16.5% |
| 市場シェア | 最も近い 5% またはソースと一致 | 27.7%→25%または30% |
| 収益 (百万ドル) | 小数点1 | 18.47 → $18.5m |
| 倍数 | 小数点1 | 9.688 → 9.7x |

**丸めの原則:**
- 丸めによって数値が大きく変わることはありません。値が小さい場合は、より細かい精度を使用します。
- 精度よりも一貫性が重要です。同様の数値では同じ丸めを使用します。
- 範囲を作成するときは、下限の場合は切り捨て、上限の場合は切り上げます。
- 要約統計量 (平均値、中央値) の場合、入力データと精度を合わせる

---

<a id="verification-checklist"></a>
## 検証チェックリスト

ソース データから計算された値を使用する前に、次のことを行ってください。

<a id="formula-verification"></a>
### 数式の検証
- [ ] 予測では正しい CAGR 式が使用されます: `PV × (1 + r)^n`
- [ ] 倍数はEV ÷ メトリックとして計算されます（逆転されません）。
- [ ] 成長率は分母に正しい基準年を使用する
- [ ] 該当する場合、割合の合計は約100%になる

<a id="input-verification"></a>
### 入力検証
- [ ] 基準年の数値はソース文書と一致します
- [ ] CAGR/成長率は記載されたソース手法と一致
- [ ] 期間 (n) が正しく計算されました
- [ ] 通貨と単位の一貫性 (10 億ドルと 100 万ドル)

<a id="output-verification"></a>
### 出力の検証
- [ ] 計算結果は情報源の記載数値と一致
- [ ] 不一致の場合は、方法論の違いを調査する
- [ ] 一貫して適用される丸め
- [ ] 結果は妥当なものです (桁違いの誤差はありません)

<a id="consensus-verification"></a>
### コンセンサス検証
- [ ] 範囲計算に含まれるすべてのソース
- [ ] 外れ値の除外方法を文書化
- [ ] 中間点の計算では正しい平均化が使用されます
- [ ] 範囲境界は実際の最小値/最大値または文書化されたサブセットを表します

---

<a id="red-flags-to-investigate"></a>
## 調査すべき危険信号

**予測の不一致:**
- 計算された予測はソースと 5% を超える差があります
- 考えられる原因: 基準年が異なる、CAGR が異なる、または端数処理が異なる

**評価倍率の不一致:**
- 計算された倍数がソースと異なります
- 考えられる原因: 指標の定義が異なる (LTM と NTM、収益と純収益)

**コンセンサスの不一致:**
- あなたのコンセンサスはソースのコンセンサスと異なります
- 考えられる原因: ソースが特定のデータ ポイントを除外している、外れ値の処理が異なる

**疑問がある場合:** 脚注内の矛盾に注意し、計算方法を示してください。
