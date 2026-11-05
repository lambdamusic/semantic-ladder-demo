**Q1.** A-. Only A01 (A-, 2024-03-12) applies on 1 Jan 2025; the next action, A02 (BBB), is dated 2025-06-20.

**Q2.** No. 2026 actions on E01 are affirmations (A03 BBB, A04 F2 short-term), with no downgrade.

**Q3.** No, BB+. I02's latest action is A07 (DG to BB+, 2025-06-20), which supersedes A23 (BBB).

**Q4.** Positive (POS). The latest outlook on E02/E03's LTIDR is set by A09 (2025-09-15).

**Q5.** E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so its credit risk is the guarantor's, and A11 (2025-09-15) sets the instrument rating at A.

**Q6.** The FC rating (BB, A14) sits at Valdoria's Country Ceiling (BB, A12, same date), which caps foreign-currency ratings, while the LC rating (BBB-, A13) is not capped. The data does not state a reason explicitly, so this is inferred from the ceiling definition. No JSON field is defined for Q6, so it is omitted below.

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and RD (A22); E10 was downgraded to BBB+ (A27). I05 is an instrument, and E16 is a QA record, so both are excluded.

**Q8.** E08. Its latest action, A22 (RD, 2026-07-08), is a default.

**Q9.** 12. The count covers E01, E02 (E03 is the same LEI), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV, each with a current LTIDR or STIDR rating. E07 was withdrawn, E11 holds only a credit opinion (CO), and E04 has no rating.

**Q10.** No. Its headline FC rating is BB (A14), though its LC rating of BBB- (A13) is investment grade.

**Q11.** BBB+. A36 (DG to BBB+, 2024-09-30) is the latest FC action on or before 2025-06-01.

**Q12.** A-. A34 (2023-01-15) is the latest action on or before 2024-01-01.

**Q13.** 1. A36 is the only DG action on E14.

**Q14.** None. E12's first rating, A30, is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. E10 (same LEI as E17) was rated A- by A26 until A27 (2026-04-15).

**Q16.** No. The rating has been BBB+ since A36; A35 (watch) and A33 (affirmation) left it unchanged.

**Q17.** No. E06 has no DG action; A17 is a Rating Watch placement, not a downgrade.

**Q18.** E06. A17 (RWN, 2026-09-03) is still in effect. E14's watch (A35, 2025-11-20) is not explicitly cleared in the data, but the 2026-05-01 affirmation (A33) likely resolved it, so I've excluded it.

**Q19.** E01 and E09. Both have NEG outlooks from A03 (2026-02-10) and A25 (2026-03-01) that no later action changes.

**Q20.** No. E07's latest action is a withdrawal (A19, WD), which is explicitly not a default.

**Q21.** E07. It had a rating that was withdrawn on 2026-05-12 (A19). E11 and VD have only CO and Country Ceiling records, which are not issuer ratings.

**Q22.** E08. It is the only entity with an RD (default) action (A22).

**Q23.** F2. This is E01's STIDR (A04, 2026-02-10).

**Q24.** Yes, BBB. A03 (affirmed BBB, 2026-02-10) is E01's latest LTIDR action.

**Q25.** 5. I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-) are investment grade. I02 is BB+, I04 is BB, and I08 is unrated (EX only).

**Q26.** A+. This is E15's LC rating from A40 (2024-03-01).

**Q27.** A-. This is I06's latest rating, from A42 (2024-03-01).

**Q28.** BBB+. This is CV's FC issuer rating from A38 (2024-01-01).

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is explicitly not a sovereign issuer rating.

**Q30.** E05 and E15. E05's FC rating (BB, A14) equals Valdoria's ceiling (BB, A12), and E15's FC rating (A, A41) equals Corvenia's ceiling (A, A37).

**Q31.** No. The only companies under ceilings are E05 and E15, and both are exactly at their ceiling, not above it.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank AG), rated BBB+. I05 is guaranteed by E10, so its credit risk and rating (A29, BBB+) follow the guarantor.

**Q34.** No. E12 has no parent link, and its LEI differs from every entity in the Halden group.

**Q35.** 3: E09, E10 (with E17, same LEI) and E11.

**Q36.** 2: E02 (with E03, same LEI) and E04.

**Q37.** 16. There are 18 IDs, but E03 duplicates E02 and E17 duplicates E10 by LEI, and E16 is a QA record to be ignored. The 16 include the two sovereigns, VD and CV.

**Q38.** No. Their LEIs and countries differ (DE vs US).

**Q39.** A. Its latest LTIDR action is A09 (2025-09-15).

**Q40.** 5: E01, E02 (with E03), E09, E12 and E14. E07 has no rating, and E16 is excluded.

**Q41.** None. E16 is a QA record, so its actions must be ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile, overriding the RATINGS record (E10: DE).

**Q43.** 1: E10/E17, Halden Bank.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. Local-currency debt is not subject to the Country Ceiling, so the BB ceiling does not limit I07's BBB- rating.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating until an AS action confirms it.

**Q48.** 7: I01 through I07. I08 is unrated, as in Q47.

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
  "Q10": {"investment_grade": "no"},
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
  "Q24": {"investment_grade": "yes", "rating": "BBB"},
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