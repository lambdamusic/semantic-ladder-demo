**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01) and not changed until the 2025-06-20 downgrade (A02).

**Q2.** No. Kestrel's 2026 actions (A03, A04) are affirmations, and the only downgrade is A02 in 2025.

**Q3.** No, rating BB+. The 2031 note is subordinated (I02), and its last action was a downgrade to BB+ (A07), so it is speculative grade.

**Q4.** POS. Northwind Holdings' latest action is A09 (2025-09-15) on E03, which has the same LEI as E02, and it carries a Positive outlook.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so it is rated on the guarantor, and its latest action is A11 (A).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps foreign-currency ratings. Its FC rating is BB (A14), while its LC rating of BBB- (A13) is not capped. This question has no JSON field in the spec, so it is omitted from the block.

**Q7.** E08 (Saxby Shipping, A21 and A22) and E10 (Halden Bank AG, A27). E10 and E17 share an LEI, so they are one entity.

**Q8.** E08. Its distressed debt exchange (A22, RD) was the latest action and no later action exists.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 has been withdrawn, E11 has only a credit opinion (A46), and the sovereign VD has only a Country Ceiling.

**Q10.** Depends. The LC rating is BBB- (A13), which is investment grade, but the FC rating is BB (A14), which is not.

**Q11.** BBB+. The downgrade to BBB+ (A36, 2024-09-30) was the latest action before 2025-06-01.

**Q12.** A-. The first assignment (A34, 2023-01-15) was the latest action before 2024-01-01.

**Q13.** 1. A36 is the only downgrade on E14; the other actions are an affirmation (A33) and a Watch placement (A35).

**Q14.** None. Halden Foods' first rating (A30) is dated 2024-02-01, after 2024-01-01.

**Q15.** A-. Halden Bank's last action before 2026-01-01 is the assignment of A- (A26), since the downgrade (A27) came on 2026-04-15.

**Q16.** No. The rating has been BBB+ since 2024-09-30 (A36); the later Watch (A35) and affirmation (A33) left it unchanged.

**Q17.** No. Orrin Bank AG (E06) has no downgrade, only a Watch placement (A17); Orrin Bancorp (E13) has no 2026 actions.

**Q18.** E06. Its latest action (A17, 2026-09-03) carries RWN. E14's Watch (A35) was superseded by the 2026-05-01 affirmation (A33), which carries no Watch flag.

**Q19.** E01 (A03, NEG) and E09 (A25, NEG).

**Q20.** No. Pellam Retail's rating was withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07 (Pellam Retail), which was withdrawn (A19). E11 never had an issuer rating, because its CO (A46) does not count.

**Q22.** E08. It is the only entity with an RD action (A22).

**Q23.** F2. This is Kestrel's STIDR, from A04 (2026-02-10).

**Q24.** Yes. Kestrel's FC LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only an expected rating (EX), so it is unrated.

**Q26.** A+. This is Corvenia Power's LC rating (A40).

**Q27.** A-. The 2032 note was assigned A- (A42).

**Q28.** BBB+. This is the sovereign's FC LTIDR (A38). Its A is a Country Ceiling (A37), not an issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 (FC BB against a Valdoria ceiling of BB) and E15 (FC A against a Corvenia ceiling of A).

**Q31.** No. Neither E05 nor E15 is above its ceiling; both are exactly at it.

**Q32.** E09 (Halden Group plc). The chain runs E11 → E10 → E09, and E09 has no parent.

**Q33.** E10 (Halden Bank AG), rated BBB+. I05 is guaranteed by E10, so it is rated on the guarantor, and its latest action is A29 (BBB+).

**Q34.** No. Halden Foods (E12) has no parent and is not in the Halden Bank chain under E09.

**Q35.** 3. These are E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2. These are E02 and E04. E03 is the same entity as E02.

**Q37.** 16. The data has 19 records. I excluded the QA record E16, and E03 and E17 duplicate E02 and E10, which leaves 16 entities including the two sovereigns.

**Q38.** No. The LEIs differ (549300AMVE3VRVG7HK43 for E06 and 815600O8X8K2F154N214 for E13).

**Q39.** A. Northwind Holdings' latest LTIDR action is A09 (2025-09-15, affirmed at A).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E17 is domiciled in LU per RESEARCH, and E07 has no rating.

**Q41.** None. Brindle Capital (E16) is a QA record, so its actions (A43, A44) are ignored.

**Q42.** LU. RATINGS gives DE (E10), but RESEARCH holds for domicile and gives LU (E17).

**Q43.** 1. The only LU entity is Halden Bank (E10 / E17).

**Q44.** Yes. The 2027 note is denominated in XVD, the domestic currency of VD, where Valdoria Telecom is domiciled (I07).

**Q45.** No. The note is local-currency, so the BB Country Ceiling (A12) does not apply to it.

**Q46.** No. Halden Leasing (E11) has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. The 2034 note (I08) has only an expected rating (EX, A47), so it is unrated until an AS action.

**Q48.** 7. The rated instruments are I01, I02, I03, I04, I05, I06 and I07. I08 is unrated.

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