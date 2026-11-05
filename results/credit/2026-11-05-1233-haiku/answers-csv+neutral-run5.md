**Q1.** A-. Kestrel's FC issuer rating was assigned A- on 2024-03-12 (A01) and not changed until the 2025-06-20 downgrade (A02).

**Q2.** No. Kestrel's only 2026 actions are an affirmation of BBB (A03) and of F2 short-term (A04).

**Q3.** No, BB+. The 2031 note (I02) is subordinated and was downgraded to BB+ on 2025-06-20 (A07).

**Q4.** Positive. E03 is the same LEI as E02, and its latest action (A09, 2025-09-15) sets the outlook to POS.

**Q5.** Northwind Holdings (E02), rated A. The 2030 notes (I03) are guaranteed by E02, so they carry its credit risk and are rated in line with its A rating (A11).

**Q6.** The data points to the Country Ceiling. Valdoria Telecom's FC rating (E05, BB) equals the Valdoria ceiling (VD, BB, A12), which caps FC ratings but not LC ones (BBB-, A13). The records don't state a reason explicitly.

**Q7.** E08 (Saxby) and E10 (Halden Bank). Both were downgraded in 2026 (A21, A22, A27). E16 is a QA record and is excluded.

**Q8.** E08 (Saxby). Its RD rating from 2026-07-08 (A22) is a default, and no other entity has a default action.

**Q9.** 12. These entities hold a current issuer rating: E01, E02, E05, E06, E08, E09, E10, E12, E13, E14, CV, E15. E07 has been withdrawn, and VD, E11 and E04 have no issuer rating.

**Q10.** Depends. Local-currency BBB- (A13) is investment grade, but foreign-currency BB (A14) is not.

**Q11.** BBB+. The 2024-09-30 downgrade (A36) is the latest action before 2025-06-01.

**Q12.** A-. The rating assigned on 2023-01-15 (A34) still held on 2024-01-01.

**Q13.** 1. A36 is the only downgrade. A35 is a watch placement and A33 an affirmation.

**Q14.** None. Halden Foods' first rating was assigned on 2024-02-01 (A30).

**Q15.** A-. The downgrade to BBB+ came on 2026-04-15 (A27), after this date.

**Q16.** No. The rating has stayed at BBB+ since 2024-09-30 (A36). The 2025 and 2026 actions (A35, A33) didn't change it.

**Q17.** No. Orrin Bank's 2026 action (A17) is a Rating Watch placement on an unchanged A-.

**Q18.** E06 (Orrin Bank). Its latest action (A17) sets Rating Watch Negative. Marlow (E14) had RWN in A35, but its later affirmation (A33) carries no watch flag, so I treated that watch as cleared. This is an interpretation.

**Q19.** E01 (Kestrel) and E09 (Halden Group). Their latest recorded outlooks are NEG (A03, A25).

**Q20.** No. Pellam's rating was withdrawn for commercial reasons (A19), and a withdrawal is not a default.

**Q21.** E07 (Pellam). Its rating was withdrawn on 2026-05-12 (A19). E11 never had an issuer rating (its CO isn't one).

**Q22.** E08 (Saxby). It is the only entity with an RD rating (A22).

**Q23.** F2. This is Kestrel's short-term rating after the 2026-02-10 affirmation (A04).

**Q24.** Yes. Kestrel's current issuer rating is BBB (A03), which is investment grade.

**Q25.** 5. The investment-grade instruments are I01 (BBB), I03 (A), I05 (BBB+), I06 (A-) and I07 (BBB-). I08 is only an expected rating, so it doesn't count.

**Q26.** A+. This is Corvenia Power's LC rating (A40).

**Q27.** A-. The 2032 note (I06) is rated A- (A42).

**Q28.** BBB+. This is the Republic of Corvenia's FC rating (A38).

**Q29.** None. Valdoria has only a Country Ceiling (A12), which is not an issuer rating.

**Q30.** E05 (Valdoria Telecom, BB against a BB ceiling) and E15 (Corvenia Power, A against an A ceiling).

**Q31.** No. Every FC issuer rating in a ceiling country is at or below its ceiling.

**Q32.** E09 (Halden Group). The chain is E11 → E10 → E09.

**Q33.** E10 (Halden Bank), rated BBB+. The 2028 notes (I05) are guaranteed by E10 and rated in line with its BBB+ rating (A27, A29).

**Q34.** No. E12 has no parent link, and it is not in the E09 chain.

**Q35.** 3. The Halden group is E09, E10 and E11.

**Q36.** 2. The Northwind group is E02 (with E03) and E04.

**Q37.** 16. The data describes 19 records. E03 and E17 duplicate E02 and E10 by LEI, and E16 is a QA record, leaving 16 distinct entities including the two sovereigns.

**Q38.** No. Their LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. Northwind Holdings' latest action is the 2025-09-15 affirmation at A (A09).

**Q40.** 5. The GB issuers with a current issuer rating are E01, E02, E09, E12 and E14. E17 is domiciled in LU, and E16 is QA.

**Q41.** None. Brindle Capital (E16) is a QA record, which must be ignored.

**Q42.** LU. The RESEARCH record (E17) holds for domicile and says LU.

**Q43.** 1. Only E10 (Halden Bank) is domiciled in LU.

**Q44.** Yes. The 2027 note (I07) is in XVD, the domestic currency of Valdoria, where the issuer is domiciled.

**Q45.** No. The note is rated BBB- (A45), but the Country Ceiling applies only to FC debt, and this is local-currency debt.

**Q46.** No. E11's only action is a credit opinion (A46), which the ontology says is never an issuer rating.

**Q47.** None. The 2034 note (I08) has only an expected rating (EX, A47), so it is not yet rated.

**Q48.** 7. I01 through I07 have ratings on 2026-10-01. I08 does not.

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