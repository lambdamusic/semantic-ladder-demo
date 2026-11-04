**Q1.** A-. E01's last action before 2025-01-01 was A01 (assigned A-, 2024-03-12); the downgrade to BBB (A02) came in June 2025.

**Q2.** No. E01's only 2026 actions are affirmations at BBB (A03, A04), with the outlook moved to Negative.

**Q3.** No, it is rated BB+. I02 was downgraded to BB+ on 2025-06-20 (A07), which is below investment grade.

**Q4.** Positive. E03 shares E02's LEI, so it is the same entity, and its latest action (A09, 2025-09-15) affirmed A with a POS outlook.

**Q5.** The guarantor, E02, rated A. I03 is issued by E04 but guaranteed by E02 (A08/A09), and I03 itself is rated A (A11).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps E05's foreign-currency rating at BB (A14). Its local-currency rating is BBB- (A13).

**Q7.** E08, E10 and E16. Their 2026 downgrades are A21/A22, A27 and A44. A17 for E06 is only a watch, not a downgrade.

**Q8.** E08. It was downgraded to RD on 2026-07-08 (A22) and has no later action.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, E15, E16 and CV. E07 is withdrawn (A19). VD has only a Country Ceiling, and E11 has only a "CO" record, which the data does not define. I did not count either as an issuer rating.

**Q10.** Depends. E05's local-currency rating is BBB- (investment grade, A13) but its foreign-currency rating is BB (not investment grade, A14).

**Q11.** BBB+. E14 was downgraded from A- to BBB+ on 2024-09-30 (A36), and the later actions A35 and A33 kept BBB+.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating was A30 on 2024-02-01.

**Q15.** A-. E10 was rated A- (A26) until the downgrade to BBB+ on 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33). A35 put it on watch in November 2025, but A33 later affirmed it with no watch.

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative with the rating unchanged at A-.

**Q18.** E06 (A17). E14's watch (A35) was resolved by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 had a rating withdrawn for commercial reasons (A19) and has no default rating.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's action code "EX" is not defined, so I did not count it.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to VD's ceiling of BB (A12, A14). E15's is A, equal to CV's ceiling of A (A37, A41).

**Q31.** No. E05 and E15 are at their ceilings, not above them, and no other country has a ceiling in the data.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, rated BBB+. E10 guarantees I05 (A29), and its rating was cut to BBB+ in A27.

**Q34.** No. The data links E12 to no parent or group, and the shared "Halden" name does not establish membership.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 and E04. E03 duplicates E02 by LEI.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs, countries (DE and US) and entity IDs.

**Q39.** A (A08, affirmed in A09).

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44).

**Q42.** DE. E10 in the RATINGS source says DE. The LU on E17 comes from a RESEARCH duplicate record.

**Q43.** 0. The only LU record is E17, a duplicate of E10, which is domiciled in DE.

**Q44.** Yes. The currency code XVD appears to be Valdoria's own currency, which the data does not define, and I07's BBB- matches E05's local-currency rating (A13, A45).

**Q45.** No. I07 is BBB-, and the BB ceiling (A12) caps foreign-currency ratings, not local-currency obligations.

**Q46.** No. E11 has only a "CO" record (A46), which the data does not define as an issuer rating. Its notes rely on E10's guarantee.

**Q47.** None. I08's only action (A47) uses the undefined code "EX", so I can't confirm a held rating. If it is a rating, it is shown as A.

**Q48.** 7: I01 to I07. I08 is excluded for the reason given in Q47.

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

**Q6.** Answered above in prose; it has no JSON field.