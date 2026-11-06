**Assumptions:** Entities are merged by LEI, QA records are ignored, RESEARCH overrides RATINGS for country, and actions dated after today (2026-11-06) are not used. Rating watches stay in force until the next action on the same thing, type and basis.

**Q1.** A-. A01 (2024-03-12) assigned A-, and the cut to BBB came later, in A02 (2025-06-20).

**Q2.** No. E01's 2026 actions are A03 and A04, both affirmations (BBB, F2). Its only downgrade was A02 in 2025.

**Q3.** No, BB+. I02 was assigned BBB (A23) and downgraded to BB+ (A07, 2025-06-20).

**Q4.** Positive (POS). E02 and E03 share an LEI, so they are one entity; the latest LTIDR action is A09 (2025-09-15), an affirmation at A with a positive outlook.

**Q5.** E02 (Northwind Holdings). I03's guarantor is E02, so the holder takes E02's credit risk, and the note is rated A (A11, 2025-09-15).

**Q6.** The Valdoria country ceiling is BB (A12), which caps foreign-currency ratings. Valdoria Telecom's FC rating (E05, BB, A14) sits at that cap, while its LC rating (BBB-, A13) is not capped.

**Q7.** Not settled by hand. I found roughly 30 issuers with 2026 downgrades, but the list is too long to verify reliably here, so it needs a query.

**Q8.** E08 (Saxby Shipping). A22 (2026-07-08) set RD, its only default rating, and nothing later overrides it.

**Q9.** Not settled by hand. Counting distinct LEIs with an in-force LTIDR rating on 1 Oct 2026 across roughly 350 records needs a query.

**Q10.** No. The headline FC rating is BB (A14). The LC rating of BBB- (A13) is investment grade but is not the headline.

**Q11.** BBB+. A36 (2024-09-30) downgraded E14 to BBB+, and nothing before 2025-06-01 changes it.

**Q12.** A-. A34 (2023-01-15) assigned A-, which held on 1 Jan 2024.

**Q13.** 1. A36 (2024-09-30) is the only downgrade; A35 is a watch placement, not a downgrade.

**Q14.** None. Halden Foods' first rating is A30 (2024-02-01), after 1 Jan 2024.

**Q15.** A-. E10 and E17 share an LEI, and A26 (2023-05-01) assigned A-. The downgrade to BBB+ (A27) came on 2026-04-15, after 1 Jan 2026.

**Q16.** No. The rating was BBB+ on 1 Jan 2025 and is still BBB+ (A33, 2026-05-01). The watch placement (A35) does not change the rating.

**Q17.** No. Orrin Bank AG (E06) was placed on Rating Watch Negative (A17, 2026-09-03) but not downgraded. Orrin Bancorp (E13) is a different LEI and has no 2026 downgrade either.

**Q18.** Not settled by hand. Several issuers appear to be on RWN, including E06, E1006, E1098 and E1238, but the list needs a full query, and some watches are years old with no follow-up action.

**Q19.** Not settled by hand. This needs a full query over the latest outlook of each in-force issuer rating.

**Q20.** No. Pellam's rating was withdrawn (A19, 2026-05-12). Its last rating was BB, not a default.

**Q21.** Not settled by hand. The set includes withdrawn-without-later-rating cases such as E07, E1057 and E1159, but the full list needs a query.

**Q22.** E08. It is the only entity with an RD or D rating (A22).

**Q23.** F2. The short-term rating is A04 (2026-02-10, affirmed).

**Q24.** Yes. The latest FC long-term rating is BBB (A03, 2026-02-10).

**Q25.** Not settled by hand. This needs instrument-level latest ratings as of 1 Oct 2026 across about 100 instruments.

**Q26.** A+. The local-currency rating is A40 (2024-03-01).

**Q27.** A-. I06 was assigned A- (A42, 2024-03-01).

**Q28.** BBB+. The Republic of Corvenia's FC issuer rating is A38 (2024-01-01).

**Q29.** None. The only VD record is a Country Ceiling (A12, BB), which the ontology says is not the sovereign's issuer rating.

**Q30.** At the VD ceiling (BB): E05, E1028, E1101, E1126, E1236. At the CV ceiling (A, A37): E15, E1039, E1194. E1039 and E1194 are on Rating Watch but still rated A.

**Q31.** No. No VD-domiciled entity has an FC rating above BB, and no CV-domiciled entity has one above A, on 1 Oct 2026.

**Q32.** E09 (Halden Group plc). The chain is E11→E10→E09, and E09 has no parent.

**Q33.** E10 (Halden Bank AG) is the guarantor, so it carries the risk. I05 is rated BBB+ after the downgrade in A29 (2026-04-15).

**Q34.** No. E12 has no parent link and a different LEI, so it is not in the Halden Group (E09, E10, E11).

**Q35.** 3: E09, E10 and E11. E17 is the same entity as E10.

**Q36.** 2: E02 and E04. E03 is the same entity as E02.

**Q37.** Not settled by hand. The count needs LEI de-duplication across about 350 non-QA records. VD and CV have no LEI but are still entities.

**Q38.** No. The LEIs differ (549300AMVE3VRVG7HK43 vs 815600O8X8K2F154N214).

**Q39.** A. E02/E03's latest LTIDR action is A09 (2025-09-15, affirmed at A).

**Q40.** Not settled by hand. This needs a count of GB-domiciled issuers with in-force ratings on 1 Oct 2026.

**Q41.** None. E16 is a QA record, so its actions must be ignored.

**Q42.** LU. The RESEARCH record E17 holds the country, and it overrides RATINGS' DE for E10.

**Q43.** 1: E10/E17 (Halden Bank), the only LU-domiciled entity.

**Q44.** Yes. XVD is Valdoria's domestic currency, and I07 is denominated in XVD.

**Q45.** No. The ceiling caps FC ratings only, and I07 is local-currency debt, so it is not capped.

**Q46.** No. E11 has only a credit opinion (A46, CO), which the ontology says is not a rating.

**Q47.** None. I08's only action is EX (A47), an expected rating that is not yet in force.

**Q48.** Not settled by hand. This needs a query over instrument ratings in force on 1 Oct 2026.

```json
{
  "Q1": {"rating": "A-"},
  "Q2": {"downgraded": "no"},
  "Q3": {"investment_grade": "no", "rating": "BB+"},
  "Q4": {"outlook": "POS"},
  "Q5": {"risk_of": "E02", "rating": "A"},
  "Q7": {"issuers": null},
  "Q8": {"entities": ["E08"]},
  "Q9": {"count": null},
  "Q10": {"investment_grade": "no"},
  "Q11": {"rating": "BBB+"},
  "Q12": {"rating": "A-"},
  "Q13": {"count": 1},
  "Q14": {"rating": "none"},
  "Q15": {"rating": "A-"},
  "Q16": {"changed": "no"},
  "Q17": {"downgraded": "no"},
  "Q18": {"issuers": null},
  "Q19": {"issuers": null},
  "Q20": {"in_default": "no"},
  "Q21": {"entities": null},
  "Q22": {"entities": ["E08"]},
  "Q23": {"rating": "F2"},
  "Q24": {"investment_grade": "yes", "rating": "BBB"},
  "Q25": {"count": null},
  "Q26": {"rating": "A+"},
  "Q27": {"rating": "A-"},
  "Q28": {"rating": "BBB+"},
  "Q29": {"rating": "none"},
  "Q30": {"entities": ["E05", "E1028", "E1101", "E1126", "E1236", "E15", "E1039", "E1194"]},
  "Q31": {"any": "no"},
  "Q32": {"parent": "E09"},
  "Q33": {"risk_of": "E10", "rating": "BBB+"},
  "Q34": {"same_group": "no"},
  "Q35": {"count": 3},
  "Q36": {"count": 2},
  "Q37": {"count": null},
  "Q38": {"same": "no"},
  "Q39": {"rating": "A"},
  "Q40": {"count": null},
  "Q41": {"rating": "none"},
  "Q42": {"country": "LU"},
  "Q43": {"count": 1},
  "Q44": {"local_currency": "yes"},
  "Q45": {"above_ceiling": "no"},
  "Q46": {"issuer_rating": "no"},
  "Q47": {"rating": "none"},
  "Q48": {"count": null}
}
```