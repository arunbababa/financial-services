---
description: Diagnose deployment issues (stale config, connect failures, missing add-in)
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/debug.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：展開の問題 (古い構成、接続の失敗、アドインの欠落) を診断します。

<a id="debug-a-claude-office-deployment"></a>
# Claude Office 展開をデバッグする

導入済みアドインが正しく動かない理由を、企業の管理者と診断します。
まず**何が問題なのか**を確認し、該当する手順へ進みます。

<a id="triage"></a>
## トリアージ

管理者に症状を説明してもらい、回答に応じて次へ進みます。

| 症状 | セクション |
|---|---|
| マニフェストが更新されましたが、ユーザーには古い設定が表示されたままです | [更新後の古い構成](#stale-config-after-update) |
| アドインに「接続に失敗しました」と表示される | [エラーペーストを読む](#read-the-error-paste) |
| アドインが Excel/PowerPoint にまったく表示されない | [アドインが表示されません](#add-in-not-visible) |
| デプロイ前にマニフェストをローカルでテスト/反復したい | [ローカル デバッグ用のマニフェストをサイドロードする](#sideload-a-manifest-for-local-debugging) |
| サインイン ポップアップが失敗するかループする | [管理者の同意](#admin-consent) |
| ブラウザコンソールを表示する必要がある | [ブラウザ開発ツールを開く](#opening-browser-devtools-on-the-add-in) |

アドインの接続失敗画面の**Copy error details**ボタンでコピーしたエラー詳細が
ある場合は、必ずそこから確認します。必要な情報がまとまっています。

---

<a id="read-the-error-paste"></a>
## コピーしたエラー詳細を読む

コピーした情報の構造：

```
Claude for Office connection failed (<Provider>)
Build: <sha>

<friendly message>

Request:
  <key>: <value actually sent>
  ...

Manifest params:
  <key>: <value the deployed manifest carries>
  ...

Raw error:
<SDK/HTTP error>
```

**確認事項:**

- `Request:`と`Manifest params:`の差分を確認します。両ブロックは同じsnake_caseの
  キー名なので直接比較できます。異なるならユーザーがフォームに上書き値を
  入れています。一致するなら、マニフェストの値が変更されずに
  渡っています。
- `Manifest params:`の`m`キーはバージョンタグです（例：`unified-1.0.0.11`）。
  最後にアップロードした版より古ければ、ユーザーは古いマニフェストを使っています。
  [更新後の構成が古い](#stale-config-after-update)へ進みます。
- `Raw error:`が実際のエラーです。よくあるパターン：
  - `invalid_client`（401、Google）→ 対象の`google_client_id`に対する
    `google_client_secret`が不正です。GCP Console → 認証情報で確認します。
  - `Load failed (<host>)` → ネットワークが WebView 層でブロックされています。ファイアウォール
    で、そのホストを許可する必要があります。
  - `STS AssumeRoleWithWebIdentity failed` → AWS IAM OIDC プロバイダー
    構成が間違っているか、ロール信頼ポリシーが間違っています。
  - `HTTP 401/403` (ゲートウェイ) → 不正なトークン、またはゲートウェイがキーを拒否しました。

---

<a id="stale-config-after-update"></a>
## 更新後の構成が古い

2 種類のキャッシュがあり、反映までの時間も異なります。

| レイヤー | 誰がそれを保持しているのか | TTL | クリア方法 |
|---|---|---|---|
| サービス | M365 管理センター → Exchange Online → クライアント | アップデートの場合は最大 **72 時間** (新規デプロイの場合は 24 時間) | 待つか、新しい `<Id>` を使用して再デプロイします |
| クライアント | 各マシン上の Office アプリの Wef フォルダー | アプリが再起動されるまで、場合によってはそれ以上かかる場合があります | キャッシュされたマニフェストをクリアします (以下を参照) |

Microsoft 自身の FAQ:
> アドインの更新、オンまたはオフからの変更がユーザーに反映されるまでに最大 72 時間かかる場合があります。
> https://learn.microsoft.com/en-us/microsoft-365/admin/manage/centralized-deployment-faq

<a id="confirm-what-admin-center-is-serving"></a>
### 管理センターが提供しているものを確認する

管理センターは同じ`<Version>`の再アップロードを黙って無視します。
第四要素を上げずに修正版をアップロードしても反映されません。M365
管理センター → 統合アプリ → 対象アドインで、表示バージョンを確認します。

<a id="force-a-client-side-refresh"></a>
### クライアント側の更新を強制する

古い **サイドロード** マニフェストは、プラットフォームごとに異なる方法で保存されます。

- **macOS** — 各アプリの`Documents/wef`フォルダーにある
  `<addin-id>.manifest-*.xml`ファイルです。他のアドインのファイルも同じ場所にあります。
- **Windows** — 以下の **レジストリ** 値
  `HKCU:\SOFTWARE\Microsoft\Office\16.0\Wef\Developer`にある値です。削除対象の
  アドイン別ファイルはありません。`Wef`*フォルダー全体*の消去は、これとは異なる、
  より大ざっぱな操作です。後述の注意事項を参照してください。

ヘルパースクリプトを使います。対象アドインの`<Id>`**だけ**を指定し、
`rm`またはレジストリを直接操作します。`office-addin-dev-settings`を
外部コマンドとして呼ぶことは**ありません**。その削除処理が、顧客との
作業中に問題を起こしたためです。

- macOS: [`scripts/clear-addin-cache.sh`](../../../claude-for-msft-365-install/scripts/clear-addin-cache.sh)
- Windows: [`scripts/clear-addin-cache.ps1`](../../../claude-for-msft-365-install/scripts/clear-addin-cache.ps1)

まずExcel/Word/PowerPointを終了します。スクリプトは**IDの直接指定を基本**とし、
アドインの`<Id>`をそのまま渡せます（新しいIDや複数IDでの反復に便利です）。
マニフェストパスの指定は、代わりに`<Id>`を読み取るための任意の補助手段です。

```bash
# macOS — list everything, do nothing:
./scripts/clear-addin-cache.sh

# Dry-run by ID (preferred), or via the manifest:
./scripts/clear-addin-cache.sh --id <GUID>
./scripts/clear-addin-cache.sh ~/path/to/manifest.xml

# Actually remove (only this ID's files):
./scripts/clear-addin-cache.sh --id <GUID> --apply
```

```powershell
# Windows — same flow, registry-scoped:
.\scripts\clear-addin-cache.ps1                  # list, do nothing
.\scripts\clear-addin-cache.ps1 -Id <GUID>       # dry-run
.\scripts\clear-addin-cache.ps1 -Id <GUID> -Apply
```

両スクリプトとも**既定はドライラン**です。`--apply`または`-Apply`なしでは
何も削除しません。引数なしで実行すると、登録済みアドインをすべて一覧表示するので、
まずIDを確認します。他のアドインには影響しません。

IDに一致するものがなければ、スクリプトは**NOT cleared**と表示して非ゼロで終了します。
これはタイプミスまたは削除済みのアドインを示し、*成功ではありません*。
引数なしで再実行し、一覧からIDをコピーしてください。ここで一致しなかったことを理由に、
フォルダー全体の消去へ広げてはいけません。

**どちらのスクリプトもユーザーデータには触れません。** チャット履歴、スキル、MCP
登録、メモリは、アドインIDではなく配信元オリジンをキーに、WebViewに保存されます。
macOSでは、ストレージはマニフェストとは異なるサブツリーです
（`Data/Library/WebKit/WebsiteData`と`Data/Documents/wef`）。
Windowsの消去スクリプトが書き込むのは`HKCU`だけで、ディスクへは書き込みません。
履歴が重要な端末でも、IDによるマニフェストの削除は安全に行えます。

**クリア後、Office アプリを完全に再起動する必要があります。**
ファイルやレジストリ項目を削除しても、起動時にアプリが再読込するまで反映されません。
バックグラウンドのアプリも実行中に数えます。残存プロセスがないことを先に確認し、
Excel / Word / PowerPointを**終了して開き直します**。確認には
macOSなら`pkill -f "Microsoft Excel"`、Windowsならタスクマネージャーを使います。
スクリプトの終了時にも、この注意事項が表示されます。

**ローカル・サイドロードのマニフェストをIDで削除する方法は、安全に動作します。**
実際に、一つのアドインのファイル（macOS）またはレジストリ値
（Windows）だけを削除すれば、そのアドインだけが外れ、他のアドインは正常に読み込まれます。
上流の作成者は日常的にこの方法を使っています。Microsoftの「個々のファイルを削除しない」という警告は、
このローカル開発・サイドロード項目ではなく、後述する*別の*キャッシュについてです。
その警告を理由に、対象を絞る方法を避ける必要はありません。

> **Windowsで管理センターから一括配備したアドインの更新が古いままになる問題**は、
> *別の*キャッシュ、`%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\<guid>\…`の話です。
> これはアドインIDではなく不透明なハッシュをキーに保存されます。Microsoftの公式
> 案内は保守的で、このフォルダーの内容全体を消去するよう求めています。
> 「個別のマニフェストファイルを削除すると、すべてのアドインが
> 読み込まれなくなる場合がある」ためです。実際には対象を絞った削除も機能する場合がありますが、
> ファイル名とIDの対応がないため、対象を絞るのは困難です。
> このため、これらのスクリプトは意図的にそのキャッシュへ**触れません**。
> 一括配備した更新が
> 古いままなら、キャッシュを手動削除するより、サービス側のTTLを待つか、
> 新しい`<Id>`で再配備する方法（後述）を優先します。
>
> ⚠️ **Windows では、ワイプは破壊的です。** アドインのチャット履歴、
> スキル、MCP登録、メモリも、同じディレクトリツリーの内側
> （`%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\webview2\…`）にあり、
> サーバー側のコピーはありません。広く紹介されている「`Wef`フォルダーを消せばよい」という
> 対処は、マニフェストキャッシュとともにユーザーの会話を削除します。
> 実施しようとしている人がいる場合、先に
> [`:export-data`](export-data.md)を実行してください。

再起動しても古いままなら、サービス側キャッシュの反映がまだ追いついていません。
待つか、新しい`<Id>`を使用します（後述）。

Microsoft のキャッシュクリアドキュメント: https://learn.microsoft.com/en-us/office/dev/add-ins/testing/clear-cache

<a id="nuclear-option-redeploy-with-a-fresh-id"></a>
### 最終手段：新しい ID で再配備する

72時間待てない場合、新しいUUIDを`<Id>`にすると、管理センターも全クライアントも
新規アドインとして扱います（新規配備のSLAは24時間、通常はそれよりかなり
短時間です）。`manifest.xml`を編集して`<Id>`内を新しいUUIDへ置き換え、
(Mac/Linux では `uuidgen`、PowerShell では `[guid]::NewGuid()`)、再アップロードします。

---

<a id="add-in-not-visible"></a>
## アドインが表示されない

- **リボンにない場合：** M365管理センター → 統合アプリ → 対象アドイン →
  「ユーザー」タブを確認します。ユーザーまたは所属グループに割り当てられていますか。入れ子のグループ
  はサポートされていません。
- **「マイ アドイン」にはあるがリボンボタンがない場合：** マニフェストの`<Hosts>`に
  対象アプリがない可能性があります。最上位と`<VersionOverrides>`内の
  両方の`<Hosts>`一覧を確認します。
- **新規配備から24時間未満の場合：** 正常な範囲です。初回配備が表示されるまでの
  MicrosoftのSLAは24時間です。

---

<a id="sideload-a-manifest-for-local-debugging"></a>
## ローカル デバッグ用のマニフェストをサイドロードする

マニフェストを**管理センターからの配備を経ずに**反復修正する場合は
（24～72時間のキャッシュ待ちを避けるため）、Officeへローカルのマニフェストを直接指定します。
マニフェストはディスク上の元の場所に置いたままで、その場所をOfficeに教えるだけです。
顧客のOSに合う手順を選びます。

ヘルパースクリプトがマニフェストから`<Id>`を読み、プラットフォームに合う方法で
インストールします。macOSでは各アプリの`Documents/wef`に`<Id>.manifest.xml`を置き、
Windowsでは次のレジストリキーの下に、`<Id>`という名前の値を作ります。
`HKCU:\SOFTWARE\Microsoft\Office\16.0\Wef\Developer`。
どちらもファイルやレジストリを直接書き換え、`office-addin-dev-settings`は**使いません**。

- macOS インストール: [`scripts/sideload-addin.sh`](../../../claude-for-msft-365-install/scripts/sideload-addin.sh)
- Windows インストール: [`scripts/sideload-addin.ps1`](../../../claude-for-msft-365-install/scripts/sideload-addin.ps1)
- 削除（どちらのOSでも）：`clear-addin-cache.{sh,ps1}`。次を参照します。
  [クライアント側のリフレッシュを強制する](#force-a-client-side-refresh)

```bash
# macOS — installs directly:
./scripts/sideload-addin.sh ~/path/to/manifest.xml
```

```powershell
# Windows — installs directly:
.\scripts\sideload-addin.ps1 C:\path\to\manifest.xml
```

サイドロードは追加操作で冪等なため、直接インストールします。**ドライランはありません**。
破壊的な`clear-addin-cache`が既定でドライランなのとは異なります。
登録名にはアドインの`<Id>`を使うため、後から削除する操作はその逆で、
`clear-addin-cache.{sh,ps1} --id <GUID>
--apply`です（サイドロードスクリプトが完了時に正確な削除コマンドを
表示します）。

その後、Excel / Word / PowerPointを**完全に終了して開き直します**。まず、Windowsならタスク
マネージャー、macOSなら`pkill -f "Microsoft Excel"`で残存プロセスを確認します。
バックグラウンドのアプリはレジストリやフォルダーを再読込しません。
アドインは**挿入 → マイ アドイン**に表示されます。Windowsでは
**ホーム**タブの**共有フォルダー**グループにも表示されるので、ピン留めします。

**注意事項 (両方のプラットフォーム):**
- ユーザーごと・端末ごとの設定であり、テナント全体の配備には影響しません。
  顧客が自分の端末でデバッグや反復修正を行うためのものです。
- 同じ`<Id>`なら、ローカルにサイドロードしたマニフェストが一括配備のものより**優先**されます。
  そのため、管理センターへ再アップロードする前に修正版マニフェストをすばやく
  テストする方法にもなります。
- [ブラウザー開発ツール](#opening-browser-devtools-on-the-add-in)も併用し、
  反復修正中にコンソールやネットワークの状態を確認します。
- 古いコピーが読み込まれ続ける場合は、キャッシュも消去します。次を参照します。
  [クライアント側の更新を強制する](#force-a-client-side-refresh)。

Microsoft のサイドローディングに関する参考資料:
- Windows: https://learn.microsoft.com/en-us/office/dev/add-ins/testing/create-a-network-shared-folder-catalog-for-task-pane-and-content-add-ins
- macOS: https://learn.microsoft.com/en-us/office/dev/add-ins/testing/sideload-an-office-add-in-on-mac

---

<a id="admin-consent"></a>
## 管理者の同意

サインインのポップアップがすぐ閉じる、または繰り返される場合、テナントで
Claudeアプリへの管理者同意が付与されていません。
[`:consent`](consent.md)で全体管理者が承認するための同意URLを
生成します。エラー詳細では`Raw error`に`user_canceled`が現れます。
ブローカーが分類できないウィンドウ終了をすべてこの値に対応付けるためです。

---

<a id="silent-sso--entra-token-failures"></a>
## サイレント SSO / Entra トークンの失敗

- **`AADSTS50194: …not configured as a multi-tenant application` /
  `Use a tenant-specific endpoint`** — あなたの `graph_client_id` (または
  `entra_scope`の対象リソースアプリ）がシングルテナントで、アドインが古く、
  まだ`/common`の認証機関にトークンを要求しています。新しい
  ビルドは、`graph_client_id`が設定されていればテナント固有の認証機関を
  自動で解決します。対処は、ユーザーに最新のアドインへ
  更新してもらうことです。古いビルドでは、マニフェストによる回避策はありません。
- **`entra_scope requires graph_client_id`** — `graph_client_id`なしで
  `entra_scope`を設定しています。独自スコープのアクセストークンは、既定のアプリではなく、
  自分のEntraアプリから発行する必要があります。両方を設定してください。この組合せは
  ビルドスクリプトでも拒否されます。
- **サイレントSSOは失敗するが、対話型ポップアップでは成功する場合：** テナントに
  サービスプリンシパルができる前の初回実行では想定内です。管理者同意が
  付与されると（前述）、サイレントSSOも成功します。

---

<a id="opening-browser-devtools-on-the-add-in"></a>
## アドインでブラウザー開発ツールを開く

JSエラー、ネットワークタブ、アドインのデバッグログなど、WebViewのコンソールを
見るには、ホストOSのブラウザー開発ツールを接続します。アドインは
アドレスバーも組込みのF12機能もないWebView内で動くため、
OSごとの手順が必要です。

<a id="macos-safari-web-inspector"></a>
### macOS (Safari Web インスペクター)

必要な設定は3つです。**特に手順3が見落とされがちです。**

1. **Office 開発者向けの追加機能** — まずアプリを終了してから、次の操作を行います。
   ```bash
   defaults write com.microsoft.Excel OfficeWebAddinDeveloperExtras -bool true
   defaults write com.microsoft.Powerpoint OfficeWebAddinDeveloperExtras -bool true
   defaults write com.microsoft.Word OfficeWebAddinDeveloperExtras -bool true
   ```
   右クリック → **要素の検査** が作業ウィンドウ内に表示されます。

2. **Safariの開発メニュー** — Safari → 設定 → 詳細で、
   *Webデベロッパ用の機能を表示*にチェックを入れます。

3. **macOSの開発者ツール許可リスト**（Sonoma以降）— システム設定
   → プライバシーとセキュリティ → 開発者ツールで、**ターミナル**をオンにします。これが
   なければ、手順1・2が済んでいてもSafariの開発メニューに
   *No Inspectable Applications*（検査可能なアプリケーションがない）と表示されます。

作業ウィンドウを開いた状態で、作業ウィンドウ内を右クリック → **要素の検査**、
または、Safari → 開発 → *[マシン名]* に移動し、アドイン ホストを見つけます。
(本番環境では `pivot.claude.ai`、それ以外の場合は構成されたドメイン)。

**注意点:**
- **Officeの更新は手順1の設定を黙ってリセットします。** 先週は検査できたのに
  今はできない場合、`defaults write`を再実行します。
- *No Inspectable Applications*は、手順3が未設定か、`defaults write`の前に
  Officeを完全終了していなかった場合です。`pkill -f "Microsoft Excel"`の後に
  再起動します。
- Safariの「開発」メニューに表示するには、アプリだけでなく
  **作業ウィンドウ自体が開いている**必要があります。

<a id="windows-edge-devtools"></a>
### Windows（Edge DevTools）

Officeが使うWebViewエンジンによって異なります。Win10/11上の現行M365で
WebView2ランタイムがあればChromiumを使います。古い買切り版Officeやランタイムの
ない端末は、IE11/Tridentを使っている場合があります。

**WebView2 (Chromium — 一般的なケース):**

タスクペイン内を右クリックして**Inspect**を選びます。それだけで、追加の有効化条件はありません。
右クリックでInspectが出ない場合、Microsoft Storeから**Microsoft Edge DevTools
Preview**をインストールします。Officeアドインも含め、接続可能なWebView2の
対象が一覧になります。起動して対象一覧からアドインのURLを
選び、クリックして接続します。

**IE11/Trident（旧型の買切り版 Office 2019/2021）：**

管理者 PowerShell から IEChooser を実行します。
```powershell
& "C:\Windows\SysWOW64\F12\IEChooser.exe"
```
リストからアドインのページを選択します。リストが空の場合、作業ウィンドウ
はまだ開いていません。まず開いてから、IEChooser を更新します。

Microsoft のウォークスルー: https://learn.microsoft.com/en-us/office/dev/add-ins/testing/debug-add-ins-using-devtools-edge-chromium
