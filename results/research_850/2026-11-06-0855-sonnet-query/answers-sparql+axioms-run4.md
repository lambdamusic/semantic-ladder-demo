**Q1.** 1. A01, A02, A03 and A101 are linked by `samePersonAs` and share ORCID 0000-0002-9841-6229.
**Q2.** 32 works: W01–W07, W1005, W1048, W1050, W12, W19, W206, W238, W271, W374, W449, W464, W555, W612, W663, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984. These are the authorships of A01, A02, A03 and A101.
**Q3.** No. W37's Jonas Brandt is A05 (I05) and W38's is A06 (I12). They have different ORCIDs and no `samePersonAs` link.
**Q4.** 9, counted from `hasPerson` for A05, which merges A104.
**Q5.** No. A04 has a different ORCID and no `samePersonAs` link to Mara Ellison.
**Q6.** A01, with 19 research works credited to I02 or its units.
**Q7.** 19.
**Q8.** I01.
**Q9.** 95.
**Q10.** 140.
**Q11.** 59.
**Q12.** Full counting gives 13 and fractional counting gives 11. The fractional figure is my own calculation and I did not cross-check it.
**Q13.** Rostval (I09) has more under full counting, with 16 against 13 for Kesting. Kesting (I07) has more under fractional counting, with 11 against 4 for Rostval.
**Q14.** Full counting gives 46 and fractional counting gives 42.
**Q15.** 25.
**Q16.** 88, summed over 2019–2025.
**Q17.** W04, W271 and W936 are editorials; W05, W813 and W949 are errata. I did not list the preprints W02, W612 and W663, because those drop out by counting as their published versions.
**Q18.** 15. A108 is a different person, with a different ORCID.
**Q19.** 27.
**Q20.** 23 preprints have a published version in the data: W226, W1049, W432, W210, W416, W506, W611, W219, W460, W663, W877, W263, W407, W42, W556, W612, W522, W728, W524, W730, W545, W322, W02.
**Q21.** 45.
**Q22.** W30 has more citations in total, with 16 against 11. W31 has more within its publication year and the two years after, with 11 against 2.
**Q23.** W30 has 16 in total and 2 within 2019–2021.
**Q24.** 12.
**Q25.** 20.
**Q26.** No. W23 is retracted, so it is not a research work.
**Q27.** I12, with 12 citing works.
**Q28.** 4.
**Q29.** Of the 27 citing works, 7 are author self-citations, 10 are University of Albury self-citations and 20 are country self-citations.
**Q30.** 14.
**Q31.** W682, W1042, W338, W52, W51, W895, W337, W546, W801, W50, W396.
**Q32.** 17. This is 7 works citing W01 plus 11 citing those, minus 1 overlap (W895).
**Q33.** W20, with 13 citations.
**Q34.** 7.
**Q35.** 25.
**Q36.** 36.
**Q37.** I06.
**Q38.** I01, I02, I03 and I04. W71's authorship also lists I06, but I06 does not appear among its credited institutions.
**Q39.** 19, in S01. The ranking gives K3 rank 1, and S01 is the only K3 source.
**Q40.** S01.
**Q41.** No. S03 is K1, which has rank 3 and is lower than S02's K2 at rank 2.
**Q42.** 0. S04 is tier K0 and has no research works.
**Q43.** No. W07 is in S04, so it is not a research work.
**Q44.** I02, I03, I04, I05, I19, I20.
**Q45.** 16.
**Q46.** I06. It lists I02 as parent, but its derived ultimate parent and `countsTowards` are I06 alone.
**Q47.** Rostval has more works (16 against 13) but with more authors per work, so its fractional shares are smaller. Kesting's works have fewer authors, so each share is larger.
**Q48.** W70's credited institution is I06 only. I06 counts towards itself only, not towards I02, so W70 is not one of the University of Albury's works. The Tessel Laboratory (I04) is not among its credited institutions.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},"Q3":{"same":"no"},"Q4":{"count":9},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":19},"Q8":{"parent":"I01"},"Q9":{"count":95},"Q10":{"count":140},"Q11":{"count":59},"Q12":{"full":13,"fractional":11},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":46,"fractional":42},"Q15":{"count":25},"Q16":{"count":88},"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},"Q18":{"count":15},"Q19":{"count":27},"Q20":{"works":["W226","W1049","W432","W210","W416","W506","W611","W219","W460","W663","W877","W263","W407","W42","W556","W612","W522","W728","W524","W730","W545","W322","W02"]},"Q21":{"count":45},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":16,"in_window":2},"Q24":{"count":12},"Q25":{"count":20},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":12},"Q28":{"count":4},"Q29":{"author":7,"institution":10,"country":20},"Q30":{"count":14},"Q31":{"works":["W682","W1042","W338","W52","W51","W895","W337","W546","W801","W50","W396"]},"Q32":{"count":17},"Q33":{"work":"W20"},"Q34":{"count":7},"Q35":{"count":25},"Q36":{"count":36},"Q37":{"institution":"I06"},"Q38":{"institutions":["I01","I02","I03","I04"]},"Q39":{"count":19},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},"Q45":{"count":16},"Q46":{"parent":"I06"}}
```