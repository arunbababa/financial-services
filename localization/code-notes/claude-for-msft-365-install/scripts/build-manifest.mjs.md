# claude-for-msft-365-install/scripts/build-manifest.mjs の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/scripts/build-manifest.mjs)

### claude-for-msft-365-install/scripts/build-manifest.mjs:2

原文：

```text
Fetches the canonical add-in manifest and writes a customized copy with your
```

日本語：

正規のアドインマニフェストを取得し、組織の設定を組み込んだコピーを書き出す。


### claude-for-msft-365-install/scripts/build-manifest.mjs:3

原文：

```text
org's config baked into the taskpane URL: sensitive settings after #, other settings after ?.
```

日本語：

組織の設定はタスクペインURLに埋め込む。機密設定は#の後、その他の設定は?の後に置く。


### claude-for-msft-365-install/scripts/build-manifest.mjs:5

原文：

```text
Usage: node build-manifest.mjs <office|outlook> <out.xml> key=value [key=value ...]
```

日本語：

`Usage: node build-manifest.mjs <office|outlook> <out.xml> key=value [key=value ...]`

実行構文。officeまたはoutlook、出力XML、key=value形式の設定を指定する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:6

原文：

```text
Example: node build-manifest.mjs office acme.xml gcp_project_id=acme gcp_region=us-east5
```

日本語：

`Example: node build-manifest.mjs office acme.xml gcp_project_id=acme gcp_region=us-east5`

office用マニフェストをacme.xmlへ出力する例。


### claude-for-msft-365-install/scripts/build-manifest.mjs:15

原文：

```text
Every URL slot Office reads from must carry the same params. Outlook's MailApp
```

日本語：

Office が読み取るすべての URL スロットには、同じパラメータが含まれている必要があります。 Outlookのメールアプリ


### claude-for-msft-365-install/scripts/build-manifest.mjs:16

原文：

```text
schema repeats Taskpane.Url across V1_0 and V1_1 VersionOverrides, hence /g.
```

日本語：

スキーマでは、V1_0とV1_1のVersionOverridesにTaskpane.Urlが繰り返し登場するため、/gを使う。


### claude-for-msft-365-install/scripts/build-manifest.mjs:19

原文：

```text
Sensitive settings; emitted in the URL fragment so they aren't part of the request.
```

日本語：

機密性の高い設定。 URL フラグメントで発行されるため、リクエストの一部ではありません。


### claude-for-msft-365-install/scripts/build-manifest.mjs:39

原文：

```text
URLSearchParams joins pairs with `&`; XML attribute values need it escaped.
```

日本語：

URLSearchParamsはキーと値の組を`&`で連結する。XML属性値ではこの文字をエスケープする必要がある。


### claude-for-msft-365-install/scripts/build-manifest.mjs:44

原文：

```text
`url` is the template's taskpane URL as it appears in the XML (already escaped,
```

日本語：

`url` は、XML に表示されるテンプレートのタスクペイン URL (すでにエスケープされています)


### claude-for-msft-365-install/scripts/build-manifest.mjs:45

原文：

```text
already carrying ?m=<tag>), so only the appended parts are escaped here.
```

日本語：

すでに ?m=<tag> を保持しているため、ここでは追加部分のみがエスケープされます。


### claude-for-msft-365-install/scripts/build-manifest.mjs:56

原文：

```text
Recognized config keys. `pattern` is a shape hint — mismatches warn but don't block
```

日本語：

認識する設定キー。`pattern`は形式の目安であり、不一致は警告するが処理は止めない。


### claude-for-msft-365-install/scripts/build-manifest.mjs:57

原文：

```text
(your infra may look different). `secret` keys warn louder: the manifest is an
```

日本語：

（インフラによって形式が異なる可能性があるため。）`secret`キーには、より強い警告を出す。マニフェストは


### claude-for-msft-365-install/scripts/build-manifest.mjs:58

原文：

```text
org-wide file and its URL can land in deploy logs; per-user secrets typically go
```

日本語：

組織全体で使うファイルであり、そのURLがデプロイログに残ることもある。ユーザー個別のシークレットは通常、


### claude-for-msft-365-install/scripts/build-manifest.mjs:59

原文：

```text
in Azure extension attributes instead.
```

日本語：

代わりにAzureの拡張属性へ格納する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:61

原文：

```text
GCP project ID
```

日本語：

GCP プロジェクト ID


### claude-for-msft-365-install/scripts/build-manifest.mjs:62

原文：

```text
GCP region, e.g. us-east5 or global
```

日本語：

GCPリージョン（例：us-east5、global）


### claude-for-msft-365-install/scripts/build-manifest.mjs:63

原文：

```text
OAuth 2.0 client ID
```

日本語：

OAuth 2.0 クライアント ID


### claude-for-msft-365-install/scripts/build-manifest.mjs:64

原文：

```text
OAuth 2.0 client secret
```

日本語：

OAuth 2.0 クライアント シークレット


### claude-for-msft-365-install/scripts/build-manifest.mjs:67

原文：

```text
e.g. arn:aws:iam::123456789012:role/ClaudeBedrockAccess
```

日本語：

例: arn:aws:iam::123456789012:role/ClaudeBedrockAccess


### claude-for-msft-365-install/scripts/build-manifest.mjs:69

原文：

```text
e.g. us-east-1
```

日本語：

例：us-east-1


### claude-for-msft-365-install/scripts/build-manifest.mjs:76

原文：

```text
From Azure Portal → your Foundry resource → Keys and Endpoint → KEY 1
```

日本語：

Azure Portal → Foundry リソース → キーとエンドポイント → KEY 1 から


### claude-for-msft-365-install/scripts/build-manifest.mjs:82

原文：

```text
HTTPS base URL
```

日本語：

HTTPSベースURL


### claude-for-msft-365-install/scripts/build-manifest.mjs:83

原文：

```text
gateway API key
```

日本語：

ゲートウェイAPIキー


### claude-for-msft-365-install/scripts/build-manifest.mjs:84

原文：

```text
auth header scheme (default: x-api-key)
```

日本語：

認証ヘッダー スキーム (デフォルト: x-api-key)


### claude-for-msft-365-install/scripts/build-manifest.mjs:85

原文：

```text
anthropic | bedrock | vertex
```

日本語：

`anthropic | bedrock | vertex`（指定可能なプロバイダー識別子）


### claude-for-msft-365-install/scripts/build-manifest.mjs:90

原文：

```text
JSON array of {url, label, headers?, discover?}
```

日本語：

`{url, label, headers?, discover?}`を要素とするJSON配列


### claude-for-msft-365-install/scripts/build-manifest.mjs:91

原文：

```text
JSON object of extra headers to attach to every model request
```

日本語：

すべてのモデルリクエストに添付する追加ヘッダーの JSON オブジェクト


### claude-for-msft-365-install/scripts/build-manifest.mjs:92

原文：

```text
HTTPS endpoint returning per-user config
```

日本語：

ユーザーごとの構成を返す HTTPS エンドポイント


### claude-for-msft-365-install/scripts/build-manifest.mjs:93

原文：

```text
OTLP/HTTP traces collector URL
```

日本語：

OTLP/HTTP トレースコレクターの URL


### claude-for-msft-365-install/scripts/build-manifest.mjs:94

原文：

```text
comma-separated k=v pairs for the OTLP exporter
```

日本語：

OTLP エクスポータのカンマ区切りの k=v ペア


### claude-for-msft-365-install/scripts/build-manifest.mjs:97

原文：

```text
comma-separated k=v pairs added to the OTEL Resource (same format as OTEL_RESOURCE_ATTRIBUTES)
```

日本語：

OTEL リソースに追加されるカンマ区切りの k=v ペア (OTEL_RESOURCE_ATTRIBUTES と同じ形式)


### claude-for-msft-365-install/scripts/build-manifest.mjs:99

原文：

```text
0 shows form, 1 (or omit) auto-connects
```

日本語：

0はフォームを表示し、1または省略時は自動接続する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:100

原文：

```text
1 enables Entra SSO (required for aws_role_arn)
```

日本語：

1 は Entra SSO を有効にします (aws_role_arn に必要)


### claude-for-msft-365-install/scripts/build-manifest.mjs:106

原文：

```text
Any non-blank string — Entra validates scope syntax, not us. May be a comma- or
```

日本語：

空白だけではない任意の文字列。スコープ構文を検証するのはこのスクリプトではなくEntra。カンマまたは


### claude-for-msft-365-install/scripts/build-manifest.mjs:107

原文：

```text
whitespace-separated list (the add-in splits it); requires graph_client_id (enforced below).
```

日本語：

空白で区切られたリスト (アドインによって分割されます)。 graph_client_id が必要です (以下で強制されます)。


### claude-for-msft-365-install/scripts/build-manifest.mjs:109

原文：

```text
scope(s) for the resource the token targets: api://<your-app-guid>/.default for your own API, or https://cognitiveservices.azure.com/.default for Foundry direct — comma/space-separated list allowed, requires graph_client_id
```

日本語：

トークンがターゲットとするリソースのスコープ: 独自の API の場合は api://<your-app-guid>/.default、Foundry ダイレクトの場合は https://cognitiveservices.azure.com/.default — カンマ/スペース区切りのリストが許可され、graph_client_id が必要


### claude-for-msft-365-install/scripts/build-manifest.mjs:112

原文：

```text
The add-in rejects unrecognized values at load and falls back to global,
```

日本語：

アドインはロード時に認識できない値を拒否し、グローバルにフォールバックします。


### claude-for-msft-365-install/scripts/build-manifest.mjs:113

原文：

```text
so a typo here degrades to commercial endpoints — heed the warning.
```

日本語：

そのため、この指定を誤ると商用クラウドのエンドポイントへフォールバックする。警告に注意する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:115

原文：

```text
Microsoft national cloud: global | us-gov-high | us-gov-dod | china — only for sovereign clouds; GCC-High and 21Vianet are also auto-detected at sign-in
```

日本語：

Microsoftの国別クラウド：`global | us-gov-high | us-gov-dod | china`。ソブリンクラウド向けの設定。GCC-Highと21Vianetはサインイン時にも自動検出される。


### claude-for-msft-365-install/scripts/build-manifest.mjs:119

原文：

```text
1 allows Claude.ai OAuth alongside 3P (default: locked when other keys present)
```

日本語：

1 は、3P と並行して Claude.ai OAuth を許可します (デフォルト: 他のキーが存在する場合はロックされます)


### claude-for-msft-365-install/scripts/build-manifest.mjs:123

原文：

```text
comma-separated feature slugs to lock for users, e.g. skills.authoring or web_search (disables native web search/fetch; pair with mcp_servers for an in-network replacement)
```

日本語：

ユーザーによる利用をロックする機能スラッグをカンマ区切りで指定する。例：`skills.authoring`、`web_search`。後者はネイティブのWeb検索/取得を無効にする。ネットワーク内の代替手段には`mcp_servers`と組み合わせる。


### claude-for-msft-365-install/scripts/build-manifest.mjs:126

原文：

```text
Comma-separated model ids, or JSON: an array of ids and/or {id, label}
```

日本語：

カンマ区切りのモデル ID、または JSON: ID および/または {id, label} の配列


### claude-for-msft-365-install/scripts/build-manifest.mjs:127

原文：

```text
objects (a lone object is single-entry shorthand). Mirrors the add-in's
```

日本語：

オブジェクトの配列（単独のオブジェクトは1件だけの配列の省略形）。アドインの


### claude-for-msft-365-install/scripts/build-manifest.mjs:128

原文：

```text
parseModelIdEntries leniency but warns where the runtime would silently drop.
```

日本語：

parseModelIdEntriesと同様に入力を柔軟に扱うが、実行時に通知なく除外されるものについて警告する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:130

原文：

```text
Opus 4.8\
```

日本語：

`Opus 4.8\`（モデル表示名を含む文字列断片。末尾のバックスラッシュを保持。）


### claude-for-msft-365-install/scripts/build-manifest.mjs:130

原文：

```text
override the model picker: comma-separated model ids, or JSON like [{\
```

日本語：

モデル ピッカーをオーバーライドします: カンマ区切りのモデル ID、または [{\ のような JSON


### claude-for-msft-365-install/scripts/build-manifest.mjs:133

原文：

```text
) && !t.startsWith(
```

日本語：

`) && !t.startsWith(`

tが指定された接頭辞で始まらないことを確認する式の断片。


### claude-for-msft-365-install/scripts/build-manifest.mjs:134

原文：

```text
).some((id) => !id.trim()) ? [
```

日本語：

`).some((id) => !id.trim()) ? [`

trim後に空になるidが配列内にあるかを確認する式の断片。


### claude-for-msft-365-install/scripts/build-manifest.mjs:146

原文：

```text
 && entry.id.trim() ? [] : [`entry[${i}]: missing string 
```

日本語：

``&& entry.id.trim() ? [] : [`entry[${i}]: missing string``

entry.idが空文字列でないかを検証し、欠落時の警告を生成するコード断片。


### claude-for-msft-365-install/scripts/build-manifest.mjs:154

原文：

```text
JSON array of policy statements — see commands/access-policies.md; e.g. [{\
```

日本語：

ポリシーステートメントのJSON配列。`commands/access-policies.md`を参照。例は原文の`[{\`から続く。


### claude-for-msft-365-install/scripts/build-manifest.mjs:162

原文：

```text
expected a JSON array of statements
```

日本語：

ステートメントの JSON 配列が必要です


### claude-for-msft-365-install/scripts/build-manifest.mjs:168

原文：

```text
Structural check for one access_policies statement. Warn-only: the add-in itself
```

日本語：

1 つの access_policies ステートメントの構造チェック。警告のみ: アドイン自体


### claude-for-msft-365-install/scripts/build-manifest.mjs:169

原文：

```text
skips and reports malformed statements rather than failing, so this catches typos
```

日本語：

不正なステートメントをスキップして報告するため、デプロイ前にタイプミスを検出できる。


### claude-for-msft-365-install/scripts/build-manifest.mjs:170

原文：

```text
before deploy without being stricter than the runtime.
```

日本語：

この検証を実行時の検証より厳しくはしない。


### claude-for-msft-365-install/scripts/build-manifest.mjs:174

原文：

```text
Mirrors the add-in: a GUID supports only equals | exists (a prefix of a GUID is
```

日本語：

アドインと同じ挙動にする。GUIDが対応するのは`equals | exists`だけ（GUIDの前方一致には


### claude-for-msft-365-install/scripts/build-manifest.mjs:175

原文：

```text
meaningless); a name supports the string operators too; a file path supports
```

日本語：

意味がない）。名前は文字列演算子にも対応する。ファイルパスが対応するのは


### claude-for-msft-365-install/scripts/build-manifest.mjs:176

原文：

```text
equals | startsWith. Other pairings are dropped at runtime, so warn here.
```

日本語：

`equals | startsWith`。それ以外の組み合わせは実行時に除外されるため、ここで警告する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:224

原文：

```text
 : typeof id[op] !== 
```

日本語：

`: typeof id[op] !==`

id[op]の型を比較する条件式の断片。


### claude-for-msft-365-install/scripts/build-manifest.mjs:224

原文：

```text
 ? typeof id.exists !== 
```

日本語：

`? typeof id.exists !==`

id.existsの型を比較する条件式の断片。


### claude-for-msft-365-install/scripts/build-manifest.mjs:225

原文：

```text
non-empty string
```

日本語：

空でない文字列


### claude-for-msft-365-install/scripts/build-manifest.mjs:236

原文：

```text
Usage: node build-manifest.mjs <office|outlook> <out.xml> key=value [key=value ...]
```

日本語：

`Usage: node build-manifest.mjs <office|outlook> <out.xml> key=value [key=value ...]`

実行構文。officeまたはoutlook、出力XML、key=value形式の設定を指定する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:240

原文：

```text
 && pairs.some((p) => p.startsWith(
```

日本語：

`&& pairs.some((p) => p.startsWith(`

pairs内の要素が指定された文字列で始まるかを検査するコード断片。


### claude-for-msft-365-install/scripts/build-manifest.mjs:241

原文：

```text
error: Amazon Bedrock (aws_role_arn/aws_region) is not currently supported for Outlook
```

日本語：

エラー: Amazon Bedrock (aws_role_arn/aws_region) は現在 Outlook でサポートされていません


### claude-for-msft-365-install/scripts/build-manifest.mjs:244

原文：

```text
graph_client_id and graph_cloud apply to both manifests: in Outlook it steers Graph +
```

日本語：

graph_client_idとgraph_cloudは両方のマニフェストに適用される。OutlookではGraphと


### claude-for-msft-365-install/scripts/build-manifest.mjs:245

原文：

```text
Entra sign-in; in office it steers the Entra SSO authority.
```

日本語：

Entraサインインを制御し、officeではEntra SSOの認証先を制御する。


### claude-for-msft-365-install/scripts/build-manifest.mjs:271

原文：

```text
entra_scope requires graph_client_id (the scope is requested as your own Entra app, not the default)
```

日本語：

entra_scope にはgraph_client_id が必要です (スコープはデフォルトではなく独自の Entra アプリとして要求されます)


### claude-for-msft-365-install/scripts/build-manifest.mjs:275

原文：

```text
gateway_auth_source=entra requires entra_scope (the gateway Bearer must be audienced to your API, not Microsoft Graph)
```

日本語：

gateway_auth_source=entraにはentra_scopeが必要（ゲートウェイ用Bearerトークンの対象リソースはMicrosoft Graphではなく、利用者のAPIでなければならない）。


### claude-for-msft-365-install/scripts/build-manifest.mjs:279

原文：

```text
note: gateway_auth_source=entra supersedes gateway_token — drop gateway_token from this manifest
```

日本語：

注：gateway_auth_source=entra は、gateway_token を置き換えます — このマニフェストからgateway_token を削除します


### claude-for-msft-365-install/scripts/build-manifest.mjs:281

原文：

```text
A non-global graph_cloud needs a BYO Entra app — Anthropic's multi-tenant
```

日本語：

非グローバルのgraph_cloudにはBYO Entraアプリが必要です - Anthropicのマルチテナント


### claude-for-msft-365-install/scripts/build-manifest.mjs:282

原文：

```text
app exists only in the commercial cloud, so the default client_id against
```

日本語：

アプリは商用クラウドにしか存在しないため、既定のclient_idで


### claude-for-msft-365-install/scripts/build-manifest.mjs:283

原文：

```text
a sovereign authority fails with an opaque AADSTS700016 at sign-in.
```

日本語：

ソブリンクラウドの認証先へアクセスすると、サインイン時に原因の分かりにくいAADSTS700016エラーとなる。


### claude-for-msft-365-install/scripts/build-manifest.mjs:285

原文：

```text
 && !params.has(
```

日本語：

`&& !params.has(`

paramsに指定されたキーがないことを確認する条件式の断片。
