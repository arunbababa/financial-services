> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../claude-for-msft-365-install/examples/python-bootstrap/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="bootstrap-endpoint--python-reference"></a>
# ブートストラップ エンドポイント — Python リファレンス

Office `/bootstrap` エンドポイントの Claude の最小限の FastAPI 実装。
呼び出し元の Entra ID トークンを検証し、従業員ごとに `skills` と
`mcp_servers` は、単純な最初に一致する RBAC テーブルに基づきます。

<a id="run-against-your-real-entra-tenant"></a>
## 実際の Entra テナントに対して実行します

```bash
pip install -r requirements.txt
# Find your tenant ID:
python get_tenant_id.py you@yourcompany.com
export TENANT_ID=<your-tenant-guid>
python app.py
```

<a id="run-locally-with-a-fake-token"></a>
## 偽のトークンを使用してローカルで実行する

```bash
pip install -r requirements.txt
export TENANT_ID=dev-tenant
TOKEN=$(python mint_dev_token.py --oid alice --group investment-banking)
DEV_JWKS_PATH=dev_jwks.json python app.py &
curl -H "Authorization: Bearer $TOKEN" \
     -H "X-Claude-User-Agent: claude-word/1.0.0" \
     http://127.0.0.1:8080/bootstrap
```

<a id="customize"></a>
## カスタマイズ

変更する項目はすべて**`config.py`**にあります。`app.py`の編集は不要なはずです。

- `SKILLS` および `MCP_SERVERS` を編集します。配布できる完全なカタログです。
- `RULES` を編集 — 最初に一致したルールが優先されます。一番下の空の `when: {}` がデフォルトです。
- `RULES` 内のプレースホルダー グループ/ユーザー名を実際の Entra オブジェクト ID (GUID) に置き換えます。
- 所属グループはトークンの`groups`クレームから読みます。テナントが
  これを発行しない場合、`app.py`の`groups = ...`を、社内ディレクトリに対する
  検索へ置き換えてください。
- ルールは、`"app": "word" | "excel" | "powerpoint"` を使用して Office ホストごとにスコープを設定できます。
  アドインが送信する `X-Claude-User-Agent` ヘッダーから解析されます。
- `groups` クレームは、デフォルトでは Entra トークンに**ありません**。以下で有効にします
  *アプリの登録 → トークン構成 → アプリのグループ要求を追加*。
- メモリ内の `RULES` を実際の信頼できるソース (DB、構成サービスなど) と交換します。

<a id="security"></a>
## セキュリティ

`DEV_JWKS_PATH`を使うと、Microsoftの代わりに自己発行の署名鍵を
信頼します。`127.0.0.1`にバインドしなければ起動を拒否します。配備済みの環境では
**決して**設定してはいけません。
