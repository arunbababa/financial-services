# scripts/deploy-managed-agent.sh の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/deploy-managed-agent.sh)

### scripts/deploy-managed-agent.sh:2

原文：

```text
Deploy a managed-agent template to POST /v1/agents.
```

日本語：

管理対象エージェント テンプレートを POST /v1/agents にデプロイします。


### scripts/deploy-managed-agent.sh:4

原文：

```text
Resolves manifest conveniences before posting:
```

日本語：

POSTする前に、マニフェストの簡略記法を次のように展開する：


### scripts/deploy-managed-agent.sh:5

原文：

```text
system: {file: ...}                  -> inlined string
```

日本語：

`system: {file: ...}                  -> inlined string`

systemのfile指定をファイル内容の文字列へ展開する。


### scripts/deploy-managed-agent.sh:6

原文：

```text
skills: [{path: ...}]                -> uploaded, referenced by skill_id
```

日本語：

`skills: [{path: ...}]                -> uploaded, referenced by skill_id`

pathで指定されたスキルをアップロードし、skill_idで参照する。


### scripts/deploy-managed-agent.sh:7

原文：

```text
callable_agents: [{manifest: ...}]   -> created first, referenced by agent id
```

日本語：

`callable_agents: [{manifest: ...}]   -> created first, referenced by agent id`

manifestで指定された呼び出し可能エージェントを先に作り、エージェントIDで参照する。


### scripts/deploy-managed-agent.sh:9

原文：

```text
Reader subagents with an `output_schema` block get a thin validation wrapper
```

日本語：

output_schemaを持つ読み取り担当のサブエージェントには、最小限の検証ラッパーを付ける。


### scripts/deploy-managed-agent.sh:10

原文：

```text
so their JSON is schema-checked before the orchestrator consumes it.
```

日本語：

そのため、JSON はオーケストレーターが使用する前にスキーマ チェックされます。


### scripts/deploy-managed-agent.sh:12

原文：

```text
Usage: scripts/deploy-managed-agent.sh <slug>
```

日本語：

使用法: scripts/deploy-managed-agent.sh <slug>


### scripts/deploy-managed-agent.sh:13

原文：

```text
e.g. scripts/deploy-managed-agent.sh gl-reconciler
```

日本語：

例: scripts/deploy-managed-agent.sh gl-reconciler


### scripts/deploy-managed-agent.sh:17

原文：

```text
${1:?usage: deploy-managed-agent.sh <slug> [--dry-run]}
```

日本語：

`${1:?usage: deploy-managed-agent.sh <slug> [--dry-run]}`

第1引数が未設定なら、使用法を示してエラーにするシェル式。


### scripts/deploy-managed-agent.sh:19

原文：

```text
 && pwd)
```

日本語：

`&& pwd)`

先行コマンド成功時に現在のディレクトリを出力するコード断片。


### scripts/deploy-managed-agent.sh:22

原文：

```text
${ANTHROPIC_API_KEY:?ANTHROPIC_API_KEY must be set}
```

日本語：

`${ANTHROPIC_API_KEY:?ANTHROPIC_API_KEY must be set}`

ANTHROPIC_API_KEY環境変数が必須であり、未設定ならエラーにする。


### scripts/deploy-managed-agent.sh:24

原文：

```text
no manifest at $DIR/agent.yaml
```

日本語：

$DIR/agent.yaml にマニフェストがありません


### scripts/deploy-managed-agent.sh:26

原文：

```text
REPO_SLUG derives from the git remote so this script stays copy-identical
```

日本語：

REPO_SLUGはgitリモートから導出し、分野別の各リポジトリでこのスクリプトを


### scripts/deploy-managed-agent.sh:27

原文：

```text
across vertical repos; override via env if running outside a checkout.
```

日本語：

同じ内容のまま使えるようにする。チェックアウト外で実行する場合は環境変数で上書きする。


### scripts/deploy-managed-agent.sh:28

原文：

```text
${REPO_SLUG:-$(basename -s .git 
```

日本語：

`${REPO_SLUG:-$(basename -s .git`

未指定のREPO_SLUGを、.git接尾辞を除いた名前から導出するコード断片。


### scripts/deploy-managed-agent.sh:29

原文：

```text
${REPO_SLUG:?cannot derive REPO_SLUG from git remote; set REPO_SLUG env var}
```

日本語：

`${REPO_SLUG:?cannot derive REPO_SLUG from git remote; set REPO_SLUG env var}`

gitリモートからREPO_SLUGを導出できない場合はエラーとし、REPO_SLUG環境変数の設定を求める。


### scripts/deploy-managed-agent.sh:33

原文：

```text
x-api-key: $ANTHROPIC_API_KEY
```

日本語：

`x-api-key: $ANTHROPIC_API_KEY`

APIキーを指定するHTTPヘッダー。値は環境変数参照。


### scripts/deploy-managed-agent.sh:34

原文：

```text
anthropic-version: 2023-06-01
```

日本語：

`anthropic-version: 2023-06-01`

APIバージョンを指定するHTTPヘッダー。


### scripts/deploy-managed-agent.sh:35

原文：

```text
anthropic-beta: managed-agents-2026-04-01
```

日本語：

`anthropic-beta: managed-agents-2026-04-01`

managed-agents機能のbetaヘッダー。


### scripts/deploy-managed-agent.sh:36

原文：

```text
content-type: application/json
```

日本語：

`content-type: application/json`

JSON形式を指定するContent-Typeヘッダー。


### scripts/deploy-managed-agent.sh:39

原文：

```text
jq + python(pyyaml) do the manifest→payload transform
```

日本語：

jq + python(pyyaml) マニフェスト→ペイロード変換を実行します


### scripts/deploy-managed-agent.sh:40

原文：

```text
requires jq
```

日本語：

jqが必要です


### scripts/deploy-managed-agent.sh:41

原文：

```text
import yaml
```

日本語：

`import yaml`

yamlモジュールを読み込むPython文。


### scripts/deploy-managed-agent.sh:41

原文：

```text
requires python3 + pyyaml
```

日本語：

python3 + pyyamlが必要です


### scripts/deploy-managed-agent.sh:52

原文：

```text
refusing ${{{name}}}: value contains characters outside [A-Za-z0-9._/:@-]
```

日本語：

${{{name}}} を拒否しています: 値に [A-Za-z0-9._/:@-] 以外の文字が含まれています


### scripts/deploy-managed-agent.sh:60

原文：

```text
$(mktemp -t skillcache)
```

日本語：

`$(mktemp -t skillcache)`

skillcacheという名前を基に一時ファイルを作る。


### scripts/deploy-managed-agent.sh:73

原文：

```text
$(mktemp -t skill).zip
```

日本語：

`$(mktemp -t skill).zip`

skillという名前を基にした一時パスに.zipを付ける。


### scripts/deploy-managed-agent.sh:74

原文：

```text
 && zip -qr 
```

日本語：

`&& zip -qr`

先行コマンド成功時にzipを静かに再帰作成するコード断片。


### scripts/deploy-managed-agent.sh:75

原文：

```text
/v1/skills uses its own beta header and multipart, not the managed-agents JSON path
```

日本語：

/v1/skills は、管理対象エージェントの JSON パスではなく、独自のベータ ヘッダーとマルチパートを使用します。


### scripts/deploy-managed-agent.sh:77

原文：

```text
x-api-key: $ANTHROPIC_API_KEY
```

日本語：

`x-api-key: $ANTHROPIC_API_KEY`

APIキーを指定するHTTPヘッダー。値は環境変数参照。


### scripts/deploy-managed-agent.sh:78

原文：

```text
anthropic-version: 2023-06-01
```

日本語：

`anthropic-version: 2023-06-01`

APIバージョンを指定するHTTPヘッダー。


### scripts/deploy-managed-agent.sh:79

原文：

```text
anthropic-beta: skills-2025-10-02
```

日本語：

`anthropic-beta: skills-2025-10-02`

skills機能のbetaヘッダー。


### scripts/deploy-managed-agent.sh:83

原文：

```text
.id // empty
```

日本語：

`.id // empty`

idが得られなければ何も出力しないjq式。


### scripts/deploy-managed-agent.sh:85

原文：

```text
POST /v1/skills failed for $path:
```

日本語：

$path の POST /v1/skills が失敗しました:


### scripts/deploy-managed-agent.sh:86

原文：

```text
 | jq . >&2 2>/dev/null || echo 
```

日本語：

`| jq . >&2 2>/dev/null || echo`

jqでエラー出力を整形し、失敗時はechoへ進むシェル断片。


### scripts/deploy-managed-agent.sh:96

原文：

```text
 && pwd)
```

日本語：

`&& pwd)`

先行コマンド成功時に現在のディレクトリを出力するコード断片。


### scripts/deploy-managed-agent.sh:99

原文：

```text
Expand any {from_plugin: <dir>} into one {path: ...} per skills/* under that dir.
```

日本語：

`{from_plugin: <dir>}`を、指定ディレクトリの`skills/*`ごとに1件の`{path: ...}`へ展開する。


### scripts/deploy-managed-agent.sh:101

原文：

```text
.skills[]? | select(.from_plugin) | .from_plugin
```

日本語：

`.skills[]? | select(.from_plugin) | .from_plugin`

from_pluginがあるskills要素からfrom_pluginを取り出すjq式。


### scripts/deploy-managed-agent.sh:107

原文：

```text
. + [{__upload:$p}]
```

日本語：

`. + [{__upload:$p}]`

__uploadに$pを設定した要素を配列へ追加するjq式。


### scripts/deploy-managed-agent.sh:110

原文：

```text
.skills = ((.skills // [] | map(select(.from_plugin | not))) + $e)
```

日本語：

`.skills = ((.skills // [] | map(select(.from_plugin | not))) + $e)`

from_pluginのある項目を除いたskills配列に$eを追加するjq式。


### scripts/deploy-managed-agent.sh:123

原文：

```text
.system.file // empty
```

日本語：

`.system.file // empty`

system.fileが得られなければ何も出力しないjq式。


### scripts/deploy-managed-agent.sh:124

原文：

```text
.system.text // empty
```

日本語：

`.system.text // empty`

system.textが得られなければ何も出力しないjq式。


### scripts/deploy-managed-agent.sh:125

原文：

```text
.system.append // empty
```

日本語：

`.system.append // empty`

system.appendが得られなければ何も出力しないjq式。


### scripts/deploy-managed-agent.sh:128

原文：

```text
system.file not found: $base/$sysfile
```

日本語：

system.file が見つかりません: $base/$sysfile


### scripts/deploy-managed-agent.sh:131

原文：

```text
 ]] && body=
```

日本語：

`]] && body=`

条件成功時にbodyを代入するシェル断片。


### scripts/deploy-managed-agent.sh:140

原文：

```text
 && pwd)
```

日本語：

`&& pwd)`

先行コマンド成功時に現在のディレクトリを出力するコード断片。


### scripts/deploy-managed-agent.sh:147

原文：

```text
 ]] || { echo 
```

日本語：

`]] || { echo`

条件失敗時にechoを実行するシェル断片。


### scripts/deploy-managed-agent.sh:148

原文：

```text
. + [$(upload_skill 
```

日本語：

`. + [$(upload_skill`

upload_skillの結果を配列に追加する式の断片。


### scripts/deploy-managed-agent.sh:149

原文：

```text
.skills[]? | select(.__upload) | .__upload
```

日本語：

`.skills[]? | select(.__upload) | .__upload`

__uploadのあるskills要素から__uploadを取り出すjq式。


### scripts/deploy-managed-agent.sh:158

原文：

```text
 --argjson v 
```

日本語：

`--argjson v`

vをJSON値として渡すjqオプション。


### scripts/deploy-managed-agent.sh:159

原文：

```text
.callable_agents[]?.manifest // empty
```

日本語：

`.callable_agents[]?.manifest // empty`

callable_agentsのmanifestを取得し、なければ出力しないjq式。


### scripts/deploy-managed-agent.sh:160

原文：

```text
.callable_agents=$c | del(.output_schema)
```

日本語：

`.callable_agents=$c | del(.output_schema)`

callable_agentsを$cに設定し、output_schemaを削除するjq式。


### scripts/deploy-managed-agent.sh:161

原文：

```text
.metadata = ((.metadata // {}) + {anthropic_cookbook: $ck})
```

日本語：

`.metadata = ((.metadata // {}) + {anthropic_cookbook: $ck})`

metadataにanthropic_cookbookキーと$ckの値を追加するjq式。


### scripts/deploy-managed-agent.sh:162

原文：

```text
{name, callable_agents}
```

日本語：

`{name, callable_agents}`

nameとcallable_agentsだけを含むオブジェクトを作るjq式。


### scripts/deploy-managed-agent.sh:166

原文：

```text
 + .name + 
```

日本語：

`+ .name +`

nameを連結する式の断片。


### scripts/deploy-managed-agent.sh:170

原文：

```text
.id // empty
```

日本語：

`.id // empty`

idが得られなければ何も出力しないjq式。


### scripts/deploy-managed-agent.sh:171

原文：

```text
.version // 1
```

日本語：

`.version // 1`

versionが得られなければ1を使うjq式。


### scripts/deploy-managed-agent.sh:173

原文：

```text
POST /v1/agents failed for $(jq -r .name <<<
```

日本語：

$(jq -r .name <<< の POST /v1/agents が失敗しました


### scripts/deploy-managed-agent.sh:174

原文：

```text
 | jq . >&2 2>/dev/null || echo 
```

日本語：

`| jq . >&2 2>/dev/null || echo`

jqでエラー出力を整形し、失敗時はechoへ進むシェル断片。


### scripts/deploy-managed-agent.sh:177

原文：

```text
$id $ver
```

日本語：

$id $ver


### scripts/deploy-managed-agent.sh:183

原文：

```text
# --dry-run: resolved POST /v1/agents bodies (subagents first, orchestrator last)
```

日本語：

# --dry-run: 解決された POST /v1/agents ボディ (サブエージェントが最初、オーケストレーターが最後)


### scripts/deploy-managed-agent.sh:191

原文：

```text
deployed: $ROLE
```

日本語：

デプロイ済み: $ROLE


### scripts/deploy-managed-agent.sh:192

原文：

```text
agent id: $AGENT_ID
```

日本語：

エージェント ID: $AGENT_ID


### scripts/deploy-managed-agent.sh:193

原文：

```text
cookbook: $COOKBOOK_TAG
```

日本語：

cookbook（実装例の識別タグ）：$COOKBOOK_TAG


### scripts/deploy-managed-agent.sh:194

原文：

```text
console:  https://console.anthropic.com/agents/$AGENT_ID
```

日本語：

コンソール: https://console.anthropic.com/agents/$AGENT_ID
