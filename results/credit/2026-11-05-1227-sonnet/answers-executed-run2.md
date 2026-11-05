**Q1.** A-. E01's LTIDR was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. The only downgrade was on 2025-06-20 (A02); the 2026-02-10 action was an affirmation with the outlook moved to Negative (A03).

**Q3.** No. The 2031 note (I02, subordinated) has been rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E02 has been on a POS outlook since 2025-09-15 (A09).

**Q5.** The holder takes E02 (Northwind Holdings) risk, as guarantor, via I03 (credit_risk_of = E02). I03 is rated A (A11), the same as E02's A (A09).

**Q6.** The data doesn't state a reason. The likely cause is the VD Country Ceiling of BB, which equals E05's foreign-currency rating of BB (A14), while the local-currency rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded on 2026-01-20 (A21) and 2026-07-08 (A22), and E10 on 2026-04-15 (A27).

**Q8.** E08. Its rating was RD, in force since 2026-07-08 (A22).

**Q9.** 12. Issuers with an issuer rating in force on 2026-10-01 are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15. E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. E05 is BB in foreign currency (A14), which is below investment grade, and BBB- in local currency (A13), which is investment grade.

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was on 2024-09-30 (A36).

**Q14.** None. E12's first rating began on 2024-02-01 (A30).

**Q15.** A- (A26, valid until 2026-04-15).

**Q16.** No. The rating level was BBB+ on 2025-01-01 and is still BBB+. Only a watch period (A35) and the outlook changed in between, and the rating was affirmed on 2026-05-01 (A33).

**Q17.** No. E06 was placed on Rating Watch Negative on 2026-09-03 at A- (A17), which is not a downgrade.

**Q18.** E06 (A17). E14's watch ended on 2026-05-01.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which was rated RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has no rating record, only a ceiling.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals the VD ceiling of BB, and E15's A equals the CV ceiling of A.

**Q31.** No. No company's foreign-currency rating exceeds its country's ceiling.

**Q32.** E09. It appears as E11's ultimate_parent_id and as its level-2 ancestor.

**Q33.** The holder takes E10 (Halden Bank), the guarantor, via I05 (credit_risk_of = E10). I05 is rated BBB+ (A29), the same as E10's BBB+ (A27).

**Q34.** No. E12 has no parent and is not in the ancestor chain of E09, E10 or E11.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 16. There are 16 entity rows, and the duplicate records are already merged (E03 into E02, E17 into E10).

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) are separate entities with different LEIs and countries, and neither lists the other in record_ids.

**Q39.** A (A09).

**Q40.** 5. The GB issuers with an issuer rating in force are E01, E02, E09, E12 and E14. E07 is excluded because its rating was withdrawn.

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** LU (E10).

**Q43.** 1. Only E10 is in LU; E17 is merged into it.

**Q44.** Yes. I07 has local_currency = yes and is denominated in XVD.

**Q45.** No. I07 is rated BBB- (A45), which is above the BB ceiling. But the ceiling constrains foreign-currency ratings, and I07 is a local-currency obligation.

**Q46.** No. E11 has no rating record of its own; I05 is rated on E10's credit risk.

**Q47.** None. I08 has no rating record.

**Q48.** 7. I01 to I07 have ratings in force and I08 has none.

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