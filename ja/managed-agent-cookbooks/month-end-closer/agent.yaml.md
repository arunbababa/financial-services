# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/month-end-closer/agent.yaml](../../../managed-agent-cookbooks/month-end-closer/agent.yaml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## L1（コメント）

**原文**

```text
Month-End Closer — managed-agent cookbook
```

**日本語**

月次決算エージェント（Month-End Closer） — Managed Agentの設定・利用例。

## /system/append

**原文**

```text
You are running headless. Produce files in ./out/; do not assume an open Office document.
```

**日本語**

GUIで開いている文書を前提としない環境で動作します。ファイルは`./out/`に生成してください。Office文書が開いていると仮定してはいけません。

## L28（行末コメント）

**原文**

```text
only leaf with Write
```

**日本語**

Writeを持つ唯一の末端作業担当。
