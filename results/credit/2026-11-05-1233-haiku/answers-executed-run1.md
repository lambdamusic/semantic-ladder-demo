**Q1.** A-. E01's FC rating of A- ran from 2024-03-12 to 2025-06-20 (A01), which covers 1 January 2025.

**Q2.** No. E01's FC rating stayed at BBB from 2025-06-20 (A02) onward; the 2026 change (A03, A04) was to outlook and short-term rating only.

**Q3.** No, rated BB+. I02 (the 6.25% 2031 notes) was downgraded to BB+ on 2025-06-20 (A07) and remains current.

**Q4.** Positive. E02's current LTIDR FC rating of A (A09, from 2025-09-15) carries outlook POS.

**Q5.** Northwind Holdings (E02), rated A. I03's credit risk is E02's (credit_risk_of), and I03 is currently rated A (A11).

**Q6.** Valdoria's FC rating (BB) sits exactly at the VD ceiling (BB, from ceilings.csv), while its LC rating (BBB-) is above it. The data supports the ceiling as the reason, but does not state it.

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and then RD (A22), and E10 was downgraded to BBB+ (A27). E07 was withdrawn (WD, A19), which I did not count as a downgrade.

**Q8.** E08. Its current rating is RD (A22, from 2026-07-08). E07's WD is a withdrawal, not a default rating.

**Q9.** 12, including the sovereign CV. These are the entities with a current LTIDR rating (valid_to empty) on 1 October 2026; E07 is excluded because its rating is WD.

**Q10.** Depends on the currency basis. Its FC rating is BB (not investment grade, E05 A-row ending none), but its LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. E14's rating was BBB+ from 2024-09-30 to 2025-11-20 (A36), which covers 1 June 2025.

**Q12.** A-. E14's rating was A- from 2023-01-15 to 2024-09-30 (A34), which covers 1 January 2024.

**Q13.** 1. The only downgrade is A- to BBB+ on 2024-09-30 (A36); later rows (A35, A33) keep BBB+.

**Q14.** None. E12's first rating (BB-, A30) starts 2024-02-01, after 1 January 2024.

**Q15.** A-. E10's rating was A- from 2023-05-01 to 2026-04-15 (A26), which covers 1 January 2026.

**Q16.** No. The rating stayed BBB+ through 2025 and 2026 (A35, A33); only the watch and outlook/action flags changed. This assumes "changed" means the rating symbol.

**Q17.** No. E06's rating stayed A- (A16, then A17 with RWN from 2026-09-03), with no lower rating recorded.

**Q18.** E06. It is the only entity with watch RWN on 1 October 2026 (A17, from 2026-09-03). E14's RWN (A35) ended on 2026-05-01.

**Q19.** E01 and E09. Both have current NEG outlooks (A03 from 2026-02-10 and A25 from 2026-03-01).

**Q20.** No. E07's rating moved to WD (A19), which is a withdrawal, and no default rating is recorded.

**Q21.** E07. Its rating was withdrawn (A19), and no current issuer rating is recorded for it on 1 October 2026.

**Q22.** E08. It is the only entity with an RD (default) rating (A22).

**Q23.** F2. This is E01's current short-term rating (A04, from 2026-02-10).

**Q24.** Yes. E01's current FC issuer rating is BBB (A02, A03), which is investment grade.

**Q25.** 5. The current investment-grade instrument ratings are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-); I02 and I04 are below investment grade and I08 has no rating.

**Q26.** A+. E15's local-currency rating is A+ (A40), in force since 2024-03-01.

**Q27.** A-. I06 is rated A- (A42), in force since 2024-03-01.

**Q28.** BBB+. CV's FC rating is BBB+ (action A38), in force since 2024-01-01.

**Q29.** None. VD has no ratings in the data.

**Q30.** E05 and E15. Their FC ratings equal their country ceilings: E05 is BB against the VD ceiling of BB, and E15 is A against the CV ceiling of A.

**Q31.** No. The two companies in ceiling-capped countries (E05, E15) sit exactly at their ceilings, not above.

**Q32.** E09. Halden Leasing's ultimate_parent_id is E09 (Halden Group plc), two levels up via E10.

**Q33.** E10, rated BBB+. I05 (Halden Leasing 2.90% 2028) has credit_risk_of E10, and its current rating is BBB+ (A29).

**Q34.** No. E12 (Halden Foods) has no parent or ultimate parent in the data, and E10's group is E09, E10 and E11.

**Q35.** 3. The Halden group is E09 (parent), E10 and E11; E17 was merged into E10 and is not a separate entity.

**Q36.** 2. The Northwind group is E02 (parent) and E04; E03 was merged into E02.

**Q37.** 16 entity records. This counts the two sovereigns (CV and VD, type SOV); excluding them gives 14 companies and banks.

**Q38.** No. They have different entity IDs, LEIs, countries (DE and US) and no parent link.

**Q39.** A. E02's current rating is A (A09), with a positive outlook.

**Q40.** 5. The GB issuers with a current issuer rating are E01, E02, E09, E12 and E14; E07 (also GB) is withdrawn.

**Q41.** None. "Brindle Capital" does not appear in the data.

**Q42.** LU. Halden Bank (E10) is domiciled in Luxembourg.

**Q43.** 1. E10 is the only entity with country LU.

**Q44.** Yes. I07 has local_currency = yes (currency XVD).

**Q45.** Depends. Its rating BBB- (A45) is numerically above VD's ceiling of BB, but the ceiling is an FC limit and I07 is a local-currency obligation.

**Q46.** No. E11 (Halden Leasing) has no LTIDR rating in the data; only its parent E10 is rated.

**Q47.** None. I08 has no rating record.

**Q48.** 7. I01 through I07 hold ratings on 1 October 2026; I08 does not.

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
  "Q45": {"above_ceiling": "depends"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```