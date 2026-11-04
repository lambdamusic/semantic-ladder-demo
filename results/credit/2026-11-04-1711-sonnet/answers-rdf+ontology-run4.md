**Q1.** A-. A01 (assigned 2024-03-12) was the latest E01 long-term foreign-currency action before 2025-01-01; the next, A02, is dated 2025-06-20.

**Q2.** No. E01's only 2026 issuer action is A03, an affirmation with a Negative outlook. The 2025 downgrades (A02, A06, A07) are outside 2026.

**Q3.** No. I02 was downgraded to BB+ (A07), which is speculative grade.

**Q4.** Positive. E03 is the same entity as E02 (same LEI), and A09 (2025-09-15) is the latest action, with a Positive outlook.

**Q5.** The holder takes Northwind Holdings' credit risk (E02, same entity as E03), rated A. I03 is guaranteed by E02, and A09 is the latest long-term action at A.

**Q6.** E05's foreign-currency rating is BB (A14) and its local-currency rating is BBB- (A13). The BB matches Valdoria's Country Ceiling (A12), which caps foreign-currency ratings but not local-currency ones.

**Q7.** E08 and E10. E08 was downgraded in A21 and A22, and E10 in A27. A44 (E16) is QA test data and is ignored. A29 is an instrument downgrade, not an issuer downgrade.

**Q8.** E08. A22 (2026-07-08) set E08 to RD, which is a default.

**Q9.** 12. These are E01, E02 (with E03), E05, E06, E08, E09, E10 (with E17), E12, E13, E14, E15 and CV. E07 was withdrawn (A19), E16 is QA, E11 has only a credit opinion, and VD has only a Country Ceiling.

**Q10.** Depends. E05's foreign-currency rating is BB, which is speculative grade (A14). Its local-currency rating is BBB-, which is investment grade (A13).

**Q11.** BBB+. A36 downgraded E14 to BBB+ on 2024-09-30, and A35 (2025-11-20) is later.

**Q12.** A-. A34 (2023-01-15) was still in force on 2024-01-01.

**Q13.** 1. Only A36 is a downgrade for E14. The Watch (A35) is not one.

**Q14.** None. E12's first action, A30, is dated 2024-02-01.

**Q15.** A-. E10 and E17 are the same entity, and A26 (A-) held until the downgrade in A27 on 2026-04-15.

**Q16.** No. E14 was BBB+ on 2025-01-01 and is still BBB+ (A33 affirmed it).

**Q17.** No. E06's only 2026 action is A17, a Rating Watch, which leaves the rating unchanged.

**Q18.** E06. A17 (2026-09-03) placed it on Watch Negative. E14's Watch (A35) was superseded by A33, which has no Watch.

**Q19.** E01 and E09. E01's Negative outlook is from A03, and E09's is from A25.

**Q20.** No. E07's rating was withdrawn (A19, commercial reasons), and a withdrawal is not a default.

**Q21.** E07. It had a long-term rating (A18) that was withdrawn on 2026-05-12 (A19).

**Q22.** E08. A22 set it to RD.

**Q23.** F2 (A04).

**Q24.** Yes. E01's long-term foreign-currency rating is BBB (A03).

**Q25.** 5. These are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-).

**Q26.** A+ (A40, E15's local-currency rating).

**Q27.** A-. I06 is rated A- in A42.

**Q28.** BBB+ (A38, CV's foreign-currency rating).

**Q29.** None. VD has only a Country Ceiling (A12), which is not a rating.

**Q30.** E05 and E15. E05's BB equals Valdoria's ceiling of BB (A12, A14), and E15's A equals Corvenia's ceiling of A (A37, A41).

**Q31.** No. E05 and E15 sit exactly at their ceilings, and no other company's country has a ceiling.

**Q32.** E09. E11's parent is E10, and E10's parent is E09.

**Q33.** The holder takes Halden Bank's credit risk (E10, same entity as E17), rated BBB+. I05 is guaranteed by E10, and A27 downgraded E10 to BBB+.

**Q34.** No. E12 has no parent recorded and no link to E09, so only the name is shared.

**Q35.** 3. These are E09, E10 (with E17) and E11.

**Q36.** 2. These are E02 (with E03) and E04.

**Q37.** 16. There are 19 records (E01–E17, VD, CV). E03 duplicates E02 and E17 duplicates E10, and E16 is QA, which leaves 16.

**Q38.** No. E06 and E13 have different LEIs and different countries, and the data links them in no other way.

**Q39.** A (A09).

**Q40.** 5. These are E01, E02, E09, E12 and E14. E07 is withdrawn and E16 is QA.

**Q41.** None. E16 is a QA record, so it and its actions are ignored.

**Q42.** DE. E10 is the RATINGS record; the LU on E17 is overridden.

**Q43.** 0. The only LU record is E17, which is E10, and the RATINGS record says DE.

**Q44.** Yes. I07 is in XVD, the domestic currency of VD, where its issuer E05 is domiciled.

**Q45.** No. I07 is local-currency debt, so the ceiling does not cap it.

**Q46.** No. E11 has only a credit opinion (A46), which is not an issuer rating.

**Q47.** None. A47 is only an Expected rating, so the note stays unrated until an Assigned action.

**Q48.** 7. These are I01–I07, and I08 is only Expected.

```json
{
"Q1": {"rating": "A-"},
"Q2": {"downgraded": "no"},
"Q3": {"investment_grade": "no", "rating": "BB+"},
"Q4": {"outlook": "Positive"},
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