# scripts/check.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/check.py)

### scripts/check.py:2

原文：

```text

Lint all plugin + managed-agent manifests and verify cross-file references.

Checks:
  1. Every *.yaml under managed-agents/ parses.
  2. Every plugin.json / marketplace.json / steering-examples.json parses.
  3. Every <vertical>/agents/*.md has valid YAML frontmatter with name + description.
  4. Every system.file, skills[].path, callable_agents[].manifest in agent.yaml
     and subagent yamls resolves to an existing file/dir.
  5. Every managed-agents/<slug>/ has agent.yaml, README.md, steering-examples.json.

Exit 0 if clean, 1 otherwise. Requires: pyyaml.

```

日本語：

すべてのプラグインおよび管理対象エージェントのマニフェストを lint し、ファイル間の参照を検証する。

確認項目:
1. managed-agents/ 配下のすべての *.yaml を解析できること。
2. すべての plugin.json / marketplace.json / steering-examples.json を解析できること。
3. すべての <vertical>/agents/*.md に、name と description を持つ有効な YAML フロントマターがあること。
4. agent.yaml とサブエージェントの YAML 内にある system.file、skills[].path、callable_agents[].manifest が、存在するファイルまたはディレクトリを参照していること。
5. すべての managed-agents/<slug>/ に agent.yaml、README.md、steering-examples.json があること。

問題がなければ終了コード 0、それ以外は 1。pyyaml が必要。


### scripts/check.py:28

原文：

```text
Point git at .githooks so the version-bump pre-commit runs.

    Native equivalent of Husky's `prepare`, piggybacked on the script
    everyone already runs before committing. Best-effort: never fatal.
    
```

日本語：

Git のフックディレクトリを .githooks に設定し、バージョン更新用の pre-commit フックが動くようにする。

Husky の `prepare` に相当する処理を Git の標準機能で行い、皆がコミット前に実行する既存スクリプトへ組み込む。設定できなくても致命的なエラーにはしない。


### scripts/check.py:44

原文：

```text
[check.py] installed git hooks (core.hooksPath -> 
```

日本語：

[check.py] git フックをインストールしました (core.hooksPath ->


### scripts/check.py:46

原文：

```text
not a git checkout / git unavailable — ignore
```

日本語：

git checkout ではない / git が利用できない — 無視してください


### scripts/check.py:49

原文：

```text
Install hooks before anything that can exit early (e.g. missing pyyaml),
```

日本語：

早期に終了できるもの (pyyaml が欠落しているなど) の前にフックをインストールします。


### scripts/check.py:50

原文：

```text
so a fresh checkout still gets the version-bump hook wired up.
```

日本語：

そのため、新たなチェックアウトでもバージョン バンプ フックが接続されます。


### scripts/check.py:56

原文：

```text
ERROR: requires pyyaml (pip install pyyaml)
```

日本語：

エラー: pyyaml が必要です (pip install pyyaml)


### scripts/check.py:68

原文：

```text
--- 1. YAML parse ----------------------------------------------------------
```

日本語：

--- 1. YAML 解析 ------------------------------------------------------


### scripts/check.py:75

原文：

```text
YAML parse: 
```

日本語：

YAML 解析:


### scripts/check.py:77

原文：

```text
--- 2. JSON parse ----------------------------------------------------------
```

日本語：

--- 2. JSON 解析 ------------------------------------------------------


### scripts/check.py:89

原文：

```text
JSON parse: 
```

日本語：

JSON 解析:


### scripts/check.py:91

原文：

```text
--- 3. agent.md frontmatter -----------------------------------------------
```

日本語：

--- 3.agent.md フロントマター --------------------------------------


### scripts/check.py:96

原文：

```text
: missing leading ---
```

日本語：

: 先頭が欠落しています ---


### scripts/check.py:103

原文：

```text
: missing '
```

日本語：

: がありません '


### scripts/check.py:108

原文：

```text
--- 4. reference resolution -----------------------------------------------
```

日本語：

--- 4. 参照先の解決 ---


### scripts/check.py:113

原文：

```text
already reported above
```

日本語：

すでに上で報告されています


### scripts/check.py:120

原文：

```text
 (not found)
```

日本語：

(見つかりませんでした)


### scripts/check.py:120

原文：

```text
: system.file -> 
```

日本語：

: system.file -> 


### scripts/check.py:126

原文：

```text
 (not found)
```

日本語：

(見つかりませんでした)


### scripts/check.py:126

原文：

```text
: skills.path -> 
```

日本語：

: skills.path -> 


### scripts/check.py:130

原文：

```text
 (no skills/ dir)
```

日本語：

（skills/ ディレクトリなし）


### scripts/check.py:130

原文：

```text
: skills.from_plugin -> 
```

日本語：

: skills.from_plugin -> 


### scripts/check.py:136

原文：

```text
 (not found)
```

日本語：

(見つかりませんでした)


### scripts/check.py:136

原文：

```text
: callable_agents.manifest -> 
```

日本語：

: callable_agents.manifest -> 


### scripts/check.py:142

原文：

```text
--- 4b. agent-plugin bundled skills match vertical source -----------------
```

日本語：

--- 4b。エージェント プラグインにバンドルされたスキルが垂直ソースと一致する -----------------


### scripts/check.py:143

原文：

```text
noqa: E402
```

日本語：

noqa: E402


### scripts/check.py:144

原文：

```text
noqa: E402
```

日本語：

noqa: E402


### scripts/check.py:152

原文：

```text
: no vertical-plugins source named '
```

日本語：

: vertical-plugins に次の名前のソースがない: '


### scripts/check.py:157

原文：

```text
 (run scripts/sync-agent-skills.py)
```

日本語：

（scripts/sync-agent-skills.py を実行）


### scripts/check.py:157

原文：

```text
: drifted from 
```

日本語：

: 次の元データと内容が不一致: 


### scripts/check.py:161

原文：

```text
--- 4b2. agent.md skill references exist in the agent's own bundle --------
```

日本語：

--- 4b2。 Agent.md スキル参照はエージェント自身のバンドルに存在します --------


### scripts/check.py:169

原文：

```text
/ is not bundled
```

日本語：

/ がバンドルに含まれていない


### scripts/check.py:169

原文：

```text
: references `
```

日本語：

: 参照 `


### scripts/check.py:169

原文：

```text
` but plugins/agent-plugins/
```

日本語：

` ただし、plugins/agent-plugins/


### scripts/check.py:173

原文：

```text
--- 4c. marketplace source paths resolve ----------------------------------
```

日本語：

--- 4c。マーケットプレイスのソース パスの解決 ----------------------------------


### scripts/check.py:178

原文：

```text
 (no plugin.json)
```

日本語：

(plugin.json はありません)


### scripts/check.py:178

原文：

```text
 source -> 
```

日本語：

ソース ->


### scripts/check.py:180

原文：

```text
--- 5. required files per managed-agent -----------------------------------
```

日本語：

--- 5. 管理対象エージェントごとに必要なファイル -----------------------------------


### scripts/check.py:188

原文：

```text
--- 6. PowerShell scripts must be pure ASCII -------------------------------
```

日本語：

--- 6. PowerShell スクリプトは純粋な ASCII でなければなりません -----------------------------


### scripts/check.py:189

原文：

```text
Windows PowerShell 5.1 -- still the default shell on managed Windows -- reads
```

日本語：

管理下の Windows で現在も標準シェルである Windows PowerShell 5.1 は、


### scripts/check.py:190

原文：

```text
a .ps1 with no BOM using the machine's ANSI code page, not UTF-8. A smart dash
```

日本語：

BOM のない .ps1 を UTF-8 ではなくマシンの ANSI コードページとして読み込む。そのため長いダッシュや


### scripts/check.py:191

原文：

```text
or curly quote then decodes to mojibake that can contain a literal '"',
```

日本語：

曲線型の引用符が文字化けし、文字としてのダブルクォート（'"'）を含むことがある。


### scripts/check.py:192

原文：

```text
which terminates a string mid-file and makes the whole script fail to PARSE.
```

日本語：

その結果、文字列がファイルの途中で閉じられ、スクリプト全体の構文解析に失敗する。


### scripts/check.py:193

原文：

```text
It is invisible on macOS and total on Windows, so gate it here.
```

日本語：

macOS では問題が見えず、Windows では全体が動作しなくなるため、ここで検査する。


### scripts/check.py:201

原文：

```text
an explicit BOM tells PS 5.1 it is UTF-8; then non-ASCII is fine
```

日本語：

明示的な BOM は PS 5.1 にそれが UTF-8 であることを伝えます。それなら非ASCIIでも大丈夫です


### scripts/check.py:207

原文：

```text
 in a .ps1 with no UTF-8 BOM -- Windows PowerShell 5.1 will mis-decode this and may fail to parse the file. Use ASCII (-- for an em dash) or add a BOM.
```

日本語：

UTF-8 BOM のない .ps1 内 -- Windows PowerShell 5.1 はこれを誤ってデコードし、ファイルの解析に失敗する可能性があります。 ASCII (全角ダッシュの場合は --) を使用するか、BOM を追加します。


### scripts/check.py:207

原文：

```text
: byte(s) 
```

日本語：

: バイト


### scripts/check.py:213

原文：

```text
--- report ----------------------------------------------------------------
```

日本語：

--- レポート ----------------------------------------------------------------


### scripts/check.py:215

原文：

```text
 issue(s) across 
```

日本語：

全体にわたる問題


### scripts/check.py:215

原文：

```text
FAIL — 
```

日本語：

失敗 —


### scripts/check.py:219

原文：

```text
 file(s) checked, 0 issues.
```

日本語：

ファイルをチェックしましたが、問題はありませんでした。


