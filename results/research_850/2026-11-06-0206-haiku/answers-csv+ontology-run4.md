**Q1.** 1. A01, A02 and A03 all carry ORCID 0000-0002-9841-6229, so they are one person.

**Q2.** W01, W02, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W612, W663, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050. This covers every record under that ORCID (A01, A02, A03, A101), of any type.

**Q3.** No. The two Jonas Brandt records have different ORCIDs (A05: 0000-0001-6105-5008; A06: 0000-0007-5475-1779), so they are different people.

**Q4.** 9. A05 and A104 share ORCID 0000-0001-6105-5008; their research works are W14, W37, W554, W565, W702, W725, W785, W792 and W1038, with preprint W556 counted once under its published version W1038.

**Q5.** No. M. Ellison (A04, ORCID 0000-0004-8662-8360) and Mara Ellison (A01, ORCID 0000-0002-9841-6229) have different ORCIDs.

**Q7.** 20. Of the 32 records for this person, I excluded editorials and errata (W04, W05, W271, W813, W936, W949), the retracted W374, and the K0-source works W07 and W449. I also merged W02 into W03, W612 into W869 and W663 into W464 as single works.

**Q8.** I01. I04 sits under I03, which sits under I02, which sits under the top-level system I01.

**Q15.** 25. I counted research-type records in S02 with year 2024, excluding the retracted W922 and the errata/editorial records. This is a hand count from a long scan, so treat it as likely but worth verifying.

**Q17.** W04, W05, W271, W813, W936, W949. These are the editorials (EDT) and errata (ERR) on that person's record.

**Q18.** 15. A07 is the only record with ORCID 0000-0009-2298-3695. Preprint W02 merges into W03, preprint W219 merges into W251, and erratum W05 and the STG-free set are excluded.

**Q24.** 12. A09 and A103 share ORCID 0000-0000-8073-7028. Excluded: W23 (retracted), W268 and W714 and W802 (STG), W693 (retracted) and W1025 (retracted).

**Q26.** No. W23 is retracted, so it is not research output.

**Q37.** I06. W70 lists A08 at I04 (seq 1) and I06 (seq 2), and the last-listed affiliation is the one credited.

**Q38.** I04, I03, I02, I01. W71's last-listed affiliation is I04, and it is credited to I04 and every institution above it.

**Q40.** S01. It is the only K3 source.

**Q41.** No. S03 is K1 and S02 is K2, so S03 is in a lower tier.

**Q42.** 0. S04 is K0 (delisted), so none of its works are research output.

**Q43.** No. W07 appeared in S04, a delisted K0 source.

**Q44.** I02, I03, I04, I05, I19, I20. These are the units below I01. I06 and I21 are affiliated institutes (AFF), so they are not units.

**Q45.** 16. These are the works whose last-listed affiliation is I06, which has no units: W70, W73, W74, W252, W378, W502, W617, W632, W664, W671, W672, W761, W926, W940, W1007, W1062.

**Q46.** I06. It is an affiliated institute, so its ultimate parent is itself.

**Q48.** W70's last-listed affiliation is I06 (seq 2), not the Tessel Laboratory I04 (seq 1). I06 is an affiliated institute, not a unit of I02, so the work is not credited to the University of Albury.

**Pending:** Q6, Q9–Q14, Q16, Q19–Q23, Q25, Q27–Q36, Q39, Q47. These need citation rollups, full-institution enumeration, or fractional counts. I'll work through them in the next pass.

```json
{"Q1": {"count": 1},
 "Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
 "Q3": {"same": "no"},
 "Q4": {"count": 9},
 "Q5": {"same": "no"},
 "Q6": {"author": null},
 "Q7": {"count": 20},
 "Q8": {"parent": "I01"},
 "Q9": {"count": null},
 "Q10": {"count": null},
 "Q11": {"count": null},
 "Q12": {"full": null, "fractional": null},
 "Q13": {"full": null, "fractional": null},
 "Q14": {"full": null, "fractional": null},
 "Q15": {"count": 25},
 "Q16": {"count": null},
 "Q17": {"works": ["W04","W05","W271","W813","W936","W949"]},
 "Q18": {"count": 15},
 "Q19": {"count": null},
 "Q20": {"works": ["W02","W42","W210","W219","W226","W263","W322","W407","W416","W432","W460","W506","W522","W524","W545","W556","W611","W612","W663","W728","W730","W877","W1049"]},
 "Q21": {"count": null},
 "Q22": {"more_in_total": null, "more_in_window": null},
 "Q23": {"total": null, "in_window": null},
 "Q24": {"count": 12},
 "Q25": {"count": null},
 "Q26": {"counts": "no"},
 "Q27": {"institution": null, "citing_works": null},
 "Q28": {"count": null},
 "Q29": {"author": null, "institution": null, "country": null},
 "Q30": {"count": null},
 "Q31": {"works": null},
 "Q32": {"count": null},
 "Q33": {"work": null},
 "Q34": {"count": null},
 "Q35": {"count": null},
 "Q36": {"count": null},
 "Q37": {"institution": "I06"},
 "Q38": {"institutions": ["I04","I03","I02","I01"]},
 "Q39": {"count": null},
 "Q40": {"source": "S01"},
 "Q41": {"higher": "no"},
 "Q42": {"count": 0},
 "Q43": {"research": "no"},
 "Q44": {"institutions": ["I02","I03","I04","I05","I19","I20"]},
 "Q45": {"count": 16},
 "Q46": {"parent": "I06"}}
```