# scripts/version_bump.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/version_bump.py)

### scripts/version_bump.py:2

原文：

```text

Single source of truth for plugin version-bump enforcement.

A plugin's `.claude-plugin/plugin.json` `version` gates update delivery to
already-installed users (Claude Code only re-delivers a plugin when its
version changes). This script guarantees that any plugin modified on a
branch ends up exactly one patch ahead of `main` — bumped once, not once
per commit.

Modes
  --apply   Mutating. For every plugin with staged changes whose version is
            not yet ahead of the base ref, patch-bump it (base + 1) and
            `git add` the result. Idempotent: a plugin already ahead of base
            is left untouched, so repeated commits on a branch bump once.
            Used by .githooks/pre-commit.

  --check   Read-only. For every plugin changed between the base ref and
            HEAD, fail (exit 1) if its version is not strictly greater than
            the base ref's version. Used by .github/workflows/version-bump.yml
            as a backstop for contributors without the local hook.

Base ref resolution (in order): explicit --base, origin/main, main.
Exit 0 clean, 1 on a --check violation, 2 on an internal error.
Requires: git, python3 (stdlib only).

```

日本語：

プラグインのバージョン更新要件を強制するための唯一の基準。

プラグインの`.claude-plugin/plugin.json`にある`version`が、既存のインストール利用者への更新配信を制御する。Claude Codeがプラグインを再配信するのは、バージョンが変わったときだけ。このスクリプトは、ブランチ上で変更されたプラグインのバージョンが`main`からちょうどパッチ1つ分進むようにする。コミットごとではなく、そのブランチで1回だけ更新する。

モード：
- `--apply`：ファイルを変更する。ステージ済みの変更がある各プラグインのうち、バージョンがまだ基準参照より先に進んでいないものを、基準のパッチ番号+1へ更新し、結果を`git add`する。冪等なので、すでに基準より進んでいるプラグインは変更せず、同一ブランチで繰り返しコミットしても更新は1回だけ。`.githooks/pre-commit`で使用する。
- `--check`：読み取り専用。基準参照からHEADまでの間に変更された各プラグインについて、バージョンが基準参照のバージョンより厳密に大きくなければ失敗（終了コード1）。ローカルフックを使わない貢献者への補完として`.github/workflows/version-bump.yml`で使用する。

基準参照は、明示的な`--base`、`origin/main`、`main`の順で解決する。
終了コードは正常時0、`--check`違反時1、内部エラー時2。
必要なもの：git、python3（標準ライブラリのみ）。


### scripts/version_bump.py:39

原文：

```text
Run a git command, returning stdout (stripped). Raises on failure.
```

日本語：

gitコマンドを実行し、前後の空白を除いた標準出力を返す。失敗時は例外を送出する。


### scripts/version_bump.py:49

原文：

```text
Run a git command, returning stdout or None if it fails.
```

日本語：

gitコマンドを実行し、成功時は標準出力、失敗時はNoneを返す。


### scripts/version_bump.py:64

原文：

```text
Every <plugin>/.claude-plugin/plugin.json in the repo.
```

日本語：

リポジトリ内のすべての <plugin>/.claude-plugin/plugin.json。


### scripts/version_bump.py:72

原文：

```text
<root>/.claude-plugin/plugin.json -> <root>
```

日本語：

`<root>/.claude-plugin/plugin.json -> <root>`

plugin.jsonのパスからプラグインのルートを求める対応。


### scripts/version_bump.py:81

原文：

```text
Parse 'x.y.z' into a comparable tuple. None if not parseable.
```

日本語：

'x.y.z'を比較可能なタプルへ解析する。解析不能ならNone。


### scripts/version_bump.py:86

原文：

```text
type: ignore[return-value]
```

日本語：

`type: ignore[return-value]`

型検査のreturn-valueエラーを抑制する指定。


### scripts/version_bump.py:94

原文：

```text
Unparseable base — start a clean patch series.
```

日本語：

解析不可能なベース — クリーンパッチシリーズを開始します。


### scripts/version_bump.py:100

原文：

```text
The plugin's version at the base ref, or None if it didn't exist there.
```

日本語：

ベース参照にあるプラグインのバージョン、またはそこに存在しない場合は None。


### scripts/version_bump.py:118

原文：

```text
True if the working version is strictly greater than the base version.
```

日本語：

作業バージョンが基本バージョンよりも厳密に大きい場合は True。


### scripts/version_bump.py:120

原文：

```text
Plugin is new on this branch — nothing to be 'ahead' of.
```

日本語：

プラグインはこのブランチでは新しいものです。「先立つ」ものは何もありません。


### scripts/version_bump.py:124

原文：

```text
Can't compare numerically — fall back to 'changed string == bump'.
```

日本語：

数値的に比較できません。「変更された文字列 == バンプ」にフォールバックします。


### scripts/version_bump.py:130

原文：

```text
Plugin roots touched relative to base (staged set, or base...HEAD).
```

日本語：

基準に対して変更されたプラグインのルートディレクトリ一覧（ステージ済みの集合、またはbase...HEADの差分）。


### scripts/version_bump.py:154

原文：

```text
already bumped on this branch — idempotent no-op
```

日本語：

このブランチではすでにバンプされています - 冪等の no-op


### scripts/version_bump.py:174

原文：

```text
). Bump .claude-plugin/plugin.json version (or run scripts/check.py once to install the pre-commit hook).
```

日本語：

）。.claude-plugin/plugin.jsonのversionを更新する（またはscripts/check.pyを1回実行してpre-commitフックをインストールする）。


### scripts/version_bump.py:174

原文：

```text
: changed but version not bumped (
```

日本語：

: 変更されましたが、バージョンは変更されませんでした (


### scripts/version_bump.py:180

原文：

```text
 plugin(s) changed without a version bump:

```

日本語：

バージョンを上げることなく変更されたプラグイン:


### scripts/version_bump.py:180

原文：

```text
FAIL — 
```

日本語：

失敗 —


### scripts/version_bump.py:186

原文：

```text
OK — all changed plugins have a version bump.
```

日本語：

OK – 変更されたすべてのプラグインにはバージョンバンプがあります。


### scripts/version_bump.py:191

原文：

```text
Plugin version-bump enforcement.
```

日本語：

プラグインのバージョンバンプの適用。


### scripts/version_bump.py:193

原文：

```text
bump staged plugins (pre-commit)
```

日本語：

ステージ済みのプラグインのバージョンを更新する（pre-commit）


### scripts/version_bump.py:194

原文：

```text
verify changed plugins are bumped (CI)
```

日本語：

変更されたプラグインがバンプされていることを確認する (CI)


### scripts/version_bump.py:195

原文：

```text
base ref (default: origin/main, then main)
```

日本語：

基準参照（既定値：origin/main、なければmain）


### scripts/version_bump.py:200

原文：

```text
No base to compare against (e.g. fresh shallow clone offline).
```

日本語：

比較対象の基準がない（例：オフラインで新規作成した浅いクローン）。


### scripts/version_bump.py:201

原文：

```text
Never block a commit over this; CI has full history as the backstop.
```

日本語：

この理由でコミットを止めない。CIには補完用の完全な履歴がある。


### scripts/version_bump.py:202

原文：

```text
[version-bump] no base ref found; skipping.
```

日本語：

[version-bump] ベース参照が見つかりません。スキップする。
