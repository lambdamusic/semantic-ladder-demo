**Q1.** A-. E01's LTIDR was assigned A- on 2024-03-12 (A01), and the next action is the 2025-06-20 downgrade (A02).

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04), and the rating stayed BBB.

**Q3.** No. I02 is rated BB+ after the 2025-06-20 downgrade (A07), which is below investment grade.

**Q4.** Positive. E03 is a duplicate record of E02 (same LEI), and its latest action is A09 (2025-09-15, POS).

**Q5.** The holder takes the credit risk of E02, rated A. I03 is issued by E04 but guaranteed by E02 (A08, A09).

**Q6.** The data gives no stated reason; the action comments are empty. The pattern fits a country ceiling: VD's ceiling is BB (A12), and E05's foreign-currency rating is BB (A14), against BBB- in local currency (A13).

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21/A22, A27, A44). E06's A17 is a watch placement, not a downgrade.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) and has no later action.

**Q9.** 13. These are E01, E02 (merged with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19), and VD has only a country ceiling (A12). E11's CO-type rating (A46) is not clearly an issuer rating, so I did not count it.

**Q10.** Depends. E05's local-currency rating of BBB- is investment grade (A13), but its foreign-currency rating of BB is not (A14).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36).

**Q12.** A-. E14 was assigned A- on 2023-01-15 (A34), before the downgrade.

**Q13.** 1. E14 has a single downgrade, A36.

**Q14.** None. E12's first rating came on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26), and the downgrade did not come until 2026-04-15 (A27). E17 is a duplicate of E10.

**Q16.** No. E14 was BBB+ on 2025-01-01 and still is (A36, A33). The watch in A35 was later resolved.

**Q17.** No. E06's only 2026 action is a Rating Watch Negative placement at A- (A17).

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's 2025 watch (A35) was superseded by the affirmation without a watch (A33).

**Q19.** E01 and E09 (A03, A25). E06's A17 carries no outlook, and its last stated outlook was Stable (A16).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08 (RD, A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are below investment grade, and I08 expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12), which is not an issuer rating.

**Q30.** E05 (BB, A14, against VD's ceiling of BB) and E15 (A, A41, against CV's ceiling of A).

**Q31.** No. The only ceilings in the data are VD (BB) and CV (A), and E05 and E15 are exactly at them, not above.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10, the guarantor, rated BBB+ (A27). I05 is issued by E11 and guaranteed by E10.

**Q34.** No. E12 has no parent and is not linked to E09 in the data.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and no link in the data.

**Q39.** A (A09 affirmed it, and A08 assigned it originally).

**Q40.** 6: E01, E02, E09, E12, E14 and E16.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU. I treated the RATINGS record as authoritative, which is a judgement call.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record is DE.

**Q44.** Yes. I07 is denominated in XVD, which appears to be Valdoria's currency, though the data has no currency table to confirm it.

**Q45.** No. I07 is rated BBB- (A45), and the BB ceiling applies to foreign-currency ratings, not local-currency ones.

**Q46.** No. E11 has only a CO-type rating (A46), not an issuer rating.

**Q47.** None. I08 was marked EX (expired) on 2026-09-01 (A47).

**Q48.** 7: I01 to I07. I08 expired.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "POS"},
"Q5": {"risk_of": "E02", "rating": "A"},
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
"Q37": {"count": 17},
"Q38": {"same": "no"},
"Q39": {"rating": "A"},
"Q40": {"count": 6},
"Q41": {"rating": "BB+"},
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```