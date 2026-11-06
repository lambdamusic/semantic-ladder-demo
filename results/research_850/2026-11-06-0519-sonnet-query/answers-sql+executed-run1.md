**Q1.** 3. The names cover A01 (which merges A01, A02, A03 and A101), A04 and A102, who have different ORCIDs.
**Q2.** 29 works: W01, W03, W04, W05, W06, W07, W1005, W1048, W1050, W12, W19, W206, W238, W271, W374, W449, W464, W555, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984. These are all the credits for A01.
**Q3.** No. W37 is credited to A05 and W38 to A06, who have different ORCIDs.
**Q4.** 9. A05 has 9 research works, including W37 and W1038.
**Q5.** No. W08 is credited to A04 and W01 to A01, who have different ORCIDs.
**Q6.** A01, with 19 research works credited to I02 and its units.
**Q7.** 19.
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9.** 95.
**Q10.** 140.
**Q11.** 59.
**Q12.** Full 13, fractional 11.0.
**Q13.** Full: I09 (16 vs 13). Fractional: I07 (11 vs 4).
**Q14.** Full 46, fractional 42.
**Q15.** 25.
**Q16.** 88.
**Q17.** W04, W05, W271, W813, W936 and W949. These are editorials and errata. W07, W449 and W763 are excluded because their sources are delisted, and W374 because it is retracted.
**Q18.** 15.
**Q19.** 27.
**Q20.** None. The preprints in the data (PPR) have no matching published-version title, and merged preprints are already folded into their published works.
**Q21.** 45.
**Q22.** In total W30 has more (16 vs 11). Within the publication year and the two years after, W31 has more (11 vs 2).
**Q23.** 16 in total, 2 within the window.
**Q24.** 12.
**Q25.** 20.
**Q26.** No. W23 is retracted and not research output.
**Q27.** I12, with 12 citing works.
**Q28.** 4.
**Q29.** Author 7, institution 10, country 20.
**Q30.** 14.
**Q31.** W51, W50, W338, W546, W52, W337, W682, W1042, W801, W895, W396 (11 works).
**Q32.** 17.
**Q33.** W20, with 13 citations.
**Q34.** 7.
**Q35.** 25.
**Q36.** 36.
**Q37.** I06.
**Q38.** I04, I03, I02 and I01. W71 is credited to I04, and the unit table rolls it up through those levels.
**Q39.** 19.
**Q40.** S01.
**Q41.** No. S03 has tier_rank 3 and S02 has rank 2, so S03 is lower.
**Q42.** 0. S04 is delisted.
**Q43.** No. W07 is in delisted source S04.
**Q44.** I02, I03, I04, I05, I19 and I20. I06 is only affiliated and does not roll up in institution_units.
**Q45.** 16.
**Q46.** I01, going by parent_id (I06 → I02 → I01). However, I06 is an affiliate (AFF) that does not count towards I02 or I01, so it could also be read as having no counted parent.
**Q47.** I07's works have more co-authors from other institutions, so its fractional total (11.0) falls below I09's... I09 leads in full count (16 vs 13) but I07 leads fractionally (11.0 vs 4.0). I09's 2024 works are thus heavily shared with other institutions' authors.
**Q48.** W70 is credited to I06 (the Halloran Institute, an affiliate), not I04. Affiliates do not roll up to I02 in institution_units.

```json
{"Q1":{"count":3},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},"Q3":{"same":"no"},"Q4":{"count":9},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":19},"Q8":{"parent":"I01"},"Q9":{"count":95},"Q10":{"count":140},"Q11":{"count":59},"Q12":{"full":13,"fractional":11},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":46,"fractional":42},"Q15":{"count":25},"Q16":{"count":88},"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},"Q18":{"count":15},"Q19":{"count":27},"Q20":{"works":[]},"Q21":{"count":45},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":16,"in_window":2},"Q24":{"count":12},"Q25":{"count":20},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":12},"Q28":{"count":4},"Q29":{"author":7,"institution":10,"country":20},"Q30":{"count":14},"Q31":{"works":["W51","W50","W338","W546","W52","W337","W682","W1042","W801","W895","W396"]},"Q32":{"count":17},"Q33":{"work":"W20"},"Q34":{"count":7},"Q35":{"count":25},"Q36":{"count":36},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":19},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},"Q45":{"count":16},"Q46":{"parent":"I01"}}
```