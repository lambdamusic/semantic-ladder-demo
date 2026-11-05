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

## How the pages are arranged

- **[Method](/method/):** how the runs are made and graded, and the ladder of conditions they compare.
- **The domains:** [credit ratings](/domains/credit/) and [research analytics](/domains/research/), each with its data, questions and ontology.
- **[Scores](/scores/):** each dataset's latest runs side by side, with notes on what each run shows.
- **[Conclusions](/conclusions/):** each goal in turn, and how far the runs have answered it.
- **[Run archive](/runs/):** every run, older ones included, with its prompts, answers and grades.

## The code and data

Everything is in the [GitHub repository](https://github.com/lambdamusic/semantic-ladder-demo): the data and how it's built, the ontologies and axioms, the questions and their keys, the code that runs and grades the ladder, and every run's prompts, answers and grades. Its README says how to run it.
