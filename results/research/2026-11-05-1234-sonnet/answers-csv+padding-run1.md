**Assumptions:**
- Research works are ART, REV and PPR. EDT, ERR, PTX and SUP are not.
- A preprint is merged into its published version.
- STG (staging) records are excluded, including as citers.
- Authors are identified by ORCID.
- K3 is taken as the highest tier, but the data doesn't define the tier order.
- A retracted work still counts, flagged.
- I06 rolls up to I02 through parent_id.

**Q1.** 1. A01, A02 and A03 share one ORCID; A04 has a different one.
**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19 (A01, A02 and A03 combined).
**Q3.** No. A05 and A06 have different ORCIDs.
**Q4.** 2. A05 wrote W14 and W37.
**Q5.** No. A04 (W08) has a different ORCID from A01.
**Q6.** A01. As one person she has 6 research works (W01, W03, W06, W07, W12, W19) at I02. Priya Ramanathan has 4.
**Q7.** 6. W02 is the preprint of W03, and W04 (EDT) and W05 (ERR) are not research.
**Q8.** I01, via I04 → I03 → I02 → I01.
**Q9.** 12: W01, W03, W06, W07, W12, W13, W19, W70, W71, W72, W73, W74.
**Q10.** 16. Add W14, W28, W29, W37 from I05 to the 12 above.
**Q11.** 6: W08, W16, W20, W21, W22, W23. W24 is SUP and W90–W92 are STG.
**Q12.** Full 3, fractional 2.0. W20 gives 0.5, W21 gives 0.5, and W22 gives 1.
**Q13.** Full: I09 (4 vs 3). Fractional: I07 (2.0 vs 1.0).
**Q14.** Full 7, fractional 6.0. The works are W06, W12, W13, W28, W29, W71 and W72; W28 and W29 give GB 0.5 each.
**Q15.** 4: W12, W21, W28, W51.
**Q16.** 10: W01, W08, W13, W20, W29, W31, W32, W52, W71, W74.
**Q17.** W04 (editorial) and W05 (erratum).
**Q18.** 4: W01, W03 (with W02), W13, W72.
**Q19.** 7: W12–W18.
**Q20.** W02 (of W03) and W42 (of W31).
**Q21.** 4: W27, W31 (with W42), W39, W50.
**Q22.** W30 has more in total (5 vs 4). W31 has more in its window (4 vs 1).
**Q23.** Total 5. In the window 2019–2021 it has 1, from W60.
**Q24.** 4: W20, W21, W22, W23.
**Q25.** 7. W20 has 3 (W32, W35, W36), W21 has 2 (W33, W36), W22 has 1 (W34), and W23 has 1 (W39).
**Q26.** Yes. W23 is a retracted ART, still counted but flagged (`is_retracted` = true).
**Q27.** I12, with 3 citing works: W33, W34 and W35.
**Q28.** 1, which is W32.
**Q29.** Author 2 (W12, W13), institution 2 (W12 at I02, W13 at I03), country 4 (W12, W13, W14, W15, all GB).
**Q30.** 3: W12, W13 and W14 (I05).
**Q31.** W50, W51, W52. W01 is cited by W40 and W41; W90 would also qualify but is STG.
**Q32.** 5: W40, W41, W50, W51, W52.
**Q33.** W20, with 3 citations. W22 has only W34 once the STG citers W90–W92 are set aside.
**Q34.** 2: W08 and W16.
**Q35.** 1, which is W21.
**Q36.** 0. S06 holds only W17 and W24 (SUP) and W76 (EDT).
**Q37.** I04, listed first. I06 is its second affiliation.
**Q38.** I06, I04, I03, I02, I01.
**Q39.** 4: W01, W13, W71, W74, all in S01.
**Q40.** S01 (K3), if K3 is highest.
**Q41.** Depends. S03 is K1 and S02 is K2; it is "no" if higher K numbers mean higher tiers, but the data doesn't define the order.
**Q42.** 2: W07 and W75.
**Q43.** Yes. W07 is an ART.
**Q44.** I02, I03, I04, I05, I06.
**Q45.** 4: W70, W71, W73, W74.
**Q46.** I01, via I06 → I02 → I01.

**Q47.** Rostval has more works in 2024 (4 vs 3), but each is a four-author paper with one Rostval author, which gives 0.25 each (1.0 total). Kesting has the sole-authored W22 (1) plus half shares of W20 and W21 (2.0 total), so it leads on fractional counting.

**Q48.** The premise is wrong. W70's author A08 lists I04, which sits under I03, I02 and I01, so W70 is credited to the University of Albury.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19"]},"Q3":{"same":"no"},"Q4":{"count":2},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":6},"Q8":{"parent":"I01"},"Q9":{"count":12},"Q10":{"count":16},"Q11":{"count":6},"Q12":{"full":3,"fractional":2},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":7,"fractional":6},"Q15":{"count":4},"Q16":{"count":10},"Q17":{"works":["W04","W05"]},"Q18":{"count":4},"Q19":{"count":7},"Q20":{"works":["W02","W42"]},"Q21":{"count":4},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":5,"in_window":1},"Q24":{"count":4},"Q25":{"count":7},"Q26":{"counts":"yes"},"Q27":{"institution":"I12","citing_works":3},"Q28":{"count":1},"Q29":{"author":2,"institution":2,"country":4},"Q30":{"count":3},"Q31":{"works":["W50","W51","W52"]},"Q32":{"count":5},"Q33":{"work":"W20"},"Q34":{"count":2},"Q35":{"count":1},"Q36":{"count":0},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":4},"Q40":{"source":"S01"},"Q41":{"higher":"depends"},"Q42":{"count":2},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06"]},"Q45":{"count":4},"Q46":{"parent":"I01"}}
```