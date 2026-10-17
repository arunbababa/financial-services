# plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../../plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py)

### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:2

原文：

```text

Quick validation script for skills - minimal version

```

日本語：


スキルのクイック検証スクリプト - 最小バージョン


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:13

原文：

```text
Basic validation of a skill
```

日本語：

スキルの基本的な検証


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:16

原文：

```text
Check SKILL.md exists
```

日本語：

SKILL.mdの存在を確認する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:19

原文：

```text
SKILL.md not found
```

日本語：

SKILL.mdが見つかりません


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:21

原文：

```text
Read and validate frontmatter
```

日本語：

フロントマターを読んで検証する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:24

原文：

```text
No YAML frontmatter found
```

日本語：

YAML フロントマターが見つかりません


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:26

原文：

```text
Extract frontmatter
```

日本語：

フロントマターを抽出する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:29

原文：

```text
Invalid frontmatter format
```

日本語：

無効なフロントマター形式です


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:33

原文：

```text
Parse YAML frontmatter
```

日本語：

YAML フロントマターを解析する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:37

原文：

```text
Frontmatter must be a YAML dictionary
```

日本語：

フロントマターは YAML 辞書である必要があります


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:39

原文：

```text
Invalid YAML in frontmatter: 
```

日本語：

フロントマターの YAML が無効です:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:41

原文：

```text
Define allowed properties
```

日本語：

許可されるプロパティを定義する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:44

原文：

```text
Check for unexpected properties (excluding nested keys under metadata)
```

日本語：

予期しないプロパティをチェックします (メタデータの下にネストされたキーを除く)


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:48

原文：

```text
. Allowed properties are: 
```

日本語：

。許可されるプロパティは次のとおりです。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:48

原文：

```text
Unexpected key(s) in SKILL.md frontmatter: 
```

日本語：

SKILL.md フロントマター内の予期しないキー:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:52

原文：

```text
Check required fields
```

日本語：

必須フィールドを確認してください


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:54

原文：

```text
Missing 'name' in frontmatter
```

日本語：

フロントマターに'name'がない


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:56

原文：

```text
Missing 'description' in frontmatter
```

日本語：

フロントマターに'description'がない


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:58

原文：

```text
Extract name for validation
```

日本語：

検証用に名前を抽出する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:61

原文：

```text
Name must be a string, got 
```

日本語：

名前は文字列でなければなりません、取得しました


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:64

原文：

```text
Check naming convention (hyphen-case: lowercase with hyphens)
```

日本語：

命名規則を確認する（hyphen-case：小文字とハイフンを使う形式）


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:66

原文：

```text
' should be hyphen-case (lowercase letters, digits, and hyphens only)
```

日本語：

'はhyphen-case形式でなければならない（小文字、数字、ハイフンのみ）


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:66

原文：

```text
Name '
```

日本語：

名前 '


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:68

原文：

```text
' cannot start/end with hyphen or contain consecutive hyphens
```

日本語：

' ハイフンで開始/終了したり、連続したハイフンを含めたりすることはできません


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:68

原文：

```text
Name '
```

日本語：

名前 '


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:69

原文：

```text
Check name length (max 64 characters per spec)
```

日本語：

名前の長さを確認します (仕様ごとに最大 64 文字)


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:71

原文：

```text
 characters). Maximum is 64 characters.
```

日本語：

文字）。最大は 64 文字です。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:71

原文：

```text
Name is too long (
```

日本語：

名前が長すぎます (


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:73

原文：

```text
Extract and validate description
```

日本語：

説明を抽出して検証する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:76

原文：

```text
Description must be a string, got 
```

日本語：

説明は文字列でなければなりません、取得しました


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:79

原文：

```text
Check for angle brackets
```

日本語：

山かっこを確認する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:81

原文：

```text
Description cannot contain angle brackets (< or >)
```

日本語：

説明に山括弧を含めることはできません (< or >)


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:82

原文：

```text
Check description length (max 1024 characters per spec)
```

日本語：

説明の長さを確認します (仕様ごとに最大 1024 文字)


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:84

原文：

```text
 characters). Maximum is 1024 characters.
```

日本語：

文字）。最大は 1024 文字です。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:84

原文：

```text
Description is too long (
```

日本語：

説明が長すぎます(


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:86

原文：

```text
Skill is valid!
```

日本語：

スキルは有効です！


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/quick_validate.py:90

原文：

```text
Usage: python quick_validate.py <skill_directory>
```

日本語：

`Usage: python quick_validate.py <skill_directory>`

スキルのディレクトリを指定して検証する実行構文。
