# claude-for-msft-365-install/examples/python-bootstrap/get_tenant_id.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../claude-for-msft-365-install/examples/python-bootstrap/get_tenant_id.py)

### claude-for-msft-365-install/examples/python-bootstrap/get_tenant_id.py:2

原文：

```text

Print your Entra (Azure AD) tenant ID.

Usage:
    python get_tenant_id.py alice@yourcompany.com
    python get_tenant_id.py yourcompany.com
    python get_tenant_id.py            # tries `az account show` if Azure CLI is logged in

Set the result as TENANT_ID before running app.py.

```

日本語：


Entra (Azure AD) テナント ID を印刷します。

使用法:
python get_tenant_id.py alice@yourcompany.com
python get_tenant_id.py yourcompany.com
python get_tenant_id.py # Azure CLI がログインしている場合は `az account show` を試行します

app.py を実行する前に、結果を TENANT_ID として設定します。


### claude-for-msft-365-install/examples/python-bootstrap/get_tenant_id.py:19

原文：

```text
Entra publishes per-tenant OIDC metadata at this well-known URL.
```

日本語：

Entra は、この既知の URL でテナントごとの OIDC メタデータを公開します。


### claude-for-msft-365-install/examples/python-bootstrap/get_tenant_id.py:20

原文：

```text
The `issuer` field is https://login.microsoftonline.com/<tenant_id>/v2.0
```

日本語：

`issuer` フィールドは `https://login.microsoftonline.com/<tenant_id>/v2.0`。


### claude-for-msft-365-install/examples/python-bootstrap/get_tenant_id.py:44

原文：

```text
Pass an email/domain, or run `az login` first (
```

日本語：

電子メール/ドメインを渡すか、最初に `az login` を実行します (


