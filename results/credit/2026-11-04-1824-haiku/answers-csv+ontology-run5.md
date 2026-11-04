**Q1.** A-. Only A01 (2024-03-12, assigned A-) precedes 1 Jan 2025; A02 (BBB) came later.

**Q2.** No. The 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No, BB+. I02 was downgraded to BB+ by A07 (2025-06-20), which superseded the BBB of A23.

**Q4.** Positive (POS). E02 and E03 are one entity (same LEI); the latest action is A09 (2025-09-15), with outlook POS.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so the holder takes E02's risk, and I03's instrument rating is A (A11).

**Q6.** Valdoria's Country Ceiling (VD, BB, A12) caps foreign-currency ratings but not local-currency ones. E05's FC rating (BB, A14) sits at the ceiling, while its LC rating (BBB-, A13) does not. The data sets the ceiling but doesn't explicitly state this as the cause, so this is an inference.

**Q7.** E08 (Saxby, DG to CCC on A21 and to RD on A22) and E10 (Halden Bank, DG to BBB+ on A27). I05 was also downgraded in 2026, but it is an instrument, not an issuer.

**Q8.** E08. Its RD rating (A22, 2026-07-08) is a default, and no other entity has RD or D.

**Q9.** 12 entities hold an LTIDR on 1 Oct 2026: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 (WD, A19) and E11 (only a credit opinion, A46) do not count, and E08 counts because RD is a point on the scale.

**Q10.** Depends. The headline FC rating is BB (A14), which is not investment grade, but the LC rating is BBB- (A13), which is.

**Q11.** BBB+. A36 (2024-09-30) set BBB+, and the next action, A35, came later (2025-11-20).

**Q12.** A-. A34 (2023-01-15) is the latest action before 1 Jan 2024.

**Q13.** 1. The only downgrade is A36 (2024-09-30); A35 is a Rating Watch, not a downgrade.

**Q14.** None. E12's first action (A30, BB-) is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. E10's A27 downgrade to BBB+ is dated 2026-04-15, after 1 Jan 2026.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 (A36) and is still BBB+ (A33); the Rating Watch in A35 does not change it.

**Q17.** No. E06 has no downgrade in 2026; its only 2026 action is A17, a Rating Watch.

**Q18.** E06 (A17, RWN, 2026-09-03). E14's Watch (A35) was cleared by the affirmation in A33, which has no watch flag.

**Q19.** E01 (A03, NEG) and E09 (A25, NEG).

**Q20.** No. E07 was withdrawn (A19, WD), and a withdrawal is not default.

**Q21.** E07. It had a rating (A18) and was withdrawn (A19). E11 never had an issuer rating, and the sovereigns only have Country Ceilings.

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2. This is the latest STIDR, A04 (2026-02-10).

**Q24.** Yes. E01's FC LTIDR is BBB (A03), which is investment grade.

**Q25.** 5 instruments are investment grade on 1 Oct 2026: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+. E15's LC rating is A+ (A40), with no later LC action.

**Q27.** A-. I06 was assigned A- (A42).

**Q28.** BBB+. CV's FC LTIDR (A38) is BBB+; the Country Ceiling (A37, A) is not its issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A).

**Q31.** No. E05 and E15 are exactly at their ceilings, and the other entities are in countries with no ceiling.

**Q32.** E09 (Halden Group plc). E11's parent is E10, and E10's parent is E09, which has no parent.

**Q33.** Halden Bank AG (E10). I05 is guaranteed by E10, so the holder takes E10's risk, and the instrument is rated BBB+ (A29).

**Q34.** No. E12 has no parent, and E09, E10 and E11 form a separate group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. The count excludes the QA record E16, and E10/E17 and E02/E03 are each counted once.

**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214).

**Q39.** A. The latest action on the entity is A09 (2025-09-15), which affirmed A.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, and E17 is recorded as LU in RESEARCH but DE in RATINGS.

**Q41.** None. E16 is a QA record, so it is ignored.

**Q42.** DE. The RATINGS record for E10 holds DE; the LU in E17 comes from RESEARCH.

**Q43.** 0. No entity is domiciled in LU per the RATINGS records.

**Q44.** Yes. I07 is denominated in XVD, Valdoria's domestic currency, so it is local-currency debt.

**Q45.** No. I07 is local-currency debt, so the BB Country Ceiling (A12) does not cap it, even though BBB- is above BB.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08's A47 is an Expected rating (EX), which is not a rating until an AS action confirms it.

**Q48.** 7 instruments hold a rating: I01 to I07. I08 is unrated.

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