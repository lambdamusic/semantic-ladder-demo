# Semantics ladder

How much does an LLM gain from being told what data *means*? This experiment asks a model the
same questions over the same invented data, given in different ways: the data alone, the data as
RDF, with an ontology that defines every term and code, with the ontology as logical axioms, or
after its rules have run. The model either reads the rows or writes SQL and SPARQL over them, and
every answer is graded by code.

**The results, the method and every run are on the website: https://semantic-ladder.michelepasin.org**

## Goals

1. **Does written-down meaning help?** Answers with the data's definitions, against answers without them.
2. **Does the form of the meaning matter?** Markdown prose, RDF, logical axioms, or rules already run over the data.
3. **Should the model read the data or query it?** And does the store need to be a graph?
4. **Does it hold across models?** Claude Haiku and Sonnet so far.
5. **Does the domain matter?** Credit ratings and research analytics so far.

The idea follows Andrea Splendiani's
["Ontologies for AI in practice / part I"](https://www.linkedin.com/pulse/ontologies-ai-practice-part-i-andrea-splendiani-fpihe/)
(October 2026), which ran a family-tree question up a similar ladder.

## How it works

- **Each domain is a folder** in `domains/`, with its data, its ontology, its questions and how to
  build each condition's prompt.
- **Every question hides a meaning the rows don't state:** an implicit meaning any analyst would
  know, or a local rule that only this dataset sets for itself.
- **Answers are graded by code,** against keys computed from the data. Only the few "why"
  questions go to an LLM grader, with a checklist.
- **Every run is kept** in `results/`, with its prompts, answers, grades and report.

The [Method page](https://semantic-ladder.michelepasin.org/method/) describes the conditions, the
grading and the setup in full.

**All the data is invented:** the companies, LEIs and ratings, the works, people and institutions.
Nothing here is any rating agency's or bibliographic database's data or definitions.

## Layout

| | |
|---|---|
| `domains/` | one folder per dataset: `data/`, `ontology/`, `questions.json` and the scripts that build them |
| `src/` | the runners (`run.py` for reading, `query.py` for querying), grading, reports, and the web app in `src/web/` |
| `results/` | every run, one folder each |
| `docs/` | the website's text, in Markdown |
| `site/` | the website as static pages, published on GitHub Pages |
| `tools/` | `rebuild` (rebuild and check every table), `run-web` and `site-dump` (the website) |

## Running it

Needs Python 3.13 with the packages in `requirements.txt` and, for Claude, the `claude` command
line. From the repo root:

```bash
python src/run.py --domain research        # reading: a dataset, every condition, 5 repeats
python src/query.py --domain credit_300    # querying: the model writes SQL or SPARQL
tools/rebuild --check                      # rebuild every table and check it against the repo
tools/run-web                              # the website, locally, at http://127.0.0.1:8030
```

[`BUILDING.md`](BUILDING.md) has the rest: every option, how each dataset is built, and how to
check the numbers.

## Licence

MIT: see [`LICENSE`](LICENSE). Made by Michele Pasin.
