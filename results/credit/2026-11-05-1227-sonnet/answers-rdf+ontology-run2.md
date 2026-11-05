**Q1.** A-. E01's FC LTIDR was assigned A- on 2024-03-12 (A01) and not changed until the downgrade of 2025-06-20 (A02).

**Q2.** No. E01's only 2026 action is an affirmation at BBB on 2026-02-10 (A03, A04); the outlook went to Negative, which is not a downgrade.

**Q3.** No. The 2031 note (I02, subordinated) has been rated BB+ since 2025-06-20 (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action is an affirmation with a Positive outlook on 2025-09-15 (A09).

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest rating is A (A09).

**Q6.** Not a graded question, but the data explains it. E05's FC rating is BB (A14) and its LC rating is BBB- (A13). Valdoria's Country Ceiling is BB (A12) and caps FC ratings but not LC ones.

**Q7.** E08 and E10. E08 was downgraded on 2026-01-20 and 2026-07-08 (A21, A22), and E10 on 2026-04-15 (A27). E16's downgrade (A44) is QA test data and is ignored, and E06's Watch (A17) is not a downgrade.

**Q8.** E08. It was rated RD, a default, from 2026-07-08 (A22).

**Q9.** 12. These are E01, E02 (also recorded as E03), E05, E06, E08, E09, E10 (also E17), E12, E13, E14, E15 and CV. E07 was withdrawn (A19), VD has only a Country Ceiling, E11 has only a credit opinion, and E16 is QA.

**Q10.** Depends. E05's FC rating is BB (speculative, A14), but its LC rating is BBB- (investment grade, A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the Watch of 2025-11-20 (A35) came later.

**Q12.** A-. It was assigned on 2023-01-15 (A34).

**Q13.** 1. The only downgrade is A36; A35 is a Watch and A33 an affirmation.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. E10 (also recorded as E17) was assigned A- on 2023-05-01 (A26) and downgraded on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35, A33).

**Q17.** No. E06 was only placed on Rating Watch Negative on 2026-09-03 (A17), which is not a downgrade.

**Q18.** E06. Its Watch (A17) is current. E14's Watch (A35) was superseded by the affirmation of 2026-05-01 (A33).

**Q19.** E01 and E09. Their latest actions carry a Negative outlook (A03, A25). E06's Watch action (A17) states no outlook.

**Q20.** No. E07 was rated BB and then withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08. It was rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's FC LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A rating (A37) is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB (A14, A12), and E15's FC rating is A, equal to CV's ceiling of A (A41, A37).

**Q31.** No. E05 and E15 are at the ceiling, not above it.

**Q32.** E09. E11's parent is E10 (also recorded as E17), whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ on 2026-04-15 (A27).

**Q34.** No. E12 has no parent link and a different LEI from E09, E10 and E11, so only the name is shared.

**Q35.** 3: E09, E10 (also recorded as E17) and E11.

**Q36.** 2: E02 (also recorded as E03) and E04.

**Q37.** 16. The data has 19 records. E03 duplicates E02 and E17 duplicates E10 (same LEIs), and E16 is QA, so the 3 are excluded.

**Q38.** No. E06 and E13 have different LEIs and different countries.

**Q39.** A (A09).

**Q40.** 5: E01, E02 (also E03), E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. E17 (RESEARCH) holds for domicile and says LU, over E10's DE.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), but local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated until an Assigned action confirms it.

**Q48.** 7: I01 through I07. I08 is only Expected.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "none"},
"Q15": {"rating": "A-"},
"Q16": {"changed": "no"},
"Q17": {"downgraded": "no"},
"Q18": {"issuers": ["E06"]},
"Q19": {"issuers": ["E01", "E09"]},
"Q20": {"in_default": "no"},
"Q21": {"entities": ["E07"]},
"Q22": {"entities": ["E08"]},
"Q23": {"rating": "F2"},
"Q24": {"investment_grade": "yes"},
"Q25": {"count": 5},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "none"},
"Q30": {"entities": ["E05", "E15"]},
"Q31": {"any": "no"},
"Q32": {"parent": "E09"},
"Q33": {"risk_of": "E10", "rating": "BBB+"},
"Q34": {"same_group": "no"},
"Q35": {"count": 3},
"Q36": {"count": 2},
"Q37": {"count": 16},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```