**Q1.** A-. The FC issuer rating was A- from A01 (2024-03-12) until the downgrade to BBB in A02 (2025-06-20).

**Q2.** No. E01's 2026 actions are affirmations (A03 BBB NEG, A04 F2).

**Q3.** No, BB+. I02 was BBB (A23) and was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. The latest outlook is POS from A09 (2025-09-15), recorded under E03, which shares E02's LEI and is treated as the same entity.

**Q5.** E04 (Northwind Finance BV), guaranteed by E02. Instrument I03 is rated A (A10, A11).

**Q6.** The data doesn't give a reason. The FC rating of BB (A14) equals Valdoria's country ceiling of BB (A12), which may explain the cap, but no record says so. (Q6 has no JSON field.)

**Q7.** E08 (A21, A22), E10 (A27), E16 (A44).

**Q8.** E08, in restricted default (RD) since A22 (2026-07-08), with no later action.

**Q9.** 13: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15, E16. E07 was withdrawn (A19), E04, E11 and VD have no LTIDR, and E03 and E17 are duplicates.

**Q10.** Depends. The FC rating is BB (A14), below investment grade, and the LC rating is BBB- (A13), which is investment grade.

**Q11.** BBB+. A36 (2024-09-30) set BBB+, and the watch placement in A35 (2025-11-20) came later without changing the rating.

**Q12.** A-. A34 (2023-01-15) set A-, and the downgrade in A36 came after 1 Jan 2024.

**Q13.** 1. A36 (2024-09-30) is the only downgrade. A35 is a watch placement.

**Q14.** None. E12's first action, A30, is dated 2024-02-01, after 1 Jan 2024.

**Q15.** A-. E10's A- (A26, 2023-05-01) stood until the downgrade to BBB+ in A27 (2026-04-15).

**Q16.** No. The rating stayed BBB+ (A36, A33). The watch in A35 was cleared by the affirmation in A33.

**Q17.** No. E06's only 2026 action is a watch placement (A17, 2026-09-03), not a downgrade.

**Q18.** E06 (A17). The watch was still open on 1 Oct 2026.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's last action is a withdrawal for commercial reasons (A19), not a default.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08 only, from the RD action in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating of BBB (A03) is investment grade on the standard scale, which the data doesn't define.

**Q25.** 6: I01, I03, I05, I06, I07, I08. I08's action is EX (A47), which the data doesn't define. Excluding it gives 5.

**Q26.** A+ (A40, local currency).

**Q27.** A- (A42).

**Q28.** BBB+ (A38, FC).

**Q29.** None. VD has only a CC record (A12, BB) and no LTIDR.

**Q30.** E05 (FC BB, A14) and E15 (FC A, A41), each exactly at its country's ceiling (VD BB in A12, CV A in A37).

**Q31.** No. Only VD and CV have ceilings in the data, and E05 and E15 sit at them, not above. Other countries have no ceiling data, so they can't be checked.

**Q32.** E09 (Halden Group plc), through E10.

**Q33.** E11 (Halden Leasing SA), guaranteed by E10. Instrument I05 is rated BBB+ (A29).

**Q34.** No. E12 has no parent_id, and sharing the name "Halden" doesn't establish group membership.

**Q35.** 3: E09, E10, E11.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10.

**Q38.** No. The LEIs and countries differ (E06 is DE, E13 is US).

**Q39.** A (A08, affirmed in A09).

**Q40.** 6: E01, E02, E09, E12, E14, E16.

**Q41.** BB+ (A44, 2026-06-01).

**Q42.** DE, from E10. E17 gives LU for the same LEI, so the records conflict.

**Q43.** 0. E17 is the only LU record and shares E10's LEI, which is domiciled in DE. Taking E17's country at face value gives 1.

**Q44.** Depends. I07 is denominated in XVD, which the data doesn't define. Its BBB- rating matches Valdoria's local-currency rating (A13).

**Q45.** Depends. BBB- (A45) is above the BB ceiling (A12), but a ceiling applies to foreign-currency obligations, and XVD's currency basis isn't defined.

**Q46.** No. E11 has only a CO record (A46), which isn't an issuer rating type. CO is undefined, so this is an interpretation.

**Q47.** A (A47). The action is EX, which is undefined.

**Q48.** 8. Every instrument, I01 through I08, has a rating record in effect on 1 Oct 2026.

**Assumptions:** CC is treated as the country ceiling, as Q45 implies. LTIDR and STIDR are issuer ratings. Investment grade means BBB- and above, which the data doesn't define. CO, EX and XVD are undefined in the data.

```json
{"Q1": {"rating": "A-"},
 "Q2": {"downgraded": "no"},
 "Q3": {"investment_grade": "no", "rating": "BB+"},
 "Q4": {"outlook": "POS"},
 "Q5": {"risk_of": "E04", "rating": "A"},
 "Q7": {"issuers": ["E08", "E10", "E16"]},
 "Q8": {"entities": ["E08"]},
 "Q9": {"count": 13},
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
 "Q33": {"risk_of": "E11", "rating": "BBB+"},
 "Q34": {"same_group": "no"},
 "Q35": {"count": 3},
 "Q36": {"count": 2},
 "Q37": {"count": 17},
 "Q38": {"same": "no"},
 "Q39": {"rating": "A"},
 "Q40": {"count": 6},
 "Q41": {"rating": "BB+"},
 "Q42": {"country": "DE"},
 "Q43": {"count": 0},
 "Q44": {"local_currency": "depends"},
 "Q45": {"above_ceiling": "depends"},
 "Q46": {"issuer_rating": "no"},
 "Q47": {"rating": "A"},
 "Q48": {"count": 8}}
```