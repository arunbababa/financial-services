# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/gl-reconciler/steering-examples.json](../../../managed-agent-cookbooks/gl-reconciler/steering-examples.json)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /0/event

**原文**

```text
Reconcile GL vs subledger, trade date 2026-04-30, classes: equities, fixed-income, derivatives
```

**日本語**

GLとサブレジャーを照合する。約定日2026-04-30、資産クラス：株式、債券、デリバティブ

## /0/description

**原文**

```text
Daily run across three asset classes
```

**日本語**

三つの資産クラスに対する日次処理

## /1/event

**原文**

```text
Reconcile GL vs subledger, trade date 2026-03-31, classes: all, threshold: 10000
```

**日本語**

GLとサブレジャーを照合する。約定日2026-03-31、資産クラス：すべて、差異の閾値：10000

## /1/description

**原文**

```text
Month-end run with explicit variance threshold
```

**日本語**

差異の閾値を明示した月末処理

## /2/event

**原文**

```text
Re-trace break: account 41200-EQ-US, trade date 2026-04-30
```

**日本語**

照合差異を再追跡する：勘定41200-EQ-US、約定日2026-04-30

## /2/description

**原文**

```text
Follow-up steering event to deep-dive a single break
```

**日本語**

単一の照合差異を掘り下げるための追加指示イベント
