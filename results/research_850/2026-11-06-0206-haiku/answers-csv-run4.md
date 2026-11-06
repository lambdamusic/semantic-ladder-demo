**Q1.** Three distinct people. A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229, while A04 (0000-0004-8662-8360) and A102 (0000-0008-4738-8328) each have their own ORCID.

**Q2.** Thirteen works, of any type: W01, W04, W05, W06, W12, W238, W271, W374, W464, W676, W813, W949 and W1005, all from authorships rows where A01 is listed.

**Q3.** No. The Jonas Brandt on W37 is A05 (ORCID 0000-0001-6105-5008) and the one on W38 is A06 (ORCID 0000-0007-5475-1779), so they are different people.

**Q4.** Seven. A05 is credited on W14, W37, W554, W565, W785, W792 and W1038, all of type ART.

**Q5.** No. The M. Ellison on W08 is A04 (ORCID 0000-0004-8662-8360), and the Mara Ellison on W01 is A01 (ORCID 0000-0002-9841-6229).

**Q8.** I01. I04 sits under I03, which sits under I02, which sits under I01.

**Q15.** 27. Ocean Sensing Letters (S02) has 27 works dated 2024 with research types (ART or REV), counting retracted W520 and W922 and excluding ERR/PTX (W05, W10, W949). This assumes research output means ART, REV and PPR. I may have missed a record in a scan of this size.

**Q17.** W04 (EDT), W05 (ERR), W271 (EDT), W813 (ERR) and W949 (ERR) are not research output because of their document type.

**Q37.** I04. W70 has two affiliation rows for A08, I04 (seq 1) and I06 (seq 2), so I06 is also credited.

**Q38.** I04 and I06 directly, then I03, I02 and I01 as their parents.

**Q40.** S01. It is the only source in tier K3, assuming K3 is the highest tier.

**Q41.** No. S03 is K1 and S02 is K2, assuming higher K-number means higher tier.

**Q43.** Yes. W07 is an ART record.

**Q44.** I02, I03, I04, I05, I06, I19, I20 and I21. These are all the descendants of I01 in parent_id.

**Q45.** 22. Research works with an I06 affiliation are W70, W71, W73, W74, W252, W378, W426, W502, W613, W617, W632, W635, W656, W664, W671, W672, W761, W822, W926, W940, W1007 and W1062.

**Q46.** I01. I06 sits under I02, which sits under I01.

**Remaining questions.** Q6, Q7, Q9–Q14, Q16, Q18–Q36, Q39, Q42 and Q47–Q48 are not yet answered. They need full per-author and per-institution tallies, citation-graph traversal and fractional-count arithmetic. I will take them in smaller batches next.

```json
{
  "Q1": {"count": 3},
  "Q2": {"works": ["W01", "W04", "W05", "W06", "W12", "W238", "W271", "W374", "W464", "W676", "W813", "W949", "W1005"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 7},
  "Q5": {"same": "no"},
  "Q8": {"parent": "I01"},
  "Q15": {"count": 27},
  "Q17": {"works": ["W04", "W05", "W271", "W813", "W949"]},
  "Q37": {"institution": "I04"},
  "Q38": {"institutions": ["I04", "I06", "I03", "I02", "I01"]},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q43": {"research": "yes"},
  "Q44": {"institutions": ["I02", "I03", "I04", "I05", "I06", "I19", "I20", "I21"]},
  "Q45": {"count": 22},
  "Q46": {"parent": "I01"}
}
```