---
name: verify
description: Verify changes to the claude-for-msft-365-install admin scripts and commands by driving them against an isolated fake $HOME.
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../claude-for-msft-365-install/.claude/skills/verify/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：claude-for-msft-365-install 管理スクリプトとコマンドへの変更を、分離された偽の $HOME に対して実行して検証します。

<a id="verifying-claude-for-msft-365-install"></a>
# claude-for-msft-365-install の検証

このプラグインは、アプリではなく**管理者向けCLIツール**です。ビルド対象や
起動するサーバーはありません。操作対象はターミナルで、macOSでは`scripts/*.sh`、
Windowsでは`scripts/*.ps1`を使用します。

<a id="lint-gate"></a>
## リントゲート

```bash
python3 scripts/check.py           # from the REPO ROOT, not the plugin dir
bash -n claude-for-msft-365-install/scripts/<script>.sh
```

`check.py`はすべてのマニフェストを検査し、`.claude-plugin/plugin.json`のパッチバージョンを上げる
pre-commitフックを自動設定します。コミット前に実行してください。

<a id="drive-the-scripts-against-a-fake-home"></a>
## 偽の $HOME に対してスクリプトを実行する

すべてのmacOSスクリプトは`$HOME`を基準にOfficeのパスを決めるため、これを上書きすると
使い捨てのサンドボックスになります。破壊的な変更を行う`--apply`の処理経路も、
実際のOfficeデータに触れずに試せます。

```bash
S=<scratchpad>/sandbox
for app in Excel Word Powerpoint; do
  mkdir -p "$S/Library/Containers/com.microsoft.$app/Data/Documents/wef"
done
printf '<x/>' > "$S/Library/Containers/com.microsoft.Excel/Data/Documents/wef/aaaaaaaa-1111-1111-1111-111111111111.manifest-a.xml"

HOME=$S ./scripts/clear-addin-cache.sh                      # list
HOME=$S ./scripts/clear-addin-cache.sh --id <GUID>          # dry-run
HOME=$S ./scripts/clear-addin-cache.sh --id <GUID> --apply  # destructive
```

**二つのアプリにまたがる少なくとも二つのID**を、**大文字と小文字を混在**させて用意します。
この二つの条件は実際のバグを検出しました。アプリを越えた影響範囲と、大文字・小文字を区別するglobが
「すでにクリア済み」と誤報して管理者をフォルダー全体の削除へ誘導した問題です。

<a id="prove-storage-is-retained"></a>
## ストレージが保持されていることを証明する

このプラグインの重要な前提は、マニフェストの削除がユーザーのチャット履歴に
決して触れないことです。操作前後に両方のディレクトリツリーのスナップショットを比較し、
**実際の**`$HOME`に対して確認してください。

```bash
snap() {
  for app in Excel Word Powerpoint; do
    find "$HOME/Library/Containers/com.microsoft.$app/Data/Library/WebKit/WebsiteData" \
         -type f -exec stat -f '%N %z %m' {} \; 2>/dev/null
    find "$HOME/Library/Containers/com.microsoft.$app/Data/Documents/wef" \
         -type f -exec stat -f 'WEF %N %z' {} \; 2>/dev/null
  done | sort
}
snap > before.txt;  <run the script>;  snap > after.txt;  diff before.txt after.txt
```

マニフェストは`Data/Documents/wef`に、ストレージは
`Data/Library/WebKit/WebsiteData`にあります。異なるサブツリーなので、差分には
削除したマニフェストだけが現れるはずです。**テスト用に置いたファイルはすべて元に戻し、再度差分を確認して、
端末を作業前の状態に戻したことを確認してください。**

<a id="gotchas"></a>
## 注意点

- **Bashツールはzshを実行します。** スクリプトは`#!/usr/bin/env bash`です。bash固有の動作
  （`shopt`、globの解釈等）は、インラインではなく`bash <<'EOF' … EOF`の中でテストします。
- **エクスポートしたIndexedDBファイルでは、`PRAGMA integrity_check`と`SELECT count(*)`が
  `no such collation sequence: IDBKEY`で失敗します。** これはWebKit固有の
  照合順序が原因で、破損ではありません。元ファイルでも失敗します。両方に対して
  `SELECT sum(length(value)) FROM Records;`を実行し、欠落がないことを確認します。
- **`.ps1` スクリプトは Windows 上で実行せずに動作すると主張しないでください。**
  macOSにはPowerShellがないため、ここでしか検証していない`.ps1`の変更は未検証です。
  実際の Windows ホスト上で Windows PowerShell 5.1 に対して実行し、常に
  動作チェックの前に **解析チェック**を含めます。

  ```powershell
  $e = $null
  [System.Management.Automation.PSParser]::Tokenize(
    (Get-Content -Raw .\clear-addin-cache.ps1), [ref]$e) | Out-Null
  if ($e.Count) { $e | ForEach-Object { $_.Message } } else { 'parse ok' }
  ```

  ファイルがmacOS上の検査では問題なくても、Windowsでは構文解析に完全に失敗することがあります。
  （後述のASCIIに関する注意を参照。）したがって、まず構文解析できることを確かめます。

- **`.ps1` ファイルは純粋な ASCII である必要があります** (`scripts/check.py` によって強制されます)。
  Windows PowerShell 5.1はBOMのない`.ps1`をANSIとして読むため、emダッシュが
  `"`を含む文字化けを生じさせ、文字列を終端して構文解析を壊す場合があります。
  `clear-addin-cache.ps1`はこの問題を含む状態で公開され、macOS上の検査では検出されませんでした。
- 引数パーサーを確認します。値を伴わない`--flag`を最後の引数にすると、`shift 2`が
  `set -e`の下で失敗し、**何も出力せず**終了コード1で終わります。各フラグには
  `[ $# -ge 2 ]`のガードが必要です。
