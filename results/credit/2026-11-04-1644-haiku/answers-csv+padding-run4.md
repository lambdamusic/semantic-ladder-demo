**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action, the downgrade to BBB in A02 (2025-06-20), came later.

**Q2.** No. The only downgrade of E01 is A02 (2025); its 2026 actions are affirmations (A03, A04).

**Q3.** No, BB+. I02 is subordinated and was cut to BB+ by A07 (2025-06-20), which is below investment grade.

**Q4.** POS, with a conflict to resolve. A09 (2025-09-15) affirmed A with a Positive outlook on E03, which has the same LEI as E02, but E02's own record shows STA (A08).

**Q5.** The holder takes the credit risk of Northwind Finance BV (E04), with the notes guaranteed by Northwind Holdings (E02). The notes are rated A (A11, affirmed 2025-09-15).

**Q6.** The data gives no reason. E05's foreign-currency rating (BB, A14) equals Valdoria's country ceiling (BB, A12), which is consistent with the ceiling capping it, but that is an inference.

**Q7.** E08 (A21 to CCC, A22 to RD), E10 (A27 to BBB+) and E16 (A44 to BB+). The I05 note of E11 was also downgraded (A29), following its guarantor E10.

**Q8.** E08, which was rated RD on 2026-07-08 (A22) with no later action.

**Q9.** 13. These are the non-withdrawn LTIDR issuers: E01, E02 (same LEI as E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19).

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) set BBB+, and the watch placed in A35 (2025-11-20) came after 1 June 2025.

**Q12.** A-. A34 (2023-01-15) assigned A-, and the next action, A36, came on 2024-09-30.

**Q13.** 1. Only A36 (A- to BBB+) is a downgrade; A35 placed the rating on watch.

**Q14.** None. E12's first rating is A30 (2024-02-01), which is after 1 January 2024.

**Q15.** A-. A26 (2023) set A-, and the first later action, A27 (2026-04-15), moved it to BBB+, so the rating on 1 January 2026 was still A-.

**Q16.** No. The rating has been BBB+ since A36 (2024-09-30). A35 placed it on watch, and A33 affirmed BBB+.

**Q17.** No. A17 (2026-09-03) placed E06 on Rating Watch Negative (RWN) at A-, which is not a downgrade.

**Q18.** E06 (A17, RWN, with no later resolution). E14's watch from A35 was cleared by the affirmation in A33.

**Q19.** E01 (A03) and E09 (A25). E06's outlook is blank after its watch action (A17), so it is not stated.

**Q20.** No. E07 was withdrawn (A19, WD), not placed in default.

**Q21.** E07, whose rating was withdrawn in A19 (2026-05-12).

**Q22.** E08, which was rated RD (A22).

**Q23.** F2 (A04, short-term rating, 2026-02-10).

**Q24.** Yes, BBB (A03), which is investment grade.

**Q25.** 6: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A). I08's action "EX" is not defined in the data; if it means expiry, the count is 5.

**Q26.** A+ (A40, local currency).

**Q27.** A- (A42). I06 is the 2032 note.

**Q28.** BBB+ (A38, foreign currency).

**Q29.** None. VD has only a country-ceiling rating (BB, A12) and no issuer (LTIDR) record.

**Q30.** E05 (BB, equal to the VD ceiling of BB in A12) and E15 (A, equal to the CV ceiling of A in A37).

**Q31.** No. Ceilings exist only for VD and CV, and E05 and E15 sit exactly at them, not above.

**Q32.** E09 (Halden Group plc). E11's parent is E10, whose parent is E09.

**Q33.** E11 (Halden Leasing), which issued I05, guaranteed by E10. The rating is BBB+ (A29).

**Q34.** No. E12 has no parent_id, and the data records the Halden group as E09, E10 and E11. The shared name alone is not a recorded link.

**Q35.** 3: E09, E10 and E11. E17 has the same LEI as E10, so it is not a separate entity.

**Q36.** 2: E02 and E04. E03 has E02's LEI.

**Q37.** 17. The data has 19 rows, but E03 and E17 share LEIs with E02 and E10. The sovereigns VD and CV have no LEI but are counted as entities.

**Q38.** No. They have different LEIs and countries (DE and US), and no parent link.

**Q39.** A (A08 for E02; A09 for E03, which has the same LEI).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because it was withdrawn.

**Q41.** BB+ (A44, 2026-06-01, from the QA source).

**Q42.** DE, per E10. E17 (same LEI, RESEARCH source) lists LU, which conflicts with E10.

**Q43.** 1 record (E17, LU). That entity has the same LEI as E10, which is recorded as DE, so the data is inconsistent.

**Q44.** Depends. I07 is denominated in XVD, but the data does not define XVD or say which currency is Valdoria's local currency.

**Q45.** Depends. I07 is rated BBB- (A45), above the BB ceiling (A12). The ceiling applies only to foreign-currency obligations, and whether I07 is one depends on Q44.

**Q46.** Depends. E11 has no LTIDR record. Its only rating is a CO-type BBB (A46), and the data does not define the CO type.

**Q47.** A (A47). The action is "EX", which is not defined in the data; the rating itself is A.

**Q48.** 8. All eight instruments (I01–I08) have instrument ratings. If I08's "EX" action removes its rating, the count is 7.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E04", "rating": "A"},
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
  "Q33": {"risk_of": "E11", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": 17},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": 6},
  "Q41": {"rating": "BB+"},
  "Q42": {"country": "DE"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "depends"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "depends"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```