**Q1.** A-. A01 (2024-03-12) set A- for E01, and the next action, A02, is not until 2025-06-20.

**Q2.** No. E01's only 2026 actions are affirmations (A03, A04); the downgrade A02 was in 2025.

**Q3.** No, it is BB+. I02 is subordinated and was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 shares E02's LEI, so they are one entity, and A09 (2025-09-15) is the latest action, with outlook POS.

**Q5.** The holder takes the credit risk of E02 (Northwind Holdings), rated A. I03 is guaranteed by E02, and E02's latest long-term rating is A (A08, A09 on E03).

**Q6.** Valdoria's Country Ceiling (VD, A12) is BB. It caps foreign-currency ratings, so E05's FC rating is BB (A14), while its LC rating of BBB- (A13) is not capped.

**Q7.** E08 and E10. E08 was downgraded (A21, A22) and E10 was downgraded (A27). The QA record E16 (A44) is ignored, and I05 is an instrument, not an issuer.

**Q8.** E08. A22 put it at RD on 2026-07-08, and RD is a default.

**Q9.** 12. Issuers with a long-term or short-term rating on 2026-10-01: E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, CV, E15. E07 was withdrawn (A19), VD has only a ceiling, E11 has only a credit opinion, and E16 is QA.

**Q10.** Depends. E05's FC rating is BB (speculative grade, A14) but its LC rating is BBB- (investment grade, A13), and the question does not say which basis.

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and the later actions (A35, A33) leave it unchanged.

**Q12.** A-. On 2024-01-01 only A34 (2023-01-15, A-) had been made.

**Q13.** 1 time. Only A36 is a downgrade; A35 is a Watch and A33 an affirmation.

**Q14.** None. E12's first rating, A30, was not assigned until 2024-02-01.

**Q15.** A-. E17 is the same entity as E10 (same LEI). A26 set A- and the downgrade A27 was not until 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 (A36) and is still BBB+ (A33).

**Q17.** No. A17 is a Rating Watch with the rating unchanged at A-, not a downgrade.

**Q18.** E06. Its latest action, A17, carries RWN. E14's Watch (A35) was cleared by the 2026 affirmation A33.

**Q19.** E01 and E09. Their latest outlooks are NEG (A03, A25). E06's and E08's latest actions record no outlook.

**Q20.** No. E07's rating was withdrawn (A19, "commercial reasons"), which is not a default.

**Q21.** E07. Its LTIDR was withdrawn (A19). E08 is in default but still holds an RD rating.

**Q22.** E08, which reached RD in A22. E16 is QA and ignored.

**Q23.** F2 (A04).

**Q24.** Yes. E01's LTIDR is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are speculative grade, and I08 is only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38). The A in A37 is the Country Ceiling, not the sovereign's rating.

**Q29.** None. VD has only a Country Ceiling (A12), no issuer rating.

**Q30.** E05 and E15. E05's FC rating is BB, equal to VD's ceiling of BB (A14, A12). E15's FC rating is A, equal to CV's ceiling of A (A41, A37). CV's own BBB+ is below the ceiling.

**Q31.** No. The only ceilings are VD (BB) and CV (A), and E05 and E15 are exactly at them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** The holder takes the credit risk of E10 (Halden Bank), rated BBB+. I05 is guaranteed by E10, whose latest rating is BBB+ (A27).

**Q34.** No. E12 has no parent and is not linked to E09.

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 duplicate E02 and E10, and E16 is QA, leaving 16 including the two sovereigns.

**Q38.** No. Their LEIs differ and there is no link between them.

**Q39.** A (A09, affirmed 2025-09-15).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 was withdrawn and E16 is QA. E10 is DE in the RATINGS record, which holds over E17's LU.

**Q41.** None. E16 is a QA record, so its actions are ignored.

**Q42.** DE. The RATINGS record E10 holds over the RESEARCH record E17's LU.

**Q43.** 0. The only LU record is E17, a RESEARCH duplicate of E10 whose RATINGS country is DE.

**Q44.** Yes. I07 pays in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. The ceiling applies to foreign-currency debt, not to local-currency debt like I07 (BBB-, A45).

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. I08 has only an Expected action (A47), so it stays unrated.

**Q48.** 7: I01 through I07.

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