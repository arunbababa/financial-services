# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/earnings-reviewer/steering-examples.json](../../../managed-agent-cookbooks/earnings-reviewer/steering-examples.json)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## /0/event

**原文**

```text
Process earnings: NVDA Q1-FY27
```

**日本語**

決算を処理する：NVDA Q1-FY27

## /0/description

**原文**

```text
Single ticker, single period
```

**日本語**

単一ティッカー・単一期間

## /1/event

**原文**

```text
Process earnings: coverage-list semis, period Q1-FY27
```

**日本語**

決算を処理する：調査担当銘柄リストsemis、期間Q1-FY27

## /1/description

**原文**

```text
Fan-out across a coverage list (orchestration layer iterates)
```

**日本語**

調査担当銘柄群に処理を展開する（オーケストレーション層が反復実行する）

## /2/event

**原文**

```text
Update model only: NVDA Q1-FY27, skip note
```

**日本語**

モデルだけを更新する：NVDA Q1-FY27、調査ノートは省略

## /2/description

**原文**

```text
Follow-up when the analyst writes the note themselves
```

**日本語**

アナリストが自分でノートを書く場合の追加指示
