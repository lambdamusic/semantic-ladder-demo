I ran out of query rounds, so only some answers are fully supported. Entries marked *unresolved* (null in the JSON) could not be computed from what I retrieved.

I treated articles and reviews as research works. I excluded editorials, errata, front matter, supplements, retracted works and preprints (the preprint's published version is counted instead).

**Q1.** 1. A01, A02 and A03 all carry ORCID 0000-0002-9841-6229.
**Q2.** 26 works, using A01, A02 and A03 as one person: W01, W04, W05, W06, W1005, W12, W238, W271, W374, W464, W676, W813, W949 (A01); W02, W07, W1048, W1050, W19, W449, W663, W869, W972 (A02); W03, W206, W763, W817 (A03). Another record with that ORCID, A101, may add more, but its rows were not shown.
**Q3.** No. A05 and A06 have different ORCIDs.
**Q4.** 7. A05 has W1038, W14, W37, W554, W565, W785 and W792. A104 (J. Brandt) shares A05's ORCID, but its works were not shown.
**Q5.** No. A04 (the M. Ellison of W08) has a different ORCID from A01.
**Q6.** Unresolved.
**Q7.** 17, from A01, A02 and A03 (A101 not counted).
**Q8.** I01. The chain is I04 → I03 → I02 → I01.
**Q9.** 116, summed from the per-year counts for I02.
**Q10.** 171, summed from the per-year counts for I01.
**Q11–Q16.** Unresolved.
**Q17.** W04 (editorial), W271 (editorial), W05, W813 and W949 (errata). W374 is retracted, but that is not a document-type reason.
**Q18.** 15. These are W01, W03, W13, W251, W262, W292, W293, W435, W553, W598, W72, W758, W787, W833 and W969. The preprints W02 and W219 and the erratum W05 are excluded.
**Q19.** 30. W02 has 9 citing works and W03 has 26, with 5 in common (W15, W315, W397, W535, W843).
**Q20.** The 23 preprints with a `versionOf` link: W02, W1049, W210, W219, W226, W263, W322, W407, W416, W42, W432, W460, W506, W522, W524, W545, W556, W611, W612, W663, W728, W730, W877.
**Q21–Q25.** Unresolved.
**Q26.** Depends. W23 is by A09 at Kesting University, but I did not retrieve its type or retraction status.
**Q27–Q36.** Unresolved.
**Q37.** I04. W70 lists I04 and I06 under the same author, with I04 first.
**Q38.** I06 and I04, plus their ancestors I03, I02 and I01.
**Q39.** Unresolved.
**Q40.** S01, assuming K3 is the highest tier. The tier scale is not documented, so this is an inference.
**Q41.** No, under the same assumption (S03 is K1, S02 is K2).
**Q42.** Unresolved.
**Q43.** Yes. W07 is an article from the main feed and is not retracted.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** Unresolved.
**Q46.** I01. The chain is I06 → I02 → I01.
**Q47, Q48.** Unresolved. I did not retrieve the data needed to explain these.

```json
{"Q1":{"count":1},"Q2":{"works":["W01","W04","W05","W06","W1005","W12","W238","W271","W374","W464","W676","W813","W949","W02","W07","W1048","W1050","W19","W449","W663","W869","W972","W03","W206","W763","W817"]},"Q3":{"same":"no"},"Q4":{"count":7},"Q5":{"same":"no"},"Q6":{"author":null},"Q7":{"count":17},"Q8":{"parent":"I01"},"Q9":{"count":116},"Q10":{"count":171},"Q11":{"count":null},"Q12":{"full":null,"fractional":null},"Q13":{"full":null,"fractional":null},"Q14":{"full":null,"fractional":null},"Q15":{"count":null},"Q16":{"count":null},"Q17":{"works":["W04","W271","W05","W813","W949"]},"Q18":{"count":15},"Q19":{"count":30},"Q20":{"works":["W02","W1049","W210","W219","W226","W263","W322","W407","W416","W42","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877"]},"Q21":{"count":null},"Q22":{"more_in_total":null,"more_in_window":null},"Q23":{"total":null,"in_window":null},"Q24":{"count":null},"Q25":{"count":null},"Q26":{"counts":"depends"},"Q27":{"institution":null,"citing_works":null},"Q28":{"count":null},"Q29":{"author":null,"institution":null,"country":null},"Q30":{"count":null},"Q31":{"works":[]},"Q32":{"count":null},"Q33":{"work":null},"Q34":{"count":null},"Q35":{"count":null},"Q36":{"count":null},"Q37":{"institution":"I04"},"Q38":{"institutions":["I06","I04","I03","I02","I01"]},"Q39":{"count":null},"Q40":{"source":"S01"},"Q41":{"higher":"no"},"Q42":{"count":null},"Q43":{"research":"yes"},"Q44":{"institutions":["I02","I03","I04","I05","I06","I19","I20","I21"]},"Q45":{"count":null},"Q46":{"parent":"I01"}}
```