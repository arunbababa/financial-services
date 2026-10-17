# .githooks/pre-commit の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../.githooks/pre-commit)

### .githooks/pre-commit:2

原文：

```text
Auto patch-bump any plugin with staged changes so it ends up exactly one
```

日本語：

ステージ済みの変更があるプラグインのパッチバージョンを自動更新し、main よりちょうど 1 段階


### .githooks/pre-commit:3

原文：

```text
patch ahead of main — bumped once per branch, not once per commit.
```

日本語：

先のパッチバージョンにする。更新はコミットごとではなく、ブランチごとに 1 回。


### .githooks/pre-commit:5

原文：

```text
Install (one-time per clone):  git config core.hooksPath .githooks
```

日本語：

インストール (クローンごとに 1 回): git config core.hooksPath .githooks


### .githooks/pre-commit:6

原文：

```text
(scripts/check.py self-installs this for you on first run.)
```

日本語：

(初回実行時に scripts/check.py がこれを自動インストールします。)


### .githooks/pre-commit:8

原文：

```text
Bypass for a single commit:    git commit --no-verify
```

日本語：

このフックを 1 回のコミットだけスキップ: git commit --no-verify


### .githooks/pre-commit:11

原文：

```text
$(git rev-parse --show-toplevel)
```

日本語：

$(git rev-parse --show-toplevel)


### .githooks/pre-commit:14

原文：

```text
[pre-commit] python3 not found; skipping version-bump.
```

日本語：

[プリコミット] python3 が見つかりません。バージョンバンプをスキップします。


