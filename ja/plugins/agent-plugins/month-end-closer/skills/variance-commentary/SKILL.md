---
name: variance-commentary
description: Write flux commentary for every P&L and balance-sheet line over threshold — current vs prior period and vs budget, with the driver explained from underlying activity. Use for the month-end close package and management reporting.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/month-end-closer/skills/variance-commentary/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：閾値を超えるすべての損益計算書・貸借対照表項目について、前期比較と予算比較による増減の説明を書く。裏付けとなる取引・活動から変動要因を説明する。月次決算資料と経営報告に使用する。

<a id="variance-commentary"></a>
# 増減・予実差異の説明

同じ対象範囲の当期実績、前期実績、予算を受け取り、説明表を作成する。

<a id="threshold"></a>
## 閾値

次の**いずれか**に当てはまる項目を、説明対象とする。

- 差異の絶対値が会社の重要性基準以上である。指定値を使用する。既定値は「その項目の5%」と「固定の下限額」のうち大きい方。
- 「必ず説明する」一覧に含まれる項目である。売上、人件費、現金など。

<a id="for-each-flagged-line"></a>
## 説明対象の各項目について

| 列 | 内容 |
|---|---|
| **項目** | 勘定科目または表示項目名 |
| **当期／前期／予算** | 3つの値 |
| **前期差**と**予算差** | 金額と割合 |
| **変動要因** | 元の取引・活動から増減を説明する1文。数値の言い換えではない |

変動要因は「何が起きたか」ではなく「なぜか」を説明する。たとえば「5月のローンチ向けにGPU予約を追加したため、クラウド費用が$1.2M増加した」と書く。「クラウド費用が$1.2M（18%）増加した」だけではない。

<a id="sourcing-the-driver"></a>
## 変動要因の裏付けを得る

internal-gl MCPを使い、項目の背景にある活動を調べる。仕訳元の内訳、取引先構成、人数の増減、数量×単価などを見る。データから要因が明らかにならなければ、作り話で埋めず「変動要因不明 — 経理責任者の確認対象」と書く。

<a id="output"></a>
## 出力

説明表と、期間中の最大の変動項目をまとめた短い文章（3〜5文）を出力する。
