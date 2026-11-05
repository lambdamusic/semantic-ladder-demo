An invented research-analytics world, shaped like OpenAlex: works, the authors who wrote them, their institutions, the journals and repositories they appeared in, and the citations between them, as an analyst's extract from a bibliographic feed and an institution's own system would come. **Everything is invented**: the works, people, institutions, journals, ORCIDs, RORs, ISSNs and DOIs. Nothing comes from OpenAlex, so no answer can come from a model's memory. The codes (`SUP`, `AFF`, `K0`) are left cryptic, and nothing in the files says what they stand for.

The 48 questions are of two kinds:

- **Implicit meanings** (Q1 to Q32): what any research analyst knows without saying. One author can have several records, and two people can share a name. A lab belongs to its centre, its university and its university system. Full and fractional counting can rank institutions differently. An editorial or an erratum isn't a research article. A preprint and its published version are one work. Citations count within a time window, and a retracted work's don't count. Self-citation means something different for an author, an institution and a country.
- **Local meanings** (Q33 to Q48): rules this dataset sets for itself, stated only in the ontology. `STG` records are test data. `SUP` is a supplement article, not supplementary material. When an author lists several affiliations, only the one listed last is credited. The journal tiers count upwards, and `K0` is a delisting. An affiliated institute (`AFF`) is not a unit of its parent. No model can know these without being told.

## The datasets

### The base data

85 works, 38 author records, 18 institutions, 8 sources, 138 authorships and 71 citations. 52 of the works are designed by hand so that each question has its point, and the other 33 are background. Small enough to read in full.

A larger dataset, with the same traps repeated many times over, is planned, so that this domain, like credit, can show whether size changes the picture.
