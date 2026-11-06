**Q1.** 3 people. The name-matched records split by ORCID: 0000-0002-9841-6229 (A01, A02, A03, A101), 0000-0004-8662-8360 (A04) and 0000-0008-4738-8328 (A102).

**Q2.** 32 works, counting every record under the ORCID 0000-0002-9841-6229 (A01, A02, A03, A101) as one person: W01, W02, W03, W04, W05, W06, W07, W12, W19, W206, W238, W271, W374, W449, W464, W555, W612, W663, W676, W763, W813, W817, W843, W869, W905, W936, W949, W972, W984, W1005, W1048, W1050.

**Q3.** No. W37's author A05 has ORCID 0000-0001-6105-5008 and W38's author A06 has 0000-0007-5475-1779, so they are different people.

**Q4.** 8 research works. A05 and A104 share ORCID 0000-0001-6105-5008; their research works are W14, W37, W554, W565, W702, W785, W792 and W1038 (W556 is a preprint of W1038, so it is counted there).

**Q5.** No. M. Ellison (A04, ORCID 0000-0004-8662-8360) and Mara Ellison (A01, ORCID 0000-0002-9841-6229) have different ORCIDs.

**Q7.** 19 research works. Counting the ORCID group, I excluded retracted W374, editorials and errata, K0 sources (W07, W449, W763) and W813/W949. Preprints W02, W612 and W663 are counted under their published versions W03, W869 and W464.

**Q8.** I01. I04 → I03 → I02 → I01, and I01 has no parent.

**Q15.** 25 research works in Ocean Sensing Letters (S02) in 2024. I excluded retracted W520 and W922, and the 2024 erratum W949. This was a manual scan, so treat it as likely but not certain.

**Q36.** 34 research works in the Proceedings of the Hydrodynamics Forum (S06): 22 articles, 10 supplement articles and 2 reviews, after excluding editorials, front matter and the erratum. This was also a manual scan.

**Q37.** I06. W70's last-listed affiliation (sequence 2) is I06, the affiliated institute (AFF).

**Q38.** I04, I03, I02, I01. W71's last-listed affiliation is I04, and I04 sits under I03, I02 and I01.

**Q40.** S01 (Journal of Marine Autonomy), the only K3 source.

**Q41.** No. Coastal Engineering Review (S03) is K1, which is lower than Ocean Sensing Letters (S02), which is K2.

**Q42.** 0. Global Marine Science Reports (S04) is K0 (delisted), so none of its works are research output.

**Q43.** No. W07 appeared in S04, a delisted K0 source.

**Q46.** I06. It is an AFF institute, so its ultimate parent is itself.

**Q48.** W70's last-listed affiliation is the Halloran Institute (I06), an affiliated institute. AFF institutes are never credited to their nominal parent or anything above it, so W70 is not credited to the University of Albury (I02). The Tessel Laboratory (I04) is only the earlier affiliation, which the house rule ignores.

**Remaining questions:** Q6, Q9–Q14, Q16–Q35, Q39, Q44, Q45 and Q47 still need working through. Q16 (S01 totals) and the institution-subtree counts (Q6, Q9–Q14) need a systematic pass over the authorships, so I'll take them next, starting with Q9.

```json
{
  "Q1": {"count": 3},
  "Q2": {"works": ["W01","W02","W03","W04","W05","W06","W07","W12","W19","W206","W238","W271","W374","W449","W464","W555","W612","W663","W676","W763","W813","W817","W843","W869","W905","W936","W949","W972","W984","W1005","W1048","W1050"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 8},
  "Q5": {"same": "no"},
  "Q7": {"count": 19},
  "Q8": {"parent": "I01"},
  "Q15": {"count": 25},
  "Q36": {"count": 34},
  "Q37": {"institution": "I06"},
  "Q38": {"institutions": ["I04","I03","I02","I01"]},
  "Q40": {"source": "S01"},
  "Q41": {"higher": "no"},
  "Q42": {"count": 0},
  "Q43": {"research": "no"},
  "Q46": {"parent": "I06"}
}
```