**Q1.** A-. Kestrel's LTIDR was assigned A- on 2024-03-12 (A01), and the next action is dated 2025-06-20 (A02), after the question date.

**Q2.** No. The only 2026 actions on Kestrel are affirmations (A03, A04).

**Q3.** No. The 2031 note (I02) is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and the latest action is A09 (2025-09-15) with a POS outlook.

**Q5.** The holder takes Northwind Holdings' (E02) credit risk, rated A. I03 is guaranteed by E02, whose latest rating is A (A09, recorded against E03).

**Q6.** The FC rating is capped by Valdoria's Country Ceiling of BB (A12). The FC rating is BB (A14), against BBB- on a local-currency basis (A13), which is not capped.

**Q7.** E08 (A21, A22) and E10 (A27, same entity as E17) were downgraded in 2026. The instrument downgrade A29 is not an issuer downgrade, and A44 is on a QA record, so it is ignored.

**Q8.** E08. Its latest action, A22, put it at RD, which is a default.

**Q9.** 12. These are E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn, VD has only a ceiling, E11 has only a credit opinion, E04 has no rating, and E16 is QA.

**Q10.** Depends. Its FC rating is BB (speculative) and its LC rating is BBB- (investment grade), per A14 and A13.

**Q11.** BBB+. A36 downgraded Marlow to BBB+ on 2024-09-30, and nothing changed the rating before 2025-06-01.

**Q12.** A-, from A34.

**Q13.** 1, which is A36. A33 and A35 are an affirmation and a Watch.

**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. A26 set it, and the downgrade A27 came on 2026-04-15.

**Q16.** No. Marlow was BBB+ on 2025-01-01 and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-.

**Q18.** Only E06 (A17). E14's Watch (A35) was superseded by the affirmation A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. A19 is a withdrawal for commercial reasons, which is not a default.

**Q21.** E07. Its rating was withdrawn (A19).

**Q22.** E08, which reached RD (A22).

**Q23.** F2 (A04).

**Q24.** Yes. Kestrel's LTIDR is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 has only an Expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A at A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), not an issuer rating.

**Q30.** E05 has FC BB, equal to VD's ceiling of BB. E15 has FC A, equal to CV's ceiling of A.

**Q31.** No. E05 and E15 are at their ceilings, not above.

**Q32.** E09. The chain runs E11 → E10 → E09.

**Q33.** The holder takes Halden Bank's (E10) credit risk, rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent link and is outside the group headed by E09.

**Q35.** 3: E09, E10 (same entity as E17) and E11.

**Q36.** 2: E02 (same entity as E03) and E04.

**Q37.** 16. There are 19 records, less the duplicates E03 and E17 and the QA record E16. I counted the two sovereigns as entities.

**Q38.** No. They have different LEIs and different names.

**Q39.** A (A09, via E03, the same entity as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E10 is domiciled in LU, because the RESEARCH record holds for country.

**Q41.** None. E16 is a QA test record, so it and its actions are ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile.

**Q43.** 1, which is Halden Bank (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where E05 is domiciled.

**Q45.** No. Its rating is BBB- (A45), and local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated.

**Q48.** 7, which is I01 to I07.

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