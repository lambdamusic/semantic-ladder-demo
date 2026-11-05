How the experiment is run, and the conditions it compares. The [domains](/domains/credit/) describe the data and the questions, the [scores](/scores/) give the numbers, and the [conclusions](/conclusions/) say what they mean for each goal.

## The runs

A run asks one model every question of one dataset under several conditions, each a few times over.

- **The models:** Claude Haiku and Sonnet, through the `claude` command line in print mode, from an empty directory with no tools, so they see only the prompt.
- **Repeats:** each condition is asked five times, unless a run says otherwise; the querying runs so far used three.
- **The prompt:** the data in the condition's form, then the questions, each to be answered in a sentence or two that cites the records used, and a closing JSON block that gives each answer in set fields. A run keeps its own prompts, so each one can be read on the run's page.

## Grading

- **By code, against keys computed from the data.** Each dataset's build script computes the key to every question from the data and its rules, and in the base datasets each key is also checked against one written by hand.
- **Correct, partial or wrong.** An answer's JSON fields are compared with the key after normalising (ratings, yes and no, entity identifiers, counts). All fields right is correct, some right is partial, none is wrong. List answers are also scored by F1, reported beside the strict grade.
- **Accuracy** is the mean over questions, with correct = 1 and partial = ½, of each question's mean over the repeats.
- **Intervals** are 95% bootstrap intervals over questions. Differences between two conditions are paired, question by question, so they compare like with like.

## The domains

- **[Credit ratings](/domains/credit/):** issuers, instruments and rating actions, with the traps of time, identity, ceilings and groups. It has three datasets: the [base data](/domains/credit/#the-base-data), the same domain at [300 issuers](/domains/credit/#at-300-issuers), and a dataset with [deep ownership chains](/domains/credit/#ownership-paths) to test whether a graph store helps with paths.
- **[Research analytics](/domains/research/):** works, authors, institutions and citations, shaped like OpenAlex, with the traps of who is who, institution hierarchies, counting methods and versions.

All the data is invented.

## The ladder

Each run asks the same questions under different conditions: what the model is given, and how it gets at the data. The conditions fall into two groups:

- **Reading** (R1 to R10): the model sees the rows, in the prompt, with or without their meaning in some form, and works out each answer itself.
- **Querying** (D1 to D6): the model never sees the rows. It writes SQL or SPARQL, the runner executes each query and sends back the results, and the model answers from those.

Within each group, the conditions differ in how much of the data's meaning the model is given, and in what form. Each has a label, so that the pages can refer to it briefly.

### Reading conditions

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

### Querying conditions

The data sits in DuckDB, queried with SQL, or in an rdflib graph store, queried with SPARQL. The model gets up to eight rounds of queries before it must answer.

| Condition | What the model gets | What it tests |
|---|---|---|
| `sql` | the raw CSV files as DuckDB tables, described by their names, columns and row counts; it queries them with SQL | the querying baseline: whether a model that writes queries does better than one that reads |
| `sql+markdown` | the same, plus the definitions in Markdown, as `csv+markdown` gets them | whether the definitions help as much when the model writes queries as when it reads |
| `sql+executed` | the tables of `executed` in DuckDB, after the rules have run: test records dropped, records merged, rating periods and ownership chains computed | whether rules applied upstream make SQL reliable, with no definitions |
| `sparql` | the raw RDF data in a graph store, described by its prefixes, classes and properties; it queries it with SPARQL | whether a graph store helps on its own, against `sql` |
| `sparql+ontology` | the same, plus the definitions in Markdown, as `sql+markdown` gets them; the ontology's triples are also loaded into the store, where queries can use them | a graph with its ontology, against `sql+markdown`: whether the store needs to be a graph |
| `sparql+axioms` | the graph after the SHACL rules have run, holding what they derive (one entity per LEI, ancestors, the ultimate parent), with no definitions (credit only) | rules run in the graph, against `sql+executed` |

Read across, D1 against D4, D2 against D5 and D3 against D6 compare SQL with SPARQL given the same meaning.
