**Q1.** A-. A01 (2024-03-12) assigned A-, and the next action, A02, came on 2025-06-20.

**Q2.** No. Kestrel's only 2026 actions are the affirmations A03 and A04. Its downgrade, A02, was in 2025.

**Q3.** No, it is rated BB+. I02 was downgraded to BB+ in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and the latest action, A09 (2025-09-15), carries a POS outlook.

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, and E02's rating is A (A08, A09 on the duplicate record E03).

**Q6.** The data gives no explanation. It only shows that the FC rating of BB (A14) equals Valdoria's country ceiling of BB (A12), while the LC rating is BBB- (A13).

**Q7.** E08, E10 and E16 were downgraded in 2026 (A21 and A22, A27, A44). Instrument downgrades such as A29 are not issuer downgrades.

**Q8.** E08 was in default on 1 October 2026. A22 put it at RD on 2026-07-08, with no later action.

**Q9.** 13. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. I excluded E07 (withdrawn in A19), E11 (only a CO record), and VD (only a country-ceiling record).

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13) and the foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 (2024-09-30) downgraded Marlow to BBB+, and A35 (2025-11-20) came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade.

**Q14.** None. Halden Foods' first rating is A30, dated 2024-02-01.

**Q15.** A-. E10 was rated A- in A26, and E17 is the same entity by LEI. The downgrade in A27 came in April 2026.

**Q16.** No. The rating was BBB+ throughout, and only a watch and an affirmation occurred (A35, A33).

**Q17.** No. The only 2026 action for E06 is A17, a Rating Watch Negative placement with the rating unchanged at A-.

**Q18.** E06 only (A17). E14's watch from A35 was resolved by the affirmation in A33, which carries no watch.

**Q19.** E01 and E09 (A03, A25).

**Q20.** No. E07's latest action is a withdrawal (A19), and there is no default rating.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which was rated RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03), which is investment grade.

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a country-ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. Their FC ratings (BB, A) equal the ceilings of VD (BB, A12) and CV (A, A37).

**Q31.** No. No FC rating exceeds its country ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. E10 guarantees I05, and A27 downgraded it to BBB+.

**Q34.** No. E12 has no parent, while E10 belongs to E09's group.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries and names.

**Q39.** A (A09 on the duplicate record E03, with A08 on E02).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE and the RESEARCH duplicate E17 says LU, so the sources conflict. I took the RATINGS record.

**Q43.** 0. The only LU record, E17, duplicates E10, which is domiciled in DE.

**Q44.** Yes, probably. XVD is not defined anywhere in the data. I read it as Valdoria's currency because it is the only non-major currency code and the issuer is in VD.

**Q45.** No. I07 is rated BBB-, matching the LC rating (A13), and the BB ceiling applies to foreign-currency ratings.

**Q46.** No. E11 has only a CO record (A46), not an issuer rating.

**Q47.** None. I08's rating expired on 2026-09-01 (A47).

**Q48.** 7, I01 through I07. I08 had expired (A47).

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