# claude-for-msft-365-install/commands/access-policies.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../claude-for-msft-365-install/commands/access-policies.md)

### claude-for-msft-365-install/commands/access-policies.md:48

原文：

```text
One-time: Install-Module ExchangeOnlineManagement
```

日本語：

初回のみ: `Install-Module ExchangeOnlineManagement`


### claude-for-msft-365-install/commands/access-policies.md:76

原文：

```text
Highly Confidential
```

日本語：

極秘


### claude-for-msft-365-install/commands/access-policies.md:91

原文：

```text
Restricted share
```

日本語：

制限付きシェア


### claude-for-msft-365-install/commands/access-policies.md:106

原文：

```text
Confidential - Restricted
```

日本語：

機密 - 制限付き


### claude-for-msft-365-install/commands/access-policies.md:150

原文：

```text
statement   := { effect, action, resource? }
```

日本語：

`statement := { effect, action, resource? }`
ポリシーの文は effect（許可・拒否）、action（操作）、任意の resource（対象）からなる。


### claude-for-msft-365-install/commands/access-policies.md:151

原文：

```text
effect      := "allow" | "deny"
```

日本語：

`effect := "allow" | "deny"`
許可は "allow"、拒否は "deny"。


### claude-for-msft-365-install/commands/access-policies.md:152

原文：

```text
action      := <slug> | [ <slug>, ... ]          # feature slugs; unknown -> skipped + reported
```

日本語：

`action := <slug> | [ <slug>, ... ]`
機能のスラッグを 1 つまたは配列で指定。不明なスラッグはスキップして報告する。


### claude-for-msft-365-install/commands/access-policies.md:153

原文：

```text
resource    := { type, identifiers: [identifier, ...], description? }
```

日本語：

`resource    := { type, identifiers: [identifier, ...], description? }`


### claude-for-msft-365-install/commands/access-policies.md:154

原文：

```text
type        := "open_file" | "uploaded_file"    # the extension point
```

日本語：

`type        := "open_file" | "uploaded_file"    # the extension point`


### claude-for-msft-365-install/commands/access-policies.md:155

原文：

```text
identifier  := { type: "mip_label_guid" | "mip_label_name" | "file_path", <one operator> }
```

日本語：

`identifier := { type: "mip_label_guid" | "mip_label_name" | "file_path", <one operator> }`
識別子は type と演算子 1 つで構成し、type はラベル GUID、ラベル名、ファイルパスのいずれか。


### claude-for-msft-365-install/commands/access-policies.md:202

原文：

```text
Confidential - 
```

日本語：

機密 -


