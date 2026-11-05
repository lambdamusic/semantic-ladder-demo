Assumptions: research works are types ART, REV and standalone PPR. EDT, ERR, PTX and SUP are excluded, and preprint versions (W02, W42) are not counted separately from their published versions. Staging records (W90–W92, `record_source` STG) are excluded, along with their citations. Retracted W23 is counted. Institution hierarchy follows `parent_id`, so I06 sits under I02. People are matched by ORCID.

**Q1.** 1. A01, A02 and A03 share ORCID 0000-0002-9841-6229. A04 is a different person.
**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19. This takes A01, A02 and A03 together as one person.
**Q3.** No. W37 is by A05 and W38 is by A06, and they have different ORCIDs.
**Q4.** 2 (W14, W37).
**Q5.** No. W08 is by A04, whose ORCID differs from Mara Ellison's.
**Q6.** A01 (Mara Ellison). She has 6 works through her three records: W01, W06, W12, W07, W19, W03. A07 has 4.
**Q7.** 6 (W01, W03, W06, W07, W12, W19). W02 is a preprint of W03, so it is not counted separately.
**Q8.** I01, via I04 → I03 → I02 → I01.
**Q9.** 12 (W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74).
**Q10.** 16. These are the 12 above plus W14, W28, W29 and W37 from I05.
**Q11.** 6 (W08, W16, W20, W21, W22, W23).
**Q12.** Full 3, fractional 2.0. The works are W20, W21 and W22, worth 0.5, 0.5 and 1.
**Q13.** Full counting favours I09 (4 vs 3), fractional favours I07 (2.0 vs 1.0). I09's works are W21, W27, W28 and W29, and it is one of four authors on each.
**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28, W29, W71 and W72, with W28 and W29 worth 0.5 each.
**Q15.** 4 (W12, W21, W28, W51).
**Q16.** 10 (W01, W08, W13, W20, W29, W31, W32, W52, W71, W74).
**Q17.** W04 (editorial) and W05 (erratum).
**Q18.** 4 (W01, W03/W02 counted once, W13, W72). W05 is an erratum.
**Q19.** 7 (W12, W13, W14, W15, W16, W17, W18).
**Q20.** W02 (of W03) and W42 (of W31).
**Q21.** 4 (W27, W31, W39, W50). W42 is the preprint of W31.
**Q22.** W30 has more in total (5 vs 4). W31 has more within its window (4 vs 1).
**Q23.** 5 in total, 1 in the window (W60 only).
**Q24.** 4 (W20, W21, W22, W23).
**Q25.** 7. W20 has 3, W21 has 2, W22 has 1 (W34) and W23 has 1.
**Q26.** Depends. W23 is an ART from I07, but it is flagged `is_retracted`, and the data gives no rule for retractions.
**Q27.** I12, with 3 citing works (W33, W34, W35).
**Q28.** 1 (W32).
**Q29.** Author 2, institution 2, country 4. Author-level self-citations are W12 and W13; W16's A04 is a different person. Institution-level are the same two, since I05 is outside I02. Country-level adds W14 and W15 (GB).
**Q30.** 3 (W12, W13, W14).
**Q31.** W50, W51, W52. W01 is cited by W40 and W41, and those are cited by W50, W51 and W52 (W90 is staging).
**Q32.** 5 (W40, W41, W50, W51, W52).
**Q33.** W20, with 3 citations.
**Q34.** 2 (W08, W16).
**Q35.** 1 (W21). W24 is a SUP.
**Q36.** 0. S06 holds only W17 and W24 (SUP) and W76 (EDT).
**Q37.** I04 (seq 1). A08 also lists I06 (seq 2), so W70 is credited to both.
**Q38.** I06 and I04, plus their parents I03, I02 and I01.
**Q39.** 4 (W01, W13, W71, W74). This assumes K3 is the highest tier; the data does not define the tier order.
**Q40.** S01, under the same assumption. If K0 were the top tier it would be S04.
**Q41.** Depends. Tier direction is undefined (K1 vs K2).
**Q42.** 2 (W07, W75).
**Q43.** Yes. W07 is an ART.
**Q44.** I02, I03, I04, I05, I06.
**Q45.** 4 (W70, W71, W73, W74).
**Q46.** I01, via I06 → I02 → I01. I06 is typed AFF (affiliate), so it may not be a true part of the system.
**Q47.** Rostval has more works in 2024 (4 vs 3), but it is one of four authors on each, so each gives it 0.25. Kesting has a sole-authored W22 and half shares of W20 and W21, so it leads on fractional counting.
**Q48.** The premise is wrong. I04 → I03 → I02, so W70 does count among the University of Albury's works (included in Q9).

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2.0},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6.0},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":7},"Q26":{"counts":"depends"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I04","I06","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"depends"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```