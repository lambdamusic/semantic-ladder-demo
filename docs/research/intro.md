An invented research-analytics world, shaped like OpenAlex: works, the authors who wrote them, their institutions, the journals and repositories they appeared in, and the citations between them, as an analyst's extract from a bibliographic feed and an institution's own system would come. **Everything is invented**: the works, people, institutions, journals, ORCIDs, RORs, ISSNs and DOIs. Nothing comes from OpenAlex, so no answer can come from a model's memory. The codes (`SUP`, `AFF`, `K0`) are left cryptic, and nothing in the files says what they stand for.

The 48 questions are of two kinds:

- **Implicit meanings** (Q1 to Q32, and Q47): what any research analyst knows without saying. One author can have several records, and two people can share a name. A lab belongs to its centre, its university and its university system. Full and fractional counting can rank institutions differently. An editorial or an erratum isn't a research article. A preprint and its published version are one work. Citations count within a time window, and a retracted work's don't count. Self-citation means something different for an author, an institution and a country.
- **Local meanings** (Q33 to Q46, and Q48): rules this dataset sets for itself, stated only in the ontology. `STG` records are test data. `SUP` is a supplement article, not supplementary material. When an author lists several affiliations, only the one listed last is credited. The journal tiers count upwards, and `K0` is a delisting. An affiliated institute (`AFF`) is not a unit of its parent. No model can know these without being told.

One ontology and one question bank are asked of both datasets. Each computes its own answer keys from its own data.

## The datasets

### The base data

85 works, 38 author records, 18 institutions, 8 sources, 138 authorships and 71 citations. 52 of the works are designed by hand so that each question has its point, and the other 33 are background. Small enough to read in full.

### At 850 works

The base works plus 765 invented ones, 515 of which repeat the same traps many times over: more author records for the same people, more labs and affiliated institutes, more works with several affiliations, preprints, test records, retractions and delisted sources, and about 1,000 citations. That makes 850 works, 167 author records, 31 institutions, 14 sources, 1,532 authorships and 1,067 citations. The same 48 questions now need counting and joining across many records. `scale.py` builds it from a fixed seed.
