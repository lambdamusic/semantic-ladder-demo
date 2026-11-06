# Research domain: design notes

The choices made in building the research-analytics domain, and the ones that could have gone
another way. The data, its traps and its local rules are described on the
[Data page](https://semantic-ladder.michelepasin.org/domains/research/data/), and how to build it in
[`BUILDING.md`](../../BUILDING.md).

**Everything is invented:** the works, people, institutions, journals, ORCIDs, RORs, ISSNs and
DOIs. Nothing was downloaded from OpenAlex. The ORCIDs aren't checksummed, and the DOIs use
the prefix 10.55555 (not checked to be unassigned).

## Choices that could have gone another way

- **"Research work" is the dataset's own term.** Most count questions ask for research works.
  Without the ontology, the model has to decide for itself what counts: that's the
  document-type trap. But it also means some `csv` answers that count editorials could be
  called a reasonable reading rather than an error. Credit's "issuer rating" was the same.
- **Author self-citation is defined broadly:** the citing and cited works share any author.
  So Q29's author count is 2 (Mara Ellison, and her co-author Priya Ramanathan, on W13). A
  model that counts only Mara's own citations says 1, which is a defensible reading without
  the ontology. Q29's institution count is also 2, by coincidence.
- **Citation windows** have only two questions, and each question states the window ("its
  publication year and the two years after"), so the trap is only raw counts against windowed
  ones. No question sets a house window length. That could be a sixth local rule.
- **Citations from any type of work count** (an editorial citing a paper is a citation), apart
  from test records and retracted works. No question depends on this choice.
- **Versions:** a merged pair takes the published version's year, source and byline. The
  build checks that each preprint's credited authors match its published version's.
  `canonical()` merges author records by ORCID only. It doesn't merge a preprint with its
  published version, because Q20 asks which records are preprints, and merging would accept
  the wrong record of the pair.
- **Field-normalised citations,** the "normalisation" trap planned for this domain, aren't covered: the data has
  no fields, and the trap needs a decimal answer.
- **The names are invented, but could collide with real ones.** Some person names (Pieter Maas,
  Jonas Brandt) are common enough to belong to real people, and some place-based names
  (Albury, Dunmore) use real towns. They were reviewed before publishing and judged fine.
- **Size:** the RDF is about 75 KB, against 19 KB for credit, because authorships and
  citations are one resource per row. So `rdf` and `rdf+ontology` are the largest prompts
  (82 KB and 100 KB, about 20,000 to 25,000 tokens). To shrink them, citations could become
  a direct `res:cites` triple, but the conversion would then no longer be strictly
  one-resource-per-row.
