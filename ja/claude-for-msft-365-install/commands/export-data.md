---
description: Export a copy of a user's add-in chat history, skills, MCP registrations, and settings before a machine is rebuilt
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/export-data.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：マシンを再構築する前に、ユーザーのアドイン チャット履歴、スキル、MCP 登録、および設定のコピーをエクスポートします。

<a id="export-add-in-data"></a>
# アドインデータのエクスポート

チャット履歴、アップロードしたスキル、MCP登録、メモリ、設定は、**ユーザー自身の端末**の
ブラウザストレージにあります。サーバー側のコピーはありません。これらの
スクリプトはそのコピーを作ります。

| プラットフォーム | スクリプト |
|---|---|
| macOS | `scripts/export-addin-data.sh` |
| Windows | `scripts/export-addin-data.ps1` |

**読取専用です。** Officeのストレージを読み、書き込むのは指定したフォルダー
だけです。Office内のデータを変更・移動・削除しません。引数なしで
実行した場合は、見つかった内容を表示するだけです。

```bash
./scripts/export-addin-data.sh                      # macOS: list
./scripts/export-addin-data.sh --out ~/claude-export
```
```powershell
.\scripts\export-addin-data.ps1                     # Windows: list
.\scripts\export-addin-data.ps1 -Out C:\claude-export
```

<a id="why-reinstalling-the-add-in-doesnt-lose-anything"></a>
## アドインを再インストールしても何も失われない理由

マニフェストは**参照先を示すもので、データの容器ではありません**。持つのは`<Id>`、
`<Version>`、`<SourceLocation>`のURLで、データは持ちません。Officeはこれを読み、
埋め込みブラウザ（macOSはWKWebView、WindowsはWebView2）でそのURLを
開きます。その後は通常のWebの規則で、ChromeやSafariと同様に、ブラウザは
ページの**オリジン**（`scheme://host:port`）ごとにIndexedDBを
割り当てます。

したがって、ID とストレージは 2 つの異なるキー上に存在します。

```
  manifest.xml                       the WebView                storage bucket
  ┌──────────────────────┐           ┌───────────────┐          ┌─────────────┐
  │ <Id>  3499c065-…     │──ignored─╳│               │          │             │
  │ <Version> 1.0.0.11   │──ignored─╳│  loads  URL   │──origin─▶│ IndexedDB   │
  │ <SourceLocation>     │──────────▶│               │          │  for that   │
  │   https://host/…     │           └───────────────┘          │   origin    │
  └──────────────────────┘                                      └─────────────┘
         ▲                                                             ▲
         │ replaced / deleted / re-ID'd / version-bumped               │
         └──── none of this reaches ───────────────────────────────────┘
```

マニフェストの削除はブックマークの削除と同様で、サイトのCookieまで一緒に
消えるわけではありません。同じURLを指す新しいマニフェストを置けば、同じストレージが
残っています。マニフェストのIDはストレージの検索には関係しません。

これは直接確認できます。試験用と本番用で**`<Id>`が異なる**マニフェストでも、
どちらも`https://pivot.claude.ai`を指すなら、一つのストアを共有します。
オリジンが同じだからです。ストレージパスのどこにもアドインIDは
現れません。

したがって、これらはすべて、何もせずに履歴を所定の位置に保持します。

- マニフェストを新しいものに置き換える
- マニフェストを削除するか、アンインストールして再インストールする
- サイドロードされたマニフェストとストアの掲載情報の間の移動
- バージョンバンプ、または管理センターのキャッシュを回避するための新しい `<Id>`

実際にデータの場所を変えるのは、オリジン、またはデータを持つ
プロファイルの変更です。

| 変更 | 効果 |
|---|---|
| 配信元ホスト、`https`→`http`、ポートが変わる | 新しいオリジンには空のストアが作られる。旧ストアは残るが、参照されない。 |
| マシンが再構築されるか、ブラウザ プロファイルが消去される | 消えた。サーバー側には何も保存されません。 |
| WindowsでOfficeへ別アカウントでサインイン | プロファイルパスとストアが変わる。元のアカウントへ戻せば元に戻る。 |

<a id="when-you-need-this"></a>
## これが必要なときは

マシンまたは保管場所が変更される直前にエクスポートします。

| 状況 | なぜ |
|---|---|
| PC または Mac が再構築、再イメージ化されている、または他の人に渡されている | サーバー側には何も保存されません。 |
| **Windows** での Office アドイン キャッシュのクリア | アドインのストレージは `Wef` フォルダー内に存在するため、「Wef フォルダーを削除」するとチャット履歴も削除されます。 macOS では、これらは別個のツリーであり、キャッシュをクリアしても無害です。 |
| ローミング プロファイル / FSLogix クリーンアップ、または `ClearBrowsingDataOnExit` などのエッジ ポリシー | アドインが保存されているブラウザー プロファイルを消去します。 |
| 昔の会話は重要です | 履歴にはアプリごとに最新の 50 件のチャットが保存され、ストレージが不足すると最も古いチャットが自動的に削除されます。 |

<a id="what-is-in-the-export"></a>
## エクスポート内容は何ですか

Office アプリ (macOS) またはサインインしたアカウントごとにグループ化されたプレーン フォルダー ツリー
(Windows)、Web サイト別:

```
claude-export/
└── Excel/                            macOS groups by app — each Office app has
    ├── pivot.claude.ai/              its own sandbox, so each keeps separate history
    │   ├── claude-chat-history/
    │   ├── claude-local-skills/
    │   ├── claude-mcp-gateways/
    │   ├── claude-memory/
    │   └── local-storage/            settings, inference config, onboarding + terms
    └── addins.contoso.com_8443/      a non-default port is kept in the name:
        └── …                         :8443 is a different origin, so a different store
```

Windows は、アプリごとではなく、サインインしている Office アカウントごとにグループ化されます。
localStorage は、そのプロファイル上のすべてのオリジンによって共有される 1 つのストアであるため、
全体がコピーされ、元のフォルダーの横に配置されます。

```
claude-export\
└── <guid>_ADAL__2\                    the Office account (see "Putting data back")
    ├── pivot.claude.ai\
    │   └── https_pivot.claude.ai_0.indexeddb.leveldb\
    ├── addins.contoso.com_8443\
    └── Local Storage\                 ⚠ whole profile store — ALL origins, not
        └── leveldb\                     just Claude's. Chromium cannot split it.
```

最後のフォルダーだけは「Claudeのデータのみ」の例外です。localStorageには
設定、推論設定、初期設定・規約同意フラグが入り、プロファイルごとに一つの
LevelDBを全オリジンで共有するため、
一つのアドインだけに絞れません。捨てずに全体をコピーし、容量を
引数なしのプレビューも含め毎回表示します。この扱いが
社内データ方針上許されない場合、エクスポートから`Local Storage`を削除してください。
それ以外はClaudeのデータだけです。macOSのlocalStorageは*オリジンごと*なので、
各オリジン内の`local-storage/`に入り、他のデータは含みません。

どちらのレイアウトも **パス ミラーではなく、読みやすくするために再ラベル付けされています** - 実際のレイアウト
場所がソルト付きハッシュ (macOS) または `…\2\[n]\EBWebView\Default\` の下にネストされている
(Windows)。これらのパスを介してエクスポートをコピーして戻すことはできません。参照してください
[データを戻す](#putting-data-back)。

サインイントークンは意図的に**含めません**。再構築した端末では再度サインインする方が
安全な既定動作だからです。ただしエクスポートには**会話本文が含まれ**、
Windowsの`Local Storage`には他のアドインの設定も含まれます。
それらの内容を複製した他のデータと同じ方針で取り扱ってください。

<a id="checking-an-export-is-complete"></a>
### エクスポートが完了したことを確認しています

macOS ではストアは SQLite であるため、コピーを元のストアと比較します。

```bash
sqlite3 <path>/IndexedDB.sqlite3 'SELECT sum(length(value)) FROM Records;'
```

合計が一致すればコピーに欠落はありません。`PRAGMA integrity_check`と
`SELECT count(*)`は、どちらも**`no such collation sequence: IDBKEY`**で失敗します。
WebKitはその照合順序を実行時に登録しますが、`sqlite3`のCLIには
登録する手段がないためです。このエラーはコピーの状態を示すものではなく、*原本*でも
発生します。破損と解釈してはいけません。

<a id="putting-data-back"></a>
## データを元に戻す

スクリプトは意図的に復元を行いません。Officeのストレージに書き込むと正常な環境を
壊すおそれがあり、適切な対処はデータが見えなくなった理由によって変わります。
エクスポートを保管し、Anthropicサポートへ相談してください。そのフォルダーに
復旧に必要なものが揃っています。

リカバリがまったく必要ないため、最初に確認する価値のあるケースが 1 つあります。
Windows のストレージ パスには **サインインした Office アカウント**が含まれます —

```
%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\webview2\<account>\2\[n]\EBWebView\
```

`_ADAL`で終わるGUIDは職場・学校のアカウント、`_LiveId`で終わるものは
個人のMicrosoftアカウントです。チャットを作成した時と別のアカウントで
Officeにサインインすると、アドインは別フォルダーを読み、
履歴が消えたように見えます。**元のアカウントへサインインし直せば、
コピーせずに履歴が戻ります。** 引数なしでエクスポートスクリプトを実行すると、
端末にあるアカウントフォルダーがラベル付きで一覧になります。

<a id="where-the-data-lives"></a>
## データが存在する場所

納得できていない管理者には、フォルダーを直接示します。何かを実行せずとも、
そのまま読めます。両方のスクリプトは`--help`／
`Get-Help`の出力にもこれらのパスを表示します。

**Windows** — ファイル エクスプローラーに貼り付けます。

```
%LOCALAPPDATA%\Microsoft\Office\16.0\Wef\webview2
```

その後、`<account>\2\[n]\EBWebView\Default\IndexedDB\`を開きます。フォルダー名は
オリジンに基づき、例えば`https_pivot.claude.ai_0.indexeddb.leveldb`です。

**macOS** — アプリごとのサンドボックス コンテナなので、各アプリには独自の履歴があります。

```
~/Library/Containers/com.microsoft.Excel/Data/Library/WebKit/WebsiteData/Default
```

各サブフォルダーは 1 つのオリジンであり、ソルト付きハッシュで名前が付けられます - プレーンテキストを読み取ります
中の `origin` ファイルを確認してください。チャット履歴は
`IndexedDB/<uppercase SHA-256 of "claude-chat-history">`;そのハッシュをチェックしてください
`printf 'claude-chat-history' | shasum -a 256`.
