The second domain, to test whether the finding is about ontologies or about credit. It's research analytics shaped like OpenAlex: works, authors, institutions, sources, authorships and citations. **Everything is invented**: the works, people, institutions, journals, ORCIDs, RORs, ISSNs and DOIs. Nothing comes from OpenAlex, so no answer can come from a model's memory.

The 48 questions cover the traps of research analytics:

- **who is who:** one author under three records, two different people with the same name;
- **institution hierarchy:** a lab under a centre under a university under a system;
- **counting:** full against fractional counting, which can flip a ranking;
- **document types:** editorials, errata and paratext;
- **versions:** a preprint and its published version;
- **citations:** time windows, retractions, citations rolled up to institutions, self-citation at several levels, and two hops.

Five local rules are stated only in the ontology:

- `STG` records are test data.
- `SUP` means a supplement article, not supplementary material.
- Only the affiliation listed last counts.
- Journal tiers count upwards, and `K0` is a delisting.
- An affiliated institute (`AFF`) is not a unit of its parent.

**In this section:** the [data](/domains/research/data/), the [questions and their traps](/domains/research/questions/), the [ontology](/domains/research/ontology/), and the [results](/domains/research/results/).
