# claude-for-msft-365-install/examples/python-bootstrap/app.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../claude-for-msft-365-install/examples/python-bootstrap/app.py)

### claude-for-msft-365-install/examples/python-bootstrap/app.py:1

原文：

```text

Claude in Office — Bootstrap endpoint reference implementation.

The Office add-in calls GET /bootstrap with the user's Entra ID token.
This server validates the token, decides which skills and MCP servers
that employee is allowed to use, and returns them.

All customer-editable settings live in config.py — edit that, not this file.

```

日本語：

Claude in Officeのbootstrapエンドポイントの参考実装。

OfficeアドインはユーザーのEntra IDトークンを付けてGET /bootstrapを呼び出す。このサーバーはトークンを検証し、その従業員が利用できるスキルとMCPサーバーを決定して返す。

顧客が編集できる設定はすべてconfig.pyに置かれている。設定変更はこのファイルではなくconfig.pyで行う。


### claude-for-msft-365-install/examples/python-bootstrap/app.py:50

原文：

```text
─── Token validation ────────────────────────────────────────────────
```

日本語：

────トークンの検証 ───────────────


### claude-for-msft-365-install/examples/python-bootstrap/app.py:55

原文：

```text
Missing bearer token
```

日本語：

Bearerトークンがない


### claude-for-msft-365-install/examples/python-bootstrap/app.py:66

原文：

```text
Invalid token: 
```

日本語：

無効なトークン:


### claude-for-msft-365-install/examples/python-bootstrap/app.py:68

原文：

```text
─── HTTP ────────────────────────────────────────────────────────────
```

日本語：

────HTTP─────────────────────


### claude-for-msft-365-install/examples/python-bootstrap/app.py:74

原文：

```text
FastAPI reflects the preflight's requested headers
```

日本語：

FastAPI はプリフライトの要求されたヘッダーを反映します


### claude-for-msft-365-install/examples/python-bootstrap/app.py:84

原文：

```text
NOTE: We assume group membership arrives in the token's `groups` claim.
```

日本語：

注: グループ メンバーシップがトークンの `groups` クレームに含まれると想定します。


### claude-for-msft-365-install/examples/python-bootstrap/app.py:85

原文：

```text
If your tenant doesn't emit it (or you prefer your own RBAC), replace
```

日本語：

テナントがgroupsクレームを発行しない場合、または独自のRBACを使いたい場合は、


### claude-for-msft-365-install/examples/python-bootstrap/app.py:86

原文：

```text
this line with a lookup against your IdP / HRIS — e.g.
```

日本語：

この行をIdP / HRISへの照会に置き換える。例：


### claude-for-msft-365-install/examples/python-bootstrap/app.py:87

原文：

```text
groups = fetch_groups_from_graph(oid)  or  your_iam.groups_for(email)
```

日本語：

`groups = fetch_groups_from_graph(oid)  or  your_iam.groups_for(email)`

Microsoft Graph、または独自のIAMを使って所属グループを取得する代替例。
