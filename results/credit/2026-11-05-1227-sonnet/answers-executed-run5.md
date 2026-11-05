**Q1.** A-. E01's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. On 2026-02-10 E01 stayed at BBB and only its outlook moved to Negative (A03, action AF). The downgrade to BBB was in 2025 (A02).

**Q3.** No. The 2031 note (I02) is subordinated and rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's current rating is A with a POS outlook (A09).

**Q5.** E02 (Northwind Holdings), rated A. I03 is issued by E04 but guaranteed by E02, and credit_risk_of is E02. E02's LTIDR is A (A09), and I03 is also A (A11).

**Q6.** Valdoria's country ceiling is BB (ceilings.csv, from 2025-04-01). E05's FC rating is capped at BB (A14), while its LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and then RD (A22), and E10 to BBB+ (A27). E11 was not included because it has no issuer rating of its own.

**Q8.** E08. Its RD rating (A22) is in force.

**Q9.** 12. Current issuer ratings: CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15. E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. E05's LC rating is BBB- (investment grade, A13), but its FC rating is BB (not investment grade, A14).

**Q11.** BBB+. This is the rating in force from 2024-09-30 to 2025-11-20 (A36).

**Q12.** A-. This is the rating in force from 2023-01-15 to 2024-09-30 (A34).

**Q13.** 1. The only downgrade is A34 to A36 on 2024-09-30.

**Q14.** None. E12's first rating (A30) starts on 2024-02-01.

**Q15.** A-. This is E10's rating from 2023-05-01 to 2026-04-15 (A26).

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now. Only the watch status changed in between (A35, then A33).

**Q17.** No. In 2026 E06 stayed at A- and was placed on Rating Watch Negative (A17), which is not a downgrade.

**Q18.** E06 (A17). E14's RWN ended on 2026-05-01.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn (WD, A19), and no default rating appears in the data.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating in the data, only a ceiling.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's BB ceiling, and E15's FC rating of A equals CV's A ceiling.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11 sits under E10, which sits under E09 (ancestors.csv).

**Q33.** E10 (Halden Bank), rated BBB+. E10 guarantees I05 (credit_risk_of is E10), and its LTIDR is BBB+ (A27).

**Q34.** No. E12 has no parent and appears in no chain, whereas E10 belongs to the E09 group.

**Q35.** 3: E09, E10 and E11. E17 is merged into E10.

**Q36.** 2: E02 and E04. E03 is merged into E02.

**Q37.** 16. The 16 entities are CV, VD, E01, E02, E04 and E05 through E15.

**Q38.** No. E06 and E13 are separate entities with different LEIs and countries (DE and US), and neither is the other's parent.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** LU (E10).

**Q43.** 1. Only E10 is domiciled in LU.

**Q44.** Yes. I07 is in XVD with local_currency set to "yes".

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 is a local-currency note. Its rating of BBB- (A45) matches E05's LC rating (A13).

**Q46.** No. E11 has no rating of its own. I05 is rated, but that rating reflects the guarantor E10.

**Q47.** None. I08 has no rating record.

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
"Q42": {"country": "LU"},
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```