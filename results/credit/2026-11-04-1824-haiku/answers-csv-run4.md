**Q1.** A-. Assigned A- on 2024-03-12 (A01) and not changed until the downgrade to BBB on 2025-06-20 (A02).

**Q2.** No. The only downgrade is A02 (2025-06-20); the 2026 actions (A03, A04) are affirmations.

**Q3.** No, BB+. The 2031 note (I02) was assigned BBB (A23) and downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive (POS). The latest action is A09 (2025-09-15, outlook POS), which is on E03, a duplicate record with the same LEI as E02. E02's own last action (A08) shows STA.

**Q5.** E02 (Northwind Holdings). The 2030 notes (I03) are guaranteed by E02, and E04 has no rating of its own. I03 is rated A (A10, A11).

**Q6.** The data doesn't state a reason. The FC rating (BB, A14) matches Valdoria's sovereign country-ceiling rating (CC BB, A12), which suggests the sovereign ceiling caps it, but this is inferred.

**Q7.** E08, E10, E16. These are the 2026 downgrades in A21/A22, A27 and A44.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22, distressed debt exchange).

**Q9.** 13. These are the distinct entities with a current LTIDR, counting E02 and E03 once (same LEI), E10 and E17 once (same LEI), and including the sovereign CV (A38). VD has only a CC rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. It was downgraded from A- to BBB+ on 2024-09-30 (A36).

**Q12.** A-. This was the rating assigned on 2023-01-15 (A34), with no change before 2024-09-30.

**Q13.** 1. The only downgrade is A36 (2024-09-30). The watch placement A35 is not a downgrade.

**Q14.** None. The first rating is assigned on 2024-02-01 (A30).

**Q15.** A-. The 2023 rating (A26) was unchanged until the downgrade to BBB+ on 2026-04-15 (A27).

**Q16.** No. The rating stayed BBB+ (A36, A35, A33). A Rating Watch Negative was placed on 2025-11-20 (A35), which is a watch change, not a rating change.

**Q17.** No. The only Orrin Bank AG action in 2026 is a Rating Watch placement (A17), with no downgrade.

**Q18.** E06. Its watch was placed on 2026-09-03 (A17). E14's 2025-11-20 watch (A35) appears cleared by the 2026-05-01 affirmation (A33), which carries no watch flag. That clearance is inferred.

**Q19.** E01 and E09. These are the outlooks marked NEG in A03 and A25 with no later change.

**Q20.** No. Pellam's rating was withdrawn on 2026-05-12 (A19). That is not a default.

**Q21.** E07 (Pellam Retail). It was withdrawn on 2026-05-12 (A19). No other entity lost its rating.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. This is the short-term rating from A04.

**Q24.** Yes. Kestrel's long-term issuer rating is BBB (A03), which is investment grade.

**Q25.** 6. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A). I08's only action is "EX", which is undefined; if it means exited, the count is 5.

**Q26.** A+. This is the LC rating from A40.

**Q27.** A-. This is the rating assigned to I06 on 2024-03-01 (A42).

**Q28.** BBB+. This is the FC LTIDR from A38.

**Q29.** None. Valdoria (VD) has only a country-ceiling rating (CC BB, A12), not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, matching Valdoria's ceiling of BB (A12). E15's FC rating is A, matching Corvenia's ceiling of A (A37).

**Q31.** No. The only two ceilings in the data (VD at BB, CV at A) are matched exactly by E05 and E15, not exceeded.

**Q32.** E09 (Halden Group plc). Halden Leasing (E11) → Halden Bank AG (E10) → Halden Group plc (E09).

**Q33.** E10 (Halden Bank AG). The 2028 notes (I05) are guaranteed by E10, and the rating is BBB+ after the downgrade in A29.

**Q34.** No. Halden Foods (E12) has no parent_id and no ownership link to E09 or E10. Only the name is similar, which isn't evidence of common ownership.

**Q35.** 3. These are E09, E10 and E11. E17 is a duplicate of E10, so it isn't counted again.

**Q36.** 2. These are E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 records. E03 duplicates E02 and E17 duplicates E10 (same LEIs), so 17 remain.

**Q38.** No. They have different LEIs, different countries (DE and US), and no parent link.

**Q39.** A. The rating was affirmed on 2025-09-15 (A09) for E03, which duplicates E02.

**Q40.** 6. These are E01, E02, E09, E12, E14 and E16. E07 is GB but was withdrawn.

**Q41.** BB+. This is the rating from A44 (2026-06-01, source QA).

**Q42.** DE. The rating record E10 says DE, but the RESEARCH record E17 says LU for the same LEI. The data conflicts.

**Q43.** 1. Only E17 has country LU. This relies on the conflicting record; if E10's DE is correct, the count is 0.

**Q44.** Depends. The currency is XVD, which matches the VD country code, but the data doesn't define XVD as the local currency.

**Q45.** Depends. The note is rated BBB- (A45), which is above Valdoria's BB ceiling. The ceiling only constrains foreign-currency obligations, so the answer turns on Q44.

**Q46.** Depends. Halden Leasing's only rating is a CO-type rating (A46), and the data doesn't define CO. The data's issuer ratings are LTIDR, which Halden Leasing does not have.

**Q47.** A. The only record is A47 (2026-09-01, action "EX"). "EX" is undefined; if it means exited, the note is unrated.

**Q48.** 8. These are I01 through I08. I08's "EX" action is undefined; if it means exited, the count is 7.

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
  "Q43": {"count": 1},
  "Q44": {"local_currency": "depends"},
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "depends"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```