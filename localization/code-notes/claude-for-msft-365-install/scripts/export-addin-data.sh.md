# claude-for-msft-365-install/scripts/export-addin-data.sh の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/scripts/export-addin-data.sh)

### claude-for-msft-365-install/scripts/export-addin-data.sh:2

原文：

```text
Export a copy of the Claude Office add-in's local data on macOS -- chat
```

日本語：

macOS 上の Claude Office アドインのローカルデータをコピーしてエクスポートする。対象はチャット


### claude-for-msft-365-install/scripts/export-addin-data.sh:3

原文：

```text
history, uploaded skills, MCP registrations, and memory.
```

日本語：

履歴、アップロードしたスキル、MCP 登録、メモリ。


### claude-for-msft-365-install/scripts/export-addin-data.sh:5

原文：

```text
READ ONLY. This script never writes to, moves, or deletes anything in Office.
```

日本語：

読み取り専用。このスクリプトは、Office 内の何かに書き込んだり、移動したり、削除したりすることはありません。


### claude-for-msft-365-install/scripts/export-addin-data.sh:6

原文：

```text
It reads the add-in's storage and copies it to a folder you name. Run it with
```

日本語：

アドインのストレージを読み取り、指定したフォルダーへコピーする。


### claude-for-msft-365-install/scripts/export-addin-data.sh:7

原文：

```text
no arguments and it only prints what it found.
```

日本語：

引数なしで実行した場合は、見つかった内容を表示するだけ。


### claude-for-msft-365-install/scripts/export-addin-data.sh:9

原文：

```text
SEE IT YOURSELF -- you do not need this script to look
```

日本語：

自分で見てください -- 見るためにこのスクリプトは必要ありません


### claude-for-msft-365-install/scripts/export-addin-data.sh:10

原文：

```text
The data is a plain, unencrypted folder. Open it in Finder:
```

日本語：

データは暗号化されていないプレーンなフォルダーです。 Finder で開きます。


### claude-for-msft-365-install/scripts/export-addin-data.sh:12

原文：

```text
open ~/Library/Containers/com.microsoft.Excel/Data/Library/WebKit/WebsiteData/Default
```

日本語：

open ~/Library/Containers/com.microsoft.Excel/Data/Library/WebKit/WebsiteData/Default


### claude-for-msft-365-install/scripts/export-addin-data.sh:14

原文：

```text
Each subfolder there is one website's storage, named with a salted hash.
```

日本語：

各サブフォルダーには 1 つの Web サイトのストレージがあり、ソルト付きハッシュで名前が付けられます。


### claude-for-msft-365-install/scripts/export-addin-data.sh:15

原文：

```text
Print which is which:
```

日本語：

どれがどれであるかを出力します:


### claude-for-msft-365-install/scripts/export-addin-data.sh:17

原文：

```text
for d in ~/Library/Containers/com.microsoft.Excel/Data/Library/WebKit/\
```

日本語：

for d in ~/Library/Containers/com.microsoft.Excel/Data/Library/WebKit/\


### claude-for-msft-365-install/scripts/export-addin-data.sh:18

原文：

```text
WebsiteData/Default/*/; do echo "$(strings "$d$(basename "$d")/origin" | \
```

日本語：

WebsiteData/Default/*/; do echo "$(strings "$d$(basename "$d")/origin" | \


### claude-for-msft-365-install/scripts/export-addin-data.sh:19

原文：

```text
head -2 | tr '\n' ' ')  <- $(basename "$d")"; done
```

日本語：

head -2 | tr '\n' ' ')  <- $(basename "$d")"; done


### claude-for-msft-365-install/scripts/export-addin-data.sh:21

原文：

```text
Chat history is IndexedDB/<uppercase SHA-256 of "claude-chat-history">.
```

日本語：

チャット履歴の格納先は IndexedDB/ 以下の「claude-chat-history」の SHA-256 を大文字表記にしたフォルダー。


### claude-for-msft-365-install/scripts/export-addin-data.sh:22

原文：

```text
Check that hash yourself: printf 'claude-chat-history' | shasum -a 256
```

日本語：

ハッシュは次のコマンドで確認できる: printf 'claude-chat-history' | shasum -a 256


### claude-for-msft-365-install/scripts/export-addin-data.sh:23

原文：

```text
Swap "Excel" for "Word" / "Powerpoint" / "Outlook" for the other apps.
```

日本語：

他のアプリについては、パス内の "Excel" を "Word" / "Powerpoint" / "Outlook" に置き換える。


### claude-for-msft-365-install/scripts/export-addin-data.sh:26

原文：

```text
* Each Office app has its own storage, so Excel / Word / PowerPoint each
```

日本語：

* 各 Office アプリには独自のストレージがあるため、Excel / Word / PowerPoint はそれぞれ


### claude-for-msft-365-install/scripts/export-addin-data.sh:27

原文：

```text
keep separate chat history. That is expected.
```

日本語：

個別のチャット履歴を保存します。それは予想通りです。


### claude-for-msft-365-install/scripts/export-addin-data.sh:28

原文：

```text
* Unlike Windows, the path has no per-Office-account segment -- storage
```

日本語：

* Windows と異なり、パスに Office アカウントごとの区分はない。ストレージは


### claude-for-msft-365-install/scripts/export-addin-data.sh:29

原文：

```text
belongs to the macOS user account, and Office accounts signed in within
```

日本語：

macOS ユーザーアカウントに属し、その環境でサインインした Office アカウントは


### claude-for-msft-365-install/scripts/export-addin-data.sh:30

原文：

```text
it share one store. So there is nothing to pick between: this exports
```

日本語：

同じストレージを共有する。そのためアカウントを選ぶ必要はなく、


### claude-for-msft-365-install/scripts/export-addin-data.sh:31

原文：

```text
everything under the current macOS user.
```

日本語：

現在の macOS ユーザー配下のデータをすべてエクスポートする。


### claude-for-msft-365-install/scripts/export-addin-data.sh:32

原文：

```text
* Sign-in tokens are deliberately NOT exported. The export does contain
```

日本語：

* サインイン トークンは意図的にエクスポートされません。エクスポートには以下が含まれます


### claude-for-msft-365-install/scripts/export-addin-data.sh:33

原文：

```text
conversation text -- handle it under your normal data policy.
```

日本語：

会話テキスト -- 通常のデータ ポリシーに従って処理します。


### claude-for-msft-365-install/scripts/export-addin-data.sh:34

原文：

```text
* Office can stay open. The data is SQLite and this takes a consistent
```

日本語：

* Office を開いたままでもよい。データは SQLite であり、開いているデータベースから


### claude-for-msft-365-install/scripts/export-addin-data.sh:35

原文：

```text
snapshot of an open database.
```

日本語：

整合性のあるスナップショットを取得する。


### claude-for-msft-365-install/scripts/export-addin-data.sh:36

原文：

```text
* Precisely: no conversation, skill, MCP or memory record is altered, and
```

日本語：

* 正確に言うと、会話、スキル、MCP、記憶記録は変更されません。


### claude-for-msft-365-install/scripts/export-addin-data.sh:37

原文：

```text
no file is moved or deleted. Opening a SQLite database does update the
```

日本語：

ファイルも移動・削除しない。ただし SQLite データベースを開くと、


### claude-for-msft-365-install/scripts/export-addin-data.sh:38

原文：

```text
mtime of its -shm shared-memory index, so a byte-level before/after audit
```

日本語：

-shm 共有メモリインデックスの更新日時（mtime）が変わるため、処理前後のバイト単位の監査では


### claude-for-msft-365-install/scripts/export-addin-data.sh:39

原文：

```text
will show those (size unchanged). Nothing else in Office is touched.
```

日本語：

その変化が確認できる（サイズは変わらない）。Office のその他のデータには触れない。


### claude-for-msft-365-install/scripts/export-addin-data.sh:40

原文：

```text
* You do NOT need this to change add-ins. Storage is keyed by the origin
```

日本語：

* アドインを切り替えるだけなら、この操作は不要。ストレージはアドイン ID ではなく、


### claude-for-msft-365-install/scripts/export-addin-data.sh:41

原文：

```text
the add-in is served from, not by add-in ID, so replacing the manifest,
```

日本語：

アドインの配信元オリジンをキーにしている。そのため、マニフェストの差し替え、


### claude-for-msft-365-install/scripts/export-addin-data.sh:42

原文：

```text
reinstalling, or moving to the store listing leaves the data in place.
```

日本語：

再インストール、ストア版への切り替えを行っても、データはそのまま残る。


### claude-for-msft-365-install/scripts/export-addin-data.sh:43

原文：

```text
Export before a machine is rebuilt or wiped.
```

日本語：

マシンが再構築または消去される前にエクスポートします。


### claude-for-msft-365-install/scripts/export-addin-data.sh:46

原文：

```text
export-addin-data.sh              # list what is on this Mac, copy nothing
```

日本語：

export-addin-data.sh # この Mac にあるものをリストし、何もコピーしません


### claude-for-msft-365-install/scripts/export-addin-data.sh:47

原文：

```text
export-addin-data.sh --out DIR    # copy it to DIR
```

日本語：

export-addin-data.sh --out DIR # DIR にコピーします


### claude-for-msft-365-install/scripts/export-addin-data.sh:56

原文：

```text
Guard the value: a bare `--out` would otherwise make `shift 2` fail under
```

日本語：

値があるか確認する。これがないと、値なしの `--out` によって `shift 2` が


### claude-for-msft-365-install/scripts/export-addin-data.sh:57

原文：

```text
`set -e` and exit 1 with no output at all.
```

日本語：

`set -e` の下で失敗し、何も出力しないまま終了コード 1 で終了してしまう。


### claude-for-msft-365-install/scripts/export-addin-data.sh:58

原文：

```text
ERROR: --out requires a directory
```

日本語：

エラー: --out にはディレクトリが必要です


### claude-for-msft-365-install/scripts/export-addin-data.sh:60

原文：

```text
2,/^set -euo/p
```

日本語：

2,/^set -euo/p


### claude-for-msft-365-install/scripts/export-addin-data.sh:61

原文：

```text
ERROR: unknown argument: $1 (see --help)
```

日本語：

エラー: 不明な引数: $1 (--help を参照)


### claude-for-msft-365-install/scripts/export-addin-data.sh:65

原文：

```text
ERROR: sqlite3 not found on PATH
```

日本語：

エラー: sqlite3 が PATH に見つかりません


### claude-for-msft-365-install/scripts/export-addin-data.sh:66

原文：

```text
xxd ships with macOS, but a trimmed PATH would otherwise fail per-origin with
```

日本語：

xxd は macOS に付属するが、PATH を制限していると、オリジンごとに処理が失敗して、


### claude-for-msft-365-install/scripts/export-addin-data.sh:67

原文：

```text
a confusing "no stores found" rather than a real error.
```

日本語：

本来のエラーではなく紛らわしい "no stores found"（ストレージが見つからない）と表示される。


### claude-for-msft-365-install/scripts/export-addin-data.sh:67

原文：

```text
no stores found
```

日本語：

ストレージが見つかりませんでした


### claude-for-msft-365-install/scripts/export-addin-data.sh:68

原文：

```text
ERROR: xxd not found on PATH
```

日本語：

エラー: xxd が PATH 上に見つかりません


### claude-for-msft-365-install/scripts/export-addin-data.sh:72

原文：

```text
A database's folder name is the uppercase SHA-256 of its name.
```

日本語：

データベースのフォルダー名は、名前の大文字の SHA-256 です。


### claude-for-msft-365-install/scripts/export-addin-data.sh:75

原文：

```text
The `origin` file is length-prefixed binary: for each of scheme and host a
```

日本語：

`origin` ファイルは、長さのプレフィックスが付いたバイナリです。スキームとホストのそれぞれに対して、


### claude-for-msft-365-install/scripts/export-addin-data.sh:76

原文：

```text
has port
```

日本語：

ポートあり


### claude-for-msft-365-install/scripts/export-addin-data.sh:76

原文：

```text
u32 LE length, a 1-byte flag, then the string; then a 1-byte "has port" flag
```

日本語：

u32 LE 長さ、1 バイトのフラグ、その後に文字列。次に、1バイトの「ポートあり」フラグ


### claude-for-msft-365-install/scripts/export-addin-data.sh:77

原文：

```text
and, if set, a u16 LE port.
```

日本語：

設定されている場合は、u16 LE ポート。


### claude-for-msft-365-install/scripts/export-addin-data.sh:79

原文：

```text
The port has to be parsed, not skipped. Storage is per-origin and an origin
```

日本語：

ポートを読み飛ばさず解析する必要がある。ストレージはオリジンごとに分かれ、オリジンには


### claude-for-msft-365-install/scripts/export-addin-data.sh:80

原文：

```text
includes the port, so https://addins.contoso.com and
```

日本語：

ポートも含まれるため、https://addins.contoso.com と


### claude-for-msft-365-install/scripts/export-addin-data.sh:81

原文：

```text
https://addins.contoso.com:8443 are two separate stores -- labelling both
```

日本語：

https://addins.contoso.com:8443 は別々のストレージである。両方を


### claude-for-msft-365-install/scripts/export-addin-data.sh:82

原文：

```text
"addins.contoso.com" would land them in one export folder, silently
```

日本語：

"addins.contoso.com" と名付けると同じエクスポート先フォルダーに入り、気づかないうちに


### claude-for-msft-365-install/scripts/export-addin-data.sh:83

原文：

```text
overwriting the first. Self-hosted deployments hit this.
```

日本語：

先に保存した方を上書きしてしまう。セルフホスト環境ではこの問題が発生する。


### claude-for-msft-365-install/scripts/export-addin-data.sh:86

原文：

```text
$(xxd -p -c 1000000 
```

日本語：

$(xxd -p -c 1000000 


### claude-for-msft-365-install/scripts/export-addin-data.sh:93

原文：

```text
); h=$(str $((off + 5)) 
```

日本語：

); h=$(str $((off + 5)) 


### claude-for-msft-365-install/scripts/export-addin-data.sh:95

原文：

```text
$((16#${hex:$((off * 2)):2}))
```

日本語：

$((16#${hex:$((off * 2)):2}))


### claude-for-msft-365-install/scripts/export-addin-data.sh:95

原文：

```text
$s://$h:$(u16 $((off + 1)))
```

日本語：

$s://$h:$(u16 $((off + 1)))


### claude-for-msft-365-install/scripts/export-addin-data.sh:99

原文：

```text
`.backup` is a sqlite3 dot-command, not SQL, and its own quoting has no
```

日本語：

`.backup` は SQL ではなく sqlite3 のドットコマンドで、その独自の引用構文には


### claude-for-msft-365-install/scripts/export-addin-data.sh:100

原文：

```text
escape for an embedded apostrophe -- so /Users/o'brien/export would break.
```

日本語：

文字列内のアポストロフィをエスケープする方法がない。そのため /Users/o'brien/export では失敗する。


### claude-for-msft-365-install/scripts/export-addin-data.sh:101

原文：

```text
Sidestep it: run from the destination directory and pass a bare filename,
```

日本語：

回避策: 出力先ディレクトリを作業ディレクトリにして実行し、パスを含まないファイル名を渡す。


### claude-for-msft-365-install/scripts/export-addin-data.sh:102

原文：

```text
which is always IndexedDB.sqlite3 or localstorage.sqlite3. The SOURCE path is
```

日本語：

これは常に IndexedDB.sqlite3 または localstorage.sqlite3 です。ソースパスは


### claude-for-msft-365-install/scripts/export-addin-data.sh:103

原文：

```text
an ordinary argv entry, so it needs no special handling.
```

日本語：

通常の argv エントリなので、特別な処理は必要ありません。


### claude-for-msft-365-install/scripts/export-addin-data.sh:105

原文：

```text
One unreadable store must not abort the run and strand a half-finished export
```

日本語：

1 つの読み取り不可能なストアによって実行が中止され、中途半端なエクスポートが残されてはなりません。


### claude-for-msft-365-install/scripts/export-addin-data.sh:106

原文：

```text
-- record it and keep going, then report at the end.
```

日本語：

-- 記録して続け、最後にレポートします。


### claude-for-msft-365-install/scripts/export-addin-data.sh:109

原文：

```text
 && sqlite3 
```

日本語：

 && sqlite3 


### claude-for-msft-365-install/scripts/export-addin-data.sh:112

原文：

```text
    !! could not copy $(basename 
```

日本語：

    !! コピーできませんでした: $(basename 


### claude-for-msft-365-install/scripts/export-addin-data.sh:112

原文：

```text
) -- skipped
```

日本語：

) -- スキップされました


### claude-for-msft-365-install/scripts/export-addin-data.sh:117

原文：

```text
 ]; then echo 
```

日本語：

 ]; then echo 


### claude-for-msft-365-install/scripts/export-addin-data.sh:118

原文：

```text
Add-in data on this Mac (pass --out DIR to copy it):
```

日本語：

この Mac 上のアドイン データ (コピーするには --out DIR を渡します):


### claude-for-msft-365-install/scripts/export-addin-data.sh:129

原文：

```text
 || true)
```

日本語：

 || true)


### claude-for-msft-365-install/scripts/export-addin-data.sh:134

原文：

```text
 ] && present+=(
```

日本語：

 ] && present+=(


### claude-for-msft-365-install/scripts/export-addin-data.sh:139

原文：

```text
localStorage sits beside IndexedDB in the same per-origin folder. It is
```

日本語：

localStorage は、同じオリジンごとのフォルダー内の IndexedDB の隣にあります。それは


### claude-for-msft-365-install/scripts/export-addin-data.sh:140

原文：

```text
small but not redundant: settings, the inference/customer config, and the
```

日本語：

サイズは小さいが、不要な重複データではない。設定、推論/顧客の構成、および


### claude-for-msft-365-install/scripts/export-addin-data.sh:141

原文：

```text
onboarding + terms-accepted flags live here, not in IndexedDB.
```

日本語：

オンボーディング完了・利用規約同意のフラグは、IndexedDB ではなくここに保存される。


### claude-for-msft-365-install/scripts/export-addin-data.sh:144

原文：

```text
[$app] $origin
```

日本語：

[$app] $origin


### claude-for-msft-365-install/scripts/export-addin-data.sh:148

原文：

```text
local-storage (settings)
```

日本語：

ローカルストレージ (設定)


### claude-for-msft-365-install/scripts/export-addin-data.sh:152

原文：

```text
Name the destination after the app and host so the export is readable
```

日本語：

エクスポートが読み取れるように、宛先にアプリとホストにちなんで名前を付けます


### claude-for-msft-365-install/scripts/export-addin-data.sh:153

原文：

```text
 would show up as 
```

日本語：

として表示されます


### claude-for-msft-365-install/scripts/export-addin-data.sh:153

原文：

```text
without knowing anything about salted hashes. ':' would show up as '/'
```

日本語：

ソルト付きハッシュを知らなくても判別できるようにする。':' は '/' として表示されるため、


### claude-for-msft-365-install/scripts/export-addin-data.sh:154

原文：

```text
in Finder, so a non-default port becomes host_port.
```

日本語：

Finder 上ではそのように見えるため、標準以外のポートは host_port の形式にする。


### claude-for-msft-365-install/scripts/export-addin-data.sh:159

原文：

```text
`.backup` rather than cp: a consistent snapshot even with Office
```

日本語：

cp ではなく `.backup` を使用する。Office を開いたままでも整合性のあるスナップショットを作成でき、


### claude-for-msft-365-install/scripts/export-addin-data.sh:160

原文：

```text
open, and it folds in the write-ahead log.
```

日本語：

先行書き込みログ（WAL）の内容も取り込める。


### claude-for-msft-365-install/scripts/export-addin-data.sh:162

原文：

```text
Any out-of-line attachment files sit beside the SQLite file.
```

日本語：

SQLite 内に直接格納されない添付ファイルは、SQLite ファイルの隣に保存されている。


### claude-for-msft-365-install/scripts/export-addin-data.sh:170

原文：

```text
    -> $dest
```

日本語：

-> $dest


### claude-for-msft-365-install/scripts/export-addin-data.sh:177

原文：

```text
  (nothing found -- has the add-in been used on this Mac?)
```

日本語：

(何も見つかりません -- この Mac でアドインが使用されましたか?)


### claude-for-msft-365-install/scripts/export-addin-data.sh:178

原文：

```text
Listing nothing is a fine answer. Being ASKED to export and exporting
```

日本語：

一覧表示で何も見つからないこと自体は正常である。しかし、エクスポートを要求されたのに


### claude-for-msft-365-install/scripts/export-addin-data.sh:179

原文：

```text
nothing is not: `export --out DIR && rm -rf ...` would treat an empty
```

日本語：

何も出力しないのは問題である。`export --out DIR && rm -rf ...` では、空のエクスポートでも


### claude-for-msft-365-install/scripts/export-addin-data.sh:180

原文：

```text
export as a green light and destroy the only copy. Fail so it can't.
```

日本語：

成功したと判断して唯一のコピーを削除しかねない。それを防ぐため失敗として終了する。


### claude-for-msft-365-install/scripts/export-addin-data.sh:183

原文：

```text
NOTHING WAS EXPORTED to $OUT. Do not wipe anything on the strength of
```

日本語：

$OUT には何もエクスポートされませんでした。この実行結果を根拠にデータを消去しないでください。


### claude-for-msft-365-install/scripts/export-addin-data.sh:184

原文：

```text
this run. On a machine where the add-in has been used, check that Office
```

日本語：

アドインを使用したことのあるマシンの場合、Office に


### claude-for-msft-365-install/scripts/export-addin-data.sh:185

原文：

```text
is signed into the expected account, then re-run.
```

日本語：

想定したアカウントでサインインしていることを確認し、再実行してください。


### claude-for-msft-365-install/scripts/export-addin-data.sh:190

原文：

```text
Done. $found location(s) exported to $OUT
```

日本語：

完了しました。 $found の場所が $OUT にエクスポートされました


### claude-for-msft-365-install/scripts/export-addin-data.sh:191

原文：

```text
Nothing in Office was modified.
```

日本語：

Office では何も変更されていません。


### claude-for-msft-365-install/scripts/export-addin-data.sh:194

原文：

```text
WARNING: $FAILED database(s) could not be copied -- this export is INCOMPLETE.
```

日本語：

警告: $FAILED データベースをコピーできませんでした -- このエクスポートは不完全です。


