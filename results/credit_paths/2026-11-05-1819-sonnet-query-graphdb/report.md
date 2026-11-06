# credit_paths: claude:sonnet, 2026-11-05 18:19

61 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `sparql` | **69%** | 59% to 79% | 17 of 61 |
| `sparql+ontology` | **83%** | 78% to 89% | 27 of 61 |
| `sparql+axioms` | **80%** | 72% to 87% | 24 of 61 |

## Against `sparql`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `sparql+ontology` | +15 points | +7 to +23 |
| `sparql+axioms` | +11 points | +4 to +19 |

## By question

| Question | Graded by | `sparql` | `sparql+ontology` | `sparql+axioms` |
|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | ✅ 🟡 ✅ 🟡 🟡 | ✅ ✅ ✅ ✅ 🟡 | 🟡 🟡 ✅ 🟡 ✅ |
| Q7 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ✅ | ❌ ❌ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q11 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q12 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q13 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q14 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ✅ ✅ ✅ |
| Q15 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q16 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q17 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q18 | code | ❌ ❌ ❌ ✅ ✅ | ✅ ✅ ❌ ❌ ✅ | ✅ ❌ ✅ ❌ ✅ |
| Q19 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ❌ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q20 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q21 | code | ❌ ✅ ❌ ✅ ✅ | ✅ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ❌ ❌ |
| Q22 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q23 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q24 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q25 | code | ✅ ✅ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q26 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q27 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q28 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q29 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q30 | code | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ | ❌ ❌ ✅ ✅ ✅ |
| Q31 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q32 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q33 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q34 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q35 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ |
| Q36 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ✅ ✅ ✅ |
| Q37 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q38 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q39 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q40 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q41 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ❌ ❌ ❌ ❌ ❌ |
| Q42 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q43 | code | ✅ ❌ ✅ ❌ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q44 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q45 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ✅ ✅ ❌ | ✅ ✅ ✅ ❌ ✅ |
| Q46 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q47 | code | ✅ ✅ ✅ ❌ ❌ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ❌ ✅ |
| Q48 | code | ✅ ✅ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ❌ | ✅ ✅ ✅ ✅ ✅ |
| Q49 | code | ❌ ❌ ✅ ❌ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ |
| Q50 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ❌ ✅ ❌ ❌ |
| Q51 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ❌ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q52 | code | ❌ ✅ ❌ ❌ ❌ | ❌ ❌ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q53 | code | ❌ ✅ ✅ ✅ ❌ | ✅ ✅ ❌ ✅ ✅ | ✅ ❌ ✅ ✅ ❌ |
| Q54 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ❌ | ❌ ❌ ❌ ✅ ❌ |
| Q55 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q56 | code | ✅ ✅ ❌ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ | ✅ ❌ ❌ ✅ ✅ |
| Q57 | code | ❌ ❌ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ✅ | ✅ ❌ ✅ ✅ ✅ |
| Q58 | code | ✅ ✅ ✅ ✅ ✅ | ❌ ✅ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q59 | code | ❌ ❌ ❌ ❌ ✅ | ✅ ✅ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ❌ |
| Q60 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |
| Q61 | code | ❌ ❌ ❌ ❌ ❌ | ✅ ✅ ❌ ✅ ❌ | ✅ ❌ ✅ ✅ ✅ |

## Lists, with partial credit

The 9 questions answered with a list of entities: strict accuracy (the whole list right) against the mean F1 of the lists given, which credits a list that is nearly right.

| Condition | Strict | Mean F1 |
|---|---|---|
| `sparql` | 53% | 81% |
| `sparql+ontology` | 62% | 78% |
| `sparql+axioms` | 47% | 68% |

**The checklist grader agreed with itself** on 14 of 15 answers graded twice.

## Why each miss was marked

**Q3.** Is Kestrel Energy's 2031 note investment grade?

- `sparql+axioms` run 2: investment_grade: expected no, got yes; rating: expected BB+, got BBB

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `sparql` run 2: Identifies the BB Country Ceiling and says it fits a cap on the foreign-currency rating, but hedges ('no explicit reason') and doesn't state that the ceiling caps foreign-currency but not local-currency ratings.
- `sparql` run 4: Names the BB Country Ceiling as the plausible cause, but never says it caps foreign-currency ratings and not local-currency ones, and hedges that no explicit reason is given.
- `sparql` run 5: Cites the BB Country Ceiling and the FC/LC ratings but says no reason is stated, never asserting the ceiling caps foreign-currency ratings and not local-currency ones as the cause.
- `sparql+ontology` run 5: Names the BB Country Ceiling as the cause, but never says the ceiling caps foreign-currency ratings and not local-currency ones; it only implies this.
- `sparql+axioms` run 1: Names the BB Country Ceiling and says foreign-currency ratings are subject to it, but hedges that the causal link isn't stated and doesn't say the ceiling doesn't cap local-currency ratings.
- `sparql+axioms` run 2: Names the BB Country Ceiling as the cause, but does not state that the ceiling caps foreign-currency ratings and not local-currency ones.
- `sparql+axioms` run 4: Mentions the BB country ceiling alongside the ratings but never states it as the cause or that it caps foreign-currency ratings only, not local-currency.

**Q7.** Which issuers were downgraded in 2026?

- `sparql` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E1285', 'E1300', 'E1151', 'E1167', 'E1080', 'E5113', 'E1051', 'E10', 'E1034', 'E1347', 'E1343', 'E1290', 'E1350', 'E1229', 'E1342', 'E5097', 'E1351', 'E5059', 'E1255', 'E1340', 'E16', 'E1186', 'E1161', 'E1263', 'E1058', 'E1349', 'E1112', 'E08', 'E5116', 'E1170', 'E1344', 'E1228', 'E1163', 'E1243', 'E1299', 'E5019', 'E1053', 'E1348', 'E1213', 'E1346', 'E1159', 'E1057', 'E1345', 'E1064', 'E1294', 'E1093', 'E1144', 'E1307', 'E5156']
- `sparql` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E1285', 'E1300', 'E1151', 'E1167', 'E1080', 'E5113', 'E1051', 'E10', 'E1034', 'E1347', 'E1343', 'E1290', 'E1350', 'E1341', 'E1229', 'E1342', 'E5097', 'E1351', 'E5059', 'E1255', 'E1340', 'E16', 'E1186', 'E1161', 'E1263', 'E1058', 'E1349', 'E1112', 'E08', 'E5116', 'E1170', 'E1344', 'E1228', 'E1163', 'E1243', 'E5033', 'E1299', 'E5019', 'E1053', 'E1348', 'E1213', 'E1346', 'E1159', 'E1057', 'E1345', 'E1064', 'E1294', 'E1093', 'E1144', 'E1307', 'E5156']
- `sparql` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10', 'E16', 'E5019']
- `sparql` run 4: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E1340', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351', 'E16', 'E5019', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156']
- `sparql` run 5: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E1285', 'E1300', 'E1151', 'E1167', 'E1080', 'E5113', 'E1051', 'E10', 'E1034', 'E1347', 'E1343', 'E1290', 'E1350', 'E1341', 'E1229', 'E1342', 'E5097', 'E1351', 'E5059', 'E1255', 'E1340', 'E16', 'E1186', 'E1161', 'E1263', 'E1058', 'E1349', 'E1112', 'E08', 'E5116', 'E1170', 'E1344', 'E1228', 'E1163', 'E1243', 'E5033', 'E1299', 'E5019', 'E1053', 'E1348', 'E1213', 'E1346', 'E1159', 'E1057', 'E1345', 'E1064', 'E1294', 'E1093', 'E1144', 'E1307', 'E5156']
- `sparql+ontology` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1161', 'E1163', 'E1167', 'E1170', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1299', 'E1300', 'E1307', 'E5019', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156']
- `sparql+ontology` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10']
- `sparql+ontology` run 5: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10']
- `sparql+axioms` run 1: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E10', 'E16']
- `sparql+axioms` run 2: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10', 'E16']
- `sparql+axioms` run 3: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E1285', 'E1300', 'E1151', 'E1167', 'E1080', 'E5113', 'E1051', 'E10', 'E1034', 'E1347', 'E1343', 'E1290', 'E1350', 'E1341', 'E1229', 'E1342', 'E5097', 'E1351', 'E5059', 'E1255', 'E1340', 'E16', 'E1186', 'E1161', 'E1263', 'E1058', 'E1349', 'E1112', 'E08', 'E5116', 'E1170', 'E1344', 'E1228', 'E1163', 'E1243', 'E5033', 'E1299', 'E5019', 'E1053', 'E1348', 'E1213', 'E1346', 'E1159', 'E1057', 'E1345', 'E1064', 'E1294', 'E1093', 'E1144', 'E1307', 'E5156']
- `sparql+axioms` run 4: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E1340', 'E1341', 'E1342', 'E1343', 'E1344', 'E1345', 'E1346', 'E1347', 'E1348', 'E1349', 'E1350', 'E1351', 'E16', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156']
- `sparql+axioms` run 5: issuers: expected ['E08', 'E10', 'E1034', 'E1051', 'E1053', 'E1057', 'E1058', 'E1064', 'E1080', 'E1093', 'E1112', 'E1144', 'E1151', 'E1159', 'E1160', 'E1163', 'E1167', 'E1169', 'E1186', 'E1213', 'E1228', 'E1229', 'E1243', 'E1255', 'E1263', 'E1285', 'E1290', 'E1294', 'E1298', 'E1300', 'E1307', 'E5019', 'E5033', 'E5059', 'E5097', 'E5113', 'E5116', 'E5156'], got ['E1285', 'E1300', 'E1151', 'E1167', 'E1080', 'E5113', 'E1051', 'E10', 'E1034', 'E1347', 'E1343', 'E1290', 'E1350', 'E1341', 'E1229', 'E1342', 'E5097', 'E1351', 'E5059', 'E1255', 'E1340', 'E16', 'E1186', 'E1161', 'E1263', 'E1058', 'E1349', 'E1112', 'E08', 'E5116', 'E1170', 'E1344', 'E1228', 'E1163', 'E1243', 'E5033', 'E1299', 'E5019', 'E1053', 'E1348', 'E1213', 'E1346', 'E1159', 'E1057', 'E1345', 'E1064', 'E1294', 'E1093', 'E1144', 'E1307', 'E5156']

**Q9.** As of 1 October 2026, how many distinct issuers hold an issuer rating?

- `sparql` run 1: count: expected 377, got 393
- `sparql` run 2: count: expected 377, got 391
- `sparql` run 3: count: expected 377, got 190
- `sparql` run 4: count: expected 377, got 393
- `sparql` run 5: count: expected 377, got 391
- `sparql+ontology` run 3: count: expected 377, got None
- `sparql+axioms` run 1: count: expected 377, got 378
- `sparql+axioms` run 2: count: expected 377, got 378

**Q10.** Is Valdoria Telecom investment grade?

- `sparql+ontology` run 5: investment_grade: expected depends, got no

**Q14.** What was Halden Foods' rating on 1 January 2024?

- `sparql+axioms` run 1: rating: expected none, got BB-
- `sparql+axioms` run 2: rating: expected none, got BB-

**Q18.** Which issuers were on Rating Watch Negative on 1 October 2026?

- `sparql` run 1: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E1203', 'E1314', 'E1194', 'E1210', 'E1260', 'E1133', 'E1146', 'E1242', 'E1066', 'E1168', 'E1297', 'E1109', 'E1061', 'E1132', 'E1088', 'E06', 'E1098', 'E1266', 'E1006', 'E1267', 'E1037', 'E1013', 'E1317', 'E1181', 'E1323', 'E1099', 'E1238', 'E1264', 'E1039', 'E1126']
- `sparql` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06']
- `sparql` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06']
- `sparql+ontology` run 3: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06']
- `sparql+ontology` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06', 'E1088', 'E1006', 'E1066', 'E1019', 'E1061', 'E1098', 'E1013', 'E1059', 'E1039', 'E1181', 'E1109', 'E1194', 'E1133', 'E1146', 'E1132', 'E1126', 'E1238', 'E1209', 'E1260', 'E1297', 'E1242', 'E1266', 'E1264', 'E1314', 'E1317', 'E1323']
- `sparql+axioms` run 2: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06']
- `sparql+axioms` run 4: issuers: expected ['E06', 'E1006', 'E1013', 'E1019', 'E1037', 'E1039', 'E1059', 'E1061', 'E1066', 'E1088', 'E1098', 'E1099', 'E1109', 'E1126', 'E1132', 'E1133', 'E1146', 'E1168', 'E1181', 'E1194', 'E1203', 'E1209', 'E1238', 'E1242', 'E1260', 'E1264', 'E1266', 'E1267', 'E1297', 'E1314', 'E1317', 'E1323'], got ['E06']

**Q19.** Which issuers had a Negative outlook on 1 October 2026?

- `sparql` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1080', 'E1105', 'E5113', 'E1034', 'E1347', 'E1343', 'E1118', 'E1056', 'E1064', 'E1350', 'E1342', 'E1055', 'E5097', 'E1351', 'E1046', 'E5059', 'E5020', 'E1340', 'E1161', 'E1263', 'E1282', 'E01', 'E5131', 'E5023', 'E5141', 'E5116', 'E09', 'E1271', 'E5039', 'E5102', 'E1344', 'E1228', 'E1060', 'E5073', 'E1079', 'E5019', 'E5050', 'E5062', 'E1348', 'E1072', 'E1190', 'E1005', 'E1345', 'E1248', 'E5057', 'E1294', 'E1188', 'E5119', 'E5170', 'E1029', 'E5013', 'E1262', 'E1158', 'E5156', 'E1211']
- `sparql` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1064', 'E5113', 'E5039', 'E1161', 'E5141', 'E1080', 'E1105', 'E1072', 'E1211', 'E1005', 'E1034', 'E1347', 'E1343', 'E1271', 'E1118', 'E1158', 'E1056', 'E1248', 'E1350', 'E1345', 'E5062', 'E1342', 'E5057', 'E1055', 'E5097', 'E1351', 'E1046', 'E5059', 'E5020', 'E1340', 'E1263', 'E1348', 'E5073', 'E1188', 'E1282', 'E01', 'E5102', 'E1029', 'E5131', 'E5023', 'E5116', 'E09', 'E1344', 'E1228', 'E1060', 'E1079', 'E5019', 'E5050', 'E1262', 'E5013', 'E1190', 'E5119', 'E1294', 'E5170', 'E5156']
- `sparql` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E01', 'E09', 'E5013', 'E5019', 'E5020', 'E5039', 'E5050', 'E5057']
- `sparql` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1080', 'E1105', 'E5113', 'E1034', 'E1347', 'E1343', 'E1118', 'E1056', 'E1064', 'E1350', 'E1342', 'E1055', 'E5097', 'E1351', 'E1046', 'E5059', 'E5020', 'E1340', 'E1161', 'E1263', 'E1282', 'E01', 'E5131', 'E5023', 'E5141', 'E5116', 'E09', 'E1271', 'E5039', 'E5102', 'E1344', 'E1228', 'E1060', 'E5073', 'E1079', 'E5019', 'E5050', 'E5062', 'E1348', 'E1072', 'E1190', 'E1005', 'E1345', 'E1248', 'E5057', 'E1294', 'E1188', 'E5119', 'E5170', 'E1029', 'E5013', 'E1262', 'E1158', 'E5156', 'E1211']
- `sparql` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1080', 'E1105', 'E5113', 'E1034', 'E1347', 'E1343', 'E1118', 'E1056', 'E1064', 'E1350', 'E1342', 'E1055', 'E5097', 'E1351', 'E1046', 'E5059', 'E5020', 'E1340', 'E1161', 'E1263', 'E1282', 'E01', 'E5131', 'E5023', 'E5141', 'E5116', 'E09', 'E1271', 'E5039', 'E5102', 'E1344', 'E1228', 'E1060', 'E5073', 'E1079', 'E5019', 'E5050', 'E5062', 'E1348', 'E1072', 'E1190', 'E1005', 'E1345', 'E1248', 'E5057', 'E1294', 'E1188', 'E5119', 'E5170', 'E1029', 'E5013', 'E1262', 'E1158', 'E5156', 'E1211']
- `sparql+ontology` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E01', 'E09']
- `sparql+ontology` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E01', 'E09', 'E1064', 'E1080', 'E1072', 'E1005', 'E1034', 'E1055', 'E1046', 'E1029', 'E1059', 'E1079', 'E1160', 'E1105', 'E1118', 'E1158', 'E1188', 'E1190', 'E1211', 'E1271', 'E1248', 'E1263', 'E1282', 'E1228', 'E1261', 'E1294', 'E1300', 'E5099', 'E5039', 'E5062', 'E5057', 'E5097', 'E5059', 'E5020', 'E5073', 'E5023', 'E5019', 'E5050', 'E5013', 'E5113', 'E5141', 'E5102', 'E5131', 'E5116', 'E5119', 'E5156']
- `sparql+axioms` run 1: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1080', 'E1105', 'E5113', 'E1034', 'E1118', 'E1056', 'E1064', 'E1055', 'E5097', 'E1046', 'E5059', 'E5020', 'E1161', 'E1263', 'E1282', 'E01', 'E5131', 'E5023', 'E5141', 'E5116', 'E09', 'E1271', 'E5039', 'E5102', 'E1228', 'E1060']
- `sparql+axioms` run 2: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E01', 'E09']
- `sparql+axioms` run 3: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1080', 'E1105', 'E5113', 'E1034', 'E1118', 'E1056', 'E1064', 'E1055', 'E5097', 'E1046', 'E5059', 'E5020', 'E1161', 'E1263', 'E1282', 'E01', 'E5131', 'E5023', 'E5141', 'E5116', 'E09', 'E1271', 'E5039', 'E5102', 'E1228', 'E1060', 'E5073', 'E5033', 'E1079', 'E5019', 'E5050', 'E5062', 'E1072', 'E1190', 'E1005', 'E1248', 'E5057', 'E1294', 'E1188', 'E5119', 'E1029', 'E5013', 'E1262', 'E1158', 'E5156', 'E1211']
- `sparql+axioms` run 4: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055']
- `sparql+axioms` run 5: issuers: expected ['E01', 'E09', 'E1005', 'E1029', 'E1034', 'E1046', 'E1055', 'E1056', 'E1059', 'E1064', 'E1072', 'E1079', 'E1080', 'E1105', 'E1118', 'E1158', 'E1160', 'E1188', 'E1190', 'E1211', 'E1228', 'E1248', 'E1261', 'E1263', 'E1271', 'E1282', 'E1294', 'E1300', 'E5013', 'E5019', 'E5020', 'E5023', 'E5039', 'E5050', 'E5057', 'E5059', 'E5062', 'E5073', 'E5097', 'E5099', 'E5102', 'E5113', 'E5116', 'E5119', 'E5131', 'E5141', 'E5156'], got ['E1300', 'E5099', 'E1080', 'E1105', 'E5113', 'E1034', 'E1118', 'E1056', 'E1064', 'E1055', 'E5097', 'E1046', 'E5059', 'E5020', 'E1161', 'E1263', 'E1282', 'E01', 'E5131', 'E5023', 'E5141', 'E5116', 'E09', 'E1271', 'E5039', 'E5102', 'E1228', 'E1060', 'E5073', 'E5033', 'E1079', 'E5019', 'E5050', 'E5062', 'E1072', 'E1190', 'E1005', 'E1248', 'E5057', 'E1294', 'E1188', 'E5119', 'E1029', 'E5013', 'E1262', 'E1158', 'E5156', 'E1211']

**Q21.** Which entities had an issuer rating at some point but no longer had one on 1 October 2026?

- `sparql` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1279']
- `sparql` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07']
- `sparql+ontology` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07']
- `sparql+ontology` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1279']
- `sparql+ontology` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1002', 'E1084', 'E1032', 'E1234', 'E1219', 'E1206', 'E1107', 'E1244', 'E1172', 'E1159', 'E1057', 'E1041', 'E07', 'E1062', 'E1277', 'E1155', 'E1254', 'E1121', 'E1063', 'E1166', 'E1021', 'E1200', 'E1279', 'E1048', 'E1124', 'E1076', 'E1138', 'E1140', 'E1316', 'E1308', 'E1007', 'E1218', 'E1225', 'E1205', 'E1320', 'E1233']
- `sparql+axioms` run 1: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07']
- `sparql+axioms` run 2: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07']
- `sparql+axioms` run 3: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1002', 'E1084', 'E1032', 'E1234', 'E1219', 'E1206', 'E1107', 'E1244', 'E1172', 'E1159', 'E1057', 'E1041', 'E1347', 'E07', 'E1062', 'E1343', 'E1277', 'E1350', 'E1345', 'E1341', 'E1155', 'E1349', 'E1254', 'E1121', 'E1063', 'E1166', 'E1021', 'E1342', 'E1200', 'E1351', 'E1048', 'E1124', 'E1340', 'E1076', 'E1138', 'E16', 'E1348', 'E1140', 'E1316', 'E1346', 'E1344', 'E1308', 'E1007', 'E1218', 'E1225', 'E1205', 'E1320', 'E1233', 'E5170']
- `sparql+axioms` run 4: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E07']
- `sparql+axioms` run 5: entities: expected ['E07', 'E1001', 'E1007', 'E1021', 'E1032', 'E1041', 'E1048', 'E1057', 'E1062', 'E1063', 'E1076', 'E1084', 'E1107', 'E1121', 'E1124', 'E1138', 'E1140', 'E1155', 'E1159', 'E1166', 'E1172', 'E1200', 'E1205', 'E1206', 'E1218', 'E1219', 'E1225', 'E1233', 'E1234', 'E1244', 'E1253', 'E1277', 'E1308', 'E1316', 'E1320'], got ['E1084', 'E1032', 'E1234', 'E1219', 'E1107', 'E1244', 'E1172', 'E1347', 'E1062', 'E1343', 'E1350', 'E1345', 'E1341', 'E1349', 'E1155', 'E1166', 'E1342', 'E1200', 'E1351', 'E1277', 'E1124', 'E1340', 'E1076', 'E1138', 'E16', 'E1348', 'E1041', 'E1159', 'E1140', 'E1346', 'E1002', 'E1344', 'E1121', 'E1308', 'E1007', 'E1316', 'E07', 'E1206', 'E1225', 'E1057', 'E1205', 'E1320', 'E1063', 'E1233', 'E1254', 'E5170', 'E1218', 'E1048', 'E1021']

**Q25.** How many instruments held an investment-grade rating on 1 October 2026?

- `sparql` run 3: count: expected 72, got None
- `sparql` run 4: count: expected 72, got 75
- `sparql` run 5: count: expected 72, got 75
- `sparql+ontology` run 3: count: expected 72, got None
- `sparql+ontology` run 5: count: expected 72, got None

**Q30.** Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?

- `sparql` run 3: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15', 'E5012', 'E5047', 'E5091', 'E5116', 'E5124'], got ['E15', 'E05', 'E5012']
- `sparql+ontology` run 3: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15', 'E5012', 'E5047', 'E5091', 'E5116', 'E5124'], got ['E05', 'E15']
- `sparql+ontology` run 5: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15', 'E5012', 'E5047', 'E5091', 'E5116', 'E5124'], got ['E5124', 'E1236', 'E1126', 'E05', 'E5047', 'E1028', 'E5012', 'E5091', 'E1194', 'E15', 'E1039', 'E5116']
- `sparql+axioms` run 1: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15', 'E5012', 'E5047', 'E5091', 'E5116', 'E5124'], got ['E05', 'E5047', 'E5012', 'E15']
- `sparql+axioms` run 2: entities: expected ['E05', 'E1028', 'E1039', 'E1101', 'E1126', 'E1194', 'E1236', 'E15', 'E5012', 'E5047', 'E5091', 'E5116', 'E5124'], got ['E05', 'E15']

**Q35.** How many entities are in the Halden group, the parent included?

- `sparql+axioms` run 1: count: expected 3, got 4

**Q36.** How many entities are in the Northwind group, the parent included?

- `sparql+axioms` run 1: count: expected 2, got 3

**Q37.** How many distinct legal entities does the data describe?

- `sparql` run 1: count: expected 497, got 511
- `sparql` run 2: count: expected 497, got 511
- `sparql` run 3: count: expected 497, got 511
- `sparql` run 4: count: expected 497, got 511
- `sparql` run 5: count: expected 497, got 511
- `sparql+ontology` run 2: count: expected 497, got 495
- `sparql+ontology` run 3: count: expected 497, got None
- `sparql+axioms` run 1: count: expected 497, got 511
- `sparql+axioms` run 2: count: expected 497, got 511
- `sparql+axioms` run 3: count: expected 497, got 511
- `sparql+axioms` run 4: count: expected 497, got 511
- `sparql+axioms` run 5: count: expected 497, got 511

**Q40.** How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?

- `sparql` run 1: count: expected 79, got 88
- `sparql` run 2: count: expected 79, got 87
- `sparql` run 3: count: expected 79, got 51
- `sparql` run 4: count: expected 79, got 88
- `sparql` run 5: count: expected 79, got 87
- `sparql+ontology` run 3: count: expected 79, got None
- `sparql+ontology` run 5: count: expected 79, got None
- `sparql+axioms` run 2: count: expected 79, got 0

**Q41.** What is Brindle Capital's current rating?

- `sparql` run 1: rating: expected none, got BB+
- `sparql` run 2: rating: expected none, got BB+
- `sparql` run 3: rating: expected none, got BB+
- `sparql` run 4: rating: expected none, got BB+
- `sparql` run 5: rating: expected none, got BB+
- `sparql+axioms` run 1: rating: expected none, got BB+
- `sparql+axioms` run 2: rating: expected none, got BB+
- `sparql+axioms` run 3: rating: expected none, got BB+
- `sparql+axioms` run 4: rating: expected none, got BB+
- `sparql+axioms` run 5: rating: expected none, got BB+

**Q42.** In which country is Halden Bank domiciled?

- `sparql` run 1: country: expected LU, got DE
- `sparql` run 2: country: expected LU, got DE
- `sparql` run 3: country: expected LU, got DE
- `sparql` run 4: country: expected LU, got DE
- `sparql` run 5: country: expected LU, got DE

**Q43.** How many distinct entities are domiciled in Luxembourg (LU)?

- `sparql` run 2: count: expected 1, got 0
- `sparql` run 4: count: expected 1, got 0
- `sparql+ontology` run 3: count: expected 1, got None

**Q45.** Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?

- `sparql` run 1: above_ceiling: expected no, got yes
- `sparql` run 2: above_ceiling: expected no, got yes
- `sparql` run 3: above_ceiling: expected no, got yes
- `sparql` run 4: above_ceiling: expected no, got yes
- `sparql+ontology` run 5: above_ceiling: expected no, got yes
- `sparql+axioms` run 4: above_ceiling: expected no, got yes

**Q47.** How is Corvenia Power's 2034 note rated?

- `sparql` run 4: rating: expected none, got A
- `sparql` run 5: rating: expected none, got A
- `sparql+axioms` run 4: rating: expected none, got A

**Q48.** How many instruments held a rating on 1 October 2026?

- `sparql` run 3: count: expected 113, got None
- `sparql` run 4: count: expected 113, got 119
- `sparql` run 5: count: expected 113, got 119
- `sparql+ontology` run 3: count: expected 113, got None
- `sparql+ontology` run 5: count: expected 113, got None

**Q49.** Who is Cerid Rosor Holdings SA's ultimate parent?

- `sparql` run 1: parent: expected E5001, got E5167
- `sparql` run 2: parent: expected E5001, got E5167
- `sparql` run 4: parent: expected E5001, got E5167
- `sparql+ontology` run 3: parent: expected E5001, got None
- `sparql+axioms` run 2: parent: expected E5001, got unknown

**Q50.** How many levels of ownership separate Cerid Rosor Holdings SA from its ultimate parent?

- `sparql` run 1: count: expected 6, got 4
- `sparql` run 2: count: expected 6, got 4
- `sparql` run 3: count: expected 6, got 4
- `sparql` run 4: count: expected 6, got 4
- `sparql+ontology` run 3: count: expected 6, got None
- `sparql+axioms` run 2: count: expected 6, got 0
- `sparql+axioms` run 4: count: expected 6, got 7
- `sparql+axioms` run 5: count: expected 6, got 7

**Q51.** How many entities are in the Cerid Group plc group, the parent included?

- `sparql` run 1: count: expected 58, got 55
- `sparql` run 2: count: expected 58, got 55
- `sparql` run 3: count: expected 58, got 170
- `sparql` run 4: count: expected 58, got 55
- `sparql` run 5: count: expected 58, got 59
- `sparql+ontology` run 2: count: expected 58, got 59
- `sparql+ontology` run 3: count: expected 58, got None
- `sparql+ontology` run 5: count: expected 58, got None
- `sparql+axioms` run 2: count: expected 58, got 0

**Q52.** How many entities are in the Rotam Group Inc group, the parent included?

- `sparql` run 1: count: expected 19, got 20
- `sparql` run 3: count: expected 19, got 18
- `sparql` run 4: count: expected 19, got 20
- `sparql` run 5: count: expected 19, got 20
- `sparql+ontology` run 1: count: expected 19, got 24
- `sparql+ontology` run 2: count: expected 19, got 25
- `sparql+ontology` run 3: count: expected 19, got None
- `sparql+ontology` run 5: count: expected 19, got None
- `sparql+axioms` run 2: count: expected 19, got 0

**Q53.** Are Belir Mining SA and Rotam Group Inc in the same group?

- `sparql` run 1: same_group: expected no, got depends
- `sparql` run 5: same_group: expected no, got depends
- `sparql+ontology` run 3: same_group: expected no, got None
- `sparql+axioms` run 2: same_group: expected no, got depends
- `sparql+axioms` run 5: same_group: expected no, got depends

**Q54.** Which members of the Wonod Group SA group are domiciled in Valdoria (VD)?

- `sparql` run 1: entities: expected ['E5106', 'E5124', 'E5130'], got ['E5124', 'E5130']
- `sparql` run 2: entities: expected ['E5106', 'E5124', 'E5130'], got ['E5124', 'E5130']
- `sparql` run 3: entities: expected ['E5106', 'E5124', 'E5130'], got []
- `sparql` run 4: entities: expected ['E5106', 'E5124', 'E5130'], got ['E5124', 'E5130']
- `sparql` run 5: entities: expected ['E5106', 'E5124', 'E5130'], got ['E5124', 'E5130']
- `sparql+ontology` run 3: entities: expected ['E5106', 'E5124', 'E5130'], got None
- `sparql+ontology` run 5: entities: expected ['E5106', 'E5124', 'E5130'], got []
- `sparql+axioms` run 1: entities: expected ['E5106', 'E5124', 'E5130'], got []
- `sparql+axioms` run 2: entities: expected ['E5106', 'E5124', 'E5130'], got []
- `sparql+axioms` run 3: entities: expected ['E5106', 'E5124', 'E5130'], got ['E5106']
- `sparql+axioms` run 5: entities: expected ['E5106', 'E5124', 'E5130'], got ['E5106', 'E5169']

**Q55.** If Valdoria (VD) came under stress, how many entities with an issuer rating in force have an entity domiciled in VD somewhere above them in their chain of parents?

- `sparql` run 1: count: expected 31, got 23
- `sparql` run 2: count: expected 31, got 23
- `sparql` run 3: count: expected 31, got None
- `sparql` run 4: count: expected 31, got 23
- `sparql+ontology` run 3: count: expected 31, got None
- `sparql+ontology` run 5: count: expected 31, got None
- `sparql+axioms` run 2: count: expected 31, got 0

**Q56.** What is the lowest current foreign-currency issuer rating held by any member of the Vesol Group BV group?

- `sparql` run 3: rating: expected BB-, got None
- `sparql+ontology` run 3: rating: expected BB-, got None
- `sparql+ontology` run 5: rating: expected BB-, got None
- `sparql+axioms` run 2: rating: expected BB-, got none
- `sparql+axioms` run 3: rating: expected BB-, got BB+

**Q57.** Which is the nearest entity that Cerid Guven Energy SA and Cerid Telecom SA both have in their chains of parents?

- `sparql` run 1: entity: expected E5002, got none
- `sparql` run 2: entity: expected E5002, got none
- `sparql+ontology` run 3: entity: expected E5002, got None
- `sparql+axioms` run 2: entity: expected E5002, got unknown

**Q58.** Which entities guarantee a note issued by an entity outside their own group?

- `sparql+ontology` run 1: entities: expected ['E5145'], got ['E5059', 'E5145']
- `sparql+ontology` run 3: entities: expected ['E5145'], got None
- `sparql+ontology` run 5: entities: expected ['E5145'], got []
- `sparql+axioms` run 2: entities: expected ['E5145'], got []

**Q59.** How many entities in the Cerid Group plc group sit exactly three levels below the top?

- `sparql` run 1: count: expected 12, got 11
- `sparql` run 2: count: expected 12, got 11
- `sparql` run 3: count: expected 12, got None
- `sparql` run 4: count: expected 12, got 11
- `sparql+ontology` run 3: count: expected 12, got None
- `sparql+ontology` run 5: count: expected 12, got None
- `sparql+axioms` run 2: count: expected 12, got 0
- `sparql+axioms` run 5: count: expected 12, got 10

**Q60.** Whose credit risk does a holder of the Cross-group 4.75% notes due 2031 take, and is that entity in the same group as the issuer?

- `sparql+ontology` run 3: risk_of: expected E5145, got None; same_group: expected no, got None
- `sparql+ontology` run 5: risk_of: expected E5145, got None; same_group: expected no, got None
- `sparql+axioms` run 2: risk_of: expected E5145, got unknown; same_group: expected no, got depends

**Q61.** How many members of the Cerid Group plc group, the top included, hold a foreign-currency issuer rating below investment grade?

- `sparql` run 1: count: expected 19, got 18
- `sparql` run 2: count: expected 19, got 18
- `sparql` run 3: count: expected 19, got None
- `sparql` run 4: count: expected 19, got 18
- `sparql` run 5: count: expected 19, got 20
- `sparql+ontology` run 3: count: expected 19, got None
- `sparql+ontology` run 5: count: expected 19, got None
- `sparql+axioms` run 2: count: expected 19, got 0

