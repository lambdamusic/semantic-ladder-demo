**Q1.** A-. Kestrel Energy's FC rating A- (A01) was valid from 2024-03-12 to 2025-06-20, which covers 1 January 2025.

**Q2.** No. The only 2026 action (A03, 2026-02-10) kept the rating at BBB and changed the outlook to NEG; the downgrade to BBB was in 2025 (A02).

**Q3.** No, rated BB+. The 2031 note (I02) currently carries BB+ (A07, from 2025-06-20), which is sub-investment grade.

**Q4.** Positive. Northwind Holdings' rating A (A09) has outlook POS and no end date.

**Q5.** Northwind Holdings (E02), rated A. The 2030 notes (I03) list E02 as credit_risk_of, and E02's current rating is A (A09).

**Q6.** The data does not state a reason. Valdoria Telecom's FC rating is BB (A14) and its LC rating is BBB- (A13); the Valdoria ceiling of BB (ceilings.csv) matches the FC rating, which is consistent with a cap but does not confirm one.

**Q7.** Halden Bank (E10) and Saxby Shipping (E08). E08 was downgraded to CCC (A21) and then RD (A22), and E10 was downgraded to BBB+ (A27). E07's move to WD (A19) is not coded as a downgrade, so I excluded it.

**Q8.** Saxby Shipping (E08). It is the only entity with an RD rating in force on 1 October 2026 (A22).

**Q9.** 12. The 13 entities with a current LTIDR record include E07, whose current record is WD (withdrawn), so I excluded it; including it would give 13.

**Q10.** Depends on currency basis. The FC issuer rating is BB (A14), which is sub-investment grade, while the LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. Marlow Utilities' BBB+ (A36) was valid from 2024-09-30 to 2025-11-20, which covers 1 June 2025.

**Q12.** A-. Marlow Utilities' A- (A34) was valid from 2023-01-15 to 2024-09-30, which covers 1 January 2024.

**Q13.** 1. Only the 2024-09-30 action (A36) is a downgrade; the later RW (A35) and AF (A33) actions did not change the rating.

**Q14.** None. Halden Foods (E12) has no rating before 2024-02-01 (A30), so there is no rating on 1 January 2024.

**Q15.** A-. Halden Bank's A- (A26) was valid from 2023-05-01 to 2026-04-15, which covers 1 January 2026.

**Q16.** No. Marlow Utilities has held BBB+ since 2024-09-30 (A36); the 2025-11-20 and 2026-05-01 actions changed watch and outlook only.

**Q17.** No. Orrin Bank's A- (A16) was followed only by a Rating Watch Negative (A17), not a downgrade.

**Q18.** Orrin Bank (E06). Its RWN (A17) is current, and Marlow's RWN (A35) ended on 2026-05-01.

**Q19.** Kestrel Energy (E01) and Halden Group (E09). Both have a current NEG outlook (A03, A25).

**Q20.** No. Pellam Retail (E07) is withdrawn (WD, A19), not in default (RD).

**Q21.** Pellam Retail (E07). It held BB (A18) until 2026-05-12, and its current record is WD (A19), so it has no active rating.

**Q22.** Saxby Shipping (E08). It is the only entity ever rated RD (A22).

**Q23.** F2. Kestrel Energy's short-term rating is F2 (A04), in force from 2026-02-10.

**Q24.** Yes. Kestrel Energy's current LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. The current instrument ratings that are investment grade are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-); I02 and I04 are sub-investment grade and I08 has no rating.

**Q26.** A+. Corvenia Power's local-currency rating is A+ (A40).

**Q27.** A-. The 2032 notes (I06) are rated A- (A42).

**Q28.** BBB+. The Republic of Corvenia's FC rating is BBB+ (CV, FC record).

**Q29.** None. Valdoria has no rating record in ratings.csv.

**Q30.** Telecom (E05) and Corvenia Power (E15). Both have current FC ratings equal to their country's ceiling: E05 BB against Valdoria's BB, and E15 A against Corvenia's A.

**Q31.** No. The only entities with FC ratings under a ceiling are E05 (BB, at ceiling) and E15 (A, at ceiling).

**Q32.** Halden Group plc (E09). Halden Leasing's ultimate_parent_id is E09 (ancestors show E09 two levels up).

**Q33.** Halden Bank (E10), rated BBB+. The 2028 notes (I05) list E10 as credit_risk_of, and E10's current rating is BBB+ (A27).

**Q34.** No. Halden Foods (E12) has no parent or ultimate parent, while Halden Bank's ultimate parent is E09.

**Q35.** 3. The Halden group is E09, E10 and E11; E12 has no parent link, and E17 is merged into E10.

**Q36.** 2. The Northwind group is E02 and E04; E03 is merged into E02.

**Q37.** 16. The entities file lists 16 records, including the two sovereigns CV and VD; excluding them leaves 14 non-sovereign entities.

**Q38.** No. Orrin Bank AG (E06, DE, LEI 549300…) and Orrin Bancorp Inc (E13, US, LEI 815600…) have different LEIs and countries and no parent link.

**Q39.** A. Northwind Holdings' current rating is A (A09).

**Q40.** 5. The GB issuers with a current rating are E01, E02, E09, E12 and E14; E07 is excluded because its current record is WD.

**Q41.** None. Brindle Capital does not appear in the data.

**Q42.** Luxembourg (LU), per entities.csv (E10).

**Q43.** 1. Only Halden Bank (E10) is domiciled in LU.

**Q44.** Yes. The 2027 note (I07) has local_currency = yes, with currency XVD.

**Q45.** Yes. The 2027 note is rated BBB- (A45), above the Valdoria ceiling of BB. The data does not say whether ceilings apply only to foreign-currency ratings, so this rests on the numbers alone.

**Q46.** No. Halden Leasing (E11) has no LTIDR or STIDR record.

**Q47.** None. The 2034 notes (I08) have no rating record.

**Q48.** 7. Instruments I01 through I07 have current ratings; I08 has none.

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
  "Q45": {"above_ceiling": "yes"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```