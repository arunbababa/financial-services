> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/entra-app.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="register-your-own-entra-app"></a>
# 独自の Entra アプリを登録する

いくつかのマニフェスト構成では、Anthropic既定のマルチテナントアプリではなく、
**自社の**テナントでEntra（Azure AD）アプリを登録する必要があります。
トークンの`aud`が自社管理のリソースと一致する必要がある場合や、テナントが
Anthropicのアプリのないソブリンクラウドにある場合です。このページに
登録手順を集約しています。機能ごとの文書からこのページへリンクし、
権限表のどの行を使うかを示します。

これは、次のいずれかを設定する場合に必要です。

| マニフェストキー | なぜ独自のアプリを作るのか |
|---|---|
| `graph_client_id` (Outlook) | グラフの権限は、Anthropic の権限ではなく、あなたのアプリに対して同意されます。 |
| `entra_scope` | アクセストークンの対象（audience）が*自社の*APIリソースでなければならない |
| `gateway_auth_source=entra` | ゲートウェイまたはFoundryリソースが、そのリソースを対象とするトークンを検証する |
| `graph_cloud` ≠ `global` | Anthropic のアプリは商用クラウドにのみ存在します |

<a id="register-the-app"></a>
## アプリを登録する

[エントラ管理センター](https://entra.microsoft.com) → *アプリ登録* →
*新規登録*を選び、シングルテナントにします。最も単純なのは、一つのアプリが
クライアント（アドインがそのアプリとしてサインイン）とリソース（バックエンドがそのアプリを
対象とするトークンを検証）の両方を担う構成です。社内方針で必要なら二つに分けます。

<a id="1-redirect-uris"></a>
### 1. リダイレクト URI

*認証* → *プラットフォームの追加* → **シングルページ アプリケーション** → 追加
**両方**:

| URI | 使用者 |
|---|---|
| `brk-multihub://pivot.claude.ai` | [NAA ブローカー](https://learn.microsoft.com/office/dev/add-ins/develop/enable-nested-app-authentication-in-your-add-in) — デスクトップ Office および Outlook Web。これが欠落しています → サインイン時に `AADSTS50011`。 |
| `https://pivot.claude.ai/msal-redirect.html` | SPA フォールバック - Web 用 Office 上の Excel/Word/PowerPoint。NAA ブリッジを挿入しません。 |

どちらも SPA プラットフォーム (Web、モバイル/デスクトップではありません) の下に置かれます。

<a id="2-permissions--api-setup"></a>
### 2. 権限/APIの設定

ここで設定する内容は、トークンの目的によって異なります。

| ユースケース | 設定する |
|---|---|
| **Outlook（Graph）** | *API permissions* → *Microsoft Graph* → Delegated → `Mail.ReadWrite`、`Calendars.Read`、`People.Read`、`User.Read`、`offline_access`。 |
| **ゲートウェイ/ブートストラップ認証** (`entra_scope`、`gateway_auth_source=entra`) | *API を公開* → アプリケーション ID URI `api://<app-guid>` を設定 → *スコープを追加* (例: `access_as_user`、管理者の同意が有効)。次に、*API 権限* → *マイ API* → そのスコープを委任された権限として追加します (単一アプリ トポロジでは、アプリをそれ自体に)。 |
| **ファウンドリダイレクト、キーレス** (`gateway_auth_source=entra` + `azure_resource_name`) | *API アクセス許可* → *Azure Cognitive Services* → 委任 → `user_impersonation`。 *API の公開* ステップはありません。トークンは独自のアプリではなく Azure の `https://cognitiveservices.azure.com` に対してオーディエンスされるため、`entra_scope=https://cognitiveservices.azure.com/.default` を設定します。また、各ユーザーに Foundry リソースに対する **Cognitive Services ユーザー** ロールを付与します (Azure ポータル → リソース → *アクセス制御 (IAM)*)。 |
| **Bedrock WIF** (`aws_role_arn`) | API 権限は必要ありません。ID トークンのみが Web ID です。 |

どの場合も最後に、*API permissions* → **Grant admin consent for
&lt;tenant&gt;**を実行します。これがないと全ユーザーに同意画面が表示されます
（ユーザー自身による同意が無効なら、アクセスを阻止されます）。

<a id="3-token-version"></a>
### 3. トークンのバージョン

上記の *API の公開* を設定した場合のみ: アプリの *マニフェスト* で、
`"accessTokenAcceptedVersion": 2`。未設定のままにすると、Entra は v1.0 へのアクセスを発行します
トークン (`/v2.0` なしの `iss`、`preferred_username` なし)、ほとんどの JWT
ミドルウェアはデフォルトで拒否します。

<a id="what-your-backend-validates"></a>
## バックエンドが検証するもの

`entra_scope` / `gateway_auth_source=entra` の場合、アドインのアクセス トークン
`Authorization: Bearer` が伝送するように送信します。

| クレーム | 期待される |
|---|---|
| `iss` | `https://login.microsoftonline.com/<tenant-id>/v2.0` |
| `aud` | アプリケーション ID URI (`api://<app-guid>`) |
| `scp` | 公開したスコープ (スペース区切り) |
| JWKS | `https://login.microsoftonline.com/<tenant-id>/discovery/v2.0/keys` |

**Foundryへ直接接続するキーレス構成**では、自社のバックエンドはなく、Azureが
トークンを検証します。`aud`は`https://cognitiveservices.azure.com`、`scp`は
`user_impersonation`です。Azureは署名とaudienceを確認し、リソースに対してユーザーが持つ
**Cognitive Services User**ロールで呼出しを認可します。この構成では
*Expose an API*も`accessTokenAcceptedVersion`も設定しません。

ロールは必ず**Cognitive Services User**です。モデルの直接推論用のデータプレーンロールです。
*Cognitive Services OpenAI User*（OpenAIモデル専用）でも、
*Foundry User*／*Azure AI User*（Foundryのエージェント・プロジェクト用プレーンの
名称変更されたロールで、別のデータプレーン）でもありません。`user_impersonation`は
アドインのユーザーごとの対話的サインインに使う委任権限です。
サーバー側で行うon-behalf-ofのトークン交換ではありません。Azure AIリソースはその交換を
サポートしません。

<a id="gcc-high--dod--21vianet"></a>
## GCC High / DoD / 21Vianet

手順は同じですが、ポータルとエンドポイントが異なります。Microsoftの各ナショナルクラウドの
間で、アプリが複製されることはありません。

- **登録先** [`portal.azure.us`](https://portal.azure.us) (米国政府) または
  [`portal.azure.cn`](https://portal.azure.cn) (21Vianet)、商用ではありません
  ポータル。
- **リダイレクト URI** は変更されていません - `brk-multihub://pivot.claude.ai` および
  `https://pivot.claude.ai/msal-redirect.html`。アドインは、
  すべてのクラウドで同じドメイン。
- **マニフェスト** — `graph_cloud=us-gov-high` (または `us-gov-dod`、`china`) を追加します
  [ソブリン クラウド](manifest.md#sovereign--national-clouds-gcc-high-dod-21vianet)
  テーブル。
- **管理者同意のURL**は、ソブリンクラウドの認証機関を使います。
  `https://login.microsoftonline.us/<tenant-id>/adminconsent?client_id=<app-id>`
- **バックエンド検証** — トークンの `iss` と JWKS は `.us` ホストを使用します。
  `https://login.microsoftonline.us/<tenant-id>/v2.0` および
  `https://login.microsoftonline.us/<tenant-id>/discovery/v2.0/keys`. A
  `.com` に固定されたバリデータはすべてのリクエストを拒否します。どの AWS にも同じことが当てはまります
  チェーン内の OIDC ID プロバイダー。

<a id="troubleshooting"></a>
## トラブルシューティング

**`AADSTS50011` (リダイレクト URI の不一致)** — 上記の 2 つの URI の 1 つは次のとおりです。
存在しないか、間違ったプラットフォーム (SPA である必要があります) で追加されました。

**Outlook for Macの`Tag: 9n156`**：ホストの認証ブローカーが処理を完了できません。
ほとんどは、ソブリンクラウドのアカウントで商用クラウド登録のアプリへアクセスしている場合です。
対処は`portal.azure.us`で登録し、`graph_cloud`を設定することです。アプリが
既に正しいクラウドにあるなら、条件付きアクセスを確認します。非推奨の*Require
approved client app*の許可条件はNAAを阻止します。ダイアログのCorrelation Idは、
Anthropicのログではなく自社Entraのサインインログで調べられます。

**`AADSTS65001` (同意が必要)** — *管理者の同意を与える* がクリックされなかった、または
同意が付与された後に権限が追加されました（再付与）。
