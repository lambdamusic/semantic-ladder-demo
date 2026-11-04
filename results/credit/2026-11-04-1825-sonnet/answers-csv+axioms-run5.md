**Q1.** A-. Kestrel's A- assigned on 2024-03-12 (A01) was still in force on that date. The downgrade to BBB came later, on 2025-06-20 (A02).

**Q2.** No. The only 2026 Kestrel action is an affirmation at BBB (A03, A04). The downgrade, A02, was in 2025.

**Q3.** No. The 2031 note (I02) was cut from BBB to BB+ on 2025-06-20 (A23, A07), which is sub-investment grade.

**Q4.** Positive. A09 (2025-09-15) is on E03, which shares Northwind Holdings' LEI, so it is the same entity. It replaced A08's Stable outlook.

**Q5.** The holder takes the risk of E02, Northwind Holdings, the guarantor of I03. E02 is rated A (A09, via E03).

**Q6.** The data does not state a reason. It shows only that the FC rating (BB, A14) equals Valdoria's Country Ceiling of BB (A12), while the LC rating is BBB- (A13). That is consistent with the ceiling capping the FC rating.

**Q7.** E08 and E10. E08 went to CCC and then RD in 2026 (A21, A22), and E10 went to BBB+ (A27). E16's downgrade (A44) is excluded because it is a QA test record. I05's downgrade (A29) is an instrument action.

**Q8.** E08. Its RD rating (A22) is still in force and was not withdrawn.

**Q9.** 12. These are E01, E02 (the same entity as E03), E05, E06, E08, CV, E09, E10, E12, E13, E14 and E15. E07 is withdrawn (A19), E16 is a test record, and E04, E11 and VD have no issuer rating in force.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and it stayed in force on 2025-06-01.

**Q12.** A-. This is A34, assigned 2023-01-15, before the A36 downgrade.

**Q13.** 1. A36 is the only DG on E14.

**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.

**Q15.** A-. A26 was in force until A27 on 2026-04-15. E17 shares the LEI of E10, so it is the same entity and has no actions of its own.

**Q16.** No. Marlow was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch placement that leaves the rating at A-.

**Q18.** E06 (A17, 2026-09-03). E14's earlier watch (A35) was superseded by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. Pellam's only ratings are BB (A18) and then a withdrawal (A19), with no default rating.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03), which is investment grade.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) hold investment-grade ratings in force. I08's rating is only expected.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB against Valdoria's ceiling of BB (A14, A12). E15's FC rating is A against Corvenia's ceiling of A (A41, A37).

**Q31.** No. No FC rating is above its country's ceiling.

**Q32.** E09. E11 has parent E10, which has parent E09.

**Q33.** The holder takes the risk of E10, Halden Bank, the guarantor of I05. E10 is rated BBB+ (A27).

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3: E09, E10 and E11. E17 is E10 under another record, since they share an LEI.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 records, but E03 duplicates E02 and E17 duplicates E10.

**Q38.** No. They have different LEIs, countries and records.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14, all GB-domiciled with an issuer rating in force. E10 is DE, E07 is withdrawn, and E16 is a test record.

**Q41.** None. E16 is a QA test record, so its actions are not treated as in-force ratings, though A44 shows BB+.

**Q42.** DE. E10's RATINGS record gives DE, and E17's LU is overridden because it shares E10's LEI.

**Q43.** 0. The only LU record is E17, which is E10 and therefore domiciled in DE.

**Q44.** Yes. I07 is in XVD, which is the domestic currency of VD, E05's domicile.

**Q45.** No. The ceiling check applies only to foreign-currency issuer ratings. I07 is a local-currency instrument rated BBB- (A45).

**Q46.** No. E11's only record is a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating of A (EX), which is not a rating in force.

**Q48.** 7: I01 to I07. I08 has only an expected rating.

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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 5},
"Q41": {"rating": "none"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```