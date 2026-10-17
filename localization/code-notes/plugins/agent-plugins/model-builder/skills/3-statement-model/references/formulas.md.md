# plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md の自然言語補訳

> 非公式な日本語補訳です。AIが全項目を原文と照合して修正しました。実行コード・設定値は原文を保持しています。

[原文](../../../../../../../../plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md)

### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:10

原文：

```text
Balance Sheet:        Assets = Liabilities + Equity
```

日本語：

`Balance Sheet:        Assets = Liabilities + Equity`

貸借対照表: 資産 = 負債 + 資本


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:11

原文：

```text
Net Income:           IS Net Income → CF Operations (starting point)
```

日本語：

`Net Income:           IS Net Income → CF Operations (starting point)`

当期純利益：損益計算書（IS）の当期純利益を営業キャッシュフロー（CF）の出発点へ転記する。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:12

原文：

```text
Cash Flow:            ΔCash = CFO + CFI + CFF
```

日本語：

`Cash Flow:            ΔCash = CFO + CFI + CFF`

キャッシュフロー: Δキャッシュ = CFO + CFI + CFF


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:13

原文：

```text
Cash Tie-Out:         Ending Cash (CF) = Cash (BS Asset)
```

日本語：

`Cash Tie-Out:         Ending Cash (CF) = Cash (BS Asset)`

現金残高の突合：キャッシュフロー計算書（CF）の期末現金 = 貸借対照表（BS）の現金（資産）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:14

原文：

```text
Cash Monthly/Annual:  Closing Cash (Monthly) = Closing Cash (Annual)
```

日本語：

`Cash Monthly/Annual:  Closing Cash (Monthly) = Closing Cash (Annual)`

月次/年次の現金：月次の期末現金 = 年次の期末現金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:15

原文：

```text
Retained Earnings:    Prior RE + Net Income - Dividends = Ending RE
```

日本語：

`Retained Earnings:    Prior RE + Net Income - Dividends = Ending RE`

利益剰余金：前期利益剰余金 + 当期純利益 - 配当 = 期末利益剰余金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:16

原文：

```text
Equity Raise:         ΔCommon Stock/APIC (BS) = Equity Issuance (CFF)
```

日本語：

`Equity Raise:         ΔCommon Stock/APIC (BS) = Equity Issuance (CFF)`

増資：貸借対照表（BS）の普通株式/追加払込資本（APIC）の増減 = 財務キャッシュフロー（CFF）の株式発行による調達額


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:17

原文：

```text
Year 0 Equity:        Equity Raised (Year 0) = Beginning Equity (Year 1)
```

日本語：

`Year 0 Equity:        Equity Raised (Year 0) = Beginning Equity (Year 1)`

0年目の増資：0年目の増資調達額 = 1年目の期首自己資本


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:25

原文：

```text
Net Revenue - Cost of Revenue = Gross Profit
```

日本語：

`Net Revenue - Cost of Revenue = Gross Profit`

純収益 - 収益原価 = 総利益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:40

原文：

```text
Gross Margin %      = Gross Profit / Net Revenue
```

日本語：

`Gross Margin %      = Gross Profit / Net Revenue`

売上総利益率 % = 売上総利益 / 純収益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:41

原文：

```text
EBITDA              = EBIT + D&A  (or = Gross Profit - OpEx)
```

日本語：

`EBITDA              = EBIT + D&A  (or = Gross Profit - OpEx)`

EBITDA = EBIT + D&A (または = 売上総利益 - OpEx)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:42

原文：

```text
EBITDA Margin %     = EBITDA / Net Revenue
```

日本語：

`EBITDA Margin %     = EBITDA / Net Revenue`

EBITDAマージン% = EBITDA / 純収益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:43

原文：

```text
EBIT Margin %       = EBIT / Net Revenue
```

日本語：

`EBIT Margin %       = EBIT / Net Revenue`

EBITマージン% = EBIT / 純収益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:44

原文：

```text
Net Income Margin % = Net Income / Net Revenue
```

日本語：

`Net Income Margin % = Net Income / Net Revenue`

純利益率 % = 純利益 / 純収益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:50

原文：

```text
Total Debt            = Current Portion of Debt + Long-Term Debt
```

日本語：

`Total Debt            = Current Portion of Debt + Long-Term Debt`

有利子負債合計 = 1年内返済予定の有利子負債 + 長期有利子負債


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:51

原文：

```text
Net Debt              = Total Debt - Cash
```

日本語：

`Net Debt              = Total Debt - Cash`

純有利子負債 = 有利子負債合計 - 現金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:52

原文：

```text
Total Debt / EBITDA   = Total Debt / EBITDA (from IS)
```

日本語：

`Total Debt / EBITDA   = Total Debt / EBITDA (from IS)`

有利子負債合計 / EBITDA = 有利子負債合計 / 損益計算書（IS）のEBITDA


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:53

原文：

```text
Net Debt / EBITDA     = Net Debt / EBITDA (from IS)
```

日本語：

`Net Debt / EBITDA     = Net Debt / EBITDA (from IS)`

純有利子負債 / EBITDA = 純有利子負債 / 損益計算書（IS）のEBITDA


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:54

原文：

```text
Interest Coverage     = EBITDA / Interest Expense (from IS)
```

日本語：

`Interest Coverage     = EBITDA / Interest Expense (from IS)`

インタレスト・カバレッジ = EBITDA / 支払利息 (IS から)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:55

原文：

```text
Net Int Exp % Debt    = Net Interest Expense / Long-Term Debt
```

日本語：

`Net Int Exp % Debt    = Net Interest Expense / Long-Term Debt`

純支払利息の有利子負債に対する比率 = 純支払利息 / 長期有利子負債


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:56

原文：

```text
Debt / Total Cap      = Total Debt / (Total Debt + Total Equity)
```

日本語：

`Debt / Total Cap      = Total Debt / (Total Debt + Total Equity)`

有利子負債 / 総資本 = 有利子負債合計 /（有利子負債合計 + 自己資本合計）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:57

原文：

```text
Debt / Equity         = Total Debt / Total Equity
```

日本語：

`Debt / Equity         = Total Debt / Total Equity`

有利子負債 / 自己資本 = 有利子負債合計 / 自己資本合計


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:58

原文：

```text
Current Ratio         = Total Current Assets / Total Current Liabilities
```

日本語：

`Current Ratio         = Total Current Assets / Total Current Liabilities`

流動比率＝流動資産合計／流動負債合計


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:59

原文：

```text
Quick Ratio           = (Total Current Assets - Inventory) / Total Current Liabilities
```

日本語：

`Quick Ratio           = (Total Current Assets - Inventory) / Total Current Liabilities`

当座比率 = (流動資産合計 - 棚卸資産) / 流動負債合計


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:65

原文：

```text
Cost of Revenue (Forecast) = Net Revenue × Cost of Revenue % Assumption
```

日本語：

`Cost of Revenue (Forecast) = Net Revenue × Cost of Revenue % Assumption`

収益原価 (予測) = 純収益 × 収益原価 % 仮定


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:66

原文：

```text
S&M (Forecast)             = Net Revenue × S&M % Assumption
```

日本語：

`S&M (Forecast)             = Net Revenue × S&M % Assumption`

S&M (予測) = 純収益 × S&M % 仮定


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:67

原文：

```text
G&A (Forecast)             = Net Revenue × G&A % Assumption
```

日本語：

`G&A (Forecast)             = Net Revenue × G&A % Assumption`

G&A (予測) = 純収益 × G&A % 仮定


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:68

原文：

```text
R&D (Forecast)             = Net Revenue × R&D % Assumption
```

日本語：

`R&D (Forecast)             = Net Revenue × R&D % Assumption`

R&D (予測) = 純収益 × R&D % 仮定


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:69

原文：

```text
SBC (Forecast)             = Net Revenue × SBC % Assumption
```

日本語：

`SBC (Forecast)             = Net Revenue × SBC % Assumption`

SBC (予測) = 純収益 × SBC % 仮定


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:75

原文：

```text
Accounts Receivable
```

日本語：

売掛金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:76

原文：

```text
  Prior AR
```

日本語：

期首売掛金（AR）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:77

原文：

```text
  + Revenue (from IS)
```

日本語：

+ 収益 (IS から)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:78

原文：

```text
  - Cash Collections (plug)
```

日本語：

- 現金回収額（残高が整合するよう逆算する調整項目）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:79

原文：

```text
  = Ending AR
```

日本語：

`= Ending AR`

= 期末売掛金（AR）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:80

原文：

```text
  DSO = (AR / Revenue) × 365
```

日本語：

`DSO = (AR / Revenue) × 365`

DSO = (AR / 収益) × 365


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:83

原文：

```text
  Prior Inventory
```

日本語：

期首棚卸資産


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:84

原文：

```text
  + Purchases (plug)
```

日本語：

+ 仕入額（残高が整合するよう逆算する調整項目）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:85

原文：

```text
  - COGS (from IS)
```

日本語：

- COGS (IS から)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:86

原文：

```text
  = Ending Inventory
```

日本語：

`= Ending Inventory`

= 期末在庫


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:87

原文：

```text
  DIO = (Inventory / COGS) × 365
```

日本語：

`DIO = (Inventory / COGS) × 365`

DIO = (在庫 / 原価) × 365


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:89

原文：

```text
Accounts Payable
```

日本語：

買掛金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:90

原文：

```text
  Prior AP
```

日本語：

期首買掛金（AP）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:91

原文：

```text
  + Purchases (from Inventory calc)
```

日本語：

+ 仕入額（棚卸資産の計算から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:92

原文：

```text
  - Cash Payments (plug)
```

日本語：

- 現金支払額（残高が整合するよう逆算する調整項目）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:93

原文：

```text
  = Ending AP
```

日本語：

`= Ending AP`

= 期末買掛金（AP）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:94

原文：

```text
  DPO = (AP / COGS) × 365
```

日本語：

DPO = (AP / COGS) × 365


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:96

原文：

```text
Net Working Capital = AR + Inventory - AP
```

日本語：

`Net Working Capital = AR + Inventory - AP`

正味運転資本 = AR + 在庫 - AP


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:97

原文：

```text
ΔWC = Current NWC - Prior NWC
```

日本語：

`ΔWC = Current NWC - Prior NWC`

運転資本の増減（ΔWC） = 当期NWC - 前期NWC


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:103

原文：

```text
Beginning PP&E (Gross)
```

日本語：

期首有形固定資産（PP&E、取得原価）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:104

原文：

```text
+ CapEx
```

日本語：

+ 設備投資


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:105

原文：

```text
= Ending PP&E (Gross)
```

日本語：

`= Ending PP&E (Gross)`

= 期末有形固定資産（PP&E、取得原価）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:107

原文：

```text
Beginning Accumulated Depreciation
```

日本語：

期首減価償却累計額


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:108

原文：

```text
+ Depreciation Expense
```

日本語：

+ 減価償却費


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:109

原文：

```text
= Ending Accumulated Depreciation
```

日本語：

`= Ending Accumulated Depreciation`

= 期末減価償却累計額


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:111

原文：

```text
PP&E (Net) = Gross PP&E - Accumulated Depreciation
```

日本語：

`PP&E (Net) = Gross PP&E - Accumulated Depreciation`

PP&E (ネット) = 総PP&E - 減価償却累計額


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:117

原文：

```text
Beginning Debt Balance
```

日本語：

期首有利子負債残高


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:118

原文：

```text
+ New Borrowings
```

日本語：

+ 新規借入


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:119

原文：

```text
- Repayments
```

日本語：

- 返済


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:120

原文：

```text
= Ending Debt Balance
```

日本語：

`= Ending Debt Balance`

= 期末有利子負債残高


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:122

原文：

```text
Interest Expense = Avg Debt Balance × Interest Rate
```

日本語：

`Interest Expense = Avg Debt Balance × Interest Rate`

支払利息 = 平均有利子負債残高 × 金利


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:123

原文：

```text
  (Use beginning balance to avoid circularity, or iterate if circular refs enabled)
```

日本語：

（循環参照を避けるため期首残高を使う。循環参照が有効なら反復計算する。）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:129

原文：

```text
Beginning Retained Earnings
```

日本語：

期首利益剰余金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:130

原文：

```text
+ Net Income (from IS)
```

日本語：

+ 当期利益（ISより）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:131

原文：

```text
+ Stock-Based Compensation (SBC) (from IS)
```

日本語：

+ 株式報酬（SBC）（ISより）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:132

原文：

```text
- Dividends
```

日本語：

- 配当金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:133

原文：

```text
= Ending Retained Earnings
```

日本語：

`= Ending Retained Earnings`

= 期末利益剰余金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:139

原文：

```text
NOL CARRYFORWARD SCHEDULE
```

日本語：

税務欠損金（NOL）の繰越明細表


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:141

原文：

```text
Beginning NOL Balance (Year 1 / Formation = 0)
```

日本語：

`Beginning NOL Balance (Year 1 / Formation = 0)`

期首NOL残高（1年目 / 設立時 = 0）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:142

原文：

```text
+ NOL Generated (if EBT < 0, then ABS(EBT), else 0)
```

日本語：

`+ NOL Generated (if EBT < 0, then ABS(EBT), else 0)`

+ NOL 生成 (EBT < 0 の場合は ABS(EBT)、それ以外の場合は 0)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:143

原文：

```text
- NOL Utilized (limited by taxable income and utilization cap)
```

日本語：

- NOL利用額（課税所得と利用上限によって制限）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:144

原文：

```text
= Ending NOL Balance
```

日本語：

`= Ending NOL Balance`

= 期末NOL残高


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:146

原文：

```text
STARTING BALANCE RULE
```

日本語：

開始残高ルール


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:148

原文：

```text
For a new business or first modeled period:
```

日本語：

新しいビジネスまたは最初のモデル期間の場合:


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:149

原文：

```text
  Beginning NOL Balance = 0
```

日本語：

`Beginning NOL Balance = 0`

開始NOL残高 = 0


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:150

原文：

```text
  NOL can only increase through realized losses (EBT < 0)
```

日本語：

`NOL can only increase through realized losses (EBT < 0)`

NOL は実現損失 (EBT < 0) を通じてのみ増加します。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:151

原文：

```text
  NOL cannot be created from thin air or assumed
```

日本語：

NOLを根拠なく作り出したり、存在するものとして仮定したりしてはならない。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:153

原文：

```text
NOL UTILIZATION CALCULATION
```

日本語：

NOL利用額の計算


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:155

原文：

```text
Pre-Tax Income (EBT)
```

日本語：

税引前利益 (EBT)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:156

原文：

```text
  If EBT > 0:
```

日本語：

`If EBT > 0:`

EBT > 0の場合:


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:157

原文：

```text
    NOL Available = Beginning NOL Balance
```

日本語：

`NOL Available = Beginning NOL Balance`

利用可能なNOL = 期首NOL残高


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:158

原文：

```text
    Utilization Limit = EBT × 80%  (post-2017 federal limit)
```

日本語：

`Utilization Limit = EBT × 80%  (post-2017 federal limit)`

利用上限 = EBT × 80%（2017年以降の連邦税上の制限）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:159

原文：

```text
    NOL Utilized = MIN(NOL Available, Utilization Limit)
```

日本語：

`NOL Utilized = MIN(NOL Available, Utilization Limit)`

NOL利用額 = MIN（利用可能なNOL、利用上限）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:160

原文：

```text
    Taxable Income = EBT - NOL Utilized
```

日本語：

`Taxable Income = EBT - NOL Utilized`

課税所得 = EBT - NOL利用額


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:161

原文：

```text
  If EBT ≤ 0:
```

日本語：

`If EBT ≤ 0:`

EBT ≤ 0 の場合:


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:162

原文：

```text
    NOL Utilized = 0
```

日本語：

`NOL Utilized = 0`

NOL利用額 = 0


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:163

原文：

```text
    Taxable Income = 0
```

日本語：

`Taxable Income = 0`

課税所得 = 0


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:164

原文：

```text
    NOL Generated = ABS(EBT)
```

日本語：

`NOL Generated = ABS(EBT)`

NOL発生額 = ABS(EBT)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:166

原文：

```text
TAX CALCULATION WITH NOL
```

日本語：

NOLを使用した税金の計算


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:168

原文：

```text
Taxes Payable = MAX(0, Taxable Income × Tax Rate)
```

日本語：

`Taxes Payable = MAX(0, Taxable Income × Tax Rate)`

支払うべき税金 = MAX(0, 課税所得 × 税率)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:169

原文：

```text
  (Taxes cannot be negative; losses create NOL asset instead)
```

日本語：

（税額は負にできない。損失が生じた場合は代わりにNOL資産が生じる。）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:171

原文：

```text
DEFERRED TAX ASSET (DTA) FOR NOL
```

日本語：

NOLの繰延税金資産(DTA)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:173

原文：

```text
DTA - NOL Carryforward = Ending NOL Balance × Tax Rate
```

日本語：

`DTA - NOL Carryforward = Ending NOL Balance × Tax Rate`

繰越NOLに係る繰延税金資産（DTA） = 期末NOL残高 × 税率


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:174

原文：

```text
ΔDTA = Current DTA - Prior DTA
```

日本語：

`ΔDTA = Current DTA - Prior DTA`

DTAの増減（ΔDTA） = 当期DTA - 前期DTA


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:175

原文：

```text
  (Increase in DTA = non-cash benefit on CF)
```

日本語：

`(Increase in DTA = non-cash benefit on CF)`

（DTAの増加 = キャッシュフロー上の非現金の利益）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:176

原文：

```text
  (Decrease in DTA = non-cash expense on CF)
```

日本語：

`(Decrease in DTA = non-cash expense on CF)`

（DTAの減少 = キャッシュフロー上の非現金の費用）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:183

原文：

```text
  Cash (from CF ending cash)
```

日本語：

現金（CF期末現金より）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:184

原文：

```text
  Accounts Receivable (from WC)
```

日本語：

売掛金（運転資本（WC）の明細から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:185

原文：

```text
  Inventory (from WC)
```

日本語：

棚卸資産（運転資本（WC）の明細から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:186

原文：

```text
  Total Current Assets
```

日本語：

流動資産合計


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:188

原文：

```text
  PP&E, Net (from DA)
```

日本語：

有形固定資産純額（PP&E、DA明細から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:189

原文：

```text
  Deferred Tax Asset - NOL (from NOL schedule)
```

日本語：

繰延税金資産 - NOL (NOLスケジュールより)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:190

原文：

```text
  Total Non-Current Assets
```

日本語：

非流動資産合計


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:191

原文：

```text
  Total Assets
```

日本語：

総資産


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:194

原文：

```text
  Accounts Payable (from WC)
```

日本語：

買掛金（運転資本（WC）の明細から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:195

原文：

```text
  Current Portion of Debt (from Debt)
```

日本語：

1年内返済予定の有利子負債（Debt明細から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:196

原文：

```text
  Total Current Liabilities
```

日本語：

流動負債合計


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:198

原文：

```text
  Long-Term Debt (from Debt)
```

日本語：

長期有利子負債（Debt明細から）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:199

原文：

```text
  Total Liabilities
```

日本語：

負債総額


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:202

原文：

```text
  Common Stock
```

日本語：

普通株式


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:203

原文：

```text
  Retained Earnings (from RE schedule)
```

日本語：

利益剰余金（REスケジュールより）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:204

原文：

```text
  Total Equity
```

日本語：

総資本


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:206

原文：

```text
CHECK: Assets - Liabilities - Equity = 0
```

日本語：

`CHECK: Assets - Liabilities - Equity = 0`

チェック: 資産 - 負債 - 資本 = 0


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:212

原文：

```text
CASH FROM OPERATIONS (CFO)
```

日本語：

営業活動によるキャッシュ (CFO)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:213

原文：

```text
  Net Income (LINK: IS)
```

日本語：

純利益 (リンク: IS)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:214

原文：

```text
  + D&A (LINK: DA schedule)
```

日本語：

+ D&A (リンク: DA スケジュール)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:215

原文：

```text
  + Stock-Based Compensation (SBC) (LINK: IS or Assumptions)
```

日本語：

+ 株式ベースの報酬 (SBC) (リンク: IS または仮定)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:216

原文：

```text
  - ΔDTA (Deferred Tax Asset) (LINK: NOL schedule; increase in DTA = use of cash)
```

日本語：

`- ΔDTA (Deferred Tax Asset) (LINK: NOL schedule; increase in DTA = use of cash)`

- ΔDTA (繰延税金資産) (リンク: NOL スケジュール、DTA の増加 = 現金の使用)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:217

原文：

```text
  - ΔAR (LINK: WC)
```

日本語：

- ΔAR (リンク: WC)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:218

原文：

```text
  - ΔInventory (LINK: WC)
```

日本語：

`- ΔInventory (LINK: WC)`

- Δ在庫 (リンク: WC)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:219

原文：

```text
  + ΔAP (LINK: WC)
```

日本語：

+ ΔAP（買掛金増減、リンク：WC明細）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:220

原文：

```text
  = CFO
```

日本語：

= CFO


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:222

原文：

```text
CASH FROM INVESTING (CFI)
```

日本語：

投資活動によるキャッシュフロー（CFI）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:223

原文：

```text
  - CapEx (LINK: DA schedule)
```

日本語：

- CapEx (リンク: DA スケジュール)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:224

原文：

```text
  = CFI
```

日本語：

`= CFI`

=CFI


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:226

原文：

```text
CASH FROM FINANCING (CFF)
```

日本語：

財務活動によるキャッシュフロー（CFF）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:227

原文：

```text
  + Debt Issuance (LINK: Debt)
```

日本語：

+ 有利子負債の発行・借入（リンク：Debt明細）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:228

原文：

```text
  - Debt Repayment (LINK: Debt)
```

日本語：

- 有利子負債の返済（リンク：Debt明細）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:229

原文：

```text
  + Equity Issuance (LINK: BS Common Stock/APIC)
```

日本語：

+ 株式発行 (リンク: BS 普通株式/APIC)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:230

原文：

```text
  - Dividends (LINK: RE schedule)
```

日本語：

- 配当金 (リンク: REスケジュール)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:231

原文：

```text
  = CFF
```

日本語：

`= CFF`

=CFF


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:233

原文：

```text
Net Change in Cash = CFO + CFI + CFF
```

日本語：

`Net Change in Cash = CFO + CFI + CFF`

現金の純変動 = CFO + CFI + CFF


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:234

原文：

```text
Beginning Cash
```

日本語：

期首現金


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:235

原文：

```text
+ Net Change in Cash
```

日本語：

+ 現金の純変動


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:236

原文：

```text
= Ending Cash (LINK TO: BS Cash)
```

日本語：

`= Ending Cash (LINK TO: BS Cash)`

= 期末現金（リンク先：貸借対照表（BS）の現金）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:242

原文：

```text
Net Revenue
```

日本語：

純収益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:243

原文：

```text
  Growth %
```

日本語：

成長率


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:244

原文：

```text
(-) Cost of Revenue
```

日本語：

(-) 収益原価


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:245

原文：

```text
  % of Net Revenue
```

日本語：

純収益の%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:247

原文：

```text
Gross Profit (= Net Revenue - Cost of Revenue)
```

日本語：

`Gross Profit (= Net Revenue - Cost of Revenue)`

粗利益 (= 純収益 - 収益原価)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:248

原文：

```text
  Gross Margin %
```

日本語：

粗利率 %


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:251

原文：

```text
  % of Net Revenue
```

日本語：

純収益の%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:253

原文：

```text
  % of Net Revenue
```

日本語：

純収益の%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:255

原文：

```text
  % of Net Revenue
```

日本語：

純収益の%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:257

原文：

```text
(-) SBC
```

日本語：

(-)SBC


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:258

原文：

```text
  % of Net Revenue
```

日本語：

純収益の%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:261

原文：

```text
  EBIT Margin %
```

日本語：

EBITマージン%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:264

原文：

```text
  EBITDA Margin %
```

日本語：

EBITDAマージン%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:266

原文：

```text
(-) Interest Expense
```

日本語：

(-) 支払利息


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:268

原文：

```text
EBT (Pre-Tax Income)
```

日本語：

EBT (税引前利益)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:269

原文：

```text
(-) NOL Utilization (from NOL schedule, reduces taxable income)
```

日本語：

`(-) NOL Utilization (from NOL schedule, reduces taxable income)`

(-) NOL 利用 (NOL スケジュールから、課税所得が減少)


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:271

原文：

```text
Taxable Income
```

日本語：

課税所得


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:272

原文：

```text
(-) Taxes (Taxable Income × Tax Rate)
```

日本語：

`(-) Taxes (Taxable Income × Tax Rate)`

(-) 税金（課税所得×税率）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:274

原文：

```text
Net Income
```

日本語：

当期純利益


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:275

原文：

```text
  Net Income Margin %
```

日本語：

純利益率%


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:281

原文：

```text
BS Balance Check:       = Assets - Liabilities - Equity  (must = 0)
```

日本語：

`BS Balance Check:       = Assets - Liabilities - Equity  (must = 0)`

貸借対照表の検算：資産 - 負債 - 自己資本。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:282

原文：

```text
Cash Tie-Out:           = BS Cash - CF Ending Cash       (must = 0)
```

日本語：

`Cash Tie-Out:           = BS Cash - CF Ending Cash       (must = 0)`

現金残高の突合：BSの現金 - CFの期末現金。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:283

原文：

```text
RE Roll-Forward:        = Prior RE + NI + SBC - Div - BS RE  (must = 0)
```

日本語：

`RE Roll-Forward:        = Prior RE + NI + SBC - Div - BS RE  (must = 0)`

利益剰余金の繰越計算：前期RE + NI + SBC - Div - BSのRE。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:284

原文：

```text
DTA Tie-Out:            = NOL Schedule DTA - BS DTA      (must = 0)
```

日本語：

`DTA Tie-Out:            = NOL Schedule DTA - BS DTA      (must = 0)`

繰延税金資産の突合：NOL明細表のDTA - BSのDTA。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:285

原文：

```text
Equity Raise Tie-Out:   = ΔCommon Stock/APIC (BS) - Equity Issuance (CFF)  (must = 0)
```

日本語：

`Equity Raise Tie-Out:   = ΔCommon Stock/APIC (BS) - Equity Issuance (CFF)  (must = 0)`

増資の突合：BSの普通株式/APICの増減 - CFFの株式発行による調達額。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:286

原文：

```text
Year 0 Equity Tie-Out:  = Equity Raised (Year 0) - Beginning Equity (Year 1)  (must = 0)
```

日本語：

`Year 0 Equity Tie-Out:  = Equity Raised (Year 0) - Beginning Equity (Year 1)  (must = 0)`

0年目の増資の突合：0年目の増資調達額 - 1年目の期首自己資本。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:287

原文：

```text
Cash Monthly vs Annual: = Closing Cash (Monthly) - Closing Cash (Annual)  (must = 0)
```

日本語：

`Cash Monthly vs Annual: = Closing Cash (Monthly) - Closing Cash (Annual)  (must = 0)`

月次と年次の現金の突合：月次の期末現金 - 年次の期末現金。必ず0であること。


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:288

原文：

```text
NOL Utilization Cap:    = NOL Utilized ≤ EBT × 80%       (must be TRUE for post-2017)
```

日本語：

`NOL Utilization Cap:    = NOL Utilized ≤ EBT × 80%       (must be TRUE for post-2017)`

NOL利用額の上限：NOL利用額 ≤ EBT × 80%（2017年以降は必ずTRUEであること）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:289

原文：

```text
NOL Non-Negative:       = Ending NOL Balance ≥ 0         (must be TRUE)
```

日本語：

`NOL Non-Negative:       = Ending NOL Balance ≥ 0         (must be TRUE)`

NOL残高の非負確認：期末NOL残高 ≥ 0（必ずTRUEであること）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:290

原文：

```text
NOL Starting Balance:   = Beginning NOL (Year 1) = 0     (must be TRUE for new business)
```

日本語：

`NOL Starting Balance:   = Beginning NOL (Year 1) = 0     (must be TRUE for new business)`

NOL期首残高：1年目の期首NOL = 0（新規事業では必ずTRUEであること）


### plugins/agent-plugins/model-builder/skills/3-statement-model/references/formulas.md:291

原文：

```text
NOL Accumulation:       = NOL increases only when EBT < 0 (losses generate NOL)
```

日本語：

`NOL Accumulation:       = NOL increases only when EBT < 0 (losses generate NOL)`

NOL の累積: = EBT < 0 の場合にのみ NOL が増加します (損失により NOL が生成されます)
