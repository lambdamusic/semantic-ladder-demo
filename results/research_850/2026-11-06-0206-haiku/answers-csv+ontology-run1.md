**Q1.** 3 people. Records A01, A02, A03 and A101 share ORCID 0000-0002-9841-6229, A04 has 0000-0004-8662-8360, and A102 has 0000-0008-4738-8328.

**Q2.** 32 works (all of them, of any type). Person-level: the ORCID 0000-0002-9841-6229 records A01, A02, A03 and A101 are one person, so their works are combined.

**Q3.** No. W37 is by A05 (ORCID 0000-0001-6105-5008) and W38 by A06 (ORCID 0000-0007-5475-1779), which are different people.

**Q4.** 8. A05 and A104 (ORCID 0000-0001-6105-5008) have research works W14, W37, W554, W565, W785, W792, W702 and W1038. The preprint W556 is a version of W1038, so it counts once.

**Q5.** No. W08 is by A04 (ORCID 0000-0004-8662-8360) and W01 by A01 (ORCID 0000-0002-9841-6229).

**Q6.** A01 (Mara Ellison, person-level). Her University of Albury (I02, with units I03, I04, I19) research works total 22, more than any other author's (next highest is about 15, for A07 Priya Ramanathan, who is credited at I03).

**Q7.** 22. The research works are W01, W03 (with its preprint W02), W06, W07, W12, W19, W206, W238, W449, W464 (with W663), W555, W763, W817, W843, W869 (with W612), W905, W972, W984, W1005, W1048 and W1050. W374 is retracted, and W04, W05, W271, W813, W936 and W949 are not research types.

**Q8.** I01. I04 sits under I03, which sits under I02, which sits under I01, the top of the chain.

**Q9–Q48: not yet answered.** Q9 onward requires building the full credited-work sets for the institution subtrees and citation sets, which I haven't finished. I'll continue with those in the next pass.

```json
{
  "Q1": {"count": 3},
  "Q2": {"works": ["W01","W04","W05","W06","W12","W238","W271","W374","W464","W676","W813","W949","W1005","W02","W07","W19","W449","W663","W869","W972","W1048","W1050","W03","W206","W763","W817","W555","W612","W843","W905","W936","W984"]},
  "Q3": {"same": "no"},
  "Q4": {"count": 8},
  "Q5": {"same": "no"},
  "Q6": {"author": "A01"},
  "Q7": {"count": 22},
  "Q8": {"parent": "I01"}
}
```