**Q1.** A-. The latest action on or before 2025-01-01 is A01 (2024-03-12, A- FC), and A02 only came in June 2025.

**Q2.** No. The only 2026 actions on E01 (A03, A04) are affirmations. The outlook moved to NEG, but that is not a downgrade.

**Q3.** No, it is BB+. The 2031 note is I02, subordinated, and its latest action is A07 (2025-06-20, BB+), which is speculative grade.

**Q4.** POS. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), has a Positive outlook.

**Q5.** The holder takes E02 (Northwind Holdings) risk, rated A. I03 is guaranteed by E02, whose latest LTIDR action is A09 (A, affirmed, recorded under E03).

**Q6.** Valdoria's Country Ceiling (VD, A12) is BB and caps foreign-currency ratings. E05's FC rating is BB (A14), at the ceiling, while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A29 is an instrument rating and A44 is a QA record, which is ignored.

**Q8.** E08. Its latest action, A22 (2026-07-08), is RD, which is a default.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08 (RD still counts as a rating), E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E11 has only a credit opinion, and E04 and VD have no issuer rating.

**Q10.** No. The headline FC rating is BB (A14), although the LC rating is BBB- (A13).

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action, A35 (2025-11-20), came after the date.

**Q12.** A-. A34 (2023-01-15) assigned A-, and the downgrade A36 came later.

**Q13.** 1. Only A36 is a downgrade. A35 is a Rating Watch and A33 is an affirmation.

**Q14.** None. The first action on E12 is A30 (2024-02-01), so it was unrated on 2024-01-01.

**Q15.** A-. E10 and E17 are the same entity. A26 set A- in 2023, and the downgrade A27 came only on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The Watch and the affirmation did not change it.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's Watch (A35) was cleared by the affirmation A33 in 2026-05.

**Q19.** E01 and E09. Their latest actions, A03 and A25, carry a NEG outlook.

**Q20.** No. E07's rating was withdrawn (A19) for commercial reasons, and a withdrawal says nothing about default.

**Q21.** E07. It was rated from A18 and withdrawn by A19.

**Q22.** E08. Its RD in A22 is the only default in the data.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. Investment grade on 2026-10-01 are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are speculative grade, and I08 is unrated.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42).

**Q28.** BBB+ (A38, FC LTIDR). The CC of A (A37) is a ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB (A14, A12). E15's FC rating of A equals the CV ceiling of A (A41, A37).

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no other company's FC rating is above a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09, and E09 has no parent.

**Q33.** The holder takes E10 (Halden Bank) risk, rated BBB+. I05 is guaranteed by E10, whose latest action is A27 (BBB+).

**Q34.** No. E12 has no parent, and the Halden group is E09 with E10 and E11.

**Q35.** 3: E09, E10 (E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records, but E03 duplicates E02 and E17 duplicates E10. E16 is a QA test record and describes no real entity.

**Q38.** No. They have different LEIs (E06 and E13), so they are separate entities.

**Q39.** A (A09, affirmed, recorded under E03).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU per the RESEARCH record, E07 is withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. RESEARCH holds for domicile, so E17's LU overrides E10's DE.

**Q43.** 1, Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. I07 is local-currency debt (BBB-, A45), which the ceiling does not cap.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated until an AS action confirms it.

**Q48.** 7. I01 to I07 hold ratings, and I08 does not.

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