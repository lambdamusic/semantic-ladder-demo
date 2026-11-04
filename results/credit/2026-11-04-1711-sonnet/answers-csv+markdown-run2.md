**Q1.** A-. A01 set A- for E01 on 2024-03-12, and the next LTIDR action, A02, came on 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the downgrade A02 was in 2025.

**Q3.** No, BB+. The 2031 note I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** The holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, whose latest rating is A (A09 on E03, the same LEI).

**Q6.** Not in the JSON. The Country Ceiling for VD is BB (A12), which caps the FC rating (A14, BB). The LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27 (E17 is the same entity). A44 is on E16, a QA record, so it is ignored.

**Q8.** E08. A22 set RD on 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02 (including E03), E05, E06, E08, E09, E10 (including E17), E12, E13, E14, E15 and CV. E07 was withdrawn, and E04, E11, VD and E16 have no issuer rating of their own (or are QA).

**Q10.** Depends. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (speculative, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action came after 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 an affirmation.

**Q14.** None. E12's first rating action, A30, is dated 2024-02-01.

**Q15.** A-. A26 (2023) set A- for E10, and the downgrade A27 came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now; the RW and AF actions did not change it.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch, which is not a downgrade.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's watch (A35) was cleared by A33.

**Q19.** E01 and E09. A03 and A25 set the NEG outlook.

**Q20.** No. E07 was withdrawn (A19) for commercial reasons, and it was never rated in default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The CC of A (A37) is a ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10, rated BBB+. I05 is guaranteed by E10, which was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent link to E09 or E10, and sharing the name "Halden" does not make it part of the group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10, and E16 is QA, which leaves 16.

**Q38.** No. E06 and E13 have different LEIs.

**Q39.** A (A09, on the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E07's rating was withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record for E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, and RATINGS says DE for that entity.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, which is E05's country.

**Q45.** No. The ceiling applies only to FC obligations, and I07 is local-currency debt rated BBB- (A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating (EX), so I08 stays unrated.

**Q48.** 7: I01 to I07. I08 has only an EX action.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```