**Q1.** A-. The 2024-03-12 assignment (A01) was still in force on 1 Jan 2025; the downgrade (A02) came in June 2025.
**Q2.** No. The 2026 actions on Kestrel (A03, A04) are affirmations, not downgrades.
**Q3.** No, BB+. I02's latest action is the downgrade A07 (2025-06-20), to BB+, which is speculative grade.
**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) carries a POS outlook.
**Q5.** The holder takes Northwind Holdings' (E02) risk, rated A. I03 is guaranteed by E02, and E02's current rating is A (A08, A09).
**Q6.** The FC rating is held to the Country Ceiling (A12, BB) because it is subject to transfer and convertibility risk. The LC rating of BBB- (A13) is not capped.
**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E16's downgrade is QA test data and is ignored, and A29 is an instrument rating.
**Q8.** E08. Its latest action A22 sets RD, which counts as a default.
**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 is withdrawn, VD has only a ceiling, E11 has only a credit opinion, and E04 and E16 have no usable issuer rating.
**Q10.** Depends. The FC rating is BB (speculative grade, A14) and the LC rating is BBB- (investment grade, A13).
**Q11.** BBB+. The downgrade A36 (2024-09-30) was the latest action on or before that date.
**Q12.** A-. A34 (2023-01-15) was still in force.
**Q13.** 1, the downgrade A36. A35 is a Watch placement and A33 an affirmation.
**Q14.** None. Halden Foods' first rating (A30) was assigned on 2024-02-01.
**Q15.** A-. E17 is the same entity as E10, and A26 (A-) was the latest action before A27 (2026-04-15).
**Q16.** No. It was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33). A35 was only a Watch.
**Q17.** No. A17 is a Rating Watch placement with the rating unchanged at A-.
**Q18.** E06. A17 placed it on RWN. E14's Watch (A35) was cleared by the A33 affirmation.
**Q19.** E01 and E09. A03 and A25 set NEG outlooks. E10's latest outlook is STA (A27), and E08's outlook is blank.
**Q20.** No. A19 is a withdrawal for commercial reasons, which is not a default.
**Q21.** E07. Its rating was withdrawn in A19, and it has no later rating.
**Q22.** E08, which reached RD in A22.
**Q23.** F2 (A04, STIDR affirmed).
**Q24.** Yes. The LTIDR is BBB (A03).
**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is unrated.
**Q26.** A+ (A40).
**Q27.** A- (A42).
**Q28.** BBB+ (A38). The A rating in A37 is the Country Ceiling, not an issuer rating.
**Q29.** None. VD has only a Country Ceiling (A12).
**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling (A12, A14), and E15's FC rating of A equals CV's ceiling (A37, A41).
**Q31.** No. No company's FC rating is above its country's ceiling.
**Q32.** E09. The chain is E11 → E10 → E09.
**Q33.** The holder takes Halden Bank's (E10) risk, rated BBB+. I05 is guaranteed by E10, and E10's current rating is BBB+ (A27).
**Q34.** No. E12 has no parent and a different LEI, so it is not linked to E09 or E10.
**Q35.** 3: E09, E10 (with E17) and E11.
**Q36.** 2: E02 (with E03) and E04.
**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA data.
**Q38.** No. They have different LEIs and different parents.
**Q39.** A. E03 is the same entity as E02, and its latest action is A09.
**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in DE (the RATINGS record holds), and E07 is withdrawn.
**Q41.** None. E16 is a QA record and is ignored.
**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.
**Q43.** 0. The only LU record is E17, and its country is overridden by the RATINGS record E10 (DE).
**Q44.** Yes. I07 is in XVD, the domestic currency of VD.
**Q45.** No. I07 is local-currency debt (BBB-, A45), and the ceiling applies only to FC debt.
**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.
**Q47.** None. A47 is only an Expected rating (EX), so I08 stays unrated.
**Q48.** 7: I01 to I07.

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