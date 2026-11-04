**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action on E01 (A02) came on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, which affirmed BBB with a Negative outlook.

**Q3.** No, BB+. I02 was cut from BBB (A23) to BB+ (A07) on 2025-06-20.

**Q4.** Positive. E03 shares E02's LEI, so it is the same legal entity, and A09 (2025-09-15) is the latest action with POS.

**Q5.** The holder takes the risk of E02, the guarantor of I03 (guarantor_id), which is rated A (A09, A11).

**Q6.** The data shows no comment explaining it. It does show a Valdoria country ceiling of BB (A12) and a foreign-currency rating of BB for E05 (A14) against a local-currency rating of BBB- (A13). The foreign-currency rating appears to be held at the ceiling.

**Q7.** E08, E10 and E16. E08 was downgraded in A21 and A22, E10 in A27, and E16 in A44. A29 is an instrument downgrade (I05), not an issuer one, and A17 is only a watch.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and no later action changes that.

**Q9.** 13. The issuers are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country ceiling (CC), and E11 has only a CO-type rating (A46).

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30, and A35 (2025-11-20) is only a watch.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 (E17 has the same LEI) was rated A- from A26 until the downgrade in A27 on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is BBB+ now (A33 affirmed it). A35 is only a watch.

**Q17.** No. A17 (2026-09-03) is a Rating Watch Negative with A- unchanged.

**Q18.** E06, from A17. E14's earlier watch (A35) was followed by an affirmation with no watch (A33).

**Q19.** E01 (A03) and E09 (A25). E06's watch row (A17) has no outlook field, so I did not count it.

**Q20.** No. A19 withdrew E07's rating for commercial reasons, and nothing indicates a default.

**Q21.** E07. It was rated BB (A18) and then withdrawn (A19).

**Q22.** E08, from A22 (RD).

**Q23.** F2, from A04.

**Q24.** Yes. E01's long-term rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's EX action (A47) is not defined in the data, so I treated it as no longer rated. If EX does not end the rating, the count would be 6.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a country ceiling record (A12, CC), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB (A14) against the Valdoria ceiling of BB (A12), and E15's is A (A41) against the Corvenia ceiling of A (A37).

**Q31.** No. Neither E05 nor E15 is above its country ceiling, and no other country has a ceiling in the data.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05, which is currently rated BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 or E10 and only shares a name.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10, and E12 is unlinked.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and different countries (DE and US).

**Q39.** A. E02 was assigned A (A08) and E03's A09 affirmed it.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because it was withdrawn.

**Q41.** BB+, from A44.

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU. I took the RATINGS record as authoritative.

**Q43.** 0. The only LU record is E17, a RESEARCH duplicate of E10, which is DE in the RATINGS record.

**Q44.** Yes, probably. I07 is denominated in XVD, which looks like Valdoria's currency, though the data does not define it.

**Q45.** No. I07 is rated BBB- (A45), matching the local-currency rating, and the BB ceiling (A12) applies to foreign-currency obligations.

**Q46.** No. E11's only rating is a CO-type record (A46), and it has no LTIDR or STIDR.

**Q47.** None, treating I08's EX action (A47) as ending the rating. The data does not define EX, so this is uncertain.

**Q48.** 7: I01 to I07. I08 is excluded on the same EX assumption as Q47.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10", "E16"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 13},
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
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```