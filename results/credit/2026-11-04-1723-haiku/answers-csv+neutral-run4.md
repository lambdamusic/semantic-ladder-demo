**Q1.** A-. The latest action on or before 1 Jan 2025 is A01 (assigned A-, 2024-03-12); the downgrade to BBB (A02) came on 2025-06-20.

**Q2.** No. The 2026 actions on E01 are affirmations (A03 LTIDR, A04 STIDR), and neither changes the rating.

**Q3.** No, rated BB+. I02 was downgraded from BBB to BB+ (A07, 2025-06-20), and BB+ is speculative grade.

**Q4.** POS (Positive). E03 is the same entity as E02 (same LEI), and its latest action A09 (2025-09-15) affirmed A with a Positive outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so the holder takes E02's credit risk, and A11 rates the note at A, in line with the guarantor.

**Q6.** Valdoria's foreign-currency rating (BB, A14) sits at its Country Ceiling (BB, A12), which caps FC ratings. Its local-currency rating (BBB-, A13) is not capped. (Not in the JSON, since Q6 is not in the requested list.)

**Q7.** E08 (DG to CCC on 2026-01-20, and DG to RD on 2026-07-08) and E10 (DG to BBB+ on 2026-04-15). The 2026 downgrade of I05 (A29) is an instrument action, not an issuer action, so it is excluded.

**Q8.** E08. A22 (2026-07-08) downgrades it to RD, which the ontology defines as a default.

**Q9.** 12. Counted: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15. Excluded: E04 (no rating), E07 (withdrawn by A19), VD and E11 (only a Country Ceiling or credit opinion), and E16 (QA, ignored).

**Q10.** Depends. The FC rating is BB (not investment grade, A14), but the LC rating is BBB- (investment grade, A13).

**Q11.** BBB+. The rating on 2025-06-01 is set by A36 (DG to BBB+, 2024-09-30), since A35 came later, on 2025-11-20.

**Q12.** A-. A34 (assigned A-, 2023-01-15) is the latest action before 1 Jan 2024.

**Q13.** 1. A36 (2024-09-30) is the only downgrade; A35 is a Rating Watch placement, not a downgrade.

**Q14.** None. Halden Foods' first action (A30) is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. A26 (assigned A-, 2023-05-01) is the latest action before 2026-01-01; the downgrade to BBB+ (A27) is dated 2026-04-15. E17 is the same entity as E10.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33); the 2025 Watch (A35) did not change it.

**Q17.** No. Orrin Bank AG (E06) was placed on Rating Watch Negative (A17, 2026-09-03), which is not a downgrade.

**Q18.** E06. A17 (2026-09-03) sets RWN with no later action on E06. E14's Watch (A35) was cleared by the affirmation A33, which has a blank watch field.

**Q19.** E01 (A03, NEG) and E09 (A25, NEG). Both are the latest outlook-setting actions on their FC issuer ratings.

**Q20.** No. E07 withdrew its rating (A19, WD), and withdrawal is not a default.

**Q21.** E07. It had a rating (A18) and it was withdrawn (A19). E11 and VD have only a credit opinion and a Country Ceiling, neither of which is an issuer rating.

**Q22.** E08. It was downgraded to RD on 2026-07-08 (A22).

**Q23.** F2. A04 (2026-02-10) affirmed F2.

**Q24.** Yes. The issuer rating is BBB (A03, affirmed 2026-02-10), which is investment grade even though its outlook is Negative.

**Q25.** 5. The instruments rated investment grade on 1 Oct 2026 are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), and I07 (BBB-). I02 and I04 are speculative grade, and I08 is unrated.

**Q26.** A+. A40 (LC, 2024-03-01) is the only LC action on E15.

**Q27.** A-. I06 was assigned A- on 2024-03-01 (A42).

**Q28.** BBB+. A38 (2024-01-01) rates the Republic of Corvenia's FC issuer rating. Its A ceiling (A37) is not an issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12), which the ontology says is not the sovereign's issuer rating.

**Q30.** E05 and E15. E05's FC rating (BB) equals Valdoria's ceiling (BB), and E15's FC rating (A) equals Corvenia's ceiling (A).

**Q31.** No. The only ceilings are VD (BB) and CV (A), and no FC issuer rating in VD or CV exceeds them.

**Q32.** E09 (Halden Group plc). Halden Leasing (E11) is owned by E10, and E10 is owned by E09.

**Q33.** Halden Bank AG (E10), rated BBB+. I05 is guaranteed by E10, and A29 rates the note at BBB+, in line with the guarantor.

**Q34.** No. Halden Foods (E12) has no parent recorded, while Halden Bank (E10) belongs to E09. The shared name is not evidence of common ownership.

**Q35.** 3. The Halden group is E09, E10 (also recorded as E17), and E11.

**Q36.** 2. The Northwind group is E02 (also recorded as E03) and E04.

**Q37.** 16. The distinct entities are E01, E02, E04, E05, VD, E06, E07, E08, E09, E10, E11, E12, E13, E14, CV, and E15. E16 is excluded as QA, and the two sovereigns are counted as entities under the ontology's definition.

**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 for E06 and 815600O8X8K2F154N214 for E13).

**Q39.** A. A09 (2025-09-15) affirmed A.

**Q40.** 5. The GB issuers with ratings on 1 Oct 2026 are E01, E02, E09, E12, and E14. E07 has been withdrawn, and E16 is QA.

**Q41.** None. E16 is a QA record, which must be ignored.

**Q42.** DE. RATINGS is the system of record, and it gives Germany (E10). The RESEARCH record (E17) says LU but is overridden.

**Q43.** 0. The only LU record is E17, which is the same entity as E10, and RATINGS records E10 as DE.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of Valdoria, so it is local-currency debt.

**Q45.** No. I07 is local-currency debt, and the Country Ceiling (BB, A12) does not apply to local-currency debt, so it cannot be "above" the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which the ontology says is never an issuer rating.

**Q47.** None. A47 (2026-09-01) is an expected rating (EX), which is not a rating until an AS action confirms it.

**Q48.** 7. I01 through I07 have ratings on 1 Oct 2026. I08 is unrated.

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