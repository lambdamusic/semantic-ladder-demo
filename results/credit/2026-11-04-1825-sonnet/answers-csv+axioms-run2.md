**Q1.** A-. E01's LTIDR was assigned A- (A01) and not changed until the June 2025 downgrade (A02).

**Q2.** No. The only 2026 actions on E01 are affirmations (A03, A04), and the downgrade to BBB was in 2025 (A02).

**Q3.** No, it is BB+. I02 was assigned BBB (A23) and downgraded to BB+ (A07).

**Q4.** Positive. The Northwind records E02 and E03 share an LEI, so they are one entity, and A09 (2026-style current action of 2025-09-15) affirmed A with a POS outlook, superseding A08.

**Q5.** The holder takes E02's credit risk, rated A. I03 is guaranteed by E02, and the current rating is A09 (recorded under E03, the same entity).

**Q6.** Valdoria Telecom's FC rating of BB (A14) is capped at the Republic of Valdoria's Country Ceiling of BB (A12). Its LC rating is BBB- (A13).

**Q7.** E08 and E10. E08 was downgraded in A21 and A22 and E10 in A27. E16's downgrade (A44) is excluded because it is a QA test record.

**Q8.** E08. It has been at RD since A22 (2026-07-08).

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10, E12, E13, E14, E15 and CV. E07 is withdrawn (A19), E11 has only a credit opinion (A46), E16 is a test record, and VD has only a ceiling (A12).

**Q10.** It depends on the currency basis. The LC rating is BBB- (investment grade, A13) and the FC rating is BB (not investment grade, A14).

**Q11.** BBB+. A36 downgraded E14 from A- to BBB+ on 2024-09-30, and nothing changed it by 2025-06-01.

**Q12.** A-, from A34.

**Q13.** 1. Only A36 is a downgrade; A35 is a watch placement.

**Q14.** None. E12's first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. E10 was assigned A- in A26 and was not downgraded until 2026-04-15 (A27).

**Q16.** No. E14 was BBB+ on 2025-01-01 and is BBB+ now (A33), and the watch in A35 did not change the rating.

**Q17.** No. E06's only 2026 action is a watch placement at A- (A17).

**Q18.** E06, from A17 (RWN). E14's earlier RWN (A35) was superseded by A33.

**Q19.** E01 (A03) and E09 (A25).

**Q20.** No. E07's rating was withdrawn (A19) and it was never rated RD or D.

**Q21.** E07. Its rating was withdrawn (A19). E16 is excluded because it is a test record.

**Q22.** E08 (RD in A22).

**Q23.** F2 (A04).

**Q24.** Yes. E01's issuer rating is BBB (A03).

**Q25.** 5: I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12) and no issuer rating.

**Q30.** E05 and E15. E05's FC rating of BB equals Valdoria's ceiling of BB (A14, A12), and E15's FC rating of A equals Corvenia's ceiling of A (A41, A37).

**Q31.** No. No company's FC rating is above its country's ceiling.

**Q32.** E09. E11's parent is E10 and E10's parent is E09.

**Q33.** The holder takes E10's credit risk, rated BBB+. I05 is guaranteed by E10, whose current rating is A27.

**Q34.** No. E12 has no parent link to E09, and the shared name is not evidence of a group.

**Q35.** 3: E09, E10 and E11. E17 is a duplicate of E10.

**Q36.** 2: E02 and E04. E03 is a duplicate of E02.

**Q37.** 17. There are 19 rows, but E03 duplicates E02 and E17 duplicates E10 (same LEIs).

**Q38.** No. They have different LEIs and no link between them.

**Q39.** A (A09).

**Q40.** 5: E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is a test record.

**Q41.** None. E16 is a QA test record, so its actions are not treated as ratings.

**Q42.** DE. E10 is domiciled in DE per its RATINGS record. E17's LU is a research-system duplicate.

**Q43.** 0. E17's LU is overridden by E10's DE.

**Q44.** Yes. I07 is in XVD, which is Valdoria's domestic currency.

**Q45.** No. The ceiling caps foreign-currency ratings, and I07 is a local-currency obligation.

**Q46.** No. E11 has only a credit opinion (A46).

**Q47.** None. I08 has only an expected rating (A47, EX), which is not a rating in force.

**Q48.** 7: the five investment-grade instruments in Q25, plus I02 (BB+) and I04 (BB).

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
"Q37": {"count": 17},
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