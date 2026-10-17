# scripts/test-cookbooks.sh の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/test-cookbooks.sh)

### scripts/test-cookbooks.sh:2

原文：

```text
Dry-run every managed-agent cookbook and assert the resolved POST /v1/agents
```

日本語：

すべての managed-agent cookbook をドライランし、展開後の POST /v1/agents の


### scripts/test-cookbooks.sh:3

原文：

```text
bodies are well-formed: valid JSON, depth-1, non-empty system prompts, no
```

日本語：

リクエスト本文が正しく構成されていることを確認する。有効な JSON、深さ 1、空でない system prompt、


### scripts/test-cookbooks.sh:4

原文：

```text
output_schema. Exits non-zero if any cookbook fails.
```

日本語：

output_schema を含まないことを検証する。いずれかが失敗した場合は、終了コードを 0 以外にする。


### scripts/test-cookbooks.sh:6

原文：

```text
 && pwd)
```

日本語：

 && pwd)


### scripts/test-cookbooks.sh:10

原文：

```text
 --dry-run 2>&1 | tail -n +2 | python3 -c 
```

日本語：

 --dry-run 2>&1 | tail -n +2 | python3 -c 


### scripts/test-cookbooks.sh:15

原文：

```text
): errs.append(f
```

日本語：

): errs.append(f


### scripts/test-cookbooks.sh:17

原文：

```text
output_schema leaked into a body
```

日本語：

リクエスト本文に output_schema が混入している


### scripts/test-cookbooks.sh:21

原文：

```text
  ✓ {sys.argv[1]:24s} {len(b)} bodies
```

日本語：

✓ {sys.argv[1]:24s} {len(b)} 個のボディ


### scripts/test-cookbooks.sh:23

原文：

```text
  ✗ $slug
```

日本語：

  ✗ $slug


