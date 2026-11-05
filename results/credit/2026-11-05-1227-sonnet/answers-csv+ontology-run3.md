**Q1.** A-. A01 (2024-03-12) set A-, and the next action on E01's LTIDR (FC) is A02 on 2025-06-20.

**Q2.** No. E01's only 2026 actions are the affirmations A03 and A04, and the NEG outlook is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02 (subordinated), and its latest action A07 (2025-06-20) downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E02 and E03 share an LEI, so they are one entity. The latest action is A09 (2025-09-15), which affirmed A with a POS outlook.

**Q5.** The holder takes Northwind Holdings' (E02) credit risk, rated A. I03 is guaranteed by E02, whose current rating is A (A09 on the same entity via E03).

**Q6.** The FC rating is capped by the Country Ceiling. VD's ceiling is BB (A12) and E05's FC rating is BB (A14), while the LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 had downgrades A21 and A22, and E10 had A27. E16's A44 is QA test data and is ignored.

**Q8.** E08. A22 (2026-07-08) downgraded it to RD, which is a default.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is withdrawn (A19), E04 has no rating, E11 has only a credit opinion (CO), VD has only a ceiling, and E16 is QA.

**Q10.** No on the headline FC rating (BB, A14), but its LC rating is investment grade (BBB-, A13). The answer depends on the currency basis, and I took the FC rating as the headline.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the watch in A35 came later.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch.

**Q14.** None. E12's first action, A30, is dated 2024-02-01.

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26) and was not downgraded until A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33).

**Q17.** No. A17 is only a Rating Watch with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch (A35) was superseded by the affirmation A33 with no watch.

**Q19.** E01 and E09 (A03 and A25). E06's A17 leaves the outlook blank, so I did not count it.

**Q20.** No. E07's rating was withdrawn (A19), which is not a credit event, and it had no default rating.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The rating is BBB (A03).

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 (BB+) and I04 (BB) are not, and I08 is only expected (EX), so it is unrated.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes Halden Bank's (E10) credit risk, rated BBB+. I05 is guaranteed by E10, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent and is not in E09's chain.

**Q35.** 3: E09, E10 (the same entity as E17) and E11.

**Q36.** 2: E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10, and E16 is QA, which leaves 16 including the two sovereigns.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU per the RESEARCH record, E07 is withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH holds for domicile (E17).

**Q43.** 1, which is Halden Bank (E10/E17).

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. It is local-currency debt, which the ceiling does not cap, and it is rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A08's action on I08 is only EX (A47), so it is unrated until an AS action confirms it.

**Q48.** 7, which is I01 through I07.

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
"Q10": {"investment_grade": "no"},
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