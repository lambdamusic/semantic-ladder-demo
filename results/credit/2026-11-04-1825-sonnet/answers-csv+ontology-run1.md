**Q1.** A-. The latest action on or before that date is A01 (A-, 2024-03-12); the downgrade A02 came in June 2025.

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04); the outlook moved to NEG, but that is not a downgrade.

**Q3.** No, it is BB+. I02 is subordinated and was downgraded to BB+ by A07, which is speculative grade.

**Q4.** Positive. E03 shares its LEI with E02, so they are one entity, and the latest action (A09, 2025-09-15) gives POS.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and E02's current LTIDR is A (A09, via E03).

**Q6.** Valdoria's Country Ceiling is BB (A12), which caps the FC rating (A14, BB). The LC rating (A13, BBB-) is not capped.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. The E16 downgrade (A44) is QA test data and is ignored.

**Q8.** E08. A22 (2026-07-08) set RD, which is a default, and nothing later changes it.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10, E12, E13, E14, CV and E15. E07 is withdrawn, E11 has only a credit opinion, and VD has only a ceiling.

**Q10.** Depends. The FC rating is BB (A14, speculative grade) and the LC rating is BBB- (A13, investment grade).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30, and A35 (a Watch) did not change it.

**Q12.** A-. A34 (2023-01-15) was the rating then, before the A36 downgrade.

**Q13.** 1. Only A36 is a downgrade; A35 is a Watch and A33 is an affirmation.

**Q14.** None. E12's first rating (A30) was assigned on 2024-02-01.

**Q15.** A-. E10 and E17 share an LEI, so they are one entity, and A26 (A-) held until the downgrade A27 on 2026-04-15.

**Q16.** No. The rating was BBB+ on 2025-01-01 and is BBB+ now (A33); the Watch in A35 did not change it.

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch with the rating unchanged at A-.

**Q18.** E06. A17 (2026-09-03) is RWN. E14's Watch (A35) was superseded by A33, which carries no watch.

**Q19.** E01 and E09. A03 and A25 set NEG, and nothing later changes them. E06's A17 states no outlook, so I do not count it.

**Q20.** No. A19 is a withdrawal for commercial reasons, which is not a credit event.

**Q21.** E07. Its rating was withdrawn by A19. The E16 ratings are QA and ignored.

**Q22.** E08. It reached RD in A22; no other non-QA entity has an RD or D rating.

**Q23.** F2 (A04).

**Q24.** Yes. The LTIDR is BBB (A03), which is investment grade.

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The CC of A (A37) is a ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to the VD ceiling of BB, and E15's FC rating is A, equal to the CV ceiling of A. CV's own FC rating is BBB+, not A, so CV is not included.

**Q31.** No. E05 (BB) and E15 (A) sit exactly at their ceilings, and no other entity has a ceiling.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent link to E09, and a shared name is not ownership.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records, minus two duplicates (E03 and E17) and the QA record E16.

**Q38.** No. They have different LEIs, and E06 is Orrin Bank AG (DE) while E13 is Orrin Bancorp Inc (US).

**Q39.** A (A09, via E03, same LEI as E02).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn, E16 is QA, and E10 is DE per the RATINGS record.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds; the RESEARCH record E17 says LU, but RATINGS is the system of record.

**Q43.** 0. The only LU record is E17, and RATINGS overrides it with DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, the issuer E05's country.

**Q45.** No. The ceiling applies only to foreign-currency debt, and I07 is local-currency, so it is not capped.

**Q46.** No. E11 has only a Credit Opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it is unrated until an AS action confirms it.

**Q48.** 7: I01 to I07. I08 is only expected.

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