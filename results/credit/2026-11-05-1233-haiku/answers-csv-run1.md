**Q1.** A-. Rated A- from 2024-03-12 (A01) until downgraded to BBB on 2025-06-20 (A02).

**Q2.** No. The 2026 actions on E01 (A03, A04) are affirmations, not downgrades.

**Q3.** No, it is BB+. I02 was BBB (A23), then downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive (POS). E03 has the same LEI as E02 and carries the only later outlook (POS, A09), but E02's own record (A08) shows STA. This assumes E03 and E02 are the same entity.

**Q5.** Holders of I03 take the credit risk of guarantor E02 (issuer E04 is the obligor), rated A. The instrument rating (A10, A11) matches E02's level, and E04 has no rating of its own.

**Q6.** The foreign-currency rating (BB, A14) is below the local-currency rating (BBB-, A13), which is consistent with the sovereign's foreign-currency country ceiling of BB (A12). The data does not state this reason explicitly.

**Q7.** E08, E10 and E16. Each was downgraded in 2026 (A21/A22, A27, A44).

**Q8.** E08. Its RD rating (A22, 2026-07-08) reflects a completed distressed debt exchange.

**Q9.** 12. Entities with an active LTIDR rating on 1 Oct 2026 are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15, E16. E03 is excluded as a duplicate of E02, E07 was withdrawn (A19), and E11's CO-type rating is not an LTIDR.

**Q10.** Depends. The local-currency rating (BBB-, A13) is investment grade, but the foreign-currency rating (BB, A14) is not.

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and that was still the rating on 2025-06-01.

**Q12.** A-. The rating was A- from 2023-01-15 (A34) until the 2024-09-30 downgrade (A36).

**Q13.** 1. The only downgrade is A36 (2024-09-30). A35 is a Rating Watch placement, not a downgrade.

**Q14.** None. Halden Foods' first rating is BB- on 2024-02-01 (A30), after 1 Jan 2024.

**Q15.** A-. Halden Bank's rating was A- until its downgrade to BBB+ on 2026-04-15 (A27).

**Q16.** No. The rating stayed BBB+ (A36, A33); only a Rating Watch Negative was placed (A35).

**Q17.** No. The only 2026 action on E06 is a Rating Watch Negative placement (A17), not a downgrade.

**Q18.** E06. Its RWN (A17, 2026-09-03) has no later resolving action. E14's RWN (A35) was cleared by the 2026-05-01 affirmation (A33).

**Q19.** E01 and E09. Their latest outlooks are NEG (A03, A25), and no later action changes them.

**Q20.** No. E07 was withdrawn on commercial grounds (A19), which is not a default.

**Q21.** E07. Its rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. This is the short-term rating from A04 (2026-02-10).

**Q24.** Yes. The current issuer rating is BBB (A03).

**Q25.** 6. The investment-grade instruments are I01, I03, I05, I06, I07 and I08. I02 (BB+) and I04 (BB) are not.

**Q26.** A+. This is the local-currency rating from A40.

**Q27.** A-. This is the instrument rating from A42.

**Q28.** BBB+. This is the foreign-currency rating from A38. The sovereign's A-rated country ceiling (A37) is a separate record.

**Q29.** None. The Republic of Valdoria has only a country ceiling (CC, BB; A12), not an issuer rating.

**Q30.** E05 and E15. Their foreign-currency ratings equal their country ceilings: BB for E05 (A14, ceiling A12) and A for E15 (A41, ceiling A37).

**Q31.** No. No foreign-currency issuer rating exceeds its country ceiling.

**Q32.** E09. E11 → E10 → E09, and E09 has no parent.

**Q33.** Holders take the credit risk of guarantor E10, which is rated BBB+ (A29). The matching BBB+ rating on E10 (A27) supports this reading. The issuer, E11, is the obligor.

**Q34.** No. E12 has no parent link, and the shared name alone does not establish a group.

**Q35.** 3. The Halden group is E09, E10 and E11. E17 shares E10's LEI, so it is not counted separately.

**Q36.** 2. The Northwind group is E02 and E04. E03 shares E02's LEI.

**Q37.** 17. The data describes 19 records, but E03 and E17 duplicate E02 and E10 by LEI. That leaves 17 distinct entities, including the two sovereigns (VD, CV), which have no LEI.

**Q38.** No. The LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. This is E02's rating from A08. E03 shares its LEI and has no separate rating.

**Q40.** 6. The GB issuers with active ratings are E01, E02, E09, E12, E14 and E16. E07 is withdrawn, and E03 duplicates E02.

**Q41.** BB+. This is Brindle Capital's downgrade from A44 (2026-06-01), though its source is QA.

**Q42.** DE. E10 (Halden Bank AG) is domiciled in DE, but the RESEARCH record E17 with the same LEI lists LU.

**Q43.** 1. Only E17 lists LU. However, E17 shares an LEI with E10, which is DE, so it may be the same entity.

**Q44.** Yes, inferred. I07 is denominated in XVD, which is presumably Valdoria's currency, though the data does not define the code.

**Q45.** Yes. The I07 rating of BBB- (A45) is above the sovereign ceiling of BB (A12). Ceilings cap foreign-currency ratings, so a local-currency note is not constrained by it.

**Q46.** Depends. E11 has only a CO-type rating (BBB, A46). The data does not define CO, and the LTIDR type is the issuer rating.

**Q47.** A. The instrument was rated A on 2026-09-01 (A47, action EX).

**Q48.** 8. Every instrument, I01 through I08, has an INST rating in the data as of 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": ["E08", "E10", "E16"]},
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
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "yes"},
  "Q46": {"issuer_rating": "depends"},
  "Q47": {"rating": "A"},
  "Q48": {"count": 8}
}
```