**Q1.** A-. E01's long-term foreign-currency rating was set at A- by A01 (2024-03-12) and stayed until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03/A04, an affirmation, and an affirmation or negative outlook is not a downgrade.

**Q3.** No. The 2031 note (I02) was assigned BBB (A23) and downgraded to BB+ by A07 (2025-06-20), which is speculative grade.

**Q4.** Positive. E03 has the same LEI as E02, so they are one entity, and its latest action (A09, 2025-09-15) carries a POS outlook.

**Q5.** E02, rated A. I03 is guaranteed by E02 (the issuer E04 is a finance subsidiary), and A10/A11 rate the note A.

**Q6.** E05's foreign-currency rating (A14) is BB and its local-currency rating (A13) is BBB-. The data doesn't state a reason, but BB equals the Valdoria Country Ceiling (A12), which caps foreign-currency ratings and not local-currency ones.

**Q7.** E08 and E10. E08 was downgraded by A21 and A22, and E10 by A27. A44 is on E16, a QA record, so I ignored it. A29 is an instrument rating, not an issuer.

**Q8.** E08. A22 gave it RD (a default) on 2026-07-08, and nothing later changes that.

**Q9.** 12. These are E01, E02 (=E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn (A19), E11 has only a credit opinion, VD has only a ceiling, and E16 is QA.

**Q10.** Depends. Its foreign-currency rating is BB (speculative grade, A14), while its local-currency rating is BBB- (investment grade, A13).

**Q11.** BBB+. E14 was downgraded to BBB+ by A36 (2024-09-30), and the Watch (A35) came later in 2025-11.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade came later.

**Q13.** 1, from A36. The Watch (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 held A- (A26) until the downgrade on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).

**Q17.** No. E06's only 2026 action is a Rating Watch (A17), which leaves the rating unchanged. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's earlier Watch (A35) was superseded by A33.

**Q19.** E01 and E09. A03 and A25 give them NEG outlooks, and nothing later changes those.

**Q20.** No. E07 was withdrawn (A19), which is not a credit event.

**Q21.** E07. It was rated BB (A18) and then withdrawn (A19).

**Q22.** E08, from the RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's current rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is unrated.

**Q26.** A+. This is E15's local-currency rating (A40).

**Q27.** A- (A42).

**Q28.** BBB+. CV's foreign-currency issuer rating is A38. A37 is the Country Ceiling, not a rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05 has foreign-currency BB, equal to the VD ceiling of BB. E15 has foreign-currency A, equal to the CV ceiling of A (A37).

**Q31.** No. Both capped entities sit exactly at their ceiling, not above it.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and A29 rates the note BBB+.

**Q34.** No. E12 has no parent link and no shared LEI with the Halden Bank/Group records.

**Q35.** 3: E09, E10 and E11. E17 shares E10's LEI, so it is the same entity.

**Q36.** 2: E02 (=E03) and E04.

**Q37.** 16. There are 19 records, of which E17=E10 and E03=E02 are duplicates, and E16 is QA. That leaves 16, counting the two sovereigns.

**Q38.** No. Their LEIs differ (E06 vs E13).

**Q39.** A, from A09 (E03 and E02 are the same entity).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record and must be ignored.

**Q42.** DE. The RATINGS record (E10) holds, and E17's "LU" disagrees with it.

**Q43.** 0. The only LU record, E17, is the same entity as E10, which is domiciled in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is BBB- (A45), but local-currency debt isn't capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, so I08 stays unrated.

**Q48.** 7: I01 through I07.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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