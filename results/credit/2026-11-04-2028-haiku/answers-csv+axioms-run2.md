**Q1.** A-. The only LTIDR action before 1 Jan 2025 is A01 (A-), and the next, A02 (BBB), came on 2025-06-20.

**Q2.** No. The 2026 actions on E01 are affirmations (A03 AF, A04 AF); the only downgrade is A02 in 2025.

**Q3.** No; the rating is BB+. I02 was assigned BBB (A23) and downgraded to BB+ (A07, 2025-06-20).

**Q4.** Positive. E03 is the same entity as E02 (identical LEI), and its A09 (2025-09-15, outlook POS) superseded E02's A08 (STA).

**Q5.** E02 (Northwind Holdings), rated A. The notes' guarantor is E02, so the guarantor's risk applies; I03 was affirmed at A (A11).

**Q6.** The foreign-currency rating is BB (A14) and the local-currency rating is BBB- (A13). The sovereign ceiling for Valdoria is BB (A12), which caps the foreign-currency rating. The data doesn't state the reason explicitly, so this follows from the ceiling constraint.

**Q7.** E08 and E10. E08 was downgraded in 2026 (A21, A22) and E10 (A27). E16 was also downgraded (A44), but it is a QA test record, so I excluded it.

**Q8.** E08. Its current LTIDR is RD (A22, 2026-07-08).

**Q9.** 12. These are the legal entities with an in-force LTIDR or STIDR on 1 Oct 2026: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15. I excluded E07 (withdrawn, A19), E04 and E11 (no issuer rating; E11 has only a credit opinion), VD (only a ceiling), and E16 (test record).

**Q10.** Depends. Local-currency BBB- (A13) is investment grade; foreign-currency BB (A14) is not.

**Q11.** BBB+. A36 (2024-09-30) was the last change before 1 Jun 2025.

**Q12.** A-. A34 (A-, 2023-01-15) was in force until A36 on 2024-09-30.

**Q13.** 1. The only downgrade is A36. The RW (A35) and AF (A33) actions are not downgrades.

**Q14.** None. E12's first rating is BB- (A30, 2024-02-01), after 1 Jan 2024.

**Q15.** A-. E10's A26 (A-) was in force until A27 (2026-04-15). E17 is the same entity as E10.

**Q16.** No. The rating has been BBB+ since A36; A35 placed a watch and A33 affirmed it.

**Q17.** No. E06 had only a watch placement (A17, RW) and no downgrade in 2026.

**Q18.** E06. A17 (RWN, 2026-09-03) has no later action. A35 (E14, RWN) was superseded by A33 (AF, 2026-05-01).

**Q19.** E01 and E09. E01 (A03) and E09 (A25) carry NEG outlooks. E06's latest action (A17) has no outlook recorded.

**Q20.** No. E07's latest action is a withdrawal (A19, WD), not a default.

**Q21.** E07, which withdrew its rating (A19, 2026-05-12). E16 also had LTIDR actions, but as a QA test record it is excluded.

**Q22.** E08. It was downgraded to RD (A22).

**Q23.** F2 (A04, STIDR).

**Q24.** Yes. Its in-force LTIDR is BBB (A03).

**Q25.** 5. The instruments with an in-force IG rating are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an expected rating (A47, EX), which is not in force.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42).

**Q28.** BBB+ (A38, FC).

**Q29.** None. VD's only rating is a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC BB (A14) equals Valdoria's ceiling BB (A12), and E15's FC A (A41) equals Corvenia's ceiling A (A37).

**Q31.** No. The only entities with a ceiling are E05 and E15, and neither is above it.

**Q32.** E09 (Halden Group plc). E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank). I05's guarantor is E10, and its latest rating is BBB+ (A29).

**Q34.** No. E12 has no parent or ancestor link in the data, while E10's ultimate parent is E09.

**Q35.** 3 distinct legal entities: E09, E10 (= E17 by LEI) and E11. The data has four Halden records, but E10 and E17 are one entity.

**Q36.** 2 distinct legal entities: E02 (= E03 by LEI) and E04.

**Q37.** 16. The data has 19 records, minus the QA record E16, minus the duplicates E03 (= E02) and E17 (= E10).

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A (A09, AF, 2025-09-15, recorded against E03, which is the same entity as E02).

**Q40.** 5. The GB-domiciled issuers with an issuer rating are E01, E02, E09, E12 and E14.

**Q41.** None. E16 is a QA test record, and the ontology says its actions are not rating actions. Its BB+ (A44) is therefore not treated as an in-force rating.

**Q42.** LU. The RESEARCH record (E17) gives Luxembourg, and that domicile is applied to the same entity as E10.

**Q43.** 1. Only E10/E17 is domiciled in LU.

**Q44.** Yes. I07 is denominated in XVD, which is Valdoria's domestic currency.

**Q45.** No. The ceiling constrains only foreign-currency LTIDR ratings, and I07 is a local-currency obligation (see Q44), even though BBB- is above the BB ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None in force. I08 has only an expected rating of A (A47, EX).

**Q48.** 7. The instruments with an in-force rating are I01 through I07; I08 has only an expected rating.

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