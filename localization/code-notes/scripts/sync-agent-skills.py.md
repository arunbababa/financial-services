# scripts/sync-agent-skills.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../scripts/sync-agent-skills.py)

### scripts/sync-agent-skills.py:2

原文：

```text

Re-sync each agent plugin's bundled skills from the vertical-plugin source.

Agent plugins under plugins/agent-plugins/<slug>/skills/<name>/ are vendored
copies of plugins/vertical-plugins/*/skills/<name>/. The vertical copy is the
source of truth; run this after editing a skill there to propagate the change
into every agent that bundles it.

Usage: python3 scripts/sync-agent-skills.py

```

日本語：

各エージェントプラグインに同梱したスキルを、vertical-plugin の元データから再同期する。

plugins/agent-plugins/<slug>/skills/<name>/ のスキルは、plugins/vertical-plugins/*/skills/<name>/ を取り込んだコピーである。vertical 側のコピーを正とし、そこでスキルを編集した後にこのスクリプトを実行して、それを同梱する全エージェントへ変更を反映する。

使用法: `python3 scripts/sync-agent-skills.py`


### scripts/sync-agent-skills.py:20

原文：

```text
index every skill name -> source dir in verticals
```

日本語：

verticals 内の各スキル名から元ディレクトリへの索引を作成


### scripts/sync-agent-skills.py:39

原文：

```text
 bundled skill dir(s) from vertical-plugins/
```

日本語：

バンドルされたスキル ディレクトリ (vertical-plugins/ から)


### scripts/sync-agent-skills.py:41

原文：

```text
WARN: no vertical source found for:
```

日本語：

警告: 以下の垂直ソースが見つかりません:


