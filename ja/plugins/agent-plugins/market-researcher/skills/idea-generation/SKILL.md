---
name: idea-generation
description: Systematic stock screening and investment idea sourcing. Combines quantitative screens, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or conducting thematic sweeps. Triggers on "idea generation", "stock screen", "find ideas", "what looks interesting", "screen for", "new ideas", or "pitch me something".
---

> 非公式日本語訳。機械翻訳初稿をAIが原文と全文照合して校閲しました。[英語原文](../../../../../../plugins/agent-plugins/market-researcher/skills/idea-generation/SKILL.md)。原文のコード・設定値を保持しています。実データ・法令・投資判断の専門検証は未実施です。

> 説明（日本語）：定量選別、テーマ調査、パターン認識を組み合わせ、体系的に新しいロング・ショート案を探す。新案探し、銘柄選別、テーマ横断調査に使う。適用表現は "idea generation"、"stock screen"、"find ideas"、"what looks interesting"、"screen for"、"new ideas"、"pitch me something"。

<a id="idea-generation"></a>
# 投資アイデアの生成

<a id="workflow"></a>
## ワークフロー

<a id="step-1-define-search-criteria"></a>
### 手順1：検索基準を決める

ユーザーへ条件を尋ねる。
- **方向：** ロング、ショート、両方。
- **時価総額：** 大型、中型、小型、超小型。
- **セクター：** 特定か横断か。
- **スタイル：** 割安、成長、質、特殊状況、イベント。
- **地域：** 米国、国外、世界。
- **テーマ：** AI、国内回帰、高齢化など。

<a id="step-2-quantitative-screens"></a>
### 手順2：定量スクリーニング

スタイルに合わせる。

**割安株**
- PERがセクター中央値未満。
- EV/EBITDAが過去平均未満。
- FCF利回り >5%。
- PBR <1.5倍。
- 過去90日に内部者の買い。
- 配当利回りが市場平均超。

**成長株**
- 売上前年比 >15%。
- 利益前年比 >20%。
- 売上成長率が加速。
- 利益率拡大。
- ROIC >15%。
- 純収益継続率が強い（SaaSで >110%）。

**質の高い企業**
- 5年以上、一貫した売上成長。
- 利益率の安定・拡大。
- ROE >15%。
- 低い負債・資本比率。
- 高いFCF転換。
- 内部者保有 >5%。

**ショート候補**
- 減収・成長減速。
- 利益率低下。
- 売上に対し売掛金・在庫が増加。
- 内部者売り。
- 根拠なく同業より高い評価。
- 高い空売り残高と悪化するファンダメンタルズ。
- 会計上の懸念（監査人変更、訂正）。

**特殊状況**
- ロックアップ解除を迎える最近のIPO・SPAC。
- 過去12か月のスピンオフ。
- 再編から立ち直る企業。
- アクティビストの関与。
- 不振企業の経営陣変更。

<a id="step-3-thematic-sweep"></a>
### 手順3：テーマ別の横断調査

テーマを調べ受益者を探す。

1. 仮説を定義する（例「AI基盤支出は2026年まで加速」）。
2. バリューチェーンを描き、直接・間接受益者を探す。
3. 専業と多角化企業の関与を区別する。
4. どの銘柄が既に織り込み済みか、過小評価かを調べる。
5. 市場がまだテーマと結び付けていない二次的受益者を探す。

<a id="step-4-idea-presentation"></a>
### 手順4：アイデアの提示

選別を通った各案に示す。

**[企業名] — [ロング／ショート] — [1行の根拠]**

| 指標 | 値 | 同業比 |
|--------|-------|-----------|
| 時価総額 | | |
| EV/EBITDA（NTM） | | |
| PER（NTM） | | |
| 売上成長率 | | |
| EBITDA利益率 | | |
| FCF利回り | | |

**根拠（3〜5箇条）：**
- 価格が適切でない理由。
- 市場の見落とし。
- 価値実現のきっかけ。

**主要リスク：**
- 何があれば誤りとなるか。

**推奨する次の行動：**
- 全モデル作成、詳細調査、専門家インタビューなど。

<a id="step-5-output"></a>
### 手順5：出力

- 各1ページの概要付き5〜10案。
- 選別基準・方法の記録。
- 全案の比較表。
- 最初に調査する案の優先順。

<a id="important-notes"></a>
## 重要事項

- 選別は結論でなく候補を出す。すべてにファンダメンタルズの検討が必要。
- 最良案は複数条件の交点から生まれがち（例、一時的な逆風で割安な優良企業）。
- 混雑した取引を避け、保有データ・空売り残高・担当アナリスト数を確認する。
- 逆張りにはきっかけが必要。きっかけなく早すぎることは、間違いと同じ。
- 的中率を追い、最良案を生む選別・手法を調べる。
- ショートはタイミングが難しくリスクが非対称なので、より強い確信が必要。
