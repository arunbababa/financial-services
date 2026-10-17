# claude-for-msft-365-install/examples/python-bootstrap/mint_dev_token.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../claude-for-msft-365-install/examples/python-bootstrap/mint_dev_token.py)

### claude-for-msft-365-install/examples/python-bootstrap/mint_dev_token.py:1

原文：

```text

Mint a self-signed dev token for local testing of app.py.

First run generates dev_private.pem + dev_jwks.json in the current directory.
Subsequent runs reuse them.

    python mint_dev_token.py --oid alice --group <gid> --group <gid2>

```

日本語：

app.pyのローカルテスト用に、自己署名の開発トークンを生成する。

初回実行時はカレントディレクトリにdev_private.pemとdev_jwks.jsonを生成し、2回目以降は再利用する。

```sh
python mint_dev_token.py --oid alice --group <gid> --group <gid2>
```
