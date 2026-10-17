# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/month-end-closer/steering-examples.json](../../../managed-agent-cookbooks/month-end-closer/steering-examples.json)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /0/event

**原文**

```text
Close entity US-OPCO for period 2026-04
```

**日本語**

主体US-OPCOの2026-04期の決算を行う

## /0/description

**原文**

```text
Standard month-end close
```

**日本語**

標準的な月次決算

## /1/event

**原文**

```text
Close entity UK-HOLDCO for period 2026-03, scope: accruals only
```

**日本語**

主体UK-HOLDCOの2026-03期の決算を行う。範囲：発生計上のみ

## /1/description

**原文**

```text
Partial close, accruals only
```

**日本語**

発生計上だけを対象にした部分的な決算

## /2/event

**原文**

```text
Re-draft variance commentary for entity US-OPCO 2026-04 after late JEs
```

**日本語**

遅れて計上された仕訳を反映した後、主体US-OPCOの2026-04期の差異要因の説明を再起草する

## /2/description

**原文**

```text
Follow-up after adjustments post
```

**日本語**

調整仕訳の記帳後のフォローアップ
