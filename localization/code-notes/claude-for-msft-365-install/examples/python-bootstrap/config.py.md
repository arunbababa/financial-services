# claude-for-msft-365-install/examples/python-bootstrap/config.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../claude-for-msft-365-install/examples/python-bootstrap/config.py)

### claude-for-msft-365-install/examples/python-bootstrap/config.py:1

原文：

```text

Edit this file to configure your bootstrap server. app.py should not need changes.

```

日本語：


このファイルを編集してブートストラップ サーバーを構成します。 app.py を変更する必要はありません。


### claude-for-msft-365-install/examples/python-bootstrap/config.py:7

原文：

```text
─── Config ──────────────────────────────────────────────────────────
```

日本語：

────構成 ─────────────────────


### claude-for-msft-365-install/examples/python-bootstrap/config.py:8

原文：

```text
your Entra tenant
```

日本語：

あなたのエントラテナント


### claude-for-msft-365-install/examples/python-bootstrap/config.py:9

原文：

```text
Claude in Office add-in app ID
```

日本語：

Claude in Office アドインのアプリ ID


### claude-for-msft-365-install/examples/python-bootstrap/config.py:15

原文：

```text
Local-dev override: point at a self-issued JWKS instead of Entra.
```

日本語：

Local-dev オーバーライド: Entra ではなく自己発行の JWKS を指します。


### claude-for-msft-365-install/examples/python-bootstrap/config.py:16

原文：

```text
Signature verification still runs. Refuses to start on non-loopback.
```

日本語：

署名検証は引き続き実行されます。非ループバックでの起動を拒否します。


### claude-for-msft-365-install/examples/python-bootstrap/config.py:19

原文：

```text
DEV_JWKS_PATH may only be used when HOST=127.0.0.1
```

日本語：

DEV_JWKS_PATH は、HOST=127.0.0.1 の場合にのみ使用できます。


### claude-for-msft-365-install/examples/python-bootstrap/config.py:21

原文：

```text
─── Catalog: every skill / MCP server you might hand out ────────────
```

日本語：

──── カタログ: 配布するすべてのスキル / MCP サーバー ──────


### claude-for-msft-365-install/examples/python-bootstrap/config.py:27

原文：

```text
Draft a deal memo from a term sheet
```

日本語：

タームシートから取引メモの草案を作成する


### claude-for-msft-365-install/examples/python-bootstrap/config.py:31

原文：

```text
Review a document for compliance issues
```

日本語：

コンプライアンス上の問題について文書を確認する


### claude-for-msft-365-install/examples/python-bootstrap/config.py:32

原文：

```text
# Compliance check

Review the document for regulatory red flags...
```

日本語：

# コンプライアンスチェック

規制上の危険信号について文書を確認してください...


### claude-for-msft-365-install/examples/python-bootstrap/config.py:35

原文：

```text
Summarize positions from the risk dashboard
```

日本語：

リスクダッシュボードからポジションを要約する


### claude-for-msft-365-install/examples/python-bootstrap/config.py:44

原文：

```text
Risk Dashboard
```

日本語：

リスクダッシュボード


### claude-for-msft-365-install/examples/python-bootstrap/config.py:45

原文：

```text
Bearer {{gateway_token}}
```

日本語：

`Bearer {{gateway_token}}`（Bearer 認証ヘッダー値）


### claude-for-msft-365-install/examples/python-bootstrap/config.py:49

原文：

```text
─── RBAC: first matching rule wins ──────────────────────────────────
```

日本語：

──── RBAC: 最初に一致したルールが優先されます ─────────────


### claude-for-msft-365-install/examples/python-bootstrap/config.py:50

原文：

```text
`when` conditions (all must match):
```

日本語：

`when` 条件 (すべて一致する必要があります):


### claude-for-msft-365-install/examples/python-bootstrap/config.py:51

原文：

```text
group — value from the Entra token's `groups` claim
```

日本語：

group — Entra トークンの `groups` クレームの値


### claude-for-msft-365-install/examples/python-bootstrap/config.py:52

原文：

```text
user  — Entra user `oid`
```

日本語：

`user`: Entra ユーザーの `oid`


### claude-for-msft-365-install/examples/python-bootstrap/config.py:53

原文：

```text
app   — Office host: "word" | "excel" | "powerpoint"
```

日本語：

`app`: Office ホスト。値は "word" | "excel" | "powerpoint"


### claude-for-msft-365-install/examples/python-bootstrap/config.py:54

原文：

```text
In production, group/user values are GUIDs — replace the names below
```

日本語：

運用環境では、グループ/ユーザーの値は GUID です。以下の名前を置き換えてください。


### claude-for-msft-365-install/examples/python-bootstrap/config.py:55

原文：

```text
with real Object IDs from Entra admin center.
```

日本語：

Entra 管理センターからの実際のオブジェクト ID を使用します。


