**Q1.** 1. A01, A02, A03 (and A101) share ORCID 0000-0002-9841-6229, so they are one person.

**Q2.** 32 works: the 29 listed below plus W01, W02, W03 and the rest of the list. They come from A01, A02, A03 and A101, which share one ORCID. A04 is a different ORCID, so W08 is excluded.

**Q3.** No. A05 (W37) and A06 (W38) have different ORCIDs.

**Q4.** 9. Taking the person by ORCID, A05 and A104 together have 9 research works (A05 alone has 7).

**Q5.** No. A04 has a different ORCID from A01.

**Q6.** A01, with 19 research works credited to I02 and its units.

**Q7.** 19.

**Q8.** I01. The chain is I04 → I03 → I02 → I01.

**Q9.** 95.

**Q10.** 140.

**Q11.** 59.

**Q12.** Full 13, fractional 11.0.

**Q13.** Full: I09 (16 against 13). Fractional: I07 (11.0 against 4.0).

**Q14.** Full 46, fractional 42.0.

**Q15.** 25.

**Q16.** 88.

**Q17.** W04, W271 and W936 are editorials. W05, W813 and W949 are errata.

**Q18.** 15.

**Q19.** 27. Citing works are counted once across W02 and W03.

**Q20.** The 23 preprints with version_of set to a work that is also in the data are listed in the JSON.

**Q21.** 45.

**Q22.** In total W30 has more (16 against 11). Within the publication year and the two years after, W31 has more (11 against 2).

**Q23.** Total 16, within the window 2.

**Q24.** 12. I counted the person by ORCID, so A09 and A103 together give 12 (A09 alone has 9).

**Q25.** 20.

**Q26.** No. W23 is retracted, so it is not research output.

**Q27.** I12, with 12 citing works.

**Q28.** 4.

**Q29.** Author 7, institution 10, country 20.

**Q30.** 14.

**Q31.** 11 works, listed in the JSON.

**Q32.** 17.

**Q33.** W20, with 13 citations.

**Q34.** 7.

**Q35.** 25.

**Q36.** 36.

**Q37.** I06. W70 lists I04 at sequence 1 and I06 at sequence 2, and only the last one is credited. I06 is an affiliated institute, so nothing above it is credited.

**Q38.** I04, I03, I02 and I01. W71's last-listed affiliation is I04, and credit passes up through its parents.

**Q39.** 19.

**Q40.** S01.

**Q41.** No. S03 is K1 and S02 is K2.

**Q42.** 0. S04 is delisted (K0).

**Q43.** No. W07 appeared in S04, which is delisted.

**Q44.** I02, I03, I04, I19, I05 and I20. The affiliated institutes I06 and I21 are excluded.

**Q45.** 16.

**Q46.** I06. It is an affiliated institute, so it is its own ultimate parent.

**Q47.** Kesting (I07) has fewer works in 2024 than Rostval (I09) under full counting (13 against 16). Under fractional counting it has more (11.0 against 4.0). Rostval's works have many authors, so each work's share is split thin. Kesting's works have few authors, so its shares stay large.

**Q48.** W70's author lists I04 (under I02) at sequence 1 and I06 at sequence 2. Only the last-listed affiliation is credited, so W70 is credited to I06. I06 is an affiliated institute, so its works never roll up to I02.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},"Q3":{"same":"no"},"Q4":{"count":9},"Q5":{"same":"no"},"Q6":{"author":"A01"},"Q7":{"count":19},"Q8":{"parent":"I01"},"Q9":{"count":95},"Q10":{"count":140},"Q11":{"count":59},"Q12":{"full":13,"fractional":11},"Q13":{"full":"I09","fractional":"I07"},"Q14":{"full":46,"fractional":42},"Q15":{"count":25},"Q16":{"count":88},"Q17":{"works":["W04","W271","W936","W05","W813","W949"]},"Q18":{"count":15},"Q19":{"count":27},"Q20":{"works":["W02","W1049","W210","W219","W226","W263","W322","W407","W416","W42","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877"]},"Q21":{"count":45},"Q22":{"more_in_total":"W30","more_in_window":"W31"},"Q23":{"total":16,"in_window":2},"Q24":{"count":12},"Q25":{"count":20},"Q26":{"counts":"no"},"Q27":{"institution":"I12","citing_works":12},"Q28":{"count":4},"Q29":{"author":7,"institution":10,"country":20},"Q30":{"count":14},"Q31":{"works":["W1042","W337","W338","W396","W50","W51","W52","W546","W682","W801","W895"]},"Q32":{"count":17},"Q33":{"work":"W20"},"Q34":{"count":7},"Q35":{"count":25},"Q36":{"count":36},"Q37":{"institution":"I06"},"Q38":{"institutions":["I04","I03","I02","I01"]},"Q39":{"count":19},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":0},"Q43":{"research":"no"},"Q44":{"institutions":["I02","I03","I04","I19","I05","I20"]},"Q45":{"count":16},"Q46":{"parent":"I06"}}
```