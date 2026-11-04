**Q1.** A- (A01, 2024-03-12). The next action, A02 (DG to BBB), is dated 2025-06-20, after the query date.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No. BB+ is the current rating (A07, DG, 2025-06-20, replacing A23's BBB), which is below BBB-.

**Q4.** Positive (POS). E02 and E03 are the same entity (same LEI), and the latest action, A09 (AF, 2025-09-15), sets the outlook to POS.

**Q5.** E02 (Northwind Holdings). The notes (I03) are issued by E04 but guaranteed by E02, so holders take E02's risk. The rating is A (A11, AF, 2025-09-15).

**Q6.** Valdoria Telecom's foreign-currency rating (BB, A14) is capped at the Valdorian Country Ceiling (BB, A12). The local-currency rating (BBB-, A13) is not subject to the ceiling.

**Q7.** E08 (A21, A22) and E10 (A27). I05 was also downgraded in 2026 (A29), but it is an instrument, and E16 (A44) is QA data.

**Q8.** E08. Its latest action, A22 (2026-07-08), is RD (restricted default).

**Q9.** 12. These are E01, E02/E03, E05, E06, E08, E09, E10/E17, E12, E13, E14, CV and E15. E07 was withdrawn (A19), E11 has only a credit opinion (CO), VD has only a Country Ceiling, and E16 is QA.

**Q10.** No. The headline rating is the FC rating, BB (A14), which is below investment grade. The LC rating, BBB- (A13), would be investment grade, so this depends on which rating you mean.

**Q11.** BBB+. The latest action on or before the date is A36 (DG, 2024-09-30).

**Q12.** A-. The rating is A34 (AS, 2023-01-15).

**Q13.** 1. Only A36 is a downgrade. A35 is a Rating Watch placement, which is not a downgrade.

**Q14.** None. Halden Foods' first action, A30 (AS, BB-), is dated 2024-02-01, after 2024-01-01.

**Q15.** A-. E10 (and E17, same LEI) was assigned A- (A26) and only downgraded to BBB+ on 2026-04-15 (A27).

**Q16.** No. The rating was BBB+ on 2025-01-01 (A36), and the later actions (A35 Watch, A33 AF) left it at BBB+.

**Q17.** No. E06's only 2026 action, A17 (RW, 2026-09-03), is a Rating Watch placement, not a downgrade.

**Q18.** E06. A17 places it on Rating Watch Negative (RWN) with no later action. E14's watch (A35) appears resolved by the affirmation A33 (watch blank), which I've assumed means the watch was cleared.

**Q19.** E01 (A03, NEG) and E09 (A25, NEG).

**Q20.** No. E07 withdrew its rating (A19, WD), and withdrawal is not a default.

**Q21.** E07. It had a rating (A18) and was withdrawn (A19). E11 never had an issuer rating, and VD never had one.

**Q22.** E08. It is the only entity with an RD action (A22).

**Q23.** F2 (A04, AF, 2026-02-10, STIDR).

**Q24.** Yes. The current issuer rating is BBB (A03), which is investment grade.

**Q25.** 5. The instruments rated investment grade on 2026-10-01 are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 is BB+, I04 is BB, and I08 is only expected (EX), so unrated.

**Q26.** A+ (A40, LC).

**Q27.** A- (A42). I06 is the 2032 note.

**Q28.** BBB+ (A38, FC issuer rating). The CC action A37 (A) is the ceiling, not an issuer rating.

**Q29.** None. VD has only a Country Ceiling (A12, BB), which the ontology says is not the sovereign's issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A). CV's own FC rating is BBB+, which is not at its ceiling.

**Q31.** No. Ceilings exist only for VD and CV, and E05 and E15 are exactly at them. No other entity has a ceiling to exceed.

**Q32.** E09 (Halden Group plc). E11's parent is E10, whose parent is E09.

**Q33.** E10 (Halden Bank). I05 is guaranteed by E10, so holders take its risk. The instrument is rated BBB+ (A29), in line with E10's issuer rating.

**Q34.** No. E12 has no parent in the data, and its LEI differs from E10's.

**Q35.** 3: E09, E10 and E11 (E17 is a duplicate of E10).

**Q36.** 2: E02 and E04 (E03 is a duplicate of E02).

**Q37.** 16. The 19 records reduce to 16 after removing duplicates E03 (of E02) and E17 (of E10), and QA record E16.

**Q38.** No. E06 and E13 have different LEIs and countries.

**Q39.** A (A09, AF, 2025-09-15).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn, so it is excluded.

**Q41.** None. E16 is a QA record, so it must be ignored.

**Q42.** DE. The RATINGS record (E10) holds, and it overrides the RESEARCH record's LU (E17).

**Q43.** 0. The only LU record (E17) is a duplicate of E10, which is domiciled in DE per RATINGS.

**Q44.** Yes. I07 is denominated in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. I07 is local-currency debt, which the ontology says is not capped by the ceiling, even though its BBB- rating is above the BB ceiling.

**Q46.** No. E11 has only a credit opinion (A46, CO), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (A47, EX), and it stays unrated until an AS action confirms it.

**Q48.** 7: I01, I02, I03, I04, I05, I06 and I07. I08 is unrated.

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