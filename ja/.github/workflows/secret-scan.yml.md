# 設定ファイルの自然言語対訳

原本：[.github/workflows/secret-scan.yml](../../../.github/workflows/secret-scan.yml)

基準コミット：`574ed3624aebd0418c7e96cd101262f30210ab26`。キー、識別子、式、ツール設定、URLは原本を正本とします。この付録は読解用で、実行設定を変更しません。

## L26（ステップ名）

**原文**

```text
internal-reference scrub
```

**日本語**

内部参照の検出・除去確認

## L33（出力メッセージ）

**原文**

```text
::error::internal Anthropic references found above
```

**日本語**

エラー：上記にAnthropic内部参照が見つかりました。

## 実行部分について

`uses`、`run`、シェルコマンド、ハッシュ、バージョン、式、環境変数はそのまま原本を参照してください。上の対訳はコメント、表示名、自然言語の出力メッセージに対応します。この翻訳作業でCIやインストール処理は実行していません。
