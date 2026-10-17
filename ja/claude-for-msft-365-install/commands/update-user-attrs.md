---
description: Set per-user config (tokens, region overrides) via Azure AD extension attributes
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/update-user-attrs.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：Azure AD の拡張属性を使い、トークンやリージョンの上書きなど、ユーザーごとの構成を設定します。

<a id="per-user-config-via-extension-attributes"></a>
# 拡張属性によるユーザーごとの構成

属性はすでに Anthropic のアプリ (`c2995f31-…`) に登録されています - あなた
スキーマは作成せず、値を記述するだけです。アドインは次のように読み取ります
ユーザーの ID トークンからの `extension_c2995f3111e74882b7a7ef9def0a0266_<key>`。

**マニフェストに`entra_sso=1`が必要です。** なければアドインはEntraトークンを
取得せず、これらの属性も読みません。エラーを出さずに
何の効果も持たない状態になります。

どの構成キーもユーザーごとに設定できます。アドインはユーザーごとの属性をマージします。
マニフェストパラメータを超えるため、ここにあるものが優先されます。すべての値は最大 256 文字です。

| キー | ユーザーごとのユースケース |
|---|---|
| `gateway_token` | ユーザーごとの API キー (ローテーション) |
| `gateway_url` | 異なるチームを異なるゲートウェイにルーティングする |
| `gateway_api_format` | ゲートウェイは Anthropic `/v1/messages` ではなく、Bedrock/Vertex パススルーを話します |
| `inference_headers` | ゲートウェイのユーザーごとのアカウンティング タグ (JSON、256 文字の上限に注意してください) |
| `bootstrap_url` | ユーザーごとの認証情報を発行・配信するエンドポイント |
| `gcp_project_id` | さまざまな GCP プロジェクトのさまざまなチーム |
| `gcp_region` | データ常駐の上書き |
| `google_client_id` `google_client_secret` | チームごとに異なる OAuth クライアント (一般的ではありません) |
| `aws_role_arn` `aws_region` | チームごとに異なるBedrockのロール |
| `otlp_endpoint` `otlp_headers` `otlp_resource_attributes` | テレメトリをチームレベルのリソース属性を持つチーム固有の OTEL コレクター/タグ スパンにルーティングします。 |

<a id="one-user"></a>
## 1人のユーザー

`<key>` をテーブルの属性名に置き換えます。非秘密キーの場合
(リージョン、プロジェクト ID) これは通常のパスです。シークレットについては (`gateway_token`、
`google_client_secret`) 値はシェル履歴に記録され、この会話の
トランスクリプト — 問題がある場合は、以下の一括 CSV パスを使用してください。

```bash
az rest --method PATCH \
  --uri "https://graph.microsoft.com/v1.0/users/<upn>" \
  --body '{"extension_c2995f3111e74882b7a7ef9def0a0266_<key>":"<value>"}'
```

成功はサイレントです。PATCH は空の本体を含む 204 を返します。確認するには:

```bash
az rest --method GET --uri "https://graph.microsoft.com/v1.0/users/<upn>?\$select=extension_c2995f3111e74882b7a7ef9def0a0266_<key>"
```

グラフの読み取りは書き込みと即座に一致し、遅延はありません。ごとにダンプするには
ユーザーの拡張属性 (正確なキー名がわからない場合) は、`/beta/` を使用します。

```bash
az rest --method GET --uri "https://graph.microsoft.com/beta/users/<upn>" | jq 'to_entries | map(select(.key | startswith("extension"))) | from_entries'
```

<a id="bulk-csv-values-never-enter-this-chat"></a>
## 一括 (CSV、値がこのチャットに入力されることはありません)

管理者に `users.csv` を準備してもらいます。最初の列は UPN です。残りの列
ヘッダーは属性キーです。空のセルは、そのユーザーの属性をスキップします。

```
upn,gateway_token,gcp_region
alice@acme.com,sk-live-aaa,
bob@acme.com,sk-live-bbb,europe-west4
carol@acme.com,,europe-west4
```

**macOS/Linux** — これを CSV の隣の `apply.sh` に書き込みます (`read -a` 配列の構文は次のとおりです)
bash のみ。 zsh への裸のペーストは壊れます)。彼らはそれを確認してから実行します
`bash apply.sh`を利用者が実行します。確認するのは✓/✗だけとし、どちらのファイルも`cat`で表示してはいけません。

```bash
#!/bin/bash
EXT=extension_c2995f3111e74882b7a7ef9def0a0266_
{
  IFS=, read -ra keys
  while IFS=, read -ra vals; do
    upn="${vals[0]}"
    for i in "${!keys[@]}"; do
      [ "$i" -eq 0 ] || [ -z "${vals[$i]}" ] && continue
      az rest --method PATCH --uri "https://graph.microsoft.com/v1.0/users/$upn" \
        --body "{\"${EXT}${keys[$i]}\":\"${vals[$i]}\"}" \
        && echo "✓ $upn ${keys[$i]}" || echo "✗ $upn ${keys[$i]}"
    done
  done
} < users.csv
```

**Windows** — これを CSV の隣の `apply.ps1` に書き込みます。 `Import-Csv` 読み取り
ヘッダーを直接スキーマとして使用します。 PowerShell で `.\apply.ps1` を実行します。

```powershell
$EXT = 'extension_c2995f3111e74882b7a7ef9def0a0266_'
Import-Csv users.csv | ForEach-Object {
  $upn = $_.upn
  $_.PSObject.Properties | Where-Object { $_.Name -ne 'upn' -and $_.Value } | ForEach-Object {
    $body = @{ "$EXT$($_.Name)" = $_.Value } | ConvertTo-Json -Compress
    az rest --method PATCH --uri "https://graph.microsoft.com/v1.0/users/$upn" --body $body
    if ($?) { "OK $upn $($_.Name)" } else { "FAIL $upn $($_.Name)" }
  }
}
```

✓ と ✗ の数を報告します。 404 は UPN が間違っていることを意味します。 403
`az login` に `User.ReadWrite.All` がないことを意味します — 再同意するか、使用する必要があります
管理者アカウント。

<a id="propagation-delay"></a>
## 伝播遅延

Graphへの書込みは即座に成功しますが、アドインはNAAサインイン時にユーザーの
IDトークンを通じて属性を読み、Azure STSはトークンのクレームをキャッシュします。新しい値が
そのユーザーに見えるまで、**最大1時間**を見込んでください。PATCH直後に
アドインを開いて未設定のように動いても、原因は
キャッシュであり、書込み失敗ではありません。待って再試行するよう案内します。タスクペインを閉じるだけでなく、
Officeを完全終了すると、次の起動で新しいNAAトークンを取得させられます。
