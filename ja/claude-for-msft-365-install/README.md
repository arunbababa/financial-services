> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../claude-for-msft-365-install/README.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

<a id="claude-for-office--direct-cloud-setup"></a>
# Claude for Office — クラウドの直接セットアップ

Claude Office アドインを構成して独自のクラウドを呼び出すための管理ツール
Anthropic の API の代わりに (Vertex AI、Bedrock、または LLM ゲートウェイ)。

<a id="install"></a>
## インストール

```bash
claude plugin marketplace add anthropics/financial-services
claude plugin install claude-for-msft-365-install@claude-for-financial-services
```

次にセッション内: `/claude-for-msft-365-install:setup`

<a id="update"></a>
## アップデート

最新バージョンのプラグインをプルします。

```bash
claude plugin update claude-for-msft-365-install@claude-for-financial-services
```

適用するにはセッションを再起動してください。新しいオプションでマニフェストを再生成する
必要がある場合に限り、`/claude-for-msft-365-install:setup`を再実行します。

<a id="bootstrap"></a>
## ブートストラップ

ユーザーごとの MCP サーバー、スキル、または動的構成の場合は、ブートストラップ エンドポイントをホストします
そしてアドインをそこにポイントします。

```bash
claude plugin marketplace add anthropics/financial-services   # if not already added
claude plugin install claude-for-msft-365-install@claude-for-financial-services
```

次にセッション内: `/claude-for-msft-365-install:bootstrap`

<a id="commands"></a>
## コマンド

| コマンド | 何をするのか |
|---|---|
| `/claude-for-msft-365-install:setup` | インタラクティブなウィザード - クラウド リソースのプロビジョニング、管理者の同意、マニフェストの書き込み |
| `/claude-for-msft-365-install:manifest` | カスタマイズされたアドイン マニフェスト XML を生成する |
| `/claude-for-msft-365-install:consent` | アドインのアプリ登録用の Azure 管理者の同意 URL |
| `/claude-for-msft-365-install:update-user-attrs` | Microsoft Graph 拡張属性を介してユーザーごとの構成を書き込む |
| `/claude-for-msft-365-install:bootstrap` | ブートストラップ エンドポイントを構築する — ユーザーごとの MCP サーバー、スキル、動的構成 |
| `/claude-for-msft-365-install:debug` | 展開の問題を診断します — 古い構成、接続の失敗、アドインの欠落 |
| `/claude-for-msft-365-install:export-data` | ユーザーのチャット履歴、スキル、MCP 登録のコピーをエクスポートする |

<a id="exporting-user-data"></a>
## ユーザーデータのエクスポート

チャット履歴、アップロードしたスキル、MCP登録、メモリ、設定は、ユーザー自身の端末の
ブラウザストレージに保存されます。サーバー側のコピーはありません。

エクスポートスクリプトは**読取専用**です。Officeのストレージを読み、書き込むのは
指定したフォルダーだけです。Office内のデータを変更・移動・削除することはありません。
引数を指定しない場合は、見つかった内容を表示するだけです。

```bash
./scripts/export-addin-data.sh                       # macOS: list
./scripts/export-addin-data.sh --out ~/claude-export
```
```powershell
.\scripts\export-addin-data.ps1                      # Windows: list
.\scripts\export-addin-data.ps1 -Out C:\claude-export
```

**アドインを変更してもデータは移動・削除されません。** ストレージはアドインIDではなく、
アドインの配信元オリジンをキーとします。そのためマニフェストの置換、
再インストール、サイドロード版マニフェストとストア掲載版の切替えを行っても、
データはそのまま残ります。端末の再構築前、または特にWindowsではOfficeアドインの
キャッシュを誰かが消去する前に、エクスポートしてください。`Wef`には
マニフェストキャッシュだけでなくアドインのストレージも保存されているためです。

正確な保存パスと、履歴が見当たらない場合の確認事項は、
`/claude-for-msft-365-install:export-data`を参照してください。
