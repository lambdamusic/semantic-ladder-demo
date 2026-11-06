Each question looks like a lookup, and each has an obvious wrong answer. Only the question text is sent to the model, which must give its answer as a typed JSON field. The trap and the key are never sent. Keys are computed from the data, and each base key is checked against one written by hand, so the two can't silently disagree. The keys shown are the base data's; the other datasets compute their own.

## The implicit meanings

| Implicit meaning | What it says | How the data sets it | Questions |
|---|---|---|---|
| **When** | A rating holds from one action to the next, so "the rating on a date" is the latest action on or before it | Kestrel Energy (E01) was A- from March 2024 and BBB from June 2025 ([Q1](#Q1)). Marlow Utilities' (E14) actions are out of date order in the file ([Q11](#Q11)). Halden Foods (E12) had no rating before its first action in February 2024 ([Q14](#Q14)) | [Q1](#Q1), [Q11](#Q11) to [Q16](#Q16) |
| **Outlook and Watch** | An outlook or a Rating Watch says where a rating may go. Neither is a rating change | Kestrel was affirmed at BBB with a Negative outlook in 2026, not downgraded ([Q2](#Q2)). Orrin Bank (E06) was placed on Watch Negative in September 2026 at an unchanged A- ([Q17](#Q17)). Marlow's Watch ended with its May 2026 affirmation ([Q16](#Q16), [Q18](#Q18)) | [Q2](#Q2), [Q16](#Q16) to [Q19](#Q19) |
| **Withdrawn isn't defaulted** | `WD` is a withdrawal, often for commercial reasons; `RD` and `D` are defaults | Pellam Retail's (E07) rating was withdrawn "for commercial reasons" in May 2026 ([Q20](#Q20), [Q21](#Q21)). Saxby Shipping (E08) went to `RD` after a distressed debt exchange ([Q8](#Q8), [Q22](#Q22)) | [Q8](#Q8), [Q20](#Q20) to [Q22](#Q22) |
| **What is rated** | Issuer, instrument, short-term, local-currency: each is a different rating | Kestrel is BBB, its subordinated 2031 note BB+ ([Q3](#Q3), [Q24](#Q24)) and its short-term rating F2 ([Q23](#Q23)). Corvenia Power (E15) is A in foreign currency and A+ in local ([Q26](#Q26)). Valdoria Telecom (E05) has no single rating ([Q10](#Q10)) | [Q3](#Q3), [Q10](#Q10), [Q23](#Q23) to [Q27](#Q27) |
| **Ceilings** | A Country Ceiling caps foreign-currency ratings in a country. It isn't the sovereign's rating | Valdoria's ceiling is BB, and the Republic has no issuer rating ([Q29](#Q29)). Valdoria Telecom is BB in foreign currency, at the ceiling, and BBB- in local ([Q6](#Q6)). Corvenia's ceiling is A, its own rating BBB+ ([Q28](#Q28)) | [Q6](#Q6), [Q28](#Q28) to [Q31](#Q31) |
| **Groups and support** | Ownership comes from parent links, not names; guaranteed debt carries the guarantor's risk | Halden Leasing (E11) sits under Halden Bank (E10), under Halden Group (E09) ([Q32](#Q32)). Its note is guaranteed by Halden Bank, not the group ([Q33](#Q33)). Halden Foods (E12) shares the name but not the group ([Q34](#Q34)). Northwind Finance's (E04) note is guaranteed by Northwind Holdings ([Q5](#Q5)) | [Q5](#Q5), [Q32](#Q32) to [Q36](#Q36) |
| **Who is who** | Same LEI, same entity; similar names, different entities | Northwind Holdings has two records with one LEI, `E02` and `E03`, and its latest action is on the second ([Q4](#Q4), [Q39](#Q39)). Orrin Bank AG (E06) and Orrin Bancorp Inc (E13) have different LEIs ([Q38](#Q38)) | [Q4](#Q4), [Q37](#Q37) to [Q40](#Q40) |

## The local meanings

Each rule is stated only in the ontology, and none can be guessed from a code's name or from general conventions.

| Local rule | How the data sets it | Where the ontology states it | Questions |
|---|---|---|---|
| QA records are test data: they and their actions are ignored | Brindle Capital (E16) comes from the QA system, with rating actions that look real: an assignment and a 2026 downgrade | `lad:sourceSystem` | [Q41](#Q41) (also [Q9](#Q9), [Q37](#Q37), [Q40](#Q40)) |
| Where records disagree, RESEARCH holds for country, RATINGS for name and parent | Halden Bank's RATINGS record (E10) puts it in Germany, its RESEARCH record (E17) in Luxembourg | `lad:sourceSystem`; `lad:country` | [Q42](#Q42), [Q43](#Q43) |
| `XVD` is the Valdorian dollar, `CVK` the Corvenian krone: local-currency debt, not capped | Valdoria Telecom's 2027 note (I07) pays in `XVD` and is rated BBB-, above Valdoria's BB ceiling, which caps only foreign-currency ratings | `lad:currency` | [Q44](#Q44), [Q45](#Q45) |
| `CO` is a credit opinion, which isn't a rating | Halden Leasing's only issuer-level action is a `CO` at BBB | `lad:type-CO` | [Q46](#Q46) |
| `EX` is an expected rating, which isn't a rating until it's assigned | Corvenia Power's 2034 note (I08) has only an expected A | `lad:action-EX` | [Q47](#Q47), [Q48](#Q48) |
