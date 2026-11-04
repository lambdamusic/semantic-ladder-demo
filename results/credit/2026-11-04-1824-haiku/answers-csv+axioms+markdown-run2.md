**Q1.** A-. Latest action on or before the date is A01 (2024-03-12, AS); the downgrade A02 came later.

**Q2.** No. E01's 2026 actions are affirmations (A03, A04) only.

**Q3.** No, rated BB+. I02 (subordinated) was downgraded to BB+ by A07 (2025-06-20).

**Q4.** Positive (POS). E03 (same LEI as E02) has the latest action, A09 (2025-09-15), with outlook POS. E03 and E02 are one entity, so this is the latest outlook for it.

**Q5.** E02 (Northwind Holdings). I03 is guaranteed by E02, so the holder takes E02's risk; I03 is rated A (A11).

**Q6.** The Valdoria Country Ceiling (VD, CC, BB, A12) caps foreign-currency ratings of Valdoria-domiciled entities. E05's FC rating (A14, BB) sits at that cap, while its local-currency rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and then RD (A22); E10 was downgraded to BBB+ (A27).

**Q8.** E08. Its RD action (A22, 2026-07-08) is the only default (RD or D) in the data.

**Q9.** 12. These entities hold a current LTIDR or STIDR: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15. E07 is withdrawn (A19), E11 has only a credit opinion, and E04 and VD have no issuer rating.

**Q10.** No. The headline FC rating is BB (A14). The LC rating (A13, BBB-) is investment grade, but the ontology treats FC as the headline.

**Q11.** BBB+. Latest action on or before 2025-06-01 is A36 (DG, 2024-09-30, BBB+); the 2025-11-20 watch placement does not change the rating.

**Q12.** A-. Only action on or before 2024-01-01 is A34 (AS, 2023-01-15).

**Q13.** 1. The only downgrade of E14 is A36 (2024-09-30). The watch placement (A35) is not a downgrade.

**Q14.** None. E12's first action is A30 (AS, 2024-02-01), which is after 2024-01-01.

**Q15.** A-. E10's latest action on or before 2026-01-01 is A26 (AS, A-); the downgrade A27 came later.

**Q16.** No. The rating on 2025-01-01 was BBB+ (A36), and the later actions A35 (watch) and A33 (affirmation) left it at BBB+.

**Q17.** No. E06's 2026 action (A17) is a Rating Watch placement, not a downgrade.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's watch (A35) appears to have been cleared by the blank-watch affirmation A33 (2026-05-01); the data does not state this explicitly.

**Q19.** E01 and E09. Both have NEG outlooks (A03, A25) and no later outlook change.

**Q20.** No. E07 was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07. It had a BB issuer rating (A18) that was withdrawn (A19). E11 and VD never held an issuer rating.

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2. E01's STIDR affirmed at F2 (A04, 2026-02-10).

**Q24.** Yes. E01's LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. Investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below, and I08 has only an expected rating.

**Q26.** A+. E15's local-currency rating is A+ (A40), with no later action.

**Q27.** A-. I06 (subordinated) was assigned A- (A42).

**Q28.** BBB+. CV's FC issuer rating is BBB+ (A38). Its CC action (A37) is a ceiling, not an issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12), which the ontology says is not the sovereign's issuer rating.

**Q30.** E05 and E15. E05 is FC BB against Valdoria's BB ceiling, and E15 is FC A against Corvenia's A ceiling.

**Q31.** No. Every company FC rating is at or below its ceiling. Only VD and CV have ceilings, and E05 and E15 sit exactly at theirs.

**Q32.** E09 (Halden Group). E11's parent is E10, and E10's parent is E09, which has no parent.

**Q33.** E10 (Halden Bank). I05 is guaranteed by E10, so the holder takes E10's risk; I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent link to the Halden Group or Halden Bank; the shared name is coincidental.

**Q35.** 3. The Halden group is E09, E10 (also recorded as E17) and E11.

**Q36.** 2. The Northwind group is E02 (also recorded as E03) and E04.

**Q37.** 16. There are 18 non-QA records, with E03 duplicating E02 and E17 duplicating E10. E16 is QA and is excluded.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. E03's latest action is A09 (AF, A, 2025-09-15).

**Q40.** 5. The GB issuers with current ratings are E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA record, and its actions must be ignored.

**Q42.** DE. RATINGS (E10) holds over RESEARCH (E17, LU).

**Q43.** 0. The only LU record is E17, which is the same entity as E10 and is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD.

**Q45.** No. I07 is local-currency debt, and the ceiling applies only to FC ratings. Its BBB- rating is above the BB ceiling numerically, but that is not a cap breach.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), which is not yet a rating.

**Q48.** 7. I01 through I07 have ratings. I08 has only an expected rating.

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