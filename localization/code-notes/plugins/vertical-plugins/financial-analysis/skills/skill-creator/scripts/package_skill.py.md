# plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../../plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py)

### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:2

原文：

```text

Skill Packager - Creates a distributable .skill file of a skill folder

Usage:
    python utils/package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python utils/package_skill.py skills/public/my-skill
    python utils/package_skill.py skills/public/my-skill ./dist

```

日本語：

スキル梱包ツール: スキルフォルダーから配布可能な .skill ファイルを作成する。

使用法:
```text
python utils/package_skill.py <path/to/skill-folder> [output-directory]
```

例:
```text
python utils/package_skill.py skills/public/my-skill
python utils/package_skill.py skills/public/my-skill ./dist
```


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:20

原文：

```text

    Package a skill folder into a .skill file.

    Args:
        skill_path: Path to the skill folder
        output_dir: Optional output directory for the .skill file (defaults to current directory)

    Returns:
        Path to the created .skill file, or None if error
    
```

日本語：

スキルフォルダーを .skill ファイルにまとめる。

引数:
- `skill_path`: スキルフォルダーのパス
- `output_dir`: .skill ファイルの任意の出力先。省略時は現在のディレクトリ。

戻り値: 作成した .skill ファイルのパス。エラーの場合は `None`。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:32

原文：

```text
Validate skill folder exists
```

日本語：

スキルフォルダーが存在することを検証する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:34

原文：

```text
❌ Error: Skill folder not found: 
```

日本語：

❌ エラー: スキルフォルダーが見つかりません:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:38

原文：

```text
❌ Error: Path is not a directory: 
```

日本語：

❌ エラー: パスはディレクトリではありません:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:41

原文：

```text
Validate SKILL.md exists
```

日本語：

SKILL.mdが存在することを検証する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:44

原文：

```text
❌ Error: SKILL.md not found in 
```

日本語：

❌ エラー: SKILL.md が見つかりません


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:47

原文：

```text
Run validation before packaging
```

日本語：

パッケージ化する前に検証を実行する


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:48

原文：

```text
🔍 Validating skill...
```

日本語：

🔍 スキルを検証中...


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:51

原文：

```text
❌ Validation failed: 
```

日本語：

❌ 検証に失敗しました:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:52

原文：

```text
   Please fix the validation errors before packaging.
```

日本語：

パッケージ化する前に検証エラーを修正してください。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:56

原文：

```text
Determine output location
```

日本語：

出力場所の決定


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:66

原文：

```text
Create the .skill file (zip format)
```

日本語：

.skill ファイル（zip 形式）を作成します。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:69

原文：

```text
Walk through the skill directory
```

日本語：

スキルディレクトリを再帰的に走査


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:72

原文：

```text
Calculate the relative path within the zip
```

日本語：

zip内の相対パスを計算します。


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:77

原文：

```text

✅ Successfully packaged skill to: 
```

日本語：

✅ スキルを次の場所へ正常にパッケージ化しました: 


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:81

原文：

```text
❌ Error creating .skill file: 
```

日本語：

❌ .skill ファイルの作成中にエラーが発生しました:


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:87

原文：

```text
Usage: python utils/package_skill.py <path/to/skill-folder> [output-directory]
```

日本語：

使用法: python utils/package_skill.py <path/to/skill-folder> [output-directory]


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:89

原文：

```text
  python utils/package_skill.py skills/public/my-skill
```

日本語：

  python utils/package_skill.py skills/public/my-skill


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:90

原文：

```text
  python utils/package_skill.py skills/public/my-skill ./dist
```

日本語：

  python utils/package_skill.py skills/public/my-skill ./dist


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:96

原文：

```text
📦 Packaging skill: 
```

日本語：

📦 パッケージ化するスキル: 


### plugins/vertical-plugins/financial-analysis/skills/skill-creator/scripts/package_skill.py:98

原文：

```text
   Output directory: 
```

日本語：

出力ディレクトリ:


