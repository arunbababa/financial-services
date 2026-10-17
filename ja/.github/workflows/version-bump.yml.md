# 設定ファイルの自然言語対訳

原本：[.github/workflows/version-bump.yml](../../../.github/workflows/version-bump.yml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## L3–5（コメント）

**原文**

```text
Backstop for contributors without the local pre-commit hook: every PR that
modifies a plugin must bump that plugin's .claude-plugin/plugin.json version,
otherwise already-installed users won't receive the change.
```

**日本語**

ローカルのpre-commitフックを使わない貢献者向けの補完策です。プラグインを変更するすべてのPRでは、そのプラグインの`.claude-plugin/plugin.json`のバージョンを上げる必要があります。そうしないと、インストール済みのユーザーへ変更が届きません。

## L20（ステップ名）

**原文**

```text
Check plugin version bumps
```

**日本語**

プラグインのバージョン更新を検査する

## 実行部分について

`uses`、`run`、シェルコマンド、ハッシュ、バージョン、式、環境変数はそのまま原本を参照してください。上の対訳はコメント、表示名、自然言語の出力メッセージに対応します。この翻訳作業でCIやインストール処理は実行していません。
