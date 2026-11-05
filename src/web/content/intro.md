If the facts stay the same, **how much better does an LLM answer when it's told what they mean?** And does it matter how the meaning is written down: as prose, as RDF, as logical axioms, or as rules already run over the data?

The experiment asks the same questions over the same invented data, given in different forms, and grades the answers by code against keys computed from the data. Every question hides a meaning that the rows don't state: an implicit meaning that any analyst would know, or a local rule that only this dataset sets for itself.

## Goals

The experiment sets out to answer five questions:

1. **Does written-down meaning help?** Compare answers given with the data's definitions against answers given without them, while ruling out that a longer prompt alone explains the difference.
2. **Does the form of the meaning matter?** The same definitions as Markdown prose, as RDF, as logical axioms, or as rules already run over the data.
3. **Should the model read the data or query it?** Have it write SQL or SPARQL instead of reading the rows, and see whether the store needs to be a graph, or whether any database will do.
4. **Does it hold across models?** Claude Haiku and Sonnet so far; Opus and Gemini later.
5. **Does the domain matter?** Run the same ladder over domains with different data and different rules, credit ratings and research analytics so far, and see whether the findings change with the domain.

Behind all five is a practical aim: to find out what an ontology is worth to an LLM, separating the meaning it writes down and the rules it runs from its file format.

The [results summary](/summary/) takes each goal in turn and says how far the runs have answered it.

## The ladder

| Condition | What the model gets | What it tests |
|---|---|---|
| `csv` | the data as CSV files | the baseline |
| `rdf` | the same facts as RDF, no ontology | what the format adds alone |
| `csv+padding` | the CSV plus a decoy: a glossary on the same subject (bond markets; scholarly publishing), as long as the definitions in Markdown, that defines none of the terms the questions depend on | whether the gain comes from any expert text on the subject, a longer prompt full of domain words, or only from the definitions of this data |
| `csv+markdown` | the CSV plus the ontology's definitions as Markdown | whether an ontology is just good documentation |
| `csv+ontology` | the CSV plus `ontology.ttl`: the same definitions in RDF (SKOS, in Turtle) | whether writing the definitions in RDF adds anything to the same definitions as Markdown |
| `rdf+ontology` | the RDF data plus `ontology.ttl` | the full knowledge-graph form: whether data and definitions in one format do better than the CSV with the definitions |
| `csv+neutral` | as `csv+ontology`, with one slanted sentence made neutral (credit only) | whether the wording of a single definition can change an answer |
| `csv+axioms` | the data plus OWL axioms and SHACL rules, with the prose taken out (credit only, so far) | whether the model can use logic it has to read |
| `csv+axioms+markdown` | the axioms and the Markdown definitions together | whether logic and prose add up |
| `executed` | the data after the definitions' rules have been applied in code, with no definitions: test records dropped, duplicate records merged into one entity, each rating with the period it held, ownership chains spelt out | whether applying the meaning upstream, as a curated knowledge graph would, can replace telling the model what the data means |

A second ladder asks the same questions without showing the rows. The model writes SQL (DuckDB) or SPARQL (rdflib), the runner executes each query and sends back the results, and the model answers from those. It's given the schema only, the schema plus the definitions, or a store where the rules have already run (`sql+executed`, `sparql+axioms`).

## The domains

- **[Credit ratings](/domains/credit/):** issuers, instruments and rating actions, with the traps of time, identity, ceilings and groups. There are three versions: the [base data](/domains/credit/), the same domain at [300 issuers](/domains/credit_300/), and a version with [deep ownership chains](/domains/credit_paths/) to test whether a graph store helps with paths.
- **[Research analytics](/domains/research/):** works, authors, institutions and citations, shaped like OpenAlex, with the traps of who is who, institution hierarchies, counting methods and versions.

## Method

The models run through the `claude` command line from an empty directory, with no tools, so they see only the prompt. Each condition is asked five times. A question's score is its mean over the repeats, a condition's accuracy is the mean over questions, and intervals come from a bootstrap over questions. Differences between conditions are paired, question by question. The [results log](/log/) records every run's findings in order.

The idea follows Andrea Splendiani's ["Ontologies for AI in practice / part I"](https://www.linkedin.com/pulse/ontologies-ai-practice-part-i-andrea-splendiani-fpihe/) (October 2026), which ran a family-tree question up a similar ladder.
