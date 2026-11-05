**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action on E01's FC LTIDR (A02) came in June 2025.

**Q2.** No. E01's only 2026 action on its long-term rating is A03, an affirmation at BBB with a Negative outlook, which is not a downgrade.

**Q3.** No. I02 is rated BB+ after A07 (DG), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with a POS outlook.

**Q5.** E02, rated A. I03 is guaranteed by E02, so the holder takes the parent's risk, and E02/E03 (A08, A09) is rated A.

**Q6.** Not in the JSON. VD's Country Ceiling is BB (A12) and caps foreign-currency ratings, so E05's FC rating is BB (A14). Its LC rating is BBB- (A13) and is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument action, and A44 is on QA record E16, which is ignored.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), VD has only a ceiling, E11 has only a credit opinion, and E16 is QA.

**Q10.** Depends. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (speculative, A14).

**Q11.** BBB+, set by A36 (DG, 2024-09-30).

**Q12.** A-, set by A34.

**Q13.** 1. A36 is the only DG on E14.

**Q14.** None. E12's first action (A30) is on 2024-02-01.

**Q15.** A-. A26 applies to E10, which is the same entity as E17, and the downgrade A27 only came in April 2026.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33 affirmed it). A35 was only a Watch.

**Q17.** No. A17 is a Rating Watch placement, and the rating stays at A-.

**Q18.** Only E06 (A17). E14's Watch (A35) was cleared by the later affirmation A33.

**Q19.** E01 (A03) and E09 (A25). E06's latest action (A17) shows no outlook, so I have not counted it.

**Q20.** No. E07's rating was withdrawn (A19), which is not a default, and it has no default rating.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's FC LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (FC BB, VD ceiling BB) and E15 (FC A, CV ceiling A).

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating was cut to BBB+ in A27.

**Q34.** No. E12 has no parent, so it is not in E09's group.

**Q35.** 3. These are E09, E10 (the same entity as E17) and E11.

**Q36.** 2. These are E02 (the same entity as E03) and E04.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates by LEI, and E16 is QA test data.

**Q38.** No. They have different LEIs and different countries.

**Q39.** A (A09, via E03).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in LU.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. RESEARCH's record (E17) holds for domicile, and it shares E10's LEI.

**Q43.** 1. Only Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is based.

**Q45.** No. The ceiling does not apply to local-currency debt.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX).

**Q48.** 7. These are I01 to I07, and I08 is unrated.

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