Counting conventions, since the data has no schema notes. "Research work" means type ART, REV or PPR. I excluded EDT, ERR, PTX and SUP, and PPRs that are `version_of` another work in the data. I also excluded `record_source` STG, which I read as staging records. Retracted works are kept, since the retraction flag is a status rather than a document type. Authors are identified by ORCID. Institution roll-ups follow `parent_id`. Most counts were tallied by hand across the whole dataset, so the larger ones (Q9, Q10, Q16) are the most likely to be off by a few.

**Q1.** 3. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229. A04 (…8662-8360) and A102 (…4738-8328) are different people.
**Q2.** 32 works. Mara Ellison is A01, A02, A03 and A101 (same ORCID); the full list is in the JSON.
**Q3.** No. W37's Jonas Brandt is A05 (ORCID …6105-5008) and W38's is A06 (…5475-1779).
**Q4.** 9. A05 plus A104 (same ORCID) gives W14, W37, W554, W565, W785, W792, W1038, W702 and W725. W556 is a preprint of W1038, so it is not counted separately.
**Q5.** No. W08's M. Ellison is A04 (…8662-8360), not A01 (…9841-6229).
**Q6.** A01. Mara Ellison has 23 research works at I02. The next highest are A110 and A07 with 15 each.
**Q7.** 23. Of her 32 works, W04, W05, W271, W813, W936 and W949 are EDT or ERR. W02, W612 and W663 are preprints of W03, W869 and W464.
**Q8.** I01. I04 → I03 → I02 → I01.
**Q9.** 119. This covers I02, I03, I04, I06 and I19.
**Q10.** 176. That is the 119 above plus 57 from I05, I20 and I21.
**Q11.** 70. This covers I07, I08 and I22.
**Q12.** Full 15, fractional 13.0. Fifteen 2024 works have a Kesting author. For example, W203 gives 5/6 and W21 gives 2/4.
**Q13.** Full: I09 (16 vs 15). Fractional: I07 (13.0 vs 4.0). Each of Rostval's 16 works has one Rostval author out of four, so each is worth 0.25.
**Q14.** Full 50, fractional 45.75. Fifty 2024 works have a GB-affiliated author, and each author's share goes to their institution's country.
**Q15.** 27. This includes the retracted W520 and W922.
**Q16.** 89.
**Q17.** W04, W05, W271, W813, W936 and W949. These are editorials (EDT) and errata (ERR).
**Q18.** 15. A07's 18 records minus W05 (ERR) and the preprints W02 and W219. A108 (ORCID …1802-8393) is a different person.
**Q19.** 30. Distinct citers of W02 or W03.
**Q20.** The 23 preprints listed in the JSON, each pointing to a work in the data through `version_of`.
**Q21.** 47.
**Q22.** Total: W30 (18 vs 13 across W31 and W42). In window: W31 (13 vs 2). W30's window is 2019–2021 and only W60 and W988 fall in it, while all 13 citers of W31/W42 are from 2023–2025.
**Q23.** Total 18, in window 2 (W60, W988).
**Q24.** 15. A09 plus A103 (same ORCID), excluding the STG records W268, W714 and W802.
**Q25.** 42. Citation counts: W20 14, W21 3, W22 19, W23 1, W366 1, W417 2, W531 1, W967 1; the other seven works have none.
**Q26.** Yes. W23 is an article in I07's output, and its retraction is a flag rather than a document type. If you exclude retracted works, it drops out.
**Q27.** I12 (Université de Lorvain), with 16 citing works. Next are I11 with 5, then I09 and I14 with 4 each.
**Q28.** 4. These are W32, W357, W586 and W777.
**Q29.** Author 7, institution 12, country 21. The author-level matches are the citers by Mara Ellison or A07: W12, W13, W598, W676, W833, W843 and W1048. W16 and W890 are by a different M. Ellison (A04), and W1056 is by A102.
**Q30.** 18. The 12 Albury citers plus W14, W214, W349, W544, W748 and W812.
**Q31.** W50, W51, W52, W90, W337, W338, W396, W546, W682, W801, W844, W895, W922 and W1042. The citers of W01 are W40, W41, W229, W602, W657, W660, W844 and W895.
**Q32.** 20. The 8 direct citers plus the second-hop citers, with W844 and W895 in both groups.
**Q33.** W22, with 19 citations. W20 is next with 14.
**Q34.** 7. These are W08, W16, W260, W603, W693, W850 and W956. The STG records W90–92, W268, W329 and others are excluded.
**Q35.** 25.
**Q36.** 26.
**Q37.** I04. W70 has A08 at I04 (`affil_seq` 1) and also at I06 (`affil_seq` 2).
**Q38.** I01, I02, I03, I04 and I06. I06 rolls up to I02 and I01; I04 rolls up through I03 to I02 and I01.
**Q39.** 21. This assumes K3 is the highest tier, which makes S01 the only highest-tier source.
**Q40.** S01. The data does not define the tier scale, so this assumes a larger number is a higher tier.
**Q41.** Depends. S03 is K1 and S02 is K2, so the answer flips with the direction of the K scale, which the data does not state.
**Q42.** 13.
**Q43.** Yes. W07 is an ART, not retracted, and its source being K0 does not change that.
**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21.
**Q45.** 22.
**Q46.** I01. I06 → I02 → I01.
**Q47.** The ranking depends on how credit is split. Rostval leads on full counting because it has more works (16 vs 15). Each of those works has only one Rostval author out of four, so fractionally it gets just 4.0. Kesting's works are mostly written by Kesting authors, so it keeps 13.0.
**Q48.** The premise is wrong. W70's affiliations (I04 and I06) both roll up to I02, so W70 is one of the University of Albury's research works and is counted once. Two affiliations in the same university do not double-count.

```json
{"Q1":{"count":3},
"Q2":{"works":["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
"Q3":{"same":"no"},
"Q4":{"count":9},
"Q5":{"same":"no"},
"Q6":{"author":"A01"},
"Q7":{"count":23},
"Q8":{"parent":"I01"},
"Q9":{"count":119},
"Q10":{"count":176},
"Q11":{"count":70},
"Q12":{"full":15,"fractional":13.0},
"Q13":{"full":"I09","fractional":"I07"},
"Q14":{"full":50,"fractional":45.75},
"Q15":{"count":27},
"Q16":{"count":89},
"Q17":{"works":["W04","W05","W271","W813","W936","W949"]},
"Q18":{"count":15},
"Q19":{"count":30},
"Q20":{"works":["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
"Q21":{"count":47},
"Q22":{"more_in_total":"W30","more_in_window":"W31"},
"Q23":{"total":18,"in_window":2},
"Q24":{"count":15},
"Q25":{"count":42},
"Q26":{"counts":"yes"},
"Q27":{"institution":"I12","citing_works":16},
"Q28":{"count":4},
"Q29":{"author":7,"institution":12,"country":21},
"Q30":{"count":18},
"Q31":{"works":["W50","W51","W52","W90","W337","W338","W396","W546","W682","W801","W844","W895","W922","W1042"]},
"Q32":{"count":20},
"Q33":{"work":"W22"},
"Q34":{"count":7},
"Q35":{"count":25},
"Q36":{"count":26},
"Q37":{"institution":"I04"},
"Q38":{"institutions":["I01","I02","I03","I04","I06"]},
"Q39":{"count":21},
"Q40":{"source":"S01"},
"Q41":{"higher":"depends"},
"Q42":{"count":13},
"Q43":{"research":"yes"},
"Q44":{"institutions":["I02","I03","I04","I05","I06","I19","I20","I21"]},
"Q45":{"count":22},
"Q46":{"parent":"I01"}}
```