# claude-for-msft-365-install/scripts/sideload-addin.sh の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/scripts/sideload-addin.sh)

### claude-for-msft-365-install/scripts/sideload-addin.sh:2

原文：

```text
Sideload an Office add-in manifest for local debugging on macOS.
```

日本語：

macOS でのローカル デバッグ用に Office アドイン マニフェストをサイドロードします。


### claude-for-msft-365-install/scripts/sideload-addin.sh:4

原文：

```text
Copies the manifest into each app's Documents/wef folder named
```

日本語：

マニフェストを、各アプリのDocuments/wefフォルダー内へ、


### claude-for-msft-365-install/scripts/sideload-addin.sh:5

原文：

```text
<addin-id>.manifest.xml, so it (a) loads in Excel/Word/PowerPoint and
```

日本語：

<addin-id>.manifest.xmlという名前でコピーする。これにより、(a) Excel/Word/PowerPointに読み込まれ、


### claude-for-msft-365-install/scripts/sideload-addin.sh:6

原文：

```text
(b) is later removable by ID with clear-addin-cache.sh.
```

日本語：

(b) は後で、clear-addin-cache.sh を使用して ID によって削除できます。


### claude-for-msft-365-install/scripts/sideload-addin.sh:8

原文：

```text
This does direct file copies — it does NOT use office-addin-dev-settings.
```

日本語：

これはファイルのコピーを直接行います。office-addin-dev-settings は使用しません。


### claude-for-msft-365-install/scripts/sideload-addin.sh:10

原文：

```text
Sideloading is additive and idempotent — it installs directly (no
```

日本語：

サイドロードは既存構成へ追加する操作で、繰り返しても結果が変わらない。直接インストールを行い、


### claude-for-msft-365-install/scripts/sideload-addin.sh:11

原文：

```text
dry-run). Reverse it any time with clear-addin-cache.sh --id <GUID> --apply.
```

日本語：

ドライランはない。`clear-addin-cache.sh --id <GUID> --apply`でいつでも元に戻せる。


### claude-for-msft-365-install/scripts/sideload-addin.sh:14

原文：

```text
sideload-addin.sh /path/to/manifest.xml
```

日本語：

`sideload-addin.sh /path/to/manifest.xml`

マニフェストのパスを指定する実行例。


### claude-for-msft-365-install/scripts/sideload-addin.sh:28

原文：

```text
usage: sideload-addin.sh /path/to/manifest.xml
```

日本語：

使用法:sideload-addin.sh /path/to/manifest.xml


### claude-for-msft-365-install/scripts/sideload-addin.sh:29

原文：

```text
ERROR: manifest not found: $MANIFEST
```

日本語：

エラー: マニフェストが見つかりません: $MANIFEST


### claude-for-msft-365-install/scripts/sideload-addin.sh:33

原文：

```text
ERROR: could not read <Id> from manifest
```

日本語：

エラー: マニフェストから <Id> を読み取れませんでした


### claude-for-msft-365-install/scripts/sideload-addin.sh:36

原文：

```text
Sideloading add-in $ADDIN_ID
```

日本語：

サイドローディング アドイン $ADDIN_ID


### claude-for-msft-365-install/scripts/sideload-addin.sh:42

原文：

```text
  installed $d/$DEST_NAME
```

日本語：

$d/$DEST_NAME をインストールしました


### claude-for-msft-365-install/scripts/sideload-addin.sh:45

原文：

```text
Quit and reopen Excel/Word/PowerPoint. The add-in appears under
```

日本語：

Excel/Word/PowerPoint を終了して、再度開きます。アドインは以下に表示されます


### claude-for-msft-365-install/scripts/sideload-addin.sh:46

原文：

```text
Insert -> My Add-ins. Remove later with:
```

日本語：

「挿入」→「マイアドイン」。後で次のように削除します。


### claude-for-msft-365-install/scripts/sideload-addin.sh:47

原文：

```text
  ./clear-addin-cache.sh --id $ADDIN_ID --apply
```

日本語：

./clear-addin-cache.sh --id $ADDIN_ID --apply
