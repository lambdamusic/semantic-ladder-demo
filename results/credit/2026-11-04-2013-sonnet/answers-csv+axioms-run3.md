**Q1.** A-. A01 assigned A- on 2024-03-12, and the next action, A02, came on 2025-06-20, after the date asked.

**Q2.** No. The only 2026 Kestrel action on the issuer is A03, an affirmation at BBB. The downgrade (A02) was in 2025.

**Q3.** No, it is BB+. A07 downgraded I02 to BB+ on 2025-06-20, superseding A23 (BBB).

**Q4.** Positive. A09 (2025-09-15) is on E03, which shares E02's LEI, so it supersedes A08 and carries POS.

**Q5.** The holder takes the credit risk of E02, Northwind Holdings, rated A. I03 is guaranteed by E02 (the guarantor takes precedence), and E02's current rating is A (A09, via the shared LEI with E03).

**Q6.** The data doesn't state a reason. A12 puts Valdoria's Country Ceiling at BB, and A14 gives the foreign-currency rating (BB) the same level, while A13 gives the local-currency rating BBB-. That is consistent with a ceiling cap, but no comment says so.

**Q7.** E08 and E10. A21 and A22 downgraded E08 in 2026, and A27 downgraded E10. A44 on E16 is a QA test record, and A29 is an instrument rating.

**Q8.** E08. A22 (2026-07-08) rated it RD, and nothing came after it.

**Q9.** 12. These are E01, E02 (E03 is the same entity), E05, E06, E08, E09, E10 (E17 is the same entity), E12, E13, E14, CV and E15. E07 is withdrawn (A19), VD has only a ceiling, E11 has only a credit opinion (A46), and E16 is a test record.

**Q10.** Depends. The local-currency rating is BBB- (A13, investment grade) and the foreign-currency rating is BB (A14, not investment grade).

**Q11.** BBB+. A36 downgraded Marlow on 2024-09-30 and nothing changed the rating before 2025-06-01.

**Q12.** A-. A34 assigned A- on 2023-01-15, and the downgrade A36 came later.

**Q13.** 1. Only A36 is a downgrade. A35 is a watch placement and A33 is an affirmation.

**Q14.** None. E12's first action, A30, was on 2024-02-01.

**Q15.** A-. A26 assigned A- in 2023, and the downgrade A27 came on 2026-04-15.

**Q16.** No. It was BBB+ on 1 January 2025 and is still BBB+ (A35 and A33 keep BBB+).

**Q17.** No. The only 2026 action on E06 is A17, a Rating Watch placement with the rating unchanged at A-.

**Q18.** E06. A17 (2026-09-03) is the current action and carries RWN. Marlow's RWN (A35) was superseded by A33.

**Q19.** E01 and E09. A03 and A25 are the current actions and carry a negative outlook.

**Q20.** No. A19 withdrew E07's rating from BB, and a withdrawal is not a default.

**Q21.** E07. Its rating was withdrawn (A19). E16 is excluded as a QA test record.

**Q22.** E08. It is the only entity ever rated RD or D (A22).

**Q23.** F2 (A04).

**Q24.** Yes. The current issuer rating is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I02 and I04 are sub-investment grade, and I08 has only an expected rating.

**Q26.** A+ (A40).

**Q27.** A- (A42).

**Q28.** BBB+ (A38).

**Q29.** None. VD has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 and E15. E05's foreign-currency rating is BB, matching Valdoria's BB ceiling (A12, A14). E15's is A, matching Corvenia's A ceiling (A37, A41).

**Q31.** No. E05 and E15 sit exactly at their ceilings, not above them.

**Q32.** E09. E11's parent is E10, whose parent is E09.

**Q33.** E10, Halden Bank, rated BBB+. The guarantor of I05 is E10, and A27 is its current rating.

**Q34.** No. E12 has no parent link or shared LEI with the Halden Bank group. Only the name is similar.

**Q35.** 3. The group is E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2. The group is E02 and E04. E03 is the same entity as E02.

**Q37.** 16. There are 19 records. E03 and E17 are duplicates by LEI, which leaves 17, and E16 is a QA test record and not a legal entity.

**Q38.** No. They have different LEIs, different countries and no link between them.

**Q39.** A (A09 via E03, same LEI).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E10 is domiciled in LU, and E07 is withdrawn.

**Q41.** None. E16 is a QA test record, so its actions are not rating actions in force.

**Q42.** LU. The research record E17 shares E10's LEI and gives LU, which overrides E10's DE.

**Q43.** 1. E10 and E17 are one entity.

**Q44.** Yes. I07 is in XVD, which is the domestic currency of VD, E05's domicile.

**Q45.** No. The ceiling (BB, A12) constrains foreign-currency ratings, and I07 is a local-currency instrument rated BBB- (A45), so it isn't tested against that ceiling.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an expected rating (EX), so no rating is in force.

**Q48.** 7. I01 to I07 hold a rating, and I08 has only an expected one.

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