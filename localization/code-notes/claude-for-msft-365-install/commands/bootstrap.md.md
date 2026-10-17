# claude-for-msft-365-install/commands/bootstrap.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/commands/bootstrap.md)

### claude-for-msft-365-install/commands/bootstrap.md:83

原文：

```text
Access-Control-Allow-Origin:  https://pivot.claude.ai
```

日本語：

`Access-Control-Allow-Origin:  https://pivot.claude.ai`


### claude-for-msft-365-install/commands/bootstrap.md:84

原文：

```text
Access-Control-Allow-Methods: GET
```

日本語：

`Access-Control-Allow-Methods: GET`


### claude-for-msft-365-install/commands/bootstrap.md:85

原文：

```text
Access-Control-Allow-Headers: Authorization, X-Claude-User-Agent, *
```

日本語：

`Access-Control-Allow-Headers: Authorization, X-Claude-User-Agent, *`


### claude-for-msft-365-install/commands/bootstrap.md:97

原文：

```text
S3 — aws s3api put-bucket-cors --bucket <name> --cors-configuration file://cors.json
```

日本語：

S3 — aws s3api put-bucket-cors --bucket <name> --cors-configuration file://cors.json


### claude-for-msft-365-install/commands/bootstrap.md:102

原文：

```text
GCS — gsutil cors set cors.json gs://<bucket>
```

日本語：

`GCS — gsutil cors set cors.json gs://<bucket>`


### claude-for-msft-365-install/commands/bootstrap.md:107

原文：

```text
Azure — az storage cors add --services b --methods GET --origins https://pivot.claude.ai --allowed-headers '*' --account-name <name>
```

日本語：

Azure — az storage cors add --services b --methods GET --origins https://pivot.claude.ai --allowed-headers '*' --account-name <name>


### claude-for-msft-365-install/commands/bootstrap.md:118

原文：

```text
GET <bootstrap_url>                            # after interpolation
```

日本語：

GET <bootstrap_url> # 補間後


### claude-for-msft-365-install/commands/bootstrap.md:119

原文：

```text
Authorization: Bearer <entra_token>            # only if entra_sso=1 in manifest
```

日本語：

Authorization: Bearer <entra_token>            # マニフェストで entra_sso=1 の場合のみ


### claude-for-msft-365-install/commands/bootstrap.md:120

原文：

```text
X-Claude-User-Agent: claude-<app>/<version>    # always sent
```

日本語：

X-Claude-User-Agent: claude-<app>/<version> # 常に送信


### claude-for-msft-365-install/commands/bootstrap.md:176

原文：

```text
Authorization=Bearer {{gateway_token}}
```

日本語：

`Authorization=Bearer {{gateway_token}}`


### claude-for-msft-365-install/commands/bootstrap.md:212

原文：

```text
Risk Dashboard
```

日本語：

リスクダッシュボード


### claude-for-msft-365-install/commands/bootstrap.md:213

原文：

```text
Bearer {{gateway_token}}
```

日本語：

`Bearer {{gateway_token}}`


### claude-for-msft-365-install/commands/bootstrap.md:233

原文：

```text
Draft a deal memo from a term sheet
```

日本語：

タームシートから取引メモの草案を作成する


### claude-for-msft-365-install/commands/bootstrap.md:271

原文：

```text
Opus 4.8
```

日本語：

`Opus 4.8`


