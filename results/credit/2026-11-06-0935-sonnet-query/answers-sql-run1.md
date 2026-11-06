**Q1.** A-. Kestrel's LTIDR was A- from A01 (2024-03-12) until the downgrade to BBB in A02 on 2025-06-20.

**Q2.** No. In 2026 Kestrel only had affirmations (A03, A04), with the outlook moved to Negative.

**Q3.** No. The 2031 note (I02, subordinated) was cut to BB+ in A07, which is below investment grade.

**Q4.** Positive. E03 "NORTHWIND HLDGS" has the same LEI as E02, so I treated it as a duplicate record of the same entity. Its latest action, A09 (2025-09-15), affirmed A with a POS outlook, which is more recent than A08.

**Q5.** The holder takes the credit risk of E02, the guarantor of I03, which is rated A. The issuer is E04, but E02 guarantees the notes.

**Q6.** The data points to the Valdoria Country Ceiling (A12), which is BB. Valdoria Telecom's foreign-currency rating is BB (A14), while its local-currency rating is BBB- (A13). The data does not state the reason explicitly.

**Q7.** E08 (A21, A22), E10 (A27) and E16 (A44) were downgraded in 2026. E06's action (A17) was a watch, not a downgrade.

**Q8.** E08. A22 moved it to RD on 2026-07-08, and nothing later changes that.

**Q9.** 13. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10 (E17 is a duplicate), E12, E13, E14, E15, E16 and CV. E07's rating was withdrawn, E11 has only a credit opinion (CO), and VD has only a country ceiling.

**Q10.** Depends. Its local-currency rating is BBB- (investment grade) and its foreign-currency rating is BB (not investment grade).

**Q11.** BBB+. A36 downgraded it from A- on 2024-09-30.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1, from A36. The later actions A35 and A33 are a watch and an affirmation.

**Q14.** None. Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 assigned it in 2023, and the downgrade to BBB+ (A27) came on 2026-04-15, after this date.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A33). Only the watch (A35) and the outlook changed in between.

**Q17.** No. A17 only placed Orrin Bank on Rating Watch Negative, and its rating stayed at A-.

**Q18.** E06. The watch from A17 is still open, whereas E14's watch (A35) was resolved by A33.

**Q19.** E01 (A03) and E09 (A25). E06's watch action carries no outlook.

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), which is not a default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. Its issuer rating is BBB (A03).

**Q25.** 6. By my reading, I01 (BBB), I03 (A), I05 (BBB+), I06 (A-), I07 (BBB-) and I08 (A) are investment grade. I08's action code "EX" is undefined in the data. If it does not count as a held rating, the answer is 5.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. The Republic of Valdoria has only a Country Ceiling (A12, BB), which is not an issuer rating.

**Q30.** E05 (FC BB, ceiling BB) and E15 (FC A, ceiling A).

**Q31.** No. No company's foreign-currency rating is above its country's ceiling.

**Q32.** E09. E11 has parent E10, and E10 has parent E09.

**Q33.** The holder takes the risk of E10, the guarantor of I05, which is rated BBB+ (A27).

**Q34.** No. E12 has no parent link to E09 or E10, and the shared "Halden" name is not evidence of a group.

**Q35.** 3, namely E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2, namely E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. The 19 rows include two duplicates by LEI: E03 duplicates E02, and E17 duplicates E10.

**Q38.** No. They have different LEIs, countries (DE and US) and records (E06 and E13).

**Q39.** A. A08 assigned it, A09 affirmed it, and there has been no change since.

**Q40.** 6, namely E01, E02, E09, E12, E14 and E16. E07 is excluded because its rating was withdrawn.

**Q41.** BB+ (A44). E16 comes from the "QA" source system, so it may be test data.

**Q42.** DE. E10 is the primary record. E17 is a research duplicate that shows LU.

**Q43.** 0. The only LU record, E17, is a duplicate of E10, which is domiciled in DE.

**Q44.** Yes. I07 is denominated in XVD, which I take to be Valdoria's local currency. That code is not defined in the data.

**Q45.** No. The note is rated BBB-, and the BB ceiling applies to foreign-currency ratings, not to a local-currency obligation.

**Q46.** No. E11 has only a credit opinion (A46, CO), not an issuer rating.

**Q47.** A (A47). Its action code "EX" is undefined in the data.

**Q48.** 8. Every instrument I01 to I08 has at least one rating action.

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
"Q25": {"count": 6},
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
"Q47": {"rating": "A"},
"Q48": {"count": 8}
}
```