**Q1.** A-. E01's long-term foreign-currency rating was A- from A01 (2024-03-12) until A02 (2025-06-20).

**Q2.** No. E01's only 2026 action is A03, an affirmation at BBB; the downgrade was A02 in 2025.

**Q3.** No. The 2031 note (I02) was downgraded to BB+ in A07 (2025-06-20), which is below investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so they are the same entity. The latest record is A09 (2025-09-15, Positive).

**Q5.** The guarantor, Northwind Holdings (E02, the same entity as E03), rated A. I03 is issued by E04 but guaranteed by E02, and A09 gives E02 an A rating.

**Q6.** The data doesn't say why. E05 is BB in foreign currency (A14) and BBB- in local currency (A13), and the sovereign VD's country ceiling is BB (A12). That fits a ceiling effect, but no record states it as the reason.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 downgraded the instrument I05, not an issuer.

**Q8.** E08. A22 moved it to RD on 2026-07-08, with no later action.

**Q9.** 12. These are E01, E02/E03 (counted once), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. I excluded E07 (withdrawn, A19) and VD, which has only a country ceiling (A12).

**Q10.** Depends. E05's foreign-currency rating is BB (A14), which is not investment grade, and its local-currency rating is BBB- (A13), which is.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 (2025-11-20) comes later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36 (2024-09-30).

**Q14.** Not rated. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. A26 set it on 2023-05-01, and the downgrade A27 only came on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33). A35 only added Rating Watch Negative, and A33 later affirmed the rating.

**Q17.** No. E06's only 2026 action is A17, which put it on Rating Watch Negative while keeping A-. Orrin Bancorp (E13) is a different entity.

**Q18.** E06, from A17 (2026-09-03). E14's earlier watch (A35) was followed by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25). E06 is on watch and has no outlook.

**Q20.** No. E07 was withdrawn (A19, WD, "commercial reasons"), and there is no default rating.

**Q21.** E07, withdrawn by A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 4. On 2026-10-01 the instruments rated BBB or better are I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-). I02 (BB+) and I04 (BB) are not.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. The A in A37 is the country ceiling, not an issuer rating.

**Q29.** It has no issuer rating. VD has only a country ceiling of BB (A12).

**Q30.** E05 and E15. Each sits exactly at its country's ceiling: E05 is BB against VD's BB (A14, A12), and E15 is A against CV's A (A41, A37).

**Q31.** No. Only VD and CV have ceilings, and no company exceeds them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The guarantor, Halden Bank (E10), rated BBB+. I05 is issued by E11 but guaranteed by E10, and A27 rates E10 at BBB+.

**Q34.** No. E12 has no parent or other link to E09/E10, and shares only the "Halden" name.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02/E03 (one entity) and E04.

**Q37.** 16. There are 17 entity records, but E02 and E03 share an LEI, so they count as one.

**Q38.** No. They have different LEIs, countries (DE and US) and entity IDs (E06 and E13).

**Q39.** A, from A09 (2025-09-15).

**Q40.** 5: E01, E02/E03, E09, E12 and E14. E07 was withdrawn.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
"Q5": {"risk_of": "E02", "rating": "A"},
"Q7": {"issuers": ["E08", "E10"]},
"Q8": {"entities": ["E08"]},
"Q9": {"count": 12},
"Q10": {"investment_grade": "depends"},
"Q11": {"rating": "BBB+"},
"Q12": {"rating": "A-"},
"Q13": {"count": 1},
"Q14": {"rating": "NR"},
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
"Q25": {"count": 4},
"Q26": {"rating": "A+"},
"Q27": {"rating": "A-"},
"Q28": {"rating": "BBB+"},
"Q29": {"rating": "NR"},
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
"Q40": {"count": 5}
}
```