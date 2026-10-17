---
name: roll-forward
description: Build a roll-forward schedule for a balance-sheet account — beginning balance plus activity less reversals equals ending balance, with each component tied to GL. Use for month-end close packages and audit support.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/vertical-plugins/fund-admin/skills/roll-forward/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：貸借対照表勘定の残高増減表を作成する。期首残高に当期の増減を加え、戻入等を差し引いて期末残高へつなぎ、各構成項目をGLと突合する。月次決算資料や監査の裏付けに使用する。

<a id="roll-forward"></a>
# 残高増減表（ロールフォワード）

勘定（または勘定グループ）、事業体、期間を受け取り、期首から期末へ整合する残高増減表を作成する。

<a id="structure"></a>
## 構成

```
Beginning balance (per prior-period close)      X
  + Additions / new activity                    A
  + Accruals booked this period                 B
  − Reversals of prior accruals                (C)
  − Payments / settlements                     (D)
  ± Reclasses / adjustments                     E
  ± FX translation                              F
Ending balance (per GL at period end)           Y
```

<a id="tie-each-line"></a>
## 各行を照合する

- **期首** — 前期の決算資料、または前期末日のGL残高。
- **各増減行** — internal-gl MCPを使ったGLクエリ。勘定、日付範囲、仕訳元のフィルターを指定し、クエリを引用する。
- **期末** — 当期末日のGL残高。

表の合計は**必ず一致**しなければならない。式は`X + A + B − C − D + E + F = Y`。一致しない場合、その差は未説明項目である。差を明示し、帳尻合わせの値を入れない。

<a id="output"></a>
## 出力

残高増減表に「照合先」列を設け、すべての行についてGLクエリまたは文書を引用する。合計一致の確認結果（pass/fail）と、あれば未説明差額も出力する。
