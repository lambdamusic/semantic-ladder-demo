The credit domain at scale: the base records plus 300 invented issuers that repeat the same traps many times over. There are duplicate RESEARCH records, QA test records, group chains, finance subsidiaries, local currencies, expected ratings, withdrawals, Watches, and rows out of date order. `scale.py` builds it from a fixed seed, so a size always gives the same data, and every key is computed from the data.

It asks the same 48 questions as the base domain, but now the answers need counting and joining across 370 entity records, 115 instruments and 787 rating actions. This is where reading the data should start to fail and writing queries should pay off.

This domain still uses the version 1 rules (domicile from RATINGS). The [ownership paths](/domains/credit_paths/) domain is the same 300-issuer data on version 2.

**In this section:** the [data](/domains/credit_300/data/), the [questions](/domains/credit_300/questions/), the [ontology](/domains/credit_300/ontology/) (the base domain's), and the [results](/domains/credit_300/results/).
