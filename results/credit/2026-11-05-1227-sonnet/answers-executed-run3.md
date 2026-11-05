**Q1.** A-. Kestrel's LTIDR FC was A- from 2024-03-12 to 2025-06-20 (A01).

**Q2.** No. The only downgrade was on 2025-06-20 (A02); the 2026-02-10 action (A03) was an affirmation with the outlook moved to Negative.

**Q3.** No. The 2031 note (I02) has been rated BB+ since 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive (A09).

**Q5.** The holder takes the risk of Northwind Holdings (E02), via the guarantee on I03. E02 is rated A, and I03 is also A (A09, A11).

**Q6.** The data does not state a reason. Valdoria's country ceiling is BB (ceilings.csv), and E05's FC rating of BB (A14) sits exactly at it, while the LC rating of BBB- (A13) is higher. This is consistent with the ceiling capping FC only, but the data does not say so.

**Q7.** Saxby Shipping (E08) and Halden Bank (E10). E08 was downgraded on 2026-01-20 and 2026-07-08 (A21, A22), and E10 on 2026-04-15 (A27).

**Q8.** Saxby Shipping (E08), rated RD since 2026-07-08 (A22).

**Q9.** 12. These are CV, E01, E02, E05, E06, E08, E09, E10, E12, E13, E14 and E15; E07 is excluded because its rating was withdrawn (A19).

**Q10.** Depends. The FC rating is BB, which is not investment grade (A14). The LC rating is BBB-, which is investment grade (A13).

**Q11.** BBB+ (A36).

**Q12.** A- (A34).

**Q13.** 1. The only downgrade was A- to BBB+ on 2024-09-30 (A36); A35 was a watch action and A33 an affirmation.

**Q14.** None. The first rating, A30, starts on 2024-02-01.

**Q15.** A- (A26).

**Q16.** No. The rating stayed at BBB+ (A36, A35, A33). Only the watch and outlook changed.

**Q17.** No. The 2026-09-03 action (A17) placed it on Rating Watch Negative and left the rating at A-.

**Q18.** Orrin Bank (E06), on RWN since A17.

**Q19.** Kestrel Energy (E01, A03) and Halden Group (E09, A25).

**Q20.** No. The rating was withdrawn (WD, A19), which is not a default rating.

**Q21.** Pellam Retail (E07), whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** Saxby Shipping (E08, A22).

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. No rating exists for VD.

**Q30.** Valdoria Telecom (E05) and Corvenia Power (E15). E05's FC rating is BB against a BB ceiling, and E15's is A against an A ceiling.

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** Halden Group plc (E09).

**Q33.** The holder takes the risk of Halden Bank (E10), via the guarantee on I05. E10 is rated BBB+ (A27).

**Q34.** No. Halden Foods (E12) has no parent and is not linked to E09.

**Q35.** 3 (E09, E10, E11).

**Q36.** 2 (E02, E04).

**Q37.** 16. That is 14 corporate entities plus the two sovereigns, after the duplicate records were merged.

**Q38.** No. They are separate entities, E06 and E13, with different LEIs and countries.

**Q39.** A (A09).

**Q40.** 5 (E01, E02, E09, E12, E14).

**Q41.** None. Brindle Capital is not in the data.

**Q42.** Luxembourg (LU), per E10.

**Q43.** 1 (E10).

**Q44.** Yes. I07 has local_currency=yes and is denominated in XVD.

**Q45.** No. I07 is BBB- (A45), but it is a local-currency obligation, and the data's ceiling is not shown to cap local-currency instruments.

**Q46.** No. E11 has no issuer rating of its own; I05 is rated through its guarantor.

**Q47.** None. I08 has no rating.

**Q48.** 7 (I01 to I07).

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