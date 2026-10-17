---
description: Generate the add-in manifest XML with your cloud config baked in
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/manifest.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：クラウド構成を組み込んだアドインのマニフェスト XML を生成します。

<a id="generate-add-in-manifest"></a>
# アドインマニフェストを生成する

スクリプトは正本のマニフェストを取得し、設定をタスクペインの
URLへ付加します。機密設定（`gateway_token`、`azure_api_key`、
`google_client_secret`、`otlp_headers`、`inference_headers`、`mcp_servers`）は
`#`以降へ、その他はクエリパラメータへ入れます。旧版で生成した
マニフェストは再生成・再配備してください。Outlookは、
Microsoftの`MailApp`スキーマが、Excel/Word/PowerPoint共通の`TaskPaneApp`スキーマと
異なるため、別のテンプレートを使います。導入するアプリを確認し、
ホスト種別ごとに一つのファイルを生成してください。

| ホスト引数 | アプリ | テンプレート |
|---|---|---|
| `office` | エクセル、ワード、パワーポイント | `pivot.claude.ai/manifest.xml` |
| `outlook` | Outlook（メール+カレンダー） | `pivot.claude.ai/manifest-outlook-3p.xml` |

<a id="keys-by-cloud"></a>
## クラウドによるキー

クラウド パスに必要なキーのみを要求します。 8つすべてを求めないでください。

| クラウド | キー |
|---|---|
| Vertex | `gcp_project_id` `gcp_region` `google_client_id` `google_client_secret` |
| Bedrock | `aws_role_arn` `aws_region` |
| Foundry | `azure_resource_name` `azure_api_key` — キーレスなら`azure_resource_name`＋Entra（[Foundry keyless](#use-the-entra-token-for-foundry-keyless)を参照） |
| ゲートウェイ | `gateway_url` `gateway_token` `gateway_auth_header` `gateway_api_format` |
| ゲートウェイ (`gateway_api_format=vertex`) | `gcp_project_id` `gcp_region` も |

Amazon Bedrock は **現在、`outlook` ホストではサポートされていません**。スクリプト
`aws_*` キーを `outlook` とともに渡すと、エラーで終了します。

<a id="outlook--microsoft-graph"></a>
## Outlook — Microsoft Graph

Outlook は、Microsoft Graph 経由でユーザーのメールボックスと予定表を読み取ります。
どのクラウドがサービスを提供するかに関係なく、テナント全体の管理者の同意を 1 回だけ必要とします
モデル。前に [consent](consent.md#outlook--microsoft-graph-consent) を実行してください。
デプロイ中 — それ以外の場合、すべてのユーザーが最初に開くときに「管理者の承認が必要」をクリックします。

ポリシーでサードパーティ アプリへの同意が禁止されている場合は、
`graph_client_id` (独自のシングルテナント Entra アプリのクライアント ID
Mail.ReadWrite、Calendars.Read、People.Read、User.Read、offline_access
委任されたアクセス許可と管理者の同意が付与されます)。それ以外の場合は未設定のままにし、
アドインは Anthropic のマルチテナント アプリを使用します。

<a id="sovereign--national-clouds-gcc-high-dod-21vianet"></a>
## ソブリン/ナショナル クラウド (GCC-High、DoD、21Vianet)

アドインはサインイン時にOfficeが報告する認証機関のホスト名から
テナントのナショナルクラウドを自動検出し、対応するGraphとEntraの
エンドポイントを解決します。したがって、多くのソブリンクラウドのテナントでは**クラウド設定は不要**です。
ただし`graph_client_id`で自社のEntraアプリを指定する手順は必要です。
Anthropicのマルチテナントアプリは商用クラウドにしかありません。
[entra-app](entra-app.md#gcc-high--dod--21vianet)にあるAzure Government／21Vianet
ポータルでの登録手順を参照してください。GCC-High向けOutlookマニフェストは、
通常のキー以外に追加設定を必要としません。

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" outlook manifest-outlook.xml \
  <provider keys> entra_sso=1 graph_client_id=<your-app-guid>
```

<a id="when-to-set-graph_cloud"></a>
### `graph_cloud` を設定する場合

クラウドは単一の列挙値として構成されます (URL ではありません)。それぞれの値のマッピング
Microsoft の固定 Graph + Entra エンドポイント ペアへ
[ナショナル クラウド展開](https://learn.microsoft.com/graph/deployments)
アドイン内。

| テナント | `graph_cloud` | 注意事項 |
|---|---|---|
| コマーシャルまたは GCC | `global` | デフォルト。省略される場合があります |
| GCC高 | `us-gov-high` | 自動検出。レビュー済みのマニフェストに固定するように明示的に設定します |
| 米国政府国防総省 | `us-gov-dod` | **常に必須** - DoD は GCC High と権限ホストを共有しているため、自動検出は GCC High を選択します |
| 中国 (21Vianet) | `china` | 自動検出。明示的に固定するように設定します |

DoD Outlook マニフェスト:

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" outlook manifest-outlook.xml \
  <provider keys> entra_sso=1 graph_client_id=<your-app-guid> graph_cloud=us-gov-dod
```

ビルドスクリプトはアドインの読込み時と同じ規則を適用します。
未知の値はエラーにし、`global`以外の`graph_cloud`では必ず
`graph_client_id`を要求します（なければサインインが分かりにくいAADSTS700016で失敗します）。

`graph_cloud` は、Word/Excel/PowerPoint の Entra SSO 権限も管理します。
これらは認証パスを共有するため、必要に応じて `office` マニフェストにも含めてください。
設定してください。

**Bedrock / WIF 注:** `.us` 発行の idToken には発行者があります
`https://login.microsoftonline.us/{tenant}/v2.0` — AWS OIDC ID
プロバイダーは、`.com` ではなく、その発行者で構成する必要があります。

<a id="entra-sso"></a>
## エントラ SSO

`entra_sso=1`を指定すると、アドインは起動時にEntra IDトークンを取得します。
ユーザーのMicrosoft IDが必要な構成で設定します。BedrockはSTSの
Webアイデンティティに使い、ブートストラップはBearer認証に使います。
ユーザーごとの拡張属性（[update-user-attrs](update-user-attrs.md)）は、トークン内の
`extn.*`クレームとして渡されます。

**管理者の同意が前提条件です。** これがないと、すべてのユーザーが Microsoft にアクセスしてしまいます。
最初に開くときに同意ダイアログが表示されます。最初に [consent](consent.md) を実行します。
`entra_sso=1` はユーザーに対してサイレントです。

静的なゲートウェイ設定やGoogle OAuthを使うVertex等、Entraが不要なら、
無効のままにします。Microsoftが関与しない構成で、
ユーザーへMicrosoftの認証画面を表示しないためです。

**独自の Entra アプリを使用してください。** デフォルトでは、トークンは Anthropic のトークンとしてリクエストされます。
マルチテナント アプリ (`c2995f31-…`) であるため、その `aud` クレームはその GUID です。もしあなたの
ブートストラップ エンドポイントまたはトークン交換サービスでは、アプリと一致するために `aud` が必要です
*あなたの*テナントに登録されている場合は、`graph_client_id=<your-app-guid>` を設定します。参照
[entra-app](entra-app.md) 登録手順 (リダイレクト URI、API セットアップ、
管理者の同意）。 [consent](consent.md) は Anthropic のデフォルト アプリのみをカバーします。

**ID トークンの代わりにアクセス トークンを送信します。** `graph_client_id` のみの場合
アドインは依然として *ID トークン * をブートストラップ エンドポイントに送信します。`aud` があなたのものです
アプリの GUID がありますが、`scp` クレームはありません。エンドポイントが標準の OAuth2 の場合
`aud` + `scp`、または RFC 8693 トークン交換を検証する保護されたリソース
サービス、`entra_scope=api://<your-app-guid>/<scope>` とアドインを設定します
代わりに、そのスコープの *アクセス トークン* を要求します。送信するベアラーは運ぶ
`aud` = API のアプリ ID URI および `scp` = 付与されたスコープ。 Entra では、あなたの
アプリの登録: **API を公開** (アプリケーション ID URI `api://<guid>`)、
`access_as_user` などのスコープを指定し、同じアプリに委任されたアクセス許可を付与します。
次に、テナントに管理者の同意を与えます。アプリマニフェストで設定します
`accessTokenAcceptedVersion: 2` なので、発行されたトークンは v2.0 クレームを使用します
(`iss = login.microsoftonline.com/<tid>/v2.0`, `azp`, `preferred_username`);
未設定のままにすると、v1.0 トークンが取得されますが、バリデーターが拒否する可能性があります。
`/.default` (同意されたすべてのスコープを要求) も機能します。

**複数スコープ：** `entra_scope`はカンマまたは空白区切りの
一覧を受け付けます。例：`entra_scope=api://<guid>/use_llm,api://<guid>/admin`。すべてのスコープは
**同じリソース**を対象にする必要があります。一つのトークンの`aud`は一つなので、MSALは
二つのAPIにまたがるトークンを発行できません（`api://torii/x,api://other/y`は失敗するか、
黙って片方だけが有効になります）。Bearerの`scp`クレームは空白区切りの一覧になります。
同意されたすべてのスコープが必要な場合は、それらを列挙するよりも `/.default` を優先してください。

`entra_scope`には`graph_client_id`が必要です。ビルドスクリプトは*この組合せ*を
検査しますが、スコープ文字列自体は検査せず、空白だけでない値は受け付けます。
構文はサインイン時にEntraが検査します。不正なスコープは
ビルド失敗ではなく`AADSTS`エラーになります。どちらのキーもマニフェスト専用です。
拡張属性の読取りやブートストラップ呼出しの*前*にNAAを初期化するために必要なので、
それらの層から渡すことはできません。
`entra_scope`を未設定にするとIDトークンを送ります。

<a id="use-the-entra-token-as-your-gateway-credential"></a>
## Entra トークンをゲートウェイ認証情報として使用する

ゲートウェイがすでに Entra JWT (`aud` + `scp` を自分のものに対して検証している場合)
API リソース)、別個の `gateway_token` やブートストラップ ホップは必要ありません。
`gateway_auth_source=entra` を設定すると、アドインは Entra アクセス トークンを送信します。
すべてのゲートウェイ呼び出しで上記で `Authorization: Bearer` として直接取得され、
有効期限が切れる前にサイレントに再取得します。エンドユーザーエクスペリエンスは入力ゼロです
SSO: アドインを開いてチャットを開始します。

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" office manifest.xml \
  gateway_url=https://llm-gateway.your-org.example \
  entra_sso=1 \
  graph_client_id=<client-app-guid> \
  entra_scope=api://<resource-app-guid>/access_as_user \
  gateway_auth_source=entra
```

`gateway_auth_source=entra`には`entra_scope`、したがって
`graph_client_id`と`entra_sso=1`が必要です。ビルドスクリプトが検査します。
`gateway_auth_header=authorization`を暗黙に指定するため、そのキーは省略できます。
`gateway_token`も同時に設定してはいけません。無視され、スクリプトが警告します。

<a id="use-the-entra-token-for-foundry-keyless"></a>
## Foundry 用の Entra トークンを使用する (キーレス)

Foundryへの直接接続は通常、リソースの固定`azure_api_key`を使います。キーを廃止し、
各ユーザーに自分のEntra IDで認証させるには、
`azure_resource_name`とともに`gateway_auth_source=entra`を設定し、
`azure_api_key`を省略します。スコープの対象は自分が公開するAPIではなく、Azureの
Cognitive Servicesリソースです。

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" office manifest.xml \
  azure_resource_name=<your-foundry-resource> \
  entra_sso=1 \
  graph_client_id=<your-app-guid> \
  entra_scope=https://cognitiveservices.azure.com/.default \
  gateway_auth_source=entra
```

アドインは、`cognitiveservices.azure.com` を対象とするアクセス トークンを取得します。
Foundry 呼び出しごとに `Authorization: Bearer` として送信し、再取得します
有効期限が切れる前に。 Azure はトークンを検証し、ユーザーがトークンを保持していることを確認します。
リソースに対する **Cognitive Services ユーザー** ロール — キーはどこにも保存されません。
Entra アプリには、Azure Cognitive Services `user_impersonation` の委任が必要です
許可 (自己公開 API ではありません)。 [entra-app](entra-app.md) を参照してください。両方の場合
`azure_api_key` および `gateway_auth_source=entra` が存在する場合、キーは無視されます。

**`ai.azure.com`ではなく`cognitiveservices.azure.com`を使う理由。** アドインは、
自社のEntraアプリに対するNested App Authenticationで各ユーザーをサインインさせます。
このユーザーごとの*委任*フローは、アプリのAzure Cognitive Servicesの
`user_impersonation`権限と組み合わせ、そのaudienceは
`https://cognitiveservices.azure.com`です。Claude Desktopの
Foundryサインインと同じスコープなので、Desktop用に登録済みのEntraアプリを
そのまま使えます。MicrosoftのSDK・マネージドIDの文書は`https://ai.azure.com/.default`を
使います。Foundryは両audienceを受け付けますが、このスコープは
`DefaultAzureCredential`、`az login`、サービスプリンシパル等の認証情報ベースのSDKフロー用で、
アプリ登録の委任権限を使いません。アドインのユーザーごとのサインインには、
`cognitiveservices.azure.com/.default`を使ってください。

**Entra セットアップ:** [entra-app](entra-app.md) を参照 — *ゲートウェイ / ブートストラップ認証*
権限テーブルの行に加えて、
[バックエンド検証](entra-app.md#what-your-backend-validates) セクション
ゲートウェイがチェックする必要がある `iss`/`aud`/`scp`/JWKS 値。 GCC 高 / 国防総省
導入については、
[同じドキュメント](entra-app.md#gcc-high--dod--21vianet)。

<a id="bootstrap-endpoint"></a>
## ブートストラップエンドポイント

`bootstrap_url` は、ホストする HTTPS エンドポイントを指します。起動時にアドイン
そこからユーザーごとの JSON (プロバイダー キー、`mcp_servers`、`skills`) を取得します。
応答はそのユーザーのマニフェスト値をオーバーライドします。 URL自体は
マニフェスト + 属性に対する [補間](bootstrap.md#template-interpolation)
フェッチの前に、1 つのエンドポイントがクエリ パラメータで分岐できるようにします。

リクエスト/レスポンスコントラクト、JWT については、[bootstrap](bootstrap.md) を参照してください。
検証とハンドラーのスキャフォールディング。

<a id="mcp-servers"></a>
## MCPサーバー

`mcp_servers` は、顧客がホストする MCP サーバーの JSON 配列です。
に直接接続します。各エントリは `{url, label, headers?, discover?}` —
`headers` の存在は静的認証を意味します。存在しない場合、OAuth 検出がトリガーされます。価値観
`{{gateway_url}}` スタイルのテンプレートを介して他の構成キーを補間します。

ここで設定すると、1 つのリストが組織全体に適用されます。ユーザーごとのリストは以下に属します
[bootstrap](bootstrap.md#mcp_servers)、これにも完全なスキーマが含まれています。の
値はシェル引数内の JSON であり、一重引用符で囲みます。

```bash
mcp_servers='[{"url":"{{gateway_url}}/deepwiki/mcp","label":"DeepWiki","headers":{"Authorization":"Bearer {{gateway_token}}"}}]'
```

<a id="telemetry"></a>
## テレメトリ

`otlp_endpoint` は、アドインの OpenTelemetry トレースをコレクターにルーティングします。
操作する。これをコレクタのベース HTTPS URL に設定します - アドインが追加します
`/v1/traces` と OTLP/HTTP を投稿します。 gRPC はサポートされていません (アドインは
ブラウザ WebView)。未設定のままにすると、カスタム コレクターは構成されません。

`otlp_headers` は、同じコレクターに認証ヘッダーを提供します。
`key1=value1,key2=value2`形式を標準搭載
`OTEL_EXPORTER_OTLP_HEADERS` 変数。マニフェスト内の値を URL エンコードします。

`otlp_resource_attributes` は、OpenTelemetry リソースに属性を追加します。
すべてのスパン、標準と同じ `key1=value1,key2=value2` 形式
`OTEL_RESOURCE_ATTRIBUTES` 変数。コレクターが必要とする場合にこれを使用してください
ルーティングまたは属性のための特定のリソース属性 (例:
`team.name=platform,deployment.environment=prod`)。アドインはすでに設定されています
`service.name`、`service.version`、および `git.sha`。ここで指定する値は
上に統合しました。

ここでこれらを設定すると、1 つのコレクタが組織全体に適用されます。ユーザーごとのルーティングは以下に属します
[bootstrap](bootstrap.md#telemetry) または拡張属性。

<a id="inference-headers"></a>
## 推論ヘッダー

`inference_headers` は、アドインが添付する追加の HTTP ヘッダーの JSON オブジェクトです。
ゲートウェイに送信されるすべてのリクエスト (`gateway_url`)。用途:
ゲートウェイが期待する会計タグまたはコスト割り当てタグ — 例: 内部タグ
アプリケーション ID — したがって、その前にヘッダーを挿入するプロキシは必要ありません。
ゲートウェイを使用する場合にのみ適用されます。クラウドへの直接接続では無視されます。

```bash
inference_headers='{"x-application-id":"app123"}'
```

アドインは値を不透明として扱います。 `Authorization`、`x-api-key`、
`Content-Type`、`Host`、`Content-Length`、`User-Agent`、`Cookie`、および任意
`anthropic-*` / `x-amz-*` / `x-goog-*` ヘッダーは予約され、サイレントに削除されます
— アドイン独自の認証とプロトコル ネゴシエーションを実行します。

ここで設定すると、1 つのヘッダー セットが組織全体に適用されます。ユーザーごとの値は以下に属します
[ブートストラップ](bootstrap.md#inference_headers)。

<a id="auto-connect"></a>
## 自動接続

デフォルト: プロバイダーのすべてのフィールドが設定されている場合、ユーザーは接続フォームをスキップします
そしてチャットに直接着陸します。質問: 代わりにフォームを最初に見たほうがよいでしょうか
(事前入力、ワンクリック)?はい→`auto_connect=0`。

<a id="allow-claudeai-sign-in"></a>
## Claude.ai のサインインを許可する

企業向けの設定キーが一つでもある場合、ユーザーは企業向けの
接続画面へ進み、Claude.aiサインインへ戻る**Back**ボタンは非表示になります。
(`allow_1p=0`、デフォルト)。 **戻る** ボタンを保持するには、`allow_1p=1` を設定します。

<a id="disabled-features"></a>
## 無効化された機能

`disabled_features`は、管理者がユーザーに利用させない機能の識別名を
カンマで区切った一覧です。識別名は`<domain>.<action>`形式です。現時点の対応は次のとおりです。

| 識別名 | 効果 |
|---|---|
| `skills.authoring` | スキルの作成、編集、アップロードをブロックします (作成/更新ツール、`/skillify`、`.skill` アップロード + ドラッグ ドロップ、スキル編集 UI)。管理者がプロビジョニングしたスキルの実行には影響しません。 |
| `thumbs` | 応答フィードバック (親指を立てる/下げる、およびフォローアップのプロンプト) をブロックします。 |
| `addin.access` | キル スイッチ — アドインは実行を拒否します。ほとんどの場合、ドキュメント `resource` が必要です。 [アクセス ポリシー](access-policies.md) を使用します。 |
| `file.upload` | 会話へのファイルの添付をブロックします。同じです。通常は `resource` によってスコープされます。 |
| `web_search` | ネイティブの web_search および web_fetch サーバー ツール (それ以外の場合、クエリは Anthropic のサードパーティ検索プロバイダーに送信されます) とユーザー側の Web 検索トグルを削除します。コードの実行には影響しません。 [`mcp_servers`](#mcp_servers) と組み合わせて、独自のネットワーク内検索ツールを置き換えます。ネイティブ検索が無効になっている場合、モデルは接続したツールを使用します。 |

```bash
disabled_features='skills.authoring'
```

不明なスラッグは無視されます (前方互換性があります)。ここで設定すると 1 つが適用されます
組織全体のポリシー。ユーザーごとのポリシーは [bootstrap](bootstrap.md#disabled_features) に属します
(JSON 配列) または拡張属性 (カンマ区切り)。

<a id="available_models"></a>
## 利用可能なモデル

`available_models`はモデル選択欄を**上書き**します。設定すると、ユーザーに表示されるのは
一覧にあるモデルだけで、順序も一覧どおりです。廃止された
`disabled_models`／`additional_models`の組合せに代わる設定です。
追加・削除分だけではなく、ユーザーに残すべきすべてのバックエンドモデルを
含めてください。上書きであるためです。

2 つの形式:

```bash
# comma-separated ids
available_models='claude-opus-4-8,claude-sonnet-5'

# JSON, when picker labels matter — an array of ids and/or {id, label} objects
available_models='[{"id":"claude-opus-4-8","label":"Opus 4.8"},"claude-sonnet-5"]'
```

未設定 (または空) は、ピッカーが変更されていないことを意味します。ここで設定すると適用されます
組織全体。ユーザーごとのポリシーは [bootstrap](bootstrap.md#available_models) に属します。

<a id="access_policies"></a>
## アクセスポリシー

`access_policies` は、`disabled_features` (JSON) の IAM 形式の後継です。
アドイン機能を制御する許可/拒否ステートメントの配列:

- **`resource`なし**：`disabled_features`の項目とまったく同じく、
  ステートメントは全体に適用され、全員に対して無効化します。
- **`resource`あり**：Purviewの機密ラベル、または開いている文書の場合はファイルパスで
  識別した、一致する文書だけに規則を適用します。
  極秘文書・制限付き共有上でアドイン自体を禁止したり、
  制限対象のOffice/PDFファイルの添付を拒否したりできます。

`disabled_features` のすべての機能に加え、条件、許可リスト、および
ステートメントごとの帰属。通常、これを構築するにはラベル GUID を取得する必要があります。
Purview から取得できるため、ガイド付きコマンドを使用します。
[アクセス ポリシー](access-policies.md)。次に、結果をもう 1 つのキーとして渡します。

```bash
access_policies='[{"effect":"deny","action":"addin.access","resource":{"type":"open_file","identifiers":[{"type":"mip_label_guid","equals":"<guid>"}]}}]'
```

マニフェスト/ブートストラップのみ - 配列は Entra 拡張属性に適合しません。

<a id="version"></a>
## バージョン

M365管理センターは`<Id>`と`<Version>`でキャッシュし、同じ
バージョンの再アップロードは黙って無視します。スクリプトが`manifest.xml`を書き込んだら、
既存の配備を置き換えるか確認します。置き換える場合は`<Version>`の
第四要素を最後に配備した値より大きくします。初回なら
テンプレートのバージョンをそのまま使えます。

<a id="run"></a>
## 実行

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" office manifest.xml \
  gcp_project_id=<value> \
  gcp_region=<value> \
  auto_connect=0 \
  ...

# and if they're also deploying Outlook:
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" outlook manifest-outlook.xml \
  <same provider keys as above> \
  graph_client_id=<value>   # only if NOT using Anthropic's app via the consent URL
```

スクリプトはキー名 (不明なキーはハード失敗) とシェイプヒント値を検証します。
(警告はしますが、ブロックはしません。インフラは異なるように見える可能性があります)。

<a id="validate"></a>
## 検証する

```bash
npx --yes office-addin-manifest validate manifest.xml
```

検証に合格しても、M365 Admin Center がアップロードを拒否または無視する場合は、
以下の症状に当てはまります。 `manifest.xml` を直接編集して、再検証してください。

| 症状 | 修正 |
|---|---|
| 「この ID のアドインはすでに存在します」 | `<Id>` 内のテキストを新しい UUID に置き換えます。テンプレートにはマーケットプレイス インストールの ID が含まれます。 |
| 再アップロードは承認されましたが、何も変わりません | M365 は ID + バージョンごとにキャッシュされます。 `<Version>` を上位 4 番目のセグメント (例: `1.0.0.9` → `1.0.0.10`) に編集し、再検証します。 |
| Excelだけが必要（PowerPointは不要） | `Presentation`の`<Host>`要素を削除します。**並列の二つの一覧**があり、最上位の`<Hosts>`では`Name="Presentation"`、`<VersionOverrides>`配下では`xsi:type="Presentation"`です。両方を削除しないと不整合になります。`xsi:type`のブロックは複数行なので、`<Host xsi:type="Presentation">...</Host>`全体を削除します。 |
| Excel/PPT のみが必要であり、Outlook は必要ありません | 削除するものはありません - Outlook は別のファイルです。ただ生成しないでください。 |
