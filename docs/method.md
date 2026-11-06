How the experiment is run, and the conditions it compares (the "ladder").

## The runs

A run asks one model every question of one dataset under several conditions, each a few times over. [`src/run.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/src/run.py) runs the reading conditions and [`src/query.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/src/query.py) the querying ones; [`BUILDING.md`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/BUILDING.md) says how to run them.

- **The models:** Claude Haiku and Sonnet, through the `claude` command line in print mode, from an empty directory with no tools, so they see only the prompt ([`src/providers.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/src/providers.py)).
- **Repeats:** each condition is asked five times.
- **The prompt:** the data in the condition's form, then the questions, each to be answered in a sentence or two that cites the records used, and a closing JSON block that gives each answer in set fields. A run keeps its own prompts, so each one can be read on the run's page.
- **What a run keeps:** each run is a folder under [`results/`](https://github.com/lambdamusic/semantic-ladder-demo/tree/main/results). [This one](https://github.com/lambdamusic/semantic-ladder-demo/tree/main/results/credit/2026-11-05-1227-sonnet), for instance, holds the run's settings and commit ([`meta.json`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/results/credit/2026-11-05-1227-sonnet/meta.json)), the questions with their keys as asked ([`questions.json`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/results/credit/2026-11-05-1227-sonnet/questions.json)), every prompt ([`prompts/`](https://github.com/lambdamusic/semantic-ladder-demo/tree/main/results/credit/2026-11-05-1227-sonnet/prompts)), every answer (such as [`answers-csv-run1.md`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/results/credit/2026-11-05-1227-sonnet/answers-csv-run1.md)), the grades ([`grades.json`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/results/credit/2026-11-05-1227-sonnet/grades.json)) and the report ([`report.md`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/results/credit/2026-11-05-1227-sonnet/report.md)). A querying run also keeps each session's queries and results, as in [this transcript](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/results/credit/2026-11-06-0935-sonnet-query/transcript-sql+markdown-run1.json).

## Grading

The grading is in [`src/grade.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/src/grade.py), and the reports are written by [`src/report.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/src/report.py).

- **By code, against keys computed from the data.** Each dataset's build script computes the key to every question from the data and its rules ([`build_questions.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/domains/credit/build_questions.py) for credit), and in the base datasets each key is also checked against one written by hand.
- **A checklist, for the questions that ask why.** One credit question ([Q6](/domains/credit/questions/#Q6)) and two research questions ([Q47](/domains/research/questions/#Q47), [Q48](/domains/research/questions/#Q48)) ask for a reason, which code can't grade. Claude Sonnet grades them against a checklist of points, twice, so that its agreement with itself can be measured.
- **Correct, partial or wrong.** An answer's JSON fields are compared with the key after normalising (ratings, yes and no, entity identifiers, counts). All fields right is correct, some right is partial, none is wrong. List answers are also scored by F1, reported beside the strict grade.
- **Accuracy** is the mean over questions, with correct = 1 and partial = ½, of each question's mean over the repeats.
- **Intervals** are 95% bootstrap intervals over questions. Differences between two conditions are paired, question by question, so they compare like with like.

## The domains

- **[Credit ratings](/domains/credit/):** issuers, instruments and rating actions, with the traps of time, identity, ceilings and groups. It has three datasets: the [base data](/domains/credit/#the-base-data), the same domain at [300 issuers](/domains/credit/#at-300-issuers), and a dataset with [deep ownership chains](/domains/credit/#ownership-paths) to test whether a graph store helps with paths.
- **[Research analytics](/domains/research/):** works, authors, institutions and citations, shaped like OpenAlex, with the traps of who is who, institution hierarchies, counting methods and versions. It has two datasets: the [base data](/domains/research/#the-base-data) and the same domain at [850 works](/domains/research/#at-850-works).

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
| `csv+axioms` | the data plus OWL axioms and SHACL rules, with the prose taken out | whether the model can use logic it has to read |
| `csv+axioms+markdown` | the axioms and the Markdown definitions together | whether logic and prose add up |
| `executed` | the data after the definitions' rules have been applied in code, with no definitions: test records dropped, duplicate records merged into one entity, each rating with the period it held, ownership chains spelt out | whether applying the meaning upstream, as a curated knowledge graph would, can replace telling the model what the data means |

### Querying conditions

The data sits either in [DuckDB](https://duckdb.org/), an in-process SQL database, queried with SQL, or in an in-memory graph store built with [rdflib](https://rdflib.readthedocs.io/), the Python library for RDF, queried with SPARQL. The model gets up to eight rounds of queries before it must answer, and a query that runs for more than 60 seconds is stopped and reported to it as failed.

The SPARQL conditions can also run on [GraphDB](https://graphdb.ontotext.com/) (the free edition), a graph database built for speed. Such a run loads exactly the same triples, in a repository with no inference, so that only the engine changes; its column in the scores says GraphDB. Reproducing those runs needs a local GraphDB.

| Condition | What the model gets | What it tests |
|---|---|---|
| `sql` | the raw CSV files as DuckDB tables, described by their names, columns and row counts; it queries them with SQL | the querying baseline: whether a model that writes queries does better than one that reads |
| `sql+markdown` | the same, plus the definitions in Markdown, as `csv+markdown` gets them | whether the definitions help as much when the model writes queries as when it reads |
| `sql+executed` | the tables of `executed` in DuckDB, after the rules have run: test records dropped, records merged, rating periods and ownership chains computed | whether rules applied upstream make SQL reliable, with no definitions |
| `sparql` | the raw RDF data in a graph store, described by its prefixes, classes and properties; it queries it with SPARQL | whether a graph store helps on its own, against `sql` |
| `sparql+ontology` | the same, plus the definitions in Markdown, as `sql+markdown` gets them; the ontology's triples are also loaded into the store, where queries can use them | a graph with its ontology, against `sql+markdown`: whether the store needs to be a graph |
| `sparql+axioms` | the graph after the SHACL rules have run, holding what they derive (on credit, one entity per LEI, ancestors and the ultimate parent; on research, one person per ORCID, credited institutions and the citations that count), with no definitions | rules run in the graph, against `sql+executed` |

Read across, D1 against D4, D2 against D5 and D3 against D6 compare SQL with SPARQL given the same meaning.

## What the runs cost, and how long they took

Every model call went through the `claude` command line in print mode, on a Claude subscription, so the runs cost nothing beyond the subscription. They did count against its usage limits, which stopped one run for about an hour.

At the API's list prices, the same calls would cost roughly **$45**, almost all of it Sonnet:

| | Sessions | Input | Output | At list prices |
|---|---|---|---|---|
| Claude Sonnet 5.5 ($2 / $10 per million tokens) | 593 | about 15.8M tokens | about 1.3M tokens | about $44 |
| Claude Haiku 5.5 ($0.10 / $0.50) | 290 | about 4.4M tokens | about 0.5M tokens | about $1 |

These are estimates from the saved prompts, answers and query transcripts, at about four characters a token, with each round of a querying session counted with the conversation before it. They leave out the thinking the models do before answering, which is billed as output but not saved, the grader's calls on the few questions it grades, and any saving from prompt caching. So read them as an order of magnitude.

The 36 runs on these pages ran between 4 and 6 November 2026: 883 sessions in all. Added up, the runs took about 41 hours. Since two or three ran at once, something was running for about 24 hours of those three days. A reading run on the base data takes 10 to 40 minutes, a querying run with six conditions about an hour, and the runs on the larger datasets two to four hours each.

Every dataset, question, key and executed table can be rebuilt from the scripts, and every grade and report from the saved answers, in about a minute and with no model calls. [`BUILDING.md`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/BUILDING.md) says how, and how to run the experiment yourself.
