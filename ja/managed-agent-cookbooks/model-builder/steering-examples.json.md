# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/model-builder/steering-examples.json](../../../managed-agent-cookbooks/model-builder/steering-examples.json)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /0/event

**原文**

```text
Build dcf for MSFT, assumptions: {wacc: 0.085, tgr: 0.025, horizon: 5}
```

**日本語**

MSFTのdcfを作成する。前提条件：{wacc: 0.085, tgr: 0.025, horizon: 5}

## /0/description

**原文**

```text
DCF with explicit assumptions
```

**日本語**

前提条件を明示したDCF

## /1/event

**原文**

```text
Build lbo for TGT, assumptions: {entry_multiple: 9.0, leverage: 5.5, hold: 5}
```

**日本語**

TGTのlboを作成する。前提条件：{entry_multiple: 9.0, leverage: 5.5, hold: 5}

## /1/description

**原文**

```text
LBO from entry multiple and leverage
```

**日本語**

取得時倍率と借入倍率から作成するLBO

## /2/event

**原文**

```text
Build 3-stmt for SHOP, source: latest 10-K
```

**日本語**

SHOPの3-stmtを作成する。情報源：最新の10-K

## /2/description

**原文**

```text
Three-statement from filings
```

**日本語**

提出書類に基づく財務三表モデル
