**Q1.** A-. A01 assigned A- on 2024-03-12, and the next change (A02) came on 2025-06-20, so it stood on 2025-01-01.

**Q2.** No. The only 2026 actions on E01 (A03, A04) are affirmations.

**Q3.** No, it is BB+. I02 is subordinated, and A07 downgraded it to BB+ on 2025-06-20, which supersedes A23 (BBB).

**Q4.** Positive. E03 shares E02's LEI, so they are the same entity, and A09 (2025-09-15) is the latest action with a POS outlook, superseding A08 (STA).

**Q5.** E02, rated A. I03 is issued by E04 but guaranteed by E02, so the holder takes the guarantor's risk; A11 and A09 rate it A.

**Q6.** The data doesn't state a reason. It does show that A12 gives Valdoria a Country Ceiling of BB, which equals E05's foreign-currency rating (A14, BB) and sits below its local-currency rating (A13, BBB-). That is consistent with a ceiling cap, but the data doesn't say so.

**Q7.** E08, E10 and E16. They were downgraded in 2026 by A21 and A22 (E08), A27 (E10) and A44 (E16). A17 for E06 is a watch, not a downgrade.

**Q8.** E08. A22 moved it to RD (restricted default) on 2026-07-08.

**Q9.** 13. The issuers are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15, E16 and CV. E07 was withdrawn (A19). VD has only a country ceiling. E11 has only a "CO" rating, not an issuer rating.

**Q10.** Depends. The local-currency rating is BBB- (A13, investment grade) and the foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the watch in A35 came later.

**Q12.** A-, from A34 (2023-01-15).

**Q13.** 1. Only A36 is a downgrade; A35 is a watch and A33 an affirmation.

**Q14.** None. E12's first rating is A30 on 2024-02-01.

**Q15.** A-. E10 was assigned A- by A26; the downgrade to BBB+ (A27) came in April 2026. E17 is the same LEI.

**Q16.** No. It was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch Negative with the rating unchanged at A-. E13 (Orrin Bancorp) is a different entity.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's earlier watch (A35) was resolved by the A33 affirmation without a watch.

**Q19.** E01 and E09, from A03 and A25.

**Q20.** No. E07's last action is a withdrawal (A19), not a default.

**Q21.** E07, whose rating was withdrawn (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The issuer rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08's rating expired on 2026-09-01 (A47).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling record (A12, BB), not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating of BB equals VD's ceiling of BB, and E15's A equals CV's ceiling of A (A37).

**Q31.** No. E05 and E15 are at their ceilings, not above them.

**Q32.** E09. E11 has parent E10, which has parent E09.

**Q33.** E10, rated BBB+. I05 is guaranteed by E10, whose rating is BBB+ after A27, and I05 itself was downgraded to BBB+ by A29.

**Q34.** No. E12 has no parent and no link to E09 or E10.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. The file has 19 rows, but E03 duplicates E02 and E17 duplicates E10, going by their shared LEIs.

**Q38.** No. They have different LEIs, countries (DE and US) and names.

**Q39.** A. A09 (affirmed on 2025-09-15) is the latest action under the E02/E03 identity.

**Q40.** 6: E01, E02, E09, E12, E14 and E16. E07 was withdrawn, and E10 is domiciled in DE.

**Q41.** BB+ (A44).

**Q42.** DE. The RATINGS record E10 says DE, while the RESEARCH duplicate E17 says LU. The conflict is unresolved, and I used the primary source.

**Q43.** 0. The only LU record is E17, a duplicate of E10, whose primary record says DE. If you trust E17's country, the answer would be 1.

**Q44.** Yes, by inference. The data doesn't state Valdoria's currency, but I07 is in XVD, not a standard code, and its rating (A45, BBB-) matches the local-currency rating A13.

**Q45.** No. The ceiling applies to foreign-currency ratings, and I07 appears to be local-currency.

**Q46.** No. E11 has only a "CO" rating (A46), whose meaning the data doesn't define, and no LTIDR.

**Q47.** None. A47 shows I08's rating expired (EX) on 2026-09-01.

**Q48.** 7, which is I01 to I07. I08 expired.

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