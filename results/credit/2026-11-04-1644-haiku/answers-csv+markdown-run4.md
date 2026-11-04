**Q1.** A-. E01's LTIDR (FC) was A- from A01 (2024-03-12) until downgraded to BBB on 2025-06-20 (A02), so the 1 Jan 2025 rating is A-.

**Q2.** No. E01's only 2026 actions are the affirmation at BBB (A03) and the short-term affirmation at F2 (A04).

**Q3.** No. I02 (subordinated 2031 note) was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E02 and E03 share LEI NWND00HOLDINGS00GB42, and the latest outlook is POS from A09 (2025-09-15).

**Q5.** Northwind Holdings (E02). I03 is guaranteed by E02, so it is rated on the guarantor and is rated A (A11).

**Q6.** Valdoria's FC rating (BB, E05, A14) is held down to the Country Ceiling of BB (VD, A12). The LC rating (BBB-, A13) is not capped because the ceiling reflects transfer and convertibility risk, which applies only to foreign-currency obligations. (Q6 is not in the JSON list.)

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. (I05's downgrade in A29 is an instrument action, so it is excluded.)

**Q8.** E08. Saxby Shipping was rated RD from A22 (2026-07-08), after a completed distressed debt exchange.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 has been withdrawn (A19), E11 has only a credit opinion (A46), VD has only a Country Ceiling, and E16 is QA data.

**Q10.** Depends. The FC rating is BB (A14), which is speculative grade, but the LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. E14's latest action on or before 2025-06-01 is the downgrade to BBB+ on 2024-09-30 (A36).

**Q12.** A-. E14's first assignment (A34, 2023-01-15) gave A-, and no action preceded 1 Jan 2024.

**Q13.** 1. The only downgrade is A36.

**Q14.** None. E12 was first assigned BB- on 2024-02-01 (A30), after 1 Jan 2024.

**Q15.** A-. E10's rating was A- from A26 (2023-05-01) until the downgrade to BBB+ on 2026-04-15 (A27), which is after 1 Jan 2026.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33). The 2025-11-20 Rating Watch (A35) is not a rating change, and A33 cleared the watch.

**Q17.** No. The only 2026 action on E06 is a Rating Watch Negative (A17), which is not a downgrade.

**Q18.** E06. Orrin Bank AG was placed on Rating Watch Negative on 2026-09-03 (A17). E14's watch from A35 was cleared by the affirmation in A33.

**Q19.** E01 and E09. Both have NEG outlooks from A03 and A25, and no later action changed them.

**Q20.** No. Pellam Retail (E07) was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19). E11 and VD never had an issuer rating.

**Q22.** E08. It is the only entity rated RD or D.

**Q23.** F2. This is E01's short-term rating from A04.

**Q24.** Yes. Kestrel's issuer rating is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only an expected rating (EX, A47), so it is not rated.

**Q26.** A+. This is E15's LC rating from A40.

**Q27.** A-. I06 was assigned A- (A42).

**Q28.** BBB+. This is CV's FC issuer rating from A38.

**Q29.** None. VD has only a Country Ceiling (A12), and a ceiling is not the sovereign's issuer rating.

**Q30.** E05 and E15. Valdoria Telecom's FC rating (BB) equals the VD ceiling (BB), and Corvenia Power's FC rating (A, A41) equals the CV ceiling (A, A37).

**Q31.** No. The only companies with ceilings are E05 and E15, and both sit exactly at their ceilings.

**Q32.** E09. Halden Leasing (E11) is owned by Halden Bank AG (E10), which is owned by Halden Group plc (E09).

**Q33.** E10 (Halden Bank AG). I05 is guaranteed by E10, so it is rated on the guarantor and is BBB+ (A29).

**Q34.** No. Halden Foods (E12) has no parent and no link to E09 or E10.

**Q35.** 3. These are E09, E10 and E11.

**Q36.** 2. These are E02 (which includes the E03 record) and E04.

**Q37.** 16. After dropping the QA record E16, the distinct entities are E01, E02, E04–E15 and the sovereigns VD and CV. If sovereigns are excluded, the count is 14.

**Q38.** No. Their LEIs differ (ORRN00BANK00000DE233 and ORBC00BANCORP000US45).

**Q39.** A. This is E02's rating from A09.

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 has no rating, and E16 is QA data.

**Q41.** None. E16 is QA data and must be ignored.

**Q42.** DE. RATINGS (E10) is the system of record, and its country is DE. The RESEARCH record E17 says LU, but RATINGS takes precedence.

**Q43.** 0. The only LU record is E17, which is the RESEARCH record for E10. RATINGS places E10 in DE.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, and the ceiling caps only foreign-currency ratings. The BBB- rating is numerically above BB, but the ceiling does not apply to it.

**Q46.** No. E11 has only a credit opinion (CO, A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (EX, A47), which is not yet a rating.

**Q48.** 7. The rated instruments are I01–I07. I08 is unrated.

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