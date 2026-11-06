**Q1.** 3. The names resolve to A01 (Mara Ellison, merging A01/A02/A03/A101), A04 and A102. A04 and A102 are both "M. Ellison" but have different ORCIDs.

**Q2.** 29 works: W01, W03, W04, W05, W06, W07, W1005, W1048, W1050, W12, W19, W206, W238, W271, W374, W449, W464, W555, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984. The list comes from credits for A01, and W03 is the merged W02/W03.

**Q3.** No. W37 is credited to A05 (I05) and W38 to A06 (I12), who have different ORCIDs.

**Q4.** 9 research works for A05.

**Q5.** No. W08 is by A04 and W01 by A01, who have different ORCIDs.

**Q6.** A01, with 19 research works credited to I02 and its units.

**Q7.** 19 research works for Mara Ellison (A01).

**Q8.** I01. I04 sits under I03, which sits under I02, which sits under I01.

**Q9.** 95.

**Q10.** 140.

**Q11.** 59.

**Q12.** Full counting gives 13 and fractional counting gives 11.0 for I07 in 2024.

**Q13.** Under full counting I09 has more (16 vs 13). Under fractional counting I07 has more (11.0 vs 4.0).

**Q14.** GB institutions have 46 works under full counting and 42.0 under fractional counting.

**Q15.** 25.

**Q16.** 88.

**Q17.** W04, W05, W271, W813, W936 and W949. These are editorials (EDT) and errata (ERR). W07, W374, W449 and W763 are excluded for other reasons (delisted source or retraction).

**Q18.** 15.

**Q19.** 27 distinct citing works, counting citations to both W02 and W03.

**Q20.** None. Preprints are already merged into their published versions (for example W02 into W03). The remaining PPR works have no same-title counterpart in the data.

**Q21.** 45.

**Q22.** W30 has more citations in total (16 vs 11). W31 has more within its publication year and the two years after (11 vs 2).

**Q23.** W30 has 16 citations in total and 2 within the window.

**Q24.** 12.

**Q25.** 20.

**Q26.** No. W23 is retracted and not research output.

**Q27.** I12, with 12 citing works.

**Q28.** 4.

**Q29.** Of the 27 citing works, 7 are author self-citations, 10 are I02 self-citations and 20 are country self-citations.

**Q30.** 14.

**Q31.** W1042, W337, W338, W396, W50, W51, W52, W546, W682, W801 and W895.

**Q32.** 17.

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 25.

**Q36.** 36.

**Q37.** I06. W70 is credited to I06 through author A08.

**Q38.** I04, I03, I02 and I01. W71 is credited to I04, which rolls up through I03 and I02 to I01.

**Q39.** 19 works, all in S01.

**Q40.** S01.

**Q41.** No. S03 has tier_rank 3 and S02 has tier_rank 2, and a lower rank number means a higher tier.

**Q42.** 0. S04 is delisted, so none of its works are research output.

**Q43.** No. W07 is in the delisted source S04.

**Q44.** I02, I03, I04, I05, I19 and I20. I06 is only affiliated and does not roll up.

**Q45.** 16.

**Q46.** I01, following the parent_id chain I06 to I02 to I01. This is ambiguous, because I06 is an affiliate whose works count only towards itself.

**Q47.** I09 has more works in total (16 vs 13) but they are heavily co-authored with other institutions and countries. I07 therefore overtakes it under fractional counting (11 vs 4).

**Q48.** W70's author is credited to I06, an affiliate whose institution_units row counts only towards itself. I06's works do not roll up to I02, unlike I04 (Tessel), which does roll up.

```json
{"Q1":{"count":3},"Q2":{"works":["W01","W03","W04","W05","W06","W07","W1005","W1048","W1050","W12","W19","W206","W238","W271","W374","W449","W464","W555","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984"]},"Q3":{"same":"no"},"Q4":{"count":9},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":19},"Q8":{"parent":"I01"},"Q9":{"count":95},"Q10":{"count":140},"Q11":{"count":59},"Q12":{"full":13,"fractional":11},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":46,"fractional":42},"Q15":{"count":25},"Q16":{"count":88},"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},"Q18":{"count":15},"Q19":{"count":27},"Q20":{"works":[]},"Q21":{"count":45},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":16,"in_window":2},"Q24":{"count":12},"Q25":{"count":20},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":12},"Q28":{"count":4},"Q29":{"author":7,"institution":10,"country":20},"Q30":{"count":14},"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W895"]},"Q32":{"count":17},"Q33":{"work":"W20"},"Q34":{"count":7},"Q35":{"count":25},"Q36":{"count":36},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":19},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I05","I19","I20"]},"Q45":{"count":16},"Q46":{"parent":"I01"}}
```