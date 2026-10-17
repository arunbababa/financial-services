---
name: break-trace
description: Root-cause a reconciliation break to its source transaction or posting — follow the audit trail from the break row back to the originating entry on each side and state what differs and why. Use after gl-recon has classified a break.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/gl-reconciler/skills/break-trace/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：照合差異の根本原因を、元の取引または記帳までさかのぼって特定する。差異の行から双方の元の記録へ監査証跡をたどり、何がなぜ異なるのかを明示する。gl-reconで差異を分類した後に使用する。

<a id="root-cause-a-break"></a>
# 照合差異の根本原因を特定する

1件の差異行（キー、GLの値、補助元帳の値、分類、推定原因）を受け取り、発生源まで追跡して根本原因を記述する。

<a id="trace-path"></a>
## 追跡する経路

1. **GL側を取得する** — internal-gl MCPを使い、この総勘定元帳（GL）の明細を生んだ仕訳または記帳を取得する。取得項目は仕訳ID、記帳日、元システム、バッチID、作成者。
2. **補助元帳側を取得する** — subledger MCPを使い、対応する取引を取得する。取得項目は取引ID、約定日・決済日、取引相手、元のデータフィード、使用した為替レート。
3. **属性の差を比較する** — 記帳日、為替レートとその日付、勘定科目へのマッピング、数量の符号、金額の符号を並べる。通常、異なる属性が原因となる。

<a id="cause--statement"></a>
## 原因から説明文へ

根本原因を **「〈どちらの側が〉〈何をしたか〉。その理由は〈理由〉である」** という1文で書く。例：

- 「GLは決済日（T+2）に、補助元帳は約定日に記帳した。時点差による照合差異であり、2026-05-07に解消する見込み。」
- 「補助元帳はWM/Rの午後4時レートを、GLはBloombergの終値を使用した。基準通貨額に対して12 bpsの為替差異がある。」
- 「銘柄ABC123はマッピング表ではGL勘定11420に対応するが、補助元帳は11410へ連携した。マッピング差異として参照データ担当へ起票する。」
- 「補助元帳が同じ取引を2回記帳した。取引ID 88412と88419が重複している。重複記帳のため88419を除外する。」

<a id="output"></a>
## 出力

追跡した差異ごとに、次の形式で返す。

```json
{
  "key": "...",
  "root_cause": "one sentence as above",
  "owner": "ops | reference-data | accounting | upstream-system",
  "expected_clear_date": "YYYY-MM-DD or null",
  "action": "monitor | adjust | raise-ticket | suppress"
}
```

調整仕訳を書き込むのはresolverだけである。このスキルは診断を行い、記帳は行わない。
