---
description: Build the bootstrap endpoint — per-user MCP servers, skills, dynamic config
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/bootstrap.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：ブートストラップ エンドポイントを構築する — ユーザーごとの MCP サーバー、スキル、動的構成

<a id="bootstrap-endpoint"></a>
# ブートストラップエンドポイント

HTTPSのGETハンドラーを用意します。アドインは起動時にユーザーの
Entraトークンを添えて呼び出し、ハンドラーはユーザーごとのJSONを返します。その応答は、
当該ユーザーのマニフェストと拡張属性を上書きします。これにより、単純な文字列属性では
持てない`mcp_servers`や`skills`等の構造化設定を配信します。

<a id="ask-first"></a>
## まず質問してください

仕様を実行する前に、自分がどのモードにいるかを確認してください。

- **仕組みを知りたいだけか。** 以下の節に基づいて回答します。よくある
  質問は、応答の形式、`{{...}}`の動作、CORSで
  問題が起きる理由です。
- **実装したいか。** 新規ハンドラーか既存の編集か、Lambda、
  Cloud Function、Express、Python等のどれを使うかを確認します。その後、
  [ハンドラーの雛形作成](#scaffolding-a-handler)へ進みます。間にある各節は、
  実装が従うインターフェース仕様です。

<a id="this-vs-extension-attrs"></a>
## ブートストラップと拡張属性の比較

どちらもユーザーごとの構成を提供します。持ち歩くものに合わせて選んでください。

| | [拡張属性](update-user-attrs.md) | ブートストラップエンドポイント |
|---|---|---|
| 実装するもの | ユーザーごとの`az rest PATCH` | HTTPSサービス |
| 保持できる値 | 256文字以下の単純な文字列 | 配列、入れ子、base64等の任意のJSON |
| に良い | トークンローテーション、リージョンオーバーライド | `mcp_servers`、`skills`、構造化されたもの |
| 更新 | トークンキャッシュにより約1時間の遅延 | `bootstrap_expires_at`で利用者側が制御 |
| 認証 | Entraトークンのクレーム（受動的） | 自分でJWTを検証（能動的） |

ユーザーごとに`gateway_token`を入れ替えるだけなら、拡張属性の方が手間を抑えられます。
あるチームにLinearのMCP、別のチームにJiraのMCPを設定したくなったら、
ブートストラップを使います。

<a id="template-interpolation"></a>
## テンプレート補間

任意の文字列値に`{{key}}`を含められます。アドインは、**設定を順に統合した結果**を
使って置換します。マニフェストのパラメータ、拡張属性、この応答の順で統合し、
後の層が前の層を上書きします。テンプレートから参照するためだけに
値を応答へ再掲する必要はありません。`gateway_token`が既にマニフェストや
拡張属性にあれば、`{{gateway_token}}`は解決できます。

応答が存在する前にリクエストが発生する必要があるため、2 つのフェーズになります。

1. **`bootstrap_url`自体**は、マニフェストと拡張属性だけで解決します。例えば、
   マニフェストに次のように指定できます。
   `bootstrap_url=https://config.internal/bootstrap?project={{gcp_project_id}}`
   チーム別のURLを拡張属性へ書き分ける代わりに、クエリパラメータで分岐する
   一つのエンドポイントを運用できます。
2. **応答内のフィールド**は、マニフェスト＋拡張属性＋今回の応答の
   すべてを統合した結果で解決します。`mcp_servers`の項目から、
   同じJSONの三行上にある`gateway_token`を参照することもできます。

未解決の `{{key}}` (タイプミス、キーがどこにも設定されていない) はそのまま残されます。
文字列 — エラーや空の置換はありません。 MCP サーバーが接続していない場合は、
アドインが実際に構築した URL を確認してください。

<a id="cors--every-url-needs-it"></a>
## CORS — すべての URL に CORS が必要です

アドインはブラウザ上で動作します。`bootstrap_url`、すべての
`mcp_servers[].url`、すべての`skills[].url`の取得は、Officeの
タスクペイン内のブラウザ側で行われます。応答に
`Access-Control-Allow-Origin: https://pivot.claude.ai`がなければ、アドインが
1バイトも受け取る前にブラウザが遮断します。サーバーは200を返してもアドインは何も受け取れず、
アドインのログにも理由が残りません。これが「動かない」ときに
最も多い原因です。

| URL | CORS が存在する場所 |
|---|---|
| `bootstrap_url` | ハンドラーの応答ヘッダー。 API ゲートウェイ / クラウド関数の背後で、`OPTIONS` プリフライトも構成します。ブラウザーは、カスタム ヘッダーを含むリクエストの前にプリフライトを送信します。以下の推奨されるプリフライト応答を参照してください。 |
| `mcp_servers[].url` | MCP サーバー自体。パブリックのもの (Linear、Atlassian) はすでに許可されています。内部のものは、追加するまでほぼ確実に機能しません。 |
| `skills[].url` | **URL ではなくバケットです。** 署名付き URL はリクエストを認証します。CORS は付与されません。 S3 にはバケットの CORS 構成が必要で、GCS には `gsutil cors set` が必要で、Azure には BLOB サービスの CORS ルールが必要です。 |
| `otlp_endpoint` | OTEL コレクターの HTTP レシーバー。ほとんどのコレクターはデフォルトで同一オリジンのみを設定します。OTLP/HTTP レシーバーに `cors.allowed_origins` を設定します。 |

`bootstrap_url` の場合、推奨されるプリフライト応答は次のとおりです。

```
Access-Control-Allow-Origin:  https://pivot.claude.ai
Access-Control-Allow-Methods: GET
Access-Control-Allow-Headers: Authorization, X-Claude-User-Agent, *
```

ここではリクエストヘッダーに`*`を許可しても安全です。安全性はヘッダーの絞込みではなくEntra
トークンで確保するためです。アドインが将来ヘッダーを追加してもプリフライトを維持できます。
`Allow-Origin`は`https://pivot.claude.ai`に固定してください。

署名付きURLの問題は特に見落としやすく、`curl`はCORSを無視するため成功し、
署名も正しくオブジェクトも存在するのに、スキルは読み込まれません。
バケット CORS を 1 回設定します。

```json
// S3 — aws s3api put-bucket-cors --bucket <name> --cors-configuration file://cors.json
{ "CORSRules": [{ "AllowedOrigins": ["https://pivot.claude.ai"], "AllowedMethods": ["GET"], "AllowedHeaders": ["*"] }] }
```

```bash
# GCS — gsutil cors set cors.json gs://<bucket>
[{"origin": ["https://pivot.claude.ai"], "method": ["GET"], "responseHeader": ["*"]}]
```

```bash
# Azure — az storage cors add --services b --methods GET --origins https://pivot.claude.ai --allowed-headers '*' --account-name <name>
```

CORS エラーをデバッグしている場合は、ブラウザ内の devtools を開きます。
タスクペイン (Windows では右クリック→「検査」、または Safari の「開発」経由で接続)
Mac のメニュー)、[ネットワーク] タブでリクエストを探します。 CORS ブロックは次のように表示されます。
失敗したリクエストには応答本文がなく、オリジンを指定するコンソール エラーが表示されます。

<a id="request"></a>
## リクエスト

```
GET <bootstrap_url>                            # after interpolation
Authorization: Bearer <entra_token>            # only if entra_sso=1 in manifest
X-Claude-User-Agent: claude-<app>/<version>    # always sent
```

`X-Claude-User-Agent` は、アドインが実行されている Office ホストを識別します。
`<app>` は、`word`、`excel`、または `powerpoint` のいずれかです。 `<version>` はアドインです
ビルド (例: `claude-excel/1.4.2`)。さまざまなスキルや MCP を返すために使用します
Office 製品ごとにサーバーを設定したり、アドインをユーザーの特定のホストにゲートしたりできます。

`entra_sso=1` がない場合、Authorization ヘッダーはありません。リクエストは次のようになります。
アドイン側からは匿名です。エンドポイントが後ろにある場合は問題ありません
ネットワーク分離、mTLS、またはアドインが認識しない別の認証レイヤー。

`entra_sso=1` を使用して、JWT を信頼する前に検証します。

| クレーム | チェックする |
|---|---|
| `aud` | `c2995f31-11e7-4882-b7a7-ef9def0a0266` — アドインのデフォルトのアプリ ID、または [マニフェスト](manifest.md#entra-sso) で `graph_client_id` を設定した場合は独自のアプリの GUID。それ以外の場合は、トークンがこのために鋳造されなかったことを意味します。 |
| `iss` | `https://login.microsoftonline.com/<YOUR_TENANT_ID>/v2.0` — あなたのテナント。他のテナントを拒否します。 |
| `exp` | 有効期限内であること。ライブラリに処理させ、自作しないでください。 |
| `oid` | ユーザーの安定したオブジェクト ID。これは検索キーです。電子メール (`upn`/`preferred_username`) は変更できますが、`oid` は変更できません。 |

[マニフェスト](manifest.md#entra-sso)で`entra_scope`を指定した場合、Bearerに入るのは
IDトークンではなく**アクセストークン**です。`aud`がAPIの
Application ID URI（クライアントGUIDではなく`api://<guid>`）と一致すること、`scp`に
定義したスコープが含まれることを確認します。`entra_scope`に複数を指定したとき、
`scp`は空白区切りのリストです。`iss`、`exp`、`oid`と署名の
検証は同じです。

署名検証にはMicrosoftのJWKS
（`https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys`）が必要です。
`jose`（Node）、`PyJWT`＋`cryptography`（Python）、`Microsoft.IdentityModel.Tokens`
（.NET）等のライブラリを使ってください。JWT検証の自作は安全上のバグを招きます。

<a id="response"></a>
## 応答

`200 OK`、`Content-Type: application/json`、CORS ヘッダーごと
[上](#cors--every-url-needs-it)。

応答本体はフラットなオブジェクトです。全フィールドは省略可能で、当該ユーザーに対して
異なる設定だけを返します。未知のキーは無視されるので、現行アドインがまだ
読まないフィールドも追加でき、対応版が公開されたときに有効になります。

<a id="provider-keys"></a>
### プロバイダーキー

[マニフェスト](manifest.md#keys-by-cloud) のクラウド構成キーのいずれか
テーブル — `gateway_url`、`gateway_token`、`aws_role_arn`、`gcp_region` など
同じ名前、同じ意味、ユーザーごとにのみ。

`gateway_api_format: "vertex"`を返す場合は、`gcp_project_id`と
`gcp_region`も返すか、下位の設定層で指定します。アドインが組み立てる
Vertexの`:rawPredict` URLのパスに必要なためです。`"bedrock"`には追加項目は不要です。

<a id="telemetry"></a>
### テレメトリ

```json
"otlp_endpoint": "https://otel-collector.your-domain.com",
"otlp_headers": "Authorization=Bearer {{gateway_token}}",
"otlp_resource_attributes": "team.name={{team}},deployment.environment=prod"
```

`otlp_endpoint`は、自分で運用するOpenTelemetryコレクターの基底HTTPS URLです。
アドインは`/v1/traces`を付けてOTLP/HTTPで送信します。`otlp_headers`は
標準の`key1=value1,key2=value2`形式で、ほかの値と同じようにテンプレート補間されます。
`otlp_resource_attributes`も同じ形式です（標準の
`OTEL_RESOURCE_ATTRIBUTES`変数と同様）。すべてのスパンのOpenTelemetry Resourceへ
統合されます。コレクターでの経路選択や帰属の判定に特定のリソース属性が
必要な場合に使います。コレクターはアドインのオリジンからの
CORSを許可する必要があります。[上記](#cors--every-url-needs-it)を参照してください。

<a id="inference_headers"></a>
### `inference_headers`

```json
"inference_headers": { "x-application-id": "app123" }
```

アドインがゲートウェイ（`gateway_url`）へ送るすべてのリクエストに付ける追加HTTPヘッダーです。
通常は、ゲートウェイが費用配賦に使う
会計用タグ等です。ゲートウェイ構成でのみ適用され、クラウドへの直接接続では
無視されます。アドインは内容を解釈せずそのまま通します。ただし`Authorization`、
`x-api-key`、
`Content-Type`、`Host`、`Content-Length`、`User-Agent`、`Cookie`と、
`anthropic-*`／`x-amz-*`／`x-goog-*`の各ヘッダーは予約済みで、除外されます。

<a id="mcp_servers"></a>
### `mcp_servers`

このユーザーに対してアドインが接続する MCP サーバーの配列。

```json
"mcp_servers": [
  { "url": "https://mcp.linear.app/sse", "label": "Linear" },
  {
    "url": "https://internal.yourcompany.com/mcp/risk",
    "label": "Risk Dashboard",
    "headers": { "Authorization": "Bearer {{gateway_token}}" }
  }
]
```

| フィールド | |
|---|---|
| `url` | MCP サーバーのエンドポイント。補間済み。 |
| `label` | アドイン UI での表示名。 |
| `headers` | 省略可能。そのMCPサーバーへの全リクエストに送信します。値はテンプレート補間されるため、ブートストラップエンドポイント自体にトークンを見せずに、ユーザーごとのトークンを引き渡せます。 |

<a id="skills"></a>
### `skills`

このユーザーにロードされたスキルの配列。それぞれは、base64 としてインライン化されるか、
URL から取得 — どちらかを設定します。

```json
"skills": [
  {
    "name": "deal-memo",
    "description": "Draft a deal memo from a term sheet",
    "url": "https://yourbucket.s3.amazonaws.com/skills/deal-memo.zip?X-Amz-..."
  },
  {
    "name": "compliance-check",
    "content": "IyBDb21wbGlhbmNlIGNoZWNrCgpSZXZpZXcgdGhlIGRvY3VtZW50IGZvci4uLg=="
  }
]
```

| フィールド | |
|---|---|
| `name` | スキル識別子。補間済み。 |
| `description` | オプション。スキルピッカーに表示されます。 |
| `content` | Base64バイト。 zip (`SKILL.md` + アセットを含む完全なスキル バンドル) または生の `SKILL.md` テキストのいずれか - アドインはデコード時にスニッフィングします。 |
| `url` | 署名付き URL (S3、GCS、Azure SAS)。裸の GET、認証ヘッダーは追加されていません - 認証を署名に焼き付けます。レスポンスボディは `content` と同じ方法でスニッフィングされました。補間済み。 |

小さなテキストだけのスキルには、インラインの`content`が最も単純です。画像を含むzipを
配布するときや、base64で応答が大きくなり始めたら`url`を使います。

<a id="disabled_features"></a>
### `disabled_features`

このユーザーに対してロックする機能スラッグの JSON 配列。と同じ語彙
[マニフェストキー](manifest.md#disabled-features) — ブートストラップはユーザーごとの
層。

```json
"disabled_features": ["skills.authoring"]
```

<a id="available_models"></a>
### `available_models`

このユーザー向けにモデル選択欄を上書きします。意味と項目形式は
[マニフェストのキー](manifest.md#available_models)と同じです。IDおよび／または
`{id, label}`オブジェクトのJSON配列です。上書きなので、ユーザーに残すべき
すべてのモデルを列挙してください。

```json
"available_models": [{ "id": "claude-opus-4-8", "label": "Opus 4.8" }, "claude-sonnet-5"]
```

<a id="access_policies"></a>
### `access_policies`

許可/拒否ステートメントのネイティブ JSON 配列 - ユーザーごとのレイヤー
[マニフェストキー](manifest.md#access_policies);で配列を構築します
[アクセス ポリシー](access-policies.md)。文字列ではなく実際の配列として渡します。

```json
"access_policies": [
  { "effect": "deny", "action": "addin.access",
    "resource": { "type": "open_file",
      "identifiers": [{ "type": "mip_label_guid", "equals": "<guid>" }] } }
]
```

<a id="bootstrap_expires_at"></a>
### `bootstrap_expires_at`

設定の有効期限を示すエポック時刻です（秒／ミリ秒は自動判別）。
アドインは期限前に再取得します。省略した場合、設定は
タスクペインが再読み込みされるまで有効です。

短命なトークンを配布する場合に設定します。キープアライブ目的で設定しないでください。
応答内に期限切れになるものがなければ、再取得は無駄になります。

<a id="scaffolding-a-handler"></a>
## ハンドラーの足場を作る

`skills`と`mcp_servers`のRBACを備えた、実行可能なPython/FastAPIの参考実装は
[`examples/python-bootstrap/`](../examples/python-bootstrap)にあります。
コピーして使えるものを求められたら、こちらを案内してください。

彼らがそれを構築したいときは、彼らに代わってそれを作成します。上記の契約書とは、
あなたはそれに対してコーディングしています。これらを正しく理解してください:

**JWT検証がセキュリティ境界です。** MicrosoftのJWKSに照らして署名を検証し、
`aud`と`iss`を厳密に確認し、ユーザー検索には`oid`を取得します。
これを省略して、未検証のトークンの`preferred_username`を信頼するハンドラーは、
手順を増やしただけの無防備な公開エンドポイントです。

**ハンドラーだけでなく、返すすべてのURLでCORSが必要です。**
[CORSの節](#cors--every-url-needs-it)を参照してください。ハンドラーだけ動作しても、
CORS未設定のバケットから署名付きスキルURLを返すと、スキルが一切
読み込めない構成を作ってしまいがちです。

**ユーザー検索は利用者側の業務ロジックです。** 実処理を入れる場所へ明確に
`// TODO: look up config for oid`を残します。DynamoDB、Postgres、YAMLファイル等、
何を正本にするかは利用者に確認し、推測で決めないでください。

**スパースを返します。** マニフェストのデフォルトと異なるキーのみ。空の
`{}` は有効な応答です。これは、「このユーザーが組織全体の構成を取得する」ことを意味します。

書く前に質問してください: Lambda + API Gateway、Cloud Function、プレーン Express、
他に何か？ユーザーごとの構成はどこに存在しますか - ハンドラー内のインライン
（パイロットには問題ありません）、それともストアから読みますか？
