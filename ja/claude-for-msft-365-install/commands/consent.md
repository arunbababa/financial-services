---
description: Azure admin consent URLs — one-time tenant approval for Entra SSO and Outlook Graph access
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/consent.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：Azure 管理者の同意 URL — Entra SSO および Outlook Graph アクセスに対する 1 回限りのテナント承認

<a id="azure-admin-consent"></a>
# Azure管理者の同意

**マニフェストで`entra_sso=1`の場合だけ必要です。** 組織共通の設定を使うGatewayやVertexの構成は
Entraを使わないため、この手順を省略できます。
`graph_client_id`（自社のEntraアプリ）を設定した場合も、このページは適用されません。
自社アプリに対する同意を直接管理します。

テナントごとに一度、全体管理者がURLを開き、Acceptをクリックすれば完了です。
完了するまでは、テナント内の全ユーザーでアドイン内のNAAサインインが失敗します。

<a id="the-url"></a>
## URL

全顧客で同じURLです。`/organizations/`はサインインしたユーザーからテナントを
決定するので、置換は不要です。

```
https://login.microsoftonline.com/organizations/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&redirect_uri=https://pivot.claude.ai/auth/callback
```

URLを表示し、そのテナントの**全体管理者**がサインイン済みのブラウザで
開くよう案内します。アドインが読む項目（ユーザープロフィール、拡張属性）が
並ぶ権限画面が表示されます。**Accept**をクリックすると、
「管理者の同意が付与されました。このタブは閉じられます」という確認ページへ移動します。

<a id="verify"></a>
## 検証する

```bash
az ad sp show --id c2995f31-11e7-4882-b7a7-ef9def0a0266 --query appId -o tsv
```

同じ GUID が返された場合、サービス プリンシパルはテナントに存在します。
同意が機能しました。 「存在しません」というエラーが出た場合は同意が完了していません。

<a id="outlook--microsoft-graph-consent"></a>
## Outlook — Microsoft Graph の同意

**Outlook マニフェストを展開する場合にのみ必要です。** `entra_sso` とは別
上記。 `entra_sso` がオフの場合でも必要です。

Claude for OutlookはMicrosoft Graphを通じてメールと予定表を読みます。Graphの
トークンはユーザーのOutlookクライアント内に留まり、ゲートウェイや
Anthropicへ送信されません。そのため、モデルを提供するクラウドがどれでも
同意は同じです。全体管理者がURLを開いてAcceptをクリックすれば完了です。

```
https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&scope=https://graph.microsoft.com/Mail.ReadWrite%20https://graph.microsoft.com/Calendars.Read%20https://graph.microsoft.com/People.Read%20https://graph.microsoft.com/User.Read%20offline_access&redirect_uri=https://pivot.claude.ai/auth/callback
```

これがなければ、Claudeが初めてメールを読もうとする際、すべてのユーザーで
「管理者の承認が必要」という画面に阻まれます。

**他社アプリへの同意を社内方針で禁止している場合：** 同じ委任Graph権限を持つ
独自のシングルテナントEntraアプリを登録できます。
権限はMail.ReadWrite、Calendars.Read、People.Read、User.Read、offline_accessです。
そのアプリに管理者同意を付与し、Outlookマニフェスト生成時にクライアントIDを
`graph_client_id`として渡します。データの流れは同じで、承認の管理先がAnthropicのアプリから
自社アプリへ変わります。
