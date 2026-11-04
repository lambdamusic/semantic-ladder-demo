**Q1.** A-. The latest action on or before 1 Jan 2025 is A01 (assigned A-, 2024-03-12); A02 (downgrade to BBB) came later, on 2025-06-20.

**Q2.** No. The 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, rated BB+. I02 (subordinated) was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E02 (same LEI as E03) has outlook POS from A09.

**Q5.** Northwind Holdings (E02). I03 is guaranteed by E02, so the holder takes its risk, and I03 is rated A (A11), matching E02's A.

**Q6.** Valdoria Telecom's FC rating is BB (A14) and its LC rating is BBB- (A13). The FC rating equals the Valdoria Country Ceiling of BB (A12), which caps foreign-currency ratings, while local-currency ratings are not capped. The data shows the values but does not state the cause.

**Q7.** E08 and E10. A21 and A22 downgrade E08, and A27 downgrades E10 on 2026-04-15. I05 (A29) is an instrument, not an issuer, and E16 is QA data.

**Q8.** E08. Its RD rating (A22, 2026-07-08, distressed debt exchange) is a default and is still current.

**Q9.** 12. The issuers with an issuer rating on 1 Oct 2026 are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E04, E07 (withdrawn, A19), E11 (credit opinion only), VD (ceiling only) and E16 (QA) are excluded.

**Q10.** No on the headline FC rating: E05 is BB (A14). Its LC rating is BBB- (A13), which is investment grade, so the answer depends on which rating is meant.

**Q11.** BBB+. A36 (2024-09-30, downgrade to BBB+) is the latest action before 1 Jun 2025; A35 came later.

**Q12.** A-. A34 (2023-01-15) is the latest action before 1 Jan 2024.

**Q13.** 1. A36 is the only downgrade (A35 is a Watch placement, not a downgrade).

**Q14.** None. E12's first action (A30, BB-) is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. A26 is the latest action on or before 1 Jan 2026; A27 (BBB+) came later, on 2026-04-15. The RESEARCH record E17 is the same LEI and has no rating actions.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33, affirmed 2026-05-01).

**Q17.** No. E06's 2026 action (A17) is a Rating Watch placement, which is not a downgrade.

**Q18.** E06. A17 is on Rating Watch Negative. E14's Watch (A35) was cleared by the later affirmation A33, whose watch field is blank.

**Q19.** E01 and E09. Their latest outlooks are NEG (A03 and A25).

**Q20.** No. E07's withdrawal (A19) is not a credit event.

**Q21.** E07. Its rating was withdrawn (A19, 2026-05-12). E11 and VD never had an issuer rating.

**Q22.** E08. It is the only entity with a default rating (RD, A22).

**Q23.** F2. This is E01's short-term rating (A04).

**Q24.** Yes. Kestrel's current long-term issuer rating is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an expected rating (A47, EX), so it is unrated.

**Q26.** A+. This is E15's local-currency rating (A40).

**Q27.** A-. I06 is rated A- (A42).

**Q28.** BBB+. This is the sovereign's FC issuer rating (A38). Its Country Ceiling (A37) is A, which is a separate record.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. Valdoria Telecom's FC rating BB (A14) equals the VD ceiling BB (A12), and Corvenia Power's FC rating A (A41) equals the CV ceiling A (A37). No other entity has a ceiling in the data.

**Q31.** No. E05 (BB) and E15 (A) are exactly at their ceilings, not above.

**Q32.** E09 (Halden Group plc). E11's parent is E10, whose parent is E09.

**Q33.** Halden Bank AG (E10). I05 is guaranteed by E10, so it is rated on E10's risk, at BBB+ (A29).

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3. The Halden group is E09, E10 (which includes E17) and E11.

**Q36.** 2. The Northwind group is E02 (which includes E03) and its subsidiary E04.

**Q37.** 16. This counts distinct LEIs (E03 merges into E02, and E17 into E10) plus the two sovereigns VD and CV, which the ontology counts as entities despite having no LEI. E16 is excluded as QA.

**Q38.** No. E06 and E13 have different LEIs (ORRN00BANK00000DE233 and ORBC00BANCORP000US45).

**Q39.** A. This is E02's current rating, affirmed by A09.

**Q40.** 5. The GB issuers with an issuer rating are E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, which must be ignored.

**Q42.** DE. The RATINGS record E10 holds, and the RESEARCH record's LU is superseded.

**Q43.** 0. No RATINGS-held entity is domiciled in LU; E17's LU value comes from RESEARCH, which is superseded by E10's DE.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD, where Valdoria Telecom is domiciled.

**Q45.** No. I07 is local-currency debt, so the BB ceiling does not apply to it, even though its BBB- rating (A45) is above BB.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08's only action is an expected rating (A47, EX), which is not yet a rating.

**Q48.** 7. I01 through I07 have ratings. I08 does not.

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