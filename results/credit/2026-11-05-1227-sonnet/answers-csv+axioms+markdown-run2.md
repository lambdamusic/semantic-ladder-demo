**Q1.** A-. A01 assigned A- on 2024-03-12, and the next Kestrel action (A02) is not until 2025-06-20.

**Q2.** No. The only 2026 Kestrel actions are affirmations (A03, A04), and the outlook moving to negative is not a downgrade.

**Q3.** No, it is BB+. I02 was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) gave outlook POS.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and the latest action on that entity (A09, recorded on E03) affirmed A.

**Q6.** The Country Ceiling for VD is BB (A12), which caps foreign-currency ratings. E05's FC rating is therefore BB (A14), while its LC rating is BBB- (A13) because local currency is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. The other 2026 downgrades are on an instrument (A29) and on a QA record (A44), so they don't count.

**Q8.** E08. It went to RD on 2026-07-08 (A22), and RD is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 is withdrawn, E04 and E11 have no issuer rating, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. The FC rating is BB (speculative) and the LC rating is BBB- (investment grade), so it turns on the currency basis.

**Q11.** BBB+. The downgrade A36 (2024-09-30) set BBB+, and the later actions only placed it on Watch or affirmed it.

**Q12.** A-, set by A34 (2023-01-15).

**Q13.** 1, the downgrade A36.

**Q14.** None. The first Halden Foods rating (A30) was assigned on 2024-02-01.

**Q15.** A-. A26 set A- in 2023 for E10, and the downgrade A27 was not until 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+; A35 and A33 did not change it.

**Q17.** No. A17 only placed E06 on Rating Watch Negative, with the rating unchanged at A-.

**Q18.** E06. A17 (2026-09-03) is its latest action. The E14 watch from A35 was superseded by A33, which carries no watch.

**Q19.** E01 and E09, from A03 and A25 (both NEG). E06's latest action A17 carries no outlook, so I have not counted it.

**Q20.** No. E07 was withdrawn (A19) and has never been rated RD or D.

**Q21.** E07, whose rating was withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 only has an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD only has a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's FC rating is A, equal to the CV ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings and no company is above one.

**Q32.** E09. E11's parent is E10, whose RATINGS record names E09 as its parent.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose latest action A27 set BBB+.

**Q34.** No. E12 has no parent, while E10 belongs to E09's group.

**Q35.** 3: E09, E10 (with E17) and E11.

**Q36.** 2: E02 (with E03) and E04.

**Q37.** 16. There are 19 records, less 2 duplicates by LEI (E03 and E17) and 1 QA record (E16).

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A09, recorded on E03, the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** LU. The RESEARCH record E17 holds for country and overrides the DE on E10.

**Q43.** 1, E10 (with E17).

**Q44.** Yes. I07 pays in XVD, which is the domestic currency of VD, E05's country.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it, and it is rated BBB- (A45).

**Q46.** No. E11 only has a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 only has an expected rating (A47, EX), so it is unrated until an assignment.

**Q48.** 7, I01 to I07. I08 has no rating.

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