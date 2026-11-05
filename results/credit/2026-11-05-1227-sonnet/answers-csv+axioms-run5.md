**Q1.** A-. A01 assigned A- on 2024-03-12, and it stayed in force until A02 on 2025-06-20.

**Q2.** No. The only 2026 action on E01's issuer rating is A03, an affirmation at BBB.

**Q3.** No, it is BB+. I02 was assigned BBB (A23), then downgraded to BB+ (A07).

**Q4.** Positive. A09 is on E03, which shares E02's LEI, so it is the same entity and supersedes A08's Stable.

**Q5.** Northwind Holdings (E02) is rated A. I03 is guaranteed by E02, so the guarantor's credit risk applies, and A09/A11 give A.

**Q6.** The data doesn't state a reason. It shows only the LC rating of BBB- (A13) against the FC rating of BB (A14), and the FC rating equals Valdoria's Country Ceiling of BB (A12).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade (A44) is excluded because it is a QA test record, and I05's downgrade is an instrument rating, not an issuer's.

**Q8.** E08. A22 put it at RD on 2026-07-08.

**Q9.** 12. These are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10 (the same entity as E17), E12, E13, E14, CV and E15. E07 is withdrawn, VD has only a ceiling, E11 has only a credit opinion, and E16 is a test record.

**Q10.** Depends. The local-currency rating is BBB-, which is investment grade (A13), but the foreign-currency rating is BB, which is not (A14).

**Q11.** BBB+. A36 downgraded it on 2024-09-30, and A35 (2025-11-20) came later.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade, and A35 is a watch placement.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 was in force until A27 on 2026-04-15, and E17 has no actions.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now (A33). The watch in A35 did not change it.

**Q17.** No. A17 is a watch placement at A-, not a downgrade.

**Q18.** E06. A17 (2026-09-03) is the latest action and carries RWN, while E14's A35 was superseded by A33.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07 was withdrawn (A19), and its last rating was BB.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08 only, from the RD rating in A22.

**Q23.** F2, from A04.

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. They are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's FC rating is A, equal to the CV ceiling of A.

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** Halden Bank (E10) is rated BBB+. E10 guarantees I05, and A27 puts it at BBB+.

**Q34.** No. E12 has no parent link, and only the name suggests a connection.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, which leaves 17, and E16 is a test record, not a legal entity.

**Q38.** No. Their LEIs differ (E06 and E13), and there is no other link between them.

**Q39.** A, from A09.

**Q40.** 5: E01, E02, E09, E12 and E14. E10's domicile is LU per the RESEARCH record.

**Q41.** None. E16 is a QA test record, so its actions are not treated as rating actions.

**Q42.** LU. The RESEARCH record E17 gives LU, and it overrides E10's DE.

**Q43.** 1. E10 and E17 are the same entity.

**Q44.** Yes. I07 is in XVD, and Valdoria's domestic currency is XVD.

**Q45.** No. The ceiling is checked only against foreign-currency issuer ratings, and I07 is a local-currency instrument.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating, so nothing is in force.

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