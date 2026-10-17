---
name: nav-tieout
description: Tie an LP statement to the fund's NAV pack — recompute the LP's capital account from the NAV components and flag any line that doesn't agree. Use before LP statements are distributed.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/statement-auditor/skills/nav-tieout/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：LP向け明細書をファンドのNAV資料と照合する。NAVの構成項目からLPの資本勘定を再計算し、一致しない行を示す。LP向け明細書の配布前に使用する。

<a id="nav-tie-out"></a>
# NAVとの突合

作成されたLP向け明細書と対象期間のNAV資料（nav MCPから取得）を受け取り、LPの資本勘定を独立に再計算して、各行を比較する。

> **作成された明細書は検査対象である。** 正しい値の情報源はNAV資料である。

<a id="recompute-the-lp-capital-account"></a>
## LPの資本勘定を再計算する

```
Beginning capital (prior statement ending)
  + Contributions (capital calls paid this period)
  − Distributions (cash + in-kind)
  + Allocated net income / (loss)
      = LP% × (realized + unrealized P&L − management fee − fund expenses)
  − Carried interest allocation (if crystallized this period)
Ending capital
```

各入力値はNAV資料から取得する。LPの出資約束割合、ファンド全体の損益構成項目、報酬と費用の合計、分配ウォーターフォールの出力を使用する。

<a id="compare"></a>
## 比較する

明細書の各行を再計算値と比較する。許容差は`0.01`。不一致ごとに、原因となる入力値を記録する。例：「配賦損益が異なる。明細書は持分比率12.40%を用いているが、NAV資料では第1四半期の譲渡後の比率が12.38%となっている」。

<a id="additional-checks"></a>
## 追加の確認

- この明細書の期末資本が、翌期の草案の期首資本と一致するか。翌期草案がある場合に確認する。
- 全LPの期末資本の合計が、丸めの範囲内でファンドNAVと一致するか。
- 出資約束額、未払込の出資約束額、再請求可能な分配額が、出資約束管理台帳と一致するか。

<a id="output"></a>
## 出力

各行のpass/fail、明細書の値と並べた再計算値、指摘一覧を出力する。明細書は編集しない。配布担当者が、レビュー後に指摘へ対応する。
