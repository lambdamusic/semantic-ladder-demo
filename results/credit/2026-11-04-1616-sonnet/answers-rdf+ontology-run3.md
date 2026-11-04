**Q1.** A-. E01's latest foreign-currency long-term action on or before that date is A01 (assigned A-, 2024-03-12).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB with the outlook revised to Negative. The downgrade was A02 in 2025.

**Q3.** No. The 2031 note is I02, subordinated, and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E02 and E03 share the LEI NWND00HOLDINGS00GB42, so they are one entity. The latest action is A09 (E03, affirmed A, 2025-09-15, Positive).

**Q5.** The holder takes E02's (Northwind Holdings) credit risk, rated A. The notes are I03, guaranteed by E02, and A11 rates them A.

**Q6.** The Republic of Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings of entities domiciled there. E05's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13) and is not capped.

**Q7.** E08 and E10. The 2026 downgrades are A21 and A22 for E08 and A27 for E10. A29 is a downgrade of instrument I05, not an issuer.

**Q8.** E08. A22 puts it at RD (a default) from 2026-07-08, with no later action.

**Q9.** 12. These are E01, E02 (the same entity as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is excluded because it was withdrawn (A19), and VD has only a Country Ceiling.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (speculative, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action, A35, came after 2025-06-01.

**Q12.** A-. A34 assigned it on 2023-01-15, before the A36 downgrade.

**Q13.** 1. The only downgrade is A36.

**Q14.** No rating. E12's first action, A30, is dated 2024-02-01, after that date.

**Q15.** A-. A26 set it in 2023, and the downgrade A27 came on 2026-04-15, after that date.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+. A35 (Watch) and A33 (affirmation) did not change the rating.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative, which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) is its latest action. E14's Watch (A35) was followed by the A33 affirmation, which carries no Watch.

**Q19.** E01 and E09 (A03 and A25). E06's latest action, A17, carries no outlook, so I did not count it.

**Q20.** No. E07 was assigned BB and then withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. BBB is investment grade (A03).

**Q25.** 4. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-). I02 (BB+) and I04 (BB) are not.

**Q26.** A+ (A40, local-currency).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** The data gives none. VD has only a Country Ceiling of BB (A12), which is not the sovereign's issuer rating.

**Q30.** E05 and E15. E05's foreign-currency BB equals the VD ceiling of BB (A14, A12). E15's foreign-currency A equals the CV ceiling of A (A41, A37).

**Q31.** No. E05 and E15 are at their ceilings, not above them, and no other country has a ceiling in the data.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's (Halden Bank) credit risk, rated BBB+. I05 is guaranteed by E10, and A29 rates it BBB+.

**Q34.** No. The data links E12 to no parent or group. It shares only the name "Halden" and has no LEI link to E09, E10 or E11.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 (the same entity as E03) and its subsidiary E04.

**Q37.** 16. There are 17 entity records, but E02 and E03 share an LEI.

**Q38.** No. E06 (Orrin Bank AG, DE) and E13 (Orrin Bancorp Inc, US) have different LEIs.

**Q39.** A. The latest action is A09, an affirmation of A by E03, which is the same entity as E02.

**Q40.** 5: E01, E02 (E03), E09, E12 and E14. E07 is excluded because it was withdrawn.

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
"Q25": {"count": 4},
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
"Q40": {"count": 5}
}
```