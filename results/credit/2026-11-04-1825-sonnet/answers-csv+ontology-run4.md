**Q1.** A-. A01 set E01's FC LTIDR at A- on 2024-03-12, and the next action (A02) was on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation (BBB, outlook NEG).

**Q3.** No, it is BB+. I02 is subordinated, and A07 downgraded it to BB+ on 2025-06-20.

**Q4.** Positive (POS). E03 has the same LEI as E02, so it is the same entity, and A09 (2025-09-15) affirmed A with a POS outlook.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, whose latest rating is A (A08, affirmed under the E03 record in A09).

**Q6.** The Country Ceiling for VD is BB (A12), which caps foreign-currency ratings (A14, BB). The local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and A44 is on QA record E16, so it is ignored.

**Q8.** E08. A22 downgraded it to RD (a default) on 2026-07-08, with no later action.

**Q9.** 12. These are E01, E02 (same entity as E03), E05, E06, E08, E09, E10 (same entity as E17), E12, E13, E14, CV and E15. E07 is withdrawn, E04 and E11 have no issuer rating (E11 has only a credit opinion), VD has only a ceiling, and E16 is QA.

**Q10.** Depends on the currency basis. The FC rating is BB, which is speculative grade (A14), and the LC rating is BBB-, which is investment grade (A13). The FC rating is the headline one.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action (A35) was after 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, and A36 came later.

**Q13.** 1. Only A36 is a downgrade. A35 is a Watch, and A33 is an affirmation.

**Q14.** None. E12's first rating, A30, was assigned on 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26, and the downgrade A27 came on 2026-04-15. E17 is the same entity as E10, and the RATINGS record holds.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33 affirmed it). The 2025-11-20 Watch (A35) did not change the rating.

**Q17.** No. A17 (2026-09-03) is a Rating Watch, and the rating stays A-.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's RWN (A35) was cleared by the affirmation A33, which has no watch.

**Q19.** E01 and E09, from A03 and A25, both NEG.

**Q20.** No. A19 is a withdrawal for commercial reasons, which is not a credit event.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are speculative grade, and I08 is only an Expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The Country Ceiling (A37) and the LC rating (A39) are different things.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB. E15's FC rating is A, equal to CV's ceiling of A.

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, which A27 downgraded to BBB+.

**Q34.** No. E12 has no parent, and E09 and E10 are unrelated to it.

**Q35.** 3: E09, E10 (E17 is the same entity) and E11.

**Q36.** 2: E02 (E03 is the same entity) and E04.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA test data.

**Q38.** No. They have different LEIs, countries and names, and no link in the data.

**Q39.** A (A09 affirmed A, under the E03 record).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn, E16 is QA, and E10 is DE in RATINGS.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, and the RATINGS record for the same entity says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating, and as a finance subsidiary its risk sits with the parent.

**Q47.** None. I08 has only an Expected action (A47), and no Assigned action has confirmed it.

**Q48.** 7: I01 to I07. I08 is unrated.

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