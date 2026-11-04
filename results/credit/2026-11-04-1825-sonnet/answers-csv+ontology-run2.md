**Q1.** A-. A01 set E01's foreign-currency long-term rating at A- on 2024-03-12, and the next action (A02) is not until 2025-06-20.

**Q2.** No. E01's only 2026 action is A03, an affirmation (AF) with the outlook moved to negative, which is not a downgrade.

**Q3.** No. I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 (2025-09-15), affirmed A with a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, so it carries the guarantor's risk, and E02's latest rating is A (A09 via E03).

**Q6.** The data supports this reading: the Country Ceiling for VD is BB (A12), and it caps foreign-currency ratings but not local-currency ones. E05's FC rating is BB (A14) and its LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's A44 is a QA record and is ignored, and I05's A29 is an instrument rating.

**Q8.** E08. A22 (2026-07-08) moved it to RD, which is a default, and nothing later changes that.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08 (RD), E09, E10 (with E17), E12, E13, E14, CV and E15. I excluded E07 (withdrawn), E04, E11 (credit opinion only), VD (ceiling only) and E16 (QA).

**Q10.** Depends. E05 is BB on a foreign-currency basis (A14, the headline rating) and BBB- on a local-currency basis (A13).

**Q11.** BBB+. A36 (2024-09-30) is the latest action on or before that date.

**Q12.** A-. A34 (2023-01-15) is the latest action on or before that date.

**Q13.** 1. Only A36 is a DG for E14; A33 is an affirmation and A35 is a watch.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26, and E17 is the same entity with no further actions before 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33); the watch in A35 was not a rating change.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement, and the rating stays A-. E13 is a different entity.

**Q18.** E06. A17 (2026-09-03) put it on RWN. E14's watch (A35) was cleared by the A33 affirmation in 2026-05.

**Q19.** E01 and E09, per A03 and A25. E06's A17 shows no outlook, and its last stated outlook was STA.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), which is not a credit event, and it had been BB.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08, through the RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 is BB+, I04 is BB, and I08 only has an expected rating.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. A37 is the Country Ceiling, not an issuer rating.

**Q29.** None. VD only has a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05 has FC BB against the VD ceiling of BB, and E15 has FC A against the CV ceiling of A. CV itself is BBB+, below the ceiling.

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no other company has a ceiling-bound rating above it.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and E10's latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent and no link to E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records, less the QA record E16, and E03 and E17 duplicate E02 and E10.

**Q38.** No. They have different LEIs (E06 and E13), so they are different entities.

**Q39.** A, from A09 (via E03, the same entity).

**Q40.** 5: E01, E02, E09, E10 and E12 (wait: E10 is DE per RATINGS), so the five are E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in DE.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record (E10) takes precedence over the RESEARCH record (E17, LU).

**Q43.** 0. The only LU record is E17, and the RATINGS record for that entity says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, and E05 is domiciled in VD.

**Q45.** No. I07 is BBB- and is local-currency debt, so the ceiling does not apply to it.

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an Expected action (A47), so it is unrated until an assignment.

**Q48.** 7. I01 to I07 are rated, and I08 is not.

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