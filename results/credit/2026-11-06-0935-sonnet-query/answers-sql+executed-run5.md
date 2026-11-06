**Q1.** A-. E01's foreign-currency issuer rating on 2025-01-01 was A- (A01, valid 2024-03-12 to 2025-06-20).

**Q2.** No. E01's only 2026 action was an affirmation with the outlook moved to Negative (A03, 2026-02-10); the downgrade to BBB was in 2025 (A02).

**Q3.** No. The 2031 note I02 is rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02's current rating action is A09, with outlook POS.

**Q5.** E02 (Northwind Holdings), the guarantor of I03. I03 is rated A (A11).

**Q6.** Valdoria's Country Ceiling is BB (VD, from 2025-04-01), and E05's foreign-currency rating is BB (A14). Its local-currency rating is BBB- (A13). That ceiling is the likely cause, but the data doesn't state the reason explicitly.

**Q7.** E08 and E10. E08 was downgraded in 2026 (A21, A22) and E10 on 2026-04-15 (A27). E06's Rating Watch Negative (RWN) is not a downgrade.

**Q8.** E08. Its rating is RD from 2026-07-08 (A22), still in force.

**Q9.** 12. Current non-withdrawn issuer ratings are held by CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07's was withdrawn (A19).

**Q10.** Depends. E05 is BB in foreign currency (A14, sub-investment grade) but BBB- in local currency (A13, investment grade).

**Q11.** BBB+. E14 on 2025-06-01 was BBB+ (A36, from 2024-09-30).

**Q12.** A-. E14 on 2024-01-01 was A- (A34).

**Q13.** 1. The only downgrade is A36 (2024-09-30).

**Q14.** None. E12's first rating (A30) starts on 2024-02-01.

**Q15.** A-. E10 (which merges E17) was A- on 2026-01-01 (A26).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), though it passed through a watch period (A35).

**Q17.** No. E06 stayed at A- and was placed on Rating Watch Negative (A17), which is not a downgrade.

**Q18.** E06 (A17).

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's rating was withdrawn (A19), not moved to a default grade, so there is no default record.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (I06, A42).

**Q28.** BBB+ (CV, A38).

**Q29.** None. VD has no rating rows.

**Q30.** E05 and E15. E05 is BB against VD's BB ceiling, and E15 is A against CV's A ceiling.

**Q31.** No. E05 and E15 are exactly at their ceilings, not above.

**Q32.** E09.

**Q33.** E10, the guarantor of I05. I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent, while E10's ultimate parent is E09.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04.

**Q37.** 16. The entities table has 16 rows after duplicates were merged.

**Q38.** No. E06 and E13 are separate entities with different LEIs and countries (DE and US).

**Q39.** A (A09).

**Q40.** 5. The GB issuers with a current issuer rating are E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

**Q41.** None. Brindle Capital is not in the data.

**Q42.** LU.

**Q43.** 1: E10.

**Q44.** Yes. I07 has local_currency = yes and is denominated in XVD.

**Q45.** No. The ceiling caps foreign-currency ratings, and I07 is a local-currency obligation rated BBB- (A45). I'm assuming the ceiling applies only to foreign currency, which the data doesn't state.

**Q46.** No. Only its instrument I05 is rated; E11 has no issuer rating rows.

**Q47.** None. I08 has no rating.

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