# claude-for-msft-365-install/scripts/clear-addin-cache.ps1 の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/scripts/clear-addin-cache.ps1)

### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:20

原文：

```text
deleting individual manifest files can stop all add-ins from loading
```

日本語：

個々のマニフェスト ファイルを削除すると、すべてのアドインの読み込みが停止する可能性があります


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:26

原文：

```text
just delete the Wef folder
```

日本語：

Wefフォルダを削除するだけです


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:46

原文：

```text
No developer key at $devKey -- nothing is sideloaded on Windows.
```

日本語：

$devKey には開発者キーがありません -- Windows には何もサイドロードされません。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:47

原文：

```text
Asked to clear a specific ID and there was nothing to clear it from: same
```

日本語：

指定した ID をクリアするよう要求されたが、削除元に登録がない場合も、


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:48

原文：

```text
miss-reads-as-success shape guarded below, so use the same exit code. With
```

日本語：

下記と同じく「一致なしを成功と誤認する」問題になるため、同じ終了コードにする。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:49

原文：

```text
no -Id this is just an empty listing, which is a legitimate 0.
```

日本語：

-Id がなければ単なる空の一覧であり、終了コード 0 でよい。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:51

原文：

```text
`nNOT cleared. If the add-in was deployed centrally rather than
```

日本語：

`nクリアされていません。アドインがサイドロードではなく一元配布されている場合、


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:52

原文：

```text
sideloaded, this script is not the tool -- see the debug command.
```

日本語：

このスクリプトは対象外です。debug コマンドを参照してください。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:61

原文：

```text
 -and $_.Name -ne 
```

日本語：

 -and $_.Name -ne 


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:65

原文：

```text
Resolve the add-in <Id> from a manifest if -Id wasn't given.
```

日本語：

-Id が指定されていない場合は、マニフェストからアドイン <Id> を解決します。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:67

原文：

```text
manifest not found: $Manifest
```

日本語：

マニフェストが見つかりません: $Manifest


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:71

原文：

```text
No ID at all -> list what's registered and exit (no deletion).
```

日本語：

ID がまったくない -> 登録されているものをリストして終了 (削除なし)。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:73

原文：

```text
Sideloaded add-ins registered under Developer (name  ->  manifest):
```

日本語：

開発者の下に登録されたサイドロード アドイン (名前 -> マニフェスト):


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:79

原文：

```text
  [<Id> $guid]
```

日本語：

[<Id> $guid]


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:81

原文：

```text
`nRe-run with -Id <GUID> (or -Manifest <path>) to remove one (add -Apply to delete).
```

日本語：

`n -Id <GUID> (または -Manifest <path>) を指定して再実行し、1 つを削除します (削除するには -Apply を追加します)。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:85

原文：

```text
$Id becomes part of a registry path below, and Remove-Item -Path expands
```

日本語：

$Id は以下のレジストリパスの一部となる。Remove-Item -Path は


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:86

原文：

```text
wildcards: an -Id of '*' would resolve to every Developer\<Id> subkey rather
```

日本語：

ワイルドカードを展開するため、-Id に '*' を渡すと、1 つではなくすべての Developer\<Id> サブキーが対象になる。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:87

原文：

```text
than one. Require a real GUID so the blast radius stays at a single add-in.
```

日本語：

影響範囲をアドイン 1 つに限定するため、正しい形式の GUID を必須とする。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:92

原文：

```text
Match a Developer value whose name IS the ID, or whose manifest data has that <Id>.
```

日本語：

値の名前自体が ID であるか、値に格納されたマニフェストの <Id> が一致する Developer の値を探す。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:103

原文：

```text
Removing sideload registration for add-in $Id
```

日本語：

アドイン $Id のサイドロード登録を削除しています


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:104

原文：

```text
DRY RUN -- would remove (re-run with -Apply to delete):
```

日本語：

DRY RUN -- 削除します (削除するには -Apply を使用して再実行します)。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:107

原文：

```text
A miss is a dead end, not a success. Read as "already clear" it sends the
```

日本語：

一致なしは成功ではなく未解決として扱う。"already clear" と受け取られると、


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:107

原文：

```text
already clear
```

日本語：

すでにクリアしています


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:108

原文：

```text
admin off to restart Office, still see the stale add-in, and reach for the
```

日本語：

管理者は Office を再起動しても古いアドインが残っているのを見て、


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:109

原文：

```text
Wef folder wipe -- which takes the user's chat history with it.
```

日本語：

Wef フォルダー全体を削除してしまい、ユーザーのチャット履歴も失う。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:110

原文：

```text
  (nothing registered for $Id)
```

日本語：

($Idには何も登録されていません)


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:111

原文：

```text
`nNOT cleared. Either it was already removed, or the ID is wrong.
```

日本語：

`nクリアされていません。すでに削除されているか、ID が間違っています。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:112

原文：

```text
Re-run with no arguments to list what is actually registered.
```

日本語：

引数を指定せずに再実行すると、実際に登録されている内容が一覧表示されます。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:116

原文：

```text
-Name is wildcard-matched, and a value name is often a manifest PATH
```

日本語：

-Name はワイルドカード照合を行う。値の名前はマニフェストのパスであることが多い


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:117

原文：

```text
(see .DESCRIPTION). A path like C:\...\[archive]\manifest.xml would parse
```

日本語：

（.DESCRIPTION を参照）。C:\...\[archive]\manifest.xml のようなパスの角括弧部分は


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:118

原文：

```text
as a character class, match nothing, and -Force would swallow the error --
```

日本語：

文字クラスとして解釈され、一致するものがなくなる。さらに -Force がエラーを抑制するため、


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:119

原文：

```text
printing "removed" for a registration that is still there.
```

日本語：

登録が残っているのに「削除済み」と表示してしまう。


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:120

原文：

```text
  removed value: $($r.Name) -> $($r.Data)
```

日本語：

削除された値: $($r.Name) -> $($r.Data)


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:121

原文：

```text
  would remove value: $($r.Name) -> $($r.Data)
```

日本語：

値を削除します: $($r.Name) -> $($r.Data)


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:124

原文：

```text
  removed settings subkey: $settingsSubkey
```

日本語：

削除された設定サブキー: $settingsSubkey


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:125

原文：

```text
  would remove settings subkey: $settingsSubkey
```

日本語：

設定サブキーを削除します: $settingsSubkey


### claude-for-msft-365-install/scripts/clear-addin-cache.ps1:128

原文：

```text
Quit and reopen the Office apps so they re-read the registry.
```

日本語：

Office アプリを終了して再度開くと、レジストリが再度読み取られます。


