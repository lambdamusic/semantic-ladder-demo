**Q1.** A-. A01 assigned A- on 2024-03-12, and the next LTIDR action (A02) was on 2025-06-20.

**Q2.** No. The only 2026 Kestrel issuer actions are affirmations (A03, A04). The outlook moved to Negative, but the rating stayed at BBB.

**Q3.** No. I02 is rated BB+ after the downgrade in A07 (the issuer rating is BBB, but the instrument is rated separately).

**Q4.** Positive. E03 shares its LEI with E02, so I treated them as one entity. The latest action, A09 (2025-09-15), gives POS.

**Q5.** The holder takes the credit risk of E02, the guarantor of I03, rated A. The issuer E04 is a finance subsidiary, and A11 affirms the instrument at A.

**Q6.** Valdoria's country ceiling is BB (A12). The foreign-currency rating is capped at that ceiling (A14, BB), while the local-currency rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. E06's A17 is a watch placement, not a downgrade.

**Q8.** E08. It was rated RD in A22 on 2026-07-08. E07's withdrawal (A19) is not a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 was withdrawn, and VD has only a country ceiling (CC) record, not an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (investment grade, A13), but the foreign-currency rating is BB (not, A14).

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-, from A34 (2023-01-15), before the downgrade in A36.

**Q13.** 1, in A36. The other actions are an assignment, an affirmation and a watch.

**Q14.** NR (not rated). Halden Foods' first rating, A30, is dated 2024-02-01.

**Q15.** A-. A26 assigned A- and the downgrade in A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ (A35 and A33 only changed the watch status and affirmed it).

**Q17.** No. A17 (2026-09-03) placed E06 on Rating Watch Negative and left the rating at A-.

**Q18.** E06 (A17). E14's watch from A35 was resolved by the affirmation with a Stable outlook in A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn for commercial reasons (A19), and its last rating was BB.

**Q21.** E07. Its rating was withdrawn in A19.

**Q22.** E08. It was rated RD in A22, and no other record shows a default rating.

**Q23.** F2, from A04.

**Q24.** Yes. The LTIDR is BBB (A03).

**Q25.** 4. I01 (BBB), I03 (A), I05 (BBB+) and I06 (A-) are investment grade. I02 (BB+) and I04 (BB) are not.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38.

**Q29.** NR. The data holds only a country ceiling of BB for VD (A12), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB, equal to Valdoria's ceiling of BB. E15's is A, equal to Corvenia's ceiling of A (A37).

**Q31.** No. E05 and E15 are at their ceilings, and the other companies' countries (GB, DE, GR, US) have no ceiling in the data.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10, the guarantor, rated BBB+. I05 was downgraded to BBB+ in A29, matching E10's rating.

**Q34.** No. E12 has no parent link and a different LEI, so the shared "Halden" name is not evidence of a group.

**Q35.** 3: E09, E10 and E11.

**Q36.** 2: E02 and E04. E03 duplicates E02 (same LEI).

**Q37.** 16. There are 17 records, but E03 duplicates E02.

**Q38.** No. They have different LEIs and countries (DE and US), and the data links them in no way.

**Q39.** A. A08 assigned A, and A09 (for E03, which is E02) affirmed A.

**Q40.** 5: E01, E02 (with E03), E09, E12 and E14. E07 was withdrawn, and E10 is domiciled in DE.

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