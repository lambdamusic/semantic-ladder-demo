**Q1.** BBB+... correction: A-. Kestrel's rating on 1 Jan 2025 was A-, set by A01 (Mar 2024) and not changed until the downgrade in A02 (Jun 2025).

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04).

**Q3.** No. The 2031 note (I02) is rated BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 shares its LEI with E02 (the same entity), and A09 (Sep 2025) sets POS.

**Q5.** Northwind Holdings (E02), rated A. I03 is guaranteed by E02, so it carries the guarantor's risk, and E02's current rating is A (A08, A09).

**Q6.** Valdoria's Country Ceiling is BB (A12). It caps the FC rating (A14, BB), while the LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27 (E17 is the same entity). E16's downgrade (A44) is QA data and is ignored. A29 is an instrument action, not an issuer one.

**Q8.** E08. It was in default (RD) from A22.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08 (RD), E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn. E11 has only a credit opinion. VD has only a Country Ceiling. E04 has no rating of its own.

**Q10.** Depends. The LC rating is BBB- (investment grade, A13), but the FC rating is BB (speculative, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ in Sep 2024, and A35 on 2025-11-20 falls after the query date.

**Q12.** A-, from A34.

**Q13.** 1, from A36. The RW (A35) and the affirmation (A33) are not downgrades.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 (the same entity as E17) was rated A- from A26 until the downgrade on 2026-04-15.

**Q16.** No. It was BBB+ on 1 Jan 2025 and is still BBB+ (A33).

**Q17.** No. Orrin Bank AG (E06) only had a Rating Watch placed in 2026 (A17), and its rating stayed A-.

**Q18.** E06, from A17. E14's watch (A35) was cleared by the later affirmation A33, which carries no watch.

**Q19.** E01 (A03) and E09 (A25). E10's outlook is now STA (A27).

**Q20.** No. E07's rating was withdrawn (A19), which is not a default.

**Q21.** E07.

**Q22.** E08.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 only has an expected rating (EX).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The Country Ceiling (A37) is not the sovereign's rating.

**Q29.** None. VD only has a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC rating of BB equals the Valdoria ceiling of BB, and E15's FC rating of A equals the Corvenia ceiling of A.

**Q31.** No.

**Q32.** E09. The chain is E11 → E10 → E09.

**Q33.** Halden Bank (E10), rated BBB+. I05 is guaranteed by E10 and E10 was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent link to E09.

**Q35.** 3: E09, E10 (with E17) and E11.

**Q36.** 2: E02 (with E03) and E04.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is QA data.

**Q38.** No. They have different LEIs (E06 and E13).

**Q39.** A (A08, A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and E10 is domiciled in LU, not DE.

**Q41.** None. E16 is a QA record and is ignored.

**Q42.** LU. The RESEARCH record (E17) holds for country.

**Q43.** 1 (E10, which is also E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.

**Q45.** No. It is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 only has a credit opinion (A46), which is not a rating.

**Q47.** None. I08 only has an expected rating (A47, EX).

**Q48.** 7, which is I01 through I07.

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

**Correction to Q1:** the answer is A-. I started the line with "BBB+" by mistake. The JSON above has the right value.