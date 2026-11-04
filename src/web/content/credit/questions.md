Each question looks like a lookup, and each has an obvious wrong answer. Only the question text is sent to the model, which must give its answer as a typed JSON field. The trap and the key are never sent. Keys are computed from the data, and each base key is checked against one written by hand, so the two can't silently disagree.

## The implicit meanings

| Implicit meaning | What it says | Questions |
|---|---|---|
| **When** | A rating holds from one action to the next, so "the rating on a date" is the latest action on or before it | Q1, Q11 to Q16 |
| **Outlook and Watch** | An outlook or a Rating Watch says where a rating may go. Neither is a rating change | Q2, Q16 to Q19 |
| **Withdrawn isn't defaulted** | `WD` is a withdrawal, often for commercial reasons; `RD` and `D` are defaults | Q8, Q20 to Q22 |
| **What is rated** | Issuer, instrument, short-term, local-currency: each is a different rating | Q3, Q10, Q23 to Q27 |
| **Ceilings** | A Country Ceiling caps foreign-currency ratings in a country. It isn't the sovereign's rating | Q6, Q28 to Q31 |
| **Groups and support** | Ownership comes from parent links, not names; guaranteed debt carries the guarantor's risk | Q5, Q32 to Q36 |
| **Who is who** | Same LEI, same entity; similar names, different entities | Q4, Q37 to Q40 |

## The local meanings

| Local rule | Questions |
|---|---|
| QA records are test data: they and their actions are ignored | Q41 (also Q9, Q37, Q40) |
| Where records disagree, RESEARCH holds for country, RATINGS for name and parent | Q42, Q43 |
| `XVD` is the Valdorian dollar, `CVK` the Corvenian krone: local-currency debt, not capped | Q44, Q45 |
| `CO` is a credit opinion, which isn't a rating | Q46 |
| `EX` is an expected rating, which isn't a rating until it's assigned | Q47, Q48 |
