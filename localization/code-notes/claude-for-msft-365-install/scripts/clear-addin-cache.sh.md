# claude-for-msft-365-install/scripts/clear-addin-cache.sh の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/scripts/clear-addin-cache.sh)

### claude-for-msft-365-install/scripts/clear-addin-cache.sh:2

原文：

```text
Clear a single Office add-in's cached / sideloaded manifest on macOS.
```

日本語：

macOS 上で単一の Office アドインのキャッシュ/サイドロードされたマニフェストをクリアします。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:4

原文：

```text
The Wef cache holds every add-in side by side, each file named
```

日本語：

Wef キャッシュには、すべてのアドインが並べて保持され、各ファイルの名前は


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:5

原文：

```text
<addin-id>.manifest-*.xml. This removes ONLY the files matching one
```

日本語：

<addin-id>.manifest-*.xml という形式になっている。この処理では、指定した 1 つの


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:6

原文：

```text
add-in ID across Excel/Word/PowerPoint -- it never wipes the folder.
```

日本語：

アドイン ID に一致するファイルだけを Excel/Word/PowerPoint 全体から削除し、フォルダー自体は削除しない。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:8

原文：

```text
It does NOT touch the add-in's stored data. On macOS chat history, skills,
```

日本語：

アドインの保存データには影響しません。 macOS のチャット履歴、スキル、


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:9

原文：

```text
MCP registrations and memory live in a different subtree entirely --
```

日本語：

MCP 登録とメモリは完全に別のサブツリーに存在します --


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:10

原文：

```text
Data/Library/WebKit/WebsiteData -- while manifests live in Data/Documents/wef.
```

日本語：

Data/Library/WebKit/WebsiteData -- マニフェストは Data/Documents/wef に存在します。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:11

原文：

```text
Clearing the manifest cannot reach the storage. (Windows is not so tidy: see
```

日本語：

マニフェストをクリアしてもストレージに到達できません。 (Windows はあまり整頓されていません: を参照してください)


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:12

原文：

```text
the note in clear-addin-cache.ps1.)
```

日本語：

clear-addin-cache.ps1 のメモ。)


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:15

原文：

```text
clear-addin-cache.sh                       # list every add-in found, do nothing
```

日本語：

clear-addin-cache.sh # 見つかったすべてのアドインをリストし、何もしません


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:16

原文：

```text
clear-addin-cache.sh /path/to/manifest.xml # dry-run: show what would be removed
```

日本語：

clear-addin-cache.sh /path/to/manifest.xml # ドライラン: 削除される内容を表示


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:17

原文：

```text
clear-addin-cache.sh --id <GUID>           # dry-run by ID (no manifest needed)
```

日本語：

clear-addin-cache.sh --id <GUID> # ID によるドライラン (マニフェストは必要ありません)


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:18

原文：

```text
clear-addin-cache.sh /path/manifest.xml --apply   # actually delete
```

日本語：

clear-addin-cache.sh /path/manifest.xml --apply # 実際には削除します


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:21

原文：

```text
Office writes the wef filename using whatever casing the manifest's <Id> had,
```

日本語：

Office は、マニフェストの <Id> の大文字小文字を使用して wef ファイル名を書き込みます。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:22

原文：

```text
so a lowercase GUID from the admin will not match an uppercase file on disk.
```

日本語：

したがって、管理者からの小文字の GUID は、ディスク上の大文字のファイルと一致しません。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:23

原文：

```text
Without this the script reports "already clear" and the admin escalates to a
```

日本語：

これがないと、スクリプトは「すでにクリア済み」と報告し、管理者は


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:23

原文：

```text
already clear
```

日本語：

すでにクリアしています


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:24

原文：

```text
folder-wide wipe. Characters that arrive from a quoted expansion (i.e. the ID
```

日本語：

フォルダー全体の削除に進んでしまう。引用符付きの変数展開から来た文字（つまり ID


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:25

原文：

```text
itself) still stay literal, so `--id '*'` remains inert.
```

日本語：

そのもの）は引き続きリテラルとして扱われるため、`--id '*'` がワイルドカードとして作用することはない。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:28

原文：

```text
Outlook included: it has its own container and its own wef folder. Scanning
```

日本語：

Outlook も対象に含める。Outlook には専用コンテナーと wef フォルダーがある。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:29

原文：

```text
NOT cleared
```

日本語：

クリアされていません


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:29

原文：

```text
only three apps would report "NOT cleared" for a correct ID that simply lives
```

日本語：

3 つのアプリだけを調べると、正しい ID が単に


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:30

原文：

```text
in the fourth -- the exact wrong-turn that sends admins to a folder-wide wipe.
```

日本語：

4 つ目のアプリに存在する場合に誤判定し、管理者をフォルダー全体の削除へ誘導してしまう。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:37

原文：

```text
Guard the value: a bare `--id` would otherwise make `shift 2` fail under
```

日本語：

値があるか確認する。これがないと、値なしの `--id` によって `shift 2` が


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:38

原文：

```text
`set -e` and exit 1 with no output at all.
```

日本語：

`set -e` の下で失敗し、何も出力せず終了コード 1 で終了する。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:39

原文：

```text
ERROR: --id requires a GUID
```

日本語：

エラー: --id には GUID が必要です


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:42

原文：

```text
Only the header block, so the shebang and internal comments stay out.
```

日本語：

ヘッダー ブロックのみなので、シバンと内部コメントは除外されます。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:43

原文：

```text
2,/^set -euo/p
```

日本語：

2,/^set -euo/p


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:48

原文：

```text
No args -> just list what's cached, then exit.
```

日本語：

引数なし -> キャッシュされたものをリストするだけで終了します。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:50

原文：

```text
Add-ins currently cached in wef (id  <-  filename):
```

日本語：

現在 wef にキャッシュされているアドイン (ID <- ファイル名):


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:56

原文：

```text
; printf 
```

日本語：

; printf 


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:60

原文：

```text
Re-run with the manifest path or --id <GUID> to clear one (add --apply to delete).
```

日本語：

マニフェストのパスまたは --id <GUID> を指定して再実行し、対象アドイン 1 つをクリアする（実際に削除するには --apply を追加）。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:64

原文：

```text
Resolve the add-in ID from the manifest if not given explicitly.
```

日本語：

明示的に指定されていない場合は、マニフェストからアドイン ID を解決します。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:66

原文：

```text
ERROR: manifest not found: $MANIFEST
```

日本語：

エラー: マニフェストが見つかりません: $MANIFEST


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:70

原文：

```text
ERROR: could not determine add-in ID
```

日本語：

エラー: アドイン ID を特定できませんでした


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:72

原文：

```text
 -eq 1 ] && echo 
```

日本語：

 -eq 1 ] && echo 


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:73

原文：

```text
DRY RUN -- would remove these (re-run with --apply to delete):
```

日本語：

DRY RUN -- これらは削除されます (削除するには --apply を使用して再実行します)。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:81

原文：

```text
 && echo 
```

日本語：

 && echo 


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:81

原文：

```text
 -eq 1 ]; then rm -f 
```

日本語：

 -eq 1 ]; then rm -f 


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:82

原文：

```text
  would remove $f
```

日本語：

$f を削除します


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:86

原文：

```text
A miss is a dead end, not a success. Reported as "already clear" it sends the
```

日本語：

一致なしは、成功ではなく未解決として扱うべきである。"already clear" と報告すると、


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:86

原文：

```text
already clear
```

日本語：

すでにクリアしています


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:87

原文：

```text
admin off to restart Office, still see the stale add-in, and reach for the
```

日本語：

管理者は Office を再起動しても古いアドインが残っているのを見て、


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:88

原文：

```text
folder-wide wipe -- which on Windows takes the user's chat history with it.
```

日本語：

フォルダー全体の削除に進んでしまう。Windows では、それによりユーザーのチャット履歴も失われる。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:90

原文：

```text
  (no manifest matched $ADDIN_ID)
```

日本語：

($ADDIN_ID に一致するマニフェストはありません)


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:92

原文：

```text
NOT cleared. Either it was already removed, or the ID is wrong.
```

日本語：

クリアされていません。すでに削除されているか、ID が間違っています。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:93

原文：

```text
Re-run with no arguments to list the IDs actually on this Mac.
```

日本語：

引数を指定せずに再実行すると、この Mac 上に実際にある ID がリストされます。


### claude-for-msft-365-install/scripts/clear-addin-cache.sh:97

原文：

```text
Quit and reopen the Office apps so they re-fetch the manifest.
```

日本語：

Office アプリを終了して再度開き、マニフェストを再取得します。


