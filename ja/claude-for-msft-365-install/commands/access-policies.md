---
description: Build the access_policies value — the granular, IAM-shaped way to allow or deny add-in features
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../claude-for-msft-365-install/commands/access-policies.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：access_policies 値を構築する - アドイン機能を許可または拒否するための IAM 形式の詳細な方法

<a id="configure-access_policies"></a>
# access_policies を構成する

`access_policies`は今後のアドインのアクセス制御方式です。IAMに似た形式の
許可・拒否の**ステートメント**をJSON配列で持ち、利用可能な機能と
その条件を決定します。`disabled_features`が、各機能を全員に対して
オン・オフする単純な一覧であるのに対し、`access_policies`は
同じ無効化機能に加えて、条件と効果を指定できます。

| 実現したいこと | `disabled_features` | `access_policies` |
|---|---|---|
| すべてのユーザーに対して機能をオフにする | ✔ `disabled_features='skills.authoring'` | ✔ リソースのない `deny` ステートメント (同じ効果) |
| 特定のドキュメントでのみ機能をオフにする | ✗ | ✔ `resource` (機密ラベルなど) を追加します。 |
| 承認されたドキュメント (許可リスト) を *除く* 機能をオフにする | ✗ | ✔ `"effect": "allow"` |
| UIの表示文・テレメトリで制限の根拠を示す | 限定的 | ✔ ステートメントごとの`description`と出所 |

**`resource`がない**ステートメントは`disabled_features`とまったく同じ効果なので、
そちらに指定する内容はこちらにも指定できます。`resource`が適用範囲を細かくし、
`type`が拡張点になります。現時点ではリソースは文書（`open_file`、
`uploaded_file`）で、**Microsoft Purviewの機密ラベル**、または開いている文書の場合は
**ファイルパス**で識別します。今後のリソース種別も、新しい設定キーを
追加せず同じ形式で拡張できます。新規導入ではこちらから始めてください。
単純な一覧で十分な場合は、`disabled_features`も引き続き使えます。

現時点で、文書の条件に応じた二つの制御があります。

- **開いている文書上でアドイン自体を実行できるか**（`addin.access`の停止
  スイッチ）。開いている文書のラベルまたはパスで判定します。
- **ファイルをアップロードとして添付できるか**（`file.upload`）。
  *添付するファイル自体*のラベルで判定します。OfficeファイルとPDFが対象です。

管理者に以下の四つの手順を案内し、完成したJSONを追加の一つのキーとして
[manifest](manifest.md#access_policies)へ渡してください。

<a id="1-get-the-label-guids"></a>
## 1. ラベルの GUID を取得します。

すべてのルールがラベルではなくファイル パス (ステップ 2) で一致する場合は、このステップをスキップします。

ステートメントはラベルの**GUID**（`mip_label_guid`）に照合します。GUIDは名前や
ロケールの変更でも変わりません。管理者にPurviewコンプライアンスのPowerShell
モジュールを使い、一度ラベル体系を取得してもらいます（アプリ登録は不要で、Microsoft自身の
サインインを使用します）。

```powershell
# One-time: Install-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@theirtenant.com
Get-Label | Sort-Object Priority | Format-Table Priority, DisplayName, Name, Guid, ParentId
```

表を貼り付けるように依頼します。そこから、彼らが関心を持っている各ラベルについてメモします。
`Guid`（照合対象）、`DisplayName`、`ParentId`（空でなければ
*サブラベル*です。後述の親ラベルの規則を参照）。

PowerShellを実行できない場合、GUIDはPurviewコンプライアンスポータルで
ラベルを編集用に開いた際のURL、またはMicrosoft Graph Explorerからも確認できます。
(`GET /security/informationProtection/sensitivityLabels`).

<a id="2-choose-the-statements"></a>
## 2. ステートメントを選択します

次のどの形式が必要かを確認します。多くのテナントでは一つ目、二つ目、または
両方が必要です。その後、各自のGUIDへ置き換えます。

**指定ラベルの文書でアドインをブロックする**（よくある要望：
「極秘ファイル上ではClaudeを動かしてはいけない」）。

```json
{
  "effect": "deny",
  "action": "addin.access",
  "resource": {
    "type": "open_file",
    "identifiers": [{ "type": "mip_label_guid", "equals": "<guid>" }],
    "description": "Highly Confidential"
  }
}
```

**指定場所の文書でアドインをブロックする**（ネットワーク共有のファイル等、
ラベルを付けられないファイル向け。後述のパスの規則を参照）。

```json
{
  "effect": "deny",
  "action": "addin.access",
  "resource": {
    "type": "open_file",
    "identifiers": [{ "type": "file_path", "startsWith": "//fileserver/restricted/" }],
    "description": "Restricted share"
  }
}
```

**指定ラベルを持つファイルのアップロードを拒否する**（「ユーザーは
制限対象のファイルを添付してはいけない」）。

```json
{
  "effect": "deny",
  "action": "file.upload",
  "resource": {
    "type": "uploaded_file",
    "identifiers": [{ "type": "mip_label_guid", "equals": "<guid>" }],
    "description": "Confidential - Restricted"
  }
}
```

**全員に対して機能を無効化する**（`disabled_features`と同等。`resource`が
ないため全体に適用します。この例では、どのユーザーもスキルを作成できません）。

```json
{ "effect": "deny", "action": "skills.authoring" }
```

**許可リスト：承認されたラベルでのみアドインを実行する。** `(action, resource type)`に
最初の`allow`を書くと、その範囲の既定動作は拒否に変わります。
`allow`の識別子に一致するファイルだけが通り、ラベルのないファイルも
通らなくなります。`deny`と`allow`が両方一致すれば、`deny`が優先されます。

```json
{
  "effect": "allow",
  "action": "addin.access",
  "resource": {
    "type": "open_file",
    "identifiers": [
      { "type": "mip_label_guid", "equals": "<general-guid>" },
      { "type": "mip_label_guid", "equals": "<public-guid>" }
    ]
  }
}
```

必要に応じて結合します。値はステートメントの 1 つの JSON 配列です。 `action`も
配列を受け入れて、1 つのステートメントを複数のアクションに適用します。

```json
[
  { "effect": "deny", "action": "addin.access", "resource": { ... } },
  { "effect": "deny", "action": ["file.upload", "skills.authoring"] }
]
```

<a id="statement-grammar-reference"></a>
### ステートメント文法 (参考)

```
statement   := { effect, action, resource? }
effect      := "allow" | "deny"
action      := <slug> | [ <slug>, ... ]          # feature slugs; unknown -> skipped + reported
resource    := { type, identifiers: [identifier, ...], description? }
type        := "open_file" | "uploaded_file"    # the extension point
identifier  := { type: "mip_label_guid" | "mip_label_name" | "file_path", <one operator> }
```

| `action`の識別名 | 制御するもの | `resource`を取るか |
|---|---|---|
| `addin.access` | 開いているドキュメント上でアドインが実行されるかどうか - Kill スイッチ | `open_file` |
| `file.upload` | 会話にファイルを添付できるかどうか | `uploaded_file` |
| `skills.authoring` | スキルの作成、編集、アップロード。管理者がプロビジョニングしたスキルの実行は影響を受けません | — |
| `thumbs` | 応答フィードバック (親指を上げる/下げる、およびフォローアップのプロンプト) | — |

未知の識別名はスキップして報告し、前方互換性を保ちます。リソースを持たない
ステートメントはどの識別名にも使えます。現時点で範囲指定用のリソース種別を持つのは、
`addin.access`と`file.upload`だけです。

| オペレーター | 値 | セマンティクス |
|---|---|---|
| `equals` | 文字列 | GUID: 大文字と小文字は区別されません。名前: 正確に、大文字と小文字が区別されます。パス: パスルールを参照 |
| `startsWith` | 文字列 | プレフィックス マッチ — `mip_label_name` (親ラベル ルールを参照) および `file_path` |
| `endsWith` | 文字列 | サフィックスマッチ — `mip_label_name` のみ |
| `exists` | ブール値 | 存在チェック — `false` = ラベルなし、`true` = 任意のラベル |

演算子は識別子一つにつき厳密に一つです。`mip_label_guid`が対応するのは`equals`と
`exists`だけで、`file_path`は`equals`と`startsWith`だけです。リソースには少なくとも
一つの識別子が必要です。空の`identifiers`配列は決して一致しません。ステートメント同士はOR、
リソース内の識別子同士もORで結合します。一致する`deny`は一致する`allow`より優先され、
`(action, resource type)`に対する最初の`allow`が、その範囲の既定動作を拒否へ変えます。
`description`は表示用の説明文です。UIの文言やテレメトリには現れますが、照合条件には使いません。

<a id="3-rules-to-explain-before-they-ship-it"></a>
## 3. 出荷前に説明するルール

出荷前に次の 6 つのことを管理者に伝えてください。それぞれがよくある驚きです。

**ステートメントは明記されたことだけを行い、他の制限は暗黙に含みません。**
ラベルを使って開いている文書でアドインを禁止しても（`open_file`の`addin.access`）、
その文書を*別の*文書へアップロードすることまでは止めません。逆も同じです。
同じラベルを「あらゆる形で」禁止するには**二つのステートメント**が必要です。一つは`open_file`、
もう一つは`uploaded_file`です。ステートメント同士、および各ステートメント内の識別子同士は、
ORで結合します。

**ファイル内に親ラベルのGUIDはなく、サブラベルのGUIDだけがあります。** 文書は
サブラベルのGUID（`ParentId`を持つ行）を保持します。親グループ全体
（「*Confidential*配下すべて」）を禁止するには、各サブラベルの
GUIDを列挙するか、Officeが書き込む合成表示名
`"Parent - Sublabel"`に照合します（プレフィックスに区切りの` - `も含め、
*Confidentiality Waiver*のような別ラベルまで一致しないようにします）。

```json
{ "type": "mip_label_name", "startsWith": "Confidential - " }
```

**名前は完全一致で照合し、名称変更で壊れるおそれがあります。** `mip_label_name`は
ラベル付けクライアントが、そのユーザーのロケールで書き込んだ表示名を、
大文字・小文字と空白を含め、一文字ずつ比較します。
`equals`、`startsWith`、`endsWith`を使えます。GUIDを優先し、名前を使うのは
上記の親グループの場合だけにします。名称変更で一致しなくなることを管理者へ説明してください。

**アドインがラベルを読めない場合は、安全側に倒して拒否します。** いずれかのステートメントが
`uploaded_file`を対象とするとき、Purviewで*暗号化*されたパッケージや旧形式の
`.xls`／`.ppt`／`.doc`のようにラベルを読めない添付ファイルは、通過を許可せず
拒否します。機密ラベルが暗号化を適用するなら、意図した動作になります。
旧形式のアップロードが必要なら、形式を変換する必要があります。

**「分類ラベル付き文書のみ」**：*ラベルのない*ファイルをアドインに拒否させるには、
GUIDではなくラベルの有無で照合します。

```json
{ "type": "mip_label_guid", "exists": false }
```

`uploaded_file`では、ラベルを一切付けられない形式
（画像、CSV、プレーンテキスト）も該当します。スクリーンショットが拒否されても驚かないよう、
この点を説明してください。

**パスの規則は、Officeが報告するパスそのものに照合します。** `file_path`は、
Officeホストが報告する開いている文書のパスまたはURLと比較します。
正規化は三つだけです。ASCII文字の大文字・小文字を区別しないこと、Windowsパスでは`\`と`/`を
同じ区切りとすること（`"//fileserver/restricted/"`と
`"\\\\fileserver\\restricted\\"`は同じプレフィックスです。スラッシュ形式なら
JSONのエスケープが不要です）、`file:` URLをそのURLが指すパスとして読むことです。それ以外では、
次の点に注意します。

- すべてのプレフィックスを区切り文字で終了します — `//fileserver/restricted` も一致します
  `//fileserver/restricted-archive/`.
- エイリアスは解決しません。同じ共有でも、割当て済みドライブ文字、
  DFS名前空間、別サーバー名を経由すれば別のパスです。それぞれの
  表記を別の識別子として追加してください。
- SharePointとOneDriveの文書はパーセントエンコードされたURL（空白は`%20`）を
  報告します。プレフィックスも同じ方式でエンコードしてください。非ASCII文字は
  完全に一致する必要があります。
- 未保存、またはOfficeがパスを報告できない等、パスを持たない文書は、
  `deny`に決して一致せず、`allow`リストではラベルのない文書と同様に
  拒否されます。
- 制御対象は開いている文書だけです。アップロードにはパスがないので、`file_path`は
  `uploaded_file`に決して一致しません。文書を別の場所に保存した場合は、
  ペインに再びフォーカスが戻った時点で新しいパスに基づき判定します。
- `file_path`導入前のアドインは、それを含むステートメント全体を捨てるため、
  そのバージョンではパスの規則が適用されません。`file_path`の識別子は
  専用のステートメントへ分け、古いバージョンでもラベルの規則が
  引き続き適用されるようにしてください。

<a id="4-validate-and-hand-off"></a>
## 4. 検証して引き渡す

何かを生成する前に、完成した配列を表（effect / action /
resource / identifiers）として管理者に提示します。その後、
`access_policies`キーとして[manifest](manifest.md#access_policies)へ渡します。ビルド
スクリプトは、不正なJSONを拒否し、上記の文法に合わないステートメントごとに警告します
（不正な`effect`、未知のリソース・識別子種別、
演算子の欠落・重複、`uploaded_file`での`file_path`等）。警告はすべて
この段階で解消してください。アドインは未知のaction識別名と解析不能な値は報告しますが、
文法に合わないステートメントは黙って捨てます。ビルド時検査が唯一の検出手段であり、
放置すると管理者は、実際には一度も適用されない規則を気付かず配布することになります。

`access_policies`はマニフェスト／ブートストラップ専用です。256文字制限のあるEntraの
拡張属性には**入りません**。ユーザーごとの
[bootstrap](bootstrap.md)を使う場合は、同じ配列を文字列ではなく
ネイティブなJSON値として渡します。
