I could only answer part of this. After the first few queries the store started returning repeated, contradictory rows (W23, W70 and W71 came back empty or duplicated). So I answered only what the clean early results support and left the rest as `null` rather than guess. That includes Q47 and Q48, which have no JSON field.

**Q1.** 1. A01, A02 and A03 all share ORCID 0000-0002-9841-6229, so they are one person.
**Q2.** Not fully answered. A01 appears on W01–W08 and on many later works (W12–W35), but the output was truncated, so I can't give the complete list.
**Q3.** No. A05 and A06 are both named Jonas Brandt but have different ORCIDs (0000-0001-6105-5008 and 0000-0007-5475-1779). I did not see the W37/W38 authorships, so I am assuming they map to A05 and A06 respectively.
**Q5.** Depends. A02 ("M. Ellison") shares Mara's ORCID, but A04 ("M. Ellison") has a different ORCID, and W08 lists both A02 and A04.
**Q8.** I01. The chain is I04 → I03 → I02 → I01, and I01 has no parent.
**Q20.** Only W02 is confirmed, as a preprint of W03. The check for others returned corrupted rows.
**Q26.** No. W23 was shown as retracted (true) in the first clean result, so it is not research output.
**Q40.** S01, which is tier K3.
**Q41.** No. S03 is K1 and S02 is K2, so S03 ranks lower.
**Q43.** No. W07 is in S04, a K0 (delisted) source.
**Q44.** I02, I03, I04 and I05. I06 is excluded because it is an affiliated institute (AFF).
**Q46.** I06. As an affiliated institute (AFF), its parent link is not followed, so it is its own ultimate parent.

```json
{
"Q1": {"count": 1},
"Q2": {"works": null},
"Q3": {"same": "no"},
"Q4": {"count": null},
"Q5": {"same": "depends"},
"Q6": {"author": null},
"Q7": {"count": null},
"Q8": {"parent": "I01"},
"Q9": {"count": null},
"Q10": {"count": null},
"Q11": {"count": null},
"Q12": {"full": null, "fractional": null},
"Q13": {"full": null, "fractional": null},
"Q14": {"full": null, "fractional": null},
"Q15": {"count": null},
"Q16": {"count": null},
"Q17": {"works": null},
"Q18": {"count": null},
"Q19": {"count": null},
"Q20": {"works": ["W02"]},
"Q21": {"count": null},
"Q22": {"more_in_total": null, "more_in_window": null},
"Q23": {"total": null, "in_window": null},
"Q24": {"count": null},
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
"Q37": {"institution": null},
"Q38": {"institutions": null},
"Q39": {"count": null},
"Q40": {"source": "S01"},
"Q41": {"higher": "no"},
"Q42": {"count": null},
"Q43": {"research": "no"},
"Q44": {"institutions": ["I02", "I03", "I04", "I05"]},
"Q45": {"count": null},
"Q46": {"parent": "I06"}
}
```