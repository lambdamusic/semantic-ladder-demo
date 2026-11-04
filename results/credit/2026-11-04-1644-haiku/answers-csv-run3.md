**Q1.** A-. A01 (A-) applied until A02 downgraded Kestrel to BBB on 2025-06-20.

**Q2.** No. A03 and A04 (both 2026-02-10) are affirmations, not downgrades.

**Q3.** No, BB+. The 2031 note's latest action is A07 (downgrade to BB+) on I02, which replaced A23 (BBB).

**Q4.** Positive. A09 (2025-09-15, outlook POS) is the latest action on Northwind Holdings, recorded as E03, which shares E02's LEI. E02's own RATINGS record (A08) shows Stable, so the two systems disagree.

**Q5.** Northwind Holdings (E02), via its guarantee of I03; the issuer is E04. The rating is A (A11). I03's guarantor is E02, so the holder bears E02's risk.

**Q6.** The data gives no reason. Valdoria's FC issuer rating is BB (A14) and its LC rating is BBB- (A13); the Republic of Valdoria's country ceiling is also BB (A12), which is consistent with a ceiling cap, but the data does not say so.

**Q7.** E08, E10, E16. These have downgrade actions in 2026: A21/A22, A27, and A44. I05's downgrade (A29) reflects its guarantor E10, not a downgrade of issuer E11.

**Q8.** E08. A22 (2026-07-08) set RD, and no later action lifts it.

**Q9.** 13. Counting LEI-distinct issuers with an active LTIDR on 2026-10-01: E01, E02/E03, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16, and CV. E07 is withdrawn, E04 and E11 have no LTIDR, and E17 shares E10's LEI.

**Q10.** Depends. The FC issuer rating is BB (A14), not investment grade, but the LC rating is BBB- (A13), which is.

**Q11.** BBB+. A36 (2024-09-30, DG to BBB+) was in effect on 2025-06-01.

**Q12.** A-. A34 (2023-01-15) was the rating in effect on 2024-01-01.

**Q13.** 1. A36 is the only downgrade; A35 is a Rating Watch Negative, not a downgrade.

**Q14.** None. Halden Foods' first rating, A30 (BB-), is dated 2024-02-01, after 2024-01-01.

**Q15.** A-. A26 (A-) was in effect until A27 downgraded E10 on 2026-04-15.

**Q16.** No. The rating stayed BBB+ across A36, A35 and A33; only the watch status changed (A35 RWN).

**Q17.** No. A17 (2026-09-03) placed Orrin Bank on Rating Watch Negative at A-; it was not downgraded.

**Q18.** E06. A17 has RWN with no later resolution. E14's RWN from A35 (2025-11-20) appears superseded by A33 (2026-05-01, watch blank), but the data does not state that a watch was cleared.

**Q19.** E01 and E09. A03 and A25 are the latest NEG outlooks for these issuers.

**Q20.** No. E07 was withdrawn (A19, WD), not defaulted.

**Q21.** E07. A19 (2026-05-12) withdrew its rating, and it has no later rating. E11 held a CO rating, not an issuer rating.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. A04 (2026-02-10) is the current short-term rating.

**Q24.** Yes. The issuer rating is BBB (A03), which is investment grade.

**Q25.** 6. I01, I03, I05, I06, I07 and I08 are investment grade. I08's action code EX (A47) is undefined in the data, so its status is uncertain.

**Q26.** A+. A40 is the current local-currency rating.

**Q27.** A-. A42 is the rating on I06.

**Q28.** BBB+. A38 is the current foreign-currency issuer rating.

**Q29.** None. The Republic of Valdoria has only a country ceiling (CC, A12, BB) and no LTIDR.

**Q30.** E05 and E15. Each has a foreign-currency issuer rating equal to its country's ceiling (E05 BB vs. A12 BB; E15 A vs. A37 A). Ceilings exist in the data only for VD and CV.

**Q31.** No. Neither E05 (BB) nor E15 (A) is above its ceiling. The data has no ceilings for other countries, so those cannot be checked.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank AG (E10), as guarantor of I05. The rating is BBB+ (A29).

**Q34.** No. E12 has no parent_id and a different LEI from E10 or E09; the shared name is the only link.

**Q35.** 3. E09, E10 and E11. E17 has the same LEI as E10.

**Q36.** 2. E02 and E04. E03 has the same LEI as E02.

**Q37.** 17. There are 19 records (E01–E17 plus VD and CV), minus two duplicate LEIs (E03 duplicates E02, E17 duplicates E10).

**Q38.** No. They have different LEIs and countries (DE vs. US).

**Q39.** A. A08 is the rating for E02; A09 (for E03, same LEI) affirms A.

**Q40.** 6. E01, E02, E09, E12, E14 and E16 are GB issuers with an active LTIDR (E03 is counted with E02, and E07 is withdrawn).

**Q41.** BB+. A44 (2026-06-01) downgraded Brindle Capital to BB+.

**Q42.** DE. E10 records Germany; E17 (same LEI) says LU. The conflict is not resolved by the data, so I use the RATINGS record.

**Q43.** 0. E17 is domiciled in LU, but it duplicates E10's LEI, which is DE.

**Q44.** Yes. I07's currency is XVD, which appears to be Valdoria's local currency, but the data does not define it.

**Q45.** Yes, numerically: BBB- (A45) is above the BB ceiling (A12). A ceiling normally caps FC ratings, and I07 is an XVD note, so the comparison may not be meaningful.

**Q46.** No. Halden Leasing has only a CO rating (A46), not an LTIDR.

**Q47.** A. A47 (2026-09-01) rates I08 at A, but the action code EX is undefined in the data.

**Q48.** 8. Every instrument (I01–I08) has a rating record dated on or before 2026-10-01; I08's status is uncertain because of the EX code.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E16"]},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": 13},
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
  "Q25": {"count": 6},
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
  "Q37": {"count": 17},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 6},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 0},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "yes"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```