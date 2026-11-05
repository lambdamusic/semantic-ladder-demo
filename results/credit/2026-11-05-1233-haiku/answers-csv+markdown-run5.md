**Q1.** A-. The latest action on or before 1 Jan 2025 is A01 (assigned A-, 2024-03-12); A02 (downgrade to BBB) came later.

**Q2.** No. The 2026 actions on E01 are A03 (affirmed BBB, Negative outlook) and A04 (affirmed F2), neither a downgrade.

**Q3.** No, rating BB+. I02 was downgraded from BBB to BB+ on 2025-06-20 (A07), and BB+ is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) set the outlook to POS.

**Q5.** The credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, so it is rated on the guarantor (A10, A11).

**Q6.** The foreign-currency rating is capped by the Republic of Valdoria's Country Ceiling of BB (A12), while the local-currency rating of BBB- (A13) is not capped. (Q6 has no JSON field in the spec.)

**Q7.** E08 and E10. E08 was downgraded to CCC (A21) and then RD (A22), and E10 was downgraded to BBB+ (A27). I05 was also downgraded, but that is an instrument action, not an issuer.

**Q8.** E08. A22 (2026-07-08) set RD, a default, and it held on 1 Oct 2026.

**Q9.** 12. These entities hold an issuer rating on 1 Oct 2026: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E11 has only a credit opinion (A46), and VD has only a Country Ceiling (A12).

**Q10.** No. Its headline foreign-currency rating is BB (A14); only its local-currency rating, BBB- (A13), is investment grade.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and the next action (A35) came in 2025-11.

**Q12.** A-. A34 (2023-01-15) assigned E14 A-, and no action on E14 precedes 1 Jan 2024 except that one.

**Q13.** 1. A36 (2024-09-30) is the only downgrade on E14.

**Q14.** None. The first rating on E12 is A30 (BB-, 2024-02-01), which is after 1 Jan 2024.

**Q15.** A-. E10 (also recorded as E17) was assigned A- by A26 (2023-05-01), and its next action, A27, came in 2026-04.

**Q16.** No. The rating was BBB+ from 2024-09-30 (A36) and was affirmed or placed on Watch without change in A35 and A33.

**Q17.** No. The only 2026 action on E06 is A17 (2026-09-03), a Rating Watch placement, which is not a downgrade.

**Q18.** E06. A17 placed it on Rating Watch Negative, and no later action changes that. E14's Watch from A35 was cleared when A33 (2026-05-01) left the watch field blank.

**Q19.** E01 and E09. Each has an outlook of NEG, from A03 (2026-02-10) and A25 (2026-03-01) respectively.

**Q20.** No. E07 had its rating withdrawn (A19), and a withdrawal is not a default.

**Q21.** E07. It had a rating (A18) and then a withdrawal (A19). E11 never had an issuer rating, since its CO (A46) is not one.

**Q22.** E08. It is the only entity with an RD rating (A22).

**Q23.** F2. A04 (2026-02-10) set Kestrel's short-term rating to F2.

**Q24.** Yes. Its long-term issuer rating is BBB (A03), which is investment grade.

**Q25.** 5. On 1 Oct 2026 the investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are BB+ and BB, and I08 is only an expected rating (EX).

**Q26.** A+. A40 (2024-03-01) assigned E15 a local-currency rating of A+.

**Q27.** A-. I06 was assigned A- by A42 (2024-03-01).

**Q28.** BBB+. A38 sets the sovereign's foreign-currency issuer rating at BBB+. Its A is the Country Ceiling (A37), not its rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not a sovereign issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals Valdoria's ceiling of BB, and E15's foreign-currency rating of A equals Corvenia's ceiling of A (A37).

**Q31.** No. E05 (BB) and E15 (A) are exactly at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, and E10's parent is E09 (Halden Group plc).

**Q33.** The credit risk of E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, so it takes that rating (A29).

**Q34.** No. E12 has no parent link, and it shares no parent with E09 or E10.

**Q35.** 3. The Halden group is E09, E10 (which includes E17, the same LEI) and E11.

**Q36.** 2. The Northwind group is E02 (which includes E03, the same LEI) and E04.

**Q37.** 16. There are 19 records, which reduce to 17 distinct entities after merging E03 into E02 and E17 into E10. Excluding the QA record E16 leaves 16.

**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214), so they are different entities.

**Q39.** A. A09 (2025-09-15) affirmed E02 at A.

**Q40.** 5. The GB issuers holding an issuer rating are E01, E02 (with E03), E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, and QA records must be ignored.

**Q42.** LU. RESEARCH (E17) holds for domicile, and it records LU, not DE.

**Q43.** 1. Only Halden Bank (E10/E17) is domiciled in LU.

**Q44.** Yes. The note is denominated in XVD, Valdoria's domestic currency, and E05 is domiciled in VD.

**Q45.** No. Local-currency debt is not subject to the Country Ceiling.

**Q46.** No. Its only rating record is a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an expected rating (EX, A47), which is not yet an assigned rating.

**Q48.** 7. Eight instruments exist, and only I08 is unrated, since its EX action is not a rating.

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
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": 7}
}
```