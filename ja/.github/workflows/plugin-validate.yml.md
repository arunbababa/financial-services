# 設定ファイルの自然言語対訳

原本：[.github/workflows/plugin-validate.yml](../../../.github/workflows/plugin-validate.yml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## L3–5（コメント）

**原文**

```text
Runs the official Claude Code plugin linter over every plugin and the
marketplace manifest. Catches malformed manifests (e.g. hooks.json as a
bare [] instead of {"hooks": {}}) before they reach users.
```

**日本語**

すべてのプラグインとmarketplaceマニフェストに対し、公式のClaude Codeプラグイン検査を実行します。不正なマニフェスト（例えば`hooks.json`が`{"hooks": {}}`ではなく単なる`[]`になっているもの）を、ユーザーへ届く前に検出します。

## L16–19（コメント）

**原文**

```text
Pinned for reproducible builds + a stable cache key. Bump by setting this
to a newer version from https://downloads.claude.ai/claude-code-releases/stable
2.1.143: first release whose `plugin validate` accepts `displayName` on
marketplace entries (2.1.140 and earlier reject it as an unrecognized key).
```

**日本語**

再現可能なビルドと安定したキャッシュキーのためにバージョンを固定しています。更新するには`https://downloads.claude.ai/claude-code-releases/stable`の新しいバージョンを設定してください。2.1.143は、`plugin validate`がmarketplace項目の`displayName`を受け付ける最初のリリースです（2.1.140以前は未認識のキーとして拒否します）。

## L28（ステップ名）

**原文**

```text
Cache Claude Code CLI
```

**日本語**

Claude Code CLIをキャッシュする

## L32–33（コメント）

**原文**

```text
~/.local/bin/claude is a symlink into the versioned dir below —
both must be cached or the restored symlink dangles (exit 127).
```

**日本語**

`~/.local/bin/claude`は、以下にあるバージョン別ディレクトリへのシンボリックリンクです。両方をキャッシュしないと、復元したリンクの参照先がなくなります（終了コード127）。

## L39（ステップ名）

**原文**

```text
Install Claude Code CLI
```

**日本語**

Claude Code CLIをインストールする

## L43（ステップ名）

**原文**

```text
Validate marketplace + every plugin
```

**日本語**

marketplaceとすべてのプラグインを検査する

## L50（出力メッセージ）

**原文**

```text
::group::marketplace
```

**日本語**

ロググループの開始：marketplace。

## L52（出力メッセージ）

**原文**

```text
::endgroup::
```

**日本語**

ロググループの終了。

## L56（出力メッセージ）

**原文**

```text
::group::$plugin_dir
```

**日本語**

ロググループの開始：`$plugin_dir`で指定されるプラグイン。

## L58（出力メッセージ）

**原文**

```text
::endgroup::
```

**日本語**

ロググループの終了。

## L62（出力メッセージ）

**原文**

```text
::error::plugin validation failed — see grouped logs above
```

**日本語**

エラー：プラグインの検査に失敗しました。上のグループ化されたログを参照してください。

## 実行部分について

`uses`、`run`、シェルコマンド、ハッシュ、バージョン、式、環境変数はそのまま原本を参照してください。上の対訳はコメント、表示名、自然言語の出力メッセージに対応します。この翻訳作業でCIやインストール処理は実行していません。
