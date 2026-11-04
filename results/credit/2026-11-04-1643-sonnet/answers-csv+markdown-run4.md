**Q1.** A-. E01's LTIDR FC was A- from A01 (2024-03-12) and not changed until A02 in June 2025.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the downgrade A02 was in 2025.

**Q3.** No. I02 was downgraded to BB+ in A07, which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02/E03's latest LTIDR is A (A09).

**Q6.** Valdoria's Country Ceiling is BB (A12). It caps the foreign-currency rating (A14, BB) but not the local-currency rating (A13, BBB-).

**Q7.** E08 and E10. E08 has the 2026 downgrades A21 and A22. E10 has A27 (E17 is the same entity). A29 is an instrument rating, and E16 is QA and ignored.

**Q8.** E08. A22 gave it RD on 2026-07-08, and RD is a default.

**Q9.** 12. These are E01, E02 (E03 is a duplicate), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 was withdrawn. E11 has only a credit opinion. VD has only a ceiling. E16 is QA.

**Q10.** Depends. Its foreign-currency rating is BB (speculative grade), and its local-currency rating is BBB- (investment grade).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later watch (A35) did not change the rating.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. A26 set it, and the downgrade A27 came later, on 2026-04-15.

**Q16.** No. It was BBB+ on 2025-01-01 and is still BBB+ now (A33, A35 and the watch did not change it).

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 put it on RWN. E14's watch (A35) was cleared by the affirmation A33.

**Q19.** E01 and E09, from A03 and A25 (both NEG).

**Q20.** No. A19 withdrew E07's rating for commercial reasons, which says nothing about default.

**Q21.** E07, whose rating was withdrawn in A19.

**Q22.** E08, which reached RD in A22.

**Q23.** F2, from A04.

**Q24.** Yes. E01's LTIDR FC is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 has only an expected rating.

**Q26.** A+, from A40.

**Q27.** A-, from A42.

**Q28.** BBB+, from A38. A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12).

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB. E15's is A, equal to CV's ceiling of A. The other countries have no ceiling.

**Q31.** No. E05 and E15 are at their ceilings, not above.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent and a different LEI, so it is not in E09's group.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates, and E16 is QA.

**Q38.** No. They have different LEIs, different names and different countries.

**Q39.** A. A09 on E03 (the same entity as E02) is the latest action.

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is QA data and is ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17, which says LU.

**Q43.** 0. The only LU record is E17, which is the same entity as E10 and is domiciled in DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where the issuer E05 is domiciled.

**Q45.** No. I07 is rated BBB- (A45), and the ceiling does not apply to local-currency debt.

**Q46.** No. E11 has only a credit opinion (A46), which is not a rating.

**Q47.** None. I08 has only an expected rating (A47, EX).

**Q48.** 7: I01 to I07.

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
"Q42": {"country": "DE"},
"Q43": {"count": 0},
"Q44": {"local_currency": "yes"},
"Q45": {"above_ceiling": "no"},
"Q46": {"issuer_rating": "no"},
"Q47": {"rating": "none"},
"Q48": {"count": 7}
}
```