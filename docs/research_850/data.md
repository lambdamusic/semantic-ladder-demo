The base data plus 765 invented works, from a fixed seed, so that the same 48 questions need counting and joining across many records. `domains/research/scale.py` builds it, and the keys are computed from the data, as for the base.

The base records stay as they are, so every question keeps its point. 515 of the added works repeat the traps, many of them on the designed people, institutions and sources, and the other 250 are background:

- **Who is who:** Mara Ellison gets a fourth record, and a third, different "M. Ellison" works at Rostval. Author records that share an ORCID go from 3 to 12, and names on more than one record from 2 to 9.
- **Hierarchy:** new labs under the University of Albury, Albury Metropolitan and Rostval, and two new affiliated institutes (`AFF`), under Albury Metropolitan and Kesting.
- **Affiliations:** authorships with several affiliations go from 2 to 26, in both orders, so the rule about the last one decides many credits.
- **Versions:** preprints with a published version go from 2 to 23, some under another record of the same person.
- **Test records, retractions and delistings:** `STG` works go from 3 to 25, retracted works from 1 to 13, and works in a `K0` source from 2 to 24.
- **Document types:** more supplements (`SUP`), editorials, errata and front matter.
- **Citations:** about 1,000, with new citing works at every level of self-citation, and blocks that keep each comparison's answer: Kesting and Rostval still swap places between full and fractional counting, and W30 still leads in total while W31 leads within its window.

Of the 46 keys graded by code, 31 change from the base data's. The 15 that don't are comparisons whose answers hold by design, or questions about one record.

The `rdf` and `rdf+ontology` prompts are about 770 KB, against 136 KB for `csv`, which is too large for the model's context, so the runs on this dataset leave them out.
