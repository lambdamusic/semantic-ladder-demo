**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action for E01 was A02 on 2025-06-20.

**Q2.** No. E01's only 2026 action is A03 (affirmed BBB, 2026-02-10), and its downgrade was A02 in 2025.

**Q3.** No. I02 is rated BB+ (A07, downgraded 2025-06-20), which is below investment grade.

**Q4.** Positive. E03 and E02 share LEI 213800PHEIYNJMHTDV74, so I treat them as one entity. The latest outlook is A09 (2025-09-15, Positive), which follows A08 (Stable).

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes the guarantor's risk. I03 is A (A11) and E02's issuer rating is A (A08, A09).

**Q6.** The data states no reason. It does show E05 with foreign-currency BB (A14) and local-currency BBB- (A13). The Valdoria country ceiling is BB (A12), which is consistent with a ceiling effect, but that is my inference.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44). I05's downgrade (A29) is on the instrument, so I did not count its issuer E11.

**Q8.** E08. A22 moved it to RD on 2026-07-08 and nothing later changes that.

**Q9.** 13. These are E01, E02/E03 (one entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV, each holding a long-term IDR. E07 was withdrawn (A19), VD has only a country ceiling, and E11 has only a type-CO rating.

**Q10.** Depends. E05's foreign-currency rating is BB (non-investment grade, A14) and its local-currency rating is BBB- (investment grade, A13).

**Q11.** BBB+. E14 was downgraded to BBB+ on 2024-09-30 (A36), and the next action was on 2025-11-20.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade for E14.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- on 2023-05-01 (A26) and downgraded on 2026-04-15 (A27). E17 shares its LEI but has no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A35 put it on watch, A33 affirmed).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch Negative at A-. Orrin Bancorp (E13) is a different entity, with a different LEI and country.

**Q18.** E06 (A17, 2026-09-03). E14's earlier watch (A35) was followed by an affirmation (A33).

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07 was assigned BB (A18) and then withdrawn for commercial reasons (A19), with no default rating.

**Q21.** E07, whose rating was withdrawn on 2026-05-12 (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04, affirmed 2026-02-10).

**Q24.** Yes. E01's long-term IDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 (BB+) and I04 (BB) are non-investment grade. I08's last action is EX (A47), which I read as expired.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 (foreign-currency BB, A14) and E15 (foreign-currency A, A41). These sit at the VD ceiling of BB (A12) and the CV ceiling of A (A37).

**Q31.** No. E05 and E15 are at their ceilings, not above them (A14, A41).

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose current rating is BBB+ (A27). I05 itself is also BBB+ (A29).

**Q34.** No. The data has no parent or group link between E12 and E10 or E09. The shared "Halden" name is not evidence.

**Q35.** 3: E09, E10 and E11. E17 duplicates E10 by LEI.

**Q36.** 2: E02 and E04. E03 duplicates E02 by LEI.

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs (549300AMVE3VRVG7HK43 and 815600O8X8K2F154N214) and different countries (DE and US).

**Q39.** A (A09, affirmed 2025-09-15).

**Q40.** 6: E01, E02/E03, E09, E12, E14 and E16. E07 is excluded because it was withdrawn.

**Q41.** BB+ (A44). The only source for E16 is "QA".

**Q42.** DE. E10 "Halden Bank AG" is DE from the RATINGS source. E17 "HALDEN BANK" has the same LEI but says LU from RESEARCH, so the data conflicts. I used the RATINGS record.

**Q43.** 0. The only LU record is E17, which duplicates E10 (DE). If you trust the E17 record, the answer would be 1.

**Q44.** Yes, by inference. I07 is in XVD, which looks like Valdoria's currency, and its BBB- matches E05's local-currency rating (A13). The data does not state the local currency explicitly.

**Q45.** No. The BB ceiling (A12) constrains foreign-currency ratings, and I07 is a local-currency note.

**Q46.** No. E11 only has a type-CO rating (A46, BBB), not a long-term IDR.

**Q47.** None. I08's only record is an EX action (A47, 2026-09-01), which I read as the rating having expired, so there is no current rating.

**Q48.** 7: I01 to I07. I08 is excluded because its rating expired (A47).

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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