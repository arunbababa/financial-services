# 設定ファイルの自然言語対訳

原本：[managed-agent-cookbooks/gl-reconciler/agent.yaml](../../../managed-agent-cookbooks/gl-reconciler/agent.yaml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## L1（コメント）

**原文**

```text
GL Reconciler — orchestrator
```

**日本語**

GL Reconciler（総勘定元帳照合）— 全体の処理を統括するエージェント。

## L3–5（コメント）

**原文**

```text
Deploy manifest for `POST /v1/agents`. Field names match the API; the deploy
script resolves {file:} / {path:} / {manifest:} references before posting.
See ../README.md for the manifest→API mapping.
```

**日本語**

`POST /v1/agents`用の配備マニフェストです。フィールド名はAPIに合わせています。配備スクリプトは送信前に`{file:}`、`{path:}`、`{manifest:}`の参照を解決します。マニフェストからAPIへの対応は`../README.md`を参照してください。

## /system/append

**原文**

```text
You are running headless. Produce files in ./out/; do not assume an open Office document.
```

**日本語**

GUIで開いている文書を前提としない環境で動作します。ファイルは`./out/`に生成してください。Office文書が開いていると仮定してはいけません。

## L14–15（コメント）

**原文**

```text
The orchestrator never reads counterparty documents directly and never holds
bash or write — it dispatches, aggregates, and hands off. See ./README.md.
```

**日本語**

全体の処理を統括するエージェントは、取引相手の文書を直接読むことも、bashやwriteを持つこともありません。作業の振分け、集約、引継ぎを行います。`./README.md`を参照してください。

## L30（行末コメント）

**原文**

```text
read-only server
```

**日本語**

読取専用のサーバー。

## L34（行末コメント）

**原文**

```text
read-only server
```

**日本語**

読取専用のサーバー。

## L39（行末コメント）

**原文**

```text
set in your environment or vault
```

**日本語**

環境変数または秘密情報の保管先で設定する。
