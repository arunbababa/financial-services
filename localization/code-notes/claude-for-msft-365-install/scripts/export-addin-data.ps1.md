# claude-for-msft-365-install/scripts/export-addin-data.ps1 の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/scripts/export-addin-data.ps1)

### claude-for-msft-365-install/scripts/export-addin-data.ps1:12

原文：

```text
s stores are copied -- other add-ins
```

日本語：

（Claude）のストアだけをコピーする。他のアドイン


### claude-for-msft-365-install/scripts/export-addin-data.ps1:18

原文：

```text
 and other sites
```

日本語：

および他のサイト


### claude-for-msft-365-install/scripts/export-addin-data.ps1:20

原文：

```text
Local Storage
```

日本語：

ローカルストレージ


### claude-for-msft-365-install/scripts/export-addin-data.ps1:46

原文：

```text
delete %LOCALAPPDATA%\Microsoft\Office\16.0\Wef
```

日本語：

%LOCALAPPDATA%\Microsoft\Office\16.0\Wef を削除します


### claude-for-msft-365-install/scripts/export-addin-data.ps1:62

原文：

```text
Export every IndexedDB store, skipping the "is this Claude's?" check. Use
```

日本語：

「Claudeのストアかどうか」の確認を省略し、すべてのIndexedDBストアをエクスポートする。次のような場合に使う。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:63

原文：

```text
when the add-in has clearly been used but its store is not recognised --
```

日本語：

アドインが明らかに使用されているが、そのストアが認識されない場合 --


### claude-for-msft-365-install/scripts/export-addin-data.ps1:64

原文：

```text
LevelDB compaction can hide the database names from a plaintext search.
```

日本語：

LevelDBのコンパクションにより、平文検索ではデータベース名が見つからなくなることがある。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:72

原文：

```text
No add-in storage at $wef -- the add-in has not run on this PC.
```

日本語：

$wef にアドイン ストレージがありません -- アドインはこの PC 上で実行されていません。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:76

原文：

```text
Unlike SQLite on macOS, LevelDB has no consistent online snapshot. Copying
```

日本語：

macOSのSQLiteとは異なり、LevelDBには整合性のあるオンラインスナップショットがない。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:77

原文：

```text
while Office is open can catch a store mid-write -- that only affects the
```

日本語：

Officeを開いたままコピーすると、書き込み途中のストアを取得することがある。影響するのは


### claude-for-msft-365-install/scripts/export-addin-data.ps1:78

原文：

```text
fidelity of the COPY, never the original, so warn instead of blocking.
```

日本語：

コピーの再現性だけであり、元データには決して影響しない。そのため処理を停止せず警告する。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:81

原文：

```text
Office is open (
```

日本語：

Officeが起動中（


### claude-for-msft-365-install/scripts/export-addin-data.ps1:82

原文：

```text
). Close it for a clean copy. Your existing data is not affected either way.
```

日本語：

）。整合性のあるコピーを取得するにはOfficeを閉じる。どちらの場合でも既存データは影響を受けない。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:85

原文：

```text
"https_pivot.claude.ai_0.indexeddb.leveldb" -> "pivot.claude.ai"
```

日本語：

`"https_pivot.claude.ai_0.indexeddb.leveldb" -> "pivot.claude.ai"`

ストアのディレクトリ名からホスト名への対応例。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:86

原文：

```text
Chromium names each store <scheme>_<host>_<port>.indexeddb.leveldb, using 0
```

日本語：

Chromiumは各ストアを`<scheme>_<host>_<port>.indexeddb.leveldb`と命名し、既定ポートには0を使う。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:87

原文：

```text
for the scheme's default port. Keep a non-default port in the label: storage
```

日本語：

スキームの既定ポートを表すのが0。既定以外のポートはラベルに残す。ストレージは


### claude-for-msft-365-install/scripts/export-addin-data.ps1:88

原文：

```text
is per-origin and an origin includes the port, so https://addins.contoso.com
```

日本語：

オリジン単位であり、オリジンにはポートも含まれる。そのため https://addins.contoso.com


### claude-for-msft-365-install/scripts/export-addin-data.ps1:89

原文：

```text
and https://addins.contoso.com:8443 are genuinely separate stores and must
```

日本語：

と https://addins.contoso.com:8443 は別個のストアであり、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:90

原文：

```text
not read as one.
```

日本語：

同一のストアとして表示してはならない。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:99

原文：

```text
...\<account>\2\[n]\EBWebView -> "<account>__2[__n]", a readable label.
```

日本語：

`...\<account>\2\[n]\EBWebView -> "<account>__2[__n]", a readable label.`

アカウントとプロファイルのパスを読みやすいラベルへ変換する例。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:102

原文：

```text
) -replace 
```

日本語：

`) -replace`

PowerShellの置換演算子を含むコード断片。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:106

原文：

```text
)   { return 
```

日本語：

`)   { return`

return文を含むコード断片。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:107

原文：

```text
) { return 
```

日本語：

`) { return`

return文を含むコード断片。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:108

原文：

```text
not signed in
```

日本語：

サインインしていません


### claude-for-msft-365-install/scripts/export-addin-data.ps1:111

原文：

```text
Only export stores that actually belong to the Claude add-in.
```

日本語：

実際に Claude アドインに属するストアのみをエクスポートします。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:113

原文：

```text
Office keeps one store per website, and other add-ins -- Microsoft's own
```

日本語：

OfficeはWebサイトごとにストアを保持する。他のアドインにも、Microsoft自身のアドインを


### claude-for-msft-365-install/scripts/export-addin-data.ps1:114

原文：

```text
included -- get their own stores in the same folder. A LevelDB store packs
```

日本語：

含め、同じフォルダー内に独自のストアがある。LevelDBのストアは、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:115

原文：

```text
every database for its website into one set of files, so we cannot copy
```

日本語：

そのWebサイトの全データベースを1組のファイルにまとめるため、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:116

原文：

```text
just our databases out of a store; what we CAN do is skip any store that
```

日本語：

自分たちのデータベースだけをストアからコピーすることはできない。可能なのは、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:117

原文：

```text
is not ours. This checks whether our database names appear in the bytes,
```

日本語：

自分たちのものではないストアを除外すること。この処理はデータベース名がバイト列中にあるかを確認するため、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:118

原文：

```text
which works whatever host the add-in is served from (production, a
```

日本語：

アドインの配信元ホストが何であっても動作する（本番環境、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:119

原文：

```text
government cloud, or a customer-specific deployment).
```

日本語：

政府向けクラウド、顧客専用のデプロイなど）。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:122

原文：

```text
Search the raw bytes. Decoding as ASCII is a byte search for our purposes:
```

日本語：

生のバイトを検索します。 ASCII としてデコードすることは、私たちの目的のためのバイト検索です。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:123

原文：

```text
the names are pure ASCII so those bytes round-trip exactly, the NUL bytes of
```

日本語：

名前はASCII文字のみなので、それに対応するバイトは変換して戻しても完全に保たれる。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:124

原文：

```text
the UTF-16LE form round-trip too, and any byte above 127 becomes '?' which
```

日本語：

UTF-16LE形式のNULバイトも保たれる。127を超えるバイトはすべて「?」になるが、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:125

原文：

```text
cannot accidentally spell a database name. ASCII is built into every .NET,
```

日本語：

それによって偶然データベース名ができることはない。ASCIIはすべての.NETに組み込まれており、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:126

原文：

```text
unlike the code-page encodings, so this works on Windows PowerShell 5.1 and
```

日本語：

コードページのエンコーディングとは異なるため、Windows PowerShell 5.1でも


### claude-for-msft-365-install/scripts/export-addin-data.ps1:127

原文：

```text
PowerShell 7 alike.
```

日本語：

PowerShell 7も同様です。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:134

原文：

```text
Read in chunks rather than slurping whole files: a heavy user's store can be
```

日本語：

ファイル全体を一括読み込みせず、チャンク単位で読む。利用量の多いユーザーのストアは


### claude-for-msft-365-install/scripts/export-addin-data.ps1:135

原文：

```text
hundreds of MB, and skipping big files would silently drop exactly the
```

日本語：

数百MBになることがあり、大きなファイルを除外すると、まさに最も大量の履歴を


### claude-for-msft-365-install/scripts/export-addin-data.ps1:136

原文：

```text
largest history from the export. The overlap keeps a name that straddles a
```

日本語：

エクスポートから通知なく落としてしまう。チャンクを一部重ねて読むことで、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:137

原文：

```text
chunk boundary from being missed.
```

日本語：

チャンク境界をまたぐ名前の見落としを防ぐ。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:141

原文：

```text
Order matters for speed AND for hit rate. LevelDB keeps recent writes in the
```

日本語：

処理順序は速度と検出率の両方に影響する。LevelDBは最近の書き込みを


### claude-for-msft-365-install/scripts/export-addin-data.ps1:142

原文：

```text
uncompressed write-ahead log and MANIFEST; only compacted .ldb blocks are
```

日本語：

非圧縮の先行書き込みログとMANIFESTに保持する。Snappy圧縮されるのは


### claude-for-msft-365-install/scripts/export-addin-data.ps1:143

原文：

```text
Snappy-compressed, where a plaintext name may not appear at all. Read the
```

日本語：

コンパクション済みの.ldbブロックだけで、そこでは平文の名前が一切現れない場合がある。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:144

原文：

```text
cheap uncompressed files first, smallest to largest, so the common case
```

日本語：

読み取りコストの低い非圧縮ファイルを、小さい順に先に読む。これにより一般的なケースでは


### claude-for-msft-365-install/scripts/export-addin-data.ps1:145

原文：

```text
answers in milliseconds instead of scanning hundreds of MB per store.
```

日本語：

ストアごとに数百MBを走査せずに、ミリ秒単位で判定できる。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:171

原文：

```text
No Claude add-in storage found under $wef.
```

日本語：

$wef の下にクロード アドイン ストレージが見つかりません。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:173

原文：

```text
Detection is a plaintext search, and LevelDB compaction can Snappy-compress
```

日本語：

検出は平文検索であり、LevelDBのコンパクションでデータベース名がSnappy圧縮され、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:174

原文：

```text
none matched
```

日本語：

どれも一致しませんでした


### claude-for-msft-365-install/scripts/export-addin-data.ps1:174

原文：

```text
the database names out of reach. So "none matched" is not proof of absence
```

日本語：

検索できなくなることがある。したがって「一致なし」は、ストアが


### claude-for-msft-365-install/scripts/export-addin-data.ps1:175

原文：

```text
when stores DO exist -- name them and let the admin decide.
```

日本語：

存在するときにデータがない証拠にはならない。ストア名を列挙し、管理者に判断してもらう。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:178

原文：

```text
`nIf one of those is the add-in, re-run with -IncludeAll to export them all.
```

日本語：

```nIf one of those is the add-in, re-run with -IncludeAll to export them all.``

改行後に表示する案内：いずれかのストアがアドインのものなら、-IncludeAllで再実行し全ストアをエクスポートする。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:182

原文：

```text
Asked to export and exported nothing: never let that read as success, or
```

日本語：

エクスポート要求に対して何も出力しなかった場合は、決して成功に見せてはならない。そうしないと、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:183

原文：

```text
`export -Out ... ; wipe` treats an empty backup as a green light.
```

日本語：

`export -Out ... ; wipe` が、空のバックアップを削除開始の合図と扱ってしまう。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:185

原文：

```text
`nNOTHING WAS EXPORTED to $Out. Do not wipe anything based on this run.
```

日本語：

```nNOTHING WAS EXPORTED to $Out. Do not wipe anything based on this run.``

改行後の警告：$Outには何もエクスポートされていない。この実行結果を根拠にデータを削除してはならない。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:186

原文：

```text
Check that Office is signed into the expected account, then re-run.
```

日本語：

Office が予期したアカウントにサインインしていることを確認してから、再実行します。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:192

原文：

```text
Exporting to $Out
```

日本語：

$Out へのエクスポート


### claude-for-msft-365-install/scripts/export-addin-data.ps1:193

原文：

```text
Claude add-in data on this PC (pass -Out <dir> to copy it):
```

日本語：

この PC 上のクロード アドイン データ (コピーするには、 -Out <dir> を渡します):


### claude-for-msft-365-install/scripts/export-addin-data.ps1:194

原文：

```text
Ignoring $skipped store(s) belonging to other add-ins.
```

日本語：

他のアドインに属する $skipped ストアを無視します。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:202

原文：

```text
...\EBWebView\Default\IndexedDB\<store> -> ...\EBWebView
```

日本語：

`...\EBWebView\Default\IndexedDB\<store> -> ...\EBWebView`

IndexedDBストアからプロファイルのディレクトリまで戻るパス対応。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:206

原文：

```text
NB: .BaseName is NOT extension-stripped for a directory -- swap the
```

日本語：

注意：ディレクトリでは.BaseNameから拡張子が除去されない。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:207

原文：

```text
suffix explicitly or the attachment folder is missed.
```

日本語：

接尾辞を明示的に置き換えなければ、添付ファイルのフォルダーを見落とす。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:212

原文：

```text
https://{0}   [{1}]
```

日本語：

https://{0}   [{1}]


### claude-for-msft-365-install/scripts/export-addin-data.ps1:213

原文：

```text
    data         {0,10:N0} bytes
```

日本語：

データ {0,10:N0} バイト


### claude-for-msft-365-install/scripts/export-addin-data.ps1:216

原文：

```text
    attachments  {0,10:N0} bytes
```

日本語：

添付ファイル {0,10:N0} バイト


### claude-for-msft-365-install/scripts/export-addin-data.ps1:220

原文：

```text
':' is illegal in a Windows path, so a ported origin becomes host_port.
```

日本語：

Windowsのパスには「:」を使えないため、ポート番号を持つオリジンはhost_port形式にする。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:223

原文：

```text
Copy-Item -Recurse into an EXISTING directory nests it (dest\store\store)
```

日本語：

Copy-Item -Recurseで既存ディレクトリにコピーすると、内容を更新せず、入れ子（dest\store\store）になる。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:224

原文：

```text
rather than refreshing it, so a re-run would hide the good copy one level
```

日本語：

そのため再実行すると、正常なコピーが1階層下に隠れ、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:225

原文：

```text
down and leave the first, possibly torn, copy on top. Clear it first.
```

日本語：

最初の、不整合を含むかもしれないコピーが上位に残る。先にコピー先を消去する。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:233

原文：

```text
    -> $dest
```

日本語：

-> $dest


### claude-for-msft-365-install/scripts/export-addin-data.ps1:238

原文：

```text
--- localStorage: one shared LevelDB per PROFILE, not per origin ------------
```

日本語：

--- localStorage: オリジンごとではなく、PROFILE ごとに 1 つの共有 LevelDB ------------


### claude-for-msft-365-install/scripts/export-addin-data.ps1:239

原文：

```text
Settings, the inference/customer config, and the onboarding + terms flags all
```

日本語：

設定、推論/顧客設定、オンボーディングと利用規約のフラグはすべて、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:240

原文：

```text
live here rather than in IndexedDB. Chromium gives every origin on a profile
```

日本語：

IndexedDBではなくここにある。Chromiumは同じプロファイルのすべてのオリジンに


### claude-for-msft-365-install/scripts/export-addin-data.ps1:241

原文：

```text
the same store, so it cannot be split per add-in -- it is copied whole.
```

日本語：

同一のストアを使うため、アドイン単位に分割できず、全体をコピーする。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:243

原文：

```text
Driven off the profile list rather than the store loop: a profile whose only
```

日本語：

ストアのループではなく、プロファイル一覧を基準に処理する。そうしなければ、唯一の


### claude-for-msft-365-install/scripts/export-addin-data.ps1:244

原文：

```text
store fails the origin-name parse would otherwise lose its settings silently.
```

日本語：

ストアのフォルダー名からオリジンを解析できないプロファイルで、設定が通知なく欠落する。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:251

原文：

```text
Default\Local Storage
```

日本語：

`Default\Local Storage`

Local Storageのディレクトリパス。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:256

原文：

```text
local storage  [{0}]  {1:N0} bytes  -- WHOLE profile store, all origins
```

日本語：

local storage [{0}] {1:N0} bytes — 全オリジンを含むプロファイルのストア全体


### claude-for-msft-365-install/scripts/export-addin-data.ps1:259

原文：

```text
Local Storage
```

日本語：

ローカルストレージ


### claude-for-msft-365-install/scripts/export-addin-data.ps1:261

原文：

```text
Copy to a scratch name and swap only on success. Deleting the old copy
```

日本語：

一時名へコピーし、成功したときだけ置き換える。古いコピーを


### claude-for-msft-365-install/scripts/export-addin-data.ps1:262

原文：

```text
first would mean a locked LOCK file (Office still running) leaves the
```

日本語：

先に削除すると、Officeが起動中でLOCKファイルがロックされている場合に、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:263

原文：

```text
export with neither the new copy nor the previous good one.
```

日本語：

新しいコピーも以前の正常なコピーもエクスポート先に残らなくなる。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:269

原文：

```text
Local Storage
```

日本語：

ローカルストレージ


### claude-for-msft-365-install/scripts/export-addin-data.ps1:270

原文：

```text
    -> $lsDest
```

日本語：

-> $lsDest


### claude-for-msft-365-install/scripts/export-addin-data.ps1:273

原文：

```text
    !! could not copy Local Storage for $acct -- skipped ($($_.Exception.Message))
```

日本語：

!! $acct のローカル ストレージをコピーできませんでした -- スキップされました ($($_.Exception.Message))


### claude-for-msft-365-install/scripts/export-addin-data.ps1:281

原文：

```text
$n can still be 0 here if every store's folder name failed to parse, so
```

日本語：

すべてのストアのフォルダー名が解析できなかった場合でも、$n は 0 になる可能性があるため、


### claude-for-msft-365-install/scripts/export-addin-data.ps1:282

原文：

```text
check the count rather than assuming the loop above copied something.
```

日本語：

上記のループが何かをコピーしたと仮定するのではなく、カウントを確認してください。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:284

原文：

```text
NOTHING WAS EXPORTED to $Out. Do not wipe anything based on this run.
```

日本語：

$Out には何もエクスポートされませんでした。この実行に基づいて何もワイプしないでください。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:287

原文：

```text
Done. $n location(s) exported to $Out
```

日本語：

完了しました。 $n 個の場所が $Out にエクスポートされました


### claude-for-msft-365-install/scripts/export-addin-data.ps1:288

原文：

```text
Nothing in Office was modified.
```

日本語：

Office では何も変更されていません。


### claude-for-msft-365-install/scripts/export-addin-data.ps1:291

原文：

```text
WARNING: Local Storage for $lsFailed profile(s) could not be copied --
```

日本語：

警告: $lsFailed プロファイルのローカル ストレージをコピーできませんでした --


### claude-for-msft-365-install/scripts/export-addin-data.ps1:292

原文：

```text
settings are MISSING from this export. Close Office and re-run.
```

日本語：

このエクスポートには設定がありません。 Office を閉じて再実行します。
