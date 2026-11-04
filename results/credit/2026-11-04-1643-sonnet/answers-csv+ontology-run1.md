**Q1.** A-. A01 set E01's foreign-currency LTIDR at A- on 2024-03-12, and the next action (A02) came on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with a Negative outlook, and only a DG counts as a downgrade.

**Q3.** No, it is BB+. I02 was downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive (POS). E03 has the same LEI as E02, so A09 (2025-09-15, affirmed A, POS) applies to Northwind Holdings.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's latest issuer rating is A (A09 via E03).

**Q6.** The question is not in the JSON, so for the record: A14 gives E05's FC rating as BB, which matches the Valdoria Country Ceiling of BB (A12). The LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and A44 (E16) is QA data, so both are ignored.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and RD is a default.

**Q9.** 12. The holders are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, E16 is QA, and E04, E11 and VD have no issuer rating.

**Q10.** Depends. E05's FC rating is BB (speculative), while its LC rating is BBB- (investment grade), per A13 and A14.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action was on 2025-11-20.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came later, on 2024-09-30.

**Q13.** 1. Only A36 is a DG for E14.

**Q14.** None. E12 was first rated on 2024-02-01 (A30).

**Q15.** A-. A26 set E10's rating at A-, and the downgrade A27 came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ after A35 (watch) and A33 (affirmed).

**Q17.** No. A17 is a Rating Watch action, and the rating stays A-.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's watch (A35) was cleared by the A33 affirmation without a watch flag.

**Q19.** E01 and E09. A03 and A25 give them NEG outlooks, and both are the latest actions for their entities.

**Q20.** No. A19 shows E07 was withdrawn at BB, and a withdrawal is not a default.

**Q21.** E07, which was withdrawn in A19. E16 is QA and is ignored.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's current LTIDR is BBB (A03).

**Q25.** 5. I01 is BBB, I03 is A, I05 is BBB+, I06 is A- and I07 is BBB-. I02 and I04 are speculative grade, and I08 is only an EX, so it is unrated.

**Q26.** A+, from A40.

**Q27.** A-. A42 rates I06 at A-, which is subordinated debt below E15's FC rating of A and within the CV ceiling of A.

**Q28.** BBB+, from A38. The Country Ceiling (A37) is a different thing.

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB against the VD ceiling of BB, and E15's FC rating is A against the CV ceiling of A.

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent and a different LEI, so it is not part of the E09 group.

**Q35.** 3. The group is E09, E10 and E11. E17 is the same entity as E10, because they share an LEI.

**Q36.** 2. The group is E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records, minus the duplicates E03 and E17, minus the QA record E16.

**Q38.** No. They have different LEIs, so they are different entities.

**Q39.** A, from A09 (the latest action, applied via E03).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record for E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, and E10's RATINGS record says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. The ceiling does not cap local-currency debt, so I07's BBB- (A45) is not above what the ceiling allows.

**Q46.** No. E11's only action is A46, a credit opinion, which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating (EX), so I08 stays unrated.

**Q48.** 7, I01 to I07. I08 has only an EX.

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