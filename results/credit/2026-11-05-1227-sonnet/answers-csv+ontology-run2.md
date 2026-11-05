**Q1.** A-. A01 set A- on 2024-03-12, and the next action on E01 LTIDR (A02) was not until 2025-06-20.

**Q2.** No. The only 2026 action on E01 is A03, an affirmation (AF) with a Negative outlook, which is not a downgrade.

**Q3.** No. I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and its latest action, A09 on 2025-09-15, gives a POS outlook.

**Q5.** The holder takes Northwind Holdings' credit risk, rated A. I03 is guaranteed by E02, whose latest LTIDR FC (A09, recorded on its duplicate E03) is A.

**Q6.** The Country Ceiling for Valdoria is BB (A12) and caps foreign-currency ratings. E05's FC rating is BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A29 is an instrument rating, and A44 is on QA record E16, which is ignored.

**Q8.** E08. A22 moved it to RD, a default, on 2026-07-08, and there has been no later action.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, CV and E15. E07 was withdrawn. VD has only a ceiling, E11 only a credit opinion, and E16 is QA.

**Q10.** Depends. Its LC rating is BBB- (investment grade, A13) and its FC rating is BB (speculative grade, A14).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the next action (A35) was not until 2025-11-20.

**Q12.** A-, from A34 on 2023-01-15.

**Q13.** 1. Only A36 is a downgrade, since A35 is a Watch and A33 an affirmation.

**Q14.** None. The first rating action on E12 (A30) was on 2024-02-01.

**Q15.** A-. A26 set A- for E10 in 2023, and the downgrade A27 came only on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is still BBB+ (A35 is a Watch, A33 an affirmation).

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch, and the rating stays A-.

**Q18.** E06. A17 placed it on RWN on 2026-09-03. E14's RWN (A35) was cleared by the later affirmation A33, which carries no watch.

**Q19.** E01 and E09. Their latest actions, A03 and A25, both carry a NEG outlook.

**Q20.** No. A19 is a withdrawal for commercial reasons, which is not a credit event.

**Q21.** E07. It was rated (A18) and then withdrawn (A19).

**Q22.** E08, which reached RD in A22.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A02, affirmed in A03), which is investment grade.

**Q25.** 5. I01 is BBB, I03 is A (via guarantor E02), I05 is BBB+, I06 is A- and I07 is BBB-. I02 and I04 are speculative grade, and I08 is only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42). It is below the Corvenia ceiling of A (A37).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not the sovereign's rating.

**Q30.** E05 and E15. E05's FC rating of BB equals VD's ceiling of BB, and E15's FC rating of A equals CV's ceiling of A.

**Q31.** No. No company's FC rating exceeds its country's ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes Halden Bank's credit risk, rated BBB+. I05 is guaranteed by E10, whose LTIDR was downgraded to BBB+ in A27.

**Q34.** No. E12 has no parent, so it is not in E09's group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates by LEI, and E16 is QA test data.

**Q38.** No. Their LEIs differ and they are separate records, so there is no evidence they are the same entity.

**Q39.** A (A09, affirmed on the duplicate record E03).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn, E16 is QA, and Halden Bank is domiciled in LU, not GB.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** LU. RESEARCH holds for domicile, so E17's LU overrides E10's DE.

**Q43.** 1, the Halden Bank entity (E10/E17).

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. Local-currency debt is not capped by the ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected (EX) rating, so I08 stays unrated.

**Q48.** 7: I01 to I07. I08 is unrated.

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