**Q1.** A-. A01 set A- on 2024-03-12, and the next action on E01's FC LTIDR (A02) came on 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation, and the outlook moved to NEG.

**Q3.** No, BB+. I02 is subordinated, and its latest action, A07, downgraded it to BB+, which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and A09 (2025-09-15) is the latest action with outlook POS.

**Q5.** The holder takes the credit risk of E02, rated A. I03 is guaranteed by E02, and its latest instrument rating (A11) is A.

**Q6.** The VD Country Ceiling is BB (A12), which caps E05's FC rating (A14, BB). The LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27; A44 is on E16, a QA record, so it is ignored.

**Q8.** E08. A22 downgraded it to RD (restricted default) on 2026-07-08.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08 (RD), E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn, E11 has only a credit opinion, E04 and VD have no issuer rating, and E16 is QA.

**Q10.** Depends. The FC rating is BB (speculative) and the LC rating is BBB- (investment grade), per A14 and A13.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action came on 2025-11-20.

**Q12.** A-, from A34.

**Q13.** 1, which is A36. The watch (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.

**Q15.** A-. E17 shares E10's LEI, so it is the same entity. A26 set A-, and the downgrade A27 came later, on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). The watch in A35 was not a change.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch, which leaves the rating unchanged.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's watch from A35 was resolved by A33, which carries no watch.

**Q19.** E01 and E09, per A03 and A25. E06's A17 shows no outlook, so I did not count it.

**Q20.** No. A19 is a commercial withdrawal, which is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, because RD is a default (A22).

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an Expected rating (A47), so it is unrated.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The CV Country Ceiling of A (A37) is not its rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals the VD ceiling of BB, and E15's FC rating of A equals the CV ceiling of A.

**Q31.** No. E05 and E15 are exactly at their ceilings, and no GB, DE or US entity has a ceiling in the data.

**Q32.** E09. I05's issuer E11 has parent E10, and E10 has parent E09; the RATINGS records hold over E17.

**Q33.** The holder takes the credit risk of E10, rated BBB+. E10 guarantees I05 (the issuer is E11), and both E10's rating (A27) and I05's rating (A29) are BBB+.

**Q34.** No. E12 has no parent, so it is not linked to E09 or E10.

**Q35.** 3: E09, E10 and E11 (E17 duplicates E10).

**Q36.** 2: E02 and E04 (E03 duplicates E02).

**Q37.** 16. There are 19 records, minus 2 duplicates (E03, E17) and 1 QA record (E16).

**Q38.** No. They have different LEIs (E06 549300AMVE3VRVG7HK43, E13 815600O8X8K2F154N214).

**Q39.** A, from A09 (E03 is the same entity).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, and RATINGS says DE for that entity.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, the issuer's country.

**Q45.** No. I07 is local-currency debt, which the ceiling does not cap.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

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