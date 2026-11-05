**Q1.** A-. Kestrel's last action before 1 Jan 2025 is A01 (assigned A-); A02 (downgrade to BBB) came later.

**Q2.** No. Its 2026 actions (A03, A04) are affirmations.

**Q3.** No. The 2031 note (I02) is rated BB+ after its 2025 downgrade (A07), which is below investment grade.

**Q4.** POS. The latest Northwind Holdings action is A09 (E03, the same LEI as E02), which set the outlook to Positive.

**Q5.** Holders take Northwind Holdings' (E02) credit risk, because I03 is guaranteed by E02. The note is rated A (A11), in line with the guarantor.

**Q6.** Valdoria's foreign-currency rating is capped by the Country Ceiling of BB (A12), which applies to FC ratings only. Its FC rating is BB (A14), at the cap, while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 (downgraded to CCC in A21, then RD in A22) and E10 (downgraded to BBB+ in A27).

**Q8.** E08. Its latest action (A22) is RD, a default.

**Q9.** 12. These entities hold an LTIDR on 1 Oct 2026: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15. E07 is withdrawn (A19), E11 has only a credit opinion (A46), and E04 and VD have no issuer rating.

**Q10.** Depends on currency basis. The FC rating is BB (A14), which is speculative grade, but the LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. The rating on 1 Jun 2025 is set by A36 (BBB+, 2024-09-30); the Rating Watch in A35 does not change the rating.

**Q12.** A-. A34 (assigned A-, 2023-01-15) was the rating on 1 Jan 2024.

**Q13.** 1. A36 (2024-09-30) is the only downgrade; A35 is a Rating Watch, not a downgrade.

**Q14.** None. Halden Foods (E12) was first rated by A30 on 2024-02-01, after the date.

**Q15.** A-. E10 was assigned A- by A26 in 2023, and its next action (A27, BBB+) is in 2026, after the date.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33, affirmed).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch placement.

**Q18.** E06. A17 (2026-09-03) placed it on RWN. E14's Rating Watch (A35) was cleared by A33's affirmation, which carries no watch.

**Q19.** E01 (Negative, A03) and E09 (Negative, A25).

**Q20.** No. Pellam Retail (E07) withdrew its rating (A19, WD) and was last rated BB, with no default.

**Q21.** E07. It held a rating until its withdrawal in A19. E11 and VD have never held an issuer rating, and E16 is a QA record.

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2. Kestrel's STIDR was affirmed at F2 (A04).

**Q24.** Yes. Its only LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+, guaranteed by E10), I06 (A-), and I07 (BBB-). I08 is only an expected rating (EX), so it is unrated.

**Q26.** A+. Corvenia Power's LC rating was assigned as A+ (A40) and has not changed.

**Q27.** A-. The 2032 note (I06) was assigned A- (A42).

**Q28.** BBB+. Corvenia's FC issuer rating is BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not a sovereign issuer rating.

**Q30.** E05 and E15. Valdoria Telecom's FC rating (BB, A14) equals the VD ceiling (A12). Corvenia Power's FC rating (A, A41) equals the CV ceiling (A37).

**Q31.** No. No company's FC issuer rating exceeds its country's ceiling. Only VD and CV have ceilings, and E05 and E15 sit exactly at them.

**Q32.** E09 (Halden Group plc). The chain is E11 → E10 → E09, and E09 has no parent.

**Q33.** Holders take Halden Bank AG's (E10) credit risk, because I05 is guaranteed by E10. The note is rated BBB+ (A29), in line with the guarantor.

**Q34.** No. Halden Foods (E12) has no parent link, and Halden Bank (E10) belongs to the E09 group.

**Q35.** 3. The Halden group is E09, E10 and E11. E17 is a second record for E10.

**Q36.** 2. The Northwind group is E02 (with E03 as the same entity) and E04.

**Q37.** 16. There are 19 records. I excluded E03 and E17 (duplicate LEIs), and E16 (a QA record).

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. Northwind Holdings' latest rating is A (A09).

**Q40.** 5. The GB issuers with an LTIDR on 1 Oct 2026 are E01, E02, E09, E12 and E14. E07 is excluded because it withdrew its rating (A19).

**Q41.** None. Brindle Capital (E16) is a QA record, which must be ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile, and it says LU, not DE.

**Q43.** 1. Only E10 (E17 is the same entity) is domiciled in LU.

**Q44.** Yes. XVD is Valdoria's domestic currency, so the note is local-currency debt.

**Q45.** No. The note (I07) is BBB- in local currency. The Country Ceiling (BB) caps only FC obligations, so the note is not capped and does not breach the ceiling.

**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. The 2034 note (I08) has only an expected rating (EX, A47), so it is not yet rated.

**Q48.** 7. The rated instruments are I01 through I07. I08 is unrated.

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