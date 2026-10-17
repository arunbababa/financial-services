---
description: Setup wizard — provision Vertex/Bedrock/Foundry/gateway, admin consent, generate manifest(s)
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/setup.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：セットアップ ウィザード - Vertex/Bedrock/Foundry/ゲートウェイのプロビジョニング、管理者の同意、マニフェストの生成

<a id="claude-in-office--direct-cloud-setup"></a>
# Claude in Office — 自社クラウドへの直接接続設定

企業の管理者に、Claude OfficeアドインをAnthropic APIではなく
自社のクラウドへ接続するための設定を案内します。成果物はカスタマイズした
`manifest.xml`で、管理者がM365管理センターから配備します。

**何よりも前に:** セットアップ ログは次の場所に保存されます。
`~/Desktop/claude-for-msft-365-install-setup.md`を使います（`~`は利用OSに合わせて解決）。
既存ファイルがあれば先に読み、前回の続きなら完了済みの
手順を省略できます。`## Run — <timestamp>`節を新設し、作業しながらコマンドと
取得した出力（ID、URL）を追記します。

**Node.js を確認する** — ステップ 4 と 6 は、`node` および `npx` をシェルアウトします。走る
`node --version`。見つからない場合は、**インストールする前に尋ねてください** - それは彼らの
機械。彼らが「はい」と言ったら、`brew install node` (mac) / `winget install OpenJS.NodeJS`
(win) / パッケージマネージャーが何であっても。 「いいえ」の場合は、ここで終了します。

**管理者から値を受け取る場合**（コンソールからコピーしたID、URL、シークレット等）は、
AskUserQuestionを使いません。それは選択肢用のUIであり、受け取るのは
文字列です。「取得したClient IDを貼り付けてください」と伝え、
次のメッセージから読み取ります。AskUserQuestionを使うのは実際の分岐
（gatewayかvertexか、ユーザー別か組織共通か）だけです。

<a id="step-1--how-does-the-add-in-reach-claude"></a>
## ステップ 1 — アドインはどのようにしてクロードに到達しますか?

管理者が誤解していることなので、最初にこれを尋ねてください: **すでに実行していますか
LLM ゲートウェイ (LiteLLM、Portkey、Kong など)?**

- **はい → `gateway`.** ゲートウェイが Vertex または Bedrock にルーティングしている場合でも
  フード — アドインは、Google や AWS ではなく、*ゲートウェイ* と通信します。あなた
  必要なのはゲートウェイ URL だけです。
- **いいえ → `vertex` または `bedrock`.** アドインは、
  クラウドプロバイダー。インフラが存在する場所を選択してください。

| パス | それが何を意味するか | プロビジョニング | マニフェストキー |
|---|---|---|---|
| `gateway` | アドイン → ゲートウェイ → (何でも) | なし | `gateway_url` (`/v1/messages` でない場合は + `gateway_api_format`) |
| `vertex` | アドイン → Google Vertex AI、直接 | Google OAuth クライアント | `gcp_project_id`, `gcp_region`, `google_client_id`, `google_client_secret` |
| `bedrock` | アドイン → AWS Bedrock、直接 | IAM OIDC プロバイダー + ロール | `aws_role_arn`, `aws_region` |
| `foundry` | アドイン → Azure AI Foundry、直接 | ファウンドリリソース + API キー | `azure_resource_name`, `azure_api_key` |
| `foundry` (キーレス) | アドイン → Azure AI Foundry、ユーザーごとの Entra サインイン | Foundry リソース + Entra アプリ | `azure_resource_name`, `entra_sso=1`, `graph_client_id`, `entra_scope=https://cognitiveservices.azure.com/.default`, `gateway_auth_source=entra` |

Bedrock およびユーザーごとの構成 (ブートストラップ エンドポイントまたは拡張属性) が必要です
`entra_sso=1` — アドインは認証のためにユーザーの Entra ID トークンを取得します
それらの流れ。 [マニフェスト](manifest.md) の Entra SSO セクションを参照してください。

<a id="step-1b--which-office-apps"></a>
## ステップ 1b — どの Office アプリですか?

質問: **Excel/Word/PowerPoint、Outlook、または両方?** Outlook は別のものです。
マニフェストには追加の前提条件が 1 つあります。

Outlook を導入している場合:
- **Bedrock は現在 Outlook でサポートされていません。** `bedrock` を選択した場合
  ステップ 1 では、Outlook は現時点では対象外です。`office` のみを生成します。
  マニフェストします。
- **Microsoft Graph 管理者の同意が必要です。** 実行
  [同意](consent.md#outlook--microsoft-graph-consent) — 全体管理者が開きます
  1 つの URL を選択し、「同意する」をクリックします。マニフェストを生成する前にこれを実行してください。
  Anthropic のアプリを使用しているかどうかを尋ねます (`graph_client_id` は必要ありません)。
  独自の Entra アプリ (`graph_client_id` をキャプチャ)。

以下の一致するセクションに分岐します。

---

<a id="vertex-ai"></a>
## Vertex AI

<a id="1a-prerequisites"></a>
### 1a.前提条件

管理者に確認してください:
- GCP プロジェクト ID (これを知っておく必要があります)
- クロード モデル クォータのあるリージョン (通常は `us-east5`)

<a id="1b-create-the-oauth-client"></a>
### 1b. OAuthクライアントを作成する

この操作に対応する`gcloud`コマンドはありません。プロジェクトIDを置き換えて
コンソールのリンクを開き、手順を案内します。管理者がClient IDとシークレットを貼り付けて返します。

> 開く: `https://console.cloud.google.com/apis/credentials?project=<PROJECT_ID>`
> → **認証情報の作成** → **OAuth クライアント ID**
> - アプリケーションの種類: **Web アプリケーション**
> - 名前: `Claude for Office`
> - 承認されたリダイレクト URI: `https://pivot.claude.ai/auth/callback`
> → **作成** → **クライアント ID** と **クライアント シークレット** をコピーします

そこにいる間に Vertex API を有効にします。

```bash
gcloud services enable aiplatform.googleapis.com --project=<PROJECT_ID>
```

キャプチャ: `gcp_project_id`、`gcp_region`、`google_client_id`、`google_client_secret`。

[ステップ3](#step-3--decide-whats-org-wide-vs-per-user)へ進みます。VertexはEntraではなく
Google OAuthを使うため、ユーザー別設定も使う場合を除き、管理者同意は不要です。
ユーザー別設定を選んだ場合は、ステップ3で決めてからステップ2へ戻ります。

---

<a id="bedrock"></a>
## Bedrock

<a id="1a-prerequisites-1"></a>
### 1a.前提条件

管理者に確認してください:
- AWS アカウント ID とクロード モデル アクセスのあるリージョン (通常は `us-east-1`)
- Azure テナント ID (Entra 管理センターから、または `az account show --query tenantId`)
- `aws` CLI がターゲット アカウントに対して構成されました

<a id="1b-create-oidc-provider--role"></a>
### 1b. OIDC プロバイダー + ロールの作成

`aws iam` 呼び出しが 3 回。信頼ポリシーの `aud` 条件はセキュリティです。
境界 — Claude アドイン用に Azure で作成されたトークンのみがこの役割を引き受けることができます。

テナント ID とリージョンを次のように置き換えます。

```bash
TENANT_ID="<their-azure-tenant-guid>"
CLAUDE_APP_ID="c2995f31-11e7-4882-b7a7-ef9def0a0266"
AWS_REGION="us-east-1"
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
ISSUER="login.microsoftonline.com/${TENANT_ID}/v2.0"

# OIDC identity provider. Thumbprint is required by the API; AWS validates
# major IdPs via its own trust store, but the param can't be omitted.
THUMBPRINT=$(openssl s_client -servername login.microsoftonline.com \
  -connect login.microsoftonline.com:443 </dev/null 2>/dev/null \
  | openssl x509 -fingerprint -sha1 -noout | cut -d= -f2 | tr -d ':')

aws iam create-open-id-connect-provider \
  --url "https://${ISSUER}" \
  --client-id-list "${CLAUDE_APP_ID}" \
  --thumbprint-list "${THUMBPRINT}"

PROVIDER_ARN="arn:aws:iam::${ACCOUNT}:oidc-provider/${ISSUER}"

# Role with trust policy gated on aud.
aws iam create-role --role-name ClaudeBedrockAccess \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"Federated": "'"${PROVIDER_ARN}"'"},
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {"'"${ISSUER}"':aud": "'"${CLAUDE_APP_ID}"'"}
      }
    }]
  }'

# Bedrock invoke permissions.
aws iam put-role-policy --role-name ClaudeBedrockAccess \
  --policy-name BedrockInvoke \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.*",
        "arn:aws:bedrock:*:'"${ACCOUNT}"':inference-profile/us.anthropic.*"
      ]
    }]
  }'

echo "aws_role_arn: arn:aws:iam::${ACCOUNT}:role/ClaudeBedrockAccess"
```

`create-open-id-connect-provider` エラーが `EntityAlreadyExists` で発生した場合、
その発行者のプロバイダーはすでに存在します。それは問題ありません。ロールはそれを信頼します。
ARN は決定的です (`arn:aws:iam::<account>:oidc-provider/<issuer>`)。

キャプチャ: `aws_role_arn`、`aws_region`。生成時に `entra_sso=1` を追加します。
マニフェスト — Bedrock には、STS Web ID として Entra ID トークンが必要です。

[ステップ 2](#step-2--azure-admin-consent) に進みます。

---

<a id="gateway"></a>
## ゲートウェイ

プロビジョニングはありません。ゲートウェイのベース URL (LiteLLM、Portkey など) と
トークン。トークンがユーザーごとに異なる場合は、[ステップ 5](#step-5--per-user-config) に進みます。
マニフェストの代わりに。

キャプチャ: `gateway_url`、`gateway_token`。

**API形式。** ゲートウェイがAnthropicの`/v1/messages` APIを公開するのか、
Bedrockの`/model/{id}/invoke…`やVertexの
`…:rawPredict`へのパススルーなのかを確認します。ほとんどはAnthropic形式です。
LiteLLM/Portkey/Kongも既定でこれを使い、統一した`/v1/messages`がゲートウェイの目的だからです。
上流の通信形式を維持する薄いプロキシである場合だけ、
`gateway_api_format`を`bedrock`または`vertex`にします。`vertex`なら、
`gcp_project_id` (GCP プロジェクト) および `gcp_region` (通常は `us-east5`) —
これらは、アドインが構築する URL 内のパス セグメントです。 `gateway_url` をポイントします
パススルーパス、例: `https://litellm.acme.com/bedrock` または
`…/vertex_ai/v1`.

**認証ヘッダー スキーム。** アドインはトークンを `x-api-key: <token>` として送信します。
デフォルト — これは、LiteLLM、Portkey、および Kong がそのまま使用できるものです。もし
ゲートウェイは代わりに `Authorization: Bearer <token>` を期待します (共通)
カスタム/エンタープライズ ゲートウェイ)、`gateway_auth_header=authorization` を設定します。もし
よくわからない場合は、`x-api-key` を使用してステップ 6 のスモーク テストを実行してください。
まず、ゲートウェイ ログに「Authorization ヘッダーがない」という 401 が表示されるということは、
`authorization`が必要です。

[ステップ 3](#step-3--decide-whats-org-wide-vs-per-user) に進みます。ゲートウェイ認証
Entra ではなくトークンベースであるため、選択しない限り管理者の同意は必要ありません
ユーザーごとの設定に追加します (この場合、ステップ 3 で決定した後、ステップ 2 に戻ってください)。

---

<a id="azure-ai-foundry"></a>
## Azure AI Foundry

<a id="1a-prerequisites-2"></a>
### 1a.前提条件

管理者に確認してください:
- 少なくとも 1 つのクロード モデルがデプロイされた Azure AI Foundry リソース
- リソース名 (エンドポイント URL のサブドメイン — 例: `contoso-foundry`)
  `https://contoso-foundry.services.ai.azure.com` から）

<a id="1b-get-the-api-key"></a>
### 1b. APIキーを取得する

Azure ポータルでリソースを開き、**キーとエンドポイント** → コピー
**キー 1**。アドインは、どのクロード モデルがデプロイされているかを自動検出します。
リソースなので、ここではモデル構成は必要ありません。

キャプチャ: `azure_resource_name`、`azure_api_key`。

<a id="1c-keyless-alternative-per-user-entra-sign-in"></a>
### 1c.キーレスの代替手段: ユーザーごとの Entra サインイン

リソースキーの配布を避けるにはキーを使わず、各ユーザーに自分のEntra IDで
認証してもらいます。APIキーの代わりに次を取得します。
`azure_resource_name`、`entra_sso=1`、`graph_client_id` (独自の Entra アプリ)、
`entra_scope=https://cognitiveservices.azure.com/.default`、および
`gateway_auth_source=entra`。これには、Azure で構成された Entra アプリが必要です
Cognitive Services `user_impersonation` 権限と各ユーザーに付与された
リソースに対する **Cognitive Services ユーザー** ロール — [entra-app](entra-app.md) を参照してください。

[ステップ 3](#step-3--decide-whats-org-wide-vs-per-user) に進みます。キーベース
ユーザーごとの構成もオプトインしない限り、Foundry 認証には管理者の同意は必要ありません。
キーレス Entra パスには常に Cognitive Services での管理者の同意が必要です
許可（ステップ 2）。

---

<a id="step-2--azure-admin-consent"></a>
## ステップ 2 — Azure 管理者の同意

**`entra_sso=1`の場合だけ必要です。** Bedrock（Entraトークンを
STSのWebアイデンティティに使用）、または拡張属性・bootstrapによるユーザー別設定が該当します。
どちらでもない場合は、ステップ3へ進みます。

`${CLAUDE_PLUGIN_ROOT}/commands/consent.md` を読み、それに従ってください。

<a id="step-3--decide-whats-org-wide-vs-per-user"></a>
## ステップ 3 — 組織全体とユーザーごとの区別を決定する

アドインはユーザー別の拡張属性を先に読み、なければマニフェストのパラメータへ
フォールバックします。どのキーもいずれかの層に置けるという前提で、**ステップ1で
取得した値のうち、ユーザーごとに異なるものがあるか**を確認します。

具体的に質問してください。自分でマッピングさせないでください。
- ゲートウェイ: それは全員に 1 つの URL ですか? 1 つのトークンですか、それともユーザーごとに 1 つのトークンですか?
- Vertex：全員同じプロジェクトか。同じリージョンか、一部のユーザーには
  データ所在地の要件に応じて別のリージョンが必要か。
- Bedrock: 全員に同じ役割、それともチーム固有の役割?

| 答え | スプリット |
|---|---|
| 何も変わらない | すべて→マニフェスト。ステップ 5 をスキップします。 |
| ユーザーごとに一意 (ゲートウェイ トークンなど) | 一意のキー → ステップ 5、残り → マニフェスト。 |

ステップ 4 とステップ 5 がそれぞれそのサブセットを認識できるように、分割をセットアップ ログに書き込みます。

<a id="step-4--generate-the-manifest"></a>
## ステップ 4 — マニフェストを生成する

`${CLAUDE_PLUGIN_ROOT}/commands/manifest.md` を読み、それに続けて
ステップ 3 の **組織全体** の値。ステップ 1b でホストごとに 1 つのファイルを生成します。

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" office  manifest.xml         <key>=<value> ...
node "${CLAUDE_PLUGIN_ROOT}/scripts/build-manifest.mjs" outlook manifest-outlook.xml <key>=<value> ...
```

次に、それぞれを検証します。

```bash
npx -y office-addin-manifest validate manifest.xml
npx -y office-addin-manifest validate manifest-outlook.xml
```

<a id="step-5--per-user-config"></a>
## ステップ 5 — ユーザーごとの構成

ステップ3でユーザー別の項目がなければ省略します。ある場合は、渡す値に応じて
方式を選びます。

| 運ぶ | 使用する | 読む |
|---|---|---|
| 1 つまたは 2 つの文字列 — トークン、リージョン | 拡張属性 | `${CLAUDE_PLUGIN_ROOT}/commands/update-user-attrs.md` |
| `mcp_servers`、`skills`、構造化されたもの | ブートストラップエンドポイント | `${CLAUDE_PLUGIN_ROOT}/commands/bootstrap.md` |

属性はユーザーごとに `az rest PATCH` です。作業は少なくなりますが、フラット文字列 ≤256 文字です。
のみ。 Bootstrap はユーザーが構築する HTTPS サービスです。より多くの作業が必要ですが、形状の制限はありません。

<a id="step-6--verify-a-model-is-reachable"></a>
## ステップ 6 — モデルが到達可能であることを確認する

配備前に、**Claude Sonnet 4.5**または
**Claude Opus 4.5**（またはそれ以降）の少なくとも一つが実際に応答することを確認します。
有効化されていないモデルを指すマニフェストも配備自体は成功し、最初のユーザーメッセージで黙って失敗します。

**ゲートウェイ:** 1 トークン リクエストによるプローブ。 200 は機能することを意味します。 404 の意味は、
ゲートウェイはそのモデル名をルーティングしません - 他のモデル名を試すか、確認するよう依頼してください
ゲートウェイ構成。 429 は、認証は機能するが、そのモデルにクォータがないことを意味します — 試してみてください
もう一方。 401/403 はトークンが間違っていることを意味し、これはステップ 1 の問題です。

`gateway_api_format` に一致するカールを選択します。 (Windows: `/dev/null` をスワップ
`NUL`の場合。 `gateway_auth_header=x-api-key` の場合、認証ヘッダー行を
`-H 'x-api-key: <token>'`.)

`gateway_api_format=anthropic` (デフォルト):
```bash
curl -s -o /dev/null -w '%{http_code}\n' "<gateway_url>/v1/messages" \
  -H 'content-type: application/json' -H 'authorization: Bearer <token>' \
  -d '{"model":"claude-sonnet-4-5","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```

`gateway_api_format=bedrock` — モデルはボディではなくパスに挿入されます。
```bash
curl -s -o /dev/null -w '%{http_code}\n' \
  "<gateway_url>/model/anthropic.claude-sonnet-4-5-v1:0/invoke" \
  -H 'content-type: application/json' -H 'authorization: Bearer <token>' \
  -d '{"anthropic_version":"bedrock-2023-05-31","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```

`gateway_api_format=vertex` — モデル、プロジェクト、リージョンはすべて次のパスに含まれます。
```bash
curl -s -o /dev/null -w '%{http_code}\n' \
  "<gateway_url>/projects/<gcp_project_id>/locations/<gcp_region>/publishers/anthropic/models/claude-sonnet-4-5:rawPredict" \
  -H 'content-type: application/json' -H 'authorization: Bearer <token>' \
  -d '{"anthropic_version":"vertex-2023-10-16","max_tokens":1,"messages":[{"role":"user","content":"hi"}]}'
```

**Vertex：** モデルの有効化は画面操作です。EULA同意用のAPIはありません。
Model Gardenを開き、対象リージョンで少なくとも一モデルが**Enabled**であり、
「Request access」ではないことを確認します。

> `https://console.cloud.google.com/vertex-ai/publishers/anthropic?project=<PROJECT_ID>`

「Request access」なら、利用者が手順を進めて規約に同意し、
有効化を待ちます。確認が取れるまでAPIは呼び出しません。

**Bedrock:** 同じ制約 — モデルへのアクセス許可には API がありません。モデルを開く
ページにアクセスし、少なくとも 1 つのクロード 4.5 以降のモデルに **アクセスが許可されました** と表示されていることを確認してください
(「リクエスト可能」ではありません):

> `https://console.aws.amazon.com/bedrock/home?region=<aws_region>#/modelaccess`

「リクエスト可能」と表示されている場合は、リクエストし、条件を受け入れ、許可を待ちます。
(通常は数分、場合によってはそれ以上かかる場合もあります)。

検証したモデル名をセットアップログへ記録します。対象の接続方式に応じて、
200応答、「Enabled」、「Access granted」のいずれかが
確認できるまで進んではいけません。

<a id="step-7--deploy"></a>
## ステップ 7 — 導入

複数画面にわたるアップロード手順を案内します。ユーザー割当ての画面には、
明示的な判断が必要です。

> 開く: `https://admin.cloud.microsoft/?#/Settings/IntegratedApps`
> → **カスタムアプリをアップロード**
> - アプリの種類: **Office アドイン**
> - 方法を選択します: **デバイスからマニフェスト ファイル (.xml) をアップロード** → `manifest.xml` を選択します
> - アップロード時に検証されます。ここでエラーが発生した場合は、ステップ 4 の `npx office-addin-manifest validate` でエラーが検出されるはずです。それを再実行します。

**ユーザー画面** — 決定点:
- ステップ 5 がスキップされた場合 (ユーザーごとに何も変わりません) → **組織全体** で問題ありません。
- ステップ5でユーザー別拡張属性を書き込んだなら、PATCHした対象と厳密に一致する
  **Specific users/groups**へ割り当てます。それ以外の人には設定がない状態でアドインが開きます。
- 最初にデプロイしますか? **私だけ**またはパイロット グループから始めて、機能することを確認してから、
  広げる。再デプロイしなくても、後で割り当てを変更できます。

> → **権限を受け入れる** → **展開を完了する**

ユーザーへの伝達には最大 24 時間かかります (通常はそれよりも早くなります)。アドイン
Excel/Word/PowerPoint の **[ホーム] → [アドイン]** に表示されます。

最終的なマニフェスト パスと割り当てスコープをセットアップ ログに追加します。終わり。
