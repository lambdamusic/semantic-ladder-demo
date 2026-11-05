**Q1.** A-. E01's last action before that date was A01 (assigned A- on 2024-03-12), and A02 came later.

**Q2.** No. E01's only 2026 actions are A03 and A04, both affirmations (BBB with Negative outlook, and F2). The downgrade was A02 in 2025.

**Q3.** No. I02 was downgraded to BB+ (A07), which is sub-investment grade.

**Q4.** Positive. E02 and E03 share one LEI, so I treat them as the same entity. The latest action is A09 (2025-09-15, Positive).

**Q5.** E02, rated A. I03 is issued by E04 and guaranteed by E02, and its rating (A10/A11) matches E02's A (A08/A09).

**Q6.** The data does not state a reason. E05 is rated BBB- in local currency (A13) and BB in foreign currency (A14). VD's Country Ceiling record is BB (A12), which is consistent with a ceiling effect, but nothing says so explicitly.

**Q7.** E08, E10 and E16. They were downgraded in A21/A22, A27 and A44. I05 was also downgraded, but it is an instrument, not an issuer.

**Q8.** E08. It was rated RD on 2026-07-08 (A22) and there is no later action.

**Q9.** 13. These are E01, E02 (E03 counted once), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. I excluded E07 (withdrawn, A19) and VD, which has only a Country Ceiling record. E11's CO-type rating is not clearly an issuer rating, so I excluded it too.

**Q10.** Depends. E05 is BBB- in local currency (investment grade) and BB in foreign currency (not investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the watch in A35 came later.

**Q12.** A-. This is from A34 (2023-01-15).

**Q13.** 1, from A36.

**Q14.** None. E12's first rating is A30, dated 2024-02-01.

**Q15.** A-. E10 was assigned A- in A26 and not downgraded until A27 (2026-04-15). E17 is a same-LEI duplicate with no ratings.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is BBB+ now (A33). The watch in A35 was resolved by an affirmation.

**Q17.** No. E06's only 2026 action is A17, which placed it on Rating Watch Negative at A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06 (A17). E14's watch (A35) was resolved by A33.

**Q19.** E01 and E09 (A03, A25). E06 is on watch, with no outlook recorded.

**Q20.** No. A19 is a withdrawal ("commercial reasons"), not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, from A22 (RD).

**Q23.** F2, from A04.

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5: I01, I03, I05, I06 and I07. I08's "EX" action is undefined in the data, so I did not count it.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** None. VD has only a Country Ceiling record (BB, A12), which is not an issuer rating.

**Q30.** E05 (FC BB, A14) and E15 (FC A, A41). They match the BB ceiling for VD (A12) and the A ceiling for CV (A37).

**Q31.** No. E05's FC rating equals the ceiling, and no other company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, and E10 was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent link to the E09/E10/E11 group, and only the shared "Halden" name suggests otherwise.

**Q35.** 3: E09, E10 and E11. E17 is a same-LEI duplicate of E10.

**Q36.** 2: E02 and E04. E03 duplicates E02.

**Q37.** 17. There are 19 entity records, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs (E06 and E13) and different countries.

**Q39.** A, from A08/A09.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 is withdrawn.

**Q41.** BB+, from A44. The source system for E16 is "QA", so the record may be less reliable.

**Q42.** DE (E10). The duplicate record E17 says LU, so the data conflicts.

**Q43.** 1, but this is uncertain. E17 is the only LU record, and it duplicates E10, which is recorded as DE.

**Q44.** Yes, by inference. I07 is in "XVD" and its BBB- matches E05's local-currency rating (A13), but the data does not define XVD.

**Q45.** No. I07's BBB- is above VD's BB ceiling (A12), but the ceiling constrains foreign-currency ratings, not a local-currency note.

**Q46.** No. E11's only rating is a CO-type rating (A46), not an issuer rating.

**Q47.** None. I08's only action is "EX" (A47), which the data does not define, so I cannot treat it as an assigned rating.

**Q48.** 7: I01 to I07. I08 is excluded for the reason in Q47.

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
"Q43": {"count": 1},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```